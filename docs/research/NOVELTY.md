# Novelty Review

Status: `M1C_DISTINCT_OBJECT_SET_STOPPED`
Protocol version: `0.4.0`
Protocol recorded: `2026-07-15`
Candidate gate: `STOP_ALL_CURRENT_CLAIMS`

## Review question

Does prior work already disclose or empirically establish a single learned controller that jointly allocates explicit, limited budgets across a bounded attention workspace, versioned episodic reads and writes, fixed-size compressed-state updates, bounded recurrent compute, verification, and halting, with complete physical resource accounting and provenance interventions?

An absence of an identical title or diagram is not evidence of novelty. A component list is not a contribution unless a discriminating interaction, objective, constraint, or empirical result survives the strongest composite baseline.

## Candidate properties to test

| ID | Candidate property | Novelty burden | Minimum discriminating comparison |
|---|---|---|---|
| P-001 | One controller allocates a shared explicit budget jointly across workspace, episodic memory, compressed state, recurrent compute, verification, and halt actions | Show that prior controllers do not already cover the same action/resource space and that joint training matters | Joint controller versus fixed composite and separately trained per-resource controllers at matched budgets |
| P-002 | Episodic mutations are versioned and transactional, with provenance bound immutably to retained content | Show a technical distinction from recurrent memory, kNN memory, neural long-term memory, and agent memory/versioning systems | Insert/supersede/revoke/expire/rollback tasks plus provenance-only interventions |
| P-003 | The controller is evaluated as a constrained resource allocator rather than only as a quality router | Show complete accounting beyond theoretical FLOPs or parameter count | Pareto fronts including indexing, transfers, writes, storage, compilation, warm-up, latency, HBM, and energy |
| P-004 | The full system creates an interaction unavailable from any component alone | Reject additive assembly as the explanation | Full factorial ablations and fixed composite baseline, with preregistered interaction analysis |

## Initial screen results

The M0 screen opened and read 27 primary records across workspace, recurrent-memory, explicit-memory, state-space, adaptive-compute, agent-memory, transactional-memory, and resource-routing families. It is not the completed M1 systematic review: database result counts, deduplication, patent searching, and a closed forward/backward snowball iteration remain outstanding.

The screen rejects the broad architecture-novelty claim:

- HOLA already combines a fixed recurrent state with a bounded exact KV memory and a write-retention rule.
- Adaptive Loops and Memory in Transformers combines learned halting with gated local/global memory, while Universal Transformers Need Memory directly studies substitution between state capacity and ponder depth.
- Sparse Delta Memory learns sparse reads and writes to a large explicit state under iso-parameter and iso-FLOP comparisons.
- MemOS covers memory scheduling, provenance, versioning, lifecycle operations, transactional pipelines, and rollback at the systems layer.
- Mixture-of-Recursions couples learned recursive depth to selective cache traffic; CAT and Engram already study controllable or optimized memory-compute operating points.

Together with the older shared-workspace, external-memory, recurrent-memory, SSM, and adaptive-computation lines, these records make a near-complete composite constructible from disclosed mechanisms. Constructing that composite is not a contribution.

The only surviving research question is narrower: under matched controller capacity and complete physical accounting, can one non-factorizing per-instance policy coordinate mutable versioned episodic I/O, fixed compressed state, recurrent compute, verification, and halting better than the same components with fixed routing and independently trained resource controllers?

This is an unsupported hypothesis, not a positive novelty finding. It remains eligible only if a preregistered causal coordination interaction or an independently useful new benchmark/resource-accounting result survives the strongest composite.

## M1 results

M1 closes both contribution routes retained by the initial screen.

### The narrowed mechanism is reducible and directly anticipated

The complete state, typed action union, transition rules, and resource vector form a constrained POMDP, or a CMDP after state or belief augmentation. Adding remaining resource to the state gives a budgeted MDP. For any joint stochastic policy over typed operations, ordinary marginalization and conditioning gives the exact decomposition

\[
\pi(k,du\mid h)=\rho(k\mid h)q_k(du\mid h).
\]

