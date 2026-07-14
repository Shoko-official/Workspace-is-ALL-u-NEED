# Luna Cross-Review: Anti-Assembly Eligibility Gate

Status: `COMPLETE`

Date: `2026-07-14`

Role: `Luna-QA / Luna-RedTeam`

Issue: `#1`

Exact model selection: `NON CONTROLLABLE`

Independent decision: `PIVOT` for the research program, `STOP` for the current broad architecture claim, and `NOT ELIGIBLE` for an architecture paper at this gate

## Review question

Does the current M0 package prevent a future paper from succeeding merely by assembling, renaming, or narratively reframing known workspace, memory, recurrence, adaptive-compute, provenance, and resource-routing mechanisms?

The answer on the initial review snapshot was `NO, NOT YET`. During this review, the working tree added an explicit initial decision, a closest-threat baseline requirement, and the `O x G` coordination study. Those changes resolve three initial objections at the M0 requirement level. Four closed blockers remain below, most importantly the mismatch between the charter's confirmatory threshold and the new anti-assembly gate.

This review supports a `PIVOT` only in the following limited sense: M1 may attempt to falsify a narrowly stated coordination hypothesis and may determine whether an independently useful benchmark or physical-accounting phenomenon exists. It does not authorize model implementation, an architecture novelty claim, or manuscript framing.

## Independent verdict on future article eligibility

The prospective paper is not currently eligible as a non-rewrite article.

It can become eligible only through at least one of these two routes:

1. **Mechanism route.** A formally specified, non-factorizing coordination mechanism produces a preregistered, practically meaningful causal coordination effect against the same-component fixed composite and separated-controller controls. The effect must survive complete matching, a resource-price intervention, replication at two model sizes, and transfer beyond a synthetic task whose generator encodes the proposed component roles.
2. **Empirical route.** A component-agnostic benchmark or complete physical-accounting study establishes a preregistered phenomenon that remains independently useful if the proposed model loses. It must change a comparative conclusion, ranking, or resource-allocation law across multiple strong architecture families. Merely reporting more metrics, wrapping known components, or constructing tasks that require the candidate action vocabulary does not qualify.

If neither route remains identifiable after M1, the program must return `STOP`. The absence of a paper containing the exact same action list, title, or diagram is never an eligibility condition.

## Reasons to decide STOP now

There are already strong reasons to stop the broad architecture direction:

