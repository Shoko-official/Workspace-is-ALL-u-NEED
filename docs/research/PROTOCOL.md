# Experimental Protocol

Status: `DRAFT_NOT_FROZEN`
Version: `0.1.0`
Recorded: `2026-07-14`
Implementation authorization: `NONE`

This document defines the protocol that must be completed and independently reviewed before confirmatory work. Pilot results may refine a later frozen version, but pilot data must never be pooled with confirmatory results.

## State and actions

The minimum model state is `M_t = (W_t, E_t, S_t, B_t)`:

- `W_t`: bounded dense active workspace;
- `E_t`: versioned episodic store with payload, immutable provenance, confidence, permissions, and dependencies;
- `S_t`: fixed-dimensional compressed recurrent or state-space state;
- `B_t`: declared limits and current consumption for compute, latency, memory, reads, writes, transfers, storage, and energy where measurable.

The controller `pi_phi` may select `PROMOTE`, `RETRIEVE`, `APPEND`, `SUPERSEDE`, `REVOKE`, `CONSOLIDATE`, `PONDER`, `VERIFY`, or `HALT`. Every action must have a typed schema, bounded cardinality, explicit failure behavior, and trace record.

## Staged program

1. **M1, novelty:** execute the registered search and issue a contradictory novelty opinion.
2. **M2, formalization:** freeze equations, invariants, complexity assumptions, hypotheses, endpoints, baselines, ablations, statistics, meaningful-effect thresholds, and stop rules.
3. **M3, harness:** implement deterministic generators, executable oracles, leak controls, and baseline reproductions.
4. **M4, oracle bound:** compare oracle, fixed, random, write-all, write-none, heuristic, separated controllers, then the joint controller.
5. **M5, pilot:** screen 10M-50M parameter configurations, estimate variance and power, and diagnose degenerate policies.
6. **M6, confirmatory:** run the frozen 50M, 150M, and 300M matrix with independent seeds and hidden tests.
7. **M7, transfer:** evaluate at least two natural-task families without test tuning; scale to 1B-3B only after prior gates pass.
8. **M8, replication:** rebuild at least one main table, one main figure, one ablation, and one hardware profile from a clean installation and raw traces.
9. **M9, manuscript:** generate LaTeX, verified BibTeX, tables, figures, limitations, negative results, and artifact documentation without submitting or releasing automatically.

## WAIN-Core task families

### Exact Recall

MQAR-style retrieval with close keys, arbitrary values, multiple queries, repeated keys, controlled distractors, and exact-copy targets. The oracle returns both target value and source event.

### Temporal Episodic Memory

Event streams contain insert, update, supersede, delete, expire, rollback, temporal-version queries, conflicting sources, and dependency invalidation. The oracle is an executable event-sourced reference implementation.

### Adaptive Algorithms

Pointer chasing, stack execution, graph traversal, function composition, addition, and multiplication vary independently in input length and required reasoning depth. Difficulty labels must come from the generator or oracle, not model loss.

### Joint Memory Machine

Every accepted instance must require episodic retrieval, compressed-state use, recurrent computation, and provenance output. Counterfactual checks must establish that removing any required information changes the oracle target.

## Independent variables

Sequence length, episode count, reasoning depth, distractor count, key distance, mutation rate, workspace capacity, compressed-state size, episodic capacity, retrieval top-k, read budget, write budget, recurrent-step budget, and source-conflict rate.

Train, validation, pilot-test, and confirmatory-test distributions must be separated by generator family or composition rule where possible, not only by seed. OOD lengths and compositions are absent from training.

## External transfer

Candidate external families are Zoology/MQAR, RULER, BABILong, NoLiMa, a natural long-context corpus, a temporal-memory benchmark, and code or algorithmic tasks with executable oracles. Dataset versions, licenses, contamination risks, and evaluation compatibility must be approved before acquisition. At least two natural families must be frozen before confirmatory execution.

## Required baselines

1. dense Transformer;
2. local or sliding-window attention Transformer;
3. Mamba-2 or a comparable selective SSM;
4. attention-SSM hybrid;
5. Recurrent Memory Transformer;
6. Memorizing Transformer or comparable kNN memory;
7. comparable Titans or ATLAS configuration;
8. Universal Transformer with ACT or PonderNet-style computation;
9. strong fixed composite containing all eligible components;
10. oracle router.

A baseline may be marked infeasible only with a recorded compatibility, license, or resource analysis and an approved replacement. Published trends must be reproduced within a preregistered tolerance before comparative claims are allowed.

## Controller sequence

Evaluate in this order:

1. write-none and read-none;
2. write-all and read-all within hard limits;
3. random policy with matched expected actions;
4. fixed heuristic policy;
5. oracle policy;
6. separately trained per-resource controllers;
7. joint controller.

The M4 gate is evaluated before optimizing a complex learned router.

