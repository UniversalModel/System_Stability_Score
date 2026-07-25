#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pmd_scale_sensitivity.py — reproducibility script for APPENDIX_PMD §16.1 (PMD-11).

Regenerates every numerical figure quoted in the reference-scale-invariance section,
plus the PMD-2R violation factor and the PMD-10 mass-elasticity check.

The EXPLICIT COUNTEREXAMPLES are proofs (a single rank reversal settles the negative
result). The PERCENTAGES are illustrative Monte-Carlo figures that depend on the
sampling design declared below -- they are not theorems and must not be quoted
outside this design.

Author: Petar Nikolov (ORCID 0009-0001-8669-2276).  License: MIT.
Pure standard library. Run:  python pmd_scale_sensitivity.py
"""
import math
import random

# ---------------------------------------------------------------- design ----
ALPHA   = 2.0                                   # P_M = x^alpha/(1+x^alpha)
ETA     = 0.5                                   # adapter weight, 0 < eta < 1
LOGIT_R = (-6.0, 6.0)                           # base log-odds sampling range
PS_R    = (0.05, 0.95)                          # P_S sampling range
LAMBDAS = [1e-3, 1e-2, 1e-1, 1e1, 1e2, 1e3]     # reference-scale sweep L* -> lambda L*
NDRAWS  = 20000

def sigma(t):   return 1.0 / (1.0 + math.exp(-t))
def logit(p):   return math.log(p / (1.0 - p))


# ------------------------------------------------------------ the meters ----
def P_L_geometric(lD, lM, c, eta=ETA, alpha=ALPHA):
    """Canonical adapter: squash THEN blend.  c = ln(lambda).
    logit P_D shifts by 2c ; logit P_M shifts by alpha*c."""
    return sigma(lD + 2.0 * c) ** (1.0 - eta) * sigma(lM + alpha * c) ** eta

def P_L_logit(lD, lM, c, eta=ETA, alpha=ALPHA):
    """Rival adapter (reinstated in v1.5.2): blend THEN squash."""
    return sigma((1.0 - eta) * (lD + 2.0 * c) + eta * (lM + alpha * c))

def score(pS, lD, lM, c, adapter=P_L_geometric):
    """P = sqrt(P_S * P_L).  P_S carries no L* dependence."""
    return math.sqrt(pS * adapter(lD, lM, c))


# ------------------------------------------------- 1. explicit reversal ------
def explicit_counterexample():
    """PROOF, not statistics: rank reversal with EQUAL logit shifts (alpha = 2)."""
    print("1. EXPLICIT COUNTEREXAMPLE (alpha=2 -> both logits shift equally; P_S = 1)")
    A, B = (0.0, 0.0), (-2.0, 3.0)
    print("   A=(l_D,l_M)=(0,0)   B=(-2,+3)")
    for Ls in (0.01, 0.10, 1.00, 10.0):
        c = math.log(Ls)
        a, b = score(1.0, *A, c=c), score(1.0, *B, c=c)
        print("     L*=%6.2f  P(A)=%.6f  P(B)=%.6f  winner=%s" %
              (Ls, a, b, "A" if a > b else "B"))
    print("   -> ranking depends on L*: geometric aggregation is NOT scale-invariant.\n")


# ------------------------------------- 2. dominance vs trade-off (seeded) ----
def dominance_split(seed=3, n=NDRAWS):
    """Dominance is SUFFICIENT for robustness. It is NOT necessary."""
    print("2. DOMINANCE vs TRADE-OFF  (seed=%d, n=%d)" % (seed, n))
    rng = random.Random(seed)
    dom_f = dom_n = tr_f = tr_n = 0
    for _ in range(n):
        A = (rng.uniform(*LOGIT_R), rng.uniform(*LOGIT_R))
        B = (rng.uniform(*LOGIT_R), rng.uniform(*LOGIT_R))
        pSA, pSB = rng.uniform(*PS_R), rng.uniform(*PS_R)
        dominant = ((A[0] >= B[0] and A[1] >= B[1] and pSA >= pSB) or
                    (B[0] >= A[0] and B[1] >= A[1] and pSB >= pSA))
        base = score(pSA, *A, c=0.0) - score(pSB, *B, c=0.0)
        flip = any(base * (score(pSA, *A, c=math.log(l)) -
                           score(pSB, *B, c=math.log(l))) < 0 for l in LAMBDAS)
        if dominant: dom_n += 1; dom_f += flip
        else:        tr_n  += 1; tr_f  += flip
    print("   dominance pairs : %5d flips / %5d  (%.2f%%)  <- provably 0" %
          (dom_f, dom_n, 100.0 * dom_f / max(dom_n, 1)))
    print("   trade-off pairs : %5d flips / %5d  (%.1f%%)  -> %.1f%% STABLE" %
          (tr_f, tr_n, 100.0 * tr_f / max(tr_n, 1),
           100.0 * (tr_n - tr_f) / max(tr_n, 1)))
    print("   -> dominance is SUFFICIENT, not NECESSARY: many trade-off pairs are stable.\n")


# ------------------------------------- 3. the logit adapter is invariant -----
def logit_adapter_invariance(seed=7, n=4000):
    print("3. LOGIT-INSIDE ADAPTER: exact rank invariance (seed=%d, n=%d)" % (seed, n))
    rng = random.Random(seed)
    flips = 0
    for _ in range(n):
        A = (rng.uniform(*LOGIT_R), rng.uniform(*LOGIT_R))
        B = (rng.uniform(*LOGIT_R), rng.uniform(*LOGIT_R))
        base = P_L_logit(*A, c=0.0) - P_L_logit(*B, c=0.0)
        if any(base * (P_L_logit(*A, c=math.log(l)) -
                       P_L_logit(*B, c=math.log(l))) < 0 for l in LAMBDAS):
            flips += 1
    print("   rank flips: %d / %d   (logit P_L shifts uniformly by [(1-eta)2 + eta*alpha]ln(lam))\n"
          % (flips, n))


# ------------------------------- 4. top-level elasticity is 1/6 either way ---
def top_level_elasticity():
    print("4. TOP-LEVEL ELASTICITY  dlnU/dlnP_S  (U = (F A)^(1/3) (P_S P_L)^(1/6))")
    h = 1e-7
    for pS, lD, lM in ((0.6, 0.4, -0.8), (0.9, 2.0, 1.0), (0.2, -1.5, 0.7)):
        row = []
        for name, ad in (("geometric", P_L_geometric), ("logit-inside", P_L_logit)):
            f = lambda s: (s * ad(lD, lM, 0.0)) ** (1.0 / 6.0)
            row.append("%s=%.8f" % (name, (math.log(f(pS * (1 + h))) - math.log(f(pS)))
                                    / math.log(1 + h)))
        print("   P_S=%.1f  %s   (1/6 = %.8f)" % (pS, "  ".join(row), 1.0 / 6.0))
    print("   -> Position keeps its 1/3 share and P_S its 1/6 elasticity for BOTH adapters.\n")


# ------------------------------------- 5. PMD-2R violation factor -----------
def pmd2r_violation():
    print("5. PMD-2R: F_Q / (8m<E_kin>/hbar^2) for the state (|+p>+|-p>)/sqrt(2)")
    print("   closed form = (sqrt(1+xi^2)+1)/2 ,  xi = p/(mc)")
    for xi in (0.01, 0.1, 1.0, 10.0, 100.0):
        s = math.sqrt(1 + xi * xi)
        direct = xi * xi / (2.0 * (s - 1.0))
        print("     xi=%8.2f  direct=%12.6f  closed=%12.6f" % (xi, direct, (s + 1) / 2))
    print("   -> > 1 for every xi > 0: 8mK/hbar^2 is NOT a relativistic ceiling.\n")


# ------------------------------------- 6. mass elasticity of the adapter ----
def mass_elasticity():
    print("6. PMD-10: mass elasticity of P_L   (correct = (1-eta)s_D + eta*alpha*(1-P_M))")
    h = 1e-7
    P_M = lambda m: m ** ALPHA / (1 + m ** ALPHA)
    P_D = lambda m: sigma(0.4 * math.log(m) + 0.3)          # arbitrary smooth example
    P_L = lambda m: P_D(m) ** (1 - ETA) * P_M(m) ** ETA
    dln = lambda f, m: (math.log(f(m * (1 + h))) - math.log(f(m))) / math.log(1 + h)
    for m in (0.3, 1.0, 3.0):
        true_, sD, sM = dln(P_L, m), dln(P_D, m), dln(P_M, m)
        print("   m=%.1f true=%.6f | (1-eta)sD+eta*sM=%.6f | withdrawn eta+(1-eta)sD=%.6f | "
              "sM=%.6f == alpha(1-P_M)=%.6f"
              % (m, true_, (1 - ETA) * sD + ETA * sM, ETA + (1 - ETA) * sD,
                 sM, ALPHA * (1 - P_M(m))))
    print("   -> the withdrawn formula is wrong except where alpha(1-P_M)=1.\n")


if __name__ == "__main__":
    print("=" * 74)
    print("PMD scale-sensitivity / elasticity reproduction  (appendix v1.5.2)")
    print("design: logits ~ U(%.0f,%.0f), P_S ~ U(%.2f,%.2f), alpha=%.0f, eta=%.1f"
          % (LOGIT_R[0], LOGIT_R[1], PS_R[0], PS_R[1], ALPHA, ETA))
    print("        lambda sweep = %s ; n = %d" % (LAMBDAS, NDRAWS))
    print("=" * 74 + "\n")
    explicit_counterexample()
    dominance_split()
    logit_adapter_invariance()
    top_level_elasticity()
    pmd2r_violation()
    mass_elasticity()
    print("Percentages above are design-dependent Monte-Carlo figures, not theorems.")
