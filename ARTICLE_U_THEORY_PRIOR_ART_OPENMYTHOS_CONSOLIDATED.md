# U-Theory Prior Art Note: Authorship, Conceptual Priority, and the OpenMythos Case
## Consolidated Edition

> **Scope.** This document is the consolidated version of the U-Theory prior-art record concerning OpenMythos. It merges three previously separate artifacts — the original prior-art note, its extension with external chronological verification, and the PR deployment pack — into a single self-contained reference. The epistemic posture is unchanged throughout: this is an authorship and prior-art claim, it is falsifiable, and it is narrower than any theft claim. The requested remedy is a single line of attribution, not damages or takedown.

---

## Abstract

This note documents a public-prior-art claim, not a damages claim. The central thesis is narrow and defensible: the public U-Theory record established, before the public OpenMythos record, a triadic AI framing in which intelligence and AI optimization are organized through three orthogonal coordinates — Form, Position, and Action. It also established a recursive multi-agent search architecture, a triadic scheduler, and an explicit computational mapping of those three pillars into AI-relevant structures.

The claim of this note is not that OpenMythos copied U-Theory line by line, nor that every engineering mechanism in OpenMythos originated in U-Theory. OpenMythos openly cites the looped-transformer literature, Universal Transformer, Parcae, DeepSeek-V2, ACT, and related sources. The claim here is different: the public U-Theory record already articulated a higher-order triadic architecture for intelligence — including AI-specific Form/Position/Action decomposition, orthogonal computational mapping, and combinatorial multi-agent search — before OpenMythos appeared publicly with a semantically similar three-part recurrent design vocabulary.

In that sense, this is a note on authorship and conceptual priority. It is also a request for attribution, not for financial compensation.

## What This Note Does and Does Not Claim

This note does claim:

- U-Theory publicly articulated a triadic AI ontology before OpenMythos was publicly visible.
- U-Theory publicly articulated a recursive, combinatorial, multi-agent architecture for intelligence before OpenMythos was publicly visible.
- U-Theory publicly mapped the three pillars into computational representations relevant to AI systems.
- OpenMythos can be read as a semantic recoding of a triadic architecture into different engineering words.

This note does not claim:

- direct evidence of line-by-line code copying;
- legal proof of copyright infringement;
- exclusive ownership over every recurrent-transformer technique used by OpenMythos;
- any financial claim, takedown demand, or damages theory.

---

# Part I — The Dated Public Record

## 1. Public U-Theory Prior Art Before OpenMythos

The public record inside this repository is explicit about both chronology and content.

