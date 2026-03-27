# GSI-RTD: Empirical Bridge — Mini Prototype v2

**Domain:** Email Marketing & Outreach Simulation (144 Agents)  
**Status:** L2/L3 Domain Implementation Candidate  
**U-Theory Alignment:** v26 Canonical (Form ↔ Time, Position ↔ Space, Action ↔ Energy)

---

## Overview

A **worked engineering instance** of AD-RTD + SSS + Triadic Scheduler in a minimal, reproducible domain, as specified in `APPENDIX_GSI-RTD v.28 §35.5`.

It demonstrates that a non-compensatory triadic selection model **categorically outperforms random candidate selection** under a finite resource budget — this is the empirical bridge to the Scheduler Sufficiency Conjecture (§6.1).

> **Epistemic status:** Mini-prototype / domain implementation candidate. Not a formal proof of GSI. Not a completed Gate 1–5 validation. Purpose: show practical implementability and generation-level behaviour.

---

## Triadic Domain Mapping (AD-RTD Order: A → F → P)

| Axis | Canonical mapping | Count | Variants |
|------|------------------|-------|---------|
| **Action (A)** | Energy | 6 | Send email; Post in forums; Fill online forms; Send postal letters; Meet key people; Pay for ads |
| **Form (F)** | Time | 6 | Ready template; Personalized report; Infographic; Video pitch; HTML email; PDF attachment |
| **Position (P)** | Space | 4 | By geography; By company/workplace; By hierarchy (CEO/Editor); By thematic interest |

$$N = 6 \times 6 \times 4 = 144 \text{ candidate systems}$$

The operational enumeration order A → F → P is methodological only; it does not invert the canonical ontology.

---

## Key Features Demonstrated

| GSI-RTD Component | Implementation |
|------------------|---------------|
| **AD-RTD** §1.1 | Action → Form → Position decomposition |
| **SSS** §7 | `SI = ∛(F×P×A) / (1+δ)²` — canonical formula |
| **Non-compensatory rule** | `min(F,P,A) ≤ ε → SI = 0` (collapse) |
| **Triadic Scheduler** §20 | Priority = SI / Cost, top-20 per generation (minimal heuristic) |
| **Random Baseline** | Same budget, random selection — validates Scheduler superiority |
| **SSS-Guard** §7.2 | LGP-10 monitor: flags if `|predicted − realised| > 0.06` |
| **Learning Law** §26 | Best agents improve each generation |
| **Triage** §1.1 Phase 6 | High (≥0.618) / Mid / Low (<0.380) |

---

## Results

| Gen | Predicted SI | Triadic Real SI | Random Baseline | Triadic Advantage |
|-----|-------------|----------------|----------------|------------------|
| 1 | 0.405 | 0.391 | 0.359 | +0.032 |
| 2 | 0.515 | 0.499 | 0.377 | +0.122 |
| 3 | 0.651 | 0.620 | 0.366 | **+0.254** |
| 4 | 0.802 | 0.783 | 0.420 | **+0.363** |
| 5 | 0.944 | 0.918 | 0.470 | **+0.448** |

**Winner:** `Post on forums` | `Infographic` | `By hierarchy (CEO/Editor)` → SI = **0.98**

**Triage (final generation):** High ≥0.618: **27** | Mid: **117** | Low: **0**

The green line (Triadic Scheduler) consistently and increasingly dominates the red line (Random Baseline), validating the Scheduler Sufficiency Conjecture §6.1.

---

## Run

```bash
pip install numpy pandas matplotlib
python gsi_rtd_email_marketing_demo.py
```

## Output files

| File | Description |
|------|-------------|
| `gsi_rtd_email_marketing_v2.png` | **SI evolution (Triadic vs Random) + final distribution** |
| `gsi_rtd_email_marketing_results.csv` | Per-generation stats + SSS-Guard status |
| `gsi_rtd_email_marketing_all_systems.csv` | All 144 systems with triage |

---

## Validation Boundary

This mini-prototype demonstrates practical implementability but does **not** satisfy the full empirical bridge requirements of §35.2–§35.3. Future work:

1. Formal A/B test with statistical significance (not just one run)
2. Scheduler ablation (remove SI-priority, measure impact)
3. Coverage / performance scaling curve (§21)
4. Domain metric agreement with SSS-Guard (§7.2)
5. Independent replication by a different operator

---

## References

- **Parent Theory:** [U-Theory / Universal Model v26](https://doi.org/10.17605/OSF.IO/74XGR)
- **Architecture:** `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` §35.5
- **Protocol:** `APPENDIX_LGP_Lady_Galaxy_Protocol.md` — Practical Note
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)

---

> *"The survivors ARE the solution."*  
> — GSI-RTD principle: intelligence emerges from structured elimination of instability.

**Author:** Petar Nikolov, Sofia, 27 March 2026

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

### Results (5 generations, canonical SI = U/(1+δ)²)

```
Gen 1 → SI: 0.405  (baseline)
Gen 2 → SI: 0.515
Gen 3 → SI: 0.651  (above θ_stable)
Gen 4 → SI: 0.802
Gen 5 → SI: 0.944  ← convergence
```

**Winner:** `Post on forums` | `Infographic` | `By hierarchy (CEO/Editor)`  
→ SI = **0.98** — the intelligence output of the process.

**Triage:** High ≥0.618: **27** | Mid 0.38–0.618: **117** | Low <0.38: **0**

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
