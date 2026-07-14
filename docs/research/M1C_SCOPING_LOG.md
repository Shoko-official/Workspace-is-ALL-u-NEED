# M1c Scoping and Resolution Log

Cutoff: `2026-07-15`
Method: targeted discovery and exact-record resolution
Status: `COMPLETE_FOR_DECISION_NOT_SYSTEMATIC`

## Scope

This log preserves the decision-critical searches that resolved the final candidate set. It is not a systematic-review flow diagram and does not report unstable search-engine result totals. Earlier broad discovery calls were exploratory and are not reconstructed from memory.

The decision does not infer novelty or non-novelty from search silence. Only read primary records, author-uploaded full text, and exact generic reductions support the `STOP`.

## Recorded discovery queries

Executed on `2026-07-15` against the web search index:

```text
site:arxiv.org/abs/2605.10990 "Skill Drift Is Contract Violation"
site:arxiv.org/abs/2603.20340 ContractSkill
site:arxiv.org/abs/2606.07711 "Rosetta Memory"
site:arxiv.org/abs/2606.17573 Cordon
LLM agent persistent memory evaluation carryover reset ranking reversal benchmark state across episodes
longitudinal agent memory benchmark reset persistent stream evaluation order effect system ranking
stateful AI agent benchmark evaluation contamination carryover between tasks persistent memory rankings
site:arxiv.org agent memory benchmark cross-episode state reset order effects ranking
"What Should Agent Evaluation Measure When Agents Change Their"
"Agents Change Their" evaluation persistent inherited state benchmark
XZ6gatzn97 agent evaluation
site:arxiv.org/abs/2606.01886 InKH memory contamination beta 1-g
site:arxiv.org/abs/2505.16067 memory error replicated rewritten agent
site:arxiv.org/abs/2510.02373 A-MemGuard
site:arxiv.org "approximate probabilistic trace equivalence" total variation
"ShiftBench: Measuring Recovery of Agent Memory Under Distribution Shift"
"CCSztIjmOy" ShiftBench PDF
site:openreview.net/forum?id=CCSztIjmOy
site:arxiv.org/abs/2606.30975 "When Regulation Has Memory"
site:arxiv.org/abs/2606.29914 MemDelta
"Time Series Experiments and Causal Estimands" Bojinov Shephard DOI
site:cs.cornell.edu/fbs/publications/Hyperproperties.pdf Clarkson Schneider Hyperproperties
```

## Exact primary-record resolutions

