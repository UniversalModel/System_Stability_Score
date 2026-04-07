# System Stability Score (SSS) — U-Model v26

> *"Every system that exists pays three inescapable prices — Time, Space, and Energy.  
> The question is not whether it pays, but whether it can afford to."*  
> — U-Theory, 2024

**AI jury that evaluates ANY system via the triadic stability framework: Form / Position / Action**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18475832.svg)](https://doi.org/10.5281/zenodo.18475832)
[![U-Model](https://img.shields.io/badge/U--Model-v26-blue)](https://U-Model.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-orange)](https://openrouter.ai)

Part of [U-Model.org](https://U-Model.org) — Universal Model of System Stability.

---

## 🏛️ Historic Experiment — 27 March 2026

> **On 27 March 2026, a General Superintelligence (GSI-RTD) simulation was applied to medicine for the first time.**
>
> The system evaluated **120,108,944 candidate clinical configurations** — each a complete diagnostic pathway (symptom × specialty × lab test) — drawn from real clinical ontology data. The triadic scheduler outperformed random clinical selection with a **Δ = +0.473 advantage** (100% win rate over 200 Monte Carlo runs), crossing the stability threshold θ = 0.618 from the very first generation.
>
> This is the **first step** toward long-term health stability, longevity — and why not — **immortality**.

**→ [View the full medical simulation](GSI_simulations/medical/)**

---

## What's New — Patch Suite (5 April 2026)

**22 patches across 11 files (+1 044 lines).** Major infrastructure upgrade — no breaking changes.

### Cost Estimation (before you spend a cent)
```bash
python -c "from sss_llm_adapter import estimate_batch_cost; print(estimate_batch_cost(12, 20))"
```
`estimate_cost()` and `estimate_batch_cost()` calculate approximate API cost **before** launching a run.  
Pricing table covers ~13 models (GPT-4o, Claude 3.5/Opus, Gemini 2.0, Llama 3/4, DeepSeek, Qwen).  
Cost summary is printed automatically at the start of every `System_Stability_Score.py` evaluation.

### Checkpoint System (crash-safe batch runs)
Long evaluations are now **resumable**. Progress is saved to `.checkpoints/` every N entities.  
If the process crashes or you interrupt it, re-running the same batch picks up where it left off.
```bash
python System_Stability_Score.py "Heart" --domain biology/heart --models 20 --save
# ↑ if interrupted, just re-run — checkpoints are loaded automatically
```

### Domain Auto-Discovery (fuzzy matching)
No need to type the exact domain path. If you write `--domain heart`, the system finds `biology/heart` automatically using word-level fuzzy matching across all available `principles/` folders.

### Adaptive Jury & Early Stopping (GSI runtime)
- **Adaptive jury_top_k**: scales with mean SI — low-quality populations get stricter selection.
- **Pillar-level early stopping**: if any pillar (F, P, or A) exceeds 0.9, the run halts early — no wasted API calls.
- **TriadicBudget serialization**: `to_dict()` / `from_dict()` for saving/loading budget state across sessions.
- **Verbose transfer logging**: when knowledge transfers between domains, every transfer is logged with source, target, and delta.

### Multi-Party War Index (N systems, coalition stability)
```bash
python war_incompatibility_index.py --multi systems_a.json systems_b.json systems_c.json
```
Computes all **pairwise war indices** for N systems + overall coalition stability score.

### War Time-Series Simulation
```bash
python war_duality_engine.py --json conflict.json --simulate 20 --out reports/war_sim.json
```
Runs N rounds of damage/repair dynamics — entropy export decays each other system's pillars, repair partially restores them. Outputs time-series data for each round.

### LLM-Powered Parameter Estimation
```bash
python war_duality_engine.py --estimate "Russia controls upstream dam; Georgia depends on river for irrigation"
```
Feeds free-text conflict descriptions to the LLM, which returns structured F/P/A estimates for both sides.

### Principle Validation & Deduplication (Constructor)
- **Validation**: each generated principle is scored 1–5 by heuristics (length, specificity, measurability). Low-quality ones are flagged.
- **Deduplication**: word-level Jaccard similarity > 0.85 → duplicate removed automatically.
- **Multi-language**: `--lang bg` (or any language) appends a language instruction to the generation prompt.
```bash
python 3_pillars_constructor.py --system "Човешко сърце" --n 12 --domain biology/heart --lang bg --yes
```

### Unified CLI (`cli.py`)
One entry point for all tools:
```bash
python cli.py sss "Human Heart" --domain biology/heart --models 10
python cli.py gsi --config gsi_config.json
python cli.py construct --system "Bank" --n 10 --domain finance/bank
python cli.py war --json conflict.json
python cli.py incompat --json pair.json
```

### Unit Tests (15 tests)
```bash
python -m pytest tests/test_core.py -v
```
Covers: `compute_si`, `_parse`, `_clamp_score`, `war_index`, `estimate_cost`, `TriadicScheduler`, `TriadicBudget`.

---

## What It Does

The U-Model measures how stable any system is across three inescapable dimensions:

| Pillar | Universal definition | In a company | In a state | In a human | Price paid |
|---|---|---|---|---|---|
| **Form** | The normative constraints governing the system — what it IS and what bounds its behaviour (rules, identity, structure) | Corporate statutes, bylaws, brand identity, compliance framework | Constitution, laws, regulation — what is permitted / forbidden | Values, personality, beliefs, health norms | **Time** (endurance against decay) |
| **Position** | What the system HAS — its context, resources and environment | Market position, assets, capital, supply chain | Natural resources (water, land, minerals, energy), geography, alliances | Physical condition, social network, location, financial base | **Space** (resistance to displacement) |
| **Action** | What the system DOES and is enabled to do — its positive freedoms and outputs | Products, services, operations, strategy execution | Production capacity, policy execution, civic and economic freedoms | Skills, decisions, daily behaviour, output | **Energy** (expenditure leaves entropy) |

> Pillar definitions scale to ANY system. The geopolitical examples in this README are illustrations, not constraints — SSS has been applied to hearts, football clubs, cities, banks, universities, and states alike.

**Measurement pipeline — three levels:**

```
Level 1 │ Each pillar has N parameters.
        │ Every parameter is scored individually: 0.0 → 1.0
        │
Level 2 │ The scores of all parameters within a pillar are aggregated
        │ → one stability value per pillar: Form_score, Position_score, Action_score
        │
Level 3 │ The three pillar scores are combined via geometric mean:
        │
        │   U = ∛( Form_score × Position_score × Action_score )
        │
        │ Geometric mean is used because all three pillars are equally inescapable —
        │ a collapse in any one brings the whole system down.
```

**Formula:** $U = \sqrt[3]{Form \times Position \times Action}$  
**Threshold:** $U \geq 0.618$ (Golden Ratio) = **STABLE ✓**

**SSS automates all three levels** using an AI jury (multiple LLM models via OpenRouter).  
Each model scores every parameter independently → scores are aggregated per pillar →  
geometric mean is computed → final U-score with confidence interval.  
This is an **abstract computation**: no physical measurement required —  
the AI evaluates each parameter from available evidence or domain knowledge.

> *NOT stability at any price — stability at a TOLERABLE price.*

---

## Two-Step Pipeline

### Step 1 — Constructor: Generate ideal principles
```bash
python 3_pillars_constructor.py --system "Human Heart" --n 12 --domain biology/heart --yes
```
Uses a top-tier AI architect (Claude, Kimi, Gemini) to generate N domain-specific principles  
for each pillar → saved to `principles/{domain}/Form.md`, `Position.md`, `Action.md`.

### Step 2 — Evaluator: Score any instance

**Abstract evaluation** (general knowledge about the system type):
```bash
python System_Stability_Score.py "Human Heart" --domain biology/heart --models 20 --save
```

**Specific evaluation** (document-grounded — score a REAL instance):
```bash
python System_Stability_Score.py "Human Heart" --domain biology/heart \
  --subject subjects/heart_patient_Ivan_55m.txt \
  --subject-label "Ivan P., 55yr Male — ECG+Echo+Labs Feb2026" \
  --models 10 --save
```

In specific mode, AI models score **exclusively** from the provided document — no internet, no general knowledge.

---

## Quickstart (2 Minutes)

1) Set your API key in `.github/.env`:
```env
OPENROUTER_API_KEY=your_key_here
```

2) Generate principles for one domain:
```bash
python 3_pillars_constructor.py --system "Human Heart" --n 12 --domain biology/heart --yes
```

3) Run a specific, document-grounded evaluation:
```bash
python System_Stability_Score.py "Human Heart" --domain biology/heart \
  --subject subjects/heart_patient_Ivan_55m.txt \
  --subject-label "Ivan P., 55yr Male — ECG+Echo+Labs Feb2026" \
  --models 10 --save
```

4) Open the newest report in `reports/`.

