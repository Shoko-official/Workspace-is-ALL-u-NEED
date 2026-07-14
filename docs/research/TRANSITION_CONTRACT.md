# Managed-State Transition Contract Audit

Status: `REDUCTION_TARGET_STOPPED`
Issue: `#5`
Search freeze: `2026-07-14`

## Purpose

This document operationalizes the proposed transition framework far enough to test whether it contains a new technical object. It is not a recommended architecture, a theorem, a validated policy, or a manuscript specification.

The candidate asks whether pre-outcome workload properties `Omega`, semantic guarantees `G`, and a vector resource envelope `B` can determine when a system incurs an obligation to maintain governed state or to allocate computation adaptively. The audit returns `STOP`: the formal shell is reconstructible from prior systems and generic decision theory, while the missing quantitative rule is unspecified rather than distinct.

## Candidate objects

### Workload descriptor `Omega`

`Omega` is a distribution over event and query traces, represented only by quantities observable before the outcome of a candidate implementation is known.

| Quantity | Operational measurement | Invalid use |
|---|---|---|
| Dependency horizon | Event or wall-clock distance between creation of a fact and the last query whose correct result depends on it | Labeling a case long-horizon after observing a model failure |
| Cross-query reuse | Number of later eligible queries per state creation or update event | Counting only successful cache or memory hits |
| Mutation load | Updates, supersessions, expirations, and revocations per unit time or per query | Defining mutation from the operations chosen by a favored system |
| Validity window | Declared maximum age or external validity interval for an answerable fact | Inferring freshness from answer correctness |
| Dependency density | Fraction of queries requiring one or more earlier events, with the dependency graph fixed independently of an implementation | Treating every retrieved item as necessary evidence |
| Exactness and provenance demand | Contract flags attached to the task before execution | Calling provenance necessary only when a provenance-aware system wins |
| Arrival process | Query and update rates, burstiness, and tail inter-arrival quantiles | Using measured service latency as a workload feature |
| Difficulty dispersion | A preregistered query-side proxy available before routing | Using generated loss, answer correctness, or realized token count unless explicitly allowed as an online probe |

