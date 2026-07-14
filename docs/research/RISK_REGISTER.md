# Risk Register

Scale: probability and impact are `LOW`, `MEDIUM`, or `HIGH`. Status is `OPEN`, `MITIGATING`, `ACCEPTED`, or `CLOSED`.

| ID | Risk | Probability | Impact | Mitigation | Trigger or evidence | Owner | Status |
|---|---|---:|---:|---|---|---|---|
| R-001 | The candidate novelty is only a composition of known components | High | High | Systematic primary-source matrix and adversarial novelty review before implementation | No discriminating property survives the composite baseline | Terra-Evidence / Sol-PI | Open |
| R-002 | The referenced underlying report is unavailable | High | Medium | Mark `INPUT_MISSING`; do not attribute claims to unseen material | Attachment inventory contains only the research program | Sol-PI | Open |
| R-003 | Confirmatory compute exceeds available resources | High | High | Cost models, oracle gate, small pilot, and written budget ceiling before scheduling | No cluster or cloud budget; local GPU has 16 GB VRAM | Terra-Engineering | Open |
| R-004 | Local ML environment cannot use the GPU reproducibly | High | High | Pin a supported Python/CUDA stack and validate in a clean OCI image | Installed PyTorch is CPU-only; Docker daemon stopped | Terra-Engineering | Open |
| R-005 | Code or dataset licensing prevents publication | Medium | High | License ledger before acquisition; do not redistribute by default | Repository has no license; datasets not reviewed | Luna-Librarian | Open |
| R-006 | Split leakage or generator-family contamination inflates OOD results | Medium | High | Family-level splits, hidden confirmatory generators, hashes, MinHash, and canaries | Train/test similarity or canary hit | Luna-QA | Open |
| R-007 | Resource matching favors the proposed model | High | High | Report separate matched regimes and complete physical costs | Omitted indexing, transfer, write, warm-up, or tuning costs | Terra-Engineering | Open |
| R-008 | Controller collapses to degenerate routing | High | High | Log all actions; preregister write-all, write-none, random, fixed, separated, and oracle controls | Saturated routing or near-zero policy entropy | Sol-Theory | Open |
| R-009 | Irregular kernels erase asymptotic savings | Medium | High | Measure p50/p95 latency, HBM, bytes, energy, warm-up, and compilation | Quality gain has no physical-cost gain | Terra-Engineering | Open |
| R-010 | Provenance is decorative rather than causal | Medium | High | Targeted provenance interventions and removal criterion | Predictions ignore source/date/pointer interventions | Sol-Theory | Open |
| R-011 | Independent review is not enforceable with one GitHub identity | High | Medium | Record distinct-agent review artifacts now; add an independent repository reviewer before confirmatory work | Self-authored PR is mergeable without external identity | Sol-PI | Open |
| R-012 | Multiple testing produces a favorable endpoint by chance | Medium | High | Frozen primary endpoints, Holm correction, hierarchical bootstrap, and all-seed reporting | Endpoint changes after result inspection | Luna-QA | Open |
| R-013 | NIM-dependent work silently becomes unavailable | Medium | Low | Treat NIM as optional; record model/version/parameters if used; never log keys | `NVIDIA_API_KEY` is absent | Sol-PI | Accepted |
| R-014 | Natural-task transfer is postponed until after synthetic tuning | Medium | High | Predeclare two natural families and prohibit test tuning | Gains survive only on WAIN-Core | Terra-Evidence | Open |
