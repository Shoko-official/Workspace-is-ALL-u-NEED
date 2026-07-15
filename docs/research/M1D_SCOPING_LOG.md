# M1d Scoping and Resolution Log

Cutoff: `2026-07-15`
Method: targeted mechanism discovery, exact-record resolution, and generic-object reduction
Status: `COMPLETE_FOR_DECISION_NOT_SYSTEMATIC`

## Scope

M1d searched specifically for an object outside M1c that couples governed
persistent state and adaptive computation without reducing to a joint router,
value of computation, POMDP, causal path effect, estimator, cache, scheduler,
database, proof-carrying system, or ordinary optimization problem.

Three read-only lanes worked independently on formal identification and bounds,
learning dynamics, and runtime mechanisms. Each lane returned eight candidates
and zero survivors. The log is not a systematic-review flow diagram. It preserves
the queries and positive records that determine the decision and makes no
novelty claim from search silence.

## Recorded discovery queries

Executed on `2026-07-15` against the web index and resolved to primary records:

```text
site:arxiv.org LLM agent persistent memory adaptive test-time compute self-reinforcement feedback loop
site:arxiv.org LLM agent memory write selection bias adaptive compute reasoning
site:arxiv.org rational metareasoning persistent memory value of computation agent
site:arxiv.org LLM reusable reasoning cache proof-carrying memory computation
site:arxiv.org "memory" "test-time compute" LLM agent 2025 2026
site:arxiv.org "persistent" "adaptive computation" language model agent
site:arxiv.org "value of computation" memory planning agent metareasoning
site:arxiv.org LLM agent memory "verification" adaptive compute
site:arxiv.org LLM agent memory consolidation compute budget adaptive 2025
site:arxiv.org LLM agent "memory consolidation" reasoning compute
site:arxiv.org "reasoning memory" adaptive computation language agents
site:arxiv.org "memory-conditioned" test-time compute LLM
BudgetMem ICML 2026 arXiv 2602.06025 runtime memory compute router
CRAM arXiv 2602.12204 consolidation routing theorem memory LLM
TriggerBench prospective memory reasoning spare capacity LLM
ReasoningBank MaTTS arXiv 2509.25140 memory test-time scaling
arXiv 2604.21018 persistent pool compute allocation language model
MemoPilot deferred credit memory writes LLM agent
site:arxiv.org/abs/2607 LLM agent memory adaptive compute
site:arxiv.org/abs/2607 persistent memory reasoning agent compute
site:arxiv.org/abs/2607 memory-aware test-time scaling LLM
site:arxiv.org/abs/2607 stateful LLM agent memory
"anytime-valid" confidence sequence adaptive stopping commit verification
adaptive doubly robust off-policy evaluation sequential data collection
longitudinal interventional indirect effect stochastic mediator
machine unlearning space recomputation tradeoff ticketed unlearning
adaptive submodularity partial realization computation acquisition
online convex optimization predictions switching costs dynamic regret
proof-carrying data incremental verification computation
LLM state transition verifier persistent memory commit
LLM interrupted inference preserve swap recompute KV state
semantic cache scheduling persistent agent memory compute
```

## Exact primary-record resolutions

