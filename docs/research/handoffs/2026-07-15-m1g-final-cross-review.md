# Handoff final M1g: revue contradictoire consolidée

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_CROSS_REVIEW`

Date: `2026-07-15`

Issue: `#25`

Milestone: `M1g - Problem-first invariant discovery`

Branche examinée: `research/25-problem-first-invariant`

Commit scientifique examiné: `94af4acb8ef2db505e9596c0946c618fc136c641`

Intégration protégée: `PENDING`

Verdict des trois fonctions indépendantes: `MERGE_AFTER_PROTECTED_VALIDATE`

Décision scientifique: `STOP`

Problèmes examinés: `8`

Objets admis: `0`

Objets `DISTINCT_CANDIDATE` survivants: `0`

## 1. Objectif

Vérifier que M1g dérive ses objets de pannes concrètes, exige la nécessité
causale de l'état persistant et du calcul adaptatif, et ne transforme ni un
analogue générique, ni une identité algébrique, ni un registre négatif en
article de réécriture.

## 2. Périmètre et exclusions

Le périmètre comprend les huit problèmes M1g, les tests bi-factoriels, les
comparateurs symétriques, équations, falsificateurs, régimes négatifs,
réductions, le crosswalk des 73 formulations M1c-M1f, les preuves, claims,
matrice, BibTeX, Decision 0009, état opérationnel, registre expérimental et
contrôles de gouvernance.

Sont exclus une affirmation d'exhaustivité, une implémentation, une expérience,
un entraînement, un manuscrit, une réplication empirique et toute tentative de
créer la nouveauté après l'échec du gate.

## 3. Hypothèses et questions testées

1. Chacun des huit incidents fixe-t-il l'événement, l'observateur,
   l'information, l'état, le calcul, l'intervention et les ressources?
2. La suppression de l'état persistant ou du calcul adaptatif élimine-t-elle ou
   change-t-elle matériellement le résultat revendiqué?
3. Les objets exacts P01, P02, P05, P06 et P08 sont-ils mathématiquement typés
   et correctement falsifiables?
4. Le crosswalk couvre-t-il exactement les 73 objets antérieurs sans forcer les
   cellules `NO_REOPENING`?
5. Un objet survit-il aux records directs, au strongest composite, à la
   substitution des labels et aux analogues génériques?
6. Les statuts, comptes, références, tests et autorisations convergent-ils?

## 4. Entrées et versions

- commit initial rejeté: `7be694155782deda2a4492ff87a47274786aea28`;
- commit scientifique corrigé et final:
  `94af4acb8ef2db505e9596c0946c618fc136c641`;
- problèmes: `M1G-P01` à `M1G-P08`;
- crosswalk: 16 M1c, 24 M1d, 24 M1e et 9 M1f, soit 73 lignes uniques;
- preuves: 182 au total, dont `EV-0170` à `EV-0182` nouvelles;
- claims: 29 au total, dont `CLM-027` à `CLM-029` M1g;
- matrice M1g: `P-055` à `P-062`;
- bibliographie: 151 clés uniques;
- cutoff: `2026-07-15`.

## 5. Travail effectué

Trois fonctions indépendantes ont relu chaque état fixe sans le modifier.

1. Sur `7be6941`, la gouvernance a passé. La science a bloqué quatre erreurs:
   P01 confondait ascendance révoquée et effet observable, P02 omettait
   l'opérateur d'effacement, P06 évaluait la dérivée sans point fixe, et P08
   appliquait une seconde espérance à une quantité déjà moyennée. La
   bibliographie a bloqué la réciprocité M1g, les pages FAccT, trois locateurs et
   une portée trop forte attribuée à Agentic Unlearning.
2. `94af4ac` sépare sûreté de lignage et effet, introduit `D_X`, pose
   `d*=F(d*)`, définit une amplification aléatoire sous couplage, précise le
   modèle produit de P05, corrige les métadonnées et automatise les cardinalités
   8/73.
3. Sur `94af4ac`, les trois fonctions ont rendu `PASS` sans blocker.

## 6. Preuves et locateurs décisifs

- P01: `V_R` mesure le commit avec ascendance révoquée; `Delta_R` mesure
  séparément la distance des traces observables.
- P02: `R_D(X;Z_T)` compare `D_X(A(Z_T))` au réentraînement canonique
  `A(Z_T^{-X})`.