An arbiter plus conditional action heads can therefore preserve the same observations, action support, feasibility mask, and trajectory distribution. "Non-factorizing" changes when actions are split, merged, or relabeled, so it is not a behavioral invariant. The candidate specifies no new learning algorithm, guarantee, lower bound, or semantic property that escapes this reduction.

The remaining learned topology is nearly explicit in primary work:

- [UMA](https://arxiv.org/abs/2602.18493) uses one end-to-end policy, a compact core summary, a mutable structured memory bank, CRUD-like tools, iterative tool use, and a terminal answer action. It also compares unified and decoupled training.
- [GRU-Mem](https://arxiv.org/abs/2602.10560) learns recurrent memory-update and exit gates with dedicated reinforcement signals.
- [AgeMem](https://arxiv.org/abs/2601.01885) integrates long- and short-term memory management into the policy through typed memory tools.
- [Memory-R1](https://arxiv.org/abs/2508.19828) learns ADD, UPDATE, DELETE, and NOOP memory operations and a separate memory-use policy.
- [Constrained Policy Optimization](https://proceedings.mlr.press/v70/achiam17a.html) and [Budgeted Reinforcement Learning in Continuous State Space](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html) establish the generic constrained and runtime-budgeted control objects.

The proposed coordination factorial could measure information access, representation sharing, or credit assignment in a finite implementation. It cannot establish a new policy class, and a positive average delta would not by itself satisfy the anti-assembly gate.

### No independent empirical phenomenon survives

WAIN-Core aggregates temporal operations already isolated by dynamic-memory work. Ledger-QA in UMA, [AMemGym](https://openreview.net/forum?id=sfrVLzsmlf), [Memora](https://arxiv.org/abs/2604.20006), and [Supersede](https://arxiv.org/abs/2606.27472) cover continuous updates, evolving state, obsolete-memory penalties, and supersession. The [bi-temporal Engram](https://arxiv.org/abs/2606.09900) covers append-only episodes, provenance, supersession chains, and point-in-time filtering.

The Joint Memory Machine cannot carry the causal claim because its admission rule encodes the need for the proposed components. Removing that ontology reduces it to component-neutral evolving-state tracking already covered by the closest benchmarks.

Complete resource accounting is mandatory for valid comparisons but is not a new contribution in this formulation. [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448) profiles construction, retrieval, generation, latency, HBM, power, and energy across ten systems. [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775) compares twelve systems across storage, extraction, routing, maintenance, update correctness, long-horizon stability, and cost-performance. Adding unmeasured axes without a new intervention or conclusion-changing law would improve rigor, not create a new empirical phenomenon.

### Feasibility reinforces, but does not create, the stop decision

The minimum mechanism study requires matched fixed and separated controllers, equal information access, randomized multi-resource prices, a full observation-by-objective factorial, and replication. The minimum systems study requires reproducible adapters and lifecycle telemetry across approximately ten to twelve heterogeneous memory systems. No written compute, instrumentation, energy, storage, or labor budget supports either design. The gate would still be `STOP` if resources were unlimited because the distinct contribution is absent.

### Search limitations do not support an absence claim

The M1 closeout retained twelve exact free-text queries, direct-resolution bundles, normalized primary records, version chains, and one targeted backward/forward cycle. It did not retain stable per-query result totals, a complete initial-title list, abstract-only exclusion counts, or every query from the interrupted architecture pass. Those fields are `NON DISPONIBLE`, not reconstructed estimates.

M1 therefore makes no exhaustive-search or absence-of-prior-art claim. The current routes stop because read primary records positively anticipate the decisive mechanisms and empirical phenomena, and because the proposed policy object reduces exactly to known constrained-control form. The separate directional route cannot inherit this incomplete search as evidence of originality.

## Preregistered search plan

Historical status: the following plan was recorded before M1. Its execution was incomplete in the fields identified above, so it is preserved as protocol history rather than represented as a completed systematic-review flow.

### Sources

Search primary records in arXiv, ACL Anthology, PMLR, OpenReview, NeurIPS proceedings, ACM Digital Library, IEEE Xplore, and official project repositories. Crossref and OpenAlex may be used for metadata and forward-citation discovery, but final support must point to a primary paper or official record where available.

### Search window

- Coverage: database inception through `2026-07-14`.
- Initial execution target: M1 issue, after this protocol is merged.
- Update search: immediately before protocol freeze and immediately before manuscript submission.

### Query families

Queries are case-insensitive and adapted only for database syntax. Every adaptation and result count must be logged.

1. `("global workspace" OR "shared workspace" OR "active workspace") AND (transformer OR attention OR neural)`
2. `(transformer OR language model) AND ("external memory" OR "episodic memory" OR "persistent memory" OR "memory transformer")`
3. `(attention AND (Hopfield OR "associative memory"))`
4. `("state space model" OR SSM OR Mamba) AND (attention OR memory OR hybrid)`
5. `("adaptive computation" OR "ponder" OR "dynamic depth" OR recurrent) AND (transformer OR language model)`
6. `(router OR controller OR policy) AND (memory AND compute AND budget)`
7. `(versioned OR temporal OR transactional OR revoke OR rollback) AND (neural memory OR agent memory OR language model)`
8. `(provenance OR citation OR source attribution) AND (memory OR retrieval) AND (language model OR transformer)`
9. `(Pareto OR "resource allocation" OR "compute budget") AND (attention OR memory OR transformer)`

### Seed set

The supplied research program names the following seeds. They are search inputs, not verified evidence: Attention Is All You Need; Hopfield Networks Is All You Need; Shared Global Workspace; Memory Transformer; Recurrent Memory Transformer; Memorizing Transformers; Mamba; Mamba-2; Jamba; Samba; Hymba; Titans; ATLAS; Universal Transformer; Adaptive Computation Time; PonderNet; Universal Transformers Need Memory; Zoology/MQAR; RULER; BABILong; NoLiMa; MemGPT; and versioned agent-memory systems.

### Snowballing

For every included seed and every newly included paper:

1. inspect references for backward snowballing;
2. inspect citing records for forward snowballing;
3. inspect official repository documentation and associated technical reports;
4. record the discovery path and stop only after one full iteration yields no new eligible mechanism family.

### Inclusion criteria

- primary research paper, official proceedings record, or official repository/specification;
- implements, formalizes, or evaluates at least one candidate mechanism or a directly competing composite;
- sufficient technical detail to map overlap and differences;
- accessible full text or official specification;
- any language, provided metadata and relevant passages can be verified.

### Exclusion criteria

- commentary, marketing material, unsourced summaries, or duplicate versions with no relevant change;
- memory used only as a loose metaphor without a mechanism;
- retrieval-augmented generation work with no relevant memory-management, routing, compute-allocation, or provenance mechanism;
- unavailable full text after a documented access attempt;
- benchmark leaderboard entries without an attributable method description.

### Deduplication and versioning

Deduplicate first by DOI, then arXiv identifier, then normalized title and author set. Retain a version chain when claims or experiments differ. Prefer the final peer-reviewed version for claims and preserve the arXiv version when it contains material omitted from proceedings.

## Extraction schema

For each included work record architecture, state variables, persistence semantics, read/write actions, versioning, provenance, controller inputs/actions, budget constraints, adaptive-depth bounds, training objective, complexity assumptions, resource accounting, datasets, baselines, ablations, effect sizes, limitations, exact locators, and verification status.

## Decision rule

- `GO`: at least one candidate property remains technically distinct and has a feasible experiment that can distinguish it from the strongest known composite.
- `PIVOT`: the broad architecture is known, but a narrower causal interaction or genuinely new empirical phenomenon, benchmark, or physical-resource result remains testable against the strongest fixed and separately controlled composites.
- `STOP`: no technically meaningful distinction survives, no feasible experiment can identify it, or the prospective paper would amount only to assembling, renaming, or narratively reframing prior work.

An architecture diagram, shared vocabulary, or new combination of known modules cannot satisfy this gate. Before any paper claim is authorized, the project must preregister the expected observation that existing components and their strongest composite cannot already explain.

## Initial gate decision

Decision: `PIVOT`.

1. Stop the current broad architecture-novelty claim.
2. Carry only the narrow constrained-policy question into a full M1 review.
3. Require a HOLA + Mixture-of-Recursions + MemOS + adaptive-stop composite, plus fixed and separately trained controller baselines.
4. Preregister randomized resource-price interventions and a matched 2x2 coordination study before implementation.
5. Convert the decision to `STOP` if no practically meaningful interaction or independently useful empirical contribution remains.

The detailed evidence and locators are recorded in the Terra-Evidence and Sol-Theory handoffs. This initial decision authorizes a dedicated M1 systematic-review issue only; it does not authorize M2 formalization, benchmark implementation, model implementation, or training.

## M1 final gate decision

Decision on current contribution routes: `STOP`.

1. Stop the non-factorizing constrained-policy mechanism claim.
2. Stop WAIN-Core and Joint Memory Machine as proposed original benchmark claims.
3. Stop complete accounting or ranking reversal as a standalone contribution without a new causal intervention, predictive law, or conclusion-changing result.
4. Keep the original architecture article and working title `NOT_ELIGIBLE`.
5. Do not implement, train, or draft a manuscript from these stopped routes.

Program decision: `PIVOT` to a separately audited direction-setting technical thesis requested by the repository owner.

That pivot must contribute an implementation-neutral transition framework for future LLM systems, technical contracts, measurable regime boundaries, and falsifiable predictions. It is not currently established as novel. It returns `STOP` if it reduces to a survey, taxonomy, manifesto, maturity model, migration diagram, or renamed synthesis of memory-OS, agent-OS, stateful-agent, long-context, test-time-learning, and systems-roadmap literature.

## M1b final gate decision

Decision: `STOP`.

M1b audited the owner's direction-setting objective as a separate candidate contribution. It operationalized pre-outcome workload descriptors `Omega`, guarantee contracts `G`, vector resource envelopes `B`, ground-truth adequacy `Adeq`, empirical certification `Cert`, pairwise comparison `Cmp`, an ideal selector `T*`, and a possible calibrated estimator `T_hat`. It also registered five falsifiable prediction candidates, counterexample regimes, and five minimum discriminating designs. Operationalization established testability, but it did not establish novelty.

The [State-Aware Runtime working paper](https://doi.org/10.33774/coe-2026-vt9t2-v2) already argues for replacing prompt accumulation with an explicit runtime-governance layer built around canonical state, validation, commit, rollback, recovery, permissions, and audit. The [PLACEMEM arXiv systems position and prototype](https://arxiv.org/abs/2607.04089v1) independently proposes a compute-aware and correction-aware memory plane with versioned validity, invalidation, reusable runtime state, and routing. These public records directly anticipate the broad direction. Reorganizing it as `Omega/G/B/Adeq/Cert/Cmp/T*/T_hat` changes vocabulary, not an observable boundary.

The formal shell also reduces to existing systems and decision-theory objects. Assume-guarantee contracts and implementation-neutral QoS specify environments, obligations, and refinement. Vector-resource allocation and working-set theory supply multidimensional budgets, locality, and feasibility. Temporal databases and W3C PROV supply valid-time, transaction-time, generation, use, and invalidation constraints. Evidence certification, Pareto comparison, value of computation, and reject-option theory supply evaluation status, efficiency, adaptive computation, and abstention. The ideal `T*` shell is generic, while no LLM-specific `T_hat`, estimator, theorem, invariant, or transportable coefficient is supplied.

The registered predictions do not rescue the article route:

1. The context-only negative regime is `ANTICIPATED` by workload-dependent stateful-system studies and selective-memory comparisons.
2. The current-version feasibility statement is `ANTICIPATED`; it is an information-access bound, not evidence for persistence architecture superiority.
3. The fixed-versus-adaptive compute boundary is `ANTICIPATED` by value-of-computation metareasoning and cost-quality routing.
4. The validity-before-compute residual is `UNSUPPORTED_NOT_DISTINCT`: STALE, A-TMA, PLACEMEM, PersistBench, X-Router, and generic metareasoning reconstruct its conceptual motivation, while no new quantitative rule is specified here.
5. Abstention under non-identifiability is `ANTICIPATED` by generic reject-option theory.

The search record contains twelve preregistered query families, four narrow state-validity-by-compute queries, fifteen exact identifier or canonical-record resolutions, and three independent reduction audits. The broad queries were only partially screened, and their per-title inclusion and exclusion counts are `NON DISPONIBLE`; this is not an exhaustive systematic review. This decision makes no absence-of-prior-art claim. `STOP` rests on positive direct collisions and formal reductions, each of which is sufficient to defeat the candidate originality claim.

The direction may be useful engineering guidance, but usefulness is not the project's publication criterion. Under the owner's anti-rewrite requirement, a managed-state manifesto, transition roadmap, maturity model, survey, or unified notation article would be a narrative synthesis of the cited systems. The direction-setting article is therefore `NOT_ELIGIBLE`. No manuscript, framework implementation, benchmark run, model training, or paid compute is authorized from issue #5.

The research program has no surviving article route. Reopening requires a new, independently motivated technical question that identifies a `DISTINCT_CANDIDATE` before implementation and survives label substitution, strongest-composite reduction, generic-theory reduction, at least one decisive falsifier, and an affordable discriminating design.

## M1c final gate decision

Decision: `STOP`.

M1c generated sixteen independently motivated technical objects instead of narrowing or renaming the M1b transition shell. Three review lanes covered revision and replay formalization, shared-state systems, and longitudinal memory dynamics. Every object was given a decisive falsifier, a negative regime, a strongest composite, a generic reduction, and a minimum discrimination burden.

The formal candidates reduce to dynamic dependence graphs and change propagation, causal intervention, provenance, approximate trace equivalence, lossy coding, and reject decisions. The systems candidates collide with Cordon semantic transactions, CoAgent serializable repair, verified anomaly hierarchies, Rosetta Memory cross-LLM adaptation, AFTER procedural transfer, and SkillGuard executable drift contracts; decision confluence is exactly I-confluence under an application invariant. CausalFlow supplies localized counterfactual repair, not a proof of the proposed global minimum-repair objective. The dynamics records observe self-reinforcing errors, longitudinal exposure effects, order sensitivity, and repeated-compaction amplification; the proposed reproduction and divergence quantities remain generic branching and stability summaries rather than directly reported objects. Ziegler additionally supplies adaptive-agent hysteresis under target reversal without reset, while Hyperproperties supplies the two-trace probabilistic non-interference form. The exact LLM `A -> B -> A` cell is unreported but `ANTICIPATED_BY_COMPOSITE`, not a new phenomenon class.

The final reset-versus-persistent ranking residual also fails. No examined record reports the exact reset-per-episode versus persistent-stream ranking inversion. Artifact Ecology anticipates the inheritance protocol, ShiftBench already reports longitudinal memory-policy selection inversions, MemDelta reports controlled comparison reversals and recommends rank-order stability checks, and time-series potential outcomes supply the path contrast. The residual is therefore `ANTICIPATED_BY_COMPOSITE`, not `ANTICIPATED_DIRECTLY`: observing the exact cell would extend an anticipated phenomenon without adding a mechanism, estimator, invariant, or general law.

The M1c search is targeted and non-exhaustive. `STOP` rests on positive primary-record collisions, explicit strongest-composite anticipations, generic reductions, and the absence of a specified distinct technical object within the candidates, not on search silence. Zero candidates are `DISTINCT_CANDIDATE`; no experiment or article is authorized. The full record is in `M1C_CANDIDATE_REGISTER.md`, `M1C_SCOPING_LOG.md`, and Decision 0005.
