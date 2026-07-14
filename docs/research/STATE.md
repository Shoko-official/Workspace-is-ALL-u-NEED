# Research State

Snapshot: `2026-07-14`
State schema: `1`
Operational status: `IN_PROGRESS`

## Current milestone

`M1 - Systematic novelty review`

M0 was completed by merged [PR #2](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/pull/2); issue #1 and milestone M0 are closed.

## Current gate

`M1-NARROW-NOVELTY-REVIEW`

The broad architecture novelty claim is `STOP`. The research program is `PIVOT` to a bounded M1 systematic review of one narrow coordination hypothesis or an independent empirical route. The current architecture paper is `NOT_ELIGIBLE`; eligibility of a future narrowed paper is `NOT_ESTABLISHED`. Training, benchmark implementation, M2 formalization, and substantive model implementation are not authorized.

## Active issues

| Issue | Milestone | Branch | Status |
|---|---|---|---|
| [#3 M1: test the narrowed contribution against prior art](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/3) | M1 | `agent/3-systematic-novelty-review` | Active |

## Capability audit

Exact Sol, Terra, and Luna model selection is not exposed by this runtime. Functional roles are retained without claiming an unverifiable model identity.

| Requested role | Requested model | Actually available | Selection controllable? | Status | Fallback |
|---|---|---|---|---|---|
| Sol-PI | GPT-5.6 Sol Ultra | Runtime-managed root agent; exact model identity not exposed | No | `NON CONTROLLABLE` | Root agent acts as PI, integrator, and gate owner |
| Sol-Theory | GPT-5.6 Sol Ultra/Max | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Bounded theory and contradiction review |
| Terra-Evidence | GPT-5.6 Terra Max | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Primary-source novelty review |
| Terra-Engineering | GPT-5.6 Terra Max | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Protocol and resource-accounting review |
| Luna-Librarian | GPT-5.6 Luna | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Citation and metadata verification pass |
| Luna-QA | GPT-5.6 Luna High/Max | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Independent validation pass when scheduled |
| Luna-RedTeam | GPT-5.6 Luna High | Runtime-managed subagent; exact model identity not exposed | No | `NON CONTROLLABLE` | Adversarial review when scheduled |

## Active agents

| Functional role | Assignment | Status | Handoff target |
|---|---|---|---|
| Sol-PI | M1 integration and gate ownership | Active | Issue #3 and M1 decision PR |
| Terra-Evidence | Reproducible narrowed systematic search and snowballing | Active | `handoffs/2026-07-14-m1-terra-systematic-search.md` |
| Sol-Theory | CMDP/router reducibility and non-factorization audit | Active | `handoffs/2026-07-14-m1-sol-reducibility.md` |
| Terra-Engineering / Luna-RedTeam | Component-agnostic benchmark and outcome-changing accounting audit | Active | `handoffs/2026-07-14-m1-terra-empirical-route.md` |

## Input inventory

| Input | Status | Evidence |
|---|---|---|
| Research-program text | `AVAILABLE` | `pasted-text.txt`, SHA-256 `F5B682FA743F15D8AEB6B125B1BC2AA0B7E99DF76CE70BFF31ABCE295C5F4714`, read in full on 2026-07-14 |
| Underlying report on Transformer/LLM limitations referenced by the program | `INPUT_MISSING` | Attachment directory contains only `pasted-text.txt` |
| Repository source/history | `AVAILABLE` | Repository was empty; root commit `6e6d45f` initialized `main` under issue #1 |
| External datasets and checkpoints | `NOT ACQUIRED` | No manifests or license review exist |

## Repository audit

- Repository: `Shoko-official/Workspace-is-ALL-u-NEED`, public.
- Initial state: empty, no commits, branches, workflows, issues, milestones, or rulesets.
- GitHub access: administrator permission through authenticated local GitHub CLI.
- Secret scanning and push protection: enabled by GitHub.
- Default branch: `main`, created by root commit `6e6d45f`.
- Branch protection: PR required, strict `validate` status check required, linear history required, conversations must be resolved, force-push and branch deletion disabled. The approval count is zero because only one GitHub identity is currently available; independent functional review is recorded in-repository.
- License: absent and undecided. No third-party code, dataset redistribution, or binary release is authorized until licenses are recorded.
- CI before issue #1: absent.

## Resource audit

Measured locally on 2026-07-14:

- Windows 11 64-bit, 24-core Intel Core Ultra 7 270K Plus, approximately 64 GiB RAM;
- NVIDIA GeForce RTX 5080, 16,303 MiB VRAM, driver 595.97, compute capability 12.0;
- CUDA toolkit 13.2 installed;
- Python 3.14.4 and `uv` 0.11.19;
- installed PyTorch 2.11.0 is CPU-only and reports no CUDA device;
- Docker client 29.5.3 is installed, but the Docker daemon is not running;
- approximately 1.65 TB free on the workspace drive at audit time;
- `NVIDIA_API_KEY` is absent; NIM is not currently usable from this environment;
- no cluster allocation, cloud budget, energy meter, training budget, or dataset budget is recorded.

This machine is sufficient for governance and small deterministic harness work after environment repair. It is not evidence of feasibility for the proposed 50M/150M/300M confirmatory matrix.

## Decisions

1. Treat the supplied formulation as a candidate hypothesis, not a result.
2. Preserve separate parameter-, training-compute-, and inference-resource-matched comparisons.
3. Keep advanced security and advanced causal modeling outside the core-paper scope.
4. Use the empty-repository exception only for the minimal root commit. All substantive changes use issue #1 and a PR.
5. Do not authorize model or benchmark implementation during M0.
6. Return `STOP` for the broad architecture novelty claim after a 27-source primary-record screen.
7. Return `PIVOT` for the research program, limited to a full M1 review of a non-factorizing constrained-policy hypothesis or an independently useful empirical route.
8. Keep the current architecture paper `NOT_ELIGIBLE` and future narrowed-paper eligibility `NOT_ESTABLISHED`; a new combination, title, diagram, or aggregate gain against weak baselines cannot establish eligibility.
9. Require a same-component fixed composite, matched separated controllers, randomized resource-price interventions, and a preregistered coordination factorial before any architecture claim.
10. Treat expiration as a deterministic store transition and committed rollback as a privileged append-only environment/store event, not learned controller actions.
11. Close M0 only after PR #2 passed the required `validate` check and merged with linear history; open issue #3 under milestone M1 for the systematic novelty gate.

## Blockers

| ID | Blocker | Effect | Resolution condition |
|---|---|---|---|
| B-001 | Underlying source report is missing | Claims attributed to that report cannot be audited | Report supplied or the program explicitly proceeds without it |
| B-002 | Compute and data budgets are unspecified | M5 and later cannot be costed or authorized | Written budget ceilings and resource owner recorded |
| B-003 | Local PyTorch is CPU-only | GPU experiments cannot run in the current environment | Reproducible CUDA-capable environment validated |
| B-004 | Docker daemon is stopped | OCI reproducibility checks cannot run | Daemon available and clean-image build verified |
| B-005 | Project and dataset licenses are undecided | Redistribution and some benchmark use are blocked | License decision and dataset license ledger approved |
| B-006 | No independent GitHub identity is configured | GitHub cannot enforce a distinct human approval | Independent functional review recorded now; repository reviewer identity added before confirmatory merges |
| B-007 | The confirmatory matrix is unbounded and unaffordable on the recorded machine | M2 and later cannot freeze or schedule a fair program | Freeze baseline tiers, grids, retention, power, and written compute/storage ceilings; cost the minimum decisive experiment first |
| B-008 | Recent 2026 prior-art records are changing rapidly | Titles, authors, claims, and locators can drift | Pin exact versions now and recheck at protocol freeze and submission |

## Last valid experiment

None. No experiment has been authorized or run.

## Next authorized action

Execute issue #3: close the systematic search and citation snowball cycle, test whether the constrained policy is reducible to known generic control, test whether an independent component-agnostic empirical route survives, cost the minimum discriminating design, and obtain a new contradictory gate review. The issue may not start model or benchmark implementation.

## M0 exit checklist

- [x] Repository and GitHub access audited.
- [x] Root initialization linked to issue #1.
- [x] Initial branch protection applied.
- [x] Runtime capability selection recorded honestly.
- [x] Local resource constraints measured.
- [x] Governance validator and unit tests pass locally.
- [x] Required `validate` check configured on `main`; GitHub blocks merge unless the latest PR head passes.
- [x] Novelty, theory, protocol, engineering, and bibliography handoffs completed.
- [x] Independent anti-assembly cross-review completed.
- [x] Explicit `PIVOT` decision recorded, with `STOP` for the broad claim, current paper `NOT_ELIGIBLE`, and future eligibility not established.
- [x] PR #2 passed required CI and merged; issue #1 and milestone M0 closed.
