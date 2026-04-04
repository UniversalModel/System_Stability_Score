#!/usr/bin/env python3
"""
gsi_multi_domain.py
===================
GSI-RTD Multi-Domain Prototype — General Superintelligence through
Recursive Triadic Decomposition (APPENDIX G, v27)

Implements:
  - Domain abstraction with F / P / A variant definitions
  - TriadicSystem: S = (F, P, A) with SSS scoring
  - TriadicScheduler: weakest-pillar targeting + non-compensatory ranking
  - MultiDomainGSI: runs parallel schedulers across N domains
  - Transfer logic: import high-SI systems between structurally similar domains
  - Monte Carlo baseline comparison (N=200 random runs)
  - Generation loop with adaptive exploration injection (ε)

SSS formulas (v26 invariant):
  U  = (F * P * A) ** (1/3)
  δ  = (max(F,P,A) - min(F,P,A)) / (max(F,P,A) + 0.01)
  SI = U / (1 + δ) ** 2

Author: Petar Nikolov — U-Theory v26 / GSI-RTD
Date:   2026-03-27
"""

import random
import math
import statistics
import itertools
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from copy import deepcopy

# ── Thresholds (LGP canonical, §5.1) ─────────────────────────────────────────
THETA_STABLE   = 0.618   # High SI — exploit + transfer
THETA_CRITICAL = 0.38    # Low SI  — redesign or reject
EXPLORATION_EPS_INIT  = 0.30   # ε₀ at generation 1
EXPLORATION_EPS_FLOOR = 0.05   # minimum ε
EXPLORATION_DECAY     = 0.10   # λ decay rate
MUTATION_STRENGTH     = 0.10   # 10% boost on weakest pillar per mutation
MAX_POPULATION_SIZE   = 500    # Patch 4.1: cap to prevent unbounded growth
MAX_POPULATION_SIZE   = 500    # §4.1 — cap to prevent population explosion


# ═══════════════════════════════════════════════════════════════════════════════
# CORE: SSS SCORING
# ═══════════════════════════════════════════════════════════════════════════════

def compute_si(F: float, P: float, A: float) -> Dict[str, float]:
    """Compute U, δ, SI for a triadic system (SSS v26 formulas)."""
    F = max(0.001, min(1.0, F))
    P = max(0.001, min(1.0, P))
    A = max(0.001, min(1.0, A))

    U     = (F * P * A) ** (1 / 3)
    delta = (max(F, P, A) - min(F, P, A)) / (max(F, P, A) + 0.01)
    SI    = U / (1 + delta) ** 2

    return {"U": round(U, 4), "delta": round(delta, 4), "SI": round(SI, 4)}


# ═══════════════════════════════════════════════════════════════════════════════
# DOMAIN — defines F / P / A variant sets
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Domain:
    """
    A triadic domain: defines the variant sets for F (Form), P (Position),
    A (Action). Each variant is a (name, base_score) tuple where base_score
    is the domain expert's prior estimate for that variant's pillar strength.
    """
    name: str
    actions:   List[Tuple[str, float]]   # (label, base_A_score)
    forms:     List[Tuple[str, float]]   # (label, base_F_score)
    positions: List[Tuple[str, float]]   # (label, base_P_score)

    def total_candidates(self) -> int:
        return len(self.actions) * len(self.forms) * len(self.positions)


# ── Built-in example domains ──────────────────────────────────────────────────

def domain_email_marketing() -> Domain:
    """Email marketing campaign — 6×6×4 = 144 systems (paper domain)."""
    return Domain(
        name="Email Marketing",
        actions=[
            ("Send newsletter",       0.75),
            ("Send promotional",      0.80),
            ("Send onboarding",       0.70),
            ("Send re-engagement",    0.60),
            ("Send transactional",    0.85),
            ("Send survey",           0.55),
        ],
        forms=[
            ("Plain text",            0.60),
            ("HTML rich",             0.80),
            ("PDF attachment",        0.65),
            ("Video embed",           0.70),
            ("Infographic",           0.75),
            ("Interactive AMP",       0.85),
        ],
        positions=[
            ("Cold audience",         0.50),
            ("Warm leads",            0.70),
            ("Existing customers",    0.85),
            ("Churned customers",     0.45),
        ],
    )


