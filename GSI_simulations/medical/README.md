# GSI-RTD Mini Prototype v1 — Medical Domain

**Domain 3** of the GSI-RTD empirical validation suite.

---

## Problem

> *"How to restore patient health stability after illness onset?"*

Framing: **clinical decision search architecture** — not AI prescribing medicine. The model generates and ranks candidate treatment configurations via triadic decomposition and stability scoring. Clinical judgment remains with the practitioner.

---

## Triadic Decomposition (AD-RTD §1.1)

| Axis | Canonical mapping | Variants (6) |
|------|------------------|--------------|
| **Action (A)** | Energy — what intervention | Pharmacotherapy, Physiotherapy, Dietary intervention, Monitoring, Rehabilitation, Behavioral/psychotherapy |
| **Form (F)** | Time — delivery vehicle | Prescription medication, Nutritional supplement, Medical device, Therapeutic protocol/care plan, Exercise programme, Digital monitoring tool |
| **Position (P)** | Space — care environment | Hospital (inpatient), Specialized clinic, Rehabilitation centre, Home care environment, Sanatorium / recovery resort, Telemedicine context |

**Search space:** 6 × 6 × 6 = **216 candidate systems**

---

## Hard Medical Gates (stricter than other domains)

| Gate | Condition | Effect |
|------|-----------|--------|
| G1 Safety | High-risk / contraindicated combination | Reject (SI = 0) |
| G2 Provider validity | Unverified non-clinical setting | Heavy penalty |
| G3 Patient fit | Mismatch to condition profile | Reject (SI = 0) |
| G4 Min pillar | min(F, P, A) < 0.30 | Reject (canonical) |

> Hard gates encode the non-compensatory principle: a single critical failure cannot be offset by strong performance elsewhere.

---

## SSS Formula (v26 invariant)

```
U  = ∛(F · P · A)               geometric mean
δ  = (max − min) / (max + 0.01)  imbalance penalty
SI = U / (1 + δ)²                Stability Index
```

---

## Triadic Scheduler

- **Budget per generation:** ~15% of N = 32 systems  
- **Learning rate:** α = 0.052  
- **Exploration rate:** ε = 0.15  
- **Generations:** 5  
- **Monte Carlo runs:** N = 200 (seed: `run * 13 + 23`)

---

## Results (Monte Carlo N=200)

| Generation | Mean advantage | 95% CI | Significant? |
|-----------|---------------|--------|-------------|
| 1 | +0.123 | [+0.055, +0.190] | ✅ YES |
| 2 | +0.167 | [+0.099, +0.236] | ✅ YES |
| 3 | +0.209 | [+0.136, +0.282] | ✅ YES |
| 4 | +0.251 | [+0.180, +0.321] | ✅ YES |
| **5** | **+0.309** | **[+0.222, +0.395]** | ✅ **YES** |

> Medical domain shows the **highest Gen-5 advantage** (+0.309) among all three domains, consistent with the hypothesis that Position matters more in medicine (care environment significantly constrains outcome).

---

## Quick Start

```bash
cd GSI_simulations/medical
python gsi_rtd_medical_demo.py
```

**Output files:**
- `gsi_rtd_medical_results.png` — 4-panel figure
- `gsi_rtd_medical_main.csv` — generation-level results
- `gsi_rtd_medical_mc.csv` — Monte Carlo summary
- `gsi_rtd_medical_all_systems.csv` — all 216 systems scored

---

## Cross-domain comparison

| Domain | Agents | Gen 5 advantage | CI |
|--------|--------|----------------|----|
| Email Marketing | 144 | +0.303 | [+0.214, +0.391] |
| Supply Chain | 144 | +0.294 | [+0.201, +0.387] |
| **Medical** | **216** | **+0.309** | **[+0.222, +0.395]** |

---

## Falsifiability tests (§32)

| Test | Expected result | Status |
|------|----------------|--------|
| Triadic > random baseline | ✅ Confirmed (all 5 generations) | Done |
| Removing Position → performance drops | Strong hypothesis (Position ↔ care env. matters) | Gate 3 pending |
| Hard gates vs no gates | Without G1-G3, unsafe systems may score high | Gate 4 pending |

---

## References

- **Architecture:** `APPENDIX_GSI-RTD` §1.1 (AD-RTD), §20 (Scheduler), §20.3.1 (Hard gates), §26.4 (Cross-domain)
- **Theory:** [doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)