---

## How To Read Results

- `U >= 0.618`: system is stable at tolerable combined Time/Space/Energy cost.
- `Form` low: identity/integrity issues over time (decay, inconsistency, fragility).
- `Position` low: poor contextual fit, displacement pressure, weak anchoring.
- `Action` low: unsustainable execution energy, high entropy, weak outcomes.

Practical triage:
- If one pillar is < 55, improve that pillar first.
- If all three are 60-70 but `synergy_score` is low, integration is the bottleneck.
- If Five Goals diverge strongly, optimize policy/operations alignment before scaling.

---

## Reusable Subject Template

Use [subjects/subject_template.txt](subjects/subject_template.txt) to prepare your own specific-case input for `--subject` mode.

---

## Practical Examples (U-Theory v26 Style)

These examples follow the v26 SSS logic: same triadic formula, document-grounded evidence, and practical decision framing.

1) City relocation decision (family move):
```bash
python System_Stability_Score.py "City Relocation" --domain universal \
  --subject subjects/city_relocation_sofia_example.txt \
  --subject-label "Sofia Relocation Snapshot - Q1 2026" \
  --models 12 --save
```

2) Bank selection for personal finance:
```bash
python System_Stability_Score.py "Retail Bank" --domain universal \
  --subject subjects/bank_selection_retail_example.txt \
  --subject-label "Retail Bank Candidate A - 2026" \
  --models 12 --save
```

