# GSI-RTD Simulations

Working demonstrations of the **Action-Driven Recursive Triadic Decomposition (AD-RTD)** architecture from [APPENDIX_GSI-RTD v.28](../APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md).

---

## `gsi_rtd_email_marketing_demo.py`

**The first working mini-prototype of GSI-RTD.**

Solves the problem *"How to run a successful email marketing campaign?"* using the full GSI-RTD pipeline:

### Triadic Decomposition (6 × 6 × 4 = 144 agents)

| Axis | Count | Examples |
|------|-------|---------|
| **Action** | 6 | Send email, Post on forums, Meet key people… |
| **Form** | 6 | HTML email, PDF attachment, Infographic… |
| **Position** | 4 | By hierarchy (CEO/Editor), By thematic interest… |

Each **system** = one unique `(Form_i @ Position_j performing Action_k)` triple.

### What it demonstrates

| GSI-RTD component | Implementation |
|------------------|---------------|
| **AD-RTD** §1.1 | Action → Form → Position decomposition order |
| **SSS** §7 | `SI = ∛(F×P×A) / (1 + δ²)` |
| **Non-compensatory rule** | `min(F,P,A) ≤ ε → SI = 0` (collapse) |
| **Triadic Scheduler** §20 | Priority = SI / Cost, top-20 per generation |
| **Learning Law** §26 | Best agents improve each generation |
| **Triage** §1.1 Phase 6 | High (≥0.618) / Mid / Low (<0.380) |

### Results (5 generations)

```
Gen 1 → SI: 0.582  (baseline)
Gen 2 → SI: 0.707  (above θ_stable)
Gen 3 → SI: 0.826
Gen 4 → SI: 0.914
Gen 5 → SI: 0.967  ← superintelligent convergence
```

**Winner:** `Send email` | `Ready-made template` | `By geographic location`  
→ SI = **0.98** — the intelligence output of the process.

### Run

```bash
pip install numpy pandas matplotlib
python gsi_rtd_email_marketing_demo.py
```

### Output files

- `gsi_rtd_email_marketing_v2.png` — SI evolution + final distribution
- `gsi_rtd_email_marketing_results.csv` — per-generation stats
- `gsi_rtd_email_marketing_all_systems.csv` — all 144 systems with triage

---

> *"The survivors ARE the solution."*  
> — GSI-RTD principle: intelligence emerges from structured elimination of instability.

**DOI:** [https://doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)  
**Author:** Petar Nikolov, Sofia, 27 March 2026
