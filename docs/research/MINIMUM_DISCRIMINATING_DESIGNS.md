# Minimum Discriminating Designs for the M1b Audit

Status: `DESIGN_ONLY_NOT_AUTHORIZED`
Issue: `#5`
Gate result: `STOP`

## Purpose

These designs preserve the falsifiability of stopped candidate objects. They are not five positive predictions supporting an article, do not establish novelty, and do not authorize data collection, model calls, implementation, or manuscript work. Any execution would require a new scientific issue that states a distinct eligible claim and freezes resources.

Counts below are lower-bound execution or decision units, not a funding request or a complete cost estimate.

## Prediction-to-design map

| Design | Prediction | Normalized status | Novelty disposition | Why retained after `STOP` |
|---|---|---|---|---|
| `M1B-D01` | `M1B-P01` | `ANTICIPATED` | Known context-only negative regime | Prevents a future universal managed-state claim from erasing a preregistered zero-reuse regime |
| `M1B-D02` | `M1B-P02` | `ANTICIPATED` | Information-access bound, not architecture superiority | Shows how to distinguish missing information from a persistence effect |
| `M1B-D03` | `M1B-P03` | `ANTICIPATED` | Value-of-computation boundary | Keeps the causal marginal-compute estimand and local rejection rule explicit |
| `M1B-D04` | `M1B-P04` | `UNSUPPORTED` | `UNSUPPORTED_NOT_DISTINCT` | Records a falsifiable interaction without treating an unexecuted factorial as a novel result |
| `M1B-D05` | `M1B-P05` | `ANTICIPATED` | Generic reject-option theory | Makes coverage, risk, and rejection cost auditable if a later eligible claim is opened |

## Shared accounting and inference

All designs require paired instances, frozen prompts and adapters, independently generated ground truth, exact model and system versions, complete lifecycle accounting, and family-level held-out evaluation. Model/API prices, GPU-hours, storage, energy, and wall-clock cost remain `NON DISPONIBLE` until eligible systems, deployment modes, and hardware are frozen.

For each cell, record:

- input, output, answer-reasoning, retrieval, repair, and maintenance tokens separately;
- model and non-model FLOPs where measurable;
- p50 and p95 end-to-end latency and throughput;
- peak volatile memory, persistent bytes, bytes moved, reads, and writes;
- construction, update, invalidation, recovery, and teardown work;
- detector, router, failed-branch, and abstention work;
- energy only from a declared meter, never inferred from nominal TDP;
- contract pass or violation with the frozen tolerance and every abstention.

Confidence intervals are simultaneous within each registered family of primary comparisons. Multiplicity procedure, cluster unit, missing-data rule, seeds, equivalence margins, and any resource normalization must be frozen before confirmation.

For a design with a balanced factorial, the call floor is the product of implementation or model families, policy arms, workload cells, seeds, and instances per cell. Power analysis can only increase the per-cell count. Token, monetary, GPU-time, storage, and energy estimates remain formulas until models, limits, adapters, and hardware are frozen.

## M1B-D01: context-only negative regime

Test `M1B-P01` with one context-only implementation, one external governed store, and one internal recurrent or compressive state realization. Every confirmatory cell has exactly zero cross-query reuse: no retained artifact produced for one episode may be read by a later episode. Cross two declared dependency occupancies within the available invocation by two positive lifecycle-overhead bands, use three independent seeds, and evaluate at least 400 paired instances per cell.

- Per-cell count: `n_D01 = max(400, n_power)`, where `n_power` is frozen for the smallest registered strict quality or resource improvement.
- Lower-bound answer executions at `n_D01 = 400`: `3 implementations * 4 cells * 3 seeds * 400 = 14,400`, plus construction and teardown traces.
- Primary variables: contract pass rate `Q`, higher is better, and every coordinate `R_j` of the registered lifecycle resource vector, lower is better.
- Exact Pareto rule: implementation `A` statistically dominates `B` only when simultaneous 95 percent intervals establish `Q_A - Q_B >= 0` and `R_A,j - R_B,j <= 0` for every registered `j`, with a strict positive quality difference or strict negative resource difference on at least one coordinate. Any resource degradation, quality degradation, or crossed trade-off is `INCOMPARABLE` unless a scalar preference was frozen before outcomes.
- Separate noninferiority label: `Q_A - Q_B >= -0.01` with lower cost may be reported as `QUALITY_NONINFERIOR_COST_BETTER`; it must never be called Pareto dominance.
- Decisive P01 rejection: one tested stateful implementation statistically dominates context-only under the exact rule. This rejects P01 for that implementation only; it does not establish a whole-class ordering.

