# M1b Directional-Thesis Search Protocol

Status: `PREREGISTERED_BEFORE_ROOT_SEARCH`
Issue: `#5`
Milestone: `M1b - Managed-state transition thesis novelty gate`
Recorded: `2026-07-14`
Search freeze: `2026-07-14`

## Question

Does prior work already entail an implementation-neutral rule `T(Omega, G, B)` that uses pre-outcome workload properties, a state-and-computation guarantee contract, and a vector physical-resource envelope to predict when context-only processing, governed persistent state, fixed computation, or bounded adaptive computation should be feasible or Pareto-preferable?

The audit tests a candidate contribution. It does not assume that the rule is novel, that persistent state is generally beneficial, or that any architecture should be built.

## Candidate objects

1. `Omega`: pre-outcome workload descriptors that change a declared feasibility or efficiency boundary.
2. `G`: implementation-neutral semantic guarantees with observable violations and permitted failures.
3. `B`: non-collapsed physical resource limits and lifecycle costs.
4. `A`: an adequacy relation that reports satisfaction, violation, incomparability, or abstention for an implementation under `(Omega, G, B)`.
5. `T`: a transition rule that predicts obligations or rank changes without returning an architecture name.
6. Boundary predictions: ex ante, falsifiable feasibility or efficiency statements with negative regimes.

## Primary sources

- arXiv API and primary arXiv records;
- OpenReview and official conference proceedings;
- ACL Anthology, PMLR, NeurIPS, ACM, IEEE, USENIX, and publisher records;
- official standards, specifications, or project technical reports when they define a decision-critical contract;
- official repositories only for details absent from the primary paper.

OpenAlex and Crossref may support metadata and forward-citation discovery. Search-engine result pages may support discovery, but no claim may rely on them.

## Registered query families

The exact source-specific strings and counts belong in `M1B_SEARCH_LOG.csv`. Adaptations may change syntax, not concepts.

1. `("memory operating system" OR "memory OS") AND ("large language model" OR LLM OR agent)`
2. `("agent operating system" OR "AI operating system" OR AgentOS OR AIOS) AND (memory OR state OR context)`
3. `("stateful agent" OR "stateful language model" OR "stateful LLM") AND (memory OR context OR persistence)`
4. `("persistent memory" OR "long-term memory") AND ("language model" OR "LLM agent") AND (framework OR system OR contract)`
5. `("test-time learning" OR "test-time training" OR "test-time compute") AND ("language model" OR transformer) AND (memory OR state OR scaling)`
6. `("adaptive computation" OR "dynamic depth" OR "early exit" OR ponder) AND ("language model" OR transformer) AND (cost OR budget)`
7. `("value of computation" OR metareasoning OR "rational metareasoning") AND (agent OR "language model")`
8. `("memory hierarchy" OR caching OR "working set") AND ("language model" OR "LLM agent") AND (cost OR allocation)`
9. `("temporal memory" OR "versioned memory" OR bitemporal OR provenance OR revocation) AND ("LLM agent" OR "language model")`
10. `("resource allocation" OR Pareto OR "resource envelope") AND memory AND ("language model" OR agent)`
11. `("service level objective" OR contract OR invariant OR adequacy) AND state AND ("AI agent" OR "language model")`
12. `("position paper" OR roadmap OR agenda OR framework) AND ("agent memory" OR "stateful AI" OR "LLM memory")`

Exact-title searches and identifier resolution are registered adaptations for seeds and newly discovered decision-critical records.

## Seed families

- MemGPT and Letta;
- MemOS;
- AIOS, AgentOS, and other agent operating-system proposals;
- UMA, AgeMem, Memory-R1, GRU-Mem, Agent Memory, and Agent-Native Memory System;
- recurrent, compressed-state, external-memory, and long-context systems retained in M0/M1;
- Adaptive Computation Time, Universal Transformer, PonderNet, early-exit and dynamic-depth work;
- test-time scaling, test-time learning, and metareasoning/value-of-computation work;
- temporal databases, event sourcing, provenance, caching, working-set, constrained-control, and multiobjective decision theory.

Seeds are discovery inputs, not evidence until their primary records are read and pinned.

## Inclusion

- primary or official record accessible in full;
- defines, implements, proves, or evaluates a candidate object, a closest competing abstraction, a regime boundary, or a negative case;
- contains enough detail for an overlap and falsifier assessment;
- position or agenda work only when it makes the same directional or contract claim being audited.

## Exclusion

- secondary summaries where primary material is available;
- marketing pages, unsourced taxonomies, or architecture lists without a technical decision rule;
- memory used only metaphorically;
- generic RAG work with no state lifecycle, allocation, contract, or boundary result;
- duplicates and mirrors after the canonical version is retained;
- inaccessible full text after a logged attempt.

## Deduplication and versions

Deduplicate by DOI, then canonical arXiv or proceedings identifier, then normalized title and author set. Preserve a version chain when authors, claims, experiments, or venue status change. Every decision-critical citation records the exact version read, access date, and locator.

## Snowballing and closure

For each included seed and newly included family:

1. inspect decision-relevant references;
2. inspect available forward citations or exact-title successors;
3. inspect the official project record for associated technical reports;
4. record the discovery edge;
5. stop only after one complete iteration adds no new eligible abstraction or framework family.

Closure applies to eligible families, not to a claim of exhaustive recall.

## Extraction

Record the technical object, architecture dependence, workload variables, guarantee semantics, resource axes, decision timing, abstention behavior, feasibility/efficiency distinction, prediction, falsifier, negative regime, evaluated systems, measurements, effect or theorem, limitations, version, locator, and discovery path.

## Anti-rewrite gate

Every residual must pass component erasure, label substitution, strongest-composite reduction, generic-theory reduction, ex ante boundary, rank-order, negative-regime, orthogonal-instantiation, independent-falsifier, and agenda-derivation tests from issue #5.

The route returns `STOP` when the residual is vocabulary, aggregation, advice, a roadmap, a taxonomy, a generic theory relabeling, or a post hoc explanation. It returns `PIVOT` only for one named narrower object with an observable distinction. `GO` requires every issue #5 acceptance criterion.

## Deviations

Any unavailable count, blocked database, syntax adaptation, inaccessible record, incomplete screening field, or search interruption must be recorded at occurrence. Missing values are `NON DISPONIBLE`; they are never reconstructed from memory or inferred from a visible result page.

## Final execution disposition

The twelve broad arXiv queries retain live result totals and the five titles screened for each query, but their per-title inclusion and exclusion decisions were not preserved. Those fields are frozen as `NON DISPONIBLE`; broad-family screening and snowball closure are not claimed. Four narrow joint-boundary queries and fifteen direct identifier resolutions provide the decision-critical positive collisions.

This deviation prevents exhaustive-recall and absence-of-prior-art claims. It does not weaken a `STOP` based on direct anticipation or generic reconstruction. The log is a reproducible execution trace with bounded missing screening data, not a completed systematic review.

The preregistered `A` and `T` notation above is preserved as protocol history. The final audit separates ground-truth `Adeq`, evidence `Cert`, pairwise `Cmp`, the ideal selector `T*`, and a possible calibrated estimator `T_hat`; this is a typing correction, not a post hoc novelty claim.
