# M1 Luna-Librarian metadata and provenance audit

Status: `COMPLETE`

Date: `2026-07-14`

Issue: `#3`

Milestone: `M1`

Architecture-route verdict: `STOP`

Empirical-route verdict: `STOP`

Directional-pivot status: `NOT_AUDITED`

## 1. Objective

Independently reconcile the decision-critical bibliographic metadata, version pins, venue labels, author counts, operation names, and precise locators used by the three M1 handoffs.

Determine whether those metadata support the current gate without silently upgrading workshop papers, preprints, fixed policies, or internally contradictory measurements.

The decisive result is that the metadata are auditable enough to support the present `STOP`, provided the UMA magnitude and the Gaikwad routing interpretation remain quarantined.

## 2. Scope and exclusions

The scope is limited to the three local M1 handoffs and `docs/research/EVIDENCE_LEDGER.csv` as they existed during this audit.

The review covers source identity, version, year, author count, venue status, operation vocabulary, measurement locator, and claim-strength calibration.

No network lookup, forward citation search, patent search, source-PDF download, experimental execution, model training, benchmark implementation, or directional-pivot literature review was performed.

This is a librarian and provenance audit, not a new systematic-search completeness certificate.

## 3. Hypotheses and questions tested

1. Are the sources that decide M1 uniquely identified and pinned to defensible versions?
2. Do the cited locators support the strength of the claims made in the handoffs?
3. Are venue and publication labels separated from arXiv version metadata?
4. Are similarly named works, especially the two Engram records, correctly disambiguated?
5. Do any contradictions or category errors weaken the `STOP` decision?
6. Has the direction-setting pivot received an audit sufficient for a novelty claim?

## 4. Inputs and source versions

- `docs/research/handoffs/2026-07-14-m1-sol-reducibility.md`, local M1 reducibility snapshot.
- `docs/research/handoffs/2026-07-14-m1-terra-empirical-route.md`, local M1 empirical-route snapshot.
- `docs/research/handoffs/2026-07-14-m1-terra-systematic-search.md`, local M1 systematic-search snapshot.
- `docs/research/EVIDENCE_LEDGER.csv`, 42 parsed evidence rows, `EV-0001` through `EV-0042`.
- Decision-critical pins checked: AgeMem `2601.01885v2`; Memory-R1 `2508.19828v5`; UMA `2602.18493v1`; GRU-Mem `2602.10560v1`.
- Additional pins checked: Gaikwad `2603.15658v1`; Agent Memory `2606.06448v1`; TraceRetain `2606.29178v1`; Agent-Native `2606.24775v1`.

The three input handoffs are integration artifacts whose SHA-256 values can change when their pending edits are integrated.

This handoff therefore certifies no input-handoff hash; only its own finalized file hash is reported out of band in the delivery message.

## 5. Work completed

1. Read all three M1 handoffs in full and mapped their decisive source claims to the local evidence ledger.
2. Parsed the ledger as CSV and confirmed its 42-row extent and terminal identifier `EV-0042`.
3. Reconciled arXiv base identifiers, exact versions, source years, revision dates, author counts, venues, and OpenReview identifiers.
4. Compared claim wording against the cited operation sets, experimental policy classes, and measurement locators.
5. Isolated contradictions, overstatements, title collisions, and venue-category risks from the gate logic.
6. Reassessed whether the corrected metadata alter the architecture, empirical, or directional-pivot decisions.

## 6. Evidence with precise locators

### 6.1 Control and learned memory operations

- Constrained Policy Optimization is correctly located at §4, PDF p. 2; it supports neural optimization with auxiliary cost constraints, not a pathwise hard-ceiling guarantee (`EV-0035`).
- AgeMem `arXiv:2601.01885v2`, §3.1 and Table 1, PDF pp. 4-5, exposes exactly `ADD`, `UPDATE`, `DELETE`, `RETRIEVE`, `SUMMARY`, and `FILTER` (`EV-0033`).
- Memory-R1 is `arXiv:2508.19828v5`, has 13 authors, retains source year `2025`, and was revised `2026-01-14`; the decision locators are §§3.1-3.3, Tables 2-4, and Appendices B and D (`EV-0034`).
- GRU-Mem is pinned to `arXiv:2602.10560v1`; §§3.1-3.2.1, PDF pp. 4-6, support learned recurrent update and exit gates (`EV-0032`).
- Gaikwad, `arXiv:2603.15658v1`, is accepted to the ICLR MemAgents workshop.
- Gaikwad evaluates oracle, heuristic, and fixed policies; it does not establish a learned store router.
- Accordingly, the handoff phrase “a policy selects among four stores” is safe only as task formalization, not as evidence of learned routing.

### 6.2 Systems characterization and accounting