| Evidence | Record | Decision locator |
|---|---|---|
| `EV-0086` | Anytime-valid confidence sequences | abstract; Section 1.1 Equation 4; Section 1.2 |
| `EV-0087`; `EV-0088` | Dynamic value of computation and metareasoning | thesis Section 2.4 and Definition 10; PMLR Definition 3 and VoC equation |
| `EV-0089` | Adaptive doubly robust policy evaluation | Section 4 estimator; Theorems 1-2 |
| `EV-0090` | Longitudinal stochastic mediation | Equation 1; assumptions A1-A2; Theorem 1 and Proposition 1 |
| `EV-0091`; `EV-0092` | Ticketed and agentic unlearning | formal deletion guarantee and space tradeoff; agentic dependency closure |
| `EV-0093` | Adaptive submodularity | Definitions 2-3; Equations 10-11; Theorem 5 |
| `EV-0094` | Online optimization with predictions and switching costs | objective Equation 1; dynamic regret Equation 2; lookahead upper and lower bounds |
| `EV-0095` | ReasoningBank/MaTTS | Sections 3.3 and 4.4; memory-quality by scaling ablation |
| `EV-0096` | MemoPilot | Section 3.1 multi-turn memory-update decision problem and turn-wise credit |
| `EV-0097` | AdaMEM | Sections 3.1-3.2 and compute-level evaluation |
| `EV-0098` | Adaptive compute with evolving demonstrations | Algorithm 1; adaptive allocation and evolving successful-response pool |
| `EV-0099` | Useful Memories Become Faulty | abstract; Section 4.1; non-monotone consolidation utility and episodic control |
| `EV-0100` | TrustMem | Sections 3.1-3.4 and 4.5-4.6; same-state candidate transitions and verifier |
| `EV-0101` | TriggerBench | Sections 4.2, 4.4, 5, and 6; Appendix C.3 Table 16; reasoning load, overload, PM behavior, and one-constraint upstream control |
| `EV-0102` | BudgetMem | Sections 4.1-4.3 and Appendix A.4; low/mid/high module tiers and state-conditioned router |
| `EV-0103` | CRAM | Sections 4.2-4.4; Equations 6-8; Section 5.1 Theorem 1 |
| `EV-0104` | INFERCEPT | Sections 3.2 and 4.1-4.4; preserve, swap, discard, and recompute scheduler |
| `EV-0105` | Preble | introduction; Section 2.4; Section 3.2; joint colocated state-compute scheduling |
| `EV-0106` | SAVeR | Sections 3.1-3.5; belief-state audit and repair before action commitment |
| `EV-0107`; `EV-0108` | TrACE and MemRouter | adaptive agreement; memory routing and admission control |
| `EV-0109`; `EV-0110` | MemDecay and Pancake | semantic decay and multi-tier memory placement |
| `EV-0111` | A-MAC | Section 3.2 Equation 1; future utility in memory admission |
| `EV-0112`; `EV-0113` | Proof-carrying and incrementally verifiable computation | proof-carrying safety contract; incremental verification construction |
| `EV-0114` | POMDPs | belief-state reduction and information-gathering actions |
| `EV-0115` | Sporadic Server | schedulability analysis for periodic and aperiodic hard-deadline tasks |

Existing `EV-0041`, `EV-0053`, `EV-0073`, `EV-0076`, and `EV-0078` were also
reused for agent-memory cost characterization, rational metareasoning, shared-
state rerollouts, contamination feedback, and dependency-aware change
propagation.

## Resolution notes

- The recent 2026 records are pinned to the inspected version. They are public
  disclosures, not automatically treated as peer-reviewed empirical truth.
- ReasoningBank is accepted to ICLR 2026 and its current arXiv version is used.
  Its key role is a positive collision: it explicitly evaluates bidirectional
  memory-quality by test-time scaling effects.
- BudgetMem, AdaMEM, and ReasoningBank supply positive records at different
  levels: per-module runtime tiers, dynamic in-episode memory refresh, and
  cross-task memory-aware experience scaling. Exact threshold, causal, and
  factorial candidates are not attributed to any one paper.
- CRAM is used for its disclosed consolidation-conditioned routing mechanism.
  The M1d decision does not rely on its numerical results or stated lower bound;
  its unresolved macro and anonymized artifact are retained as reliability
  limitations.
- TriggerBench directly supports the primary-task-to-prospective-memory
  opportunity cost. Appendix C.3 Table 16 reports that one inserted constraint
  leaves upstream AIME accuracy within standalone variation; intention load is
  not varied, so M1d claims neither a positive reverse impairment nor a general
  no-effect result.
- INFERCEPT and Preble concern runtime KV and prefix state rather than semantic
  long-term memory. They are valid reconstruction threats for the specific
  continuation and residence candidates, not evidence about all persistent
  memory.
- Several formal candidates remain empirically testable. They are rejected
  because their estimands or guarantees are known generic objects, not because
  no exact LLM experiment was found.
- No result count, screening total, snowball closure, or exhaustive-coverage
  claim is made.

## Search outcome

The search found positive records or reconstruction threats at every relevant
layer:

- agent learning: ReasoningBank, MemoPilot, AdaMEM, TrustMem, Memory-R2, and
  adaptive evolving demonstrations;
- model dynamics: CRAM;
- runtime state and compute: BudgetMem, INFERCEPT, and Preble;
- failure regimes: Useful Memories and TriggerBench; and
- generic theory: dynamic value of computation, POMDPs, adaptive DR,
  longitudinal mediation, adaptive submodularity, online optimization, and
  proof-carrying computation;
- real-time scheduling: the primary Sporadic Server report.

The formal observation is independent of search coverage: at fixed history and
with unrestricted information passage, every behavioral joint state-compute
distribution admits the conditional factorization recorded in the candidate
register. A future behavioral separation claim must therefore justify a
restricted information, communication, computation, or learning class before
observing results. This observation does not decide causal, complexity, or
learning equivalence. No M1d candidate states the matched class and result it
would need, and none supplies a new law, estimator, invariant, bound, or theorem
after the positive and conditional reductions.
