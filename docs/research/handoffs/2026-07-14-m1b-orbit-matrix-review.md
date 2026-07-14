# M1b literature-matrix coverage review

Date: `2026-07-14`  
Base commit: `86cb827b3ad7acfdad43106dce54f95ceaa6529a`  
Functional role: independent coverage reviewer  
Recommended gate effect: `STOP`, with no `DISTINCT_CANDIDATE`

## 1. Objective

Review whether a future M1b extension of `LITERATURE_MATRIX.csv` can represent every decision-critical collision in the committed transition artifacts without treating an unreported paper, test, coefficient, or estimator as evidence of novelty.

## 2. Scope and exclusions

The review is limited to the committed state at the base SHA. Concurrent worktree changes were excluded. It checks matrix coverage and evidence-link discipline; it does not reopen primary-paper metadata, claim a systematic-search recall level, draft an article, or authorize an experiment.

## 3. Questions tested

1. Are the direction, `Omega/G/B/A` contract, state transition, compute transition, validity-by-compute residual, and full systems reduction represented by positive collisions?
2. Does each `difference` field identify a positive residual technical object, or correctly classify its absence as unsupported?
3. Can the rows fit the existing matrix schema without inventing evidence identifiers?

## 4. Inputs and versions

- `docs/research/TRANSITION_CONTRACT.md`, especially **Reduction result**, **Residual test: state validity before adaptive compute**, and **Disposition**.
- `docs/research/PREDICTION_REGISTER.csv`, `M1B-P01` through `M1B-P05`.
- `docs/research/COUNTEREXAMPLE_REGISTER.csv`, `M1B-C01` through `M1B-C08`.
- `docs/research/MINIMUM_DISCRIMINATING_DESIGNS.md`, `M1B-D01` through `M1B-D05`.
- `docs/research/M1B_SEARCH_LOG.csv`, especially `DQ-01` through `DQ-04` and `IR-01` through `IR-14`.
- `docs/research/handoffs/2026-07-14-m1b-terra-stateful-systems.md`, Sections 4.2 and 6.2-6.8.
- `docs/research/handoffs/2026-07-14-m1b-terra-regime-boundaries.md`, Sections 6.1-6.6.
- `docs/research/handoffs/2026-07-14-m1b-sol-contract-reduction.md`, Sections 1.2-1.7, 3, 5, and 6.
- Committed `CLAIM_LEDGER.csv`, `EVIDENCE_LEDGER.csv`, and `LITERATURE_MATRIX.csv` at the base SHA.

## 5. Proposed matrix rows

These eight rows are the smallest complete mapping. `Status` remains the matrix workflow value `INCLUDED`; the novelty disposition belongs explicitly in `notes`. `NEW ID REQUIRED` means that a verified evidence-ledger row must exist before integration, not that a provisional identifier may be placed in the matrix.

