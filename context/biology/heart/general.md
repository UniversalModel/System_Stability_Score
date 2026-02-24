# Domain Context: Human Heart — Cardiology Reference

**Domain:** `biology/heart`  
**Use:** Injected into constructor (principle generation) and abstract evaluator.  
**Not used** when evaluating a specific patient (`--subject` mode).

---

## Anatomy & Structure (Form)

The adult human heart weighs 250–350 g (women) / 300–400 g (men). It has four
chambers: two atria (receiving) and two ventricles (pumping). Normal wall
thickness:
- Left ventricular (LV) wall: **6–11 mm** (diastole). ≥12 mm = hypertrophy.
- Interventricular septum: **6–11 mm**. Same threshold for hypertrophy.
- Right ventricular (RV) wall: **3–5 mm**.
- Left atrial (LA) diameter: **<40 mm** (parasternal). ≥40 mm = dilation.

Four valves ensure unidirectional flow:
- **Mitral** (MV): bicuspid, left AV valve. Area normal >4 cm². Stenosis <2 cm².
- **Aortic** (AoV): trileaflet, left outflow valve. Area normal >2 cm². Stenosis <1 cm².
- **Tricuspid** (TV): right AV valve. Regurgitation graded trace/mild/moderate/severe.
- **Pulmonary** (PV): right outflow valve.

Pericardial fluid: normal <50 mL. Effusion ≥200 mL = hemodynamic risk.

---

## Function & Hemodynamics (Action)

### Systolic Function
- **Ejection Fraction (EF / LVEF)**: normal **≥55%**.
  - Mildly reduced: 41–54%
  - Moderately reduced: 30–40%
  - Severely reduced: <30%
- **Stroke Volume**: 60–100 mL/beat at rest.
- **Cardiac Output (CO)**: 4–8 L/min at rest. CO = HR × SV.
- **Cardiac Index (CI)**: 2.5–4.0 L/min/m² (body surface area adjusted).
- **Fractional Shortening (FS)**: 25–45%.

### Diastolic Function (LV Relaxation)
- Graded by E/A ratio, tissue Doppler E' velocity, E/E' ratio.
- Normal diastolic function: E/A > 0.8, E/E' < 8.
- Grade 1 (impaired relaxation): E/A < 0.8.
- Grade 2 (pseudonormal): E/A 0.8–2 with LAVI >34 mL/m².
- Grade 3 (restrictive): E/A > 2, E/E' > 14.

### Heart Rate & Rhythm
- Normal sinus rhythm: **60–100 bpm** at rest.
- Bradycardia: <60 bpm. Tachycardia: >100 bpm.
- PR interval: 120–200 ms. QRS duration: <120 ms. QTc: <440 ms (men), <460 ms (women).
- Atrial fibrillation (AF): irregular rhythm, absent P-waves, risk of stroke.

### Blood Pressure
- Normal: <120/80 mmHg.
- Elevated: 120–129/<80 mmHg.
- Grade 1 HTN: 130–139 / 80–89 mmHg.
- Grade 2 HTN: ≥140/90 mmHg.
- Hypertensive crisis: >180/120 mmHg.

---

## Perfusion & Coronary Anatomy (Position)

### Coronary Arteries
- **Left Main (LM)**: bifurcates into LAD and LCx.
- **LAD (Left Anterior Descending)**: supplies anterior LV wall and septum.
- **LCx (Left Circumflex)**: supplies lateral and posterior walls.
- **RCA (Right Coronary Artery)**: supplies RV and inferior LV wall.

### Coronary Artery Calcium (CAC)
- **0**: no calcification, very low risk.
- **1–99**: mild calcification, low-moderate risk.
- **100–399**: moderate calcification, moderate-high risk. Consider statin therapy.
- **≥400**: severe calcification, high risk.

### Ischemia Assessment
- Stress test: ≥1 mm horizontal/downsloping ST depression = significant.
- Perfusion imaging: reversible defects = ischemia; fixed defects = infarct.
- TIMI flow grades 0–3: TIMI 3 = normal flow.