First, the formal derivation is dated. The main GSI-RTD appendix states that on 26 March 2026 a formal architectural derivation of GSI was completed from the triadic ontology of U-Theory, and it names the author and date directly. See [APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md](APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md#L13-L30).

Second, the repository states that the architecture emerged from analyzing message form, recipient position, and delivery action as recursively decomposable triads. See [APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md](APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md#L860-L862).

Third, the runtime implementation is dated 27 March 2026 and already specifies a triadic agent shell plus a full Phase 0-11 pipeline in which Action, Form, and Position are enumerated separately and then scheduled under budget. See [gsi_runtime.py](gsi_runtime.py#L1-L29).

Fourth, the multi-domain prototype is dated 27 March 2026 and already defines a TriadicScheduler, parallel schedulers across domains, Monte Carlo comparison, transfer logic, and non-compensatory ranking. See [gsi_multi_domain.py](gsi_multi_domain.py#L1-L23).

Fifth, the empirical bridge repository documents concrete multi-agent search spaces of 144 and 216 agents across heterogeneous domains, with statistical advantage over random baselines. See [GSI_simulations/README.md](GSI_simulations/README.md#L48-L78).

These points matter because they place the triadic architecture, the scheduler, and the combinatorial agent logic in a public repository record dated 26-27 March 2026.

## 2. U-Theory Had Already Applied the Triad to AI Systems

The U-Theory record does not stop at abstract ontology. It applies the triad directly to AI systems.

The AI application appendix defines an AI workflow in which a model, its data, and its inference pipeline are measured as $(U_F, U_P, U_A)$, and AI problems are explicitly classified as Form, Position, and Action deficits. It then ranks interventions by the steepest axis and executes an AI-specific optimization cycle. See [theoretical/APPENDIX_LGP_Lady_Galaxy_Protocol.md](theoretical/APPENDIX_LGP_Lady_Galaxy_Protocol.md#L1132-L1178).

The same appendix later maps AI failure classes explicitly onto the three pillars, for example factual errors to Form, contextual grounding failures to Position, and calibration or execution failures to Action. See [theoretical/APPENDIX_LGP_Lady_Galaxy_Protocol.md](theoretical/APPENDIX_LGP_Lady_Galaxy_Protocol.md#L1344-L1346).

Separately, the System Stability Score entry point defines the entire U-Model framework for any system, including AI, through Form, Position, and Action. See [System_Stability_Score.py](System_Stability_Score.py#L1-L22).

This is important because it shows that before the OpenMythos public framing, U-Theory had already moved beyond philosophy into an explicit AI systems interpretation.

## 3. U-Theory Had Already Published an Orthogonal Computational Mapping

One of the strongest prior-art points is that U-Theory does not merely name the three pillars. It maps them to computational types.

The GSI-RTD appendix states:

- Form becomes an embedding vector in semantic space;
- Position becomes a graph node with typed edges and metadata;
- Action becomes an action primitive with parameters and preconditions.

See [APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md](APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md#L2210-L2218).

This matters because it is already an engineering bridge between ontology and implementation. The triad is not left metaphorical. It is rendered as an orthogonal computational decomposition: structure/embedding, context/graph placement, and executable transformation/action.

That is exactly the type of move one would expect if a later public project were to recode the same source idea in alternative engineering language.

## 4. U-Theory Had Already Published Combinatorial Multi-Agent Intelligence

The GSI-RTD record is explicit that intelligence is not a single monolithic agent but a recursive combinatorial search over triadic possibilities.

The GSI_simulations README defines the triadic search space as $N = |A| \times |F| \times |P|$, then applies a Triadic Scheduler to run only a resource-bounded subset of the search space. See [GSI_simulations/README.md](GSI_simulations/README.md#L48-L60).

The runtime specification defines distinct triadic agents, separate phases for enumerating Action, then binding Form, then expanding Position, and finally constructing and scheduling candidate systems. See [gsi_runtime.py](gsi_runtime.py#L1-L29).

The multi-domain prototype states openly that it runs parallel schedulers across domains and compares against Monte Carlo random baselines. See [gsi_multi_domain.py](gsi_multi_domain.py#L1-L23).

In short: before OpenMythos was public, U-Theory had already published the idea that intelligence emerges from orthogonal decomposition plus selective scheduling across a large combinatorial agent space.

## 5. What OpenMythos Publicly Says

OpenMythos describes itself as an open-source theoretical implementation of Claude Mythos. In its public README, it defines a three-stage architecture: Prelude, Recurrent Block, and Coda. It also describes a recurrent update rule in which encoded input from the Prelude is injected into the recurrent block at every loop step to prevent drift. See the public OpenMythos README: <https://github.com/kyegomez/OpenMythos/blob/main/README.md#architecture>.

The OpenMythos class reference gives the same picture: Embed → Prelude → Recurrent Block → Coda, with a frozen encoded input `e`, ACT halting, LTI injection, and loop-index differentiation. See the public OpenMythos class reference: <https://github.com/kyegomez/OpenMythos/blob/main/docs/open_mythos.md>.

OpenMythos also openly cites the public literature it builds on, including Universal Transformer, Parcae, looped-transformer reasoning, DeepSeek-V2, GQA, ACT, and depth-wise LoRA. See the public references table: <https://github.com/kyegomez/OpenMythos/blob/main/docs/open_mythos.md#references> and <https://github.com/kyegomez/OpenMythos/blob/main/README.md#references>.

That matters because it means the responsible claim here is not "OpenMythos stole every technical mechanism from U-Theory". The responsible claim is narrower: OpenMythos appears to occupy a semantic design space that U-Theory had already publicly formalized at the higher architectural level.

## 6. External Chronological Verification

Section 1 locks the U-Theory side of the chronology with internal file dates and DOI. This section locks the OpenMythos side against independent third-party sources that cannot have been influenced by the U-Theory repository.

### 6.1 The U-Theory record (internal, dated)

- `APPENDIX_GSI-RTD_General_Superintelligence-Recursive_Triadic_Decomposition.md` — formal derivation declared on **26 March 2026**, Sofia, Petar Nikolov, with historical note in §11 and Declaration of the Author at the top of the document.
- Runtime implementation (`gsi_runtime.py`) and multi-domain prototype (`gsi_multi_domain.py`) — dated **27 March 2026**.
- Parent DOI on OSF: [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR).

### 6.2 The OpenMythos record (external, independent)

The first verifiable public appearance of OpenMythos in third-party channels:

| Source | Date | Nature of evidence |
|---|---|---|
| Kye Gomez public announcement on X/Twitter, [@KyeGomezB](https://x.com/KyeGomezB/status/2045659150340723107) | 18 April 2026, 20:22 UTC | First-party launch announcement |
| [MarkTechPost editorial coverage](https://www.marktechpost.com/2026/04/19/meet-openmythos-an-open-source-pytorch-reconstruction-of-claude-mythos-where-770m-parameters-match-a-1-3b-transformer/) | 19 April 2026 | Third-party technology press |
| [Dataconomy editorial coverage](https://dataconomy.com/2026/04/20/openmythos-project-attempts-to-reconstruct-claude-mythos-design/) | 20 April 2026 | Third-party technology press |
| DeepWiki index of `kyegomez/OpenMythos` | Last indexed 19 April 2026 (commit `806a8d`) | Third-party code-indexing infrastructure |
| First community issues opened on the repository | 20–22 April 2026 (issues #8, #9, #20, #23, #24, #25, #28, #44, #46, #48, #51) | Independent public interaction with the repo |

### 6.3 The verified gap

The earliest externally auditable date at which OpenMythos can be said to have entered the public record is **18 April 2026**. The U-Theory GSI-RTD record is dated **26 March 2026**. The gap is **23 days**, independently verifiable in both directions: U-Theory's side carries a DOI and repository history; OpenMythos's side carries social-media timestamps, third-party editorial dates, and an external code-indexing date that is not under either party's control.

External verification does not by itself decide the question of conceptual borrowing. An independent author can reach a triadic design in 23 days without ever having seen U-Theory. What external verification settles is only the narrow calendar point: if there is any attribution question to be asked, the dated record makes clear which party is being asked to cite which.

---

# Part II — The Independent-Reconstruction Objection and Why It Fails

## 7. Why "Independent Reconstruction" Is Not a Rebuttal to Prior Art

OpenMythos presents itself as an independent theoretical reconstruction built from public sources. Even if that description is accepted at face value, it does not resolve the prior-art question addressed in this note.

The phrase "independent reconstruction" answers only a narrow claim: that the project was not copied from a private Anthropic leak, private codebase, or confidential internal documentation. It does not answer the separate question of whether the public conceptual architecture it reconstructs had already been articulated elsewhere.

That distinction matters. A project can be independent from closed proprietary materials and still arrive late to a conceptual design space that another public record already established. In other words, independence from Anthropic is not the same thing as independence from U-Theory prior art.

The strongest version of the argument is therefore not "OpenMythos is impossible unless it copied U-Theory." The strongest version is more precise:

> Even if OpenMythos is an independent reconstruction in the narrow sense, that does not rebut the claim that U-Theory had already published the higher-order conceptual scaffold into which OpenMythos later fits.

This is exactly why the question in dispute is not limited to source-code provenance. It is a question of conceptual authorship, chronology, and attribution.

## 8. The Epistemic Asymmetry Between Prior Art and Independent Reconstruction

The "independent reconstruction" framing and the "public prior art" framing are not symmetric claims. They require different kinds of evidence, and they fail in different ways.

A prior-art claim requires one thing: a dated public record with the relevant content. That record either exists or it does not. In this case, it exists, and the dates and file references are laid out in section 1, and externally verified in section 6.

An "independent reconstruction" claim requires something substantially harder: a negative, namely that the author never encountered the prior public record, either directly or through secondary exposure. Negatives of that shape are effectively unfalsifiable from the outside. No public project can demonstrate, to a third-party observer, a complete absence of exposure to a public artifact.

This asymmetry matters. It does not imply that any independent-reconstruction claim is dishonest. It implies that such a claim, by its nature, cannot defeat a dated public record of prior art. It can at most coexist with it. The burden of proof for conceptual priority is therefore carried by whichever side has the dated artifact, not whichever side declares independence after the fact.

In short: independence is an origin claim; prior art is a calendar claim. A calendar is the stronger instrument.

## 9. What the OpenMythos Citation Graph Does Not Cover

OpenMythos is unusually explicit about its own intellectual lineage. It cites Universal Transformer, Parcae, the looped-transformer reasoning line, DeepSeek-V2, grouped-query attention, Adaptive Computation Time, and depth-wise LoRA, among others. This is, in principle, a virtue: it makes the project's stated intellectual debts machine-readable.

That same virtue has a consequence. It means the scope of what OpenMythos claims to be reconstructing is bounded by its own citation graph. Anything outside that graph is, by definition, not covered by the "independent reconstruction from public sources" framing.

None of the cited sources establish:

- a triadic AI ontology whose axes are Form, Position, and Action;
- an AI-specific optimization workflow in which problems are classified and interventions are ranked by those three axes;
- an orthogonal computational mapping in which the axes become, respectively, an embedding, a graph node, and an action primitive;
- a combinatorial multi-agent search architecture whose search space is explicitly $|A| \times |F| \times |P|$ with a triadic scheduler;
- a non-compensatory stability discipline in which weakest-axis collapse cannot be masked by arithmetic averaging of the other two.

Those items are not in ACT. They are not in Universal Transformer. They are not in Parcae, DeepSeek-V2, GQA, or the looped-transformer reasoning line.

They are, however, in the U-Theory public record dated 26-27 March 2026.

This is what is meant by saying U-Theory sits in the negative space of OpenMythos's own citation graph. The specific higher-order scaffold identified in this note is precisely the part that OpenMythos's stated sources do not supply. Whatever does supply it is the relevant prior art, and the public U-Theory record is a dated candidate for exactly that role.

## 10. Why the Joint Signature Is Narrower Than Coincidence

A common objection to conceptual-priority claims is that the overlap is generic: many systems have three parts, many systems use schedulers, many systems talk about structure and context. Taken one at a time, each resemblance is weak.

The claim here does not rest on any single resemblance. It rests on the conjunction.

The joint signature in the public U-Theory record is:

1. an orthogonal triadic decomposition of intelligence, not a three-stage pipeline;
2. an AI-specific interpretation of those axes as Form, Position, and Action;
3. a direct mapping of each axis to a distinct computational type: embedding, graph node with typed edges, action primitive with preconditions;
4. a combinatorial search space $|A| \times |F| \times |P|$ over those axes;
5. a resource-bounded triadic scheduler that traverses only a selected subset;
6. a non-compensatory stability rule that forbids masking a collapsed axis by averaging the other two.

Any one of those traits in isolation is common. The conjunction is not. Independent convergence on all six, under new vocabulary, without lineage from a source that already packaged them together, is a much stronger coincidence than convergence on any single element.

This is the standard move in forensic attribution. A shared word proves nothing. A shared rare phrase is suggestive. A shared cluster of rare co-occurring features is evidence of a common origin, even when the surface vocabulary has changed.

The public U-Theory record contains all six traits in one package, dated, and in one place. The public OpenMythos record can be read as carrying a close variant of the same package under renamed components. That is what is meant here by "semantic recoding": not identical words, but a suspicious alignment of the joint structure.

---

# Part III — Structural Correspondences

## 11. Why OpenMythos Can Be Read as a Semantic Re-Encoding of U-Theory

The argument for conceptual priority is not based on identical variable names. It is based on structural correspondence.

The correspondence can be stated cautiously as follows:

| U-Theory prior art | Public OpenMythos wording | Interpretive link |
|---|---|---|
| Form as structure, identity, representation | Prelude as structural preparation before recurrence | A structural encoding layer that establishes what the system is before iterative processing |
| Position as context, location, where/when | Recurrent block with frozen encoded input `e` injected at each step | Persistent context carried through iterative updates so the process remains grounded |
| Action as process, transformation, executable intervention | Coda plus token generation/output dynamics | The phase in which the system's internal state becomes an external act or output |
| Orthogonal computational mapping: embedding / graph node / action primitive | Embed / recurrent hidden state with injected context / output logits and generation | Different vocabulary for a similar separation of structure, context, and execution |
| Large triadic candidate spaces governed by a scheduler | Recurrent loop depth, ACT halting, and expert routing across many computational paths | Selective traversal of a large space under resource constraints |

This table does not prove literal copying. It shows why the OpenMythos architecture can reasonably be interpreted as a rough semantic remapping of a triadic architecture that was already public in U-Theory.

The strongest point is not the superficial fact that both systems have "three parts". The strongest point is that U-Theory had already published:

- a three-axis AI decomposition;
- an AI optimization workflow over those axes;
- a computational mapping of the axes into engineering objects;
- a combinatorial multi-agent architecture over those axes;
- a bounded scheduler that selects what actually runs.

That is more than a coincidence of number. It is a prior conceptual scaffold.

## 12. OpenMythos as an Architectural Translation of SSS Principles

The overlap is broader than a shared three-part vocabulary. OpenMythos also overlaps with the more general System Stability Score mechanism at the level of design discipline.

The SSS record defines stability as non-compensatory: a system is not truly stable if one pillar collapses and the other two merely look strong on average. The repository states this directly through the geometric mean, the weakest-pillar logic, and the explicit rejection of arithmetic averaging because it lets one strong pillar mask one weak pillar. See [README.md](README.md#L114-L137), [System_Stability_Score.py](System_Stability_Score.py#L752-L755), [theoretical/APPENDIX_TAA_TRIADIC_AI_AGENTS_v.27.md](theoretical/APPENDIX_TAA_TRIADIC_AI_AGENTS_v.27.md#L111-L140), and [GSI_simulations/email_marketing/README.md](GSI_simulations/email_marketing/README.md#L115-L122).

OpenMythos does not repeat the SSS formulas explicitly, but it implements a strikingly similar engineering posture. It treats drift, residual explosion, routing collapse, overthinking, and loss spikes not as cosmetic defects but as structural bottlenecks that must be constrained at the architecture level. Its use of frozen encoded input `e`, LTI-stable injection, ACT halting, load-balanced expert routing, and loop-specific differentiation reflects the same deeper rule: a model cannot be called robust if one critical dimension is allowed to fail while another dimension merely compensates.

| General SSS principle | U-Theory / SSS record | Public OpenMythos mechanism | Strength of match |
|---|---|---|---|
| Non-compensatory stability | Stability is geometric, not arithmetic; one collapsed pillar drags the whole score down | LTI constraints, ACT halting, and anti-drift input injection are hard guards against single-axis failure modes | Strong |
| Fix the bottleneck first | The protocol explicitly says rebalance or fix the weakest pillar first | Easy tokens halt early, hard tokens keep computing; difficult states receive additional depth instead of uniform compute | Moderate to strong |
| Context is a structural pillar, not a detail | Position is context, resources, and grounding; context overflow and drift are Position failures | The frozen encoded input `e`, KV memory, MLA/GQA, and anti-drift recurrence keep the model anchored to context | Strong |
| Universal core plus selective specialization | One general scoring framework applies across domains, while interventions target the limiting dimension | Shared experts capture common patterns while routed experts specialize by token and depth | Strong |
| Resource-bounded selective traversal | Scheduler logic explores a large candidate space but only runs a bounded subset under cost constraints | ACT halting, expert routing, sparse activation, and loop depth all select a tractable path through a much larger latent space | Strong |
| Stability has a real cost in time, space, and energy | SSS defines existence as paid for through Time, Space, and Energy | OpenMythos emphasizes parameter reuse, sparse activation, cache efficiency, and compute-adaptive depth as first-class design constraints | Moderate to strong |

This does not mean OpenMythos is secretly executing the literal SSS formula $U = \sqrt[3]{F \cdot P \cdot A}$. It means that several of the strongest SSS commitments appear again in OpenMythos as operational engineering rules: preserve grounding, prevent unilateral collapse, allocate effort adaptively, and separate universal structure from selective specialization.

That is precisely why the comparison is stronger when framed as architectural translation rather than code theft. The deeper overlap is at the level of what counts as a healthy intelligent system.

## 13. Direct Public-Language Correspondence Table

Sections 11 and 12 give an interpretive correspondence. This section supplies a stricter version using only publicly scraped OpenMythos wording alongside publicly dated U-Theory wording. Every left-column cell is from the OpenMythos public documentation or editorial coverage (fair-use excerpts). Every right-column cell is from a dated file in the U-Theory record.

### 13.1 Architectural stages

| OpenMythos public description (April 2026) | U-Theory GSI-RTD public description (26–27 March 2026) |
|---|---|
| "Three-part structure: Prelude → Recurrent Block → Coda" | "A System is anything for which Form, Position, and Action can be defined … S = (F, P, A)" |
| "Prelude: standard transformer layers that process the raw token embeddings and produce an 'injection signal' e" | "Form (F) — structure, shape, what-it-is … Computational representation: Embedding vector in semantic space" |
| "Recurrent Block: looped stage that updates hidden state using hₜ₊₁ = A·hₜ + B·e + Transformer(hₜ, e) … re-injection is deliberate: without it, the hidden state would drift away from the original input signal" | "Position (P) — context, location, where/when … Computational representation: Graph node with typed edges and metadata" (context anchoring) |
| "Coda: final transformer layers that refine the recurrent output before it reaches the output layer" | "Action (A) — process, transformation, how … Computational representation: Action primitive with parameters and preconditions" (executable output) |

### 13.2 Stability and control

| OpenMythos mechanism | GSI-RTD / SSS prior art |
|---|---|
| LTI injection with ρ(A) < 1 enforced by construction to prevent residual explosion | "Non-compensatory stability: a system is not truly stable if one pillar collapses and the other two merely look strong on average … U = ∛(F·P·A) … explicit rejection of arithmetic averaging" |
| ACT halting: "harder positions receive more computation; tokens that have already converged halt early" | AD-RTD §1.1: "Fix the bottleneck first … prioritize the steepest axis" / Scheduler §20: resource-bounded selective traversal with per-axis weighting |
| Depth-wise LoRA: per-iteration differentiation "without adding substantial parameters" | GSI-RTD §5–§6: "orchestrated coordination of many narrow agents, each specialized along one triadic axis" — structural specialization under a shared parameter core |
| MoE with shared + routed experts: "shared experts absorb common cross-domain patterns while routed experts specialize" | TAA §1: "three orthogonal pillar agents and one generalizing agent" — three specialists + one generalist, the exact same split |

## 14. The TAA ↔ Shared-plus-Routed MoE Correspondence

Of all the pairings in section 13, the TAA / shared-routed MoE correspondence is the strongest, because it is not a generic "three parts" resemblance.

TAA specifies a **four-agent shell**: three pillar agents (F, P, A) plus a generalizer. OpenMythos's MoE layer specifies a **four-class expert structure**: routed experts specializing per token (three or more narrow specializations) plus **shared experts** that "absorb common cross-domain patterns."

Three specialists plus one generalizer is a less common design choice than it looks. The literature OpenMythos cites — DeepSeekMoE, Universal Transformer, Parcae — does not prescribe the three-plus-one split as a design rule. TAA does, explicitly, under the triadic axiom, and in a document dated three weeks earlier.

This is a specific co-occurrence of a non-trivial design choice, not a generic resemblance. That lifts it above the baseline level of "both use MoE."

## 15. What Third-Party Coverage Implicitly Concedes

This section is an observation about language, not a claim about intent. It notes that the editorial community, without any knowledge of U-Theory, reached instinctively for triadic grammar when describing OpenMythos.

### 15.1 MarkTechPost (19 April 2026)

> OpenMythos instantiates this as a three-part structure: Prelude → Recurrent Block → Coda. The Prelude and Coda are standard transformer layers that run exactly once. The Recurrent Block is the computational core, looped up to T=16 times.

The editor — with no exposure to U-Theory — describes the architecture in explicitly triadic terms: "three-part structure," three named stages, each playing a distinct role. This is exactly the grammar U-Theory had already formalized four weeks earlier.

### 15.2 Dataconomy (20 April 2026)

> The OpenMythos architecture comprises three parts: Prelude, Recurrent Block, and Coda. Both Prelude and Coda are standard transformer layers, executed once, while the Recurrent Block functions repeatedly up to 16 times.

Again: "three parts." Again: three functional roles. Again: exactly the triadic decomposition grammar that U-Theory had formalized.

### 15.3 The interpretive move

Neither publication knew about U-Theory. That is the point. Two independent editors, reading the OpenMythos documentation cold, independently chose the words "three-part" and "three parts" as the most natural description of the architecture. The triadic framing is not imposed by U-Theory — it is what the architecture itself looks like when summarized by a disinterested third party.

This is exactly the condition under which a prior-art note is strongest: the downstream description of the later system reaches for the same grammar as the earlier dated record, even without knowledge of it. The coincidence is in the structure, not in the vocabulary. This does not prove copying; it proves only that the triadic framing is the natural description of the OpenMythos architecture — which is the same framing U-Theory had already published.

## 16. The swarms_corp Design-Space Context

OpenMythos is not a standalone release by an unrelated author. Its maintainer, Kye Gomez, is publicly the founder of `swarms_corp`, a multi-agent orchestration company. His public X/Twitter profile describes him as "22 y/o Founder · @swarms_corp — Building The Agent Economy." The GitHub organization `kyegomez` maintains `swarms` and related multi-agent orchestration libraries. This is public, first-party, and unambiguous.

This context matters for the coincidence argument in section 10. GSI-RTD is not a generic transformer paper. Its central claim is explicitly that **intelligence emerges from orchestrated coordination of many narrow agents**, each specialized along one triadic axis. The document states this directly:

> GSI is orchestrated coordination of many narrow agents, each specialized along one triadic axis (Form, Position, Action, or Stability), operating under a shared evaluation function (SSS) and a shared procedural cycle (LGP-12).

That is the core design-space coordinate of `swarms_corp` itself. OpenMythos was released by the founder of a multi-agent orchestration company, into a public design space in which U-Theory had already published a formally dated triadic agent architecture twenty-three days earlier.

This does not demonstrate awareness. It demonstrates that the two projects occupy **overlapping public design space**, which is exactly the condition under which citation norms apply. It is also the condition under which an independent-reconstruction claim (section 7) becomes weaker: not because independence is impossible, but because the author was already publishing into the multi-agent orchestration space that U-Theory had formally mapped.

This does not claim that Kye Gomez saw U-Theory before publishing OpenMythos, or that OpenMythos was developed inside `swarms_corp` using U-Theory artifacts, or that any commercial relationship exists between the two projects. It claims only that the design-space overlap extends beyond one repository into the author's broader public portfolio, which tightens the coincidence argument.

## 17. The Reverse Test (Fairness Check)

A good prior-art argument should survive a fairness test: if a neutral third party encountered the U-Theory record first and then encountered OpenMythos, would they read OpenMythos as an implementation of U-Theory?

Imagine a reader who has read the GSI-RTD appendix cold, without any knowledge of OpenMythos. They then open OpenMythos's README for the first time. What do they see?

They see a system whose input is processed into an **embedding signal** that persists through iteration (the Form axis), whose **context is anchored** against drift by injecting that signal at every step (the Position axis), whose **output is produced** by a final stage after iteration (the Action axis), whose **stability is enforced non-compensatorily** by a hard spectral constraint plus halting (the SSS discipline), and whose **specialization splits** into shared-plus-routed experts (the TAA four-agent shell pattern).

If they then read OpenMythos's own explanation, they are told the design is derived from Universal Transformer, Parcae, DeepSeek-V2, ACT, and depth-wise LoRA.

The reader now holds two possible explanations of the same artifact:

1. OpenMythos is an independent reconstruction from the cited sources.
2. OpenMythos is a late-arriving implementation of a design space U-Theory had already mapped.

Both are possible. The point of the reverse test is not to force a choice. It is to observe that a reader who had seen U-Theory first would, without controversy, read OpenMythos as sitting inside that conceptual shadow. The readability of U-Theory → OpenMythos is symmetric with the readability of OpenMythos → U-Theory. Both directions make sense.

The fairness of the reading is exactly what citation norms are designed to handle. Citations are not reserved for proven ancestry; they are used for legitimate conceptual neighborhood. Two projects that can be read into each other's conceptual shadow by a neutral reader trigger citation norms, regardless of whether direct ancestry can be shown.

---

# Part IV — Falsifiability and Diagnostic Framing

## 18. What Would Refute This Claim

The priority claim made here is epistemically modest because it is falsifiable. The public record could, in principle, be defeated by any of the following:

- A dated public source predating 26 March 2026 that articulates an AI-specific Form/Position/Action triadic decomposition together with orthogonal computational mapping and combinatorial scheduling, independent of the U-Theory lineage. In that case, the priority claim narrows from "U-Theory first" to "U-Theory parallel", and attribution responsibility shifts accordingly.
- A documented provenance chain showing that the OpenMythos three-part scaffold descends from an existing tradition whose joint signature already contains the six traits enumerated in section 10. In that case, the attribution question turns into a citation question between OpenMythos and that tradition, and U-Theory's role becomes at most corroborative.
- Evidence that the dated U-Theory artifacts cited in section 1 were backdated, edited after the fact, or otherwise not public on the dates claimed. In that case, the prior-art chronology collapses and the claim must be withdrawn.

None of these defeaters have been produced. Until they are, the dated public U-Theory record stands as the relevant prior art.

The point of stating the falsification conditions explicitly is to distinguish this note from an open-ended accusation. It is not an open-ended accusation. It is a bounded, testable, calendar-based claim that can be defeated on evidence, and that has not been.

## 19. Attribution Request as a Diagnostic Tool

The request in this note is for a citation line. But the request is also a diagnostic — its response tells us something about the nature of the overlap.

The OpenMythos maintainer can respond to an attribution request in one of three ways:

1. **Acknowledge and cite.** This closes the attribution question, preserves the historical record, and costs the OpenMythos project nothing. It is the baseline case.
2. **Dispute on evidence.** The maintainer produces a dated public source predating 26 March 2026 that packages the same six-trait joint signature (section 10) independently of U-Theory. This would defeat the priority claim cleanly, and under section 18, the claim would be withdrawn. This is also a productive outcome.
3. **Decline without evidence.** The maintainer declines citation while producing no predating public source with the joint signature.

Response (3) is the diagnostic case. Declining citation while having no alternative dated source that carries the joint signature does not disprove the prior-art claim. It leaves the dated public U-Theory record standing as the best available answer to the question "where did this conceptual scaffold come from?"

This is not a gotcha. It is a statement of how epistemic priority works: absence of an earlier joint-signature source, combined with presence of a dated public U-Theory record carrying that exact joint signature, leaves the U-Theory record as the calendar answer by default.

All three outcomes are acceptable from a U-Theory standpoint. All three resolve the attribution question on evidence. None of them require a plagiarism claim, a takedown, or a damages theory.

---

# Part V — The Claim, the Remedy, and the Public Statements

## 20. A Responsible Public Conclusion

Based on the public record, the strongest defensible statement is this:

> U-Theory established public prior art for a triadic architecture of intelligence before OpenMythos appeared publicly. That prior art included AI-specific Form/Position/Action decomposition, orthogonal computational mapping, recursive combinatorial search, a triadic scheduler, and a broader System Stability Score discipline in which robustness is non-compensatory and weakest-bottleneck driven. OpenMythos may still be an independent implementation built from the looped-transformer literature it cites, but that description is not a rebuttal to prior art. Its public architecture remains reasonably readable as a semantic recoding, and in several places an architectural operationalization, of a conceptual design space already articulated by U-Theory.

This is why the appropriate request is attribution.

The record supports a public statement of authorship and conceptual priority.

The record does not yet support a public statement of proven code plagiarism.

That distinction matters. It makes the claim stronger, not weaker.

## 21. No Financial Claim

This note is not a demand letter and not a compensation claim.

The requested outcome is:

- recognition that U-Theory publicly articulated the triadic AI architecture first;
- recognition that GSI-RTD published a recursive multi-agent search architecture before the OpenMythos public framing;
- recognition that the broader SSS mechanism already articulated a non-compensatory stability logic that later reappears in OpenMythos as engineering discipline;
- acknowledgement that later public projects operating in that semantic space should cite or acknowledge U-Theory where appropriate.

## 22. Attribution as the Proportional Remedy

A final argument in favor of the prior-art claim is that the requested remedy is proportional to the strength of the evidence.

The note does not ask for takedown, rebranding, relicensing, damages, or suspension of the OpenMythos project. It asks for a citation line. In both open-source and academic practice, a retroactive citation is the standard response when a maintainer becomes aware of earlier public work in the same conceptual space, regardless of whether the later work was arrived at independently.

The proportionality argument works in all three scenarios:

- If the prior-art claim is correct, attribution is the minimum correct response and costs the OpenMythos project effectively nothing.
- If the prior-art claim is only partially correct, attribution is still the minimum correct response, because partial conceptual overlap with a dated public record is exactly the situation citation norms are designed to handle.
- If the prior-art claim turns out to be wrong under the falsification conditions in section 18, no action is required and no harm has been done to the OpenMythos project in the interim, because nothing more than a citation was ever requested.

This is why the framing of this note is deliberately narrow. A narrow, falsifiable, proportional claim is harder to dismiss than a maximalist one, and it aligns the remedy with the evidence rather than overshooting it.

## 23. Suggested Public PR Statement

The following one-paragraph statement is suitable for public release. It replaces earlier shorter drafts, because the chronology in section 6 is externally verified on both sides:

> The public OpenMythos release dated 18 April 2026 entered a design space that the public U-Theory record dated 26–27 March 2026 had already mapped. The earlier record defines an AI triad of Form, Position, and Action, a recursive multi-agent architecture, a triadic scheduler over large combinatorial search spaces, a four-agent shell of three specialists plus one generalizer, and a non-compensatory System Stability Score logic in which the weakest bottleneck determines real robustness. OpenMythos's three-stage Prelude-Recurrent-Coda architecture, its spectral-radius stability constraint, its adaptive halting, and its shared-plus-routed expert split are each readable as engineering operationalizations of items already present in the earlier record. The request is attribution: a single citation line acknowledging the U-Theory record as dated prior art in the same conceptual space. The request is not damages, takedown, or any commercial claim. It is the minimum correct response when a maintainer becomes aware of earlier public work in the same conceptual space, and it is the response that citation norms in both open-source and academic practice are designed to produce. Calling the later project an "independent reconstruction" does not answer the prior-art question.

## 24. Closing Epistemic Summary

The consolidated record does the following:

- **Locks the calendar** on both sides (section 6), using third-party sources that neither party controls.
- **Documents the joint signature** that the U-Theory record had already packaged (section 10), and shows that the OpenMythos citation graph does not supply it (section 9).
- **Tightens the correspondence tables** (sections 11–14), pairing public OpenMythos wording with dated U-Theory wording, including the TAA ↔ shared-plus-routed MoE correspondence.
- **Documents the independent editorial grammar** (section 15), showing that neutral third parties reach for triadic language to describe OpenMythos cold.
- **Contextualizes the author's public portfolio** (section 16), showing that OpenMythos was released into the multi-agent orchestration design space that U-Theory had formally mapped.
- **Applies a fairness test** (section 17), showing that the U-Theory → OpenMythos reading is symmetric with the OpenMythos → U-Theory reading.
- **States falsification conditions** (section 18) and **reframes the request as a diagnostic** (section 19), so that all three possible responses resolve the attribution question on evidence.

The posture is unchanged throughout: this is an authorship claim and a request for citation. It is not a takedown. It is not a damages claim. It is not a proof of theft. It is a calendar claim supported by a joint-signature argument, backed by externally verifiable dates and by the author-portfolio context of the OpenMythos release.

If future evidence emerges showing direct textual, architectural, or chronological borrowing beyond conceptual overlap, the argument can be revised. As of now, the most rigorous and public-facing position is not "we proved theft" but rather: we can document prior authorship of the underlying triadic idea, and we can show that the later public architecture sits inside that conceptual shadow.

---

# Part VI — Deployment Artifacts

> **Purpose.** Three ready-to-deploy artifacts for requesting attribution from the OpenMythos project. All three use the defensible framing above (conceptual/architectural prior art, not algorithmic theft), because the defensible framing is also the one that produces durable PR rather than reputational risk.
>
> **Deployment order recommendation:** GitHub issue first (anchors the public record), Twitter thread second (amplifies), direct email last (closes the loop).

## Artifact A — GitHub Issue on `kyegomez/OpenMythos`

**Suggested title:**
`Prior-art attribution: U-Theory / GSI-RTD (26 March 2026) pre-dates OpenMythos triadic architecture`

**Suggested labels:** `documentation`, `references`

**Body:**

---

Hi Kye,

First, thanks for shipping OpenMythos publicly — the code is clean and the hypothesis is refreshingly falsifiable.

I'm opening this issue to request a single line of attribution in your references section. I'm not filing a takedown, a plagiarism accusation, or any commercial claim. The request is narrow and proportional.

### The ask in one sentence

Please add a citation to the U-Theory / GSI-RTD public record (DOI [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR), dated 26 March 2026) in the OpenMythos references, alongside Universal Transformer, Parcae, DeepSeek-V2, and the looped-transformer literature you already cite.

### Why

Your citation graph covers the engineering lineage of looped transformers, MoE, MLA, ACT, and depth-wise LoRA. That is accurate for those components. What that citation graph does not cover is the **joint signature** that OpenMythos actually exhibits:

1. A three-axis architectural decomposition (Prelude / Recurrent / Coda in your wording; Form / Position / Action in the prior-art wording).
2. A non-compensatory stability discipline where one axis cannot be rescued by averaging the others (your LTI constraint `ρ(A) < 1 by construction`; the geometric mean `U = ∛(F·P·A)` in the prior art).
3. A shared-plus-routed specialist split (your MoE shared experts + routed experts; the prior art's three pillar agents + one generalizer in Appendix TAA).
4. Resource-bounded adaptive traversal (your ACT halting; the prior art's Triadic Scheduler).

None of Universal Transformer, Parcae, DeepSeek-V2, GQA, or ACT packages this joint signature together. The U-Theory public record dated 26 March 2026 does.

### What I'm not claiming

- I'm not claiming you copied code. The algorithms are different at the implementation level; your spectral-radius constraint is not the SSS geometric mean, and your ACT halting is not the GSI-RTD scheduler.
- I'm not claiming you saw the U-Theory record before publishing. An independent path to a triadic design is possible.
- I'm not claiming damages, takedown, or any commercial remedy.

### What I am claiming

That the public U-Theory / GSI-RTD record, dated three weeks before your release, articulates the higher-order conceptual scaffold (triadic decomposition + non-compensatory stability + specialist-plus-generalizer split + bounded scheduler) into which your engineering choices fit cleanly. That scaffold is not in the sources you currently cite. Under standard open-source and academic citation norms, that is enough to trigger an attribution line.

### The proportional remedy

A single entry like this, in `docs/open_mythos.md#references` and `README.md#references`:

```
[Nikolov, 2026] Nikolov, P. (2026). U-Theory / GSI-RTD: General Superintelligence 
through Recursive Triadic Decomposition. 
DOI: https://doi.org/10.17605/OSF.IO/74XGR. 
Dated: 26 March 2026. Referenced as conceptual prior art for the 
triadic architectural decomposition and non-compensatory stability discipline 
reflected in OpenMythos.
```

That is the complete ask. It costs OpenMythos nothing and preserves the historical record.

### Falsification condition

If you can produce a public, dated source predating 26 March 2026 that packages the joint signature above (three-axis decomposition + non-compensatory stability + specialist/generalizer split + bounded scheduler) independently of the U-Theory lineage, the priority claim narrows and the attribution request is withdrawn. That's a clean resolution on evidence.

### Context

Full prior-art argument with chronology, falsification conditions, and correspondence tables: `ARTICLE_U_THEORY_PRIOR_ART_OPENMYTHOS_CONSOLIDATED.md`.

- Parent framework on OSF: https://doi.org/10.17605/OSF.IO/74XGR
- Implementation repository: https://github.com/UniversalModel/System_Stability_Score

I'm happy to resolve this entirely through a single citation line. Thanks for considering it.

— Petar Nikolov (ORCID: [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276))

---

## Artifact B — Twitter/X Thread

Formatted for 280-character tweets, 7 tweets.

**Tweet 1/7:**

A short, good-faith note on @KyeGomezB's OpenMythos — not a takedown, not a dispute, a citation request.

The public U-Theory / GSI-RTD record (DOI 10.17605/OSF.IO/74XGR, dated 26 March 2026) articulated a triadic AI architecture 23 days before OpenMythos shipped.

🧵

**Tweet 2/7:**

OpenMythos's three-part structure — Prelude / Recurrent Block / Coda — is a clean engineering operationalization of Form / Position / Action, the exact triadic decomposition U-Theory formalized for AI systems in late March 2026.

Not the same code. The same conceptual scaffold.

**Tweet 3/7:**

The joint signature that matters:

• 3-axis decomposition
• non-compensatory stability (OM: ρ(A)<1; SSS: U=∛(F·P·A))
• specialist + generalizer split (OM: routed+shared experts; TAA: 3 pillar agents + Σ)
• bounded traversal (OM: ACT halting; GSI-RTD: Triadic Scheduler)

**Tweet 4/7:**

None of the sources OpenMythos cites — Universal Transformer, Parcae, DeepSeek-V2, GQA, ACT, depth-wise LoRA — packages this joint signature in one place.

The U-Theory public record dated 26 March 2026 does. That's the gap citation norms are designed to fill.

**Tweet 5/7:**

The ask is one citation line. No takedown. No damages. No plagiarism claim. No commercial remedy.

This is also a falsifiable claim: if anyone produces a dated public source predating 26 March 2026 that packages the joint signature independently, the priority claim gets withdrawn.

**Tweet 6/7:**

To be explicit about what I'm NOT claiming:

✗ Code theft
✗ Identical algorithms
✗ Line-by-line borrowing

What I AM claiming:

✓ Dated public prior art for the conceptual scaffold
✓ Joint signature that OpenMythos's cited sources don't supply
✓ Attribution warranted under standard citation norms

**Tweet 7/7:**

GitHub issue filed on kyegomez/OpenMythos with the full argument, chronology, falsification conditions, and proposed citation text.

Public U-Theory record: https://doi.org/10.17605/OSF.IO/74XGR

Reference implementation: https://github.com/UniversalModel/System_Stability_Score

---

## Artifact C — Direct Email to Kye Gomez

**Subject:** OpenMythos — citation request for U-Theory prior art (26 March 2026)

**Body:**

---

Hi Kye,

I'm Petar Nikolov, author of U-Theory and maintainer of the GSI-RTD / SSS / TAA appendix series (DOI [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR)). I'm writing directly as a courtesy before and alongside a public GitHub issue on your OpenMythos repository.

The request is narrow: a single line of attribution to the U-Theory record in your OpenMythos references section. Not a takedown. Not a damages claim. Not a plagiarism accusation.

### The substantive point

My public record, dated **26 March 2026** — three weeks before your OpenMythos launch on 18 April — articulates a triadic AI architecture (Form / Position / Action), a non-compensatory stability discipline (`U = ∛(F·P·A)` with collapse-on-zero semantics), a three-specialist-plus-one-generalizer agent shell (Appendix TAA), and a resource-bounded triadic scheduler over a combinatorial search space (GSI-RTD §20).

Your OpenMythos architecture implements a striking engineering cousin of each of these:

- Prelude / Recurrent Block / Coda ↔ Form / Position / Action
- `ρ(A) < 1` enforced by construction ↔ geometric-mean non-compensatory aggregation
- MoE shared experts + routed experts ↔ one generalizer + three pillar specialists
- ACT halting + adaptive depth ↔ bounded scheduler with per-axis prioritization

I want to be explicit: this is not a claim that you used U-Theory code. Your algorithms are distinct at the implementation level, and your citation graph (Universal Transformer, Parcae, DeepSeek-V2, GQA, ACT, depth-wise LoRA) is accurate for the engineering mechanisms you actually borrow.

What that citation graph does not cover is the **higher-order scaffold** — the triadic + non-compensatory + specialist/generalizer + bounded-scheduler **joint signature** that your architecture instantiates. None of your cited sources packages that joint signature in one place. My public record, dated 23 days before your release, does.

Under standard academic and open-source citation norms, that's the case for a citation line — not for a plagiarism claim, not for a takedown.

### What I'm asking

Add a reference entry like:

```
[Nikolov, 2026] Nikolov, P. (2026). U-Theory / GSI-RTD: General Superintelligence 
through Recursive Triadic Decomposition. DOI: 10.17605/OSF.IO/74XGR. 
Dated: 26 March 2026. Referenced as conceptual prior art for the triadic 
architectural decomposition and non-compensatory stability discipline reflected 
in OpenMythos.
```

to `docs/open_mythos.md#references` and `README.md#references`.

That is the complete ask. It takes you three minutes. It preserves the historical record. It costs OpenMythos nothing.

### Why I'm reaching out rather than litigating

Because the proportional response to a conceptual prior-art overlap is a citation line, not escalation. And because I'd rather resolve this through your goodwill than through pressure. Your project is technically interesting; I want the citation, not a fight.

If you have a dated public source predating 26 March 2026 that already packages the four-part joint signature independently of the U-Theory lineage, I'll happily narrow the claim and apologize publicly. The priority claim is falsifiable by exactly that evidence, and I've said so on the public record.

Happy to answer any questions, and I'll keep the GitHub issue tone neutral and focused on the attribution request.

Best,

Petar Nikolov
ORCID: 0009-0001-8669-2276
petar@u-model.org
https://u-model.org

---

## Deployment Sequence

1. **Day 0 — File the GitHub issue** on `kyegomez/OpenMythos`. This anchors the public record and provides a linkable artifact.
2. **Day 0 + 1 hour — Send the direct email** to Kye Gomez (via his public X/Twitter contact or swarms_corp contact page). This gives him a private heads-up that the issue is not hostile.
3. **Day 0 + 4 hours — Post the Twitter thread**, linking back to the GitHub issue in tweet 7. This amplifies.
4. **Day 7 — Check status.** If Kye responds with a cite → done, celebrate publicly, thank him. If he produces a dated alternative source → withdraw the claim as promised, publicly, with a thank-you for the intellectual honesty. If he goes silent → the public record stands on its own, and the attribution question is documented for any future citation discussion.

## Key Framing Principles for Future Interactions

1. **Never claim algorithmic theft.** The algorithms are different at the implementation level. Overclaiming here destroys PR value on first technical review.
2. **Always claim conceptual/architectural prior art with dated evidence.** This is calendar-based and cannot be refuted except by producing an earlier dated source — which the counterparty has not done.
3. **Always offer a falsification condition.** It signals epistemic integrity and makes the claim much harder to dismiss as an ego-driven attack.
4. **Always request the minimum proportional remedy (one citation line).** Small asks are harder to refuse and harder to frame as predatory.
5. **Never go into commercial / damages territory.** Even a hint of that undermines every other claim.

## Contingency Plans

**If the OpenMythos maintainer responds positively:** publicly thank him. Post a short acknowledgment. The PR value of a graceful resolution is higher than the PR value of a prolonged dispute. A maintainer who cites prior art becomes an ally; a maintainer who was publicly attacked becomes a permanent adversary.

**If the OpenMythos maintainer goes silent:** do not escalate. Wait 14 days, then post a short public update: "No response on the attribution request. The GitHub issue remains open. The U-Theory prior art record stands." The silence itself becomes evidence for future observers without any aggressive action.

**If the OpenMythos maintainer produces an earlier dated source:** withdraw the claim as promised under section 18. Thank him publicly for the intellectual honesty. Update this document to acknowledge the new source. The falsifiability clause is load-bearing — honoring it is what makes the entire framing credible for any future priority claim.

---

*Consolidated: 24 April 2026, Sofia.*
*Author: Petar Nikolov. ORCID: [0009-0001-8669-2276](https://orcid.org/0009-0001-8669-2276).*
*DOI of parent framework: [10.17605/OSF.IO/74XGR](https://doi.org/10.17605/OSF.IO/74XGR).*
*Context: Attribution request for OpenMythos (kyegomez), released 18 April 2026.*
*Supersedes: `ARTICLE_U_THEORY_PRIOR_ART_OPENMYTHOS.md`, `ARTICLE_U_THEORY_PRIOR_ART_OPENMYTHOS_EXTENDED.md`, `OPENMYTHOS_ATTRIBUTION_PR_ARTIFACTS.md`.*
