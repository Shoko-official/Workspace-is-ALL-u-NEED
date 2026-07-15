# M1g Problem-First Invariant Register

Cutoff: `2026-07-15`
Issue: [#25](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/25)
Gate result: `PROPOSED_STOP`
Incident-first problems tested sequentially: `8`
Admitted objects: `0`
Surviving `DISTINCT_CANDIDATE` objects: `0`

## Gate

M1g changed the discovery unit from a proposed mechanism to an externally
observable deployment failure. Each attempt had to state the incident before
the architecture and then fix:

1. event order, observer, available information, persistent state, computation,
   intervention, and resource boundary;
2. a two-factor causal-necessity test under which removing either persistence
   or adaptive computation eliminates or materially changes the claimed result;
3. one primitive and intrinsic comparison class;
4. the strongest co-designed comparator with the same observations, state,
   randomness, transcript, work, latency, feedback, and permitted operations;
5. one exact theorem, estimand, invariant, or transportable law;
6. a decisive falsifier and a negative regime;
7. generic-label substitution and the simplest non-LLM analogue; and
8. a complete no-recycling crosswalk against all 73 M1c-M1f formulations.

The eight problems were tested sequentially. Failure of either causal-necessity
factor, direct anticipation, earlier-object recycling, generic reduction, or an
unsupported exact result ended the attempt. Search silence was never used.

## Problem register

### M1G-P01: Revocation during in-flight derived computation

- Incident and harm: a worker reads persistent version `v`, begins a variable
  amount of reasoning, `v` is revoked, and the worker nevertheless commits an
  externally visible action whose ancestry includes `v`.
- Fixed boundary: `READ(v) -> PONDER -> REVOKE(v) -> COMMIT`; the observer sees
  the revocation log and committed trace. The candidate and comparator receive
  the same versions, epochs, cancellation channel, replay input, work, and
  commit latency budget.
- Two-factor necessity: persistence supplies a revocable version, but adaptive
  reasoning is not necessary. Any delayed deterministic transaction can race
  with revocation and exhibit the same stale commit.
- Exact object: separate lineage safety from observable effect. Let
  `V_R = P(COMMIT and Anc(COMMIT) intersects R)` for revoked ancestry `R`.
  `V_R>0` violates the declared no-revoked-ancestry commit rule. Separately,
  `Delta_R = sup_(E in F_tau) |P_actual(E)-P_replay_without_R(E)|` measures an
  observable counterfactual effect on the registered trace sigma-algebra
  `F_tau`. Revoked ancestry alone does not imply `Delta_R>0`; that conclusion
  requires the two observable laws to differ.
- Strongest comparator: serialize revocation and commit, cancel in-flight work,
  invalidate descendants by dependency closure, or validate an epoch at commit
  and replay on mismatch.
- Decisive falsifier: one committed trace with ancestry intersecting `R`
  falsifies the lineage-safety invariant `V_R=0`. A stale read whose registered
  trace equals replay instead falsifies an effect-distance-only detector while
  leaving the lineage violation visible.
- Negative regime: no revocation, no derived work, or atomic epoch validation
  immediately before every effect.
- Reduction boundary: linearizability, optimistic concurrency control,
  invalidation, replay, and M1C-C01/C02/C06/C08/C11 already determine the
  object (`EV-0170`).
- Disposition: `FAILS_ADAPTIVE_COMPUTE_NECESSITY_AND_REDUCED_TO_CONCURRENCY`.

### M1G-P02: Deletion after adaptive internalization

- Incident and harm: a record is repeatedly retrieved or used for adaptation,
  the external copy is deleted, and later behavior still reveals or depends on
  the deleted subject.
- Fixed boundary: `WRITE(X) -> ADAPT(X) -> DELETE(X) -> QUERY`; the observer has
  black-box access to outputs and costs. Parameters, fast weights, caches,
  summaries, optimizer state, and dependency records are charged as state.
- Two-factor necessity: persistence identifies a deletion target and adaptive
  updates can internalize it, but the resulting problem is exactly deletion
  from learned state rather than a new persistence-compute class.
- Exact object: distinguish learning operator `A` from deletion procedure
  `D_X`. For training history `Z_T` and query kernel `K_q`,
  `R_D(X;Z_T) = sup_q TV(K_q(D_X(A(Z_T))), K_q(A(Z_T^{-X})))`.
  Removing an external row alone cannot force `R_D(X;Z_T)=0` when parameters
  or caches retain behaviorally relevant influence.
- Strongest comparator: canonical retraining on `Z_T^{-X}`, dependency-aware
  exact or approximate unlearning, and an auditor charged for the information
  needed to distinguish the two output laws.
- Decisive falsifier: a declared `D_X` that leaves at least one causally
  `X`-dependent component unchanged yet attains `R_D(X;Z_T)=0` for every
  permitted continuation and registered trace.
- Negative regime: `X` is never read or learned, all descendants are exactly
  reconstructible and removed, or the application requires only external-row
  deletion rather than behavioral deletion.
- Reduction boundary: machine unlearning, verifiable unlearning, dependency
  closure, and replay cover the constructive branch. Finite black-box audit of
  an unrestricted learner is non-identifying, while stronger behavioral audit
  carries a privacy cost (`EV-0091`; `EV-0092`; `EV-0177`).
- Disposition: `DIRECT_COLLISION_AND_REDUCED_TO_MACHINE_UNLEARNING`.

### M1G-P03: Forked continuation uniqueness

- Incident and harm: an accepted checkpoint containing an outstanding
  obligation is copied; two descendants continue independently and both spend,
  attest, or execute an effect intended to occur once.
- Fixed boundary: `CHECKPOINT -> FORK -> CONTINUE_A || CONTINUE_B -> EFFECT`;
  each fork has the same state and local randomness interface. The observer may
  see one branch before effects, both branches after reconciliation, or an
  external coordination service if the comparator is allowed one.
- Two-factor necessity: persistent clonable state supplies the fork, but
  adaptive computation is not necessary. Two deterministic state machines can
  equivocate or duplicate an obligation.
- Exact object: a non-equivocation witness would require every accepted state
  to have at most one effect-capable descendant in the declared continuation
  order. Indistinguishable isolated copies cannot locally select a unique
  descendant while retaining both availability and symmetric correctness.
- Strongest comparator: fork-linearizable collective memory, a consensus or
  ledger service, at-most-once effect identifiers, monotonic counters,
  non-exportable credentials, or another externally non-clonable resource.
- Decisive falsifier: a purely local protocol over freely clonable identical
  state that preserves availability and guarantees a unique effect on every
  partitioned execution.
- Negative regime: read-only continuations, idempotent effects, no fork,
  immediate communication, or an external unique-effect primitive.
- Reduction boundary: rollback/fork detection, state continuity, equivocation,
  at-most-once semantics, and communication are ordinary distributed-systems
  objects. Lightweight Collective Memory supplies a positive construction;
  the agent-identity literature states the copyability problem directly
  (`EV-0171`; `EV-0172`).
- Disposition: `FAILS_ADAPTIVE_COMPUTE_NECESSITY_AND_REDUCED_TO_STATE_CONTINUITY`.

### M1G-P04: Purpose-scoped causal influence

- Incident and harm: a valid record collected for one user or purpose changes
  an action outside its declared scope, for example another user's decision or
  a tool call for which the record supplied no authority.
- Fixed boundary: `WRITE(r, Sigma(r)) -> RETRIEVE -> REASON -> ACT`; `Sigma(r)`
  is the authorized set of trace components. The observer sees the complete
  low-scope trace and tool effects; candidate and comparator receive identical
  labels, policy, records, compute, and mediation points.
- Two-factor necessity: persistence enables delayed cross-context influence,
  but adaptive computation is not necessary. A deterministic lookup or
  workflow can violate the same purpose restriction.
- Exact object: for admissible contexts `X`, low-equivalent replacements, and
  the out-of-scope projection `Pi_not_Sigma`,
  `Delta_scope = sup_(x in X, r' equiv_low r)
  TV(Law(Pi_not_Sigma tau | do(r),x),
  Law(Pi_not_Sigma tau | do(r'),x))`. Zero residual is probabilistic
  non-interference with an explicit declassification boundary.
- Strongest comparator: information-flow labels, purpose-based access control,
  capabilities, complete mediation, conservative propagation, and explicit
  declassification.
- Decisive falsifier: a trace outside `Sigma(r)` whose distribution changes
  under `do(r)` versus a low-equivalent replacement.
- Negative regime: one user and purpose, no consequential action, explicit
  declassification, or complete mediation that blocks every out-of-scope flow.
- Reduction boundary: non-interference, information-flow control, authority,
  and causal read-set closure already supply the invariant (`EV-0084`;
  `EV-0156`). CIMemories, cross-user contamination, Memory-Induced Tool-Drift,
  and Intent Legitimation directly occupy the persistent-agent incidents
  (`EV-0173` through `EV-0176`).
- Disposition: `FAILS_ADAPTIVE_COMPUTE_NECESSITY_AND_DIRECT_COLLISION`.

### M1G-P05: Snapshot staleness during adaptive reasoning

- Incident and harm: an agent reads a versioned world snapshot, spends a
  variable deliberation time, the relevant world state changes, and the agent
  acts on the obsolete snapshot.
- Fixed boundary: `READ(x_t,v_t) -> PONDER(b) -> REFRESH? -> VALIDATE_COMMIT`.
  Let `tau(b)` be deliberation time, `q(b)` its anytime quality, `S(t)` the
  probability that the decision-relevant state survives for `t`, and `c(b)`
  the fully charged cost.
- Two-factor necessity: adaptive computation creates a variable exposure
  interval, but persistent governed state is not necessary. A transient sensor
  snapshot in any dynamic planner has the same trade-off.
- Exact object: assume `q(b)>0`, `S(t)>0`, and `q`, `S`, `tau`, and `c` are
  differentiable on the interior of the registered budget domain. Under the
  product model `J(b) = q(b) S(tau(b)) - c(b)` and hazard
  `h(t) = -d log S(t)/dt`,
  `J'(b) = S(tau(b))[q'(b) - h(tau(b)) tau'(b) q(b)] - c'(b)`.
  With `c'(b)=0`, a local increase in compute hurts at `b` exactly when
  `d log q(b)/db < h(tau(b)) tau'(b)`.
- Strongest comparator: refresh-on-change, age-aware stopping, snapshot
  validation at commit, optimistic retry, or a semi-Markov policy jointly
  choosing deliberate, refresh, and act under the same observations and cost.
- Decisive falsifier: two registered environments with the same marginal
  `q`, `S`, `tau`, and `c` but different expected success because reasoning
  quality and state changes are dependent. Such a pair falsifies transport of
  the product model; conditional on the product model, the derivative is an
  identity rather than an empirical claim.
- Negative regime: static world, zero-latency reasoning, monotone freshness not
  required by the task, or free validation and replay.
- Reduction boundary: the equation is the product rule for anytime quality and
  state-survival probability, plus ordinary value of computation. Real-Time
  Reasoning Agents studies the same frozen-observation incident, while Yamada
  already stops deliberation from success and persistence probabilities
  (`EV-0178`; `EV-0179`).
- Disposition: `FAILS_PERSISTENT_STATE_NECESSITY_AND_DIRECT_COLLISION`.

### M1G-P06: History-dependent compute and service disparity

- Incident and harm: persistent outcomes alter later compute allocations;
  unequal allocations alter later outcomes, producing a widening service gap
  between otherwise symmetric subjects or groups.
- Fixed boundary: group history is the persistent state; an adaptive policy
  allocates a fixed per-round compute budget; outcome, service, and allocation
  gaps are observed over a fixed horizon. The comparator may use the complete
  history and jointly optimize utility and the same declared fairness measure.
- Two-factor necessity: clearing history removes the feedback state and fixing
  allocations removes adaptive amplification. Both factors can therefore be
  causal in a chosen recurrence.
- Exact object: for differentiable disparity recurrence `d_(t+1)=F(d_t)` and a
  fixed point `d*` satisfying `F(d*)=d*`, the perturbation multiplier is
  `mu=F'(d*)` and its local exponent is `Lambda=log|mu|`. Perturbations are
  locally unstable when `|mu|>1` and locally asymptotically stable when
  `|mu|<1`; `|mu|=1` is inconclusive. This is the ordinary Jacobian stability
  criterion, not a new law.
- Strongest comparator: a fair constrained MDP or weakly coupled MDP with the
  same transition kernel, history, resource budget, utility objective, and
  group-symmetric or generalized-Gini constraint.
- Decisive falsifier: under the stated differentiability assumptions, either a
  claimed locally unstable fixed point with `|F'(d*)|<1` or a claimed locally
  asymptotically stable fixed point with `|F'(d*)|>1`.
- Negative regime: history-independent allocation, contractive dynamics,
  symmetric outcomes, active equalization, or one-shot service.
- Reduction boundary: Jacobian/Lyapunov stability, fair sequential decision
  making, and constrained resource allocation reproduce the object. Fair
  resource allocation in weakly coupled MDPs supplies the direct generic
  comparator (`EV-0180`); M1C-C13 and M1D-C15 already cover the feedback
  family.
- Disposition: `REDUCED_TO_GENERIC_DYNAMICAL_FAIR_CONTROL`.

### M1G-P07: Declared-state completeness

- Incident and harm: two executions expose the same declared persistent state
  but produce different outputs, actions, or compute traces because an
  undeclared cache, parameter update, scheduler state, or hidden history
  remains causally active.
- Fixed boundary: histories `h,h'` satisfy `D(h)=D(h')` for the declared-state
  extractor `D`; the observer sees the registered output-and-cost trace. All
  randomness is coupled or compared distributionally.
- Two-factor necessity: persistent hidden influence can violate the contract,
  but adaptive computation is not necessary. Ordinary hidden deterministic
  state or nondeterminism is sufficient.
- Exact object: declared-state sufficiency requires
  `D(h)=D(h') => Law(tau | h)=Law(tau | h')` for every permitted continuation.
  This is observational determinism or probabilistic non-interference, a
  two-trace hyperproperty.
- Strongest comparator: make all causal state explicit, reset the hidden
  runtime, replay from a canonical state, verify the transition system, or
  weaken the contract to a registered finite continuation class.
- Decisive falsifier: one pair of low-equivalent histories and one continuation
  with distinguishable registered trace laws.
- Negative regime: deterministic replay from complete declared state, a finite
  verified transition system, or a contract that explicitly includes the
  previously hidden state.
- Reduction boundary: Hyperproperties, probabilistic non-interference,
  observational determinism, replay closure, and program verification already
  define the requirement (`EV-0084`). Finite black-box testing cannot certify
  the universal continuation claim for an unrestricted implementation.
- Disposition: `FAILS_ADAPTIVE_COMPUTE_NECESSITY_AND_REDUCED_TO_HYPERPROPERTY`.

### M1G-P08: Persistent cost amplification and denial of wallet

- Incident and harm: a low-cost hostile write remains stored and repeatedly
  triggers expensive retrieval, validation, tool use, or reasoning on future
  requests, exhausting a shared compute budget.
- Fixed boundary: couple executions with and without write `w` on the same
  requests and registered randomness. Let
  `Delta C_t(w)=[C_t^(+w)-C_t^(-w)]_+`, admission cost `a(w)>0`, horizon `H`,
  and random amplification
  `A_tilde_H(w)=sum_(t<=H) Delta C_t(w)/a(w)`. Candidate and comparator receive
  the same requests, state, cache, policy class, and total resource budget.
- Two-factor necessity: persistence enables repeated activation, but adaptive
  computation is not necessary for the horizon-linear bound. A fixed expensive
  handler triggered by retained state is enough.
- Exact object: let `I_t` indicate activation. If the write remains eligible,
  `P(I_t=1 | H_(t-1)) >= p`, and the coupled marginal cost satisfies
  `Delta C_t(w) >= kappa` whenever `I_t=1`, then
  `E[A_tilde_H(w)] >= H p kappa / a(w)`. This is conditional expectation plus
  linearity under the assumptions, not a distinct persistence law.
- Strongest comparator: charge every descendant activation to an immutable
  resource principal; enforce lifetime quota `Q_w`, lease or TTL, bounded
  validation fuel, admission price, caching, and revocation. Then
  `sum_t Delta C_t(w) <= Q_w` by construction.
- Decisive falsifier: a coupled trace process satisfying the retained-write,
  conditional activation-probability, and conditional marginal-cost
  assumptions but violating the expectation lower bound.
- Negative regime: one-shot state, zero marginal activation cost, strict TTL,
  descendant caching, principal-level quota, or immediate revocation.
- Reduction boundary: algorithmic-complexity denial of service, amortized
  resource accounting, quotas, and resource principals reproduce both the
  lower and bounded branches. AgentDoS reports persistent resource-lifecycle
  abuse and quota mitigations directly; Resource Containers supplies the
  generic accounting primitive (`EV-0181`; `EV-0182`). M1D-C06/C11/C17/C23 and
  M1F-O09 already cover the nearest state-compute and strategic-write objects.
- Disposition: `FAILS_ADAPTIVE_COMPUTE_NECESSITY_AND_DIRECT_COLLISION`.

## Crosswalk against all 73 prior formulations

`NO_REOPENING` means that a nearby incident does not state a result in the
prior object's exact class. It is not an absence-of-prior-art claim.

| Prior object | Relation to M1g attempt | Boundary result |
|---|---|---|
| M1C-C01 | P01/P05 require revision-aware invalidation and replay before commit or refresh | `RECYCLED` |
| M1C-C02 | P01/P02 require dependency closure for invalidation or deletion | `RECYCLED` |
| M1C-C03 | P01/P05 permit full cancellation or refresh and supply no new minimum repair-cone result | `NO_REOPENING` |
| M1C-C04 | P04/P07 ask whether causally effective influence escapes the declared graph or state | `RECYCLED` |
| M1C-C05 | P02 compares deletion with a counterfactual fresh state but supplies no selective compaction certificate | `NO_REOPENING` |
| M1C-C06 | P01 linearizes revocation against an in-flight commit; P03 linearizes forked continuation effects | `RECYCLED` |
| M1C-C07 | P03 requires unique continuation, not a new coordination-free merge or I-confluence result | `NO_REOPENING` |
| M1C-C08 | P01/P03 reuse epoch, version, and replay closure; P07 restates the hidden-runtime boundary | `RECYCLED` |
| M1C-C09 | P02 asks whether transformed state matches canonical reconstruction without the deleted datum | `RECYCLED` |
| M1C-C10 | P04/P07 are causal read-set or influence-closure conditions | `RECYCLED` |
| M1C-C11 | P01/P03 require versioned validity contracts for procedures, continuations, or obligations | `RECYCLED` |
| M1C-C12 | P04/P08 define no contaminated-offspring or supercritical reproduction threshold | `NO_REOPENING` |
| M1C-C13 | P06's feedback multiplier and exponent are the same read-write stability family | `RECYCLED` |
| M1C-C14 | P02/P07 test residual influence after nominal deletion or restoration of declared state | `RECYCLED` |
| M1C-C15 | P06/P08 use persistent streams but claim no reset-versus-stream ranking reversal | `NO_REOPENING` |
| M1C-C16 | P06/P08 supply neither a cross-family collapse nor a transportable scaling exponent | `NO_REOPENING` |
| M1D-C01 | P01/P08 use deterministic validation or quotas, not a new anytime-valid e-process guarantee | `NO_REOPENING` |
| M1D-C02 | P05 prices deliberation against state survival; P08 prices a write over its full future cost | `RECYCLED` |
| M1D-C03 | P06 may generate selection feedback but supplies no new OPE estimand or correction | `NO_REOPENING` |
| M1D-C04 | P06/P08 make persistent state or writes mediate later compute | `RECYCLED` |
| M1D-C05 | P01/P02 directly reuse the revocation or deletion storage-recomputation frontier | `RECYCLED` |
| M1D-C06 | P08's accumulated descendant cost is validation or resource debt accounting | `RECYCLED` |
| M1D-C07 | No M1g problem states an adaptive-submodular acquisition result | `NO_REOPENING` |
| M1D-C08 | P01 recourse and P06 fairness introduce no new dynamic-regret or switching-cost bound | `NO_REOPENING` |
| M1D-C09 | P05/P08 compute discounted benefit or cost across future state reuse | `RECYCLED` |
| M1D-C10 | P05 couples snapshot validity with the marginal return to reasoning compute | `RECYCLED` |
| M1D-C11 | P08 is the negative-cost form of delayed causal credit for a persistent write | `RECYCLED` |
| M1D-C12 | P05 contains the refresh-versus-deliberate threshold; P01 adds version validation | `RECYCLED` |
| M1D-C13 | P08 distinguishes admission cost from later activation cost but claims no build/read response kernel | `NO_REOPENING` |
| M1D-C14 | No M1g object depends on correlated rollout consensus or self-judged confidence | `NO_REOPENING` |
| M1D-C15 | P06's state-dependent allocation feedback is the same self-sealing undercompute family | `RECYCLED` |
| M1D-C16 | P03 duplicates obligations and P08 charges their future opportunity cost | `RECYCLED` |
| M1D-C17 | P03/P08 reuse persistent obligations, triggers, budgets, and resource reservation | `RECYCLED` |
| M1D-C18 | P01/P07 claim no proof-carrying artifact or incremental-certificate complexity result | `NO_REOPENING` |
| M1D-C19 | P01/P03 require commit consistency but introduce no distinct dual-consensus barrier | `NO_REOPENING` |
| M1D-C20 | P01/P03 concern valid resumption, cancellation, replay, and forked continuations | `RECYCLED` |
| M1D-C21 | P02 concerns residual influence after internalization, not consolidation-driven compute retirement | `NO_REOPENING` |
| M1D-C22 | P05 co-schedules snapshot residence, refresh, deliberation, and commit; P06 allocates compute by state | `RECYCLED` |
| M1D-C23 | P05's objective and P08's descendant budget are reuse-shadow-price calculations | `RECYCLED` |
| M1D-C24 | P02 deletion audits and P08 hostile-write audits purchase information for a governed-state choice | `RECYCLED` |
| M1E-C01 | P02 retains information after adaptation but supplies no one-pass INDEX or coding bound | `NO_REOPENING` |
| M1E-C02 | P05 uses a stale external snapshot, not a new attention-cache memory-time frontier | `NO_REOPENING` |
| M1E-C03 | P04/P08 have query-dependent activation but no adaptive cell-probe result | `NO_REOPENING` |
| M1E-C04 | P01/P03 require mutable-state consistency but no partial-sums operation or probe tradeoff | `NO_REOPENING` |
| M1E-C05 | No M1g problem introduces a graph-stream space-pass result | `NO_REOPENING` |
| M1E-C06 | P03 uniqueness requires communication, coordination, or an external non-clonable resource | `REDUCED` |
| M1E-C07 | No M1g object supplies the missing generic element-distinctness lower bound | `NO_REOPENING` |
| M1E-C08 | P01/P03 persist intermediate continuations but claim no parity-learning or supervision separation | `NO_REOPENING` |
| M1E-C09 | P02/P08 reuse audit coverage and non-identification when relevant histories are never inspected | `RECYCLED` |
| M1E-C10 | P02/P07 ask whether a compressed or declared state preserves identification of hidden influence | `RECYCLED` |
| M1E-C11 | No M1g problem uses randomized encouragement or claims an IV estimand | `NO_REOPENING` |
| M1E-C12 | P06's history-dependent allocation is a stationary-policy or fair-MDP effect | `RECYCLED` |
| M1E-C13 | P03/P04 become causal coordination under private views and bounded communication | `REDUCED` |
| M1E-C14 | P02/P08 do not select among persistent interventions under a fixed sampling budget | `NO_REOPENING` |
| M1E-C15 | P02/P06/P07 supply no exact-belief sufficient statistic or Bayes-adaptive bound | `NO_REOPENING` |
| M1E-C16 | P06/P08 directly make future compute depend on persistent writes or state | `RECYCLED` |
| M1E-C17 | P02 may include fast-weight internalization but claims no matched sample-efficiency separation | `NO_REOPENING` |
| M1E-C18 | P06 allocates service, not verifier-guided expert samples or online-expert regret | `NO_REOPENING` |
| M1E-C19 | P04 scoped retrieval supplies no sparse-representation sample bound | `NO_REOPENING` |
| M1E-C20 | P05 varies reasoning depth but claims no recurrent-state expressivity theorem | `NO_REOPENING` |
| M1E-C21 | P06/P08 introduce no lifelong feature library or acquisition-rate result | `NO_REOPENING` |
| M1E-C22 | P02 concerns deletion after internalization, not lifelong-representation sample complexity | `NO_REOPENING` |
| M1E-C23 | P05 fixes a real-time stopping objective but does not rescue the unspecified meta-learning frontier | `NO_REOPENING` |
| M1E-C24 | P03/P04 reduce to distributed learning or communication under private views | `REDUCED` |
| M1F-O01 | P04/P08 define no ancestry-adjusted evidence mass or confidence inflation | `NO_REOPENING` |
| M1F-O02 | P02/P03 use state transitions and versions but claim no writer-reader semantic ABI | `NO_REOPENING` |
| M1F-O03 | P05/P06/P08 all price how durable state changes later reasoning work | `RECYCLED` |
| M1F-O04 | P04's purpose-scoped causal influence is ordinary authority and information-flow control | `RECYCLED` |
| M1F-O05 | P04/P07 restate low-equivalent hidden-state influence on observable traces | `RECYCLED` |
| M1F-O06 | P03 may duplicate work but claims no joint-versus-factorized work-depth separation | `NO_REOPENING` |
| M1F-O07 | P07 universal completeness and P08 hostile-write admission reuse verification and undecidability | `RECYCLED` |
| M1F-O08 | Purpose labels in P04 introduce no codec, transcode, or mission-tokenization capability | `NO_REOPENING` |
| M1F-O09 | P08 is strategic persistent contribution with costly audit and principal accounting | `RECYCLED` |

## Strongest-composite result

The strongest composite does not need one new architecture. It combines only
established controls under symmetric information and resources:

1. epoch validation, cancellation, dependency invalidation, replay, and
   linearizable effect commit for P01;
2. canonical retraining or dependency-aware unlearning for P02;
3. fork-linearizable continuity plus at-most-once external effects for P03;
4. IFC, capabilities, complete mediation, and explicit declassification for
   P04 and P07;
5. age-aware deliberation, refresh, and validate-at-commit for P05;
6. a fair constrained sequential policy for P06; and
7. immutable resource principals, descendant charging, quotas, leases, and
   revocation for P08.

This composite is not proposed as a contribution. It demonstrates that the
eight incidents do not identify a residual unavailable to existing theory and
systems mechanisms.

## Minimum-design decision

No minimum experiment is authorized. P01, P03, P04, P05, P07, and P08 fail a
preregistered two-factor necessity condition. P02 is the established machine-
unlearning object. P06 supplies only a generic Jacobian stability condition and
fair-control problem. Running an LLM benchmark would measure implementations
inside those known classes, not distinguish a new scientific object.

A later experiment becomes eligible only after a different candidate fixes an
exact residual that survives the 81-object crosswalk, the strongest generic
analogue, and independent contradictory review.

## Decision

Propose `STOP` for all eight M1g incident-first problems.

- Zero objects are admitted.
- Zero objects are `DISTINCT_CANDIDATE`.
- The closest apparent residual, forked-continuation uniqueness, does not
  require adaptive computation and reduces to state continuity,
  fork-linearizability, at-most-once effects, communication, or an external
  non-clonable resource.
- The real-time stopping inequality is an exact and useful engineering rule,
  but it is a compositional identity already occupied by dynamic deliberation
  control and does not require persistent governed state.
- No article, implementation, benchmark, training run, experiment, proof
  project, paid compute, or submission is authorized.

The direction-setting objective remains active. This proposed decision is a
negative originality gate, not the requested article.
