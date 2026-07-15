# Handoff final M1d: revue contradictoire consolidée

Status: `COMPLETE`

Type: `FINAL_INDEPENDENT_CROSS_REVIEW`

Date: `2026-07-15`

Issue: `#13`

Milestone: `M1d - Non-factorizing state-compute object discovery`

Branche examinée: `agent/13-nonfactorizing-state-compute`

Commit scientifique examiné: `94fed8d8c893d76e96de23de165b535e73736e1e`

Verdict des trois fonctions indépendantes: `MERGE`

Décision scientifique: `STOP`

Objets `DISTINCT_CANDIDATE` survivants: `0`

## 1. Objectif

Vérifier que M1d recherche réellement un objet scientifique original entre état
persistant gouverné et calcul adaptatif, sans transformer le résultat en
réécriture, taxonomie, manifeste, roadmap, assemblage de composants ou
expérience destinée à réparer un échec de nouveauté.

## 2. Périmètre et exclusions

Le périmètre comprend les 24 candidats M1d, leurs falsificateurs, régimes
négatifs, collisions, composites, réductions, charges minimales, claims,
preuves, matrice de littérature, bibliographie, Decision 0006, état opérationnel,
registre expérimental et contrôles de gouvernance.

Sont exclus toute affirmation d'exhaustivité, toute expérience, implémentation,
formation de modèle, rédaction de manuscrit, réplication de prépublication ou
validation de résultats empiriques non exécutés dans ce dépôt.

## 3. Hypothèses et questions testées

1. Un candidat conserve-t-il un mécanisme, estimateur, invariant, bound, théorème
   ou loi prédictive après comparaison positive et réduction générique?
2. Le no-recycling exclut-il réellement M1c, validity-before-compute et les
   continuations ou certificats renommés?
3. La factorisation manager-router est-elle bornée à l'équivalence
   comportementale qu'elle démontre effectivement?
4. Les dispositions directes, composites, réduites, non distinctes et hors
   périmètre sont-elles soutenues individuellement et exhaustives?
5. Les sources, locateurs, références croisées, statuts et autorisations
   convergent-ils vers la même décision?

## 4. Entrées et versions

- commit scientifique: `94fed8d8c893d76e96de23de165b535e73736e1e`;
- cutoff bibliographique: `2026-07-15`;
- candidats: `M1D-C01` à `M1D-C24`;
- preuves M1d: 30 entrées décisives jusqu'à `EV-0115`, avec réutilisation
  contrôlée d'entrées antérieures;
- claims: `CLM-016` à `CLM-018`;
- matrice M1d: `P-023` à `P-035`;
- bibliographie: 85 clés uniques après intégration M1d.

## 5. Travail effectué

Trois fonctions indépendantes ont relu le même lot en lecture seule:

- revue scientifique adversariale des claim types, réductions, directness,
  composites et frontières d'admission;
- audit bibliographique des identifiants, titres, auteurs, dates, versions,
  venues, URLs, locateurs, BibTeX et limites de portée;
- audit de gouvernance des CSV, références croisées, matrice, statuts, tests,
  registre expérimental et périmètre Git.

Les corrections structurantes suivantes ont été exigées puis relues:

1. La règle de chaîne a été limitée à la loi comportementale à histoire fixe,
   avec conditionnelle régulière définie `pi_M`-presque sûrement. Elle ne conclut
   rien, à elle seule, sur l'ordre causal, le coût, la latence, l'apprentissage,
   l'optimisation ou la sample efficiency.
2. Les premières anticipations directes ont été reclassées. Le résultat final
   est `1 direct / 6 composite / 9 reduced / 2 unsupported / 6 out of scope`.
3. C11 nomme son effet longitudinal sous cohérence, positivité et échangeabilité;
   C12 combine AdaMEM et dynamic VoC; C17 cite le rapport primaire Sporadic
   Server.
4. C02, C23, C24, P-026 et P-033 demandent désormais des bornes dans une classe
   restreinte préenregistrée, pas une contradiction avec un état déclaré complet.
5. CRAM, SAVeR, MemRouter, INFERCEPT, TriggerBench et proof-carrying computation
   sont décrits dans leur portée exacte.
6. TriggerBench Appendix C.3 Table 16 est conservé comme contrôle négatif: une
   contrainte PM ne perturbe pas l'accuracy AIME au-delà de la variation
   standalone; la charge en intentions n'est pas variée.
7. La matrice explicite C02/C24, C09 et C19; les backrefs de `CLM-018` et le
   locator `EV-0089` ont été corrigés.

## 6. Preuves et locateurs décisifs

