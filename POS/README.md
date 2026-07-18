# POS — The Principle of Sequence (Readiness-Ordered Commitment)

A U-Theory / U-Model appendix + its runnable engine. POS is a **commitment-control
discipline**: `U = ∛(F·P·A)` scores a *state*; POS decides *when* an already-chosen
action may pass from reversible exploration to irreversible commitment — **verify
Form, secure Position, then commit.** Premature irreversible commitment is the
*Forbidden Action*; it burns the base.

## Contents

| File | What it is |
|---|---|
| `APPENDIX_POS_PRINCIPLE_OF_SEQUENCE.md` (+ `.md.pdf`) | The appendix, **v1.6.1** — the principle, the gate, falsifiers POS-P1/P2/P3, formal core |
| `APPENDIX_POS_ENGINE_PROFILE.md` (+ `.md.pdf`) | **v1.1** — the universal kernel + domain adapters (research · funds · factories · government · military-space) |
| `pos_reference.py` | **v0.2** reference gate (pure stdlib): readiness ratio, LCB, κ, exposure cap, robust emergency (log-enforced), input validation |
| `test_pos.py` | property tests — **19/19 pass** |
| `pos_example_lbo.py` | a **computational** worked illustration (LBO/restructuring) — program output, ZERO decision authority |
| `pos_p1_harness.py` | the **POS-P1 calibration/falsification harness** — synthetic benchmark environments, frozen baselines, PASS/INCONCLUSIVE/KILL |

## Run (no dependencies — Python 3 stdlib only)

```
python test_pos.py            # property tests (expect 19/19)
python pos_reference.py       # the gate on worked scenarios
python pos_example_lbo.py     # LBO illustration (computational, not empirical)
python pos_p1_harness.py      # POS-P1 on synthetic benchmarks
```

## Honest status (load-bearing)

Everything here is an **L2/B2 candidate operationalization** — NOT a validated law,
NOT a theorem of `U = ∛(F·P·A)`, and NOT a decision engine for real use. Every
threshold and coefficient is **illustrative, ZERO decision authority, research-use-only**.
The decisive arbiter is the calibration test **POS-P1 / POS-P2**.

The harness gives a first *synthetic* signal and, importantly, it **discriminates**
rather than rubber-stamping POS: readiness-gating **PASSES** when premature commitment
is costly and the signal is noisy, and is **KILLED** (loses to an eager baseline) when
failure is cheap and delay is expensive. Real validation means pointing the same
harness at real or high-fidelity simulated data, with a public pre-registration of
baselines and Δ_min, scored on **external** outcomes.

## License
Text: CC BY 4.0 · Code (`*.py`): MIT · © 2026 Petar Nikolov (ORCID 0009-0001-8669-2276)
Parent record: DOI 10.17605/OSF.IO/74XGR · https://u-model.org
