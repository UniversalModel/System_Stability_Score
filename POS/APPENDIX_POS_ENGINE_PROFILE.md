# ═══════════════════════════════════════════════════════════════════════════════
# APPENDIX POS-EP — ENGINE PROFILE: UNIVERSAL FORMAL BASE & DOMAIN ADAPTERS
# ═══════════════════════════════════════════════════════════════════════════════
### *One kernel, many domains — the companion build sheet to the Principle of Sequence*

> **Copyright © 2026 Petar Nikolov. Licensed under CC BY 4.0.**
> **Companion to `APPENDIX_POS` — U-Theory / U-Model v.28 appendix series** | Aligned with SSS / GSI-RTD / TE / TAA
> **Status:** L2 methodology — a **commitment-control engine profile**: the universal formal kernel plus its per-sector adapters.
> **Version:** 1.1
> **Epistemic Level:** B2 / L2 — a disciplined, inspectable operationalization of the POS commitment gate. The claim that readiness-gated commitment beats ungated alternatives at equal cost is a **pre-registered hypothesis**, not a validated result.
> **Author:** Petar Nikolov (ORCID 0009-0001-8669-2276)
> **Prerequisites:** `APPENDIX_POS` (the gate), `APPENDIX_SSS` (the score), `APPENDIX_GSI-RTD` (the runtime), `APPENDIX_TE` (the umbrella)
> **v26 Invariant:** Form ↔ Time · Position ↔ Space · Action ↔ Energy

---

> **Epistemic banner (read once, applies everywhere below).** Everything in this profile — the kernel formalism, the type system, every adapter, and every worked number — is an **L2/B2 candidate operationalization**, **NOT** a validated law and **NOT** a theorem of `U = ∛(F·P·A)`. Every illustrative figure is **illustrative — ZERO decision authority** and **research-use-only (RUO)**. The decisive arbiter of whether any of this pays is the still-**unrun** calibration test **POS-P1 / POS-P2**. A formula makes a claim *inspectable*; it does not make it *true*.

---

## 0. Purpose & how to instantiate

`APPENDIX_POS` states the commitment gate once, abstractly. This profile is its **build sheet**: it shows that the gate is a *single reusable engine* and that a new sector is added not by rewriting the engine but by writing one small, quarantined translator. The document is deliberately split in two, and the split is the load-bearing idea.

**The kernel-vs-adapter separation.**

- The **universal kernel** (§§1–10) owns everything domain-*invariant*: the formal universe `D_d = (X_d, O_d, A_d, Y_d, T_d, W_d)`, the type system, the zero-clamped geometric sub-aggregator, the critical-component veto, the robust readiness ratio `R_rob`, the LCB/coverage discipline, the irreversibility/exposure kernel `(κ, e)`, the three-door gate `G_POS`, the control objective, the stopping heuristic `τ_POS`, the calibration/falsifier machinery, and the within-model properties POS-F1…F8. The kernel **never sees native units.** It reads only typed inputs in `[0,1]`, veto bits in `{0,1}`, and `(κ, e, s)` tags.
- A **domain adapter** `DA_d = (Ψ, N, G, Θ, K, L, C, V)` owns everything domain-*specific*, and nothing else. It is the *only* place a sector's raw units, its optimism, and its ethics are allowed to live. Because trading, medicine, factories, and rocketry differ **only** in their adapter and share **one** kernel, a property proven or a bug fixed in the kernel holds for all of them at once, and no sector can smuggle its units or its shortcuts past the boundary.

**The 4-step instantiation recipe.** To bring a new domain under the engine:

```
1. MAP     domain quantities → F/P/A indicators, each normalized to [0,1]
           (Ψ carries units; N strips them; declare direction, range, outlier &
            missing policy, and monotonicity BEFORE the gate is evaluated)
2. ATTACH  the tags: irreversibility κ (prefer κ_H = 1 − ρ_H when a transition
           model exists), normalized exposure e, and stakes s — kept SEPARATE,
           never collapsed into one number
3. CALIBRATE  the thresholds θ (θ_F, θ_P, θ_ij^crit, α(s), κ_probe, e_cap) per
              POS-P1 — until then every θ is illustrative, ZERO decision authority
4. WIRE    the gate at the commit boundary: G_POS = C_d · 1[G_probe ∨ G_ready ∨ G_emg],
           firewall-dominant, critical veto ∏_{i∈{F,P}} H_i (= H_F·H_P) wired IN, gating on Form-then-
           Position only (Action is the pillar spent by the commitment, not a gate)
```

The kernel gates on **Form and Position** — the base every future `U` multiplies against — and treats **Action** as the pillar *spent* by the commitment, read for triage and reward-shaping but not as a commit veto. Preserve the invariant throughout: **Form ↔ Time · Position ↔ Space · Action ↔ Energy.**

**The five shipped adapters.** This release ships five reference instantiations, each conforming to `DA_d` and each carrying its own firewall, worked example, and 16-point compliance map:

| Adapter | Domain | `a^commit` (the gated object) | Firewall anchor |
|---|---|---|---|
| **Research** | Labs & scientific programmes | Launch a large pre-registered study / lock a research direction | IRB · DURC dual-use · legal · biosafety |
| **Investment funds** | Capital allocation, LBO & restructuring | Full leveraged buyout / major fund allocation | Securities law · antitrust · fiduciary · ESG red-lines |
| **Factories** | Industrial operations & safety | Major line changeover / capacity scale-up / new-product launch | Worker safety · environmental permits · product-safety regulation |
| **Government administration** | Public programmes, reforms, procurement | Launch a major reform / large programme / irreversible procurement | Constitutional & legal limits · GDPR · anti-corruption / procurement law |
| **Military-space & aerospace** | Missions, launch, defense systems (per `APPENDIX_TRA`) | Launch / commit to an irreversible mission phase | **Non-negotiable HARD dual-use firewall** — own-vehicle / stabilize-only; weaponization type-forbidden · MTCR / export-control (`APPENDIX_WAR`) |

Each adapter fills the same eight slots in the same order, so a reader who learns one learns all five; only the units, the indicators, and the firewall clauses change. The kernel underneath is byte-for-byte the same.


---

# PART I — THE UNIVERSAL KERNEL  *(domain-invariant — one engine for every sector)*

## 1. Formal universes

The kernel treats every sector as an instance of one abstract dynamical universe. A **domain** `d` is a modelled slice of the world — a body under training, a firm, a clinical protocol, a power grid, a governance reform, a trading book — and the kernel never sees its native units directly. It sees a **formal universe** `D_d`, a typed object the domain must supply:

```
D_d = ( X_d ,  O_d ,  A_d ,  Y_d ,  T_d ,  W_d )
```

| Component | Name | Reading |
|---|---|---|
| `X_d` | state space | the full latent condition of the system — what is true whether or not it is observed |
| `O_d` | observation space | what the domain can actually measure, generally a lossy image of `X_d` |
| `A_d` | action space | the interventions available, each carrying a `κ` irreversibility tag (see §2, K-map) |
| `Y_d` | outcome space | the externally-scored consequences (task success, damage, cost, survival, regret) |
| `T_d` | time index | discrete `t ∈ {0,1,2,…}`, continuous `t ∈ ℝ_≥0`, or an event index; the currency of **Form** |
| `W_d` | disturbance space | exogenous noise, adversaries, shocks — everything the controller does not choose |

**Dynamics.** State evolves under a domain transition operator driven by the chosen action and the disturbance:

```
x_{t+1} = f_d( x_t , a_t , w_t ) ,        w_t ~ P_d^W( · | x_t )
```

**Observation.** The controller reads state only through a domain observation channel with its own measurement noise:

```
o_t = h_d( x_t , v_t ) ,                  v_t ~ P_d^V( · | x_t )
```

`f_d` and `h_d` are **carriers of the invariant**, not free choices of notation. `f_d` advances the system in `T_d` — it is where **Form ↔ Time** lives: Form is what must persist step to step for the base to survive `f_d` unbroken. The *reachable* region of `X_d` under `f_d` from the current state — where the system can stand and be defended — is where **Position ↔ Space** lives. The selection and injection of `a_t` into `f_d` — the expenditure that changes state — is where **Action ↔ Energy** lives. The kernel's job in §2–§3 is to read F, P, A *out of* `D_d` without ever importing its raw units.

**Model-class agnosticism (load-bearing for interdisciplinary use).** `f_d` and `h_d` are contracts, not commitments to a single mathematical form. The kernel accepts any model class that can present the `(f_d, h_d)` interface:

| Model class | How `f_d`/`h_d` are supplied |
|---|---|
| Deterministic | `w_t ≡ 0`, `v_t ≡ 0`; `f_d`, `h_d` are ordinary maps |
| Stochastic | `f_d`, `h_d` are kernels; `P_d^W`, `P_d^V` are declared distributions |
| Bayesian / latent-state | `x_t` is a posterior belief; `f_d` is a filtering/prediction step |
| Simulation / Monte-Carlo | `f_d` is a black-box sampler; readiness read from sample statistics |
| ODE / continuous-time | `f_d` is a flow `dx/dt = f_d(x,a,w)`; `T_d ⊆ ℝ_≥0` |
| Agent-based | `x_t` is the joint micro-state; `f_d` is the interaction update |
| Graph / network | `X_d` carries a graph; `f_d` is a propagation/diffusion operator |
| Data-driven / learned | `f_d`, `h_d` are fitted estimators with a declared uncertainty model |

The kernel is **indifferent** to which of these a sector uses. It requires only that the model expose state transition, observation, an action set with irreversibility tags, and outcomes — and that whatever uncertainty the model carries be *declared before* the gate reads it (the pre-declaration discipline of APPENDIX_POS §2.6.2, inherited here unchanged).

> **Epistemic status.** `D_d` and the `(f_d, h_d)` contract are an **L2/B2 candidate operationalization**, not a validated law and not a theorem of `U = ∛(F·P·A)`. Any structure, constant, or number appearing in a `D_d` instance is **illustrative — ZERO decision authority**, **research-use-only (RUO)**. The decisive arbiter of whether this formalization pays remains the unrun calibration test **POS-P1 / POS-P2**.

---

## 2. Domain Adapter Contract

The kernel cannot and must not know that a domain measures milliliters of lactate, basis points of spread, or seats in a coalition. Everything sector-specific is quarantined in one object — the **Domain Adapter** — and the kernel consumes **only its typed output**. This quarantine is not a convenience; it is **the single enabler of interdisciplinary use**: because trading, medicine, and governance differ *only* in their adapters and share *one* kernel, a result proven or a bug fixed in the kernel holds for all of them at once, and no sector can smuggle its units, its optimism, or its ethics-blind shortcuts past the boundary.

The adapter for domain `d` is the tuple:

```
DA_d = ( Ψ_d ,  N_d ,  G_d ,  Θ_d ,  K_d ,  L_d ,  C_d ,  V_d )
```

| Symbol | Role | What it must deliver to the kernel | Reading |
|---|---|---|---|
| `Ψ_d` | **extract** | maps `o_t` (and admissible history) to raw F/P/A indicator vectors `r_t^F, r_t^P, r_t^A`, each element carrying explicit units | the *only* place raw domain units are legal |
| `N_d` | **normalize** | per-indicator maps `R[u] → [0,1]` with declared direction, valid range, outlier & missing policy, calibration date (§3) | strips units; makes indicators comparable |
| `G_d` | **aggregate** | the per-pillar sub-aggregators `G_F, G_P, G_A` (weighted geometric, zero-clamped; §3) and the critical-veto channels `H_i` | collapses each indicator vector to one pillar readiness + a veto bit |
| `Θ_d` | **thresholds** | the readiness thresholds `θ_i(a,d,s)` and critical thresholds `θ_ij^crit` (calibration candidates, POS-P1) | the *when* of the gate |
| `K_d` | **irreversibility / recoverability** | the irreversibility tag `κ(a) ∈ [0,1]`, normalized exposure `e(a)`, and recoverability / recovery-cost metadata per action | separates probes from commitments |
| `L_d` | **losses / outcomes** | the outcome map into `Y_d` and the loss functions `L(a)`, `L(inaction)` on a common declared scale | feeds outcome scoring and the emergency branch |
| `C_d` | **feasibility / safety constraints** | the hard feasibility and domain safety set — actions physically impossible or operationally unsafe | pre-filters `A_d` before any readiness math |
| `V_d` | **values / legal / ethics firewall** | the boolean `Firewall_d(a) ∈ {PASS, FAIL}` over ethics, law, dual-use | **dominates every readiness result** |

**The consumption rule (the boundary).**

```
raw domain units  ──►  Ψ_d  ──►  N_d  ──►  typed kernel input ∈ [0,1]^• × {0,1}^• × tags
                                              │
  the kernel reads ONLY from here ────────────┘   (it never touches R[u])
```

The kernel's readiness and authorization logic (§3, and the gate of APPENDIX_POS §2.6) is defined **entirely** over the typed adapter output: normalized pillar scores in `[0,1]` with lower confidence bounds, veto bits in `{0,1}`, and the `(κ, e, s)` tags. It has **no path** to `R[u]`. This is what makes "the same code serves a trading system, a clinical protocol, and a governance reform" (APPENDIX_POS §10) a structural guarantee rather than a slogan.

**Firewall / feasibility dominance.** `V_d` and `C_d` are evaluated *first* and *categorically*. No readiness score, however high, and no irreversibility tag, however favorable, overrides a `Firewall_d(a) = FAIL` or a `C_d` infeasibility. This is the kernel-level restatement of the two-meanings-of-forbidden discipline (APPENDIX_POS §7): sequencing can unlock a *hard* action; it can never legitimize a *wrong* or *infeasible* one.

> **Epistemic status.** Every component of `DA_d` is an **L2/B2 candidate operationalization**, RUO. The adapter makes a domain's F/P/A claims *inspectable*; it does not make them *true*. All coefficients, thresholds, and mappings inside a concrete adapter are **illustrative — ZERO decision authority** until POS-P1 calibrates them against the domain's external outcomes.

---

## 3. Measurement & type system

This section fixes the types that cross the adapter boundary and the two correctness-critical aggregation rules that operate on them: the **zero-clamped geometric sub-aggregator** and the **critical-component veto**.

### 3.1 Raw indicators carry units

Every raw indicator is a real number tagged with an explicit unit; units never leave `Ψ_d`:

```
r_tj^i ∈ R[u_ij]        i ∈ {F, P, A} ,  j = 1 … n_i ,  time t
```

`u_ij` is the declared unit of indicator `j` of pillar `i` (e.g. `ms`, `bp`, `mmol·L⁻¹`, `count`, `dimensionless`). Two indicators may be combined only *after* normalization, never in raw form — the kernel has no unit algebra and must not acquire one.

### 3.2 Normalization: `n : R[u] → [0,1]`

Each indicator has a normalizer `n_ij` mapping its raw value to a unit-free readiness score in `[0,1]`. Every normalizer must publish a fixed **spec block** — declared *before* the gate reads it (the no-friendlier-model-after-the-fact rule, APPENDIX_POS §2.6.2):

| Spec field | Required content |
|---|---|
| **Direction** | one of `higher-better` / `lower-better` / `target-band` (best inside `[lo*, hi*]`, decaying outside) |
| **Valid range** | `[r_min, r_max]` in `R[u]`; values outside are handled by the outlier policy, not silently clipped to a passing score |
| **Outlier policy** | declared rule (e.g. winsorize at published quantiles, or route to `missing`) — never a rule chosen after seeing the value |
| **Missing-data policy** | explicit map for absent/stale inputs; default is **conservative** (missing ⇒ low readiness or veto trigger, never a free pass) |
| **Calibration date** | the date the normalizer's anchors were last fit; stale calibration is itself an audit flag |

**Monotonicity requirement.** Within its valid range each normalizer must be monotone in the declared direction — strictly for `higher-better` / `lower-better`, and monotone toward the band centre on each side for `target-band`. This guarantees that "a better raw measurement never lowers the normalized readiness," so the sub-aggregator and the gate inherit a well-defined sensitivity. A non-monotone `n_ij` is a specification error, not a modelling choice.

```
n_ij : R[u_ij] → [0,1] ,     monotone in the declared direction on [r_min, r_max]
z_tj^i := n_ij( r_tj^i )      the normalized indicator the kernel consumes
```

### 3.3 Per-pillar sub-aggregation: weighted geometric mean, zero-clamped

The normalized indicators of a pillar are combined by a **weighted geometric** sub-aggregator, mirroring the geometric non-compensation of `U = ∛(F·P·A)` one level down:

```
G_i(z) = ∏_{j=1..n_i} z_j^{ w_ij }        w_ij ≥ 0 ,   ∑_j w_ij = 1 ,   z_j ∈ [0,1]
```

**FIX 1 — the zero-clamp (do not reintroduce the ε bug).** `G_i` maps a **true zero to exactly 0**: if any structurally-required or genuinely-measured-zero component `z_j = 0` is present, `G_i(z) = 0`, full stop — no surplus in the other indicators can rescue the pillar. A logarithmic form may be used *only* as a numerical device on **strictly-positive, noisy** measurements:

```
log G_i(z) = ∑_{j=1..n_i} w_ij · log( z_j + ε )        ONLY IF every z_j > 0 (strictly positive, noisy)
```

Here `ε > 0` exists **solely** to avoid a numerical `−∞` on strictly-positive readings; it is **never** a semantic floor. The binding rule:

```
if  ∃ j : z_j is a structural / true zero      →   G_i(z) := 0   (HARD CLAMP; the log form is not used)
else (all z_j strictly positive)               →   G_i(z) = exp( ∑ w_ij · log(z_j + ε) )
```

`ε` must **never** convert a true zero into a passing score. Any implementation that lets `log(0 + ε)` produce a finite, non-veto contribution for a genuine zero has reintroduced the bug.

### 3.4 Critical-component veto channel `H_i`

Some indicators are **non-compensable by design**: a single critical failure must veto the whole pillar regardless of the geometric score. The adapter marks a subset `crit(i) ⊆ {1…n_i}` of critical indicators, each with a critical threshold `θ_ij^crit`, and the kernel computes a veto bit on **lower confidence bounds** (never point estimates):

```
H_i = 1[ ∀ j ∈ crit(i) :  LCB( z_ij ) ≥ θ_ij^crit ]        H_i ∈ {0,1}
```

`H_i = 0` (any critical component below its bound) forces the pillar to fail readiness *irrespective* of `G_i`.

### 3.5 Pillar readiness

A pillar is ready only if **both** its geometric aggregate clears the pillar threshold on a lower confidence bound **and** its critical veto passes:

```
PillarReady_i = 1[ LCB( G_i ) ≥ θ_i ] · H_i        i ∈ {F, P, A}
```

The `LCB` here is the same uncertainty-aware lower bound the commitment gate uses (APPENDIX_POS §2.6.2): readiness is asserted on a conservative bound, never on an optimistic point estimate.

### 3.6 Readiness authorization with the critical veto wired in

**FIX 2 — critical-veto wiring (so POS-F2 non-compensation is actually a theorem).** The kernel's readiness authorization is the readiness ratio **times the product of the vetoes**, equivalently the minimum pillar-readiness:

```
R_rob = min(  LCB(G_F)/θ_F ,  LCB(G_P)/θ_P  )          (robust readiness ratio, F & P per POS)

G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i
        = min_i PillarReady_i                            (equivalent form)

with     H_i = 1[ ∀ critical j :  LCB(z_ij) ≥ θ_ij^crit ]
```

Because the veto enters as a *multiplicative* `∏_i H_i` (equivalently `min_i`), a single critical shortfall drives `G_ready` to 0 no matter how large the compensating scores elsewhere. **Only with the veto wired this way is "critical non-compensation" (POS-F2) an actual theorem of the kernel** rather than an aspiration; drop the `∏_i H_i` factor and non-compensation is silently lost. `G_ready` is the readiness input to the full POS authorization gate `G_POS` (APPENDIX_POS §2.6.3), which additionally requires `Firewall(a) = PASS` and admits the probe and forced-move branches.

### 3.7 Stopping time — a heuristic, not an optimum

**FIX 3 — do not claim optimality for one-step lookahead.** The kernel exposes a commitment stopping time, defined as the earliest moment either readiness clears or an emergency fires:

```
τ_ready = inf{ t : G_ready(t) = 1  ∧  Firewall(a_t) = PASS }
τ_emg   = inf{ t : G_emg(t) = 1 }
τ_POS  := min( τ_ready , τ_emg )
```

`τ_POS` is a **one-step-lookahead commitment heuristic**: it commits as soon as the readiness/emergency predicate holds, comparing "commit now" against "wait one step," and is **not claimed optimal**. A genuine optimal stopping claim requires the full continuation value — the Snell envelope:

```
V_wait(t) = max(  V_commit(t) ,  E[ V_wait(t+1) | information_t ]  )
```

and only a policy solving that envelope may be called *optimal*. The kernel ships `τ_POS` as the disciplined default and flags `V_wait` as the research upgrade. Note also that `τ_POS` is defined once as a `min` of two hitting times — it is **never** accumulated or mutated (`τ_POS += …` is a category error, since a stopping time is a single first-passage instant, not a running total).

### 3.8 Confidence coverage — per-component vs. joint (record which)

