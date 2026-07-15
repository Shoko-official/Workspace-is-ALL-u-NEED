# Handoff final M1f: revue contradictoire consolidée

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_CROSS_REVIEW`

Date: `2026-07-15`

Issue: `#21`

Milestone: `M1f - Mechanism-first technical object discovery`

Branche examinée: `agent/21-mechanism-first-object`

Commit scientifique examiné: `76d3ae0ee6266a5f8031e66f83f0d79b405fe033`

Commit scientifique fusionné après rebase protégé: `e5b4bd69a06b6959fd6c7d524a65ace396ad8112`

Commit de revue fusionné: `67c0bdcf4b68671cda91d40c56bde99333dc36c8`

Intégration protégée: `COMPLETE`

Verdict des trois fonctions indépendantes: `MERGE`

Décision scientifique: `STOP`

Objets examinés: `9`

Objets admis: `0`

Objets `DISTINCT_CANDIDATE` survivants: `0`

## 1. Objectif

Vérifier que M1f cherche un objet technique distinct plutôt qu'une réécriture
du rapport, une taxonomie, un manifeste ou un assemblage, et que son `STOP`
repose sur des collisions positives, des réductions ou des compilateurs exacts.

## 2. Périmètre et exclusions

Le périmètre comprend les neuf objets M1f, le crosswalk des 64 formulations
M1c-M1e, le rapport récupéré, les comparateurs symétriques, les résultats,
falsificateurs, régimes négatifs, preuves, claims, matrice, BibTeX, Decision
0008, état opérationnel, registre expérimental et contrôles de gouvernance.

Sont exclus une affirmation d'exhaustivité, une implémentation, une expérience,
un entraînement, un manuscrit, une réplication empirique et toute tentative de
créer la nouveauté après l'échec du gate.

## 3. Hypothèses et questions testées

1. Chacun des neuf objets fixe-t-il primitive, classe, comparateur, résultat,
   falsificateur, régime négatif et frontière de réduction?
2. Le compilateur O06 reproduit-il exactement la loi jointe sous ressources
   symétriques?
3. Le transcodage O08 ferme-t-il réellement le cas réversible et isole-t-il la
   perte non injective?
4. O05 utilise-t-il le bon critère de confidentialité approximative sans
   dépasser sa source?
5. Un objet distinct survit-il aux 64 antécédents, sources directes, strongest
   composite, substitution des labels et théorie générique?
6. Les statuts, comptes, références et autorisations convergent-ils?

## 4. Entrées et versions

- commit initial: `7429417724ddac33ef4fe987b08aca5642a9c0bf`;
- premier correctif: `c1472aa921e50bb2d4198de32aab178e580a4fe1`;
- commit scientifique final: `76d3ae0ee6266a5f8031e66f83f0d79b405fe033`;
- arbre scientifique fusionné byte-for-byte sous
  `e5b4bd69a06b6959fd6c7d524a65ace396ad8112`;
- état de revue fusionné sous
  `67c0bdcf4b68671cda91d40c56bde99333dc36c8`;
- rapport: 23 pages, SHA-256
  `c584128e870e22e2c0372c5cdc6dc41558f9655c256dc46770f50937cd2f8046`;
- objets: `M1F-O01` à `M1F-O09`;
- crosswalk: 16 M1c, 24 M1d et 24 M1e, soit 64 lignes uniques;
- preuves: 169 au total, dont `EV-0153` à `EV-0169` nouvelles;
- claims: 26 au total, dont `CLM-022` à `CLM-026` M1f;
- matrice M1f: `P-047` à `P-054`;
- bibliographie: 138 clés uniques.

## 5. Travail effectué

Trois fonctions indépendantes ont relu chaque état fixe en lecture seule.

1. Sur `7429417`, la science a passé. La gouvernance a bloqué l'en-tête M1e
   résiduel de `NOVELTY.md`. La bibliographie a bloqué UniTok, l'année du papier
   sur les audits, quatre titres et la portée attribuée à timing privacy.
2. Sur `c1472aa`, bibliographie et gouvernance ont passé. La science a bloqué le
   falsificateur O05, qui confondait probabilités différentes et violation DP,
   ainsi que deux résidus `IFC/DP`.
3. Sur `76d3ae0`, les trois fonctions ont rendu `PASS` sans blocker.

Les corrections ont également explicité `2S` en parallèle ou `2D` en
séquentiel pour O06, l'alphabet fini du compilateur par message et la réduction
de l'arrêt pour O07.

## 6. Preuves et locateurs décisifs

