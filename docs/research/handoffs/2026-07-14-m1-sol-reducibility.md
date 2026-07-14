# M1 Sol-Theory reducibility audit

Status: `COMPLETE`

Mechanism-route verdict: `STOP`

Residual route: `EMPIRICAL PIVOT ONLY, NOT YET JUSTIFIED`

Date: `2026-07-14`

Issue: `#3`

Handoff target: `Sol-PI`, issue `#3`, milestone `M1`

## Decision in one sentence

The proposed contribution, one constrained policy that jointly chooses memory input/output, compressed-state updates, recurrence, verification, and halting, is behaviorally reducible to a budgeted constrained POMDP with a disjoint-union action space, and its supposedly non-factorizing policy is exactly equivalent to an arbiter plus conditional action heads; therefore it is not a new technical object or mechanism.

## Scope and burden of proof

This audit tests only the narrowed M1 claim left open after M0:

> A single non-factorizing constrained policy jointly coordinates memory input/output, compressed state, recurrence, verification, and halting under a vector resource budget.

It does not test whether the full proposed system would be useful, whether a particular neural parameterization would train well, or whether a complete-accounting benchmark could expose a new empirical phenomenon. Those are different questions. In particular, universal representability, trainability, sample efficiency, optimization stability, and algorithmic novelty must not be conflated.

The audit used the current `CHARTER.md`, `PROTOCOL.md`, `NOVELTY.md`, `STATE.md`, decision record 0002, the M0 Sol-Theory handoff, and primary literature. It did not infer novelty from the absence of an identical product diagram or identical action names.

## 1. Canonical formalization

### 1.1 Controlled process

Let the complete operational state at controller step `t` be

\[
z_t=(W_t,E_t,S_t,b_t,L_t,x_t,q_t),
\]

where `W` is the bounded active workspace, `E` is the versioned episodic store, `S` is fixed-capacity recurrent or compressed state, `b` is remaining resource, `L` is the audit or transaction state, `x` is the current external input, and `q` contains bounded control state. The policy observes

\[
o_t=O(z_t),
\]

which may omit the contents of `E` except for bounded retrieval results and metadata.

Let `K` index operation classes. The typed action space is the measurable disjoint union

\[
\mathcal A=\bigsqcup_{k\in K}\{k\}\times U_k,
\]

with

\[
K=\{\texttt{PROMOTE},\texttt{RETRIEVE},\texttt{APPEND},
\texttt{SUPERSEDE},\texttt{REVOKE},\texttt{CONSOLIDATE},
\texttt{PONDER},\texttt{VERIFY},\texttt{HALT}\}.
\]

`U_k` is the bounded argument space for operation `k`. A transition kernel

\[
P(dz_{t+1}\mid z_t,k_t,u_t)
\]

contains both learned and non-learned state changes. Version checks, provenance requirements, transaction commit rules, and rollback semantics are transition preconditions or invariants. They do not require a new control formalism.

Each transition incurs a non-negative resource vector

\[
c(z_t,k_t,u_t,z_{t+1})\in\mathbb R_+^d.
\]

For reservable resources, pathwise feasibility is enforced by

\[
b_{t+1}=b_t-c_t,\qquad
\mathcal A(z_t,b_t)=\{(k,u):\widehat c(z_t,k,u)\le b_t-r\}
\cup\{\texttt{HALT}\},
\]

where `r` reserves termination and trace-flush cost. The objective may be written as expected terminal utility, discounted return, or a vector-constrained objective. A scalar price such as `lambda^T c` is an optimization device, not a substitute for the pathwise feasibility mask.

This is a constrained Markov decision process when `z_t` is observed. With the project-specified bounded observation `o_t`, it is a constrained POMDP. Markovizing the observation history yields a belief-state constrained MDP. Adding the remaining budget to the state gives the standard budgeted MDP form, abbreviated BMDP here in the sense used by Carrara et al. Variable-duration retrieval, verification, and tool calls produce an SMDP, or equivalently an MDP whose temporally extended actions are options.