def domain_publisher_outreach() -> Domain:
    """Publisher outreach campaign — 5×5×5 = 125 systems."""
    return Domain(
        name="Publisher Outreach",
        actions=[
            ("Email pitch",           0.70),
            ("LinkedIn message",      0.65),
            ("X/Twitter DM",          0.55),
            ("Contact form",          0.60),
            ("Phone call",            0.75),
        ],
        forms=[
            ("Plain text email",      0.65),
            ("HTML email",            0.75),
            ("PDF proposal",          0.80),
            ("Video pitch",           0.70),
            ("Infographic abstract",  0.60),
        ],
        positions=[
            ("Academic publisher",    0.70),
            ("Literary publisher",    0.65),
            ("Literary agent",        0.75),
            ("Journal editor",        0.80),
            ("Cultural foundation",   0.60),
        ],
    )


def domain_content_creation() -> Domain:
    """Content creation / publication — 4×5×4 = 80 systems."""
    return Domain(
        name="Content Creation",
        actions=[
            ("Write article",         0.80),
            ("Record podcast",        0.70),
            ("Create video",          0.75),
            ("Write thread",          0.65),
        ],
        forms=[
            ("Long-form essay",       0.80),
            ("Short-form post",       0.65),
            ("Visual explainer",      0.75),
            ("Technical paper",       0.85),
            ("Story / narrative",     0.70),
        ],
        positions=[
            ("General audience",      0.60),
            ("Academic community",    0.75),
            ("Tech community",        0.80),
            ("Business audience",     0.70),
        ],
    )


# ═══════════════════════════════════════════════════════════════════════════════
# TRIADIC SYSTEM — S = (F, P, A)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class TriadicSystem:
    """A single candidate system S = (F, P, A)."""
    domain_name: str
    action_label: str
    form_label:   str
    position_label: str
    F: float   # current Form score [0,1]
    P: float   # current Position score [0,1]
    A: float   # current Action score [0,1]
    generation: int = 0

    @property
    def scores(self) -> Dict[str, float]:
        return compute_si(self.F, self.P, self.A)

    @property
    def SI(self) -> float:
        return self.scores["SI"]

    @property
    def delta(self) -> float:
        return self.scores["delta"]

    def weakest_pillar(self) -> str:
        """Return name of the weakest pillar ('F', 'P', or 'A')."""
        vals = {"F": self.F, "P": self.P, "A": self.A}
        return min(vals, key=vals.get)

    def triage_category(self) -> str:
        si = self.SI
        if si >= THETA_STABLE:
            return "HIGH"
        elif si >= THETA_CRITICAL:
            return "MID"
        else:
            return "LOW"

    def __repr__(self) -> str:
        return (f"S({self.action_label[:12]} | {self.form_label[:12]} | "
                f"{self.position_label[:12]}) SI={self.SI:.3f} [{self.triage_category()}]")


# ═══════════════════════════════════════════════════════════════════════════════
# SCHEDULER — weakest-pillar targeting + non-compensatory ranking
# ═══════════════════════════════════════════════════════════════════════════════