These dimensions are not retained as a contribution. [Agent Memory](https://arxiv.org/abs/2606.06448), [Agent-Native Memory](https://arxiv.org/abs/2606.24775), and existing long-horizon systems already condition recommendations and feasibility on workload, update, reuse, freshness, and bottleneck structure.

### Guarantee contract `G`

For a trace `tau`, a contract is a finite set of obligations

`g_j = (domain_j, predicate_j, tolerance_j, window_j, permitted_failure_j)`.

The predicates apply to observable behavior rather than to a storage topology. They may cover:

- current-version use and rejection of superseded or revoked values;
- retention, expiration, deletion, and verified forgetting;
- provenance binding and principal-scoped access;
- bounded degradation, explicit failure, and non-silent infeasibility;
- replay, rollback, recovery, and restoration of the next valid state view;
- traceability of committed external effects.

A contract violation is an observed predicate failure outside its declared tolerance. A missing component name is never a violation.

This object is anticipated by the strongest composite of [ClawVM](https://arxiv.org/abs/2604.10352), [TOKI](https://arxiv.org/abs/2606.06240), [Verifiable Memory Governance](https://arxiv.org/abs/2604.16548), [MemOS](https://arxiv.org/abs/2507.03724), and the versioned [State-Aware Runtime](https://doi.org/10.33774/coe-2026-vt9t2-v2) working paper.

### Resource envelope `B`

`B` is a vector of separately reported limits and lifecycle charges:

`B = (FLOPs, latency, throughput, volatile_memory, bytes_moved, persistent_bytes, reads, writes, energy, maintenance_work)`.

Each coordinate declares its aggregation and tail statistic. A scalar utility may be reported for a declared deployment preference, but it does not establish simultaneous budget matching. Construction, update, retrieval, serving, invalidation, recovery, and teardown costs remain attributable.

This accounting is required hygiene, not a distinct object. Existing characterizations already measure construction and service costs, HBM or VRAM, power, energy, storage, freshness, and workload-dependent amortization.

### Adequacy relation

For implementation `I`, workload evidence `E`, and candidate tuple `(Omega,G,B)`, the proposed relation is set-valued:

`A(I; Omega,G,B,E) in {ADEQUATE, SEMANTIC_VIOLATION, RESOURCE_VIOLATION, INCOMPARABLE, ABSTAIN}`.

- `ADEQUATE`: every tested contract predicate and resource constraint passes with its preregistered uncertainty bound.
- `SEMANTIC_VIOLATION`: at least one guarantee fails beyond tolerance.
- `RESOURCE_VIOLATION`: at least one resource coordinate exceeds its bound.
- `INCOMPARABLE`: two adequate implementations trade off non-dominated resource or quality coordinates under no declared scalar preference.
- `ABSTAIN`: coverage, uncertainty, or identifiability is insufficient for a compliance or ordering decision.

Architecture labels confer no adequacy. The relation is ordinary contract checking plus constrained multiobjective comparison; notation does not make it a new scientific object.

### Candidate transition rule `T`

The most charitable implementation-neutral form is:

`T(Omega,G,B,E) -> (state_obligation, compute_obligation, decision_status)`.

The outputs are obligations, not products:

- no cross-invocation state obligation, or a durable validity-governed state obligation;
- fixed computation is admissible, or bounded adaptive allocation is a candidate;
- decided, infeasible, incomparable, or abstain.

A feasibility boundary excludes a class because no member can satisfy `G` under the stated assumptions and `B`. An efficiency boundary changes Pareto ordering among still-feasible classes. A measured performance loss does not prove infeasibility, and a semantic obligation does not prove one implementation superior.

## Reduction result

| Candidate object | Closest positive reconstruction | Disposition |
|---|---|---|
| `Omega` | Stateful-workload characterization, query/update regimes, freshness constraints, reuse amortization, and bottleneck-dependent recommendations | `ANTICIPATED` |
| `G` | Typed minimum-fidelity state, temporal isolation, provenance, authorization, scoped retrieval, rollback, recovery, and verified forgetting | `ANTICIPATED` by strongest composite |
| `B` | Multi-phase physical accounting and Pareto or hard-resource constraints | `ANTICIPATED` |
| `A` | Assume/guarantee checking, SLO compliance, robust constrained comparison, Pareto dominance, and reject or abstain decisions | `ANTICIPATED` by generic theory |
| State transition | Memory-OS and state-aware runtime positions plus context-only, selective-state, and harmful-memory regimes | `ANTICIPATED` as direction |
| Compute transition | Value of computation, adaptive depth, evidence/reasoning routing, and cost-conditioned stopping | `ANTICIPATED` |
| Unified quantitative `T` | No complete calibrated cross-family estimator was identified, but none is specified here either | `UNSUPPORTED`, not `DISTINCT_CANDIDATE` |

The direct anti-rewrite collision is unusually strong. State-Aware Runtime already argues that future long-horizon reliability depends on explicit runtime governance rather than prompt accumulation, including canonical state, validation, commit, rollback, recovery, permissions, and audit. PLACEMEM separately proposes a compute-aware, correction-aware memory plane with versioned validity and reusable runtime state. Recasting those positions as `Omega/G/B/T` would change vocabulary and organization, not an observable decision or falsifier.

## Residual test: state validity before adaptive compute

The narrowest residual considered was:

> Under matched queries and models, a router that tests whether governing state is current and sufficient before buying additional reasoning should dominate a difficulty-only compute router when persistent state is stale, missing, or contradictory.

It is experimentally falsifiable through a state-validity by compute-budget factorial. It is not retained as a contribution for this issue:

1. [STALE](https://arxiv.org/abs/2605.06527) already isolates current-state adjudication and shows that retrieving updated evidence does not ensure that it governs downstream reasoning.
2. [X-Router](https://aclanthology.org/2026.findings-acl.994/) already separates evidence necessity from reasoning necessity under a cost-quality objective.
3. [PLACEMEM](https://arxiv.org/abs/2607.04089) already couples validity, correction, runtime-state reuse, invalidation, and compute-aware routing in one systems direction.
4. [PersistBench](https://arxiv.org/abs/2602.01146) reports that reasoning versus non-reasoning changes memory-induced failures inconsistently across model families and does not resolve near-saturated regimes.
5. Value-of-computation metareasoning already says to buy computation only when its expected utility exceeds its cost.

The exact factorial may remain unreported in this source set, but search silence is not novelty evidence. No LLM-specific estimator, margin, theorem, or cross-family law remains after label substitution and strongest-composite reduction. The residual is therefore `UNSUPPORTED_NOT_DISTINCT`, not a `PIVOT`.

## Disposition

The broad direction-setting article route fails component erasure, label substitution, strongest-composite reduction, generic-theory reduction, and agenda derivation. Its negative regimes are scientifically necessary, but they are also already part of the prior-art composite.

`STOP` means:

- do not draft a managed-state manifesto, roadmap, maturity model, unified framework, or migration diagram from these materials;
- do not present `Omega/G/B/T`, the adequacy labels, or the validity-before-compute slogan as original results;
- do not weaken the claim until it becomes a survey after the originality gate fails;
- do not implement or benchmark the stopped framework under issue #5.
