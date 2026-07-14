# M1 Luna-QA adversarial cross-review

Status: `COMPLETE`

Date: `2026-07-14`

Issue: `#3`

Pull request: `#4`

Reviewed head: `9ac4949c56010764ff48f01159202fc9a6bdc2e2`, plus the uncommitted blocker-resolution diff inspected after that head

Verdict: `MERGE_READY`

Architecture-route verdict after review: `STOP`

Empirical-route verdict after review: `STOP`

Program disposition after review: `PIVOT`, conditional on a separate directional-thesis novelty audit

Directional-thesis novelty: `NOT_AUDITED`; article eligibility: `NOT_ESTABLISHED`

## 1. Objective

Independently challenge the integrated M1 decision and determine whether pull request #4 can merge without overstating search completeness, prior-art metadata, or the originality of the future direction-setting article.

The user objective is preserved exactly: a future article must not rewrite earlier work and must give future LLM research a falsifiable direction toward managed persistent state, memory, and adaptive computation. M1 is not allowed to treat that objective itself as an established novel contribution.

## 2. Scope and exclusions

The review covers `main...9ac4949`, the subsequent blocker-resolution diff, issue #3, pull request #4, all changed governance documents, decision 0003, the four M1 handoffs, the claim, evidence, and literature CSV files, the experiment registry, and `paper/references.bib`.

It checks the internal scientific gate, issue acceptance criteria, source qualifications, cross-file consistency, links, CSV references, BibTeX metadata, and CI evidence.

It does not perform the future directional-thesis literature audit, implement a model or benchmark, execute experiments, draft an article, or claim exhaustive bibliometric recall. No existing file was modified by this reviewer; this handoff is the only created file.

## 3. Questions tested

1. Does the mechanism route reduce to known constrained or budgeted control, with no relabeling-invariant technical novelty?
2. Does the empirical fallback expose any original architecture-neutral phenomenon?
3. Do the integrated artifacts consistently say `STOP` for both current routes and only conditional `PIVOT` for the program?
4. Are UMA, Gaikwad, TraceRetain, Memory-R1, and both Engram records qualified precisely?
5. Are `UNSUPPORTED` and `DISPUTED` used without implying that unrun experiments produced negative results?
6. Does the evidence package satisfy issue #3, or does it disclose any required protocol deviation?
7. Would any current wording let the directional article become a survey, roadmap, or renamed assembly?

## 4. Inputs and source versions

- Base commit: `93eacf5a22bf6b1ec951f8d43b526c12d96d278e` on `main`.
- Reviewed head: `9ac4949c56010764ff48f01159202fc9a6bdc2e2` on `agent/3-systematic-novelty-review`.
- Issue #3 and pull request #4, including the successful `validate` check at the reviewed head.
- UMA `arXiv:2602.18493v1`.
- Gaikwad `arXiv:2603.15658v1` and OpenReview `iGRGjdhl9r`.
- TraceRetain `arXiv:2606.29178v1` and OpenReview `9JiPHfleLn`.
- Memory-R1 `arXiv:2508.19828v5`.
- Bi-temporal Engram `arXiv:2606.09900v1` and Conditional Memory / Engram `arXiv:2601.07372v2`.
- All other source records and locators listed in the M1 handoffs and ledgers.

## 5. Work completed

1. Read the initial 16-file diff, the complete blocker-resolution diff, and every changed file in full.
2. Compared the integrated gate with issue #3 scope, nine acceptance criteria, and stop conditions.
3. Reconciled the four handoffs against the decision, state, charter, novelty review, protocol, registry, and ledgers.
4. Rechecked the decision-sensitive 2025-2026 qualifications against arXiv and official OpenReview records.
5. Parsed the three CSV files, checked identifiers and cross-references, and inspected all fourteen BibTeX entries.
6. Checked all local Markdown links and all 43 unique HTTP primary URLs in the evidence ledger.
7. Ran repository-native governance validation, unit tests, and whitespace validation.
8. Performed an adversarial pass for novelty leakage, false exhaustiveness, causal overclaiming, and survey/roadmap substitution.

