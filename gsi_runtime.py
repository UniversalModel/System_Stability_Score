#!/usr/bin/env python3
"""
gsi_runtime.py
==============
GSI-RTD v0.1 — Full AD-RTD Runtime (APPENDIX G, §33)

Implements the remaining §33 blueprint components on top of gsi_multi_domain.py:

  TriadicBudget  — triadic resource envelope  (T_max, S_max, E_max)
  TriadicAgent   — Form / Position / Action / Generalizer agents with LLM evaluation
  LearningLaw    — §26 impact weight update rule
  gsi_runtime()  — full AD-RTD pipeline (Phase 0–11)

Operational flow (AD-RTD):
  Phase 0:  Scan    → detect problem / instability
  Phase 1:  Action  → enumerate admissible A variants
  Phase 2:  Form    → bind F variants given A
  Phase 3:  Position→ expand P variants given (F, A)
  Phase 4:  Construct m×n×k candidate systems
  Phase 5:  Evaluate U-Score / SI via LLM agents or heuristic
  Phase 6:  Triage  → HIGH / MID / LOW
  Phase 7:  Prioritize ΔSI / Cost
  Phase 8:  Schedule → TriadicScheduler (§20) + budget gate
  Phase 9:  Execute → deploy agents via LGP-12
  Phase 10: Learn   → update impact weights
  Phase 11: Iterate → next generation or halt

Author:  Petar Nikolov — U-Theory v26 / GSI-RTD
Date:    2026-03-27
Requires: gsi_multi_domain.py, sss_llm_adapter.py
"""

import json
import math
import random
import statistics
import time
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# ── Import simulation core ────────────────────────────────────────────────────
from gsi_multi_domain import (
    Domain,
    TriadicSystem,
    TriadicScheduler,
    MultiDomainGSI,
    compute_si,
    THETA_STABLE,
    THETA_CRITICAL,
    EXPLORATION_EPS_INIT,
    EXPLORATION_EPS_FLOOR,
    EXPLORATION_DECAY,
)

# ── Import LLM adapter ────────────────────────────────────────────────────────
from sss_llm_adapter import api_generate, OPENROUTER_API_KEY


# ═══════════════════════════════════════════════════════════════════════════════
# TRIADIC BUDGET  (§22 — resource envelope)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class TriadicBudget:
    """
    Triadic resource envelope: (T_max, S_max, E_max).

    T → Time    budget  (generations, seconds, or logical steps)
    S → Space   budget  (concurrent agents, memory slots, DB rows)
    E → Energy  budget  (API calls, compute cycles, cost units)

    Cost per generation:  ∛(ΔT × ΔS × ΔE)  — geometric, non-compensatory.
    Any dimension hitting its max immediately halts the generation loop.
    """
    T_max: float   # time budget
    S_max: float   # space budget
    E_max: float   # energy budget
    T_used: float = 0.0
    S_used: float = 0.0
    E_used: float = 0.0

    @property
    def exhausted(self) -> bool:
        return self.T_used >= self.T_max or \
               self.S_used >= self.S_max or \
               self.E_used >= self.E_max

    @property
    def remaining_ratio(self) -> float:
        """Worst-case remaining budget fraction (non-compensatory min)."""
        t_r = max(0.0, 1.0 - self.T_used / max(self.T_max, 1e-9))
        s_r = max(0.0, 1.0 - self.S_used / max(self.S_max, 1e-9))
        e_r = max(0.0, 1.0 - self.E_used / max(self.E_max, 1e-9))
        return min(t_r, s_r, e_r)

    def charge(self, delta_T: float = 1.0, delta_S: float = 1.0,
               delta_E: float = 1.0) -> float:
        """
        Consume resources for one generation step.
        Returns the triadic cost ∛(ΔT × ΔS × ΔE).
        """
        self.T_used += delta_T
        self.S_used += delta_S
        self.E_used += delta_E
        return (delta_T * delta_S * delta_E) ** (1 / 3)

    def summary(self) -> str:
        return (f"Budget T={self.T_used:.1f}/{self.T_max:.1f}  "
                f"S={self.S_used:.1f}/{self.S_max:.1f}  "
                f"E={self.E_used:.1f}/{self.E_max:.1f}  "
                f"remaining={self.remaining_ratio:.2f}")

    def to_dict(self) -> dict:
        """Serialize budget state for checkpointing (Patch 3.2)."""
        return {
            "T_max": self.T_max, "S_max": self.S_max, "E_max": self.E_max,
            "T_used": self.T_used, "S_used": self.S_used, "E_used": self.E_used,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "TriadicBudget":
        """Restore budget from checkpoint dict (Patch 3.2)."""
        b = cls(T_max=d["T_max"], S_max=d["S_max"], E_max=d["E_max"])
        b.T_used = d.get("T_used", 0.0)
        b.S_used = d.get("S_used", 0.0)
        b.E_used = d.get("E_used", 0.0)
        return b

    # ── Budget persistence (§3.2) ────────────────────────────────────────────
    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in
                ("T_max", "S_max", "E_max", "T_used", "S_used", "E_used")}

    @classmethod
    def from_dict(cls, d: dict) -> "TriadicBudget":
        return cls(**{k: float(d[k]) for k in
                      ("T_max", "S_max", "E_max", "T_used", "S_used", "E_used")})


