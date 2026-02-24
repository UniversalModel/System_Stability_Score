# Measuring the Stability of Anything: The System Stability Score

**U-Model v25 — AI-Aggregated Triadic Evaluation Framework**

*February 2026 | UniversalModel.org*

---

## The Problem: How Do You Know If a System Is Stable?

A hospital asks: *Is our patient's heart stable enough for surgery?*  
A government asks: *Is Germany's democratic structure holding?*  
A sports analyst asks: *Will LA Galaxy sustain its performance this season?*  
A city planner asks: *Is this water distribution system resilient?*

These questions sound completely different. Yet they share a single underlying structure: **how well does this system maintain its existence under pressure?**

Current tools give partial answers. Medical scoring (APACHE, EuroSCORE) works only for medicine. Rating agencies (S&P, Moody's) work only for finance. Sports analytics works only for sports. Each domain reinvents the wheel using domain expertise that cannot transfer.

The **System Stability Score (SSS)** is a universal scoring engine — one framework, any system, comparable results.

---

## The Theory: Three Prices of Existence

Every system that exists — from a human heart to a nation-state to a glass of water — pays three inescapable prices to maintain its existence:

$$U = \sqrt[3]{Form \times Position \times Action}$$

| Pillar | What it measures | The price paid |
|---|---|---|
| **Form** | What the system *IS* — structural integrity, identity over time | **Time** — endurance against decay and fragmentation |
| **Position** | Where the system *IS* — spatial, contextual, relational placement | **Space** — resistance against displacement and irrelevance |
| **Action** | What the system *DOES* — purposeful function and output | **Energy** — expenditure that leaves irreversible entropy |

**The key insight:** paying these prices is not optional. Every system pays. The question is *whether it can afford to* — whether the cost of maintaining stability is bearable given the system's resources.

> A glass of water sitting on a table pays a trivial price in all three dimensions. A human heart beating 100,000 times per day pays an immense energy price. A nation at war pays catastrophic prices across all three.

**The stability threshold:** $U \geq 0.618$ — the Golden Ratio, $\varphi^{-1}$.

This is not arbitrary. The Golden Ratio appears at the boundary between ordered and disordered systems across mathematics, biology, and physics. A system at $U = 0.618$ is the minimum viable stability — below it, collapse becomes probable.

**The geometric mean is critical:** because $U = \sqrt[3]{F \times P \times A}$, a system with Form = 1.0, Position = 1.0, and Action = 0.0 has $U = 0$. No pillar can compensate for another's collapse. This models reality correctly — a structurally perfect system that cannot act is not stable.

---

## The Architecture: How It Works

The SSS pipeline has two stages:

### Stage 1 — The Constructor
A top-tier AI architect (Claude Opus, Kimi k2, Gemini Pro) generates **domain-specific stability principles** for the system being evaluated.

For a **Human Heart**, the constructor generates principles like:
- Form: *"Myocardial Integrity — left ventricular wall thickness and EF within physiological bounds"*
- Position: *"Hemodynamic Placement — BP within 120/80 mmHg, LV geometry appropriate to body surface area"*
- Action: *"Rhythmic Output Consistency — sinus rhythm maintained, cardiac output 4–8 L/min at rest"*

These are not generic platitudes. They are **falsifiable, domain-specific stability conditions** derived from the actual physics and biology of the system. Each principle names what guarantees stability AND what causes failure when violated.

### Stage 2 — The AI Jury
Up to 50 AI models from OpenRouter run **in parallel**, each independently scoring every principle (0–100) and providing evidence-based assessments. Results are aggregated via:

1. **IQR filtering** — removes statistical outliers before averaging
2. **Weighted aggregation** — per-principle consensus across all responding models
3. **Geometric mean** — computes final $U$ score from the three pillar averages
4. **Consensus agreement** — percentage of models that agree on STABLE vs FRAGILE verdict

The jury's independence mirrors peer review: no model knows what the others scored. The aggregate is more reliable than any single model's answer.

---

## Two Evaluation Modes

### Abstract Mode — What Is This System Like in General?
The jury evaluates the *type* of system using general knowledge, optionally grounded by a domain context file (`context/{domain}/general.md`).

```bash
python System_Stability_Score.py "Human Heart" \
  --domain biology/heart --models 20 --save
```

### Specific Mode — What Is THIS Particular Instance Like?
The jury evaluates **a specific documented instance** using ONLY the provided document. General knowledge is explicitly forbidden. If the document doesn't contain data for a principle, the score is set to 50 (neutral).

```bash
python System_Stability_Score.py "Human Heart" \
  --domain biology/heart \
  --subject subjects/Ivan_P_cardiac_report.txt \
  --subject-label "Ivan P., 55yr Male — ECG+Echo+Labs Feb2026" \
  --models 10 --save
```

This is the critical innovation: **the same framework scores both the ideal type and a real measured instance**. The gap between the two is a precise measure of how far the instance deviates from ideal stability.

---

## Real Test Results

The SSS has been validated across radically different system types, all using the same formula and the same scoring process:

### Test 1: Germany (National Governance System)
*Domain: universal | Models: 10 | Date: Feb 2026*

```
FORM     (costs Time)    ████████████████████████░  87.3/100
POSITION (costs Space)   █████████████████████░░░░  82.6/100
ACTION   (costs Energy)  ███████████████████████░░  85.2/100
─────────────────────────────────────────────────────────────
U = ∛(0.873 × 0.826 × 0.852) = 0.8503   STABLE ✓
```

**Interpretation:** Germany's constitutional form is highly stable (Form). Its geopolitical positioning (Position) shows mild vulnerability — NATO dependency, energy import exposure. Its governmental action (Action) remains effective but energy-costly in the post-2022 restructuring era.

---

### Test 2: Human Heart (Abstract Type)
*Domain: biology/heart | Models: 10 | Date: Feb 2026*

```
FORM     (costs Time)    ██████████████████████░░░  85.4/100
POSITION (costs Space)   █████████████████████░░░░  82.1/100
ACTION   (costs Energy)  ████████████████████░░░░░  80.7/100
─────────────────────────────────────────────────────────────
U = ∛(0.854 × 0.821 × 0.807) = 0.7744   STABLE ✓
```

**Interpretation:** The ideal human heart is structurally robust (Form) but pays a high energy price (Action) — it beats 3.5 billion times in a lifetime with no rest. Position is mildly costly: the heart's anatomical dependencies on the coronary supply chain make it the most catastrophic single point of failure in the body.

---

### Test 3: Ivan P., 55yr Male — Specific Cardiac Evaluation
*Domain: biology/heart | Models: 5 | Input: ECG + Echo + Labs Feb2026*

The patient document contained: BP 148/92 mmHg, LVEF 54%, LV wall 12.5mm, LA 43mm, ST depression under stress, CAC=127, LDL=4.1 mmol/L, HbA1c=5.9%, BNP=78 pg/mL.

```
FORM     (costs Time)    ████████████████████░░░░░  80.8/100
POSITION (costs Space)   ██████████████████████░░░  92.5/100
ACTION   (costs Energy)  ████████████████████░░░░░  78.3/100
─────────────────────────────────────────────────────────────
U = ∛(0.808 × 0.925 × 0.783) = 0.8364   STABLE ✓
```

**Key findings from document (selected):**
- Form gap: borderline LVEF 54% (normal ≥55%), mild LV hypertrophy — early remodeling
- Position strong: anatomical placement and hemodynamic context intact
- Action gap: stress-induced anterolateral hypokinesia, moderate LAD calcification (CAC=127)
- Risk: 10-year MACE ~12–15%

**Critical observation:** Ivan scored *higher* than the abstract ideal (0.8364 vs 0.7744). This is methodologically correct — the jury scored ONLY what the document contained. The document showed a heart that, on the measured dimensions, is performing within borders. The risks (dyslipidemia, prediabetes, smoking) affect *future* stability, not current snapshot.

---

### Test 4: LA Galaxy (MLS Team)
*Domain: sport/MLS | Models: 10 | Date: Feb 2026*

```
U = 0.7930   STABLE ✓
```

The same formula produced a valid, interpretable result for a completely different domain — no change to the framework, only the domain-specific principles changed.

---

## The Context System: Grounding AI Knowledge

A key engineering challenge is that AI models have varying domain expertise. A model trained heavily on medical literature will score a cardiac report differently than a model trained on legal texts.

The SSS addresses this through the **context system**:

```
context/
  biology/heart/general.md   ← 6,000 chars of cardiology reference
                                 (LVEF norms, CAC scoring, biomarkers,
                                  coronary anatomy, failure modes)
  sport/MLS/general.md       ← MLS-specific reference
  ...
```

**In abstract mode:** the context file is injected into every prompt alongside the principles. Models with weaker domain training are brought up to the same reference level as domain experts.

**In specific mode:** the context file is intentionally *not* injected. The subject document is the sole source of truth. This prevents the model from "filling gaps" with general knowledge when evaluating a real patient — a critical correctness property for medical or audit applications.

---

## Why the Geometric Mean Matters

Most scoring systems use additive aggregation: total score = weighted sum of components. This allows high scores in one dimension to compensate for low scores in another.

The U-Model uses the **geometric mean**:

$$U = \sqrt[3]{F \times P \times A}$$

This creates **non-compensability** — the formal property that no dimension can substitute for another. Consider:

| System | Form | Position | Action | Arithmetic mean | U-Score |
|---|---|---|---|---|---|
| System A | 100 | 100 | 0 | 66.7 | **0.000** |
| System B | 70 | 70 | 70 | 70.0 | **0.700** |
| System C | 100 | 62 | 62 | 74.7 | **0.731** |

System A would score 66.7 under additive aggregation despite being completely non-functional (Action = 0). Under U-Model, it correctly scores 0. System C scores 74.7 additively but 0.731 under U-Model — acknowledging that the Form/Action excess cannot compensate for Position's gap.

This property is essential for modelling systems where structural collapse in any single dimension is catastrophic (heart stops pumping → death; government loses territorial control → collapse; glass loses containment integrity → ceases to exist as a glass).

---

## Scalability and Universality

The SSS was designed from the start to evaluate *any* system — not a specific class. What changes between domains is the **principles** (generated by the Constructor). What stays constant is the **formula, the aggregation method, and the stability threshold**.

Systems evaluated to date (partial list):

| Category | Examples |
|---|---|
| Biological | Human Heart, A Forest |
| Political | Germany, United Nations |
| Military | NATO |
| Sports | LA Galaxy (MLS), Football clubs |
| Physical | A Glass of Water, The Eiffel Tower |
| Social | A Marriage, Democracy |
| Technical | The Internet, Quantum Computer |

The same Python scripts, the same AI jury, the same $U = \sqrt[3]{F \times P \times A}$ — across all of these.

---

## Technical Specifications

| Component | Detail |
|---|---|
| AI models | Up to 50, parallel, via OpenRouter |
| Outlier removal | IQR (interquartile range) filtering |
| Aggregation | Per-principle weighted mean → pillar average → geometric mean |
| Context injection | Auto-loaded from `context/{domain}/general.md` |
| Output | 4-page Markdown report with principle breakdown, model jury table, CI interval |
| Prompt sizes | Abstract: ~9KB | Specific: ~16KB (subject doc + principles) |
| Runtime | 30–90s for 10 models (parallel) |

**System requirements:** Python 3.12+, `OPENROUTER_API_KEY`

---

## Limitations and Open Questions

1. **Model quality variance:** 2–5 of the called models typically fail to return valid JSON for large prompts. IQR filtering compensates, but a minimum of 3–5 successful responses is needed for reliable aggregation.

2. **Principle quality:** The constructor's output depends on the architect model. Claude Opus and Kimi k2 consistently produce the most specific, falsifiable principles. Generic models produce platitudes.

3. **Temporal snapshots:** U-Score is a snapshot, not a trajectory. A heart with U=0.83 today may have U=0.60 in two years if risk factors are not managed. The framework does not yet model trend/velocity.

4. **Specific mode calibration:** When a document is sparse, many principles score 50 (neutral). This compresses the score toward 0.50 and reduces differentiation. Future work: detect and flag low-evidence scorings.

5. **Cross-domain comparability:** Is Germany's U=0.85 directly comparable to a Human Heart's U=0.77? Philosophically yes (both measure the same three prices). Practically, the principle granularity differs and a formal cross-domain normalization is ongoing research.

---

## Getting Started

```bash
git clone https://github.com/UniversalModel/System_Stability_Score.git
cd System_Stability_Score

# Set your OpenRouter API key
echo "OPENROUTER_API_KEY=sk-or-..." > ../.github/.env

# Step 1: Generate principles for your system
python 3_pillars_constructor.py --system "Your System" --n 12 --domain your_domain --yes

# Step 2a: Abstract evaluation
python System_Stability_Score.py "Your System" --domain your_domain --models 10 --save

# Step 2b: Specific instance evaluation
python System_Stability_Score.py "Your System" --domain your_domain \
  --subject path/to/document.txt \
  --subject-label "Instance Name" \
  --models 10 --save
```

---

## Conclusion

The System Stability Score makes a single claim: **every system that exists can be measured by the same three coordinates — Form, Position, Action — and the geometric mean of those coordinates is its stability score.**

This is not a metaphor. It is a formal measurement. The test results across Germany, a human heart, a sports team, and a physical object suggest the claim holds.

The implications are significant: once any system can be scored on the same scale, comparisons become possible across domains. A nation-state and a hospital and a patient and a company can all be evaluated by the same jury, using the same formula, producing comparable numbers. Not because they are the same — but because they all pay the same three prices to exist.

The framework is open source. The principles are generated by AI and can be regenerated for any domain in minutes. The evaluation costs a few cents of API credits. The result is a rigorous, evidence-grounded, multi-model consensus score for the stability of anything.

---

*System Stability Score v25 | [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)*  
*U-Model.org | [Donate.U-Model.org](https://Donate.U-Model.org)*  
*© 2026 Universal Model. License: MIT.*
