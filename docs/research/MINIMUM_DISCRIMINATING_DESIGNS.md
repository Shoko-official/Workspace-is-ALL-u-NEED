# Minimum Discriminating Designs for the M1b Audit

Status: `DESIGN_ONLY_NOT_AUTHORIZED`
Issue: `#5`

## Purpose

These designs test whether the candidate predictions are falsifiable. They do not establish novelty, authorize experiments, or make the stopped transition framework article-eligible. Counts are lower-bound execution units, not a funding request.

All designs require paired instances, frozen prompts and adapters, independently generated ground truth, exact model and system versions, complete lifecycle accounting, and family-level held-out evaluation. Model/API prices, energy, and wall-clock estimates are `NON DISPONIBLE` until eligible systems and deployment modes are fixed.

## Shared accounting

For each cell, record:

- input, output, reasoning, retrieval, and maintenance tokens separately;
- model and non-model FLOPs where measurable;
- p50 and p95 end-to-end latency and throughput;
- peak volatile memory, persistent bytes, bytes moved, reads, and writes;
- construction, update, invalidation, recovery, and teardown work;
- energy only from a declared meter, never inferred from nominal TDP;
- contract pass or violation with confidence intervals and every abstention.

The minimum call estimate is

`N = implementation_families * policies * workload_cells * seeds * instances_per_cell`.

Token, monetary, GPU-time, and energy estimates remain formulas until models, context sizes, decoding limits, and hardware are frozen.

## M1B-D01: context-only negative regime

Test M1B-P01 with one context-only implementation, one external governed store, and one internal recurrent or compressive state realization. Cross four preregistered reuse and horizon cells, use three independent seeds, and evaluate at least 400 paired instances per cell.

- Lower bound: `3 * 1 * 4 * 3 * 400 = 14,400` query executions, plus state construction and teardown traces.
- Primary decision: quality noninferiority within 1 percentage point and vector resource dominance.
- Decisive result: a stateful class must beat context-only in both non-isomorphic families without hiding lifecycle costs to falsify the negative regime.

## M1B-D02: semantic feasibility under unseen updates

Use independently generated held-out facts that postdate the frozen model or are synthetic nonces. Compare context-only, a bitemporal external store, and an orthogonal append-only or governed internal-state realization across three mutation or supersession rates, three seeds, and 400 paired update-query episodes per cell.

- Lower bound: `3 * 1 * 3 * 3 * 400 = 10,800` answer executions, plus at least 3,600 update transactions per implementation family.
- Primary decision: current-version and provenance contract pass rate, not aggregate QA alone.
- Required control: a leakage audit proving that the current value is absent from model training, prompt text, filenames, ordering artifacts, and evaluator metadata.
- Decisive falsifier: context-only satisfies the contract without any path to the update.

## M1B-D03: fixed versus adaptive computation

Across three model families, compare fixed-low, fixed-high, difficulty-routed, and value-of-computation policies. Freeze four difficulty/proxy cells, three seeds, and at least 400 paired queries per cell.

- Lower bound: `3 * 4 * 4 * 3 * 400 = 57,600` policy-query executions.
- Primary decision: at least 15 percent charged-cost reduction at quality noninferiority within 1 percentage point.
- Required controls: router probes and failed branches are charged; the best fixed policy is selected only on training or validation data.
- Decisive falsifier: a fixed policy weakly dominates adaptive policies across all three held-out model families.

## M1B-D04: state validity by compute interaction

Use a paired factorial with four state conditions (current, stale, missing, contradictory), two independently assigned difficulty strata, and four policies (fixed-low, fixed-high, difficulty-only routing, validity-aware routing). Test three model families, two seeds, and at least 200 paired instances per state-by-difficulty cell.

- Lower bound: `4 * 2 * 4 * 3 * 2 * 200 = 38,400` policy-query executions, plus validity checks and state lifecycle operations.
- Primary decision: the state-validity by compute interaction and the validity-aware router's complete cost-compliance frontier.
- Required controls: validity labels are hidden from answering models; the validity detector is evaluated and charged separately; current evidence is held constant within paired interventions.
- Decisive falsifier: the interaction confidence interval includes zero in all held-out families, or the difficulty-only router weakly dominates after validity-check costs.

This design could measure an interaction. It would not by itself make the M1b thesis original because STALE, X-Router, PLACEMEM, PersistBench, and generic value-of-computation already reconstruct its conceptual motivation.

## M1B-D05: abstention under shift

Reuse held-out families and workload cells from M1B-D01 through M1B-D04. Freeze coverage, calibration, and selective-risk thresholds on disjoint validation data, then compare forced and abstaining decisions on at least 10,000 decision records.

- Additional lower bound: 10,000 transition decisions; no new model inference is required if all necessary pre-outcome features and outcomes were logged prospectively.
- Primary decision: conditional contract-violation risk below the declared bound after charging abstention cost.
- Decisive falsifier: the forced comparator meets the same risk bound at strictly lower total cost on two held-out implementation families.

## Resource disposition

The combined lower bound is 131,200 query or policy executions before tuning, replication beyond the minimum, lifecycle transactions, or independent reproduction. This cannot be converted to GPU-hours, API cost, storage, or energy credibly from the current repository because model families, context lengths, output limits, adapters, and deployment modes are not frozen.

No execution is authorized. The designs are retained only as falsifiability checks for the stopped objects.
