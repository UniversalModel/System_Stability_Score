# -*- coding: utf-8 -*-
"""Smoke test for pos_reference.py (v0.2) — asserts the gate's formal properties.
Run: python test_pos.py   (exit 0 = all pass). Pure stdlib, no pytest needed."""
from pos_reference import (Pillar, Action, PosConfig, pos_gate, readiness,
                           violation_severity, verification_cost, z_lower,
                           persistent_burn)

cfg = PosConfig()
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name); assert cond, name

# --- the gate authorizes a prepared, decisive commit ---
ok, why, d = pos_gate(Pillar(0.92, 0.02), Pillar(0.85, 0.03),
                      Action("race", kappa=0.85, exposure=0.6, stakes=0.7), cfg)
check("prepared commit -> authorized (ready_commit)", ok and why == "ready_commit")

# --- the same commit from an unready base is the Forbidden Action ---
ok, why, d = pos_gate(Pillar(0.45, 0.05), Pillar(0.80, 0.03),
                      Action("race", kappa=0.85, exposure=0.6, stakes=0.7), cfg)
check("unprepared commit -> withheld (forbidden_action)", (not ok) and why == "forbidden_action")

# --- a reversible, capped-exposure probe is ungated even at low readiness ---
ok, why, d = pos_gate(Pillar(0.30, 0.10), Pillar(0.30, 0.10),
                      Action("pilot", kappa=0.10, exposure=0.1, stakes=0.3), cfg)
check("reversible+capped probe -> authorized (probe_or_prep) despite low readiness", ok and why == "probe_or_prep")

# --- v0.2: low-kappa BUT over the exposure cap is NOT an auto-authorized probe ---
ok, why, d = pos_gate(Pillar(0.30, 0.05), Pillar(0.30, 0.05),
                      Action("large-exposure reversible trade", kappa=0.10, exposure=0.90, stakes=0.4), cfg)
check("low-kappa but over exposure cap -> NOT probe_or_prep", not (ok and why == "probe_or_prep"))

# --- values-forbidden dominates even a perfectly ready base ---
ok, why, d = pos_gate(Pillar(0.99, 0.001), Pillar(0.99, 0.001),
                      Action("prohibited", kappa=0.9, stakes=1.0, firewall_pass=False), cfg)
check("values-forbidden -> withheld regardless of readiness", (not ok) and why == "values_forbidden")

# --- emergency with a robust positive margin AND a complete log is a forced move ---
ok, why, d = pos_gate(Pillar(0.50, 0.05), Pillar(0.45, 0.05),
                      Action("emg", kappa=0.8, stakes=0.9, is_emergency=True, emergency_log_complete=True,
                             L_action=(0.30, 0.45), L_inaction=(0.70, 0.90)), cfg)
check("emergency, M_emg>0, log complete -> authorized (forced move)", ok and "emergency" in why)

# --- v0.2: emergency with M_emg>0 but log NOT complete is withheld ---
ok, why, d = pos_gate(Pillar(0.50, 0.05), Pillar(0.45, 0.05),
                      Action("emg-unlogged", kappa=0.8, stakes=0.9, is_emergency=True, emergency_log_complete=False,
                             L_action=(0.30, 0.45), L_inaction=(0.70, 0.90)), cfg)
check("emergency, M_emg>0 but log incomplete -> withheld", not ok)

# --- emergency WITHOUT a positive robust margin is still forbidden ---
ok, why, d = pos_gate(Pillar(0.50, 0.05), Pillar(0.45, 0.05),
                      Action("emg2", kappa=0.8, stakes=0.9, is_emergency=True, emergency_log_complete=True,
                             L_action=(0.60, 0.95), L_inaction=(0.50, 0.70)), cfg)
check("emergency, M_emg<=0 -> withheld", not ok)

# --- margin identity m_R == R - 1 ---
d = readiness(Pillar(0.7, 0.05), Pillar(0.6, 0.05),
              Action("x", kappa=0.5, stakes=0.4), cfg)
check("m_R == R - 1", abs(d["mR"] - (d["R"] - 1.0)) < 1e-9)

# --- V_POS properties: zero when ready; positive & ordered when unready ---
check("V_POS = 0 when R >= 1", abs(violation_severity(Action("a", kappa=0.9, stakes=0.9), 1.2)) < 1e-12)
check("V_POS grows with shortfall", violation_severity(Action("a", kappa=0.9, stakes=0.9), 0.2)
      > violation_severity(Action("a", kappa=0.9, stakes=0.9), 0.8))

# --- verification economics: F-first preferred iff cF(1-pP) <= cP(1-pF) ---
_, _, f_first = verification_cost(cF=1.0, cP=5.0, pF=0.6, pP=0.9)
check("cheap high-reject gate checked first (F-first preferred)", f_first)

# --- z_lower matches the standard normal quantiles ---
check("z_lower(0.05) ~ 1.6449", abs(z_lower(0.05) - 1.6449) < 1e-3)
check("z_lower(0.025) ~ 1.9600", abs(z_lower(0.025) - 1.9600) < 1e-3)

# --- base burn: a persistent decline burns more than a recovering dip ---
check("persistent decline burns more than a recovering dip",
      persistent_burn([0.9, 0.5, 0.5, 0.5], [0.8, 0.6, 0.6, 0.6])
      > persistent_burn([0.9, 0.86, 0.9, 0.92], [0.8, 0.79, 0.82, 0.83]))

# --- v0.2: input validation rejects out-of-range / negative-SE inputs ---
def raises(fn):
    try:
        fn(); return False
    except ValueError:
        return True
check("Pillar rejects mean > 1", raises(lambda: Pillar(1.5, 0.0)))
check("Pillar rejects negative SE", raises(lambda: Pillar(0.5, -0.1)))
check("Action rejects kappa out of [0,1]", raises(lambda: Action("bad", kappa=1.4)))
check("Action rejects inverted loss interval", raises(lambda: Action("bad", kappa=0.5, L_action=(0.9, 0.2))))

print("\nAll POS smoke tests passed.")