| property_id | proposed_property | prior_work_id / positive collision | overlap | difference that may be stated | evidence_ids at committed HEAD | discriminating_experiment | status / required note |
|---|---|---|---|---|---|---|---|
| `P-005` | Future LLM systems should shift from prompt accumulation to runtime-governed state and compute | `PW-P005-RUNTIME-PLACEMEM`: State-Aware Runtime + PLACEMEM | Canonical state, validation, commit/rollback/recovery, permissions/audit, plus a correction- and compute-aware memory plane with validity and reuse | The candidate changes organization and vocabulary but supplies no new observable boundary or falsifier | `NEW ID REQUIRED` for both direct records | `M1B-D01`-`D04` test already-known regime questions, not the slogan itself | `INCLUDED`; direction `ANTICIPATED` |
| `P-006` | Pre-outcome `Omega` descriptors select among context-only and stateful classes | `PW-P006-WORKLOAD-CHAR`: Agent Memory + Agent-Native Memory | Update rate, reuse, freshness, maintenance, horizon, bottleneck, and cost-performance already condition feasibility and recommendations | No calibrated cross-family selector is specified; that missing result is `UNSUPPORTED`, not a distinction | `EV-0041;EV-0042` | `M1B-D01;M1B-D02` on held-out workload and implementation families | `INCLUDED`; `Omega` `ANTICIPATED`, quantitative `T` `UNSUPPORTED_NOT_DISTINCT` |
| `P-007` | `G` guarantees and `A` adequacy govern validity, provenance, rollback, authorization, and explicit failure | `PW-P007-GA-COMPOSITE`: ClawVM + TOKI + Verifiable Memory Governance + State-Aware Runtime + assume/guarantee satisfaction | Typed fidelity, temporal isolation, provenance, scoped retrieval, rollback/recovery/forgetting, validation, audit, and satisfaction under assumptions | Collecting these predicates into `G` and defining `A` as satisfaction adds no new invariant, guarantee, or realizability result | `NEW ID REQUIRED` for the direct and generic records | `M1B-D02` with two non-isomorphic governed-state realizations | `INCLUDED`; `G/A` `ANTICIPATED_BY_COMPOSITE` |
| `P-008` | `B` is a vector resource envelope separating feasibility, efficiency, and Pareto ordering | `PW-P008-RESOURCE-COMPOSITE`: QML/SLO + OS reservations/DRF + working-set theory + Agent Memory + Agent-Native Memory | Vector caps, enforcement horizons, locality/reuse, lifecycle accounting, hard feasibility, and Pareto comparison | Applying the vector to LLM state systems supplies no new allocation law or conclusion-changing accounting result | `EV-0041;EV-0042`, plus `NEW ID REQUIRED` for generic records | `M1B-D01`-`D04` with every lifecycle resource charged | `INCLUDED`; `B` `ANTICIPATED`; complete accounting is experimental hygiene |
| `P-009` | Persistent-state use depends on currentness, relevance, consent, reuse, and downstream harm | `PW-P009-STATE-BOUNDARIES`: When Should Memory Stay Silent + PersistBench + Shared Selective Persistent Memory + A-TMA + Agent-Native Memory | No-memory, selective-memory, stale-state, harmful-memory, failure-localization, and rank-reversal regimes are positively reported | The candidate supplies no new transportable memory-use rule, threshold, or invariant | `EV-0042`, plus `NEW ID REQUIRED` for the other records | `M1B-D01;M1B-D02;M1B-D04` across orthogonal state realizations | `INCLUDED`; state-transition direction and negative regimes `ANTICIPATED` |
| `P-010` | Adaptive compute is warranted only when expected marginal value repays compute and routing overhead | `PW-P010-COMPUTE`: value-of-computation metareasoning + ACT/PonderNet/adaptive depth + X-Router + ATLAS allocation | Compute-or-stop, cost-conditioned depth, evidence-versus-reasoning routing, and adaptive stopping are established | No new value estimator, policy guarantee, LLM-specific margin, or cross-family law is supplied | `EV-0013;EV-0015;EV-0029`, plus `NEW ID REQUIRED` for metareasoning and X-Router | `M1B-D03` against strongest fixed schedules with routing costs charged | `INCLUDED`; compute transition `ANTICIPATED` |
| `P-011` | State validity should be checked before buying more reasoning on stale, missing, or contradictory state | `PW-P011-VALIDITY-COMPUTE`: STALE + A-TMA + PLACEMEM + PersistBench + X-Router + value of computation | Current-state adjudication, state-failure localization, validity-aware memory, non-monotone reasoning effects, evidence/reasoning routing, and conditional compute value reconstruct the motivation | The exact factorial may be unreported, but the candidate specifies no estimator, theorem, coefficient, or margin; search silence creates no novelty | `NEW ID REQUIRED` for the decision-critical records | `M1B-D04`, the preregistered validity-by-compute factorial | `INCLUDED`; `UNSUPPORTED_NOT_DISTINCT`, never `PIVOT` from absence |
| `P-012` | The implementation-neutral `Omega/G/B/A/T` shell selects feasible nondominated classes or abstains | `PW-P012-GENERIC-SYSTEMS`: contracts + QoS/SLO + temporal DB/PROV/event sourcing/revocation + OS resources/caching + metareasoning + robust Pareto/reject theory | The composite reconstructs environments, guarantees, resource vectors, temporal validity, adequacy, feasibility, efficiency, and abstention | The notation proves no LLM-specific separation and derives no calibrated architecture predictor or boundary | `NEW ID REQUIRED` for the generic-theory records | `M1B-D05` under held-out workload and implementation families | `INCLUDED`; generic shell `ANTICIPATED_BY_COMPOSITE`, calibrated LLM `T` `UNSUPPORTED_NOT_DISTINCT` |

## 6. Coverage findings

1. The eight rows cover the requested orbit exactly once. Splitting `G` from `A` would duplicate the same contract-satisfaction reduction; merging `P-005` with `P-012` would hide the distinction between a direct domain-level direction collision and a generic formal reconstruction.
2. The matrix must preserve two levels for `T`: the set-valued constrained-selection shell is anticipated, while a calibrated LLM-specific predictor is unsupported and not distinct. A single undifferentiated `T` verdict would be misleading.
3. A `difference` such as “no single paper combines everything” or “the exact factorial was not found” is inadmissible. Each row above instead records the positive composite and states that no positive residual object is currently specified.
4. At committed HEAD, only `EV-0041`, `EV-0042`, `EV-0013`, `EV-0015`, and `EV-0029` among the proposed links already exist. The future matrix must not cite uncommitted or guessed IDs; direct M1b and generic-theory sources require verified ledger entries first or in the same reviewed change.
5. `CLM-009` is `UNSUPPORTED` with no evidence IDs at committed HEAD. Adding collision rows supports a negative novelty determination; it cannot silently convert that claim into an original or article-eligible result.

## 7. Uncertainties and contradictions

- This is an artifact-coverage review, not an independent bibliographic re-verification. Recent 2026 records still require the scheduled locator/version audit.
- The source set does not establish a calibrated cross-family transition law. That uncertainty weakens the candidate result rather than generating novelty.
- `M1B-D04` could produce a useful empirical interaction, but the present conceptual claim is already reconstructed and the experiment is not authorized by this review.

## 8. Files modified

- Added only `docs/research/handoffs/2026-07-14-m1b-orbit-matrix-review.md`.
- No existing file was edited.

## 9. Verification

- Read all decision-critical artifacts from committed HEAD rather than concurrent worktree versions.
- Checked the proposed rows against the existing ten-column matrix schema.
- Checked every proposed evidence link against committed `EVIDENCE_LEDGER.csv`; no future evidence ID was invented.
- Checked that all eight rows rest on positive prior-art or generic-theory collisions and that no absence statement carries novelty weight.

## 10. Recommended decision

Integrate the eight-row coverage only after the corresponding evidence-ledger records and locators are verified. The covered direction remains `STOP`: all formal objects and transition directions are anticipated or reconstructed, while the only quantitative residuals are unsupported and not distinct.

## 11. Next authorized action

The integrator may translate these rows into the CSV schema, assign only verified evidence IDs, then submit the completed matrix and ledgers to the scheduled bibliographic and anti-rewrite reviewers. No manuscript or experiment follows from this review.

## 12. Roles

- Authoring role: independent M1b matrix-coverage reviewer.
- Required reviewing role: Luna-Librarian for metadata/locators, followed by Luna-QA or Luna-RedTeam for anti-rewrite consistency.