The scalar lower bound `SCALAR_LCB` used above delivers only **per-component** `(1 − α_j)` coverage — it guarantees the bound for *one* indicator or pillar at a time. Asserting a **joint** `(1 − α)` statement across `m` components does **not** follow from stacking per-component bounds; by the union bound the honest joint guarantee is only:

```
P( ∀ j :  z_j ≥ LCB_{α_j}(z_j) )  ≥  1 − ∑_{j=1..m} α_j          (union bound)
```

To make a genuine joint `(1 − α)` readiness claim across `m` components, the adapter must either:

| Method | Rule | When |
|---|---|---|
| **Bonferroni** | set each `α_j = α / m` so `∑ α_j = α` | small `m`, simple and conservative |
| **JOINT_CHANCE** | a joint chance constraint solved directly | correlated components, moderate `m` |
| **DRO** | distributionally-robust bound over an ambiguity set | model/ distribution uncertainty |

Whichever is used **must be recorded** in the adapter's spec block alongside the calibration date. A readiness claim that quietly reuses per-component `α` as if it were joint has overstated its confidence by up to `∑ α_j`.

> **Epistemic status.** The entire type system, the geometric sub-aggregator, the veto channel, `G_ready`, and `τ_POS` are **L2/B2 candidate operationalizations**, RUO. Every weight `w_ij`, threshold `θ_i` / `θ_ij^crit`, `ε`, `α`, horizon, and loss scale is **illustrative — ZERO decision authority** until fit and validated. None of this is a theorem of `U = ∛(F·P·A)` — the geometric forms *echo* the keystone but do not derive the gate from it (APPENDIX_POS §3.1). Making a measurement formula explicit makes its claim *inspectable*; it does not make the claim *true*. The decisive arbiter remains the unrun calibration test **POS-P1 / POS-P2**.

## 4. Readiness kernel

The kernel's first job is a **verdict**: given a candidate action `a` at time `t`, is the base *ready* to carry it? Readiness is read per pillar, per indicator, always on a **lower confidence bound** (LCB) and never on an optimistic point estimate — inheriting the confidence discipline of `APPENDIX_POS §2.6.2`. Everything below is a **L2/B2 candidate operationalization**, not a validated law and not a theorem of `U = ∛(F·P·A)`. The decisive arbiter is the unrun calibration test **POS-P1/POS-P2**. A formula makes the readiness claim inspectable; it does not make it true.

The invariant is preserved throughout: **Form ↔ Time · Position ↔ Space · Action ↔ Energy.** The readiness kernel gates on Form and Position (the base every future `U` multiplies against); Action is the pillar spent by the commitment, not a gate.

### 4.1 Component-level readiness

Each pillar is measured by a set of indicators. For Form, indicators `f_tj` (`j = 1…n_F`) each carry an action·domain·stakes-conditioned threshold `θ_Fj(a,d,s)`. The **component readiness** is the worst normalized clearance across that pillar's indicators:

```
R_F(a,t) = min_j  LCB(f_tj | a) / θ_Fj(a,d,s)
R_P(a,t) = min_k  LCB(p_tk | a) / θ_Pk(a,d,s)          k = 1…n_P
```

`min`, not a weighted mean: within a pillar, an unmet critical indicator is not compensated by surplus elsewhere (the non-compensation intent). The **vector readiness** conjoins the two pillars — again by the worst case:

```
R_vec(a,t) = min( R_F(a,t) , R_P(a,t) )

R_vec ≥ 1   ⇔   every Form- and Position-indicator clears its threshold
                on its LCB, at the declared confidence standard.
```

`R_vec` is the multi-indicator generalization of the scalar `R(a,t)` of `APPENDIX_POS §2.6`: with one indicator per pillar it collapses exactly to `min(LCB(F)/θ_F, LCB(P)/θ_P)`. **Robust when `R_vec ≥ 1`.**

| Symbol | Meaning | Reads |
|---|---|---|
| `R_F` | Form component readiness | `min_j LCB(f_tj)/θ_Fj` |
| `R_P` | Position component readiness | `min_k LCB(p_tk)/θ_Pk` |
| `R_vec` | vector (system) readiness | `min(R_F, R_P)` |
| `R_vec ≥ 1` | robust-ready verdict | all indicators clear on LCB |

### 4.2 Per-component margins, system reserve, and the active bottleneck

`R_vec` says *whether* the base clears; the **margins** say *by how much*, indicator by indicator:

```
m_Fj(a,t) = LCB(f_tj | a) / θ_Fj(a,d,s) − 1
m_Pk(a,t) = LCB(p_tk | a) / θ_Pk(a,d,s) − 1
```

`m > 0`: clears with reserve · `m = 0`: exactly on the boundary · `m < 0`: unmet. The **system reserve** is the minimum margin over *all* components of *both* pillars:

```
m_R(a,t) = min( min_j m_Fj , min_k m_Pk ) = R_vec(a,t) − 1
```

The **active bottleneck** is the exact blocking indicator — the single component that pins `R_vec`:

```
b(a,t) = argmin_{c ∈ (F-indicators ∪ P-indicators)}  m_c(a,t)
```

`b` names *which* indicator (e.g. `f_t3` = "capital runway", `p_t2` = "regulatory standing"), not merely which pillar. It authorizes nothing — the gate is `1[R_vec ≥ 1]` — but it points preparatory effort (`a^prep`, ungated when low-`κ`) at the component with the highest immediate readiness value. Ties (multiple components at the same minimum) are reported as a bottleneck *set*, not silently broken.

### 4.3 Readiness deficit — distance to the readiness set

The **readiness set** is `𝓡 = { z : LCB(z_c) ≥ θ_c ∀ c }` — the region where every component clears. The **readiness deficit** `D_R` measures the distance from the current base to `𝓡`, aggregating shortfalls into a single "how far from ready" scalar for triage and monitoring:

```
D_R(a,t) = ‖ ( [ 1 − LCB(z_c)/θ_c ]_+ )_c ‖_{w}          [x]_+ = max(x, 0)
```

a weighted norm over the per-component **shortfalls** `[1 − LCB/θ]_+` (a component already clearing contributes exactly 0).

> **Caveat (load-bearing, do not weaken).** `D_R = 0 ⟺ R_vec ≥ 1` holds **only** under (i) a **genuine, strictly positive weighted norm** (`w_c > 0` for every component; `‖x‖_w = 0 ⇒ x = 0`) **and** (ii) **strictly positive thresholds** (`θ_c > 0`). If any weight is zero, a real shortfall on that component is invisible to `D_R` and `D_R = 0` no longer implies readiness. If any threshold is zero, `LCB/θ` is undefined (division by zero) and the ratio form is inadmissible. Under those two conditions the equivalence is exact; outside them `D_R` is a **monitoring heuristic only** and the *binary* verdict `1[R_vec ≥ 1]` — never `D_R` — governs authorization.

`D_R` is an audit / prioritization signal (a smooth companion to the binary gate), not a second gate. Its norm, weights `w_c`, and the threshold-positivity precondition are **declared before evaluation**; POS may not choose a friendlier norm after seeing whether the action would pass.

---

## 5. Uncertainty & robust readiness

Readiness is a claim under uncertainty, so the kernel fixes **how** the LCB is taken and **against what** the thresholds are compared — before the gate is evaluated. All numbers in this section are **illustrative — ZERO decision authority** and **research-use-only (RUO)**; the operative `α(s)`, uncertainty model, and mode are calibration outputs of POS-P1, not defaults.

### 5.1 The LCB confidence standard, stakes-scaled

For any readiness quantity `X ∈ {f_tj, p_tk}` conditioned on action `a`:

```
LCB_{1−α}(X | a) = Q_α( X | a, D_t )                    (lower α-quantile of the posterior / sampling dist.)
                 ≈ mean[X(a)] − z_{1−α} · SE[X(a)]       (approximately-Gaussian estimator)
```

The confidence requirement **tightens with stakes**:

```
α = α(s) ,     dα/ds ≤ 0
```

higher stakes `s` → smaller `α` → a more conservative (lower) bound → a stronger evidence demand. *Illustrative only — ZERO decision authority, RUO:* an ordinary-stakes gate might read `α ≈ 0.05` (one-sided 95%) and a critical-infrastructure gate `α ≈ 0.005` (one-sided 99.5%). Estimator, uncertainty model, and `α(s)` are **declared before the gate is evaluated**; the engine may not swap in a friendlier uncertainty model after seeing whether the action passes.

### 5.2 Three exposed uncertainty modes

The kernel exposes three ways to convert per-indicator uncertainty into a *system* readiness verdict. The engine selects one; the choice is recorded in the decision certificate (§5.3).

| Mode | Verdict rule | Coverage guarantee | When to use |
|---|---|---|---|
| **SCALAR_LCB** | `min_c LCB_{1−α}(z_c)/θ_c ≥ 1` — each indicator on its own `(1−α)` bound | **per-component** `(1−α)` only; see caveat | cheap default; few indicators; low correlation concern |
| **JOINT_CHANCE** | `Pr( ⋀_c LCB(z_c) ≥ θ_c ) ≥ 1 − α(s)` — one joint chance constraint | **joint** `(1−α)` across all `m` components | many indicators; a genuine "all clear together" claim |
| **ROBUST_SET / DRO** | `inf_{Q ∈ 𝒰} min_c Q-LCB(z_c)/θ_c ≥ 1` — worst case over an ambiguity set `𝒰` (or a DRO program) | distribution-robust over `𝒰` | model/ambiguity risk; adversarial or non-stationary environments |

> **SCALAR_LCB Bonferroni caveat (load-bearing).** `SCALAR_LCB` gives only **per-component** `(1−α)` coverage. Under the union bound, the **joint** coverage of `m` components is
>
> ```
> Pr( ⋀_c { LCB(z_c) ≥ θ_c } )  ≥  1 − ∑_c α_c      (union / Bonferroni bound)
> ```
>
> so `m` independent-looking 95% checks give a *joint* guarantee no better than `1 − 0.05m` — which for `m = 20` is a vacuous `0`. To obtain a genuine **joint `(1−α)`** meaning from `SCALAR_LCB`, apply **Bonferroni** — spend `α/m` per component (`z_{1−α/m}`) — **or escalate** to `JOINT_CHANCE` / `ROBUST_SET`/DRO, which model the joint object directly. Which correction was used (raw per-component, Bonferroni `α/m`, or an escalated mode) is **recorded** — an uncorrected `SCALAR_LCB` may never be reported as a joint readiness guarantee.

### 5.3 The selected mode is stored in the decision certificate

The uncertainty mode is not an implementation detail; it is part of the auditable verdict. Every gate evaluation emits a certificate carrying at least: the selected mode (`SCALAR_LCB` / `JOINT_CHANCE` / `ROBUST_SET`), the multiplicity correction (`none` / `Bonferroni α/m` / `escalated`), `α(s)` and the stakes `s`, the uncertainty model and estimator, the ambiguity set `𝒰` if applicable, and the resulting `R_vec`, `m_R`, `b`, and verdict. This makes the coverage claim **inspectable and reproducible**, and forecloses post-hoc mode-shopping. The stored mode has **no decision authority of its own** — it documents *how* the L2/B2 readiness verdict was computed, pending POS-P1 calibration of the modes themselves.

---

## 6. Irreversibility & exposure

Irreversibility `κ` sets *how high the readiness bar rises* (`APPENDIX_POS §2.6.3`: `∂θ/∂κ ≥ 0`); exposure `e` measures *how much is at risk in this move*. They are **distinct quantities** and the kernel keeps them separate. Both definitions below are **L2/B2 candidate operationalizations, ZERO decision authority, RUO** — the arbiter is POS-P1/POS-P2.

### 6.1 Recoverability-derived irreversibility

The principled definition of irreversibility is **failure of recovery**: how unlikely the system is to return to an acceptable state after the action, within a cost budget.

```
κ_H(a) = 1 − ρ_H(a)

ρ_H(a) = Pr(  ∃ τ ≤ H :  x_{t+τ} ∈ 𝓐_rec  |  do(a),  ∑ recovery-cost ≤ C_budget  )
```

where `ρ_H` is the **H-horizon probability of returning to an acceptable recovery region `𝓐_rec`** within cost budget `C_budget`, under a transition model. Fully recoverable → `ρ_H = 1 → κ_H = 0` (a reversible probe); practically unrecoverable → `ρ_H → 0 → κ_H → 1` (a hard commitment). `κ_H` is the preferred definition **whenever a transition model exists**, because it derives irreversibility from dynamics rather than assigning it by hand.

### 6.2 The proxy composite — an explicit approximation

When **no transition model exists**, the kernel falls back to a proxy that composes per-dimension irreversibility judgments over the dimensions *cost, time, state, legal, social, option*:

```
κ_proxy(a) = 1 − ∏_j ( 1 − κ_j )^{w_j}   j ∈ {cost,time,state,legal,social,option},  κ_j∈[0,1], w_j>0, ∑_j w_j=1
κ(a)       = max[ κ_proxy(a) ,  max_{j∈J_crit} κ_j(a) ]     # hard envelope: a critical irreversibility cannot be averaged away
```

Each `κ_j ∈ [0,1]` grades irreversibility on one dimension; a true zero on any weighted dimension pulls the product toward reversibility, and any dimension near 1 pulls `κ` toward 1 (no single dimension can be fully compensated by the others). *Illustrative dimension reading — ZERO decision authority, RUO:* `κ_legal ≈ 1` for an action that triggers an irrevocable statutory obligation; `κ_option ≈ 0` for a paper trade.

> **Flagged as an approximation (do not upgrade).** The composite `κ = 1 − ∏(1−κ_j)^{w_j}` is a **hand-built proxy used only when no transition model is available.** It is not derived from dynamics, its dimensions are not proven orthogonal, and its weights `w_j` are uncalibrated. Where a transition model exists, prefer `κ_H = 1 − ρ_H` (§6.1). The proxy's dimensions, weights, and grading rubric are **declared before use**, and both `κ` forms remain L2/B2 candidates pending POS-P1.
>
> **Critical-irreversibility envelope (exact non-compensation).** The product composite is only *partially* non-compensatory below the endpoint: a positively-weighted `κ_j = 1` forces `κ_proxy = 1`, but a value merely *near* 1 carrying a small weight can be diluted. Domain-critical irreversibility dimensions therefore enter through the **hard envelope** `κ(a) = max[κ_proxy, max_{j∈J_crit} κ_j]`, so a low weight can never mask a severe legal, physical, temporal, or option-loss irreversibility (`κ_j∈[0,1]`, `w_j>0`, `∑ w_j=1`).

### 6.3 Normalized exposure — distinct from κ

Exposure answers a different question than irreversibility: not *"can this be undone?"* but *"how much is on the line?"*

```
e(a,t) = C_at_risk(a,t) / ( C_available(t) + ε )        e ∈ [0,1] under normalization,  ε > 0
```

`C_at_risk` is the resource / capital / standing placed at risk by `a`; `C_available` is the total the system can currently muster; `ε > 0` avoids division by zero when the available base is momentarily nil. `e` is the `e(a)` fed to the threshold family `θ_i(a,d,s)` of `APPENDIX_POS §2.6.3` (`∂θ/∂e ≥ 0`).

**`e` and `κ` are orthogonal by construction.** An action can be highly reversible yet high-exposure (a large but fully refundable deposit: `κ → 0`, `e → 1`), or nearly zero-exposure yet irreversible (a tiny but permanent public statement: `e → 0`, `κ → 1`). The kernel never collapses them into one number; both enter the threshold independently.

### 6.4 The three mandatory correctness fixes (baked into the kernel)

These three properties are **structural requirements** of any faithful implementation of this kernel. They correct known bugs and must not be reintroduced.

**Fix 1 — geometric sub-aggregator zero-clamp.** A pillar's geometric sub-aggregator over indicators `z_j` is

```
G_i(z) = ∏_j z_j^{w_ij}
```

which maps a **true zero to exactly 0** — a genuinely absent component cannot be bought back by surplus elsewhere. A log form may be used for numerical stability:

```
log G_i(z) = ∑_j w_ij · log( z_j + ε )
```

> Here `ε` is **only** a numerical −∞-avoidance device on **strictly-positive noisy measurements** (a small `z_j` that is not structurally zero). Whenever any **structural / true-zero** component is present, `G_i` is **HARD-CLAMPED to 0** — the ε log form is not used. **`ε` must NEVER convert a true zero into a passing score.** True-zero detection precedes the log transform; if it fires, `G_i := 0` regardless of `ε`.

**Fix 2 — critical-veto wiring (makes critical non-compensation, POS-F2, a theorem).** Readiness authorization is **not** `1[R_rob ≥ 1]` alone; it conjoins the critical veto:

```
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i        ( equivalently  min_i PillarReady_i )

H_i = 1[ ∀ critical j :  LCB(z_ij) ≥ θ_ij^crit ]
```

`H_i` is the per-pillar critical-indicator gate: it is `1` only when **every** indicator flagged *critical* clears its critical threshold `θ_ij^crit` on its LCB. Because `G_ready` multiplies by `∏_i H_i`, a single unmet critical indicator forces `G_ready = 0` no matter how large the surplus elsewhere — **only with this wiring is "critical non-compensation" (POS-F2) actually a theorem** rather than a hope. `R_rob` is the robust readiness of the selected uncertainty mode (§5.2). `G_ready` still sits *downstream* of the values-firewall, which dominates unconditionally (`APPENDIX_POS §7`).

**Fix 3 — stopping time (no false optimality claim).** The kernel's commitment stopping time is a **one-step-lookahead commitment heuristic**, not an optimal stopping rule:

```
τ_POS := min( τ_ready , τ_emg )

τ_ready = inf{ t : G_ready(t) = 1 }
τ_emg   = inf{ t : G_emg(t)   = 1 }
```

> `τ_POS` is defined as a **min of two hitting times**, computed once — it is never accumulated (`τ_POS += …` is a bug and is forbidden). It is a **one-step-lookahead commitment heuristic**: it commits at the first time the base is ready *or* an emergency forces the move, and does **not** claim optimality against waiting. To claim optimality one must instead solve the optimal-stopping problem via the **Snell envelope** — define `V_wait(t) = max( commit-value(t) , E[ V_wait(t+1) | D_t ] )` and stop when `commit-value(t) ≥ E[V_wait(t+1)|D_t]`. The kernel exposes `τ_POS` as the heuristic and `V_wait` as the (heavier) optimal alternative; it never labels the one-step rule "optimal."

**Epistemic status of §§4–6.** The readiness kernel, the LCB/mode machinery, and the irreversibility/exposure definitions are all **L2/B2 candidate operationalizations** — not validated laws, not theorems of `U = ∛(F·P·A)`. Every illustrative number here carries **ZERO decision authority** and is **research-use-only**. The functional forms, thresholds, weights, confidence rules, horizons, and ambiguity sets require preregistration and calibration; the decisive arbiter remains the **unrun POS-P1/POS-P2** test. A formula makes a claim inspectable; it does not make it true.

## 7. The generalized gate

The engine's authorization primitive is a single computable predicate over a candidate action `a` in state `x`. It is the domain-invariant generalization of §2.6.3's `G_POS`: the admissibility firewall dominates, and above it exactly one of three doors must open — a reversible **probe**, a prepared **readiness** commitment, or a logged **emergency** forced move. No door bypasses the firewall.

> **Epistemic status.** Everything in this section is an **L2 / B2 candidate operationalization** — a mechanism made *inspectable*, not a validated law and not a theorem of `U = ∛(F·P·A)`. The decisive arbiter is the unrun calibration test **POS-P1 / POS-P2**. A formula makes a claim checkable; it does not make it true.

### 7.1 The gate

```
G_POS(a, x, t) = C_d(a, x) · 1[ G_probe ∨ G_ready ∨ G_emg ]

C_d(a, x)      = C_feasible(a,x) · C_domain(a,x) · C_quality(a,x) · C_firewall(a,x)

G_probe        = 1[ κ(a) ≤ κ_probe  ∧  e(a) ≤ e_cap ]
G_ready        = 1[ R_rob(a,t) ≥ 1 ] · H_F(a,t)·H_P(a,t)      (readiness veto over Form & Position ONLY; Action → C_d^A, not a third veto — see box below)
G_emg          = 1[ a = a^emg  ∧  M_emg(a,t) > 0  ∧  LogComplete(a) = 1 ]
M_emg(a,t)     = LCB[ L(inaction) ] − UCB[ L(a) ]
```

`C_d ∈ {0,1}` is the **admissibility conjunction** — a product of hard gates, so *any* failing factor sends `C_d = 0` and forces `G_POS = 0` no matter how favorable the doors:

| Factor | Meaning | Zero when |
|---|---|---|
| `C_feasible` | the action is physically/operationally executable in state `x` | out of range, resource-infeasible, adapter cannot emit it |
| `C_domain` | mandatory domain constraints hold (regulatory, physical limits, protocol) | a hard domain rule is violated |
| `C_quality` | inputs meet the declared data/model quality floor | inputs stale, model invalid, coverage unmet |
| `C_firewall` | the **values/legal/safety firewall** passes — **dominant** | ethics, law, or a domain safety constraint forbids `a` |

**Firewall dominance is structural, not weighted.** Because `C_d` is a *product* and `C_firewall` is one factor, a firewall failure clamps the whole gate to zero — it can never be compensated by high readiness, low `κ`, or a strong emergency margin. This is the engine encoding of §2.6.3's rule: *no `R` or `κ`, however favorable, authorizes a firewall-barred action.*

