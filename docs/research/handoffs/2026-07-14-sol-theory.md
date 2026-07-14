# Sol-Theory contradictory formalization handoff

Status: `COMPLETE`

Recommended gate decision: `PIVOT`

Date: `2026-07-14`

Issue: `#1`

Handoff target: `Sol-PI`, issue `#1`

## Objective

Stress-test the Budgeted Workspace Model before M2 by giving its state, actions, budgets, mutations, failures, objectives, and costs semantics precise enough to implement and falsify. The decision is whether the current formulation can enter M2 unchanged, must be narrowed, or should stop.

## Scope

Included: the bounded active workspace, versioned episodic store, fixed-size compressed state, adaptive computation, verification, halting, per-instance inference budgets, training-objective choices, resource accounting, comparison policies, and decisive ablations.

Excluded: implementation, empirical results, a claim of novelty, advanced ACL/capability security, causal world models, model selection claims, and authorization for training. The missing underlying report on Transformer/LLM limitations is not reconstructed.

## Inputs and evidence inventory

| Input | Use | Evidence status |
|---|---|---|
| `docs/research/CHARTER.md` v0.1.0 | Scientific question, definitions, invariants, gates | Read in full; project-local normative input |
| `docs/research/PROTOCOL.md` v0.1.0 | Action set, baselines, endpoints, resource regimes, ablations | Read in full; draft, not frozen |
| `docs/research/STATE.md` snapshot 2026-07-14 | Authorization, blockers, missing report | Read in full; operational source of truth |
| Supplied `pasted-text.txt`, SHA-256 recorded in `STATE.md` | Original research-program context | Read in full; program text, not the underlying report |
| [HOLA, arXiv:2607.02303v1](https://arxiv.org/abs/2607.02303) | Fixed recurrent state plus bounded exact KV memory | Primary abstract read: already combines lossy recurrent state and bounded exact cache with residual-based writes |
| [MemOS, arXiv:2507.03724v4](https://arxiv.org/abs/2507.03724) | Provenance, versioning, scheduling, rollback | Primary abstract and HTML sections 4.3, 5.3.2, 5.3.3 read: MemCubes carry provenance/versioning; version chains and pipelines support rollback/transactional behavior |
| [Engram, arXiv:2601.07372v2](https://arxiv.org/abs/2601.07372) | Memory-versus-compute allocation | Primary abstract read: static conditional memory is allocated against neural compute under fixed parameter/FLOP regimes |
| [Frey et al., OpenReview F87X9c107e](https://openreview.net/forum?id=F87X9c107e) | Memory plus adaptive loops | Primary abstract read: gated local/global memory and per-layer adaptive loops with learned halting already coexist |
| [Universal Transformers Need Memory, arXiv:2604.21999v3](https://arxiv.org/abs/2604.21999) | Depth-state substitution | Primary abstract read: memory-token count and ponder depth substitute under halt pressure at fixed accuracy |

These sources are novelty threats, not a completed novelty review. They rule out treating “memory plus recurrence,” “memory versus compute,” provenance/versioning alone, or adaptive loops plus memory as the contribution. They do not establish that the narrowed formulation below is novel.

## Work performed

1. Replaced the informal state tuple with typed, bounded transition semantics.
2. Separated enforceable per-instance inference limits from global training budgets and ex-post physical measurements.
3. Defined append-only version/provenance invariants and distinguished transaction abort, compensating rollback, and experiment retry.
4. Derived time, space, and I/O bounds with the assumptions needed for any near-linear statement.
5. Constructed controls that isolate joint coordination from extra parameters, supervision, component capacity, and oracle leakage.
6. Searched for countermodels in which the headline is false or not identifiable.

## Formal candidate for M2

### Indices, boundaries, and base types

Let `t = 1..T` index externally supplied events or token blocks in one episode and `j = 0..H_a-1` index controller microsteps for event `t`. `H_a` is a configured hard maximum independent of `T`. Unless a benchmark explicitly declares cross-episode persistence, `W`, `S`, and `E` are initialized from a frozen manifest for every example; allowing memory to leak between evaluation examples is forbidden.

Required finite types include `Bytes[p_max]`, `SlotId < K_W`, `RecordId`, `EventId`, `LogicalKey`, `SchemaId`, `SourceId`, `SourceLocator`, `SourceVersion`, `CommitTime`, `ValidTime`, and bounded lists `Vec[X, n_max]`. Numeric precision for `W` and `S` is part of the configuration. A fixed real-vector dimension without fixed precision is not a meaningful information bound.

The model-visible state is

\[
M_{t,j}=(W_{t,j},E_{t,j},S_{t,j},B_{t,j}).
\]

The append-only audit trace `L_{t,j}` is runtime state, not model-visible memory. The complete operational state is `(M_{t,j}, L_{t,j})`.

### Active workspace `W`

\[
W=(Z,m,r),\quad Z\in\mathbb F^{K_W\times d_W},\quad
m\in\{0,1\}^{K_W},\quad r\in\text{Ref}^{K_W}.
\]

`Z` holds exactly `K_W` dense slots, `m` is the occupancy mask, and `r` binds occupied slots to an input span, state projection, retrieved record, verifier result, or prior workspace slot. `K_W`, `d_W`, and numeric precision are fixed for a declared model. Slot replacement is explicit in the action arguments and is traced; silent growth or an unbounded KV cache violates the definition.

### Episodic store `E`

`E = (G, I, V)` consists of an append-only authoritative event log `G`, a rebuildable retrieval index `I`, and a materialized snapshot view `V`. The index is never the source of truth.

```text
Provenance := {
  source_id, source_locator, source_version,
  valid_time, ingest_time, asserted_confidence,
  permission_snapshot_digest,
  dependencies: Vec[RecordId, D_max]
}

ContentRecord := {
  record_id, logical_key, record_version, parent_record?,
  schema_id, payload: Bytes[p_max], provenance,
  expires_at?, binding_hash
}

MemoryEvent :=
  PUT(ContentRecord)
  | SUPERSEDE(new_record, expected_head)
  | REVOKE(target_record, mutation_provenance)
  | EXPIRE(target_record, scheduler_event)
  | ROLLBACK(target_event, restored_record, mutation_provenance)
```

`record_version`, `source_version`, model/config version, and commit sequence are distinct fields. Temporal queries specify both `valid_as_of` and `known_as_of`; omitting either creates bitemporal leakage ambiguity. `resolve(E,key,valid_as_of,known_as_of)` folds committed events in commit order and returns only records visible at that snapshot.

### Compressed state `S`

\[
S=(s,q),\quad s\in\mathbb F^{d_S},\quad q\in Q_{\mathrm{finite}}.
\]

`d_S`, precision, and any finite control state `q` are fixed. `CONSOLIDATE` is the only policy action that commits a learned update `s' = F_\theta(s,W,mask)`. In the minimal identifiable design, `PONDER` may read `S` but updates `W` only. If `PONDER` also updates `S`, recurrence and consolidation are not separable and that alternative must be preregistered as a different architecture.

### Budget state `B`

\[
B=(\ell,u,\rho),\qquad 0\le u_r\le \ell_r,
\]

where `ell` is the vector of per-instance limits, `u` is monotonically increasing actual usage, and `rho` reserves enough budget for one `HALT`, trace flush, and output validation. At minimum, enforceable integer/resource axes are controller actions, `PONDER` steps, retrieval calls, index probes, returned records, logical writes, payload bytes read/written, transfer bytes, workspace slots, and persistent bytes. FLOPs can be enforced when kernels have declared upper bounds. HBM can be allocator-capped.

Wall-clock latency and energy are not exactly reservable before an irregular operation. They are timeout/metered axes: a watchdog can terminate after a ceiling, but overshoot and energy are observed ex post. Therefore M2 must distinguish `HARD_ENFORCED`, `WATCHDOG_CAPPED`, and `MEASURED_ONLY`; it must not call all physical axes hard constraints.

Training data/FLOPs are global experiment budgets `B_train`, enforced by the scheduler and manifest. They are not part of the per-instance Markov state and must not be mixed with `B` in equations.

For action `a`, let `c_hat(a,M)` be a conservative reservable upper bound and `c(a,M)` the measured usage. The feasible set is

\[
\mathcal A(M)=\{a:\operatorname{pre}(a,M)\land
u+\widehat c(a,M)+\rho\le\ell\}\cup\{\texttt{HALT}\}.
\]

Failed attempts consume their actual compute and I/O and never receive a budget refund. Controller evaluation, action masking, index maintenance, failed actions, trace writes, compilation/warm-up under the declared policy, and CPU-GPU transfers are charged.

### Joint policy `pi_phi`

The controller has no direct scan access to `E`; it observes the bounded tuple

\[
o_{t,j}=O(W_{t,j},S_{t,j},\ell-u,x_t,\text{bounded retrieval metadata}).
\]

It samples or chooses a typed action and arguments only from the feasible set:

\[
(a_{t,j},\eta_{t,j})\sim\pi_\phi(\cdot\mid o_{t,j}),\qquad
(M',L')=\mathcal T(M,L,a,\eta,x_t,\xi).
\]

The policy is “joint” only if one trainable policy can condition each resource decision on the shared remaining-budget vector and cross-resource state. A shared policy name is insufficient; the separated baseline below fixes the comparison.

### Typed action semantics

| Action and bounded arguments | Preconditions | Atomic success effect |
|---|---|---|
| `PROMOTE(source_ref, dest_slots <= K_promote)` | Source visible; destinations valid | Encode/copy selected input or state projection into named `W` slots |
| `RETRIEVE(query_slots, top_k <= K_ret, probe_cap, byte_cap, snapshot, dest_slots)` | Snapshot valid; read/probe/byte budget available | Query `I`, validate candidates against `G/V`, then atomically materialize only visible records and their immutable references into `W` |
| `APPEND(key, payload_slots, provenance_ref, expected_absent_or_head, expires_at?)` | Payload bounded; provenance originates from authenticated input/retrieved metadata; compare-and-swap succeeds | Append `PUT`, commit record and index delta |
| `SUPERSEDE(key, expected_head, payload_slots, provenance_ref, expires_at?)` | Expected head is current and visible | Append a new child record plus `SUPERSEDE`; prior bytes remain intact |
| `REVOKE(target_record, reason_ref, expected_head?)` | Target committed and not already inactive | Append `REVOKE`; never delete or rewrite target content |
| `CONSOLIDATE(slot_mask)` | State-update and compute budget available | Commit one `F_theta(S,W)` update to `S`; `W/E` unchanged |
| `PONDER(step_tag)` | Ponder count below `H_ponder` | Apply one recurrent `G_theta(W,S)` update to `W`; `S/E` unchanged in the minimal design |
| `VERIFY(claim_slots, evidence_refs, verifier_id)` | Frozen verifier accessible; no target/test-label access | Put a typed verification result in `W`; verifier cost is charged |
| `HALT(answer_slots, citation_refs, confidence)` | Always feasible through reserved budget | Validate visible citations, emit output/status, flush trace, terminate |

Expiration is a deterministic store transition triggered by declared `expires_at`, not a learned policy decision. A committed temporal rollback is a privileged/environmental store event, not currently in `pi_phi`'s declared action set. If the paper intends the controller to choose expiration or rollback, `EXPIRE` and `ROLLBACK` must be added to the action algebra and baselines. Leaving them simultaneously claimed but absent is an M2 blocker.

If the hard action maximum is reached without `HALT`, the runtime emits `BUDGET_EXHAUSTED`; it must not grant a free final reasoning step. The preregistration must decide whether this counts as incorrect output or abstention before evaluation.

## Provenance and version invariants

1. `record_id` and `(logical_key, record_version)` are unique. Per-key versions are monotonically ordered at the commit linearization point; gaps are allowed after aborted reservations.
2. Every parent and dependency references an earlier committed record. This makes lineage acyclic and bounds validation by `D_max` per event.
3. `binding_hash = H(canonical(schema_id, payload_bytes, logical_key, record_version, parent, provenance))`. The original bytes and schema are retained; a hash alone is not lossless storage.
4. Payload, provenance, parent, and version never mutate after commit. A correction creates a new record/event. Retrieval returns `record_id`, payload hash, provenance hash, and snapshot coordinates together.
5. Provenance integrity is not provenance truth. Source identity and confidence are assertions unless independently authenticated. The controller may select an available provenance object but may not fabricate source locators or event times.
6. `permission_snapshot_digest` records the write-time policy. A separately versioned current authorization policy is checked at read time; otherwise immutable old permissions could grant stale access. Full ACL semantics remain out of scope.
7. Revocation, expiration, dependency invalidation, and rollback change visibility through appended lifecycle events. They do not detach or replace content provenance.
8. A rollback to an older value appends `ROLLBACK` and makes a prior immutable `ContentRecord` visible as the restored value. The rollback event has its own mutation provenance; it does not rebind the restored payload to new content provenance.
9. Every action, failure, candidate filter, visibility decision, halt, state/config version, pre/post state digest, reservation, and measured cost is logged. Sensitive payloads may be represented by digests in the audit log, but exact bytes remain in the governed store.

## Failure, atomicity, recovery, and rollback

Action execution returns `Success(delta,cost)` or `Failure(code,cost)` with at least `BUDGET_REJECTED`, `INVALID_ARGUMENT`, `PRECONDITION_FAILED`, `CONFLICT`, `NOT_FOUND`, `PERMISSION_DENIED`, `IO_ERROR`, `INDEX_ERROR`, `TIMEOUT`, and `NUMERIC_ERROR`.

- A state-changing action stages all changes and has one commit marker. Before that marker, failure leaves `W/E/S` unchanged. `B` usage and the trace still advance.
- `RETRIEVE` validates index candidates against the authoritative snapshot before committing workspace slots. A stale index may reduce recall under the probe cap but may not expose a revoked, future, expired, or unauthorized record.
- If data append succeeds but index update fails before commit, the record is invisible; recovery rebuilds the index from committed log events. No partial index result is authoritative.
- Transaction abort reverts an uncommitted action. Logical rollback of an already committed mutation is the append-only compensating event defined above. These are distinct operations and must not share one metric.
- Runtime/process crashes classify the experiment run as failed. A deterministic replay from the immutable initial manifest may be a separately logged retry; the failed run remains in analysis. Restoring arbitrary in-memory `W/S/B` from an unlogged checkpoint is forbidden.
- Repeated failures cannot bypass budgets: retries count toward action, compute, latency, read/write, and I/O limits.

## Training-objective options, not results

All options retain hard action masks; a soft penalty never substitutes for feasibility.

1. **Budget-conditioned constrained objective**

   \[
   \min_{\theta,\phi}\;\mathbb E_{z,b\sim P_B}
   [L_{task}+\alpha_pL_{prov}+\alpha_vL_{version}+\lambda^\top \widetilde C]
   \quad\text{s.t. }C_r(z)\le b_r\;\forall r\in R_{hard}.
   \]

   `P_B`, all loss weights, and dual updates are frozen on pilot/validation data. Weighted sums may miss non-convex Pareto regions, so evaluation still reports full fronts.

2. **Oracle imitation then constrained policy optimization.** Supervise action schedules using generator dependency annotations, then fine-tune with policy gradient/actor-critic for task quality and cost. Oracle annotations, their generation cost, and extra training FLOPs must be given equally to eligible controller baselines or reported as a separate supervision regime.

3. **Discrete policy optimization from scratch.** REINFORCE/actor-critic avoids a differentiable action fiction but may have high variance and collapse. Report every seed and action distribution.

4. **Differentiable relaxation.** Straight-through or Gumbel-style gates can be a pilot option, but train-time soft mixtures differ from hard inference actions and may pay for every branch. Charge actual branch compute and validate the train/inference gap.

Direct optimization of confirmatory hypervolume is not recommended: it entangles training with the frozen evaluation reference point and invites endpoint overfitting. Auxiliary retrieval/write/version/provenance losses are diagnostic treatments, not free supervision; ablate them and match training compute.

## Complexity derivation

Let `K=K_W`, `d=d_W`, `s=d_S`, `h=H_a`, `r` be maximum retrieval actions per input event, `w` maximum memory mutations, `k` returned records, `q` index probes, `N_t` committed memory records, and `p_r/p_w` logical payload bytes read/written. Let one dense workspace block cost

\[
C_W(K,d)=\Theta(K^2d+Kd^2),
\]

and let `C_pi`, `C_S`, and `C_V` denote declared controller, state-update, and verifier costs. With index query cost `Q(N_t,q,k)` and update cost `J(N_t)`, a conservative online bound is

\[
C_{online}\in O\!\left(
T C_{enc}+T h(C_\pi+C_W+C_S+C_V)
+\sum_{t=1}^{T}[rQ(N_t,q,k)+wJ(N_t)]
\right).
\]

For a bounded-probe approximate index, `Q = O(q d_e + k log k)` only if `q`, embedding dimension, and candidate materialization are hard-capped; retrieval quality may then degrade with `N`. Exact scan is `Theta(N_t d_e)`. A balanced-tree-like lookup gives `O(log N_t)` rather than constant time. Full or periodic index rebuilds can make total maintenance quadratic unless moved off-path and still accounted.

Total resident plus persistent space is

\[
\Theta(P_\theta+Kd+s+k p_r)
+\Theta\!\left(N_T(d_e+m_{meta})+\sum_{i=1}^{N_T}|payload_i|\right)
+\Theta(T h m_{trace}).
\]

Thus `W` and `S` are fixed-size, but episodic content, its index, and the mandatory trace grow with committed events. With `N_T <= T w` and bounded payloads, they are `O(T)`, not `O(1)`.

Logical episode I/O satisfies

\[
bytes_{read}\le T r(q\,page_{index}+k p_r),\qquad
bytes_{write}\le T w p_w+bytes_{WAL}+bytes_{index}+bytes_{trace}.
\]

Physical I/O can exceed these bounds through write amplification, compaction, cache misses, retries, and transfer duplication. Those terms require measurement or an explicitly bounded storage engine.

A near-linear-in-`T` claim is permitted only if `K,d,s,h,r,w,k,q,p_r,p_w`, verifier work, and amortized index maintenance remain independent of `T`, and if external storage/index/trace costs are reported separately. If `Q=O(log N)`, the honest bound is `O(T log T)`; if expected ponder depth grows with length, expected linearity also fails. Tail depth, not only the mean, must be reported.

Training through `h` recurrent steps multiplies forward/backward compute by up to `h` and activation memory by up to `h` absent recomputation/checkpointing. Discrete routing estimator overhead is part of training FLOPs.

## Minimal comparison that can identify the candidate delta

Every row uses identical data, tokenizer, backbone/component implementations, capacities, feasible action set, hard budgets, evaluation instances, tuning allocation, and physical accounting. Controller parameters and controller FLOPs are counted; report both component-matched and total-parameter-matched views.

| Policy | Allowed information and training | Purpose / prohibition |
|---|---|---|
| Minimal oracle router | Generator dependency graph, mutation necessity, and required reasoning depth; same actions/budgets/components | Upper bound on routing only. It may not read the answer, inject payloads, bypass retrieval, relax budgets, or select unavailable evidence. Report oracle decision cost separately and never call it a fair learned baseline. |
| Strong fixed composite | Same components; validation-selected, instance-independent schedule and thresholds; no latent difficulty labels | Tests whether adaptivity is needed. Include fixed depth at joint model mean compute and strongest schedule under the same tuning budget. |
| Separated controllers | Resource-family heads for workspace, episodic I/O, state update, and ponder/verify/halt, independently trained with no cross-resource gradients; fixed preregistered arbiter; same total controller capacity | Tests whether joint optimization adds value. The arbiter may not be a learned coordinator in disguise. Also compare the same multi-head architecture with stop-gradient/local observations. |
| Joint controller | One policy with cross-resource observations, shared remaining budget, and joint objective | Candidate treatment. It wins only against the strongest eligible fixed and separated controls after complete matching. |

“Separated” and “joint” are otherwise label-equivalent: an expressive arbiter can implement any joint policy, while a single nominal controller can factor into independent heads. M2 must freeze observation interfaces, gradient paths, parameter counts, arbiter logic, and resource prices.

To identify a coordination interaction rather than a rhetorical assembly, add a matched 2x2 factorial controller study:

- `O=0/1`: local-only versus cross-resource observations and remaining budgets;
- `G=0/1`: resource-local versus joint gradient/objective coupling.

For preregistered Pareto hypervolume `HV`, estimate

\[
I_{coord}=(HV_{O=1,G=1}-HV_{O=1,G=0})
-(HV_{O=0,G=1}-HV_{O=0,G=0}).
\]

Random assignment of training seeds/configurations and paired evaluation on the same instances makes this a causal architecture intervention within the declared design. A nonzero `I_coord` is still not a general causal mechanism claim; it is evidence of interaction in these tasks and budgets.

## Decisive ablations and stop interpretations

| Ablation/intervention | Confound controlled | Decisive interpretation |
|---|---|---|
| Remove `E`; compensate parameters and matched compute | Extra capacity | No meaningful loss: remove episodic memory from the claim |
| Read-only prefilled `E` versus online mutable `E` | Retrieval versus mutation | No incremental effect: persistent mutation is unsupported |
| Latest-value KV store versus version/event store at matched bytes/I/O | Plain retrieval versus temporal semantics | No EP2/provenance gain: versioning is ornamental |
| Remove `S`, then compensate `W` bytes or recurrent compute separately | State capacity substitution | No robust loss: compressed state is not necessary |
| Remove `PONDER`; fixed depth at mean and matched quantiles | Adaptive depth versus more compute | No frontier gain: learned depth unsupported |
| Joint versus matched separated controllers and the 2x2 interaction above | Joint training/cross-resource information | No joint advantage or `I_coord` compatible with zero: no joint-allocation contribution |
| Blind controller to remaining budget; swap resource-price/budget vectors at evaluation | Budget conditioning versus generic routing | Allocation does not respond correctly: “budgeted controller” is unsupported |
| Remove `VERIFY`; matched extra ponder step | Verification versus compute | No correctness/unsupported-claim gain: verification is redundant |
| Payload held constant; independently permute source, date, confidence order, availability, and provenance pointer | Provenance causality | Provenance-dependent targets unchanged: remove provenance from the primary claim |
| Exact/oracle retrieval versus approximate retrieval under same store | Storage/version semantics versus retriever quality | Gains only with oracle retrieval: practical architecture claim fails |
| Fault injection before/after prepare, log append, index update, commit, and trace flush | Transactional semantics | Any partial visibility, provenance detachment, or non-replayable state: STOP temporal-memory claim |
| Component-action saturation and instance-label permutation | Degenerate/write-all policies or synthetic leakage | Joint policy reduces to fixed/read-all/write-all, or survives label permutation: claim is false or benchmark leaks |

## Ways the headline can be false or non-identifiable

1. **Fixed-dimensional is not necessarily compressed.** With unconstrained precision, a fixed real vector can injectively encode any finite benchmark history. Conversely, a sufficiently large `W` or `E` can emulate `S`. Capacity in bits, noise/precision, and matched compensating ablations are required before attributing a benefit to architectural roles.
2. **Joint versus separated is undefined without interfaces.** Independent heads plus a learned arbiter can reproduce a joint policy; a “joint” network can factorize. Without the frozen 2x2 intervention and matched arbiter, a gain is attributable to parameters, information access, or training, not joint allocation.
3. **The broad memory-compute hypothesis is anticipated.** HOLA, Engram, adaptive-loop-plus-memory work, and the Universal-Transformer depth/state study already cover neighboring combinations or trade-offs. Merely assembling them or renaming the scheduler is not a contribution.
4. **Pareto hypervolume is reference- and scale-dependent.** “Improves at least one frontier” can be manufactured by endpoint/reference selection or unit scaling. Directions, normalization, reference points, strongest-baseline selection, and multiplicity family must be frozen.
5. **Exact storage does not identify useful memory.** Output gains may come entirely from the retriever, extra bytes, or privileged metadata. Exact payload retention says nothing about retrieval accuracy, temporal resolution, or downstream use.
6. **Synthetic necessity can be tautological or leaked.** A generator that exposes mutation type, difficulty, or oracle action labels can make routing easy; a task constructed to require all components cannot establish natural necessity. Hidden family-level splits and counterfactual target changes are required.
7. **Controller overhead and supervision can explain the gain.** Extra controller parameters, oracle imitation labels, tuning trials, or training FLOPs can move the frontier without any coordination effect.
8. **The policy may be degenerate.** Write-all/read-all, fixed-depth, always-verify, or budget-saturating behavior can match a learned router. Entropy alone does not exclude functional degeneracy.
9. **Physical budgets may reverse theoretical savings.** Index maintenance, random I/O, device transfers, trace/WAL writes, irregular kernels, and failed actions can erase FLOP savings. A logical action bound is not a latency or energy bound.
10. **Persistence creates a leakage fork.** Resetting `E` every example weakens “persistent” memory; sharing it across examples can contaminate evaluation. Episode, user, split, and reset boundaries must be frozen.

The headline is directly falsified if the leak-free minimal oracle cannot improve a practically relevant matched frontier, if the joint controller does not beat the strongest fixed/separated composite, if the coordination interaction is absent, or if mutable episodic semantics add no effect beyond a latest-value store.

## Uncertainties and required M2 resolutions

- The underlying limitations report is `INPUT_MISSING`; claims attributed to it remain unaudited.
- M1 has not established novelty of the narrowed controller. The sources above materially narrow it.
- `EXPIRE` and committed `ROLLBACK` are claimed behaviors but absent from the declared policy action set.
- The persistence boundary, concurrency model, payload schema, current-policy check, index/backend, verifier definition, numeric precision, and per-axis limits are not frozen.
- A practically feasible exact physical-cost matrix is unknown because the compute/data budget and CUDA-capable environment are unresolved in `STATE.md`.
- The strongest separated-controller interface and the hypervolume reference point are not yet preregistered.

## Recommended decision

`PIVOT`, confidence `HIGH` for the formalization decision.

Do not enter M2 with the broad claim that a model allocates “memory versus compute,” combines memory with adaptive recurrence, or adds versioning/provenance. Those ideas are already directly threatened by primary antecedents and are not identifiable in the current protocol.

The only candidate worth formalizing is narrower:

> Under hard per-instance action, recurrent-step, episodic-I/O, byte, and transfer ceilings, and under matched controller capacity, training compute, and physical accounting, does one non-factorizing policy coordinating a bounded workspace, online mutable versioned episodic I/O, fixed-size compressed state, verification, and halting improve a preregistered quality-cost frontier over the same strong composite with fixed routing and with independently trained resource controllers?

This is a hypothesis, not a novelty or performance claim. M2 receives a conditional `GO` only if M1 finds that this exact delta is not already disclosed and the protocol adopts the causal coordination factorial or a demonstrably new, discriminating phenomenon/benchmark against the strong composite. If the proposed contribution is only a rhetorical recombination of prior mechanisms, if no causal interaction is identifiable, or if no new discriminating phenomenon survives the composite, the decision must be `STOP`, not paper reframing.

## Files modified

- `docs/research/handoffs/2026-07-14-sol-theory.md` only.

## Verification

- Read all required local inputs and the supplied 889-line request context.
- Checked the five named novelty threats against their primary arXiv/OpenReview pages; no novelty conclusion was inferred from them.
- Audited the formalization against every required charter invariant, all nine policy actions, hard-budget failure paths, rollback semantics, comparison controls, and complexity assumptions.
- Confirmed the handoff contains no empirical result and no assertion of novelty.
- Repository diff/status checks are recorded after file creation.

## Next action

Sol-PI should use this handoff to narrow issue #1, require Terra-Evidence to test the exact narrowed delta, and make the M0/M1 gate explicit. If that gate permits continuation, open a dedicated M2 issue to freeze: typed schemas, `EXPIRE/ROLLBACK` ownership, persistence boundaries, the hard-versus-measured budget taxonomy, the four-policy comparison, the 2x2 coordination interaction, decisive ablations, and stop rules before implementation.
