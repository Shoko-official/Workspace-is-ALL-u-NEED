# Decision 0007: Stop the M1e intrinsic restricted-class candidate set

Date: `2026-07-15`
Status: `PROPOSED`
Issue: [#17](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/17)
Milestone: `M1e - Intrinsic restricted-class separation discovery`
Supersedes: no prior `STOP`; Decisions 0002 through 0006 remain in force
Reviewed scientific commit: `PENDING_INDEPENDENT_REVIEW`

## Context

Decision 0006 rejected unrestricted behavioral non-factorization because a
state manager followed by a compute router can reproduce any fixed-history
joint action law when information passage is unrestricted. It left open a
narrower possibility: an original separation in a class with intrinsic
restrictions on information, communication, online order, space, time,
feedback, or learning.

M1e tested that possibility directly. Three lanes screened 24 formulations in
communication and streaming complexity, causal identification, and learning or
sample efficiency. Twenty-two fix the required class, comparator, result,
falsifier, negative regime, and minimum burden. C10 and C23 are retained as
unsupported admission failures because the former lacks its claimed finite-bit
if-and-only-if result and the latter does not select one task family and
frontier.

## Findings

### The strongest factorized protocol is already a broad technical class

The matched comparator may be jointly designed and trained, share all allowed
observations and public randomness, and communicate the same bounded transcript
over the same number of rounds. It receives the same total parameters,
persistent bits, samples, gradients, probes, passes, oracle calls, feedback, and
compute.

Under this comparison:

- persistent encoding followed by a query is a communication protocol or
  static data structure;
- mutable state with reads and writes is a dynamic data structure;
- recurrent passes are a streaming algorithm;
- bounded manager-router interaction is an interactive communication protocol;
- state, write, compute, audit, and future outcome form a longitudinal policy;
- compressed epistemic state plus information purchase is belief-state
  control; and
- persistent representation plus adaptive training compute is a jointly
  optimized online, meta, lifelong, or distributed learner.

The decomposition does not assume that modules train independently or optimize
local losses. Weakening the comparator in either way would manufacture a
separation not implied by the architecture.

### Communication and time-space results are positive collisions

Attention-cache memory barriers already reduce online generation to INDEX and
state exact dimensional and structural regimes. Tensor-attention work extends
that memory-time analysis. Associative-retrieval theory uses streaming and
one-way communication bounds to separate bounded-memory recurrent models from
Transformers, then shows that retrieval augmentation or one Transformer layer
closes its stated gap.

Static and dynamic cell-probe results already characterize adaptivity, update-
query tradeoffs, word size, and probe budgets. Multi-pass graph-stream results
already translate communication rounds into space-pass lower bounds. Pointer-
chasing results already quantify the price of deleting an interaction round.
Chain-of-thought parity theory already separates final-label training,
teacher-forced intermediate state, and augmented verification data.

Element distinctness exposes a genuine generic lower-bound gap. M1e neither
solves it nor introduces a governed-state parameter. Rebranding that open
problem as an LLM direction would violate the admission gate.

### Causal restrictions identify known estimands

Endogenous audits reduce to selective labels followed by longitudinal g-
formula, IPW, or adaptive or partially observed OPE under the declared
assumptions. Existing compressed-proxy results supply sufficient completeness,
bridge, rank, and invertibility conditions, but not C10's proposed necessary-
and-sufficient bit threshold; C10 is therefore unsupported rather than reduced.
Randomized commit
encouragement is an instrumental-variable problem. Long-run feedback through
future request populations is stationary OPE, performative prediction, or
carryover. Bounded private causal views reduce to distributed estimation.
The registered persistent-intervention task is fixed-budget best-intervention
selection; causal discovery and general-SCM cumulative regret are adjacent
classes rather than components of that direct collision.
Epistemic audits are dual control. Compute effects mediated by future writes
are longitudinal mediation, MSM, SNMM, or proximal mediation.

The two delayed-write formulations also recycle families excluded by M1d.
Adding persistence to the variable names does not create a new estimand or
identification theorem.

### Learning restrictions are directly occupied

Existing theory already establishes:

- a test-time-training sample advantage over static in-context learning;
- different sample rates for self-consistency and best-of-n, plus
  self-correction as online expert learning;
- Transformer-versus-recurrent sparse-retrieval sample separation;
- formal looped-Transformer task decompositions with adaptive iteration counts,
  accompanied by empirical rather than theorem-level length generalization;
- lifelong acquisition guarantees for costly shared features; and
- lifelong representation upper and black-box lower bounds.

Online meta-learning, adaptive gradient methods, memory-reduced bilevel
optimization, and modular credit assignment reconstruct components of C23, but
do not establish adaptive stopping or a joint memory-oracle frontier. Because
C23 fixes neither one task class nor one theorem, it is unsupported rather than
anticipated by that composite. Private support plus a bounded transcript is
distributed learning and sparse-recovery communication complexity.

In several direct collisions, the apparent advantage compares different
operations or different training information. Teacher forcing, augmented
verification data, test-time weight updates, extra rounds, or extra probes must
be granted to the matched comparator as well.

### Disposition and search limitation

The exclusive result is:

- nine `ANTICIPATED_DIRECTLY`;
- one `ANTICIPATED_BY_COMPOSITE`;
- nine conditional reductions to known theory;
- three scope violations through forbidden recycling or a relabeled generic
  open problem; and
- two `UNSUPPORTED_NOT_DISTINCT` admission failures.

The targeted search is current through 15 July 2026. It is not exhaustive and
does not infer novelty or non-novelty from search silence. The proposed stop
rests on positive primary records, exact matched classes, generic reductions,
and scope violations.

## Decision

Return global `STOP` for all 24 M1e screened formulations.

- Zero candidates are `DISTINCT_CANDIDATE`.
- No theorem, estimator, invariant, complexity parameter, or transportable
  phase law remains after the strongest matched comparison and label
  substitution.
- No model, benchmark, implementation, training run, experiment, paid compute,
  or manuscript is authorized.
- The register and decision are negative governance results, not the requested
  article.

The owner's direction-setting objective remains active at the program level.
This cycle does not satisfy it.

## Anti-rewrite determination

The following are explicitly insufficient for a future article:

- calling an INDEX, pointer-chasing, cell-probe, streaming, or time-space lower
  bound a persistent-workspace theorem without a new problem parameter;
- comparing a centralized system with a modular protocol that receives less
  information or fewer bits, rounds, probes, passes, or supervision;
- treating teacher forcing, test-time weight updates, verifier labels, or
  augmented data as architecture gains after withholding them from the
  comparator;
- renaming selective labels, OPE, proximal bridges, IV, causal bandits,
  performative prediction, longitudinal mediation, or dual control;
- adding adaptive halting to lifelong or meta-learning without a new bound;
- presenting an unresolved classical lower bound as a direction-setting LLM
  contribution; or
- converting this negative register into a survey, taxonomy, manifesto,
  roadmap, benchmark axis, or architecture assembly.

## Alternatives considered

- `GO` was rejected because no candidate survived direct prior art, strongest
  positive composites, generic reduction, restricted-class matching, and
  minimum-burden review.
- `PIVOT` to an attention memory-time law was rejected because the current
  candidates are already occupied by attention-compression lower bounds and
  supply no new structural parameter.
- `PIVOT` to causal identification was rejected because each estimand is
  represented by selective-label, OPE, bridge, IV, performative, causal-bandit,
  mediation, or belief-control theory under its stated assumptions.
- `PIVOT` to persistent test-time learning was rejected because test-time
  training, online experts, looped Transformers, lifelong representation, and
  meta-learning provide direct records or strongest composites.
- `PIVOT` to element distinctness was rejected because no new proof exists and
  solving a generic open problem would not by itself establish the requested
  state-compute object.
- Running a minimum experiment was rejected because an empirical interaction
  cannot create novelty after the formal class and theorem gate fails.

## Evidence

- `docs/research/M1E_CANDIDATE_REGISTER.md`: 24 screened formulations, 22
  admitted classes, two explicit admission failures, strongest comparators,
  candidate results, falsifiers, negative regimes, reductions, minimum burdens,
  and dispositions.
- `docs/research/M1E_SCOPING_LOG.md`: targeted queries, exact primary-record
  resolutions, version corrections, and limitations.
- `docs/research/EVIDENCE_LEDGER.csv`: exact source metadata and locators.
- `docs/research/CLAIM_LEDGER.csv`: M1e gate, comparator, and article-eligibility
  claims.
- `paper/references.bib`: decision bibliography, not a manuscript.

## Consequences

- Decisions 0002 through 0006 continue to stop every earlier architecture,
  benchmark, accounting, directional, distinct-object, and unrestricted
  non-factorization route.
- The experiment registry remains empty.
- Issue #17 and milestone M1e may close only after independent scientific,
  bibliographic, and governance review, local validation, required protected
  CI, and merge.
- Any later reopening must begin with a new issue and a technical object outside
  all 64 formulations screened in M1c, M1d, and M1e. It must supply the new theorem,
  estimand, or parameter before implementation.