class TriadicScheduler:
    """
    Implements GSI-RTD §20: Two-stage selection.
      Stage 1 — Hard gates (reject collapsed candidates)
      Stage 2 — Non-compensatory geometric ranking
    Plus: weakest-pillar mutation, exploration injection (ε-greedy).
    """

    def __init__(self, domain: Domain):
        self.domain     = domain
        self.population = self._generate_all()
        self.generation = 0
        self.si_history: List[float] = []

    def _generate_all(self) -> List[TriadicSystem]:
        """Generate all A×F×P candidate systems."""
        systems = []
        for (a_lbl, a_score), (f_lbl, f_score), (p_lbl, p_score) in itertools.product(
            self.domain.actions, self.domain.forms, self.domain.positions
        ):
            # Add small random noise (±5%) to break ties and simulate real variance
            noise = lambda s: max(0.01, min(1.0, s + random.uniform(-0.05, 0.05)))
            systems.append(TriadicSystem(
                domain_name    = self.domain.name,
                action_label   = a_lbl,
                form_label     = f_lbl,
                position_label = p_lbl,
                F = noise(f_score),
                P = noise(p_score),
                A = noise(a_score),
            ))
        return systems

    # ── Stage 1: Hard Gates ───────────────────────────────────────────────────
    def _passes_gates(self, s: TriadicSystem) -> bool:
        """Reject if any pillar is collapsed (< 0.05)."""
        return min(s.F, s.P, s.A) >= 0.05

    # ── Stage 2: Non-compensatory geometric score ─────────────────────────────
    def _scheduler_score(self, s: TriadicSystem) -> float:
        """∛(SI × (1-δ) × balance) — geometric mean, non-compensatory."""
        balance = 1.0 - s.delta
        # Improvement potential: room to grow toward 1.0
        potential = 1.0 - s.SI
        return (s.SI * balance * potential) ** (1 / 3)

    # ── Mutation: boost weakest pillar (adaptive strength) ──────────────────
    def _mutate(self, s: TriadicSystem) -> TriadicSystem:
        """Boost weakest pillar with decaying mutation strength."""
        m = deepcopy(s)
        # Adaptive: strength decays as generations increase (§4.4)
        max_gen = max(50, self.generation)
        strength = MUTATION_STRENGTH * (1.0 - 0.5 * self.generation / max_gen)
        strength = max(0.02, strength)
        w = m.weakest_pillar()
        if w == "F":
            m.F = min(1.0, m.F * (1 + strength))
        elif w == "P":
            m.P = min(1.0, m.P * (1 + strength))
        else:
            m.A = min(1.0, m.A * (1 + strength))
        m.generation = self.generation
        return m

    # ── Adaptive exploration rate ε(g) ───────────────────────────────────────
    def _epsilon(self) -> float:
        coverage = min(1.0, self.generation / max(1, len(self.population)))
        eps = EXPLORATION_EPS_INIT * math.exp(-EXPLORATION_DECAY * self.generation * coverage)
        return max(EXPLORATION_EPS_FLOOR, eps)

    def _trim_population(self):
        """Enforce MAX_POPULATION_SIZE by dropping lowest-SI systems."""
        if len(self.population) > MAX_POPULATION_SIZE:
            self.population.sort(key=lambda s: s.SI, reverse=True)
            self.population = self.population[:MAX_POPULATION_SIZE]

    # ── Main step ─────────────────────────────────────────────────────────────
    def step(self, top_k: int = 20) -> List[TriadicSystem]:
        """
        Execute one GSI generation:
        1. Filter by hard gates
        2. Rank by scheduler score (geometric, non-compensatory)
        3. Select top-k
        4. Elitism: preserve top-1 unmutated
        5. Mutate remaining top candidates (weakest-pillar boost)
        6. Inject ε-exploration (random novel candidates)
        7. Merge into population (capped at MAX_POPULATION_SIZE)
        Returns: top_k best systems after mutation
        """
        self.generation += 1

        # Stage 1 + 2
        survivors = [s for s in self.population if self._passes_gates(s)]
        ranked    = sorted(survivors, key=self._scheduler_score, reverse=True)
        top       = ranked[:top_k]

        # Elitism: keep top-1 system unmutated (§4.3)
        elite = [deepcopy(top[0])] if top else []
        mutated = [self._mutate(s) for s in top[1:]]

        # Exploration injection
        eps = self._epsilon()
        n_explore = max(1, int(top_k * eps))
        explorers = random.sample(self.population, min(n_explore, len(self.population)))

        # Merge: elite + mutated + explorers + remaining ranked
        keep_n = max(0, len(ranked) - len(elite) - len(mutated) - len(explorers))
        self.population = elite + mutated + explorers + ranked[:keep_n]

        # Population cap (§4.1)
        self._trim_population()

        mean_si = statistics.mean(s.SI for s in top) if top else 0.0
        self.si_history.append(round(mean_si, 4))

        return top

    def best(self, n: int = 5) -> List[TriadicSystem]:
        return sorted(self.population, key=lambda s: s.SI, reverse=True)[:n]


