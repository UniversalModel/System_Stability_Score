# APPENDIX PMD — POSITION–MASS DUALITY
## The Context-Price of a Definite Location — how *localization* is bought with **mass** as well as with **space**

> *"To be anywhere in particular, a thing must pay twice: once in space, by giving up everywhere; and once in mass, by letting the rest of the universe hold it in place. A 'here' is context that has begun to weigh."*
> — Petar Nikolov, opening the PMD hypothesis, 2026-07-19
>
> *(Figurative framing, and **historical**: the title and epigraph date from v1.0, when the second sub-price was still read as "Mass". **The canonical law is §5 as restated in v1.5.2** — Position's two sub-meters are *distinguishability* `P_S` and *localization accessibility* `P_L`, with mass a capacity proxy **inside** `P_L` in the massive sector only. The defensible core claim is **not** gravitational weight or a literal Machian mechanism — it is §30's Localization-Leverage: mass sets localization **capacity**, context realizes **access**. The Machian reading is flagged open throughout, §4 / §8 / §30.)*

---

**Author:** Petar Nikolov (ORCID 0009-0001-8669-2276)
**Date:** 2026-07-19
**Framework:** U-Theory v31 · deepens the **Position ↔ Space** currency
**Status:** **L3 / L4 SPECULATIVE (Part I) + L1/L2/L3 FORMAL (Part II)** — a coherent *interpretive* extension of the canon, **NOT** a derivation of new physics, **NOT** a modification of GR or QFT. **(v1.5.3 — formal layer: PMD-2R/10/11/12 added in v1.5; **seven errors found by two rounds of adversarial review have been corrected and are recorded in the changelog, not removed** — see it for the full list. v1.5.3 clears the remaining stale cross-references so §1, §5, the CEPT map and the roadmap agree with the corrected §5 law and the `0 < η < 1` adapter.)**
**Date (this revision):** 2026-07-25
**Prerequisites:** the core triad `Form↔Time · Position↔Space · Action↔Energy`; `APPENDIX_MMT` (Meaning–Matter Transformation), `APPENDIX_DIM` (Dimensionless Meaning), `APPENDIX_ST` / DPR (Dimensional Price Registry), `APPENDIX_QMC` (measurement collapse), `APPENDIX_GEN` (Genesis Law), `APPENDIX_SSS` (the score); for Part II, basic quantum estimation theory (Fisher information, Cramér–Rao, quantum Fisher information) and `APPENDIX_RH` (null-model / rival discipline).

> **How to read this document.** **PART I (§0–§8)** is the *interpretation*: what the Position↔Mass duality means, its honest scope, and where it is speculative (L3/L4). **PART II (§9–§30)** is the *formal layer*: what can actually be **proved** (identities and information inequalities, L1/L2), what is a **declared modelling choice** (the `[0,1]` meters, L3), and what is **forbidden** without a new observable (the no-go theorem). If you want anything quantitative, go to Part II. **Minimal reading paths:** *conceptual reader* — Part I only, stop at §8; *quantitative user* — §12 (the bound), §17 (the adapter), §23 (the no-go), §30 (the core claim).

---

# ═══════════════════ PART I — INTERPRETATION ═══════════════════

## 0. What this appendix IS and IS NOT

| This appendix **IS** | This appendix **IS NOT** |
|---|---|
| A sharpening of the **Position** currency: a location has *two* non-substitutable prices, not one | A new ontology or a new fundamental theory |
| A reading of the real, textbook link between **mass and localizability** through the F/P/A lens | A derivation from the L1 axioms |
| Anchored on established physics where it is established (Compton wavelength, inertia) | A claim to overturn or replace GR / QFT |
| Explicit about which step is rigorous and which is speculative interpretation | A claim of empirical proof of "context = mass" |
| Marked **L3/L4 speculative** throughout, with honest failure hooks (§8) | A claim that a delocalized state *must* be massless (it need not — §8) |

**Core thesis (domain-limited).** *Position ↔ Space* is the canon. PMD adds a **narrower** bridge: **for a massive one-particle state in a chosen rest-frame description**, invariant mass fixes the reduced-Compton scale `ƛ_C = ħ/(mc)` at which a fixed-particle-number localization becomes QFT-sensitive, and it sets the **inertial response to changes in momentum**. U-Theory reads these two roles as a **mass-sensitive sub-meter within the Position pillar** — *one* proxy for localizability, not a universal one. **Massless field excitations (photons) need a separate localization/detection meter and are NOT assigned zero Position merely because their invariant mass vanishes** (§5, §8).

---

## 1. The question (stated cleanly)

The canon says **resistance-against-Form = Time**, **resistance-against-Position = Space**, **resistance-against-Action = Energy**. Position is priced in Space: to occupy a unique location you must **exclude** a region — you give up being everywhere.

But a location has a *second* face the canon leaves implicit:

- For a **massive** particle, a sharp rest-frame **"here"** is bounded below by the reduced-Compton scale `ƛ_C = ħ/(mc)`, so mass **sets the rest-frame localization scale** *(it does not follow that massless quanta cannot be localized at all — §8)*.
- To **change its state of motion**, a system must overcome **inertia** — resistance to a *change of momentum*, `F = dp/dt` (reducing to `F ≈ m·a` only for `v ≪ c`).

So the Position currency splits into two coupled sub-meters — **spatial/contextual distinguishability** (the exclusion/extent face, `P_S`) and **localization accessibility** (`P_L`), **inside which invariant mass is one capacity proxy, valid in the massive rest-frame sector only** (§5). This appendix makes that duality explicit and connects it to the rest of the corpus. *(Mass is deliberately **not** named as the second sub-price: the appendix's own massless branch pays `P_L` through detection alone — see §5, §6, §8.)*

---

## 2. The rigorous anchor — the Compton wavelength (established physics)

This section is **not** speculative. It is textbook relativistic quantum mechanics, and it is the load-bearing core on which the interpretation rests.

The **Compton wavelength** of a particle of mass `m` is:

```
ƛ_C = ħ / (m·c)          (the REDUCED Compton wavelength)
λ_C = h / (m·c) = 2π · ƛ_C   (the ordinary Compton wavelength)
```

It is the **characteristic scale at which a fixed-particle-number, one-particle description becomes unreliable** (QFT particle-production becomes relevant) — **not** an unconditional, Lorentz-invariant minimum width of every possible state. Sketch: to pin a particle to a region of size `Δx` you must inject momenta of order `ħ/Δx` (uncertainty principle), i.e. energies of order `ħc/Δx`. Once `Δx ≲ ƛ_C`, that energy reaches `~m·c²` — enough to **pair-create** — and the very idea of "one particle at a point" dissolves. Consequences (within the one-particle description):

- **`m → 0` ⇒ `ƛ_C → ∞` ⇒ no rest-frame one-particle localization scale.** A massless excitation (the photon) has **no rest frame** and no standard sharp one-particle position operator (there is none for massless spin > ½), so it cannot be pinned as a rest-frame "here." *(Nuance, §8: it CAN still be prepared as a finite wave packet and register **local detection events** — masslessness forbids the rest-frame particle-"here", not every local detection.)*
- **Larger `m` ⇒ smaller `ƛ_C` ⇒ a finer one-particle localization scale.** Mass **sets** that scale (and the inertial response, §3); PMD reads it as the *mass sub-price* of a definite Position.

> **Rigorous takeaway (physics, not analogy):** mass **sets the finite one-particle, rest-frame localization scale `ƛ_C`** and the inertial response. More mass → a finer rest-frame "here"; zero mass → no rest-frame "here" (local detections still occur). PMD *reads* this scale as the mass sub-price of Position — the physical fact (the scale) is not in dispute, only the reading is.

> **Technical note — reduced scale & localization scope.** Here `ƛ_C = ħ/(mc)` is the **reduced** Compton wavelength (ordinary `λ_C = h/(mc) = 2π·ƛ_C`). The localization claim is about the breakdown of a **stable one-particle, rest-frame** description: confining a *massive* particle to `Δx ≲ ƛ_C` makes particle creation relevant. For *massless* quanta (photons) the point is not that no local detection can occur, but that there is **no rest frame** and **no standard sharp Newton–Wigner one-particle position observable**. PMD reads mass as *enabling a finite rest-frame localization scale*, not as the sole cause of all spatial detection.

---

## 3. The second face — inertia (the price of *changing* a location)

Newton, relativistically safe: **`F = dp/dt`** with **`p = γ·m·v`**, reducing to **`F ≈ m·a`** only for `v ≪ c`. **Inertial mass is resistance to a *change of motion / position*** (acceleration). Placing this beside the canon:

| what is being resisted | the price (currency) |
|---|---|
| Form being changed (endurance in time) | **Time** |
| **occupying** a location (exclusion in space) | **Space** |
| Action being performed (work) | **Energy** |
| **changing** its state of motion (acceleration / Δmomentum) | **Mass (inertia)** |

> **Note (mass is not a fourth pillar).** This row places **Mass** beside Time/Space/Energy only to display the *parallel structure* of "what is resisted → the price." It does **not** promote mass to a fourth top-level currency. Mass is a **sub-price nested inside the Position pillar** — the inertial/localizability face of Position ↔ Space — formalized in §5 as `P = √(P_S · P_L)`, where the mass proxy `P_M` is one component of `P_L`, not a peer of `F`, `P`, `A`. The core triad remains `U = ∛(F · P · A)`. *(Proved unique in Part II, §19 / PMD-6, with the elasticity split in §20 / PMD-7 showing the nesting does not double-weight Position.)*

So mass plays **two** roles for Position: it sets the *rest-frame localization scale* (§2) **and** the *inertial response to a change of momentum* (§3) — **not** a "cost of moving" (a free body coasts arbitrarily far at constant momentum with no force; mass resists **acceleration**, not displacement). Space answers *"is the system relationally distinguishable / placeable?"*; mass answers *"what is its rest-frame localization scale and inertial response?"* — the spatial face and the inertial face of one currency.

---

## 4. Mass as *concentrated context* (the interpretive leap — L3)

Why *read* mass as "context"? Because **several** mass contributions and effective inertial parameters are **interaction- or environment-dependent** — *without* this meaning that **all** invariant mass is relational:

- **Mach's principle.** Inertial mass is (on the Machian reading) determined by the distribution of **all other matter** in the universe — inertia is a relation to the cosmic context, not an intrinsic label. *(Status honestly stated: Mach's principle is a real, historically central idea — it motivated Einstein — but it is **not fully established** in GR; frame-dragging realizes it only partially. See §8.)*
- **The Higgs mechanism.** In the Standard Model, elementary fermion and weak-boson masses arise from **coupling to the nonzero Higgs vacuum expectation value** — an *interaction-generated* mass term, **not** friction or drag through a medium. A field without such a coupling gets no Higgs mass term. PMD reads this *interaction origin* of some mass as context — but the Higgs mechanism does not by itself establish that reading, and most of the mass of ordinary matter is **QCD dynamics, not Higgs** (§8).
- **Relational position** *(philosophical, not a physics result).* A "here" is defined only **against** a context of other things; with no context, "here" has no referent.

**Scope (honest).** Mach's principle is an *open* hypothesis (only partially realized in GR via frame-dragging); the Higgs mechanism is *specific and established*; relational position is *philosophical*. PMD interprets the **interaction-dependence** of mass as context — it does **not** claim that *all* invariant mass is Machian or relational.

**U-Theory reading (speculative, L3):** *mass is what a system pays to be **counted as somewhere** by the rest of the universe.* Concentrate context → localizability and inertial response appear together; remove context → the system delocalizes and its "here" dissolves. This is `APPENDIX_MMT` at the Position axis: MMT says **matter = crystallized meaning**; PMD says, more specifically, **mass = crystallized context** — the Position-currency's share of that crystallization. *(Epigraph "begun to weigh" is figurative; the body claim is inertial mass / rest-frame localizability, not gravitational weight.)*

---

## 5. The dual price of Position (the law)

