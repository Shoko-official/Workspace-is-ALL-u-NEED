# Handoff final M1e: revue contradictoire consolidée

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_CROSS_REVIEW`

Date: `2026-07-15`

Issue: `#17`

Milestone: `M1e - Intrinsic restricted-class separation discovery`

Branche examinée: `agent/17-intrinsic-restricted-separation`

Commit scientifique examiné: `265ad2605381d7c94c01355b54a10e1c57884680`

Intégration protégée: `PENDING`

Verdict des trois fonctions indépendantes: `MERGE`

Décision scientifique: `STOP`

Formulations examinées: `24`

Classes admises: `22`

Objets `DISTINCT_CANDIDATE` survivants: `0`

## 1. Objectif

Vérifier que M1e teste réellement une séparation intrinsèque entre état
persistant gouverné et calcul adaptatif, sans recycler M1c ou M1d, affaiblir le
comparateur, renommer un problème générique, assembler des résultats connus ou
autoriser une expérience destinée à fabriquer la nouveauté.

## 2. Périmètre et exclusions

Le périmètre comprend les 24 formulations M1e, leurs classes, résultats,
falsificateurs, régimes négatifs, comparateurs, réductions, charges minimales,
claims, preuves, matrice, bibliographie, Decision 0007, état opérationnel,
registre expérimental et contrôles de gouvernance.

Sont exclus toute affirmation d'exhaustivité, toute implémentation, expérience,
formation de modèle, rédaction de manuscrit, réplication empirique ou extension
du scope par simple relabeling LLM/workspace.

## 3. Hypothèses et questions testées

1. Chaque formulation fixe-t-elle une tâche, un ordre causal, des budgets, un
   feedback, un hasard, une information d'entraînement et un résultat uniques?
2. Le comparateur factorisé est-il co-conçu, conjointement entraîné et apparié
   sur toutes les ressources autorisées?
3. Un théorème, estimand, paramètre ou invariant distinct survit-il aux sources
   directes, composites et réductions génériques?
4. Les esquisses non admises sont-elles distinguées des réductions connues?
5. Les sources, statuts, tallies, références croisées et autorisations
   convergent-ils vers une seule décision?

## 4. Entrées et versions

- commit scientifique examiné:
  `265ad2605381d7c94c01355b54a10e1c57884680`;
- cutoff bibliographique: `2026-07-15`;
- formulations: `M1E-C01` à `M1E-C24`;
- classes admises: 22; échecs d'admission: C10 et C23;
- disposition exclusive: `9 direct / 1 composite / 9 reduced / 3 out of scope /
  2 unsupported`;
- preuves M1e: `EV-0116` à `EV-0152`, plus `EV-0090`;
- claims: `CLM-019` à `CLM-021`;
- matrice: `P-036` à `P-046`;
- bibliographie: 122 clés uniques.

## 5. Travail effectué

Trois fonctions indépendantes ont relu le même commit en lecture seule:

- revue scientifique adversariale des classes, résultats, réductions,
  directness, strongest composite et frontières d'admission;
- audit bibliographique des records primaires, versions, locateurs, BibTeX et
  limites de portée;
- audit de gouvernance des CSV, références croisées, tallies, statuts, tests,
  registre expérimental, issue, milestone et périmètre Git.

Les blockers successifs ont conduit aux corrections structurantes suivantes:

1. Un contrat causal commun ferme ordre, budgets, feedback, hasard et training;
   C12 déclare explicitement son exception stationnaire ergodique.
2. C10 et C23 sont `UNSUPPORTED_NOT_DISTINCT`, jamais présentés comme réduits ou
   anticipés.
3. C05 fixe l'approximation multi-pass du matching maximum planaire et sa courbe
   exacte.
4. C07 fixe le word-RAM de sa source au lieu de mélanger RAM, probes et branching
   programs.
5. C09 ajoute les mappings OPE longitudinal requis; C11 fixe son résultat LATE.
6. C14 devient la collision directe unique du best-intervention simple regret à
   budget fixe; C15 ne revendique aucune garantie de belief compression.
7. C20 distingue décomposition formelle et généralisation empirique.
8. Les titres, venues, versions et locateurs bibliographiques signalés par
   l'audit ont été corrigés.

## 6. Preuves et locateurs décisifs