### 7.2 The probe door

```
G_probe = 1[ κ(a) ≤ κ_probe  ∧  e(a) ≤ e_cap ]
```

A reversible, capped-exposure action passes without a readiness proof — this is the exploration that *builds* Form and Position. Both conditions are required: low irreversibility `κ` **and** bounded exposure `e`. A "reversible" action with unbounded exposure is a commitment in disguise and does not qualify (no label-gaming; the door keys on `κ` and `e`, not on what the action is called).

- `κ_probe`, `e_cap` illustrative defaults `κ_probe = 0.15`, `e_cap = 0.05` of the recoverable-loss budget — **illustrative — ZERO decision authority; research-use-only (RUO)**; superseded by POS-P1 calibration.

### 7.3 The readiness door — with the critical veto wired in (FIX 2)

```
G_ready = 1[ R_rob(a,t) ≥ 1 ] · ∏_i H_i(a,t)   ≡   min_i PillarReady_i(a,t)

H_i(a,t) = 1[ ∀ critical j ∈ pillar i :  LCB(z_ij) ≥ θ_ij^crit ]
```

`R_rob ≥ 1` is the robust readiness ratio of §2.6 (both/all pillar readiness ratios clear their thresholds on lower confidence bounds). **The veto term `∏_i H_i` is not optional and not decorative.** Each `H_i` is a hard indicator that *every* component marked **critical** in pillar `i` clears its own critical floor `θ_ij^crit` on its lower confidence bound. Because `G_ready` is the product `1[R_rob ≥ 1] · ∏_i H_i` (equivalently `min_i PillarReady_i`), a single failing critical component sends `G_ready = 0` regardless of how high every other score is.

> **Why the wiring matters (POS-F2, critical non-compensation).** Only with the veto factor present is "a critical deficiency cannot be bought off by surplus elsewhere" an actual **theorem** of the gate rather than an aspiration. Drop `∏_i H_i` and the aggregate ratio `R_rob` would let a soaring non-critical score float a failed critical one over the line — the exact bug this fix forbids. The critical veto is therefore part of the gate's definition, not a post-hoc filter.

**Action does not enter POS as a third readiness veto (index convention, load-bearing).** Throughout this profile, `∏_i H_i` denotes `∏_{i∈{F,P}} H_i = H_F·H_P` — the readiness veto ranges over **Form and Position only**, and `R_rob = min(R_F, R_P)`:

    G_ready(a,t) = 1[ R_rob(a,t) ≥ 1 ] · H_F(a,t) · H_P(a,t)

Any hard requirement *without which the candidate action cannot be executed at all* — actuator / liquidity / energy / staffing capacity, technical capability, authorization, an executable plan — is an **Action-side feasibility** condition and belongs to the domain feasibility predicate `C_d^A(a,x) ∈ {0,1}`, NOT to the readiness gate. The Action pillar `A_t` remains in SSS, candidate ranking, expected-outcome modelling, execution monitoring, and post-action evaluation — diagnostic, not a readiness prerequisite distinct from the candidate's own executability. The full gate:

    G_POS = C_d^A · C_d^safety · V_d · 1[ G_probe ∨ G_ready ∨ G_emg ]

This keeps the invariant **Action ↔ Energy** intact without making Action a readiness pillar. An adapter that previously marked an Action indicator "critical" must route that hard-stop through `C_d^A` / the firewall, never through `∏ H_i`.

#### 7.3.1 Pillar sub-aggregation and the zero-clamp (FIX 1)

Each pillar readiness `z_i` is a **geometric** sub-aggregate of its component readiness scores `z_ij ∈ [0,1]`:

```
G_i(z) = ∏_j z_ij^{ w_ij } ,   w_ij ≥ 0 ,   ∑_j w_ij = 1
```

The geometric form maps a **true zero to exactly zero**: if any structural/true-zero component is present, `G_i = 0` — no weight configuration can rescue it. This is the intended non-compensatory behavior and it is preserved literally.

A log form may be used **only** for numerical `−∞` avoidance on strictly-positive noisy measurements:

```
log G_i = ∑_j w_ij · log( z_ij + ε ) ,   ε > 0
```

- `ε` exists **solely** to keep floating-point `log` finite on measurements that are already strictly positive but noisy. It carries no semantic meaning.
- `ε` must **NEVER** convert a true zero into a passing score. Therefore `G_i` is **HARD-CLAMPED to 0** whenever any structural / true-zero component is present:

```
G_i = 0                                   if ∃ j : z_ij is a structural/true zero
    = exp( ∑_j w_ij · log(z_ij + ε) )      otherwise (all z_ij strictly positive, ε for stability only)
```

The clamp is evaluated **before** the log form is ever reached. `ε` on the order of `1e−9` is **illustrative — ZERO decision authority; RUO**.

#### 7.3.2 Coverage bookkeeping (union bound / Bonferroni)

`SCALAR_LCB` delivers only **per-component** `(1 − α_j)` coverage. Joint coverage over `m` components is **not** `1 − α`; by the union bound it is:

```
Pr( ∀ j :  z_ij ≥ LCB_{1−α_j}(z_ij) )  ≥  1 − ∑_j α_j
```

To make `G_ready` carry a **joint** `1 − α` guarantee, one of the following MUST be applied and **recorded in the certificate**:

| Method | Rule | When |
|---|---|---|
| Bonferroni | set each `α_j = α / m` | cheap, `m` moderate, components possibly dependent |
| JOINT_CHANCE | solve a joint chance constraint directly | dependence structure known/estimable |
| DRO | distributionally-robust bound over an ambiguity set | dependence unknown, worst-case required |

The engine records *which* method produced the coverage it claims. A gate that reports "joint 95%" while summing per-component 95% bounds is making a false coverage claim — the union-bound arithmetic above is the anti-bug.

### 7.4 The emergency door

```
G_emg = 1[ a = a^emg  ∧  M_emg(a,t) > 0  ∧  LogComplete(a) = 1 ]
M_emg = LCB[ L(inaction) ] − UCB[ L(a) ]
```

The forced-move door fires only when **all three** hold: the action is declared `a^emg`, the **robust** loss margin is positive (loss of inaction, on its *lower* bound, exceeds loss of acting on its *upper* bound — never point estimate vs point estimate), and the mandatory forced-move log is complete. `LogComplete = 0` (no audit record) blocks the emergency door even when the margin is large — an unlogged forced move is not authorized. The firewall factor `C_firewall` in `C_d` still dominates: an emergency does **not** license a values-forbidden action.

### 7.5 Three-valued output and reason codes

The binary `G_POS` is the *authorization* bit. The engine's *reported verdict* is **three-valued**, because "not authorized" must distinguish a considered refusal from an inability to decide:

| Verdict | Condition | Meaning |
|---|---|---|
| **AUTHORIZE** | `G_POS = 1`, certificate complete | commit / proceed |
| **WITHHOLD** | `C_d = 1` but no door open (`R_rob < 1`, no valid emergency) | decidable and **not yet** ready — a positive "wait" |
| **ABSTAIN** | certificate **incompletable** | the engine cannot form a valid judgment |

**ABSTAIN triggers** (any one): required data missing; model invalid or out of validated scope; distribution drift detected; unknown/unvalidated adapter; input out-of-distribution (OOD); coverage/certificate cannot be completed at the declared standard. ABSTAIN is **not** WITHHOLD: WITHHOLD says "I judged, and the base is not ready"; ABSTAIN says "I cannot validly judge." Every verdict carries a machine-readable **reason code** naming the binding factor (e.g. `FIREWALL_BLOCK`, `CRIT_VETO:pillar_i.comp_j`, `READINESS_SHORT:b(a,t)`, `PROBE_EXPOSURE_CAP`, `EMG_NO_LOG`, `ABSTAIN_OOD`, `ABSTAIN_DRIFT`, `ABSTAIN_COVERAGE`).

### 7.6 Anti-paralysis — ABSTAIN and liveness ship together

A three-valued gate that can ABSTAIN is exploitable as a stall: a system could withhold or abstain forever and never be wrong. To forbid this, the ABSTAIN capability is **paired with a mandatory liveness obligation** — the two are specified and deployed together, never one without the other:

```
G[ ( Ready ∧ Values ∧ Beneficial ) → F ( Commit ∨ RejectReason ) ]
```

Read as a temporal-logic requirement (`G` = always, `F` = eventually): *whenever an action is readiness-clear, values-clear, and net-beneficial, the engine must eventually either commit to it or emit an explicit machine-readable reject reason.* Indefinite silence in that state is a **conformance failure** of the engine. ABSTAIN buys the right to not-decide only under genuine incompleteness (§7.5 triggers); it does not buy the right to stall on an action that is ready, permitted, and beneficial. This liveness clause is the anti-paralysis counterweight that makes the safety of ABSTAIN honest.

---

## 8. Control, objective & stopping

The gate (§7) decides *whether* a specific action may commit. This section places the gate inside a **control objective** — what the engine optimizes over trajectories — and a **stopping rule** — *when* it commits. Both are **L2 / B2 candidate operationalizations, RUO**; POS-P1/POS-P2 remain the decisive arbiter.

### 8.1 The canonical control objective

One objective, stated once, in the currencies of the invariant (**Form ↔ Time · Position ↔ Space · Action ↔ Energy** — the integrals accumulate over Time, the safety set lives in the state/Position space, and the commitment/energy costs are Action-side):

```
maximize  J(π) = E[ Y_ext(T)
                    + λ_U ∫ U dt
                    − λ_B ∫ B dt
                    − λ_C ∫ C_commit dt
                    − λ_D ∫ C_delay dt ]
                 − λ_R · CVaR_β[ L_T ]

subject to
   (S1)  Firewall = PASS                             at all times
   (S2)  G_POS(a,x,t) = 1                            for every non-emergency commitment
   (S3)  C_total ≤ C_max                             total budget
   (S4)  Pr( x ∈ X_safe  ∀ t ∈ [0,T] ) ≥ 1 − ε_s     safety chance constraint
```

| Term | Reading | Sign |
|---|---|---|
| `Y_ext(T)` | terminal external outcome (domain payoff) | reward |
| `λ_U ∫U dt` | accumulated stability `ℳ = ∫U dt` — the area under the `U`-trajectory | reward |
| `λ_B ∫B dt` | accumulated harm/side-effects | penalty |
| `λ_C ∫C_commit dt` | cost of committing (resource spend, foreclosed options) | penalty |
| `λ_D ∫C_delay dt` | cost of waiting (opportunity/decay of delay) | penalty |
| `λ_R · CVaR_β[L_T]` | tail risk of terminal loss at level `β` (not just mean) | penalty |

The `C_commit` vs `C_delay` pair is the formal tension POS exists to arbitrate: committing too early spends the base; committing too late bleeds opportunity. `CVaR_β` (not variance, not mean) makes the objective **tail-aware**, consistent with the LCB/robust discipline of the gate. The multipliers `λ_•` and levels `β, ε_s` are **illustrative until calibrated — ZERO decision authority; RUO**.

**Constraints are hard, not traded.** `(S1)`–`(S4)` are not folded into `J` as penalties; they bound the feasible set. `(S2)` requires the §7 gate to authorize every non-emergency commitment — emergencies route through `G_emg` and its mandatory log, not through this constraint. `(S4)` is a genuine **chance constraint**: safety must hold jointly across the horizon with probability at least `1 − ε_s`, and the joint-coverage bookkeeping of §7.3.2 (union bound / Bonferroni / JOINT_CHANCE / DRO) applies to how that probability is certified.

### 8.2 The lexicographic alternative

Scalarizing everything through the `λ_•` weights presumes the weights are commensurable and calibrated. When they are not — or when a stakeholder rejects trading safety against outcome at *any* exchange rate — the engine offers a **lexicographic** ordering instead: optimize each level fully before the next is even considered.

```
1. values / legal        (firewall — never traded)
   ≻
2. critical safety        (X_safe, critical vetoes H_i)
   ≻
3. catastrophe probability (minimize Pr of tail catastrophe)
   ≻
4. readiness              (maximize robust readiness margin m_R)
   ≻
5. outcome                (maximize Y_ext / ℳ)
   ≻
6. cost                   (minimize C_commit + C_delay)
```

`A ≻ B` means *no gain at level B can ever compensate a loss at level A.* This mirrors the gate's own structure: firewall dominance (§7.1) and critical non-compensation (§7.3) are exactly levels 1–2 of this order made global over the trajectory. The scalar objective (§8.1) and the lexicographic objective (§8.2) are **two declared modes**, not a blend; which one is in force is recorded in the run certificate.

### 8.3 Commitment timing — a one-step-lookahead heuristic (FIX 3)

The engine still needs a *when-to-commit* rule. The default is a **one-step-lookahead commitment heuristic** — explicitly a heuristic, **not** claimed optimal:

```
commit at the first t where  Q_commit(a,x,t)  ≥  V_wait(a,x,t)

Q_commit(a,x,t) = value of committing to a now
V_wait(a,x,t)   ≈ E[ value of the best decision available after one more step of information/preparation ]
                  − C_delay(t)
```

If `V_wait` is instead defined as the true continuation value via the **Snell envelope** of the optimal stopping problem, then — and only then — may the stopping rule be called *optimal*; with a one-step lookahead it may not. The engine records which definition is in force.

The realized POS stopping time is the earliest moment **either** the readiness door or the emergency door opens:

```
τ_ready = inf{ t :  G_ready(a,t) = 1 }        (readiness door, §7.3)
τ_emg   = inf{ t :  G_emg(a,t)   = 1 }        (emergency door, §7.4)

τ_POS  :=  min( τ_ready , τ_emg )
```

> **Do not write `τ_POS += …`.** `τ_POS` is a stopping time — a first-hitting time defined by `min(τ_ready, τ_emg)`, not an accumulator to be incremented. Emergencies do not *extend* a deadline; they open an independent, earlier door. The probe door (§7.2) does not appear here: a probe is capped-exposure exploration that flows continuously, not a commitment whose timing `τ_POS` governs.

Before `τ_POS`, the engine reports **WITHHOLD** (decidable, not yet ready) or **ABSTAIN** (cannot validly judge), subject to the §7.6 anti-paralysis liveness clause `G[(Ready ∧ Values ∧ Beneficial) → F(Commit ∨ RejectReason)]` — so waiting is bounded and accountable, never an indefinite stall.

> **Closing epistemic note.** §7–§8 specify a gate, an objective, and a stopping rule that are **inspectable and falsifiable** — not validated. No number here has decision authority; each is RUO. The claim that readiness-gated commitment under this objective beats ungated alternatives at equal cost is the **pre-registered hypothesis POS-P1 / POS-P2**, and that unrun test — not any formula above — is the decisive arbiter.

## 9. Calibration & validation

The kernel makes claims *inspectable*; only calibration and the pre-registered falsifiers can make them *earned*. Everything in this section is an **L2/B2 candidate operationalization**, not a validated law and not a theorem of `U = ∛(F·P·A)`. Every numeric threshold below is **illustrative — ZERO decision authority — research-use-only (RUO)**. The decisive arbiter is the still-**unrun** calibration test **POS-P1 / POS-P2**; until it reports, the kernel is scaffolding.

### 9.1 The two error currencies

A commitment gate `G_POS ∈ {0,1}` can be wrong in two directions, and the invariant `Form ↔ Time · Position ↔ Space · Action ↔ Energy` demands both be priced, because a gate that only avoids one error simply relocates the harm.

```
FA = 1[ G_POS = 1  ∧  Y_unsafe ]      false authorization  — a SAFETY error
FD = 1[ G_POS = 0  ∧  Y_beneficial ]  false deferral       — an OPPORTUNITY error
```

| Error | Reads as | Currency spent | Invariant face |
|---|---|---|---|
| `FA` (false authorization) | committed to an action that was not ready → base burns | Energy released into a Position that could not carry it | Action ↔ Energy |
| `FD` (false deferral) | withheld a commitment the base could in fact carry | Time lost, options decayed while waiting | Form ↔ Time |

A pure-safety gate drives `FA → 0` by deferring almost everything and pays for it entirely in `FD`; a pure-throughput gate does the reverse. The kernel refuses to hide either cost — both enter the objective and both are audited (§11).

### 9.2 Threshold optimization under a hard safety constraint

The operating thresholds `θ` (the `θ_F, θ_P, θ_ij^crit` family of the readiness definition) are chosen to minimize expected cost **subject to a stakes-monotone cap on the safety error** — not to minimize a free-floating loss:

```
θ* = argmin_θ  E[ c_FA·FA(θ) + c_FD·FD(θ) + c_D·C_delay(θ) ]

     s.t.   Pr( FA | s ) ≤ ε_FA(s)      for every stakes level s
            dε_FA/ds ≤ 0                 (higher stakes ⇒ tighter safety cap)

     if the constraint set is empty at any admissible θ  →  ABSTAIN
```

- `c_FA, c_FD, c_D ≥ 0` are domain-declared costs of the two errors and of delay; `C_delay` is the accrued cost of waiting (option decay, missed window).
- The safety cap `ε_FA(s)` is a **primary constraint, not a term to be traded away** — cost minimization happens only *inside* the feasible region where `Pr(FA|s) ≤ ε_FA(s)`. This is the machine-level expression of "the values-firewall dominates every readiness result."
- `dε_FA/ds ≤ 0` enforces that a more consequential decision buys a stricter safety budget — the same monotonicity the risk-adjusted thresholds carry.
- **Infeasibility is a first-class output.** If no admissible `θ` satisfies the cap (e.g. estimator uncertainty is too wide to certify `Pr(FA|s) ≤ ε_FA(s)`), the kernel does not silently pick the least-bad `θ`; it returns **ABSTAIN**. Abstention conservatism (POS-F8, §10) guarantees this never itself authorizes a commit.

*Illustrative only — ZERO decision authority, RUO:* `ε_FA(s) = 0.05` at ordinary stakes falling to `0.005` at critical-infrastructure stakes; `c_FA/c_FD = 20`. These placeholders are superseded the instant POS-P1 delivers a calibrated cost/constraint pair.

### 9.3 Calibration diagnostics

A gate that consumes lower confidence bounds is only as honest as the probabilities feeding them. The kernel is required to *report* calibration, not assume it:

```
Calibration (reliability):   Pr( Y_ready | p̂ = p ) ≈ p     for all p ∈ [0,1]
Brier score:                 BS  = (1/N) · ∑_n ( p̂_n − y_n )²
Expected calibration error:  ECE = ∑_b (N_b/N) · | acc(b) − conf(b) |
```

| Diagnostic | Question it answers | Failure signature |
|---|---|---|
| Reliability curve `Pr(Y_ready\|p̂)` | are stated readiness probabilities truthful? | curve bows below diagonal ⇒ over-confident ⇒ silent `FA` risk |
| Brier `BS` | overall probabilistic accuracy | high ⇒ estimates carry little information |
| `ECE` | average miscalibration across bins | large ⇒ LCBs are untrustworthy; widen bounds or recalibrate |

**Split discipline (mandatory).** Calibration, threshold selection, and evaluation run on **separated data partitions**: a *calibration* split fits `p̂`; a *selection* split tunes `θ*`; a held-out *evaluation* split reports FA/FD/Brier/ECE and the POS-P1 endpoint. No partition may serve two roles — reusing the selection split for evaluation manufactures optimism exactly where the safety cap must be trusted.

### 9.4 Drift monitoring

Deployment distributions move; a gate calibrated on `P_train` may silently decalibrate on the live stream `P_t`. The kernel tracks a drift statistic and responds monotonically:

```
D_t = D( P_t , P_train )     (e.g. PSI, KL, or an MMD/energy distance on the estimator inputs)
```

| `D_t` band (illustrative — ZERO authority, RUO) | Kernel response |
|---|---|
| `D_t ≤ d_lo` | nominal — operate |
| `d_lo < D_t ≤ d_hi` | **lower confidence** (raise `α` toward more conservative LCBs) and **widen bounds** |
| `D_t > d_hi` | **recalibrate** on fresh labeled data before trusting the gate |
| recalibration infeasible / `D_t ≫ d_hi` | **ABSTAIN** (treat as out-of-domain, §9.6) |

Drift never *loosens* the gate. Every escalation direction is toward caution, consistent with abstention conservatism.

### 9.5 The pre-registered falsifiers

These are the decisive arbiters. Nothing in the kernel is validated until they report; both require **full preregistration** (endpoint, N, power, minimum effect, analysis plan, public registration record) *before* any run.

**POS-P1 — does the gate pay?** Does readiness-gated commitment beat the baselines at equal total budget on **external** outcomes?

- **Baselines (mandatory):** an **ungated** policy; **AD-RTD alone** (Action-first discovery, no commitment gate — the incumbent baseline of record); weakest-pillar `π*`-greedy; expert/domain policy; explore-then-commit; random-order; and the two isolating ablations **thresholds-without-order** and **order-without-gate**.
- **Outcomes:** primarily *external* domain metrics (task success, failure/damage rate, cost, time, survival, cumulative regret) — **never** an internal quantity computed from the same F/P/A estimates the gate consumes (self-confirming).
- **Equal budget:** total = time + resources + information + compute + **risk exposure**.
- **Verdicts:**