### 1.2 What the reduction does and does not claim

The reduction is semantic. It establishes that the proposed behavior belongs to an existing control class. It does not establish that every finite neural implementation has equal parameter count, equal optimization geometry, or equal sample efficiency. A particular shared network can be a useful inductive bias. That could support an empirical or algorithmic result, but the shared network itself does not create a new decision process.

The distinction is decisive:

| Question | Result of this audit |
|---|---|
| Can a generic CMDP/BMDP or constrained POMDP represent the proposed controller? | Yes |
| Can an arbiter plus conditional heads represent the same stochastic policy? | Yes, exactly |
| Must arbitrary finite neural implementations have the same size or train equally well? | No |
| Has a new learning algorithm, guarantee, invariant, or complexity separation been specified? | No |
| Does the current mechanism therefore clear the novelty gate? | No |

## 2. Exact policy decomposition

### Proposition 1: disjoint-union decomposition

Let `H` be the policy's history or sufficient information state. For any stochastic joint policy

\[
\pi(k,u\mid h),\qquad (k,u)\in\mathcal A,
\]

define the operation arbiter

\[
\rho(k\mid h)=\int_{U_k}\pi(k,du\mid h)
\]

and, whenever `rho(k|h) > 0`, the conditional operation head

\[
q_k(du\mid h)=\frac{\pi(k,du\mid h)}{\rho(k\mid h)}.
\]

When `rho(k|h) = 0`, `q_k` may be arbitrary because operation `k` is never selected. Then

\[
\pi(k,du\mid h)=\rho(k\mid h)q_k(du\mid h).
\]

For finite actions this is elementary marginalization and conditioning. For the project's continuous and typed argument spaces, the same factorization follows from regular conditional distributions on standard Borel spaces.

### Proof consequence

Every proposed single joint policy is behaviorally identical to:

1. an arbiter that selects the operation class; and
2. one conditional controller per operation class that selects its arguments.

Conversely, any such arbiter-plus-heads composition defines a joint policy by multiplication. The feasible-action mask and vector budget can be shared by both representations without changing the induced trajectory distribution.

The same conclusion survives common attempts to avoid it:

- If several actions are emitted simultaneously, the joint distribution factorizes autoregressively by the probability chain rule.
- If actions run for variable durations, each action is an option with an initiation set, internal policy, and termination rule.
- If action classes share a neural trunk, that is parameter sharing inside the same factorization.
- If the controller uses recurrent hidden state, augmenting `h` or the belief state preserves the factorization.
- If writes are transactional or version-checked, the validity conditions enter the action mask and transition kernel.

### Corollary 1: “non-factorizing” is not a behavioral invariant

Whether a controller appears factorized changes when the action ontology is relabeled. Splitting one operation into subtypes, merging two operation labels, or serializing a vector action can change the apparent factorization without changing any input-output behavior or trajectory probability. A contribution that depends on this labeling choice is not an invariant technical object.

### Corollary 2: one network versus several heads is an implementation comparison

A finite architecture may make one parameterization cheaper or easier to optimize than another. This is an inductive-bias, capacity-allocation, or credit-assignment claim. It requires capacity-matched learning curves, not a claim that the joint policy class is new. A shared trunk with an operation arbiter and typed heads can preserve all cross-resource information while retaining the exact decomposition above.

## 3. Reduction to existing control objects

### Proposition 2: budget and state augmentation

For every reservable resource axis, append remaining budget `b_t` to the state and mask any action whose conservative upper-bound cost exceeds the remainder after the termination reserve. This converts a pathwise resource ceiling into ordinary state-dependent feasibility. Multiple budget axes merely make `b_t` a vector.

This is stronger operationally than a CMDP that constrains only expected cumulative cost, but it is not a new policy object. It is a standard state augmentation. Carrara et al. explicitly condition the policy on a running budget and make budget evolution part of the transition. Altman's CMDP treatment already covers multiple objectives and inequality constraints.