- Factorisation comportementale: `M1D_CANDIDATE_REGISTER.md`, section
  *Unrestricted behavioral factorization*; Decision 0006, section
  *The behavioral comparison class was underidentified*.
- Dynamic VoC: `EV-0087`, Definition 10 et Equation 2.43; `EV-0088`, Section 2.2
  et Definition 3.
- Longitudinal causal: `EV-0090`, Equation 1, assumptions A1-A2, Theorem 1 et
  Proposition 1.
- ReasoningBank: `EV-0095`, Sections 3.3 et 4.4, Figure 5.
- TriggerBench: `EV-0101`, Sections 4.2, 4.4, 5 et 6, Appendix C.3 Table 16.
- BudgetMem: `EV-0102`, Sections 4.1 à 4.3 et Appendix A.4.
- CRAM: `EV-0103`, Sections 4.2 à 4.4 et Section 5.1; les chiffres et le théorème
  annoncé ne sont pas décision-critiques.
- PCC et IVC: `EV-0112` et `EV-0113`; contrats symboliques et calcul
  incrémentalement vérifiable sous leurs hypothèses propres.
- Sporadic Server: `EV-0115`, rapport `CMU/SEI-89-TR-011`, abstract et analyse de
  schedulability.

## 7. Incertitudes et contradictions

- La recherche est ciblée et non exhaustive; aucun silence bibliographique ne
  supporte le `STOP`.
- Plusieurs sources 2026 sont des prépublications susceptibles d'évoluer.
- CRAM v1 conserve un macro non résolu et un artefact anonymisé.
- Une future borne de communication, information, calcul en ligne ou apprentissage
  reste possible en principe. Elle doit commencer comme nouvel objet formel dans
  une classe intrinsèque, pas comme réinterprétation de ce lot arrêté.
- Le résultat négatif satisfait la gouvernance, pas l'objectif programmatique de
  produire l'article original demandé.

## 8. Fichiers modifiés

Le commit scientifique et son intégration de revue touchent uniquement:

- `README.md`;
- `docs/research/CHARTER.md`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1D_CANDIDATE_REGISTER.md`;
- `docs/research/M1D_SCOPING_LOG.md`;
- `docs/research/NOVELTY.md`;
- `docs/research/STATE.md`;
- `docs/research/decisions/0006-stop-nonfactorizing-state-compute-discovery.md`;
- les deux handoffs M1d;
- `experiments/registry.yaml`;
- `paper/references.bib`;
- `scripts/validate_governance.py`;
- `tests/test_validate_governance.py`.

Le répertoire non suivi `.codex-remote-attachments/` reste hors périmètre.

## 9. Vérifications exécutées

| Vérification | Résultat |
|---|---|
| `python scripts/validate_governance.py` | `PASS` |
| `python -m unittest discover -s tests -v` | `5/5 PASS` |
| `git diff --check` | `PASS` |
| Registre candidat | 24 candidats; `1 + 6 + 9 + 2 + 6 = 24` |
| Réciprocité M1d claim-preuve | `PASS` |
| Matrice M1d | C02/C24, C09 et C19 explicitement couverts |
| BibTeX | 85 clés uniques, structure équilibrée |
| Registre expérimental | `stopped_m1d_no_experiments`; liste vide |
| Périmètre Git | `PASS`; `.codex-remote-attachments/` non suivi |

## 10. Décision recommandée

`MERGE` après passage du check distant protégé `validate`.

Decision 0006 peut être `ACCEPTED` avec `STOP` pour les 24 candidats, zéro objet
distinct et aucune autorisation de modèle, benchmark, implémentation,
entraînement, expérience, compute payant ou manuscrit.

## 11. Prochaine action autorisée

Pousser la branche, ouvrir une pull request contenant `Closes #13`, obtenir le
check protégé `validate`, fusionner avec historique linéaire, fermer le milestone
M1d, puis réconcilier l'état post-merge dans un nouveau cycle issue, milestone et
PR. Toute reprise scientifique doit commencer par un objet extérieur aux 24
candidats arrêtés.

## 12. Rôles et indépendance

- Fonction auteur et intégrateur: direction scientifique et propriétaire du gate.
- Fonction scientifique indépendante: portée mathématique, réductions,
  directness, strongest composite et anti-recycling.
- Fonction bibliographique indépendante: métadonnées, versions, locateurs,
  sources primaires et BibTeX.
- Fonction gouvernance indépendante: réciprocité, matrice, statuts, tests,
  registre expérimental et périmètre Git.

Aucune fonction indépendante n'a modifié les fichiers qu'elle a relus. Les trois
ont rendu `PASS` après correction.
