# -*- coding: utf-8 -*-
"""Worked ILLUSTRATION (computational, not empirical): POS on a leveraged-buyout /
restructuring decision. Runs the scenario through the REAL pos_reference.py gate — so
the numbers are PROGRAM OUTPUT, not asserted. This is a computational consistency
check of the illustration, NOT an empirical validation and NOT a pilot calibration:
the inputs, thresholds and trajectories are hand-specified, not drawn from LBO data.
ZERO decision authority; research-use-only; the verdict is a function of the
(unvalidated) threshold calibration (that is POS-P1). (c) 2026 Petar Nikolov, MIT."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # find pos_reference.py beside this file
from dataclasses import dataclass
from pos_reference import Pillar, Action, PosConfig, ThetaModel, pos_gate

# --- LBO domain adapter: an ILLUSTRATIVE threshold profile (hand-specified, NOT calibrated) ---
@dataclass
class LBOTheta(ThetaModel):
    # ILLUSTRATIVE LBO thresholds — hand-set for mechanism demonstration; ZERO decision authority.
    def theta_F(self, a): return 0.65      # "do not commit if organizational readiness < 0.65"
    def theta_P(self, a): return 0.55      # "do not commit if market/debt position < 0.55"

# domain-declared caps (illustrative): a partial-stake prep (e<=0.35) is an ungated prep;
# a full buyout (kappa>=0.9, e=0.7) must clear the readiness gate.
cfg = PosConfig(theta=LBOTheta(), kappa_probe=0.35, exposure_cap=0.35)

def run(label, F, P, act):
    ok, why, d = pos_gate(F, P, act, cfg)
    print("  %-46s R=%.3f  ->  %-10s (%s)  bottleneck=%s  V_POS=%.2f"
          % (label, d["R"], "AUTHORIZE" if ok else "WITHHOLD", why, d["bottleneck"], d["V_POS"]))
    return d

def U(F, P, A): return (F*P*A) ** (1/3.0)

print("=== LBO / restructuring — POS worked illustration (computational; ZERO decision authority) ===\n")

commit    = Action("full leveraged buyout + restructuring", kappa=0.90, exposure=0.70, stakes=0.8)
prep      = Action("partial stake + operational improvement", kappa=0.30, exposure=0.30, stakes=0.5)
fake_prep = Action("large-exposure 'prep' (commitment in disguise)", kappa=0.30, exposure=0.70, stakes=0.6)

print("Point estimates (SE=0) — reproduces the hand arithmetic exactly:")
run("commit now  F=0.40 P=0.50", Pillar(0.40, 0.0), Pillar(0.50, 0.0), commit)
run("a^prep now  F=0.40 P=0.50 (e=0.30<=cap)", Pillar(0.40, 0.0), Pillar(0.50, 0.0), prep)
run("large-exposure 'prep' (e=0.70>cap)", Pillar(0.40, 0.0), Pillar(0.50, 0.0), fake_prep)
run("commit after preparation F=0.72 P=0.61", Pillar(0.72, 0.0), Pillar(0.61, 0.0), commit)

print("\nWith due-diligence uncertainty (pre-prep SE=0.05, post-prep SE=0.04) —")
print("POS reads the per-pillar (scalar) LOWER confidence bound [SCALAR_LCB mode, NOT a joint bound]:")
run("commit now  F=0.40 P=0.50 (SE=0.05)", Pillar(0.40, 0.05), Pillar(0.50, 0.05), commit)
run("commit after prep F=0.72 P=0.61 (SE=0.04)", Pillar(0.72, 0.04), Pillar(0.61, 0.04), commit)

# --- accumulation gap: commit-now (base burns) vs prep-then-commit ---
print("\n=== Counterfactual accumulation gap  ΔM = Σ (U_seq − U_prem)  over 12 abstract periods ===")
# premature commit: leverage strains an unready org -> F,P burn, U stays low
F_prem = [0.40,0.34,0.30,0.28,0.27,0.27,0.28,0.29,0.30,0.31,0.32,0.33]
P_prem = [0.50,0.44,0.40,0.38,0.37,0.37,0.38,0.39,0.40,0.41,0.42,0.43]
# sequenced: several periods of a^prep build the base, then commit on a ready base
F_seq  = [0.40,0.48,0.58,0.66,0.72,0.74,0.75,0.76,0.77,0.78,0.79,0.80]
P_seq  = [0.50,0.54,0.58,0.60,0.61,0.63,0.64,0.65,0.66,0.67,0.68,0.69]
A = 0.70
DT = 1.0   # abstract period length; set to the real step (e.g. 2 months) for score-time units
dM = DT * sum(U(F_seq[k],P_seq[k],A) - U(F_prem[k],P_prem[k],A) for k in range(len(F_seq)))
print("  U_seq(end)=%.3f  U_prem(end)=%.3f   ΔM = %.3f  (Δt=%.0f period; ×Δt_real for score-time units)"
      % (U(F_seq[-1],P_seq[-1],A), U(F_prem[-1],P_prem[-1],A), dM, DT))

print("""
--- HONEST READING (load-bearing) ---
* COMPUTATIONAL, not empirical. Numbers are program output on hand-specified inputs — no LBO data,
  no experiment, no calibration sample. ZERO decision authority; RUO. Not an investment tool.
* The gate FLIPS from WITHHOLD to AUTHORIZE only under THIS illustrative theta (0.65 / 0.55).
  Under pos_reference.py's stricter default theta the same post-prep state can still withhold —
  the verdict is a FUNCTION of the (unvalidated) calibration. That is exactly what POS-P1 must fix.
* Point estimates authorize the post-prep commit (R=1.108); with due-diligence uncertainty the
  per-pillar LCB gate holds it (R=0.970, bottleneck=Position). Propagating uncertainty tightens the gate.
* Exposure cap works: a low-kappa move with e>cap is a commitment-in-disguise, NOT a free probe.
* ΔM is a dimensionless sum over 12 abstract periods (× Δt_real for units); an ILLUSTRATIVE internal
  quantity. A real 'premature commitment burns the base' claim needs the causal comparator (POS-P2).
""")