For stochastic latency or energy that cannot be upper-bounded before dispatch, the system can use a chance constraint, watchdog, or ex-post metering. Calling such axes hard pathwise constraints would be false, but their uncertainty still does not create a new architecture.

### Proposition 3: mutable memory and verification

`APPEND`, `SUPERSEDE`, `REVOKE`, and `CONSOLIDATE` are controlled state transitions. `RETRIEVE` and `VERIFY` are observations or tool options with costs and stochastic outputs. `PONDER` is an internal computation action. `HALT` is a terminal action. Therefore their union remains an ordinary action space in a CMDP/BMDP, constrained POMDP, or SMDP.

The semantic richness of a versioned store matters for correctness and benchmarking. It does not by itself change the mathematical class of the controller.

## 4. Adversarial countermodels

### Countermodel A: apparent joint advantage is only information access

There are two feasible operations, `RETRIEVE` and `PONDER`, and one unit of budget. A query bit `g` determines which operation returns reward one. A joint controller observing `g` succeeds with probability one. Two resource-local heads that do not observe `g` cannot.

An arbiter that observes `g` and selects the matching head also succeeds with probability one. The gap is caused by cross-resource observation access, not an irreducible joint policy.

### Countermodel B: action relabeling destroys “non-factorization”

Start with a policy over labels `RETRIEVE` and `VERIFY`. Replace them with one label `TOOL` and an argument `tool_type`. The identical trajectory distribution now looks factorized in a different place. Alternatively, split `RETRIEVE` into `LEXICAL_RETRIEVE` and `DENSE_RETRIEVE`; the same behavior acquires more heads. No scientific property changed.

### Countermodel C: global budget arbitration reproduces coordination

Give each resource-local controller its preferred action and marginal value estimate. A global arbiter, dual-price scheduler, or dynamic program selects the feasible proposal under the shared vector budget. If the arbiter sees the same history as the alleged joint policy, its conditional heads can reproduce that policy exactly by Proposition 1. A baseline that forbids the arbiter from seeing global state is a deliberately information-restricted baseline.

### Countermodel D: transaction semantics remain environment semantics

A `SUPERSEDE` option performs read-head, compare-version, append-new-record, update-index, and commit-or-abort. The option's internal policy and termination state reproduce the full operation in an SMDP. Provenance and linearizability can be valuable system properties, but their presence does not make the policy class new.

## 5. The proposed 2x2 observation-by-gradient experiment

Let `O=0` mean resource-local observations and budgets, `O=1` mean cross-resource observations and budgets, `G=0` mean resource-local objectives or gradient paths, and `G=1` mean a jointly coupled end-to-end objective and gradient path.

| Cell | Formal interpretation | What a gain can identify | What it cannot establish |
|---|---|---|---|
| `O0 G0` | Restricted product or decentralized policy plus a fixed feasibility arbiter | Baseline performance under both restrictions | Natural lower bound for all factorized implementations |
| `O1 G0` | Globally conditioned arbiter and heads trained with local losses | Value of cross-resource information and global budget state | Novelty of a joint policy |
| `O0 G1` | Shared or end-to-end objective with local observations | Value of shared representation or credit assignment | Information-level coordination |
| `O1 G1` | Centralized CMDP/BMDP or belief-state policy | Combined effect of information and training coupling | A new computational object |

For a declared endpoint `J`, the interaction contrast

\[
\Delta_{O\times G}=(J_{11}-J_{10})-(J_{01}-J_{00})
\]

tests whether the two interventions are superadditive under the frozen model, task distribution, optimizer, and resource regime. It does not test non-reducibility. Even a large, replicated interaction can arise from optimization geometry, shared feature learning, finite network capacity, hyperparameter asymmetry, or a benchmark that makes the global cue unusually easy to exploit.

The design is interpretable only if all cells share the same action support, hard-budget feasibility layer, terminal reserve, base-model capacity, training data, update count, search budget, and oracle access. The `G0` definition must not silently change the reward function, and the `O0` cells still need an identical safety arbiter to enforce the shared budget. Otherwise the factors do not isolate observation and gradient coupling.

