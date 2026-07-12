# -*- coding: utf-8 -*-
"""
tra_gsm_reference.py — reference implementation of the TRA Gaussian Stability Matrix (GSM).

APPENDIX_TRA §11. Turns the point keystone U = (F·P·A)^(1/3) into a *distribution*:
the three pillar probabilities are modelled as correlated log-odds (multivariate normal),
so that when pillars are coupled (POGO / slosh / aeroservoelasticity), the uncertainty
in U widens and its lower tail drops — the honest risk picture a scalar U hides.

  F,P,A  = pillar requirement-satisfaction probabilities in (0,1), awaiting empirical calibration
  z      = logit(p),  z ~ N(mu, Sigma),  Sigma = D R D
  R      = correlation matrix; off-diagonals = rho = m(Lambda), a monotone MAPPING of the measured
           TRA-P0 leakage -- a modelling choice, NOT an identity (Lambda is unsigned distance-
           dependence; rho is a signed Gaussian correlation). Under-determined -> bounds / fail-closed.
  U      = (pF pP pA)^(1/3) per sample -> credible interval + P(U >= threshold).
           NOTE: U is a normalized geometric-mean INDEX of the joint survival prob pF*pP*pA
           (exact only under independence); it is NOT itself a survival probability.

Research use only. A diagnostic / risk-visualisation object, never a control law. © 2026 Petar Nikolov, MIT.
"""
import numpy as np

def logit(p):     return np.log(p / (1.0 - p))
def sigmoid(z):   return 1.0 / (1.0 + np.exp(-z))

def gsm_u(F, P, A, sd=(0.15, 0.15, 0.15), R=None, rho=0.1,
          n=400_000, seed=0, thr=0.75):
    """Return the GSM distribution of U for pillar probabilities (F,P,A).
    R: 3x3 correlation matrix; if None, an equicorrelation matrix with off-diagonal `rho` is used."""
    rng = np.random.default_rng(seed)
    mu = logit(np.clip(np.array([F, P, A], float), 1e-4, 1 - 1e-4))
    D = np.diag(sd)
    if R is None:
        R = np.array([[1, rho, rho], [rho, 1, rho], [rho, rho, 1]], float)
    Sigma = D @ R @ D
    Z = rng.multivariate_normal(mu, Sigma, size=n)
    p = sigmoid(Z)
    U = np.cbrt(p[:, 0] * p[:, 1] * p[:, 2])
    lo, hi = np.percentile(U, [5, 95])
    return dict(meanU=float(U.mean()), lo=float(lo), hi=float(hi),
                width=float(hi - lo), p_above=float((U >= thr).mean()),
                pi_star=("F", "P", "A")[int(np.argmin([F, P, A]))])

def show(tag, F, P, A, **kw):
    r = gsm_u(F, P, A, **kw)
    pt = (F * P * A) ** (1 / 3)
    print("%-34s pointU=%.3f  meanU=%.3f  90%%CI[%.3f-%.3f] width=%.3f  P(U>=0.75)=%.0f%%  pi*=%s"
          % (tag, pt, r["meanU"], r["lo"], r["hi"], r["width"], 100 * r["p_above"], r["pi_star"]))

if __name__ == "__main__":
    print("=== GSM demo: coupling widens the U distribution and drops the lower tail ===\n")
    print("Scenario 1 — good overall state  F=0.90 P=0.85 A=0.88")
    show("  low coupling  (rho=0.10)", 0.90, 0.85, 0.88, rho=0.10, seed=1)
    show("  high coupling (rho=0.65)", 0.90, 0.85, 0.88, rho=0.65, seed=1)
    print("\nScenario 2 — imbalanced (one weak pillar)  F=0.90 P=0.55 A=0.90")
    show("  low coupling  (rho=0.10)", 0.90, 0.55, 0.90, rho=0.10, seed=2)
    show("  high coupling (rho=0.65)", 0.90, 0.55, 0.90, rho=0.65, seed=2)

    print("\n=== Starship-class phase profile (ILLUSTRATIVE pillar inputs; the U-math is real) ===")
    print("decision rule: PASS a phase iff P(U >= 0.75) >= 0.90  (a distributional gate, not a scalar)\n")
    # phase: (F, P, A, dominant coupling off-diagonals)
    def Rmat(fp, fa, pa): return np.array([[1, fp, fa], [fp, 1, pa], [fa, pa, 1]], float)
    phases = [
        ("Ascent (nominal)",      0.92, 0.90, 0.88, Rmat(0.15, 0.15, 0.15)),
        ("Max-Q (F<->P aeroel.)", 0.80, 0.76, 0.93, Rmat(0.60, 0.20, 0.25)),  # airframe x Q-alpha
        ("Staging (all coupled)", 0.85, 0.82, 0.80, Rmat(0.45, 0.45, 0.45)),
        ("Landing burn (A<->P)",  0.90, 0.72, 0.70, Rmat(0.20, 0.25, 0.62)),  # throttle x reachable set
    ]
    for name, F, P, A, R in phases:
        r = gsm_u(F, P, A, R=R, seed=7)
        gate = "PASS" if r["p_above"] >= 0.90 else "FLAG"
        pt = (F * P * A) ** (1 / 3)
        print("%-24s pointU=%.3f meanU=%.3f 90%%CI[%.3f-%.3f] P(U>=0.75)=%3.0f%% pi*=%s  -> %s"
              % (name, pt, r["meanU"], r["lo"], r["hi"], 100 * r["p_above"], r["pi_star"], gate))
