# APPENDIX PMD — Position–Mass Duality

**The context-price of a definite location — how *localization* is bought with mass as well as with space.**

> *The title is **historical** (v1.0). The canonical law is the v1.5.2 restatement in §5: Position's two sub-meters are **distinguishability** `P_S` and **localization accessibility** `P_L`, with mass a capacity proxy **inside** `P_L` in the massive sector only.*

A U-Theory appendix on the **Position ↔ Space** currency. Position carries two non-compensable sub-meters — **spatial/contextual distinguishability** `P_S` and **localization accessibility** `P_L` — combined as `P = √(P_S·P_L)` so that `U = ∛(F·P·A)` is untouched. **In the massive one-particle rest-frame sector**, invariant mass supplies *one capacity proxy* inside `P_L` via the reduced Compton scale `ƛ_C = ħ/(mc)`. Mass is **not** a fourth pillar, and **not** a universally required sub-price: massless quanta pay `P_L` through detection alone.

## Structure (single document, two parts)

- **Part I (§0–§8) — Interpretation.** What the duality means, its honest scope, where it is speculative. **L3/L4.**
- **Part II (§9–§30) — Formal layer.** What is **proved**, what is a **declared modelling choice**, and what is **forbidden** without a new observable. Per-result epistemic labels throughout.

## What Part II establishes

| Result | Statement | Level |
|---|---|---|
| **PMD-1** | `m·ƛ_C = ħ/c` | L1 identity |
| **PMD-2** | `F_Q ≤ 8mK/ħ²` — valid **iff** `K ≡ ⟨p̂²⟩/2m`; strictly non-relativistic | L2 (NR only) |
| **PMD-2R** | `F_Q ≤ 4(⟨Ĥ²⟩−m²c⁴)/(ħ²c²)` — one particle, free, positive-energy, `⟨Ĥ²⟩<∞` | L2 |
| **PMD-3** | `J_𝒞 = Σ Jₖ` for **product / conditionally independent** channels only | L2 |
| **PMD-4** | `J_Z ≤ J_Y` under a **parameter-independent** coarse-graining kernel | L2 |
| **PMD-5** | `g_M(x) = x^α/(1+x^α)` from a log-odds axiom | L3 conditional |
| **PMD-6** | Nested-mean uniqueness `P = √(P_S·P_L)` within the declared axiom set | L3 conditional |
| **PMD-7** | Elasticity split `1/6 + 1/6 = 1/3` — the nesting does not double-weight Position | L2 |
| **PMD-8** | `Mc² = E_COM` exact; the kinetic/field/interaction split is **partition- and scheme-dependent** | L1 + caveat |
| **PMD-9** | **No-go:** `C = f(X_std) ⇒ I(Y;C\|X_std) = 0` (proved by conditional independence) | L1 |
| **PMD-10** | `J_𝒞 = ε·u·(8mK/ħ²)` — a **definitional decomposition**, content in the scoped ranges | L3 |
| **PMD-11** | Reference-scale invariance: **holds per meter**; **fails** for the combined score. Dominance ⟹ robust (converse false) | L2 both ways |
| **PMD-12** | `𝔼[Δ log-loss] = I(Y;C_R\|X_std)` for the **true** conditionals | L1 + estimator caveats |

**Core claim (not "mass = context"):** *mass scales a localization-capacity bound; context determines measurement access.* Formally `J_𝒞 ≤ F_Q ≤ 8mK/ħ²` (NR budget).

## Honest status

- **No new physics.** PMD does not modify GR or QFT; it re-describes established estimation theory and relativistic kinematics in F/P/A terms.
- **No present empirical surplus.** PMD-9 *proves* this holds until an independent context observable `C_R` with `I(Y;C_R|X_std) > 0` is supplied. PMD-12 gives the effect size in **nats**.
- **One concrete falsifiable ceiling:** `Var(x̂) ≥ ħ²/(8NmK)` (NR) — a consequence of standard quantum estimation theory, offered as a test of PMD's *framing*, not of new physics.
- The appendix **records its own corrected errors** rather than removing them: seven errors found across two rounds of adversarial review are corrected *and kept visible* in the changelog (v1.5 → v1.5.1 → v1.5.2 → v1.5.3), with superseded claims marked inline so no historical row reads as current fact.

## Canonical location

> **This folder is the single source of truth for PMD.** The appendix was briefly duplicated at the corpus root (`v.28\.md\APPENDIX_PMD_*`); those copies were removed on 2026-07-25 after verifying they were byte-identical, and `APPENDIX_MASTER_INTEGRATION_MAP.md` + `THEORY_OF_EVERYTHING_v31.index.md` now point here. **Edit only this copy** — a second copy is how the v1.5.1 → v1.5.3 contradictions arose in the first place. The GitHub mirror is `System_Stability_Score/PMD/`.

## Files

- [`APPENDIX_PMD_POSITION_MASS_DUALITY.md`](APPENDIX_PMD_POSITION_MASS_DUALITY.md) — the appendix (v1.5.3).
- [`APPENDIX_PMD_POSITION_MASS_DUALITY.md.pdf`](APPENDIX_PMD_POSITION_MASS_DUALITY.md.pdf) — rendered PDF.
- [`pmd_scale_sensitivity.py`](pmd_scale_sensitivity.py) — reproduces every numerical figure in §16.1 (reference-scale sensitivity), the PMD-2R violation factor, and the PMD-10 mass elasticity. Pure standard library; `python pmd_scale_sensitivity.py`.

> The explicit counterexamples in §16.1 are **proofs**; the percentages are **design-dependent Monte-Carlo figures** whose seeds and sampling ranges are declared in the script.

## Provenance

- **Parent record:** U-Theory / U-Model — DOI [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR) · https://u-model.org
- **Author:** Petar Nikolov (ORCID [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276)).
- **License:** CC BY 4.0 (text) / MIT (code).
