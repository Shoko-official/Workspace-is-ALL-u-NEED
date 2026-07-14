# Revue RedTeam indépendante finale M1b

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_REDTEAM`

Branche examinée: `agent/5-directional-thesis-audit`

Commit exact examiné: `32adaccc31bc92858fca4d3b8a94f32cac548edc`

Commit court: `32adacc`

Date: `2026-07-14`

Issue: `#5`

Verdict: `PASS`

Décision scientifique: `STOP CONFIRMÉ`

Objet distinct survivant: `0 DISTINCT_CANDIDATE`

Décision de merge: `MERGE APRÈS INTÉGRATION MÉCANIQUE DE CETTE REVUE ET PASSAGE DU CHECK DISTANT validate`

## 1. Mission et indépendance

Cette revue finale teste le commit exact `32adacc` après les corrections demandées par `2026-07-14-m1b-sol-preintegration-review.md`. Elle porte sur le typage formel, la justification du `STOP`, les registres de falsifiabilité, les coûts minimaux, la recherche, la bibliographie, la cohérence des artefacts de gouvernance, les tests et le périmètre du diff.

Aucun résultat expérimental n'est évalué, car aucun modèle, benchmark ou protocole M1b n'a été exécuté ni autorisé. Aucun fichier existant n'a été modifié pendant cette revue. Le présent handoff est le seul fichier produit.

## 2. Verdict exécutif

Le commit reçoit `PASS`, sans finding scientifique ou de cohérence bloquant.

Les six blockers de la revue pré-intégration sont corrigés. Le `STOP` ne dépend ni d'une prétention de recherche exhaustive, ni d'un argument par silence bibliographique, ni d'un échec expérimental. Il repose sur deux bases positives et indépendantes:

1. une collision directionnelle directe avec State-Aware Runtime v2 et PLACEMEM v1;
2. une reconstruction du shell `Omega/G/B/Adeq/Cert/Cmp/T*/T_hat` par contrats, QoS, ressources vectorielles, temporalité, provenance, métarésonnement, Pareto et rejet.

Le souhait de guider les futurs LLM vers un état géré reste une direction d'ingénierie légitime. Le présenter comme l'article original demandé produirait toutefois une synthèse, une reformulation ou une roadmap des systèmes déjà publics. Le `STOP` respecte donc précisément l'exigence du propriétaire de ne pas réécrire les travaux antérieurs.

## 3. Vérification des blockers B-01 à B-06

| Blocker | Vérification sur `32adacc` | Résultat |
|---|---|---|
| `B-01`, adéquation mal typée | `TRANSITION_CONTRACT.md` sépare `Adeq`, les ensembles de violations `V_G/V_B`, `Cert`, `Cmp` et le statut du sélecteur. Deux violations peuvent coexister; `INCOMPARABLE` et `ABSTAIN` ne sont plus des valeurs d'adéquation. | `CORRIGÉ` |
| `B-02`, confusion entre idéal et estimateur | `T*(Omega,G,B)` utilise les quantités vraies; `T_hat(Omega,G,B;E_cal)` utilise une calibration gelée et ne reçoit pas les résultats de la cible. `ABSTAIN` appartient à `T_hat`, pas à `T*` ni à `Adeq`. | `CORRIGÉ` |
| `B-03`, théorème view-only trop large | Le handoff de réduction restreint explicitement la proposition aux obligations locales à un pas. Les contrats de trace utilisent une stratégie gagnante sous observation partielle. Le `STOP` est déclaré indépendant de ce lemme. | `CORRIGÉ` |
| `B-04`, inférence excessive sur une classe | `F_D=1` exige un témoin adéquat; l'échec d'un nombre fini d'implémentations ne prouve jamais `F_D=0`. Une impossibilité de classe exige une borne, un théorème ou une couverture exhaustive de la classe. | `CORRIGÉ` |
| `B-05`, dominance Pareto incomplète | La dominance impose aucune dégradation sur tous les axes déclarés et une amélioration stricte sur au moins un axe, avec régions d'incertitude simultanées. Les compromis croisés sont `INCOMPARABLE`. | `CORRIGÉ` |
| `B-06`, clôture de recherche surdéclarée | Les douze familles larges ont `included=NON DISPONIBLE` et `excluded=NON DISPONIBLE`, sans champ `PENDING`. Le protocole enregistre une déviation bornée et interdit toute prétention exhaustive ou d'absence d'antériorité. | `CORRIGÉ` |