- communication et streaming: `EV-0142` à `EV-0150`, avec C05 fixé par
  `EV-0148` Result 2(ii) et C07 par le word-RAM de `EV-0150`;
- causalité: `EV-0128` à `EV-0141`, `EV-0151` et `EV-0152`, avec C14 fixé par
  `EV-0151` Algorithm 1, Definition 3, Theorems 2 et 5;
- apprentissage: `EV-0116` à `EV-0127`, avec les limites de portée de C20 et
  C23 explicitement conservées;
- médiation réutilisée: `EV-0090`;
- détails complets: handoff bibliographique M1e, evidence ledger, scoping log et
  lignes `P-036` à `P-046`.

## 7. Incertitudes et contradictions

- La recherche est ciblée et non exhaustive; elle n'établit pas qu'aucun
  théorème original de ce type ne pourra jamais exister.
- C10 pourrait être rouvert seulement après formalisation et preuve d'un seuil
  causal nécessaire-et-suffisant réellement nouveau.
- C23 pourrait être rouvert seulement après choix d'une tâche, d'un feedback et
  d'une frontière mémoire-oracle uniques.
- Le matching lower bound d'Element Distinctness demeure un problème générique
  ouvert que M1e ne résout pas.
- Les records récents peuvent dériver et devront être revérifiés avant toute
  future soumission.
- Ce résultat négatif satisfait le gate, pas l'objectif programmatique de
  produire l'article original demandé.

## 8. Fichiers modifiés

Le lot scientifique et son intégration de revue concernent uniquement:

- `README.md`;
- `docs/research/CHARTER.md`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1E_CANDIDATE_REGISTER.md`;
- `docs/research/M1E_SCOPING_LOG.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/STATE.md`;
- `docs/research/decisions/0007-stop-intrinsic-restricted-class-discovery.md`;
- les deux handoffs M1e;
- `experiments/registry.yaml`;
- `paper/references.bib`;
- `scripts/validate_governance.py`;
- `tests/test_validate_governance.py`.

Le répertoire non suivi `.codex-remote-attachments/` reste hors périmètre.

## 9. Vérifications exécutées

| Vérification | Résultat |
|---|---|
| Revue scientifique finale sur `265ad26` | `PASS` |
| Audit bibliographique final sur `265ad26` | `PASS` |
| Audit de gouvernance final sur `265ad26` | `PASS` |
| `python scripts/validate_governance.py` | `PASS` |
| `python -m unittest discover -s tests -v` | `5/5 PASS` |
| `git diff --check` et `git show --check` | `PASS` |
| Registre | 24 identifiants; `9 + 1 + 9 + 3 + 2 = 24` |
| Réciprocité claim-preuve-matrice | `PASS` |
| BibTeX | 122 entrées et 122 clés uniques |
| Registre expérimental | liste vide; aucune expérience autorisée |
| Issue et milestone | issue #17 ouverte; milestone #9 ouvert |
| Périmètre Git | `PASS`; attachment runtime non suivi |

## 10. Décision recommandée

`MERGE` après passage du check distant protégé `validate`.

Decision 0007 peut être `ACCEPTED` avec `STOP` pour les 24 formulations, zéro
objet distinct et aucune autorisation d'article, modèle, benchmark,
implémentation, entraînement, expérience ou compute payant.

## 11. Prochaine action autorisée

Pousser la branche, ouvrir une pull request contenant `Closes #17`, obtenir le
check protégé `validate`, fusionner avec historique linéaire, fermer le milestone
M1e, puis réconcilier l'état post-merge dans un nouveau cycle issue, milestone
et PR. Toute reprise scientifique doit commencer par un objet extérieur aux 64
formulations déjà filtrées et fournir le nouvel objet avant implémentation.

## 12. Rôles et indépendance

- Fonction auteur et intégrateur: direction scientifique et propriétaire du gate.
- Fonction scientifique indépendante: portée mathématique, réductions,
  directness, comparator matching et admission.
- Fonction bibliographique indépendante: métadonnées, versions, locateurs,
  sources primaires et BibTeX.
- Fonction gouvernance indépendante: réciprocité, matrice, statuts, tests,
  registre expérimental, GitHub et périmètre Git.

Aucune fonction indépendante n'a modifié les fichiers relus. Les trois ont rendu
`PASS` sur le même commit scientifique.
