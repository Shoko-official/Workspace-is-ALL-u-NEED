# Terra-Engineering feasibility, fairness, and reproducibility audit

Date: `2026-07-14`  
Issue: [#1](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/1)  
Milestone: `M0 - Audit and charter`  
Authoring functional role: `Terra-Engineering`  
Required independent reviewing role: `Sol-PI`, then `Luna-QA` before this can support a gate

## Objective

Audit whether the draft protocol can be executed fairly and reproducibly under the measured local environment. Quantify its implied matrix, expose hidden cost and leakage paths, separate M1/M2 blockers from M3+ blockers, and define a minimum viable M3/M4 sequence without implementing it.

## Scope and exclusions

The audit covers benchmark and oracle design, baseline comparability, resource matching, telemetry, run counts, compute and storage order of magnitude, OCI/environment readiness, registry and CI gaps, and stop rules. It does not authorize model or benchmark implementation, acquire datasets, import third-party code, or claim exact reproduction of any cited paper. Code availability does not constitute license approval.

## Inputs and versions

- `docs/research/CHARTER.md`, draft `0.1.0`, especially hypotheses, invariants, M4 gate, success thresholds, and refutation triggers.
- `docs/research/PROTOCOL.md`, `DRAFT_NOT_FROZEN` `0.1.0`, especially staged program, task families, baselines, controller sequence, endpoints, matching regimes, seeds, ablations, contamination controls, and manifest.
- `docs/research/RISK_REGISTER.md`, risks R-003, R-004, R-006 through R-009, and R-012.
- `docs/research/STATE.md`, snapshot `2026-07-14`.
- `experiments/registry.yaml`, schema `1`, empty experiment list.
- `scripts/validate_governance.py`, `tests/test_validate_governance.py`, and `.github/workflows/governance.yml`.
- Closest-primary-work updates supplied by Sol-PI and checked against the primary paper pages: Frey et al., arXiv `2603.08391` / OpenReview `F87X9c107e`; *Universal Transformers Need Memory*, arXiv `2604.21999v3`; HOLA `2607.02303`; Sparse Delta Memory `2607.07386`; Engram `2601.07372`; MemOS `2507.03724v4`; Larimar `2403.11901v4`; and MemLLM `2404.11672`.

## Recommended decision

`PIVOT` the protocol before M2 freeze. Permit M1 novelty review and M2 formalization, but do not authorize M3 yet. The current confirmatory program is under-specified and is not feasible on the sole recorded GPU.

The claim must not survive as a mere recombination claim. M2 must require an identical-component strong fixed composite, a factorial interaction test, and the charter's practical-effect threshold. `STOP` the joint-allocation contribution if the full joint controller does not beat the strong fixed composite, if the preregistered interaction confidence interval includes zero or is practically negligible, or if any purportedly essential component can be removed without a meaningful loss. A narrower component result may then be proposed only through a new claim and gate.

## Work completed and findings

### 1. Local capability was independently rechecked

The 2026-07-14 measurements remain current:

- Python `3.14.4`, `uv 0.11.19`;
- PyTorch `2.11.0+cpu`, `torch.cuda.is_available() == False`, no PyTorch CUDA runtime;
- RTX 5080, `16,303 MiB`, driver `595.97`, compute capability `12.0`;
- Docker client `29.5.3`, with no reachable Docker Desktop Linux daemon.

This is sufficient for governance and CPU oracle/generator work. It is not a reproducible GPU environment and is not evidence that 300M long-context training fits or that custom sparse/recurrent kernels support `sm_120`.

### 2. The protocol implies a larger matrix than its prose suggests

The coherent reading of the current protocol is eight standalone architecture baselines plus seven composite routing variants. The fixed and oracle variants satisfy required baselines 9 and 10, and the joint controller is one of the seven. Therefore:

| Matrix layer | Count | Interpretation |
|---|---:|---|
| Core confirmatory | `15 x 3 x 5 = 225` | systems/policies x sizes x seeds |
| Three resource-regime result cells | `225 x 3 = 675` | parameter, training-FLOP, and inference-resource comparisons; not necessarily distinct checkpoints |
| Minimum task-family cells | `675 x 6 = 4,050` | four WAIN-Core plus two natural families, before length and budget grids |
| Seven structural ablations at all sizes | `7 x 3 x 5 = 105` additional | excludes routing controls already counted |

The literal `10 baselines + joint` reading gives 165 core cells but violates the required controller sequence. Let `L` be length points and `K` inference-budget points. A full evaluation is at least `4,050 x L x K` result cells. Six required sweeps have no level counts, so the total is currently unbounded.

Pilot sizing is also incomplete: screening costs `3C` runs for an unspecified candidate count `C`; the variance pilot is fixed at 24 runs; M4 has seven policies but no seed rule. A defensible minimum M4 is 21 policy-seed cells at one small size, before factorial tests.

The baseline update changes scheduling materially. Frey is an additional mandatory composite. HOLA and SDM are credible target-scale executable threats after compatibility work. Adding those three raises the practical core to `18 x 3 x 5 = 270` cells and 810 resource-regime result cells. Treating Engram, MemOS, Larimar, and MemLLM as full matched training baselines would be scientifically mismatched and would raise the matrix without yielding a fair comparison; they should instead receive targeted subsystem tests.

### 3. Compute and storage are not locally schedulable

Illustrative assumptions, not measured performance: dense-equivalent training FLOPs `F = 6PT`, token budget `T = 20P`, and sustained effective throughput of 30 to 100 TFLOP/s. For the 15-system, three-size, five-seed core, the estimate is `1.035e21` FLOPs, or about 120 to 399 uninterrupted GPU-days. At 70 and 160 tokens per parameter it becomes `3.622e21` and `8.280e21` FLOPs, about 1.1 to 3.8 and 2.6 to 8.8 raw GPU-years. These figures exclude tuning, evaluation, retries, indexing, transfers, long-context inefficiency, and telemetry.

At `20P`, a 50M variance pilot with three systems and eight seeds is about `7.2e18` FLOPs, 20 to 67 idealized hours. A 50M screening candidate with three seeds is about `9e17` FLOPs, 2.5 to 8.3 idealized hours. Actual throughput must be benchmarked before budgeting.

For 15 systems, five seeds, and the three sizes, one retained snapshot represents 37.5 billion parameter-instances: about 75 GB as BF16 weights or 525 to 675 GB as 14 to 18 byte/parameter training checkpoints. Three retained training checkpoints require roughly 1.6 to 2.0 TB, already at or above the recorded 1.65 TB free space. Detailed action traces can add hundreds of GB or TB: 1,350 system-size-seed-family cells, 10,000 instances, and 100 actions per instance produce 1.35 billion action rows. At 64 to 256 compressed bytes per row this is about 86 to 346 GB, before budget sweeps. Synthetic examples should be regenerated from immutable manifests, and checkpoint retention and trace schemas must be capped before M5.

### 4. Closest baselines require tiers

| Work | What it threatens | Local status and matching cost |
|---|---|---|
| Frey et al. | Learned halting plus gated local/global memory, iso-parameter and iso-FLOP | Mandatory reduced-scale M4 composite. Its memory is learned and static at inference, not mutable episodic storage. About 200M/14B tokens implies `1.68e19` FLOPs, 1.9 to 6.5 idealized GPU-days for one run; no public implementation was located in the primary record, so exact reproduction also carries reimplementation risk. |
| Universal Transformers Need Memory | ACT depth/state trade-off, fixed-accuracy compute, seed instability | Strong, locally reproducible harness baseline: 3.2M parameters with public code. Count compute as `(sequence + memory tokens) x ponder steps`; ponder-step savings alone are insufficient. Test zero/positive/deep-start router initialization and retain stuck seeds. |
| HOLA | Compressed recurrent state plus bounded exact KV cache | Public code and 340M/15B scale. About `3.06e19` FLOPs, 3.5 to 11.8 idealized days for one run. Reduced-scale M4 is plausible after `sm_120` validation; full reproduction is not budgeted. Cache is within-context and heuristic-written, not persistent/versioned. |
| Sparse Delta Memory | Sparse explicit state, online reads/writes, iso-FLOP GDN | Public code; target-scale reduction is plausible only after custom-kernel validation. The smallest published ladder point, 257M/110.7B, is about `1.71e20` FLOPs, 20 to 66 idealized days. The 8B/1.141T result is concept-only locally. Learned initial state and sparse state capacity must be counted separately from activated parameters. |
| Engram | Static conditional lookup and activated-parameter accounting | Public code, but 27B/40B total, 3.8B activated, 262B tokens. One model is optimistically about `5.97e21` FLOPs and cannot fit 16 GB. Concept-only at published scale; use a downsized static-lookup ablation, not a claimed reproduction. |
| MemOS | Provenance, versioning, lifecycle, and system-level memory management | Public system code. Useful as an API/semantics comparator after Docker and service pinning, not as a parameter- or FLOP-matched neural baseline. Pin a paper-era commit because the product has evolved. |
| Larimar | Dynamic episodic memory, one-shot update and forgetting | Public code around pretrained 1.3B/6B decoders. The 1.3B inference path may be locally testable; exact training and 6B reproduction are not credible on 16 GB without offload/quantization that changes comparability. Use targeted temporal-memory tests. |
| MemLLM | Explicit structured read/write API | Public Mistral-7B LoRA implementation and large triple store. A reduced QLoRA/API test may fit, but a full matched reproduction is not comparable to scratch 50M-300M training. Use targeted read/write and mutation tests. |

Published-trend reproduction cannot be a universal prerequisite at original scale under the recorded budget. M2 must freeze tiers: full target-scale baseline, reduced-scale mechanism check, or concept-only novelty threat, with an approved replacement and no false reproduction claim.

### 5. Fairness and oracle design need stronger contracts

- Report total trainable, non-embedding, activated-per-token, controller, trainable-memory, recurrent-state, and persistent-store capacity separately. Excluding a learned memory table while counting ordinary weights is not parameter matching.
- Use the same ordered data/token stream, tokenizer, split, precision, optimizer policy, seed policy, and tuning-compute ceiling. Include tuning, failed runs, compilation, index build/maintenance, writes, retrieval, CPU/GPU transfer, verification, and retries.
- Inference matching needs both a per-instance hard ceiling and stratified mean, plus tail cost. Match on identical instances and randomized interleaved hardware runs. Publish cold-start and warm-cache results separately, with an explicit index-cost amortization lifetime.
- The oracle must emit a feasible action trace under the same budgets. A causal oracle may use generator annotations available at the decision point; a future-aware oracle must be labeled clairvoyant and cannot decide M4. Prove optimality by exhaustive search on small cases. A larger heuristic teacher must not be called an oracle.
- The strong composite must contain the same eligible workspace, episodic, state, recurrence, provenance, verification, and capacity operators as the proposal. Its fixed schedule is the intended difference.
- Run a `2 x 2 x 2 x 2` M4 factorial over episodic memory, compressed state, recurrence, and joint-versus-fixed routing, at one small size and at least three seeds, 48 cells. Pre-register the joint interaction contrast. Require the full joint system to meet the charter threshold against the strongest fixed composite and require the interaction's 95% interval to exclude zero with a practical threshold, suggested as at least 20% of the full-system gain. Otherwise `STOP` the joint-allocation claim.

The Joint Memory Machine is not yet construct-valid. A generator cannot merely label all components as required. It needs paired counterfactual instances where removing each information channel makes two visible states indistinguishable but changes the target. Episodic storage must be prevented, by schema and budget, from copying the compressed statistic or full workspace.

### 6. Main leakage paths

- seeds, event IDs, timestamps, source ordering, padding, lengths, difficulty labels, or mutation counts encoding the target;
- oracle actions, latent generator annotations, or answer-bearing provenance entering learner inputs, caches, checkpoints, or telemetry;
- global retrieval indexes crossing split or episode boundaries, or episodic state not reset when required;
- confirmatory generator code, manifests, canaries, or metrics accessible to model developers;
- random-action budgets matched from confirmatory behavior rather than frozen validation behavior;
- fixed depth selected from confirmatory mean adaptive depth;
- hypervolume reference points, interpolation bounds, non-inferiority margins, or baseline eligibility changed after result access;
- discarded router-collapse, OOM, timeout, or kernel-failure seeds;
- pretrained contamination in natural tasks.

### 7. Telemetry, registry, and CI are insufficient beyond M0

Every action trace needs run/instance/action IDs, monotonic step, typed arguments, pre/post state and budget counters, result/error/retry, causal provenance links, host and device timings, bytes transferred, allocation/peak memory, index operations, and halt probabilities. Universal-Transformer acceptance additionally logs per-step router probability, router-gradient norm, step-weight distribution, memory attention mass, token-steps, and initialization. Store compact counters for every instance; reserve expensive profiler traces for a frozen sample and measure telemetry overhead.

The current registry validator only regex-checks five top-level fields. Before `RUNNING`, a parsed schema must require unique experiment ID, issue/milestone/commit/PR, phase, protocol and frozen digest, authorization, hypothesis/endpoints, system and comparator, config/data/tokenizer hashes, seed, all parameter counts, resource regime, requested and actual budget vector, OCI digest, software and hardware, randomized order, commands, artifact URIs and hashes, failure class, deviations, and access records. Status-transition validation must reject mutation of frozen confirmatory fields.

Current CI checks file presence, Markdown headings, three CSV enums/duplicates, and the registry header. This is adequate only as a narrow M0 smoke test. M3 requires parsed schema tests, deterministic generator golden hashes, oracle differential/property tests, mutation-state-model tests, trace replay and budget conservation, split/canary/near-duplicate tests, offline evaluation tests, and an OCI build/smoke test. M4+ also needs a pinned GPU job for supported kernels and profiler-counter reconciliation. Pin CI actions by immutable commit for a reproducible supply chain.

## Minimum viable M3/M4 sequence

1. M2 freezes typed event/action schemas, oracle information sets, budgets, factorial contrast, baseline tiers, effect thresholds, failure handling, split custody, and registry schema.
2. Repair the environment with a pinned Python 3.12 CUDA-capable OCI image. Validate `nvidia-smi`, CUDA PyTorch, `sm_120`, deterministic modes, and selected custom kernels; record the image digest and run evaluation with network disabled.
3. Implement CPU-first deterministic Exact Recall and Temporal Episodic generators plus an event-sourced oracle. Add insert, supersede, revoke, expire, rollback, dependency invalidation, replay, and budget-conservation property tests.
4. Add Joint Memory Machine only after paired counterfactual necessity tests pass. Keep hidden confirmatory generators outside development code and build immutable hash manifests.
5. Implement trace-only write-none, write-all, random, fixed, causal-oracle, separated, and joint policy interfaces. Exhaustively validate oracle optimality on small instances.
6. Reproduce the 3.2M Universal-Transformer memory/ACT result as the first adaptive-depth harness test, including deep-start, default initialization, fixed-depth, all seeds, and token-step accounting.
7. At one 10M-50M size, three seeds, run the seven-policy M4 gate and the 16-cell factorial. Add reduced-scale Frey first; add HOLA/SDM only after kernel and budget acceptance. Do not start broad baseline training if the oracle or interaction gate fails.

## Concrete acceptance and stop tests

- Same seed, manifest, and OCI digest produces identical sample, oracle, and replay hashes; split canaries and exact hashes never cross families.
- Two independent oracle implementations agree on at least 10,000 randomized small cases; exhaustive search confirms the claimed oracle action cost on bounded cases.
- Replaying any trace exactly reconstructs state and output; no budget becomes negative; every mutation has one immutable provenance chain.
- Counterfactual pairs change only the intended channel and target. Removing episodic, state, recurrence, or provenance must not leave an alternate answer-bearing channel.
- Baseline parameter counts are within the frozen tolerance, suggested `1%`; training FLOPs within `1%`; inference compute within `2%`; otherwise compare Pareto curves rather than claim equality.
- Profiler FLOPs agree with analytic counters within `5%`; allocator/transfer counters within `10%`; repeated warm latency coefficient of variation is below `5%` or uncertainty is reported.
- ACT tests retain all initialization failures. Deep-start, default, and positive-bias pilots use equal tuning allowance; fixed-depth includes both maximum depth and validation-derived mean depth. Compute is token-steps plus measured physical cost.
- `STOP` at M3 for unresolved oracle disagreement, replay failure, split leakage, or inability to build an offline digest-pinned environment.
- `STOP` or claim-reduce at M4 if the causal oracle misses the charter's meaningful-effect threshold, requires unbounded resources, is dominated by a fixed policy, or if the factorial joint interaction is absent.
- `STOP` before M6 if power requires more seeds/instances than the written budget, natural families or licenses remain unfrozen, or storage/compute ceilings cannot retain the preregistered artifacts.

## Blockers by stage

### M1/M2 blockers

- The closest-work matrix must include the papers above and decide whether any discriminating property remains after the strong composite.
- Model/task mappings, tokens, tuning ceilings, length/budget grids, sweep levels, oracle information, interaction estimand, hypervolume reference, missing-run policy, and M4 threshold are unfrozen.
- Written compute, storage, data, and energy ceilings have no owner.
- Baseline tiers and published-trend tolerances are undefined. The missing underlying report blocks attribution, not the independent M1 review.

### M3 and later blockers

- CUDA PyTorch and the Docker daemon are unavailable; `sm_120` kernels are unvalidated.
- Code and dataset licenses are not approved, and no natural family is frozen.
- The registry cannot represent an authorized run and CI cannot validate a harness.
- Confirmatory target custody and an independent repository identity are absent.
- The sole 16 GB GPU, no cluster/cloud budget, no energy meter, and 1.65 TB free space cannot support the current confirmatory matrix. These do not block CPU M3 work after M2, but they block M5+ authorization.

## Evidence, assumptions, and uncertainties

The local commands above are direct evidence. FLOP/time/storage numbers are order-of-magnitude planning estimates using stated assumptions; no GPU throughput benchmark was run, and the estimates are optimistic. Evaluation instance counts, length grids, budget grids, sweep levels, checkpoint retention, and episodic record sizes are absent, so exact cost is not identifiable. Paper-scale cost estimates use `6PT`; sparse/conditional architectures need measured operation accounting before any claim.

## Files modified

- `docs/research/handoffs/2026-07-14-terra-engineering.md` only.

## Checks run

- Read all requested governance, protocol, state, risk, registry, validator, test, and workflow files.
- Rechecked Python, uv, PyTorch CUDA availability, GPU model/VRAM/driver/compute capability, and Docker daemon availability.
- Recomputed matrix, FLOP, elapsed-time, checkpoint, and trace orders of magnitude from explicit formulas.
- `python scripts/validate_governance.py`: passed.
- `python -m unittest discover -s tests -v`: 3 tests passed. These checks validate only the current narrow governance rules, not the scientific protocol.

## Next authorized action

Sol-PI should record `PIVOT` for the draft protocol, route this handoff to Luna-QA, and open a dedicated M1/M2 issue that freezes the strong composite, baseline tiers, `2^4` factorial interaction, oracle contract, complete matrix/budget, registry schema, and environment acceptance tests. No model or benchmark implementation should begin under issue #1.