## M1B-D02: semantic feasibility under unseen updates

Use independently generated 128-bit value nonces and 128-bit provenance nonces that postdate the frozen model or are synthetic. Compare four arms: no-update view-only, stateless live-input or prompt reinjection, an external bitemporal store, and an orthogonal append-only or governed internal-state realization. Cross three mutation or supersession rates, three seeds, and 400 paired update-query episodes per cell.

- Lower-bound answer executions: `4 arms * 3 mutation cells * 3 seeds * 400 = 14,400`.
- Additional operations outside the answer count: at least 3,600 live reinjections and 7,200 state-update transactions across the two persistent arms.
- Contract: exact current value and exact provenance are required on every episode. Compliance threshold is 100 percent; permitted stale or unprovenanced answers are 0 percent. One verified violation therefore fails the per-episode contract, independently of the aggregate confidence interval.
- Information control: the live stateless arm receives the same update as the stateful arms. If it matches them, persistence is not identified as the cause. The no-update arm differs only in access to the decision-critical update.
- Leakage control: prove that both nonces are absent from model training, prompt text, filenames, ordering artifacts, caches, evaluator metadata, and every other accessible channel.
- Class-inference rule: no-update infeasibility follows from the declared information-access assumption and nonce construction, not from one model's empirical failure. Empirical failures alone cannot establish that every view-only implementation is infeasible.
- Decisive premise falsifier: after a clean leakage audit, a no-update arm emits the exact independently sampled value-provenance pair. Its chance probability is at most `2^-256` per episode. A successful stateless live-input arm is an expected orthogonal control, not a falsifier of the information bound.

## M1B-D03: fixed versus adaptive answer computation

Across three model families, compare fixed-low, fixed-high, generic-difficulty routing, and value-of-computation routing. On a group-disjoint fit split, randomize low versus high answer compute and train a cross-fitted estimator `tau_hat(x)` of the conditional causal gain from extra computation. Do not train the routing proxy on generic difficulty or realized correctness alone.

Use nested calibration to select the best fixed baseline, calibrate `tau_hat`, and freeze the decision threshold `tau_hat(x) > added compute cost + router overhead`. Lock four treatment-benefit cells and every threshold before evaluating the held-out confirmation set.

- Per-cell count: `n_D03 = max(400, n_power)`, where `n_power` targets 80 percent power at one-sided alpha 0.05 for both a 15 percent charged-cost saving and the 1 percentage point quality noninferiority margin, with the registered cluster structure and multiplicity correction.
- Lower-bound policy-query executions if `n_power <= 400`: `3 model families * 4 policies * 4 cells * 3 seeds * 400 = 57,600`.
- Primary decision: relative charged-cost saving of at least 15 percent versus the calibration-selected best fixed schedule, with quality loss no more than 1 percentage point.
- Required controls: identical evidence; router probes, failed branches, calibration, and scheduling overhead charged; no threshold selection on confirmation outcomes.
- Local rejection rule: reject P03 in a preregistered support cell if the one-sided 95 percent upper confidence bound on saving is below 15 percent or the one-sided 95 percent lower bound on quality loss is above 1 percentage point. Fixed dominance across all three families is a stronger secondary result, not a prerequisite for rejection.

The number 400 is only a floor. If the frozen power analysis returns a larger `n_power`, every count and resource formula must use it.

## M1B-D04: state validity by answer-compute interaction

Use four independently assigned state conditions, `current`, `stale`, `missing`, and `contradictory`, two difficulty strata, and five policy arms:

1. fixed-low answer-only compute;
2. fixed-high answer-only compute;
3. difficulty-only answer-compute routing;
4. validity-aware answer-only routing;
5. validity-aware repair-plus-compute.

In arms 1 through 4, state is frozen after assignment: retrieval from a new source, mutation, repair, reacquisition, and prompt reinjection are prohibited. The validity detector may only emit a routing signal and its full cost and errors are charged separately. Arm 5 may acquire or repair state, but its gains are a distinct repair estimand and cannot be credited to answer-only computation.

Let `Y` be binary contract compliance. For model family `f`, define the preregistered answer-only interaction in percentage points as

`I_f = 100 * 0.5 * sum_d { [E(Y | current,d,high) - E(Y | current,d,low)] - (1/3) * sum_s_in_{stale,missing,contradictory} [E(Y | s,d,high) - E(Y | s,d,low)] }`.