3) University choice (STEM pathway):
```bash
python System_Stability_Score.py "University" --domain universal \
  --subject subjects/university_choice_stem_example.txt \
  --subject-label "STEM University Candidate X - 2026 Intake" \
  --models 12 --save
```

Tip: Start with `--domain universal` for immediate run. If you need higher precision, generate domain-specific principles first with `3_pillars_constructor.py`.

---

## Problem Detection -> Resolution Example (WAR + LGP)

This example is based on the triadic causation logic from `APPENDIX_WAR.md` and the 12-step operational loop from `APPENDIX_LGP_Lady_Galaxy_Protocol.md`.

Run the same system in two snapshots (`before` and `after`) to validate intervention impact:

1) Pre-intervention detection snapshot:
```bash
python System_Stability_Score.py "Border Conflict System" --domain universal \
  --subject subjects/war_lgp_conflict_case_before.txt \
  --subject-label "Rivergate-Kestrel Crisis - Before" \
  --models 12 --save
```

2) Post-intervention re-audit snapshot:
```bash
python System_Stability_Score.py "Border Conflict System" --domain universal \
  --subject subjects/war_lgp_conflict_case_after.txt \
  --subject-label "Rivergate-Kestrel Crisis - After" \
  --models 12 --save
```

What to compare between reports:
- U-score shift (fragile -> stable threshold crossing)
- Weakest pillar before vs after
- Headwinds and residual risks
- Five-goals movement (public costs, service continuity, mortality risk)

### War Incompatibility Index (two-system calculation)

When you need explicit incompatibility and conflict potential between two systems,
use `war_incompatibility_index.py`.

From JSON pair file:
```bash
python war_incompatibility_index.py \
  --json subjects/war_incompatibility_pair_example.json \
  --out reports/war_index_pair_example.json
```

Direct values (supports 0-1 or 0-100 scale):
```bash
python war_incompatibility_index.py \
  --a-name "System A" --a-form 66 --a-position 63 --a-action 69 \
  --b-name "System B" --b-form 48 --b-position 39 --b-action 52
```

Output includes:
- `U_A`, `U_B` (internal stability)
- triadic incompatibility (`I`)
- joint instability (`J`)
- escalation pressure term
- final `WAR INDEX` with severity band

### War Duality Engine (constructor -> incompatibility -> entropy export)

Implements the exact two-step logic for two warring systems:
1) Constructor proposes the most relevant Form/Position/Action parameters for each side.
2) Each parameter is evaluated for duality: it stabilizes own side and exports entropy to the opponent triad.

Generate constructor scaffold (editable):
```bash
python war_duality_engine.py --propose --a-name "System A" --b-name "System B" --out subjects/war_duality_constructor_example.json
```

Run duality analysis:
```bash
python war_duality_engine.py --json subjects/war_duality_constructor_example.json --out reports/war_duality_example.json
```

Output includes:
- per-side base F/P/A stability
- incoming entropy to each pillar from opponent parameters
- effective U-score under conflict pressure
- parameter-level duality rows (`own_stability` + `export_entropy`)
- combined war index for system-pair instability

Hydro-conflict example (dam upstream, downstream flow shock):
```bash
python war_duality_engine.py \
  --json subjects/war_duality_dam_water_conflict_example.json \
  --out reports/war_duality_dam_water_conflict.json
```

