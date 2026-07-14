# M1 Terra Empirical-Route Audit

Date: 2026-07-14

Role: Terra-Engineering / Luna-RedTeam

Target: Sol-PI, milestone M1, issue [#3](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/3)

Candidate model selection: non-controllable

Verdict: STOP

Confidence: high for the empirical route audited here

## Decision in one sentence

Do not turn WAIN-Core, the Joint Memory Machine, or complete physical accounting into the fallback paper: the proposed temporal operations, provenance interventions, replay semantics, adaptive memory management, system profiling, and ranking-shift claims are already substantially covered by primary work, while JMM encodes the candidate's component roles by construction.

This is a route-specific decision. It does not independently decide the narrowed causal-coordination mechanism reviewed elsewhere in M1.

## Objective and anti-rewrite criterion

The task was to test the second potentially publishable route left by M0:

1. a component-agnostic benchmark of temporal memory, provenance, mutations, and replay; or
2. complete end-to-end physical accounting that changes the comparative ranking of memory systems.

The governing standard is stricter than finding an uncombined metric list. A contribution is not new merely because it:

- places known temporal operations in one generator;
- combines existing memory benchmarks;
- measures more resource axes in one table;
- gives familiar failure modes new names;
- favors the proposed model on a benchmark whose instances require the proposed components.

A surviving route had to expose one independently measurable phenomenon not already isolated by the closest benchmarks, remain useful if the candidate model lost, and change a scientific conclusion rather than improve presentation or coverage.

No such phenomenon survived this audit.

## Evidence and scope

The audit used the M0 charter, protocol, novelty review, risk register, decision 0002, and the existing Terra and Luna handoffs. In particular:

- WAIN-Core Temporal Episodic Memory includes insert, update, supersede, delete, expire, rollback, temporal-version queries, conflicting sources, and dependency invalidation.
- JMM requires episodic retrieval, compressed-state use, recurrent computation, and provenance output in every accepted instance.
- The protocol already acknowledges that JMM is a diagnostic stress test, not primary evidence of architectural necessity.
- The candidate accounting vector includes model execution, index construction and maintenance, reads, writes, transfers, persistent storage, compilation, warm-up, latency, HBM, bytes moved, energy, and throughput.

The pass prioritised primary papers and official proceedings records. It is not a PRISMA completion certificate: the search interface did not expose reproducible database result totals, patent searching was out of scope, and several closest threats are recent 2026 preprints or anonymous review submissions whose versions may change.

Those limitations weaken any exhaustive absence claim. They do not rescue a route for which multiple direct anticipations were found.

## Search journal

Access date for every record: 2026-07-14.

The exact query strings used in the bounded search were:

1. site:arxiv.org LLM agent memory benchmark temporal update delete rollback provenance
2. site:openreview.net long term memory benchmark LLM agents temporal knowledge update
3. site:aclanthology.org benchmark long term conversational memory temporal reasoning knowledge update LLM
4. site:arxiv.org bitemporal knowledge graph agent memory benchmark
5. site:arxiv.org LLM memory system benchmark latency token cost storage write read energy HBM
6. site:aclanthology.org LLM agent memory benchmark efficiency latency storage cost
7. site:openreview.net memory benchmark LLM agent latency efficiency storage writes retrieval
8. site:arxiv.org RAG benchmark end-to-end energy HBM bytes moved index construction retrieval generation Pareto
9. site:aclanthology.org LLM RAG provenance citation intervention source metadata conflict
10. site:openreview.net agent memory provenance benchmark stale conflicting source temporal
11. Direct resolution of arXiv identifiers 2410.10813, 2507.05257, 2603.01966, 2604.20006, 2606.27472, 2605.06527, 2509.11145, 2602.18493, 2508.19828, 2601.01885, 2606.09900, 2606.06240, 2606.12290, 2603.10765, 2606.06448, 2606.24775, 2604.15774, and 2606.29178.
12. Direct resolution of OpenReview records T3S5Blz7jM, CCSztIjmOy, iGRGjdhl9r, sfrVLzsmlf, 9JiPHfleLn, and t33i8z9IeU.

The interface returned ranked surfaced records but no stable corpus total. Accordingly, this handoff records the actual primary records inspected and does not fabricate search-result counts.

## Primary records and locators

### Temporal, evolving, and selective memory

| Primary record | Directly relevant content | Locator read |
|---|---|---|
| [LongMemEval, arXiv:2410.10813](https://arxiv.org/abs/2410.10813) | Long-term information extraction, multi-session and temporal reasoning, knowledge updates, and abstention | Abstract; benchmark taxonomy and evaluation sections |
| [LoCoMo, ACL 2024](https://aclanthology.org/2024.acl-long.747/) | Very long multi-session conversational memory with temporal and multi-hop reasoning | §§3-5 |
| [MemoryAgentBench, arXiv:2507.05257](https://arxiv.org/abs/2507.05257) | Incremental interaction, retrieval, test-time learning, long-range understanding, and selective forgetting | Abstract; §§3-5 |
| [AMemGym, arXiv:2603.01966](https://arxiv.org/abs/2603.01966) | On-policy structured state evolution and separate write, read, and utilization diagnostics | §§3.1-3.4, §§4.2-4.4, §5 |
| [Memora, arXiv:2604.20006](https://arxiv.org/abs/2604.20006) | Changing and invalidated memories; scoring that penalizes obsolete-memory use | §§3.2-4.2 |
| [Supersede, arXiv:2606.27472](https://arxiv.org/abs/2606.27472) | Direct memory-update gap, current versus stale values, bounded memory, and update training | §§2-5 |
| [STALE, arXiv:2605.06527](https://arxiv.org/abs/2605.06527) | Implicit invalidation, state resolution, premise resistance, and policy adaptation | §§3-5 |
| [RECON, OpenReview:T3S5Blz7jM](https://openreview.net/forum?id=T3S5Blz7jM) | Cascading invalidations, source conflict, counterfactuals, multi-hop evidence, and temporal constraints | Abstract; §§3-5 |
| [Text2Mem, Findings of ACL 2026](https://aclanthology.org/2026.findings-acl.100/) | Typed memory-operation language including update, merge, lock, expire, delete, retrieve, and summarize, with executable reference behavior | §§3-5; Tables 2-3 |
| [Learning to Remember / UMA, arXiv:2602.18493](https://arxiv.org/abs/2602.18493) | Compact core state plus a structured CRUD bank; Ledger-QA continuous update tracking | §§3-4; Appendix B |
| [Memory-R1, arXiv:2508.19828](https://arxiv.org/abs/2508.19828) | Learned ADD, UPDATE, DELETE, and NOOP memory manager | §§3.1-3.3; Tables 2-4; Appendices B and D |
| [AgeMem, arXiv:2601.01885](https://arxiv.org/abs/2601.01885) | Unified long- and short-term management using store, retrieve, update, summarize, and discard actions | §§3-5 |
| [MemEvoBench, arXiv:2604.15774](https://arxiv.org/abs/2604.15774) | Noisy, biased, and adversarial memory evolution across domains and risk types | Benchmark construction and evaluation sections |
| [Selective Memory Retention, arXiv:2606.29178](https://arxiv.org/abs/2606.29178) | Bounded retention versus unbounded and cache heuristics, including noise and memory-efficiency stress | Method and evaluation sections |

### Version, provenance, replay, and structural integrity

| Primary record | Directly relevant content | Locator read |
|---|---|---|
| [Bi-temporal Engram, arXiv:2606.09900](https://arxiv.org/abs/2606.09900) | Lossless append-only episodes, bi-temporal knowledge graph, invalidation rather than deletion, provenance, supersession, and as-of filtering | §§3-5; Tables 1-3 |
| [APEX-MEM, ACL 2026](https://aclanthology.org/2026.acl-long.749/) | Append-only temporal evolution, conflict, and evolving information | §§3-5 |
| [TOKI, arXiv:2606.06240](https://arxiv.org/abs/2606.06240) | Bi-temporal operators, isolation, provenance and audit rows, replay consistency, and anomaly tests | §§3.1-4.6; Appendices D and F |
| [Selection Integrity, arXiv:2606.12290](https://arxiv.org/abs/2606.12290) | Provenance-authenticated records are insufficient when unauthenticated structure controls selection | §§3-6 |
| [ALCE, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.398/) | Automatic evaluation of citation correctness, completeness, and quality | Evaluation framework and experiments |
| [Do Metadata and Appearance Affect LLM Reasoning in RAG?, BlackboxNLP 2024](https://aclanthology.org/2024.blackboxnlp-1.24/) | Controlled swaps of publication time, source, and appearance across conflicting pages | Experimental setup and results |

### Routing and learned memory operations

| Primary record | Directly relevant content | Locator read |
|---|---|---|
| [Cost-Sensitive Store Routing, OpenReview:iGRGjdhl9r](https://openreview.net/forum?id=iGRGjdhl9r) | Routing among short-term, summary, long-term, and episodic stores with coverage, exact match, waste, token, and cost-sensitive objectives | §§3.2-3.4 |
| [GRU-Mem, arXiv:2602.10560](https://arxiv.org/abs/2602.10560) | Learned update and exit gates with speed-quality measurements | Method and experiments |
| [Memory-R1, arXiv:2508.19828](https://arxiv.org/abs/2508.19828) | Explicit learned CRUD choice | §§3.1-3.3 |
| [Learning to Remember / UMA, arXiv:2602.18493](https://arxiv.org/abs/2602.18493) | One policy over compact state and structured memory updates | §§3-4 |
| [AgeMem, arXiv:2601.01885](https://arxiv.org/abs/2601.01885) | Policy-level store, update, summarize, and discard behavior | §§3-5 |

### End-to-end systems and physical/resource accounting

| Primary record | Directly relevant content | Locator read |
|---|---|---|
| [RAGPerf, arXiv:2603.10765](https://arxiv.org/abs/2603.10765) | Modular end-to-end RAG profiling across query/update ratios, INSERT/UPDATE/DELETE, latency, throughput, CPU/GPU utilization, host/device memory, and I/O | §§3.2-3.4, §§5.2-5.8 |
| [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads, arXiv:2606.06448](https://arxiv.org/abs/2606.06448) | Phase-aware construction, retrieval, and generation costs across ten systems; read/write cost shifts, amortization, and freshness-latency trade-offs | Abstract; §§3-5 |
| [Are We Ready For An Agent-Native Memory System?, arXiv:2606.24775](https://arxiv.org/abs/2606.24775) | Twelve memory systems, five workloads, eleven datasets, maintenance, update correctness, long-horizon stability, and cost-performance | Abstract; §§3-5 |
| [MemBench, Findings of ACL 2025](https://aclanthology.org/2025.findings-acl.989/) | Effectiveness, efficiency, and capacity evaluation for memory systems | Benchmark and evaluation sections |
| [ShiftBench, OpenReview:CCSztIjmOy](https://openreview.net/forum?id=CCSztIjmOy) | Ranking instability and inversion under distribution shift | Benchmark design and rank-correlation results |
| [AMemGym, arXiv:2603.01966](https://arxiv.org/abs/2603.01966) | Different conclusions under on-policy state evolution versus off-policy evaluation | §§4.2-4.4; §5 |
| [Inverted Locality, OpenReview:t33i8z9IeU](https://openreview.net/forum?id=t33i8z9IeU) | Agent-memory access patterns and their systems implications | Characterization and implications sections |

## Overlap matrix

The verdict column tests publishable novelty, not whether the proposed implementation would be useful engineering.

| Proposed construct or claim | Closest prior work | Material overlap | Residual after comparison | Verdict |
|---|---|---|---|---|
| WAIN-Core temporal mutation stream | LongMemEval, MemoryAgentBench, Memora, Supersede, STALE, RECON, Text2Mem, Ledger-QA | Updates, stale-value rejection, invalidation, deletion/expiry, conflict, temporal questions, selective forgetting, typed mutations | One generator could place every operation together, but aggregation is not a new phenomenon | REJECT |
| Exact learned CRUD policy | Memory-R1, UMA, AgeMem, Text2Mem | ADD/UPDATE/DELETE/NOOP and broader typed operation selection already learned or executed | Candidate-specific controller coupling | REJECT as benchmark novelty |
| Versioned and bi-temporal semantics | Engram, APEX-MEM, TOKI | Append-only evolution, valid-time and transaction-time reasoning, as-of views, provenance, supersession, replay consistency | Candidate schema names and dependency invalidation details | REJECT |
| Rollback and replay fidelity | TOKI, Engram, MemOS from M0, RECON | Replay consistency, audit rows, historical state, invalidation chains, and counterfactual timelines | A single rollback opcode and executable oracle | REJECT |
| Payload-constant provenance intervention | Metadata/Appearance study, ALCE, RECON, Selection Integrity | Source/time swaps, citation support, source conflict, and structurally mediated provenance failures | Candidate-specific immutable pointer semantics | REJECT |
| JMM requirement that every instance use all proposed resources | The benchmark definition itself; AMemGym and existing state-evolution diagnostics as external comparators | The target construction assigns the component roles before evaluation | Hidden component-agnostic tasks would remove the circularity, but then become ordinary long-horizon state tracking | CIRCULAR, REJECT |
| Cost-sensitive routing among memory stores | Cost-Sensitive Store Routing, UMA, AgeMem, GRU-Mem | Learned route/update/exit actions with token, waste, speed, or cost objectives | One shared price vector over more action types | REJECT as empirical route; mechanism question belongs elsewhere |
| Complete read/write/index/transfer accounting | RAGPerf, Agent Memory Characterization, Agent-Native Memory System, MemBench | End-to-end construction, update, retrieval, maintenance, latency, memory, utilization, storage/I/O, and cost-performance | Energy, bytes moved, compilation, and warm-up could make the vector more complete | REJECT: remaining delta is axis completion |
| Accounting changes the system ranking | ShiftBench, AMemGym, Agent-Native Memory System, Agent Memory Characterization | Ranking/configuration changes under shift, on-policy evolution, workload mix, maintenance, and freshness | A particular new hardware/workload cell may yield another reversal | REJECT: the phenomenon is already known |
| Bounded retention under noisy mutation | Selective Memory Retention, MemEvoBench, Memora, STALE | Capacity limits, noise, obsolete records, invalidation, and downstream task success | Candidate controller's retention policy | REJECT |

## Why WAIN-Core is not a clean model benchmark

### Temporal Episodic Memory

The event family is useful for testing a store implementation, but it is not yet an independent test of learned memory:

1. Insert, supersede, revoke, expire, rollback, and as-of queries have deterministic event-sourced semantics.
2. A database or reference store can solve the state-transition layer without learning the candidate architecture.
3. Giving the model the same operation ontology rewards conformance to the proposed API, not discovery of a new memory capability.
4. Hiding the operation labels converts the task into evolving-state resolution, stale-premise rejection, or long-horizon tracking, all directly represented in STALE, RECON, Supersede, Memora, AMemGym, and Ledger-QA.

WAIN-Core can remain an internal conformance suite. It should not be presented as the new scientific object without a distinct phenomenon.

### Joint Memory Machine

JMM is more directly circular:

1. Every accepted instance is required to need episodic retrieval, compressed state, recurrent computation, and provenance output.
2. The benchmark constructor therefore assigns necessity to the exact candidate components.
3. Ablating a required information channel then confirms the constructor's premise, not architectural necessity in naturally occurring tasks.
4. Counterfactual indistinguishability checks improve oracle validity but do not remove the ontological selection bias.
5. If the action ontology and component roles are hidden, JMM collapses into component-agnostic long-context state tracking already covered by existing benchmarks.

The protocol is correct to label JMM diagnostic. It cannot carry the paper's novelty or anti-assembly claim.

An instructive nearby warning is Cost-Sensitive Store Routing: labels derived from query type can make routing performance partly reflect the labeling rule. WAIN/JMM would face a stronger version of the same problem if task construction exposes which store or state path should be used.

## Candidate phenomenon considered and rejected

No original phenomenon is retained.

The strongest last candidate was:

> Lifecycle-complete ranking reversal: charging creation, update, invalidation, retrieval, transfer, persistence, and rollback costs reverses the quality-cost ordering obtained from query-only evaluation.

It is measurable independently of the candidate model and would remain useful if that model lost. It still fails the novelty test:

- RAGPerf already varies query/update mixtures and profiles INSERT, UPDATE, DELETE, memory, I/O, latency, and throughput.
- Agent Memory Characterization already attributes construction, retrieval, and generation costs across ten systems and analyses amortization and freshness.
- Agent-Native Memory System already compares twelve systems across update correctness, maintenance, long-horizon stability, and cost-performance and reports that no architecture dominates.
- AMemGym and ShiftBench already establish evaluation-induced rank and configuration changes.

Adding energy, bytes moved, rollback, compilation, and warm-up could improve measurement integrity. It would not establish a new phenomenon unless a preregistered intervention contradicted the conclusions of these studies. No evidence presently supports that contradiction.

A second possible angle, history-equivalent snapshots with different event histories, was also rejected before proposal: TOKI directly tests replay consistency, while RECON includes counterfactual timelines and cascading invalidation.

## Design discriminant and conditions to reopen

No benchmark design is authorized by this handoff. Reopening the empirical route requires all of the following before implementation:

1. State one effect that is absent from the primary records above. A longer operation list is not an effect.
2. Define the effect without WAIN action names, candidate modules, or oracle access to the intended routing decision.
3. Use paired or randomized interventions whose visible task state is controlled and whose outcome cannot be solved by a deterministic event store alone.
4. Include at least three strong systems from different memory families, plus a non-neural database/reference-store control.
5. Freeze adapters and tuning budgets before seeing comparative results.
6. Predeclare the practically meaningful effect, estimand, multiplicity policy, missing-run policy, and stop threshold.
7. Show that the result changes a scientific conclusion beyond the published workload, maintenance, shift, or cost ranking results.
8. Preserve standalone utility if the candidate model ranks last: reusable data, executable oracle, architecture-neutral adapters, and an identifiable failure taxonomy.
9. Demonstrate feasibility under a written hardware, energy, storage, API, and labor budget.

Failure of any item returns STOP without a pilot.

## Feasibility and cost

The existing Terra environment audit records:

- one RTX 5080 with 16,303 MiB VRAM;
- PyTorch 2.11.0+cpu with no available CUDA runtime;
- a Docker client with no reachable Docker Desktop Linux daemon;
- no cluster or cloud budget;
- no energy meter;
- 1.65 TB free storage, already tight for the broader checkpoint and trace plan.

A credible lifecycle-complete comparison would need:

- pinned and isolated adapters for roughly ten to twelve heterogeneous memory systems to match the closest systems papers;
- query-heavy and update-heavy workloads, long mutation streams, multiple capacities, and at least five independent seeds for confirmatory ranking claims;
- separate construction, retrieval, generation, maintenance, invalidation, replay, and persistence traces;
- host/device transfer and storage telemetry;
- an external energy meter or a validated and explicitly limited proxy;
- controlled warm-up, compilation, cache, index-build, and failure accounting;
- licensing and reproducibility review for every system and dataset.

The current machine cannot support that claim as written. Repairing CUDA and Docker would only make a reduced pilot possible; it would not supply the multi-system engineering effort, energy instrumentation, or replication budget needed for a publishable systems comparison.

The least expensive decisive experiment is the literature audit already completed. It returned STOP. No compute should be spent to rediscover an already reported workload-dependent ranking effect.

## Stop rules

Apply these rules before any implementation:

1. STOP if a proposed task differs from a cited benchmark only by combining its operations or metrics.
2. STOP if novelty depends on measuring additional axes without a new intervention or conclusion.
3. STOP if benchmark admission rules encode use of the candidate components.
4. STOP if deterministic store semantics can solve the claimed memory phenomenon.
5. STOP if the benchmark is valuable only when the candidate wins.
6. STOP if the strongest baselines cannot be run with frozen, comparable adapters and budgets.
7. STOP if the ranking claim lacks a preregistered minimum change and uncertainty analysis.
8. STOP if the physical measurement plan lacks energy, transfer, storage, warm-up, and failed-operation policies while claiming complete accounting.
9. STOP if the required systems, seeds, traces, and instrumentation do not fit a written budget.
10. STOP if a fresh primary-source check finds a direct anticipation before protocol freeze.

## Verdict

STOP for the empirical fallback route.

The evidence does not support presenting WAIN-Core or JMM as a new benchmark contribution. WAIN-Core is suitable as an internal executable conformance and diagnostic suite. JMM is unsuitable as primary causal evidence because its construction encodes the proposed component roles.

The evidence also does not support a standalone paper whose novelty is complete accounting or ranking reversal. Recent systems work already evaluates construction, update, retrieval, maintenance, workload mix, stability, and cost-performance across broad sets of agent-memory systems. Completing the telemetry vector would be good experimental hygiene, not sufficient novelty.

This STOP is the appropriate anti-rewrite outcome. It avoids turning the strongest parts of prior work into a newly named benchmark package.

## Uncertainty

- RECON and several June 2026 records are preprints or review submissions; their archival status and versions must be rechecked if M1 is reopened.
- Search totals were unavailable, so this is not an exhaustive bibliometric review.
- A truly new phenomenon may still exist, but none was identified in the proposed temporal, provenance, mutation, replay, or physical-accounting space.
- The separate causal-coordination mechanism route is outside this handoff and must stand or fall on its own evidence.

## Files modified and verification

- Created docs/research/handoffs/2026-07-14-m1-terra-empirical-route.md only.
- No code, benchmark, dataset, ledger, bibliography, registry, or decision record was modified.
- Every positive overlap claim above is tied to a primary paper or official proceedings record.
- The proposed empirical route was evaluated for model-loss utility, circularity, feasibility, and explicit stop conditions.