```
PASS          iff  LCB95( effect vs. best baseline ) > Δ_min
KILL          iff  UCB95( effect ) < 0                  (the gate HARMS)
INCONCLUSIVE  otherwise                                 (neither victory nor death)
```

**POS-P2 — does the base actually burn?** A *causal*, not observational, test of base damage:

```
ΔB = E[ base_damage | π_premature ]  −  E[ base_damage | π_sequenced ]
```

estimated under matched initial conditions, randomized assignment, or a causally adjusted design (identification strategy pre-registered — regression to the mean and confounders are the named threats). `ΔB > 0` supports the base-burning mechanism; `ΔB ≤ 0` demotes it to metaphor under the pre-registered equivalence criterion.

### 9.6 Cross-domain universality & domain-of-applicability

"Universal" is a claim to be *tested per domain*, never assumed. The kernel's universality criterion is a lower-confidence-bounded fraction of domains with a positive effect:

```
LCB95[ Pr_d( δ_d > Δ_min ) ] ≥ q_min
```

where `δ_d` is the per-domain effect (hierarchically estimated), `Δ_min` the minimum practically-important effect, and `q_min` the required fraction of domains. *Illustrative only — ZERO authority, RUO:* `q_min = 0.8`, `Δ_min` domain-normalized. Universality is asserted **only** if this LCB clears `q_min`; a gate that pays in some domains and harms in others fails the criterion honestly.

**Domain-of-applicability (DoA).** Each deployment declares a DoA set `𝒟` (the input region where the estimators and `θ` calibration are validated).

- **Out-of-domain ⇒ ABSTAIN.** If the live state estimate falls outside `𝒟`, the kernel abstains rather than extrapolating a calibration it does not have.
- **No transport without a transportability argument.** A `θ` calibrated in domain `d` may not be reused in `d′` absent an explicit, recorded transportability argument (matched estimand, overlap, invariance assumptions). Silent transfer is prohibited and is itself an audit-loggable violation.

---

## 10. Formal kernel properties (within-model)

The following are propositions **true within the kernel's own definitions** — they say the machinery does what its symbols say. **None is an empirical proof.** They establish internal consistency (a necessary condition), not that the gate pays in the world — that is POS-P1/POS-P2 (§9.5). Each is stated in one line.

Throughout, the **fixed readiness authorization** is

```
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i  =  min_i PillarReady_i ,
   with   H_i = 1[ ∀ critical j :  LCB(z_ij) ≥ θ_ij^crit ]
```

so a critical shortfall vetoes authorization regardless of any surplus elsewhere.

| # | Property | One-line statement (true within the definitions — NOT an empirical proof) |
|---|---|---|
| **POS-F1** | **Firewall soundness** | If `Firewall(a) ≠ PASS` then `G_POS(a,t) = 0` for every value of `R_rob`, `κ`, and every readiness surplus — the firewall is a dominating multiplicative factor, so no readiness result can override a values-forbidden action. |
| **POS-F2** | **Critical non-compensation** | Because `G_ready = 1[R_rob≥1]·∏_i H_i` and each `H_i` requires `LCB(z_ij) ≥ θ_ij^crit` on every critical `j`, a single failed critical component forces `G_ready = 0` — no surplus in any non-critical component can compensate for a critical shortfall. |
| **POS-F3** | **Readiness monotonicity** | Holding all else fixed, raising any `LCB(z_ij)` (never crossing below a threshold it already met) can only keep `G_ready` equal or flip it 0→1, never 1→0 — more evidence of readiness never withdraws authorization. |
| **POS-F4** | **Stakes monotonicity** | Since every `θ` is non-decreasing in stakes `s` and `α(s)` is non-increasing, raising `s` can only raise the bar `R_rob` must clear — higher stakes weakly shrink the authorized set, never enlarge it. |
| **POS-F5** | **Probe containment** | For `κ(a) ≤ κ_probe` the gate authorizes on the reversible-probe branch with capped exposure `e(a) ≤ e_max`, and this branch can never satisfy the `a^commit` branch — a probe's authorization cannot escalate into an irreversible commitment. |
| **POS-F6** | **Order-independence of F∧P** | The readiness conjunction `1[LCB(F)≥θ_F] ∧ 1[LCB(P)≥θ_P]` is commutative, so its truth value is identical whether F or P is verified first — the fixed F-first *verification* order changes only check-economy, never the authorized set. |
| **POS-F7** | **Emergency auditability** | The emergency branch fires only on `a = a^emg ∧ M_emg > 0 ∧ Log(a,t) = COMPLETE`, so every forced move is, by construction, recorded before it is authorized — an unlogged emergency override is unrepresentable in the kernel. |
| **POS-F8** | **Abstention conservatism** | `ABSTAIN` is defined to entail `G_POS = 0` on every gated commitment (it withholds, never authorizes), so abstaining under infeasibility, OOD, or unresolved drift can never itself produce a false authorization. |

**Zero-clamp lemma (feeds POS-F2).** Each geometric sub-aggregator is `G_i(z) = ∏_j z_j^{w_ij}`, which maps any true-zero component to **exactly 0**. A logarithmic evaluation form may be used *only* to avoid numerical `−∞` on **strictly-positive, noisy measurements**:

```
log G_i(z) = ∑_j w_ij · log( z_j + ε )     — ε > 0 is a numerical guard ONLY
```

`ε` exists solely to keep floating-point arithmetic finite on measurements known to be strictly positive. `G_i` is **HARD-CLAMPED to 0** whenever any structural or true-zero component is present:

```
if  ∃ j : z_j is a structural/true zero   →   G_i(z) := 0   (clamp overrides the log form)
```

`ε` must **never** convert a true zero into a passing score — a true zero is a veto, not a small number.

**Stopping-time note (heuristic, not optimal).** The kernel's commitment time is a **one-step-lookahead commitment heuristic**, not a proven optimum:

```
τ_POS := min( τ_ready , τ_emg )
   τ_ready = inf{ t : G_ready(t) = 1 ∧ Firewall = PASS }
   τ_emg   = inf{ t : G_emg(t)   = 1 }
```

No optimality is claimed for the one-step lookahead. A genuinely *optimal* stopping rule would require defining a wait-value `V_wait` via the Snell envelope (`V_wait(t) = max( commit-now value , E[ discounted V_wait(t+1) ] )`) and committing when continuation value no longer dominates — the kernel flags this as future work and does **not** conflate it with `τ_POS`.

**Coverage note (feeds every LCB in the kernel).** `SCALAR_LCB` delivers only **per-component** `(1 − α)` coverage. For `m` jointly-read components the union bound gives joint coverage `≥ 1 − ∑_j α_j`. To obtain a *joint* `1 − α` meaning, apply **Bonferroni** (`α_j = α/m`) or escalate to a **JOINT_CHANCE / DRO** formulation — and the Decision Certificate (§11) must **record which coverage mode was used**. A gate that reads several LCBs at nominal per-component `α` while claiming joint `α` is silently under-covered.

---

## 11. Machine interface, decision certificate & compliance

The kernel is designed to drop in as a **filter between candidate selection and irreversible execution** — one checkpoint, engine-agnostic. This section fixes the machine contract so that any implementation is inspectable and reproducible. Nothing here upgrades epistemic status: a POS-compatible engine is still an **L2/B2 candidate** until POS-P1/POS-P2 report.

### 11.1 The evaluation signature

```
evaluate_pos(
    domain_adapter,      # maps domain quantities → F,P,A ∈ [0,1]; declares DoA 𝒟, θ calibration
    state_estimate,      # current F,P,A with uncertainty (mean + SE / posterior)
    candidate_action,    # the action, with κ, exposure e, and its identity
    stakes_profile,      # s, cost weights c_FA/c_FD/c_D, safety cap ε_FA(s)
    uncertainty_config,  # α(s), estimator, LCB mode, coverage mode (per-comp / Bonferroni / DRO)
    policy_config,       # θ family, κ_probe, e_max, drift bands, abstain rules
    audit_context        # kernel/adapter versions, data/model hashes, run id
) -> POSDecision
```

### 11.2 Typed inputs and outputs

**`POSInput` (assembled from the arguments):**

| Field | Type | Meaning |
|---|---|---|
| `F, P, A` | float[0,1] + SE | pillar estimates with uncertainty (Form↔Time, Position↔Space, Action↔Energy) |
| `critical_components z_ij` | float[0,1][] | per-pillar components, with a `critical` flag per `j` |
| `firewall_verdict` | enum{PASS, FAIL} | values-firewall result — dominating (POS-F1) |
| `kappa` | float[0,1] | irreversibility / commitment degree |
| `exposure e` | float[0,1] | capped-exposure ceiling for probes |
| `stakes s` | float[0,1] | drives θ, α, ε_FA monotonically |
| `alpha` | float(0,1) | confidence level; `dα/ds ≤ 0` |
| `coverage_mode` | enum{PER_COMPONENT, BONFERRONI, JOINT_CHANCE, DRO} | how joint LCB coverage is obtained |
| `emergency_bounds` | {LCB[L(inact)], UCB[L(a)]} \| null | required only for the emergency branch |
| `drift D_t` | float | live-vs-train distribution distance |
| `in_domain` | bool | is `state_estimate` ∈ DoA 𝒟 |

**`POSDecision` (the returned object):**

| Field | Type | Meaning |
|---|---|---|
| `authorize` | enum{AUTHORIZE, WITHHOLD, ABSTAIN} | the gate verdict; ABSTAIN on infeasible/OOD/undecidable |
| `G_POS` | {0,1} | binary gate (ABSTAIN ⇒ 0 on any commit, POS-F8) |
| `branch` | enum{PROBE, READY, EMERGENCY, FIREWALL_BLOCK, ABSTAIN} | which condition decided it |
| `R_rob, m_R, bottleneck` | float, float, enum{F,P,tie} | robust readiness ratio, margin, limiting pillar |
| `V_POS` | float | severity of an attempted violation (audit only, not a gate) |
| `reason_codes` | code[] | machine-readable justification (see 11.4) |
| `certificate` | DecisionCertificate | the immutable record (11.3) |

### 11.3 The immutable Decision Certificate

Every `evaluate_pos` call emits a tamper-evident certificate — the object an auditor replays. It is **append-only**; a re-decision produces a new certificate, never a mutation of an old one.

| Certificate field | Content |
|---|---|
| `kernel_version`, `adapter_version` | exact versions of the kernel and the domain adapter |
| `data_hash`, `model_hash` | content hashes of the input estimates and the estimator/model |
| `normalization_maps` | the exact domain-quantity → `F/P/A ∈ [0,1]` maps used |
| `thresholds` | the `θ` (incl. `θ_ij^crit`), `κ_probe`, `e_max` actually applied |
| `uncertainty_mode` | estimator, `α(s)`, LCB rule, **coverage_mode** (per §10 note) |
| `gate_result` | `authorize`, `branch`, `G_POS`, `R_rob`, `V_POS` |
| `reason_codes` | the codes emitted (11.4) |
| `override_log` | every `a^emg` forced move: `M_emg`, loss bounds, timestamp, operator, `Log=COMPLETE` |
| `drift_state` | `D_t`, band, and any lower-confidence / widen / recalibrate action taken |

### 11.4 Reason codes (illustrative registry — RUO)

`FW_BLOCK` (firewall failed) · `NOT_READY` (`R_rob < 1`) · `CRIT_VETO` (a critical `H_i = 0`) · `PROBE_OK` (`κ ≤ κ_probe`) · `READY_OK` (`R_rob ≥ 1`) · `EMG_FORCED` (`a^emg`, logged) · `ABSTAIN_INFEASIBLE` (empty feasible θ set) · `ABSTAIN_OOD` (outside DoA) · `ABSTAIN_DRIFT` (drift too high to trust). These are illustrative — ZERO decision authority — and stabilized per domain during POS-P1.

### 11.5 The 16-point Minimal Compliance Standard

An engine may call itself **"POS-compatible"** only if it satisfies all sixteen. Each is a checkable contract, not a performance claim.

| # | Requirement |
|---|---|
| 1 | Implements the `evaluate_pos` signature and returns a fully-typed `POSDecision`. |
| 2 | The values-firewall is a **dominating** factor: `Firewall ≠ PASS ⇒ G_POS = 0` unconditionally (POS-F1). |
| 3 | Uses the fixed authorization `G_ready = 1[R_rob≥1]·∏_i H_i`, with the critical veto `H_i` wired in (POS-F2). |
| 4 | Reads pillars at declared **lower confidence bounds**, never optimistic point estimates; `α(s)` declared before evaluation. |
| 5 | Records the **coverage mode** (per-component / Bonferroni / JOINT_CHANCE / DRO) and never claims joint `1−α` from per-component LCBs. |
| 6 | Geometric sub-aggregators **hard-clamp to 0** on any structural/true-zero; `ε` is a numerical guard on strictly-positive measurements only and never turns a true zero into a passing score. |
| 7 | Gate applicability keys on `κ, e, s` — **no label-gaming**; naming a high-`κ` commit "preparation" does not exempt it. |
| 8 | Probes (`κ ≤ κ_probe`) are ungated but **exposure-capped** (`e ≤ e_max`) and cannot escalate to the commit branch (POS-F5). |
| 9 | Thresholds and `α` are **stakes-monotone** (`dθ/ds ≥ 0`, `dα/ds ≤ 0`) and enforce the safety cap `Pr(FA\|s) ≤ ε_FA(s)`, `dε_FA/ds ≤ 0`. |
| 10 | The emergency branch fires only with `M_emg > 0` **and** a COMPLETE log; unlogged overrides are impossible (POS-F7). |
| 11 | The commitment time is exposed as `τ_POS = min(τ_ready, τ_emg)`, labeled a one-step-lookahead **heuristic** (no optimality claim). |
| 12 | Emits an **immutable, append-only Decision Certificate** with all fields of §11.3, including data/model hashes and normalization maps. |
| 13 | Returns **ABSTAIN** (⇒ `G_POS=0`) on infeasible θ, out-of-domain input, or undecidable drift (POS-F8). |
| 14 | Declares a **domain-of-applicability** set and refuses **transport** of a calibration without a recorded transportability argument. |
| 15 | Reports calibration diagnostics (reliability, Brier, ECE) on **separated** calibration / selection / evaluation splits. |
| 16 | Ships **preregistered** POS-P1/POS-P2 hooks (external outcomes, mandatory ungated & AD-RTD baselines, PASS/INCONCLUSIVE/KILL bands) and labels itself **L2/B2 — RUO — not validated** until they report. |

> **Scope (unchanged).** §11 makes the kernel *runnable, auditable, and embeddable* — not *validated*. A certificate proves what the engine did, not that gating pays. The gate remains an L2/B2 candidate operationalization with **ZERO decision authority** until POS-P1/POS-P2 clear it in the deployment's own domain. A formula — or an interface — makes a claim inspectable; it does not make it true.


---

# PART II — DOMAIN ADAPTERS  *(the formulas each sector applies)*

### Adapter — Research (labs, scientific programmes)

> **Status:** L2/B2 candidate operationalization of the POS commitment gate for the Research domain — **not** a validated law and **not** a theorem of `U = ∛(F·P·A)`. Every number below is **illustrative — ZERO decision authority** and **research-use-only (RUO)**. The decisive arbiter is the unrun calibration test **POS-P1 / POS-P2**. A formula makes a claim inspectable; it does not make it true.
>
> **Invariant (held):** Form ↔ Time · Position ↔ Space · Action ↔ Energy.
> Here: **F = method/team/instrument readiness** (the *when* — can the base carry the study), **P = field position / priority / funding runway / timing window** (the *where* — is this the place and moment), **A = execution capacity** (compute, data access, throughput — the *energy* to run it). `a^commit` = launch a large pre-registered study or lock a research direction; `a^prep` = pilots, instrument calibration, hiring, coalition-building; `a^probe` = a single cheap exploratory run, a literature spike, one exploratory dataset.

Conforms to the Domain Adapter Contract `DA_d = (Ψ, N, G, Θ, K, L, C, V)`. Each numbered block below fills one or more slots: (1) Ψ, (2) N, (3) Θ, (4) K, (5) L+V-firewall, (6) V worked, (7) C publication map.

---

#### (1) Ψ — F/P/A indicator set (units + direction)

Direction key: **↑** higher-is-readier · **↓** lower-is-readier (invert on normalize) · **⊙ band** target-band (score peaks inside a window, falls off either side).

| Pillar | Indicator | Symbol | Raw unit | Direction | Critical? |
|---|---|---|---|---|---|
| **F** (method/team/instrument) | Protocol maturity (pre-registration draft completeness) | `f_proto` | % of pre-reg fields locked | ↑ | — |
| **F** | Pilot effect-size stability | `f_pilot` | \|Δ effect\| across pilot batches (rel.) | ↓ | ✔ critical |
| **F** | Instrument calibration validity | `f_cal` | pass/partial/fail vs. reference standard, [0,1] | ↑ | ✔ critical |
| **F** | Team competency coverage | `f_team` | fraction of required roles filled + qualified | ↑ | — |
| **F** | Measurement reproducibility | `f_repro` | test–retest ICC / replication rate | ↑ | — |
| **P** (field position / priority / timing / runway) | Funding runway | `p_run` | months of committed budget at planned burn | ↑ | ✔ critical |
| **P** | Field priority / novelty margin | `p_prio` | reviewer-panel priority percentile | ↑ | — |
| **P** | Timing window | `p_win` | months until a scoop / obsolescence / policy deadline | ⊙ band | — |
| **P** | Ethics/access standing | `p_access` | IRB + data-use agreements secured, [0,1] | ↑ | ✔ critical |
| **P** | Collaboration / infrastructure standing | `p_collab` | fraction of MOUs / beam-time / cohort access signed | ↑ | — |
| **A** (execution capacity) | Compute throughput | `a_comp` | GPU·h/wk available ÷ GPU·h/wk required | ↑ | — |
| **A** | Data access volume | `a_data` | usable N (subjects / samples / tokens) ÷ powered N | ↑ | ✔ critical |
| **A** | Sustained pipeline throughput | `a_thru` | runs completed/wk ÷ runs/wk required to finish in window | ↑ | — |

> `A` is measured for completeness and reward-shaping but **is not a POS gate input** — POS gates on F-then-P only (§2). `A` shortfalls route to `a^prep` (buy compute, negotiate data), not to a commit veto.

---

#### (2) N — normalization notes

- **Target codomain:** every indicator maps to `z_j ∈ [0,1]`, readier = higher, via a **pre-declared** monotone map (declared *before* the gate is evaluated — POS forbids picking a friendlier map after seeing the verdict, §2.6.2).
- **↑ ratio indicators** (`a_comp, a_data, a_thru, p_run` after horizon-scaling): `z = clip_[0,1]( raw / requirement )`. A value ≥ requirement saturates at 1.
- **↓ indicators** (`f_pilot`): invert, e.g. `z = clip_[0,1]( 1 − |Δ|/Δ_tol )`.
- **⊙ band indicators** (`p_win`): score peaks in a declared window `[w_lo, w_hi]` (too-soon = under-prepared scoop risk *and* too-late = missed) and decays outside:
  ```
  z_win = exp( − ( (t_win − t_center) / w_scale )² )
  ```
- **Sub-aggregation per pillar — geometric, with a hard zero-clamp (FIX 1).**
  ```
  G_i(z) = ∏_j z_j^{w_ij}          Σ_j w_ij = 1 ,  w_ij ≥ 0        (i ∈ {F,P,A})
  ```
  A true/structural zero in any component maps `G_i` to **exactly 0** — non-negotiable. Example structural zeros: `f_cal = fail` (instrument invalid), `p_access = 0` (no IRB / no data-use agreement), `a_data = 0` (dataset does not exist).
  If a **log form** is used for numerical convenience:
  ```
  log G_i(z) = ∑_j w_ij · log( z_j + ε )     — ε ONLY to avoid −∞ on strictly-positive noisy measurements
  ```
  `ε` is a floating-point guard for **strictly-positive** noisy readings only. `ε` **must NEVER convert a true zero into a passing score.** Whenever any component is a structural/true zero, `G_i` is **HARD-CLAMPED to 0** *before* the log path runs. (In code: detect true-zero components first; clamp; only then apply the ε-log to the remaining strictly-positive terms.)
- **Confidence bound, not point estimate (N + Θ shared).** Each pillar readiness enters the gate as a **lower confidence bound** `LCB_{1−α}(F|a)`, `LCB_{1−α}(P|a)`, never the mean. `α = α(s)` tightens with stakes.
  - **`SCALAR_LCB` gives only PER-COMPONENT (1−α) coverage.** With `m` indicators inside a pillar, the naive joint coverage is only `≥ 1 − ∑_j α_j` (union bound). For a **joint 1−α** reading use **Bonferroni** (`α_j = α/m`) or escalate to **JOINT_CHANCE / DRO**. **Record which was used** in the C-slot publication (block 7). Default here: Bonferroni per pillar, `α/m`, recorded.

---

#### (3) Θ — ILLUSTRATIVE readiness thresholds `θ_F / θ_P`

> **ILLUSTRATIVE — ZERO decision authority · RUO.** These numbers exist only to make the mechanism concrete. They are un-calibrated placeholders superseded the instant POS-P1 calibration exists. Do **not** deploy them to authorize any real research commitment.

