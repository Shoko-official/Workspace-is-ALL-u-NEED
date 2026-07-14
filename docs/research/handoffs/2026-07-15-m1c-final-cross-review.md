# Handoff final M1c: revue contradictoire consolidée

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_CROSS_REVIEW`

Date: `2026-07-15`

Issue: `#9`

Milestone: `M1c - Distinct technical object discovery`

Branche examinée: `agent/9-distinct-object-discovery`

Commit scientifique examiné: `f25098c258072db39e213b6a072097bf5068e64a`

Verdict des trois fonctions indépendantes: `MERGE`

Décision scientifique: `STOP`

Objets `DISTINCT_CANDIDATE` survivants: `0`

## 1. Objectif

Vérifier contradictoirement que le lot M1c satisfait l'exigence de ne pas remplacer une contribution scientifique originale par une réécriture, une taxonomie, un manifeste ou un assemblage de travaux existants. La revue devait déterminer si l'un des seize objets techniques survit aux collisions directes, aux composites les plus forts, aux réductions génériques, aux falsificateurs et au coût de discrimination minimal.

## 2. Périmètre et exclusions

Le périmètre comprend le registre des seize candidats, la décision 0005, les claims, les preuves, la matrice de littérature, le journal de résolution, le BibTeX, l'état opérationnel, le registre expérimental et les contrôles de gouvernance du commit `f25098c`.

Sont exclus:

- toute affirmation d'exhaustivité bibliographique;
- toute expérience, implémentation, formation de modèle ou rédaction de manuscrit;
- toute validation de résultats expérimentaux, car aucune expérience M1c n'a été autorisée ni exécutée;
- le répertoire utilisateur non suivi `carte-btp-mobile/`.

## 3. Hypothèses et questions testées

1. Au moins un candidat possède-t-il un observable, mécanisme, estimateur, invariant, bound ou théorème que le composite antérieur ne reconstruit pas?
2. Les mappings C08, C09, C12, C13, C14 et C15 sont-ils explicites plutôt que seulement nommés?
3. L'absence d'une cellule LLM exacte est-elle indûment transformée en preuve de nouveauté?
4. C14 et C15 sont-ils correctement bornés comme anticipations par composite, sans prétention d'anticipation directe?
5. Les registres, métadonnées, locateurs, statuts et autorisations convergent-ils vers la même décision?

## 4. Entrées et versions

- Commit scientifique: `f25098c258072db39e213b6a072097bf5068e64a`.
- Cutoff de recherche: `2026-07-15`.
- Registre: `M1C-C01` à `M1C-C16`.
- Preuves: `EV-0001` à `EV-0085`, dont les sources M1c décisives `EV-0064` à `EV-0085`.
- Claims: `CLM-001` à `CLM-015`.
- Matrice: 46 entrées de littérature pour 22 propriétés distinctes, dont `P-013` à `P-022` pour M1c.
- Sources adjacentes finales: Ziegler arXiv `2606.30975v1`, ShiftBench OpenReview `CCSztIjmOy`, MemDelta arXiv `2606.29914v1`, Hyperproperties DOI `10.3233/JCS-2009-0393`, et Bojinov-Shephard DOI `10.1080/01621459.2018.1527225` avec arXiv `1706.07840v2`.

## 5. Travail effectué

Trois fonctions indépendantes ont relu le même arbre scientifique:

- revue scientifique adversariale des réductions, composites et frontières de directness;
- revue bibliographique des titres, auteurs, dates, versions, identifiants, pages, URLs, locateurs et BibTeX;
- revue de gouvernance des CSV, références croisées, statuts, tests, périmètre Git et absence d'autorisation expérimentale.

Les corrections demandées avant verdict final ont été intégrées:

1. C03 et C10 ne sont plus décrits comme des collisions directes avec Causal Agent Replay ou CausalFlow. Ces sources fournissent des ingrédients; les objectifs globaux résiduels restent des extensions génériques sans estimateur ni théorème distinct.
2. C14 et C15 sont `ANTICIPATED_BY_COMPOSITE`, jamais `ANTICIPATED_DIRECTLY`.
3. Le registre distingue les collisions directes, les composites, les réductions génériques et l'absence de contenu technique distinct.
4. La réciprocité entre `CLM-015` et `EV-0072` à `EV-0074` a été restaurée.
5. `EV-0085` distingue la révision arXiv du 18 juillet 2017 du manuscrit daté du 19 juillet 2017; le PDF contient 42 pages.
6. Le PDF Hyperproperties est décrit comme 55 pages physiques, soit 54 pages d'article et une page de copyright.

## 6. Preuves et locateurs décisifs

### 6.1 C14, hystérésis de révision

- `EV-0081`, abstract, Sections 3.1 à 3.5, Equation 11 et Section 4: même cible atteinte par des chemins opposés sans reset, avec aire de boucle d'hystérésis signée.
- `EV-0084`, Section 2.3 Equation 2.6 et Section 7.2.4 Equation 7.5: propriétés à deux traces et non-interférence probabiliste.
- `EV-0050`, `EV-0056`, `EV-0062` et `EV-0063`: validité d'état LLM, temporalité et provenance de la vue courante.

