# Decision 0003: Stop the current claims and pivot to a directional thesis

Date: `2026-07-14`
Status: `ACCEPTED`
Issue: [#3](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/3)
Milestone: `M1 - Systematic novelty review`
Supersedes: [Decision 0002](0002-initial-novelty-pivot.md)

## Context

Decision 0002 stopped the broad architecture claim but allowed two narrowly defined routes through M1:

1. a technically distinct joint constrained-policy mechanism with an identifiable causal coordination effect; or
2. an architecture-neutral benchmark, intervention, or physical-accounting phenomenon that would remain useful if the candidate model lost.

The repository owner additionally required that a prospective article not be a rewrite, renamed assembly, or narrative synthesis of prior work. M1 therefore tested the mathematical object, the closest learned-memory mechanisms, the proposed benchmark construction, and the proposed resource-accounting contribution separately.

The owner then clarified a second publication objective: the article should give future LLM research a concrete direction for moving from monolithic context use toward managed state, persistent memory, and adaptive computation. That objective is distinct from claiming invention of the component architecture. It can proceed only as a separately audited technical thesis with original, falsifiable content.

## Findings

### Mechanism route

The proposed state and typed action union form a constrained POMDP, or a CMDP after state or belief augmentation. Appending remaining resource to the state gives the standard budgeted-MDP form. Variable-duration retrieval and verification are options or SMDP actions.

For every stochastic policy over a disjoint union of typed actions,

\[
\pi(k,du\mid h)=\rho(k\mid h)q_k(du\mid h),
\]

where `rho` selects an operation class and `q_k` selects its conditional arguments. This exact decomposition preserves the trajectory distribution and shared feasibility mask. Consequently, "non-factorizing" is not a behavioral invariant and cannot establish a new control object. A shared neural parameterization may still affect optimization, but the current project specifies no new learning algorithm, guarantee, lower bound, or semantic invariant.

The remaining topology is also directly anticipated. [UMA](https://arxiv.org/abs/2602.18493) trains one policy over a compact core summary, a mutable structured memory bank, CRUD-like operations, retrieval, repeated tool use, and a terminal action. [GRU-Mem](https://arxiv.org/abs/2602.10560) adds learned recurrent update and exit gates. [AgeMem](https://arxiv.org/abs/2601.01885) integrates long- and short-term memory operations into one policy. Generic constrained and budgeted control is established by [Constrained Policy Optimization](https://proceedings.mlr.press/v70/achiam17a.html) and [Budgeted Reinforcement Learning in Continuous State Space](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html).

### Empirical route

The proposed WAIN-Core temporal operations overlap with benchmarks and environments that already isolate evolving state, stale memory, supersession, invalidation, selective retention, and memory updates. Direct threats include [Ledger-QA in UMA](https://arxiv.org/abs/2602.18493), [AMemGym](https://openreview.net/forum?id=sfrVLzsmlf), [Memora](https://arxiv.org/abs/2604.20006), and [Supersede](https://arxiv.org/abs/2606.27472). Version, provenance, supersession, and point-in-time behavior are also implemented by the [bi-temporal Engram](https://arxiv.org/abs/2606.09900).

The Joint Memory Machine is circular as primary causal evidence because its admission rule requires every instance to use the candidate's own component ontology. Hiding that ontology reduces the task to component-neutral evolving-state tracking already covered by the closest benchmarks.

Complete accounting remains required experimental hygiene, but it is not an independent contribution here. [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448) already attributes construction, retrieval, and generation costs across ten systems. [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775) evaluates twelve systems across storage, extraction, routing, maintenance, update correctness, stability, and cost-performance. Adding more telemetry axes without a new intervention or outcome-changing law would complete a metric vector, not establish a new phenomenon.

### Feasibility

The minimum credible mechanism experiment would require same-component fixed and separated policies, matched information and controller capacity, randomized multi-resource price interventions, a full observation-by-objective factorial, and replication. The minimum credible systems experiment would require reproducible adapters and lifecycle traces across approximately ten to twelve heterogeneous memory systems. Neither design has a written compute, instrumentation, energy, storage, or labor budget, and the recorded local environment cannot execute it credibly. More importantly, neither design currently tests a distinct contribution.

## Decision

Return `STOP` for both M1 contribution routes and `PIVOT` for the research program.

- The mechanism route is not a new technical object and is nearly anticipated by a small composite of direct prior work.
- The empirical route identifies no new architecture-neutral phenomenon; WAIN-Core is an aggregation of covered capabilities and JMM is circular for the intended claim.
- The physical-accounting route identifies no preregistered result that would extend or contradict the existing multi-system characterizations.
- The proposed article, including the working title **Budgeted Workspace Models: Joint Allocation of Attention, Persistent Memory, and Recurrent Compute**, is `NOT_ELIGIBLE`.

The only authorized pivot is a direction-setting technical article for future LLM development. Its candidate contribution is not the known component stack. It must instead define and defend all of the following as one independently testable framework:

1. a transition model describing when an LLM system must move from context-only processing to bounded active state, persistent governed memory, and adaptive internal computation;
2. implementation-neutral contracts for state classes, transitions, provenance, resource ceilings, observability, and failure handling;
3. measurable regime boundaries or decision rules that predict which state-management design should dominate for a declared workload and physical budget;
4. falsifiable predictions and counterexamples that can invalidate the transition model; and
5. a research agenda whose milestones follow from those predictions rather than from the candidate architecture's module list.

This directional route is a candidate, not an established original contribution. It requires its own prior-art audit against memory-OS, agent-OS, stateful-agent, long-context, test-time-learning, and systems-roadmap literature before any article drafting is authorized.

This decision does not claim that the proposed system would perform poorly. No model was implemented or trained, and no empirical null was tested. It states that a favorable result under the current formulation would not satisfy the project's originality burden.

## Anti-rewrite determination

The project must not convert this result into an architecture article by:

- adding the remaining known actions to UMA, GRU-Mem, AgeMem, or another learned memory agent;
- renaming a generic CMDP/BMDP policy as a non-factorizing workspace controller;
- combining existing temporal-memory tasks under the WAIN-Core label;
- using JMM to encode the necessity of the proposed components;
- reporting a larger accounting table without a new causal intervention, predictive law, or conclusion-changing result; or
- presenting the M1 literature synthesis itself as the original scientific contribution requested by the owner.

The directional pivot also fails if it merely turns those same sources into a survey, maturity model, manifesto, taxonomy, or roadmap without a new technical contract and falsifiable predictions.

## Alternatives considered

- `GO_TO_FORMALIZATION` was rejected because no distinct mechanism, theorem, invariant, or empirical phenomenon survived.
- A further `PIVOT` within the same architecture, routing, temporal-benchmark, provenance, or accounting claims was rejected because every surviving formulation was an assembly, coverage extension, or already known evaluation effect.
- A survey or negative novelty-audit article was rejected because it would not meet the owner's requirement for an original research contribution.
- Running a pilot anyway was rejected because implementation cannot repair a failed novelty gate and would consume resources without an eligible claim.
- Stopping the entire program was rejected after the owner specified the distinct direction-setting objective. That objective is retained only behind a new anti-rewrite novelty gate.

## Evidence

- `docs/research/handoffs/2026-07-14-m1-terra-systematic-search.md`: reproducible narrowed search, deduplication, version chains, and snowball closure.
- `docs/research/handoffs/2026-07-14-m1-sol-reducibility.md`: exact policy decomposition, CMDP/BMDP reduction, countermodels, and mechanism verdict.
- `docs/research/handoffs/2026-07-14-m1-terra-empirical-route.md`: benchmark circularity, existing empirical coverage, accounting audit, feasibility, and stop rules.
- `docs/research/handoffs/2026-07-14-m1-luna-librarian.md`: independent metadata, version, and locator verification.
- `docs/research/handoffs/2026-07-14-m1-luna-cross-review.md`: independent contradictory review of the integrated M1 decision.
- `docs/research/NOVELTY.md`, `docs/research/CLAIM_LEDGER.csv`, `docs/research/EVIDENCE_LEDGER.csv`, and `docs/research/LITERATURE_MATRIX.csv`: consolidated gate record.
- `paper/references.bib`: version-pinned bibliography for the decision-critical M1 sources; it is not a manuscript draft.

## Consequences

- M2 architecture formalization, benchmark implementation, model implementation, training, paid compute, and manuscript drafting remain unauthorized.
- No article is drafted from the stopped architecture or empirical routes.
- The repository remains a traceable negative gate record rather than a vehicle for repackaging prior work.
- The next authorized action is a new issue and milestone that audits the directional transition framework as its own contribution.
- The directional route must begin from an original technical contract and falsifiable regime predictions, not from another rearrangement of the stopped components.