Threshold family (the §2.6.3 calibration candidate, per-domain baseline + risk terms):
```
θ_i(a,d,s) = clip_[0,1]( θ_i⁰(research) + β_i·κ(a) + γ_i·e(a) + η_i·s ) ,   i ∈ {F,P}
```

| Quantity | Illustrative value | Note |
|---|---|---|
| `θ_F⁰(research)` | **0.70** | method/team/instrument base bar (RUO) |
| `θ_P⁰(research)` | **0.60** | field-position/runway base bar (RUO) |
| `β_F, β_P` | 0.12, 0.10 | irreversibility loading (RUO) |
| `γ_F, γ_P` | 0.06, 0.06 | exposure loading (RUO) |
| `η_F, η_P` | 0.08, 0.10 | stakes loading (RUO) |
| `κ_probe` | 0.20 | at/below → ungated probe (RUO) |
| `α(s)` band | 0.05 → 0.01 | one-sided; tighter for high-stakes / dual-use (RUO) |
| Critical-component floors `θ_ij^crit` | `f_cal ≥ 0.99`, `p_access ≥ 0.99`, `a_data ≥ 0.80`, `f_pilot z ≥ 0.60`, `p_run z ≥ 0.60` | LCB must clear these (FIX 2, RUO) |

Illustrative resolved bars for a high-`κ` pre-registered launch (`κ≈0.85, e≈0.7, s≈0.7`): `θ_F ≈ 0.70+0.12·0.85+0.06·0.7+0.08·0.7 ≈ 0.90`, `θ_P ≈ 0.60+0.10·0.85+0.06·0.7+0.10·0.7 ≈ 0.80`. **RUO — ZERO decision authority.**

**Readiness authorization with critical veto (FIX 2 — non-compensation as a theorem):**
```
H_i = 1[ ∀ critical j ∈ pillar i :  LCB_{1−α}(z_ij) ≥ θ_ij^crit ]        (per-pillar critical veto)
R_rob(a,t) = min(  LCB(F_t|a)/θ_F(a,d,s) ,  LCB(P_t|a)/θ_P(a,d,s)  )
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i      ≡   min_i PillarReady_i
```
Only with the `∏_i H_i` veto wired in is **critical non-compensation (POS-F2)** an actual theorem: a failed instrument calibration or a missing IRB cannot be bought back by a surplus of compute or a stellar pilot. The geometric sub-aggregator (block 2) enforces this at the component level; `H_i` enforces it at the confidence-bound level.

---

#### (4) K — irreversibility κ and exposure e

**κ(a) ∈ [0,1] — from sunk cost + opportunity cost of a wrong direction (recoverability).** Estimate as a recoverability complement:
```
κ(a) = 1 − Recover(a) ,   Recover(a) = (salvageable_budget + redeployable_time + transferable_assets) / (total_committed)
```
Research-specific drivers that push `κ → 1`:
- **Sunk cost:** non-refundable beam-time / cohort-recruitment / bespoke-instrument spend that cannot be redeployed.
- **Opportunity cost of a wrong direction:** the field-time lost while a competitor addresses the *right* question; a pre-registered arm that locks the design and forecloses pivots.
- **Reputational / credibility lock-in:** a public pre-registration or large-cohort commitment that, if it fails from an unready base, poisons the programme's standing (base-burning, §3.1 institutional analogue).

Illustrative `κ` ladder (RUO): one exploratory run `κ≈0.05` · pilot batch `κ≈0.15` · hire a postdoc `κ≈0.35` · buy a bespoke rig `κ≈0.6` · **launch a 3-year pre-registered multi-site study `κ≈0.85`**.

**Exposure e(a) ∈ [0,1]** (distinct from κ — how much of the programme is *at stake* on this one action):
```
e(a) = clip_[0,1]( committed_resource(a) / total_programme_capacity )
```
e captures blast radius (fraction of budget/headcount/reputation staked); κ captures un-recoverability. A cheap-but-irreversible act has low e, high κ; a large-but-reversible act has high e, low κ. Both raise `θ` monotonically (block 3).

---

#### (5) L + V-firewall — values / legal / safety firewall

**The firewall DOMINATES every readiness result. It is checked FIRST. No `R`, no `κ`, no margin, however favorable, authorizes a firewall-forbidden action.** (§2.5, §7.)

| Firewall gate | Instantiation | Failure verdict |
|---|---|---|
| **Research ethics / IRB** | Human/animal-subjects approval current & scoped to *this* protocol; informed-consent instrument approved | `Firewall = FAIL` → categorically prohibited (not merely readiness-forbidden) |
| **Dual-use research of concern (DURC)** | Screened against the corpus dual-use firewall (`APPENDIX_WAR`, TRC/TRA firewalls): no enhancement-of-pathogen / weaponizable-capability / uplift class; DURC review board sign-off | `FAIL` → prohibited at every readiness level |
| **Legal / regulatory** | Data-protection (GDPR/HIPAA-equiv.) lawful basis; export-control on methods/data; licensing of materials | `FAIL` → prohibited |
| **Safety** | Biosafety/chemical/radiation containment level matched to protocol; incident plan filed | `FAIL` → prohibited |

```
Firewall(a) = IRB(a) ∧ ¬DURC(a) ∧ Legal(a) ∧ Safety(a)
G_POS(a,t) = 1[ Firewall(a)=PASS ] · [ 1[κ ≤ κ_probe] ∨ G_ready ∨ (M_emg>0 ∧ a=a^emg ∧ Log=COMPLETE) ]
```
A values-firewall failure is **never** folded into the audit severity `V_POS` and is never traded against readiness — it is a hard categorical refusal (§2.6.4). Note the two senses of "forbidden": `p_access` low is *readiness*-forbidden (fixable by securing IRB → an `a^prep`); a DURC hit is *values*-forbidden (never unlockable by any amount of preparation).

---

#### (6) V — worked mini-example (ALL numbers illustrative / RUO — ZERO decision authority)

**Candidate `a^commit`:** *"Launch a 3-year, multi-site, pre-registered clinical-imaging study."* `κ = 0.85`, `e = 0.70`, `s = 0.70`.

**Step 0 — Firewall.** IRB: approved for this protocol ✔. DURC: n/a (not DURC class) ✔. Legal (data-use agreements): ✔. Safety: ✔. → `Firewall = PASS`. Proceed to readiness. `κ = 0.85 > κ_probe = 0.20`, so the probe branch does **not** apply — full readiness required.

**Step 1 — resolved thresholds (from block 3, RUO):** `θ_F ≈ 0.90`, `θ_P ≈ 0.80`.

**Step 2 — measured pillar LCBs (Bonferroni α/m, recorded — RUO):**

| Pillar | `LCB(·)` | `θ` | ratio |
|---|---|---|---|
| F | 0.93 | 0.90 | 1.03 |
| P | **0.72** | 0.80 | **0.90** |

`R_rob = min(1.03, 0.90) = 0.90`.

**Step 3 — critical veto `H_i` (FIX 2):** F critical floors clear (`f_cal` LCB 0.99 ✔, `f_pilot z` 0.71 ✔). P critical floors: `p_access` LCB 0.99 ✔, but **`p_run` z = 0.55 < 0.60 floor** ✘ (funding runway short of the powered study length). → `H_P = 0` → `∏_i H_i = 0`.

**Step 4 — state R and verdict.**
```
R_rob = 0.90 (< 1)   AND   ∏_i H_i = 0   ⇒   G_ready = 0
G_POS = 1[PASS] · [ 0 ∨ 0 ∨ 0 ] = 0
```
**VERDICT: readiness-forbidden — the Forbidden Action.** Active bottleneck `b = P` (runway/timing). Audit severity `V_POS = s·κ·[1−R]_+ = 0.70·0.85·0.10 ≈ 0.060` (RUO) — a real but not extreme violation, dominated by the critical `p_run` veto rather than the soft ratio.

**Step 5 — `a^prep` alternative (ungated, low-κ, flows freely).** Do **not** launch. Instead: (i) secure a bridge grant / extend the funding runway to cover the powered horizon (lifts `p_run` z past 0.60, clears `H_P`); (ii) run a 6-month single-site pilot (`a^probe`, `κ≈0.15`) to tighten the F effect-size CI and lift `LCB(P)` via a stronger priority score; (iii) re-run the gate. Sequence the Position, then commit — the door that is shut now opens on a prepared base.

---

#### (7) C — one-line mapping to the 16-point compliance standard

**This adapter must publish, per the 16-point compliance standard:** (1) the Ψ indicator list with units/direction; (2) the N normalization maps *pre-declared*; (3) the geometric sub-aggregator **with its hard zero-clamp rule and the ε-scope statement** (FIX 1); (4) the critical-component set + floors `θ_ij^crit`; (5) the wired veto `G_ready = 1[R_rob≥1]·∏_i H_i` (FIX 2); (6) `θ_i⁰, β,γ,η, κ_probe` values flagged **illustrative/ZERO-authority/RUO**; (7) the `κ` recoverability estimator + drivers; (8) the exposure `e` estimator; (9) `α(s)` schedule; (10) **which multiplicity correction was used — Bonferroni α/m vs. JOINT_CHANCE/DRO** (never bare per-component SCALAR_LCB for a joint claim); (11) the firewall instantiation (IRB / DURC / legal / safety) as a *dominating first check*; (12) the SSS-Guard independent-metric cross-check for the irreversible verdict; (13) `V_POS` audit log + every `a^emg` forced-move log; (14) the stopping-time definition (below); (15) the POS-P1/P2 pre-registration pointer as the decisive arbiter; (16) the epistemic banner (L2/B2 candidate operationalization, RUO).

**Stopping time (FIX 3 — no false optimality claim):**
```
τ_ready = inf{ t : G_ready(a,t) = 1 }
τ_emg   = inf{ t : G_emg(a,t)  = 1 }
τ_POS  := min( τ_ready , τ_emg )
```
`τ_POS` is a **one-step-lookahead commitment heuristic**, **not** a proven-optimal stopping rule. (For an optimality claim, define `V_wait` via the Snell envelope and solve the optimal-stopping problem — out of scope here.) Do **not** write `τ_POS += …`; `τ_POS` is a min of first-hitting times, defined once.

### Adapter — Investment funds (capital allocation, LBO & restructuring)

> **Status:** L2/B2 candidate operationalization of the POS commitment gate for a capital-allocation / buyout / restructuring desk. **Not** a validated law and **not** a theorem of `U = ∛(F·P·A)`. Every number below is **illustrative — ZERO decision authority** and **research-use-only (RUO)**. The decisive arbiter remains the unrun calibration test **POS-P1/POS-P2**. A formula makes a claim inspectable; it does not make it true.
>
> **Invariant (unchanged):** Form ↔ Time · Position ↔ Space · Action ↔ Energy.
> **Domain reading:** F = organizational / thesis readiness and diligence completeness (Time — is the base built yet?); P = market position, valuation, debt structure and competitive standing (Space — can the place carry the blow?); A = capital-deployment and integration capacity (Energy — can you actually execute the conversion?).
> **Gated object:** `a^commit` = full leveraged buyout / major fund allocation. `a^prep` = partial stake, operational-improvement mandate, extended diligence, staged tranche. `a^probe` = LOI, data-room read, expert calls, small toehold within a capped exposure.

This section instantiates the Domain Adapter Contract `DA_d = (Ψ, N, G, Θ, K, L, C, V)`: the indicator schema **Ψ**, normalization **N**, sub-aggregators **G**, thresholds **Θ**, irreversibility/exposure kernel **K**, the loss model **L**, the compliance map **C**, and the values/legal firewall **V**.

---

#### 1. Ψ — F/P/A indicator table (units · direction)

Direction key: **↑** higher-is-better · **↓** lower-is-better · **⊙** target-band. "crit?" marks a **critical** indicator subject to the non-compensating veto (§2, fix 2). All raw indicators are mapped to `z_j ∈ [0,1]` by **N** (§2) before aggregation.

**F — organizational / thesis readiness & diligence completeness (Time)**

| Indicator | Symbol | Unit | Dir | crit? |
|---|---|---|---|---|
| Diligence coverage (workstreams signed-off / total) | z_F1 | fraction [0,1] | ↑ | **yes** |
| Quality-of-earnings / EBITDA verified vs. reported | z_F2 | ratio | ⊙ (→1.0) | **yes** |
| Investment-thesis specificity (value-creation plan gated milestones) | z_F3 | count, normalized | ↑ | no |
| Deal-team capacity vs. deal complexity | z_F4 | staffed-FTE / required-FTE | ↑ | no |
| Legal/tax/environmental red-flag closure | z_F5 | fraction resolved [0,1] | ↑ | **yes** |
| Open material contingencies (unresolved diligence gaps) | z_F6 | count | ↓ | no |
| Data-room completeness / representation confidence | z_F7 | fraction [0,1] | ↑ | no |

**P — market position / valuation / debt structure / competitive standing (Space)**

| Indicator | Symbol | Unit | Dir | crit? |
|---|---|---|---|---|
| Entry multiple vs. sector median | z_P1 | EV/EBITDA ratio | ↓ (⊙ discount band) | no |
| Margin of safety (intrinsic − entry) / intrinsic | z_P2 | fraction | ↑ | no |
| Net leverage at close | z_P3 | Net debt / EBITDA (×) | ↓ | **yes** |
| Interest / fixed-charge coverage | z_P4 | EBITDA / interest (×) | ↑ | **yes** |
| Debt maturity runway (nearest wall) | z_P5 | years | ↑ | **yes** |
| Covenant headroom | z_P6 | % cushion to trip | ↑ | **yes** |
| Competitive moat / market-share defensibility | z_P7 | ordinal 0–1 | ↑ | no |
| Cyclicality / demand-shock exposure | z_P8 | β-like, normalized | ↓ | no |

**A — capital-deployment & integration capacity (Energy)**

| Indicator | Symbol | Unit | Dir | crit? |
|---|---|---|---|---|
| Dry powder vs. commitment size | z_A1 | committed / required | ↑ | no |
| Concentration after deploy (position / fund NAV) | z_A2 | fraction | ↓ (⊙ mandate cap) | **yes** |
| Integration / 100-day plan readiness | z_A3 | fraction of plan staffed [0,1] | ↑ | no |
| Operating-partner / management bench depth | z_A4 | ordinal 0–1 | ↑ | no |
| Financing certainty (committed vs. best-efforts) | z_A5 | fraction committed [0,1] | ↑ | **yes** |
| Time-to-value-realization vs. fund life remaining | z_A6 | ratio | ⊙ | no |

---

#### 2. N — normalization notes

- **Range map.** Each raw indicator is mapped to `z_j ∈ [0,1]`, higher = more ready. Directions are enforced *in N*, before **G** sees any value:
  - **↑** indicators: `z = clip_[0,1]( (x − x_lo) / (x_hi − x_lo) )`.
  - **↓** indicators (leverage, contingencies, concentration): invert — `z = clip_[0,1]( (x_hi − x) / (x_hi − x_lo) )`.
  - **⊙ target-band** indicators (QoE ratio, entry multiple, time-to-value): `z = clip_[0,1]( 1 − |x − x*| / w )` for band centre `x*` and half-width `w`.
- **Anchors are declared before the gate is evaluated** (POS §2.6.2). Choosing a friendlier `x_lo/x_hi/x*` after seeing whether the deal passes is prohibited.
- **True-zero discipline (fix 1).** A structural/true zero on a component — e.g. `z_A5 = 0` financing *not committed*, `z_F5 = 0` an unresolved environmental red flag, `z_P6 = 0` covenant already tripped — must survive normalization as **exactly 0**, never a small floor. `N` may not clamp a genuine zero up to `ε`.
- **LCB, not point estimate.** Each pillar is read at a lower confidence bound. Diligence uncertainty enters here: a *point-estimate* "ready" pillar can fall **below** the gate once the LCB is taken (worked in §6).

---

#### 3. G — sub-aggregators (geometric, with the zero-clamp baked in)

Each pillar is a weighted geometric mean of its normalized indicators:

```
G_i(z) = ∏_j z_j^(w_ij) ,     ∑_j w_ij = 1 ,   w_ij ≥ 0 ,   i ∈ {F, P, A}
```

The geometric form is deliberate: it maps a **true zero to exactly 0**, so an unfinanced, red-flagged, or covenant-tripped deal cannot be "averaged up" by a strong thesis. Non-compensation at the zero-limit is the whole point.

**Fix 1 — the ε is numerical only.** If a log form is used for stability on **strictly-positive noisy measurements**:

```
log G_i(z) = ∑_j w_ij · log(z_j + ε) ,   ε ≈ 1e−9   (ONLY to avoid −∞ on strictly-positive noisy inputs)
```

then `ε` is a floating-point guard and nothing else. Whenever **any structural/true-zero component is present**, `G_i` is **HARD-CLAMPED to 0**:

```
if ∃ j : z_j is a structural/true zero   →   G_i(z) := 0     (ε is ignored)
```

`ε` must **never** convert a true zero into a passing score. A best-efforts financing (`z_A5 = 0`) drives `G_A = 0` regardless of how attractive the entry multiple looks.

Then, unchanged from the engine: `U = ∛(F·P·A)` with `F = G_F`, `P = G_P`, `A = G_A`.

---

#### 4. Θ — illustrative readiness thresholds (ZERO decision authority)

Thresholds are **functions**, not constants: `θ_F(a,d,s)`, `θ_P(a,d,s)` per POS §2.6.3, compared against the **LCB** of each pillar. The values below are the retained engine placeholders — **illustrative — ZERO decision authority · RUO** — kept only to make the mechanism concrete. They are un-calibrated; the asymmetry is unjustified; they are superseded by the calibrated `θ(a,d,s)` the moment POS-P1 exists.

| Action class | κ band | θ_F (illustrative) | θ_P (illustrative) | Note |
|---|---|---|---|---|
| `a^probe` (LOI, data-room, toehold) | κ ≤ κ_probe ≈ 0.15 | ungated | ungated | capped exposure only |
| `a^prep` low-κ (diligence, ops mandate, minority stake) | κ ≲ 0.4 | ungated | ungated | this *is* the sequencing work |
| `a^prep` high-κ (large staged tranche disguised as prep) | κ ≳ 0.6 | **0.65** | **0.55** | no label-gaming — must clear |
| `a^commit` (full LBO / major allocation) | κ ≳ 0.8 | **0.65** | **0.55** | plus stakes-scaling below |

Stakes scaling (illustrative): `θ_i(a,d,s) = clip_[0,1]( θ_i⁰ + β_i·κ(a) + γ_i·e(a) + η_i·s )`, all coefficients `≥ 0`, monotone in κ, e, s. For a flagship-fund-scale buyout (`s → 1`) the effective `θ_F` rises toward the SSS critical band (≥ 0.75) — **cited for scale only, no independent authority**.

**Fix 2 — the critical-veto is wired into authorization, not bolted on:**

```
H_i     = 1[ ∀ critical j in pillar i :  LCB(z_ij) ≥ θ_ij^crit ]
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i        (equivalently  min_i PillarReady_i )

R_rob   = min(  LCB(F)/θ_F ,  LCB(P)/θ_P  )
```

Only with the veto wired *inside* `G_ready` is critical non-compensation (POS-F2) actually a theorem of the gate: a single tripped covenant (`z_P6` critical, LCB below `θ^crit`) forces `H_P = 0` and `G_ready = 0`, no matter how high the aggregate `R_rob`.

