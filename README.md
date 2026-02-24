# System Stability Score (SSS) — U-Model v25

> *"Every system that exists pays three inescapable prices — Time, Space, and Energy.  
> The question is not whether it pays, but whether it can afford to."*  
> — U-Theory, 2024

**AI jury that evaluates ANY system via the triadic stability framework: Form / Position / Action**

[![U-Model](https://img.shields.io/badge/U--Model-v25-blue)](https://U-Model.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-orange)](https://openrouter.ai)

Part of [U-Model.org](https://U-Model.org) — Universal Model of System Stability.

---

## What It Does

The U-Model measures how stable any system is across three inescapable dimensions:

| Pillar | What it measures | Price paid |
|---|---|---|
| **Form** | What the system IS — structural integrity, identity | **Time** (endurance against decay) |
| **Position** | Where the system IS — spatial/contextual placement | **Space** (resistance to displacement) |
| **Action** | What the system DOES — purposeful function | **Energy** (expenditure leaves entropy) |

**Formula:** $U = \sqrt[3]{Form \times Position \times Action}$  
**Threshold:** $U \geq 0.618$ (Golden Ratio) = **STABLE ✓**

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
  --subject subjects/Ivan_55m.txt \
  --subject-label "Ivan P., 55yr Male — ECG+Echo+Labs Feb2026" \
  --models 10 --save
```

In specific mode, AI models score **exclusively** from the provided document — no internet, no general knowledge.

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

---

## Requirements

- Python 3.12+
- `OPENROUTER_API_KEY` in `.github/.env`
- [`ai_subagent.py`](https://github.com/UniversalModel/Quantum-triadic-autopsy) from the bot infrastructure

---

## Related

- [Quantum-triadic-autopsy](https://github.com/UniversalModel/Quantum-triadic-autopsy) — quantum computer evaluation
- [U-Model.org](https://U-Model.org)
- [Donate.U-Model.org](https://Donate.U-Model.org)