# ═══════════════════════════════════════════════════════════════════════════════
# LEARNING LAW  (§26 — impact weight update)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ImpactRecord:
    """One observation: a system's SI improved by delta_SI at a cost."""
    system_repr: str
    SI_before:   float
    SI_after:    float
    cost:        float
    generation:  int

    @property
    def delta_SI(self) -> float:
        return self.SI_after - self.SI_before

    @property
    def roi(self) -> float:
        return self.delta_SI / max(self.cost, 1e-9)


class LearningLaw:
    """
    §26 Learning Law — tracks observed (ΔSI, Cost) pairs and updates
    impact weights for the three pillars.

    Weight update rule (exponential moving average):
      w_pillar(g+1) = α × observed_impact + (1−α) × w_pillar(g)

    Proposition 26.1 (Triadic Transfer): high-SI configurations from one
    domain serve as weight priors for new domains (cold-start acceleration).
    """

    ALPHA: float = 0.3   # EMA smoothing factor

    def __init__(self):
        self.history: List[ImpactRecord] = []
        # Pillar weights: initial prior = balanced (1/3 each)
        self.weights: Dict[str, float] = {"F": 0.333, "P": 0.333, "A": 0.334}

    def record(self, record: ImpactRecord) -> None:
        self.history.append(record)

    def update_weights(self, s_before: TriadicSystem,
                       s_after: TriadicSystem) -> None:
        """
        Observe which pillar improved most and update its weight upward.
        This biases future scheduler priority toward the most impactful pillar.
        """
        delta_F = abs(s_after.F - s_before.F)
        delta_P = abs(s_after.P - s_before.P)
        delta_A = abs(s_after.A - s_before.A)
        total   = delta_F + delta_P + delta_A + 1e-9

        # Observed relative impact per pillar
        obs = {"F": delta_F / total, "P": delta_P / total, "A": delta_A / total}

        # EMA update
        for pillar in ("F", "P", "A"):
            self.weights[pillar] = (
                self.ALPHA * obs[pillar] +
                (1 - self.ALPHA) * self.weights[pillar]
            )
        # Renormalize
        total_w = sum(self.weights.values())
        for pillar in self.weights:
            self.weights[pillar] /= total_w

    def mean_roi(self) -> float:
        if not self.history:
            return 0.0
        return statistics.mean(r.roi for r in self.history)

    def dominant_pillar(self) -> str:
        return max(self.weights, key=self.weights.get)

    def summary(self) -> str:
        return (f"weights F={self.weights['F']:.3f}  "
                f"P={self.weights['P']:.3f}  A={self.weights['A']:.3f}  "
                f"dominant={self.dominant_pillar()}  "
                f"mean_ROI={self.mean_roi():.4f}")


# ═══════════════════════════════════════════════════════════════════════════════
# TRIADIC AGENT  (§33.3 — LLM-powered pillar evaluation)
# ═══════════════════════════════════════════════════════════════════════════════

