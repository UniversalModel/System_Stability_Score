# GSI_simulations — Empirical Bridge Repository

Working domain implementations of the **GSI-RTD** architecture.  
Each subdirectory is a self-contained **empirical bridge instance** (§35.5).

---

## Structure

```
GSI_simulations/
├── email_marketing/        ← Domain 1: Publisher outreach (6×6×4 = 144 agents)
│   ├── README.md
│   ├── gsi_rtd_email_marketing_demo.py
│   ├── gsi_rtd_stats_analysis.py
│   ├── gsi_rtd_email_marketing_v2.png
│   ├── gsi_rtd_stats_figures.png
│   ├── gsi_rtd_email_marketing_results.csv
│   ├── gsi_rtd_email_marketing_all_systems.csv
│   ├── gsi_rtd_monte_carlo_results.csv
│   ├── gsi_rtd_real_stats.csv
│   └── gsi_rtd_real_stats_report.txt
│
├── supply_chain/           ← Domain 2: Disruption management (6×6×4 = 144 agents)
│   ├── README.md
│   ├── gsi_rtd_supply_chain_demo.py
│   ├── gsi_rtd_supply_chain_results.png
│   ├── gsi_rtd_supply_chain_main.csv
│   ├── gsi_rtd_supply_chain_mc.csv
│   └── gsi_rtd_supply_chain_all_systems.csv
│
├── medical/                ← Domain 3: Clinical decision search (6×6×6 = 216 agents)
│   ├── README.md
│   ├── gsi_rtd_medical_demo.py
│   ├── gsi_rtd_medical_results.png
│   ├── gsi_rtd_medical_main.csv
│   ├── gsi_rtd_medical_mc.csv
│   └── gsi_rtd_medical_all_systems.csv
│
└── [your_domain]/          ← Add your own domain here (see template below)
```

---

## How to extend to your own domain

Any problem can be decomposed into three triadic axes (AD-RTD §1.1):

| Axis | Canonical mapping | Question |
|------|------------------|---------|
| **Action (A)** | Energy | What intervention is applied? |
| **Form (F)** | Time | In what representation / vehicle? |
| **Position (P)** | Space | Toward which contextual target? |

**Steps:**

1. **List your variants** for each axis (aim for 4–8 per axis)
2. **Enumerate** all combinations: `N = |A| × |F| × |P|`
3. **Score** each system using SSS: `SI = ∛(F·P·A) / (1+δ)²`
4. **Run** the Triadic Scheduler (budget = ~15% of N per generation)
5. **Compare** against random baseline (Gate 1 — §6.1)
6. **Run Monte Carlo** N≥200 to establish statistical significance

Copy `email_marketing/gsi_rtd_email_marketing_demo.py` as your starting point and replace the three axes lists and the cost dictionaries.

---

## Results summary — Gate 1 (§32, §6.1)

All three domains complete. Cross-domain generalizability confirmed (§26.4).

| Domain | Agents | Triadic advantage (Gen 5) | 95% CI | Significant? |
|--------|--------|--------------------------|--------|-------------|
| [Email Marketing](email_marketing/) | 144 (6×6×4) | **+0.303** | [+0.214, +0.391] | ✅ YES (N=200) |
| [Supply Chain](supply_chain/) | 144 (6×6×4) | **+0.294** | [+0.201, +0.387] | ✅ YES (N=200) |
| [Medical](medical/) | 216 (6×6×6) | **+0.309** | [+0.222, +0.395] | ✅ YES (N=200) |

> **Gate 1 status:** 3/5 domains required for Gate 1 pass. Three heterogeneous domains all show statistically significant triadic advantage with comparable effect sizes (~+0.30), supporting domain-agnostic generalizability.

---

## Gate roadmap

| Gate | Criterion | Status |
|------|-----------|--------|
| Gate 1 | Triadic scheduler > random baseline (≥5 domains) | 🔶 3/5 complete |
| Gate 2 | Triadic scheduler > GA baseline | ⬜ Pending |
| Gate 3 | Ablation: removing Position degrades performance | ✅ Confirmed (email domain) |
| Gate 4 | Hard gates vs no gates on medical domain | ⬜ Pending |
| Gate 5 | Independent replication | ⬜ Pending |

---

## References

- **Architecture:** `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` §35.5
- **Protocol:** `APPENDIX_LGP_Lady_Galaxy_Protocol.md`
- **Theory:** [doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)
