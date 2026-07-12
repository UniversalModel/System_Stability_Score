# Triadic Rocketry & Astronautics (TRA)

**A conformant `TriadicDomain` on `aerospace.launch_vehicle`** — the Form / Position / Action
registration of an ascending and propulsively-landing rocket, scored by the non-compensatory
keystone **U = ∛(F·P·A)**. Part of the U-Theory / Universal Model corpus.

> **Dedication.** *To Elon Musk — who made the landing burn the ordinary end of a flight, and in
> doing so showed a generation the hardest truth this appendix formalizes: a rocket you fly home
> is one that must keep all three pillars — structure, trajectory, and thrust — alive at the same
> time, on the same razor, with the propellant nearly gone.*

---

## What this is (the useful core)

TRA is a **unifying diagnostic language for rocket stability** — one map that sits *above* the
specialist toolchain (FEA, CFD, GNC, combustion, PRA) and makes a single question legible across
all of it: *of structure, trajectory, and thrust, which is the floor right now?*

| Pillar | On a rocket | Canonical mirror |
|---|---|---|
| **Form** | geometry · structure · mass properties | Form ↔ Time |
| **Position** | trajectory · atmosphere · gravity field · reachable corridor | Position ↔ Space |
| **Action** | thrust · control · propellant · sense-act cycles | Action ↔ Energy |

The keystone **U = ∛(F·P·A)** is *non-compensatory*: a rocket **multiplies** its virtues, it does
not average them. A dead pillar is unrecoverable — full thrust cannot save a buckled airframe; a
perfect airframe cannot save a spent tank on a lost trajectory. On a rocket this **zero-limit
non-compensation is a literal engineering fact, not an analogy** — which is why TRA is the corpus's
flagship domain instance. The weakest-pillar router `π* = argmin(F,P,A)` names which specialist gets
the next question.

**Honest scope.** This is a **research registration + a pre-registered validation programme**, *not*
a validated survival model, not a certified design tool, and not a flight-control law. `U` is a
*normalized geometric-mean index* of the joint survival probability `F·P·A` (exact only under
independence) — **it is not itself a probability.** Whether the number `U` *predicts* loss-of-vehicle
better than existing margins is exactly what the §B falsifiers (TRA-P0/P1/P2) are built to test.

---

## Contents

| File | What it is |
|---|---|
| `APPENDIX_TRA_TRIADIC_ROCKETRY_ASTRONAUTICS.md` | The full appendix (v1.5 FINAL) — registration, stability matrix, GSM, Kuramoto coherence layer, falsifiers, dual-use firewall |
| `APPENDIX_TRA_TRIADIC_ROCKETRY_ASTRONAUTICS.pdf` | Typeset PDF (~29 pp, A4) |
| `tra_gsm_reference.py` | **Gaussian Stability Matrix** — turns the point `U` into a credible interval under measured cross-pillar coupling |
| `tra_kuramoto_reference.py` | **Coherence layer** — Kuramoto order parameter `r` for multi-engine / combustion synchrony, and the `r → ρ` bridge into the GSM |
| `test_tra.py` | Smoke test asserting the headline numbers below |
| `requirements.txt` | `numpy` (the only dependency) |

---

## Quickstart — run the test code

```bash
pip install -r requirements.txt

python tra_gsm_reference.py       # GSM demo + Starship-class phase gates
python tra_kuramoto_reference.py  # coherence r vs coupling K, rogue engine, r->rho bridge
python test_tra.py                # smoke test: asserts the headline numbers
```

### What `tra_gsm_reference.py` demonstrates

Models the three pillar probabilities as **correlated log-odds** (multivariate normal), so that when
pillars are coupled (POGO / slosh / aeroservoelasticity) the uncertainty in `U` widens and its lower
tail drops — the honest risk picture a scalar `U` hides. Scoring a Starship-class phase profile
against the distributional gate **"pass iff `P(U ≥ 0.75) ≥ 0.90`"**:

| Phase | point-`U` | `P(U≥0.75)` | gate |
|---|---|---|---|
| Ascent (nominal) | 0.900 | 100% | PASS |
| Max-Q (F↔P aeroelastic) | 0.827 | 100% | PASS |
| Staging (all coupled) | 0.823 | 100% | PASS |
| **Landing burn (A↔P)** | 0.768 | **79%** | **FLAG** |

The landing burn is the only phase the gate flags — precisely the hardest regime physically
(near-depleted propellant + a narrow corridor). The scalar `U=0.768` looks "fine"; the *distribution*
correctly says otherwise. (Pillar inputs are illustrative; the U-distribution math is exact.)

### What `tra_kuramoto_reference.py` demonstrates

The **Kuramoto order parameter `r ∈ [0,1]`** is the *measurable* coherence of a coupled cluster
(each engine an oscillator; structure/feed the coupling). For N=33 (Raptor-class) with a unit-std
natural-frequency spread the critical coupling is `K_c = 2√(2/π) ≈ 1.60`; below it the cluster is
incoherent, above it it locks (K=3.0 → r≈0.89). A detuned "rogue" engine stays out of the lock at
`K_c` but is entrained by K=3.0. The **`r → ρ` bridge** feeds coherence back into the GSM
off-diagonal (`ρ ≈ ρ_max·r`): rising synchrony ⇒ rising coupling ⇒ a wider, lower-tailed `U`.
This is the one place the corpus's "coherence" currency becomes a running number.

> **Note.** `Λ` (measured leakage) *informs* the GSM correlation `ρ` via a stated monotone mapping
> `ρ = m(Λ)` — a modelling choice, **not** an identity (`Λ` is unsigned distance-dependence, `ρ` a
> signed Gaussian correlation). The GSM interval is a **risk-visualization, not an instability
> certificate.**

---

## The pre-registered falsifiers (§B of the appendix)

- **TRA-P0** — does a flight state actually factor into F/P/A (net of coupling)?
- **TRA-P1** — does `U` beat a fitted margin-ensemble **and** a compensatory aggregate **and** a
  free-exponent power law (the last isolates the cube-root specifically)?
- **TRA-P1b** — do `δ` / `SI` add predictive value over `U` alone?
- **TRA-P2** — does weakest-pillar routing beat uniform effort at equal budget?
- **TRA-S0** — *executable now*: blind π*-coding of public accident investigations (Challenger,
  Columbia, Ariane 501, CRS-7, AMOS-6, …); inter-rater κ + phase-profile fit. Tests the *language's*
  reliability, a rung below TRA-P1.

---

## Dual-use firewall

A launch vehicle and a ballistic missile share the physics. TRA optimizes **only** stabilize-polarity,
own-vehicle, safety-of-flight nodes declared by a named accountable human. Weaponization, targeting,
destabilization of third-party vehicles, and any operationally hazardous specifics are **type-forbidden
and never produced.** This firewall is never gated by a falsifier and never retired. It aligns with,
but does not substitute for, MTCR / national export-control law.

---

## Provenance

The `REVIEW` accompanying this appendix is an **internal multi-model editorial hardening record**
(adversarial LLM panels, v1.0→v1.5) — **not** independent human peer review.

- Parent record (U-Theory): **DOI 10.17605/OSF.IO/74XGR**
- Project: https://u-model.org · sibling repos: `UniversalModel/core`, `UniversalModel/System_Stability_Score`
- Author: **Petar Nikolov** (ORCID 0009-0001-8669-2276)

## License

- **Text** (appendix, PDF, this README): CC BY 4.0
- **Code** (`*.py`): MIT — see `LICENSE`
