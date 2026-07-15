# Handoff M1f: audit bibliographique indépendant

Status: `COMPLETE`

Type: `INDEPENDENT_BIBLIOGRAPHIC_AUDIT`

Date: `2026-07-15`

Issue: `#21`

Milestone: `M1f - Mechanism-first technical object discovery`

Branche examinée: `agent/21-mechanism-first-object`

Commit scientifique examiné: `76d3ae0ee6266a5f8031e66f83f0d79b405fe033`

Verdict: `PASS_AFTER_CORRECTIONS`

## 1. Objectif

Vérifier les métadonnées, versions, venues, locateurs et limites de portée des
sources qui déterminent le gate M1f, en particulier le rapport récupéré, la
catégorie réelle d'UniTok, les deux compilateurs et les réductions génériques.
L'audit ne transforme ni un préprint en résultat répliqué, ni un assemblage de
composants en contribution originale.

## 2. Périmètre et exclusions

L'audit couvre `EV-0153` à `EV-0169`, les réutilisations `EV-0069`, `EV-0070`,
`EV-0076` et `EV-0099`, les claims `CLM-022` à `CLM-026`, les lignes `P-047` à
`P-054`, les deux registres M1f, Decision 0008 et les 138 clés de
`paper/references.bib`.

Sont exclus la réplication empirique, l'exhaustivité bibliographique, une preuve
d'impossibilité globale et toute autorisation d'article ou d'expérience.

## 3. Questions testées

1. Chaque identifiant résout-il vers le record primaire et la version déclarés?
2. Les titres, auteurs, années, venues, DOI et pages sont-ils exacts?
3. Les locateurs soutiennent-ils la disposition mobilisée sans extension de
   portée?
4. UniTok traite-t-il des tokens lexicaux ou des identifiants d'items?
5. Les ledgers, la matrice et le BibTeX sont-ils réciproques et sans collision?

## 4. Entrées et versions

- rapport local: 23 pages, 517,191 octets, SHA-256
  `c584128e870e22e2c0372c5cdc6dc41558f9655c256dc46770f50937cd2f8046`;
- UniTok: publication AAAI 2026, volume 40(17), pages 14848-14855, DOI
  `10.1609/aaai.v40i17.38505`;
- timing privacy: arXiv `2409.05623v2`;
- TriRoute: arXiv `2607.06601v1`, soumis le 7 juillet 2026;
- TMA-NM: arXiv `2606.24322v1`;
- SEVerA: arXiv `2603.25111v2`;
- adaptive costly audits: arXiv `2502.08412v3`, article bibliographique 2025,
  révision du 26 mai 2026;
- cutoff: `2026-07-15`.

## 5. Travail effectué

Trois états fixes ont été audités en lecture seule.

1. `7429417` a révélé la notice UniTok périmée, l'année erronée du papier sur
   les audits, quatre titres non exacts et une portée trop large attribuée à la
   seule source de timing privacy.
2. `c1472aa` a corrigé les métadonnées, le BibTeX, les titres et limité O05 à
   `output + runtime`; l'audit bibliographique a alors rendu `PASS`.
3. `76d3ae0` a corrigé le falsificateur DP d'O05 et ses résumés sans régression
   bibliographique; le verdict final est `PASS`.

## 6. Preuves et locateurs décisifs

- `EV-0167`: abstract, Sections 3.1-3.3 du preprint et notice AAAI publiée;
  les entrées sont des items de recommandation projetés et discrétisés.
- `EV-0166`: abstract et Section 4.2; extension de vocabulaire de domaine, sans
  routeur de mission.
- `EV-0168` et `EV-0169`: adaptation lexicale dynamique ou évolutive réelle.
- `EV-0162`: Sections 3.2-3.7 et Table 4; collision thématique récente, statut
  `PARTIAL` conservé.
- `EV-0159`: output et runtime uniquement; aucun résultat sur adresses,
  branches, appels, actions ou composition adaptative ne lui est attribué.
- `EV-0158`: Definition 1 et Theorems 1-3; collision directe pour l'autorité
  non malléable liée à l'origine.
- `EV-0163`: contrats formels, rejection sampling et fallback vérifié dans un
  domaine restreint.

## 7. Incertitudes et contradictions

- Plusieurs records 2026 sont des préprints récents et non répliqués.
- TriRoute n'est utilisé que comme collision thématique, jamais comme vérité
  empirique indépendante.
- Le rapport local est une entrée propriétaire fixée par hash, pas une source
  scientifique indépendante.
- La recherche est ciblée et ne soutient aucune absence universelle d'antériorité.
- Les notices devront être revérifiées si un futur objet atteint le gate de
  protocole ou de soumission.

## 8. Fichiers concernés

- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1F_CANDIDATE_REGISTER.md`;
- `docs/research/M1F_SCOPING_LOG.md`;
- `docs/research/decisions/0008-stop-mechanism-first-object-discovery.md`;
- `paper/references.bib`.

## 9. Vérifications exécutées

- 21 records nouveaux ou réutilisés contrôlés: `PASS_AFTER_CORRECTIONS`;
- 17 nouvelles preuves, 5 claims M1f et 8 lignes de matrice: réciprocité
  `PASS`;
- UniTok, vocabulaire de domaine, tokenisation dynamique et Ted-Tok: portée
  `PASS`;
- O05 contre `EV-0159`: attribution `output + runtime` uniquement, `PASS`;
- BibTeX: 138 clés, 138 uniques, structure équilibrée;
- `git show --check` et `git diff --check`: `PASS`.

## 10. Décision recommandée

Aucun blocker bibliographique ne subsiste sur le commit scientifique
`76d3ae0ee6266a5f8031e66f83f0d79b405fe033`. Le volet bibliographique de
Decision 0008 peut être accepté avec `STOP`.

## 11. Prochaine action autorisée

Intégrer les trois verdicts indépendants, puis soumettre Decision 0008 au check
protégé. Aucun article, modèle, benchmark, entraînement ou expérience n'est
autorisé.

## 12. Rôles et indépendance

- Fonction bibliographique indépendante: sources, versions, locateurs et
  portée, en lecture seule.
- Fonction scientifique indépendante: objets, comparateurs, compilateurs,
  falsificateurs et réductions.
- Fonction gouvernance indépendante: réciprocité, statuts, tests et périmètre.
- Fonction auteur et intégrateur: direction scientifique et tenue du gate.

Aucune fonction indépendante n'a modifié les fichiers relus.