AGENT_SYSTEM_PROMPT = """You are a U-Theory triadic analyst.
U-Theory: every system S = (F, P, A) where:
  F = Form     (structure / identity — costs TIME to maintain)
  P = Position (context / location  — costs SPACE to maintain)
  A = Action   (process / energy    — costs ENERGY to maintain)

Stability Index: SI = U / (1+δ)²   where U = ∛(F·P·A),  δ = (max−min)/(max+0.01)
Non-compensatory: any pillar → 0 collapses SI to ~0.

You must score the requested pillar on [0.0, 1.0].
Respond with ONLY a JSON object: {"score": <float 0-1>, "rationale": "<one sentence>"}"""


class TriadicAgent:
    """
    An LLM-powered agent that evaluates one triadic pillar (F, P, or A)
    for a given (action, form, position) combination in a domain.

    Falls back to heuristic scoring when no API key is available.
    """

    ROLES = ("Form", "Position", "Action", "Generalizer")

    def __init__(self, role: str,
                 model: str = "openai/gpt-4o-mini",
                 use_llm: bool = True):
        if role not in self.ROLES:
            raise ValueError(f"role must be one of {self.ROLES}")
        self.role    = role
        self.model   = model
        self.use_llm = use_llm and bool(OPENROUTER_API_KEY)
        self._cache: Dict[str, float] = {}

    def _cache_key(self, s: TriadicSystem) -> str:
        return f"{self.role}|{s.domain_name}|{s.action_label}|{s.form_label}|{s.position_label}"

    def _build_prompt(self, s: TriadicSystem) -> str:
        if self.role == "Form":
            pillar_desc = (
                "the FORM pillar — structural quality, identity clarity, "
                "and endurance of this system over time"
            )
            focus = f"Form variant: '{s.form_label}'"
        elif self.role == "Position":
            pillar_desc = (
                "the POSITION pillar — contextual fit, spatial/relational "
                "relevance, and resistance to displacement"
            )
            focus = f"Position variant: '{s.position_label}'"
        elif self.role == "Action":
            pillar_desc = (
                "the ACTION pillar — process effectiveness, purposeful energy "
                "expenditure, and transformational impact"
            )
            focus = f"Action variant: '{s.action_label}'"
        else:  # Generalizer
            pillar_desc = (
                "the OVERALL STABILITY — cross-pillar coherence, triadic "
                "balance, and emergent stability index"
            )
            focus = (
                f"Action='{s.action_label}', Form='{s.form_label}', "
                f"Position='{s.position_label}'"
            )

        return (
            f"Domain: {s.domain_name}\n"
            f"{focus}\n\n"
            f"Score {pillar_desc} on [0.0, 1.0].\n"
            f"Current numeric estimates: F={s.F:.3f}, P={s.P:.3f}, A={s.A:.3f}\n"
            f"Use these as starting priors but apply your own judgment.\n"
            f"Return JSON: {{\"score\": <float>, \"rationale\": \"<one sentence>\"}}"
        )

    def _heuristic_score(self, s: TriadicSystem) -> float:
        """Fallback: perturb the existing pillar score slightly."""
        base = {"Form": s.F, "Position": s.P, "Action": s.A,
                "Generalizer": s.SI}.get(self.role, s.SI)
        noise = random.gauss(0, 0.02)
        return round(max(0.01, min(1.0, base + noise)), 4)

    def evaluate(self, s: TriadicSystem) -> Tuple[float, str]:
        """
        Evaluate the pillar for system s.
        Returns (score, rationale).
        """
        key = self._cache_key(s)
        if key in self._cache:
            return self._cache[key], "(cached)"

        if not self.use_llm:
            score = self._heuristic_score(s)
            self._cache[key] = score
            return score, "(heuristic — no API key)"

        prompt = self._build_prompt(s)
        result = api_generate(
            provider="openrouter",
            prompt=prompt,
            model=self.model,
            system=AGENT_SYSTEM_PROMPT,
            max_tokens=128,
            temperature=0.1,
        )

        if not result.success:
            score = self._heuristic_score(s)
            self._cache[key] = score
            return score, f"(fallback — {result.error[:60]})"

        try:
            data      = json.loads(result.text)
            score     = float(data.get("score", self._heuristic_score(s)))
            rationale = str(data.get("rationale", ""))
            score     = max(0.01, min(1.0, score))
        except (json.JSONDecodeError, ValueError, KeyError):
            score     = self._heuristic_score(s)
            rationale = "(parse error — fallback)"

        self._cache[key] = score
        return score, rationale


