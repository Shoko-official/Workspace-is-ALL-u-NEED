# M1f Mechanism-First Object Register

Cutoff: `2026-07-15`
Issue: [#21](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/21)
Gate result: `PROPOSED_STOP`
Mechanism-first objects tested sequentially: `9`
Admitted objects: `0`
Surviving `DISTINCT_CANDIDATE` objects: `0`

## Gate

M1f did not generate another fixed-size candidate batch. It first mapped the
blind spots left by all 64 M1c, M1d, and M1e formulations, then tested one
technical object at a time. An object was rejected immediately unless it fixed:

1. a primitive or observable not obtained by renaming an earlier object;
2. one intrinsic task and comparison class;
3. the strongest co-designed and jointly trained comparator with the same
   observations, randomness, state, transcript, work, depth, feedback, and
   operation class;
4. one exact theorem, estimand, invariant, or transportable law;
5. a decisive falsifier and a negative regime;
6. a boundary against generic information flow, communication, coding,
   scheduling, mechanism-design, program-verification, and online-control
   reductions; and
7. technical content that remains specific after all LLM, memory, workspace,
   manager, and router labels are replaced.

The search used the newly recovered upstream report as an input, not as
scientific evidence. The 23-page PDF is fixed by SHA-256
`c584128e870e22e2c0372c5cdc6dc41558f9655c256dc46770f50937cd2f8046`
(`EV-0153`). Its central "tokenisation par mission" route received the same
gate as every independently generated object.

The result is exclusive: no object reached admission. Each object below is
retained because its failed boundary prevents later work from reviving it by
relabeling.

## Candidate register

### M1F-O01: Endogenous evidence inflation

- Primitive: an evidence-dependence graph in which consolidation can turn
  descendants of one observation into apparently independent corroboration.
- Observable: effective independent evidence mass after quotienting records by
  common ancestry, versus the confidence or authority assigned by the reader.
- Class: multi-session `observe -> consolidate -> retrieve -> decide` systems
  with immutable origin identifiers and an unbounded sequence of derived
  summaries.
- Strongest comparator: a co-designed store and reader that retain raw episodes,
  lineage, uncertainty, and dependency-aware aggregation under the same storage
  and compute budgets.
- Candidate result: repeated self-derived records cannot increase evidential
  support beyond the mass of their independent roots; a reader that treats
  descendants as independent exhibits confidence inflation.
- Decisive falsifier: a construction in the same information class where
  derived copies add calibrated independent evidence without a new observation.
- Negative regime: genuinely independent sources, authenticated new evidence,
  or a store that never consolidates.
- Reduction boundary: Bayesian dependence, provenance, data lineage, duplicate
  evidence, and branching-process feedback. M1C-C12 through C14 and M1D-C03,
  C06, C12, C14, C15, C19, C21, and C24 already cover the application loop.
  Manufactured Confidence, A-MemGuard, and Useful Memories provide direct
  positive LLM-memory collisions (`EV-0154`; `EV-0076`; `EV-0099`).
- Disposition: `RECYCLING_AND_DIRECT_COLLISION`.

### M1F-O02: Semantic ABI across persistent writer-reader versions

- Primitive: a versioned contract between a writer model, stored representation,
  and later reader model.
- Class: a record written by model or runtime `a` is consumed after replacement
  by `b`, with the same payload and declared migration budget.
- Strongest comparator: jointly designed writer, migration layer, and reader
  that know both versions and may preserve a canonical representation.
- Candidate result: a compatibility certificate preserves a registered decision
  or output distribution across model replacement.
- Decisive falsifier: a replacement pair that passes the certificate but changes
  the registered decision outside tolerance.
- Negative regime: fixed writer and reader, canonical lossless payloads, or full
  replay after replacement.
- Reduction boundary: representation contracts, schema migration, replay, and
  decision-preserving state migration. This is M1C-C08, C09, and C11. Rosetta
  Memory and AFTER already treat cross-model writer-reader compatibility,
  versioning, validation, and rollback (`EV-0069`; `EV-0070`).
- Disposition: `RECYCLING_AND_DIRECT_COLLISION`.

### M1F-O03: Durable experience displaces future reasoning compute

- Primitive: the reduction in matched inference work on a task family caused by
  retaining prior solved trajectories or abstractions.
- Class: recurrent exposure to related tasks with memory construction, retrieval,
  and reasoning costs fully charged.
- Strongest comparator: any memory and adaptive-compute method under the same
  total past and current compute, storage, task-similarity information, and
  answer-quality requirement.
- Candidate result: a task-relevance-conditioned reduction in later reasoning
  cost without loss of quality.
- Decisive falsifier: the reduction disappears after memory construction and
  retrieval are charged, or an equally informed memoryless amortized learner
  matches it.
- Negative regime: unrelated tasks, unusable memories, or one-shot evaluation.
- Reduction boundary: amortized computation and learning from experience; it
  also recycles M1D-C02, C04, C09 through C13, C20 through C23. SpeedupLLM
  already formalizes adaptive compute plus memory and reports the target
  behavior (`EV-0155`).
- Disposition: `ANTICIPATED_DIRECTLY`.

### M1F-O04: Non-malleable authority for persistent records

- Primitive: origin-bound authority that cannot increase through summarization,
  tool echo, or manufactured corroboration without authenticated endorsement.
- Observable: `Amplify(e,L) = 1[a(L(e)) > a(e) and no endorsement]`.
- Class: multi-session `write -> retrieve -> transform -> act` pipelines with
  consequential actions.
- Strongest comparator: complete mediation, immutable labels, conservative
  propagation, capabilities, and an external monitor under the same utility
  and latency budget.
- Candidate result: content and malleable lineage are insufficient; write-time
  origin binding is necessary; non-malleable authority with corroboration-gated
  elevation is sufficient.
- Decisive falsifier: a content- or lineage-only defense safe under the declared
  laundering channels, or a mediated trace that violates the invariant.
- Negative regime: trusted-only memory, no consequential action, compromised
  origin authentication, or a finite whitelist.
- Reduction boundary: information-flow control, Biba integrity, capabilities,
  and confused-deputy prevention. More importantly, TMA-NM states essentially
  the same LLM-memory invariant and necessity/sufficiency results; f-secure and
  CaMeL supply the surrounding IFC/capability constructions (`EV-0156` through
  `EV-0158`).
- Disposition: `ANTICIPATED_DIRECTLY`.

### M1F-O05: Persistent-secret leakage through adaptive-compute traces

- Primitive: a secret-to-trace channel from persistent state `S` to observable
  `Tau = (depth, halt time, latency, calls, addresses, branches)`.
- Class: `H` adaptive interactions in which the adversary selects the next
  public query from earlier traces while the same secret persists.
- Strongest comparator: a manager-router system judged on `(output,Tau)` and
  allowed constant-time padding, random delay, the same public seed, the same
  worst-case compute ceiling, and adaptive privacy composition.
- Candidate result: noninterference of low-equivalent states, or an
  `(epsilon,delta)` likelihood-ratio bound on the enriched output trace.
- Decisive falsifier: two low-equivalent states with a trace event of unequal
  probability, or a violation of the registered likelihood-ratio bound.
- Negative regime: a public state, a constant trace, or padding to the declared
  worst case.
- Reduction boundary: once `Tau` is treated as output, the object is timing
  privacy, information-flow noninterference, covert-channel capacity, and
  adaptive DP composition. Ratliff and Vadhan define precisely this output-plus-
  runtime privacy class (`EV-0159`). M1e already charged every timing, address,
  and action side channel to the transcript.
- Disposition: `REDUCED_TO_TIMING_PRIVACY_IFC_DP`.

### M1F-O06: Shared-subcomputation work-depth separation

- Primitive: for a randomized circuit `J(h,r) = (m,c)`, the ratio between the
  least factorized work and joint work under matched depth and messages.
- Class: two co-designed modules with common public input `h`, common public
  seed `r`, total work `W`, depth `D`, fast memory `S`, and transcript `B`.
- Strongest comparator: parallel execution, shared code and parameters, common
  public preprocessing, and all activation transfers charged.
- Candidate result: a superconstant work or depth separation for jointly
  choosing a memory action and a compute action.
- Decisive falsifier: run two copies of `J` with the same `(h,r)`, retain one
  output from each, and obtain the exact joint law with work at most `2W`, depth
  `D`, and zero message. Alternatively, execute `J` once and transmit `c` in
  `ceil(log |C|)` bits. This compiler already falsifies the candidate.
- Negative regime: common inputs and randomness, bounded outputs, or a message
  large enough to carry one output.
- Reduction boundary: private or late inputs yield communication complexity;
  private randomness yields channel synthesis; isolated memories yield red-blue
  pebbling; restricted fanout yields circuit complexity. SFRL and multiprocessor
  pebbling fix those boundaries (`EV-0160`; `EV-0161`). TriRoute is also a direct
  recent empirical collision for a shared controller over attention, experts,
  depth, and KV precision (`EV-0162`), although its preprint results remain
  unreviewed and unreplicated.
- Disposition: `REDUCED_TO_CIRCUIT_SHARING_COMMUNICATION_PEBBLING`.

### M1F-O07: Universal gate for executable persistent writes

- Primitive: a total gate `V(p,sigma)` deciding whether every future execution
  of a persisted program or policy `p` satisfies a nontrivial trace property.
- Class: Turing-complete writes, unbounded inputs and horizons, and adaptive
  scheduling.
- Strongest comparator: any total computable verifier with the same program,
  specification, and resources.
- Candidate result: `V(p)=1` iff all executions are safe, with both soundness and
  completeness.
- Decisive falsifier: a total sound and complete verifier for the declared
  nontrivial semantic property, or a property that is actually syntactic.
- Negative regime: finite automata, bounded horizons, total DSLs, decidable
  contracts, or proof-carrying restricted writes.
- Reduction boundary: Rice's theorem, halting, and ordinary program
  verification; it also recycles M1C-C11 and M1D-C18. SEVerA already supplies a
  recent restricted constructive branch using formal contracts, rejection
  sampling, verified fallback, and synthesis (`EV-0163`).
- Disposition: `GENERIC_UNDECIDABILITY_PLUS_PRIOR_RESTRICTED_CONSTRUCTION`.

### M1F-O08: Mission-switch codec closure

- Primitive: a persistent record `(a,z)` where `a` versions the writer codec and
  `z=T_a(x)`, later consumed under reader mission and codec `b` with compute
  choice `c`.
- Class: arbitrary mission sequences, reversible text tokenizers
  `D_a(T_a(x))=x`, and explicit state, tokenization, migration, and inference
  budgets.
- Strongest comparator: co-designed manager and router with the record, all
  codecs, a canonical byte representation, the same models, and the same total
  budget.
- Candidate result: mission-conditioned tokenizer switching creates an
  intrinsic semantic or state-compute capability unavailable to the comparator.
- Decisive falsifier: the exact transcode `C_ab = T_b o D_a` gives
  `D_b(C_ab(T_a(x)))=x`; the comparator therefore reproduces the reader input,
  action `(b,c)`, and output law with the same transcode cost. If the code is
  non-injective, two inputs collide and no amount of later compute can recover
  both without extra information.
- Negative regime: fixed tokenizers, canonical byte storage, inaccessible
  decoders, destructive normalization, model-specific latent or KV payloads,
  or truncation after retokenization.
- Reduction boundary: reversible text gives ordinary transcoding; learned
  embeddings give tokenizer transfer; token IDs or latent payloads give schema
  migration, rate-distortion, Rosetta-style writer-reader adaptation, and
  exactly M1C-C09. Dynamic and evolving text tokenization are already active
  primary literatures (`EV-0166`; `EV-0168`; `EV-0169`).
- Report audit: the upstream report's use of UniTok is a category error. UniTok
  maps recommender-system item embeddings into discrete item identifiers; it
  does not segment prose, code, or mathematics (`EV-0167`). Vocabulary
  customization supports at most its stated domain-tokenization results, not
  the report's assembled mission swarm (`EV-0166`).
- Disposition: `CATEGORY_ERROR_AND_DIRECT_COMPOSITE`.

### M1F-O09: Strategic memory contribution with costly audits

- Primitive: strategic senders propose persistent records, may misreport private
  information, and face an audit policy whose verification is costly.
- Class: repeated information acquisition with full or bandit feedback,
  incentive constraints, and an explicit audit budget.
- Strongest comparator: any incentive-compatible online mechanism with the same
  sender information, transfers or non-monetary sanctions, audits, feedback,
  and horizon.
- Candidate result: a new truthful-reporting and audit-regret frontier caused by
  persistence and adaptive reasoning.
- Decisive falsifier: an ordinary online information-acquisition or costly-audit
  mechanism attains the same incentive, regret, and audit guarantees after
  records are renamed reports.
- Negative regime: nonstrategic writers, free verification, or fully observed
  truth.
- Reduction boundary: online mechanism design for information acquisition and
  repeated allocation with adaptive costly audits already define the class and
  its regret/audit tradeoffs (`EV-0164`; `EV-0165`). Persistent storage changes
  neither the private-information nor incentive object.
- Disposition: `REDUCED_TO_MECHANISM_DESIGN`.

## Crosswalk against all 64 prior formulations

The crosswalk records the nearest recycling path before an M1f object is tested.
`Outside` means the new primitive was not itself an earlier candidate; it does
not mean that it survived a generic reduction or direct collision.

| Prior object | Relation to M1f attempt | Boundary result |
|---|---|---|
| M1C-C01 | O02/O08 recycle replay across representations | `RECYCLED` |
| M1C-C02 | O02/O08 reuse dependency closure for migration | `RECYCLED` |
| M1C-C03 | O02/O08 reuse the minimum recomputation cone | `RECYCLED` |
| M1C-C04 | O02/O08 reuse revision escape after codec drift | `RECYCLED` |
| M1C-C05 | O01/O08 reuse compaction coverage | `RECYCLED` |
| M1C-C06 | O02 reuses transaction semantics across writers | `RECYCLED` |
| M1C-C07 | O02 reuses confluence under version changes | `RECYCLED` |
| M1C-C08 | O02/O08 are runtime-drift replay closure | `RECYCLED` |
| M1C-C09 | O02/O08 are decision-preserving migration | `RECYCLED` |
| M1C-C10 | O04 reuses authority-bearing read closure | `RECYCLED` |
| M1C-C11 | O02/O07 reuse contract-carrying procedure | `RECYCLED` |
| M1C-C12 | O01 is the same contamination feedback family | `RECYCLED` |
| M1C-C13 | O01 is the same read-write divergence family | `RECYCLED` |
| M1C-C14 | O01 reuses post-consolidation resurrection | `RECYCLED` |
| M1C-C15 | O03 reuses reset-versus-stream exposure | `RECYCLED` |
| M1C-C16 | O03 reuses cross-family persistent scaling | `RECYCLED` |
| M1D-C01 | O04/O07 reuse safe-write admission | `RECYCLED` |
| M1D-C02 | O03 is lifetime value of compute | `RECYCLED` |
| M1D-C03 | O01 reuses compute-conditioned selection bias | `RECYCLED` |
| M1D-C04 | O03 reuses memory-mediated future compute | `RECYCLED` |
| M1D-C05 | O02/O08 reuse storage-recompute migration | `RECYCLED` |
| M1D-C06 | O01/O07 reuse validation debt | `RECYCLED` |
| M1D-C07 | O09 reuses governed adaptive acquisition | `RECYCLED` |
| M1D-C08 | O04/O09 reuse governance recourse | `RECYCLED` |
| M1D-C09 | O03 is durable-compute amortization | `RECYCLED` |
| M1D-C10 | O03 is state-conditioned compute elasticity | `RECYCLED` |
| M1D-C11 | O03 reuses deferred write credit | `RECYCLED` |
| M1D-C12 | O01/O07 reuse verification before refresh | `RECYCLED` |
| M1D-C13 | O03 reuses build/read compute response | `RECYCLED` |
| M1D-C14 | O01 reuses correlated-consensus contamination | `RECYCLED` |
| M1D-C15 | O01 reuses the self-sealing undercompute loop | `RECYCLED` |
| M1D-C16 | O09 reuses prospective compute opportunity cost | `RECYCLED` |
| M1D-C17 | O09 reuses compute reservation by obligations | `RECYCLED` |
| M1D-C18 | O07 is proof-carrying state verification | `RECYCLED` |
| M1D-C19 | O01/O04 reuse persistent commit consensus | `RECYCLED` |
| M1D-C20 | O02/O03 reuse durable deferred reasoning | `RECYCLED` |
| M1D-C21 | O01/O03 reuse consolidation-driven retirement | `RECYCLED` |
| M1D-C22 | O03/O06/O08 reuse state-compute co-scheduling | `RECYCLED` |
| M1D-C23 | O03/O09 reuse the shadow price of reusable compute | `RECYCLED` |
| M1D-C24 | O01/O09 reuse epistemic compute for state choice | `RECYCLED` |
| M1E-C01 | O02/O08 become one-way encoding and recall | `RECYCLED_OR_REDUCED` |
| M1E-C02 | O08 latent/KV payloads become cache memory-time | `RECYCLED_OR_REDUCED` |
| M1E-C03 | O06 private intermediate access becomes cell-probe | `REDUCED` |
| M1E-C04 | O02 mutable compatibility becomes dynamic data structure | `REDUCED` |
| M1E-C05 | O06 repeated recomputation becomes multi-pass streaming | `REDUCED` |
| M1E-C06 | O06 bounded coordination becomes communication | `REDUCED` |
| M1E-C07 | No M1f object supplies the missing generic lower bound | `NO_REOPENING` |
| M1E-C08 | O06/O07 external traces reuse supervised computation | `RECYCLED` |
| M1E-C09 | O01/O09 selective audits reuse endogenous labels | `RECYCLED` |
| M1E-C10 | O01 compressed evidence reuses proxy identification | `RECYCLED` |
| M1E-C11 | O09 incentives reuse randomized encouragement | `RECYCLED` |
| M1E-C12 | O03/O09 persistent populations reuse stationary effects | `RECYCLED` |
| M1E-C13 | O06 private inputs become bounded-message causal views | `REDUCED` |
| M1E-C14 | O09 audits reuse fixed-budget intervention selection | `RECYCLED` |
| M1E-C15 | O01/O09 reuse dual epistemic audit | `RECYCLED` |
| M1E-C16 | O03 reuses compute mediated by writes | `RECYCLED` |
| M1E-C17 | O03 is persistent test-time adaptation | `RECYCLED` |
| M1E-C18 | O01/O06 reuse verifier state and expert selection | `RECYCLED` |
| M1E-C19 | O02/O08 reuse persistent sparse representation | `RECYCLED` |
| M1E-C20 | O06 is recurrent state and adaptive depth | `RECYCLED` |
| M1E-C21 | O03/O09 reuse costly-feature lifelong learning | `RECYCLED` |
| M1E-C22 | O02/O03 reuse lifelong representation | `RECYCLED` |
| M1E-C23 | O03/O06 reuse adaptive inner-loop depth | `RECYCLED` |
| M1E-C24 | O06/O09 private information becomes bounded transcript | `REDUCED` |

The only primitives outside the exact 64-object surface were origin-bound
authority, timing privacy, strategic reporting, universal executable-write
verification, and shared circuit work-depth. They fail respectively by direct
collision, generic IFC/DP, mechanism design, undecidability plus restricted
verification, and a constant-factor compiler plus communication/pebbling.

## Strongest-composite result

The strongest surviving composition is not a new object. A system may combine:

- canonical byte storage and versioned writer-reader adaptation;
- domain or dynamically adapted tokenization;
- persistent episodic records and lineage-aware consolidation;
- a shared adaptive controller over attention, experts, depth, and cache;
- origin-bound authority and complete mediation; and
- timing padding or privacy accounting.

Every component and each declared interface is directly occupied or reducible.
The composition supplies no theorem, invariant, estimand, or capability that
the matched co-designed comparator cannot reproduce. An implementation could
still be useful, but utility cannot substitute for article-level originality.

## Minimum-design decision

No minimum experiment is authorized. The decisive outcomes are pre-empirical:

1. O06 is falsified by an exact compiler with at most a factor-two work cost and
   no depth separation.
2. O08 is closed by exact transcoding for reversible tokenizers and by
   information loss for non-injective codebooks.
3. O04 and O03 are directly occupied.
4. O01 and O02 recycle earlier objects and direct LLM-memory work.
5. O05, O07, and O09 become established generic classes after label
   substitution.

An experiment cannot repair any of these admission failures. The experiment
registry remains empty.

## Decision

M1f returns `STOP` for all nine sequential mechanism-first attempts.

- Zero objects are admitted.
- Zero objects are `DISTINCT_CANDIDATE`.
- The recovered report does not authorize its "mission tokenization" pipeline;
  its key UniTok mapping is a category error and the remaining pipeline is an
  architecture assembly.
- The result is targeted and non-exhaustive. It relies on explicit compilers,
  direct primary collisions, generic reductions, and the complete 64-object
  crosswalk, not search silence.
- No article, proof program, model, benchmark, implementation, training run,
  experiment, paid compute, or submission is authorized.

This proposed decision requires independent scientific, bibliographic, and
governance review before protected integration.
