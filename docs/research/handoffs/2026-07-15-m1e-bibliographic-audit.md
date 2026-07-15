# Handoff M1e: audit bibliographique indépendant

Status: `COMPLETE`

Type: `INDEPENDENT_BIBLIOGRAPHIC_AUDIT`

Date: `2026-07-15`

Issue: `#17`

Milestone: `M1e - Intrinsic restricted-class separation discovery`

Branche examinée: `agent/17-intrinsic-restricted-separation`

Commit scientifique examiné: `265ad2605381d7c94c01355b54a10e1c57884680`

Verdict: `PASS_AFTER_CORRECTIONS`

## 1. Objectif

Vérifier les identifiants, auteurs, titres, dates, versions, venues, locateurs,
BibTeX et limites de portée des sources qui déterminent le gate M1e. L'audit ne
transforme ni une prépublication en résultat répliqué, ni une absence de source
exacte en preuve de nouveauté.

## 2. Périmètre et exclusions

L'audit couvre `EV-0116` à `EV-0152`, avec réutilisation contrôlée de `EV-0090`,
les backrefs `CLM-019` et `CLM-021`, les lignes M1e `P-036` à `P-046`, le
registre candidat, le journal de recherche et les 122 entrées de
`paper/references.bib`.

Sont exclus la réplication des résultats, l'évaluation empirique, toute
affirmation d'exhaustivité et la décision scientifique autonome sur la
distinctness des candidats.

## 3. Questions testées

1. Chaque identifiant résout-il vers le record primaire déclaré?
2. Les titres, auteurs, années, versions et venues sont-ils attribués au bon
   support?
3. Les locateurs soutiennent-ils exactement le résultat mobilisé?
4. Les dispositions restent-elles dans la portée mathématique de leurs sources?
5. Les ledgers, la matrice et le BibTeX sont-ils réciproques et sans doublon?

## 4. Entrées et versions

Le cutoff est le 15 juillet 2026. Les versions décisives comprennent les records
ICLR 2026, NeurIPS 2025, COLT 2025, ICML 2017, AISTATS 2024, les versions arXiv
épinglées, les actes ICALP, ITCS, FOCS et SODA, ainsi que les articles de revue
causaux enregistrés dans `EVIDENCE_LEDGER.csv`.

Le commit relu contient 152 preuves au total. La tranche M1e comprend 37
nouvelles preuves plus `EV-0090`, 21 claims existent au total, la matrice compte
70 lignes de données, et le BibTeX contient 122 clés uniques.

## 5. Travail effectué

Les audits successifs ont exigé puis validé les corrections suivantes:

1. `EV-0117` est un poster ICLR 2026 sous OpenReview `RJDIX75TEE`, avec arXiv v2.
2. `EV-0118` utilise la publication principale NeurIPS 2025, volume 38; HiLD
   reste seulement une provenance antérieure.
3. `EV-0142` porte le titre publié *Compression Barriers in Autoregressive
   Transformers*, PMLR 291, et le lower bound temporel non adaptatif est le
   Theorem 19.
4. `EV-0144` pointe vers Appendix C.4 et Lemma C.24.
5. `EV-0119` sépare les décompositions formelles n-RASP-L de la généralisation
   apprise, qui est empirique.
6. C09 ajoute `EV-0134` et `EV-0139` pour l'OPE séquentiel et le traitement
   longitudinal.
7. C05 fixe le problème de matching maximum planaire de `EV-0148`, Result 2(ii).
8. C14 fixe le simple regret à budget donné de `EV-0151`, au lieu de fusionner
   découverte causale et best intervention.
9. `EV-0152` distingue la borne supérieure générale des bornes supérieures et
   minimax inférieures propres aux sous-classes.

## 6. Preuves et locateurs décisifs

- `EV-0116`: Proposition 3.1, Theorems 4.2, 4.5 et 5.3, corollaires associés.
- `EV-0117`: Propositions 1.1-1.2, Theorems 3.1-3.2 et 4.7.
- `EV-0118`: q-Sparse Token Regression, Theorems 1, 3, 5, 7 et 9.
- `EV-0119`: Definition 3.1, Propositions 3.2-3.4, Sections 4 et 6.
- `EV-0128` à `EV-0141`: locateurs d'identification, OPE, instruments,
  performativité, communication causale, intervention, croyance et médiation
  inscrits individuellement dans le ledger.
- `EV-0142`: Definition 4, Theorems 2, 5, 6, 8 et 19, Corollary 16.
- `EV-0144`: Definitions 4.1-4.4, Appendix C.4, Lemma C.24.
- `EV-0148`: Result 2(ii), formalisé par Theorem 4 pour le matching planaire.
- `EV-0151`: Algorithm 1, Definition 3, Theorems 2 et 5.
- `EV-0152`: Assumptions 2.1-2.3, Theorem 5.3 et Theorems 5.5-5.10.

## 7. Incertitudes et contradictions

- La recherche est ciblée, pas systématique; aucun silence bibliographique ne
  soutient la décision.
- Plusieurs sources récentes restent susceptibles de changer de version.
- C10 conserve un seuil nécessaire-et-suffisant non fourni par ses sources.
- C23 conserve des composants connus sans tâche ni frontière conjointe admise.
- Le résultat de généralisation de C20 reste empirique; seule la décomposition
  formelle est décisionnelle.
- `EV-0152` ne fournit pas un lower bound général distinct pour toute la classe
  Lipschitz.

## 8. Fichiers concernés

- `docs/research/EVIDENCE_LEDGER.csv`;
- `docs/research/CLAIM_LEDGER.csv`;
- `docs/research/LITERATURE_MATRIX.csv`;
- `docs/research/M1E_CANDIDATE_REGISTER.md`;
- `docs/research/M1E_SCOPING_LOG.md`;
- `paper/references.bib`.

## 9. Vérifications exécutées

- 38 preuves M1e contrôlées contre les sources primaires: `PASS`;
- métadonnées, versions, venues et locateurs: `PASS_AFTER_CORRECTIONS`;
- C05 contre `EV-0148` et C14 contre `EV-0151`: `PASS`;
- réciprocité claims, evidence et matrice: `PASS`;
- BibTeX: 122 entrées, 122 clés uniques, structure équilibrée;
- `git show --check` et `git diff --check`: `PASS`.

## 10. Décision recommandée

L'audit ne laisse aucun blocker bibliographique. Il recommande l'acceptation du
volet bibliographique de Decision 0007, sous réserve des revues scientifique et
de gouvernance distinctes, qui ont également rendu `PASS` sur le même commit.

## 11. Prochaine action autorisée

Intégrer les trois verdicts dans le handoff contradictoire final, accepter
Decision 0007, puis soumettre le tout au check distant protégé. Aucun article,
modèle, benchmark, entraînement ou expérience n'est autorisé.

## 12. Rôles et indépendance

- Fonction bibliographique indépendante: sources, versions, locateurs et
  portée, en lecture seule.
- Fonction scientifique indépendante: classes, théorèmes, réductions et
  distinctness.
- Fonction gouvernance indépendante: réciprocité, statuts, tests et périmètre.
- Fonction auteur et intégrateur: direction scientifique du programme.

Aucune fonction indépendante n'a modifié les fichiers relus.