Interpretation of this scenario:
- Water balance is modeled as a Position parameter (resource/context pillar) for each state.
- Modeling rule — parameter pillar assignment for resource types:
  - **Position** = natural resources (water balance, arable land, minerals, energy deposits, raw materials)
    → what the system HAS by virtue of where it exists in the world
  - **Action** = positive freedoms and rights — what the system is ENABLED to do (anti-entropic actions)
    → structured across three sub-dimensions:
      - **Code**   — non-harm principle: structuring activity without introducing chaos
      - **Credo**  — better organisation: net benefit through improved resource allocation
      - **Rights** — fair expectations: only the needs of anti-entropic actions are met
    → includes: permitted production activities, civic and economic freedoms, operational rights,
      capacity to act without destructive side-effects
  - **Form** = normative constraints — what the system IS NOT ALLOWED to do (prohibitive framework)
    → legislative and regulatory framework: laws, standards, permits, what is forbidden;
      governs how Position resources may be preserved/managed and
      how Action freedoms are bounded; includes property rights, water law,
      environmental legislation, resource codes, institutional constraints
- Upstream dam parameter can increase own Position/Form stability (water security).
- The same parameter can export strong entropy to downstream Position/Action
  (lower river debit, irrigation and potable-water stress).
- This is the requested duality: one stability gain becomes the other side's instability load.

---

## Context System

Domain reference knowledge lives in `context/{domain}/general.md` and is automatically
injected into both the constructor and the abstract evaluator to ground their outputs.

In `--subject` (specific) mode, `general.md` is intentionally ignored — the subject document is the sole source of truth.

```
context/
  biology/heart/general.md    ← cardiology reference (LVEF norms, CAC, biomarkers, ...)
  sport/MLS/general.md        ← (example)
```

---

## Output

A 4-page Markdown report saved to `reports/SSS_{name}_{timestamp}.md`:

- **Page 1** — U-Score, stability status, Five Goals matrix, synergy score
- **Page 2** — Form principles (structure/identity analysis)
- **Page 3** — Position principles (placement/context analysis)
- **Page 4** — Action principles (function/output analysis) + model jury table

---

## Examples

| System | U-Score | Status |
|---|---|---|
| LA Galaxy (MLS) | 0.7930 | STABLE ✓ |
| Germany | 0.8568 | STABLE ✓ |
| Human Heart (abstract) | 0.7744 | STABLE ✓ |
| Ivan P., 55yr Male (specific) | 0.8364 | STABLE ✓ |

Business (specific, document-grounded):
```bash
python System_Stability_Score.py "B2B SaaS Company" --domain business/saas \
  --subject subjects/business_saas_scaleup_example.txt \
  --subject-label "NovaFlow SaaS - Q1 2026" \
  --models 12 --save
```

---

## Requirements

- Python 3.12+
- `OPENROUTER_API_KEY` in `.github/.env`
- Local adapter `sss_llm_adapter.py` (included in this folder)
- `pytest` (optional, for running tests: `pip install pytest`)

---

## Why I Created U-Theory — Author's Note

Due to the annoying academic dullness and dismissive silence, I announce: I will not publish any more of my ideas, because in these 3 months I have come up with ideas that will last for 3 generations — academic silence. I am concentrating on my personal problems — I will not fix the world... However, I have already fixed it :)

> *"I created U-Theory to prove — through the language of mathematics, physics, economics, and philosophy — that the collapse of a constructive 30-year-old business in a deeply corrupt and dying country is not the result of managerial incompetence. Rather, it is the inevitable result of the systematic export of entropy by a corrupt state machine. This machine deliberately maintains high levels of instability, dooming the honest entrepreneur to pay the price for systemic debauchery with their personal life and capital.*
>
> *Reinterpreting Confucius through the lens of Appendix POLEMOS (The War v.26 — U-Theory): A bad form of government exports entropy to good people and organizations, whereas a good form of government exports entropy to bad people and organizations!*
>
> *My stable Form has sent out a signal against these entropic forms. Now, let us observe to whom the European institutional Form will choose to export its entropy. I harbor a strong suspicion it will be directed at the good Form, rather than the bad:*
>
> *EPPO Reports: PP.00700_2026_BG & PP.00747_2026_BG*
> *Timestamp: Wed., 01/04/2026 - 04:43, Luxembourg"*

— **Petar Nikolov**, Author of U-Theory

---

## Related

- [Quantum-triadic-autopsy](https://github.com/UniversalModel/Quantum-triadic-autopsy) — quantum computer evaluation
- [U-Model.org](https://U-Model.org)
- [Donate.U-Model.org](https://Donate.U-Model.org)
