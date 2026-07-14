# Handoff M1b - Luna - Vérification bibliographique EV-0045 à EV-0063

- Date de contrôle : 2026-07-14
- Rôle : bibliothécaire indépendant, distinct de l'assemblage d'évidence Terra et de la réduction Sol
- Périmètre : métadonnées, identifiants, venues, versions, locateurs et BibTeX des sources EV-0045 à EV-0063
- Résultat : **PASS WITH CORRECTIONS** pour l'utilisabilité bibliographique du corpus
- Limite : aucune correction n'est appliquée aux ledgers dans ce lot

## 1. Objectif

Vérifier chaque notice EV-0045 à EV-0063 contre une source primaire ou un registre officiel et fournir :

1. le titre canonique ;
2. les auteurs dans l'ordre publié ;
3. l'année et la version pertinentes ;
4. le DOI, l'identifiant arXiv/HAL/W3C ou l'URL stable ;
5. la venue seulement lorsqu'elle est établie ;
6. les corrections explicites à reporter ultérieurement dans le ledger ;
7. une entrée BibTeX minimale pour chaque source décisive.

Le contrôle distingue un DOI de publication d'un DOI d'archive `10.48550/arXiv.*`. Ce dernier identifie un dépôt arXiv, pas une venue évaluée par les pairs.

## 2. Périmètre et exclusions

### 2.1 Inclus

- `docs/research/EVIDENCE_LEDGER.csv`, lignes EV-0045 à EV-0063 du HEAD partagé.
- Pages de version arXiv, API Atom arXiv, actes ACL/USENIX/ACM, Crossref, HAL/Inria, IEEE et recommandation W3C.
- Venue indiquée par un acte officiel, un DOI de publication, un programme officiel, ou explicitement par la notice primaire.

### 2.2 Exclus

- Modification des ledgers, claims ou handoffs existants.
- Validation scientifique des résultats, déjà traitée dans les handoffs M1b de domaine.
- Inférence d'une venue à partir de profils secondaires ou d'agrégateurs.
- Invention d'un DOI de publication pour les préprints arXiv-only.

## 3. Questions et règles de décision

1. Le titre et l'ordre des auteurs correspondent-ils au registre primaire épinglé ?
2. La version citée est-elle celle effectivement lue par les audits M1b ?
3. La venue est-elle publiée, acceptée, seulement revendiquée dans les commentaires, ou absente ?
4. Le DOI désigne-t-il l'article publié, une version de working paper ou seulement l'archive ?
5. Une différence modifie-t-elle l'identité de la source, ou constitue-t-elle seulement un enrichissement de notice ?

Les corrections sont classées ainsi :

- `MATERIAL` : titre, auteur, identifiant ou venue erronés ;
- `QUALIFIER` : statut de publication insuffisamment borné ;
- `ENRICHMENT` : volume, numéro, pages, date ou booktitle manquants ;
- `TYPOGRAPHY` : casse, ponctuation ou diacritique sans ambiguïté d'identité.

## 4. Entrées et registres utilisés

