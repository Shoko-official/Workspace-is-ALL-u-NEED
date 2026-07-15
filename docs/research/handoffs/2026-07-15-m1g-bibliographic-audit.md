# Handoff M1g: audit bibliographique indépendant

Status: `COMPLETE`

Type: `INDEPENDENT_BIBLIOGRAPHIC_AUDIT`

Date: `2026-07-15`

Issue: `#25`

Milestone: `M1g - Problem-first invariant discovery`

Branche examinée: `research/25-problem-first-invariant`

Commit scientifique examiné: `94af4acb8ef2db505e9596c0946c618fc136c641`

Verdict: `PASS_AFTER_CORRECTIONS`

## 1. Objectif

Vérifier les métadonnées, versions, venues, pages, locateurs, portées et liens
claim-preuve des sources qui déterminent le gate M1g. L'audit doit empêcher
qu'un préprint récent, un protocole proposé ou un analogue générique soit
présenté comme preuve répliquée d'une nouvelle loi LLM.

## 2. Périmètre et exclusions

L'audit couvre `EV-0170` à `EV-0182`, les réutilisations `EV-0084`, `EV-0091`,
`EV-0092` et `EV-0156`, les claims `CLM-027` à `CLM-029`, les lignes `P-055` à
`P-062`, les deux registres M1g, Decision 0009 et les 151 clés de
`paper/references.bib`.

Sont exclus une réplication empirique, une recherche bibliographique exhaustive,
une preuve universelle d'impossibilité et toute autorisation d'article ou
d'expérience.

## 3. Questions testées

1. Chaque identifiant résout-il vers le record primaire et la version déclarés?
2. Les auteurs, titres, années, venues, DOI, pages et statuts de publication
   sont-ils exacts?
3. Les locateurs permettent-ils de reproduire la vérification de portée?
4. Les sources soutiennent-elles la réduction déclarée sans être étendues en
   garantie universelle?
5. Les claims M1g et leurs preuves sont-ils réciproques, et le BibTeX est-il
   unique et complet?

## 4. Entrées et versions

- linearizability: DOI `10.1145/78969.78972`;
- Lightweight Collective Memory: DOI `10.1109/DSN.2017.45`, arXiv
  `1701.00981v2`;
- Dissociative Identity: DOI `10.1145/3805689.3806748`, FAccT 2026 pages
  4199-4219, arXiv `2605.30169v3`;
- CIMemories: arXiv `2511.14937v1`;
- cross-user contamination: arXiv `2604.01350v1`;
- Memory-Induced Tool-Drift: arXiv `2605.24941v1`;
- Intent Legitimation: DOI `10.18653/v1/2026.acl-long.1260`;
- behavioral unlearning audit: arXiv `2606.14518v1`;
- Real-Time Reasoning Agents: ICLR 2026 poster, OpenReview `n1AvXiU2lu`, arXiv
  `2511.04898v1`;
- Yamada AIPS 1996, Tu et al. PMLR 258, AgentDoS USENIX Security 2026
  prepublication, and Resource Containers OSDI 1999;
- cutoff: `2026-07-15`.

## 5. Travail effectué

Deux états fixes ont été audités en lecture seule.

1. `7be694155782deda2a4492ff87a47274786aea28` a été bloqué pour quatre liens
   claim-preuve non réciproques, l'absence des pages FAccT, trois locateurs trop
   faibles ou mal typés, et une garantie de fermeture trop large attribuée au
   protocole Agentic Unlearning.
2. `94af4acb8ef2db505e9596c0946c618fc136c641` corrige la réciprocité, les pages
   et le titre des actes FAccT, les locateurs PDF et la formulation de portée.
   Le nouvel audit rend `PASS` sans blocker.

## 6. Preuves et locateurs décisifs

- `EV-0170`: abstract et Sections 2-3, définition du point d'effet et localité
  de linearizability.
- `EV-0171`: Sections II-IV, fork-linearizability et operation stability.
- `EV-0172`: DOI primaire, pages 4199-4219; abstract, Sections 1-3 et direction
  protocol-harness page PDF 14.
- `EV-0173`: abstract et pages PDF 1-3; benchmark de contextual integrity et
  violations cumulatives.
- `EV-0177`: Theorem 3.3, pages PDF 5-6; résultat borné au cadre convexe déclaré.
- `EV-0178`: formulation page PDF 2 et résultats/discussion pages 7-8.
- `EV-0179`: probabilité de persistance page PDF 4 et seuil d'arrêt page 8.
- `EV-0181`: accumulation persistante page PDF 8 et quotas pages 14-15.
- `EV-0182`: pages PDF 2, 4 et 6; séparation du principal de ressource et du
  contexte d'exécution.

## 7. Incertitudes et contradictions

- CIMemories, cross-user contamination, Tool-Drift et l'audit d'unlearning sont
  des préprints ou records en révision lorsqu'indiqué.
- AgentDoS est une prépublication USENIX Security 2026.
- Les résultats empiriques récents sont utilisés comme collisions positives,
  jamais comme vérités indépendamment répliquées.
- Le théorème d'audit d'unlearning ne justifie pas une impossibilité universelle.
- La recherche est ciblée et ne soutient aucune absence globale d'antériorité.

## 8. Fichiers concernés

- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1G_PROBLEM_REGISTER.md`;
- `docs/research/M1G_SCOPING_LOG.md`;
- `docs/research/decisions/0009-stop-problem-first-invariant-discovery.md`;
- `paper/references.bib`.

## 9. Vérifications exécutées

- 13 nouveaux records et 4 records réutilisés: `PASS_AFTER_CORRECTIONS`;
- `CLM-027` à `CLM-029`: réciprocité avec toutes leurs preuves `PASS`;
- `P-055` à `P-062`: attribution et portée `PASS`;
- versions arXiv et notices primaires: `PASS`;
- BibTeX: 151 clés, 151 uniques, structure équilibrée;
- `python scripts/validate_governance.py`: `PASS`;
- `python -m unittest tests.test_validate_governance`: `6/6 PASS`;
- `git diff --check`: `PASS`.

## 10. Décision recommandée

Aucun blocker bibliographique ne subsiste sur le commit scientifique
`94af4acb8ef2db505e9596c0946c618fc136c641`. Le volet bibliographique de
Decision 0009 peut être accepté avec `STOP`.

## 11. Prochaine action autorisée

Intégrer les trois verdicts indépendants, puis soumettre Decision 0009 au check
protégé. Aucun article, modèle, benchmark, entraînement, expérience ou compute
payant n'est autorisé.

## 12. Rôles et indépendance

- Fonction bibliographique indépendante: sources, versions, locateurs et
  portée, en lecture seule.
- Fonction scientifique indépendante: objets, équations, falsificateurs,
  comparateurs et réductions.
- Fonction gouvernance indépendante: statuts, tests, cardinalités et périmètre.
- Fonction auteur et intégrateur: direction scientifique et tenue du gate.

Aucune fonction indépendante n'a modifié les fichiers relus.
