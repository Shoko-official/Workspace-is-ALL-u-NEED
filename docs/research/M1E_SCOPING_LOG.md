# M1e Scoping and Resolution Log

Cutoff: `2026-07-15`
Method: restricted-class candidate generation, primary-record resolution, and generic-object reduction
Status: `COMPLETE_FOR_DECISION_NOT_SYSTEMATIC`

## Scope

M1e searched for a theorem, lower or upper bound, identified estimand, or
transportable phase law in which governed persistent state and adaptive
computation remain jointly necessary after the comparison class is fully
matched.

Three read-only lanes examined communication and streaming complexity, online
causal identification, and learning or sample efficiency. Each lane returned
eight candidates and zero survivors. The search is not a systematic review and
does not infer novelty from a missing result. It records the positive sources,
version corrections, and generic reductions that determine the decision.

The comparison class fixed task family, observation order, online causality,
state and transcript bits, rounds, probes or passes, compute or oracle calls,
feedback, shared randomness, training information, and cross-module
communication. Factorized modules could be jointly trained and co-designed.

## Recorded discovery queries

The following queries were executed on `2026-07-15` against the web index and
resolved to primary records:

```text
site:arxiv.org transformer recurrent memory time space tradeoff lower bound formal language 2024 2025
site:openreview.net recurrent transformer adaptive computation theoretical separation ICLR 2025
site:arxiv.org in-context learning test-time training sample complexity separation theorem 2025
site:dl.acm.org streaming interactive communication lower bound future adaptive queries persistent memory
"this separation arises because looping the" transformer ICLR 2025
"looped Transformers with an adaptive" ICLR 2025
site:openreview.net/forum?id=n2NidsYDop
site:arxiv.org "process supervision" "looping" transformers complexity theory
site:arxiv.org dynamic data structures adaptive query lower bound preprocessing communication complexity cell probe 2024 2025
site:arxiv.org online learning persistent memory adaptive computation lower bound regret task recurrence
site:arxiv.org test time compute persistent memory theoretical sample complexity language models
site:proceedings.mlr.press external memory adaptive computation lower bound neural network
online learning experts limited memory limited queries per round regret tradeoff
site:proceedings.mlr.press bandit experts memory query complexity regret
site:arxiv.org memory computation regret tradeoff online learning experts queries
site:dl.acm.org streaming online learning memory query regret tradeoff
site:proceedings.mlr.press adaptive data collection persistent state causal identification policy dependent data online learning
site:arxiv.org agent memory causal effect adaptive computation longitudinal intervention LLM
site:proceedings.mlr.press off-policy evaluation endogenous state representation adaptive data collection
site:arxiv.org performative prediction stateful environment memory causal intervention adaptive policy
"Compression Barriers for Autoregressive Transformers" Haris Onak 2025
site:arxiv.org "RNNs are not Transformers (Yet)"
site:arxiv.org "When Do Transformers Outperform Feedforward and Recurrent Networks?"
site:arxiv.org "Transformers Provably Solve Parity Efficiently with Chain of Thought"
"Time-Space Tradeoffs for Element Distinctness and Set Intersection via Pseudorandomness" SODA 2023 DOI
site:proceedings.mlr.press "Identifying Best Interventions through Online Importance Sampling"
site:proceedings.mlr.press "Causal Bandits with General Causal Models and Interventions"
site:openreview.net "Sample Complexity and Representation Ability of Test-time Scaling Paradigms"
site:proceedings.neurips.cc "When Do Transformers Outperform Feedforward and Recurrent Networks?"
```

Citation following was limited to records needed to resolve a candidate,
identify its strongest factorized comparator, or verify a theorem, venue,
version, or withdrawn-source correction.

## Exact primary-record resolutions