1. The central memory-versus-recurrent-compute story is directly anticipated. [Universal Transformers Need Memory](https://arxiv.org/abs/2604.21999v3) reports state/depth substitution under ACT at fixed accuracy (§§2.1-2.2, §4.3, and §5.1; PDF pp. 2-3, 5-6, and 8-9).
2. Fixed compressed state plus bounded exact memory is directly anticipated by [HOLA](https://arxiv.org/abs/2607.02303) (§§3.1-3.4 and matched eviction ablations in §4.5; PDF pp. 4-6 and 8-9).
3. Learned recursive allocation coupled to KV-memory traffic and a reported quality-cost frontier is anticipated by [Mixture-of-Recursions](https://arxiv.org/abs/2507.10524) (§2 and §§3-4; PDF pp. 4-10).
4. Provenance, versions, lifecycle management, transactions, scheduling, and rollback are substantially anticipated at the system layer by [MemOS](https://arxiv.org/abs/2507.03724v4) (MemCube representation and scheduler, PDF pp. 13-21).
5. Explicit memory/computation allocation and infrastructure-aware accounting are already central to [Engram](https://arxiv.org/abs/2601.07372v2) (§3 and §6.4; PDF pp. 6-8 and 17-18), while [CAT](https://arxiv.org/abs/2511.05313v2) already exposes a single-model quality/compute/memory operating curve (§3 and §4.1; PDF pp. 4-5 and 7-9).
6. A single orchestrator that gathers evidence, allocates reasoning effort, and stops is directly threatened by [Agentic ATLAS](https://arxiv.org/abs/2606.01667) (§3.1 and §4; PDF pp. 3-9).

Together these records make a near-complete composite constructible from disclosed mechanisms. The remaining phrase, “one controller over all actions,” is currently a union of known action families, not a new algorithmic invariant. A generic policy can select any finite action set; enlarging that set does not itself create a scientific contribution.

The program nevertheless merits a narrow `PIVOT` rather than immediate termination because a coordination interaction or an outcome-changing accounting/benchmark phenomenon is testable. That is an empirical opportunity, not evidence of novelty.

## Findings

### BLOCKING

#### B-01: The confirmatory success rule can pass without defeating the assembly explanation

`CHARTER.md` requires one causal interaction or new phenomenon in the candidate-contribution paragraph, but its confirmatory threshold later accepts either length-AUC improvement or physical-cost reduction. Neither result is conjunctively tied to a coordination contrast. The new `PROTOCOL.md` text and decision record require the interaction, but the charter remains a conflicting success path. A known composite could therefore pass one source of truth even when the joint-versus-separated interaction is zero.

Required correction: make the charter's confirmatory success rule conjunctive with the article-eligibility gate already added elsewhere. For the mechanism route, success on quality or cost is necessary but insufficient. The preregistered coordination contrast must also exceed a practically meaningful threshold with its 95% confidence interval above that threshold, beat the strongest same-component fixed and separated policies, remain non-degenerate under resource-price interventions, and replicate under the declared transfer requirement. Failure closes the architecture route; it may not be reframed as a positive architecture paper.

#### B-02: The Joint Memory Machine benchmark is circular as primary novelty evidence

`PROTOCOL.md` requires every accepted Joint Memory Machine instance to need episodic retrieval, compressed state, recurrence, and provenance. This can make the proposed decomposition true by construction. Counterfactual target checks prevent trivial leakage but do not show that natural problems require the architecture or that a simpler composite cannot solve them.

Required correction: label this family as a diagnostic stress test only. The primary anti-assembly result must also hold on hidden, component-agnostic task families whose targets and difficulty annotations do not expose the candidate action ontology, and on the frozen natural transfer families. A benchmark-route paper must remain useful across architecture families and if the candidate loses.

#### B-03: The claimed narrow action delta is internally inconsistent

`CHARTER.md` defines the controller action set without `EXPIRE` or `ROLLBACK`. Terra-Evidence describes `EXPIRE` and `ROLLBACK` as semantics exposed to the same learned policy, while Sol-Theory defines expiration as deterministic and committed rollback as a privileged environmental event. These are different candidate mechanisms and require different baselines.

Required correction: record one owner for each transition in the source-of-truth specification. It is sufficient at M0 to declare expiration and committed rollback environmental/store transitions and preserve exact formalization as an M2 blocker. If the controller is intended to own them, add them to the candidate action set and required controls. No novelty claim may switch between these interpretations.

#### B-04: The M0 integration is not complete in every source of truth

`NOVELTY.md` and decision `0002` now distinguish the completed bounded screen from the pending M1 review and record the correct `PIVOT`. `STATE.md` still lists the review roles as active, contains no explicit gate decision, and has unchecked handoff/cross-review items. The decisive primary-source claims are not yet visible in the evidence/literature ledgers. Terra-Engineering and bibliography verification are also required by issue #1 and were incomplete at this review freeze.

Required correction: update `STATE.md`; integrate every decisive prior-art assertion into the evidence/literature ledgers with primary URL, exact version, and locator; reconcile the remaining independent handoffs; and record the three-part outcome exactly: broad architecture claim `STOP`, research program `PIVOT`, article eligibility `NOT ESTABLISHED`.

These four findings are the closed set of corrections blocking the M0 pull request from the current review snapshot.

### MAJOR

#### M-01: The surviving delta is still not a technical object

Terra-Evidence correctly says that the full action set was not observed in one primary record and immediately warns that this does not validate the combination. The current charter names the “joint budget-allocation mechanism” before a non-factorizing policy, learning rule, or constraint has been defined. The new novelty decision correctly downgrades this to an unsupported hypothesis, which is sufficient for M0. By the M1 exit, the program must either specify a technical object that cannot be reduced to a generic router over known actions and a discriminating test for that object, or select the empirical route. If neither exists, return `STOP` before M2.

#### M-02: Joint/separated identification and the strongest composite require an M2 freeze

The updated protocol now mandates the Sol-Theory `O x G` factorial, closest published threat families, and a same-component fixed/separated composite. This resolves the M0-level omission. M2 must still freeze observation sets, gradient paths, arbiter, action feasibility, capacity, supervision, tuning budget, and executable composite configuration. If the same-component comparison cannot be implemented and matched fairly, the architecture route is `STOP`, not “baseline infeasible.”

#### M-03: A causal interaction is not automatically a novel mechanism

Even a statistically nonzero higher-order interaction can arise from optimization instability, capacity mismatch, tuning, or a synthetic generator. The effect must be attributable to the frozen coordination intervention, practically meaningful, stable across seeds and sizes, and transferable. Otherwise it is a local empirical result, not architecture novelty.

#### M-04: Complete accounting is methodological quality unless it changes a conclusion

Measuring index maintenance, transfers, writes, storage, warm-up, latency, HBM, and energy is required for validity. It becomes a paper contribution only if a preregistered, reproducible result changes an architecture ranking, identifies a stable resource-allocation law, or falsifies a prevailing conclusion. A longer metric list is not novelty.

#### M-05: PIVOT must not be interpreted as a positive novelty opinion

The Terra-Evidence pass is bounded, lacks database result counts, and has not closed one full snowball cycle. It supports rejection of broad claims, but cannot support an exhaustive absence claim for the narrow policy. M1 must search the narrowed computational graph, policy interfaces, constrained-control formulation, and benchmark route before any `GO_TO_FORMALIZATION` decision.

#### M-06: Feasibility can still force STOP before implementation

`STATE.md` records no compute/data budget, a CPU-only PyTorch installation, no energy meter, undecided licenses, and no evidence that the 50M/150M/300M matrix is affordable. M1/M2 must cost the minimum decisive experiment first. If the strongest composite, factorial controls, and replication cannot be executed, the claim is not feasibly falsifiable and the gate is `STOP` or a narrower benchmark-only pivot.

### MINOR

#### N-01: Disambiguate the two ATLAS records

The test-time neural-memory paper (`arXiv:2505.23735`) and Agentic Test-time Learning-to-Allocate Scaling (`arXiv:2606.01667`) share the name ATLAS. Always include title and identifier in ledgers and manuscript notes.

#### N-02: Recheck rapidly changing 2026 preprints

HOLA, Sparse Delta Memory, Engram v2, CAT v2, Universal Transformers Need Memory, MELT, and Agentic ATLAS are recent. Freeze exact versions at M1, then refresh metadata and claims immediately before protocol freeze and submission.

## Gate consistency after required corrections

| Gate | Permitted decision | Anti-rewrite interpretation |
|---|---|---|
| M0 | `PIVOT` | Authorizes only the narrowed M1 search and feasibility analysis. Broad architecture claim is `STOP`. |
| M1 | `GO_TO_FORMALIZATION`, `PIVOT`, or `STOP` | `GO_TO_FORMALIZATION` requires a technically defined delta or independently useful empirical route plus a feasible discriminating design. It is not article eligibility. |
| M4 | `PIVOT` or `STOP` on oracle failure | Oracle success is only an upper bound; failure closes the corresponding route. |
| M5/M6 | `GO`, `PIVOT`, or `STOP` at anti-assembly gate | Same-component fixed/separated controls, causal coordination contrast, practical threshold, and complete accounting are conjunctive for the mechanism route. |
| M7 | `GO` or `STOP` on transfer | Synthetic-only gains cannot support the architecture route. |
| M9 | Eligible or ineligible manuscript | A manuscript is eligible only if at least one of the two routes in this review has survived its preregistered gates. |

## Assertion audit

| Assertion | Review status | Evidence treatment |
|---|---|---|
| Memory capacity and ponder depth can substitute | `SUPPORTED THREAT` | Primary source and exact locator: Universal Transformers Need Memory, §4.3 and §5.1. |
| Fixed recurrent state and bounded exact KV memory coexist | `SUPPORTED THREAT` | Primary source and exact locator: HOLA, §§3.1-3.4. “Exact KV” is not generalized to schema-exact source payloads. |
| Adaptive recursion can alter KV traffic and a Pareto frontier | `SUPPORTED THREAT` | Primary source and exact locator: Mixture-of-Recursions, §2 and §§3-4. |
| Provenance, versioning, lifecycle, transaction, and rollback concepts already exist in an AI-memory system | `SUPPORTED THREAT` | Primary source and exact locator: MemOS, PDF pp. 13-21. This does not establish identical neural invariants. |
| One trained policy over the complete candidate action set is absent from all prior art | `NOT ESTABLISHED` | The bounded screen did not observe one. This negative observation is not used as novelty evidence. |
| Joint allocation creates a non-additive benefit | `HYPOTHESIS` | No result exists. It requires the matched factorial intervention and strongest composite. |
| Immutable provenance binding causally improves decisions | `HYPOTHESIS` | No result exists. It requires payload-held-constant interventions and a fixed store control. |
| Complete accounting changes the comparative conclusion | `HYPOTHESIS` | No result exists. Accounting alone is a validity requirement. |

No positive novelty claim in this review rests on the absence of an identical source.

## Terra-Engineering status

`docs/research/handoffs/2026-07-14-terra-engineering.md` was not present at the review freeze. Its later conclusions must be checked against B-01 through B-05 before integration, especially baseline feasibility, physical accounting, and the ownership of expiration/rollback actions.

## Files read

- `docs/research/CHARTER.md`
- `docs/research/STATE.md`
- `docs/research/NOVELTY.md`
- `docs/research/PROTOCOL.md`
- `docs/research/handoffs/2026-07-14-terra-evidence.md`
- `docs/research/handoffs/2026-07-14-sol-theory.md`
- GitHub issue `#1`, including acceptance criteria and stop conditions

## Files modified

- `docs/research/handoffs/2026-07-14-luna-cross-review.md` only

## Verification

- Read every required local file in full.
- Independently reopened the official primary records for Universal Transformers Need Memory, HOLA, MemOS, Mixture-of-Recursions, Engram, CAT, and Agentic ATLAS and checked that their current metadata and abstracts support the threat characterization.
- OpenReview presented a browser challenge for the Frey et al. record. Its exact method locator remains supported by the Terra-Evidence PDF read but was not independently reopened in this pass; it must remain `SECOND_PASS_PENDING` until the bibliography review confirms it.
- Compared the M1, M4, and confirmatory rules for logical consistency and traced every currently acceptable success path against the anti-assembly criterion.
- Searched explicitly for reasons to return `STOP`; they are recorded above rather than softened into recommendations.

## Required next action

Sol-PI should resolve B-01 through B-04 before merging issue #1. The resulting decision must say, without ambiguity: broad architecture claim `STOP`; research program `PIVOT` to a bounded M1 falsification; article eligibility `NOT ESTABLISHED`. No architecture implementation should begin until M1 defines a non-reducible technical object or selects the independent empirical route.

## Final disposition after integration

This disposition supersedes the earlier snapshot classifications in this handoff, including the historical note that Terra-Engineering was unavailable. It evaluates the integrated working tree after reading the completed Terra-Engineering audit.

| Finding | Status | Evidence and disposition |
|---|---|---|
| B-01, confirmatory success could bypass the anti-assembly interaction | `RESOLVED` | `CHARTER.md`, **Candidate contribution hypothesis** and **Confirmatory success threshold**, now states that quality/cost thresholds are necessary but insufficient and conjunctively requires a practically meaningful coordination interaction, same-component fixed/separated superiority, non-degenerate price response, and transfer. `PROTOCOL.md`, **Coordination identifiability**, and decision `0002`, **Anti-rewrite gate**, enforce the same rule. Terra-Engineering, **Recommended decision** and §5, independently requires the interaction interval and practical threshold. The exact numerical interaction threshold remains an explicit M2 freeze item, not an M0 omission. |
| B-02, joint versus separated control was non-identifiable | `RESOLVED` | `PROTOCOL.md`, **Coordination identifiability**, defines the required `O x G` intervention and mandates frozen observation interfaces, gradient paths, parameter counts, arbiter logic, and resource-price inputs. Decision `0002`, **Required discriminating controls** items 2 and 5, preserves matched capacity and the 2x2 study. Terra-Engineering §5 adds the complementary component factorial and identical-component contract. Exact interfaces remain correctly blocked on M2. |
| B-03, strongest composite was undefined | `RESOLVED` | `PROTOCOL.md`, **Required baselines**, names the closest-threat families, the fixed adaptive-stop composite, same-component separated control, matrix costing, and the prohibition on weak-baseline substitution. Decision `0002`, **Required discriminating controls** item 1, defines the mechanism-equivalent composite. Terra-Engineering §§2-4 provides the feasibility tiers and distinguishes full target-scale, reduced-scale mechanism checks, concept-only threats, and targeted subsystem tests. M2 must freeze the executable representatives and budget, but the M0 requirement is unambiguous. |
| B-04, Joint Memory Machine could manufacture architectural necessity | `RESOLVED` | `PROTOCOL.md`, **Joint Memory Machine**, now labels the family diagnostic only, forbids treating it as primary novelty evidence, requires hidden component-agnostic and natural transfer, and requires usefulness when the candidate loses. Terra-Engineering §5 and **Minimum viable M3/M4 sequence** add paired counterfactual indistinguishability and anti-copy constraints. Those construct-validity tests remain mandatory before M3, which is consistent with `Implementation authorization: NONE`. |
| B-05, ownership of expiration and rollback was contradictory | `RESOLVED` | `PROTOCOL.md`, **State and actions**, now defines expiration as deterministic and committed rollback as a privileged append-only environment/store event; neither is a learned controller action. This matches the controller action set in `CHARTER.md` and the Sol-Theory semantics. Terra-Engineering treats both as event-sourced oracle/generator transitions, not controller novelty. `NOVELTY.md` mentions them only as temporal tasks/interventions, so no action-set expansion remains. |
| B-06, the surviving delta was inferred from absence rather than defined as a hypothesis | `RESOLVED` | `CHARTER.md`, **Candidate contribution hypothesis**, explicitly says the policy is neither a technically established mechanism nor a positive novelty finding. `NOVELTY.md`, **Initial screen results**, calls it an unsupported hypothesis; **Initial gate decision** authorizes only M1. Decision `0002`, **Decision** and **Consequences**, requires M1 to find a technical disclosure gap plus a feasible discriminating experiment or return `STOP`. Terra-Engineering, **Recommended decision** and **M1/M2 blockers**, independently prohibits recombination survival and M3 authorization. |
| B-07, M0 source-of-truth integration | `RESOLVED` | `STATE.md`, **Current gate**, now records broad-claim `STOP`, program `PIVOT`, and article eligibility `NOT_ESTABLISHED`; **Active agents** marks every independent role complete; **Decisions** records the anti-rewrite controls and expiration/rollback ownership; **Next authorized action** limits work to PR/CI and a later M1 issue; and the M0 review/gate checklist is complete. `LITERATURE_MATRIX.csv` now maps P-001 through P-004 to the decision-critical prior work, differences, evidence IDs, discriminating experiments, and the primary composite. `CLAIM_LEDGER.csv` classifies the broad novelty claim as disputed and the narrow mechanism/accounting claims as unsupported. `EVIDENCE_LEDGER.csv` supplies versioned primary URLs and locators for every cited evidence ID. The remaining unchecked PR-CI item is the normal post-review merge condition, not a source-of-truth defect. |

### Engineering coherence

The integrated charter, novelty decision, and protocol are consistent with Terra-Engineering at the M0 authorization level:

- the sole recorded GPU cannot execute the confirmatory matrix, and no M3+ work is authorized;
- baseline tiers, matrix size, tuning ceilings, oracle information sets, factorial design, effect threshold, registry schema, and environment acceptance remain explicit M1/M2 blockers;
- the engineering proposal for a reduced one-size M4 screen is a feasibility stage, not the two-size article-eligibility replication required later;
- the engineering phrase permitting M2 formalization is necessarily conditional on passing M1, because `PROTOCOL.md`, **Staged program**, and decision `0002`, **Consequences**, explicitly prohibit immediate M2 work;
- the stronger paired-counterfactual and anti-copy requirements refine the future diagnostic benchmark and do not reauthorize it under M0.

No engineering finding weakens the anti-rewrite gate. It instead confirms that failure to fund and execute the same-component controls makes the architecture claim infeasible and therefore stoppable.

### Final verdict

Verdict: `MERGE_READY`.

B-01 through B-07 are resolved for M0. The scientific and governance content is ready for pull-request review and CI. Actual merge remains conditional on the required PR CI passing. This verdict does not authorize M2, M3, implementation, or training.