## 4. Cohérence scientifique et de gouvernance

Les artefacts canoniques convergent vers la même décision:

- `CHARTER.md` indique que toutes les routes d'article sont arrêtées et que la route directionnelle M1b retourne `STOP`;
- `STATE.md` place le gate à `M1B-STOP-PENDING-FINAL-REVIEW-AND-PR`, marque l'article directionnel `NOT_ELIGIBLE` et n'autorise ni modèle, ni benchmark, ni expérience, ni manuscrit;
- `NOVELTY.md` enregistre `STOP`, `0 DISTINCT_CANDIDATE`, la collision directe, la réduction générique, le rejet de P04 comme pivot et la limite de recherche;
- la décision 0004 supersède uniquement l'autorisation directionnelle de la décision 0003 et conserve tous les `STOP` antérieurs;
- `CLAIM_LEDGER.csv` classe `CLM-009`, `CLM-011`, `CLM-012` et `CLM-013` comme `DISPUTED`;
- `LITERATURE_MATRIX.csv`, lignes `P-005` à `P-012`, relie chaque objet M1b au composite le plus fort et ne transforme aucun écart non mesuré en nouveauté;
- `experiments/registry.yaml` reste vide avec le statut `stopped_m1b_no_experiments`.

Les handoffs antérieurs conservent correctement leur état historique. Leurs formulations pré-correction ne remplacent pas les registres et contrats canoniques du commit examiné.

## 5. Vérification formelle

### 5.1 `Adeq`, `Cert` et `Cmp`

`Adeq(I;Omega,G,B)` est un prédicat vrai/faux sur l'absence simultanée de violations sémantiques et de ressources. `Cert(I;Omega,G,B,E)` est un statut empirique `PASS`, `FAIL` ou `UNRESOLVED`. `Cmp(I,J)` est une relation entre vecteurs de résultats complets d'implémentations adéquates. Cette séparation corrige l'erreur de catégorie signalée avant intégration.

### 5.2 `T*` et `T_hat`

`T*` est un sélecteur idéal, set-valued, sur classes faisables et résultats non dominés. `T_hat` est un estimateur empirique distinct, calibré avant les résultats cibles, avec statut décisionnel et abstention épistémique. Le shell idéal est classé `ANTICIPATED`; l'estimateur LLM quantitatif reste `UNSUPPORTED`, jamais `DISTINCT_CANDIDATE`.

### 5.3 Faisabilité de classe et Pareto

Les conclusions empiriques sont bornées aux implémentations testées, sauf argument couvrant toute une classe. La dominance est définie sur toutes les dimensions déclarées. Une amélioration de qualité ou de coût isolée ne suffit plus si un autre axe se dégrade. Aucune conclusion de classe ni aucun ordre total n'est inféré à partir d'une préférence choisie après les résultats.

## 6. Prédictions, contre-exemples et designs

Le registre contient exactement cinq prédictions:

| Prédiction | Statut normalisé | Disposition de nouveauté |
|---|---|---|
| `M1B-P01` | `ANTICIPATED` | régime négatif context-only connu |
| `M1B-P02` | `ANTICIPATED` | borne d'accès à l'information, pas supériorité d'architecture |
| `M1B-P03` | `ANTICIPATED` | valeur de computation |
| `M1B-P04` | `UNSUPPORTED` | `UNSUPPORTED_NOT_DISTINCT` |
| `M1B-P05` | `ANTICIPATED` | théorie générique du rejet |

