# M1e Intrinsic Restricted-Class Candidate Register

Cutoff: `2026-07-15`
Issue: [#17](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/17)
Gate result: `PROPOSED_STOP`
Candidates tested: `24`
Surviving `DISTINCT_CANDIDATE` objects: `0`

## Gate

M1e tested the only reopening left by Decision 0006: a separation inside an
intrinsic restricted information, communication, online-causality,
computation, or learning class. It did not test unrestricted behavioral
non-factorization again.

A candidate was admissible only if it:

1. lay outside M1C-C01 through M1C-C16 and M1D-C01 through M1D-C24;
2. declared its claim type before any result;
3. fixed the task, observation order, online causality, persistent-state and
   message budgets, compute budget, feedback, shared randomness, training
   information, and cross-module communication;
4. compared against the strongest factorized protocol under the same total
   resources, including joint training and interactive messages when allowed;
5. stated a theorem, lower or upper bound, identified estimand, or
   transportable phase law with a decisive falsifier and negative regime;
6. survived direct prior art and reduction to communication complexity,
   streaming, cell-probe, time-space tradeoffs, online learning, POMDP control,
   causal inference, distributed learning, and ordinary optimization; and
7. retained a novel mathematical object after all LLM and workspace labels
   were substituted away.

No experiment was admissible as a means of creating novelty after this formal
gate failed.

### Matched factorized comparator

Across lanes, the strongest comparator was not a pair of independently trained
modules. It could:

- co-design and jointly train the state encoder, updater, compute policy, and
  decoder;
- share the declared public randomness, training data, gradients, centralized
  critic, and every observation allowed by the comparison class;
- exchange the full declared transcript of at most `B_m` bits over the same
  number of rounds;
- use the same total persistent state `B_s`, compute or oracle budget `B_c`,
  parameters, samples, probes, passes, and feedback; and
- condition every later action on all earlier allowed messages and actions.

Any action, timing choice, expert selection, state address, or side channel
that transmits information counts toward the transcript budget. A candidate
does not establish a joint-versus-factorized separation by granting the joint
system more information, more rounds, more state, intermediate labels, or a
different operation class.

## Candidate register

### Communication, streaming, and time-space

#### M1E-C01: Associative recall after a one-pass stream

- Claim type: communication and persistent-space complexity.
- Class: an encoder observes `n` key-value pairs, emits at most `b` bits of
  persistent state, and loses the stream. A query is then revealed to a decoder
  with `c` post-query steps. Randomness, error, and query distribution are
  declared before evaluation.
- Candidate result: exact recall with error at most `1/3` requires
  `b = Omega(n)` even when `c` is unbounded.
- Decisive falsifier: an `o(n)`-bit protocol solves the corresponding uniform
  INDEX family at the registered error.
- Negative regime: the query is known before encoding, the query support is
  restricted, the stream is redundant, or nonzero distortion is permitted.
- Strongest factorized comparator: any jointly designed randomized encoder
  `E(X)` and decoder `D(E(X),q)` with the same state and compute.
- Reduction: this is one-way INDEX, random-access coding, or rate-distortion
  (`EV-0142`; `EV-0144`).
  Transformer-specific memory lower bounds already make the same reduction,
  and associative-retrieval separations already identify the same bottleneck.
- Minimum burden: a new task parameter whose lower bound is not inherited from
  INDEX or rate-distortion and whose upper bound uses governed persistence.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C02: Attention-cache memory-time frontier

- Claim type: streaming space and online-time complexity.
- Class: causal `(q_i,k_i,v_i)` tuples arrive online; an algorithm must emit an
  exact or registered approximation to attention after each token using at most
  `b` bits and `t` operations or probes per token.
- Candidate result: a dimension-dependent memory lower bound and a
  memory-time frontier for unstructured inputs.
- Decisive falsifier: a sublinear-state or sublinear-time algorithm meets the
  same worst-case approximation guarantee without an additional structure
  assumption.
- Negative regime: low dimension, bounded window, known sparsity, clustering,
  or another declared distributional restriction.
- Strongest factorized comparator: any co-designed streaming summary and query
  routine under the same state, time, randomness, and approximation contract.
- Reduction: existing KV-cache barriers (`EV-0142`; `EV-0143`) already reduce attention generation to
  INDEX and give linear-space, low-dimensional, structured, and time-memory
  regimes. Tensor-attention work extends the same construction.
- Minimum burden: a new structural parameter with a matching lower and upper
  bound that is not a renamed attention-compression assumption.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C03: Adaptive addressing of static state

- Claim type: cell-probe complexity.
- Class: a dictionary of `n` pairs is preprocessed into `s` words of `w` bits.
  A later query may make `t` adaptive probes over a fixed number of rounds.
  There are no updates or external feedback.
- Candidate result: an adaptivity advantage over non-adaptive lookup at the
  same space.
- Decisive falsifier: a non-adaptive structure violates the registered lower
  bound, or an adaptive factorized structure matches the proposed joint system.
- Negative regime: small universe, strongly superlinear space, unbounded word
  size, or queries known during preprocessing.
- Strongest factorized comparator: the full class of static data structures
  whose preprocessing and adaptive query algorithm are co-designed.
- Reduction: static cell-probe and asymmetric communication (`EV-0146`) already
  characterize the effect of adaptive probes and exhibit a gap from
  non-adaptive lookup.
- Minimum burden: a new governed-state operation or restriction that changes
  the cell-probe problem rather than relabeling its preprocessing and query
  phases.
- Disposition: `REDUCED_TO_CELL_PROBE`.

#### M1E-C04: Mutable state with partial-sum queries

- Claim type: dynamic cell-probe complexity.
- Class: online `update(i,Delta)` and `sum(j)` operations share `S` cells of
  `w` bits; each answer precedes the next operation and costs `t_u` or `t_q`
  adaptive probes.
- Candidate result: a tradeoff such as
  `t_q log(t_u/t_q) = Omega(log n)` and its symmetric branch.
- Decisive falsifier: a dynamic structure lies below the claimed curve in the
  same word and adversary model.
- Negative regime: offline batching, unbounded words, easy input
  distributions, or no updates.
- Strongest factorized comparator: any co-designed update and query algorithms
  sharing the entire state under the same probe budgets.
- Reduction: this is the dynamic partial-sums cell-probe problem (`EV-0147`). Its state and
  computation interaction is already the object of the model.
- Minimum burden: a new operation family and non-inherited lower bound tied to
  a justified governance constraint.
- Disposition: `REDUCED_TO_CELL_PROBE`.

#### M1E-C05: Recurrent passes over a graph stream

- Claim type: streaming space-pass complexity.
- Class: graph edges arrive in adversarial order; a randomized algorithm makes
  `p` complete passes, keeps `S` bits between passes, and returns a promised
  graph statistic. Local per-edge computation is not the bottleneck.
- Candidate result: a polynomial-space or logarithmic-pass lower bound.
- Decisive falsifier: an algorithm below the registered space-pass curve solves
  the same promised family.
- Negative regime: enough passes to materialize the structure, or enough space
  to retain the graph.
- Strongest factorized comparator: every `p`-pass streaming algorithm whose
  transitions and final computation are co-designed.
- Reduction: multi-pass streaming lower bounds (`EV-0148`) already use multi-round
  communication, hidden matching, or pointer chasing for these graph problems.
- Minimum burden: a distinct persistent operation that yields a new
  space-pass theorem rather than an LLM interpretation of a graph-stream bound.
- Disposition: `REDUCED_TO_STREAMING`.

#### M1E-C06: Bounded-round bidirectional coordination

- Claim type: interactive communication complexity.
- Class: two parties observe alternating pointer functions, exchange at most
  `B` bits in `r` public-coin rounds, and must output the terminal pointer.
- Candidate result: removing a round forces an asymptotic communication
  increase.
- Decisive falsifier: an `(r-1)`-round protocol communicates below the claimed
  lower bound at the same error.
- Negative regime: the full number of correctly ordered rounds, linear
  communication, or strongly structured functions.
- Strongest factorized comparator: every public-coin interactive protocol with
  arbitrary conditional messages under the same transcript and round budget.
- Reduction: round-elimination and pointer-chasing results (`EV-0149`) already state the
  separation. A state-compute policy with those messages is exactly such a
  protocol.
- Minimum burden: a new communication problem induced by an intrinsic
  governance rule, with a proof not inherited from pointer chasing.
- Disposition: `REDUCED_TO_COMMUNICATION_COMPLEXITY`.

#### M1E-C07: Element distinctness under bounded workspace

- Claim type: random-access time-space complexity.
- Class: a read-only input is accessed by a randomized RAM or branching
  program using `S` workspace and `T` time or probes.
- Candidate result: a smooth strong lower bound matching the best known
  element-distinctness upper bound.
- Decisive falsifier: an algorithm below the proposed curve.
- Negative regime: sorted inputs, small universe, frequent duplicates, or
  linear workspace.
- Strongest factorized comparator: the entire randomized RAM or branching
  program class with the same access, space, time, and randomness.
- Reduction: the missing matching lower bound is a classical open problem
  (`EV-0150`).
  Solving it would be a generic complexity result, but the candidate supplies
  no governed-state parameter or proof route.
- Minimum burden: an actual new proof of the classical bound or a genuinely
  different formal problem. An LLM application alone is inadmissible.
- Disposition: `OUT_OF_SCOPE_GENERIC_OPEN_PROBLEM`.

#### M1E-C08: Externalized intermediate state for parity

- Claim type: learning and computational efficiency.
- Class: a finite-precision one-layer Transformer learns parity either from
  final labels, teacher-forced intermediate parities, or augmented
  verification data, with fixed samples, gradient iterations, generated steps,
  parameters, and persistent intermediate outputs.
- Candidate result: fewer samples or iterations for sequentially externalized
  computation than direct prediction.
- Decisive falsifier: the matched modular learner attains the same rate, or the
  advantage vanishes after intermediate supervision and augmentation are
  equalized.
- Negative regime: constant-size sufficient statistic, constant parity order,
  an explicitly supplied linear representation, or uninformative intermediate
  labels.
- Strongest factorized comparator: jointly trained step encoder and final
  solver with exactly the same intermediate outputs and supervision.
- Reduction: existing parity-with-chain-of-thought theory (`EV-0145`) gives the relevant
  iteration and supervision separations; retrieval theory supplies the
  complementary recurrent-memory limitation.
- Minimum burden: a result that persists after the operation and supervision
  classes are matched.
- Disposition: `ANTICIPATED_DIRECTLY`.

### Online causality, identification, and endogenous observation

#### M1E-C09: Audit floor under endogenous labels

- Claim type: causal identification.
- Class: `(S_t,X_t)` precede write and compute decisions, which precede an
  audit decision `A_t`; `Y_t` is observed only when `A_t=1`. Propensities are
  logged and feedback is bandit.
- Estimand: discounted policy value or the contrast between forced-write and
  no-write policies over horizon `H`.
- Candidate result: identification under sequential exchangeability,
  consistency, and positive audit probability on every target history, with
  non-identification when positive target mass has zero audit propensity.
- Decisive falsifier: observationally equivalent models with different values
  despite the stated assumptions, or invalid coverage under them.
- Negative regime: complete free feedback or writes with no future effect.
- Strongest factorized comparator: a jointly trained state manager and compute
  router sharing the same histories, propensities, public randomness, and
  transcript.
- Reduction: selective labels plus longitudinal g-formula, IPW, or adaptive
  OPE. Hidden confounding moves the problem to proximal or POMDP OPE.
  The decision-critical records are `EV-0128` and `EV-0129`.
- Minimum burden: an identification theorem outside these assumptions and
  existing bridge constructions.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1E-C10: Identification-preserving proxy memory

- Claim type: causal identification under compression.
- Class: a proxy history `Z_{\le t}` for latent `U_t` is compressed to
  `S_t=e(Z_{\le t})` of at most `B_s` bits; only `(S_t,C_t,Y_t)` remain
  available for OPE.
- Candidate result: identification exactly when the compressed proxy operator
  admits a bridge, with a finite-alphabet rank or bit threshold.
- Decisive falsifier: universal nonparametric identification below the proposed
  rank, or equal-rank operators with opposite identification status under the
  full stated conditions.
- Negative regime: fully observed state, injective compression, or incomplete
  proxies.
- Strongest factorized comparator: a co-designed encoder and target-policy
  evaluator under the same state and transcript budgets.
- Reduction: proximal/POMDP OPE already uses completeness and rank conditions
  (`EV-0130`; `EV-0131`);
  data processing and communication-constrained inference supply any induced
  bit lower bound.
- Minimum burden: a new causal complexity parameter with a proved necessary
  and sufficient compressed-state threshold.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1E-C11: Randomized encouragement to commit

- Claim type: longitudinal causal identification.
- Class: a randomized recommendation `Z_t` affects actual write `W_t`, which
  affects persistent state and later outcomes; latent `U_t` may confound write
  and outcome.
- Estimand: a local average effect of commit among compliers under relevance,
  independence, exclusion, and monotonicity.
- Decisive falsifier: a direct path from encouragement to the outcome, failed
  monotonicity, or observationally equivalent compatible laws with different
  LATE.
- Negative regime: weak instrument, perfect compliance, or compute
  encouragement that directly changes the outcome.
- Strongest factorized comparator: the same manager-router protocol using the
  same instrument and budget.
- Reduction: instrumental variables, instrument-armed bandits (`EV-0132`;
  `EV-0133`), and
  longitudinal MSM or SNMM. The delayed effect of a write also recycles an
  excluded M1d family.
- Minimum burden: a new identified estimand that cannot be expressed by IV or
  longitudinal causal models.
- Disposition: `OUT_OF_SCOPE_RECYCLING`.

#### M1E-C12: Stationary effect on a performative population

- Claim type: stationary policy-value identification.
- Class: persistent state changes write and compute actions, which change the
  future request population. One adaptive trajectory is observed under
  sequential ignorability, overlap, and mixing assumptions.
- Estimand: the difference in long-run average outcome between two policies.
- Candidate result: an identified estimator with a rate depending on mixing
  time and overlap.
- Decisive falsifier: equivalent mixing chains with distinct stationary values
  despite the assumptions, or a claimed minimax rate violated without added
  structure.
- Negative regime: exogenous requests, no mixing, or disjoint support.
- Strongest factorized comparator: the same jointly trained policy represented
  as a state manager and compute router under the same trajectory information.
- Reduction: stationary OPE in partially observed systems, state-dependent
  performative prediction, and switchback or carryover analysis.
  The decision-critical records are `EV-0134`, `EV-0135`, and `EV-0141`.
- Minimum burden: a new transportable estimand or rate not reconstructed by
  those objects.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1E-C13: Private causal order with a bounded message

- Claim type: causal estimation under communication constraints.
- Class: the manager privately observes proxy `Z_t`, writes state, and sends
  `B_m` bits; the router later observes `X_t` and chooses compute and audit.
- Candidate result: an ATE or policy value cannot be estimated below a target
  error when `B_m` is below the information complexity of a causally
  sufficient statistic.
- Decisive falsifier: a one-way protocol below the bound achieves the uniform
  error, or the gap remains after the sufficient statistic fits in the
  transcript.
- Negative regime: independent private views, a low-dimensional sufficient
  statistic, or unrestricted communication.
- Strongest factorized comparator: every public-coin one-way protocol with the
  same private observations and total resources.
- Reduction: distributed statistical estimation and data-processing
  inequalities already give the restriction. A centralized controller also
  sees more information and is not a matched factorized comparator.
  See `EV-0127` and `EV-0136`.
- Minimum burden: a new causal identification phenomenon at equal information,
  not a central-versus-distributed information gap.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1E-C14: Causal bandit over persistent interventions

- Claim type: causal discovery and best-intervention sample efficiency.
- Class: each episode intervenes on one persistent-state cell, then allocates
  `B_c` observations to descendants in a declared DAG.
- Candidate result: simple-regret or identification bounds controlled by a
  separating system or causal coverage parameter.
- Decisive falsifier: regret exceeds the bound under its hypotheses, or a
  lower-bound instance is solved with fewer interventions.
- Negative regime: no shared causal information, non-identifiability under the
  allowed interventions, or dominant intervention cost.
- Strongest factorized comparator: a manager and acquisition router choosing
  the same adaptive interventions and observations with the same DAG and
  budget.
- Reduction: causal bandits and adaptive experimental design already supply
  the separating systems, track-and-stop rules, and lower bounds. Persistence
  only reindexes the intervention across episodes.
  `EV-0137` is the decision-critical positive record.
- Minimum burden: a new causal structural parameter or bound created by an
  operation absent from the existing intervention model.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1E-C15: Dual audit against epistemic lock-in

- Claim type: Bayes-adaptive control.
- Class: a belief over latent environment and model parameters is compressed
  into persistent state; actions either exploit or purchase informative audits.
- Candidate result: an audit threshold or regret guarantee relative to the
  Bayes-optimal controller.
- Decisive falsifier: the proposed policy rejects a positive-value audit, or a
  lower-resource policy dominates it over the registered class.
- Negative regime: known model, uninformative observations, unit horizon, or
  audits whose cost exceeds their value.
- Strongest factorized comparator: a co-designed belief updater and compute or
  audit policy sharing the compressed belief and same resources.
- Reduction: Bayes-adaptive POMDPs (`EV-0138`), dual control, and information-reward POMDPs
  already represent the persistent belief and epistemic actions.
- Minimum burden: a new sufficient statistic or performance bound outside the
  belief-MDP representation.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

#### M1E-C16: Compute effect mediated by persistent writes

- Claim type: longitudinal mediation.
- Class: current compute changes a write trajectory, which changes later state,
  later compute, and outcome; time-varying confounders may be affected by prior
  treatment.
- Estimand: an interventional indirect effect of present compute through writes.
- Candidate result: identification under stochastic interventions with a
  sequentially doubly robust estimator.
- Decisive falsifier: disagreement with randomized compute and write overrides
  under consistency, positivity, and exchangeability.
- Negative regime: writes disabled, no reuse, positivity failure, or a hidden
  recanting witness without a complete proxy.
- Strongest factorized comparator: the same longitudinal policy and intervention
  schedule decomposed into manager and router.
- Reduction: longitudinal g-formula, MSM, SNMM, and proximal mediation
  (`EV-0090`; `EV-0139`; `EV-0140`). This is
  also the forbidden M1D-C04 family.
- Minimum burden: a distinct path-specific estimand with new identification
  conditions and proof.
- Disposition: `OUT_OF_SCOPE_RECYCLING`.

### Learning, sample efficiency, and optimization

#### M1E-C17: Fast weights versus static in-context learning

- Claim type: sample efficiency.
- Class: a pretrained linear Transformer receives target demonstrations,
  performs one registered gradient update, and predicts; state, forward and
  backward compute, context length, and base weights are charged.
- Candidate result: test-time training succeeds with `o(d)` target context
  where static ICL needs `Omega(d)`.
- Decisive falsifier: the gap vanishes when the modular learner receives the
  same update operation and fast-weight state.
- Negative regime: strong source-target alignment, too few target examples,
  high noise, or harmful initialization.
- Strongest factorized comparator: an update module producing `Delta W` and a
  predictor using `W+Delta W`, jointly trained under identical resources.
- Reduction: test-time-training theory (`EV-0116`) already proves the stated sample
  advantage. Comparing it only with static ICL changes the allowed operation
  class.
- Minimum burden: a separation between matched learners that both receive the
  same adaptation primitive.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C18: Verifier state and adaptive expert selection

- Claim type: test-time sample efficiency and online regret.
- Class: a system repeatedly selects among `K` experts, samples an answer,
  observes verifier feedback, updates state, and repeats under identical query
  and verifier budgets.
- Candidate result: different `Delta`-dependent sample rates for
  self-consistency and best-of-n, plus online-expert expressivity under
  self-correction.
- Decisive falsifier: an experts-algorithm module coupled to the generator
  achieves the same rate and regret.
- Negative regime: zero answer-probability gap or an uninformative or
  adversarial verifier.
- Strongest factorized comparator: Hedge, EXP3, or any online-experts policy
  receiving the full allowed verifier transcript.
- Reduction: existing test-time-scaling theory (`EV-0117`) proves the sample separation and
  shows self-correction simulating online learning over experts.
- Minimum burden: a new persistent cross-task learning bound beyond experts
  algorithms and conditional sampling.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C19: Persistent representation for sparse retrieval

- Claim type: representation-learning sample efficiency.
- Class: only `q` of `N` tokens determine each output and their addresses are
  described in the prompt; the learner has `q` reads, `q log N` interface bits,
  and the same persistent representation budget.
- Candidate result: sample complexity nearly independent of `N` versus
  `N^{Omega(1)}` for a recurrent learner.
- Decisive falsifier: a modular address encoder transmits the `q` positions and
  attains the same rate.
- Negative regime: `q=Theta(N)`, missing addresses, or unidentifiable supports.
- Strongest factorized comparator: jointly trained address encoder and retriever
  with the full registered transcript.
- Reduction: Transformer-versus-recurrent sparse-retrieval theory (`EV-0118`) gives the
  statistical separation, while lifelong representation learning supplies the
  durable component (`EV-0121`). Restricting the interface further becomes distributed
  learning or communication complexity.
- Minimum burden: a new joint persistence-compute sample bound not obtained by
  composing these two results.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1E-C20: Recurrent state and adaptive depth

- Claim type: length generalization and computational expressivity.
- Class: a shared block is looped `T(n)` times on iterative `n`-RASP-L tasks,
  with fixed activations, training compute, inference FLOPs, stopping
  information, and supervision.
- Candidate result: length generalization from recurrent state and
  input-dependent depth.
- Decisive falsifier: a separated transition block and stopping controller with
  the same state and compute generalizes equally.
- Negative regime: no shared iterative transition, unknown or unidentifiable
  iteration count, or non-iterative tasks.
- Strongest factorized comparator: the same tied transition and a jointly
  trained halting module with complete access to the recurrent state.
- Reduction: looped-Transformer results (`EV-0119`) already establish adaptive-step length
  generalization, and related results show Transformers implementing multi-step
  gradients.
- Minimum burden: a cross-task persistence theorem that is not ordinary
  meta-learning or recurrence.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C21: Lifelong learning with costly features

- Claim type: lifelong sample and acquisition efficiency.
- Class: sequential tasks share a small library among `d` costly features; the
  learner selects features before full observation and retains the library.
- Candidate result: amortized future acquisition approaches target prediction
  cost.
- Decisive falsifier: retained features do not reduce later feature
  measurements under the declared shared-library model.
- Negative regime: independent tasks, library size `d`, or many unrelated
  tasks.
- Strongest factorized comparator: a persistent feature-library learner and
  feature selector sharing the entire library and jointly optimized.
- Reduction: lifelong learning with costly features (`EV-0120`) already supplies algorithms,
  guarantees, and lower bounds for this object.
- Minimum burden: a new complexity parameter or rate produced by an additional
  governed-state operation.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C22: Lifelong representation against a black-box task learner

- Claim type: lifelong sample complexity.
- Class: `m` targets lie in an unknown `k`-dimensional subspace of
  `R^d`; a persistent basis of `O(dk)` state is updated task by task.
- Candidate result: a matched upper and lower sample bound against a black-box
  single-task learner.
- Decisive falsifier: an equally informed black-box protocol beats the claimed
  asymptotic bound.
- Negative regime: `k=d` or tasks share no subspace.
- Strongest factorized comparator: the representation updater plus the best
  single-task learner used as a black box, with the same samples and state.
- Reduction: existing lifelong representation theory (`EV-0121`) gives the proposed upper
  bound and an associated black-box lower bound.
- Minimum burden: a result that changes after adaptive compute is added and
  cannot be represented as ordinary oracle or bilevel optimization.
- Disposition: `ANTICIPATED_DIRECTLY`.

#### M1E-C23: Meta-state with adaptive inner-loop depth

- Claim type: online and meta-learning efficiency.
- Class: sequential tasks expose support and query losses; persistent state
  stores initialization and similarity information, while a scheduler chooses
  a charged number of gradient, Hessian, and hypergradient calls.
- Candidate result: a new joint memory-oracle frontier or dynamic-regret bound.
- Decisive falsifier: the matched modular meta-learner and scheduler attain the
  same frontier.
- Negative regime: homogeneous well-conditioned tasks or exact convex
  objectives.
- Strongest factorized comparator: an end-to-end trained meta-learner and
  scheduler with a common loss, common hypergradients, and the same persistent
  state and oracle budget.
- Reduction: adaptive gradient meta-learning, online meta-learning, memory-
  reduced bilevel optimization, and modular credit assignment reconstruct the
  object (`EV-0122`; `EV-0123`; `EV-0124`; `EV-0125`).
- Minimum burden: a new lower or upper bound depending on a state-compute
  structural parameter not present in bilevel optimization.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

#### M1E-C24: Co-learning under a bounded transcript

- Claim type: distributed learning under communication constraints.
- Class: a state encoder privately observes a sparse latent support and a
  compute module observes queries; they exchange `B` bits over `R` rounds, with
  every action and timing channel charged.
- Candidate result: a centralized sample advantage when
  `B < k log(d/k)`.
- Decisive falsifier: a matched interactive protocol attains the centralized
  rate, or the separation remains after the support entropy fits in the
  transcript.
- Negative regime: complete communication, low dimension, or known support.
- Strongest factorized comparator: every interactive distributed learner under
  the same observations, transcript, rounds, samples, parameters, and state.
- Reduction: distributed estimation, sparse recovery, and interactive
  communication complexity already provide this form of lower bound.
  See `EV-0126` and `EV-0127`.
- Minimum burden: a new learning problem and state-dependent rate that is not
  inherited from support transmission.
- Disposition: `GENERIC_DISTRIBUTED_LEARNING_REDUCTION`.

## Strongest-composite result

The maximum comparator closes the apparent architectural gap in every lane:

- streaming summaries plus adaptive query algorithms reconstruct persistent
  state followed by compute;
- dynamic data structures reconstruct jointly designed writes and reads;
- interactive communication protocols reconstruct bounded coordination;
- longitudinal causal policies reconstruct write, compute, audit, and future
  outcomes;
- belief-state control reconstructs epistemic state and information purchase;
- jointly trained representation and scheduler modules reconstruct meta-state
  plus adaptive computation; and
- distributed learning reconstructs private views plus bounded transcripts.

The positive literature goes further than a generic reconstruction. It already
contains attention-cache lower bounds, adaptive-probe gaps, multi-pass
space-pass bounds, chain-of-thought learning separations, selective-label and
POMDP identification conditions, causal-bandit designs, test-time-training
sample gains, sparse-retrieval separations, looped-Transformer length
generalization, and lifelong-representation bounds.

## Minimum-design decision

No proof or experiment is authorized for this candidate set.

M1E-C07 points to a real generic open problem, but the register supplies neither
a proof nor a state-compute-specific parameter. Every other minimum burden
requires a new theorem or estimand before implementation. Measuring one more
interaction, adding an LLM benchmark, or weakening the factorized comparator
cannot satisfy that burden.

## Decision

Propose `STOP` for all 24 M1e candidates:

- zero `DISTINCT_CANDIDATE` objects survive;
- eight candidates are directly anticipated;
- three are anticipated by positive composites;
- ten reduce to established communication, streaming, data-structure,
  causal, control, learning, or optimization theory; and
- three violate the no-recycling or no-generic-open-problem boundary.

The exact labels overlap in two composite cases, so the disposition tally used
for governance is exclusive: `8 direct / 3 composite / 10 reduced / 3 out of
scope = 24`.

This register is a negative scientific result. It is not an article, survey,
taxonomy, manifesto, benchmark proposal, or permission to rewrite prior work.
The owner's direction-setting objective remains unsatisfied.
