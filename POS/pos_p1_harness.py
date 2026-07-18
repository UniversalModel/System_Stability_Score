# -*- coding: utf-8 -*-
"""
pos_p1_harness.py — a runnable POS-P1 calibration / falsification harness.  (v0.1)

POS-P1 asks the decisive question the appendix defers: DOES readiness-gated
commitment beat ungated / alternative-ordered baselines at EQUAL budget, on an
EXTERNAL outcome?  This module runs that experiment on *synthetic* benchmark
environments with FROZEN baselines and reports PASS / INCONCLUSIVE / KILL bands.

HONESTY (load-bearing):
  * SYNTHETIC, not real-world. A "PASS" here means: IF the world behaves like the
    modelled environment (premature commitment risks a costly failure and the
    signal is noisy), THEN gating pays. It is NOT external validation on real data;
    it is the harness POS-P1 needs, ready to be pointed at real/simulated datasets.
  * The environments are NOT rigged for POS. In the "burn" regime the gate should
    help; in the "cheap-failure / costly-delay" regime an eager policy may WIN and
    POS may lose or tie. A harness that always favoured POS would be worthless.
  * External outcome only (net payoff), equal budget (same horizon), paired draws
    (every policy faces the identical environment randomness), bootstrap CI on the
    POS-minus-best-baseline difference.

Pure-Python stdlib. Research use only. (c) 2026 Petar Nikolov, MIT.
"""
import sys, os, random, statistics
from dataclasses import dataclass, field
from typing import List, Dict, Callable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pos_reference import Pillar, Action, PosConfig, ThetaModel, pos_gate, clip01


# ---------------------------------------------------------------------------
# Synthetic environment
# ---------------------------------------------------------------------------
@dataclass
class Regime:
    name: str
    V: float            # payoff of a successful commit
    L: float            # loss of a failed commit (the "base burn" cost)
    slope: float        # how sharply P(success) rises with true readiness above theta_true
    theta_true: float   # true readiness at which P(success)=0.5
    prep_gain: float    # true-pillar improvement per a^prep step
    prep_cost: float    # cost per a^prep step
    delay_cost: float   # cost per period waited (guards against paralysis)
    noise_se: float     # observation noise on F,P estimates
    T: int              # horizon = equal budget (max periods)
    f0: float           # mean initial (unready) Form
    p0: float           # mean initial (unready) Position

def make_draw(reg: Regime, rng: random.Random) -> Dict:
    return dict(
        F0=clip01(rng.gauss(reg.f0, 0.03)),
        P0=clip01(rng.gauss(reg.p0, 0.03)),
        nF=[rng.gauss(0.0, reg.noise_se) for _ in range(reg.T)],
        nP=[rng.gauss(0.0, reg.noise_se) for _ in range(reg.T)],
        u=[rng.random() for _ in range(reg.T)],   # commit-outcome coin per period
        r=[rng.random() for _ in range(reg.T)],   # for the random policy
    )

def run_episode(policy: Callable, reg: Regime, draw: Dict) -> float:
    """Run one policy on ONE fixed environment draw; return net external payoff."""
    F, P = draw["F0"], draw["P0"]
    preps = 0
    for t in range(reg.T):
        Fhat = clip01(F + draw["nF"][t])
        Phat = clip01(P + draw["nP"][t])
        act = policy(Fhat, Phat, t, reg, draw)
        if act == "commit":
            q = min(F, P)                                   # TRUE readiness governs the outcome
            p_succ = clip01(0.5 + reg.slope * (q - reg.theta_true))
            outcome = reg.V if draw["u"][t] < p_succ else -reg.L
            return outcome - reg.prep_cost * preps - reg.delay_cost * t
        elif act == "prep":                                 # a^prep raises the weaker (estimated) pillar
            if Fhat <= Phat: F = clip01(F + reg.prep_gain)
            else:            P = clip01(P + reg.prep_gain)
            preps += 1
        # else: wait
    return 0.0 - reg.prep_cost * preps - reg.delay_cost * reg.T   # never committed = opportunity cost


# ---------------------------------------------------------------------------
# Frozen baselines + POS (all share prep routing; they differ in WHEN to commit)
# ---------------------------------------------------------------------------
TH = 0.60   # the fixed commit threshold the non-LCB baselines and the POS gate share

def pol_ungated(Fh, Ph, t, reg, draw):            # action-first: commit immediately
    return "commit"

def make_etc(k):                                  # explore-then-commit: prep k periods, then commit
    def p(Fh, Ph, t, reg, draw): return "commit" if t >= k else "prep"
    return p

def pol_thresholds_no_lcb(Fh, Ph, t, reg, draw):  # commit on POINT estimates >= TH (no LCB, no veto)
    return "commit" if min(Fh, Ph) >= TH else "prep"

def pol_random(Fh, Ph, t, reg, draw):             # random commit/prep
    return "commit" if draw["r"][t] < 0.25 else "prep"

