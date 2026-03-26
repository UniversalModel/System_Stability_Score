# U-Theory v26 — Appendices Overview

> **v26 Invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy  
> **Author:** Petar Nikolov · Sofia · March 2026  
> **DOI:** [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)

---

## Canonical Chain

```text
U-Theory (L1 ontology)
     ↓
GSI-RTD (L3 search architecture — derived via L2 isomorphisms)
     ↓
TAA (L2 agent shell) → LGP-12 (L2 procedural cycle)
     ↓
SSS (L2 measurement engine)
     ↓
Scheduler (learning law → next generation)
```

---

## Appendix Map

| File | Short | What it answers | Start here if you… |
|------|-------|-----------------|---------------------|
| [`APPENDIX_GSI-RTD`](APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md) | **G** | How does triadic decomposition create General Superintelligence? | Want the big picture: search space, Scheduler, combinatorial theorem |
| [`APPENDIX_TAA`](APPENDIX_TAA_TRIADIC_AI_AGENTS.md) | **T** | Which 4 agents do I need and how do they interact? | Want to build the multi-agent system |
| [`APPENDIX_LGP`](APPENDIX_LGP_Lady_Galaxy_Protocol.md) | **L** | How do the agents proceed step-by-step in time? | Want the 12-step operational checklist |
| [`APPENDIX_SSS`](APPENDIX_SSS_SYSTEM_STABILITY_SCORE.md) | **S** | How do I measure stability and get a verdict? | Want a numerical score for any system |

---

## How They Connect

```text
┌─────────────────────────────────────────────────────┐
│                     GSI-RTD                         │
│  Recursive Triadic Decomposition + Scheduler        │
│  (search space, hard gates, geometric ranking)      │
└────────────────────┬────────────────────────────────┘
                     │ spawns
          ┌──────────┴──────────┐
          │                     │
    ┌─────┴─────┐         ┌────┴────┐
    │    TAA    │         │   LGP   │
    │  4 agents │◄────────┤ 12 steps│
    │ F,P,A,Σ  │ populates│ in time │
    └─────┬─────┘         └────┬────┘
          │                     │
          └──────────┬──────────┘
                     │ produces data for
              ┌──────┴──────┐
              │     SSS     │
              │ U, δ, SI    │
              │ verdict     │
              └──────┬──────┘
                     │ feeds back to
                     ▼
              Scheduler (next generation)
```

---

## Key Formulas (identical across all appendices)

| Formula | Meaning |
|---------|---------|
| $U = \sqrt[3]{F \cdot P \cdot A}$ | Geometric mean — non-compensatory |
| $\delta = \frac{\max - \min}{\max + 0.01}$ | Imbalance penalty |
| $SI = \frac{U}{(1+\delta)^2}$ | Stability Index |
| $\|S^{(d)}\| = k^{3^d}$ | Combinatorial search space at depth $d$ |

---

## Reading Order

1. **New to U-Theory?** → Start with SSS (smallest, most concrete)
2. **Want to implement agents?** → TAA → LGP → SSS
3. **Want the full theoretical picture?** → GSI-RTD (§1–§12) → TAA → LGP → SSS → GSI-RTD (§20–§34)

---

*Part of the Universal Stability Model (U-Theory)*  
*GitHub: [github.com/UniversalModel/System_Stability_Score](https://github.com/UniversalModel/System_Stability_Score)*