## 6. Evidence and findings

### 6.1 Scientific gate

| Route | Finding | Evidence | Result |
|---|---|---|---|
| Mechanism | The typed joint policy has the exact decomposition `pi(k,du|h) = rho(k|h) q_k(du|h)` and remains a constrained POMDP/CMDP/BMDP or SMDP after ordinary state and action augmentation. The proposed artifacts specify no new algorithm, invariant, lower bound, or guarantee. | Reducibility handoff §§1-7; decision 0003 lines 22-35; UMA, GRU-Mem, AgeMem, Memory-R1, CPO, and BMDP records | `STOP` is supported with high confidence. |
| Empirical | WAIN-Core aggregates covered temporal operations; JMM encodes the candidate component ontology; accounting adds axes without an identified causal intervention, predictive law, or conclusion-changing result. | Empirical handoff §§4-10; decision 0003 lines 36-46; Ledger-QA, AMemGym, Memora, Supersede, bi-temporal Engram, Agent Memory, and Agent-Native records | `STOP` is supported with high confidence. |
| Directional pivot | The new objective is explicitly separated from the stopped architecture and marked unaudited. The charter requires an implementation-neutral contract and a falsifiable regime prediction, and rejects a survey, taxonomy, manifesto, maturity model, or migration diagram. | `CHARTER.md` lines 14 and 87-89; `STATE.md` lines 17-19 and 118-126; decision 0003 lines 57-65 and 69-88; `RISK_REGISTER.md` R-015 | Conditional `PIVOT` is internally coherent; novelty and article eligibility remain unestablished. |

The two `STOP` decisions are based on positive prior-art collisions and a formal reduction. They do not require an exhaustive absence claim. Missing search-log fields therefore do not rescue either stopped route.

### 6.2 Required source qualifications

| Source | Independent check | Integrated status |
|---|---|---|
| UMA | Section 4.4 prose gives `76.46`, Table 1 gives `77.36`, and the two-stage value is `66.29`. Only the direction of the comparison is safe. | Correctly quarantined in the librarian handoff, evidence row `EV-0031`, systematic handoff, novelty review, and decision. No exact effect magnitude is promoted. |
| Gaikwad | ArXiv records acceptance at an ICLR 2026 memory workshop. The paper evaluates oracle, fixed-subset, rule-based, and hybrid heuristic policies; learned routing is motivated as future work. | `EV-0043`, the literature matrix, and all three affected handoffs now consistently restrict the result to formalization plus fixed, oracle, and heuristic evaluation. |
| TraceRetain | ArXiv uses the broad label “Accepted at ICML 2026”; the official OpenReview venue lists `CATS@ICML26 Poster`. It is not an ICML main-track paper. | `EV-0044`, the literature matrix, and BibTeX correctly retain the workshop-poster qualifier. Other handoffs make no main-track claim. |
| Memory-R1 | First submitted in 2025, revised to v5 on 2026-01-14, with thirteen authors. Source year remains 2025. | Ledger and BibTeX year/version are correct. The author is now encoded as `Sch{\"u}tze`, which preserves “Schütze.” |
| Two Engram works | `2606.09900v1` is Liuyin Wang's bi-temporal agent-memory engine; `2601.07372v2` is Xin Cheng et al.'s conditional lookup memory. They are not a version chain. | Correctly distinguished in the librarian and systematic handoffs, evidence rows `EV-0022` and `EV-0040`, and the literature matrix. |

### 6.3 Claim classifications

- `CLM-006` remains `UNSUPPORTED`, correctly indicating that empirical superiority was never tested. It is not mislabeled as empirically refuted merely because policy-class novelty failed.
- `CLM-007` remains `UNSUPPORTED`, correctly indicating that no ranking reversal or predictive resource law was produced.
- `CLM-002`, `CLM-008`, and `CLM-010` are `DISPUTED` because direct prior work defeats current originality or eligibility claims without pretending to prove global non-existence.
- `CLM-009` is `UNSUPPORTED` with no evidence identifier, correctly preventing the owner's directional objective from becoming a novelty claim.