| Evidence | Record | Decision locator |
|---|---|---|
| `EV-0116` | Test-Time Training Provably Improves Transformers as In-context Learners | Proposition 3.1; Theorems 4.2, 4.5, 5.3; Corollaries 4.4, 4.6, 5.4 |
| `EV-0117` | Sample Complexity and Representation Ability of Test-time Scaling Paradigms | Propositions 1.1-1.2; Theorems 3.1-3.2 and 4.7 |
| `EV-0118` | When Do Transformers Outperform Feedforward and Recurrent Networks? | q-Sparse Token Regression; Theorems 1, 3, 5, 7, 9 |
| `EV-0119` | Looped Transformers for Length Generalization | Definition 3.1; Propositions 3.2-3.4; architecture and adaptive inference in Section 4; empirical length generalization in Section 6 |
| `EV-0120` | Lifelong Learning in Costly Feature Spaces | Algorithms 1-3; Theorems 1 and 11; lower-bound lemmas |
| `EV-0121` | Provable Lifelong Learning of Representations | Theorems 1-6; Appendix B |
| `EV-0122`-`EV-0125` | Online and memory-reduced meta-learning; modular credit | Registered algorithms and theorem locators in the evidence ledger |
| `EV-0126`-`EV-0127` | Memory, communication, statistical queries, and distributed estimation | Protocol classes and lower-bound theorems |
| `EV-0128` | Decision-Making Under Selective Labels | Section 2; Theorem 1; Propositions 2-4 |
| `EV-0129` | Semiparametric Efficient Inference in Adaptive Experiments | Section 2.1; Theorems 2, 4, 5 |
| `EV-0130`-`EV-0131` | Confounded and partially observed OPE through proxies | Bridge, rank, completeness, invertibility, and identification theorems |
| `EV-0132`-`EV-0133` | Instrument-armed and endogenous causal bandits | Instrument assumptions, regret, consistency, and identification results |
| `EV-0134` | OPE under sequential ignorability | Models 1-3; Theorems 2.1, 3.1, 3.5 |
| `EV-0135` | State-dependent performative prediction | Equations 2-5; Algorithm 1; Theorem 1 |
| `EV-0136` | Distributed data-processing inequality | Theorem 1.1; Corollary 1.2; Theorem 4.5; Corollary 4.8 |
| `EV-0137` | Adaptive Online Experimental Design for Causal Discovery | Theorems 1-2; Algorithm 1 |
| `EV-0138` | Bayes-Adaptive POMDP | Sections 3-5; Theorems 1 and 4 |
| `EV-0139` | Marginal structural models | Sections 1, 4, 6.1, 7; Equation 14 |
| `EV-0140` | Proximal mediation with hidden recanting witnesses | Assumptions 2.1-2.3 and 3.1-3.5; Theorems 3.1-3.3 and 4.1-4.3 |
| `EV-0141` | Switchback experiments | Theorems 1-3; Corollary 2; carryover sensitivity |
| `EV-0142` | Compression Barriers in Autoregressive Transformers | Definition 4; Theorems 2, 5, 6, 8, 19; Corollary 16 |
| `EV-0143` | Tensor-attention KV memory bounds and time comparison | Definition 3.10; Lemma 3.11; Theorems 4.1-4.3 |
| `EV-0144` | RNN retrieval bottleneck | Sections 3, 4.2.1, 5.1-5.2; Appendix C.4; Lemma C.24 |
| `EV-0145` | Transformers solve parity with chain of thought | Theorems 2, 5, 7; Sections 3.2-3.3 |
| `EV-0146` | Optimal non-adaptive cell-probe dictionaries | Theorems 1-2; Section 4 |
| `EV-0147` | Logarithmic cell-probe lower bounds | Theorems 2.1-2.5 |
| `EV-0148` | Multi-pass graph-stream lower bounds | Results 1-2; Theorems 1-2; Section 1.4 correction |
| `EV-0149` | Pointer-chasing round lower bound | Definition 1; Theorem 2; Corollary 3 |
| `EV-0150` | Element-distinctness time-space upper frontier | Main upper bound and contrast with Set Intersection lower bound |
| `EV-0151` | Identifying Best Interventions through Online Importance Sampling | Section 2; Algorithm 1; Definition 3; Theorems 1-2 and 5 |
| `EV-0152` | Causal Bandits with General Causal Models and Interventions | Assumptions 2.1-2.3; Algorithms 1-2; Theorems 5.3 and 5.5-5.10 |

