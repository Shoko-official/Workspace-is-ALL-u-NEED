# Terra-Evidence Handoff: Initial Novelty Audit of the Budgeted Workspace Model

Date: `2026-07-14`

Role: `Terra-Evidence`

Target: `Sol-PI`, milestone `M0`, issue [#1](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/1)

Decision status: `PIVOT`, with a default `STOP` for the current broad architecture claim

## Objective

Test whether prior work already discloses or empirically establishes the candidate's joint allocation mechanism: a bounded active-attention workspace, mutable episodic memory, fixed-size compressed state, recurrent compute, verification, and halting controlled under explicit resource ceilings.

This is a bounded initial novelty audit. It is evidence for narrowing or stopping claims, not a systematic-review completion certificate and not a positive novelty opinion.

## Scope and exclusions

Included:

- primary papers, official proceedings records, and official technical specifications available through `2026-07-14`;
- mechanisms that anticipate at least one candidate property, especially joint memory/compute routing, adaptive depth, explicit memory mutation, state/attention hybrids, provenance, rollback, or physical cost accounting;
- the seed families named in `CHARTER.md` and `NOVELTY.md`, plus recent direct threats discovered during the audit.

Excluded:

- surveys, commentary, vendor summaries, benchmark leaderboards without an attributable method, and secondary citation pages;
- work that uses memory only as a metaphor;
- implementation-code auditing, patent searching, and a complete forward/backward citation closure;
- a claim that no unobserved prior work exists. Recent 2026 records have too little citation history for that inference.

The governing anti-assembly criterion is strict: the paper must not be a rewrite or packaging of known components. A surviving delta must either produce a causally discriminating mechanism effect against the strongest composite baseline or constitute a genuinely new, independently useful experimental/benchmark contribution. If neither survives, the recommendation becomes `STOP`.

## Search execution

Access date for every record below: `2026-07-14`.

The protocol query families in `NOVELTY.md` were used as the coverage checklist. The following are the exact web query strings or direct primary-record resolutions actually used in this bounded pass:

1. `site:proceedings.mlr.press Shared Global Workspace for Deep Learning Goyal 2022`
2. `site:openreview.net Recurrent Memory Transformer Bulatov 2022 Memorizing Transformers Wu 2022`
3. `site:proceedings.mlr.press Mamba-2 Transformers are SSMs Dao Gu 2024`
4. `site:arxiv.org Jamba Samba Hymba hybrid state space attention`
5. `"Shared Global Workspace for Deep Learning" official paper`
6. `site:openreview.net "Universal Transformers" "PonderNet"`
7. `site:proceedings.mlr.press "PonderNet" "Adaptive Computation Time"`
8. `site:arxiv.org "MemGPT" "Titans" "ATLAS" memory`
9. `site:arxiv.org/abs/2501.00663 Titans Learning to Memorize at Test Time`
10. `site:arxiv.org ATLAS learning to optimally memorize context test time`
11. `site:arxiv.org/abs/2310.08560 MemGPT Towards LLMs as Operating Systems`
12. `site:arxiv.org/abs/2607.02303 HOLA memory recurrent state`
13. `site:arxiv.org/abs/2607.07386 "Sparse Delta Memory"`
14. `site:arxiv.org/abs/2601.07372 Engram Conditional Memory`
15. `site:arxiv.org/abs/2507.03724 MemOS memory operating system`
16. `site:arxiv.org/abs/2403.11901 Larimar episodic memory forgetting`
17. `site:arxiv.org/abs/2404.11672 MemLLM read write memory API`
18. `site:arxiv.org/abs/2404.02258 Mixture of Depths dynamically allocating compute`
19. `site:openreview.net/forum?id=F87X9c107e "Adaptive Loops and Memory in Transformers"`
20. `site:arxiv.org/abs/2511.05313 CAT adaptive compute memory Pareto`
21. `site:arxiv.org/abs/2507.10524 "Mixture-of-Recursions"`
22. `site:arxiv.org/abs/2605.07721 MELT shared KV reasoning loops`
23. Direct resolution of `arXiv:2604.21999v3`, `arXiv:2606.01667`, and the other seed identifiers listed below.

Search result counts were not recorded because the web endpoint did not expose reproducible database totals. This prevents presenting the pass as a PRISMA-style systematic search.

## Primary sources actually opened and read

The locators below refer to PDF pages, not publisher running-page numbers, unless stated otherwise. Twenty-seven primary records across more than eight distinct mechanism families were opened. Relevant methods, experiments, and limitations were read rather than inferred from titles.

| Primary record | Mechanism read | Precise locator used |
|---|---|---|
| [Coordination Among Neural Modules Through a Shared Global Workspace, arXiv:2103.01197](https://arxiv.org/abs/2103.01197) | Bounded workspace slots, competition for writes, broadcast reads | §2, PDF pp. 3-5; hard/soft competition and capacity experiments, pp. 7-9 |
| [Recurrent Memory Transformer, arXiv:2207.06881](https://arxiv.org/abs/2207.06881) | Fixed-count memory tokens carried across segments; learned read/write representations | §3 and Fig. 2, PDF p. 4; results and attention analysis, pp. 6-9 |
| [Memorizing Transformers, OpenReview:TrjbxzRcnf-](https://openreview.net/forum?id=TrjbxzRcnf-) | Non-differentiable recent key-value memory, append policy, approximate kNN retrieval | §3.1, PDF pp. 4-5; Tables 1 and 5, pp. 6-7; clearing semantics, p. 10 |
| [Mamba: Linear-Time Sequence Modeling with Selective State Spaces, arXiv:2312.00752](https://arxiv.org/abs/2312.00752) | Fixed recurrent state with input-dependent selective propagation/forgetting | §§3.1-3.3, PDF pp. 5-8; selective-copy result, p. 10 |
| [Transformers are SSMs / Mamba-2, PMLR 235](https://proceedings.mlr.press/v235/dao24a.html) | State-space duality, linear recurrent mode, enlarged recurrent state | §§3.5 and 3.10, PDF pp. 6-8; MQAR state-size comparison, Fig. 3 p. 8; runtime, Fig. 4 p. 9 |
| [Jamba: A Hybrid Transformer-Mamba Language Model, arXiv:2403.19887](https://arxiv.org/abs/2403.19887) | Fixed interleaving of attention, Mamba, and MoE; configurable resource ratio | §§2-3, PDF pp. 3-5; attention/Mamba ablations, §6.1 pp. 10-11 |
| [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling, arXiv:2406.07522](https://arxiv.org/abs/2406.07522) | Layer-wise Mamba compression plus sliding-window exact recall | §2.1, PDF pp. 3-4; architecture comparisons, pp. 5-6; throughput and extrapolation, §3.3 pp. 7-9 |
| [Hymba: A Hybrid-head Architecture for Small Language Models, arXiv:2411.13676](https://arxiv.org/abs/2411.13676) | Parallel attention/SSM heads, meta-token memory, shared KV cache | Table 1, PDF p. 2; §§2.1-2.4, pp. 3-6; cost/accuracy comparisons, pp. 8-10 |
| [Titans: Learning to Memorize at Test Time, arXiv:2501.00663](https://arxiv.org/abs/2501.00663) | Short-term attention, test-time neural long-term memory, persistent memory, gated combination | §3.1, PDF pp. 5-6; §4, pp. 9-11; component ablations, p. 16 |
| [ATLAS: Learning to Optimally Memorize the Context at Test Time, arXiv:2505.23735](https://arxiv.org/abs/2505.23735) | High-capacity fixed-size neural memory and context-aware optimization | §§3.1-3.2, PDF pp. 5-8; DeepTransformers, §4 pp. 9-11; Atlas, §5 p. 12; experiments, pp. 13-16 |
| [Adaptive Computation Time for Recurrent Neural Networks, arXiv:1603.08983](https://arxiv.org/abs/1603.08983) | Learned halt probabilities, ponder cost, hard maximum | §2, PDF pp. 2-5; hard limit in Eq. 13, p. 5 |
| [Universal Transformers, arXiv:1807.03819](https://arxiv.org/abs/1807.03819) | Weight-tied recurrent attention with per-position ACT halting | §§2.1-2.2, PDF pp. 3-5; difficulty-correlated ponder depth, p. 6 |
| [PonderNet: Learning to Ponder, arXiv:2107.05407](https://arxiv.org/abs/2107.05407) | Probabilistic halting distribution and bounded evaluation depth | §§2.2-2.5, PDF pp. 3-4; ACT comparison, pp. 9-10 |
| [MemGPT: Towards LLMs as Operating Systems, arXiv:2310.08560](https://arxiv.org/abs/2310.08560) | One LLM agent pages between bounded context and persistent external stores, chains calls, and chooses when to return | §§2-2.2, PDF pp. 2-3; control-flow interrupts and function chaining, §2.3 p. 4 |
| [Mixture-of-Depths, arXiv:2404.02258](https://arxiv.org/abs/2404.02258) | Learned token router under a fixed total compute capacity | §§3.1 and 3.4, PDF pp. 4-7; isoFLOP analysis, §4.1 pp. 8-10 |
| [Adaptive Loops and Memory in Transformers: Think Harder or Know More?, OpenReview:F87X9c107e](https://openreview.net/forum?id=F87X9c107e) | Per-layer learned halting combined with input-gated local/global memory banks | §§2.1-2.2 and Fig. 1, PDF pp. 1-3; iso-parameter/iso-FLOP comparison on pp. 2-3. The official indexed PDF text was read; a later automated re-open encountered OpenReview's browser challenge. |
| [Universal Transformers Need Memory: Depth-State Trade-offs in Adaptive Recursive Reasoning, arXiv:2604.21999v3](https://arxiv.org/abs/2604.21999v3) | Memory-token capacity and ACT ponder depth as empirically substitutable resources | §§2.1-2.2, PDF pp. 2-3; memory-depth trade-off, §4.3 pp. 5-6; compute recovery, §5.1 pp. 8-9 |
| [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets, arXiv:2607.02303](https://arxiv.org/abs/2607.02303) | Fixed recurrent state plus bounded exact KV cache; surprise-based retention | §§3.1-3.4, PDF pp. 4-6; matched eviction ablations, §4.5 pp. 8-9 |
| [Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity, arXiv:2607.07386](https://arxiv.org/abs/2607.07386) | Learned sparse reads/writes to large explicit state under isoFLOP and iso-parameter constraints | §§3.1-3.2, PDF pp. 3-5; results, Table 2 p. 8; resource limitation, p. 10 |
| [Conditional Memory via Scalable Lookup / Engram, arXiv:2601.07372v2](https://arxiv.org/abs/2601.07372v2) | Explicit allocation between neural computation and static lookup memory | §3, PDF pp. 6-8; isoFLOP results, pp. 11-13; host-memory prefetch accounting, §6.4 pp. 17-18 |
| [MemOS: A Memory OS for AI System, arXiv:2507.03724v4](https://arxiv.org/abs/2507.03724v4) | Schedulable memory units with provenance, versioning, lifecycle, transactional pipelines, and rollback | MemCube representation, PDF pp. 13-16; scheduler, p. 17 and §5.4.2 pp. 20-21; provenance/update APIs and transactional pipeline, §5.3.2-5.3.3 p. 19; historical rollback, p. 21 |
| [Larimar: Large Language Models with Episodic Memory Control, arXiv:2403.11901v4](https://arxiv.org/abs/2403.11901v4) | One-shot episodic writes, sequential updates, inverse forgetting | Memory updates, PDF pp. 2-4; sequential editing, §5.3 p. 6; selective forgetting, §5.4 p. 7 |
| [MemLLM: Finetuning LLMs to Use Explicit Read-Write Memory, arXiv:2404.11672](https://arxiv.org/abs/2404.11672) | Learned explicit read/write API over relation triples and replacement of stale values | §§3.1-3.3, PDF pp. 3-7; model-selected reads, pp. 9-10; replacement semantics, p. 11 |
| [Controllably Efficient Language Models / CAT, arXiv:2511.05313v2](https://arxiv.org/abs/2511.05313v2) | One model traverses a quality/compute/memory operating curve at test time | §3, PDF pp. 4-5; throughput/memory frontier, §4.1 pp. 7-9; explicit lack of data-dependent budget allocation, limitations p. 10 |
| [Mixture-of-Recursions, arXiv:2507.10524](https://arxiv.org/abs/2507.10524) | Learned token-level recursion depth plus selective KV caching and throughput-quality Pareto frontier | §2 and Fig. 2, PDF pp. 4-5; compute/KV comparisons, §§3-4 pp. 6-10; conclusion, p. 12 |
| [Memory-Efficient Looped Transformer / MELT, arXiv:2605.07721](https://arxiv.org/abs/2605.07721) | Recurrent computation with one gated, constant-size KV state shared across loops | §3.1 and Fig. 2, PDF pp. 3-4; gate ablation, §4.4 p. 8; fixed-loop limitation, §5 p. 9 |
| [ATLAS: Agentic Test-time Learning-to-Allocate Scaling, arXiv:2606.01667](https://arxiv.org/abs/2606.01667) | One orchestrator adaptively gathers evidence, selects reasoning effort/solver, and stops; cost-quality Pareto analysis | §3.1, PDF pp. 3-4; cost and controller experiments, §4 pp. 5-8; stopping analysis, p. 9 |

## Property-by-property overlap and difference

### P-001: one controller over workspace, episodic memory, compressed state, recurrent compute, verification, and halt

Prior overlap is extensive:

- Shared Global Workspace already supplies a capacity-limited attention workspace with competitive write access and broadcast.
- ACT, Universal Transformer, and PonderNet supply learned bounded recurrent depth and halting.
- Mixture-of-Depths and Mixture-of-Recursions supply learned routing under fixed compute capacity; MoR couples recursion decisions to selective KV caching and reports a Pareto frontier.
- Frey et al. directly combine learned per-layer halting with input-gated local/global memory under iso-parameter and iso-FLOP comparisons.
- Universal Transformers Need Memory directly shows that memory capacity and ponder depth substitute at fixed accuracy. The memory/compute trade-off itself is therefore not novel.
- MemGPT lets one LLM control bounded-context paging, persistent reads/writes, chained processing, and return-to-user decisions.
- Agentic ATLAS lets one orchestrator allocate evidence gathering and reasoning effort and decide when to stop.
- HOLA and MELT couple fixed recurrent state or recurrent loops to bounded/gated exact-state paths.

The narrow difference that remains unobserved in a single primary record is an explicit, learned, constrained policy whose action space simultaneously contains mutable episodic transactions, fixed compressed-state updates, active-workspace promotion, extra recurrent compute, verification, and halting, and whose decisions are all charged to the same declared resource-price vector with hard ceilings.

This is a narrow technical hypothesis, not demonstrated novelty. Existing works often have separate gates, a deterministic consequence of one routing decision, user-selected operating points, static learned memory, or an LLM prompt policy rather than one trained constrained controller. No source above combines every candidate action and invariant. That absence does not validate the combination.

Status: `SURVIVES ONLY AS A NARROW, UNTESTED MECHANISM CLAIM`.

### P-002: versioned transactional mutations with immutable provenance binding

Component overlap is strong enough to reject a broad novelty claim:

- MemOS defines MemCubes with source metadata, version tracking, persistent provenance IDs, mutation logs, version-aware snapshots, append/merge/overwrite, transactional consistency, fault isolation, and historical rollback.
- Larimar implements online episodic writes, sequential editing, and selective inverse forgetting.
- MemLLM learns explicit read/write calls and replaces an old triple when a new fact has the same entity/relation key.
- Memorizing Transformers can clear external memory, but it lacks version semantics.

The candidate's possible distinction is narrower than “versioned memory” or “provenance”: an enforceable invariant that provenance cannot be detached from or rewritten independently of the exact retained payload, plus explicit `SUPERSEDE`, `REVOKE`, `EXPIRE`, and `ROLLBACK` semantics exposed to the same learned constrained policy. MemOS comes close at the systems layer. Its paper does not establish the candidate's schema-exact immutable binding as a neural-model invariant, nor a causal provenance intervention benchmark.

Status: `COMPONENT NOVELTY REJECTED`; only an integrated empirical/benchmark claim may survive.

### P-003: constrained allocation with complete physical resource accounting

Prior work already covers important parts:

- Mixture-of-Depths reports isoFLOP and wall-clock behavior under fixed token capacity.
- Mixture-of-Recursions reports FLOPs, KV memory/I/O, throughput, and a quality-throughput Pareto frontier.
- CAT explicitly treats measured throughput and memory as the relevant operating curve and reports HBM/KV-cache savings.
- Engram includes strict iso-parameter/iso-FLOP comparisons and measures host-memory offload/prefetch overhead.
- Sparse Delta Memory reports explicit memory footprint and aggregate accelerator use; Jamba, Samba, and Hymba report cache and throughput behavior.

No read source reports the charter's complete set in one matched evaluation: index construction and maintenance, host/device transfers, bytes moved, writes, persistent storage, compilation, warm-up, latency distribution, HBM, and energy, while separating training and inference regimes.

This surviving delta is evaluation/protocol novelty, not component novelty. It is valuable only if executed reproducibly and if it changes the comparative conclusion.

Status: `SURVIVES AS AN EMPIRICAL PROTOCOL CLAIM`.

### P-004: a non-additive interaction unavailable from components alone

The broad interaction premise is threatened:

- Jamba, Samba, and Hymba evaluate fixed attention/SSM hybrids.
- Titans compares several ways to combine short-term attention, long-term neural memory, and persistent memory.
- Frey et al. jointly vary looping and memory under matched resources.
- Engram identifies a U-shaped memory/computation allocation curve.
- Universal Transformers Need Memory directly measures substitution between state capacity and recurrent depth.
- CAT shows that existing mixers can be wrapped to obtain controllable efficiency, and MoR jointly changes recursion and KV traffic.

No read work performs a full factorial experiment on the exact candidate, especially mutable transactional episodic I/O, fixed compressed state, verification, and one shared constrained policy. Therefore the claimed interaction is neither anticipated exactly nor established. Merely adding the remaining modules would still be assembly.

Status: `SURVIVES ONLY AS A FALSIFIABLE EMPIRICAL INTERACTION CLAIM`.

## Strongest anticipation arguments

1. **A near-complete composite is already constructible from disclosed mechanisms.** Shared Global Workspace supplies `W`; HOLA supplies bounded exact KV plus fixed recurrent state; MoR supplies learned recursive allocation and selective cache traffic; MemOS supplies scheduling, versions, provenance, transactions, expiration, and rollback; Agentic ATLAS supplies evidence gathering and stop; CAT/Engram supply resource-frontier evaluation. Combining these disclosures is not itself a paper contribution.
2. **The memory-versus-compute allocation idea is directly anticipated.** Universal Transformers Need Memory observes a fixed-accuracy state/depth substitution curve; Engram optimizes memory/computation allocation; Frey et al. combine adaptive loops and gated memory; CAT exposes a test-time compute/memory operating point. The candidate cannot claim the trade-off as new.
3. **P-002 is primarily systems integration, not a new memory primitive.** MemOS is especially damaging: its provenance, version-aware mutation, transactional pipeline, scheduler, lifecycle, and rollback cover most of the language in P-002. Larimar and MemLLM cover neural write/forget/replace behavior.
4. **Adaptive routing plus memory traffic is already empirical, not hypothetical.** MoR learns token recursion depth, selectively caches KV pairs, measures traffic, and reports a Pareto frontier. A candidate controller must demonstrate cross-resource decisions beyond this coupled routing consequence.
5. **Complete accounting can be new without making the architecture new.** CAT, Engram, MoD, MoR, and SDM make partial physical accounting strong prior art. A broader accounting protocol may remain publishable as a benchmark contribution only if independently reusable and outcome-changing.

## Component novelty versus empirical novelty

| Claim type | Audit conclusion |
|---|---|
| Bounded workspace, recurrent state, exact/explicit memory, adaptive depth, halting, verification loops, provenance, versioning, transactions, rollback, or resource routing individually | Not novel |
| Attention plus SSM/recurrent state | Not novel |
| Attention plus long-term memory | Not novel |
| Memory plus adaptive recurrent depth | Not novel |
| Memory/compute quality-cost trade-off | Not novel |
| One policy over the full candidate action set under a shared explicit price vector and hard caps | Not found in one read source, but currently only an untested narrow mechanism hypothesis |
| Immutable payload/provenance binding with causal mutation tests | Not established by the read sources in the candidate's exact form; broad provenance/versioning is not novel |
| Complete physical accounting across all declared axes | Not found in one read evaluation; potentially new protocol/benchmark work |
| Non-additive gain of the exact full system | Unknown empirical question, not a novelty fact |

## Discriminating experiments required for every surviving property

### Experiment for P-001: randomized resource-price intervention

Train one shared constrained policy and compare it with:

1. a fixed composite using the same modules;
2. separately trained per-resource controllers;
3. random, write-all/read-all, write-none/read-none, and fixed-depth policies;
4. an oracle allocation policy on a tractable task subset;
5. a MoR/Frey-style controller that only couples recurrent depth and cache/memory gates.

At evaluation, randomize exogenous per-action prices and hard ceilings for workspace promotions, episodic reads/writes, state updates, recurrent steps, verification calls, and latency/HBM. Hold data, parameters, tokenizer, tuning budget, and one declared matching regime fixed. The shared controller survives only if it obeys every cap, changes allocations in the expected cross-resource directions, reduces regret to the oracle, and improves Pareto hypervolume over both fixed and separated controllers. A controller that converges to write-all, read-all, fixed-depth, or a static route refutes the claim.

### Experiment for P-002: temporal transaction and provenance intervention suite

Construct episodes with schema-exact payloads and independent ground truth for `INSERT`, `SUPERSEDE`, `REVOKE`, `EXPIRE`, and `ROLLBACK`. Include conflicting versions, delayed events, identical content from different sources, and provenance-only swaps where payload text is held constant.

Compare the candidate with MemOS-style versioned storage plus a fixed router, Larimar-style episodic updates, MemLLM-style learned I/O, and an ablation where provenance can be detached or rewritten. Report exact payload-and-version match, invalid-version leakage, rollback fidelity, revoke/expire compliance, retrieval error separately from storage error, and downstream decision changes under provenance-only interventions. The claim survives only if immutable binding is enforced and provenance interventions causally change provenance-dependent targets without changing non-provenance controls.

### Experiment for P-003: end-to-end physical-cost frontier

For every candidate and baseline operating point, measure separately:

- training FLOPs and accelerator-hours;
- inference FLOPs, p50/p95/p99 latency, throughput, HBM peak, host RAM, bytes moved, and read/write counts;
- persistent bytes, index-build/update time, index memory, CPU-to-accelerator transfers, compilation, and warm-up;
- energy with the same meter/sampling protocol where measurable.

Publish raw traces and compute Pareto hypervolume with bootstrap confidence intervals under separately declared parameter-matched, training-compute-matched, and inference-resource-matched regimes. P-003 survives only if complete accounting is reproducible and the claimed advantage remains after indexing, transfer, and mutation costs are charged.

### Experiment for P-004: preregistered factorial interaction test

At a tractable oracle scale, run a full factorial over episodic memory, compressed state, adaptive recurrent depth, provenance/transactions, verification, and joint versus separated control, while keeping the bounded workspace present and matching resources. Include the strongest fixed composite assembled from HOLA/MoR/MemOS-style mechanisms.

Preregister the interaction contrast, correction for multiple tests, seeds, exclusion rules, and minimum practically relevant effect. Test whether the full system's gain exceeds the sum of component main effects and lower-order interactions on both quality and physical cost. Replicate at two model sizes. If no preregistered higher-order interaction survives, the full-model paper is an assembly and the gate is `STOP`, even if the aggregate model beats weak baselines.

## Uncertainties and limitations

- This pass did not complete the protocol's full database-by-database result-count log or one closed snowball iteration. It cannot support an exhaustive absence claim.
- Several closest threats are 2025-2026 preprints, including records posted days before this audit. Peer review status and version drift must be rechecked before protocol freeze and submission.
- “One controller” needs a formal definition. Prior work uses separate learned gates, implicit coupling, prompted LLM orchestration, or a user-set operating knob. Without a computational-graph definition, the candidate could manufacture novelty by terminology.
- HOLA's “exact” object is a retained internal KV pair, not necessarily a bitwise source payload. That leaves a storage-semantics distinction, but not a general exact-memory novelty claim.
- MemOS specifies system invariants and APIs but does not demonstrate every one as a learned neural invariant. Conversely, system-level prior art still defeats a claim that versioning, provenance, transactions, or rollback are new concepts.
- Complete physical accounting is hardware- and implementation-sensitive. A protocol contribution needs reference implementations and raw traces, not only a metric list.
- No evidence currently establishes that the proposed full controller creates a causal interaction unavailable to a fixed composite. This is the central unresolved risk.

## Tentative gate recommendation

`PIVOT`, with the following hard interpretation:

- `STOP` the current broad architecture novelty claim. Its components, most pairwise combinations, and the memory/compute trade-off are anticipated.
- Narrow the candidate contribution to one explicit constrained per-instance policy over mutable versioned episodic I/O, fixed compressed state, recurrent compute, verification, and halt, plus a reusable transaction/provenance benchmark and complete cost protocol.
- Do not label that narrowed formulation novel yet. First pass the P-001 oracle/resource-price intervention and the P-004 factorial interaction test.
- Convert `PIVOT` to `STOP` if the shared policy does not beat the strongest fixed composite and separated controllers under complete accounting, if the policy degenerates, or if the preregistered interaction is not practically meaningful and replicated.
- A future `GO` is justified only by causal discrimination or a genuinely new benchmark/protocol that remains useful independently of the model. An assembled performance gain against weak baselines is insufficient.

## Files modified

- `docs/research/handoffs/2026-07-14-terra-evidence.md` only.

Temporary PDFs used for page-level verification were stored outside the repository under the operating-system temporary directory.

## Verification

- Read `docs/research/CHARTER.md` and `docs/research/NOVELTY.md` before extraction.
- Opened and read the relevant sections of 27 primary records across bounded-workspace, recurrent-memory, kNN-memory, SSM, hybrid, test-time-memory, adaptive-compute, agent-memory, transactional-memory, and resource-routing families.
- Checked every cited locator against the primary PDF or official primary record; no secondary source is used as evidence.
- Distinguished component novelty, narrow mechanism novelty, and empirical/protocol novelty.
- Assigned at least one falsifying experiment to each surviving property.
- No model implementation, ledger edit, bibliography edit, or novelty-register edit was made.

## Next action for Sol-PI and issue #1

Rewrite the candidate claim and M1 gate around the narrow constrained-policy delta. Add the four experiments above as mandatory pre-implementation gates, designate the HOLA + MoR + MemOS + adaptive-stop composite as the minimum strong baseline, and require an independent reviewer to confirm the causal interaction analysis. If the oracle/resource-price experiment or factorial interaction fails, close the broad model direction as `STOP` rather than converting the literature assembly into a paper narrative.