### 6.4 Issue #3 acceptance audit

| Acceptance criterion | Disposition | Reason |
|---|---|---|
| Exact source, query, date, result count, screening count, and adaptation rationale | `DEVIATION RECORDED` | The systematic handoff marks unavailable fields `NON DISPONIBLE`; decision 0003, `NOVELTY.md`, `PROTOCOL.md`, and `STATE.md` now state that this literal criterion was not completed and cannot support an exhaustive claim. |
| Every included claim has a primary record, version, and precise locator | `PARTIAL, DISCLOSED` | Decision-critical positive collisions are pinned and located. The complete reported 43-work corpus is not enumerated as a normalized table, and the corrected governance artifacts no longer represent it as an exhaustive systematic flow. |
| Reproducible deduplication and version chains | `PARTIAL, DISCLOSED` | Four major version chains and the Engram collision are explicit. The exact 43-work count remains an agent-reported normalization rather than an independently reconstructible review flow and is not used to infer absence. |
| One closed backward/forward snowball iteration | `PASS, BOUNDED` | The Memory-R1 to UMA lineage and an exact-title forward check are documented. The handoff correctly limits closure to the decision-critical lineage rather than exhaustive recall. |
| Narrow policy defined or reduced | `PASS` | The formal reduction and exact factorization are explicit. |
| Empirical route identifies a new phenomenon or is rejected | `PASS` | The route is explicitly rejected with positive benchmark and systems collisions. |
| Fixed and separated composites specified and costed sufficiently | `PARTIAL, ROUTE STOPPED EARLIER` | Comparator interfaces and minimum studies are specified qualitatively. Decision 0003 now records that no quantitative budget exists and that the experiment remains unexecuted because the route first fails the assembly stop condition. |
| Independent contradictory review resolves blockers | `PASS AFTER CORRECTION` | `B-01` through `B-03` were corrected and rechecked in the current diff. |
| State, novelty, ledgers, and decision agree | `PASS` | All integrated artifacts now separate the bounded positive-collision audit from exhaustive systematic-review completion and preserve `STOP / STOP / conditional PIVOT`. |

The repository took the correct resolution: it did not reconstruct missing counts or rerun an irrecoverable trace merely to support a conservative `STOP`. It records the acceptance deviation, labels the evidence as a bounded positive-collision audit, and forbids systematic-completeness and exhaustive-coverage claims. Closing issue #3 therefore records a negative novelty gate under disclosed limitations, not literal completion of every search-process criterion.

### 6.5 Artifact integrity

- CSV parsing returned 10 claims, 44 evidence rows, and 28 literature rows.
- No duplicate claim, evidence, or prior-work identifier was found.
- No missing claim-to-evidence, evidence-to-claim, or literature-to-evidence reference was found.
- All local Markdown links resolve.
- All 43 unique HTTP primary URLs in the evidence ledger returned a non-error status during the check.
- Fourteen BibTeX entries and fourteen closing entry braces are present; the Memory-R1 author-name encoding is corrected.
- `experiments/registry.yaml` consistently records `stopped_m1_no_experiments` with an empty experiment list.

## 7. Uncertainties and contradictions

- The search trace is a bounded positive-collision audit, not a completed systematic review or PRISMA record.
- The exact reported set of 43 normalized M1 works cannot be independently reconstructed from one enumerated corpus table.
- Recent 2026 arXiv and workshop records can change. Version pins and venue qualifiers must be rechecked at any later manuscript freeze.
- OpenReview and arXiv use different breadth for the TraceRetain venue label; the narrower official OpenReview workshop-poster label controls.
- Gaikwad's venue name varies slightly between arXiv metadata, the paper header, and OpenReview's abbreviated `MemAgents` label. All agree it is an ICLR 2026 workshop work, not a main-conference paper.
- No evidence in this PR establishes that the directional thesis, contract, regime boundaries, or predictions are original. This is an intentional open question, not a defect in the M1 `STOP` decision.