## Primary endpoints

- **EP1:** normalized area under accuracy versus `log2(sequence length)` over a frozen grid. Interpolation and normalization bounds must be fixed before confirmatory runs.
- **EP2:** joint exact match of payload, requested temporal version, and mutation status.
- **EP3:** quality at equal mean inference compute and compute at non-inferior quality, reported as Pareto curves rather than a single matched point.
- **EP4:** answer correctness, source exact match, citation precision/recall, and unsupported-claim rate.
- **EP5:** end-to-end p50/p95 latency, peak HBM, bytes moved, energy, and throughput, including compilation and warm-up policy.
- **EP6:** performance on at least two frozen natural-task families without test-set tuning.

The preferred global criterion is Pareto-hypervolume improvement with a hierarchical 95% confidence interval excluding zero. Reference points and metric directions must be frozen before confirmatory evaluation.

## Diagnostic metrics

Recall@k, read precision/recall, write precision/recall, write amplification, regrettable eviction rate, retention of unmodified facts, OOD degradation slope, selected depth, halt calibration, router entropy, action saturation, index construction/query cost, transfer bytes, persistent-storage growth, and between-seed variance.

## Resource-matching regimes

Publish three separate comparisons:

1. parameter-matched;
2. training-data and training-FLOP-matched;
3. inference-budget-matched.

Inference accounting includes model execution, index construction and maintenance, episodic writes, retrieval, CPU-GPU transfer, persistent storage I/O, compilation, warm-up, verification, and failed or retried actions. No report may state that parameters, FLOPs, memory, latency, and energy are all equal unless each equality is separately demonstrated.

## Seeds, pilot, and confirmatory runs

- Screening pilot: three independent seeds per candidate.
- Variance pilot: eight seeds for the proposed model and the two closest baselines.
- Confirmatory default: five independent seeds per architecture-size cell, replaceable only by a documented power analysis.
- Model sizes: 50M, 150M, and 300M non-embedding parameters, with counting rules frozen in M2.
- Confirmatory run order is randomized and all failed runs are retained with failure classifications.

Pilot instances, checkpoints, and metrics are excluded from confirmatory estimates.

## Statistical policy

1. Determine instance counts and any seed-count deviation with simulation-based power analysis using the pilot variance model and a preregistered smallest effect of interest.
2. Use hierarchical bootstrap sampling seeds, generator families, and instances at their actual sampling levels.
3. Report 95% confidence intervals, effect sizes, distributions, and every seed.
4. Model length effects with a mixed regression containing architecture, `log(length)`, and their interaction, plus preregistered random effects.
5. Use non-inferiority tests for quality-preserving cost reductions.
6. Apply Holm correction across primary endpoint families. Benjamini-Hochberg is restricted to labeled exploratory analyses.
7. Never use an LLM judge as the only metric for a primary endpoint.

The estimand, bootstrap unit, missing-run handling, non-inferiority margin, hypervolume reference point, and multiplicity family must be explicit in the frozen protocol.

## Required ablations and interventions

- without episodic memory;
- without compressed state;
- without recurrence;
- fixed depth equal to measured mean adaptive depth;
- without learned halting;
- without provenance;
- permuted provenance;
- write-all, write-none, random, fixed, separated, and oracle routing;
- workspace-size, state-size, top-k, episodic-capacity, read-budget, and write-budget sweeps;
- separately trained versus jointly trained components.

Provenance interventions independently alter source identity, date, source availability, confidence ordering for conflicting sources, and the provenance pointer while holding payload constant. Failure on explicitly provenance-dependent targets removes provenance from the primary contribution.

## Contamination controls

- train from scratch where pretrained contamination would invalidate the endpoint;
- hash every shard and generated manifest;
- exact deduplication plus MinHash or a documented stronger near-duplicate method;
- family-level generator separation;
- confirmatory generators hidden from model-development code paths;
- unique split canaries and automatic canary checks;
- no network access during evaluation;
- immutable test manifests and access logs.

## Reproducibility manifest

Every experiment record must identify issue, milestone, commit or PR, hypothesis, data-manifest hashes, generator version, tokenizer, configuration, seeds, model parameter count, environment or OCI digest, CUDA/compiler/library/driver versions, hardware, raw trace location, checkpoint location, metric implementation version, and result report.

Each table and figure must have one command that rebuilds it from immutable raw traces without private intermediate files. Mermaid remains the diagram source and is exported to SVG or PDF for LaTeX.

## Deviations and freezing

Any protocol change receives a timestamped decision record, rationale, affected endpoints, and classification as pre-pilot, post-pilot, or post-confirmatory-access. The confirmatory protocol is frozen before anyone with model-development responsibility can inspect confirmatory targets or results.

No experiment may be added to `experiments/registry.yaml` as `RUNNING` until its issue, manifest, configuration, budget, and authorization gate are all present.
