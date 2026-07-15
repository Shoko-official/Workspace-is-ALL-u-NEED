# Research Charter

Status: `M1F_ACCEPTED_STOP`
Version: `0.7.1`
Last scientific milestone: `M1f - Mechanism-first technical object discovery`
Last scientific issue: [#21](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/21)

## Scientific question

Under separately matched parameter, training-compute, and inference-resource regimes, can a learned controller jointly allocate a bounded budget among active-workspace attention, versioned episodic-memory operations, fixed-size compressed-state updates, recurrent computation, verification, and halting so that it improves the quality-cost Pareto frontier over strong fixed-routing and learned-routing baselines?

The working title is **Budgeted Workspace Models: Joint Allocation of Attention, Persistent Memory, and Recurrent Compute**.

M1 rejected this question as an original architecture contribution and retired the working title. M1b separately audited the owner's objective of giving future LLM development a technically actionable direction toward managed state, persistent memory, and adaptive computation. That route also returned `STOP`: the broad direction is directly anticipated, the implementation-neutral transition shell reduces to known systems and decision-theory objects, and no distinct prediction survives.

M1c then generated sixteen independently motivated objects covering revision repair, dependency closure, compaction certificates, concurrency, replay, migration, causal read sets, procedural drift, longitudinal feedback, revision hysteresis, evaluation carryover, and stability scaling. All sixteen failed direct anticipation, strongest-composite anticipation, generic reduction, or the requirement to specify distinct technical content. The program still has no article-eligible route.

M1d next generated 24 objects specifically aimed at a non-factorizing relation between governed persistent state and adaptive compute. The gate excluded every M1c family, validity-before-compute restatements, another joint router, and narrative synthesis. One candidate was directly anticipated, six were reconstructed by positive composites, nine conditionally reduced to known theory, two were unsupported and non-distinct, and six violated the no-recycling boundary. Zero survived. The program still has no article-eligible route.

M1e directly tested the restricted-class opening left by M1d. It screened 24
communication, streaming, causal-identification, and learning formulations. Of
these, 22 fix the required information, order, state, transcript, compute,
feedback, randomness, training, and strongest factorized comparison classes;
two are retained as unsupported admission failures rather than being
misreported as reductions. The accepted result is nine direct
anticipations, one positive composite, nine generic reductions, three scope
violations, two unsupported non-distinct sketches, and zero survivors. Decision
0007 passed independent scientific, bibliographic, and governance review and
merged through protected PR #18. The program still has no article-eligible
route.

M1f mapped all 64 prior formulations before constructing nine objects
sequentially. The apparently external primitives either collide directly,
reduce to timing privacy, information flow, communication, pebbling, mechanism
design, coding, migration, or verification, or are falsified by an exact
compiler. The recovered upstream report is now available, but its central
mission-tokenization proposal misclassifies recommender item tokenization as
lexical tokenization and otherwise assembles established components. Accepted
Decision 0008 returns `STOP` with zero admitted objects after independent
scientific, bibliographic, and governance reviews all passed on commit
`76d3ae0ee6266a5f8031e66f83f0d79b405fe033`. Protected integration is pending.

## Candidate contribution hypothesis

The following hypothesis is retained as the historical M0 candidate and was stopped by M1. It is not an active article claim. The candidate was a non-factorizing joint budget-allocation policy and its falsifiable evaluation. The project does not claim that attention, external memory, state-space recurrence, adaptive computation, provenance, or shared workspaces are individually novel.

The paper is not eligible to proceed as an architecture contribution merely because it combines those mechanisms or renames their roles. At least one preregistered result must distinguish the proposal from the strongest fixed composite and separately controlled composite. The acceptable result must be either a causal interaction attributable to joint allocation or a genuinely new empirical phenomenon, benchmark, or resource-accounting result that changes what can be concluded about the memory-compute trade-off. If neither survives, the project stops instead of rewriting prior work.

The permitted provisional formulation is:

> Attention is used as the communication and computation operator of a bounded active workspace, rather than as a sufficient mechanism for persistent memory.

This is a design statement until supported by comparative evidence. It is not a claim that attention cannot implement memory or that the proposed system is a cognitive model.

## Hypotheses

### Primary alternative

At controlled data and declared resource budgets, the proposed joint controller increases the hypervolume of at least one preregistered quality-cost Pareto frontier, with a 95% confidence interval excluding zero, against the strongest eligible baseline.

### Primary null

After complete resource accounting and uncertainty estimation, the proposed controller does not improve Pareto hypervolume against the strongest eligible baseline.

### Secondary hypotheses

1. Length extrapolation degrades more slowly out of distribution.
2. Versioned insert, supersede, revoke, expire, and rollback operations improve value-and-version exact match.
3. Additional recurrent computation is allocated to instances with independently measured difficulty.
4. Provenance interventions causally alter decisions on tasks whose target explicitly depends on provenance.
5. Typed transactional writes reduce persistent poisoning without an unacceptable utility loss.

## Operational definitions

- **Active workspace, `W_t`:** a dense set of slots whose configured capacity is independent of total history length. Attention communicates and computes within these slots.
- **Episodic memory, `E_t`:** an append-oriented, versioned store. Selected payloads and their provenance are retained losslessly. Retrieval may be approximate, and total storage may grow with episodes.
- **Compressed state, `S_t`:** a fixed-dimensional recurrent or state-space summary. It is not assumed to be lossless.
- **Budget, `B_t`:** a vector of explicit ceilings and measured consumption. It includes training FLOPs, inference FLOPs, wall-clock latency, HBM, bytes moved, persistent storage, reads, writes, recurrent steps, and energy where measurable. These axes must not be collapsed into a claim of simultaneous equality.
- **Joint controller, `pi_phi`:** one policy that chooses among `PROMOTE`, `RETRIEVE`, `APPEND`, `SUPERSEDE`, `REVOKE`, `CONSOLIDATE`, `PONDER`, `VERIFY`, and `HALT` under `B_t`.
- **Exact episodic content:** bitwise or schema-exact retention of selected stored payloads. It does not mean exact retrieval, bounded infinite memory, or error-free generation.
- **Provenance:** immutable source identity, source locator, version, event time, confidence, permissions, and dependency links bound to a stored payload.
- **Adaptive computation:** a variable number of recurrent steps with a configured hard maximum and a complete decision trace.
- **Comparable baseline:** a baseline evaluated with the same data, tokenizer, split, tuning allocation, instances, seeds policy, and one explicitly named resource-matching regime.

## Required invariants

1. Workspace capacity is independent of total sequence length.
2. Compressed-state dimensionality is fixed for a declared model configuration.
3. Selected episodic payloads are stored losslessly; retrieval quality is reported separately.
4. Provenance cannot be silently detached from or rewritten independently of its stored payload.
5. Recurrent iterations, reads, writes, and retrieved items have hard configurable bounds.
6. Every memory mutation, retrieval, routing action, verification action, and halt decision is traceable.
7. Near-linear complexity may be claimed only when workspace size, retrieval top-k, and expected recurrent iterations remain bounded. Episodic storage, indexing, and transfers are reported separately.

## Scope

The historical M0 paper scope covered bounded workspace communication, selected lossless episodic memory, fixed-size compressed state, bounded adaptive computation, provenance, recall, temporal mutations, length extrapolation, and physical cost. Decisions 0003 through 0007 stop that scope, its direction-setting successor, and the M1c/M1d/M1e object sets. Accepted Decision 0008 additionally stops all nine M1f mechanism-first attempts after independent review. Decision 0007 passed protected integration; Decision 0008 still awaits it. None is authorized for drafting or implementation.

Advanced security mechanisms such as ACL systems, capability models, taint tracking, prompt-injection defenses, and exfiltration controls are a separate extension. Explicit causal world models, counterfactual objectives, and causal losses are also a separate extension.

## Decision gates

### M0 exit

- inputs, resources, licenses, repository controls, risks, and stop rules are recorded;
- the governance validator passes;
- independent functional handoffs are available for novelty, theory, protocol, and bibliography;
- no unresolved blocker makes M1 invalid.

### M1 novelty gate

Return `PIVOT` or `STOP` if the defensible difference is only an untested assembly, renaming, or narrative synthesis of known components. `PIVOT` requires a precise new empirical question and a discriminating experiment against the strongest composite. Return `STOP` if no causal interaction or genuinely new empirical phenomenon remains identifiable. A `GO` permits formalization, not model implementation.

### Directional-thesis gate

The direction-setting pivot could proceed to article design only if it defined an implementation-neutral technical contract and at least one falsifiable regime prediction not already supplied by memory-OS, agent-OS, stateful-agent, long-context, test-time-learning, or systems-roadmap work. M1b applied this rule and returned `STOP`. The contract shell and every proposed regime prediction were anticipated, generic, tautological under their assumptions, or unsupported without a distinct technical object.

### Distinct-object reopening gate

M1c required every independently motivated object to state a new observable, mechanism, estimator, invariant, bound, or theorem; a decisive falsifier; a negative regime; the strongest prior-art composite; a generic-theory reduction; and a minimum discrimination burden. A testable LLM-specific relabeling of dynamic computation, semantic transactions, I-confluence, provenance, causal intervention, rejection, branching, stability, hysteresis, path effects, or carryover does not pass. An exact application axis being unreported also does not pass when a positive composite already supplies its protocol ingredients, phenomenon class, and ordinary estimator. M1c applied this rule and returned `STOP` for all sixteen candidates.

### Non-factorizing state-compute gate

M1d required a new mechanism, estimator, invariant, bound, theorem, or predictive law outside M1C-C01 through M1C-C16. Each object had to state a decisive falsifier, a negative regime, its strongest direct or composite collision, a generic reduction, an identified comparison class, and a minimum discrimination burden before implementation. A fixed-history behavioral joint distribution factorizes under unrestricted information passage, but this fact does not establish causal, computational, optimization, learning, or sample-efficiency equivalence. A future behavioral separation must prove a result inside a preregistered intrinsic information, communication, computation, or learning class; other claim types require their own matched estimand or bound. M1d applied this rule and returned `STOP` for all 24 candidates.

### Intrinsic restricted-class gate

M1e requires the task, observation order, online causality, persistent and
message budgets, compute or oracle budget, feedback, shared randomness,
training information, and allowed communication to be fixed before evaluation.
The strongest factorized comparator may be co-designed and jointly trained and
receives every resource and observation allowed to the candidate. A candidate
must state a theorem, identified estimand, or transportable law that survives
communication, streaming, cell-probe, time-space, causal, POMDP, online,
distributed-learning, and optimization reductions. A relabeled generic open
problem, different operation class, weaker comparator, recycled M1c/M1d object,
unsupported sketch, or empirical interaction cannot pass. M1e returns `STOP`
for all 24 screened formulations after corrected independent review.

### Mechanism-first object gate

M1f requires a complete crosswalk against M1C-C01 through M1E-C24 before an
object may be admitted. The object must fix a primitive, intrinsic class,
strongest symmetric comparator, exact result, decisive falsifier, negative
regime, and generic-reduction boundary before an empirical search. Public
inputs, randomness, codecs, shared activations, and permitted frontends must be
available symmetrically. A category error, constant-factor common-subexpression
saving, exact transcode, generic privacy or mechanism-design problem, direct
collision, or recycled migration object returns `STOP`. M1f applies this gate
to nine sequential attempts and proposes zero admissions.

### M4 oracle gate

Return `PIVOT` or `STOP` if an oracle router fails to produce a practically relevant advantage under complete accounting relative to fixed, random, write-all, write-none, and separated-controller policies.

### Confirmatory success threshold

A quality or cost result requires at least one of the following, plus replication at two model sizes, survival against the composite baseline, and no relative degradation greater than 1% on the primary natural-task metric:

- at least 5 percentage points in length-generalization AUC with the lower 95% confidence bound above 3 points; or
- at least 20% reduction in a preregistered physical cost at non-inferior quality.

These thresholds are necessary but insufficient for article eligibility. The architecture route also requires a preregistered practically meaningful coordination-interaction threshold whose 95% confidence interval clears that threshold, superiority to the same-component fixed and separated policies, non-degenerate response to resource-price interventions, and transfer beyond component-encoded synthetic tasks. Failure closes the architecture route. The empirical route instead requires a component-agnostic benchmark or accounting result that changes a comparative conclusion across strong architecture families and remains useful when the candidate model loses.

### Refutation or claim-reduction triggers

- gains disappear under the declared matched budget;
- the router converges to write-all, read-all, fixed-depth, or another degenerate policy;
- episodic memory, compressed state, adaptive depth, or provenance can be removed without a meaningful effect;
- provenance interventions do not affect provenance-dependent targets;
- gains remain synthetic-only;
- irregular kernels erase theoretical savings in measured latency, memory traffic, or energy;
- variance prevents independent reproduction.

## Governance

The mandatory lifecycle is issue, milestone, isolated branch, issue-linked commits, pull request with `Closes #N`, independent functional review, CI, merge, and state/registry update. `docs/research/STATE.md` is the operational source of truth. No agent may approve its own scientific conclusion without a distinct review pass.

No arXiv submission, release, deployment, paid compute commitment, dataset redistribution, or license selection is authorized by this charter.
