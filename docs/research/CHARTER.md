# Research Charter

Status: `DRAFT`
Version: `0.1.0`
Milestone: `M0 - Audit and charter`
Tracking issue: [#1](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/1)

## Scientific question

Under separately matched parameter, training-compute, and inference-resource regimes, can a learned controller jointly allocate a bounded budget among active-workspace attention, versioned episodic-memory operations, fixed-size compressed-state updates, recurrent computation, verification, and halting so that it improves the quality-cost Pareto frontier over strong fixed-routing and learned-routing baselines?

The working title is **Budgeted Workspace Models: Joint Allocation of Attention, Persistent Memory, and Recurrent Compute**.

## Candidate contribution hypothesis

The candidate contribution hypothesis is a non-factorizing joint budget-allocation policy and its falsifiable evaluation. It is not yet a technically established mechanism or a positive novelty finding. The project does not claim that attention, external memory, state-space recurrence, adaptive computation, provenance, or shared workspaces are individually novel.

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

The core paper may cover bounded workspace communication, selected lossless episodic memory, fixed-size compressed state, bounded adaptive computation, provenance, recall, temporal mutations, length extrapolation, and physical cost.

Advanced security mechanisms such as ACL systems, capability models, taint tracking, prompt-injection defenses, and exfiltration controls are a separate extension. Explicit causal world models, counterfactual objectives, and causal losses are also a separate extension.

## Decision gates

### M0 exit

- inputs, resources, licenses, repository controls, risks, and stop rules are recorded;
- the governance validator passes;
- independent functional handoffs are available for novelty, theory, protocol, and bibliography;
- no unresolved blocker makes M1 invalid.

### M1 novelty gate

Return `PIVOT` or `STOP` if the defensible difference is only an untested assembly, renaming, or narrative synthesis of known components. `PIVOT` requires a precise new empirical question and a discriminating experiment against the strongest composite. Return `STOP` if no causal interaction or genuinely new empirical phenomenon remains identifiable. A `GO` permits formalization, not model implementation.

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