Existing `EV-0090` is reused for longitudinal mediation. Earlier POMDP, dynamic
value-of-computation, online-optimization, and adaptive-estimation records remain
background threats, but the M1e decision does not require duplicating them.

## Resolution notes

- Gözeten et al. is pinned to arXiv v2 and the ICML 2025 PMLR record. Its
  separation applies to the studied linear Transformer and declared covariance,
  noise, alignment, and asymptotic regimes.
- Huang et al. is pinned to the ICLR 2026 OpenReview record and arXiv v2. The `Delta` bounds require `Delta>0` and a
  reward uniquely maximized by the correct answer; upper bounds include the
  confidence logarithm. Theorem 4.7 is expressivity, not durable cross-task
  memory.
- The sparse-retrieval record is pinned to the NeurIPS 2025 main-conference
  version; the earlier HiLD at ICML 2025 oral remains provenance only. It
  supplies only the retrieval component of the composite.
- Looped Transformers receives `T(n)` during training and uses either that
  count or a confidence stopping rule at inference. It proves the n-RASP-L
  decompositions in Propositions 3.2-3.4 and empirically demonstrates learned
  length generalization; it does not prove a learning/generalization theorem.
- The causal-bandit IV record is an arXiv preprint and NeurIPS 2022 workshop
  poster, not a main-proceedings paper.
- The proximal hidden-recanting-witness record is a current v1 preprint. It
  strengthens a reduction but is not needed to establish the older
  longitudinal-mediation collision.
- Haris and Onak is pinned to the COLT 2025 PMLR record and arXiv v1. Theorem 19,
  not Theorem 17, is the non-adaptive time lower bound. Its results apply to the
  registered attention approximation and dimension regimes, not all persistent
  memory.
- The tensor-attention cache record is pinned to v2 and supports two tensor-
  cache memory lower bounds plus a time comparison, not a general memory-time
  frontier.
- The published ICALP 2024 non-adaptive-dictionary record is a merged revision
  of withdrawn arXiv:2001.05053 and arXiv:2308.16042. The withdrawn preprint is
  not evidence.
- Assadi et al. is pinned to corrected v2; Section 1.4 documents the repaired
  technical lemma and states that the main results remain correct.
- The pointer-chasing theorem numbering differs between the preprint and ITCS
  publication. The evidence ledger uses the published numbering.
- The parity result changes training information across final-label,
  teacher-forced, and augmented-data regimes. It does not prove a separation
  after that information is equalized.
- Lyu and Zhu gives the Element Distinctness upper frontier and a matching lower
  bound for Set Intersection. It does not claim a matching Element
  Distinctness lower bound.

## Search outcome

Positive records or generic reductions resolve the 22 admitted formulations:

- one-way and interactive communication, data processing, and sparse
  distributed estimation;
- static and dynamic cell-probe, online attention, and multi-pass streaming;
- selective labels, adaptive inference, confounded or partially observed OPE,
  instruments, stationary OPE, performative prediction, switchbacks, causal
  discovery, best-intervention identification, causal-bandit regret,
  longitudinal mediation, and Bayes-adaptive control; and
- test-time training, test-time sampling, online experts, sparse retrieval,
  looped computation, lifelong feature acquisition, lifelong representation,
  online meta-learning, and bilevel optimization.

The result is `8 direct / 2 composite / 9 reduced / 3 out of scope / 2
unsupported`, with zero `DISTINCT_CANDIDATE` objects. The three out-of-scope
candidates are two recycled longitudinal write-effect objects and one relabeled
generic open lower-bound problem. C10 and C23 are retained as unsupported,
non-distinct admission failures; neither is counted as a known reduction.

M1e therefore proposes `STOP`. The search does not establish that no original
state-compute theorem can ever exist. It establishes that none of the 22
admitted candidates survives and neither of the two rejected sketches supplies
an admitted theorem object. No proof or experiment is currently authorized.