UMA already reports the generic direction of this empirical result: its Section 4.4 prose and Table 1 both place unified end-to-end training above the decoupled two-stage variant, although they conflict on the exact unified aggregate value. The proposed factorial design is cleaner, but “joint end-to-end training beats a separated pipeline” is already directly anticipated. This audit does not rely on the disputed magnitude.

## 6. Primary-source anticipation map

The closest anticipation is composite but nearly exact:

1. UMA supplies a single policy over compact summary state, a mutable key-value memory bank with CRUD-like actions, retrieval and tool recurrence, and a terminal answer action. It also directly compares unified and decoupled training.
2. GRU-Mem supplies an explicitly recurrent memory agent with learned update and exit gates, plus dedicated rewards for updating and terminating.
3. A resource vector and pathwise mask are generic CMDP/BMDP machinery, while Gaikwad explicitly formalizes cost-sensitive store selection without evaluating a learned router.

No cited source needs to contain the project's exact list of operation names. The reducibility result means that adding the remaining operation labels is action-space composition, not a new control formalism.

| Candidate element | Primary anticipation and exact locator | Effect on novelty claim |
|---|---|---|
| Budget-conditioned control | [Carrara et al., *Budgeted Reinforcement Learning in Continuous State Space*, NeurIPS 2019](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html), Section 1, PDF page 2; Definition 1 and Theorem 1 in Section 2, PDF pages 2-3 | Budget is a policy input and evolves in the dynamics; the candidate vector is an extension, not a new object |
| Multiple constrained objectives | [Altman, *Constrained Markov Decision Processes*, 1999](https://www-sop.inria.fr/members/Eitan.Altman/mdp1.html), Chapters 2-4 | Foundational CMDP treatment includes multiple objectives, inequality constraints, occupation measures, and linear programs |
| Neural CMDP optimization | [Achiam et al., *Constrained Policy Optimization*, ICML 2017](https://proceedings.mlr.press/v70/achiam17a.html), Section 4, PDF page 2 | Neural policy learning under auxiliary cost constraints is established; it does not itself provide pathwise ceilings |
| Variable-duration operations | [Sutton, Precup, and Singh, *Between MDPs and Semi-MDPs*, 1999](https://www.ece.uvic.ca/~bctill/papers/learning/Sutton_etal_1999.pdf), abstract and Section 2, PDF pages 1-2 and 6-7 | Retrieval, verification, and multi-step tools are options in an SMDP |
| Single policy, compressed core, mutable external memory, retrieval, recurrence, terminal answer | [Zhang et al., *Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning* (UMA), arXiv:2602.18493v1](https://arxiv.org/pdf/2602.18493), Sections 2.1-2.3, PDF pages 2-4 | Near-direct anticipation of the proposed control topology |
| Unified memory action policy with tool and context costs | [Yu et al., *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents* (AgeMem), arXiv:2601.01885v2](https://arxiv.org/pdf/2601.01885), Section 3.1 and Table 1, PDF pages 4-5 | One policy already selects `ADD`, `UPDATE`, `DELETE`, `RETRIEVE`, `SUMMARY`, and `FILTER` with terminal and cost rewards |
| Recurrent update and learned halt | [Sheng et al., *When to Memorize and When to Stop: Gated Recurrent Memory for Long-Context Reasoning* (GRU-Mem), arXiv:2602.10560v1](https://arxiv.org/pdf/2602.10560), Sections 3.1-3.2.1, PDF pages 4-6 | Closes most of the recurrence, state-update, and exit portion of the proposed combination |
| Memory update as an MDP | [Cai et al., *From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory* (MemoPilot), arXiv:2606.08656v1](https://arxiv.org/pdf/2606.08656), Section 3.1, PDF page 3 | Explicitly formulates memory updates as state, action, transition, and cumulative reward |
| Cost-sensitive routing across memory stores | [Gaikwad, *Did You Check the Right Pocket?*, arXiv:2603.15658v1](https://arxiv.org/pdf/2603.15658), Sections 3.1-3.4, PDF pages 2-3 | Formalizes selection among four stores with expected accuracy minus access cost; experiments compare oracle, heuristic, and fixed policies, not learned routing |
| Learned compute and halting | [Graves, *Adaptive Computation Time*, arXiv:1603.08983](https://arxiv.org/pdf/1603.08983), Section 2, PDF pages 2-5; [Banino et al., *PonderNet*, arXiv:2107.05407](https://arxiv.org/pdf/2107.05407), Sections 2.2-2.5, PDF pages 2-4 | Internal compute, ponder cost, stochastic halting, and hard maximum steps are established components |
| External read/write memory plus recurrent controller state | [Graves et al., *Neural Turing Machines*, arXiv:1410.5401v2](https://arxiv.org/pdf/1410.5401), Section 3, PDF pages 5-10; [Graves et al., *Hybrid computing using a neural network with dynamic external memory*, Nature 2016](https://www.nature.com/articles/nature20101), abstract and Figure 1 | Selective external reads and writes coordinated with internal recurrent state are established |
| Learned routing of compute or function blocks | [Rosenbaum et al., *Routing Networks*, ICLR 2018](https://arxiv.org/abs/1711.01239), abstract and Section 2; [Wu et al., *BlockDrop*, CVPR 2018](https://openaccess.thecvf.com/content_cvpr_2018/html/Wu_BlockDrop_Dynamic_Inference_CVPR_2018_paper.html), Section 3.2, PDF pages 3-4 | A learned router and conditional compute policy are established abstractions |
| Computations treated as costly actions | [Russell and Wefald, *Principles of Metareasoning*, Artificial Intelligence 1991](https://www.sciencedirect.com/science/article/pii/000437029190015C), pages 361-395; [Callaway et al., *Learning to Select Computations*, arXiv:1711.06892](https://arxiv.org/abs/1711.06892), abstract and Section 2 | Choosing internal computation and termination under cost is a metareasoning problem |
| Retrieval plus self-critique or verification in one LM | [Asai et al., *Self-RAG*, ICLR 2024](https://openreview.net/forum?id=hSyW5go0v8), Section 3 and Algorithm 1, PDF pages 3-5 | On-demand retrieval, critique of evidence, generation, and utility scoring already coexist |
| Versioning, provenance, scheduling, transaction and rollback semantics | [Li et al., *MemOS*, arXiv:2507.03724v4](https://arxiv.org/abs/2507.03724v4), MemCube discussion on PDF pages 13-16, APIs and transactions on page 19, scheduling on page 20, lifecycle and rollback on page 21 | These semantics are strong system requirements, but are not unique to the candidate controller |
| Learned supersession and stale-memory pressure | [Patel, *Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents*, arXiv:2606.27472v1](https://arxiv.org/pdf/2606.27472), Section 3, PDF pages 3-4, and Section 5.3, PDF pages 7-8 | Temporal update behavior is already an active direct research target; current evidence remains early |

Several 2026 items are recent preprints or conference submissions. They are used here as direct novelty threats, not as proof that their empirical conclusions are settled. The formal CMDP/BMDP and policy-decomposition results do not depend on those empirical conclusions.

## 7. Conditions that could establish non-reducibility or a distinct contribution

The current artifacts satisfy none of the following conditions.

### 7.1 Representation-theoretic condition

Define a behavioral invariant that survives action relabeling, splitting, merging, and serialization, then prove that the candidate realizes trajectories that no CMDP/BMDP policy or arbiter-plus-heads construction can realize under matched information. The exact decomposition above makes this route implausible for the current object.

### 7.2 Complexity-separation condition

Prove a lower bound under a precisely restricted comparator class: the candidate solves a family with asymptotically lower parameters, memory, computation, communication, sample complexity, or regret than every arbiter-plus-heads controller with the same observations and resources. Finite-network optimization differences on a benchmark do not constitute this proof.

### 7.3 New algorithm and guarantee condition

Specify an algorithm that materially exceeds generic CMDP methods, for example a policy-learning method that guarantees pathwise feasibility for a stochastic multi-resource vector while also proving a non-trivial regret, violation, or convergence bound. A feasibility mask plus an off-the-shelf optimizer does not meet this condition.

### 7.4 New semantic invariant condition

Prove a transactional, provenance, or temporal noninterference property enforced by the learned controller and its transition protocol, not merely supplied by the storage API. The property must be formal, falsifiable, and stronger than existing versioned-memory behavior.

### 7.5 New empirical law condition

Discover a stable, predictive, architecture-agnostic law or phase boundary for allocation among memory input/output, compressed state, recurrence, and verification. It must replicate across task families, base architectures, seeds, resource prices, hard ceilings, and at least two hardware regimes. A positive average accuracy delta is not such a law.

## 8. Residual empirical route

The mechanism route is stopped. A separate empirical paper could still become eligible, but only if it is justified independently of the “one non-factorizing policy” claim.

An acceptable empirical pivot would need at least one outcome-changing result:

1. **Complete-accounting ranking reversal.** Under matched training, inference, memory, I/O, transfer, latency, and energy accounting, accepted architecture rankings reverse by a practically material amount and the reversal replicates.
2. **Predictive allocation law.** Exogenous price or ceiling interventions reveal a stable elasticity, threshold, or phase transition that predicts when memory traffic, compressed state, recurrent compute, or verification should dominate.
3. **Architecture-agnostic temporal-memory benchmark.** Causal supersession, provenance, rollback, and stale-evidence interventions expose failures across strong systems, and the benchmark remains informative even when the proposed controller loses.

The following are insufficient by themselves:

- one joint network outperforming a deliberately separated pipeline;
- adding more CRUD, verification, or halt labels to a generic action union;
- implementing a fixed transactional store;
- reporting a larger set of resource metrics without changing any conclusion;
- outperforming weak fixed-budget or information-restricted baselines;
- a non-zero `O x G` interaction on one synthetic benchmark.

UMA already raises the bar for unified-versus-decoupled comparisons. Supersede raises it for temporal updates. MemOS raises it for provenance, versioning, transactions, and scheduling. The residual route therefore needs a pre-registered practical threshold, strong same-component controls, exogenous budget interventions, and replication, not another architectural recombination claim.

## 9. Strict gate decision

### Mechanism route: `STOP`

The action union plus vector cost is a generic CMDP/BMDP construction. Partial observability gives a constrained belief-state formulation. Variable-duration actions give options or an SMDP. The “non-factorizing” policy is exactly equivalent to an arbiter plus conditional heads and is not invariant to action labeling. UMA plus GRU-Mem provides near-exact composite anticipation, while AgeMem and cost-sensitive memory routing further narrow the gap.

No new algorithm, theorem, invariant, lower bound, or guaranteed learning procedure is currently specified. The proposed 2x2 experiment can study information access and credit assignment, but it cannot rescue the mechanism as a new technical object.

### Empirical route: `PIVOT`, conditional

Retain only a separately motivated complete-accounting, predictive-law, or temporal-memory benchmark route. If M1 cannot pre-register an outcome-changing phenomenon of the kind listed in Section 8, the correct overall decision is `STOP`, not a paper whose contribution is a more comprehensive recombination.

## 10. Claims safe to carry forward

Safe:

- The candidate is a useful systems specification for studying joint resource allocation.
- Pathwise resource feasibility is operationally stronger than an expected-cost constraint and must be implemented explicitly.
- Observation access and gradient coupling are distinct empirical factors worth isolating if the empirical route proceeds.
- Complete resource accounting and causal temporal-memory interventions may support an independent contribution if they change conclusions.

Unsafe:

- The single joint policy is a new control object.
- “Non-factorizing” establishes representational novelty.
- Joint-versus-separated gains prove irreducible coordination.
- The exact combination of known action labels is sufficient novelty.
- Versioning, provenance, verification, or halting becomes novel merely because one policy selects it.