> ### ⬛ THE POSITION LOCALIZATION LAW (PMD)
> **Position has two non-compensable sub-meters — and mass is a proxy inside the second, not one of the two (v1.5.2 restatement):**
> **(i) Spatial / contextual distinguishability (`P_S`):** become relationally placeable — a constrained spatial support and a context-resolved "where," measured against a declared reference prior. *(Exclusion / non-overlap is **one** realization, not the universal definition — bosons and fields can share support.)*
> **(ii) Localization accessibility (`P_L`):** the degree to which a "here" can actually be resolved. **In the massive one-particle rest-frame sector**, invariant mass supplies *one capacity proxy* for this face — it sets the localization scale (reduced Compton `ƛ_C = ħ/mc` finite) and the **inertial response to a change of momentum** (`F = dp/dt`, i.e. `F ≈ m·a` for `v ≪ c`) — *not* a resistance to displacement itself. **Outside that sector (massless quanta) `P_L` is carried by the detection channel alone and mass plays no role.**
>
> *(Why the restatement: the earlier wording — "the two sub-prices are Space and Mass" — is contradicted by this appendix's own massless branch `P_L = P_D`, in which no mass is paid yet Position is nonzero. Mass is universally a **proxy within** `P_L`, never a universally required sub-price.)*
> **The zero-mass limit is NOT automatically "delocalized" (v1.2.1 correction).** At `m → 0` the **massive rest-frame localization channel `P_M` vanishes** (`ƛ_C → ∞`; no rest frame; no rest-frame "here"; **zero invariant rest mass**, yet still carrying energy-momentum and gravitating, at the speed of light). But the overall localizability meter `P_L` need **not** be zero — a massless quantum is still scored through the detection channel `P_D` (the massless adapter `g_0`), so it is **not** misclassified as zero-Position. A genuinely *unpaid* Position requires **both** `P_S → 0` **and** `P_L → 0`. **Localization is the crystallization of context into a finite localization scale — carried by mass in the massive rest-frame sector, and by the detection channel for massless quanta.**

| face of Position | currency | physics anchor | the zero-limit (unpaid) |
|---|---|---|---|
| **be relationally placeable** | Space (spatial support / distinguishability) | constrained support; context-resolved placement | no distinguishable "where" — the canon's `P→0` |
| **be localizable & resist Δmomentum** | **`P_L` — localization accessibility** *(mass is a proxy inside it, massive sector only)* | `ƛ_C = ħ/mc`; `F = dp/dt`; Mach; Higgs | `ƛ_C → ∞`: the **mass channel `P_M`** vanishes (no rest-frame "here", no rest inertia; still carries `E`–`p`) — but `P_L` via `P_D` need not vanish |

Both **sub-meters** (`P_S`, `P_L`) must be nonzero for a system to *have a position at all* — but note this is a statement about `P_S` and `P_L`, **not** about mass: a massless quantum pays `P_L` through detection alone. A system rich in one sub-meter and starved of the other has an **ill-defined** Position — which, under `U = ∛(F·P·A)`, drags the whole product down (non-compensation).

**Operational placeholder for "context" (upgraded in Part II).** In this appendix, **context** is a *working label* for the interaction / environment dependence that makes a system's "here" and inertial response well-defined. The minimal placeholder is:

```
Context_proxy  ≔  { couplings, boundary conditions, reference frame,
                    and co-present degrees of freedom that enter the
                    system's localization or inertial description }
```

This is **not** a claim that context is a new observable, nor that it equals invariant mass. **Part II (§10, §14) upgrades this placeholder to a concrete definition:** context ≔ the **measurement channel `𝒞`** itself (`p(y|x,𝒞)`); its *localization content* is quantified by the **Fisher information `J_𝒞`** about the position parameter `x`, with additivity across independent channels (PMD-3) and a data-processing bound (PMD-4). *(The channel is the object; `J_𝒞` is how much it tells you about **where**.)* Every numerical use of PMD must still declare its own proxy explicitly (§8).

**Nesting (keeps Position as ONE pillar — not a fourth price), with a domain gate.** The two faces compose *inside* Position, geometrically, so a zero in either zeros Position. The localizability face is a **general localization/detection meter `P_L`**, defined **(v1.4, adopting §17)** as a weighted geometric blend of a **detection channel `P_D`** and the **mass-capacity proxy `P_M`**, with the **pre-registered default `η = ½`**:

```
POSITION ↔ SPACE
   ├─ P_S : constrained spatial support / relational distinguishability     ∈ [0,1)
   └─ P_L : localizability / localization-detection meter                   ∈ [0,1)
            ├─ massive rest-frame sector : P_L = P_D^(1−η) · P_M^η ,  η = ½ default   (§17)
            │        P_D = detection/Fisher channel (§15) ;  P_M = g_M(L*/ƛ_C) (§16)
            │        η is STRICTLY interior: 0 < η < 1  (endpoints break the controls, §17)
            └─ massless field sector     : P_L = P_D = g_0( Pr[detect in R,Δt], σ_R, frame )

   P = P_PMD = √( P_S · P_L )        U = ∛( F · P_PMD · A )
```

This blend discharges the two key negative controls **by construction** (§8, §17): a *massive-but-delocalized* state has `P_D = 0 ⇒ P_L = 0`; a *massless-but-detected* quantum has `P_L = P_D > 0` (never zero-Position). Mass is **not** a fourth top-level pillar; it is **one component** (via `P_M`) of the nested `P_L` meter. **The mass-only reading `P_L = P_M` is *not* a value of the canonical adapter:** `η = 1` breaks the massive-but-delocalized control (and `0⁰` is indeterminate), so `0 < η < 1` is required and mass-only survives only as a **separate legacy comparator** in the model comparison (§17, §29). `g_M`, `g_0`, `η`, the reference scale `L*`, the normalization, and a missing-data rule are **declared before use** and are **calibration candidates, not canon** (§8). *(Part II §16–§17 derives the admissible forms and the adapter; `η` must be pre-registered, never fit post hoc.)*

---

## 6. The conjugacy — position, momentum, and the massless limit

A **massless** excitation (e.g. a photon) has **no rest frame** and **no massive-particle rest-frame localization scale** — it is not a little ball with a coordinate. But it is **not** "everywhere": a single-photon **wave packet** can be prepared with finite spatial–temporal localization and produce **local detection events** (there is simply no sharp Newton–Wigner one-particle position observable for it). So masslessness removes the *rest-frame particle-"here"*, **not all localization.** Acquiring mass gives a massive particle a rest-frame localization scale (`ƛ_C`) and an inertial response — it does **not** follow that massless quanta cannot be localized at all.

This mirrors the **position–momentum uncertainty** `Δx·Δp ≥ ħ/2`: a sharp "here" (`Δx` small) costs a large momentum spread. **The conjugate of position is momentum, not mass** — but mass enters the trade through the relativistic dispersion `E² = p²c² + m²c⁴` and the localization scale `ƛ_C = ħ/mc`. (In general `p = γ·m·v`; a photon carries `p = E/c` despite **zero** rest mass — so `p = m·v` is only the `v ≪ c` approximation and is never applied here to massless or relativistic cases.) Sharpening a "here" costs momentum spread; for a **massive** particle **mass sets the rest-frame scale** of that trade. But it is **momentum, not mass**, that is conjugate to position — and a massless quantum can still be wave-packet-localized. The defensible statement is **not** "delocalized ↔ massless"; it is only that mass **sets a massive particle's rest-frame localization scale.**

---

## 7. Binding it to the whole corpus

- **`SSS` / `U = ∛(F·P·A)`:** the **Position pillar** now carries an explicit *dual meter* — spatial support / distinguishability **and** localizability (with mass as one proxy). A system with strong Form and Action but near-zero relational placement / localizability has a near-zero Position, so `U` collapses. This is the **physical face** of the corpus's central thesis (autobiography, POS): *strong Form and Action do not compensate a Position near zero.* *Illustrative flavour only (not a classification):* a system rich in Form and Action but poor in relational placement / localizability scores low on Position and, by non-compensation, low on `U`. **This must not be read literally for a photon** — a massless quantum is locally detectable and is *not* zero-Position (§5 adapter `g_0`, §8).
- **`MMT`:** matter = crystallized meaning; PMD refines the Position axis — **mass = crystallized context** *(interpretive)*. The Big Bang as maximal concentration (`max ℳ`) is, *under the Machian reading* (§4, §8 — an open question, not settled physics), context concentrating until inertial response appears; without that reading, the same event is simply maximal energy density, and PMD adds no extra claim.
- **`DIM`:** required meaning scales with dimension; localization is a *spatial-dimensional* act, and PMD says the massive rest-frame sector of that act is paid partly in mass/context.
- **`QMC` (measurement):** a **localized position measurement records a localized outcome** and, under standard state-update modelling, **conditionally prepares a more localized post-measurement state** — via an interaction (context) with an apparatus. PMD reads that interaction as paying the context price, without committing to any one interpretation of measurement. *(Formalized in Part II §11–§15: the apparatus channel contributes Fisher information `J_𝒞` about position.)*
- **`POS` (Principle of Sequence):** `F → P → A`. Physically, a system needs **Form** (persistence in time) and then a **Position** (a "here," bought with space **and**, in the massive sector, mass/context) *before* it can spend **Energy** in Action. No "here" → no base to act from — the Forbidden Action at the level of physics.

---

## 8. Falsifiability and honest scope

**What is rigorous (not speculative):**
- `ƛ_C = ħ/mc` (reduced) as the **one-particle, rest-frame** localization scale; `m → 0 ⇒` no rest-frame localization scale, `m ↑ ⇒` a finer one — standard relativistic QM.
- Inertia as resistance to a *change of momentum* (`F = dp/dt`; `F ≈ m·a` only for `v ≪ c`) — standard mechanics.
- Mass from Higgs coupling — Standard Model. **Caveat:** the Higgs gives **elementary** rest masses; **most** of the mass of ordinary matter (protons, neutrons) is **QCD binding / field energy**, not a Yukawa coupling. PMD reads both as *context becoming inertial* — but only the Higgs part is a *direct* SM mass-generation mechanism. *Why the composite (QCD) case strengthens the reading rather than weakening it:* nucleon mass is not carried by its constituents in isolation — it is the **energy of the internal interactions** (gluon fields, confined quark motion) of the system *with itself*. A proton's inertia is therefore the inertial face of its own **internal relational context** — the "mass = crystallized context" reading applied to a system's interactions with its own parts, exactly the composite it is meant to describe. The Higgs case is *interaction with an external field* (the VEV); the QCD case is *interaction of the system with itself* — both are context becoming inertial, and the second is the more direct instance. *(Avoid "weight" language here: the claim is about inertial mass / rest energy, not gravitational weight. The signed mass-defect subtlety — QCD adds mass, nuclear/atomic binding subtracts it — is formalized in Part II §22 / PMD-8 as `χ_int`.)*

**What is speculative interpretation (L3/L4), and its honest hooks:**
- **"Mass = concentrated context / the Position-currency's inertia face"** is a *reading*, not a derivation. It does not add to or modify GR/QFT; it re-describes them in F/P/A terms.
- **The strong converse — "no location ⇒ no mass" — is NOT standard physics and is flagged as the most speculative claim.** A *delocalized but massive* state exists in ordinary QM (a momentum eigenstate of a massive particle is spread over all space yet has mass). PMD's honest claim is the *rigorous direction only*: **masslessness forbids the rest-frame particle-"here"** (no rest frame; no sharp one-particle position operator for the photon), **while mass enables a finite localization scale**; local detection of massless quanta still occurs. The reverse (delocalized ⇒ massless) is offered as a suggestive lens, not asserted.
- **Mach's principle is genuinely open.** If inertia were shown to be entirely independent of the cosmic matter distribution, the "context confers mass" reading weakens to a metaphor. If frame-dragging / relational-inertia results strengthen the Machian picture, it strengthens. PMD is therefore **hostage to a real open question in physics**, and says so.

**Null model, empirical content, and required controls (RH).**
- **Present empirical content (honest):** as of v1.5, PMD makes **no observation that standard ƛ_C, relativistic kinematics, QFT, and GR do not already make** — the one concrete falsifiable ceiling it now states (`Var(x̂) ≥ ħ²/(8NmK)`, §12.1) is a consequence of *standard* quantum estimation theory, not new physics. The functions `g_M`, `g_0`, and the scale `L*` are calibration candidates, not fitted laws. This is not a soft admission — Part II **proves** it: the **no-go theorem (§23 / PMD-9)** shows that if the PMD context variable is any deterministic function of the standard variables, `C = f(X_std)`, then `I(Y ; C | X_std) = 0` for every observable `Y`. **PMD earns empirical content only against an independently measured context observable `C_R` with `I(Y ; C_R | X_std) > 0`.**
- **Null model:** `H₀: every observation is explained by the standard ƛ_C, pᵘ, and QFT/GR, with no PMD context variable.`
- **What would count as content:** a mass/localization meter that is (i) independently measurable, (ii) adds predictive power over `H₀`, and (iii) never misclassifies massless, locally-detected systems.
- **Required negative controls before any use:** **(a) massive-but-delocalized** (a momentum eigenstate — massive yet spread out → refutes "delocalized ⇒ massless"); **(b) massless-but-locally-detected** (a photon wave packet → refutes `P_L = 0` for massless); **(c) inertial-motion null** (constant-velocity coasting, no force → refutes "mass resists displacement"); **(d) `P_S`-only rival** (must the mass sub-meter beat a Position score built from spatial support alone?). *(These are discharged by construction in the upgraded adapter, Part II §17.)*

**Epistemic level (Part I):** **L3/L4 speculative** — a coherent, corpus-consistent *interpretation* resting on a rigorous physical core. It makes no claim of empirical proof and adds no new governing equation. It sharpens the meaning of the Position currency; it does not re-derive physics. *(The formal core that IS provable — the localization–energy bound, Fisher additivity, the nested-mean uniqueness, and the no-go — is Part II.)*

---

# ═══════════════════ PART II — FORMAL LAYER (PMD-MATH) ═══════════════════

> **From philosophical analogy to a formal measurement framework** — what can be *proved*, what is a *modelling choice*, and what is *forbidden* without a new observable.
>
> **One-line thesis (the strongest defensible claim).** In the massive non-relativistic sector, **invariant mass upper-bounds the spatial Fisher information extractable per unit kinetic energy** (`F_Q/K ≤ 8m/ħ²`); the **measurement context** determines what fraction of that capacity is actually realized (`J_𝒞 ≤ F_Q`). Therefore **mass sets capacity; context realizes accessibility** — two distinct, complementary roles, *not* an identity.

## 9. Consistency audit

### 9.1 What CAN be proved mathematically (Part II)
- the reciprocal identity `m·ƛ_C = ħ/c` (§11 / PMD-1);
- the mass–energy–localization inequality `F_Q ≤ 8mK/ħ²` (§12 / PMD-2);
- additivity of context Fisher information across independent channels (§13 / PMD-3);
- the data-processing (monotonicity) bound: losing context cannot raise position information (§14 / PMD-4);
- the admissible one-parameter family for `g_M` from a log-odds axiom (§16 / PMD-5);
- uniqueness of the nested geometric mean under separability + symmetry + idempotence (§19 / PMD-6);
- the elasticity split showing the nesting does **not** double-weight Position (§20 / PMD-7);
- the exact participation of interactions in composite invariant mass (§22 / PMD-8);
- the condition for empirical surplus over the null model, as a **no-go** (§23 / PMD-9);
- the **exact relativistic** localization bound, of which the NR bound is the leading term (§12.1 / PMD-2R);
- the **capacity–efficiency factorization** `J_𝒞 = ε·u·(8mK/ħ²)` (§15.1 / PMD-10);
- **per-meter reference-scale invariance** — and its **failure for the combined score** (§16.1 / PMD-11);
- the **surplus identity** `𝔼[Δ log-loss] = I(Y;C_R|X_std)` (§23.1 / PMD-12).

### 9.2 What CANNOT be proved by mathematics alone
The following stay **interpretive (L3/L4)** and are *not* elevated by Part II:

```
mass = context
localization = crystallization of context
cosmic context causes all inertia
```

Mathematics can derive consequences *once a formal definition of "context" is accepted*, but it cannot prove that definition corresponds to a fundamental physical reality.

### 9.3 Residual wording defect in Part I (fixed in v1.2.1)
Part I §5's law box once carried "the unpaid limit is the massless, **delocalized** state," while §6/§8 correctly reject "massless ⇔ delocalized." The mathematically correct statement — now enforced in §5 — is: at `m → 0` the **massive rest-frame channel `P_M` vanishes**, but the overall localizability meter `P_L` need **not** be zero (it is carried by the detection/Fisher channel `P_D`). Masslessness removes the rest-frame particle-"here", not all localization.

---

## 10. Formal domain

Let:

```
L*  > 0     a pre-registered, task-specific localization scale        [m]
m   ≥ 0     invariant mass                                            [kg]
ƛ_C = ħ/(mc)   reduced Compton wavelength (for m>0)                   [m]
x  ∈ ℝ^d    spatial-translation parameter (the "where")
ρ_x         quantum state after translation by x
𝒞           the measurement context
P_S,P_D,P_M,P_L,P ∈ [0,1]   (P_D, P_S, P_M lie strictly in [0,1) — they saturate toward 1, never reach it)
```

Spatial translation is generated by momentum `p̂`:

```
ρ_x = e^(−i x p̂ / ħ) · ρ_0 · e^(+i x p̂ / ħ)
```

The context 𝒞 is represented by a POVM / classical measurement channel:

```
p(y | x, 𝒞) = Tr( ρ_x · E_y^(𝒞) )
```

so **"context" stops being a word.** It is:

```
𝒞 = { coupling, boundary, frame, measurement channel }
```

— and it fixes *how much information about x can actually be extracted.*

---

## 11. Theorem PMD-1 — Compton reciprocity  ·  **[L1: identity]**

For `m > 0`:  `ƛ_C = ħ/(mc)`, hence

```
■  m · ƛ_C = ħ / c        (mass × localization scale is a universal constant)
```

**Proof.** `m·ƛ_C = m·ħ/(mc) = ħ/c`. ∎  Also `dƛ_C/dm = −ħ/(cm²) < 0`, so the Compton scale is strictly decreasing in mass.

**Non-relativistic inertial corollary.** At fixed force `F` and `v ≪ c`, `a = F/m`, so

```
ƛ_C / a = (ħ/mc) / (F/m) = ħ / (cF)   ⇒   ■ ƛ_C ∝ a ∝ 1/m   (at fixed F)
```

**Reading (not a proof of "mass = context").** The *same* parameter `m` that shrinks the massive rest-frame localization scale also shrinks the acceleration response at fixed force. The two PMD anchors — localization scale (§2) and inertia (§3) — are governed by **one** physical quantity. That is a genuine structural unification; it is *not* a claim that mass is context.

---

## 12. Theorem PMD-2 — Localization Information–Energy bound  ·  **[L2: proved, non-relativistic]**

*(The strongest new formal result — the defensible quantitative core of PMD.)*

For the translation family `ρ_x` generated by `p̂`, the **quantum Fisher information** for estimating `x` obeys

```
F_Q(ρ_x) ≤ 4 (Δp)² / ħ²          (equality for pure states)
```

With non-relativistic kinetic energy `K = ⟨p²⟩ / (2m)` and `(Δp)² = ⟨p²⟩ − ⟨p⟩² ≤ ⟨p²⟩ = 2mK`:

```
■  F_Q ≤ 8 m K / ħ²        (equality for a pure, zero-mean-momentum state)
```

**Proof.** Combine `F_Q ≤ 4(Δp)²/ħ²` (QFI of a unitary family = 4·Var of its generator, with `≤` for mixed states) and `(Δp)² ≤ 2mK`. ∎

**Cramér–Rao corollary.** For `N` independent measurements, `Var(x̂) ≥ 1/(N·F_Q)`, hence

```
■  Var(x̂) ≥ ħ² / (8 N m K)
```

**Capacity reading (defensible).** Per unit kinetic-energy budget, larger mass permits a lower fundamental error floor on estimating a spatial displacement:

```
■  F_Q / K ≤ 8 m / ħ²        ("mass = localization-information leverage per unit energy")
```

This is far more defensible than "localization is bought with mass": it is a *proved inequality*, explicitly scoped to the non-relativistic massive sector, that assigns mass a precise operational role (capacity), not a metaphysical one. **Scope:** as stated the bound is **non-relativistic** (it uses `K = ⟨p²⟩/2m`). §12.1 now supplies the **exact relativistic form**, of which this is the leading term.

---

## 12.1. Theorem PMD-2R — exact relativistic localization bound  ·  **[L2: proved, exact]**

*(New in v1.5. Closes the non-relativistic scope gap of PMD-2 — the bound is not merely an NR approximation but the leading term of an exact result.)*

Spatial translation is generated by `p̂` **at all velocities**, so `F_Q ≤ 4·Var(p̂)/ħ² ≤ 4⟨p̂²⟩/ħ²` holds relativistically as well. For a free particle the dispersion is an **operator identity**, `Ĥ² = p̂²c² + m²c⁴`, hence

```
⟨p̂²⟩ = ( ⟨Ĥ²⟩ − m²c⁴ ) / c²          (exact — no expansion)
```

and therefore

```
■  F_Q ≤ 4( ⟨Ĥ²⟩ − m²c⁴ ) / (ħ²c²)          (exact, all velocities)
```

**Proof.** `Var(p̂) ≤ ⟨p̂²⟩`; substitute the operator identity. ∎

> ### Scope — four hypotheses, all load-bearing
> 1. **Single particle.** `Ĥ² = c²p̂² + m²c⁴` is an operator identity **only** on a one-particle positive-energy Poincaré irrep. For `N > 1` it is **false**: the correct object is the *invariant-mass operator* `M̂²c⁴ ≡ Ĥ² − c²P̂²`, which acts nontrivially on relative momenta. *Counterexample (notation made explicit, v1.5.2):* take two free particles each of rest mass `m`, with momenta `±p`, and insert the **constituent baseline** `M_Σ ≡ 2m` into the single-particle formula. The state has `P̂|ψ⟩ = 0`, so `⟨P̂²⟩ = 0`, yet `(⟨Ĥ²⟩ − M_Σ²c⁴)/c² = 4p² ≠ 0` — the formula overstates `⟨P̂²⟩` without bound. *(The system's own invariant mass is of course `M_sys c² = 2√(p²c² + m²c⁴)`, for which `⟨Ĥ²⟩ − M_sys²c⁴ = 0` in the COM frame — which is precisely the point: `M̂` is an **operator** on relative momenta, not the c-number `M_Σ`, so the substitution that makes the one-particle identity work is unavailable.)* It also fails for interacting `Ĥ = Ĥ_free + V̂` and for general Fock states.
> 2. **Positive-energy sector.** On the full Dirac spectrum a negative-energy state has `⟨E_kin⟩ < 0` and the expansion below loses its sign.
> 3. **Finite second moment,** `⟨Ĥ²⟩ < ∞`; otherwise the bound is true but vacuous.
> 4. **"Exact" qualifies the identity, not the bound.** The inequality discards `⟨p̂⟩²`, so it is loose by exactly `4⟨p̂⟩²/ħ²` — a **frame-dependent** slack that grows like `γ²` under boosts. It is saturable only in the zero-mean-momentum frame.

**Relation to PMD-2 — and a correction to the naive reading.** Writing `Ê_kin ≡ Ĥ − mc²` and `(ΔH)² = ⟨Ĥ²⟩ − ⟨Ĥ⟩²`, the algebra is exact (on the positive-energy sector, where every term is non-negative):

```
⟨Ĥ²⟩ − m²c⁴ = 2mc²⟨E_kin⟩ + ⟨E_kin⟩² + (ΔH)²

■  F_Q ≤ 8m⟨E_kin⟩/ħ²  +  4( ⟨E_kin⟩² + (ΔH)² ) / (ħ²c²)
        └ PMD-2 form ┘     └──── O(1/c²), ≥ 0 ────┘
```

> ### ⚠ This does **NOT** make `8mK/ħ²` a relativistic ceiling — it proves the opposite
> The extra terms are **non-negative and added to the right-hand side**, so the relativistic ceiling **exceeds** the PMD-2 expression. A larger ceiling does not validate the smaller one; it *removes* its status as a bound. **`F_Q ≤ 8mK/ħ²` is therefore NOT valid relativistically when `K` denotes relativistic kinetic energy — it is violated at every nonzero momentum.**
>
> **Exact violation factor.** For the zero-mean state `(|+p⟩ + |−p⟩)/√2` one has `F_Q = 4p²/ħ²` exactly, while `E_kin = mc²(√(1+u²) − 1)` with `ξ ≡ p/(mc)` (the relativity parameter; `u` is reserved for utilization, §15.1). Then
>
> ```
> ■  F_Q / ( 8m·E_kin/ħ² )  =  ξ² / [ 2(√(1+ξ²) − 1) ]  =  ( √(1+ξ²) + 1 ) / 2   >  1   for every ξ > 0
> ```
>
> | `ξ = p/mc` | 0.01 | 0.1 | 1 | 10 | 100 |
> |---|---|---|---|---|---|
> | violation factor | 1.000025 | 1.0025 | **1.207** | **5.52** | **50.50** |
>
> (Closed form verified against direct computation; as `m → 0` the PMD-2 expression → 0 while `F_Q` stays finite — violation by an unbounded factor.)
>
> **Corrected status of PMD-2.** `F_Q ≤ 8mK/ħ²` holds **if and only if `K` is defined as `⟨p̂²⟩/2m`** — in which case it is not an independent physical bound at all but a *rewriting* of `F_Q ≤ 4⟨p̂²⟩/ħ²` using the NR definition of kinetic energy. Its content is the **identification** of `⟨p̂²⟩` with a mass-times-energy budget, and that identification is exactly what fails relativistically. PMD-2 is thus **strictly non-relativistic**, and PMD-2R is the correct statement whenever velocities are not small.

*(This correction was forced by adversarial review of the v1.5 draft, which had read the expansion backwards; the error and its repair are recorded here rather than silently removed.)*

> ### ⚠ Honest consequence — the "capacity" reading is **budget-dependent**
> The direction of the mass effect depends on **which energy budget is held fixed** — and the contrast is *not* relativistic-vs-non-relativistic:
>
> ```
> fixed KINETIC budget  K = ⟨p̂²⟩/2m     :  ceiling = 8mK/ħ²                     → INCREASES with m
> fixed KINETIC budget  K = ⟨Ĥ⟩ − mc²   :  ceiling = 4(2mc²K + K² + (ΔH)²)/(ħ²c²) → INCREASES with m,
>                                            **but only if `(ΔH)²` is ALSO held fixed** (see note)
> fixed TOTAL   budget  ⟨Ĥ²⟩            :  ceiling = 4(⟨Ĥ²⟩ − m²c⁴)/(ħ²c²)       → DECREASES with m
> ```
>
> So the reversal is driven entirely by **whether rest energy sits inside the budget**, not by relativistic kinematics: at fixed *kinetic* energy the direction is the same in both regimes. **"More mass = more localization capacity" holds under a kinetic-energy budget and reverses under a total-energy budget**, because rest energy consumes what would otherwise buy momentum spread.
>
> **Necessary technical care.** The total-energy budget must be stated as fixed **second moment `⟨Ĥ²⟩`**, *not* fixed mean `⟨Ĥ⟩`. Since `⟨Ĥ²⟩ = ⟨Ĥ⟩² + (ΔH)²` and `(ΔH)²` is unbounded at fixed mean, **the ceiling is unbounded above at fixed `⟨Ĥ⟩`** (explicitly: a two-component superposition holding `⟨Ĥ⟩ = 2mc²` while pushing the upper branch up gives `⟨Ĥ²⟩ − m²c⁴ = 4, 11, 101, 10⁴, 10⁸ …` in units `m = c = 1`). Writing the budget as `E² − m²c⁴` with `E = ⟨Ĥ⟩` — as the v1.5 draft did — is an error.
>
> **A mean alone never fixes a ceiling (v1.5.2).** The relativistic ceiling contains `(ΔH)²`, which is free once only a *mean* is constrained. So "fixed kinetic budget ⇒ capacity increases with `m`" requires, in addition to fixed `⟨E_kin⟩`, **one** of: a sharp-energy state (`ΔH = 0`), a fixed second kinetic moment `⟨E_kin²⟩`, or a separately fixed energy variance. The same caution is what forces the total-energy budget to be stated as `⟨Ĥ²⟩` rather than `⟨Ĥ⟩`.
>
> Any application of PMD **must declare which budget is held fixed** — *and pin its second moment*; the §30 Localization-Leverage statement is scoped to the fixed-kinetic-energy reading.

**One concrete falsifiable ceiling (answers "PMD makes no checkable statement").** Combining PMD-2R with the Braunstein–Caves inequality (`J_𝒞 ≤ F_Q` for *any* POVM) gives a hard design constraint on **every** localization protocol — any measurement, any number of detectors, any classical post-processing:

```
■  J_𝒞  ≤  4⟨p̂²⟩/ħ²  ≤  4(⟨Ĥ²⟩ − m²c⁴)/(ħ²c²)    ⇒    Var(x̂)  ≥  ħ²c² / ( 4N(⟨Ĥ²⟩ − m²c⁴) )
   (non-relativistically, with K ≡ ⟨p̂²⟩/2m:   Var(x̂) ≥ ħ²/(8NmK) )
```
(one-particle, free, positive-energy, `⟨Ĥ²⟩ < ∞`; the `⟨p̂²⟩` form is the primitive one and is what a metrology test actually constrains)

This **is** experimentally falsifiable: a certified localization variance below the floor, at a certified energy budget, refutes it. **Honest label:** it follows from *standard* quantum estimation theory — it is **not new physics**. PMD's contribution is to *identify this ceiling as the Position-axis capacity* and to build the meter around it. PMD-9 (§23) still blocks any claim of *novel* predictive content.

---

## 13. Theorem PMD-3 — context Fisher information is additive  ·  **[L2: proved]**

For `n` conditionally independent channels, `p(y₁,…,yₙ | x) = ∏ₖ pₖ(yₖ | x)`, with per-channel classical Fisher information `Jₖ(x) = 𝔼[(∂ₓ ln pₖ)²]`:

```
■  J_𝒞(x) = Σₖ Jₖ(x)
```

**Proof.** The score of the product is the sum of scores, `s = Σₖ sₖ`. Then `J_𝒞 = 𝔼[(Σ sₖ)²] = Σₖ 𝔼[sₖ²] + 2 Σ_{i<j} 𝔼[sᵢsⱼ]`. For regular models `𝔼[sₖ] = 0`; under conditional independence `𝔼[sᵢsⱼ] = 𝔼[sᵢ]𝔼[sⱼ] = 0`. Hence `J_𝒞 = Σₖ Jₖ`. ∎

> **Scope (v1.5.2) — this is *not* a general "more detectors ⇒ more information" law.** Additivity requires a genuine **product likelihood**: independent copies, or conditionally independent channels given `x`. It does **not** hold automatically for sequential measurements on the *same* quantum system, incompatible POVMs, correlated detectors, adaptive protocols, or any channel that disturbs the state. In those cases the **full joint** Fisher information must be computed and can be strictly sub-additive.

**Interpretation.** Within that scope this gives a precise meaning to "more context": *more conditionally independent relational channels ⇒ more position information.* It does **not** say context creates mass — only that relational context increases the **measurability** of "where."

---

## 14. Theorem PMD-4 — losing context cannot raise localization information  ·  **[L2: proved]**

For a coarse-graining Markov chain `x → Y → Z`:

```
■  J_Z(x) ≤ J_Y(x)        (Fisher-information data-processing inequality)
```

**Proof (sketch, under standard regularity** — support of `Y` independent of `x`, `∂/∂x` interchangeable with integration, and — essential — the coarse-graining kernel `q(z|y)` **independent of `x`**; if the post-processing itself depends on the parameter, the inequality does not follow in this form**).** The coarse-grained score is a conditional expectation, `s_Z = 𝔼[s_Y | Z]`; by Jensen, `𝔼[s_Z²] = 𝔼[ 𝔼[s_Y|Z]² ] ≤ 𝔼[s_Y²]`, i.e. `J_Z ≤ J_Y`. ∎

**The defensible context thesis.** Removing or coarse-graining relational channels **cannot increase** the information with which a system is localizable. (The converse — that adding context *creates* location rather than reveals it — is *not* claimed.)

---

## 15. Operational localization (detection) meter `P_D`  ·  **[L3: modelling choice]**

Define the dimensionless Fisher ratio `z_D = L*² · J_𝒞` and

```
■  P_D = z_D / (1 + z_D) = L*²·J_𝒞 / (1 + L*²·J_𝒞)
```

Properties (all verified): `0 ≤ P_D < 1`; `P_D(0) = 0`; `P_D → 1` as `J → ∞`; `∂P_D/∂J = L*²/(1+L*²J)² > 0`. It is dimensionless, bounded, strictly monotone, saturating, and **valid for both massive and massless local detections** — a cleaner realization of Part I's massless adapter `g_0`.

---

## 15.1. PMD-10 — the capacity–efficiency decomposition  ·  **[L3: a definition + two scoped range claims — NOT a theorem]**

*(New in v1.5; **demoted in v1.5.1** after review. The decomposition itself is true **by construction**; all of its content sits in the two range claims and their scope.)*

Two inequalities chain together — the first is Braunstein–Caves (the classical Fisher information of **any** POVM cannot exceed the quantum Fisher information), the second is PMD-2:

```
J_𝒞  ≤  F_Q  ≤  8mK/ħ²        (non-relativistic; use PMD-2R for the exact form)
```

Define two dimensionless ratios, each in `[0,1]` by exactly those two inequalities:

```
ε = J_𝒞 / F_Q            ∈ [0,1]     CONTEXT EFFICIENCY  — how much of what is knowable the channel extracts
u = F_Q / (8mK/ħ²)       ∈ [0,1]     STATE UTILIZATION   — how much of the mass-energy ceiling the state uses
```

Then, identically:

```
   J_𝒞  =  ε · u · ( 8mK/ħ² )
     └ context ┘ └ state ┘ └ mass-energy capacity ┘
```

> **Honesty note (v1.5.1, degenerate cases split in v1.5.2).** As an equation this is **`J_𝒞 = J_𝒞`** — a tautology, since `ε` and `u` are *defined* as the two ratios. It is a bookkeeping decomposition, not a theorem. All the substantive content is in the two range claims, which must therefore carry their own scope:
> - **`ε ∈ [0,1]` — sound**, by Braunstein–Caves, *provided* `J_𝒞` is the classical Fisher information of the **same** family `ρ_x`, about the **same** parameter, per **identical resource unit** (a per-`N`-copy or per-unit-time `J_𝒞` compared against a single-shot `F_Q` can exceed 1; so can a finite-sample plug-in estimate, which is upward-biased).
> - **`u ∈ [0,1]` — sound only in the non-relativistic sector with `K ≡ ⟨p̂²⟩/2m`.** It **fails** for relativistic kinetic energy at every nonzero momentum (§12.1), and for any phenomenological "budget" that is not `⟨p̂²⟩/2m`. *(It does survive one useful generalization: for NR multi-particle centre-of-mass translation, Cauchy–Schwarz gives `⟨P̂²⟩ ≤ 2MT` with `M = Σmᵢ`, so `u ≤ 1` holds for the collective generator.)*
> - **Degenerate cases must be split — `ε` and `u` do *not* fail together (v1.5.2):**
>
>   | condition | `ε = J_𝒞/F_Q` | `u = F_Q/(8mK/ħ²)` |
>   |---|---|---|
>   | `F_Q > 0`, `K > 0` | defined | defined |
>   | `F_Q = 0`, `K > 0` (e.g. a momentum eigenstate with `p ≠ 0`) | **undefined** (`0/0`) | **`0`** — well defined |
>   | `F_Q = 0`, `K = 0` | **undefined** | **undefined** (`0/0`) |

**Reading.** Within that scope the three factors name the three genuinely distinct things PMD talks about: *what the world permits* (mass-energy), *what the state offers* (utilization), *what the context extracts* (efficiency). This is the informal content of §30's "mass sets capacity; context realizes accessibility."

> ### Consequence for the §17 adapter — `η` is **not** the weight on mass
> *(The v1.5 draft asserted here that `P_D^(1−η)·P_M^η` "double-counts mass" as a *proved structural fact*. **That claim is withdrawn in v1.5.1** — it does not follow. The bound `J_𝒞 ≤ 8mK/ħ²` is *one-directional*: it constrains only the ceiling, and since `ε, u` range freely over `[0,1]`, the realized `J_𝒞` is **not a monotone function of `m`** — for any mass there are states with `J_𝒞 = 0`. A ceiling that grows with `m` therefore implies nothing about whether the realized `P_D` grows with `m`. Statistical dependence between `P_D` and `P_M` is an **empirical** property of the population being scored, not a derivable one; the bound induces only a triangular support region.)*
>
> **What does survive, and is checkable — but the v1.5.1 formula for it was wrong.** Because `P_D`'s realized value may itself vary with `m`, the elasticity of the composite with respect to `log m` is not `η`. The **correct** elasticity is the full chain rule:
>
> ```
> ■  ℰ_m(P_L) ≡ ∂log P_L/∂log m = (1−η)·s_D + η·s_M ,     s_D ≡ ∂log P_D/∂log m ,  s_M ≡ ∂log P_M/∂log m
>
>    and for  P_M = x^α/(1+x^α)  with  x ∝ m :        ■  s_M = α·(1 − P_M)
>
>    hence   ■  ℰ_m(P_L) = (1−η)·s_D + η·α·(1 − P_M)
> ```
>
> *(v1.5.2 correction: the v1.5.1 draft printed `η_eff = η + (1−η)·s`, which is **wrong** — it silently assumed `s_M = 1`. It happens to coincide with the truth only where `α(1−P_M) = 1`. Worked check at `α = 2, η = ½`: at `m = 0.3` the true elasticity is `1.026486` while the withdrawn formula gives `0.609055`; at `m = 3` truth is `0.164625` versus `0.564625`. Only at `m = 1`, where `P_M = ½` and `α(1−P_M) = 1`, do they agree.)*
>
> Two further claims from v1.5.1 are **withdrawn**: (i) the bound `s_D ∈ [0,1]` — there is none, because the realized `J_𝒞` is not a monotone function of mass, so `s_D` may be negative, zero, or exceed 1; and consequently (ii) `η_eff ∈ [η,1]`. Also, `Corr(logit P_D, logit P_M)` is **not** "equivalent" to an elasticity — a correlation and a derivative measure different things.
>
> **`ℰ_m` is a local log-elasticity, not a weight in `[0,1]`.** It may legitimately exceed 1 (at `α = 2` with `P_M` small, `s_M = α(1−P_M) ≈ 2` alone pushes it there — hence the `1.026` above), and it may be negative if `s_D < 0`. Reading it as a normalized share is a category error.
>
> So **`η` may not be read as "the weight on mass"**: the realized mass elasticity is `ℰ_m(P_L)` above, it is state- and population-dependent, and `s_D` must be **estimated on the scored corpus**, never asserted. Pre-registering `η` without reporting `s_D` leaves the effective mass weight undetermined.
>
> **Calibration rival (unchanged in status).** Blending the two factors that are *not* nested in one another remains a reasonable alternative to test:
>
> ```
>    P_L = P_cap^(1−η) · P_eff^η ,    P_cap = g( L*²·8mK/ħ² ) ,   P_eff = ε = J_𝒞/F_Q
> ```
>
> **Status:** L3 modelling choice for the §29 model comparison — motivated by interpretability of `η`, **not** by a proved redundancy.

---

## 16. Theorem PMD-5 — the admissible family for `g_M`  ·  **[L3: conditional derivation]**

Let `x_M = L*/ƛ_C = mcL*/ħ = m/m*`, with reference mass `m* = ħ/(cL*)`. Require `g_M : (0,∞) → (0,1)` continuous, strictly increasing, `g_M(1) = ½`, and **log-odds additive under multiplicative rescaling** of `x_M`:

```
ℓ(x·y) = ℓ(x) + ℓ(y),    where  ℓ(x) = ln[ g_M(x) / (1 − g_M(x)) ]
```

Then the continuous solutions of that Cauchy equation are `ℓ(x) = α·ln x` (`α > 0`), so

```
■  g_M(x) = x^α / (1 + x^α)
```

**Proof.** `ℓ(xy)=ℓ(x)+ℓ(y)` continuous ⇒ `ℓ(x)=α ln x`; exponentiating `g/(1−g)=x^α` and solving gives the logistic form. ∎

**Preferred Fisher exponent.** If the mass channel is read as an inverse-variance capacity `J_M ∝ 1/ƛ_C²`, the natural exponent is `α = 2`, giving

```
■  P_M = (L*/ƛ_C)² / (1 + (L*/ƛ_C)²) = (m/m*)² / (1 + (m/m*)²)
```

This is **not** a new physical law — it is a canonical normalization candidate justified by dimensional analysis, inverse-variance reading, boundedness, and scale symmetry. `α ∈ {1, 2, free}` is a calibration/model-comparison question, not settled.

---

## 16.1. Theorem PMD-11 — reference-scale invariance: what survives and what does **not**  ·  **[L2: proved (both directions)]**

*(New in v1.5. The reference scale `L*` is a declared convention, so it is essential to know exactly which PMD conclusions depend on it. One half of this result is positive; the other half is a **negative result** that constrains how PMD may be used.)*

### (a) Per-meter — invariance **holds** (positive)

Under a change of reference scale `L* → λL*` (`λ > 0`), each meter's log-odds shifts by a **constant that is the same for every system**:

```
logit P_M(m; λL*) = logit P_M(m; L*) + α·ln λ
logit P_D(J; λL*) = logit P_D(J; L*) + 2·ln λ
```

Therefore, for **any two systems** compared *within one meter*:

```
■  logit P_M(m₁) − logit P_M(m₂) = α·ln(m₁/m₂)      — independent of L*
■  logit P_D(J₁) − logit P_D(J₂) = ln(J₁/J₂)        — independent of L*
```

**Corollary.** Within a single meter, not only the ranking but the **entire log-odds gap** is scale-free; `L*` fixes only where the ½-point sits. *(Verified: the electron–proton `P_M` log-odds gap is `−15.0306891424` at `L* = 1 fm`, `1 pm`, `1 nm`, `1 μm` — identical to ten decimals.)* ∎

### (b) Combined score — invariance **FAILS** (negative result)

The meters are combined **on the probability scale** (`P_L = P_D^(1−η)·P_M^η`, then `P = √(P_S·P_L)`). Writing `g(ℓ) ≡ log σ(ℓ)`, the combined log-score is `log P_L = (1−η)·g(ℓ_D + 2c) + η·g(ℓ_M + αc)` with `c = ln λ`. Since **`g` is strictly concave**, a translation of its argument does **not** pass through as an additive constant and therefore does **not** cancel in the difference `log P_L^A − log P_L^B`. The shift survives *inside* a non-linear function, and the ranking can invert.

*(v1.5.1 correction: the v1.5 draft attributed the failure to the meters shifting by **different** amounts, `α ln λ` vs `2 ln λ`. That explanation is **wrong** — the failure occurs even when the shifts are **equal**. The true mechanism is the concavity of `log σ`, which re-weights each meter differentially across systems: `∂ log P_L/∂ℓ_D = (1−η)(1−P_D)` and `∂ log P_L/∂ℓ_M = η(1−P_M)` both depend on `L*` **and** on the system. Asymptotically the aggregation rule even changes character — as `L* → 0` it ranks by the arithmetic mean of logits; as `L* → ∞` it degenerates to a soft-minimum dominated by the worst meter.)*

```
■  There exist systems A, B and scales λ with  P(A) > P(B)  at  L*  but  P(A) < P(B)  at  λL*.
```

*Explicit counterexample **with equal shifts*** (`α = 2, η = ½, P_S ≡ 1`; base log-odds `A = (ℓ_D, ℓ_M) = (0, 0)`, `B = (−2, +3)` — note `B` has the *larger* logit mean):

| `L*` | `P(A)` | `P(B)` | winner |
|---|---|---|---|
| 0.01 | 0.010000 | 0.012834 | **B** |
| 0.10 | 0.099504 | 0.122618 | **B** |
| 1.00 | 0.707107 | 0.580492 | **A** |
| 10.0 | 0.995037 | 0.982214 | **A** |

A pure change of reference scale reverses the winner. A randomized sweep over `λ ∈ [10⁻³, 10³]` flips **15.3 %** of random pairs at the canonical `α = 2, η = ½` (29.7 % at `α = 1`; at `α = 1` the ordering is not even monotone in `L*` — it can reverse twice). ∎

### (c) The dichotomy that makes PMD usable

The flips are not arbitrary — they are **exactly** confined to trade-off comparisons:

| comparison type | definition | `L*`-robust? | measured flip rate |
|---|---|---|---|
| **Dominance** | one system is `≥` the other on **every** sub-meter | **YES — provably 0**: the shifts are system-independent and every meter is monotone, so a uniform shift cannot cross the components | **0 / 10 093** |
| **Trade-off** | system A wins some sub-meters and loses others | **No guarantee** — some are stable, some flip; must be checked individually | flip rate depends on the sampling design (see §16.1d) |

```
■  DOMINANCE  ⟹  reference-scale-robust ranking.        (proved)
■  The converse is FALSE: robustness does NOT imply dominance.
```

> **v1.5.2 correction.** The v1.5.1 draft stated this as an **"⟺"**. That is wrong, and the appendix's own simulation refutes it: if ~60 % of trade-off pairs flip somewhere in the sweep, then ~40 % **do not** — those are non-dominance rankings that were nevertheless stable over the scanned range. (Under the published script's documented settings — §16.1d, `seed = 3` — **8 981 / 14 979 = 60.0 %** of trade-off pairs flip somewhere in the sweep and **40.0 % remain stable**, while **0 / 5 021** dominance pairs flip.) Dominance is therefore **sufficient** for scale robustness, **not necessary**: a trade-off comparison simply carries *no guarantee* and must be checked case by case.

**Mandatory methodological consequence (binding on all PMD use).**
1. **Dominance conclusions** ("system A is `≥` B on every sub-meter") are objective and may be reported without reference to `L*`.
2. **Trade-off conclusions** carry **no guarantee either way**. They are defined relative to a pre-registered `L*` and **must** be reported with an explicit **`L*`-sensitivity interval** — the range of `L*` over which that particular ordering holds. Many trade-off rankings *are* stable; the point is that stability must be **demonstrated per comparison**, never assumed. Reporting a trade-off ranking as if it were scale-free is an error.

### (d) Reproducibility of the simulation figures

The **counterexamples above are proofs** — a single explicit rank reversal establishes the negative result, and needs no statistics. The **percentages** are **illustrative Monte-Carlo figures, not theorems**, and they move with the sampling design — which is exactly why the design is fixed here and shipped as code. Generating procedure: base log-odds `ℓ_D, ℓ_M ~ Uniform(−6, 6)` i.i.d. per system, `P_S ~ Uniform(0.05, 0.95)`, `α = 2`, `η = ½`, full score `P = √(P_S·P_L)`, scale sweep `λ ∈ {10⁻³, 10⁻², 10⁻¹, 10, 10², 10³}`, a pair counted as "flipped" if the sign of the score difference changes at any swept `λ`; 20 000 draws, Python `random` with `seed = 3` (dominance / trade-off split) and `seed = 7` (logit-adapter check). Under exactly that design: **dominance 0 / 5 021 flips**, **trade-off 8 981 / 14 979 flips (60.0 %), i.e. 40.0 % stable**. The script is published alongside this appendix (`pmd_scale_sensitivity.py`) and regenerates every number quoted in this section. **Any use of these numbers outside that design is unwarranted**; what is established without qualification is the *existence* of reversals and the *sufficiency* of dominance.

### (e) The log-odds alternative — reconsidered

Aggregating in log-odds space instead — `P_L = σ( (1−η)·logit P_D + η·logit P_M )` — **does** restore exact invariance (`0 / 4 000` flips in every parameter setting tested), because the combined log-odds then shifts uniformly by `[(1−η)·2 + η·α]·ln λ`. *(Confirmed independently: `logit P_L^A − logit P_L^B` is constant to six decimals across `L* = 0.01, 1, 100`. More generally, **any affine rule in logit space with system-independent coefficients preserves ranking, and no non-affine aggregation of the probabilities does**.)*

> ### ⚠ v1.5.2 — the v1.5.1 reason for rejecting this fix was **wrong**
> The v1.5.1 draft claimed the logit blend "destroys the constant elasticity" and quoted `∂lnU/∂lnP_S = 0.2083` instead of `1/6`. **That computation applied the logit mean at the TOP level (between `P_S` and `P_L`), which is a different construction.** Applying it *inside* `P_L` — which is all that is proposed — leaves the top level untouched: with `P = √(P_S·P_L)` and `U = ∛(F·P·A)`,
> ```
> ■  ∂lnU/∂lnP_S = (1/3)·(1/2) = 1/6      exactly — independent of how P_L is built internally
> ```
> *(Verified: `0.16666667` for both the geometric and the logit-inside adapter at `(P_S, ℓ_D, ℓ_M)` = (0.6, 0.4, −0.8), (0.9, 2.0, 1.0), (0.2, −1.5, 0.7).)* **Position keeps its `1/3` share and `P_S` its `1/6` elasticity either way.**
>
> **What the logit blend actually changes** is the *internal* `P_D`/`P_M` split, which stops being the constant `((1−η)/6, η/6)` of §20 and becomes state-dependent: `∂lnP_L/∂lnP_D = (1−η)(1−P_L)/(1−P_D)` rather than `(1−η)(1−P_D)`. It also gives zero-annihilation only in the limit (`P_D → 0 ⇒ P_L → 0`) instead of exactly, and — importantly — **it changes which systems win**.

```
■  geometric inside P_L : exact zero-annihilation, constant internal split, L*-dependent trade-off rankings.
■  logit    inside P_L : exact L*-invariance of P_L rankings, state-dependent internal split, limiting annihilation.
   Both preserve Position's 1/3 share of U and P_S's 1/6 elasticity.
```

**Status (v1.5.2): this is an open, pre-registerable calibration choice, not a settled one.** The canon retains **geometric** aggregation for continuity and exact annihilation, but the logit-inside adapter is a **legitimate rival that must be included in the §29 model comparison** — it is no longer rejected, because the stated ground for rejecting it did not hold.

---

## 17. Upgraded massive adapter (Part I §5 `P_L = P_M` → v1.3+ proposal)  ·  **[L3]**

Part I's current `P_L = P_M` in the massive sector cannot distinguish a **localized** massive particle from a **massive momentum eigenstate delocalized over all space**. The proposed fix folds in the detection channel:

```
■  massive sector:   P_L = P_D^(1−η) · P_M^η ,   0 < η < 1     ← STRICT (see below)
■  massless sector:  P_L = P_D
```

At the symmetric point `η = ½`, `P_L = √(P_D · P_M)`.

> **Why `η` must be *strictly* interior (v1.5.2).** The endpoints break the very controls the adapter exists to enforce. At **`η = 1`** the form degenerates to `P_L = P_D⁰·P_M = P_M`, so a *massive-but-delocalized* state with `P_D = 0, P_M > 0` scores `P_L = P_M > 0` — the control **fails** (and `0⁰` is indeterminate besides). At **`η = 0`** the mass channel vanishes entirely. Hence the canonical adapter requires **`0 < η < 1`**, and the mass-only reading `P_L = P_M` is **not** a special case of it: it survives only as a **separate legacy comparator** in the §29 model comparison, and it does *not* discharge the negative controls.

With `0 < η < 1`, the two essential negative controls (Part I §8) are satisfied **by construction**:

```
massive-but-delocalized :  P_D = 0, P_M > 0  ⇒  P_L = 0     (correctly not localized)
massless-but-detected   :  m = 0,   P_D > 0  ⇒  P_L = P_D>0 (correctly not zero-Position)
```

With `0 < η < 1` this is strictly stronger than the `P_L = P_M` branch because it embeds the two controls into the formula rather than relying on a case split. **Status:** adopted into the Part I §5 core meter in **v1.4**; `η` must be **pre-registered**, never fit post hoc. **Three caveats attach to this form (v1.5.2):** (i) **`0 < η < 1` is required** — the endpoints break the negative controls (box above). (ii) **`η` is not the weight on mass:** the realized mass elasticity is `ℰ_m(P_L) = (1−η)s_D + η·α(1−P_M)` (§15.1), which is state- and population-dependent; `s_D` must be estimated, not assumed. *(The v1.5 draft asserted here that the blend "double-counts mass" as a structural fact — **withdrawn in v1.5.1**: the bound is one-directional and any dependence between `P_D` and `P_M` is an **empirical** property of the scored population, to be measured and tested, never inferred from an upper bound.)* (iii) Trade-off rankings from this blend carry **no reference-scale guarantee** (§16.1 / PMD-11b) and require an `L*`-sensitivity interval.

---

## 18. Spatial-support meter `P_S`  ·  **[L3: modelling choice]**

Let `ρ(x)` be a normalized spatial distribution over a pre-declared reference region `Ω`, and `u_Ω = 1/|Ω|` the uniform. Define the distinguishability information as a KL contrast:

```
D_S = D_KL(ρ ‖ u_Ω) = ∫_Ω ρ(x) · ln[ ρ(x) / u_Ω(x) ] dx ≥ 0   (Gibbs; =0 iff ρ=u_Ω a.e.)
```

and

```
■  P_S = 1 − e^(−D_S / D*) ,   D* > 0
```

so `P_S ∈ [0,1)`, `P_S = 0 ⇔ ρ = u_Ω` a.e., `∂P_S/∂D_S = (1/D*)e^(−D_S/D*) > 0`. This operationalizes "constrained support" as an information contrast against a chosen context.

> **What `P_S = 0` does and does not mean (v1.5.2).** It means **no spatial-concentration information *relative to the declared reference prior*** — not an absolute absence of Position. The meter is a contrast, so it inherits the prior: a system uniform on `Ω` scores `0` against `u_Ω` while scoring positively against a different prior. Accordingly the general form should be written against a **pre-registered reference prior** `π_Ω`, `D_S = D_KL(ρ ‖ π_Ω)`, with `u_Ω` merely the default choice; `Ω` and `π_Ω` must both be declared before use.

---

## 19. Theorem PMD-6 — uniqueness of the nested geometric mean  ·  **[L3: conditional]**

Assume the Position aggregator is **multiplicatively separable**, `G(P_S,P_L) = f(P_S)·f(P_L)`, and require symmetry, idempotence `G(t,t)=t`, zero-annihilation, and monotonicity. Idempotence gives `f(t)² = t`, so `f(t) = √t`, hence

```
■  G(P_S, P_L) = √(P_S · P_L)
```

The geometric nesting is therefore **not arbitrary** — it is forced once separability + symmetry + idempotence + non-compensation are accepted. ∎

**Scope of the uniqueness (honest).** This is uniqueness *within the axiom set*. Rival aggregators that violate one axiom — the minimum `min(P_S,P_L)`, a soft-min, or a weighted geometric mean `P_S^a · P_L^b` with `a ≠ b` (breaks symmetry) — are **not refuted**; they simply fall outside {multiplicative separability, symmetry, idempotence}. CEPT `CORE.PMD.08` records this as *conditionally proved*, and the four-model comparison of §29.9 (`P_S` ; `P_S·P_D` ; `P_S·P_M` ; `P_S·P_D·P_M`) is the model-comparison arm where such rivals are tested.

---

## 20. Theorem PMD-7 — full nested U and elasticity (no double-weighting)  ·  **[L2 given the meters]**

With `P = √(P_S·P_L)` and `U = ∛(F·P·A)`:

```
■  U = F^(1/3) · A^(1/3) · P_S^(1/6) · P_L^(1/6)
```

Log-elasticities:

```
∂lnU/∂lnF = 1/3      ∂lnU/∂lnA  = 1/3
∂lnU/∂lnP_S = 1/6    ∂lnU/∂lnP_L = 1/6
```

The two Position sub-meters together carry `1/6 + 1/6 = 1/3` — **exactly** Position's original share. The nesting **splits** Position's existing weight into two equal halves; it does **not** add weight. *(With the §17 adapter `P_L = P_D^(1−η)·P_M^η`, the `P_L` share `1/6` splits further into `P_D:(1−η)/6` and `P_M:η/6` — at `η=½`, `1/12` each; see §21.)* This is what keeps PMD compatible with `SSS`, where the three top-level pillars aggregate geometrically.

---

## 21. Full proposed PMD operational formula

**Massive sector** (`η`-weighted adapter):

```
P_M = (mcL*/ħ)^α / (1 + (mcL*/ħ)^α)
P_D = L*²·J_𝒞 / (1 + L*²·J_𝒞)
P_L = P_D^(1−η) · P_M^η
P   = √(P_S · P_L)

■  U_PMD = F^(1/3) · A^(1/3) · P_S^(1/6) · P_D^((1−η)/6) · P_M^(η/6)
```

**Massless sector** (`P_L = P_D`; there is **no** `P_M = 0`, only an *inapplicable* mass channel):

```
■  U_PMD^(0) = F^(1/3) · A^(1/3) · P_S^(1/6) · P_D^(1/6)
```

---

## 22. Theorem PMD-8 — interactions participate in composite invariant mass  ·  **[L1: standard, with signed correction]**

For a closed system with total four-momentum `P^μ`:

```
■  M²c² = P_μ P^μ ,   and in the centre-of-momentum frame (𝐏=0):   ■ Mc² = E_COM
```

Writing `H = Σᵢ mᵢc² + H_kin,int + H_field + H_int`:

```
■  M − Σᵢ mᵢ = ( ⟨H_kin,int⟩ + ⟨H_field⟩ + ⟨H_int⟩ ) / c²
```

> **Exactly what is exact (v1.5.2).** `M²c² = P_μP^μ` and `Mc² = E_COM` are **exact and observable**. The *split* of `E_COM` into kinetic, field and interaction pieces is **not** a unique physical decomposition: it depends on the chosen Hamiltonian partition, the constituent baseline, the gauge, and — in QCD — on the renormalization scheme and scale (the individual quark, gluon and trace-anomaly contributions are not each scheme-independent). Written honestly, after **declaring** a decomposition `Ĥ = Σᵢ mᵢc² + Ĥ_rem`, one has the **bookkeeping identity**
> ```
>    M − Σᵢ mᵢ = ⟨Ĥ_rem⟩_COM / c²        (relative to the declared decomposition)
> ```
> This is the rigorous sense in which a system's **internal relations participate in its invariant mass** — a statement about a declared partition, not a unique physical apportionment.

**Essential sign correction (honest).** The sign is **not** universally positive:
- **Nucleons:** QCD dynamics contribute a *large positive* mass over the sum of current-quark masses.
- **Atomic / nuclear bound states:** binding energy gives a *mass defect* (mass **below** the sum of separated parts).

So the defensible statement is `interaction context MODIFIES invariant mass`, **not** `more context always means more mass`. Define a **signed** interaction-mass fraction:

```
χ_int = (M − Σᵢ mᵢ) / M
   χ_int > 0 : interactions raise total mass over the constituent baseline (e.g. QCD)
   χ_int < 0 : binding mass defect (e.g. nuclei, atoms)
   χ_int = 0 : no net interaction contribution vs baseline
```

`χ_int` is a candidate for a *partial* operationalization of "internal relational context" — but note it is **baseline- and scheme-dependent** by construction (it is defined against a chosen constituent baseline `Σᵢmᵢ`), so any reported `χ_int` must declare that baseline and, where relevant, the renormalization scheme. It is a *descriptor relative to a declared decomposition*, not a scheme-independent observable.

**Why the composite (QCD) case still strengthens the reading** (see Part I §8): a nucleon's mass is the energy of its **own internal interactions with itself** made inertial — the "mass = crystallized context" reading applied to a system's relations with its own parts. The signed correction simply forbids the *slogan* "more context ⇒ more mass" while keeping the *structural* claim "interaction context is inertial."

---

## 23. Theorem PMD-9 — no-go for automatic empirical surplus  ·  **[L1: information theory — the honesty gate]**

Let the standard model of the phenomenon use all standard variables `X_std = (m, p^μ, ρ, H_int, 𝒞_measurement, …)`, and let the PMD "context" variable be a **deterministic function** of them, `C = f(X_std)`. Then for **every** observable `Y`:

```
■  I(Y ; C | X_std) = 0
```

**Proof (conditional independence — valid for discrete *and* continuous `C`).** If `C = f(X_std)` then, conditionally on `X_std = x`, `C` is almost surely the constant `f(x)`: `p(c | x, y) = p(c | x) = δ(c − f(x))` for every `y`. Hence `C ⊥ Y | X_std`, and conditional mutual information of conditionally independent variables is zero. ∎

> *(v1.5.2: the v1.5 draft argued via `I ≤ H(C|X_std) = 0`. That is fine for discrete Shannon entropy but **fails for continuous `C`**, where the differential entropy of a degenerate conditional is `h(C|X_std) = −∞`, not `0`. The conditional-independence argument above covers both cases and is the one to cite.)*

**Consequence (the discipline).** If "context" is merely a **relabelling** of variables standard physics already uses, PMD **cannot** add predictive information. Empirical surplus **requires** an *independently measured* context observable `C_R` with

```
■  I(Y ; C_R | X_std) > 0
```

This is the formal version of the Part I §8 null model `H₀`. PMD is honest precisely because it proves its own emptiness absent a new observable.

---

## 23.1. Theorem PMD-12 — the exact surplus identity  ·  **[L1: proved]**

*(New in v1.5. Turns §24's `Δ_CV` from an ad hoc score into an estimator of a specific information quantity, and makes PMD-9 its zero case.)*

For the **true** conditional distributions, the expected log-loss (in nats) of the null model is `𝔼[ℓ₀] = H(Y | X_std)` and of the PMD model `𝔼[ℓ₁] = H(Y | X_std, C_R)`. Hence:

```
■  𝔼[ℓ₀] − 𝔼[ℓ₁]  =  H(Y|X_std) − H(Y|X_std, C_R)  =  I(Y ; C_R | X_std)
```

**Proof.** Both terms are conditional entropies of the same `Y`; their difference is the conditional mutual information by definition. ∎ *(Valid for differential entropies too — the individual `h(·)` are not reparametrization-invariant but their difference is. For continuous `C` the no-go should be argued from conditional independence — `C` is a.s. constant given `X_std` — not from `I ≤ H(C|X_std) = 0`, since `h(C|X_std) = −∞` there.)* *(Verified numerically on a random joint distribution: `I = 0.095060227113` versus `H(Y|X) − H(Y|X,C) = 0.095060227113`; and for a deterministic `C = f(X)`, `I = 0.00e+00` — PMD-9 recovered exactly.)*

**Three consequences that sharpen the empirical programme:**

1. **PMD-9 is the zero case.** `C = f(X_std) ⇒ I(Y;C|X_std) = 0 ⇒` the achievable log-loss gain is *exactly* zero, not merely "unproven." The no-go and the surplus criterion are one theorem seen from two sides.
2. **The effect size has units.** Any claimed PMD improvement is quantified in **nats per observation**, so pre-registration can name a *numerical* threshold (`Δ ≥ δ` nats with a CI excluding 0) instead of a vague "beats the null."
3. **Held-out loss is only a *proxy* estimator — with four documented failure modes (v1.5.1).** The identity holds for the **true** conditionals; `Δ_CV` inherits none of that automatically:
   - **Misspecification breaks the bridge (the important one).** Under a *restricted* model class, a deterministic `C = f(X_std)` with `I(Y;C|X_std) = 0` **can still strictly improve held-out loss** — handing a non-linear feature to a linear/logistic model is the canonical case. A positive `Δ_CV` is therefore **not** evidence that `I(Y;C_R|X_std) > 0`; it may only measure the model class's inability to represent `f`.
   - **`Δ_CV` is biased downward.** k-fold CV estimates the risk of the *fitting procedure*; the two model classes differ in complexity, so their optimism terms do not cancel and the larger model is penalized. Hence `Δ_CV ≤ 0` does **not** refute `I > 0`.
   - **Fold-wise inference is unreliable.** CV folds are dependent and there is no unbiased variance estimator for k-fold CV; naive t-tests across folds are anticonservative. Use a **permutation null on `C_R`** with the entire pipeline inside the permutation.
   - **Plug-in mutual-information estimates are biased upward**, so `Î > 0` on finite data is expected even when `I = 0`; a null distribution is required, not a point estimate.
4. **Scope of the no-go.** `C = f(X_std)` must be a function of **exactly the conditioning set**. If `C = f(X_full)` while only `X_std ⊂ X_full` is conditioned on, then `I(Y;C|X_std)` is generically `> 0`. Note also that `I(Y;C|X) = 0` neither implies nor is implied by `I(Y;C) = 0` (explaining-away): a marginally useless `C_R` can be conditionally informative, and vice versa.

---

## 24. Pre-registered PMD empirical model (how surplus would be earned)

**Outcome must be a *raw* observable, never the constructed `P_D`.** Using `P_D` as the target would be **circular** — it is built from the same channel `𝒞` as the predictors. Let `Y` be a directly measured quantity: the empirical localization error `Var(x̂)`, a detection hit-rate in region `R`, or a resolved position residual.

**Null model.**  `H₀:  g(Y) = f_std(m, Δp, E, POVM, geometry) + ε`

**PMD model.**
```
H₁:  g(Y) = β₀ + β_m·ln x_M + β_C·C_R + β_{mC}·(ln x_M)·C_R + ε
```
where `g` is a fixed link (e.g. `ln Var(x̂)`) and `C_R` is an **independently measured** relational-context variable (**not** a deterministic function of `X_std` — otherwise PMD-9 forces zero surplus).

**PMD earns content only if**, on held-out data, `β_C ≠ 0` or `β_{mC} ≠ 0`, and
```
Δ_CV = Loss(H₀) − Loss(H₁) > 0        (against a pre-set statistical margin, with a permutation null on C_R)
```
> **`Δ_CV > 0` is NOT equivalent to `I(Y;C_R|X_std) > 0` (v1.5.2).** The identity of §23.1 holds for the **true** conditionals; `Δ_CV` compares two **fitted** models and therefore estimates a difference in predictive risk *within the selected model classes*. Under misspecification a deterministic `C = f(X_std)` with `I = 0` can still lower held-out loss (it may simply supply a transform the model class cannot represent), and conversely the CV bias runs downward, so `Δ_CV ≤ 0` does not refute `I > 0`. Report `Δ_CV` as what it is — a predictive-risk difference — and treat any inference to `I > 0` as requiring a well-specified class plus a permutation null.
`RH` requires exactly this contest against the null and against rivals — not mere internal mathematical coherence.

---

## 25. Worked example for `P_M` (illustration only)

With `α = 2`, `L* = 1 fm`, and `P_M = (L*/ƛ_C)² / (1 + (L*/ƛ_C)²)`:

| particle | ƛ_C | L*/ƛ_C | P_M |
|---|---:|---:|---:|
| electron | 386.159 fm | 0.00259 | 6.7 × 10⁻⁶ |
| proton | 0.2103 fm | 4.755 | 0.958 |
| **photon (massless)** | — (`ƛ_C→∞`) | — | **N/A** — mass channel inapplicable; scored via `P_D > 0` (§17 massless adapter), **not** `P_L = 0` |

This does **not** mean the proton "has Position 0.958" and the electron "has almost none." It means only: *relative to the task scale `L* = 1 fm`, the proton's mass Compton-capacity proxy is near-saturated and the electron's is not.* Choose a different `L*` and the numbers change. Therefore `L*` must be **task-specific, pre-registered, and never chosen after seeing the result.** *(All numbers verified numerically.)*

---

## 26. Claim–Evidence–Prediction–Test map

| ID | Claim | Status | Basis | Test |
|---|---|---|---|---|
| CORE.PMD.01 | `m·ƛ_C = ħ/c` | established | identity | unit check |
| CORE.PMD.02 | mass ↔ acceleration-susceptibility reciprocal | established (NR) | `a=F/m` | fixed-force test |
| CORE.PMD.03 | `F_Q ≤ 8mK/ħ²` | proved (scoped) | QFI + kinetic energy | displacement estimation |
| CORE.PMD.04 | context channels add Fisher info | proved | conditional independence | multi-detector experiment |
| CORE.PMD.05 | coarse-graining lowers position info | proved | data processing | sensor removal |
| CORE.PMD.06 | `g_M = x^α/(1+x^α)` | conditionally proved | log-odds axiom | calibration |
| CORE.PMD.07 | `α = 2` | model choice | inverse-variance scaling | model comparison |
| CORE.PMD.08 | `P = √(P_S·P_L)` | conditionally proved | separability + symmetry | rival aggregators |
| CORE.PMD.09 | interactions modify composite mass | established | invariant mass | mass-defect data |
| CORE.PMD.10 | context *always* increases mass | **false in general** | sign varies (χ_int) | binding controls |
| CORE.PMD.11 | mass = context | L3 interpretation | no derivation | independent `C_R` |
| CORE.PMD.12 | PMD adds prediction | **not yet** | requires `I>0` | held-out test |
| CORE.PMD.13 | `F_Q ≤ 4(⟨Ĥ²⟩−m²c⁴)/(ħ²c²)` | proved **(1 particle, free, `E>0`, `⟨Ĥ²⟩<∞`)** | operator identity + QFI | relativistic metrology |
| CORE.PMD.13b | `F_Q ≤ 8mK/ħ²` with **relativistic** `K` | **FALSE** — violated by `(√(1+ξ²)+1)/2` at every `ξ>0` | §12.1 counterexample | fixed-`K` metrology |
| CORE.PMD.14 | "more mass ⇒ more capacity" | **only at fixed *kinetic* energy** | reverses at fixed total `E` | budget must be declared |
| CORE.PMD.15 | `J_𝒞 = ε·u·(8mK/ħ²)` | **tautology** (definition); content is `ε,u ∈ [0,1]`, NR-scoped | Braunstein–Caves + PMD-2 | efficiency estimation |
| CORE.PMD.16 | `P_D^(1−η)P_M^η` double-counts mass | **WITHDRAWN v1.5.1** — bound is one-directional; dependence is empirical | replaced by the chain rule `ℰ_m(P_L) = (1−η)s_D + η·α(1−P_M)` (v1.5.2; the earlier `η+(1−η)s` was wrong) | estimate `s_D` on corpus |
| CORE.PMD.17 | per-meter ranking is `L*`-invariant | proved | uniform log-odds shift | scale sweep |
| CORE.PMD.18 | combined-score ranking is `L*`-invariant | **FALSE** (explicit counterexample) | 60.0 % of trade-off pairs flip under the published design; dominance pairs 0/5021 | dominance ⟹ robust (converse false); trade-offs need an `L*`-sensitivity interval |
| CORE.PMD.19 | `𝔼[Δ log-loss] = I(Y;C_R\|X_std)` | proved **for true conditionals only** | conditional entropies | permutation null; `Δ_CV` is a biased proxy |

---

## 27. Variable & equation registry

| symbol | meaning | units |
|---|---|---|
| `m` | invariant mass | kg |
| `ƛ_C` | reduced Compton wavelength | m |
| `L*` | target localization scale | m |
| `m* = ħ/(cL*)` | reference mass | kg |
| `x_M = m/m*` | Compton ratio | — |
| `J_𝒞` | classical Fisher information for position | m⁻² |
| `F_Q` | quantum Fisher information | m⁻² |
| `D_S` | KL support information | — |
| `P_S` | support / distinguishability score | [0,1) |
| `P_D` | detection / localization score | [0,1) |
| `P_M` | massive Compton-capacity score | [0,1) |
| `P_L` | combined localizability score | [0,1) |
| `η` | mass-proxy weight | — |
| `χ_int` | signed interaction-mass fraction | — |
| `C_R` | independently measured context | protocol-specific |
| `ε = J_𝒞/F_Q` | context efficiency (extraction fraction) | [0,1] |
| `u = F_Q/(8mK/ħ²)` | state utilization of the mass-energy ceiling (NR scope) | [0,1] |
| `E_kin = Ĥ − mc²` | relativistic kinetic energy | J |
| `(ΔH)²` | energy variance | J² |
| `λ` | reference-scale rescaling factor (`L* → λL*`) | — |
| `ξ = p/(mc)` | momentum in units of `mc` (relativity parameter — distinct from utilization `u`) | — |
| `s_D = ∂log P_D/∂log m` | population elasticity of detection w.r.t. mass | unbounded |
| `s_M = α(1−P_M)` | elasticity of the mass proxy | (0, α) |
| `ℰ_m(P_L)` | **realized** mass elasticity `= (1−η)s_D + η s_M` | unbounded |
| `U` | nested stability score | [0,1] |

---

## 28. Dependency graph

```
Standard physics
   ├── ƛ_C = ħ/(mc)
   ├── F = dp/dt
   ├── QFI / Cramér–Rao
   └── M²c² = P_μ P^μ
        │
        ▼
PMD mathematical bridge
   ├── mass capacity      P_M
   ├── detection info     P_D
   ├── support info       P_S
   └── interaction frac.  χ_int
        │
        ▼
Nested Position
   P_L = P_D^(1−η) · P_M^η
   P   = √(P_S · P_L)
        │
        ▼
SSS:  U = ∛(F · P · A)
        │
        ▼
Empirical test:  H₀ vs H₁ ,  I(Y ; C_R | X_std) > 0 ?
```

---

## 29. Open issues / calibration tasks (v1.6 roadmap)

1. Corrected §5 wording (done — v1.2.1).
2. ~~Replace `P_L = P_M` with the `P_D`-inclusive adapter~~ — **done in v1.4** (§5 core now `P_L = P_D^(1−η)·P_M^η`, `η = ½` default, **`0 < η < 1` strictly**); mass-only `P_L = P_M` is a **separate legacy comparator**, not a value of the adapter (v1.5.2).
3. Choose or compare `α ∈ {1, 2, free}`.
4. Fix `η` by pre-registration, never post hoc.
5. Declare the reference region `Ω` for `P_S`.
6. Set `L*` from task resolution, not from the result.
7. Separate internal-context from external/Machian context.
8. Use the **signed** `χ_int` (interactions can lower mass).
9. Compare the aggregator/meter rivals head-to-head: `P_S` ; `P_S·P_D` ; `P_S·P_M` ; `P_S·P_D·P_M`; **plus the two adapters raised in v1.5.2** — the **logit-inside** blend `σ((1−η)logit P_D + η logit P_M)` (§16.1e) and the **capacity/efficiency** blend `P_cap^(1−η)·P_eff^η` (§15.1). Six arms, pre-registered. *(Synchronised with item 11.)*
10. Count PMD as empirically upgraded **only** if `I(Y; C_R | X_std) > 0` — now quantified in **nats** by PMD-12 (§23.1).
11. **Measure, do not assume, any `P_D`–`P_M` dependence** in the scored population (§15.1), and calibrate `P_D^(1−η)P_M^η` against the `P_cap^(1−η)·P_eff^η` blend **and** against the logit-inside adapter (§16.1e) — three rivals, pre-registered.
12. **Report `L*`-sensitivity** for every trade-off ranking (§16.1c) — dominance rankings are exempt.
13. **Declare the energy budget** (fixed kinetic vs fixed total-`⟨Ĥ²⟩`) in every capacity claim (§12.1) — the mass effect reverses between them.
14. **Estimate `s_D`** on the scored corpus and report the realized mass elasticity `ℰ_m(P_L) = (1−η)s_D + η·α(1−P_M)` (§15.1) — `η` alone does not determine it, and `ℰ_m` is a **local log-elasticity, not a weight in `[0,1]`**.
15. **Use a permutation null** for any surplus claim, and never read `Δ_CV > 0` as `I > 0` without a well-specified model class (§23.1).

---

## 30. Strongest formulation of the hypothesis (replaces "mass = concentrated context" as the core)

> **PMD Localization-Leverage Hypothesis.** In the massive non-relativistic sector, invariant mass bounds the spatial Fisher information available per unit kinetic-energy budget,
> ```
> F_Q / K ≤ 8m / ħ²
> ```
> and the measurement context bounds how much of that available information is actually extracted,
> ```
> J_𝒞 ≤ F_Q .
> ```
> Hence mass and context have distinct, complementary roles:
> ```
> ■  mass sets capacity ;  context realizes accessibility .
> ```
> **Scope (v1.5.2).** "Capacity" is defined at a **fixed kinetic-energy budget** *(with its second moment pinned — §12.1)*; at fixed *total* energy the mass dependence reverses (§12.1). The three-way split of that capacity, `J_𝒞 = ε·u·(8mK/ħ²)`, is a **definitional decomposition**, not a theorem — its content lies entirely in the scoped ranges `ε, u ∈ [0,1]` (§15.1).

So the defensible corpus statement is **not** `Mass = Context` but

```
■  Position quality = f( massive capacity , spatial state , measurement context )
```

---

## References & provenance
- **Parent record:** U-Theory / U-Model — DOI **10.17605/OSF.IO/74XGR** · https://u-model.org
- **Sibling appendices:** `MMT` (matter = crystallized meaning), `DIM`, `ST`/DPR (currency registry), `QMC` (measurement/localization), `GEN`, `SSS`, `RH`, `POS`.
- **Physics anchors (established):** the **reduced** Compton wavelength `ƛ_C = ħ/mc` (ordinary `λ_C = h/mc`) & the pair-creation one-particle localization limit; the relativistic dispersion `E² = p²c² + m²c⁴` and photon `p = E/c`; inertia via `F = dp/dt` (`F ≈ ma` at low `v`); the absence of a sharp Newton–Wigner position operator for massless spin > ½; quantum Fisher information & the Cramér–Rao bound; Fisher-information additivity and the data-processing inequality; invariant mass `M²c² = P_μ P^μ`; Mach's principle (historical, only partially realized in GR via frame-dragging); the Higgs mechanism (elementary masses; composite mass mostly QCD binding); the position–momentum uncertainty relation.
- **Author:** Petar Nikolov (ORCID 0009-0001-8669-2276). © 2026, CC BY 4.0 (text) / MIT (any code).

---

## Changelog

| version | date | change |
|---|---|---|
| **v1.5.3** | 2026-07-25 | **Consistency sweep — clears the stale v1.5.1 wording that the v1.5.2 fixes had left contradicting themselves.** §5 nesting box no longer presents `η = 1` as a "special case" (it breaks the control; mass-only is a **separate legacy comparator**); §1 no longer names **Mass** as the second sub-price (now *localization accessibility*, mass a proxy inside it); §5 table's currency column for face (ii) changed `Mass` → `P_L`; `CORE.PMD.16` carries the corrected chain-rule elasticity instead of the withdrawn `η_eff`; `CORE.PMD.18` cites the published-design figures (60.0 % flip, 0/5021 dominance) and states *dominance ⟹ robust, converse false*; §29.2 / §29.9 / §29.14 and the footer synchronised (six pre-registered aggregator arms, `s_D` + `ℰ_m` reporting); §16.1 subsections reordered `(d)` ↔ `(e)` with cross-references rewired; §30 scope label bumped and its second-moment condition noted; epigraph flagged **historical** (the canonical law is the v1.5.2 §5 restatement); status header shortened; new note that `ℰ_m` is a **log-elasticity, not a weight in `[0,1]`**. |
| **v1.5.2** | 2026-07-25 | **Second deep review applied — four further errors corrected, plus scope repairs.** (1) **`η_eff` was wrong**: the correct mass elasticity is `ℰ_m(P_L) = (1−η)s_D + η·α(1−P_M)`, not `η+(1−η)s` (which assumed `s_M = 1`; numerically `0.609` vs true `1.026` at `m=0.3`); the bounds `s_D ∈ [0,1]` and `η_eff ∈ [η,1]` are **withdrawn**, and correlation ≠ elasticity. (2) **"dominance ⟺ robustness" was an overclaim** — dominance is *sufficient*, not necessary — under the published, seeded design **40.0 %** of trade-off pairs are stable (and `0/5021` dominance pairs flip). (3) **The ground for rejecting logit-inside aggregation was invalid**: `∂lnU/∂lnP_S = 1/6` **exactly** for both adapters (the v1.5.1 figure came from applying the logit mean at the *top* level); the logit adapter is reinstated as a legitimate pre-registerable rival. (4) **`η = 1` breaks the massive-but-delocalized control** (`P_L = P_M > 0`, and `0⁰` is indeterminate) — the canonical adapter now requires **`0 < η < 1`**, with mass-only kept only as a separate legacy comparator. **Scope repairs:** §5 law restated as *distinguishability + localization accessibility* (mass is a proxy **inside** `P_L`, not a universal sub-price — the massless branch pays no mass); PMD-3 restricted to product/conditionally-independent channels; PMD-4 requires a parameter-independent kernel; PMD-8's kinetic/field/interaction split declared **partition- and scheme-dependent** (`χ_int` is baseline-dependent); PMD-9 reproved by conditional independence (valid for continuous `C`); §24's "equivalently `I>0`" removed; fixed-`K` claims must also pin `(ΔH)²`; `ε`/`u` degenerate cases tabulated; `P_S = 0` clarified as *no contrast vs the declared prior*; two-particle counterexample notation disambiguated (`M_Σ = 2m`); symbol collision resolved (`ξ = p/mc` vs utilization `u`); Monte-Carlo figures given a documented, seeded generating design (script published). |
| **v1.5.1** | 2026-07-25 | **Self-correction after adversarial review of the v1.5 draft — three real errors fixed, one claim withdrawn.** (1) **PMD-2R inference was backwards**: the non-negative relativistic corrections mean the relativistic ceiling *exceeds* `8mK/ħ²`, so PMD-2 is **not** a relativistic bound — it is violated at *every* nonzero momentum by the exact factor `(√(1+ξ²)+1)/2`, `ξ ≡ p/mc` (1.207 at `ξ=1`, 50.5 at `ξ=100`). PMD-2 is now stated as valid **iff** `K ≡ ⟨p̂²⟩/2m`, i.e. as a rewriting, and strictly NR. (2) **`E² → ⟨Ĥ²⟩`**: at fixed *mean* energy the ceiling is unbounded (`(ΔH)²` is free), so the total-energy budget must be stated as fixed second moment; the reversal was also mislabelled relativistic-vs-NR when it is fixed-`K`-vs-fixed-`E`. (3) **PMD-11's mechanism was wrong**: the failure is caused by the **concavity of `log σ`**, not by unequal logit shifts — it occurs even at `α=2` where the shifts are equal (new explicit counterexample table). (4) **Withdrawn:** the "adapter double-counts mass" claim — the bound is one-directional, `J_𝒞` is not monotone in `m`, and dependence is empirical; replaced by the checkable `η_eff = η + (1−η)s`. Also: PMD-2R scoped to one-particle/free/positive-energy/`⟨Ĥ²⟩<∞` (the identity **fails for `N>1`**); PMD-10 demoted from theorem to a definitional decomposition with `ε,u` range scopes; PMD-12 given four estimator caveats (misspecification, CV bias, fold dependence, plug-in MI bias). |
| **v1.5** | 2026-07-25 | **Mathematical-apparatus upgrade (4 new theorems, 1 negative result).** **PMD-2R** (§12.1): exact relativistic bound `F_Q ≤ 4(⟨Ĥ²⟩−m²c⁴)/(ħ²c²)` via the operator identity `Ĥ²=p̂²c²+m²c⁴`, ~~with PMD-2 recovered as its leading term~~ *(**superseded v1.5.1** — the inference was backwards)*; ~~parametrization-reversal caveat as first stated~~ *(**superseded v1.5.2** — needs `⟨Ĥ²⟩`, not `E²`)*, and **one concrete falsifiable ceiling** `Var(x̂) ≥ ħ²/(8NmK)`. **PMD-10** (§15.1): capacity–efficiency factorization `J_𝒞 = ε·u·(8mK/ħ²)`, ~~which proves a mass double-count in the adapter~~ *(**withdrawn v1.5.1** — the bound is one-directional; dependence is empirical)*, and the `P_cap`/`P_eff` alternative. **PMD-11** (§16.1): per-meter reference-scale invariance **proved**, combined-score invariance **disproved** with an explicit counterexample (~~59.8 %~~ → **60.0 %** under the published seeded design, v1.5.2), ~~yielding a "dominance-only" rule~~ *(**corrected v1.5.2** — dominance is sufficient, not necessary)*; ~~the log-odds fix is rejected because it breaks PMD-7's `1/6` elasticity~~ *(**invalid ground, reversed v1.5.2** — `∂lnU/∂lnP_S = 1/6` for both adapters; the logit blend is reinstated as a rival)*. **PMD-12** (§23.1): exact surplus identity `𝔼[Δ log-loss] = I(Y;C_R\|X_std)`, making PMD-9 its zero case and giving effect sizes in nats. All results verified numerically. **No new physics.** |
| **v1.4.1** | 2026-07-25 | Final review polish: `P_L` registry range → `[0,1)` (consistent with `P_S`/`P_D`/`P_M`); §8 "as of" version bumped to v1.4; §19 cross-reference rewired to §29.9 four-model comparison (§24 has no explicit aggregator arm). |
| **v1.4** | 2026-07-25 | **Review-hardening (P0/P1/P2).** Adopted the §17 adapter into the §5 core meter: `P_L = P_D^(1−η)·P_M^η` (pre-registered `η=½`; `P_L=P_M` retained as the `η=1` legacy Compton reading) — the two negative controls now hold *by construction*, resolving the §5↔§17 dual-state. Clarified context ≔ **channel `𝒞`** vs its Fisher **content `J_𝒞`** (§5). Added: PMD-2 non-relativistic **scope caveat** (§12); PMD-4 **regularity** note (§14); PMD-6 **rival-aggregator** scope (§19); `[0,1)` ranges (§10, §27); **raw-observable** protocol to kill circularity in §24 (`Y` must not be `P_D`); a massless-photon **negative-control row** (§25); PMD-7 adapter elasticity split (§20); epigraph *figurative* footnote; minimal reading-path guide; §29 renamed to v1.5 roadmap. **No new physics; PMD-2/PMD-9/χ_int/§30 untouched.** |
| **v1.3** | 2026-07-25 | **Single-document merge.** Folded the entire formal layer (former `APPENDIX_PMD_MATH`) into this file as **PART II (§9–§30)**: all theorems PMD-1…9 with proofs, the operational meters (`P_D`, `P_M`, `P_S`), the upgraded adapter, the composite-mass `χ_int`, the empirical no-go, the CEPT map, registry, and dependency graph — nothing dropped. Part I (§0–§8) is the interpretation; per-result epistemic labels live in Part II. Internal cross-references rewired to the merged numbering. |
| **v1.2.1** | 2026-07-25 | Consultant v1.2 + PMD-MATH §2.3 fix: the residual §5 "massless⇒delocalized" wording corrected (at `m→0` the mass channel `P_M` vanishes but `P_L` via `P_D` need not; unpaid Position needs **both** `P_S→0` **and** `P_L→0`). |
| **v1.2** | 2026-07-25 | Consultant review-hardening: anti-fourth-pillar note (§3); operational `Context_proxy` placeholder (§5); `resist Δmomentum` table wording; QCD internal-interaction justification (§8); Machian scope qualifier (§7); explicit **no present empirical surplus** clause; changelog table. |
| **v1.1.2** | 2026-07-25 | Review polish draft: QCD strengthens-the-reading argument; §3 nested-sub-price note; §7 Machian qualifier. |
| **v1.1.1** | 2026-07-19 | §8 discipline through the body: massless ≠ delocalized; inertia resists Δmomentum not displacement; Higgs = VEV coupling not drag; massless adapter `g_0`; `H₀` and negative controls. |
| **v1.1** | 2026-07-19 | Physics-hardened core: reduced Compton `ƛ_C`; relativistic `F = dp/dt`, `p = γmv`, photon `p = E/c`; nested meter `P = √(P_S·P_L)`; mass `P_M` as one proxy only in the massive rest-frame sector. |

*Status: **v1.5.3 single document** — Part I is L3/L4 speculative interpretation on a rigorous physical core; Part II is the formal layer (L1/L2 proved core: `m·ƛ_C = ħ/c`; `F_Q ≤ 8mK/ħ²`; Fisher additivity `J_𝒞 = Σ Jₖ`; data-processing monotonicity; nested-mean uniqueness `P = √(P_S·P_L)`; composite mass `Mc² = E_COM` with signed `χ_int`; empirical no-go `C = f(X_std) ⇒ I(Y;C|X_std) = 0`; **v1.5 additions:** exact relativistic bound PMD-2R, capacity–efficiency factorization PMD-10, reference-scale invariance PMD-11 (per-meter **yes**, combined score **no**; dominance ⟹ robust, converse false — trade-off comparisons need an `L*`-sensitivity interval), surplus identity PMD-12 (true conditionals only); **v1.5.1 records three corrected errors and one withdrawn claim from the v1.5 draft**; L3 modelling choices: `P_M`, `P_D`, `P_S`, `α = 2`, `η`). The one-particle reduced-Compton localization scale is textbook physics; reading mass as the Position-currency's context/inertia price is a U-Theory interpretation, not a derivation; "mass = context" is **not** upgraded by the formal layer and remains L3/L4. Position pays twice — in space, and in mass — **for a massive particle in its rest frame.***
