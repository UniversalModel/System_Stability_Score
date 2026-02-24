# Context Directory — U-Model System Stability Score

## Purpose

This directory contains **domain context files** that ground both the
**constructor** (`3_pillars_constructor.py`) and the **evaluator**
(`System_Stability_Score.py`) in domain-specific knowledge.

## How It Works

### Abstract evaluation (no `--subject` flag)
Both scripts auto-load `context/{domain}/general.md` if it exists and inject
it into the AI prompt. The models use this as background knowledge alongside
their own training.

### Specific evaluation (`--subject FILE` flag)
The evaluator uses **ONLY** the `--subject` document — `general.md` is
intentionally ignored. This guarantees that scores are grounded exclusively in
the provided local measurements, not in general or internet knowledge.

## Directory Structure

```
context/
  biology/
    heart/
      general.md          ← general cardiology reference (used by constructor + abstract eval)
  sport/
    MLS/
      general.md          ← MLS league reference knowledge
  glass/
    general.md
  ...
```

## Auto-loading Rules

| Script | Mode | context/general.md | --subject FILE |
|---|---|---|---|
| `3_pillars_constructor.py` | always | ✅ loaded | n/a |
| `System_Stability_Score.py` | abstract | ✅ loaded | n/a |
| `System_Stability_Score.py` | specific | ❌ ignored | ✅ exclusive source |

## CLI Override

Both scripts accept `--context FILE` to override the auto-loaded context:

```bash
# Constructor with explicit context file
python 3_pillars_constructor.py --system "Human Heart" --domain biology/heart \
  --context context/biology/heart/general.md --yes

# Evaluator with explicit context file (abstract mode)
python System_Stability_Score.py "Human Heart" --domain biology/heart \
  --context context/biology/heart/general.md --models 10 --save

# Evaluator specific mode — context auto-ignored even if present
python System_Stability_Score.py "Human Heart" --domain biology/heart \
  --subject subjects/Ivan_55m.txt --subject-label "Ivan P 55yr" --models 5 --save
```

## Format

`general.md` is a plain text / Markdown file. No special structure required.
Write it as a reference summary a domain expert would use before scoring.
Include: key metrics, measurement ranges, clinical thresholds, typical failure
modes, and stability indicators relevant to the system.
