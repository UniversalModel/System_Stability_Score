# GSI-RTD Mini Prototype v1 — Supply Chain Domain

**Domain 2** of the GSI-RTD empirical validation suite.

---

## Problem

> *"How to restore supply chain stability after a disruption?"*

Framing: triadic search architecture over operational response options — not a prescriptive logistics system.

---

## Triadic Decomposition (AD-RTD §1.1)

| Axis | Canonical mapping | Variants (6) |
|------|------------------|--------------|
| **Action (A)** | Energy — what is done | Reorder from primary supplier, Activate backup supplier, Expedite shipping, Redistribute inventory, Renegotiate contracts, Automate reorder |
| **Form (F)** | Time — via what structure | Purchase order, Emergency procurement doc, Expedite request, Transfer order, Contract amendment, Automated reorder rule |
| **Position (P)** | Space — in what context | Tier-1 supplier, Tier-2/backup supplier, 3PL logistics partner, Regional distribution hub |

**Search space:** 6 × 6 × 4 = **144 candidate systems**

---

## SSS Formula (v26 invariant)

```
U  = ∛(F · P · A)          geometric mean (non-compensatory)
δ  = (max − min) / (max + 0.01)   imbalance penalty
SI = U / (1 + δ)²           Stability Index
```

Hard kill gate: `min(F, P, A) < 0.30 → SI = 0`

---

## Triadic Scheduler

- **Budget per generation:** ~15% of N = 22 systems  
- **Learning rate:** α = 0.052  
- **Exploration rate:** ε = 0.15  
- **Generations:** 5  
- **Monte Carlo runs:** N = 200 (seed: `run * 11 + 17`)

---

## Results (Monte Carlo N=200)

| Generation | Mean advantage | 95% CI | Significant? |
|-----------|---------------|--------|-------------|
| 1 | +0.118 | [+0.055, +0.180] | ✅ YES |
| 2 | +0.160 | [+0.089, +0.232] | ✅ YES |
| 3 | +0.196 | [+0.120, +0.271] | ✅ YES |
| 4 | +0.246 | [+0.167, +0.325] | ✅ YES |
| **5** | **+0.294** | **[+0.201, +0.387]** | ✅ **YES** |

> Triadic scheduler significantly outperforms random baseline across all 5 generations. Effect comparable to Email Marketing domain (+0.303), confirming cross-domain generalizability (§26.4).

---

## Quick Start

```bash
cd GSI_simulations/supply_chain
python gsi_rtd_supply_chain_demo.py
```

**Output files:**
- `gsi_rtd_supply_chain_results.png` — 4-panel figure
- `gsi_rtd_supply_chain_main.csv` — generation-level results
- `gsi_rtd_supply_chain_mc.csv` — Monte Carlo summary
- `gsi_rtd_supply_chain_all_systems.csv` — all 144 systems scored

---

## Cross-domain comparison

| Domain | Agents | Gen 5 advantage | CI |
|--------|--------|----------------|----|
| Email Marketing | 144 | +0.303 | [+0.214, +0.391] |
| **Supply Chain** | **144** | **+0.294** | **[+0.201, +0.387]** |
| Medical | 216 | +0.309 | [+0.222, +0.395] |

---

## References

- **Architecture:** `APPENDIX_GSI-RTD` §1.1 (AD-RTD), §20 (Scheduler), §26.4 (Cross-domain)
- **Theory:** [doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)
