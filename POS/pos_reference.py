# -*- coding: utf-8 -*-
"""
pos_reference.py — the Principle of Sequence as a plug-in commitment gate.  (v0.2)

Reference implementation of APPENDIX_POS v1.6 (§2.6, §2.6.1-2.6.5, §3.3, §9) and
APPENDIX_POS_ENGINE_PROFILE. Pure-Python, standard library only — so it drops into
any mathematical engine (RL / MPC / hierarchical planning / multi-agent /
discrete-event simulation) as a filter layer BETWEEN candidate selection and
irreversible execution, without touching the discovery / optimization loop.

POS answers one question: given readiness estimates (with uncertainty) and an
action's irreversibility AND exposure, MAY this action be committed now?  It is a
gate, not an optimizer, and it NEVER authorizes a values-forbidden action.

v0.2 (spec-conformance fixes, per external review):
  * probe branch now requires BOTH kappa<=kappa_probe AND exposure<=exposure_cap
    (a low-kappa but high-exposure move is NOT a free probe).
  * emergency branch now REQUIRES emergency_log_complete=True (the log is enforced,
    not merely labelled).
  * input validation: Pillar/Action reject out-of-range, negative-SE, NaN, or
    inverted loss intervals instead of silently producing wrong verdicts.
  * gate reads PER-PILLAR (scalar) LCBs — SCALAR_LCB mode, NOT a joint bound.

Epistemic status: L2/B2 candidate operationalization — a runnable specification,
NOT a validated law and NOT a theorem of U = cbrt(F*P*A). Thresholds, coefficients,
confidence rules and loss scales require per-domain calibration (POS-P1/P2).

Research use only. (c) 2026 Petar Nikolov, MIT.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from math import log, sqrt, isfinite
from typing import Optional, Tuple, List


# ---------------------------------------------------------------------------
# Inverse standard-normal CDF (Acklam) — lets alpha(s) work without SciPy/NumPy
# ---------------------------------------------------------------------------
_A = (-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
      1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00)
_B = (-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
      6.680131188771972e+01, -1.328068155288572e+01)
_C = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
      -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00)
_D = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
      3.754408661907416e+00)

def _norm_ppf(p: float) -> float:
    """Inverse CDF of the standard normal (Acklam's rational approximation)."""
    if not (0.0 < p < 1.0):
        raise ValueError("p must be in (0,1)")
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = sqrt(-2 * log(p))
        return (((((_C[0]*q+_C[1])*q+_C[2])*q+_C[3])*q+_C[4])*q+_C[5]) / \
               ((((_D[0]*q+_D[1])*q+_D[2])*q+_D[3])*q+1)
    if p <= phigh:
        q = p - 0.5; r = q*q
        return (((((_A[0]*r+_A[1])*r+_A[2])*r+_A[3])*r+_A[4])*r+_A[5])*q / \
               (((((_B[0]*r+_B[1])*r+_B[2])*r+_B[3])*r+_B[4])*r+1)
    q = sqrt(-2 * log(1 - p))
    return -(((((_C[0]*q+_C[1])*q+_C[2])*q+_C[3])*q+_C[4])*q+_C[5]) / \
            ((((_D[0]*q+_D[1])*q+_D[2])*q+_D[3])*q+1)

def z_lower(alpha: float) -> float:
    """z_{1-alpha}: multiplier for a one-sided lower confidence bound."""
    return _norm_ppf(1.0 - alpha)


def clip01(x: float) -> float:
    return max(0.0, min(1.0, x))

def _unit(name: str, v: float) -> None:
    if not isfinite(v) or not (0.0 <= v <= 1.0):
        raise ValueError("%s must be finite and in [0,1], got %r" % (name, v))


# ---------------------------------------------------------------------------
# Data model  (with input validation — v0.2)
# ---------------------------------------------------------------------------
@dataclass
class Pillar:
    """A readiness estimate in [0,1] with a standard error (uncertainty-aware)."""
    mean: float
    se: float = 0.0
    def __post_init__(self):
        _unit("Pillar.mean", self.mean)
        if not isfinite(self.se) or self.se < 0.0:
            raise ValueError("Pillar.se must be finite and >= 0, got %r" % (self.se,))

@dataclass
class Action:
    name: str
    kappa: float                 # irreversibility in [0,1]  (0 reversible probe, 1 hard commit)
    exposure: float = 0.0        # normalized exposure e(a) in [0,1]
    stakes: float = 0.0          # normalized stakes s(a) in [0,1]
    domain: str = "generic"
    firewall_pass: bool = True   # values-firewall verdict (False = ethically/legally barred)
    is_emergency: bool = False
    emergency_log_complete: bool = False   # v0.2: the emergency branch ENFORCES this (LogComplete=1)
    # expected loss as (LCB, UCB) tuples, on ONE common loss scale:
    L_action: Optional[Tuple[float, float]] = None
    L_inaction: Optional[Tuple[float, float]] = None
    def __post_init__(self):
        for n, v in (("Action.kappa", self.kappa), ("Action.exposure", self.exposure),
                     ("Action.stakes", self.stakes)):
            _unit(n, v)
        for lname, L in (("L_action", self.L_action), ("L_inaction", self.L_inaction)):
            if L is not None:
                lo, hi = L
                if not (isfinite(lo) and isfinite(hi)) or lo > hi:
                    raise ValueError("%s must be a finite (LCB<=UCB) tuple, got %r" % (lname, L))

@dataclass
class ThetaModel:
    """theta_i(a,d,s) = clip[ theta0_i(d) + beta*kappa + gamma*e + eta*s ] — §2.6.3.
    A CALIBRATION CANDIDATE (illustrative coefficients), not a validated law."""
    theta0_F: float = 0.60
    theta0_P: float = 0.50
    beta: float = 0.10       # weight on kappa   (illustrative — calibrate per domain, POS-P1)
    gamma: float = 0.05      # weight on exposure
    eta: float = 0.10        # weight on stakes
    def theta_F(self, a: Action) -> float:
        return clip01(self.theta0_F + self.beta*a.kappa + self.gamma*a.exposure + self.eta*a.stakes)
    def theta_P(self, a: Action) -> float:
        return clip01(self.theta0_P + self.beta*a.kappa + self.gamma*a.exposure + self.eta*a.stakes)

@dataclass
class PosConfig:
    theta: ThetaModel = field(default_factory=ThetaModel)
    kappa_probe: float = 0.15          # <= this AND exposure<=exposure_cap = an ungated reversible probe/prep
    exposure_cap: float = 0.20         # v0.2: probe branch also requires e <= exposure_cap
    alpha0: float = 0.10               # base one-sided miss rate
    alpha_stakes_slope: float = 0.09   # alpha(s) = alpha0 - slope*s  (more conservative at high stakes)
    def alpha(self, a: Action) -> float:
        return max(0.005, self.alpha0 - self.alpha_stakes_slope * a.stakes)


# ---------------------------------------------------------------------------
# Readiness metrics (§2.6, §2.6.1) — SCALAR_LCB mode (per-pillar, NOT a joint bound)
# ---------------------------------------------------------------------------
def lcb(p: Pillar, alpha: float) -> float:
    return clip01(p.mean - z_lower(alpha) * p.se)

def readiness(F: Pillar, P: Pillar, a: Action, cfg: PosConfig) -> dict:
    al = cfg.alpha(a)
    F_lcb, P_lcb = lcb(F, al), lcb(P, al)
    thF, thP = cfg.theta.theta_F(a), cfg.theta.theta_P(a)
    rF = F_lcb / thF if thF > 0 else float("inf")
    rP = P_lcb / thP if thP > 0 else float("inf")
    R = min(rF, rP)
    mF, mP = rF - 1.0, rP - 1.0
    return dict(alpha=al, coverage="SCALAR_LCB(per-pillar)", F_lcb=F_lcb, P_lcb=P_lcb, thF=thF, thP=thP,
                R=R, mF=mF, mP=mP, mR=R - 1.0,
                bottleneck=("F" if mF <= mP else "P"))

def emergency_margin(a: Action) -> Optional[float]:
    """M_emg = LCB[L(inaction)] - UCB[L(action)]  — §2.6.5 (robust)."""
    if not a.L_inaction or not a.L_action:
        return None
    return a.L_inaction[0] - a.L_action[1]

def violation_severity(a: Action, R: float) -> float:
    """V_POS = s * kappa * [1 - R]_+  — §2.6.4 (audit, not a gate)."""
    return a.stakes * a.kappa * max(0.0, 1.0 - R)


# ---------------------------------------------------------------------------
# THE GATE (§2.6 authorization predicate) — the faithful formal predicate.
# NOTE: high kappa does NOT auto-authorize; a hard commit REQUIRES R >= 1.
# Probe needs kappa<=kappa_probe AND exposure<=exposure_cap; emergency needs a log.
# ---------------------------------------------------------------------------
def pos_gate(F: Pillar, P: Pillar, a: Action, cfg: Optional[PosConfig] = None):
    """Return (authorized: bool, reason: str, diagnostics: dict)."""
    cfg = cfg or PosConfig()
    d = readiness(F, P, a, cfg)
    d["V_POS"] = violation_severity(a, d["R"])
    d["M_emg"] = emergency_margin(a)

    if not a.firewall_pass:                                     # values-firewall dominates everything
        return False, "values_forbidden", d
    if a.kappa <= cfg.kappa_probe and a.exposure <= cfg.exposure_cap:   # reversible AND capped-exposure probe/prep
        return True, "probe_or_prep", d
    if d["R"] >= 1.0:                                           # prepared -> commit
        return True, "ready_commit", d
    if (a.is_emergency and d["M_emg"] is not None and d["M_emg"] > 0.0
            and a.emergency_log_complete):                      # robust emergency AND log enforced
        return True, "emergency_forced_move", d
    return False, "forbidden_action", d        # unprepared + irreversible = the Forbidden Action


# ---------------------------------------------------------------------------
# Base-burning (§3.2, §3.3) and verification economics (§4.1)
# ---------------------------------------------------------------------------
def base_burn(F: float, F_next: float, P: float, P_next: float,
              wF: float = 0.5, wP: float = 0.5) -> float:
    return wF * max(0.0, F - F_next) + wP * max(0.0, P - P_next)

def persistent_burn(F_series: List[float], P_series: List[float],
                    wF: float = 0.5, wP: float = 0.5, gamma: float = 0.9) -> float:
    F0, P0 = F_series[0], P_series[0]
    return sum((gamma ** (h - 1)) * (wF * max(0.0, F0 - F_series[h]) + wP * max(0.0, P0 - P_series[h]))
               for h in range(1, len(F_series)))

def verification_cost(cF: float, cP: float, pF: float, pP: float,
                      c_invalid: float = 0.0, q_P_given_notF: float = 0.0):
    """Return (C_F->P, C_P->F, F_first_preferred)  — §4.1."""
    C_FP = cF + pF * cP
    C_PF = cP + pP * cF + c_invalid * q_P_given_notF
    return C_FP, C_PF, (C_FP <= C_PF)


# ---------------------------------------------------------------------------
# Reward shaping helper for RL engines (§10): r' = r + lU*U - lB*B - lV*V_POS
# ---------------------------------------------------------------------------
def shaped_reward(base_reward: float, U: float, B: float, V_POS: float,
                  lU: float = 1.0, lB: float = 1.0, lV: float = 1.0) -> float:
    return base_reward + lU * U - lB * B - lV * V_POS


if __name__ == "__main__":
    cfg = PosConfig()

    print("=== POS gate — the same decisive action, different readiness ===")
    scenarios = [
        ("athlete: peak form, final race (commit)",
         Pillar(0.90, 0.03), Pillar(0.80, 0.04),
         Action("race", kappa=0.85, exposure=0.7, stakes=0.8)),
        ("athlete: unrecovered, same race (commit)",
         Pillar(0.45, 0.06), Pillar(0.80, 0.04),
         Action("race", kappa=0.85, exposure=0.7, stakes=0.8)),
        ("startup: cheap market probe (reversible, capped)",
         Pillar(0.40, 0.08), Pillar(0.35, 0.08),
         Action("A/B pilot", kappa=0.10, exposure=0.1, stakes=0.3)),
        ("low-kappa BUT over exposure cap (not a free probe)",
         Pillar(0.40, 0.08), Pillar(0.35, 0.08),
         Action("big reversible bet", kappa=0.10, exposure=0.9, stakes=0.5)),
        ("reform: unready base, delay worse, log complete (emergency)",
         Pillar(0.50, 0.06), Pillar(0.45, 0.06),
         Action("emergency reform", kappa=0.80, exposure=0.6, stakes=0.9,
                is_emergency=True, emergency_log_complete=True,
                L_action=(0.30, 0.45), L_inaction=(0.70, 0.90))),
        ("same emergency BUT log NOT complete",
         Pillar(0.50, 0.06), Pillar(0.45, 0.06),
         Action("emergency reform (unlogged)", kappa=0.80, exposure=0.6, stakes=0.9,
                is_emergency=True, emergency_log_complete=False,
                L_action=(0.30, 0.45), L_inaction=(0.70, 0.90))),
        ("weaponization request (values-forbidden)",
         Pillar(0.95, 0.01), Pillar(0.95, 0.01),
         Action("prohibited", kappa=0.9, stakes=1.0, firewall_pass=False)),
    ]
    for label, F, P, a in scenarios:
        ok, reason, d = pos_gate(F, P, a, cfg)
        print("  %-54s -> %-26s  R=%.2f  V_POS=%.2f  bottleneck=%s"
              % (label, ("AUTHORIZE:" + reason) if ok else ("WITHHOLD:" + reason),
                 d["R"], d["V_POS"], d["bottleneck"]))

    print("\n=== verification economics (§4.1): check the cheap/high-reject gate first ===")
    C_FP, C_PF, f_first = verification_cost(cF=1.0, cP=5.0, pF=0.6, pP=0.9)
    print("  C(F->P)=%.2f  C(P->F)=%.2f  ->  %s" % (C_FP, C_PF, "F-first preferred" if f_first else "P-first preferred"))

    print("\n=== base burn: premature commit degrades the base vs a recovering probe ===")
    burn_commit = persistent_burn([0.90, 0.55, 0.50, 0.50], [0.80, 0.60, 0.55, 0.55])
    burn_probe  = persistent_burn([0.90, 0.86, 0.90, 0.92], [0.80, 0.79, 0.82, 0.83])
    print("  B_H(premature commit)=%.3f   B_H(reversible probe)=%.3f" % (burn_commit, burn_probe))

    print("\n=== z_lower sanity: alpha=0.05 -> %.4f , alpha=0.025 -> %.4f (expect 1.6449, 1.9600)"
          % (z_lower(0.05), z_lower(0.025)))