- Agent Memory, `arXiv:2606.06448v1`, has 9 authors (`EV-0041`).
- Its §3.3, PDF p. 5, measures energy, GPU power, HBM, and latency; these are direct accounting anticipations, not inferred proxies.
- Agent-Native Memory System is pinned to `arXiv:2606.24775v1`; §§3-5 cover maintenance, updates, stability, and cost-performance across twelve systems plus two reference baselines (`EV-0042`).
- These records support the claim that adding axes to an accounting vector is insufficient unless it changes a scientific conclusion.

### 6.3 Temporal memory, benchmarks, and venues

- TraceRetain is `arXiv:2606.29178v1` and appears as a Poster at CATS@ICML26 through OpenReview `9JiPHfleLn`.
- TraceRetain must not be represented as a main-track ICML paper.
- The bi-temporal Engram, `arXiv:2606.09900v1`, is a distinct work from Conditional Memory / Engram, `arXiv:2601.07372v2` (`EV-0040`, `EV-0022`).
- The former concerns append-only episodes, provenance, supersession chains, and point-in-time filtering; the latter concerns scalable conditional lookup memory.
- AMemGym's arXiv author display begins `Cheng Jiayang`; the work is associated with ICLR 2026 and its benchmark locators are §§3.1-3.4, §§4.2-4.4, and §5 (`EV-0037`).
- Memora is `arXiv:2604.20006v1`, accepted to Findings of ACL 2026; §§3.2-4.2 support obsolete-memory and invalidation evaluation (`EV-0038`).

### 6.4 UMA contradiction quarantine

- UMA is pinned to `arXiv:2602.18493v1` (`EV-0031`).
- Its §4.4 prose reports a unified aggregate of `76.46`.
- Table 1 reports the corresponding unified aggregate as `77.36`.
- The disclosed decoupled baseline is `66.29`.
- The exact unified magnitude is therefore internally contradictory and must not be quoted as a settled value.
- Only the direction “unified exceeds decoupled in the disclosed comparison” is retained.
- That directional result anticipates the proposed comparison but does not establish irreducibility, causal interaction, or a new control object.

## 7. Uncertainties and contradictions

- UMA's `76.46` versus `77.36` conflict is a source-internal contradiction; the magnitude is quarantined.
- Gaikwad's evaluated policies are oracle, heuristic, and fixed, so any learned-router interpretation is rejected.
- TraceRetain's workshop-poster status must remain distinct from ICML main-track acceptance.
- The ledger does not currently contain dedicated rows for Gaikwad or TraceRetain, although both are decision-relevant in the M1 handoffs.
- Recent 2026 preprints can change version or venue; every future citation must retain an explicit version pin and access date.
- The bounded local audit cannot establish exhaustive literature coverage or novelty for the directional pivot.

None of these qualifications rescues the stopped routes: they narrow claim strength without removing the positive collisions from UMA, GRU-Mem, AgeMem, Memory-R1, temporal-memory benchmarks, and systems-accounting work.

## 8. Files modified

- Created `docs/research/handoffs/2026-07-14-m1-luna-librarian.md` only.
- No ledger, bibliography, decision record, protocol, registry, source handoff, code, benchmark, or dataset was modified.

## 9. Verification executed

1. Parsed `EVIDENCE_LEDGER.csv` successfully as 42 records from `EV-0001` through `EV-0042`.
2. Checked the required evidence identifiers, version fields, author lists, years, locators, and notes against the three handoffs.
3. Checked all twelve required handoff sections against `docs/research/handoffs/README.md`.
4. Checked final line count against the required 100-160-line range.
5. Ran whitespace and patch validation with `git diff --check`.
6. Computed SHA-256 only after finalizing the file; the digest is intentionally absent here to avoid self-referential hash invalidation.

## 10. Recommended decision

Metadata decision: `VERIFIABLE WITH EXPLICIT QUARANTINES`.

Retain `STOP` for the architecture route and `STOP` for the empirical benchmark/accounting fallback.

The positive-collision basis remains sufficient after correction; the UMA contradiction affects magnitude only, and Gaikwad is not needed as a learned-router precedent.

Keep the directional pivot at `NOT_AUDITED`, with novelty and publication eligibility `NOT_ESTABLISHED`.

## 11. Next authorized action

After independent gate review, integrate the metadata corrections into the ledgers and decision artifacts without weakening version or venue qualifiers.

Do not implement, train, benchmark, or draft a paper under the stopped routes.

Open any direction-setting route only under a new issue, charter, contribution class, systematic prior-art protocol, falsifiable theses, and anti-rewrite gate.

## 12. Functional roles

Authoring functional role: `Luna-Librarian`, independent metadata, version, venue, locator, and provenance reconciliation.

Independent reviewing role required before gate use: `Sol-PI` or another role distinct from Luna-Librarian; that review is not claimed by this handoff.
