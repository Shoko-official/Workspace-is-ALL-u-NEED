# M1g Problem-First Scoping Log

Cutoff: `2026-07-15`
Issue: [#25](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/25)
Method: concrete incident, two-factor causal-necessity test, complete prior-object
crosswalk, then targeted primary-source and generic-reduction review

## Scope

M1g searched for at most one irreducible failure law outside all 73 M1c-M1f
formulations. It began from deployment incidents rather than components:
in-flight revocation, post-internalization deletion, forked continuations,
purpose-misaligned influence, real-time snapshot staleness, persistent service
disparity, undeclared causal state, and persistent cost amplification.

For each incident, persistence and adaptive computation had to be separately
causally necessary. The strongest comparator received the same event stream,
observations, state, randomness, transcript, feedback, latency, and total
resource budget. Architecture assembly, weak comparators, generic theory with
LLM labels, benchmark-cell novelty, and an empirical search before object
admission remained excluded.

The search is targeted and non-exhaustive. Every disposition rests on a fixed
counterexample, positive primary record, exact identity, generic reduction, or
earlier-object crosswalk. Absence from search results is never evidence.

## Recorded discovery queries

Search-result counts are not used. Query wording was adapted only to reach
canonical primary records and full texts.

| Problem | Query family | Resolution path |
|---|---|---|
| In-flight revocation | `revocation in flight computation stale commit linearizability invalidation epoch replay` | Linearizability, dependency invalidation, optimistic validation, and M1c replay objects |
| Internalized deletion | `machine unlearning behavioral audit deletion parameters memory cache privacy` | Existing unlearning records plus the bounded convex-model audit/privacy theorem |
| Forked continuation | `fork rollback cloned state unique continuation non equivocation agent identity` | Lightweight Collective Memory, fork-linearizability, at-most-once effects, and Dissociative Identity |
| Scoped influence | `persistent LLM memory contextual integrity cross user contamination tool drift purpose limitation` | CIMemories, cross-user contamination, Memory-Induced Tool-Drift, Intent Legitimation, and IFC |
| Snapshot staleness | `real time reasoning evolving environment stale observation deliberation persistence probability` | Real-Time Reasoning Agents and Yamada's success-probability deliberation control |
| Service disparity | `fair resource allocation sequential MDP persistent history compute allocation disparity` | Fair weakly coupled MDP allocation and generic local stability |
| Declared-state completeness | `observational determinism hidden state probabilistic noninterference black box audit` | Hyperproperties, probabilistic non-interference, replay, and verification |
| Cost amplification | `LLM agent denial of service persistent resource accumulation quota resource principal` | AgentDoS and Resource Containers |

Current-date discovery also screened records available through 15 July 2026.
Recent preprints were version-pinned and used only for claims visible in the
inspected version.

## Exact primary-record resolutions

### Concurrent revocation and forked state

Herlihy and Wing define linearizability by assigning each concurrent operation
an effect point between invocation and response and prove locality of the
condition (`EV-0170`, abstract and Sections 2-3). Epoch validation, cancellation,
or serialization of revocation against commit is therefore an instance of a
generic concurrent-object contract, not a new adaptive-reasoning invariant.

Brandenburger et al. define rollback and forking detection with lightweight
collective memory and fork-linearizability (`EV-0171`, Sections II-IV). Hu,
Rong, and Van Kleek independently identify copyability, modular mutability, and
weak sanction continuity as obstacles to identity-based reputation for language
model agents (`EV-0172`, abstract and Sections 1-3). A unique effect-capable
continuation needs communication, an at-most-once effect service, or an external
non-clonable anchor. Adaptive computation is not required for the failure.

### Deletion after internalization

Existing machine-unlearning records already treat removal from learned state
and synchronized parameter-memory dependencies (`EV-0091`; `EV-0092`). Tang,
Joshi, and Kundu prove a behavioral-audit privacy trade-off for their declared
convex-model setting (`EV-0177`, Theorem 3.3, PDF pages 5-6). M1g does not
promote that bounded theorem to a universal audit impossibility. Its deletion
residual is the ordinary comparison with canonical retraining, and no stronger
unlearning or verification result was derived.

### Purpose and context boundaries

CIMemories measures contextual-integrity violations in persistent-memory
assistants (`EV-0173`). No Attacker Needed isolates benign cross-user
contamination in shared state (`EV-0174`). Memory-Induced Tool-Drift evaluates
out-of-scope persistent influence on tool arguments across 105 scenarios, seven
models, and three memory architectures (`EV-0175`). Intent Legitimation reports
that benign personalization memories can bias intent inference and increase
harmful-query success (`EV-0176`).

These positive incidents matter operationally, but the proposed zero-flow law
is ordinary probabilistic non-interference with an explicit declassification
boundary. Hyperproperties and f-secure provide the generic two-trace and IFC
objects (`EV-0084`; `EV-0156`).

### Real-time snapshot survival

Wen et al. directly study agents whose environment changes while reasoning and
the resulting quality-latency tension (`EV-0178`). Yamada models the probability
that a plan remains successful in a dynamic environment and uses it to control
the planning-to-execution switch (`EV-0179`, PDF pages 4 and 8).

For declared anytime quality `q(b)`, survival `S(tau(b))`, and cost `c(b)`, the
M1g objective `q(b)S(tau(b))-c(b)` yields its stopping inequality by ordinary
differentiation. It is exact, but compositional and older than LLM agents.
Persistent governed state is not necessary because a transient sensor snapshot
has the same law.

### Fairness and resource amplification

Tu et al. formulate sequential fair allocation in weakly coupled MDPs with a
generalized-Gini objective and a permutation-invariant reduction for the
homogeneous case (`EV-0180`, PDF pages 1 and 4). A local disparity multiplier is
the generic Jacobian stability criterion inside such a sequential control
problem.

AgentDoS examines resource-lifecycle denial of service across 20 open-source
agents, including persistent accumulation and quota mitigations (`EV-0181`, PDF
pages 8 and 14-15). Resource Containers separates resource principals from
execution contexts for explicit accounting and scheduling (`EV-0182`, Sections
2, 4, and 6). M1g's horizon-linear lower bound follows immediately from its
positive per-round activation probability and marginal-cost assumptions; a
lifetime principal quota supplies the bounded branch by construction.

### Declared-state completeness

The requirement that equal declared states induce equal continuation-trace laws
is observational determinism or probabilistic non-interference, already covered
by Hyperproperties (`EV-0084`). A finite black-box test can falsify but cannot
universally certify that property for unrestricted implementations. A complete
declared transition system, canonical replay, or a restricted verified class is
the ordinary constructive branch.

## Resolution notes

1. Six of eight incidents fail the preregistered two-factor necessity test.
   Revocation, fork uniqueness, purpose control, declared-state completeness,
   and persistent cost abuse do not require adaptive computation; snapshot
   staleness does not require persistent governed state.
2. Passing two-factor necessity is necessary, not sufficient. P02 is machine
   unlearning, and P06 is fair sequential control plus a generic stability
   derivative.
3. P03 is the closest object outside the exact wording of the earlier 73, but
   free state cloning makes local unique descent impossible without ordinary
   coordination, continuity, or an external non-clonable resource.
4. The P05 derivative and P08 expectation bound are useful engineering checks.
   Their exactness does not make them new scientific laws.
5. CIMemories, cross-user contamination, Tool-Drift, the unlearning audit, and
   AgentDoS are recent preprints or prepublication records where noted. They are
   not treated as independently replicated empirical truth.
6. The 73-row crosswalk contains explicit `NO_REOPENING` entries rather than
   forcing thematic overlap. That label is not a novelty verdict.

## Search outcome

Eight incident-first problems were tested. None passed admission:

- six fail the causal necessity of one of the two required factors and also
  meet direct records or generic reductions;
- deletion after internalization is machine unlearning plus a bounded
  behavioral-audit question;
- history-dependent disparity is generic dynamical stability inside fair
  sequential resource allocation.

The outcome is `ACCEPTED_STOP`. Zero objects are admitted, the experiment
registry remains empty, and no article, implementation, benchmark, proof
project, training run, experiment, paid compute, or submission is authorized.
Independent scientific, bibliographic, and governance reviews all returned
`PASS` on scientific commit
`94af4acb8ef2db505e9596c0946c618fc136c641`. Its tree was rebased byte-for-byte
as `64b79fbc2296d618ba5b5ec4b8c9e0a7fceecea6`; protected PR #26 passed and
merged as `777293f87a79d95d39a516097be2246716dd55d5`.
