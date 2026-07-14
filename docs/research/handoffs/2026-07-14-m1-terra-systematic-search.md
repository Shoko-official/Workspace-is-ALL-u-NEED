# M1 Terra Systematic Novelty Search

Date: 2026-07-14

Role: Terra-Evidence

Target: Sol-PI, milestone M1, issue [#3](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/3)

Candidate model selection: non-controllable

Architecture-route verdict: `STOP`

Empirical-route verdict: `STOP`

Directional-pivot status: `NOT_AUDITED`, novelty `NOT_ESTABLISHED`

## 1. Decision

Stop the budgeted-workspace architecture and its fallback benchmark/accounting paper. Positive prior-art collisions, rather than an absence-of-evidence argument, decide the gate:

1. UMA already trains one policy over a compact core, a mutable structured memory bank, explicit CRUD and retrieval actions, recurrent tool use, consolidation, and a terminal answer action.
2. GRU-Mem already adds learned recurrent memory-update and exit gates.
3. AgeMem and Memory-R1 already learn broad memory-operation policies, while generic CMDP/BMDP, options, and routing results cover the proposed control abstraction.
4. Existing benchmarks and systems studies already isolate evolving state, supersession, invalidation, provenance, bounded retention, update cost, and evaluation-induced ranking changes.

Adding the remaining operation names, resource meters, or benchmark cases would be assembly or axis completion. It would not meet the project's anti-rewrite criterion.

This decision does not reject a separate direction-setting article intended to guide future LLMs toward stateful, actively managed memory. That is a new contribution class and a new research question. It was not the object of this search, has not been checked against position papers or roadmaps, and must not be described as novel on the basis of M1.

## 2. Objective, scope, and decision criteria

M1 tested two routes left open by M0:

1. whether the full action policy was a distinct technical object rather than a CMDP/BMDP, router, options, or known memory-agent composition; and
2. whether a component-agnostic temporal-memory benchmark or complete physical-accounting result exposed a new scientific phenomenon.

The search covered formal control, learned memory operations, recurrent update and halt, temporal mutation, provenance and replay, bounded retention, memory-system characterization, and cost-sensitive evaluation. It did not cover patents, non-public industrial systems, every commercial index, or the literature on position papers and future-facing research agendas.

A route survived only if it met at least one of these criteria:

- a behaviorally defined mechanism effect that could not be reduced to action relabeling or a generic arbiter plus conditional heads;
- a preregisterable causal interaction against same-component fixed and separated controls, beyond the already reported unified-versus-decoupled result;
- an architecture-neutral empirical phenomenon absent from the closest primary work, useful even if the candidate model lost; or
- a new algorithmic guarantee, lower bound, or control object beyond established constrained and budgeted decision processes.

The following did not count as novelty:

- placing known components or operation names in one diagram;
- making an existing memory manager end-to-end without a new causal result;
- combining existing benchmark families;
- completing a resource-accounting vector without changing a scientific conclusion;
- defining tasks that require the proposed components by construction; or
- renaming known mechanisms and presenting the result as a new architecture.

## 3. Search journal and observable counts

All searches and direct resolutions in this closeout were accessed on `2026-07-14`. The endpoint returned ranked records but no stable database corpus totals. Result counts are therefore `NON DISPONIBLE`; none is inferred from the visible page length.

### 3.1 Exact free-text queries retained in the M1 trace

1. `site:arxiv.org LLM agent memory benchmark temporal update delete rollback provenance`
2. `site:openreview.net long term memory benchmark LLM agents temporal knowledge update`
3. `site:aclanthology.org benchmark long term conversational memory temporal reasoning knowledge update LLM`
4. `site:arxiv.org bitemporal knowledge graph agent memory benchmark`
5. `site:arxiv.org LLM memory system benchmark latency token cost storage write read energy HBM`
6. `site:aclanthology.org LLM agent memory benchmark efficiency latency storage cost`
7. `site:openreview.net memory benchmark LLM agent latency efficiency storage writes retrieval`
8. `site:arxiv.org RAG benchmark end-to-end energy HBM bytes moved index construction retrieval generation Pareto`
9. `site:aclanthology.org LLM RAG provenance citation intervention source metadata conflict`
10. `site:openreview.net agent memory provenance benchmark stale conflicting source temporal`
11. `"Anatomy of Agentic Memory"`
12. `"Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning"`

The interrupted architecture pass did not retain every free-text query string in a reproducible log. Those strings are `NON DISPONIBLE` and are not reconstructed from memory. The decision-critical architecture records were instead closed by direct primary-record resolution below.

### 3.2 Exact direct-resolution bundles retained in the M1 trace

ArXiv identifiers:

`2410.10813`, `2507.05257`, `2603.01966`, `2604.20006`, `2606.27472`, `2605.06527`, `2509.11145`, `2602.18493`, `2508.19828`, `2601.01885`, `2606.09900`, `2606.06240`, `2606.12290`, `2603.10765`, `2606.06448`, `2606.24775`, `2604.15774`, `2606.29178`.

OpenReview identifiers:

`T3S5Blz7jM`, `CCSztIjmOy`, `iGRGjdhl9r`, `sfrVLzsmlf`, `9JiPHfleLn`, `t33i8z9IeU`.

Additional decision-critical direct resolutions:

- `arXiv:2602.10560v1` (GRU-Mem);
- `arXiv:2603.15658v1` (Cost-Sensitive Store Routing);
- `arXiv:2606.08656v1` (MemoPilot);
- [Constrained Policy Optimization](https://proceedings.mlr.press/v70/achiam17a.html);
- [Budgeted Reinforcement Learning in Continuous State Space](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html);
- [Constrained Markov Decision Processes](https://www-sop.inria.fr/members/Eitan.Altman/mdp1.html); and
- [Between MDPs and Semi-MDPs](https://www.ece.uvic.ca/~bctill/papers/learning/Sutton_etal_1999.pdf).

### 3.3 Counts that can and cannot be supported

| Quantity | Value | Basis |
|---|---:|---|
| Exact M1 free-text query strings retained | 12 | Journal above |
| Direct empirical arXiv identifiers retained | 18 | Direct-resolution bundle above |
| Direct empirical OpenReview identifiers retained | 6 | Direct-resolution bundle above |
| Unique primary works normalized across the M1 formal/architecture and empirical source tables | 43 | Title, authors, and canonical identifier deduplication |
| Closed targeted backward/forward snowball cycles | 1 | Section 5 |
| Stable result count per query | `NON DISPONIBLE` | Search endpoint did not expose a reproducible corpus total |
| Titles initially surfaced | `NON DISPONIBLE` | Not retained by the interrupted pass |
| Abstract-only exclusions | `NON DISPONIBLE` | No complete exclusion log was retained |
| Patent results | `NON DISPONIBLE` | Patent search was outside scope |

The M0 seed pass had separately opened 27 primary records. That count is not added to the 43 M1 works because cross-stage overlap was not normalized into a single PRISMA flow.

## 4. Deduplication and version chains

Records were normalized by canonical arXiv base identifier or proceedings identifier, then checked by title and authors. Multiple URLs, venue mirrors, HTML/PDF forms, and arXiv versions count as one work. The audit cites the newest primary version actually checked on the access date.

| Work | Version chain observed on 2026-07-14 | Version used | Deduplication decision |
|---|---|---|---|
| AgeMem, arXiv:2601.01885 | v1, 2026-01-05; v2, 2026-04-30 | `v2` | Two arXiv versions collapsed to one work |
| Memory-R1, arXiv:2508.19828 | v1, 2025-08-27; v2, 2025-08-29; v3, 2025-09-03; v4, 2025-10-08; v5, 2026-01-14 | `v5` | Five arXiv versions collapsed to one work |
| UMA, arXiv:2602.18493 | v1, 2026-02-13 | `v1` | ArXiv, HTML, PDF, and later submission mirrors collapsed to one work |
| GRU-Mem, arXiv:2602.10560 | v1, 2026-02-11 | `v1` | ArXiv and OpenReview/conference representations collapsed to one work |
| Cost-Sensitive Store Routing | arXiv:2603.15658v1 and OpenReview:iGRGjdhl9r | `v1` plus primary OpenReview metadata | Same title/work counted once |
| Conditional Memory via Scalable Lookup / Engram | arXiv:2601.07372v2 | `v2` | Kept distinct from the bi-temporal Engram |
| Bi-temporal Engram | arXiv:2606.09900 | Current record | Kept distinct because title, authors, mechanism, and identifier differ |

The name collision between the two Engram papers is not a version chain. Treating them as one record would erase the distinction between conditional lookup memory and a provenance/versioning system.

## 5. Targeted backward and forward snowball cycle

One bounded citation cycle was closed around the most decision-critical transition from a learned memory manager to a unified memory-and-task policy.

### 5.1 Backward step

Seed: [Memory-R1, arXiv:2508.19828v5](https://arxiv.org/abs/2508.19828v5).

Memory-R1's Introduction and Related Work trace its `{ADD, UPDATE, DELETE, NOOP}` action set to prior CRUD-style systems, especially Mem0 and MemGPT (§1, PDF/HTML discussion corresponding to the CRUD and Mem0 paragraphs; §2.1). Its own technical delta is learned operation selection and a separately trained answer agent (§§3.1-3.2). This backward edge shows that the operations are inherited primitives, not a new memory ontology.

### 5.2 Forward step

Forward target: [UMA, arXiv:2602.18493v1](https://arxiv.org/abs/2602.18493v1).

UMA explicitly cites Memory-R1 in §1 as a decoupled architecture, then unifies memory operations and question answering in one end-to-end policy (§§2.1-2.3, PDF pp. 2-4). Its §4.4 text reports a higher average for unified training than for the decoupled two-stage variant, but the unified value in that prose conflicts with the last column of Table 1. M1 uses only the direction of the disclosed comparison, not either disputed aggregate value. This closes the exact residual that M0 had left for a joint policy.

### 5.3 Closure check

An exact-title forward search for UMA surfaced the primary arXiv record and duplicate/mirror records, but no additional admissible primary work needed to decide the gate. Stable forward-citation counts were `NON DISPONIBLE`. The cycle is closed for the decision-critical lineage, not for exhaustive bibliometric recall.

Stopping here is evidence saturation under a positive-collision rule. The gate does not rely on asserting that no other work exists.

## 6. Decision-critical primary sources and locators

### 6.1 Architecture and control

| Primary source | Decision-critical overlap | Locator checked |
|---|---|---|
| [UMA, arXiv:2602.18493v1](https://arxiv.org/abs/2602.18493v1) | Single policy, compact core, structured mutable bank, CRUD, retrieval, recurrent tool loop, consolidation, terminal answer; unified-versus-decoupled ablation | §§2.1-2.3, PDF pp. 2-4; §4, PDF p. 8; Ledger-QA §3 |
| [GRU-Mem, arXiv:2602.10560v1](https://arxiv.org/abs/2602.10560v1) | Recurrent memory with learned update and exit gates and dedicated update/exit rewards | §§3.1-3.2.1, PDF pp. 4-6; experiments |
| [AgeMem, arXiv:2601.01885v2](https://arxiv.org/abs/2601.01885v2) | One policy selects `ADD`, `UPDATE`, `DELETE`, `RETRIEVE`, `SUMMARY`, and `FILTER` operations with task and cost signals | §3.1 and Table 1, PDF pp. 4-5 |
| [Memory-R1, arXiv:2508.19828v5](https://arxiv.org/abs/2508.19828v5) | Learned `ADD`, `UPDATE`, `DELETE`, `NOOP` manager plus an answer agent | §§3.1-3.3; Tables 2-4; Appendices B and D |
| [Cost-Sensitive Store Routing, arXiv:2603.15658v1](https://arxiv.org/abs/2603.15658v1) | Store-subset routing with accuracy-minus-access-cost objective | §§3.1-3.4, PDF pp. 2-3 |
| [MemoPilot, arXiv:2606.08656v1](https://arxiv.org/abs/2606.08656v1) | Memory updates formulated as a trainable sequential decision problem | §3.1, PDF p. 3 |
| [Constrained Policy Optimization](https://proceedings.mlr.press/v70/achiam17a.html) | Neural policies under auxiliary cost constraints | §4, PDF p. 2; method sections |
| [Budgeted Reinforcement Learning in Continuous State Space](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html) | Budget as policy input and part of the dynamics | §1, PDF p. 2; Definition 1 and Theorem 1, §2, pp. 2-3 |
| [Constrained Markov Decision Processes](https://www-sop.inria.fr/members/Eitan.Altman/mdp1.html) | Multiple objectives, inequality constraints, occupation measures | Chapters 2-4 |
| [Between MDPs and Semi-MDPs](https://www.ece.uvic.ca/~bctill/papers/learning/Sutton_etal_1999.pdf) | Variable-duration actions as options/SMDP decisions | Abstract and §2, PDF pp. 1-2 and 6-7 |

### 6.2 Empirical and benchmark route

| Primary source | Decision-critical overlap | Locator checked |
|---|---|---|
| [AMemGym, OpenReview:sfrVLzsmlf](https://openreview.net/forum?id=sfrVLzsmlf) | On-policy structured state evolution with separate write, read, and utilization diagnostics | §§3.1-3.4, §§4.2-4.4, §5 |
| [Memora, arXiv:2604.20006](https://arxiv.org/abs/2604.20006) | Obsolete and invalidated memory with a penalty for stale-memory use | §§3.2-4.2 |
| [Supersede, arXiv:2606.27472v1](https://arxiv.org/abs/2606.27472v1) | Bounded-memory supersession gap and a trainable temporal-currency reward | §3, PDF pp. 3-4; §5.3, pp. 7-8 |
| [Bi-temporal Engram, arXiv:2606.09900](https://arxiv.org/abs/2606.09900) | Append-only episodes, bi-temporal graph, provenance, invalidation, supersession, as-of filters | §§3-5; Tables 1-3 |
| [TOKI, arXiv:2606.06240](https://arxiv.org/abs/2606.06240) | Bi-temporal operators, isolation, audit rows, provenance, and replay consistency | §§3.1-4.6; Appendices D and F |
| [Text2Mem, Findings of ACL 2026](https://aclanthology.org/2026.findings-acl.100/) | Typed update, merge, lock, expire, delete, retrieve, and summarize operations | §§3-5; Tables 2-3 |
| [Selective Memory Retention, arXiv:2606.29178](https://arxiv.org/abs/2606.29178) | Capacity-bounded retention under noise and memory-efficiency stress | Method and evaluation sections |
| [RAGPerf, arXiv:2603.10765](https://arxiv.org/abs/2603.10765) | End-to-end query/update mixtures, CRUD, latency, throughput, utilization, memory, and I/O | §§3.2-3.4, §§5.2-5.8 |
| [Agent Memory Characterization, arXiv:2606.06448](https://arxiv.org/abs/2606.06448) | Construction, retrieval, generation, read/write shifts, amortization, and freshness costs | §§3-5 |
| [Agent-Native Memory System, arXiv:2606.24775](https://arxiv.org/abs/2606.24775) | Multi-system comparison of maintenance, update correctness, stability, and cost-performance | §§3-5 |
| [ShiftBench, OpenReview:CCSztIjmOy](https://openreview.net/forum?id=CCSztIjmOy) | Ranking instability and inversion under distribution shift | Design and rank-correlation results |

Recent 2026 preprints are used as direct novelty threats. Their presence defeats a claim of first disclosure even if later empirical conclusions change.

## 7. Overlap map

| Proposed object or claim | Closest anticipation | Residual after comparison | Gate |
|---|---|---|---|
| One learned controller over compressed state, mutable memory, retrieval, recurrence, and halt | UMA plus GRU-Mem; AgeMem | Additional operation labels, hard caps, and verifier action | `STOP`: near-direct topology plus known components |
| Non-factorizing joint action policy | Generic arbiter plus conditional heads; routing networks | Parameterization or optimization preference | `STOP`: not a behaviorally invariant object |
| Shared resource-price vector and hard ceilings | CMDP, BMDP, CPO, options/SMDP | Pathwise feasibility implementation | `STOP`: generic constrained-control construction absent a new guarantee |
| Learned CRUD and active memory maintenance | Memory-R1, UMA, AgeMem, MemoPilot | Candidate-specific schema | `STOP`: action-set assembly |
| Unified training beats separated stages | UMA's unified-versus-two-stage ablation | Cleaner factorial controls | `STOP` as novelty; the paper contains a conflicting unified aggregate value and M1 does not rely on its magnitude |
| Temporal mutation, supersession, expiry, rollback, provenance | Supersede, Memora, Text2Mem, TOKI, bi-temporal Engram | One combined generator | `STOP`: aggregation, not a new phenomenon |
| Component-agnostic evolving-state benchmark | Ledger-QA, AMemGym, Memora, Supersede, existing long-memory suites | Broader operation coverage | `STOP`: no independent unmeasured effect identified |
| Complete physical accounting | RAGPerf, Agent Memory Characterization, Agent-Native Memory System | Energy, bytes moved, compilation, warm-up, rollback in one vector | `STOP`: axis completion without a new conclusion |
| Accounting changes comparative ranking | ShiftBench and system-characterization results | One more hardware/workload cell | `STOP`: ranking instability is already known |
| Direction-setting agenda for future LLM migration toward active state and memory | Not searched under an agenda/position-paper protocol | Scope, theses, audience, falsifiable predictions, and distinct prior art remain undefined | `NOT_AUDITED`; no novelty claim permitted |

## 8. Why both publication routes stop

### 8.1 Architecture route

The formal object reduces to a constrained or budgeted decision process over the union of known actions. Any policy over that union can be represented as an arbiter choosing an action family followed by a conditional head choosing the family-local action. Calling one neural parameterization “non-factorizing” does not create a behaviorally distinct policy class.

UMA then removes the main practical residual: it already implements one learned policy over compact and structured mutable memory, recurrent tools, retrieval, consolidation, and task completion, and directly compares unified with decoupled training. GRU-Mem adds the learned update/stop pair. The remaining proposed actions are known primitives. No new theorem, lower bound, feasibility guarantee, or replicated causal interaction remains.

### 8.2 Empirical route

The temporal-memory proposal combines phenomena already isolated by Ledger-QA, AMemGym, Memora, Supersede, Text2Mem, TOKI, and the bi-temporal Engram. The accounting proposal makes the metric vector more complete, but RAGPerf and recent systems characterizations already measure lifecycle and workload costs, while ShiftBench already establishes ranking instability.

A benchmark that requires every candidate component by construction is circular. Hiding those component labels turns it into ordinary evolving-state tracking, which the cited work already covers. No architecture-neutral effect survived that would remain scientifically distinct if the candidate system ranked last.

## 9. Directional pivot is separate and unvalidated

The newly stated objective is broader than an architecture claim: give future LLM builders a direction as systems shift toward active, persistent, budget-aware state and memory management.

That objective may support a position paper, research agenda, reference taxonomy, or migration roadmap. M1 does not validate it. In particular:

- the position-paper and roadmap literature was not systematically searched;
- no unique thesis, audience, adoption prediction, or falsifiable directional claim has been frozen;
- the agenda's relation to UMA, GRU-Mem, AgeMem, Memory-R1, MemOS, and agent operating-system work has not been mapped;
- no evidence shows that this project was first to identify the direction; and
- the value standard for a direction-setting artifact differs from architecture novelty.

Therefore the directional pivot is `NOT_AUDITED`, its novelty is `NOT_ESTABLISHED`, and publication eligibility is `NOT_ESTABLISHED`. It must receive a new charter and prior-art search before prose is written. It may cite the stopped architecture as one synthesis or reference design, but may not relabel that synthesis as a new model.

## 10. Limitations

- This is a bounded closeout, not a PRISMA completion certificate.
- Stable database result totals and a complete title/abstract exclusion log were unavailable.
- Every free-text query from the interrupted architecture pass was not retained, so missing strings are explicitly marked `NON DISPONIBLE`.
- Patent searching and closed industrial systems were outside scope.
- Several closest records are recent preprints or submissions and may change version or venue.
- One targeted citation cycle was closed; exhaustive forward citation chasing was not possible through the available endpoint.
- The underlying original report remained unavailable, so this audit tests the governed claims in the repository rather than undisclosed report language.
- These limitations preclude an exhaustive absence claim. They do not weaken the positive collisions that decide `STOP`.

## 11. Final gate

`STOP` the architecture route.

`STOP` the component-agnostic benchmark and physical-accounting fallback route.

Do not implement, train, or turn the known-component synthesis into an article rewrite.

Treat the direction-setting objective as a separate, unaudited pivot. Open it only under a new issue with its own contribution type, literature protocol, falsifiable theses, and anti-rewrite gate.