class AgentJury:
    """
    Orchestrates Form + Position + Action + Generalizer agents (§33.3).
    Returns consensus (F, P, A) scores for a candidate system.
    """

    def __init__(self, model: str = "openai/gpt-4o-mini",
                 use_llm: bool = True):
        self.form_agent    = TriadicAgent("Form",       model, use_llm)
        self.pos_agent     = TriadicAgent("Position",   model, use_llm)
        self.act_agent     = TriadicAgent("Action",     model, use_llm)
        self.gen_agent     = TriadicAgent("Generalizer", model, use_llm)

    def evaluate(self, s: TriadicSystem,
                 verbose: bool = False) -> TriadicSystem:
        """
        Run all four agents on system s.
        Returns a new TriadicSystem with LLM-revised pillar scores.
        """
        f_score, f_rationale = self.form_agent.evaluate(s)
        p_score, p_rationale = self.pos_agent.evaluate(s)
        a_score, a_rationale = self.act_agent.evaluate(s)
        g_score, _           = self.gen_agent.evaluate(s)

        # Generalizer acts as a soft regularizer:
        # blend agent scores 80% direct + 20% generalizer cross-signal
        blend = 0.20
        f_blended = (1 - blend) * f_score + blend * g_score
        p_blended = (1 - blend) * p_score + blend * g_score
        a_blended = (1 - blend) * a_score + blend * g_score

        revised = TriadicSystem(
            domain_name    = s.domain_name,
            action_label   = s.action_label,
            form_label     = s.form_label,
            position_label = s.position_label,
            F              = round(f_blended, 4),
            P              = round(p_blended, 4),
            A              = round(a_blended, 4),
            generation     = s.generation,
        )

        if verbose:
            print(f"    [Jury] {s.action_label[:12]} | {s.form_label[:12]} | "
                  f"{s.position_label[:12]}")
            print(f"      F: {s.F:.3f} → {revised.F:.3f}  {f_rationale[:60]}")
            print(f"      P: {s.P:.3f} → {revised.P:.3f}  {p_rationale[:60]}")
            print(f"      A: {s.A:.3f} → {revised.A:.3f}")
            print(f"      SI: {s.SI:.3f} → {revised.SI:.3f}")

        return revised


# ═══════════════════════════════════════════════════════════════════════════════
# GSI RUNTIME  — full AD-RTD pipeline (§23.1 pseudocode + §33 blueprint)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class RuntimeConfig:
    """Configuration for a gsi_runtime() execution."""
    generations:        int   = 10
    top_k:              int   = 20
    jury_top_k:         int   = 5    # how many top candidates to send to AgentJury
    transfer_interval:  int   = 3    # cross-domain transfer every N generations
    budget:             Optional[TriadicBudget] = None
    use_llm:            bool  = True
    model:              str   = "openai/gpt-4o-mini"
    verbose:            bool  = False
    halt_si_threshold:  float = 0.85  # halt if mean SI ≥ this (§22.4)
    halt_plateau:       int   = 3     # halt if SI stagnant for N generations


@dataclass
class GenerationResult:
    """Per-generation output record."""
    generation:  int
    domain:      str
    mean_SI:     float
    best_SI:     float
    best_system: str
    budget_snap: str
    learning:    str


