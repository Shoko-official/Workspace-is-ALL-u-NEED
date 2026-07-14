# M1c Distinct-Object Candidate Register

Cutoff: `2026-07-15`
Issue: [#9](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/9)
Gate result: `STOP`
Surviving `DISTINCT_CANDIDATE` objects: `0`

## Gate

M1c did not ask whether managed state is useful. It asked whether an independently motivated observable, mechanism, estimator, invariant, bound, or theorem survives all of the following:

1. a decisive falsifier and a declared negative regime;
2. the strongest direct prior-art composite;
3. substitution of LLM-specific labels by the underlying systems object;
4. reduction to generic database, provenance, incremental-computation, information, control, causal, or statistical theory; and
5. a minimum discriminating design stated before implementation.

`ANTICIPATED_DIRECTLY`, `ANTICIPATED_BY_COMPOSITE`, `REDUCED_TO_KNOWN_THEORY`, and `UNSUPPORTED_NOT_DISTINCT` are terminal novelty dispositions. A testable but reduced candidate does not authorize an experiment.

An exact experimental axis being unreported is insufficient for `PIVOT` when the strongest composite already supplies the protocol ingredients, phenomenon class, and ordinary estimator. Reopening then requires a predictive law, mechanism, causal estimator, invariant, or guarantee that the composite cannot reconstruct, not merely a new application cell.

## Candidate register

### M1C-C01: Exact revision-replay equivalence certificate

- Independent motivation: avoid full recomputation after a fact, tool result, or state revision while preserving the output of a fresh execution.
- Technical object: a verifier `V` accepts a repaired trace only when it is pathwise equivalent, or distributionally within `(epsilon, alpha)`, to fresh execution on the revised history.
- Decisive falsifier: one accepted pathwise divergence, or a lower confidence bound on false acceptance above `alpha`.
- Negative regime: unlogged randomness or effects, new control-flow dependencies, opaque services, or verification as expensive as fresh replay.
- Strongest composite: dynamic dependence graph plus change propagation, approximate probabilistic trace equivalence, and replay validation (`EV-0078`; `EV-0080`; `EV-0067`; `EV-0068`).
- Generic reduction: self-adjusting computation plus approximate probabilistic trace equivalence.
- Minimum discrimination: a proof of a family accepted by the proposed certificate but not representable by the generic composite while retaining the same equivalence guarantee. Finite benchmark gains cannot establish that separation.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C02: Revision dependency-closure certificate

- Independent motivation: identify exactly which derived state must be invalidated after a revision.
- Technical object: compute the transitive closure of changed sources through the actual read-dependency graph, recompute the closure, and reuse its complement.
- Decisive falsifier: a real omitted dependency permits reuse of an incorrect value.
- Negative regime: dense attention, position shifts invalidating a suffix, hidden dynamic dependencies, or opaque calls.
- Strongest composite: adaptive functional programming, provenance, incremental view maintenance, and truth maintenance (`EV-0078`).
- Generic reduction: change propagation on a dynamic dependence graph. The cited primary work proves correspondence to complete re-evaluation under its safety assumptions.
- Minimum discrimination: a formal non-reduction or countermodel; an empirical speedup over full recomputation is already predicted by the generic object.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C03: Minimum repair cone

- Independent motivation: localize the least-cost subset of a trace or cache that must be recomputed after a revision.
- Technical object: minimize repair cost subject to the repaired output distribution remaining within `epsilon` of fresh execution.
- Decisive falsifier: violation of the output-distance constraint or no gain over suffix recomputation and selective-recompute baselines.
- Negative regime: diffuse influence, global attention, long causal cascades, or adversarial revisions.
- Strongest composite: dependency-aware change propagation (`EV-0078`) plus causal intervention and localized repair (`EV-0067`; `EV-0068`). These records supply the ingredients but do not solve the stated global minimum-cost repair problem.
- Generic reduction: weighted dynamic computation plus minimum sufficient causal intervention. The global objective is a generic optimization extension, not a directly anticipated LLM-specific result.
- Minimum discrimination: exhibit a repair family outside dependency closure and causal intervention while preserving the same guarantee. No such family is specified.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

### M1C-C04: Revision escape rate

- Independent motivation: quantify causally relevant dependencies that a declared provenance graph misses.
- Technical object: conditional probability that a revision changes fresh behavior by more than `gamma` while the declared dependency indicator remains zero.
- Decisive falsifier: for a claimed complete provenance mechanism, one causally effective undeclared dependency; for a positive escape hypothesis, an upper bound below the preregistered threshold.
- Negative regime: exhaustively specified symbolic dependencies, or stochastic environments that prevent controlled paired interventions.
- Strongest composite: provenance constraints, causal replay, and stale-state adjudication (`EV-0067`; existing `EV-0050`; existing `EV-0063`).
- Generic reduction: provenance recall, actual causality, and non-interference.
- Minimum discrimination: a new estimator with a guarantee unavailable from paired interventions and ordinary recall. The current rate is only a relabeling.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

### M1C-C05: Conservative compaction-coverage certificate

- Independent motivation: allow an agent to answer from a compacted history only when discarded information cannot change the answer beyond `epsilon`.
- Technical object: a selective answer-or-reject rule with calibrated accepted risk and coverage, optionally backed by a no-false-negative support filter.
- Decisive falsifier: for a deterministic certificate, one accepted query that depends on lost or stale information; for a calibrated-risk certificate, a simultaneous lower confidence bound on accepted-query loss risk above `alpha`.
- Negative regime: open-ended queries, latent support, repeated irreversible compaction, adversarial revisions, or a certificate approaching archive size.
- Strongest composite: `EV-0071` formally supplies rate-distortion optimization, lower bounds, query-unknown irreversible loss, and a repeated-compaction prediction. Its Sections 13.2 and 15 propose confidence, loss attribution, abstention, re-expansion, fetch, and escalation as a research agenda rather than an evaluated certificate; `EV-0060` supplies existing reject-option theory.
- Generic reduction: lossy coding plus provenance or approximate membership plus selective classification.
- Minimum discrimination: a theorem giving sublinear certificate size, non-trivial coverage, and bounded risk for open natural-language queries after adversarial revisions. No such theorem or mechanism is supplied.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C06: Stochastic decision serializability

- Independent motivation: shared-state agents have opaque read sets and stochastic decisions, so byte-level serializability can be stronger than necessary.
- Technical object: accept a concurrent history only when some serialization preserves irreversible effects and keeps the probability of decision-distribution divergence above `epsilon` below `delta`.
- Decisive falsifier: the held-out divergence bound exceeds `delta`, or any irreversible effect differs despite certification.
- Negative regime: deterministic explicit read sets, low decision margins, high entropy, or non-compensable effects.
- Strongest composite: CoAgent serializability and repair, Cordon semantic transactions, and the verified anomaly hierarchy (`EV-0064`; `EV-0065`; `EV-0066`).
- Generic reduction: semantic serializability under an observation function plus approximate probabilistic trace equivalence and statistical model checking (`EV-0080`).
- Minimum discrimination: `36,000` executions before serial replays. This design would measure an extension already named by the direct and generic composite, not establish novelty.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

### M1C-C07: Decision confluence without coordination

- Independent motivation: merge independent state updates without serializing them when downstream decision contracts remain valid.
- Technical object: two descendants of a common valid state are mergeable exactly when the merge preserves a declared decision invariant.
- Decisive falsifier: two branches declared mergeable whose merge violates the invariant.
- Negative regime: non-monotone constraints, hidden invariants, irreversible effects, or a stochastic validator.
- Strongest composite: shared-state systems plus invariant confluence (`EV-0064`; `EV-0065`; `EV-0079`).
- Generic reduction: the decision contract is an application invariant. I-confluence already gives the necessary and sufficient condition for valid coordination-free execution.
- Minimum discrimination: a family decision-confluent but not I-confluent under the same invariant. The definitions rule it out.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C08: Replay-closure certificate under runtime drift

- Independent motivation: know when a recorded agent run remains reproducible after model, tool, schema, or service changes.
- Technical object: a content-addressed dependency DAG covering model, tokenizer, tools, schemas, nondeterministic inputs, and effect receipts; replay fails closed outside the captured boundary.
- Decisive falsifier: two certified-closed executions diverge on a declared observable action or effect.
- Negative regime: unpinnable models, unrecorded time or network inputs, semantically changed external services, or non-idempotent effects.
- Strongest composite: Cordon lineage and recovery plus dependency-aware replay and causal execution records (`EV-0064`; `EV-0067`; `EV-0078`).
- Generic reduction: let `d` be the complete dependency vector, `r` the recorded nondeterministic inputs and effect receipts, and `F(d, x, r)` the declared observable. Content-addressed closure certifies only that both executions use identical `(d, x, r)`, so the promised equality is `F(d, x, r) = F(d, x, r)`. If runtime drift changes any element to `d'`, closure fails unless a separate equivalence proof establishes `F(d', x, r) = F(d, x, r)`. This is hermetic deterministic replay over closed provenance, not a new drift invariant.
- Minimum discrimination: `12,000` replays across 50 workflows, four drift axes, three systems, and 20 repetitions. Recorded responses make equality tautological; recomputed responses require the old environment or an equivalence proof.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

### M1C-C09: Decision-preserving state migration

- Independent motivation: move persistent state between model or runtime versions without silently changing downstream decisions.
- Technical object: certify a migration when action distributions on the target remain within `epsilon` of canonical reconstruction from source history, with risk at most `delta`.
- Decisive falsifier: a simultaneous lower confidence bound on post-migration violation risk exceeds `delta`, or the registered distance margin is exceeded with its declared uncertainty; one counterexample suffices only for a deterministic per-instance guarantee.
- Negative regime: model-specific KV state, lossy summaries, target semantic shifts, missing canonical history, or injected state.
- Strongest composite: Rosetta Memory cross-LLM writer/reader adaptation and unseen-model replacement, AFTER cross-model procedural transfer, and existing PLACEMEM validity (`EV-0069`; `EV-0070`; existing `EV-0051`).
- Generic reduction: for canonical history `h`, migrated state `mu(M_s)`, target reconstruction `R_t(h)`, query `q`, and target observation kernel `P_t`, the certificate is exactly `D(P_t(. | mu(M_s), q), P_t(. | R_t(h), q)) <= epsilon` except on a set of risk at most `delta`. This is approximate probabilistic trace equivalence under the target observation kernel (`EV-0080`) plus a statistical non-inferiority decision; changing the state labels adds no invariant.
- Minimum discrimination: `18,000` episodes across 12 source-target pairs, 100 tasks, three migration methods, and five draws, plus a reconstruction oracle.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C10: Causal closure of a semantic read set

- Independent motivation: infer the smallest memory subset whose intervention can materially change a downstream action.
- Technical object: a selected set `S` is sufficient when interventions on its complement change the action distribution by at most `epsilon`; its causal closure is an inclusion-minimal sufficient set.
- Decisive falsifier: an intervention on the complement violates the sufficiency guarantee, or a proper subset of `S` also satisfies it and refutes inclusion-minimality.
- Negative regime: synergistic dependencies, position effects, high stochasticity, or non-monotone interactions.
- Strongest composite: Causal Agent Replay and CausalFlow supply stochastic run-forward interventions, confidence intervals, dependency-aware localized repair, and interaction attribution, but neither establishes a globally minimal sufficient read-set closure (`EV-0067`; `EV-0068`).
- Generic reduction: dynamic slicing, causal provenance, and minimal sufficient intervention.
- Minimum discrimination: `30,000` counterfactual continuations for 100 traces, 20 items, three models, and five draws per method.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

### M1C-C11: Contract-carrying procedural memory

- Independent motivation: prevent a reusable skill from silently decaying when packages, APIs, schemas, services, or configurations change.
- Technical object: a procedure carries executable environmental assumptions, versions, preconditions, postconditions, provenance, and validation evidence; reuse requires resolution or revalidation.
- Decisive falsifier: an accepted skill fails because of covered drift, a fresh skill is rejected, or localized repair does not restore the contract.
- Negative regime: behavioral drift behind an unchanged schema, hidden dependencies, non-hermetic services, or underspecified natural language.
- Strongest composite: SkillGuard already formulates skill drift as contract violation, extracts executable role-bearing environment contracts, validates live conditions, and localizes repair; AFTER supplies versioned procedural-memory validation and cross-model transfer (`EV-0075`; `EV-0070`).
- Generic reduction: dependency invalidation, build systems, regression or property testing, and proof-carrying artifacts.
- Minimum discrimination: at least `8,361` controls from 929 existing skill cases across three backbones and three systems before adding new API cases.
- Disposition: `ANTICIPATED_DIRECTLY`.

### M1C-C12: Memory-contamination reproduction number

- Independent motivation: distinguish self-extinguishing memory errors from errors that reproduce through repeated read-write cycles.
- Technical object: mean descendants of a traceable contaminated memory, or the spectral radius of a multitype reproduction matrix.
- Decisive falsifier: a simultaneous upper confidence bound below one in the claimed supercritical regime.
- Negative regime: writes disabled, no retrieval, read-only state, or perfect independent validation.
- Strongest composite: A-MemGuard measures a self-reinforcing error cycle and rising injection success across rounds; Longitudinal Safety measures growth with accumulated memory. Neither record defines or estimates the proposed reproduction number (`EV-0076`; `EV-0072`).
- Generic reduction: let `K_ij = E[N_j | one contaminated item of type i]`, where `N_j` counts traceable type-`j` descendants in the next read-write generation. The proposed scalar is exactly `R_M = rho(K)`, the spectral radius of the mean-offspring matrix in a multitype branching process. Under the candidate's independent-offspring premise, `R_M > 1` is the ordinary supercritical threshold; if that premise fails, the candidate supplies no replacement model or theorem.
- Minimum discrimination: `28,800` evaluations across three systems, two backbones, two feedback regimes, four horizons, 200 episodes, and three seeds.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C13: Divergence exponent under read-write cycles

- Independent motivation: measure whether a small initial memory perturbation contracts, remains bounded, or amplifies over a long-lived agent trajectory.
- Technical object: finite-horizon gain or a log-divergence exponent between paired perturbed and unperturbed streams.
- Decisive falsifier: no positive exponent beyond the preregistered margin.
- Negative regime: reversible archive, read-only state, NullMemory, or an independent correction oracle.
- Strongest composite: Longitudinal Safety observes exposure-dependent amplification, and the rate-distortion analysis predicts repeated-compaction amplification. Neither record defines or estimates the proposed Lyapunov-style quantity (`EV-0072`; `EV-0071`).
- Generic reduction: for paired state distributions separated initially by `D_0 > 0` and after `H` read-write transitions by `D_H`, the proposed exponent is exactly `lambda_H = H^{-1} log(D_H / D_0)`. This is the definition of a finite-time logarithmic gain; replacing physical state distance by an agent-output divergence does not create a new estimator, transition law, or stability theorem.
- Minimum discrimination: `57,600` generations across systems, backbones, domains, horizons, perturbations, streams, seeds, and paired arms.
- Disposition: `REDUCED_TO_KNOWN_THEORY`.

### M1C-C14: Revision hysteresis and post-forgetting resurrection

- Independent motivation: test whether returning from `A` through `B` to the same mandated current view `A` restores behavior or leaves path-dependent residue.
- Technical object: distance between answers under direct `A` and `A -> B -> A`, with current and historical queries separated.
- Decisive falsifier: equivalence within one percentage point and no stale resurrection across the declared current-query support.
- Negative regime: historical queries should differ; a fully reconstructed current view should be path-independent.
- Strongest composite: STALE and A-TMA supply LLM-specific stale-state validity failures (`EV-0050`; `EV-0056`); temporal provenance supplies the current-view contract (`EV-0062`; `EV-0063`); Hyperproperties supplies two-trace observational and probabilistic non-interference (`EV-0084`); and Ziegler drives an adaptive artificial agent through a target ramp and reversal without reset, obtaining different control burden at the same target and a signed hysteresis-loop area (`EV-0081`).
- Generic reduction: let `U_A` and `U_B` be state-update operators, `s_A = U_A(s_0)`, `s_ABA = U_A(U_B(U_A(s_0)))`, and `K(. | s, q)` the observation kernel. For current-view queries, the proposed statistic is `H(q) = D(K(. | s_A, q), K(. | s_ABA, q))`; the test `sup_{q in Q_current} H(q) <= epsilon` is a quantitative two-trace non-interference condition in which the intervening history is hidden and historical queries are explicitly declassified. `H(q) > 0` is the loop gap of an already formalized path-dependent system. The LLM state labels add no new observable, estimator, invariant, or guarantee.
- Minimum discrimination: `28,800` responses across four systems, two backbones, three histories, 200 facts, three seeds, and two query classes.
- Directness boundary: no examined document reports the exact LLM `A -> B -> A` forgetting-and-resurrection protocol. Ziegler anticipates the adaptive-agent hysteresis phenomenon, Hyperproperties anticipates the two-trace condition, and the LLM records anticipate the stale-state failure. The exact application is therefore not a new phenomenon class.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

### M1C-C15: Reset-to-stream ranking reversal

- Independent motivation: a benchmark that resets memory before every item may rank persistent systems differently from their deployed stream behavior.
- Technical object: compare isolated and persistent-stream estimands and register a reversal only when their paired system differences have opposite signs beyond three percentage points with simultaneous 95% intervals.
- Decisive falsifier: no held-out system pair has a replicated sign reversal beyond the margin.
- Negative regime: NullMemory, fixed read-only state, or zero cross-episode reuse.
- Strongest composite: Artifact Ecology defines reset, persistent, governed-persistent, and held-out inheritance branches and recommends replayable orders and causal inherited-state estimands (`EV-0077`). ShiftBench already reports that a longitudinal recovery axis reverses memory-policy rankings and changes system selection (`EV-0082`). MemDelta shows that controlled model and embedding factors reverse memory-system conclusions and explicitly recommends testing rank-order stability (`EV-0083`). Bojinov and Shephard supply potential outcomes and exact causal contrasts for treatment paths (`EV-0085`). Longitudinal Safety, EvoMemBench, and Memory-R2 add order randomization, cross-episode state, and shared-state comparison controls (`EV-0072`; `EV-0074`; `EV-0073`).
- Generic reduction: for systems `a,b`, conditions `c in {reset, stream}`, and cell means `theta_sc = E[Y | system=s, condition=c]`, the proposed flag is `R_ab = 1{(theta_a,reset - theta_b,reset)(theta_a,stream - theta_b,stream) < 0}` with added margins and simultaneous intervals. It is a thresholded ordinal interaction computed from the ordinary `2 x 2` cell means; the associated interaction is `(theta_a,stream - theta_b,stream) - (theta_a,reset - theta_b,reset)`. Time-series potential outcomes already express the corresponding path contrast. Persistent inheritance changes the stream cells, but the rank flag introduces no distinct estimand, mechanism, or estimator.
- Minimum discrimination: a credible realization requires four systems, two backbones, two inheritance conditions, three task regimes, four balanced orders, eight independent trajectories, and 30 scored items, plus swapped-state probes: `46,848` answer generations before memory writes or judges. It is currently infeasible under the recorded environment and would still test an anticipated phenomenon class rather than establish originality.
- Directness boundary: no examined document reports the exact inversion between reset-per-episode and persistent-stream rankings. Artifact Ecology anticipates the inheritance protocol; ShiftBench anticipates selection inversions under longitudinal evaluation; MemDelta anticipates conclusion reversals under controlled variation. An observed inversion would extend those results to inheritance without establishing a new estimator, mechanism, invariant, or general phenomenon.
- Disposition: `ANTICIPATED_BY_COMPOSITE`.

### M1C-C16: Cross-family memory-stability scaling law

- Independent motivation: seek a transportable dimensionless law across model families rather than another system-specific benchmark curve.
- Technical object: collapse the contamination or divergence rate after normalization by write propensity, retrieval probability, and validation accuracy.
- Decisive falsifier: dominant family-by-architecture interaction, unstable exponent, or held-out residual beyond the predictive margin.
- Negative regime: zero write or zero reuse must yield a zero feedback coefficient.
- Strongest composite: existing multi-family longitudinal and compaction studies (`EV-0071`; `EV-0072`; existing `EV-0049`).
- Generic reduction: an unspecified regression over a branching or stability coefficient.
- Minimum discrimination: `43,200` evaluated trajectories across three families, two sizes, two policies, three perturbations, four horizons, 100 streams, and three seeds.
- Disposition: `UNSUPPORTED_NOT_DISTINCT`.

## Strongest-composite result

The candidates fail for four independent reasons:

1. primary records instantiate proposed LLM-specific objects or phenomenon classes used by the strongest composites, notably semantic transactions, serializable multi-agent repair, causal stochastic replay, cross-LLM memory adaptation, procedural contract drift, longitudinal contamination, compaction loss, inheritance-aware evaluation, ranking instability, and adaptive-agent hysteresis;
2. positive composites reconstruct the exact-application residuals from longitudinal ranking instability, controlled conclusion reversals, adaptive-agent hysteresis, two-trace non-interference, LLM state-validity work, and path-indexed causal effects;
3. several remaining formulations are exact instances of dynamic dependence graphs, I-confluence, provenance, causal intervention, reject rules, branching processes, two-trace non-interference, path effects, or crossover interactions; and
4. the few numerically precise residuals supply no distinct observable and specify no new estimator, mechanism, invariant, bound, or theorem.

The targeted search is not exhaustive. The `STOP` uses positive direct and composite records, explicit generic reductions, and candidate specifications' failure to supply distinct technical content; it makes no search-silence inference.

## Minimum-design decision

The arithmetic floors above total hundreds of thousands of model executions if naively combined. That cost is not the decision basis. No design is authorized because zero candidate survives the originality gate. Running an experiment cannot manufacture technical distinctness after direct or composite anticipation or exact generic reduction.

## Decision

Global M1c decision: `STOP`.

- `0` objects are `DISTINCT_CANDIDATE`.
- No experiment, implementation, benchmark execution, training run, or manuscript is authorized.
- The negative audit is governance evidence, not the requested article.
- A future reopening still requires an independently motivated technical object that survives the same gate before implementation.
