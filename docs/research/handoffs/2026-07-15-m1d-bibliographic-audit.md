# Handoff M1d: audit bibliographique indépendant

Status: `COMPLETE`

Type: `INDEPENDENT_BIBLIOGRAPHIC_AUDIT`

Date: `2026-07-15`

Issue: `#13`

Milestone: `M1d - Non-factorizing state-compute object discovery`

Branche examinée: `agent/13-nonfactorizing-state-compute`

Verdict: `PASS_AFTER_CORRECTIONS`

## 1. Objectif

Vérifier les identifiants, auteurs, titres, dates, versions, venues, locateurs et
limites de portée des sources décisives utilisées pour le gate M1d. L'audit est
bibliographique: il ne transforme ni une prépublication en résultat répliqué, ni
une absence de résultat exact en preuve de nouveauté.

## 2. Périmètre et exclusions

L'audit couvre les 26 identifiants arXiv demandés, les versions de venue
associées lorsque disponibles, ainsi que les sources primaires hors arXiv pour
la valeur du calcul, l'estimation doublement robuste adaptative, la médiation
longitudinale, la sous-modularité adaptative, l'optimisation en ligne, le
proof-carrying code, le calcul incrémentalement vérifiable et les POMDP.

Sont exclus l'évaluation de la vérité des résultats empiriques, la réplication
des artefacts, toute affirmation d'exhaustivité et toute décision autonome sur
la nouveauté scientifique.

## 3. Questions testées

1. Chaque identifiant et URL primaire résout-il vers le record déclaré?
2. Les titres, auteurs, versions et venues sont-ils attribués au bon support?
3. Les claims du registre restent-ils à l'intérieur de la portée de la source?
4. Les prépublications 2026 et leurs limites de réplication sont-elles signalées?

## 4. Entrées et versions

Les 26 identifiants arXiv testés existent et résolvent. Les entrées utilisées par
M1d ont été épinglées à leur version inspectée dans `EVIDENCE_LEDGER.csv` et
`paper/references.bib`. Les sources 2026 sans venue déclarée restent qualifiées
de prépublications et leurs résultats empiriques sont attribués aux auteurs.

Les entrées décisives sont `EV-0086` à `EV-0115`, avec réutilisation contrôlée de
`EV-0041`, `EV-0053`, `EV-0073` et `EV-0076`. Le cutoff est le 15 juillet 2026.

## 5. Travail effectué

Corrections structurantes intégrées:

1. `2210.10768v3` est *Anytime-valid off-policy inference for contextual
   bandits*, publié dans *ACM/IMS Journal of Data Science* en 2024, DOI
   `10.1145/3643693`.
2. `1811.03035v1` est le texte mono-auteur de Can Eren Sezener; il reste distinct
   du papier UAI 2020 de Sezener et Dayan.
3. Le titre NeurIPS 2021 exact est *The Adaptive Doubly Robust Estimator and a
   Paradox Concerning Logging Policy*.
4. `2203.15085v1` et la version revue au DOI `10.1515/jci-2022-0077` portent des
   titres légèrement différents; le support de chaque titre est conservé.
5. ReasoningBank est cité comme prépublication initialement déposée en 2025 et
   papier ICLR 2026.
6. Preble est un papier ICLR 2025, pas ICML.
7. La version 5 du travail sur l'adaptive submodularity corrige une preuve et
   affaiblit une garantie sous une hypothèse additionnelle.

## 6. Preuves et locateurs décisifs

- Waudby-Smith et al.: arXiv `2210.10768v3`, abstract, Section 1.1 Equation 4 et
  Section 1.2; DOI `10.1145/3643693`.
- Sezener: arXiv `1811.03035v1`, abstract, Section 2.4, Definition 10 et Equation
  2.43; Sezener-Dayan: PMLR 124, Section 2.2 et Definition 3.
- ReasoningBank: arXiv `2509.25140v2`, Sections 3.3 et 4.4, Figure 5.
- BudgetMem: arXiv `2602.06025v3`, Sections 4.1 à 4.3 et Appendix A.4.
- TriggerBench: arXiv `2606.23459v1`, Sections 4.2, 4.4, 5 et 6, Appendix C.3
  Table 16.
- CRAM: arXiv `2602.12204v1`, Sections 4.2 à 4.4, Equations 6 à 8 et Section 5.1.
- SAVeR: arXiv `2604.08401v1`, Sections 3.1 à 3.5.
- Proof-Carrying Code: DOI `10.1145/263699.263712`, pages 106 à 119; IVC: DOI
  `10.4230/LIPIcs.ITCS.2026.6`, pages 6:1 à 6:22.
- Sporadic Server: rapport primaire `CMU/SEI-89-TR-011`, abstract et analyse de
  schedulability des tâches périodiques et apériodiques à échéance.

## 7. Incertitudes et contradictions

- La borne de `2506.13048v1` concerne des modèles précis d'unlearning; elle ne
  supporte pas une borne universelle sur les workspaces LLM.
- Les garanties de valeur du calcul, OPE, médiation, sous-modularité et regret
  restent conditionnelles à leurs hypothèses.
- SAVeR vérifie et répare des états de croyance avant engagement d'action; il ne
  fournit pas un certificat incrémental sur un cône de dépendances.
- TriggerBench supporte l'effet de la charge de raisonnement sur la mémoire
  prospective. Son régime à une contrainte ne perturbe pas l'accuracy AIME au-
  delà de la variation standalone; la charge en intentions n'est pas variée.
- CRAM v1 contient un macro non résolu et un lien de code anonymisé. Son
  mécanisme divulgué constitue la collision utile; ses chiffres et son théorème
  annoncé ne sont pas décision-critiques sans réplication.
- Les garanties de transition du papier *Symmetry* restent limitées à
  l'abstraction symbolique produite par l'extracteur.

## 8. Fichiers concernés

- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/M1D_SCOPING_LOG.md`;
- `docs/research/M1D_CANDIDATE_REGISTER.md`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `paper/references.bib`.

## 9. Vérifications exécutées

- résolution des 26 identifiants arXiv: `PASS`;
- comparaison titres, auteurs, années, versions et venues: `PASS_AFTER_CORRECTIONS`;
- contrôle des locateurs et des limites de portée: `PASS_AFTER_CORRECTIONS`;
- présence des entrées BibTeX décisives: `PASS_AFTER_CORRECTIONS`.

## 10. Décision recommandée

L'audit bibliographique ne laisse aucun identifiant manquant ni contradiction de
métadonnées bloquante après correction. Il ne valide pas à lui seul le `STOP`:
la portée de la factorisation et les dispositions des candidats relèvent de la
revue scientifique indépendante.

## 11. Prochaine action autorisée

Faire relire les corrections de portée par une fonction scientifique distincte,
puis soumettre les registres à la validation de gouvernance. Aucun modèle,
benchmark, entraînement, expérience ou manuscrit n'est autorisé par cet audit.

## 12. Rôles et indépendance

- Fonction d'audit: vérification bibliographique indépendante, en lecture seule.
- Fonction auteur et intégrateur: direction scientifique du programme.
- Fonction de décision: revue scientifique contradictoire, distincte de l'audit
  bibliographique.
