# -*- coding: utf-8 -*-
"""
tra_kuramoto_reference.py — coherence layer for APPENDIX_TRA (§13).

The Kuramoto order parameter r ∈ [0,1] measures phase synchronization of N coupled
oscillators. In TRA it is the *measurable* coherence quantity for:
  - multi-engine clusters (each engine = an oscillator; structure/feed = coupling),
  - combustion-acoustic + structural modes locking in phase (POGO / screech),
  - the NDT 'coherence' analogue TRA marks provisional.

Two uses:
  (1) r(K) — how strongly a cluster locks as coupling K rises past the critical K_c;
  (2) r -> drives the GSM off-diagonal ρ (§11): rising coherence == rising cross-pillar
      coupling == a widening, lower-tailed U distribution. This unifies §11 and §13.

Research use only; a diagnostic. © 2026 Petar Nikolov, MIT.
"""
import numpy as np

def kuramoto_r(N, K, omega=None, T=40.0, dt=0.01, seed=0):
    """Steady-state Kuramoto order parameter r for N oscillators at coupling K."""
    rng = np.random.default_rng(seed)
    if omega is None:
        omega = rng.normal(0.0, 1.0, N)      # natural-frequency spread (std = 1)
    theta = rng.uniform(0, 2 * np.pi, N)
    steps = int(T / dt); rs = np.empty(steps)
    for t in range(steps):
        z = np.exp(1j * theta).mean()
        r = np.abs(z); psi = np.angle(z)
        theta = theta + (omega + K * r * np.sin(psi - theta)) * dt
        rs[t] = r
    return float(rs[int(steps * 0.7):].mean())   # average over the last 30% (steady state)

def rho_from_r(r, rho_max=0.7):
    """Illustrative monotone map coherence r -> a GSM cross-pillar correlation rho (the
    §11<->§13 bridge). A modelling choice (rho = rho_max*r), not an identity -- calibrate per vehicle."""
    return float(rho_max * r)

if __name__ == "__main__":
    print("=== Kuramoto: cluster coherence r vs coupling K  (N=33, Starship-Raptor-class) ===")
    print("critical coupling for a unit-std Gaussian spread: K_c = 2*sqrt(2/pi) ≈ %.2f\n" % (2*np.sqrt(2/np.pi)))
    for K in [0.0, 0.5, 1.0, 1.6, 2.0, 3.0, 4.0]:
        r = kuramoto_r(33, K, seed=3)
        bar = "#" * int(r * 40)
        print("  K=%.1f   r=%.3f  |%-40s|  %s" % (K, r, bar, "LOCKED" if r > 0.8 else ("partial" if r > 0.3 else "incoherent")))

    print("\n=== a detuned 'rogue' engine (1 of 33 off-frequency) — does the cluster still lock? ===")
    rng = np.random.default_rng(5)
    om = rng.normal(0, 1, 33); om[0] = 6.0   # one engine far off-frequency
    for K in [1.6, 3.0, 5.0]:
        r = kuramoto_r(33, K, omega=om, seed=5)
        print("  K=%.1f  r=%.3f  -> %s" % (K, r, "cluster locks, rogue pulled in" if r > 0.8 else "rogue stays detuned (partial sync)"))

    print("\n=== §11<->§13 bridge: coherence r drives the GSM off-diagonal ρ ===")
    for r in [0.10, 0.40, 0.70, 0.95]:
        print("  coherence r=%.2f  ->  GSM ρ_FPA=%.2f  (higher sync => wider, lower-tailed U — see §11.2)" % (r, rho_from_r(r)))
