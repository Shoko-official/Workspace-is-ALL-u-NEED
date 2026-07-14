# Decision 0002: Initial novelty pivot

Date: `2026-07-14`
Status: `ACCEPTED`
Issue: [#1](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/1)
Milestone: `M0 - Audit and charter`

## Context

The candidate initially combined a bounded attention workspace, versioned episodic memory, fixed-size compressed state, adaptive recurrent computation, verification, halting, and explicit resource budgets. The repository owner requires that any resulting article make an original scientific contribution rather than rewrite, rename, or package prior work.

The bounded M0 screen read 27 primary records. HOLA and Sparse Delta Memory threaten the exact/explicit-memory plus recurrent-state claim; Adaptive Loops and Memory and Universal Transformers Need Memory threaten the memory-depth allocation claim; MemOS threatens versioning, provenance, transactions, lifecycle, and rollback; Mixture-of-Recursions, CAT, and Engram threaten adaptive resource routing and memory-compute frontier claims. Older workspace, external-memory, recurrent-memory, state-space, and adaptive-computation work covers the remaining individual components.

## Decision

Return `PIVOT` and stop the broad architecture-novelty claim.

Only the following research question may proceed to a dedicated M1 systematic review:

> Under hard per-instance action, recurrent-step, episodic-I/O, byte, and transfer ceilings, and under matched controller capacity, training compute, and complete physical accounting, does one non-factorizing policy coordinating a bounded workspace, online mutable versioned episodic I/O, fixed-size compressed state, verification, and halting improve a preregistered quality-cost frontier over the same strong composite with fixed routing and independently trained resource controllers?

This question is a hypothesis, not a novelty finding. M1 must either find a technically distinct disclosure gap and a feasible discriminating experiment or return `STOP`.

## Anti-rewrite gate

A future article is ineligible as an architecture contribution if its result can be explained by assembling known components, adding capacity or supervision, using weak baselines, renaming existing controls, or selecting a favorable accounting regime.

Eligibility requires at least one of:

1. a preregistered causal coordination interaction that is practically meaningful, survives the strongest fixed and separately controlled composites under complete accounting, and replicates at two sizes; or
2. a genuinely new benchmark, intervention suite, or physical-resource result that remains independently useful and changes the scientific conclusion even if the proposed model does not win.

If neither condition survives, the gate is `STOP`; prior work must not be converted into a new narrative.

## Required discriminating controls

1. A fixed composite containing HOLA/SDM-equivalent exact or explicit memory plus compressed state, Mixture-of-Recursions-equivalent adaptive depth/cache traffic, MemOS-style versioned transactional storage, and adaptive stopping.
2. Separately trained resource controllers with the same components and matched total controller capacity.
3. Random, write-all/read-all, write-none/read-none, fixed-depth, and oracle policies.
4. Randomized exogenous resource-price and hard-ceiling interventions.
5. A matched 2x2 study of local versus cross-resource observations and local versus joint gradient/objective coupling.
6. Full factorial component ablations and complete physical accounting, including index, transfer, mutation, compilation, warm-up, latency distribution, HBM, persistent storage, and energy where measurable.

## Alternatives considered

- `GO` on the original architecture was rejected because the components, pairwise combinations, and memory-compute trade-off are substantially anticipated.
- Immediate `STOP` was rejected because one narrow coordination question and a transaction/provenance benchmark may remain empirically discriminating, subject to a full M1 review.
- A related-work synthesis paper was rejected because it would not satisfy the required original contribution.

## Evidence

- `docs/research/handoffs/2026-07-14-terra-evidence.md`: page-level audit of 27 primary records, property matrix, closest composite, and falsifying experiments.
- `docs/research/handoffs/2026-07-14-sol-theory.md`: typed semantics, complexity bounds, identifiability threats, matched controls, and causal coordination contrast.
- `docs/research/handoffs/2026-07-14-terra-engineering.md`: matrix and resource feasibility, baseline tiers, oracle contract, leakage paths, and minimum decisive sequence.
- `docs/research/handoffs/2026-07-14-luna-librarian.md`: independent metadata, version, licence, and locator verification for all 27 records plus DNC.
- `docs/research/handoffs/2026-07-14-luna-cross-review.md`: independent anti-assembly review; all seven M0 findings resolved and final verdict `MERGE_READY` subject to PR CI.
- `docs/research/NOVELTY.md`: preregistered search protocol and initial-screen decision.

This is an initial gate, not a certificate that M1 is complete or that the narrowed question is novel.

## Consequences

- M0 may authorize only the dedicated M1 systematic-review issue.
- M2 formalization, benchmark implementation, model implementation, and training remain unauthorized.
- The broad working title and architecture claim must be treated as provisional until the M1 gate.
- Failure of the M1 distinction, M4 oracle/resource-price test, or coordination interaction closes the architecture direction as `STOP`; a separate empirical contribution may proceed only on its own evidence.