**Critical-component coverage (union bound).** `SCALAR_LCB` gives only **per-component** `(1−α)` coverage. With `m` critical indicators vetted at level `α_j`, joint coverage is `≥ 1 − ∑_j α_j` (union bound). For a genuine **joint 1−α** guarantee across the critical set, use **Bonferroni** (`α_j = α/m`) or escalate to **JOINT_CHANCE / DRO** — and **record which was used** in the deal file. (This adapter's default: Bonferroni across the critical set; escalate to DRO for `s → 1` flagship deals.)

---

#### 5. K — irreversibility κ and exposure e in this domain

**κ (irreversibility, via recoverability).** In capital allocation, κ is *commitment* irreversibility — how little of the position and its opportunity cost you get back if the thesis breaks. Estimate from recoverability drivers, each normalized to [0,1] and combined (declared method, e.g. weighted mean, monotone in each):

```
κ(a) ≈ f( lockup, leverage, secondary_illiquidity, control_stake, restructuring_depth )

 lockup              = normalized capital lock-up horizon / fund-life fraction
 leverage            = net debt / EBITDA, mapped ↑ (more leverage → less reversible)
 secondary_illiquidity = 1 − (estimated recoverable-at-fair-value fraction on forced exit)
 control_stake       = share of a controlling/hard-to-unwind position
 restructuring_depth = irreversibility of operational moves (layoffs, plant closure, refinancing)
```

Illustrative κ ladder (**ZERO authority · RUO**): data-room read κ≈0.05 · minority PIPE with registration rights κ≈0.35 · staged control tranche κ≈0.6 · **full LBO with committed leverage and 5–7yr lock-up κ≈0.85** · deep restructuring with irreversible headcount/asset actions κ≈0.9+.

**e (exposure).** Fraction of the fund genuinely at risk in the commitment:

```
e(a) = clip_[0,1]( (capital_at_risk + λ·recourse_guarantees) / fund_NAV )
```

`capital_at_risk` includes equity check plus any fund-level recourse or bridge exposure; `λ ≥ 1` up-weights recourse/guarantee overhang. e is **separate from κ** (fix per POS §2.6.3): a small toehold in an illiquid name is high-κ / low-e; a large committed but liquid allocation is low-κ / high-e. Both feed Θ.

---

#### 6. V — the values / legal / safety firewall (this domain)

**The firewall dominates every readiness result** (POS §7): no `R`, however high, authorizes a firewall-barred deal. `Firewall(a) = PASS` is checked **first**; a fail is categorical and is **never** folded into the readiness score or `V_POS`.

| Firewall gate | Fails (→ categorical PROHIBIT) when… |
|---|---|
| **Securities law** | material non-public information in the thesis; disclosure/registration defect; market-manipulation exposure; sanctions/KYC-AML hit on counterparties |
| **Antitrust / merger control** | deal creates a prohibited concentration; gun-jumping; required HSR / EC / CMA clearance not obtained |
| **Fiduciary duty** | breach of duty to LPs (undisclosed conflict, self-dealing, side-letter/allocation violation, mandate breach) |
| **Safety / ESG hard constraints** | environmental/worker-safety liabilities above the fund's absolute red-line; dual-use / prohibited-sector exclusions |

Firewall PASS is necessary, never sufficient — a legally clean deal from an unready base is still the **Forbidden Action**.

---

#### 7. Worked mini-example (illustrative · RUO · ZERO decision authority)

*A flagship-fund full LBO of a mid-market industrial (`a^commit`, κ≈0.85, e≈0.30, s≈0.8). All numbers illustrative — ZERO decision authority.*

1. **Firewall (V).** HSR filing cleared, no MNPI, LP conflicts disclosed → `Firewall = PASS`. (A fail here would end it regardless of the rest.)
2. **Pillars — point estimate then LCB.** Diligence and ops work have advanced the base: F improved **0.40 → 0.72** and P improved **0.50 → 0.61** as point estimates. But open contingencies (`z_F6`) and QoE noise widen the diligence uncertainty, so the Bonferroni-adjusted **LCB** pulls the readings down: `LCB(F) ≈ 0.63`, `LCB(P) ≈ 0.58`.
3. **Critical veto (H).** All critical indicators clear their `θ^crit` **except** none tripped here — financing committed (`z_A5=1`), covenants have headroom (`z_P6`), leverage within band → `H_F = H_P = H_A = 1`. (Had financing been best-efforts, `G_A = 0` by the zero-clamp and the deal dies immediately.)
4. **Readiness ratio (R_rob).** Against illustrative `θ_F = 0.65`, `θ_P = 0.55`:

```
R_rob = min( LCB(F)/θ_F , LCB(P)/θ_P )
      = min( 0.63/0.65 , 0.58/0.55 )
      = min( 0.969 , 1.055 )
      = 0.969   →   Form is the active bottleneck b = F
```

5. **Verdict.** `R_rob = 0.969 < 1` and although `∏_i H_i = 1`, `1[R_rob ≥ 1] = 0` → `G_ready = 0`. **Readiness-forbidden.** Note the trap the LCB caught: the *point-estimate* F (0.72) sits comfortably above `θ_F` (0.65) and would have read "ready" — but **adding due-diligence uncertainty (the LCB) keeps the point-estimate-ready state below the gate.**

> **Model-sensitive bottleneck note (Variant B — audit lesson, not a contradiction).** This component-aware diligence illustration yields **Form** as the active bottleneck (`b = F`). The executable reference `pos_example_lbo.py` uses aggregate-level Gaussian `SCALAR_LCB` uncertainty on the same state and yields **Position** (`R_F ≈ 0.990`, `R_P ≈ 0.970`, `b = P`). These are **distinct uncertainty instantiations, not contradictory executions of one identical state.** The final verdict — `WITHHOLD` — is **robust across both**, while the bottleneck *identity* is model-sensitive. Every reported bottleneck MUST therefore carry its adapter version, indicator structure, and coverage mode.
6. **a^prep alternative.** The bottleneck is F, so the disciplined move is a low-κ preparation that raises Form-readiness without committing: close the named diligence contingencies (`z_F6 ↓`), finish QoE (`z_F2 → 1.0`), and — if a position is wanted now — take a **minority / staged tranche** (κ≈0.35, ungated) rather than the full LBO. Re-run the gate when `LCB(F)` clears `θ_F`. Severity of the attempted violation, for the audit log: `V_POS = s·κ·[1−R]_+ = 0.8·0.85·0.031 ≈ 0.021` — small, because the deal was *close*, not reckless; still, `G_ready = 0` holds.

*This is a one-step readiness check, not a claim of optimality (see §8).*

---

#### 8. Stopping time (fix 3)

The desk does not "add up" waiting steps. The commitment time is:

```
τ_POS := min( τ_ready , τ_emg )
   τ_ready = inf{ t : G_ready(a,t) = 1 }        (base becomes ready)
   τ_emg   = inf{ t : G_emg(a,t)  = 1 }        (forced-move branch fires)
```

`τ_POS` is a **one-step-lookahead commitment heuristic** — it is **not** claimed optimal. (For an optimality claim, define `V_wait` via the Snell envelope and solve the optimal-stopping problem; this adapter does not.) Never written as `τ_POS += …`. The emergency branch (`a^emg`, e.g. a rescue-financing where inaction is the larger irreversible loss) requires the robust margin `M_emg > 0` on confidence bounds and **mandatory logging**.

---

#### 9. C — one-line mapping to the 16-point compliance standard

**This adapter must publish, per deal:** (1) the Ψ indicator schema with units/direction/critical flags; (2) the declared N anchors (`x_lo/x_hi/x*/w`) fixed *before* evaluation; (3) the G weights `w_ij` and the true-zero-clamp attestation; (4) the Θ threshold functions `θ_F/θ_P(a,d,s)` with every illustrative constant flagged ZERO-authority/RUO; (5) the critical veto set and its `θ^crit`; (6) the LCB method, `α(s)`, and **which multiplicity correction was used** (Bonferroni α/m vs. JOINT_CHANCE/DRO); (7) the κ recoverability decomposition and (8) the exposure `e` computation; (9) the firewall verdict (securities / antitrust / fiduciary / safety) with evidence; (10) the computed `R_rob`, `G_ready`, bottleneck `b`, and `V_POS`; (11) the `a^commit` vs `a^prep` decision and rationale; (12) `τ_POS` with any `a^emg` forced-move log; (13) the SSS-Guard independent cross-check on the irreversible verdict; (14) the POS-P1/POS-P2 preregistration status (calibration **unrun** — stated plainly); (15) the equal-budget accounting for any comparison claim; and (16) the standing epistemic-status stamp: **L2/B2 candidate operationalization, RUO, ZERO decision authority, decisive arbiter = the unrun POS-P1/POS-P2 calibration test.**

### Adapter — Factories & manufacturing (industrial operations & safety)

> **Status:** L2/B2 candidate operationalization of the POS commitment gate for `DA_d = (Ψ, N, G, Θ, K, L, C, V)`. **Not** a validated law and **not** a theorem of `U = ∛(F·P·A)`. Every number below is **illustrative — ZERO decision authority** and **research-use-only (RUO)**. The decisive arbiter is the unrun calibration test **POS-P1/POS-P2**. A formula makes a claim inspectable; it does not make it true.
> **Invariant preserved:** Form ↔ Time · Position ↔ Space · Action ↔ Energy. Here: **Form** = the plant's built-up readiness *over time* (qualification, maintenance, competence — Time); **Position** = its standing *in the supply/regulatory space* (order book, permits, site, second-source map — Space); **Action** = the *energy* it can deploy to change state (changeover, ramp, launch — Energy).

The gated commitment `a^commit` in this domain is a **major line changeover, a capacity scale-up, or a new-product launch** — moves whose retooling is costly-to-undo. Ungated `a^prep` / `a^probe`: a pilot line, a requalification run, an FAT/SAT dry-run, operator training, a single-cell trial. Small reversible trials flow freely; the decisive irreversible commit must clear the gate.

#### (Ψ, N) — F/P/A indicator set with units and direction

Each raw indicator `x` is mapped to a pillar-component score `z ∈ [0,1]` by the normalizer `N` (notes below). Direction column: **↑** higher-is-better, **↓** lower-is-better, **⊡** target-band. **crit** marks a *critical component* subject to the veto `H_i` (§ fix 2) — never averaged away.

**Form `F` — equipment / process / workforce readiness, maintenance & qualification state**

| Component | Raw indicator | Unit | Dir. | crit |
|---|---|---|---|---|
| `z_F,mnt` | maintenance-plan compliance (PMs done on schedule) | % | ↑ | |
| `z_F,oee` | equipment health / OEE at target line | % | ↑ | |
| `z_F,cpk` | process capability of the critical CTQ | Cpk (idx) | ↑ | crit |
| `z_F,cal` | calibration currency of gauges/instruments | % in-date | ↑ | |
| `z_F,mtbf` | reliability reserve = MTBF / demanded-run-length | ratio | ↑ | |
| `z_F,skill` | operators certified for the new config / total needed | % | ↑ | crit |
| `z_F,spare` | safety-critical spare-part coverage | % SKUs stocked | ↑ | |
| `z_F,pq` | PQ/qualification state (IQ→OQ→PQ complete) | stage 0–3 | ↑ | crit |

**Position `P` — supply-chain position / order book / regulatory & site position**

| Component | Raw indicator | Unit | Dir. | crit |
|---|---|---|---|---|
| `z_P,perm` | environmental / operating permits valid for the new state | 0/1 or % clauses | ↑ | crit |
| `z_P,ob` | firm order-book coverage of the new capacity | months / % | ↑ | |
| `z_P,src` | qualified second-source coverage of critical inputs | % critical BOM | ↑ | crit |
| `z_P,inv` | input-inventory buffer vs. ramp demand | days-of-supply | ⊡ | |
| `z_P,leadΔ` | supplier lead-time slack vs. ramp schedule | days (slack) | ↑ | |
| `z_P,reg` | product-safety / regulatory clearance for the new SKU | 0/1 | ↑ | crit |
| `z_P,cust` | customer PPAP/first-article approval state | % approved | ↑ | |
| `z_P,site` | site capacity headroom (space, power, utilities) | % headroom | ↑ | |

**Action `A` — production / changeover / ramp capacity** *(diagnostic pillar; POS gates on `F`, `P` — `A` is read for triage/monitoring, not as a gate threshold)*

| Component | Raw indicator | Unit | Dir. |
|---|---|---|---|
| `z_A,cap` | demonstrated throughput vs. target rate | % of target | ↑ |
| `z_A,sur` | changeover/SMED time vs. planned window | ratio | ↓ |
| `z_A,ramp` | yield at ramp vs. steady-state yield | % | ↑ |
| `z_A,flex` | mix-flexibility / schedule slack | % | ↑ |

#### (N) — Normalization notes

- **Map to [0,1] against a declared reference, not a rolling max.** Use fixed anchors: `z = clip_[0,1]((x − x_floor)/(x_target − x_floor))` for ↑ indicators; mirror for ↓; two-sided ramp for ⊡ (e.g. inventory buffer penalized both when starved *and* when overstocked). Anchors `x_floor, x_target` are **declared before** the gate is evaluated (§2.6.2 discipline) — no re-anchoring after seeing the verdict.
- **Structural / true zeros are HARD ZEROS, not small numbers.** A missing permit, an incomplete PQ stage, or an expired product-safety clearance maps to `z = 0` **exactly** — a categorical/structural zero, distinct from a merely low continuous measurement.
- **Geometric sub-aggregator (G), zero-clamp (fix 1).** Each pillar is aggregated geometrically so a dead component cannot be bought back:

```
G_i(z) = ∏_j z_j^(w_ij)            with  ∑_j w_ij = 1 ,  w_ij ≥ 0
```

  A true zero in any `z_j` maps `G_i` to **exactly 0**. A log form may be used **only** for numerical −∞ avoidance on strictly-positive noisy measurements:

```
log G_i(z) = ∑_j w_ij · log(z_j + ε)        ε > 0, ε ≈ 1e-9
```

  **ε is ONLY a floating-point guard on strictly-positive components.** `G_i` is **HARD-CLAMPED to 0** whenever any structural/true-zero component is present:

```
if  ∃ j : is_structural_zero(z_j)   →   G_i := 0     (ε path is NOT taken)
```

  **ε must NEVER convert a true zero into a passing score.** A plant with `z_P,perm = 0` has `P = 0`, full stop — no maintenance surplus rescues it.
- **`A` is diagnostic only.** `A` is normalized identically but does **not** enter the readiness ratio `R`; it feeds the active-bottleneck triage and LGP-10 monitoring.

#### (Θ) — ILLUSTRATIVE readiness-threshold set — **ZERO decision authority, RUO**

> These placeholders exist only to make the mechanism concrete. They are **un-calibrated**; the asymmetry between `θ_F` and `θ_P` is **unjustified**; they are **superseded by `θ_i(a,d,s)` the moment POS-P1 calibration exists.** Do not use for any real changeover, scale-up, or launch decision.

Baseline (domain baseline `θ_i⁰(d)`, before the `κ/e/s` uplift of §2.6.3):

| Action class `a^commit` | `κ` band (illus.) | `θ_F` (illus.) | `θ_P` (illus.) | critical LCB `θ_ij^crit` (illus.) |
|---|---|---|---|---|
| Minor line changeover | 0.30 | 0.60 | 0.55 | 0.70 |
| Capacity scale-up | 0.65 | 0.72 | 0.68 | 0.80 |
| New-product launch (safety-relevant) | 0.85 | 0.80 | 0.75 | 0.90 |

Applied through the calibration-candidate family (a family to *test*, not a law):

```
θ_i(a,d,s) = clip_[0,1]( θ_i⁰(d) + β_i·κ(a) + γ_i·e(a) + η_i·s ) ,   i ∈ {F,P}
             β_i, γ_i, η_i ≥ 0   →   ∂θ_i/∂κ ≥ 0, ∂θ_i/∂e ≥ 0, ∂θ_i/∂s ≥ 0
```

Read against a **lower confidence bound**, never a point estimate:

```
LCB_(1−α)(X_t|a) = mean[X_t(a)] − z_(1−α)·SE[X_t(a)] ,   X ∈ {F,P}
```

**Coverage discipline (multi-component).** `SCALAR_LCB` gives only **per-component** `(1−α)` coverage. For a pillar built from `m` critical components, joint coverage is only `≥ 1 − ∑_j α_j` (union bound). For a *joint* `(1−α)` meaning across the critical set, use **Bonferroni** `α_j = α/m` per component, or escalate to **JOINT_CHANCE / DRO**. **Record which was used** in the compliance publication. (Illustrative default: Bonferroni `α/m`, `α = 0.05`.)

#### (K) — Irreversibility `κ` and exposure `e`

`κ(a) ∈ [0,1]` is estimated from **recoverability** — retooling irreversibility plus teardown cost — not from how "big" the project feels:

```
κ(a) = clip_[0,1](  ω_1·(1 − recover_frac)
                  +  ω_2·(teardown_cost / project_cost)
                  +  ω_3·(specificity)  ) ,   ∑ω = 1, declared before use
```

- `recover_frac` = fraction of committed capital/tooling redeployable to the prior product/line if the move is aborted (jigs, dies, fixtures resold or reconfigured). Low redeployability → high `κ`.
- `teardown_cost / project_cost` = cost to reverse (rip-out, re-validate the old state, scrap WIP) as a share of the commit. High teardown → high `κ`.
- `specificity` = asset/process specialization (a single-purpose transfer line ≈ 1; a flexible cell ≈ 0.2).

Exposure `e(a) ∈ [0,1]` is the *breadth of the blast radius*, separate from irreversibility:

```
e(a) = clip_[0,1](  ν_1·(affected_capacity / total_capacity)
                  +  ν_2·(customers_on_line / customers_total)
                  +  ν_3·(safety_population_at_risk_norm)  ) ,   ∑ν = 1
```

A change touching one non-safety cell serving one customer is low-`e`; a plant-wide scale-up feeding regulated end-markets is high-`e`. Both `κ` and `e` raise the readiness bar (never waive it): high irreversibility is exactly what *demands* stronger evidence.

#### (L, V) — Values / legal / safety firewall instantiation (dominates every readiness result)

The firewall is checked **first** and **dominates**: no `R`, no `κ`, no order-book urgency authorizes a firewall-barred action.

```
Firewall(a) = PASS  ⇔  worker_safety(a)=OK  ∧  environmental(a)=OK  ∧  product_safety(a)=OK
```

| Firewall clause (domain instantiation) | Barred unless… |
|---|---|
| **Worker safety** (e.g. OSHA / machine-guarding / LOTO / PSM) | HAZOP/PHA closed, guarding & interlocks verified, LOTO procedures in place for the new config |
| **Environmental permits** (air/water/waste, emissions caps) | permit valid **for the new operating state** (`z_P,perm` structural — a lapsed permit is a hard zero, not a low score) |
| **Product-safety regulation** (sector regs, recalls, labeling) | regulatory clearance + PPAP/first-article for the new SKU obtained |

**Critical-component veto (fix 2) — makes non-compensation (POS-F2) an actual theorem here.** The readiness authorization is *not* a bare `R ≥ 1`; it conjoins the per-pillar critical veto:

```
H_i = 1[ ∀ critical j :  LCB(z_ij) ≥ θ_ij^crit ]          (critical components of pillar i)

G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i        ( equivalently  min_i PillarReady_i )
```

A **single** failed safety-critical qualification (e.g. `z_F,pq` below its critical LCB, or `z_P,reg = 0`) sets its `H_i = 0` and **vetoes** the commit — it cannot be averaged away by strong maintenance or a full order book. Only with the veto wired in is "critical non-compensation" a theorem rather than a hope.

**Full gate (firewall-dominant, veto-wired):**

```
G_POS(a,t) = 1[ Firewall(a)=PASS ]
           · [  1[κ(a) ≤ κ_probe]                              (reversible pilot/prep → capped)
              ∨ ( 1[R_rob(a,t) ≥ 1] · ∏_i H_i )                (prepared + critical-clear → commit)
              ∨ ( 1[M_emg(a,t) > 0] · 1[a = a^emg] · Log ) ]   (forced move → logged)
```

**Stopping time (fix 3).** `τ_POS` is a **one-step-lookahead commitment heuristic**, *not* claimed optimal (an optimal wait/commit rule would require the Snell-envelope `V_wait`). It is defined as a `min`, never accumulated:

```
τ_ready = inf{ t : Firewall=PASS ∧ (R_rob ≥ 1) ∧ ∏_i H_i = 1 }
τ_emg   = inf{ t : G_emg = 1 }
τ_POS  := min( τ_ready , τ_emg )      # one-step-lookahead heuristic; never  τ_POS += …
```

#### (C) — One worked mini-example — **illustrative / RUO, ZERO decision authority**

*Candidate `a^commit`: scale up Line 3 to 2× throughput for a safety-relevant SKU.* Stakes `s = 0.7`, exposure `e = 0.6`, `κ = 0.65` (single-purpose transfer line, low redeployability, high teardown). All numbers illustrative.

Measured pillar LCBs (Bonferroni `α/m`, one-sided):

| Pillar | LCB(pillar) | θ_i(a,d,s) (illus.) | ratio |
|---|---|---|---|
| `F` | 0.78 | 0.72 | 1.083 |
| `P` | 0.71 | 0.68 | 1.044 |

Naïvely `R_rob = min(1.083, 1.044) = 1.044 ≥ 1` — looks like a pass. **But** the critical veto:

| Critical component | LCB(z) | θ_ij^crit (illus.) | H contribution |
|---|---|---|---|
| `z_F,pq` (PQ stage) | 0.88 | 0.80 | ✓ |
| `z_F,skill` (operators certified) | 0.82 | 0.80 | ✓ |
| `z_F,cpk` (CTQ capability) | 0.83 | 0.80 | ✓ |
| `z_P,perm` (env. permit, new state) | 0.83 | 0.90 | ✗ |
| `z_P,reg` (product-safety clearance) | 0.85 | 0.90 | ✓* |
| `z_P,src` (2nd-source critical BOM) | 0.86 | 0.80 | ✓ |

`H_P = 0` because `LCB(z_P,perm) = 0.83 < 0.90`: the environmental permit for the doubled-throughput state is **not** confirmed to standard. Therefore:

```
G_ready = 1[R_rob ≥ 1] · H_F · H_P = 1 · 1 · 0 = 0
```

**Verdict: readiness-forbidden — the Forbidden Action.** Despite `R_rob ≥ 1`, the single unmet safety-critical component vetoes; strong Form does not compensate. (Had the permit been *lapsed* rather than merely below-LCB, `z_P,perm = 0` → `P = 0` structurally, same refusal by the zero-clamp.)

**`a^prep` alternative (ungated, low-`κ`):** run Line 3 at 2× on a **time-boxed pilot campaign under the existing permit envelope** while (i) filing the permit amendment for the new operating state and (ii) completing the confirmatory emissions test. These are reversible (`κ ≤ κ_probe`), build `z_P,perm` toward its critical LCB, and re-open the gate legitimately once `H_P = 1`. The bottleneck `b(a,t) = P` (permit) points the prep effort precisely.

#### (V) — One-line mapping to the 16-point compliance standard

This adapter must **publish**: (1) the F/P/A indicator set with units/direction/crit-flags; (2) fixed normalization anchors `x_floor/x_target`; (3) the geometric `G_i` with its structural-zero hard-clamp rule and ε-scope statement; (4) `θ_i⁰(d)`, `θ_ij^crit`, and the `θ_i(a,d,s)` coefficients `β_i,γ_i,η_i` (all flagged illustrative-until-POS-P1); (5) the `κ` and `e` estimators with weights `ω,ν`; (6) the `α`, uncertainty model, and **coverage method used** (Bonferroni `α/m` vs JOINT_CHANCE/DRO); (7) the firewall clause map (OSHA / environmental / product-safety) with its dominance rule; (8) the critical-veto wiring `G_ready = 1[R_rob ≥ 1]·∏_i H_i`; (9) `τ_POS := min(τ_ready, τ_emg)` labeled a one-step-lookahead heuristic; (10) the loss scales for `M_emg`; (11) every `a^emg` forced-move log; (12) the `V_POS` audit trail; (13) the SSS-Guard independent-metric cross-check on irreversible verdicts; (14) the base-burn comparator design for POS-P2; (15) the equal-budget accounting for POS-P1; and (16) the standing epistemic label — **L2/B2 candidate, RUO, ZERO decision authority, decisive arbiter = unrun POS-P1/POS-P2.**

### Adapter — Government administration (public programmes, reforms, procurement)

> **Epistemic status.** Everything below is an **L2/B2 candidate operationalization**, not a validated law and not a theorem of `U = ∛(F·P·A)`. Every number is **illustrative — ZERO decision authority** and **research-use-only (RUO)**. The decisive arbiter is the *unrun* calibration test **POS-P1 / POS-P2**. A formula makes a claim inspectable; it does not make it true. This adapter instantiates the Domain Adapter Contract `DA_d = (Ψ, N, G, Θ, K, L, C, V)` for `d = gov`.
>
> **Invariant preserved:** Form ↔ Time · Position ↔ Space · Action ↔ Energy. In this domain: **Form** = institutional capacity built *over time*; **Position** = legitimacy and legal standing occupying a *political-constitutional space*; **Action** = delivery *energy* spent to execute.

---

#### 1. F/P/A indicator table — Ψ (indicators) with units and direction

`Ψ_gov` maps observable administration signals to the three pillars. Direction is one of **higher-better**, **lower-better**, or **target-band**. Critical indicators (marked ⚠) are subject to the non-compensatory veto `H_i` of §2 — a shortfall on a ⚠ indicator cannot be bought back by surplus elsewhere.

**F — Institutional capacity / competence / administrative readiness** (↔ Time)

| ID | Indicator | Unit | Direction | Crit |
|---|---|---|---|---|
| F1 | Staffing adequacy (filled vs. required FTE for the programme) | ratio [0,1] | higher-better | |
| F2 | Relevant skills coverage (staff certified/trained for the mandate) | % of roles | higher-better | |
| F3 | Prior delivery track record (share of comparable programmes hitting milestones) | % | higher-better | |
| F4 | Data & IT system readiness (systems live, tested, interoperable) | ordinal 0–4 → [0,1] | higher-better | ⚠ |
| F5 | Budget execution capacity (historical absorption rate of allocated funds) | % of allocation spent as planned | target-band 0.85–1.00 | |
| F6 | Process maturity (documented, audited SOPs for the programme) | ordinal 0–5 → [0,1] | higher-better | |
| F7 | Administrative error/rework rate (baseline caseload) | errors / 1000 cases | lower-better | |

**P — Legitimacy / coalition / legal & constitutional position / timing** (↔ Space)

| ID | Indicator | Unit | Direction | Crit |
|---|---|---|---|---|
| P1 | Legal/constitutional basis secured (enabling act, vires confirmed) | ordinal 0–3 → [0,1] | higher-better | ⚠ |
| P2 | Legislative/coalition support margin | votes secured − votes needed, normalized | higher-better | |
| P3 | Stakeholder alignment (signed-off key stakeholders / total) | % | higher-better | |
| P4 | Public legitimacy / trust for this mandate | survey index [0,1] | higher-better | |
| P5 | Timing/window fit (electoral, fiscal, calendar risk) | ordinal window-risk 0–3 → [0,1] inv. | higher-better | |
| P6 | Fiscal headroom (secured, ring-fenced funding vs. lifecycle cost) | % funded | target-band 0.90–1.10 | ⚠ |
| P7 | Judicial/legal-challenge exposure (pending or credible challenges) | count, weighted | lower-better | |

**A — Implementation & delivery capacity** (↔ Energy)

| ID | Indicator | Unit | Direction | Crit |
|---|---|---|---|---|
| A1 | Delivery plan completeness (WBS, milestones, dependencies mapped) | ordinal 0–5 → [0,1] | higher-better | |
| A2 | Procurement/contracting readiness (compliant pipeline in place) | ordinal 0–4 → [0,1] | higher-better | ⚠ |
| A3 | Supplier/market capacity (qualified bidders available) | count → normalized | higher-better | |
| A4 | Pilot evidence (pilots run, success rate) | % of pilots meeting target | higher-better | |
| A5 | Change-management & frontline readiness (trained delivery staff) | % ready | higher-better | |
| A6 | Monitoring & abort capability (live M&E, kill-switch defined) | ordinal 0–3 → [0,1] | higher-better | ⚠ |

> Note: **A is diagnosed and reported but is NOT a POS gate input.** POS gates on **Form-then-Position readiness only** (Gates 1–2); A informs the delivery plan and the abort discipline downstream. This adapter keeps A visible so the compliance publication (§7) is complete.

---

#### 2. Normalization notes — N, and the aggregators G

**Per-indicator normalization `N`.** Each raw indicator `x` is mapped to `z ∈ [0,1]`:

```
higher-better :  z = clip_[0,1]( (x − x_lo) / (x_hi − x_lo) )
lower-better  :  z = clip_[0,1]( (x_hi − x) / (x_hi − x_lo) )
target-band   :  z = 1 − clip_[0,1]( dist(x, [b_lo, b_hi]) / w_band )   (1 inside band, decays outside)
ordinal k/K   :  z = k / K
```

Anchors `(x_lo, x_hi, band, w_band)` are **declared before scoring** and published (SIGMA-style transparency, RUO — not a governance mandate).

**Pillar sub-aggregation `G_i` — geometric, with a HARD zero-clamp (Fix 1).** Within each pillar, indicators combine geometrically so that a true structural zero (e.g. *no legal basis*, `P1 = 0`) drives the pillar to exactly 0 — no averaging can rescue it:

```
G_i(z) = ∏_j z_j^(w_ij) ,   Σ_j w_ij = 1 ,   w_ij ≥ 0        (i ∈ {F, P, A})
```

A log form may be used **only** for numerical stability on **strictly-positive noisy measurements**:

```
G_i(z) = exp( Σ_j w_ij · log(z_j + ε) )        ε > 0, ONLY to avoid −∞ on strictly-positive z_j
```

> **ε rule (load-bearing).** `ε` exists solely to avoid `−∞` when a *measured, strictly-positive* value is tiny and noisy. `ε` **must NEVER convert a true/structural zero into a passing score.** Whenever any component is a genuine structural zero (legal basis absent, funding unsecured, no procurement pipeline), `G_i` is **HARD-CLAMPED to 0**:
>
> ```
> if any structural_zero(z_j):  G_i(z) := 0        # dominates the ε-log form
> ```

**Pillar scores fed to the gate.** `F = G_F(z_F)`, `P = G_P(z_P)` (both in `[0,1]`), read at their **lower confidence bounds** `LCB(F|a)`, `LCB(P|a)` per the confidence standard below — never point estimates.

**Joint-coverage note (which multiple-comparison rule was used).** `SCALAR_LCB` gives only **per-component** `(1−α)` coverage. For a pillar built from `m` indicator LCBs, the *joint* coverage is only `≥ 1 − Σ_j α_j` (union bound). To assert a **joint `1−α`** readiness statement, either apply **Bonferroni** (`α_j = α/m`) or escalate to **JOINT_CHANCE / DRO**. This adapter's default: **Bonferroni per pillar**, and the publication (§7) must **record which rule was used**.

---

#### 3. Illustrative readiness thresholds θ_F / θ_P — Θ

> **ILLUSTRATIVE — ZERO decision authority — RUO.** These placeholders exist only to make the mechanism concrete. They are **superseded the moment POS-P1 calibration exists**. Do not use for any live authorization.

Threshold family (from APPENDIX_POS §2.6.3), instantiated for `d = gov`:

```
θ_i(a, gov, s) = clip_[0,1]( θ_i⁰(gov) + β_i·κ(a) + γ_i·e(a) + η_i·s ) ,   i ∈ {F, P}
```

| Symbol | Illustrative value | Meaning |
|---|---|---|
| `θ_F⁰(gov)` | 0.60 | Form baseline for government commitments |
| `θ_P⁰(gov)` | 0.55 | Position baseline |
| `β_F, β_P` | 0.15, 0.20 | irreversibility loading (Position loads harder — political lock-in) |
| `γ_F, γ_P` | 0.10, 0.10 | exposure loading |
| `η_F, η_P` | 0.10, 0.10 | stakes loading |
| `κ_probe` | 0.20 | at/below this, actions flow ungated (pilots, consultations) |

Illustrative resulting bar for a high-stakes irreversible reform (`κ=0.9, e=0.8, s=0.9`): `θ_F ≈ clip(0.60+0.135+0.08+0.09)=0.905`, `θ_P ≈ clip(0.55+0.18+0.08+0.09)=0.90`. **(illustrative — ZERO decision authority — RUO.)** Critical-infrastructure-grade programmes sit at the high end, consistent with the SSS ≥ 0.75 scale band (cited for scale only, no independent authority).

**Critical-veto thresholds `θ_ij^crit`** apply per ⚠ indicator (§Fix 2 wiring below), e.g. illustratively `LCB(P1) ≥ 0.99` (legal basis effectively confirmed), `LCB(P6) ≥ 0.90` (funding secured), `LCB(A2) ≥ 0.75` (procurement pipeline compliant). **(illustrative — ZERO decision authority — RUO.)**

---

#### 4. Estimating κ (irreversibility via recoverability) and exposure e — K

**Irreversibility `κ(a) ∈ [0,1]`** is estimated from **recoverability**: how much of the consumed resource, option, and standing returns, and on what timescale, if the action must be unwound.

```
κ(a) = clip_[0,1]( 1 − Recoverability(a) )

Recoverability(a) = Σ_r ω_r · recover_r(a) ,   Σ_r ω_r = 1
```

with recoverability sub-factors (each in `[0,1]`, `1` = fully recoverable):

| Sub-factor `recover_r` | What it measures (gov) | Low recoverability (κ↑) example |
|---|---|---|
| Legal/statutory reversibility | can the enabling law/contract be undone? | primary legislation, treaty commitment |
| Financial recoverability | sunk cost recoverable? | non-refundable capital build, paid grants |
| Contractual lock-in | exit/termination cost of procurement | long PPP/PFI, single-vendor lock-in |
| Political/reputational | is standing recoverable after reversal? | flagship reform whose failure discredits the institution |
| Beneficiary/social lock-in | can service changes be rolled back? | benefits already disbursed, entitlements created |

> **Political/legal irreversibility & lock-in** enter through the legal, contractual, and political sub-factors — a reform enacted in primary legislation with a signed multi-year PPP and a public flagship framing has κ → 1 even if the cash outlay is modest.

**Exposure `e(a) ∈ [0,1]`** (separate from κ — *how much is at stake*, not *how irreversible*):

```
e(a) = clip_[0,1]( w1·Reach + w2·BudgetShare + w3·Duration + w4·RightsImpact )
```

where **Reach** = citizens/entities affected ÷ population; **BudgetShare** = programme cost ÷ relevant departmental budget; **Duration** = normalized commitment horizon; **RightsImpact** = severity of impact on individual rights/entitlements. Weights `w1..w4` declared before scoring.

---

#### 5. Values / legal / safety firewall — V (dominates every readiness result)

The firewall is checked **first** and **dominates**: no `R(a,t)`, `κ`, or margin, however favorable, authorizes an action the firewall bars (APPENDIX_POS §7). `Firewall_gov(a) ∈ {PASS, FAIL}`; any FAIL ⇒ `G_POS = 0` categorically, and a FAIL is **never** folded into the audit severity `V_POS`.

| Firewall gate | Constraint (illustrative instantiation) | FAIL condition |
|---|---|---|
| Constitutional / vires | action within constitutional powers and enabling legislation | acting ultra vires, or absent legal basis |
| Data protection | GDPR / national data-protection law; DPIA completed where required | processing personal data without lawful basis or DPIA |
| Procurement law | national/EU public-procurement rules, open & fair competition | uncompetitive award, undisclosed conflict, threshold breach |
| Anti-corruption | conflict-of-interest, transparency, beneficial-ownership rules | undeclared COI, opaque beneficial ownership |
| Fundamental rights / equality | non-discrimination, equality-impact assessment | disproportionate rights impact without justification |
| Fiscal legality | authorized appropriation exists | spending without lawful appropriation |

> **Natural fit, kept RUO.** A public **U-Score / registry** and **SIGMA-style transparency** systems are a natural home for publishing this firewall register, the Ψ anchors, and the θ/κ/e declarations — making each commitment *inspectable*. This is a **research-use-only** affordance, **not** a governance mandate: publishing a score does not confer decision authority, and the firewall — not the score — bars values-forbidden action.

---

#### 6. Worked mini-example — running a candidate `a^commit` through the gate

> **All numbers illustrative — ZERO decision authority — RUO.** Purpose: show the wiring, not to authorize anything.

**Candidate `a^commit`:** launch a nationwide digital benefits-administration reform via a single 7-year PPP contract, going live for all claimants at once (no phased rollout).

**Firewall (V) — checked first.** Legal basis: enabling act passed (PASS). DPIA: **not yet completed** for the new data-sharing → **data-protection gate FAIL**.

**Verdict path A (as-is): Firewall = FAIL ⇒ `G_POS = 0` categorically.** No readiness computation can override this. Stop.

*To show the readiness gate, suppose the DPIA is completed so Firewall = PASS, and evaluate readiness:*

**Inputs (illustrative).** `κ(a) ≈ 0.9` (primary legislation + 7-year PPP lock-in + flagship standing → low recoverability). `e(a) ≈ 0.8` (whole claimant population, large budget share, rights impact). `s = 0.9`.

Illustrative thresholds from §3: `θ_F ≈ 0.905`, `θ_P ≈ 0.90`.

Measured pillars at Bonferroni-adjusted LCB:

```
LCB(F|a) = 0.72     (F4 IT-system readiness weak — systems not fully tested)
LCB(P|a) = 0.83

R(a,t) = min( 0.72/0.905 , 0.83/0.90 ) = min( 0.796 , 0.922 ) = 0.796   < 1
m_R = R − 1 = −0.204      bottleneck b = F
```

**Critical veto (Fix 2 — wired into readiness authorization):**

```
H_i = 1[ ∀ critical j in pillar i : LCB(z_ij) ≥ θ_ij^crit ]
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i        (equivalently min_i PillarReady_i)
```

Here `LCB(A2)` procurement-pipeline readiness = 0.68 < `θ^crit`=0.75 → `H_A = 0`. Even if `R ≥ 1` had held, `G_ready = … · 0 = 0`. This is why **critical non-compensation (POS-F2) is an actual theorem** of the gate, not a hope: a single failed critical indicator zeroes authorization regardless of surplus elsewhere.

**Readiness verdict:** `R = 0.796 < 1` **and** `H_A = 0` ⇒ **`G_ready = 0` — readiness-forbidden (the Forbidden Action).** Committing now would burn the base: a failed flagship reform degrades institutional Form and burns Position (legitimacy), per APPENDIX_POS §3.1.

Audit severity (not a second gate): `V_POS = s·κ·[1−R]_+ = 0.9·0.9·0.204 ≈ 0.165`.

**`a^prep` alternative (ungated, low-κ, flows freely):**
- Run a **regional pilot** of the digital system (`κ ≈ 0.15 < κ_probe`) → lifts F4 (IT readiness) and A4 (pilot evidence).
- Complete the **DPIA** and a **competitive, modular procurement** with multiple qualified suppliers (raises A2 above `θ^crit`, reduces lock-in κ).
- **Phase the rollout** (cohort-by-cohort), which lowers `κ` and `e` of the eventual commit and preserves an abort path (A6).

These preparatory moves clear the critical veto and raise `LCB(F)` above `θ_F` **before** any irreversible commitment — turning a Forbidden Action into a sequenced, low-blood one.

**Stopping time (Fix 3 — heuristic, not claimed optimal):**

```
τ_ready = inf{ t : G_ready(a,t) = 1 }
τ_emg   = inf{ t : G_emg(a,t)   = 1 }
τ_POS  := min( τ_ready , τ_emg )      # one-step-lookahead commitment heuristic
```

`τ_POS` is a **one-step-lookahead commitment heuristic**, **not** an optimal stopping rule. For an optimality claim, define `V_wait` via the Snell envelope and solve the optimal-stopping problem explicitly. We do **not** write `τ_POS += …`.

---

#### 7. Mapping to the 16-point compliance standard — C (what this adapter must publish)

> One line per the contract: **This gov adapter must publish, for every gated commitment** — (1) domain id `d=gov` & profile POS; (2) the `Ψ_gov` indicator set with units/direction; (3) the `N` normalization anchors; (4) the `G_i` geometric aggregators **with the hard zero-clamp and the ε-scope statement**; (5) illustrative `Θ` = θ_F⁰/θ_P⁰ + β/γ/η coefficients marked **ZERO decision authority / RUO**; (6) the `θ_ij^crit` critical thresholds and the ⚠ critical-indicator list; (7) the `K` estimation of `κ` (recoverability sub-factors) and `e` (exposure); (8) the confidence standard `α(s)` and estimator, declared **before** gate evaluation; (9) **which multiple-comparison rule** was used (Bonferroni `α/m` by default, else JOINT_CHANCE/DRO); (10) the veto-wired readiness `G_ready = 1[R_rob≥1]·∏_i H_i`; (11) the firewall register `V` (constitutional, GDPR/DPIA, procurement, anti-corruption, rights, fiscal-legality) with each verdict; (12) the readiness ratio `R`, margin `m_R`, and bottleneck `b`; (13) the audit severity `V_POS` and every `a^emg` forced-move log; (14) the `a^prep` alternative when a commit is refused; (15) the stopping rule labelled `τ_POS` as a **one-step-lookahead heuristic** (not optimal); (16) the epistemic banner — **L2/B2 candidate, RUO, decisive arbiter = unrun POS-P1/POS-P2** — plus the SSS-Guard independent cross-check on any irreversible verdict. Publication venue: a public U-Score/registry / SIGMA-style transparency layer (**RUO, not a governance mandate**).

### Adapter — Military-space agencies (missions, launch, aerospace)

> **Status.** L2/B2 candidate operationalization of the POS commitment gate on `domain d = aerospace.mission_commit`, riding on the TRA registration (`APPENDIX_TRA`, `aerospace.launch_vehicle`). It is **not** a validated law, **not** a theorem of `U = ∛(F·P·A)`, **not** a flight controller, and **not** admissible in any safety-of-flight, abort, range-safety, or certification loop. It is a **design-review / mission-readiness-review diagnostic over declared, logged, or simulated states**. The decisive arbiter is the **unrun** calibration test **POS-P1 / POS-P2**. A formula makes a claim inspectable; it does not make it true. **Research-use-only (RUO).**
>
> **Invariant carried verbatim:** **Form ↔ Time · Position ↔ Space · Action ↔ Energy.** Form = the vehicle/system geometry that must persist *through* the burn; Position = the point in the gravitational-atmospheric field *in space*; Action = the thrust/control/*energy* release that flies it. The mirror is forbidden.
>
> **⛔ HARD DUAL-USE FIREWALL (read before anything below; carried in spirit from `APPENDIX_TRA` §5, never gated, never retired).** A launch vehicle and a ballistic missile are the same physics; a "weakest-pillar, cheapest-fix" readiness engine is, sign-flipped, a destabilizer/target-finder for a third party's vehicle. This adapter optimizes **stabilize-polarity, own-vehicle, safety-of-flight readiness ONLY**, on states declared by a **named, accountable human**. **Weaponization, targeting, guidance tuning for weapons delivery, range/payload/yield trades for warheads, interception/spoofing/destabilization of any third-party vehicle, and operationally hazardous specifics (propellant formulation/synthesis, illicit-system tuning, quantities, scale-up) are TYPE-FORBIDDEN and are never produced — whether or not any readiness result or falsifier passes.** This is a policy-and-accountability boundary, not a mathematical impossibility; it **aligns with but does NOT substitute for MTCR / Wassenaar / national export-control law**, which govern directly. **The values-firewall dominates every readiness result on this page: no `R`, no `κ`, no margin, however favorable, authorizes a firewall-forbidden action.**

---

#### (1) Ψ — the F/P/A indicator set (units + direction)

Each indicator is mapped to a normalized pillar-input `z_j ∈ [0,1]` under the calibrated "probability the requirement is met over the stated phase horizon" semantics inherited from `APPENDIX_TRA` (★★ measurement contract). "Direction" is the *raw* sense before normalization; every normalized `z_j` is **higher-is-readier**.

**Form (F ↔ Time) — vehicle/system structural integrity & qualification**

| Indicator | Symbol | Raw unit | Raw direction | Normalized `z_j` |
|---|---|---|---|---|
| Structural margin of safety (primary load path, max-Q + landing-burn line-load) | z_F1 | MoS (dimensionless) | higher | P(shell/thrust-structure allowable retained) |
| Qualification / test coverage vs. flight envelope | z_F2 | % of qual envelope demonstrated | higher | fraction of envelope with passed qual |
| Thermal-protection & nozzle-throat integrity margin | z_F3 | recession margin (mm) / A* fidelity | higher | P(TPS + throat hold through phase) |
| Open critical NCRs / waivers on structure | z_F4 | count | lower | 1 − (weighted open-critical fraction) |
| Mass-properties fidelity (CG, MOI, bending-mode) vs. model | z_F5 | σ deviation | target-band | P(CG/modes inside qualified box) |

**Position (P ↔ Space) — trajectory / mission window / orbital & environmental context**

| Indicator | Symbol | Raw unit | Raw direction | Normalized `z_j` |
|---|---|---|---|---|
| Corridor margin (state inside survivable trajectory corridor) | z_P1 | σ to corridor edge | higher | P(state inside corridor through phase) |
| Upper-level wind / shear & load-relief margin | z_P2 | q·α (Pa·rad) vs. limit | lower | P(q·α under structural limit) |
| Launch/injection window fit (phasing, lighting, conjunction/COLA) | z_P3 | s of open window / miss-distance (km) | higher / higher | P(window open ∧ COLA clear) |
| Range / airspace / maritime-clearance & weather constraints | z_P4 | Go/No-Go criteria met (%) | higher | fraction of range criteria GO |
| Ground-segment & landing-site context (pad, recovery footprint) | z_P5 | reachable-set margin | higher | P(viable footprint exists) |

**Action (A ↔ Energy) — propulsion / GNC / operations readiness**

| Indicator | Symbol | Raw unit | Raw direction | Normalized `z_j` |
|---|---|---|---|---|
| ΔV / propellant + landing-fuel reserve | z_A1 | m/s reserve above requirement | higher | P(ΔV + landing margin suffice) |
| Propulsion health (Pc, mixture ratio, combustion-acoustic margin, engine-out capability) | z_A2 | margin fraction | higher | P(thrust adequate incl. engine-out) |
| GNC / TVC control authority & closed-loop gain/phase margin | z_A3 | dB / deg margin | higher | P(control authority not saturated) |
| Flight-software / avionics & sensor-suite readiness | z_A4 | verified requirements (%) | higher | fraction of V&V complete |
| Ground ops, comms/uplink, tracking & console-poll readiness | z_A5 | GO polls / link margin (dB) | higher | P(ground segment ready) |

> **Cross-pillar confounds are real and named** (per `APPENDIX_TRA` §1.3): POGO, slosh, aeroservoelastic / control-structure interaction, static margin (F×P), and closed-loop margins (F×P×A) do **not** file cleanly to one bag. Separability here is a hypothesis under **POS-P0/TRA-P0**, not an assumption; when in doubt, a confounded item is scored as a **critical** indicator in the pillar where its *floor* binds and vetoed there (see the critical-veto below).

---

#### (2) N — normalization notes

- **One cardinal semantics.** Every `z_j` is a calibrated `[0,1]` "probability the requirement is met over the stated phase horizon," against a **frozen reference distribution** declared **before** the gate is evaluated (measurement contract, `APPENDIX_TRA` ★★). No post-hoc rescaling; `π* = argmin(F,P,A)` must be rescale-stable.
- **LCB, never point estimate.** The gate consumes a **lower confidence bound** `LCB_{1−α}(z_j)`, per POS §2.6.2, with `α = α(s)`, `dα/ds ≤ 0` — higher stakes demand a more conservative bound. Estimator and uncertainty model are declared pre-gate.
- **Joint coverage (load-bearing).** `SCALAR_LCB` gives only **per-component** `(1−α)` coverage. For `m` components the joint coverage is only `≥ 1 − ∑_j α_j` (union bound). For a genuine joint `1−α` readiness statement across a pillar's `m` indicators, use **Bonferroni** (`α_j = α/m`) or escalate to **JOINT_CHANCE / DRO**; **record which was used** in the readiness certificate. A crewed/high-`κ` commit defaults to Bonferroni or DRO, not per-component bounds.
- **Target-band indicators** (e.g. mass-properties `z_F5`, mixture ratio) normalize by distance-into-band, `z = P(value ∈ qualified band)`, not one-sided.
- **Direction unified.** After normalization every `z_j` is higher-is-readier so the sub-aggregators are monotone.

**G — pillar sub-aggregation (with the zero-clamp fix, mandatory).** Each pillar is a **geometric** sub-aggregate of its normalized indicators:

```
G_i(z) = ∏_j z_j^{w_ij} ,   ∑_j w_ij = 1 ,   w_ij ≥ 0 ,   i ∈ {F, P, A}
```

- A **true/structural zero maps to exactly 0**: `G_i` is **HARD-CLAMPED to 0** whenever any structural or true-zero component is present (a lost load path, a violated hard `Q`-limit, an engine-out beyond capability). This preserves zero-limit non-compensation — the one B1-robust claim.
- A log form `∑_j w_ij·log(z_j + ε)` may be used **only** for numerical `−∞` avoidance on **strictly-positive noisy measurements**. `ε` is a numerical guard **only**; it **must NEVER convert a true zero into a passing score**. If any component is a structural/true zero, the clamp overrides the log form and `G_i := 0`.

---

#### (3) Θ — ILLUSTRATIVE readiness-threshold set θ_F / θ_P

> **ILLUSTRATIVE — ZERO DECISION AUTHORITY — RUO.** Every number below is a placeholder to make the mechanism concrete. It is un-calibrated; the asymmetries are unjustified; it is **superseded the instant POS-P1 calibration exists**. Do not read scale, ranking, or a flight threshold into it. `φ⁻¹ = 0.618` is an inherited SSS placeholder with **no physical meaning for flight** (`APPENDIX_TRA` §2, minor-3).

Threshold family under test (POS §2.6.3), per pillar `i ∈ {F,P}`:

```
θ_i(a,d,s) = clip_[0,1]( θ_i⁰(d) + β_i·κ(a) + γ_i·e(a) + η_i·s ) ,   β_i,γ_i,η_i ≥ 0
```

| Mission class (illustrative) | s | θ_F⁰ | θ_P⁰ | θ_F(a,d,s) | θ_P(a,d,s) | confidence rule |
|---|---|---|---|---|---|---|
| Uncrewed tech-demo, recoverable | 0.4 | 0.55 | 0.50 | ≈ 0.70 | ≈ 0.65 | per-component `α=0.05` |
| Operational sat, single-launch value | 0.7 | 0.65 | 0.60 | ≈ 0.82 | ≈ 0.78 | Bonferroni `α/m` |
| Crewed / high-consequence irreversible phase | 0.95 | 0.75 | 0.72 | ≈ 0.92 | ≈ 0.90 | JOINT_CHANCE / DRO |

Intended monotonicity `∂θ_i/∂κ ≥ 0`, `∂θ_i/∂e ≥ 0`, `∂θ_i/∂s ≥ 0`: the more irreversible, exposed, or consequential the phase, the stronger the readiness evidence required. **A calibration candidate, not a validated law** — POS-P1 tests it against simpler and non-linear rivals, and against the "thresholds-without-order" and "order-without-gate" ablations.

---

#### (4) K — estimating κ (irreversibility, via recoverability) and exposure e

**κ from flight irreversibility.** Model `κ(a) ∈ [0,1]` as `1 − recoverability`, where recoverability is the fraction of committed resources/options/standing recoverable on a useful timescale after `a`:

```
κ(a) = 1 − R_rec(a) ,   R_rec(a) = w_rev·(recoverable ΔV/propellant + safe-abort availability)
                                  + w_state·(reversible state change)
                                  + w_asset·(hardware/mission recoverability)
```

| Mission phase (illustrative) | Recoverability picture | κ (illustrative) |
|---|---|---|
| Sim / model run, paper review | fully reversible | ≈ 0.00 |
| Wet dress rehearsal, tanking test | detank & recycle | ≈ 0.10 |
| Static fire (held-down) | vehicle retained, abort clean | ≈ 0.25 |
| Countdown inside recycle window | scrub still available | ≈ 0.45 |
| **Ignition / liftoff commit** | no re-stow; energy released | ≈ 0.97 |
| Staging / TLI / deorbit-burn commit | phase irreversible | ≈ 0.99 |

`a^commit` = launch / commit to an irreversible mission phase (`κ → 1`). `a^prep` = static fires, rehearsals, sims, load tests (low-`κ`, ungated *unless* a "preparation" is itself a large hard-to-reverse capital/commit-in-disguise, which then clears the gate). `a^probe` = capped-exposure tests. Landing-burn coupling (`APPENDIX_TRA` §2, §12): once committed, the landing burn is **Action-margin-bound** (near-depleted propellant → thin ΔV/throttle authority) and **Position-corridor-bound**, with Form loads already past their ascent/entry peak — so its `κ` is high and its binding pillar is expected in {A, P}, not F.

**Exposure e.** `e(a) ∈ [0,1]` is normalized **magnitude of what is put at risk**, kept **separate from κ** (POS §2.6.3): a function of crew presence, public overflight/casualty expectation, payload value/uniqueness, and third-party/environmental exposure, normalized against a declared reference. High `e` raises `θ` via `γ_i`; it does not, by itself, waive the gate.

---

#### (5) L + V — the values / legal / safety firewall instantiation (non-negotiable, dominates every result)

The firewall is checked **first** and **dominates** (POS §7, §2.6). Order of precedence on this domain:

1. **V — dual-use / values type-check.** Is `a` stabilize-polarity, own-vehicle, safety-of-flight, on a state declared by a named accountable human? If it is weaponization / targeting / third-party destabilization / hazardous-specifics → `Firewall(a) = FORBIDDEN`, output refused, **no readiness computed**. This is TYPE-forbidden and cannot be unlocked by any `R`, `κ`, stakes, or emergency.
2. **L — legal / regulatory floor.** MTCR / Wassenaar / national export-control, launch-license (e.g. national civil-launch authority), range-safety / flight-termination-system authority, orbital-debris & COLA regulation, crew-safety certification. This adapter **aligns with but never substitutes for** these; a legal No-Go is a hard stop the readiness gate cannot override.
3. **Safety hard constraints.** Hard `Q`-limits, minimum static margin, minimum landing-fuel reserve, FTS readiness — where flight safety is a *hard* constraint, `U`/`R` is the wrong object and the specialist constraint governs (`APPENDIX_TRA` §2, minor-1). These wire into the **critical-veto** below.
4. **Human-on-top.** No autonomous action, no live-loop authority; **SSS-Guard is scoped to simulation / design-review only — NO flight/abort/certification authority** (`APPENDIX_TRA` header correction).

**Critical-veto wiring (mandatory fix — makes critical non-compensation, POS-F2, an actual theorem).** Readiness is authorized only when the robust readiness ratio clears **and** every critical component clears its own critical floor:

```
G_ready = 1[ R_rob ≥ 1 ] · ∏_i H_i        ( equivalently  min_i PillarReady_i )

H_i     = 1[ ∀ critical j :  LCB(z_ij) ≥ θ_ij^crit ]        i ∈ {F, P, A}

R_rob   = min(  LCB(F|a)/θ_F(a,d,s) ,  LCB(P|a)/θ_P(a,d,s)  )   (LCBs under the declared joint-coverage rule)
```

`H_i` is the per-pillar critical-component conjunction (FTS, engine-out capability, corridor floor, structural hard-limit, COLA). A single critical component below its floor forces `H_i = 0` and vetoes authorization **regardless** of how high the aggregate `R_rob` is — no averaging past a dead-critical item. The full POS gate:

```
G_POS(a,t) = 1[ Firewall(a) = PASS ]
           · 1[  κ(a) ≤ κ_probe                                   (reversible probe/prep → capped exposure)
              ∨  G_ready(a,t) = 1                                 (prepared AND no critical veto → commit)
              ∨  ( M_emg(a,t) > 0  ∧  a = a^emg  ∧  Log=COMPLETE ) ] (forced move → logged, uncertainty-robust)
```

**Stopping time (mandatory fix — no false optimality claim).** The commit instant is a **one-step-lookahead commitment heuristic**, not a proven-optimal rule (for an optimal formulation, define `V_wait` via the Snell envelope):

```
τ_POS := min( τ_ready , τ_emg )
τ_ready = inf{ t : G_POS(a^commit, t) = 1  via the readiness branch }
τ_emg   = inf{ t : G_emg = 1 }
```

Never written as an accumulator; `τ_POS` is the first time either the readiness branch or the logged-emergency branch fires.

---

#### (6) Worked mini-example — a candidate `a^commit` through the gate

> **CONSISTENCY ILLUSTRATION ONLY — every number is an abstract placeholder, ZERO flight evidence, ZERO decision authority, RUO.** Not a launch recommendation.

**Candidate.** `a^commit` = ignition/liftoff commit of an operational single-launch payload. Stakes `s = 0.7`, exposure `e ≈ 0.6`, `κ ≈ 0.97`. Firewall: own-vehicle, stabilize-polarity, safety-of-flight, named accountable launch director → `Firewall = PASS`, `κ > κ_probe` so the readiness branch must carry it. Thresholds (illustrative row 2): `θ_F ≈ 0.82`, `θ_P ≈ 0.78`. Coverage rule: Bonferroni.

**State R (illustrative LCBs after Bonferroni correction).**

```
LCB(F|a) = 0.86   →  F ratio = 0.86 / 0.82 = 1.05     (clears)
LCB(P|a) = 0.61   →  P ratio = 0.61 / 0.78 = 0.78     (fails — bottleneck)
R_rob    = min(1.05, 0.78) = 0.78    →   R_rob < 1

Critical check:
  H_F = 1  (all critical structural items ≥ floor)
  H_A = 1  (engine-out capability, ΔV reserve ≥ floor)
  H_P = 0  (critical z_P2 upper-level wind/load-relief:
            LCB(q·α) = 0.60 < θ^crit = 0.80  → veto)

G_ready = 1[0.78 ≥ 1] · H_F·H_P·H_A = 0 · (1·0·1) = 0
```

**Verdict.** `G_POS = 0` — **readiness-forbidden** (the Forbidden Action). Two independent reasons, either sufficient: (a) `R_rob = 0.78 < 1`, and (b) the Position critical-veto `H_P = 0` (wind/load-relief below its hard floor) — so even a favorable aggregate could not authorize. Active bottleneck `b = Position`. Violation severity for audit: `V_POS = s·κ·[1−R]_+ = 0.7·0.97·0.22 ≈ 0.15` (audit measure, not a second gate). Because `A` is high and `F` clears, the naïve "engine's ready, thrust looks great, just go" reading is exactly inverted — high `κ` **raises** the bar, never waives it.

**`a^prep` alternative (ungated, low-`κ`).** Hold in the recycle window (κ ≈ 0.45, still recoverable) and route preparatory effort at the Position bottleneck: re-poll the upper-level wind sounding / balloon data, run the day-of-launch load-relief trajectory reshape and steering-update, re-assess the window/COLA, and re-run the readiness gate. If the wind LCB recovers to `LCB(P|a) ≥ 0.78` with `H_P = 1`, `R_rob ≥ 1`, `G_ready = 1`, then `τ_ready` fires and the commit is authorized *on a prepared base*. If the window closes first, **scrub** — a logged, reversible `a^prep`, base intact, `ℳ`-growth preserved for the next attempt. No relabeling of a failed commit as a "probe" after the fact.

---

#### (7) C — one-line mapping to the 16-point compliance standard

**What this adapter must publish (all 16, RUO, before any use):** (1) domain path & DA contract `(Ψ,N,G,Θ,K,L,C,V)`; (2) frozen Ψ indicator set with units/direction; (3) normalization + reference distributions declared pre-gate; (4) LCB estimator, `α(s)`, and **joint-coverage rule used (per-component / Bonferroni / JOINT_CHANCE / DRO)**; (5) geometric sub-aggregator `G_i` with the **true-zero HARD-CLAMP** and the `ε`-is-numerical-only caveat; (6) `θ_i(a,d,s)` family + illustrative values flagged **ZERO decision authority**; (7) `κ` (recoverability) and `e` estimation tables; (8) critical-component list + critical floors `θ_ij^crit`; (9) **critical-veto** `G_ready = 1[R_rob≥1]·∏_i H_i`; (10) full gate `G_POS` incl. emergency branch with `M_emg`/log; (11) `τ_POS` as **one-step-lookahead heuristic** (or Snell-envelope `V_wait`); (12) `V_POS` audit measure + every `a^emg` logged; (13) **HARD DUAL-USE FIREWALL** (type-forbidden list) + MTCR/Wassenaar/export-control & launch-license alignment; (14) human-on-top / SSS-Guard **design-review-only, no flight authority** declaration; (15) POS-P1/POS-P2 (+ TRA-P0/P1) preregistration status and KILL bands; (16) epistemic banner: **L2/B2 candidate operationalization, RUO, ZERO decision authority, decisive arbiter is the unrun POS-P1/POS-P2** — a formula makes a claim inspectable, not true.


---

## Epistemic guardrail & honest scope

This profile makes the POS commitment engine **inspectable**. It does not make it **validated** — and the distinction is the whole point.

- **Formalization ≠ validation.** Writing `D_d`, `DA_d`, the geometric sub-aggregator, `R_rob`, `G_POS`, and `τ_POS` down precisely means their claims can now be *checked, attacked, and falsified*. It does **not** mean they are true. A formula exposes a claim to scrutiny; it does not earn the claim. The within-model properties of §10 (POS-F1…F8) are propositions **true inside the kernel's own definitions** — statements that the machinery does what its symbols say — and are explicitly **not** empirical proofs that the gate pays in the world.

- **Everything here is an L2/B2 candidate operationalization.** Nothing in this document is a validated law, and nothing is a theorem of `U = ∛(F·P·A)`. The geometric forms *echo* the keystone's non-compensation one level down; they do **not** derive the gate from it. Every weight `w_ij`, threshold `θ_F / θ_P / θ_ij^crit`, guard `ε`, confidence level `α(s)`, probe cap `κ_probe / e_cap`, horizon, loss scale, and multiplier `λ_•` in the kernel or in any adapter is **illustrative — ZERO decision authority — research-use-only (RUO)**, and is superseded the instant a calibrated value exists. No number in this profile may be used to authorize any real commitment in any domain.

- **The decisive arbiter is the unrun POS-P1 / POS-P2.** Until the pre-registered falsifiers report, the engine is **scaffolding**. **POS-P1** asks whether readiness-gated commitment beats its baselines (ungated, AD-RTD-alone, weakest-pillar greedy, expert policy, explore-then-commit, and the isolating ablations) at *equal total budget* on *external* outcomes — never on an internal quantity computed from the same F/P/A estimates the gate consumes. **POS-P2** asks, causally, whether a premature commitment actually burns the base (`ΔB > 0`). `PASS` requires `LCB95(effect) > Δ_min`; `KILL` if `UCB95(effect) < 0` (the gate *harms*); otherwise `INCONCLUSIVE`. No formula above overrides that unrun test.

- **Illustrative numbers carry zero decision authority.** Every worked example — the research clinical-imaging launch, the flagship LBO, the factory scale-up, and their aerospace and military-space counterparts — is a *mechanism demonstration*. Its arithmetic shows how the gate would compute a verdict; it asserts nothing about any real decision. Treat every figure as a placeholder awaiting calibration.

- **The military-space / dual-use firewall is non-negotiable.** The values/legal/safety firewall `C_firewall` is a *dominating multiplicative factor*: a `FAIL` clamps `G_POS = 0` no matter how high the readiness, how low the irreversibility, or how large the emergency margin (POS-F1). This is structural, not weighted, and it is **absolute** at the dual-use boundary. Sequencing can unlock a *hard* action; it can **never** legitimize a *wrong*, *infeasible*, or *weaponizable-prohibited* one. No adapter — least of all the aerospace or military-space adapter — may fold a firewall failure into a readiness score, trade it against outcome, or route it to preparation. There is no readiness surplus, no calibration, and no emergency that buys past this line.

---

## References

- **Parent record (DOI):** `10.17605/OSF.IO/74XGR` — U-Theory / U-Model v.28 appendix series (canonical citation for this profile).
- **`APPENDIX_POS` — The Principle of Sequence: Readiness-Ordered Commitment** — the parent gate this profile instantiates (`§2.6` gate, `§7` firewall dominance, `§8` pre-registered falsifiers).
- **`APPENDIX_TRA` — Triadic Rocketry & Astronautics** — the domain source for the **aerospace adapter**.
- **`APPENDIX_WAR` / `APPENDIX_TRC` (L4 societal telos & dual-use firewall)** — the dual-use firewall the military-space adapter inherits unchanged.
- **`APPENDIX_SSS`, `APPENDIX_GSI-RTD`, `APPENDIX_TE`** — the measurement engine, runtime, and umbrella prerequisites.
- **Project home:** `u-model.org`
- **Author:** Petar Nikolov — **ORCID `0009-0001-8669-2276`**.