Aucun statut `DISTINCT_CANDIDATE` n'est présent. Chaque ligne est marquée `FALSIFIABILITY_ONLY_FOR_STOPPED_OBJECT`.

Le registre de contre-exemples contient exactement `M1B-C01` à `M1B-C09`. Il distingue les falsificateurs dans le support, régimes hors support, instanciations orthogonales et falsificateurs contractuels indépendants. P01 à P05 ont chacune au moins un négatif relié, et les anciens mauvais ciblages de C02 à C06 sont corrigés.

Les designs contiennent exactement `M1B-D01` à `M1B-D05`. Le plancher arithmétique est correct:

- D01: `14 400` exécutions;
- D02: `14 400` exécutions, hors réinjections et transactions;
- D03: `57 600` exécutions si le plancher de puissance n'augmente pas `n`;
- D04: `48 000` exécutions avec cinq bras, hors détection, réparation et lifecycle;
- D05: `10 000` décisions de transition.

Le total est `134 400` exécutions ou policy-queries plus `10 000` décisions, soit `144 400` unités. GPU-heures, prix, stockage, énergie et temps mur restent correctement `NON DISPONIBLE`. Le document est marqué `DESIGN_ONLY_NOT_AUTHORIZED` et répète qu'aucune exécution n'est autorisée.

## 7. Recherche et portée de la conclusion

Le journal contient 31 lignes: douze requêtes larges, quatre requêtes jointes étroites et quinze résolutions directes. Aucun champ `PENDING` ne subsiste. Les douze requêtes larges n'ont que les cinq premiers titres examinés, avec décisions par titre non conservées. Les comptes inclusion/exclusion sont donc gelés à `NON DISPONIBLE`.

La recherche est ciblée et partiellement dépouillée, pas exhaustive. Le `STOP` n'utilise pas cette lacune comme preuve. State-Aware Runtime et PLACEMEM sont des collisions positives; la réduction générique est également positive. L'absence d'un factorial exact P04 dans le jeu lu n'est jamais présentée comme une nouveauté.

## 8. Vérification bibliographique

Les corrections du handoff bibliographique sont intégrées dans `EVIDENCE_LEDGER.csv` et `paper/references.bib`:

- State-Aware Runtime est épinglé au working paper v2 du 11 juillet 2026, DOI `10.33774/coe-2026-vt9t2-v2`, avec qualifier non peer-reviewed;
- PLACEMEM est épinglé à arXiv `2607.04089v1` et décrit comme systems position et prototype, sans venue inventée;
- ClawVM conserve arXiv v1, le DOI ACM, le booktitle EuroMLSys officiel et les pages 1-12;
- PersistBench conserve arXiv v2 et ICML 2026, sans DOI de proceedings ni pages inventés;
- X-Router conserve le DOI ACL, le booktitle complet et les pages 19856-19874;
- la ponctuation, les versions et les listes d'auteurs de VMG, Rational Metareasoning, A-TMA et des autres prépublications sont exactes dans les registres;
- W3C PROV distingue Tom De Nies comme auteur, James Cheney, Paolo Missier et Luc Moreau comme éditeurs, et le W3C comme institution émettrice.

Le contrôle primaire indépendant a confirmé les pages canoniques de State-Aware Runtime v2, PLACEMEM v1, PersistBench v2, STALE v1, A-TMA v2, Rational Metareasoning v3, ClawVM v1, VMG v2, When Should Memory Stay Silent v1, Shared Selective Persistent Memory v1, X-Router ACL et W3C PROV. La vérification n'est pas une nouvelle recherche exhaustive. Elle valide les métadonnées et qualifiers décisifs déjà sélectionnés.

Le BibTeX contient 33 entrées et 33 clés uniques, avec accolades équilibrées. Les URL arXiv décisives sont épinglées à une version. Aucun qualifier de prépublication ou working paper n'est surdéclaré en résultat universel ou publication évaluée par les pairs.

## 9. Findings

### 9.1 Bloquants