# ═══════════════════════════════════════════════════════════════════════════════
# MULTI-DOMAIN GSI
# ═══════════════════════════════════════════════════════════════════════════════

class MultiDomainGSI:
    """
    Runs TriadicSchedulers across multiple domains in parallel.
    Implements cross-domain transfer (GSI-RTD §26.4 — Proposition 26.1).
    """

    def __init__(self, domains: List[Domain]):
        self.schedulers: Dict[str, TriadicScheduler] = {
            d.name: TriadicScheduler(d) for d in domains
        }

    def run(self, generations: int = 10, top_k: int = 20) -> Dict[str, List[float]]:
        """Run all schedulers for N generations. Returns SI history per domain."""
        for g in range(generations):
            for name, scheduler in self.schedulers.items():
                scheduler.step(top_k=top_k)

            # Cross-domain transfer every 3 generations
            if (g + 1) % 3 == 0:
                self._transfer_high_si()

        return {name: s.si_history for name, s in self.schedulers.items()}

    def _transfer_high_si(self):
        """
        Transfer high-SI systems across domains (§26.4 Triadic Transfer).
        A high-SI system from domain A is injected into domain B if their
        triadic overlap is ≥ 30%. Population cap enforced after transfer.
        """
        all_schedulers = list(self.schedulers.values())
        for i, src in enumerate(all_schedulers):
            for j, tgt in enumerate(all_schedulers):
                if i == j:
                    continue
                similarity = self._structural_similarity(src.domain, tgt.domain)
                if similarity < 0.3:
                    continue

                donors = [s for s in src.population if s.triage_category() == "HIGH"]
                if not donors:
                    continue

                for donor in donors[:2]:
                    t_a = random.choice(tgt.domain.actions)
                    t_f = random.choice(tgt.domain.forms)
                    t_p = random.choice(tgt.domain.positions)
                    adapted = TriadicSystem(
                        domain_name    = tgt.domain.name,
                        action_label   = t_a[0],
                        form_label     = t_f[0],
                        position_label = t_p[0],
                        F = donor.F,
                        P = donor.P,
                        A = donor.A,
                        generation = donor.generation,
                    )
                    tgt.population.append(adapted)

                # Enforce population cap after transfer (§4.1)
                tgt._trim_population()

    @staticmethod
    def _structural_similarity(d1: Domain, d2: Domain) -> float:
        """
        Triadic Jaccard similarity — average of action/form/position overlap (§4.2).
        """
        def _jaccard(s1, s2):
            u = s1 | s2
            return len(s1 & s2) / len(u) if u else 0.0
        a_sim = _jaccard(set(a[0] for a in d1.actions),   set(a[0] for a in d2.actions))
        f_sim = _jaccard(set(f[0] for f in d1.forms),     set(f[0] for f in d2.forms))
        p_sim = _jaccard(set(p[0] for p in d1.positions), set(p[0] for p in d2.positions))
        return (a_sim + f_sim + p_sim) / 3.0

    def summary(self) -> Dict[str, Dict]:
        """Return final generation statistics per domain."""
        result = {}
        for name, sched in self.schedulers.items():
            best = sched.best(1)[0]
            result[name] = {
                "total_candidates": sched.domain.total_candidates(),
                "generations":      sched.generation,
                "best_SI":          best.SI,
                "best_system":      str(best),
                "mean_SI_final":    round(sched.si_history[-1], 4) if sched.si_history else 0,
                "si_trajectory":    sched.si_history,
            }
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# MONTE CARLO BASELINE
# ═══════════════════════════════════════════════════════════════════════════════