| Registre primaire | Usage | Locator de métadonnées |
|---|---|---|
| arXiv version pages et API Atom | EV-0046 à EV-0051, EV-0053 à EV-0056 | Bloc Title/Authors, Comments, Submission history, version explicite dans l'URL. |
| [Cambridge Open Engage](https://www.cambridge.org/engage/coe/article-details/6a4abb75810b9dcc82ce84f2) et Crossref | EV-0045 | En-tête, Authors, Version History, DOI ; type Crossref `posted-content`, subtype `preprint`. |
| [ACL Anthology](https://aclanthology.org/2026.findings-acl.994/) | EV-0052 | Anthology ID, volume, mois, année, pages, DOI et BibTeX officiel. |
| HAL API et bibliographie Inria | EV-0057 | `hal-00757488v1`, `number_s=RR-8147`, `page_s=65`, `producedDate_s=2012-11-27`. |
| USENIX official records | EV-0058 et EV-0059 | Authors, booktitle, date, address, publisher et URL d'actes. |
| Crossref + DOI éditeur IEEE/ACM | EV-0046, EV-0060 à EV-0062 | Type, container title, volume, issue, pages, date et DOI. |
| [W3C Recommendation](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/) | EV-0063 | En-tête normatif : titre, date, editors, author, version URI et issuing group. |

## 5. Travail réalisé

- Résolution des 19 identifiants du ledger.
- Comparaison titre-auteurs-version pour les dix notices arXiv.
- Résolution du DOI de ClawVM vers les actes ACM et contrôle de la pagination.
- Contrôle indépendant de la venue ICML de PersistBench sur le programme officiel ICML 2026.
- Export de la notice ACL officielle de X-Router.
- Résolution des notices historiques via HAL, USENIX, IEEE/ACM Crossref et W3C.
- Construction de BibTeX minimaux sans champs non établis.

## 6. Évidence et métadonnées canoniques

### 6.1 Sources M1b directes, EV-0045 à EV-0056

| EV | Notice canonique vérifiée | Identifiant et venue | Locator primaire | Écart avec le ledger |
|---|---|---|---|---|
| EV-0045 | **Xiwei Chen** (2026), *State-Aware Runtime for Long-Horizon LLM Agents: A Conceptual Framework and Research Agenda* | DOI [10.33774/coe-2026-vt9t2-v2](https://doi.org/10.33774/coe-2026-vt9t2-v2) ; Cambridge Open Engage, Working Paper, version 2, 11 juillet 2026 ; non peer-reviewed au dépôt | Cambridge page : en-tête, Authors, Version History, DOI ; Crossref type `posted-content`, subtype `preprint` | `QUALIFIER` : la notice est exacte, mais toute citation doit conserver « working paper, v2 », pas « article Cambridge ». |
| EV-0046 | **Mofasshara Rafique ; Laurent Bindschaedler** (2026), *ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents* | arXiv:2604.10352v1 ; DOI publié [10.1145/3805621.3807648](https://doi.org/10.1145/3805621.3807648) ; *Proceedings of the Sixth European Workshop on Machine Learning and Systems*, pp. 1-12, ACM, 27 avril 2026 | [arXiv v1](https://arxiv.org/abs/2604.10352v1), Title/Authors/Comments/Related DOI ; Crossref DOI, container/page/date | `ENRICHMENT` : remplacer la seule mention « EuroMLSys 2026 » par le booktitle officiel et les pages 1-12. |
| EV-0047 | **Zehao Lin ; Xixuan Hao ; Renyu Fu ; Shaobo Cui ; Kai Chen ; Chunyu Li ; Zhiyu Li ; Feiyu Xiong** (2026), *A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle* | arXiv:2604.16548v2, révision 11 juin 2026 ; aucune venue ni DOI de publication séparé établi | [arXiv v2](https://arxiv.org/abs/2604.16548v2), Title/Authors/Submission history | `TYPOGRAPHY` importante : rétablir les virgules canoniques après *Attacks* et *Defenses*. |
| EV-0048 | **Lingxiang Xu ; Jiaoyun Yang ; Min Hu ; Hongtu Chen ; Ning An** (2026), *When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents* | arXiv:2606.06055v1 ; arXiv-only à la date de coupe | [arXiv v1](https://arxiv.org/abs/2606.06055v1), Title/Authors/Submission history | Confirmé, aucune correction. |
| EV-0049 | **Sidharth Pulipaka ; Oliver Chen ; Manas Sharma ; Taaha S Bajwa ; Vyas Raina ; Ivaxi Sheth** (2026), *PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?* | arXiv:2602.01146v2, révision 2 juin 2026 ; ICML 2026 confirmé par le programme officiel ; aucun DOI de proceedings séparé résolu au 2026-07-14 | [arXiv v2](https://arxiv.org/abs/2602.01146v2), Title/Authors/Comments ; [ICML Downloads 2026](https://icml.cc/Downloads/2026), titre dans le programme | `QUALIFIER` : conserver ICML 2026, mais ne pas inventer DOI, volume PMLR ou pages non encore établis. |
| EV-0050 | **Hanxiang Chao ; Yihan Bai ; Rui Sheng ; Tianle Li ; Yushi Sun** (2026), *STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?* | arXiv:2605.06527v1 ; arXiv-only | [arXiv v1](https://arxiv.org/abs/2605.06527v1), Title/Authors/Submission history | Confirmé, aucune correction. |
| EV-0051 | **Sukanta Ganguly** (2026), *PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents* | arXiv:2607.04089v1 ; arXiv-only, systems position et prototype selon le résumé | [arXiv v1](https://arxiv.org/abs/2607.04089v1), Title/Authors/Abstract/Submission history | Confirmé, aucune correction. Ne pas présenter comme venue publiée. |
| EV-0052 | **Zixuan Wang ; Yinze Ding ; Zihan Wang ; Jinyu Guo ; Zhenhong Zhou ; Junhao Dong ; Chaomeng Chen** (2026), *X-Router: Decoupling Knowledge and Reasoning for Cost-Effective LLM Inference* | DOI [10.18653/v1/2026.findings-acl.994](https://doi.org/10.18653/v1/2026.findings-acl.994) ; *Findings of the Association for Computational Linguistics: ACL 2026*, pp. 19856-19874, ACL, juillet 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.994/), metadata et BibTeX officiel | `ENRICHMENT` : employer le booktitle officiel complet ; le rendu `X -Router` de la page est un artefact du tag de casse, la forme canonique exportée est `X-Router`. |
| EV-0053 | **C. Nicolò De Sabbata ; Theodore R. Sumers ; Badr AlKhamissi ; Antoine Bosselut ; Thomas L. Griffiths** (2024), *Rational Metareasoning for Large Language Models* | arXiv:2410.05563v3, révision 23 juin 2025 ; arXiv-only | [arXiv v3](https://arxiv.org/abs/2410.05563v3), Title/Authors/Submission history | Confirmé. Important : citer les cinq auteurs de v3, pas la liste plus courte d'une version antérieure. |
| EV-0054 | **Ziming Wang** (2026), *TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory* | arXiv:2606.06240v1 ; arXiv-only | [arXiv v1](https://arxiv.org/abs/2606.06240v1), Title/Authors/Submission history | Confirmé, aucune correction. |
| EV-0055 | **Sanjana Pedada ; Aditya Dhavala ; Neelraj Patil** (2026), *Shared Selective Persistent Memory for Agentic LLM Systems* | arXiv:2607.09493v1 ; arXiv-only ; DOI d'archive arXiv indiqué comme pending registration au dépôt | [arXiv v1](https://arxiv.org/abs/2607.09493v1), Title/Authors/Submission history/DOI note | Confirmé. Ne pas convertir le DOI d'archive en DOI de publication. |
| EV-0056 | **Zitong Shi ; Yixuan Tang ; Anthony Kum Hoe Tung** (2026), *A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory* | arXiv:2607.01935v2, révision 8 juillet 2026 ; arXiv-only | [arXiv v2](https://arxiv.org/abs/2607.01935v2), Title/Authors/Submission history | Confirmé, aucune correction. |

### 6.2 Sources de réduction générique, EV-0057 à EV-0063

| EV | Notice canonique vérifiée | Identifiant et venue | Locator primaire | Écart avec le ledger |
|---|---|---|---|---|
| EV-0057 | **Albert Benveniste ; Benoit Caillaud ; Dejan Nickovic ; Roberto Passerone ; Jean-Baptiste Raclet ; Philipp Reinkemeier ; Alberto Sangiovanni-Vincentelli ; Werner Damm ; Thomas Henzinger ; Kim Guldstrand Larsen** (2012), *Contracts for System Design* | HAL `hal-00757488v1` ; Inria Research Report **RR-8147**, 65 p., 27 novembre 2012 ; aucun DOI | [HAL v1](https://inria.hal.science/hal-00757488v1) ; [bibliographie Inria](https://radar.inria.fr/rapportsactivite/RA2017/hycomes/bibliography.html) | `ENRICHMENT` : normaliser `RR-8147` et 65 pages. Le champ HAL de cette version donne `Benoit Caillaud`; une autorité auteur moderne affiche aussi `Benoît`, mais il n'est pas nécessaire de réécrire le record versionné. |
| EV-0058 | **Svend Frølund ; Jari Koistinen** (1998), *Quality of Service Specification in Distributed Object Systems Design* | *4th Conference on Object-Oriented Technologies and Systems (COOTS 98)*, Santa Fe, avril 1998, USENIX Association ; aucun DOI | [USENIX record](https://www.usenix.org/conference/coots-98/quality-service-specification-distributed-object-systems-design), titre/auteurs/BibTeX/booktitle ; PDF officiel, page de titre et §§3-4 | `TYPOGRAPHY` : le record HTML/BibTeX USEN translittère `Frolund`, tandis que le nom de l'auteur et le PDF sont `Frølund`. Conserver `Fr{\o}lund` en BibTeX. |
| EV-0059 | **Ali Ghodsi ; Matei Zaharia ; Benjamin Hindman ; Andy Konwinski ; Scott Shenker ; Ion Stoica** (2011), *Dominant Resource Fairness: Fair Allocation of Multiple Resource Types* | *8th USENIX Symposium on Networked Systems Design and Implementation (NSDI 11)*, Boston, mars 2011, USENIX Association ; aucun DOI | [USENIX record](https://www.usenix.org/conference/nsdi11/dominant-resource-fairness-fair-allocation-multiple-resource-types), authors/BibTeX ; PDF p. 1 | Confirmé ; enrichir seulement le booktitle, le mois et l'adresse si une bibliographie complète est souhaitée. |
| EV-0060 | **C. K. Chow** (1970), *On Optimum Recognition Error and Reject Tradeoff* | DOI [10.1109/TIT.1970.1054406](https://doi.org/10.1109/TIT.1970.1054406) ; *IEEE Transactions on Information Theory* 16(1), pp. 41-46, janvier 1970 | Crossref DOI : title/author/container/volume/issue/pages ; IEEE document 1054406 | `ENRICHMENT` : ajouter volume 16, numéro 1 et pages complètes 41-46. Les pages 41-43 du ledger sont un locator de preuve, pas la pagination bibliographique. |
| EV-0061 | **Peter J. Denning** (1968), *The Working Set Model for Program Behavior* | DOI [10.1145/363095.363141](https://doi.org/10.1145/363095.363141) ; *Communications of the ACM* 11(5), pp. 323-333, mai 1968 | ACM/Crossref DOI : title/author/container/volume/issue/pages | `ENRICHMENT` : ajouter volume 11, numéro 5 et pages 323-333. |
| EV-0062 | **Richard Snodgrass ; Ilsoo Ahn** (1985), *A Taxonomy of Time in Databases* | DOI [10.1145/318898.318921](https://doi.org/10.1145/318898.318921) ; *Proceedings of the 1985 ACM SIGMOD International Conference on Management of Data*, pp. 236-246, ACM, mai 1985 | PDF primaire, page de titre ; [bibliographie officielle de Richard T. Snodgrass](https://www2.cs.arizona.edu/~rts/publications.html) ; DOI ACM/Crossref pour booktitle/pages | Confirmé, aucune correction du titre. L'export DOI ACM/Crossref omet erronément `in`; le PDF primaire et la bibliographie de l'auteur font autorité et conservent *Time in Databases*. |
| EV-0063 | **Tom De Nies**, auteur ; **James Cheney ; Paolo Missier ; Luc Moreau**, éditeurs (2013), *Constraints of the PROV Data Model* | W3C Recommendation, 30 avril 2013 ; version URI [REC-prov-constraints-20130430](https://www.w3.org/TR/2013/REC-prov-constraints-20130430/) ; aucun DOI | En-tête W3C : lignes Author/Editors, date, This version ; status : Provenance Working Group | `MATERIAL` : `W3C Provenance Working Group` est l'issuing group, pas l'auteur affiché. Le document nomme Tom De Nies comme auteur et les trois éditeurs ci-dessus. |

### 6.3 Corrections explicites à reporter ultérieurement

| Priorité | EV | Champ | Valeur actuelle problématique | Valeur recommandée |
|---|---|---|---|---|
| 1 | EV-0063 | `authors` | `W3C Provenance Working Group` | `Tom De Nies` comme auteur ; `James Cheney; Paolo Missier; Luc Moreau` comme éditeurs ; W3C Provenance Working Group comme issuing group |
| 2 | EV-0047 | `title` | Ponctuation supprimée | `A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle` |
| 2 | EV-0046 | `venue/version` | `EuroMLSys 2026` seulement | Booktitle ACM complet, pages 1-12, DOI 10.1145/3805621.3807648 |
| 2 | EV-0052 | `venue/version` | `Findings of ACL 2026` | `Findings of the Association for Computational Linguistics: ACL 2026`, pp. 19856-19874 |
| 3 | EV-0057 | `version` | `INRIA Research Report 8147` | `Inria Research Report RR-8147, 65 pages, 2012-11-27` |
| 3 | EV-0058 | `authors` | Les exports USENIX ASCII peuvent donner `Frolund` | Préserver `Svend Frølund` ou `Fr{\o}lund, Svend` en BibTeX |
| 3 | EV-0060 | `venue/version` | Revue sans pagination complète | `IEEE Transactions on Information Theory, 16(1):41-46` |
| 3 | EV-0061 | `venue/version` | Revue sans pagination complète | `Communications of the ACM, 11(5):323-333` |
| 3 | EV-0062 | `venue/version` | `SIGMOD 1985 official proceedings` | Booktitle complet et pages 236-246 ; conserver le titre primaire avec `in` malgré l'export DOI défectueux |

### 6.4 BibTeX minimaux proposés

Les 19 sources soutiennent directement soit la collision M1b, soit sa réduction générique ; elles sont donc toutes traitées comme décisives. Les notices arXiv-only restent des `@misc`. Une mention de version est conservée dans `note` lorsque plusieurs versions existent.

```bibtex
@misc{chen2026stateaware,
  author = {Chen, Xiwei},
  title = {State-Aware Runtime for Long-Horizon {LLM} Agents: A Conceptual Framework and Research Agenda},
  year = {2026},
  doi = {10.33774/coe-2026-vt9t2-v2},
  url = {https://doi.org/10.33774/coe-2026-vt9t2-v2},
  note = {Cambridge Open Engage working paper, version 2, 11 July 2026}
}

@inproceedings{rafique2026clawvm,
  author = {Rafique, Mofasshara and Bindschaedler, Laurent},
  title = {{ClawVM}: Harness-Managed Virtual Memory for Stateful Tool-Using {LLM} Agents},
  booktitle = {Proceedings of the Sixth European Workshop on Machine Learning and Systems},
  year = {2026},
  pages = {1--12},
  publisher = {ACM},
  doi = {10.1145/3805621.3807648},
  url = {https://doi.org/10.1145/3805621.3807648}
}

@misc{lin2026memorysecurity,
  author = {Lin, Zehao and Hao, Xixuan and Fu, Renyu and Cui, Shaobo and Chen, Kai and Li, Chunyu and Li, Zhiyu and Xiong, Feiyu},
  title = {A Survey on Long-Term Memory Security in {LLM} Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle},
  year = {2026},
  eprint = {2604.16548},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.16548v2},
  note = {Version 2, revised 11 June 2026}
}

@misc{xu2026memorysilent,
  author = {Xu, Lingxiang and Yang, Jiaoyun and Hu, Min and Chen, Hongtu and An, Ning},
  title = {When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents},
  year = {2026},
  eprint = {2606.06055},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2606.06055v1}
}

@inproceedings{pulipaka2026persistbench,
  author = {Pulipaka, Sidharth and Chen, Oliver and Sharma, Manas and Bajwa, Taaha S and Raina, Vyas and Sheth, Ivaxi},
  title = {{PersistBench}: When Should Long-Term Memories Be Forgotten by {LLM}s?},
  booktitle = {International Conference on Machine Learning},
  year = {2026},
  eprint = {2602.01146},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2602.01146v2},
  note = {{ICML} 2026; arXiv version 2, revised 2 June 2026}
}

@misc{chao2026stale,
  author = {Chao, Hanxiang and Bai, Yihan and Sheng, Rui and Li, Tianle and Sun, Yushi},
  title = {{STALE}: Can {LLM} Agents Know When Their Memories Are No Longer Valid?},
  year = {2026},
  eprint = {2605.06527},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2605.06527v1}
}

@misc{ganguly2026placemem,
  author = {Ganguly, Sukanta},
  title = {{PLACEMEM}: Toward a Compute-Aware Memory Plane for Lifelong Agents},
  year = {2026},
  eprint = {2607.04089},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.04089v1}
}

@inproceedings{wang2026xrouter,
  author = {Wang, Zixuan and Ding, Yinze and Wang, Zihan and Guo, Jinyu and Zhou, Zhenhong and Dong, Junhao and Chen, Chaomeng},
  title = {{X}-Router: Decoupling Knowledge and Reasoning for Cost-Effective {LLM} Inference},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2026},
  year = {2026},
  pages = {19856--19874},
  publisher = {Association for Computational Linguistics},
  doi = {10.18653/v1/2026.findings-acl.994},
  url = {https://aclanthology.org/2026.findings-acl.994/}
}

@misc{desabbata2024rational,
  author = {De Sabbata, C. Nicolò and Sumers, Theodore R. and AlKhamissi, Badr and Bosselut, Antoine and Griffiths, Thomas L.},
  title = {Rational Metareasoning for Large Language Models},
  year = {2024},
  eprint = {2410.05563},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2410.05563v3},
  note = {Version 3, revised 23 June 2025}
}

@misc{wang2026toki,
  author = {Wang, Ziming},
  title = {{TOKI}: A Bitemporal Operator Algebra for Contradiction Resolution in {LLM}-Agent Persistent Memory},
  year = {2026},
  eprint = {2606.06240},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2606.06240v1}
}

@misc{pedada2026shared,
  author = {Pedada, Sanjana and Dhavala, Aditya and Patil, Neelraj},
  title = {Shared Selective Persistent Memory for Agentic {LLM} Systems},
  year = {2026},
  eprint = {2607.09493},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.09493v1}
}

@misc{shi2026atma,
  author = {Shi, Zitong and Tang, Yixuan and Tung, Anthony Kum Hoe},
  title = {{A-TMA}: Decoupling State-Aware Memory Failures in Long-Term Agent Memory},
  year = {2026},
  eprint = {2607.01935},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2607.01935v2},
  note = {Version 2, revised 8 July 2026}
}

@techreport{benveniste2012contracts,
  author = {Benveniste, Albert and Caillaud, Benoit and Nickovic, Dejan and Passerone, Roberto and Raclet, Jean-Baptiste and Reinkemeier, Philipp and Sangiovanni-Vincentelli, Alberto and Damm, Werner and Henzinger, Thomas and Larsen, Kim Guldstrand},
  title = {Contracts for System Design},
  institution = {Inria},
  number = {RR-8147},
  year = {2012},
  url = {https://inria.hal.science/hal-00757488v1}
}

@inproceedings{frolund1998qos,
  author = {Fr{\o}lund, Svend and Koistinen, Jari},
  title = {Quality of Service Specification in Distributed Object Systems Design},
  booktitle = {4th Conference on Object-Oriented Technologies and Systems (COOTS 98)},
  year = {1998},
  month = apr,
  address = {Santa Fe, NM},
  publisher = {USENIX Association},
  url = {https://www.usenix.org/conference/coots-98/quality-service-specification-distributed-object-systems-design}
}

@inproceedings{ghodsi2011drf,
  author = {Ghodsi, Ali and Zaharia, Matei and Hindman, Benjamin and Konwinski, Andy and Shenker, Scott and Stoica, Ion},
  title = {Dominant Resource Fairness: Fair Allocation of Multiple Resource Types},
  booktitle = {8th USENIX Symposium on Networked Systems Design and Implementation (NSDI 11)},
  year = {2011},
  month = mar,
  address = {Boston, MA},
  publisher = {USENIX Association},
  url = {https://www.usenix.org/conference/nsdi11/dominant-resource-fairness-fair-allocation-multiple-resource-types}
}

@article{chow1970reject,
  author = {Chow, C. K.},
  title = {On Optimum Recognition Error and Reject Tradeoff},
  journal = {IEEE Transactions on Information Theory},
  year = {1970},
  volume = {16},
  number = {1},
  pages = {41--46},
  doi = {10.1109/TIT.1970.1054406},
  url = {https://doi.org/10.1109/TIT.1970.1054406}
}

@article{denning1968workingset,
  author = {Denning, Peter J.},
  title = {The Working Set Model for Program Behavior},
  journal = {Communications of the ACM},
  year = {1968},
  volume = {11},
  number = {5},
  pages = {323--333},
  doi = {10.1145/363095.363141},
  url = {https://doi.org/10.1145/363095.363141}
}

@inproceedings{snodgrass1985time,
  author = {Snodgrass, Richard and Ahn, Ilsoo},
  title = {A Taxonomy of Time in Databases},
  booktitle = {Proceedings of the 1985 ACM SIGMOD International Conference on Management of Data},
  year = {1985},
  pages = {236--246},
  publisher = {ACM},
  doi = {10.1145/318898.318921},
  url = {https://doi.org/10.1145/318898.318921}
}

@techreport{denies2013provconstraints,
  author = {De Nies, Tom},
  editor = {Cheney, James and Missier, Paolo and Moreau, Luc},
  title = {Constraints of the {PROV} Data Model},
  institution = {World Wide Web Consortium},
  type = {{W3C} Recommendation},
  year = {2013},
  month = apr,
  url = {https://www.w3.org/TR/2013/REC-prov-constraints-20130430/},
  note = {30 April 2013}
}
```

## 7. Incertitudes et contradictions

1. Le DOI arXiv `10.48550/arXiv.*` est un identifiant de dépôt. Il n'est pas répété dans les BibTeX lorsqu'un eprint et une URL de version suffisent.
2. PersistBench apparaît dans le programme officiel ICML 2026 et l'arXiv indique `ICML (2026)`, mais aucun DOI ou numéro de pages de proceedings distinct n'a été résolu à la date de coupe. Le BibTeX s'arrête donc au booktitle et à l'eprint.
3. La page HAL versionnée d'EV-0057 fournit `Benoit Caillaud`, tandis que l'autorité auteur HAL moderne utilise également `Benoît Caillaud`. Le BibTeX suit le record de version pour éviter une correction silencieuse.
4. USENIX translittère `Svend Frolund` dans le HTML/BibTeX, tandis que le nom publié est `Svend Frølund`. La forme BibTeX `Fr{\o}lund` préserve le nom sans dépendre de l'encodage.
5. L'export DOI ACM/Crossref d'EV-0062 donne *A taxonomy of time databases*, mais le PDF primaire et la bibliographie officielle de l'auteur donnent *A Taxonomy of Time in Databases*. Le ledger et le BibTeX doivent suivre le document primaire, pas propager cette erreur de registre.
6. Les pages de preuve des ledgers ne doivent pas être confondues avec la pagination totale d'un article, notamment EV-0060.

## 8. Fichiers modifiés

- Créé uniquement : `docs/research/handoffs/2026-07-14-m1b-luna-librarian.md`.
- Aucun ledger, claim, handoff existant ou fichier de code n'a été modifié par ce lot.
- Tous les changements partagés observés hors de ce chemin cible, suivis ou non suivis, ont été laissés intacts.

## 9. Vérification

- Résolution des 19 IDs : effectuée.
- Contrôle des 12 sections du contrat de handoff : 12/12 présentes.
- Contrôle BibTeX : 19 entrées, 19 clés uniques, 173 accolades ouvrantes et 173 fermantes.
- Contrôle des espaces de fin de ligne : 0 occurrence.
- Contrôle du statut Git : seul ce handoff est imputable à ce lot ; les changements partagés hors cible n'ont pas été touchés.
- Tests logiciels : non applicables, lot documentaire et bibliographique.
- SHA-256 : calculé après la dernière écriture et transmis au parent.

## 10. Décision recommandée

### PASS WITH CORRECTIONS

Les 19 sources sont identifiables et résolubles. Aucune notice ne correspond à une source fantôme ou rétractée dans les registres consultés. Le corpus peut soutenir la décision M1b, sous réserve de corriger avant publication :

1. l'attribution auteur/éditeurs d'EV-0063 ;
2. la ponctuation canonique d'EV-0047 ;
3. les venues et paginations enrichies d'EV-0046, EV-0052 et EV-0060 à EV-0062 ;
4. les qualifiers working-paper/arXiv-only afin de ne pas surdéclarer le peer review ;
5. la conservation du titre primaire d'EV-0062 avec `in`, malgré l'export DOI défectueux.

Ces corrections bibliographiques ne changent pas les conclusions scientifiques des handoffs M1b. Elles améliorent leur traçabilité et empêchent une fausse apparence de publication.

## 11. Prochaine action autorisée recommandée

Le parent peut intégrer ce handoff au verdict final. Une modification ultérieure des ledgers, si elle est autorisée dans un lot séparé, doit appliquer exactement la table de la section 6.3 et conserver les identifiants de preuve existants. Aucun manuscrit ne doit copier les BibTeX sans conserver les qualifiers de statut.

## 12. Rôles d'auteur et de revue indépendante

- Auteur de ce contrôle : **Luna-Librarian**, vérification indépendante des métadonnées et registres.
- Rôle à ne pas fusionner avec ce contrôle : **Terra-Evidence**, auteur de l'audit stateful-systems.
- Relecteur recommandé : mainteneur de l'issue #5 ou Sol-PI, uniquement pour vérifier que les corrections bibliographiques n'altèrent pas les associations EV-claim.