| Record | Resolution path | Full-text check | Decision locator |
|---|---|---|---|
| `EV-0064` Cordon | arXiv `2606.17573v1` | PDF, 14 pages | abstract; Sections 3-4.1; effect outbox, lineage, validation, commit, rollback |
| `EV-0065` CoAgent | arXiv `2606.15376v1` | PDF, 14 pages | abstract; MTPO serial order, advisory conflict notification, repair, ToolSmith |
| `EV-0066` verified concurrency anomalies | arXiv `2606.17182v1` | PDF, 32 pages | abstract; Section 2.2 and PDF page 4 on deterministic semantics and stochastic scope |
| `EV-0067` Causal Agent Replay | arXiv `2606.08275v1` | PDF, 5 pages | abstract; Sections 3-4 on stochastic run-forward, confidence intervals, and Shapley attribution |
| `EV-0068` CausalFlow | arXiv `2605.25338v1` | PDF, 30 pages | Sections 3-4; Appendix A; dependency-annotated intervention and re-execution |
| `EV-0069` Rosetta Memory | arXiv `2606.07711v1` | PDF, 19 pages | abstract; Sections 1-3; writer/reader operators and unseen-model replacement |
| `EV-0070` AFTER | arXiv `2606.23127v1` | PDF, 18 pages | PDF pages 1-4 and 6; cross-model transfer and versioned EVOLUTION harness |
| `EV-0071` rate-distortion compaction | arXiv `2607.08032v1` | PDF, 24 pages | Sections 2, 13.2, 14.2, and 15 |
| `EV-0072` longitudinal safety | arXiv `2605.17830v1` | PDF, 42 pages | Sections 3.3 and 5.1; PDF pages 5-8; snapshots and order randomization |
| `EV-0073` Memory-R2 | arXiv `2605.21768v1` | PDF, 26 pages | abstract; Section 3.3; paired rerollouts from one memory state |
| `EV-0074` EvoMemBench | arXiv `2605.18421v1` | PDF, 30 pages | Section 5.1 PDF page 6; Appendix B.2 PDF page 21 |
| `EV-0075` Skill Drift | arXiv `2605.10990v1` | PDF, 22 pages | abstract; Sections 3-6; Appendices B, F, G, J, and O |
| `EV-0076` A-MemGuard | arXiv `2510.02373v1` | PDF, 27 pages | Section 4.2 PDF page 6; Section 5.2 and Figure 3 PDF page 8 |
| `EV-0077` Artifact Ecology | OpenReview `XZ6gatzn97`; author upload DOI `10.13140/RG.2.2.22606.42563` | author-uploaded full text | Definition 1; Sections 4.2-4.4; Table 2; future-work paragraphs on task streams and causal estimands |
| `EV-0078` Adaptive Functional Programming | official CMU author PDF | PDF, 45 pages | Sections 4.4-4.5 and 7.2; correctness statement and theorem on PDF pages 33-36; Section 7.2 continues through page 42 |
| `EV-0079` I-confluence | official PVLDB PDF | PDF, 12 pages | Sections 4.1-4.2; Theorem 1 on PDF page 5 |
| `EV-0080` approximate probabilistic trace equivalence | arXiv `1701.04547v3` | PDF, 27 pages | Sections 3-4; Definitions 7-8; Theorems 2-4 |
| `EV-0081` artificial-agency hysteresis | arXiv `2606.30975v1` | PDF, 16 pages | abstract; Sections 3.1-3.5; Equation 11; Section 4 |
| `EV-0082` ShiftBench | OpenReview `CCSztIjmOy` | primary forum metadata and abstract; indexed primary-PDF Section 1 | abstract ranking-reversal results; Section 1 protocol and Equation 1 |
| `EV-0083` MemDelta | arXiv `2606.29914v1` | PDF, 13 pages | abstract; Sections 3-5; controlled rank reversals and recommended protocol |
| `EV-0084` Hyperproperties | Journal of Computer Security 18(6); DOI `10.3233/JCS-2009-0393` | official author PDF, 55 physical pages: 54 article pages plus one copyright page | Section 2.3 Equation 2.6; Section 7.2.4 Equation 7.5 |
| `EV-0085` time-series causal estimands | JASA 114(528); DOI `10.1080/01621459.2018.1527225`; arXiv `1706.07840v2` | author PDF, 42 pages | Section 2; Section 3.1 Definition 1; Section 5.1 Equation 9 |

## Resolution notes

- Recent arXiv records are pinned to the read version. They are public disclosures, not treated as peer-reviewed empirical truth.
- The OpenReview interface challenged automated retrieval. The authors' public full-text upload was read instead and retains the OpenReview identifier in the evidence record.
- The same interface blocked local full-text retrieval for ShiftBench. The primary forum metadata and abstract were read directly, and the indexed primary-PDF extract exposed the Section 1 protocol. The decision uses only those verified passages and does not claim to have inspected its appendices.
- PDF text extraction was checked against rendered pages for the decision-critical longitudinal, Memory-R2, AFTER, rate-distortion, hysteresis, MemDelta, Hyperproperties, and time-series causal-estimand passages.
- ContractSkill changed author metadata between arXiv versions: the v1 metadata lists six authors including Chen Dai, while the downloaded unpinned v3 first page lists seven authors including Lianyong Qi and Shi Jin. It is not used as decision-critical evidence; Skill Drift and AFTER already provide the positive collision.
- No result count, excluded-title count, snowball closure, or exhaustive coverage claim is made.

## Search outcome

The final carryover candidate was not rejected because no exact phrase was found. No examined record reports the exact reset-per-episode versus persistent-stream ranking inversion. `EV-0077` anticipates the inheritance protocol, `EV-0082` reports longitudinal memory-policy ranking reversals that change system selection, `EV-0083` reports controlled conclusion reversals and requests rank-order stability checks, and `EV-0085` supplies path-indexed causal estimands. The explicit `2 x 2` mapping in the candidate register shows that the exact inheritance cell adds no distinct estimator or mechanism.

Likewise, no examined record reports the exact LLM `A -> B -> A` forgetting-and-resurrection protocol. `EV-0081` already establishes the adaptive-agent hysteresis phenomenon under target reversal without reset, `EV-0084` supplies the two-trace non-interference form, and the earlier LLM state-validity records supply the stale-state application. The decision is a positive composite anticipation, not an absence-of-prior-art inference.