_POS_CFG = PosConfig(theta=ThetaModel(theta0_F=TH, theta0_P=TH, beta=0.0, gamma=0.0, eta=0.0),
                     kappa_probe=0.15, exposure_cap=0.20)
def pol_pos(Fh, Ph, t, reg, draw):                # POS: prep until the LCB gate authorizes the commit
    a = Action("commit", kappa=0.90, exposure=0.50, stakes=0.70)
    # give the gate this regime's known observation noise as the SE it reasons on:
    ok, why, _ = pos_gate(Pillar(Fh, reg.noise_se), Pillar(Ph, reg.noise_se), a, _POS_CFG)
    return "commit" if (ok and why == "ready_commit") else "prep"

BASELINES = {
    "ungated(action-first)": pol_ungated,
    "explore-then-commit(4)": make_etc(4),
    "thresholds-no-LCB":     pol_thresholds_no_lcb,
    "random":                pol_random,
}
POS = ("POS (LCB-gated)", pol_pos)


# ---------------------------------------------------------------------------
# Experiment + bootstrap verdict
# ---------------------------------------------------------------------------
def bootstrap_ci(diffs: List[float], n_boot: int, rng: random.Random, lo=2.5, hi=97.5):
    n = len(diffs)
    means = []
    for _ in range(n_boot):
        s = sum(diffs[rng.randrange(n)] for _ in range(n)) / n
        means.append(s)
    means.sort()
    return means[int(lo/100*n_boot)], means[int(hi/100*n_boot)]

def run_regime(reg: Regime, n_episodes=4000, n_boot=1000, delta_min=0.02, master_seed=20260718):
    gen = random.Random(master_seed)
    draws = [make_draw(reg, gen) for _ in range(n_episodes)]
    payoffs = {name: [run_episode(pol, reg, d) for d in draws] for name, pol in BASELINES.items()}
    payoffs[POS[0]] = [run_episode(POS[1], reg, d) for d in draws]

    means = {name: statistics.mean(v) for name, v in payoffs.items()}
    best_base = max(BASELINES, key=lambda nm: means[nm])            # POS must beat the BEST baseline
    diffs = [payoffs[POS[0]][i] - payoffs[best_base][i] for i in range(n_episodes)]
    eff = statistics.mean(diffs)
    lcb, ucb = bootstrap_ci(diffs, n_boot, random.Random(master_seed + 1))
    verdict = "PASS" if lcb > delta_min else ("KILL" if ucb < 0.0 else "INCONCLUSIVE")

    print("\n=== Regime: %s  (V=%.2f L=%.2f delay=%.3f noise_se=%.2f theta_true=%.2f) ==="
          % (reg.name, reg.V, reg.L, reg.delay_cost, reg.noise_se, reg.theta_true))
    for name in list(BASELINES) + [POS[0]]:
        star = "  <- best baseline" if name == best_base else ("  <- POS" if name == POS[0] else "")
        print("   %-26s mean payoff = %+.4f%s" % (name, means[name], star))
    print("   POS − best baseline (%s):  effect = %+.4f   95%% CI [%+.4f, %+.4f]   Δ_min=%.02f"
          % (best_base, eff, lcb, ucb, delta_min))
    print("   >>> POS-P1 VERDICT (synthetic, this regime): %s" % verdict)
    return verdict


if __name__ == "__main__":
    burn = Regime("BURN (premature commit is costly, signal noisy)",
                  V=1.0, L=3.0, slope=3.0, theta_true=0.65,
                  prep_gain=0.08, prep_cost=0.03, delay_cost=0.010, noise_se=0.06, T=15, f0=0.40, p0=0.45)
    cheap = Regime("CHEAP-FAILURE / COSTLY-DELAY (eagerness should win)",
                   V=1.0, L=0.30, slope=3.0, theta_true=0.55,
                   prep_gain=0.08, prep_cost=0.06, delay_cost=0.090, noise_se=0.06, T=15, f0=0.45, p0=0.50)

    print("POS-P1 harness — SYNTHETIC benchmark. A PASS is conditional on the model, NOT real-world validation.")
    v1 = run_regime(burn)
    v2 = run_regime(cheap)

    print("""
--- HONEST READING ---
* If BURN=PASS and CHEAP=KILL/INCONCLUSIVE, the harness DISCRIMINATES: gating pays exactly when
  premature commitment is costly and the signal is noisy, and does NOT pay when failure is cheap
  and delay is expensive. That conditional result is the honest B2/L2 finding — not "POS always wins".
* This is the executable POS-P1 apparatus. Real validation = point it at real or high-fidelity
  simulated datasets, freeze the baselines and Δ_min in a public pre-registration, and report the
  same PASS/INCONCLUSIVE/KILL bands on EXTERNAL outcomes. Until then: L2/B2 scaffolding, RUO.
""")