- P03: deux copies isolées et symétriques ne garantissent pas descendance unique,
  disponibilité et effets non dupliqués sans coordination ou ancre externe.
- P04/P07: les lois proposées sont non-interference, declassification ou
  observational determinism.
- P05: sous le modèle produit positif et différentiable,
  `J=qS-c`; sa dérivée est une identité locale, et la dépendance qualité-changement
  en falsifie la transportabilité.
- P06: autour de `d*=F(d*)`, `|F'(d*)|` est le critère local générique;
  `|F'|=1` reste inconclusif.
- P08: sous couplage et bornes conditionnelles,
  `E[A_tilde_H] >= H p kappa/a(w)`; les quotas par principal bornent la branche
  constructive.
- Crosswalk: exactement 73 identifiants uniques, zéro omission ou doublon.

## 7. Incertitudes et contradictions

- Le résultat est ciblé et non exhaustif. Il ne prouve pas qu'aucun futur objet
  original n'existe.
- Plusieurs sources 2026 sont récentes, en révision ou non répliquées.
- Les règles P05 et P08 peuvent être utiles en ingénierie sans être de nouvelles
  lois scientifiques.
- P03 est le résidu de surface le plus proche d'un objet extérieur, mais son
  résultat dépend d'une ressource de continuité ou de coordination déjà connue.
- Le `STOP` satisfait M1g, pas l'objectif programmatique de produire l'article
  original demandé.

## 8. Fichiers modifiés

Le lot M1g concerne uniquement:

- `README.md`;
- `docs/research/CHARTER.md`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1G_PROBLEM_REGISTER.md`;
- `docs/research/M1G_SCOPING_LOG.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/STATE.md`;
- `docs/research/decisions/0009-stop-problem-first-invariant-discovery.md`;
- les deux handoffs M1g;
- `experiments/registry.yaml`;
- `paper/references.bib`;
- `scripts/validate_governance.py`;
- `tests/test_validate_governance.py`.

Le répertoire non suivi `.codex-remote-attachments/` reste hors périmètre.

## 9. Vérifications exécutées

| Vérification | Résultat |
|---|---|
| Revue scientifique finale sur `94af4ac` | `PASS` |
| Audit bibliographique final sur `94af4ac` | `PASS` |
| Audit de gouvernance final sur `94af4ac` | `PASS` |
| `python scripts/validate_governance.py` | `PASS` |
| `python -m unittest tests.test_validate_governance` | `6/6 PASS` |
| `git diff --check` | `PASS` |
| Problèmes et crosswalk | 8 problèmes; 73 lignes uniques; zéro admission |
| Réciprocité claim-preuve M1g | `PASS` |
| BibTeX | 151 entrées et 151 clés uniques |
| Registre expérimental | liste vide; aucune expérience autorisée |
| Check protégé distant | `PENDING` |
| Intégration | `PENDING` |
| Issue et milestone scientifiques | issue #25 ouverte; milestone #13 ouvert |
| Périmètre Git | attachment runtime non suivi |

## 10. Décision recommandée

`MERGE_AFTER_PROTECTED_VALIDATE`.

Decision 0009 est `ACCEPTED` avec `STOP` pour les huit problèmes, zéro objet
distinct et aucune autorisation d'article, modèle, benchmark, implémentation,
entraînement, expérience, preuve implémentée ou compute payant.

## 11. Prochaine action autorisée

Soumettre le lot accepté au PR fermant #25 et au check protégé `validate`.
Après merge, réconcilier l'état sous une issue et un milestone de gouvernance
sans changer le contenu scientifique. Aucun article ou experiment n'est
autorisé.

## 12. Rôles et indépendance

- Fonction auteur et intégrateur: direction scientifique et propriétaire du gate.
- Fonction scientifique indépendante: validité mathématique, falsificateurs,
  réductions, comparateurs et admission.
- Fonction bibliographique indépendante: métadonnées, versions, locateurs,
  sources primaires et BibTeX.
- Fonction gouvernance indépendante: statuts, tests, cardinalités, registre
  expérimental, GitHub et périmètre Git.

Aucune fonction indépendante n'a modifié les fichiers relus. Les trois ont
rendu `PASS` sur le même commit scientifique final.