The cross-family estimand is `I = (I_1 + I_2 + I_3) / 3`, with equal weights frozen before outcomes. The minimum scientifically meaningful interaction is 5 percentage points.

- Per-cell count: `n_D04 = max(200, n_power)`, where `n_power` targets 80 percent power at one-sided alpha 0.05 for a 5 percentage point interaction after the registered multiplicity and clustering corrections.
- Lower-bound policy-query executions if `n_power <= 200`: `4 state conditions * 2 difficulty strata * 5 arms * 3 model families * 2 seeds * 200 = 48,000`, plus validity checks, repair operations, and lifecycle traces.
- Primary interaction decision: the lower one-sided 95 percent confidence bound for `I` reaches 5 percentage points. Reject the meaningful-interaction claim when the upper one-sided 95 percent bound is below 5 percentage points.
- Primary routing decision: versus difficulty-only routing, validity-aware answer-only routing saves at least 15 percent charged answer compute at no more than 1 percentage point compliance loss after detector cost. Apply the same rejection inequalities as P04.
- Cross-family rule: report every `I_f`, the equal-weight `I`, heterogeneity, leave-one-family-out estimates, and a hierarchical 90 percent prediction interval. A pooled nonzero interval alone cannot establish transportability; a transport claim additionally requires the prediction interval to remain above zero.
- Repair rule: report the repair-plus-compute contrast separately against validity-aware answer-only routing, including acquired bytes, retrieval latency, mutations, and repair failures.

This design could measure an interaction. It would not make the M1b thesis original because `EV-0049` through `EV-0053` and `EV-0056`, together with generic value-of-computation theory, already reconstruct its conceptual motivation.

## M1B-D05: abstention under shift

Use group-disjoint records from D01 through D04 only if every required pre-outcome feature was collected prospectively. Split workload and implementation-family groups into 50 percent fit, 25 percent calibration, and 25 percent locked shift-test groups. No group may cross a split.

On the fit split, freeze the `Omega` feature vector, robust scaling, and covariance estimate. Define nonconformity `s(x)` as nearest-neighbor Mahalanobis distance to the fit set. On calibration data, define coverage `c(x) = 1 - F_cal(s(x))` and freeze the 90th-percentile conformal boundary; `c(x) < 0.10` is out of support. Also abstain when simultaneous Pareto intervals do not identify a dominance relation.

- Comparison: forced selection versus the identical selector with the frozen abstention rule.
- Risk target: conditional contract-violation risk among non-abstained decisions at most 5 percent.
- Uncertainty method: one-sided 95 percent workload-by-implementation-family block-bootstrap upper bound with 10,000 resamples and a frozen random seed.
- Loss: contract violation `1.00`, abstention `0.10`, correct non-abstained decision `0`. Physical resource coordinates remain separately reported and may enter the loss only through weights frozen before outcomes.
- Minimum locked test size: 10,000 transition decisions across at least two held-out implementation families.
- Decisive rejection: forced selection has a one-sided 95 percent risk upper bound at or below 5 percent and the one-sided 95 percent lower bound of `L_abstain - L_forced` exceeds 0.02 normalized loss units.

No-new-inference reuse is allowed only when the pre-outcome features, outcomes, group identities, and all charged costs were logged prospectively before this design was evaluated. Otherwise D05 requires new data under a separately authorized issue, and the claimed zero-inference increment is invalid.

## Resource disposition

At the stated per-cell floors, the revised plan contains:

- D01: 14,400 answer executions;
- D02: 14,400 answer executions, plus live reinjections and state transactions;
- D03: 57,600 policy-query executions if its power floor does not exceed 400;
- D04: 48,000 policy-query executions if its power floor does not exceed 200, plus detector, repair, and lifecycle operations;
- D05: 10,000 transition decisions, with no new inference only under the prospective-log rule.

The arithmetic floor is `134,400` answer or policy-query executions plus `10,000` transition decisions, or `144,400` execution-or-decision units. Power analysis, tuning, lifecycle transactions, repair, independent reproduction, and missing prospective logs can only increase it.

`144,400` is not a complete cost. GPU-hours, API price, storage, energy, wall-clock time, and labor remain `NON DISPONIBLE` until models, context lengths, output limits, adapters, hardware, and deployment modes are frozen.

No execution is authorized. The designs remain falsifiability records for stopped objects; reopening any experiment requires a new issue with a distinct claim that survives the novelty gate.