## 8. Files modified

- Created `docs/research/handoffs/2026-07-14-m1-luna-cross-review.md` only.
- No existing governance, evidence, bibliography, protocol, registry, code, benchmark, dataset, issue, pull request, or branch state was modified by this reviewer.

## 9. Verification executed

1. `python scripts/validate_governance.py`: passed.
2. `python -m unittest discover -s tests -v`: three tests passed.
3. `git diff --check main...HEAD`: passed.
4. CSV duplicate and cross-reference audit: passed.
5. Local Markdown-link audit: passed.
6. Evidence-ledger HTTP reachability audit: 43 of 43 non-error responses.
7. Primary metadata checks for UMA, Gaikwad, TraceRetain, Memory-R1, and both Engram records: completed.
8. Pull request #4 required `validate` check at the reviewed head: successful.

## 10. Resolved findings and recommended decision

Verdict: `MERGE_READY`.

No scientific or governance blocker remains in the reviewed correction diff. The three initially blocking findings are resolved as follows.

### B-01: Search-completeness and issue-acceptance overstatement

Severity: `HIGH`.

Status: `RESOLVED`.

Decision 0003 now contains a dedicated search-protocol deviation and explains why positive collisions are sufficient for the conservative `STOP`. `NOVELTY.md` and `PROTOCOL.md` carry the same limitation. `STATE.md` no longer checks a reproducible systematic closeout and describes the Terra handoff as a bounded positive-collision trace with targeted snowballing. The uncosted experiment is explicitly retired by the earlier assembly stop condition.

Administrative pre-merge cleanup: change the pull-request summary phrase “records the systematic novelty search” to “records the bounded positive-collision novelty audit and explicit search-protocol deviations.” The repository evidence already supplies the controlling qualification; this metadata edit must accompany the final PR update.

### B-02: Incorrect Memory-R1 author encoding in BibTeX

Severity: `MEDIUM`.

Status: `RESOLVED`.

`paper/references.bib` now uses `Hinrich Sch{\"u}tze`. The fourteen-entry structural check and explicit accent check pass.

### B-03: Gaikwad qualification is not consistent across handoffs

Severity: `MEDIUM`.

Status: `RESOLVED`.

The reducibility, empirical, and systematic handoffs now say that Gaikwad formalizes cost-sensitive store selection and evaluates oracle, heuristic, and fixed policies, not learned routing. The empirical overlap matrix separately attributes learned memory, update, and exit behavior to the other works. This narrowing does not weaken the formal reduction or either `STOP` decision.

## 11. Next authorized action

Integrate this handoff, mark the contradictory review complete in `STATE.md`, update the pull-request summary with the bounded-audit qualifier, commit and push the corrected diff, and require a fresh successful `validate` check on that new head. If the final pushed diff contains no scientific changes beyond this reviewed correction set, pull request #4 may merge.

After merge, a new issue and milestone may audit the directional thesis against memory-OS, agent-OS, stateful-agent, long-context, test-time-learning, systems-roadmap, position-paper, and migration-framework literature.

No article drafting, model implementation, benchmark implementation, training, or positive originality claim is authorized by this review.

## 12. Functional roles

Authoring functional role: `Luna-QA / Luna-RedTeam`, independent adversarial integration review.

Reviewed functional roles: `Sol-PI`, `Sol-Theory`, `Terra-Evidence`, `Terra-Engineering`, and `Luna-Librarian` artifacts.

Gate-owner follow-through: `Sol-PI` must perform the mechanical state, PR-description, CI, and merge checks. A new scientific review is required only if the final diff changes the reviewed evidence or the `STOP / STOP / conditional PIVOT` separation.
