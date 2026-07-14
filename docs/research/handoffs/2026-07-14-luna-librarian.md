# Luna-Librarian Handoff: Decision-Source Verification

Date: `2026-07-14`  
Role: `Luna-Librarian`  
Target: `Sol-PI`, milestone `M0`, issue [#1](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/1)  
Overall status: `VERIFIED WITH REQUIRED CORRECTIONS`

## Objective

Verify the metadata, version, primary URL, publication status, record-specific licence, and cited PDF locators for every source used in the Terra-Evidence novelty gate. The purpose is bibliographic control, not another novelty assessment.

## Scope

This pass covers all 27 primary records in `2026-07-14-terra-evidence.md`, plus the Differentiable Neural Computer record requested as a possible baseline. Metadata were checked against arXiv versioned records and API output, OpenReview venue records, PMLR proceedings, the ICLR proceedings site, ACL Anthology, or Nature. PDF locators were independently checked against the exact cited versions when accessible.

Author fields below use full names when short and `first author et al. (N authors)` when long. In every abbreviated row, the complete ordered list was checked on the linked primary record. No DOI or BibTeX record was inferred. The only non-arXiv DOI reported is the publisher-verified Nature DOI for DNC.

## Inputs

- `docs/research/handoffs/2026-07-14-terra-evidence.md`
- The versioned primary records linked below
- arXiv Atom metadata and the licence link embedded in each versioned abstract page
- Official OpenReview, PMLR, ICLR, ACL Anthology, and Nature records

## Decision-critical verification table

| Record and verified authors | Exact record, year, status, licence | Locator audit | Status |
|---|---|---|---|
| [HOLA](https://arxiv.org/abs/2607.02303v1), Wanyun Cui (sole author) | `arXiv:2607.02303v1`, 2026 preprint; arXiv non-exclusive distribution licence | Terra's §§3.1-3.4, PDF pp. 4-6 and §4.5, pp. 8-9 are correct. | `VERIFIED` |
| [Sparse Delta Memory](https://arxiv.org/abs/2607.07386v1), Loïc Cabannes et al. (9) | `arXiv:2607.07386v1`, 2026 preprint; CC BY 4.0 | Method is §3, especially §§3.1-3.3, PDF pp. 4-5, not pp. 3-5. Table 2 is p. 8 and the resource limitation is p. 10. | `CORRECT LOCATOR` |
| [Conditional Memory / Engram](https://arxiv.org/abs/2601.07372v2), Xin Cheng et al. (21 in v2) | `arXiv:2601.07372v2`, revised `2026-07-12`; CC BY 4.0 | §3 spans PDF pp. 6-8; §6.4 spans pp. 17-18. Terra's locators are correct for v2. | `VERSION CONFLICT`, see alerts |
| [Adaptive Loops and Memory](https://openreview.net/forum?id=F87X9c107e), Markus Frey, Behzad Shomali, Ali Hamza Bashir, David Berghaus, Joachim Koehler, Mehdi Ali | OpenReview `F87X9c107e`, LIT Workshop at ICLR 2026, published `2026-03-02`, modified `2026-03-18`; CC BY 4.0 | §§2.1-2.2 and Fig. 1 are within PDF pp. 1-3. Official PDF text was verified; the forum later presented an intermittent browser challenge. | `VERIFIED` |
| [Universal Transformers Need Memory](https://arxiv.org/abs/2604.21999v3), Grigory Sapunov (sole author) | `arXiv:2604.21999v3`, 2026 preprint; CC BY-SA 4.0 | §§2.1-2.2, pp. 2-3; §4.3, pp. 5-6; §5.1, pp. 8-9 are correct. | `VERIFIED` |
| [MemOS](https://arxiv.org/abs/2507.03724v4), Zhiyu Li et al. (39 in v4) | `arXiv:2507.03724v4`, 2025 preprint, revised `2025-12-03`; CC BY 4.0 | MemCube pp. 13-16, API/transactions p. 19, scheduler §5.4.2 p. 20, lifecycle/rollback p. 21 are adequate. | `VERIFIED`, pin v4 |
| [Larimar](https://proceedings.mlr.press/v235/das24a.html), Payel Das et al. (12) | ICML 2024, PMLR 235:10109-10126; corresponding preprint `arXiv:2403.11901v4`, CC BY 4.0 on arXiv | Memory operations are concentrated in PDF pp. 3-4; §5.3 p. 6 and §5.4 p. 7 are correct. | `VERIFIED WITH AUTHOR CORRECTION` |
| [MemLLM](https://openreview.net/forum?id=dghM7sOudh), Ali Modarressi, Abdullatif Köksal, Ayyoob Imani, Mohsen Fayyaz, Hinrich Schütze | TMLR, published April 2025; `arXiv:2404.11672v3`; CC BY 4.0 on both records | §§3.1-3.3, pp. 3-7; read results pp. 9-10; exact replacement rule p. 11 are correct. | `VERIFIED` |
| [CAT](https://arxiv.org/abs/2511.05313v2), Jatin Prakash, Aahlad Puli, Rajesh Ranganath | `arXiv:2511.05313v2`, revised `2026-07-13`; ICLR 2026 submission, not an accepted paper in the official record; CC BY 4.0 | Mechanism is §2, especially §§2.1-2.2, PDF pp. 3-5, not §3. Results are §4, pp. 6-9; data-dependent allocation limitation is p. 10. | `CORRECT TITLE AND LOCATOR` |
| [Mixture-of-Recursions](https://arxiv.org/abs/2507.10524v3), Sangmin Bae et al. (11) | `arXiv:2507.10524v3`, 2025; NeurIPS 2025 poster; arXiv CC BY 4.0, OpenReview venue copy CC BY-NC 4.0 | §2 starts on PDF p. 3 and Fig. 2 is p. 4; compute/KV evidence spans §§3-4, pp. 5-10; conclusion p. 12. | `VERIFIED WITH VERSION-SPECIFIC LICENCE` |
| [MELT](https://arxiv.org/abs/2605.07721v2), Victor Conchello Vendrell, Arnau Padrés Masdemont, Niccolò Grillo, Jordi Ros-Giralt, Arash Behboodi, Fabio Valerio Massoli | `arXiv:2605.07721v2`, 2026, CC BY-NC-SA 4.0; ICML 2026 FoGen Workshop poster copy, CC BY 4.0 | §3.1/Fig. 2, pp. 3-4; §4.4 p. 8; limitations p. 9 are correct. | `VERIFIED WITH VERSION-SPECIFIC LICENCE` |
| [Shared Global Workspace](https://openreview.net/forum?id=XzTtHjgPDsT), Anirudh Goyal et al. (10) | ICLR 2022 Oral; corresponding `arXiv:2103.01197v2`, arXiv non-exclusive distribution licence | §2, pp. 3-5 and competition/capacity evidence pp. 7-9 are correct. | `VERIFIED` |
| [Recurrent Memory Transformer](https://openreview.net/pdf?id=Uynr3iPhksa), Aydar Bulatov, Yuri Kuratov, Mikhail S. Burtsev | NeurIPS 2022; `arXiv:2207.06881v2`, arXiv non-exclusive distribution licence | §3 starts on PDF p. 3 and Fig. 2 spans pp. 3-4, not solely p. 4. Results/attention evidence pp. 6-9 are correct. | `CORRECT LOCATOR` |
| [Titans](https://arxiv.org/abs/2501.00663v1), Ali Behrouz, Peilin Zhong, Vahab Mirrokni | `arXiv:2501.00663v1`, 2025 record; NeurIPS 2025 poster; CC BY 4.0 | §3.1, pp. 5-6; §4, pp. 9-11; component evidence around pp. 15-16. Terra's locator is adequate. | `VERIFIED` |
| [ATLAS: Learning to Optimally Memorize](https://arxiv.org/abs/2505.23735v1), Ali Behrouz et al. (8) | `arXiv:2505.23735v1`, 2025, CC BY 4.0; subsequently an ICML 2026 regular paper | §§3.1-3.2, pp. 5-8; §4, pp. 9-11; §5 p. 12 are correct for arXiv v1. The ICML copy is newer and must not inherit these locators unchecked. | `VERSION DRIFT RISK` |
| [Adaptive Computation Time](https://arxiv.org/abs/1603.08983v6), Alex Graves (sole author) | `arXiv:1603.08983v6`, 2016/2017 preprint; arXiv non-exclusive distribution licence | §2, pp. 2-5; computation limit and Eq. 13 are on p. 5. Terra's locator is correct. | `VERIFIED` |
| [Universal Transformers](https://openreview.net/forum?id=HyzdRiR9Y7), Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, Łukasz Kaiser | ICLR 2019; `arXiv:1807.03819v3`, arXiv non-exclusive distribution licence | Model starts p. 2; dynamic halting is §2.2 p. 4; difficulty-correlated ponder evidence is pp. 5-6. Replace Terra's broad “§§2.1-2.2, pp. 3-5” with these locators. | `CORRECT LOCATOR` |
| [PonderNet](https://arxiv.org/abs/2107.05407v2), Andrea Banino, Jan Balaguer, Charles Blundell | `arXiv:2107.05407v2`, 2021; arXiv non-exclusive distribution licence. A workshop presentation is reported, but the versioned arXiv record is the stable citation verified here. | §§2.2-2.5, PDF pp. 2-4; ACT comparison pp. 9-10 are correct. | `VERIFIED` |
| [Differentiable Neural Computer](https://www.nature.com/articles/nature20101), Alex Graves et al. (20) | Nature 538, 471-476 (2016), published `2016-10-12`; DOI [10.1038/nature20101](https://doi.org/10.1038/nature20101). No CC licence was displayed on the official article record. | Not used in Terra's decision table, so no Terra locator to validate. The publisher abstract and Fig. 1 establish a neural controller with external read-write memory. | `METADATA VERIFIED; NOT YET CITED` |

## Contextual-source verification table

| Record and verified authors | Exact status and licence | Locator audit | Status |
|---|---|---|---|
| [Memorizing Transformers](https://openreview.net/forum?id=TrjbxzRcnf-), Yuhuai Wu, Markus Norman Rabe, DeLesley Hutchins, Christian Szegedy | ICLR 2022 Spotlight; licence not stated in the opened official record | §3.1, pp. 4-5; Tables 1/5, pp. 6-7; clearing semantics p. 10 are adequate. | `VERIFIED` |
| [Mamba](https://arxiv.org/abs/2312.00752v2), Albert Gu, Tri Dao | COLM 2024 Outstanding Paper; arXiv v2, CC BY 4.0 | §§3.1-3.3, pp. 5-8; selective-copy evidence p. 10 are correct. | `VERIFIED` |
| [Transformers are SSMs / Mamba-2](https://proceedings.mlr.press/v235/dao24a.html), Tri Dao, Albert Gu | ICML 2024, PMLR 235:10041-10071; use the PMLR version of record | §3.5 starts p. 6 and §3.10 p. 7; MQAR Fig. 3 p. 8. Efficiency is Fig. 5 p. 9, not Fig. 4. | `CORRECT FIGURE NUMBER` |
| [Jamba](https://arxiv.org/abs/2403.19887v2), Opher Lieber et al. (22) | `arXiv:2403.19887v2`, 2024 technical report; CC BY-SA 4.0 | §§2-3, pp. 3-6 are adequate. §6.1 starts p. 9 and continues p. 10, not pp. 10-11. | `CORRECT LOCATOR`; author spelling differs between metadata and PDF header |
| [Samba](https://proceedings.iclr.cc/paper_files/paper/2025/hash/84a7fc24ed52e8eff514c33e8ac76ea3-Abstract-Conference.html), Liliang Ren, Yang Liu, Yadong Lu, Yelong Shen, Chen Liang, Weizhu Chen | ICLR 2025; `arXiv:2406.07522v3`, CC BY 4.0 | §2.1, pp. 3-4; architecture evidence pp. 5-6; §3.3 pp. 7-9 are adequate. | `VERIFIED` |
| [Hymba](https://openreview.net/forum?id=A1ztozypga), Xin Dong et al. (13) | ICLR 2025 Spotlight; `arXiv:2411.13676v1`; CC BY 4.0 | Table 1 p. 2; §§2.1-2.4, pp. 3-6; comparisons pp. 8-10 are correct. | `VERIFIED` |
| [MemGPT](https://arxiv.org/abs/2310.08560v2), Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez | `arXiv:2310.08560v2`, 2023/2024 preprint; CC BY 4.0 | §§2-2.2, pp. 2-3 are correct. Function executor is §2.3 p. 3; control-flow interrupts/function chaining are §2.4 p. 4. Terra assigns chaining to §2.3 and should correct it. | `CORRECT SECTION` |
| [Mixture-of-Depths](https://arxiv.org/abs/2404.02258v1), David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro | `arXiv:2404.02258v1`, 2024 preprint; CC BY 4.0 | §3.1 p. 4; §3.4 p. 6; results §4 start p. 7 and isoFLOP evidence spans pp. 7-9. | `VERIFIED` |
| [ATLAS: Agentic Test-time Learning-to-Allocate Scaling](https://arxiv.org/abs/2606.01667v1), Peijia Qin, Qi Cao, Pengtao Xie | `arXiv:2606.01667v1`, 2026 preprint; CC BY 4.0 | Method §3 begins p. 3; action variants p. 4; experiments pp. 5-8; stopping analysis is chiefly pp. 8-9. Terra's locator is adequate. | `VERIFIED` |

## Required corrections and alerts

1. **Do not mix Engram versions.** `arXiv:2601.07372v2` was revised two days before this audit and has 21 authors, an Engram formulation, and v2 locators. The official ACL 2026 long-paper record has 14 authors and calls the module Deep Sparse Embedding (DSE). Treat these as separate bibliographic manifestations. Cite one exact version and re-extract claims from that version.
2. **Pin all fast-moving 2026 sources.** HOLA v1, SDM v1, Universal Transformers Need Memory v3, Engram v2, CAT v2, MELT v2, and Agentic ATLAS v1 must be cited with version suffixes. Recheck them immediately before protocol freeze and submission. CAT v2 changed on `2026-07-13`.
3. **Use exact CAT metadata.** The current arXiv v2 title is *Controllably Efficient Language Models*. The OpenReview submission title is *Attention and Compression is all you need for Controllably Efficient Language Models*. Terra's hybrid label is understandable but not citation-safe. CAT's mechanism is §2, not §3.
4. **Use venue versions where final.** Larimar should cite PMLR `das24a`; MemLLM should cite TMLR/OpenReview `dghM7sOudh`; Mamba-2 should cite PMLR `dao24a`; Shared Global Workspace, RMT, Mamba, Samba, Hymba, Titans, Universal Transformers, Memorizing Transformers, and MoR should carry their verified venue status.
5. **Preserve record-specific licences.** MoR's arXiv and OpenReview copies display different licences. MELT's arXiv and workshop copies also display different licences. Licence metadata must attach to the exact artifact, never to the abstract work in general.
6. **Correct final-version author strings.** Larimar's PMLR record uses `Sarathkrishna Swaminathan`; the arXiv metadata uses a shortened form. MemOS v4 has 39 authors and a materially changed order relative to cached v1/GitHub citation strings. Jamba's arXiv metadata and PDF header differ on spellings for Avshalom/Avashalom Manevich and Erez Schwartz/Shwartz. Preserve the metadata of the exact cited record and flag these discrepancies rather than normalizing silently.
7. **Fix locator errors before ledger import.** Required changes are SDM method pp. 4-5; RMT §3/Fig. 2 pp. 3-4; Universal Transformer dynamic halting §2.2 p. 4; Mamba-2 efficiency Fig. 5 p. 9; Jamba §6.1 pp. 9-10; MemGPT chaining §2.4 p. 4; CAT mechanism §2 pp. 3-5.
8. **DNC metadata is valid but was not part of Terra's gate evidence.** If it becomes a baseline, add it explicitly to the evidence ledger and extract a page-level method locator from the Nature article or its supplementary material. Do not cite `arXiv:1610.06258` as DNC; that identifier is *Using Fast Weights to Attend to the Recent Past*.

## Source-status summary

- All 27 Terra records were resolved to a primary or official record.
- 19 records are citation-ready after version pinning.
- 7 records require locator, title, author, licence, or version corrections before ledger import.
- Engram has one material cross-version publication conflict that prohibits mixing metadata and locators.
- DNC's publisher metadata and DOI are verified, but it is not yet evidence in Terra's gate.
- No source was left unverifiable. OpenReview's browser challenge was intermittent, but the required venue metadata and indexed PDF text were available from official records during this pass.

## Files modified

- `docs/research/handoffs/2026-07-14-luna-librarian.md` only.

Temporary PDFs used for locator checks were stored outside the repository in the operating-system temporary directory.

## Verification performed

- Queried exact version metadata for 24 arXiv records and compared titles, complete ordered author lists, submission/revision dates, and embedded licence targets.
- Opened official OpenReview records for venue, decision status, author, and licence metadata where applicable.
- Opened PMLR records for Larimar and Mamba-2, the ICLR proceedings record for Samba, ACL Anthology for the published Conditional Memory manifestation, and Nature for DNC.
- Extracted text from the exact PDFs and mapped the cited sections, figures, tables, and limitations to PDF page numbers.
- Confirmed that no DOI or BibTeX entry was fabricated.

## Recommendation

Keep the Terra gate at `PIVOT`, but treat this handoff as a mandatory citation-correction layer before importing evidence. The decision is robust to the corrections: the closest threats remain HOLA, Universal Transformers Need Memory, Adaptive Loops, MemOS, MoR, CAT, Engram, and MELT. The corrections strengthen traceability and prevent the article from presenting a version mixture as if it were one coherent prior-work record.

## Next action

Import only version-pinned rows into the literature matrix and evidence ledger. Apply the seven locator corrections, select either Engram arXiv v2 or the ACL DSE version for each claim, and schedule an automatic version recheck at protocol freeze. Add DNC as a baseline only after a page-level method extraction is entered in the evidence ledger.
