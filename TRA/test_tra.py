# -*- coding: utf-8 -*-
"""Smoke test for the TRA reference code — asserts the headline numbers in the README.
Run: python test_tra.py    (exit 0 = all pass). No pytest required."""
import numpy as np
from tra_gsm_reference import gsm_u
from tra_kuramoto_reference import kuramoto_r, rho_from_r

def Rmat(fp, fa, pa):
    return np.array([[1, fp, fa], [fp, 1, pa], [fa, pa, 1]], float)

def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    assert cond, name

# --- GSM: imbalanced state loses tail mass ---
r = gsm_u(0.90, 0.55, 0.90, rho=0.10, seed=2)
check("GSM imbalanced P(U>=0.75) ~ 0.75", 0.70 <= r["p_above"] <= 0.80)
check("GSM weakest pillar is P", r["pi_star"] == "P")

# --- GSM: Starship-class phase gate flags the landing burn, passes ascent ---
ascent  = gsm_u(0.92, 0.90, 0.88, R=Rmat(0.15, 0.15, 0.15), seed=7)
landing = gsm_u(0.90, 0.72, 0.70, R=Rmat(0.20, 0.25, 0.62), seed=7)
check("GSM ascent PASSes the 0.90 gate", ascent["p_above"]  >= 0.99)
check("GSM landing burn FLAGs (<0.90 gate)", landing["p_above"] < 0.90)

# --- Kuramoto: incoherent below K_c, locked well above ---
check("Kuramoto incoherent at K=0.5",  kuramoto_r(33, 0.5, seed=3) < 0.40)
check("Kuramoto locks at K=3.0",        kuramoto_r(33, 3.0, seed=3) > 0.80)
check("Kc = 2*sqrt(2/pi) ~ 1.60", abs(2*np.sqrt(2/np.pi) - 1.60) < 0.01)

# --- the r -> rho bridge ---
check("rho_from_r(0.7) ~ 0.49", abs(rho_from_r(0.7) - 0.49) < 1e-6)

print("\nAll smoke tests passed.")
