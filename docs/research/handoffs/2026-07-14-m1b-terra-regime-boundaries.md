# M1b Terra Regime-Boundary Prior-Art Audit

Date: 2026-07-14

Role: Terra-Evidence with adversarial reducibility review

Target: Sol-PI, milestone `M1b - Managed-state transition thesis novelty gate`, issue [#5](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/5)

Search freeze: 2026-07-14

Status: `COMPLETE` for this bounded four-boundary audit

Boundary-route verdict: `STOP`

Novelty result: no `DISTINCT_CANDIDATE`

## 1. Objective

This handoff tests four ex ante, implementation-neutral regime boundaries requested by issue #5:

1. context-only processing versus governed persistent state;
2. useful versus harmful durable state;
3. fixed versus adaptive computation; and
4. Pareto-rank reversal under workload `Omega`, guarantee contract `G`, and resource envelope `B`, including the proposed interaction that state validity must be established before adaptive compute can have positive value.

For each boundary, the audit records pre-outcome variables, matching conditions, an expected rank, a negative regime, a decisive falsifier, two non-isomorphic instantiations, and a minimum discriminating design. Each candidate is then reduced immediately against its closest individual prior and the strongest adjacent composite.

The result is deliberately narrower than an M1b-wide decision. It establishes that these four intuitive regime claims cannot by themselves support a new direction-setting article. It does not prove that no narrower, presently unspecified technical law could ever survive.

## 2. Scope and exclusions

### 2.1 Included

The search covered primary and official records for:

- Adaptive Computation Time (ACT), Universal Transformer, PonderNet, recurrent and elastic depth, early exit, and token/layer routing;
- test-time compute scaling, verifier-guided search, and negative test-time scaling regimes;
- rational metareasoning and value of computation;
- long-context versus retrieval or external memory;
- stateful long-horizon agent-memory characterization, update robustness, stale-state failures, lifecycle cost, and state-trajectory governance;
- memory/compute substitution and non-substitution;
- classical working sets, online paging, amortization, and resource allocation; and
- 2026 position or survey records making an overlapping persistent-state governance argument, used only as contextual collision evidence unless they also report primary results.

The freeze includes arXiv records submitted through 2026-07-08 that were discoverable on 2026-07-14. A-TMA v2 is therefore included.

### 2.2 Excluded from decision-critical evidence

- Patents, non-public systems, marketing pages, blog summaries, and product documentation.
- Secondary summaries when a primary paper or official proceedings record resolved.
- `Learning to Forget Attention` (`arXiv:2602.12204v1`) as decision-critical evidence. It is an eligible adjacent preprint on a synthetic benchmark and directly couples consolidation to reduced attention, but the bounded decision does not depend on its unusually strong unreviewed claims.
- `Inverted Locality` (`OpenReview:t33i8z9IeU`) as decision-critical evidence. It is an anonymous 2026 workshop submission; its reported lack of temporal locality is retained only as a caution against importing recency assumptions.
- `Always-OnAgents` (`arXiv:2606.30306v1`) as primary empirical proof. It is a survey and pilot evaluation-contract proposal, but its lifecycle, governance, rollback, and persistent-state framing is a direct article-positioning collision.
- Architecture design, implementation, benchmark construction, experiments, and manuscript drafting.

### 2.3 Decision standard

`DISTINCT_CANDIDATE` requires a residual that changes an observable compliance decision, rank prediction, or falsifier after all names and implementation labels are erased. A formula assembled from measured cost curves, generic Pareto selection, value of computation, or known state-validity prerequisites does not qualify merely because it is written with new symbols.

No novelty inference is made from a search miss. `UNSUPPORTED` means that the proposed claim lacks sufficient primary support; it does not mean novel.

## 3. Hypotheses and questions

### 3.1 Shared operational vocabulary

The boundary tests use the following implementation-neutral terms.

- A **context-only system** receives a bounded episode-local input and has no writable state that survives the evaluated invocation. If a prompt builder stores, mutates, or materializes cross-session state, that builder belongs to the evaluated system and the system is not context-only.
- A **governed persistent-state system** carries state across invocations and exposes observable semantics for at least retrieval plus the applicable update, supersession, revocation, expiration, recovery, or audit obligations in `G`.
- A **fixed-compute policy** spends the same declared compute budget for every member of a matched input stratum.
- An **adaptive-compute policy** chooses among bounded compute actions from pre-outcome signals and pays all routing, scoring, verification, and synchronization overhead.
- A system is **adequate** only if it passes every semantic obligation in `G` and every separate resource ceiling in `B`. Quality is compared only among adequate systems. Resource axes are not collapsed unless issue #5 has declared the scalarization before outcomes.
- A **feasibility boundary** is a contract or hard-resource failure. An **efficiency boundary** is a Pareto-rank change among systems that remain feasible.

### 3.2 Questions

1. Can workload observables predict when replaying bounded context remains sufficient and when persistent state is required or Pareto-preferable?
2. Can reuse, mutation, staleness, and distractor observables predict when durable state helps or harms?
3. Can a cheap, frozen difficulty or marginal-value signal predict when adaptive compute beats a fixed budget after overhead?
4. Can one implementation-neutral rule predict a held-out rank reversal under `Omega`, `G`, and `B`, rather than merely recompute a Pareto frontier after observing outcomes?
5. Does the narrower interaction "validate state before allocating more compute" survive as a distinct LLM-specific result?

## 4. Inputs and source versions

### 4.1 Repository inputs

Repository snapshot inspected at commit `fe4e7ce351f7c40a1fcd1b1500f7361feef29d5d`:

- issue #5, updated `2026-07-14T20:30:31Z`;
- `docs/research/STATE.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/handoffs/README.md`;
- `docs/research/handoffs/2026-07-14-m1-luna-cross-review.md`;
- `docs/research/handoffs/2026-07-14-m1-luna-librarian.md`;
- `docs/research/handoffs/2026-07-14-m1-sol-reducibility.md`;
- `docs/research/handoffs/2026-07-14-m1-terra-empirical-route.md`; and
- `docs/research/handoffs/2026-07-14-m1-terra-systematic-search.md`.

M1 had already stopped the architecture, joint-controller, benchmark, and complete-accounting routes. It explicitly left the direction-setting thesis unaudited.

### 4.2 Decision-critical primary records

| Family | Primary record and version used | Precise locator used | What it establishes for this audit |
|---|---|---|---|
| Adaptive recurrence | Graves, *Adaptive Computation Time for Recurrent Neural Networks*, [arXiv:1603.08983v6](https://arxiv.org/abs/1603.08983v6) | Section 2, PDF pp. 2-5; sorting and Wikipedia results in Section 4; conclusion | Per-input recurrent halting, compute penalty, positive and no-gain task regimes |
| Recurrent depth | Dehghani et al., *Universal Transformers*, [arXiv:1807.03819v3](https://arxiv.org/abs/1807.03819v3), ICLR 2019 | Sections 2.1-2.2, adaptive per-position halting; experiments in Section 4 | Fixed versus dynamically halted recurrent depth was already an explicit design axis |
| Learned halting | Banino et al., *PonderNet: Learning to Ponder*, [arXiv:2107.05407v2](https://arxiv.org/abs/2107.05407v2) | Sections 2.1-2.5; Section 3 parity, bAbI and extrapolation experiments | Learned step distributions, accuracy/compute regularization, hard maximum, and adverse prior settings |
| Early exit | Schuster et al., *Confident Adaptive Language Modeling*, [NeurIPS 2022 paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/6fac9e316a4ae75ea244ddcef1982c71-Paper-Conference.pdf) | Abstract and pp. 1-2; Sections 3-4; Section 6 | Calibrated token-level exit under a sequence-level risk/consistency contract; confidence overhead can matter |
| Token routing | Raposo et al., *Mixture-of-Depths*, [arXiv:2404.02258v1](https://arxiv.org/abs/2404.02258v1) | Abstract; Sections 2-4 | Context-sensitive token compute allocation under a fixed aggregate FLOP budget |
| Test-time scaling | Snell et al., *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*, [arXiv:2408.03314v1](https://arxiv.org/abs/2408.03314v1), ICLR 2025 | Sections 3.1-3.2; Section 5.3 and Figure 3; conclusion | Strategy and benefit depend on difficulty and base model; search can over-optimize; hardest items can gain little |
| Elastic depth | Jeddi et al., *LoopFormer*, [arXiv:2602.11451v1](https://arxiv.org/abs/2602.11451v1), ICLR 2026 | Abstract; official paper Sections 3-5; compute-matched fixed-loop and early-exit comparisons | Budget-conditioned variable recurrent depth is already a current positive result |
| Negative depth scaling | Capps, *CART*, [arXiv:2606.01495v2](https://arxiv.org/abs/2606.01495v2) | Abstract; Sections 7.4 and 7.6; Section 9.3 | Variable recurrence at inference degrades on both sides of trained depth under this recipe; dense baseline wins |
| Memory/depth trade-off | Sapunov, *Universal Transformers Need Memory*, [arXiv:2604.21999v3](https://arxiv.org/abs/2604.21999v3) | Sections 4.2-4.4; Tables 4-5 | On one Sudoku architecture, memory tokens and ponder depth partly substitute, but total token-steps and accuracy do not form a universal fungibility law |
| Metareasoning | Russell and Wefald, *Principles of Metareasoning*, [Artificial Intelligence 49 (1991), 361-395](https://doi.org/10.1016/0004-3702(91)90015-C) | Abstract; pp. 361-395 | Computation is a costly action selected by its expected value |
| Learned metareasoning | Callaway et al., *Learning to Select Computations*, [arXiv:1711.06892v3](https://arxiv.org/abs/1711.06892v3), UAI 2018 | Abstract; terminate, allocation, and planning experiments | A domain-general approximation selects computations and accounts for metareasoning overhead |
| Dynamic value of computation | Sezener and Dayan, *Static and Dynamic Values of Computation in MCTS*, [PMLR 124:31-40](https://proceedings.mlr.press/v124/sezener20a.html) | Abstract; PDF Section 2.2; main result | Computation value is its expected effect on later action quality, including future computations |
| Working sets | Denning, *The Working Set Model for Program Behavior*, [CACM 11(5), 1968, pp. 323-333](https://denninginstitute.com/pjd/PUBS/WSModel_1968.pdf) | PDF pp. 323-326, especially Section 3; conclusion | Recent-use working set and joint processor/memory demand as an online allocation problem |
| Online caching | Sleator and Tarjan, *Amortized Efficiency of List Update and Paging Rules*, [CACM 28(2), 1985, pp. 202-208](https://www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf) | Abstract; Sections 1 and 4 | LRU and paging already formalize online state retention against an offline comparator and memory size |
| Long context/RAG | Li et al., *Retrieval Augmented Generation or Long-Context LLMs?*, [EMNLP Industry 2024](https://aclanthology.org/2024.emnlp-industry.66.pdf) | Section 3.3, PDF pp. 2-3; Section 4, pp. 3-4; Section 5.1, p. 4 | Sufficiently resourced long context wins average quality, RAG wins cost, and Self-Route makes query-level routing explicit |
| Harmful retrieval | Jin et al., *Long-Context LLMs Meet RAG*, [arXiv:2410.05983v1](https://arxiv.org/abs/2410.05983v1) | Abstract; Sections 3.1-3.3; Sections 4-5 | More retrieved state first helps and then harms because of hard negatives |
| RAG workload control | Li et al., *RAGPerf*, [arXiv:2603.10765v1](https://arxiv.org/abs/2603.10765v1) | Abstract; workload generator and reported metric set | Query/update ratios, query distributions, memory footprint, utilization, accuracy, and factual consistency are already benchmark controls |
| Stateful systems characterization | Omri et al., *Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads*, [arXiv:2606.06448v1](https://arxiv.org/abs/2606.06448v1) | Section 3.3; Sections 4.1-4.8; Figures 2-10; Table 3 | Construction/read/serve costs, query-volume amortization, freshness feasibility, growth, and workload-dependent frontiers are measured directly |
| Agent-native state | Zhou et al., *Are We Ready For An Agent-Native Memory System?*, [arXiv:2606.24775v1](https://arxiv.org/abs/2606.24775v1) | Section 4.1 and Figure 7; Section 4.3 and Table 2/Figure 9; Section 4.4 | No memory architecture dominates; raw context can win; update correctness and stale-state resolution depend on workload and organization |
| Governed state trajectory | Orogat and Mansour, *Is Agent Memory a Database?*, [arXiv:2605.26252v1](https://arxiv.org/abs/2605.26252v1) | Abstract; Sections 2.2-2.4; Section 3; Section 4.2; Section 5 | Persistent agent memory as governed state trajectory, with ingestion, revision, forgetting, retrieval, correctness conditions, and a research agenda |
| State-failure decomposition | Shi et al., *A-TMA*, [arXiv:2607.01935v2](https://arxiv.org/abs/2607.01935v2) | Abstract; Sections 3-4.6; Sections 5.2-5.3 | Old/current/transition facts can coexist and mislead; bank, retrieval, and answer failures must be separated; gains are host dependent |

### 4.3 Contextual and adjacent current records

| Record | Status in this audit | Reason |
|---|---|---|
| Oncescu et al., *The Recurrent Transformer*, [arXiv:2604.21215v1](https://arxiv.org/abs/2604.21215v1) | Adjacent primary | Recurrence trades effective depth, parameter width, KV footprint, and latency, but does not define the requested cross-family transition law |
| Shihab et al., *Learning to Forget Attention*, [arXiv:2602.12204v1](https://arxiv.org/abs/2602.12204v1) | Adjacent preprint, not decision-critical | Direct memory-consolidation/adaptive-compute collision on a synthetic benchmark; unusually strong claims remain unreviewed |
| Ding et al., *Always-OnAgents*, [arXiv:2606.30306v1](https://arxiv.org/abs/2606.30306v1) | Contextual survey/agenda collision | Defines always-on agents by durable state, a governance lifecycle, state obligations, and AOEP-v0; not used as primary proof |
| *Inverted Locality*, [OpenReview:t33i8z9IeU](https://openreview.net/forum?id=t33i8z9IeU) | Contextual anonymous workshop record | Its reported absence of temporal locality cautions against assuming LRU-like agent-memory behavior |

### 4.4 Version normalization

ArXiv base identifiers, HTML/PDF views, venue mirrors, and project pages were deduplicated into one work. The latest primary version inspected at the freeze is used. Material version chains relevant to conclusions were:

- ACT: current `v6`;
- Universal Transformer: current `v3`;
- PonderNet: `v1` to current `v2`;
- Callaway et al.: `v1` to current `v3`;
- Universal Transformers Need Memory: `v1` to current `v3`;
- CART: `v1` to current `v2`;
- A-TMA: `v1` to current `v2` on 2026-07-08;
- all other cited arXiv records above: `v1` at the freeze.

## 5. Work completed

### 5.1 Search method

The audit used four routes:

1. exact seed resolution for canonical adaptive-compute, metareasoning, caching, long-context/RAG, and stateful-agent papers;
2. targeted free-text searches for boundary terms and negative regimes;
3. backward snowballing from the closest 2026 records into their foundational mechanism families; and
4. one additional forward/exact-title iteration after new 2026 seeds were found.

The search endpoint exposed ranked records but not a stable corpus total. Every per-query count is therefore `NON DISPONIBLE`; no count is inferred from the visible result page.

### 5.2 Exact query journal

All queries below were executed on `2026-07-14`. Source: web search endpoint. Stable result count for every query: `NON DISPONIBLE`.

| # | Exact query |
|---:|---|
| 1 | `site:arxiv.org/abs adaptive computation time Graves 1603.08983` |
| 2 | `site:proceedings.neurips.cc PonderNet learning to ponder 2021` |
| 3 | `site:openreview.net Universal Transformer adaptive computation time per position` |
| 4 | `site:aclanthology.org early exiting adaptive language model CALM confident adaptive language modeling` |
| 5 | `PonderNet Learning to Ponder NeurIPS 2021 proceedings` |
| 6 | `Confident Adaptive Language Modeling CALM NeurIPS 2022 proceedings` |
| 7 | `Scaling LLM Test-Time Compute Optimally ICLR 2025 OpenReview` |
| 8 | `Mixture-of-Depths dynamically allocating compute transformer arXiv 2404.02258` |
| 9 | `"PonderNet: Learning to Ponder"` |
| 10 | `site:proceedings.neurips.cc/paper/2021 "PonderNet"` |
| 11 | `site:arxiv.org/abs "Universal Transformers Need Memory"` |
| 12 | `site:openreview.net "Universal Transformers Need Memory"` |
| 13 | `site:arxiv.org/abs value of computation metareasoning select computations Callaway 1711.06892` |
| 14 | `site:proceedings.mlr.press metareasoning value of computation selection computations` |
| 15 | `site:aaai.org "Learning to Select Computations"` |
| 16 | `site:sciencedirect.com "Principles of Metareasoning" Russell Wefald` |
| 17 | `working set model program behavior Denning 1968 ACM PDF` |
| 18 | `Belady study replacement algorithms virtual storage computer 1966 IBM PDF` |
| 19 | `Sleator Tarjan amortized efficiency list update paging rules 1985 ACM` |
| 20 | `online caching admission reuse cost benefit threshold primary paper` |
| 21 | `site:arxiv.org/abs/2606.06448 "Agent Memory" characterization stateful long-horizon workloads` |
| 22 | `site:arxiv.org/abs/2606.24775 "Agent-Native Memory System"` |
| 23 | `site:arxiv.org/abs/2603.10765 RAGPerf query update ratio latency memory I/O` |
| 24 | `site:openreview.net "Inverted Locality" agent memory` |
| 25 | `site:aclanthology.org retrieval augmented generation or long-context LLMs comprehensive study hybrid approach 2024` |
| 26 | `site:arxiv.org/abs long context vs RAG cost quality retrieval augmented generation` |
| 27 | `site:openreview.net long context RAG comparison cost performance` |
| 28 | `site:aclanthology.org long context external memory agent comparison` |
| 29 | `site:arxiv.org/abs/1807.03819 Universal Transformers` |
| 30 | `site:arxiv.org/abs 2026 agent memory lifecycle governance workload query update cost long context persistent state` |
| 31 | `site:arxiv.org/abs 2026 adaptive test-time compute routing difficulty verifier overhead early exit language model` |
| 32 | `site:arxiv.org/abs 2026 memory compute tradeoff recurrent transformer adaptive depth persistent state` |
| 33 | `site:openreview.net 2026 agent memory cache working set staleness update workload` |
| 34 | `"Governed Evolving Memory" agent memory` |
| 35 | `"state trajectory" "agent memory" persistent LLM` |
| 36 | `"The Recurrent Transformer" adaptive depth memory compute` |
| 37 | `"adaptive compute" stateful LLM memory workload persistent` |
| 38 | `"A-TMA" "ghost memory" state-aware memory failures` |
| 39 | `"LoopFormer" adaptive compute fixed depth negative regime` |
| 40 | `"Always-OnAgents" persistent state governance evaluation contract` |
| 41 | `"CART" "Variable-R inference" recurrent transformer` |

### 5.3 Direct primary resolutions

The following canonical identifiers were opened directly after search discovery or backward snowballing:

`1603.08983`, `1807.03819`, `2107.05407`, `2404.02258`, `2408.03314`, `1711.06892`, `2410.05983`, `2602.11451`, `2602.12204`, `2603.10765`, `2604.21215`, `2604.21999`, `2605.26252`, `2606.01495`, `2606.06448`, `2606.24775`, `2606.30306`, `2607.01935`.

Official proceedings records were resolved for CALM, Li et al. 2024, Russell and Wefald 1991, Sezener and Dayan 2020, Denning 1968, and Sleator and Tarjan 1985.

### 5.4 Snowball paths

1. **Adaptive-depth path:** `Universal Transformers Need Memory` -> its ACT/Universal Transformer/PonderNet antecedents -> CALM and Mixture-of-Depths -> Snell test-time scaling -> 2026 LoopFormer/CART. This path closed on the already known families of recurrent halting, early exit/routing, and test-time search. The final exact-title iteration returned LoopFormer and CART again, plus same-family recurrent-depth records, not a new boundary theory.
2. **Metareasoning path:** Russell and Wefald -> Callaway et al. -> Sezener and Dayan -> targeted comparison with Snell. The direct historical edge is verified within the metareasoning papers. The Snell comparison is a conceptual forward snowball, not a claimed citation edge.
3. **Memory-allocation path:** Denning working sets -> Sleator/Tarjan online paging -> modern query/update, staleness, and locality searches -> RAGPerf and Agent Memory. Classical caching does not by itself model semantic revision, but it already supplies reuse, footprint, online retention, and amortization abstractions.
4. **Context-to-managed-state path:** Li et al. long-context/RAG and Self-Route -> Jin et al. hard negatives -> Agent Memory and Agent-Native Memory -> GEM -> A-TMA and Always-OnAgents. This path moves from cost/quality routing to lifecycle, state-trajectory correctness, and stale-state failure without leaving an unclaimed general transition thesis.
5. **Closure iteration:** exact searches for GEM, state trajectory, Recurrent Transformer, adaptive compute plus state, then A-TMA, LoopFormer, Always-OnAgents, and CART. It surfaced A-TMA as a new July record and CART/LoopFormer as current depth evidence. A final iteration returned those same records and same-family fixed-point/recurrent papers. No new eligible mechanism or framework family appeared.

### 5.5 Search limitations

- Stable database corpus sizes and forward-citation counts were `NON DISPONIBLE`.
- This is a reproducible targeted review, not an exhaustive systematic-review census.
- Full patent and commercial-system searches were outside scope.
- Some 2026 records are preprints. Their venue status is not upgraded in this handoff.
- The closure claim is family-level saturation for these four boundaries, not universal literature exhaustion.

## 6. Evidence, boundary register, and reductions

### 6.1 Summary classification

| ID | Candidate boundary at the claimed grain | Classification | Result |
|---|---|---|---|
| RB-1 | Context-only versus governed persistent state | `ANTICIPATED` | Semantic persistence is definitional under a durable-state contract; lifecycle crossover is already an amortization/freshness frontier |
| RB-2 | Durable state useful versus harmful | `ANTICIPATED` | Reuse benefits, stale-state harm, hard negatives, destructive consolidation, and workload-dependent reversals are already reported |
| RB-3 | Fixed versus adaptive computation | `ANTICIPATED` | ACT, PonderNet, Universal Transformer, CALM, metareasoning, test-time scaling, LoopFormer, and negative results cover the direction and counter-regimes |
| RB-4 | Pareto reversal under `Omega/G/B`, including validity-before-compute | `UNSUPPORTED` as a predictive universal rule; generic shell `ANTICIPATED` | A held-out cross-family law is not established; the shell reduces to constrained Pareto selection plus value of computation and state-validity gating |

There is no `DISTINCT_CANDIDATE`. The absence of a supported universal rule in RB-4 is not evidence of novelty.

### 6.2 RB-1: context-only versus governed persistent state

#### Claim unit

Predict whether a context-only system remains adequate or whether governed persistent state is semantically required or lifecycle-Pareto-preferable.

#### Pre-outcome variables

- `H_req`: maximum history/evidence span required by the task distribution, measured from generated or labeled dependency traces before system outcomes;
- `W_ctx`: usable input window after instruction/output reserve;
- `Q`: expected query count against one stable history snapshot;
- `U`: update or ingestion operations per snapshot or per unit time;
- `A`: inter-session arrival interval;
- `R_x`: required cross-session retention horizon;
- contract bits for update, supersession, revocation, expiration, rollback, provenance, and audit;
- predicted input token volume and analytic or calibration-only costs `C_full(H)`, `C_build(H)`, `C_update`, and `C_read`; and
- separate ceilings for latency, throughput, HBM, bytes moved, storage, reads/writes, energy, and maintenance work.

No accuracy result from the held-out comparison may be used to assign the regime.

#### Boundary statement and expected rank

**Feasibility:** if `G` requires state to survive an invocation and the required state is not re-supplied as input, a context-only system fails by definition. If another component reconstructs the stateful prompt, that component is persistent state and must be included in the system boundary. This is a scope fact, not an LLM discovery.

**Efficiency:** when both classes satisfy `G`, persistent state is predicted to reduce a particular lifecycle resource component only when, for that same component,

`Q * [C_full(H) - C_read] > C_build(H) + U * C_update`.

The expression must be applied axis by axis. It cannot license a claim of overall superiority by adding unlike units. For strict cross-session freshness, an additional feasibility condition is

`C_update + C_retrieve <= A`.

Expected rank:

- high `Q`, stable histories, and repeated queries: governed external state should beat full-history replay on query latency and bytes processed, conditional on contract-equivalent quality;
- low `Q`, continuous ingestion, or short trace-sensitive histories that fit `W_ctx`: context replay should beat construction-heavy state on lifecycle work and may beat it on quality.

#### Matching regime

- Same generator checkpoint, tokenizer, decoding, output budget, source history, query stream, and quality metric.
- Same semantic information is available at the source boundary. Retrieval misses count against the stateful system; omitted long-context evidence counts against context-only.
- Construction, maintenance, retrieval, prompt processing, and generation are all metered.
- Quality must meet the same `G` floor before resource dominance is asserted.
- Hardware-specific thresholds are fitted only on a calibration split and frozen before held-out evaluation.

#### Negative regimes and counterexamples

1. One query over a short, immutable, exact-order trace that fits in context. Long context can preserve details that extraction or retrieval drops.
2. Continuous updates with sparse queries. Agent Memory Recommendation 6 explicitly predicts that low-construction systems are favored.
3. An arrival interval shorter than construction plus retrieval. Persistent state cannot satisfy both freshness and latency even if its batch QA accuracy is higher.
4. A context-only run backed by an undeclared persistent prompt builder. This is a boundary-definition failure, not evidence that context alone satisfied durability.

#### Decisive falsifier

Reject the proposed crossover if the frozen inequalities fail to predict the held-out rank direction in either non-isomorphic family, if the predicted high-`Q` and low-`Q` orderings do not reverse, or if the threshold moves materially after observing held-out quality. A managed-state aggregate win does not rescue a failed boundary prediction.

#### Two non-isomorphic instantiations

1. **Conversational evidence:** replay the full raw multi-session transcript versus query a versioned external memory.
2. **Procedural state:** reconstruct a workflow/database state from an event log in the prompt versus query a durable materialized state with version and rollback semantics.

The second is not conversational retrieval: correctness depends on state transitions and operation order.

#### Minimum decisive design

- Two task families above.
- Cross `Q in {1, 8, 64}` with update load `U in {0, moderate, arrival-bound}` and two history spans, one below and one above the efficient-context region.
- At least two context realizations and two persistent-state realizations that do not share a retrieval/index implementation.
- Paired queries, a calibration/confirmation split, at least 200 independent histories per boundary cell, and at least three seeds for stochastic pipelines; replace the floor with a larger simulation-based power result if required.
- Repeat the confirmation cells on two accelerator/serving stacks and report lifecycle calls, tokens, FLOPs, wall time, P50/P99 latency, HBM/host bytes, storage, reads/writes, and energy separately.
- Provisional run floor: `2 families * 3 Q levels * 3 U levels * 2 history spans * 4 implementations * 200 histories`, before seeds and hardware replication. A final device-hour estimate requires the frozen model and serving stack.

#### Immediate prior-art reduction

- Closest individual system result: Agent Memory Sections 4.5-4.6 already reports the construction/serve/accuracy frontier, says high-volume stable histories favor moving work into construction, says continuous ingestion with sparse queries favors low construction cost, and defines construction plus retrieval against the arrival interval as a hard freshness constraint.
- Closest context comparison: Li et al. already finds sufficiently resourced long context stronger on average quality, RAG cheaper, and routes between them per query.
- Closest governed-state framing: GEM already defines persistent agent memory as a governed state trajectory with explicit evolution operators and correctness conditions.
- Classical reduction: the crossover is amortization plus online working-set allocation once semantic contract feasibility is separated.

Classification: `ANTICIPATED`. A cross-family quantitative coefficient set remains `UNSUPPORTED`, not distinct.

### 6.3 RB-2: durable state useful versus harmful

#### Claim unit

Predict the sign of durable-state contribution rather than assuming persistence is always beneficial.

#### Pre-outcome variables

- `R_valid`: expected future valid reuses per write;
- `mu`: mutation/supersession/revocation probability per state item;
- `tau`: invalidation or maintenance delay divided by the relevant arrival interval;
- `eta`: hard-negative or distractor fraction in the candidate evidence set;
- dependency density and temporal-order sensitivity;
- retrieval recall/precision estimated on a disjoint calibration corpus;
- allowed forgetting, archive recovery, provenance, and current-versus-historical query mix; and
- footprint and update-work ceilings.

A preregistered empirical boundary can use

`DeltaQ = beta_0 + beta_R * log(1 + R_valid) - beta_S * (mu * tau) - beta_N * eta`,

with expected `beta_R > 0`, `beta_S > 0`, and `beta_N > 0`. Coefficients are fitted on calibration workloads and frozen. The held-out scientific claim is the signs and rank reversal, not the fitted notation.

#### Expected rank

- High valid reuse, low churn, low invalidation delay, and high evidence precision: versioned durable state should beat stateless reconstruction on quality at a matched serving budget and on serving cost at a matched quality floor.
- Low reuse, high churn/staleness, high hard-negative density, or exact trace/order dependence: raw context or a lossless event log should beat compressed, append-only, or semantically consolidated durable state.

#### Matching regime

- Same generator, source event stream, answer prompt budget, output policy, and target queries.
- Equal source information, but each pipeline is responsible for preservation, retrieval, and current/historical resolution.
- Separate bank correctness, retrieval support, and answer resolution, following A-TMA, so a lucky final answer cannot hide a corrupted store.
- Match footprint or report the full footprint frontier; do not call a larger store a free quality improvement.
- Freeze update policies and thresholds before confirmation.

#### Negative regimes and counterexamples

1. No future reuse: durable derived state adds write/maintenance cost without benefit.
2. Rapidly superseded user facts: append-only or stale retrieval mixes old and current values and can cause "ghost memory."
3. More retrieved passages: Jin et al. reports an initial quality increase followed by decline as hard negatives accumulate.
4. Semantic consolidation of a procedural trace: summary facts can destroy operation order required by DB/workflow tasks; Agent-Native Memory reports trace-preserving approaches and even raw long context winning such workloads.
5. Unbounded accumulation: Agent Memory finds monotonic footprint growth by default and super-linear construction-token growth in agentic stores.

#### Decisive falsifier

Reject the boundary if the preregistered reuse/staleness/noise interactions have the wrong sign, if no held-out rank reversal occurs between high-valid-reuse and high-staleness regimes in both task families, or if a lossless raw-state control dominates across all tested cells. A single managed system winning the macro-average is not a falsifier of the negative regime; failure must be cell-specific and predeclared.

#### Two non-isomorphic instantiations

1. **Mutable personal facts:** append-only embedding memory versus a versioned or relation-aware store that distinguishes current, historical, and transition state.
2. **Procedural execution:** compressed fact memory versus an immutable, ordered event ledger with materialized current state and replay.

#### Minimum decisive design

- Two task families above.
- A `2 x 2 x 2` factorial over valid reuse, churn/staleness, and hard-negative rate, plus intermediate calibration cells to locate the sign change.
- Four state policies: no durable derived state/raw replay, append-only retrieval, lossy consolidation, and versioned/revisable state.
- At least 200 paired sequences per extreme cell, three stochastic seeds, and blinded labels for current, historical, and transition truth.
- Report bank-state accuracy, evidence support, current/historical answer accuracy, footprint, write amplification, update latency, query latency, and energy separately.
- Provisional confirmation floor: `2 families * 8 extreme cells * 4 policies * 200 sequences`, before seeds. Calibration cells and power analysis are additional.

#### Immediate prior-art reduction

- Agent-Native Memory Sections 4.1 and 4.3 already show workload-dependent leaders, raw long-context wins on trace-preserving tasks, and stale/flat accumulation weakness under updates.
- A-TMA v2 explicitly separates bank, retrieval, and QA failures caused by old/current/transition state mixing and reports host-dependent gains.
- Jin et al. provides the hard-negative non-monotonicity.
- GEM makes revision, forgetting, and state-modifying retrieval explicit because append-only and CRUD-like abstractions fail the desired trajectory conditions.
- Denning and online caching already make reuse and retention policy central, while Agent Memory adds lifecycle and semantic-state measurements.

Classification: `ANTICIPATED`. The exact cross-family response surface is `UNSUPPORTED`; inventing coefficients would not create novelty.

### 6.4 RB-3: fixed versus adaptive computation

#### Claim unit

Predict when bounded adaptive compute should beat a fixed compute allocation after all controller and verifier overhead.

#### Pre-outcome variables

- a cheap difficulty or marginal-value signal `z(x)` trained only on disjoint calibration data;
- dispersion of predicted marginal value across inputs;
- calibration error and distribution-shift diagnostics for `z`;
- router, confidence, verifier, synchronization, and search overhead;
- base-model first-pass success probability estimated on calibration, not by sampling the held-out answer;
- maximum compute, average compute, P99 latency, and deadline ceilings; and
- failure severity under early exit or extra search.

The metareasoning form is:

`allocate one more computation iff E[loss_now - loss_after | z(x)] > lambda * DeltaCost + C_control`.

This is a testable policy statement, but it is also the standard value-of-computation reduction.

#### Expected rank

- High input-difficulty dispersion, a calibrated pre-outcome signal, positive marginal gains, and low control overhead: adaptive compute should dominate fixed compute at matched average cost.
- Homogeneous inputs, unreliable difficulty prediction, high routing/verifier overhead, strict tail latency, easy inputs susceptible to over-optimization, or extremely hard inputs outside the base model's capability: fixed compute should dominate or the rule should abstain.

#### Matching regime

- Same base checkpoint and task data.
- Same maximum and matched mean compute, plus an additional hard-budget comparison.
- Include controller/verifier computation and wall-clock effects.
- Fixed baselines at every budget used by the adaptive policy, not one weak fixed baseline.
- Difficulty bins and thresholds frozen before held-out answers.
- Report both quality and the complete resource vector, including tail latency.

#### Negative regimes and counterexamples

1. ACT's Wikipedia experiment did not obtain the same benefit seen on algorithmic tasks; extra compute was not universally useful.
2. PonderNet performance depends on the halting prior and hard maximum; an adverse prior can collapse the intended behavior.
3. CALM shows confidence measures differ in overhead; a softmax score can reduce layers while failing to reduce total FLOPs.
4. Snell et al. reports beam-search over-optimization on easy problems, diminishing returns at high budgets, lookahead underperformance from overhead, and little progress on the hardest problems.
5. CART reports that inference at recurrence counts above or below the trained value degrades under its recipe.

#### Decisive falsifier

Reject the boundary if, after matched average compute and full overhead, adaptive allocation does not improve the held-out Pareto frontier; if the frozen marginal-value signal fails to rank gains above chance; if the predicted difficulty interaction does not replicate across both instantiations; or if fixed allocation wins in the preregistered high-dispersion/low-overhead regime.

#### Two non-isomorphic instantiations

1. **Latent recurrent computation:** fixed recurrent depth versus ACT/PonderNet-style halting or budget-conditioned elastic depth.
2. **Black-box test-time search:** fixed sample/search budget versus prompt-conditioned allocation among revision, parallel sampling, and verifier-guided search.

Token/layer early exit is a third eligible family, not required for the two-family minimum.

#### Minimum decisive design

- Two implementation families above.
- Four difficulty strata defined by a frozen cheap predictor, three compute budgets, fixed and adaptive allocation, and both matched-average and hard-ceiling comparisons.
- At least 500 paired items per stratum for deterministic comparisons and five seeds for sampling/search policies, subject to a larger power-analysis result.
- Train/calibrate on one task subset; confirm on a disjoint task family and a shifted difficulty mix.
- Meter generated tokens, model FLOPs, verifier/router FLOPs, wall time, P50/P99 latency, HBM traffic, and energy.
- Provisional floor per family: `4 strata * 3 budgets * 2 policies * 500 items`, before stochastic seeds and shift replication.

#### Immediate prior-art reduction

- Russell/Wefald, Callaway, and Sezener/Dayan already define the expected benefit of an additional computation net of its cost.
- ACT, Universal Transformer, PonderNet, CALM, Mixture-of-Depths, and LoopFormer instantiate recurrence, early exit, token routing, and elastic depth.
- Snell et al. explicitly conditions the compute-optimal strategy on task difficulty and base model, while documenting no-gain and negative regimes.
- CART supplies a current fixed-depth-favored counterexample.

Classification: `ANTICIPATED`. No LLM-specific residual remains after value-of-computation substitution.

### 6.5 RB-4: Pareto reversal under `Omega`, `G`, and `B`, including validity-before-compute

#### Claim unit

Predict, before outcomes, which implementation class becomes feasible or changes Pareto rank as workload, guarantee, or resource constraints cross a boundary, and abstain when observables do not identify the ordering.

#### Pre-outcome variables

- the RB-1 workload variables (`H_req`, `Q`, `U`, `A`, retention and contract bits);
- the RB-2 variables (`R_valid`, `mu`, `tau`, `eta`, dependency/order sensitivity);
- the RB-3 variables (difficulty dispersion, marginal-value calibration, control overhead);
- each explicit guarantee in `G`, including current/historical validity, provenance, revocation, recovery, and bounded failure; and
- each separate ceiling and declared priority in `B`.

For two systems `a` and `b`, a rank reversal is meaningful only if both remain feasible and neither dominates on all declared axes. A scalar boundary such as

`w . [C_a(Omega) - C_b(Omega)] + lambda * [L_a(Omega) - L_b(Omega)] = 0`

is admissible only when `w`, `lambda`, response estimators, and abstention intervals are frozen before confirmation. Choosing weights or fitting response surfaces after outcomes makes the claim tautological.

#### Expected rank and abstention

- In the memory instantiation, high query reuse over stable histories should move rank toward constructed persistent state; sparse queries over continuously updated histories should move it toward replay or low-construction state.
- In the compute instantiation, heterogeneous inputs with reliable marginal-value estimates should move rank toward adaptive compute; homogeneous or miscalibrated regimes should move it toward fixed compute.
- If confidence intervals overlap the reversal surface, if systems are incomparable on non-scalarized axes, or if the validity of the input state is not identifiable, `T` must abstain.

#### The validity-before-compute interaction

Proposed residual:

> Extra adaptive computation should have positive value only after the evidence/state supplied to that computation is valid for the requested temporal view; when state is missing, stale, revoked, or mixed, more compute should not be expected to restore contract correctness and may amplify the wrong state.

This is falsifiable as an interaction, but it is not distinct at the claimed grain:

1. A-TMA already decomposes bank, retrieval, and answer-time failures and shows that relevant-looking old/current/transition evidence can still produce state-wrong answers.
2. Agent-Native Memory Section 4.3 reports that stronger answer backbones change absolute quality more than memory-pipeline ordering and argues that model scaling is useful after grounding succeeds, not as the primary remedy for stale or conflicting memory.
3. Metareasoning defines computation value conditional on the agent's current information state. If the action-relevant state is absent or invalid, the value of more inference over that state is low or negative unless the computation action can acquire or repair evidence.
4. Snell et al. shows extra search can over-optimize a verifier or yield little benefit. That supplies a compute-side negative regime.

Therefore the serial prerequisite is a strongest-composite consequence of state adequacy plus conditional value of computation. A quantitative cross-family interaction coefficient is `UNSUPPORTED`; it is not a `DISTINCT_CANDIDATE`.

#### Matching regime

- Freeze `Omega`, `G`, `B`, scalarization priorities if any, and abstention intervals.
- Separate state repair/acquisition actions from answer-only computation. If adaptive compute may retrieve or repair state, meter and label that action rather than crediting pure reasoning.
- Use the same base models and source event streams across policies.
- Fit response surfaces on calibration workloads and predict new tasks, implementations, and hardware without refitting.
- Evaluate contract feasibility before quality/cost rank.

#### Negative regimes and counterexamples

1. One system dominates on every declared axis: no reversal exists.
2. The systems are incomparable and no scalarization was declared: the correct output is abstention, not a winner.
3. A stale-state cell where extra compute includes an undeclared retrieval/repair call: the apparent interaction is confounded.
4. An invalid-state cell where the answer happens to be guessed from parametric knowledge: final accuracy hides a contract failure.
5. A response surface fitted on the confirmation outcomes: any observed reversal can be restated after the fact and has no predictive content.

#### Decisive falsifier

Reject `T` if a rule frozen on calibration data fails to predict the sign of held-out pairwise rank in either orthogonal instantiation, if its abstention intervals are miscalibrated, if rank changes under harmless relabeling of implementations, or if the validity-by-compute interaction disappears when state repair is separated from answer-only compute.

For the interaction specifically, preregister a `state validity x compute policy` term. Reject it if additional answer-only compute improves contract-valid current/historical resolution equally in valid and invalid-state cells, or if the predicted negative/zero marginal value under invalid state does not reproduce in both task families.

#### Two non-isomorphic instantiations

1. **Memory-system selection:** raw context, low-construction retrieval, and governed versioned state under varying query/update/freshness contracts.
2. **Compute-policy selection:** fixed versus adaptive latent recurrence or test-time search under varying difficulty and latency envelopes.

For the validity interaction, use mutable conversational facts and procedural/event-ledger state as the two non-isomorphic task families.

#### Minimum decisive design

- Reuse only frozen calibration models from RB-1 to RB-3; do not rerun until `T` and abstention are executable.
- At least 24 held-out `Omega/G/B` cells spanning both sides of each proposed surface, with at least eight cells reserved for the validity-by-compute interaction.
- Train the rule on one task/hardware pairing and confirm on a different task family and serving stack.
- For validity-before-compute, cross valid/current evidence, stale/mixed evidence, and missing evidence with fixed-low, fixed-high, and adaptive answer-only compute. Add a separately labeled repair-plus-compute arm.
- Use paired items, at least 200 items per interaction cell, three seeds for deterministic routing, and five for sampling/search.
- Primary outcomes: contract-valid answer rate, rank-prediction accuracy, abstention coverage/error, and the full non-collapsed resource vector.
- A rule that merely recomputes measured Pareto fronts on the same cells fails before testing.

#### Immediate prior-art reduction

- Agent Memory already measures and recommends workload-dependent construction/serve/accuracy selection and hard freshness feasibility.
- Agent-Native Memory already observes workload-dependent leaders and no universal memory architecture.
- Generic Pareto and constrained selection supplies the decision shell.
- Metareasoning supplies compute allocation conditional on information state and cost.
- A-TMA and Agent-Native Memory supply the validity prerequisite and the failure of stronger answer computation to repair upstream state coordination reliably.

Classification: predictive universal `T` is `UNSUPPORTED`; its existence or generic form is `ANTICIPATED`. The validity-before-compute interaction is `ANTICIPATED` directionally and `UNSUPPORTED` as a transportable quantitative law. Neither is distinct.

### 6.6 Strongest-composite and anti-rewrite result

The strongest composite reconstructs the entire proposal without new vocabulary:

1. GEM and Always-OnAgents provide state-trajectory governance and lifecycle contracts.
2. Agent Memory provides query/update amortization, construction/serve/accuracy frontiers, freshness constraints, and resource accounting.
3. Agent-Native Memory, A-TMA, and Jin et al. provide workload reversals, stale-state failure, and harmful retrieval regimes.
4. Li et al. provides long-context/RAG routing and a no-shift context regime.
5. Denning and Sleator/Tarjan provide working-set, online-retention, and amortization abstractions.
6. Russell/Wefald, Callaway, ACT, PonderNet, Universal Transformer, CALM, Snell, LoopFormer, and CART provide value-of-computation, adaptive allocation, and negative compute regimes.
7. Generic constrained multiobjective selection maps feasibility plus declared resource priorities to a Pareto set or abstention.

| Anti-rewrite test | Outcome |
|---|---|
| Component erasure | The four predictions remain executable, but reduce to known contract, amortization, state-validity, and value-of-computation statements |
| Label substitution | Replacing "managed state" with governed evolving memory/materialized state and "adaptive compute" with value-of-computation control changes no decision or falsifier |
| Strongest-composite reduction | Complete reconstruction succeeds |
| Generic-theory reduction | RB-1 reduces to feasibility plus amortization; RB-3 to value of computation; RB-4 to constrained Pareto selection |
| Ex ante boundary | Candidate observables can be preregistered, but universal response coefficients are not supplied by theory and cannot be invented post hoc |
| Rank order | Four rank predictions can be written, but their directions are already anticipated |
| Negative regime | Multiple explicit losing regimes exist for persistent state and adaptive compute |
| Orthogonal instantiation | Each prediction can be run in at least two non-isomorphic families |
| Independent falsifier | Each prediction can fail even if a favored managed-state system wins a macro-average |
| Agenda derivation | A validation agenda can be derived, but no unresolved distinct technical object remains to authorize it as a novel article route |

Testability is not novelty. Passing falsifiability checks does not repair the failed reduction tests.

## 7. Uncertainties and contradictions

1. Agent Memory and Agent-Native Memory are June 2026 preprints. They are highly decision-relevant and current but have not been upgraded to peer-reviewed status here.
2. A-TMA v2 is a July 2026 preprint. Its host-dependent gains and level decomposition are used as bounded evidence, not a universal result.
3. Universal Transformers Need Memory is a single-author preprint on a single-block Sudoku system. It demonstrates a local depth/state trade-off, not general fungibility.
4. CART is a single-author preprint at modest scale. Its negative result is a counterexample to universality, not proof that fixed depth generally wins.
5. Li et al. 2024 and Agent-Native Memory report cases where raw long context is stronger; Agent Memory reports large serving advantages for external memory. These findings are compatible once construction, query volume, task type, and lifecycle are separated.
6. Snell et al.'s oracle difficulty estimate uses many samples; its deployable verifier proxy is closer to ex ante operation but still has cost. The proposed M1b rule must not import an outcome-adjacent oracle as a free workload descriptor.
7. Classical temporal locality cannot be assumed for agent memory. The anonymous `Inverted Locality` record raises this concern, but the decision does not rely on it.
8. No independent librarian or adversarial reviewer has validated this exact handoff. This bounded subtask cannot claim the M1b-wide independent-review acceptance criteria.

## 8. Files modified

Created only:

- `docs/research/handoffs/2026-07-14-m1b-terra-regime-boundaries.md`

No source code, ledger, state file, issue, commit, branch, pull request, or external system was modified by this task.

## 9. Verification

### 9.1 Content checks

- Four and only four boundary candidates are registered.
- Every candidate contains pre-outcome variables, a matching regime, expected rank, negative regime, decisive falsifier, two non-isomorphic instantiations, and a minimum design.
- Feasibility and efficiency are separated.
- Context-only and fixed-compute winning regimes are explicit.
- Durable-state harm, adaptive-compute harm, abstention, and a favored-system contract failure are explicit.
- The stale/invalid-state by adaptive-compute interaction is explicitly classified and reduced.
- Every decision-critical source has a primary URL, frozen version or proceedings identity, and a section/page/figure/table locator.
- Exact queries, date, unavailable stable counts, direct resolutions, and snowball paths are retained.
- No novelty conclusion relies on absence.

### 9.2 Repository checks

- Target existence and size check: passed, 668 lines before this verification-note update.
- Required-field scan: passed for all four `Minimum decisive design` sections and for the shared pre-outcome, matching, rank, negative-regime, falsifier, and orthogonal-instantiation fields.
- `git diff --no-index --check -- NUL docs/research/handoffs/2026-07-14-m1b-terra-regime-boundaries.md`: no whitespace-error output; exit `1` is the expected no-index difference status for a new file.
- `git status --short`: this handoff is untracked as intended. Concurrent unrelated worktree paths were present and were not touched by this task.
- Commit, push, pull request, and issue mutation: not performed.
- SHA-256: computed after the final content check and reported externally to Sol-PI, because embedding a file's own digest would change the digest.

## 10. Recommended decision

Verdict: `STOP` for the four-boundary direction-setting article route.

Reasons:

1. RB-1 is already the combination of semantic scope, lifecycle amortization, and a measured freshness constraint.
2. RB-2's positive and harmful regimes are already reported in current stateful-memory, update, and retrieval work.
3. RB-3 is a direct instance of value-of-computation control with many LLM implementations and documented negative regimes.
4. RB-4 has no validated ex ante cross-family response law. Its generic shell is anticipated, while its coefficients and transportability are unsupported.
5. The validity-before-compute interaction is scientifically worth controlling for, but it is anticipated by upstream-state adequacy plus conditional value of computation. A-TMA and Agent-Native Memory make the state-side prerequisite explicit; metareasoning and Snell cover the compute side.
6. The strongest composite reconstructs the full proposal. No observable decision, ordering, or falsifier remains uniquely changed by the new `Omega/G/B/T` notation.

This is not a recommendation to publish a weaker manifesto, survey, roadmap, or narrative review from the same materials. Issue #5 defines those conversions as `STOP` conditions.

## 11. Next action

Sol-PI should integrate this route-specific `STOP` with the other M1b handoffs and independent reviews. Do not open a validation or manuscript milestone from these four candidates.

If M1b is not stopped globally, the only legitimate next search target is one newly specified, narrow technical law that:

1. freezes measurable coefficients before held-out outcomes;
2. predicts across both memory and compute implementation families;
3. changes a compliance or rank decision beyond generic Pareto/VOC selection; and
4. survives direct comparison with GEM, Agent Memory, Agent-Native Memory, A-TMA, and Always-OnAgents.

No such residual is defined in this handoff, so this condition does not justify `PIVOT`.

## 12. Authoring and reviewing roles

- Authoring role: Terra-Evidence, primary-source retrieval, version/locator verification, boundary design, and falsifier construction.
- Adversarial role performed in the same bounded task: immediate individual, strongest-composite, label-substitution, and generic-theory reduction.
- Independent bibliographic reviewer: not assigned within this task.
- Independent adversarial reviewer: not assigned within this task.
- Decision owner: Sol-PI for issue #5 and milestone M1b.

Final handoff verdict: `STOP`.
