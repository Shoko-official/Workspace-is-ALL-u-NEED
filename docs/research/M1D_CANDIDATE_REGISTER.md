# M1d Non-Factorizing State-Compute Candidate Register

Cutoff: `2026-07-15`
Issue: [#13](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/13)
Gate result: `STOP`
Candidates tested: `24`
Surviving `DISTINCT_CANDIDATE` objects: `0`

## Gate

M1d searched outside M1C-C01 through M1C-C16 for a mechanism, estimator,
invariant, bound, theorem, or predictive law whose state-compute interaction
could not be reconstructed by a strong separable composite. A candidate had to:

1. specify a decisive falsifier and a negative regime;
2. survive direct prior art and the strongest positive composite;
3. survive substitution of the LLM labels by the underlying statistical,
   control, causal, database, scheduling, coding, or systems object;
4. predict a held-out result unavailable to a state manager plus a compute
   router; and
5. state a minimum discriminating burden before implementation.

Operational coupling is not sufficient. A memory decision and a compute
decision can interact strongly while remaining an ordinary joint policy or a
composition of known mechanisms.

### Unrestricted behavioral factorization

At a fixed history `h`, for any joint behavioral distribution over a governed
memory action `m` and a compute action `c` on discrete or standard Borel spaces,

\[
\pi(m,c\mid h)
=
\pi_M(m\mid h)\,\pi_C(c\mid h,m).
\]

An unrestricted manager may sample `m`, transmit `(h,m)`, and let the router
sample `c`. A regular conditional exists and is determined `pi_M`-almost surely;
its values on a `pi_M`-null set are immaterial. In the discrete case, this means
the conditional may be assigned arbitrarily to zero-marginal actions. This
reproduces only the fixed-history law of `(m,c)`. It assumes unrestricted
information passage and does not imply
causal-order, computational-cost, latency, private-information, learning,
optimization, or sample-efficiency equivalence.

Accordingly, a claim of intrinsic *behavioral* non-factorization is not
identified unless the comparator interface is restricted before evaluation,
including message size, decision order, observations, feedback, shared
randomness, and training information. A causal, computational, or learning
separation instead needs its own matched comparator, estimand, or bound. The
factorization is the probability chain rule, not a new theorem. None of the
candidates below supplies and justifies a restriction under which its claimed
separation follows.

## Candidate register

### Formal identification and bounds

#### M1D-C01: Anytime-valid safe-write commit

- Technical object: an e-process accumulates verifier losses for a proposed
  write and commits at the first stopping time whose evidence crosses
  `1 / delta`, giving an anytime false-commit bound under the declared
  martingale assumptions.
- Decisive falsifier: unsafe-commit probability exceeds `delta` while the
  filtration, bounded-loss, and predictability assumptions hold.
- Negative regime: uninformative verifier samples, hidden feedback,
  misspecified abstractions, or verification as costly as regeneration.
- Reduction: confidence sequences and e-processes followed by a shield or
  selective reject. TrustMem already compares candidate transitions from one
  memory state with a transition verifier (`EV-0086`; `EV-0100`).
- Minimum discrimination: prove a write guarantee unavailable from an
  anytime-valid test plus transition shield under the same information.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C02: Lifetime persistent value of computation

- Technical object:
  \[
  \operatorname{LVOC}(c\mid x)
  =-\kappa(c)+\mathbb E[V^*(T_c(x,o))]-V^*(x),
  \]
  where the hyperstate `x` contains environment state, persistent memory, and
  epistemic state.
- Decisive falsifier: an augmented-state Bellman or meta-MDP baseline
  reconstructs every predicted allocation and ranking.
- Negative regime: no reuse, zero discount, disabled writes, known dynamics,
  or an uninformative computation.
- Reduction: under a correctly specified Markov hyperstate and tractable action
  model, dynamic value of computation represents internal actions by their
  effect on all later decisions; persistent memory can be included in that
  state (`EV-0087`; `EV-0088`). This is a representation, not an automatic
  identification or computation result.
- Minimum discrimination: predeclare a bounded state, observation, or
  computational representation and prove that no member is sufficient, or give
  a new identification or efficiency bound inside that class.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C03: Compute-induced memory-selection bias with doubly robust correction

- Technical object: sequential importance weighting or doubly robust off-policy
  evaluation for a history in which compute controls memory admission and
  admitted items alter later observations.
- Decisive falsifier: bias or confidence-interval undercoverage exceeds the
  registered tolerance under randomized admission with shadow outcomes.
- Negative regime: zero propensity, hidden common causes, non-mixing streams,
  missing-not-at-random labels, or cross-agent interference.
- Reduction: under recorded propensities, positivity, consistency, and
  sequential exchangeability, adaptive doubly robust estimation supplies the
  ordinary correction. Hidden-state regimes require additional POMDP/OPE
  assumptions rather than following from adaptive DR alone. Memory-R2 directly
  observes that divergent writes create different future environments and uses
  local rerollouts from a shared memory state (`EV-0089`; existing `EV-0073`).
- Minimum discrimination: an identified estimand under a regime where the
  sequential DR or POMDP assumptions provably cannot identify it.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C04: Compute-to-write mediated future-compute effect

- Technical object: a longitudinal interventional indirect effect in which
  current compute changes the write trajectory and the write trajectory changes
  later compute demand.
- Decisive falsifier: randomized compute plus randomized write override yields a
  held-out mediated effect incompatible with the estimator.
- Negative regime: disabled writes, no reuse, deterministic writes independent
  of compute, positivity failure, or hidden time-varying confounding.
- Reduction: substitute compute for treatment, writes for the longitudinal
  mediator, and future compute for the outcome in the stochastic mediation
  g-formula (`EV-0090`).
- Minimum discrimination: identify a path effect outside longitudinal
  stochastic mediation under the same intervention semantics.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C05: Revocation storage-recompute frontier

- Technical object: a minimax frontier between retained provenance bits and
  recomputation calls needed to match fresh execution after deletion.
- Decisive falsifier: a protocol below the claimed frontier satisfies the same
  distributional guarantee.
- Negative regime: full archives, full recomputation, independently deletable
  records, or a bounded simple hypothesis class.
- Reduction: ticketed machine unlearning and agentic dependency closure already
  trade retained state against deletion-time work (`EV-0091`; `EV-0092`).
- Minimum discrimination: a new semantic complexity parameter with a proved
  lower bound not inherited from unlearning or communication complexity.
- Disposition: `OUT_OF_SCOPE_RECYCLING`. It also re-enters the forbidden M1c
  repair and dependency-closure family.

#### M1D-C06: Validation-debt potential

- Technical object: a potential
  `Phi_t = sum_i exposure_i * violation_risk_i * repair_cost_i` charges cheap
  unverified commits now against expected validation or repair later.
- Decisive falsifier: violation of the telescoping amortized inequality, or
  equal-potential histories with unboundedly different optimal future cost.
- Negative regime: read-only memory, free perfect validation, no reuse, or
  invalid marginal-risk factorization.
- Reduction: the proposed guarantee is the ordinary potential method plus
  integrity-maintenance accounting. No state-compute theorem follows from the
  chosen scalar.
- Minimum discrimination: prove that the scalar is sufficient for optimal
  scheduling across a nontrivial governed-state class.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

#### M1D-C07: Governance-constrained adaptive acquisition

- Technical object: adaptive submodular acquisition in which computation
  outcomes determine both what may persist and which computation runs next.
- Decisive falsifier: increasing conditional marginal value under a refined
  partial realization, or greedy performance below the claimed bound.
- Negative regime: complementary evidence, poisoning, revocation interactions,
  or non-downward-closed governance constraints.
- Reduction: when adaptive submodularity and the declared feasibility
  conditions hold, this is adaptive submodular optimization under partial
  observability and knapsack or matroid constraints (`EV-0093`).
- Minimum discrimination: a new approximation guarantee outside the existing
  adaptive-submodular conditions.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C08: Governance-recourse dynamic regret

- Technical object: dynamic regret over a persistent memory-configuration path,
  with compute lookahead and a cost for mutation or revocation.
- Decisive falsifier: the claimed regret or lookahead-decay bound fails under
  its registered smoothness, convexity, and forecast assumptions.
- Negative regime: arbitrary adversarial costs, no switching cost, stationary
  state, or inaccurate unbounded forecasts.
- Reduction: under the declared convexity, smoothness, forecast, and switching-
  cost assumptions, this is online optimization with predictions and switching
  costs, or model predictive control (`EV-0094`).
- Minimum discrimination: a lower or upper bound that depends on a new governed
  state quantity rather than relabeled path variation.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### Learning dynamics and adaptive compute

#### M1D-C09: Durable-compute amortization law

- Technical object: discounted saved recomputation minus construction,
  verification, reuse, and invalidation cost over a future horizon.
- Decisive falsifier: its sign fails to predict the optimal policy across held-out
  reuse, drift, and horizon regimes.
- Negative regime: no reuse, rapid drift, or prohibited writes.
- Strongest composite: phase-aware agent-memory characterization already
  measures construction, retrieval, generation, amortization, freshness, and
  query volume, while dynamic value of computation supplies the lifetime
  objective (existing `EV-0041`; `EV-0087`).
- Minimum discrimination: a transportable law not reconstructed by amortized
  caching plus dynamic value of computation.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C10: State-quality-conditioned compute elasticity

- Technical object: the factorial interaction between valid versus invalid
  memory and low versus high test-time compute.
- Decisive falsifier: a zero interaction on held-out tasks and architectures.
- Negative regime: memory is unread, state is perfectly validated, or compute
  performance saturates.
- Strongest composite: ReasoningBank Section 4.4 varies memory mechanisms and
  scaling and reports different scaling returns; it does not run the exact
  valid-versus-invalid factorial (`EV-0095`).
- Minimum discrimination: a mechanism or invariant beyond the already measured
  memory-quality by compute interaction.
- Disposition: `OUT_OF_SCOPE_RECYCLING`. The ReasoningBank result is a secondary
  composite collision, but the candidate is inadmissible first because it
  restates validity-before-compute as a factorial score.

#### M1D-C11: Deferred credit of a persistent write

- Technical object: the causal discounted effect of a current write on future
  task utility and compute cost under forced reuse.
- Decisive falsifier: no downstream effect when the committed item is actually
  retrieved.
- Negative regime: single-episode tasks or no future retrieval.
- Strongest composite: MemoPilot formulates memory updates as a multi-turn
  decision problem and learns them from turn-wise future rewards, while
  Memory-R2 supplies shared-state local rerollouts (`EV-0096`; existing
  `EV-0073`). Neither record identifies the exact forced-reuse causal effect.
- Reduction: under consistency, positivity, and sequential exchangeability,
  forced write and forced reuse are longitudinal interventions and their effect
  on later utility and compute is an ordinary g-formula or path-effect estimand
  (`EV-0090`).
- Minimum discrimination: a credit estimator or guarantee unavailable from the
  longitudinal causal estimand and shared-state rerollout controls.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C12: Compute-verification threshold for state refresh

- Technical object: refresh when expected future memory improvement exceeds the
  refresh compute price.
- Decisive falsifier: no stable threshold or no downstream effect from refresh.
- Negative regime: stationary state, free refresh, or certain validity.
- Strongest composite: AdaMEM dynamically refreshes short-term strategy memory
  and reports the token-efficiency versus adaptation frontier across inference
  compute levels; dynamic value of computation supplies the expected-benefit
  minus compute-price decision rule (`EV-0097`; `EV-0087`; `EV-0088`).
- Minimum discrimination: a threshold law unavailable from value of information
  or value of computation and not implemented by adaptive refresh.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C13: Build-compute by read-compute response kernel

- Technical object: a held-out `2 x 2` interaction between compute spent building
  a committed artifact and compute spent using it later.
- Decisive falsifier: an additive kernel on the held-out joint cell.
- Negative regime: independent tasks, no commit, or no retrieval.
- Strongest composite: ReasoningBank generates multiple trajectories to curate
  future memory and then uses that memory during later scaling; Zuo et al.
  jointly change the generation distribution through an evolving successful
  demonstration pool while reallocating samples (`EV-0095`; `EV-0098`).
- Minimum discrimination: a law beyond non-additivity that neither closed loop
  predicts.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C14: Correlated-consensus overcompute contamination

- Technical object: more correlated self-judged rollouts raise artificial
  confidence, increase false commits, and make later memory quality non-monotone
  in inference compute.
- Decisive falsifier: false commits do not rise with rollout count, or an
  independent verifier does not remove the effect.
- Negative regime: independent rollouts, perfect external proof, or disabled
  writes.
- Strongest composite: ReasoningBank supplies scaled trajectory aggregation;
  Useful Memories directly reports memory utility rising then falling below the
  no-memory baseline under repeated consolidation; TrustMem verifies candidate
  transitions; M1c already covers contamination feedback (`EV-0095`; `EV-0099`;
  `EV-0100`; existing `EV-0076`).
- Minimum discrimination: an identified mechanism not reconstructed by noisy
  scaling, faulty consolidation, verifier quality, and feedback propagation.
- Disposition: `OUT_OF_SCOPE_RECYCLING`.

#### M1D-C15: Self-sealing undercompute trap

- Technical object: false persistent state increases confidence, causes early
  stopping, suppresses audits, and becomes approximately absorbing.
- Decisive falsifier: audits do not decline with false confidence, or adaptive
  stopping is no more persistent than a fixed audit schedule.
- Negative regime: forced audits, read-only state, or a trusted external oracle.
- Strongest composite: biased-observation POMDP control plus TrustMem transition
  supervision and the M1c contamination cycle reconstruct the trap
  (`EV-0100`; existing `EV-0076`).
- Minimum discrimination: a new stability theorem or phase boundary outside the
  POMDP and feedback model.
- Disposition: `OUT_OF_SCOPE_RECYCLING`.

#### M1D-C16: Prospective-intention compute opportunity cost

- Technical object: a latent persistent obligation consumes reasoning capacity,
  while a difficult primary task consumes capacity needed to recall the
  obligation.
- Decisive falsifier: no loss as intention load or primary reasoning burden
  rises.
- Negative regime: one explicit cue, external reminders, or ample capacity.
- Strongest composite: TriggerBench directly finds a reasoning-dependent
  prospective-memory precision-recall tradeoff, degradation under concurrent
  requests, and lower recall on long or failed reasoning trajectories
  (`EV-0101`). Its Appendix C.3 reports no upstream AIME-accuracy perturbation
  from one inserted prospective-memory constraint; intention load was not varied.
- Minimum discrimination: a positive load-dependent reverse impairment plus an
  identified mechanism, estimator, or bound beyond a generic shared-capacity
  account.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

### Runtime mechanisms and governed transitions

#### M1D-C17: Compute reservation by persistent obligation

- Technical object: a versioned obligation with trigger, deadline, budget, and
  provenance reserves compute when its schedulability margin becomes critical.
- Decisive falsifier: an obligation is missed under a schedulable load, or false
  triggers exceed the registered bound.
- Negative regime: overload, unobservable triggers, or incompatible obligations.
- Reduction: prospective memory or event-condition-action state plus sporadic-
  server real-time scheduling and QoS. TriggerBench supplies the LLM
  prospective-memory failure class; Sprunt, Sha, and Lehoczky supply the primary
  schedulability object (`EV-0101`; `EV-0115`).
- Minimum discrimination: a schedulability theorem requiring an LLM-specific
  state-compute object rather than ordinary jobs and deadlines.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1D-C18: Proof-carrying state with incremental verification

- Technical object: each state value carries provenance and a certificate;
  updates incrementally revalidate only the changed dependency cone.
- Decisive falsifier: an invalid state is accepted, or incremental proof work is
  no cheaper than complete verification.
- Negative regime: undecidable natural-language properties, hidden
  dependencies, or proof generation dominating execution.
- Strongest composite: proof-carrying code plus incrementally verifiable
  computation supply the generic certificate object. SAVeR verifies and repairs
  belief state before action commitment, but does not implement incremental
  dependency-cone certificates (`EV-0112`; `EV-0113`; `EV-0106`).
- Minimum discrimination: a soundness or complexity result not reconstructed by
  incremental certificates plus dependency invalidation.
- Disposition: `OUT_OF_SCOPE_RECYCLING`. Certificate, dependency, and
  incremental-revalidation objects re-enter the forbidden M1c families; the
  proof-carrying composite is a secondary reduction.

#### M1D-C19: Dual-consensus persistent commit barrier

- Technical object: commit only when action consensus and memory-transition
  validity both exceed separate thresholds.
- Decisive falsifier: harmful writes pass both thresholds, or the dual barrier
  does not improve over the strongest single barrier.
- Negative regime: correlated rollouts or a shared failing verifier.
- Strongest composite: TrACE provides adaptive agreement, TrustMem supplies a
  same-state memory-transition verifier, and MemRouter provides memory routing
  (`EV-0107`; `EV-0100`; `EV-0108`).
- Minimum discrimination: a guarantee or held-out prediction unavailable from
  the literal conjunction of the two gates.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C20: Durable deferred reasoning continuation

- Technical object: persist a continuation containing program counter, hidden or
  KV state, read/write sets, randomness, receipts, and versions; resume if the
  boundary remains valid and otherwise replay.
- Decisive falsifier: divergence from uninterrupted execution inside the
  captured boundary, or no reuse gain.
- Negative regime: non-idempotent effects, opaque services, or long external
  drift.
- Strongest composite: INFERCEPT explicitly chooses preserve, swap, discard, or
  recompute for interrupted KV/context state, and Preble jointly schedules
  colocated prefix state and compute (`EV-0104`; `EV-0105`). They do not provide
  the proposed semantic boundary over read/write sets, randomness, receipts,
  and versions.
- Minimum discrimination: an equivalence or performance result outside
  checkpoint/continuation, cache scheduling, and replay.
- Disposition: `OUT_OF_SCOPE_RECYCLING`. Its semantic-boundary extension
  re-enters the forbidden M1c replay and repair family; the runtime records are
  a secondary partial anticipation.

#### M1D-C21: Consolidation-driven retirement of compute

- Technical object: consolidation quality controls a router that progressively
  replaces episodic attention with semantic state and reduces compute.
- Decisive falsifier: compute does not decline after valid consolidation, or
  quality is not preserved.
- Negative regime: nonstationarity, rare events, or contradictions.
- Strongest composite: CRAM directly routes from consolidation quality and its
  authors report decreasing attention plus a static-routing lower bound for
  recurring patterns (`EV-0103`). The preprint's unresolved macro and
  anonymized artifact keep the theorem claim non-decision-critical.
- Minimum discrimination: a different law or bound not entailed by CRAM plus
  ordinary invalidation after drift.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1D-C22: Co-scheduling semantic state residence and compute

- Technical object: residency decisions jointly charge queue delay, prefill,
  eviction, reuse, semantic priority, pinning, and governed lifetime.
- Decisive falsifier: semantic annotations improve no latency-memory frontier or
  violate pinned regions.
- Negative regime: uniform reuse, thrashing, or incorrect annotations.
- Strongest composite: Preble jointly places prefix state and computation;
  INFERCEPT schedules preserved, swapped, and recomputed state; MemDecay and
  Pancake supply semantic decay and multi-tier placement (`EV-0105`; `EV-0104`;
  `EV-0109`; `EV-0110`).
- Minimum discrimination: a state role whose scheduling behavior is not a cache,
  working-set, placement, or QoS decision.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C23: Reuse-shadow-priced compute investment

- Technical object: allocate more current compute to artifacts with higher
  expected future fan-out, charging current cost against future reuse value.
- Decisive falsifier: allocation is insensitive to randomized fan-out or fails
  to amortize over realized reuse.
- Negative regime: unpredictable reuse, rapid drift, or dominant storage cost.
- Strongest composite: BudgetMem routes multiple memory modules across low,
  medium, and high compute tiers from query and intermediate state; A-MAC scores
  future utility for admission; dynamic value of computation supplies the
  lifetime objective (`EV-0102`; `EV-0111`; `EV-0087`).
- Minimum discrimination: a lower bound or identifiable fan-out estimator under
  a preregistered partial-information or bounded-computation class that is not
  supplied by the augmented objective.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1D-C24: Epistemic compute for governed-state choice

- Technical object: select an information-gathering rollout or tool because its
  observation changes the belief over which state version may be committed,
  even when its immediate reward is lower.
- Decisive falsifier: the probe has no future information value or the belief is
  not calibrated.
- Negative regime: non-identifying observations, excessive exploration cost, or
  adversarial dynamics.
- Reduction: belief-state POMDP value of information, with write and verify
  included in the action space (`EV-0114`; `EV-0102`). No separate dual-control
  guarantee is claimed.
- Minimum discrimination: an identification, approximation, or complexity bound
  under a preregistered belief representation or observation class, rather than
  a contradiction with an assumed complete belief state.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

## Strongest-composite result

The positive composite is substantially stronger than the original project
formulation:

1. ReasoningBank/MaTTS supplies a positive bidirectional memory by test-time
   scaling loop; with Zuo et al. it reconstructs the exact-kernel candidate as a
   composite rather than directly measuring its held-out factorial.
2. BudgetMem directly implements query- and intermediate-state-conditioned
   compute tiers for runtime memory modules; AdaMEM and MemoPilot add the
   refresh and delayed-credit ingredients without proving the candidate laws.
3. AdaMEM, MemoPilot, TrustMem, Memory-R2, Useful Memories, and TriggerBench
   cover adaptive refresh, delayed write credit, transition verification, fair
   shared-state rerollouts, non-monotone consolidation, and the primary-task-to-
   prospective-memory opportunity cost.
4. CRAM directly anticipates consolidation-conditioned compute retirement; its
   authors also state a lower bound against static routing, which is not needed
   for the disposition.
5. INFERCEPT and Preble supply preserve/swap/recompute and joint state-compute
   placement mechanisms at runtime; they partially anticipate the richer
   continuation and reconstruct the residence candidate as a composite.
6. Confidence sequences, dynamic value of computation, POMDPs, adaptive DR,
   longitudinal mediation, adaptive submodularity, online optimization,
   scheduling, and proof-carrying computation reconstruct every remaining
   formal object.

The composite need not be one implementation. The gate asks whether a new
technical object remains after the strongest reconstructive comparison. None
does. A new label, a held-out factorial cell, or a full-stack assembly cannot
turn these positive ingredients into originality.

## Minimum-design decision

No empirical design is authorized. The candidate-specific minimum burdens above
are formal non-reduction or new-guarantee burdens, not invitations to run the
listed experiments. Measuring another interaction cannot repair a failed
technical-distinctness gate.

A future candidate must first state whether it claims behavioral expressivity,
causal identification, computational complexity, online efficiency, or learning
efficiency. A behavioral separation must predeclare a scientifically intrinsic
information, communication, computation, or learning class and prove a result
inside it. Other claim types need a matched comparator and their own estimand or
bound. An augmented-state meta-MDP remains a generic representation test, not a
reason to erase a valid complexity or identification separation.

## Decision

Return `STOP` for all 24 M1d candidates.

- `DISTINCT_CANDIDATE`: `0`
- `ANTICIPATED_DIRECTLY`: C21
- `ANTICIPATED_BY_COMPOSITE`: C09, C12, C13, C19, C22, C23
- `REDUCED_TO_KNOWN_THEORY`: C01, C02, C03, C04, C07, C08, C11, C17, C24
- `UNSUPPORTED_NOT_DISTINCT`: C06, C16
- `OUT_OF_SCOPE_RECYCLING`: C05, C10, C14, C15, C18, C20

No model, benchmark, experiment, training run, implementation, or manuscript is
authorized. The negative register is governance evidence, not the requested
direction-setting article.