- O06: deux copies de `J(h,r)` donnent exactement `(m,c)` avec `2W/2S/D`, ou
  `2W/S/2D`; le compilateur par message exige un alphabet fini.
- O08: `C_ab = T_b o D_a` et
  `D_b(C_ab(T_a(x))) = x`; une collision non injective interdit la
  reconstruction universelle sans information additionnelle.
- O05: les deux inégalités événementielles `(epsilon,delta)` sont symétriques;
  une simple différence de probabilités ne falsifie que `(0,0)`.
- O07: `p[q,y]` émet une action interdite si et seulement si `q(y)` s'arrête;
  un vérificateur total déciderait l'arrêt.
- O03 et O04: collisions directes avec SpeedupLLM et TMA-NM.
- O01, O02 et O09: recyclage ou réduction positive documentée dans `P-047`,
  `P-048` et `P-054`.
- O08/report: UniTok discrétise des items de recommandation et ne segmente pas
  lexicalement prose, code ou mathématiques.

## 7. Incertitudes et contradictions

- Le résultat est ciblé et non exhaustif. Il ne prouve pas qu'aucun futur objet
  original n'existe.
- Plusieurs sources 2026 sont récentes, non évaluées ou non répliquées.
- Le facteur constant d'O06 peut encore avoir une utilité d'ingénierie, mais ne
  donne pas la séparation superconstante revendiquée.
- Les codecs non réversibles peuvent créer des compromis utiles, mais ceux-ci
  relèvent de perte d'information, migration ou rate-distortion.
- Le `STOP` satisfait le gate M1f, pas l'objectif programmatique de produire
  l'article original demandé.

## 8. Fichiers modifiés

Le lot M1f concerne uniquement:

- `README.md`;
- `docs/research/CHARTER.md`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1F_CANDIDATE_REGISTER.md`;
- `docs/research/M1F_SCOPING_LOG.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/STATE.md`;
- `docs/research/decisions/0008-stop-mechanism-first-object-discovery.md`;
- les deux handoffs M1f;
- `experiments/registry.yaml`;
- `paper/references.bib`;
- `scripts/validate_governance.py`;
- `tests/test_validate_governance.py`.

Le répertoire non suivi `.codex-remote-attachments/` reste hors périmètre.

## 9. Vérifications exécutées

| Vérification | Résultat |
|---|---|
| Revue scientifique finale sur `76d3ae0` | `PASS` |
| Audit bibliographique final sur `76d3ae0` | `PASS` |
| Audit de gouvernance final sur `76d3ae0` | `PASS` |
| `python scripts/validate_governance.py` | `PASS` |
| `python -m unittest discover -s tests -v` | `5/5 PASS` |
| `git show --check` et `git diff --check` | `PASS` |
| Objets et crosswalk | 9 objets; 64 lignes uniques; zéro admission |
| Réciprocité claim-preuve-matrice | `PASS` |
| BibTeX | 138 entrées et 138 clés uniques |
| Registre expérimental | liste vide; aucune expérience autorisée |
| Check protégé distant | [`validate` PASS](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/actions/runs/29429209486/job/87399526624) sur PR #22 |
| Intégration | PR #22 fusionnée avec historique linéaire sous `67c0bdcf4b68671cda91d40c56bde99333dc36c8` |
| Issue et milestone scientifiques | issue #21 fermée; milestone #11 fermé |
| Périmètre Git | `PASS`; attachment runtime non suivi |

## 10. Décision recommandée

`MERGE`, exécuté après passage du check distant protégé `validate`.

Decision 0008 est `ACCEPTED` avec `STOP` pour les neuf objets, zéro objet
distinct et aucune autorisation d'article, modèle, benchmark, implémentation,
entraînement, expérience ou compute payant.

## 11. Prochaine action autorisée

Réconcilier l'état post-merge sous l'issue #23 et le milestone #12 sans changer
le contenu scientifique. Après leur fermeture protégée, seule une nouvelle
recherche problem-first, issue-scoped et extérieure aux 73 formulations peut
rouvrir le programme.

## 12. Rôles et indépendance

- Fonction auteur et intégrateur: direction scientifique et propriétaire du gate.
- Fonction scientifique indépendante: portée mathématique, falsificateurs,
  réductions, comparateurs et admission.
- Fonction bibliographique indépendante: métadonnées, versions, locateurs,
  sources primaires et BibTeX.
- Fonction gouvernance indépendante: réciprocité, statuts, tests, registre
  expérimental, GitHub et périmètre Git.

Aucune fonction indépendante n'a modifié les fichiers relus. Les trois ont
rendu `PASS` sur le même commit scientifique final.
