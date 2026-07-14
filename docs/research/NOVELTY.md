# Novelty Review

Status: `SEARCH_NOT_EXECUTED`
Protocol version: `0.1.0`
Protocol recorded: `2026-07-14`
Candidate gate: `M1`

## Review question

Does prior work already disclose or empirically establish a single learned controller that jointly allocates explicit, limited budgets across a bounded attention workspace, versioned episodic reads and writes, fixed-size compressed-state updates, bounded recurrent compute, verification, and halting, with complete physical resource accounting and provenance interventions?

An absence of an identical title or diagram is not evidence of novelty. A component list is not a contribution unless a discriminating interaction, objective, constraint, or empirical result survives the strongest composite baseline.

## Candidate properties to test

| ID | Candidate property | Novelty burden | Minimum discriminating comparison |
|---|---|---|---|
| P-001 | One controller allocates a shared explicit budget jointly across workspace, episodic memory, compressed state, recurrent compute, verification, and halt actions | Show that prior controllers do not already cover the same action/resource space and that joint training matters | Joint controller versus fixed composite and separately trained per-resource controllers at matched budgets |
| P-002 | Episodic mutations are versioned and transactional, with provenance bound immutably to retained content | Show a technical distinction from recurrent memory, kNN memory, neural long-term memory, and agent memory/versioning systems | Insert/supersede/revoke/expire/rollback tasks plus provenance-only interventions |
| P-003 | The controller is evaluated as a constrained resource allocator rather than only as a quality router | Show complete accounting beyond theoretical FLOPs or parameter count | Pareto fronts including indexing, transfers, writes, storage, compilation, warm-up, latency, HBM, and energy |
| P-004 | The full system creates an interaction unavailable from any component alone | Reject additive assembly as the explanation | Full factorial ablations and fixed composite baseline, with preregistered interaction analysis |

## Preregistered search plan

### Sources

Search primary records in arXiv, ACL Anthology, PMLR, OpenReview, NeurIPS proceedings, ACM Digital Library, IEEE Xplore, and official project repositories. Crossref and OpenAlex may be used for metadata and forward-citation discovery, but final support must point to a primary paper or official record where available.

### Search window

- Coverage: database inception through `2026-07-14`.
- Initial execution target: M1 issue, after this protocol is merged.
- Update search: immediately before protocol freeze and immediately before manuscript submission.

### Query families

Queries are case-insensitive and adapted only for database syntax. Every adaptation and result count must be logged.

1. `("global workspace" OR "shared workspace" OR "active workspace") AND (transformer OR attention OR neural)`
2. `(transformer OR language model) AND ("external memory" OR "episodic memory" OR "persistent memory" OR "memory transformer")`
3. `(attention AND (Hopfield OR "associative memory"))`
4. `("state space model" OR SSM OR Mamba) AND (attention OR memory OR hybrid)`
5. `("adaptive computation" OR "ponder" OR "dynamic depth" OR recurrent) AND (transformer OR language model)`
6. `(router OR controller OR policy) AND (memory AND compute AND budget)`
7. `(versioned OR temporal OR transactional OR revoke OR rollback) AND (neural memory OR agent memory OR language model)`
8. `(provenance OR citation OR source attribution) AND (memory OR retrieval) AND (language model OR transformer)`
9. `(Pareto OR "resource allocation" OR "compute budget") AND (attention OR memory OR transformer)`

### Seed set

The supplied research program names the following seeds. They are search inputs, not verified evidence: Attention Is All You Need; Hopfield Networks Is All You Need; Shared Global Workspace; Memory Transformer; Recurrent Memory Transformer; Memorizing Transformers; Mamba; Mamba-2; Jamba; Samba; Hymba; Titans; ATLAS; Universal Transformer; Adaptive Computation Time; PonderNet; Universal Transformers Need Memory; Zoology/MQAR; RULER; BABILong; NoLiMa; MemGPT; and versioned agent-memory systems.

### Snowballing

For every included seed and every newly included paper:

1. inspect references for backward snowballing;
2. inspect citing records for forward snowballing;
3. inspect official repository documentation and associated technical reports;
4. record the discovery path and stop only after one full iteration yields no new eligible mechanism family.

### Inclusion criteria

- primary research paper, official proceedings record, or official repository/specification;
- implements, formalizes, or evaluates at least one candidate mechanism or a directly competing composite;
- sufficient technical detail to map overlap and differences;
- accessible full text or official specification;
- any language, provided metadata and relevant passages can be verified.

### Exclusion criteria

- commentary, marketing material, unsourced summaries, or duplicate versions with no relevant change;
- memory used only as a loose metaphor without a mechanism;
- retrieval-augmented generation work with no relevant memory-management, routing, compute-allocation, or provenance mechanism;
- unavailable full text after a documented access attempt;
- benchmark leaderboard entries without an attributable method description.

### Deduplication and versioning

Deduplicate first by DOI, then arXiv identifier, then normalized title and author set. Retain a version chain when claims or experiments differ. Prefer the final peer-reviewed version for claims and preserve the arXiv version when it contains material omitted from proceedings.

## Extraction schema

For each included work record architecture, state variables, persistence semantics, read/write actions, versioning, provenance, controller inputs/actions, budget constraints, adaptive-depth bounds, training objective, complexity assumptions, resource accounting, datasets, baselines, ablations, effect sizes, limitations, exact locators, and verification status.

## Decision rule

- `GO`: at least one candidate property remains technically distinct and has a feasible experiment that can distinguish it from the strongest known composite.
- `PIVOT`: the broad architecture is known, but a narrower property or evaluation contribution remains testable.
- `STOP`: no technically meaningful distinction survives, or no feasible experiment can identify it.

No novelty decision has been made in this document.
