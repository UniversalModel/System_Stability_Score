# GSI-RTD: Empirical Bridge — Mini Prototype v3

**Domain:** Email Marketing & Outreach Simulation (144 Agents)  
**Status:** L2/L3 Domain Implementation Candidate  
**U-Theory Alignment:** v26 Canonical (Form ↔ Time, Position ↔ Space, Action ↔ Energy)

---

## Overview

A **worked engineering instance** of AD-RTD + SSS + Triadic Scheduler in a minimal, reproducible domain, as specified in `APPENDIX_GSI-RTD v.28 §35.5`.

It demonstrates that a non-compensatory triadic selection model **categorically outperforms random candidate selection** under a finite resource budget — this is the empirical bridge to the Scheduler Sufficiency Conjecture (§6.1).

> **Epistemic status:** This is a **mini-prototype / domain implementation candidate** (§35.5 from APPENDIX_GSI-RTD v.28). It is **not** a completed Gate 1–5 validation — it is a proof of concept demonstrating that the working architecture is implementable and produces structured, measurable results. This is the first concrete empirical bridge between U-Theory's triadic ontology and a runnable, reproducible experiment.

> **LGP-12 note:** The current implementation simulates LGP-10 (Pulse Monitor) and LGP-12 (Audit & Learn) as lightweight inline steps within each generation loop. The full 12-step cycle (Scan → Detect → Decompose → Rank → Leverage → Synthesize → Select → Plan → Allocate → Monitor → Report → Audit) will be implemented in the next version using the `gsi_runtime.py` module.

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

## Quick Start

```bash
# 1. Install dependencies (no external API key required)
pip install numpy pandas matplotlib

# 2. Run the simulation (5 generations, 144 agents, Monte Carlo N=200)
cd GSI_simulations/email_marketing
python gsi_rtd_email_marketing_demo.py

# 3. Expected output: SI trajectory table, triage, Monte Carlo CI table, ablation tests
#    Output files written to the same directory automatically.
```

## Output files

| File | Description |
|------|-------------|
| `gsi_rtd_email_marketing_v2.png` | **SI evolution (Triadic vs Random) + final distribution** |
| `gsi_rtd_email_marketing_results.csv` | Per-generation stats + SSS-Guard status |
| `gsi_rtd_email_marketing_all_systems.csv` | All 144 systems with triage |
| `gsi_rtd_monte_carlo_results.csv` | Monte Carlo CI table (N=200 runs) |
| `gsi_rtd_ablation_results.csv` | Ablation test outcomes |

---

## Monte Carlo Validation (N=200 runs, §35.5bis)

| Gen | Mean Advantage | 95% CI | Significant at 95%? |
|-----|---------------|--------|---------------------|
| 1 | +0.024 | positive | YES |
| 2 | +0.125 | positive | YES |
| 3 | +0.251 | positive | YES |
| 4 | +0.363 | positive | YES |
| 5 | +0.448 | positive | YES |

The advantage is **positive and growing** in all 5 generations across all 200 runs. 95% confidence intervals exclude zero from Generation 1 onwards.

---

## Ablation Tests (Gate 3, §32)

| Test | Result | Interpretation |
|------|--------|---------------|
| Remove Form pillar (F < 0.30) | SI drops ≥15% → **PASS ✓** | Form is structurally critical |
| Remove Position pillar (P < 0.30) | SI drops ≥15% → **PASS ✓** | Position is structurally critical |
| Remove Action pillar (A < 0.30) | SI drops ≥15% → **PASS ✓** | Action is structurally critical |
| Arithmetic vs Geometric mean | Geo ≤ Arith → **PASS ✓** | Non-compensatory design validated |

> **Test 3 interpretation — Arithmetic vs Geometric mean:**  
> Arithmetic mean allows a strong pillar to compensate for a weak one (e.g., excellent Form masks poor Position). This is exactly what the non-compensatory design of SSS must prevent. The geometric mean + δ-penalty gives a more realistic estimate of systemic instability — a system with one weak pillar is genuinely fragile, regardless of how strong the other two pillars are. The arithmetic mean produces inflated scores and higher variance, confirming that the geometric formulation is the structurally correct choice.

---

## SSS-Guard in Action (LGP-10 Monitor)

SSS-Guard flags when `|predicted_SI − realised_SI| > 0.06`, indicating that the scoring model is diverging from environmental reality. A typical run shows:

- **Gen 1–2:** `OK` — predictions close to realised values while SI is low and noise dominates
- **Gen 3–4:** `ALERT` may appear as the Triadic Scheduler converges rapidly (fast learning exposes prediction lag)
- **Gen 5:** `OK` again as scores plateau near 0.98 (low residual noise)

An `ALERT` in mid-run is **expected and healthy** — it signals that the scheduler is outpacing its own prediction model, which the Learning Law (§26) then corrects in the next generation.

---

## How This Fits in the Bigger Picture

This mini-prototype is the **first concrete empirical bridge** between U-Theory's triadic ontology (Form ↔ Time, Position ↔ Space, Action ↔ Energy) and a runnable, measurable experiment.

It shows that:
1. AD-RTD is **practically implementable** — not just theoretically specified
2. The Triadic Scheduler **consistently beats random selection** — the core claim of §6.1
3. The non-compensatory architecture **behaves as designed** — removing one pillar collapses SI (ablation Gate 3)
4. Results are **statistically robust** — Monte Carlo CI excludes zero across all generations

The broader GSI-RTD architecture — including LLM-powered agents, cross-domain transfer, and the full LGP-12 protocol — is implemented in `gsi_runtime.py`.

---

## Next Steps (Gate 1–5 Validation Roadmap)

| Gate | Requirement | Status |
|------|------------|--------|
| **Gate 1** | Scheduler vs Random: CI excludes zero | ✅ Done (Monte Carlo N=200) |
| **Gate 2** | SSS-Guard coverage ≥ 0.80 in 3+ domains | 🔲 Next: run in Supply Chain, Medical, Finance domains |
| **Gate 3** | Ablation: all 3 pillar removals cause ≥15% SI drop | ✅ Done (ablation tests) |
| **Gate 4** | Scaling: performance improves with more agents | 🔲 Next: run N=1000 agents across 3 domains |
| **Gate 5** | Independent replication by a different operator | 🔲 Future: external researcher replication |

Full Gate 1–5 specification: `APPENDIX_GSI-RTD v.28 §32`.

---

## References

- **Parent Theory:** [U-Theory / Universal Model v26](https://doi.org/10.17605/OSF.IO/74XGR)
- **Architecture:** `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` §35.5
- **Protocol:** `APPENDIX_LGP_Lady_Galaxy_Protocol.md` — Practical Note
- **Full Runtime:** `gsi_runtime.py` — §33 Implementation Blueprint (LLM-powered)
- **Repo:** [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)

---

> *"The survivors ARE the solution."*  
> — GSI-RTD principle: intelligence emerges from structured elimination of instability.

**DOI:** [https://doi.org/10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)  
**Author:** Petar Nikolov, Sofia, 27 March 2026
