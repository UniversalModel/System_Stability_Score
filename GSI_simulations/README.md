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
│   ├── gsi_rtd_email_marketing_v2.png
│   ├── gsi_rtd_email_marketing_results.csv
│   ├── gsi_rtd_email_marketing_all_systems.csv
│   └── gsi_rtd_monte_carlo_results.csv
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

## Results summary

| Domain | Agents | Triadic advantage (Gen 5) | Significant? |
|--------|--------|--------------------------|-------------|
| [Email Marketing](email_marketing/) | 144 | **+0.30** [CI: +0.21, +0.39] | ✅ YES (N=200) |

---

## References

- **Architecture:** `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` §35.5
- **Protocol:** `APPENDIX_LGP_Lady_Galaxy_Protocol.md`
- **Theory:** [doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)