---

## Key Biomarkers (Position in metabolic context)

| Marker | Normal | Borderline | Abnormal |
|---|---|---|---|
| LDL cholesterol | <2.6 mmol/L (low-risk) | 2.6–3.4 | >3.4 → >4.1 high risk |
| HDL cholesterol | >1.0 mmol/L (men) | 0.8–1.0 | <0.8 |
| Triglycerides | <1.7 mmol/L | 1.7–2.3 | >2.3 |
| HbA1c | <5.7% | 5.7–6.4% (prediabetes) | ≥6.5% (diabetes) |
| BNP | <35 pg/mL | 35–100 | >100 (heart failure likely) |
| NT-proBNP | <125 pg/mL | | >125 (age-adjusted thresholds) |
| hs-CRP | <1 mg/L | 1–3 | >3 (high CV risk) |
| Troponin I | <0.04 ng/mL | | >0.04 (myocardial injury) |
| Creatinine | 60–110 µmol/L | | >110 (renal dysfunction → cardiorenal) |

---

## Risk Stratification

### 10-Year MACE (Major Adverse Cardiovascular Events) Risk
- Low: <5%
- Moderate: 5–10%
- High: 10–20%
- Very High: >20%

### Major Risk Factors
- Age (men ≥45yr, women ≥55yr)
- Hypertension (BP ≥130/80)
- Dyslipidemia (LDL >2.6 mmol/L)
- Diabetes / prediabetes (HbA1c ≥5.7%)
- Smoking (current or <10yr cessation)
- Obesity (BMI ≥30, waist >102 cm men / >88 cm women)
- Family history of premature CVD (1st-degree, men <55yr, women <65yr)
- Chronic kidney disease (GFR <60 mL/min)
- Atrial fibrillation
- Prior MI or revascularization (very high risk category)

---

## Failure Modes & Stability Conditions

| System Component | Normal Stability Condition | Failure Signal |
|---|---|---|
| Myocardium | LVEF ≥55%, WMAs absent | LVEF <40%, regional wall motion abnormalities |
| Valves | No significant stenosis/regurgitation | Severe regurgitation, area <1 cm² (aortic stenosis) |
| Conduction | Sinus rhythm, PR/QRS normal | AF, bundle branch block, AV block |
| Coronary supply | TIMI 3 flow, no ischemia | ST changes on stress, fixed/reversible perfusion defects |
| BP regulation | <120/80 at rest | ≥140/90 sustained |
| Metabolics | LDL<2.6, HbA1c<5.7%, BNP<35 | LDL>3.4, HbA1c≥6.5%, BNP>100 |
| Renal-cardiac axis | Creatinine normal, eGFR >60 | Progressive cardiorenal syndrome |
| Pericardium | Fluid <50 mL | Effusion >200 mL (tamponade risk) |

---

## Standard Treatment Thresholds

- **Statin indicated**: LDL >2.6 + intermediate/high risk OR CAC ≥100
- **Antihypertensive**: BP ≥130/80 with risk factors; ≥140/90 always
- **Anticoagulation (AF)**: CHA₂DS₂-VASc ≥2 (men) / ≥3 (women)
- **ICD**: LVEF ≤35% despite 3-month OMT for primary prevention
- **Revascularization (PCI/CABG)**: significant proximal stenosis ≥70% (≥50% LM) with symptoms or ischemia

---

## Lifespan & Endurance (Form — Time Cost)

- Heart beats ~100,000 times/day, ~3.5 billion times in a lifetime.
- Cardiomyocytes renew at ~1%/year; most adult cardiomyocytes are life-long.
- Fibrosis accumulates with age, hypertension, and ischemic injury.
- Hypertrophy is initially adaptive (increased wall stress) → maladaptive at sustained
  levels → dilated cardiomyopathy.

---

*Source: Adapted from ACC/AHA, ESC Guidelines, and standard clinical cardiology references.*  
*Last updated: February 2026.*