class GSIRuntime:
    """
    Full AD-RTD runtime engine (§33).

    Phase 0:  Scan    — problem / instability detection
    Phase 1:  Action  — enumerate A
    Phase 2:  Form    — bind F | A
    Phase 3:  Position— expand P | F,A
    Phase 4:  Construct candidates
    Phase 5:  Evaluate (AgentJury or heuristic)
    Phase 6:  Triage
    Phase 7:  Prioritize ΔSI/Cost
    Phase 8:  Schedule (TriadicScheduler §20)
    Phase 9:  Execute
    Phase 10: Learn (LearningLaw §26)
    Phase 11: Iterate / halt
    """

    def __init__(self, domains: List[Domain], config: Optional[RuntimeConfig] = None):
        self.config = config or RuntimeConfig()
        self.domains = domains
        self.schedulers: Dict[str, TriadicScheduler] = {
            d.name: TriadicScheduler(d) for d in domains
        }
        self.jury = AgentJury(
            model   = self.config.model,
            use_llm = self.config.use_llm,
        )
        self.learning = LearningLaw()
        self.budget   = self.config.budget or TriadicBudget(
            T_max=float(self.config.generations),
            S_max=float(self.config.top_k * self.config.generations * len(domains)),
            E_max=float(self.config.jury_top_k * self.config.generations * len(domains)),
        )
        self.history: List[GenerationResult] = []
        self.transfer_log: List[dict] = []
        self._plateau_counts: Dict[str, int] = {d.name: 0 for d in domains}
        self._prev_mean_SI:   Dict[str, float] = {d.name: 0.0 for d in domains}

    # ── Phase 0: Scan ─────────────────────────────────────────────────────────
    def _phase0_scan(self, scheduler: TriadicScheduler) -> bool:
        """Detect instability: return True if population needs improvement."""
        mean_si = statistics.mean(s.SI for s in scheduler.population)
        return mean_si < THETA_STABLE

    # ── Phase 5: Evaluate (AgentJury on top-k) ───────────────────────────────
    def _phase5_evaluate(self, scheduler: TriadicScheduler,
                         top: List[TriadicSystem], mean_si: float = 0.0) -> List[TriadicSystem]:
        """
        Run AgentJury on the top jury_top_k candidates.
        Patch 3.3: adaptive jury_top_k — more evaluation when SI is low.
        Replace them in the population with jury-revised scores.
        """
        # Adaptive: evaluate more candidates when SI is low (more room for improvement)
        base_k = self.config.jury_top_k
        adaptive_k = max(2, int(base_k * (1.5 - mean_si)))  # low SI → more jury
        k = min(adaptive_k, len(top))
        jury_candidates = top[:k]
        revised = []
        for s in jury_candidates:
            r = self.jury.evaluate(s, verbose=self.config.verbose)
            revised.append(r)
            # Phase 10 update — observe ΔSI and update weights
            self.learning.update_weights(s, r)
            rec = ImpactRecord(
                system_repr=str(s),
                SI_before=s.SI,
                SI_after=r.SI,
                cost=self.budget.charge(delta_T=0, delta_S=0, delta_E=1.0),
                generation=scheduler.generation,
            )
            self.learning.record(rec)
        # Stitch revised back with the rest unchanged
        return revised + top[k:]

    # ── Phase 6-7: Triage + Prioritize ───────────────────────────────────────
    @staticmethod
    def _phase6_triage(systems: List[TriadicSystem]) -> Dict[str, List[TriadicSystem]]:
        return {
            "HIGH": [s for s in systems if s.triage_category() == "HIGH"],
            "MID":  [s for s in systems if s.triage_category() == "MID"],
            "LOW":  [s for s in systems if s.triage_category() == "LOW"],
        }

    @staticmethod
    def _phase7_prioritize(systems: List[TriadicSystem]) -> List[TriadicSystem]:
        """Sort by ΔSI/Cost proxy: (1−SI) / ∛(F·P·A cost estimate)."""
        def priority(s: TriadicSystem) -> float:
            potential = 1.0 - s.SI
            cost_est  = (max(1 - s.F, 0.01) * max(1 - s.P, 0.01) *
                         max(1 - s.A, 0.01)) ** (1 / 3)
            return potential / cost_est
        return sorted(systems, key=priority, reverse=True)

    # ── Cross-domain transfer ─────────────────────────────────────────────────
    def _transfer_high_si(self):
        """Inject high-SI templates across structurally similar domains (§26.4).
        Patch 3.4: structured logging of transfer details."""
        schedulers = list(self.schedulers.values())
        for i, src in enumerate(schedulers):
            for j, tgt in enumerate(schedulers):
                if i == j:
                    continue
                sim = _jaccard_similarity(src.domain, tgt.domain)
                if sim < 0.3:
                    continue
                donors = [s for s in src.population if s.triage_category() == "HIGH"]
                for donor in donors[:2]:
                    t_a = random.choice(tgt.domain.actions)
                    t_f = random.choice(tgt.domain.forms)
                    t_p = random.choice(tgt.domain.positions)
                    adapted = TriadicSystem(
                        domain_name    = tgt.domain.name,
                        action_label   = t_a[0],
                        form_label     = t_f[0],
                        position_label = t_p[0],
                        F=donor.F, P=donor.P, A=donor.A,
                        generation=donor.generation,
                    )
                    tgt.population.append(adapted)
                    if self.config.verbose:
                        print(f"      [Transfer] {src.domain.name} → {tgt.domain.name}: "
                              f"SI={donor.SI:.3f} adapted as ({t_a[0][:12]}, {t_f[0][:12]}, {t_p[0][:12]})")
                    # Structured transfer log (§3.4)
                    self.transfer_log.append({
                        "src_domain": src.domain.name,
                        "tgt_domain": tgt.domain.name,
                        "donor_SI": round(donor.SI, 4),
                        "adapted_labels": f"{t_a[0]}|{t_f[0]}|{t_p[0]}",
                        "similarity": round(sim, 3),
                    })
                # Enforce population cap after transfer
                tgt._trim_population()

    # ── Halt check (§22.4 + Patch 3.5 pillar-level) ──────────────────────────
    def _should_halt(self, domain_name: str, mean_si: float,
                     scheduler: TriadicScheduler = None) -> bool:
        if mean_si >= self.config.halt_si_threshold:
            return True
        if abs(mean_si - self._prev_mean_SI[domain_name]) < 1e-4:
            self._plateau_counts[domain_name] += 1
        else:
            self._plateau_counts[domain_name] = 0
        self._prev_mean_SI[domain_name] = mean_si
        if self._plateau_counts[domain_name] >= self.config.halt_plateau:
            return True
        # Patch 3.5: pillar-level early stopping
        # If all pillars are stable (>0.9) for this domain, no point continuing
        if scheduler and scheduler.population:
            best = max(scheduler.population, key=lambda s: s.SI)
            if best.F > 0.9 and best.P > 0.9 and best.A > 0.9:
                return True
        return False

    # ── Checkpoint persistence (§3.2) ─────────────────────────────────────────
    def save_checkpoint(self, path: str):
        """Serialize runtime state to JSON for resume."""
        import json as _json
        from pathlib import Path as _Path
        state = {
            "budget": self.budget.to_dict(),
            "transfer_log": self.transfer_log,
            "history_len": len(self.history),
            "plateau_counts": self._plateau_counts,
            "prev_mean_SI": self._prev_mean_SI,
            "populations": {
                name: [
                    {"F": s.F, "P": s.P, "A": s.A, "SI": s.SI,
                     "domain": s.domain_name, "action": s.action_label,
                     "form": s.form_label, "position": s.position_label,
                     "gen": s.generation}
                    for s in sched.population
                ]
                for name, sched in self.schedulers.items()
            },
            "si_history": {
                name: sched.si_history
                for name, sched in self.schedulers.items()
            },
        }
        _Path(path).write_text(_json.dumps(state, indent=2), encoding="utf-8")

    @classmethod
    def load_checkpoint(cls, path: str, domains: "List[Domain]",
                        config: "Optional[RuntimeConfig]" = None) -> "GSIRuntime":
        """Restore runtime from a JSON checkpoint file."""
        import json as _json
        from pathlib import Path as _Path
        state = _json.loads(_Path(path).read_text(encoding="utf-8"))
        rt = cls(domains, config)
        rt.budget = TriadicBudget.from_dict(state["budget"])
        rt.transfer_log = state.get("transfer_log", [])
        rt._plateau_counts = state.get("plateau_counts", rt._plateau_counts)
        rt._prev_mean_SI = state.get("prev_mean_SI", rt._prev_mean_SI)
        for name, pop_data in state.get("populations", {}).items():
            if name in rt.schedulers:
                sched = rt.schedulers[name]
                sched.population = [
                    TriadicSystem(
                        domain_name=s["domain"], action_label=s["action"],
                        form_label=s["form"], position_label=s["position"],
                        F=s["F"], P=s["P"], A=s["A"], generation=s["gen"],
                    )
                    for s in pop_data
                ]
        for name, hist in state.get("si_history", {}).items():
            if name in rt.schedulers:
                rt.schedulers[name].si_history = hist
        return rt

    # ── Main runtime loop ─────────────────────────────────────────────────────
    def run(self) -> List[GenerationResult]:
        """
        Execute the full AD-RTD pipeline for all configured generations.
        Returns per-generation result records.
        """
        print(f"\n{'═'*68}")
        print(f"  GSI-RTD RUNTIME v0.1 — AD-RTD Pipeline")
        print(f"  Domains: {[d.name for d in self.domains]}")
        print(f"  Generations: {self.config.generations}  "
              f"top_k={self.config.top_k}  "
              f"LLM={'ON' if self.config.use_llm else 'OFF (heuristic)'}")
        print(f"  {self.budget.summary()}")
        print(f"{'═'*68}")

        active_domains = set(d.name for d in self.domains)

        for g in range(1, self.config.generations + 1):
            # Stage 1 budget gate — halt entire run if budget exhausted
            if self.budget.exhausted:
                print(f"\n  [Gen {g}] Budget exhausted — halting. {self.budget.summary()}")
                break

            print(f"\n  ── Generation {g}/{self.config.generations} "
                  f"{'─'*(40 - len(str(g)))}")

            self.budget.charge(delta_T=1.0, delta_S=0.0, delta_E=0.0)

            for domain_name, scheduler in self.schedulers.items():
                if domain_name not in active_domains:
                    continue

                # Phase 0: Scan
                if not self._phase0_scan(scheduler):
                    print(f"    [{domain_name}] Phase 0: already stable — skip")
                    continue

                # Phase 8+9: Schedule + Execute (TriadicScheduler.step)
                top = scheduler.step(top_k=self.config.top_k)
                self.budget.charge(delta_T=0.0, delta_S=float(len(top)), delta_E=0.0)

                # Phase 5: Evaluate — AgentJury on top-jury_top_k (adaptive)
                top = self._phase5_evaluate(scheduler, top, mean_si=0.0)

                # Phase 6: Triage
                triage = self._phase6_triage(top)

                # Phase 7: Prioritize mid candidates
                mid_prioritized = self._phase7_prioritize(triage["MID"])

                mean_si = statistics.mean(s.SI for s in top) if top else 0.0
                best    = max(top, key=lambda s: s.SI) if top else None

                result = GenerationResult(
                    generation  = g,
                    domain      = domain_name,
                    mean_SI     = round(mean_si, 4),
                    best_SI     = round(best.SI, 4) if best else 0.0,
                    best_system = str(best) if best else "—",
                    budget_snap = self.budget.summary(),
                    learning    = self.learning.summary(),
                )
                self.history.append(result)

                print(
                    f"    [{domain_name}] "
                    f"mean_SI={mean_si:.4f}  best_SI={result.best_SI:.4f}  "
                    f"HIGH={len(triage['HIGH'])} MID={len(triage['MID'])} "
                    f"LOW={len(triage['LOW'])}"
                )
                if mid_prioritized and self.config.verbose:
                    print(f"      top-MID priority: {mid_prioritized[0]}")
                if self.config.verbose:
                    print(f"      Learning: {self.learning.summary()}")

                # Phase 11: Halt check for this domain
                if self._should_halt(domain_name, mean_si, scheduler=scheduler):
                    print(f"    [{domain_name}] Halt condition met — removing from active set")
                    active_domains.discard(domain_name)

            # Cross-domain transfer every N generations
            if g % self.config.transfer_interval == 0:
                self._transfer_high_si()
                if self.config.verbose:
                    print(f"    [Transfer] Gen {g} — high-SI cross-domain injection done")

            if not active_domains:
                print(f"\n  All domains halted at generation {g}.")
                break

        return self.history

    def report(self) -> None:
        """Print final summary report."""
        print(f"\n{'═'*68}")
        print("  GSI RUNTIME — FINAL REPORT")
        print(f"{'═'*68}")
        print(f"  {self.budget.summary()}")
        print(f"  {self.learning.summary()}")

        for domain_name, scheduler in self.schedulers.items():
            best5 = scheduler.best(5)
            traj = scheduler.si_history
            trend = " → ".join(
                f"{v:.3f}" for v in traj[::max(1, len(traj) // 5)]
            )
            print(f"\n  ▶ {domain_name}")
            print(f"    Generations run:  {scheduler.generation}")
            print(f"    SI trajectory:    {trend}")
            print(f"    Top 5 systems:")
            for i, s in enumerate(best5, 1):
                sc = s.scores
                print(f"      {i}. {s}")
                print(f"         F={s.F:.3f}  P={s.P:.3f}  A={s.A:.3f}  "
                      f"U={sc['U']:.3f}  δ={sc['delta']:.3f}  SI={sc['SI']:.3f}")

        print(f"\n{'═'*68}")
        print("  COMBINED TRIAGE")
        print(f"{'─'*68}")
        all_sys = []
        for sched in self.schedulers.values():
            all_sys.extend(sched.population)
        high  = sum(1 for s in all_sys if s.triage_category() == "HIGH")
        mid   = sum(1 for s in all_sys if s.triage_category() == "MID")
        low   = sum(1 for s in all_sys if s.triage_category() == "LOW")
        total = max(len(all_sys), 1)
        print(f"  HIGH (≥{THETA_STABLE}): {high:4d}  ({high/total*100:.1f}%)")
        print(f"  MID  (≥{THETA_CRITICAL}): {mid:4d}  ({mid/total*100:.1f}%)")
        print(f"  LOW  (<{THETA_CRITICAL}): {low:4d}  ({low/total*100:.1f}%)")
        print(f"{'═'*68}\n")


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def _jaccard_similarity(d1: Domain, d2: Domain) -> float:
    a1 = set(a[0] for a in d1.actions)
    a2 = set(a[0] for a in d2.actions)
    union = a1 | a2
    inter = a1 & a2
    return len(inter) / len(union) if union else 0.0


# ═══════════════════════════════════════════════════════════════════════════════
# PUBLIC API  (convenience wrappers)
# ═══════════════════════════════════════════════════════════════════════════════

def gsi_runtime(
    domains: List[Domain],
    generations: int = 10,
    top_k: int = 20,
    use_llm: bool = True,
    verbose: bool = False,
    budget: Optional[TriadicBudget] = None,
    model: str = "openai/gpt-4o-mini",
) -> GSIRuntime:
    """
    Convenience entry point for the full GSI-RTD AD-RTD pipeline.

    Example:
        from gsi_multi_domain import domain_email_marketing, domain_publisher_outreach
        from gsi_runtime import gsi_runtime

        runtime = gsi_runtime(
            domains=[domain_email_marketing(), domain_publisher_outreach()],
            generations=10,
            use_llm=False,   # True requires OPENROUTER_API_KEY
        )
        runtime.run()
        runtime.report()
    """
    cfg = RuntimeConfig(
        generations=generations,
        top_k=top_k,
        use_llm=use_llm,
        verbose=verbose,
        budget=budget,
        model=model,
    )
    rt = GSIRuntime(domains=domains, config=cfg)
    rt.run()
    return rt


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse

    random.seed(42)

    parser = argparse.ArgumentParser(
        description="GSI-RTD Runtime v0.1 — Full AD-RTD Pipeline"
    )
    parser.add_argument("--generations", type=int,   default=10)
    parser.add_argument("--top-k",       type=int,   default=20)
    parser.add_argument("--jury-k",      type=int,   default=5,
                        help="Top-k candidates sent to AgentJury per generation")
    parser.add_argument("--use-llm",     action="store_true", default=False,
                        help="Enable LLM evaluation (requires OPENROUTER_API_KEY)")
    parser.add_argument("--verbose",     action="store_true", default=False)
    parser.add_argument("--model",       type=str,
                        default="openai/gpt-4o-mini")
    args = parser.parse_args()

    # Import domain definitions
    from gsi_multi_domain import (
        domain_email_marketing,
        domain_publisher_outreach,
        domain_content_creation,
    )

    domains = [
        domain_email_marketing(),
        domain_publisher_outreach(),
        domain_content_creation(),
    ]

    cfg = RuntimeConfig(
        generations       = args.generations,
        top_k             = args.top_k,
        jury_top_k        = args.jury_k,
        use_llm           = args.use_llm,
        verbose           = args.verbose,
        model             = args.model,
    )

    rt = GSIRuntime(domains=domains, config=cfg)
    rt.run()
    rt.report()