Aucun document examiné ne rapporte le protocole LLM exact `A -> B -> A`. Le composite fournit toutefois la classe de phénomène, la condition à deux traces et les ingrédients LLM. L'application exacte ne fournit aucun nouvel estimateur, mécanisme, invariant ou résultat général.

### 6.2 C15, inversion reset-versus-stream

- `EV-0077`, Definition 1 et Sections 4.2 à 4.4: branches reset, persistante, persistante gouvernée et held-out.
- `EV-0082`, abstract et Section 1 Equation 1: inversions de sélection de politiques mémoire sous évaluation longitudinale.
- `EV-0083`, abstract et Sections 3 à 5: renversements de conclusions sous variation contrôlée et recommandation de vérifier la stabilité du classement.
- `EV-0085`, Section 2, Section 3.1 Definition 1 et Section 5.1 Equation 9: résultats potentiels indexés par chemin et tests causaux exacts.

Aucun document examiné ne rapporte l'inversion exacte entre classement reset-per-episode et classement persistent-stream. Le résultat serait une extension à l'axe d'héritage, pas un nouvel objet technique sous le seuil anti-assemblage. Le design crédible minimal demanderait 46 848 générations avant les écritures mémoire et les juges; son exécution ne réparerait pas l'échec de nouveauté.

### 6.3 Autres mappings structurants

- C08: replay hermétique sur un vecteur de dépendances fermé; toute dérive exige une preuve d'équivalence séparée.
- C09: équivalence probabiliste approchée sous le noyau d'observation cible.
- C12: `R_M = rho(K)` pour la matrice de reproduction multitype.
- C13: `lambda_H = H^-1 log(D_H / D_0)` comme gain logarithmique fini.

## 7. Incertitudes et contradictions

- La recherche est ciblée et non exhaustive. Le `STOP` n'utilise jamais le silence de recherche.
- Plusieurs sources de 2026 sont des prépublications susceptibles d'évoluer. Les versions lues sont épinglées et devront être revérifiées si un futur objet rouvre le programme.
- Le texte intégral local de ShiftBench a été bloqué par l'interface OpenReview. Seuls la page primaire, l'abstract et l'extrait indexé de la Section 1 ont été utilisés; aucune annexe non lue n'est revendiquée.
- Les cellules LLM exactes de C14 et C15 restent non rapportées dans les documents examinés. Cette limite est explicitement conservée et n'est pas convertie en nouveauté.

## 8. Fichiers du commit scientifique

Le commit `f25098c` modifie ou crée uniquement:

- `README.md`;
- `docs/research/CHARTER.md`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1C_CANDIDATE_REGISTER.md`;
- `docs/research/M1C_SCOPING_LOG.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/STATE.md`;
- `docs/research/decisions/0005-stop-distinct-object-discovery.md`;
- `experiments/registry.yaml`;
- `paper/references.bib`;
- `scripts/validate_governance.py`;
- `tests/test_validate_governance.py`.

## 9. Vérifications exécutées

| Vérification | Résultat |
|---|---|
| `python scripts/validate_governance.py` | `PASS` |
| `python -m unittest discover -s tests -v` | `5/5 PASS` |
| `git diff --check` | `PASS` |
| CSV indépendant | 85 preuves, 15 claims, 46 entrées de littérature et 22 propriétés distinctes; IDs uniques, colonnes et références valides |
| Réciprocité M1c claim-preuve | `PASS` après correction de `CLM-015` |
| Registre candidat | 16 candidats, huit champs requis pour chacun |
| BibTeX | 55 clés uniques, structure équilibrée, aucune duplication DOI, eprint ou URL |
| Registre expérimental | `stopped_m1c_no_experiments`; liste vide |
| Périmètre Git | aucun chemin `carte-btp-mobile/`; artefacts temporaires de lecture supprimés |

## 10. Décision recommandée

`MERGE` après passage du check distant protégé `validate`.

La décision scientifique reste `STOP`:

- zéro objet distinct;
- aucune expérience ou implémentation autorisée;
- aucun article, survey, manifeste ou roadmap autorisé;
- le présent audit négatif ne constitue pas l'article demandé.

## 11. Prochaine action autorisée

Pousser la branche, ouvrir une pull request contenant `Closes #9`, obtenir le check protégé `validate`, fusionner avec un historique linéaire, puis fermer le milestone M1c et réconcilier l'état opérationnel dans le cycle GitHub suivant. Toute réouverture scientifique doit commencer par un objet extérieur aux seize candidats arrêtés et satisfaire les décisions 0004 et 0005.

## 12. Rôles et indépendance

- Rôle auteur et intégrateur: direction scientifique du programme, responsable du gate et des corrections.
- Rôle de revue scientifique indépendant: réduction formelle, directness, strongest-composite et anti-assembly.
- Rôle bibliographique indépendant: métadonnées, versions, locateurs, pages et BibTeX.
- Rôle gouvernance et QA indépendant: registres, références croisées, tests, statut expérimental et périmètre Git.

Aucune fonction n'a validé seule sa propre conclusion. Les trois fonctions indépendantes ont rendu `MERGE` après correction de leurs findings.