def monte_carlo_baseline(domain: Domain, n_samples: int = 200) -> float:
    """
    Random search baseline: sample N random (F, P, A) triples from the domain
    and return the mean SI. Used to verify that the Scheduler outperforms chance.
    """
    si_values = []
    for _ in range(n_samples):
        _, f = random.choice(domain.forms)
        _, p = random.choice(domain.positions)
        _, a = random.choice(domain.actions)
        noise = lambda s: max(0.01, min(1.0, s + random.uniform(-0.05, 0.05)))
        si_values.append(compute_si(noise(f), noise(p), noise(a))["SI"])
    return round(statistics.mean(si_values), 4)


# ═══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ═══════════════════════════════════════════════════════════════════════════════

def print_report(gsi: MultiDomainGSI, mc_baselines: Dict[str, float]):
    """Print a structured generation report."""
    print("\n" + "═" * 72)
    print("  GSI-RTD MULTI-DOMAIN REPORT — U-Theory v26")
    print("  SI = U/(1+δ)²   |   θ_stable=0.618   |   θ_critical=0.38")
    print("═" * 72)

    summary = gsi.summary()
    for domain_name, stats in summary.items():
        mc = mc_baselines.get(domain_name, 0)
        improvement = round((stats["mean_SI_final"] - mc) / max(mc, 0.001) * 100, 1)
        trend = " → ".join(
            f"{v:.3f}" for v in stats["si_trajectory"][::max(1, len(stats["si_trajectory"]) // 5)]
        )

        print(f"\n  ▶ DOMAIN: {domain_name}")
        print(f"    Candidates:       {stats['total_candidates']}")
        print(f"    Generations run:  {stats['generations']}")
        print(f"    Monte Carlo mean: {mc}")
        print(f"    GSI final SI:     {stats['mean_SI_final']}  (+{improvement}% vs random)")
        print(f"    Best SI:          {stats['best_SI']}")
        print(f"    Best system:      {stats['best_system']}")
        print(f"    SI trajectory:    {trend}")

    print("\n" + "─" * 72)
    print("  TRIAGE SUMMARY (all domains combined)")
    print("─" * 72)
    all_systems = []
    for sched in gsi.schedulers.values():
        all_systems.extend(sched.population)

    high = sum(1 for s in all_systems if s.triage_category() == "HIGH")
    mid  = sum(1 for s in all_systems if s.triage_category() == "MID")
    low  = sum(1 for s in all_systems if s.triage_category() == "LOW")
    total = max(len(all_systems), 1)

    print(f"  HIGH (SI ≥ {THETA_STABLE}): {high:4d}  ({high/total*100:.1f}%)")
    print(f"  MID  (SI ≥ {THETA_CRITICAL}): {mid:4d}  ({mid/total*100:.1f}%)")
    print(f"  LOW  (SI < {THETA_CRITICAL}): {low:4d}  ({low/total*100:.1f}%)")
    print("═" * 72 + "\n")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    random.seed(42)

    print("\nInitializing GSI-RTD Multi-Domain Prototype...")

    domains = [
        domain_email_marketing(),
        domain_publisher_outreach(),
        domain_content_creation(),
    ]

    # Monte Carlo baselines (random search, N=200)
    print("Running Monte Carlo baselines (N=200 per domain)...")
    mc_baselines = {d.name: monte_carlo_baseline(d, n_samples=200) for d in domains}

    # Run multi-domain GSI
    print(f"Running GSI Scheduler across {len(domains)} domains × 10 generations...")
    gsi = MultiDomainGSI(domains)
    gsi.run(generations=10, top_k=20)

    # Report
    print_report(gsi, mc_baselines)

    # Top 3 systems per domain
    print("  TOP 3 SYSTEMS PER DOMAIN:")
    print("─" * 72)
    for name, sched in gsi.schedulers.items():
        print(f"\n  {name}:")
        for i, s in enumerate(sched.best(3), 1):
            sc = s.scores
            print(f"    {i}. {s}")
            print(f"       F={s.F:.3f}  P={s.P:.3f}  A={s.A:.3f}  "
                  f"U={sc['U']:.3f}  δ={sc['delta']:.3f}  SI={sc['SI']:.3f}")
    print()