`AUCUN`

### 9.2 Non bloquants

#### NB-01: phrase administrative périmée dans `STATE.md`

`STATE.md:21` dit encore que la décision attend la revue bibliographique, alors que `STATE.md:53` et la checklist M1b indiquent correctement que cette revue est terminée et intégrée. La mise à jour mécanique qui ajoutera le présent handoff doit remplacer cette mention par l'attente de la RedTeam, de la CI et du merge, puis marquer la RedTeam terminée. Ce changement ne modifie aucune conclusion scientifique et ne nécessite pas une nouvelle revue si rien d'autre n'est changé.

#### NB-02: CI distante non encore observée

Les contrôles locaux passent, mais aucun résultat de PR n'était disponible sur le commit examiné. Le check protégé `validate` reste une condition de merge, pas un défaut scientifique du commit.

## 10. Commandes et contrôles exécutés

| Commande ou contrôle | Résultat |
|---|---|
| `git rev-parse --short=12 HEAD` | `32adaccc31bc` |
| `git show -s --format="%H%n%P%n%s" 32adacc` | SHA exact confirmé, parent `77ab855`, commit `docs: harden M1b STOP gate (#5)` |
| `git log --oneline 86cb827..32adacc` | deux commits d'intégration M1b inspectés |
| `git diff --stat 86cb827..32adacc` | périmètre M1b et gouvernance inspecté |
| `git diff --check 86cb827..32adacc` | `PASS` |
| `git diff --check main..32adacc` | `PASS` |
| `python scripts/validate_governance.py` | `governance validation passed` |
| `python -m unittest discover -s tests -v` | 4 tests, `OK` |
| parse CSV indépendant | 5 prédictions, 9 contre-exemples, 5 designs, IDs uniques, références de claims/evidence/matrix résolues |
| contrôle M1B_SEARCH_LOG | 31 lignes, aucun `PENDING`, douze paires `NON DISPONIBLE` cohérentes |
| contrôle BibTeX indépendant | 33 entrées, 33 clés uniques, 290 accolades ouvrantes et 290 fermantes |
| recalcul des designs | `14 400 + 14 400 + 57 600 + 48 000 + 10 000 = 144 400` |
| `git diff --name-status main..32adacc` | aucun chemin `carte-btp-mobile/`; uniquement les artefacts M1b et leurs contrôles de gouvernance |
| `git status --short` pendant la revue | `M scripts/validate_governance.py`, modification concurrente root hors du commit examiné; `?? carte-btp-mobile/`, répertoire utilisateur préexistant; `?? docs/research/handoffs/2026-07-14-m1b-luna-cross-review.md`, présent handoff. Le contenu scientifique a été lu depuis le commit exact `32adacc`; la modification concurrente du validateur n'appartenait pas à ce commit. |
| `git fsck --no-progress --connectivity-only` | code retour 0; connectivité valide, blobs non atteignables sans effet sur le commit |

## 11. Décision de merge

Verdict de contenu: `PASS`.

Le commit `32adacc` est scientifiquement prêt à entrer en PR. La fusion est recommandée après les étapes mécaniques suivantes:

1. ajouter ce handoff;
2. actualiser uniquement les statuts administratifs de `STATE.md` pour marquer la revue bibliographique et la RedTeam complètes;
3. rejouer le validateur, les tests et `git diff --check`;
4. obtenir le check distant protégé `validate` sur le dernier SHA de la PR;
5. fusionner avec l'historique linéaire exigé, puis fermer l'issue #5 et le milestone M1b.

Si l'intégration modifie une conclusion scientifique, une prédiction, un registre, un design, une source ou une formule au-delà de ces mises à jour mécaniques, une nouvelle revue du nouveau SHA exact est nécessaire.

Le merge n'autorise aucun article, manifeste, roadmap, benchmark, entraînement, modèle ou expérience. Il clôt la dernière route d'article actuelle avec `STOP` et `0 DISTINCT_CANDIDATE`.
