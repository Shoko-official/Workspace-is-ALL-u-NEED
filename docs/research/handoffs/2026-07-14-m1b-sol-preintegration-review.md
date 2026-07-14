# Revue scientifique indépendante pré-intégration M1b

Status: `COMPLETE`

HEAD examiné: `86cb827` (`docs: reduce M1b transition framework (#5)`)

Verdict scientifique: `STOP CONFIRMÉ`

État pré-PR: `NOT READY`, corrections de cohérence requises

Objet distinct survivant: `0 DISTINCT_CANDIDATE`

Date: `2026-07-14`

Issue: `#5`

## 1. Mission et périmètre

Cette revue teste indépendamment trois points:

1. si le verdict `STOP` de M1b suit bien des règles enregistrées dans l'issue `#5`;
2. si la direction souhaitée par le propriétaire, guider les futurs LLM vers un état géré, une persistance gouvernée et un calcul adaptatif, risque d'être présentée à tort comme une contribution nouvelle;
3. si les artefacts à intégrer sont scientifiquement et administrativement cohérents avant ouverture de la PR.

Le verdict porte sur l'éligibilité de l'article directionnel comme contribution originale. Il ne dit pas que l'état persistant, la provenance, la révocation, le calcul adaptatif ou l'abstention sont inutiles. Il ne teste aucune performance, aucun modèle n'ayant été exécuté.

Les modifications non commitées de `CLAIM_LEDGER.csv` et `EVIDENCE_LEDGER.csv` présentes dans le worktree ne font pas partie du HEAD examiné. Elles n'ont pas été utilisées pour attribuer au commit une conclusion qu'il ne contient pas encore.

## 2. Inventaire des preuves

| Élément | Ce qu'il établit | Fiabilité pour la décision | Limite |
|---|---|---|---|
| Issue `#5` | Règles `GO/PIVOT/STOP`, tests anti-réécriture, objets requis et interdiction d'un manifeste de repli | Élevée, critère enregistré avant conclusion | Les critères `GO` ne sont pas tous des prérequis logiques à un `STOP` fondé sur une réduction positive |
| `TRANSITION_CONTRACT.md` | Opérationnalisation de `Omega/G/B`, adéquation et `T`; verdict de réduction | Moyenne | L'adéquation, l'incertitude et l'incomparabilité y sont actuellement mélangées |
| `2026-07-14-m1b-sol-contract-reduction.md` | Réduction formelle à contrats assume/guarantee, QoS/SLO, ressources vectorielles, temporalité, cache, VOC, Pareto et rejet | Élevée pour le noyau générique | Une proposition de réalisabilité est formulée trop largement, voir B-03 |
| `2026-07-14-m1b-terra-stateful-systems.md` | Collision directe avec les systèmes stateful, mémoire gouvernée, régimes de bénéfice et de dommage | Moyenne à élevée | Plusieurs collisions récentes sont des prépublications; elles valent comme antériorités publiques mais pas comme résultats universels validés |
| `2026-07-14-m1b-terra-regime-boundaries.md` | Réduction de quatre familles de frontières, régimes négatifs, instanciations orthogonales et designs minimaux | Élevée pour la réduction, moyenne pour les coefficients empiriques | Aucun coefficient transportable ni estimateur ex ante n'est établi |
| `PREDICTION_REGISTER.csv` | Cinq hypothèses falsifiables ou contre-régimes | Moyenne | Statuts non normalisés, marges hétérogènes et plusieurs contradictions internes |
| `COUNTEREXAMPLE_REGISTER.csv` | Huit négatifs, dommages ou instanciations orthogonales | Moyenne | Plusieurs lignes ne réfutent pas la prédiction qu'elles ciblent, car leur régime est hors de ses prémisses |
| `MINIMUM_DISCRIMINATING_DESIGNS.md` | Plans de tests et plancher de 131 200 exécutions/décisions | Moyenne | Ce sont des unités d'exécution, pas un coût matériel complet; certains estimands et contrôles doivent être alignés |
| `NOVELTY.md`, `STATE.md`, décision 0003 | Historique M1 et autorisation conditionnelle d'auditer la thèse directionnelle | Élevée comme historique | Ces fichiers n'enregistrent pas encore le résultat M1b du HEAD |
| `M1B_SEARCH_LOG.csv` | 31 recherches ou résolutions avec heure et compte | Moyenne | 12 lignes conservent `included=PENDING` et `excluded=PENDING`; la clôture ne peut pas être déclarée complète |

## 3. Reconstitution indépendante du verdict

### 3.1 Pourquoi `GO` est exclu

Le test décisif de l'issue exige au moins un objet `DISTINCT_CANDIDATE` qui change une décision de conformité, un ordre prédit ou un falsificateur après effacement des composants et réduction au meilleur composite.

Le HEAD ne fournit aucun tel objet:

- `Omega` est un domaine d'exploitation, une distribution et des covariables ex ante;
- `G` est un contrat assume/guarantee enrichi de métriques QoS/SLO, de temporalité et de provenance;
- `B` est un ensemble de contraintes et mesures vectorielles de ressources;
- l'adéquation est une satisfaction de contrat avec incertitude empirique;
- la nécessité d'information persistante est une question de réalisabilité sous observation partielle;
- le bénéfice de persistance est une frontière d'amortissement, fraîcheur, erreur et maintenance;
- le calcul adaptatif est une décision de valeur de calcul conditionnelle à son coût;
- l'ordre entre systèmes adéquats est Pareto ou dépend d'une préférence déclarée;
- l'abstention est une décision de rejet sous incertitude ou identification partielle.

La combinaison est utile comme discipline d'évaluation. Aucun de ses éléments ni leur composition actuelle ne change une prédiction après substitution par ces abstractions établies.

### 3.2 Pourquoi l'absence d'un `T` complet n'est pas une nouveauté

Le candidat qui pourrait encore sembler original est un estimateur ex ante, calibré et transportable entre familles, de la forme `T_hat(Omega,G,B)`. Aucun estimateur, coefficient, seuil stable, marge de décision ou garantie de couverture n'est fourni.

Cette absence classe le candidat `UNSUPPORTED`, pas `DISTINCT_CANDIDATE`. Une variable non mesurée ou une loi non écrite ne peut pas devenir une contribution par le seul fait qu'aucune source ne l'a fournie sous la même notation.

### 3.3 Objection la plus forte: le résidu validité-avant-calcul

`M1B-P04` est le meilleur candidat à un `PIVOT`: tester si un routeur qui évalue la validité de l'état avant d'acheter du calcul domine un routeur basé seulement sur la difficulté.

Cette hypothèse est précise et testable, mais elle ne survit pas au grain revendiqué:

1. un décideur de valeur de calcul conditionne déjà son choix sur l'état d'information disponible;
2. un test de validité est une covariable ou une acquisition d'information supplémentaire, dont le coût et l'erreur doivent être chargés;
3. la séparation entre défaut de banque, défaut de récupération et défaut de réponse est déjà explicitée dans le corpus stateful;
4. aucune propriété des LLM, de l'autorégression ou des représentations linguistiques n'est utilisée pour déterminer le signe de l'interaction;
5. le seuil de 15 % porte sur l'économie de calcul du routeur, pas sur une loi LLM transportable de l'interaction validité par calcul.

Un factorial exact pourrait rester une expérience utile. Il ne constitue pas aujourd'hui une loi distincte, et une expérience non exécutée n'est pas un résultat original. `P04` reste donc `UNSUPPORTED`, sans justifier `PIVOT`.

### 3.4 Objection de recherche incomplète

Le journal M1b n'est pas clos au sens strict, et la revue bibliographique indépendante reste à intégrer. Cela interdit une affirmation d'exhaustivité ou d'absence d'antériorité.

Cela ne renverse pas le verdict actuel. Le `STOP` repose sur des reconstructions positives et sur l'absence de spécification du seul résidu possible, pas sur une recherche silencieuse. Une source manquante peut renforcer le `STOP`; elle ne peut rendre distinct un objet déjà réductible sans modifier cet objet.

### 3.5 Conclusion scientifique

Le verdict correct est `STOP`, avec confiance élevée pour le noyau formel et confiance moyenne à élevée pour la cartographie des travaux LLM récents. `PIVOT` serait injustifié car aucun résidu positif n'est nommé après réduction.

Le souhait du propriétaire reste légitime, mais il n'est pas satisfait par ces matériaux comme article original. Présenter `Omega/G/B/T`, le contrat de transition, la carte des régimes ou l'agenda de validation comme la contribution reviendrait précisément à transformer une synthèse rigoureuse en nouveauté déclarative. Ce serait une réécriture des abstractions et directions existantes, contrairement à la demande utilisateur et à l'issue `#5`.

## 4. Incohérences scientifiques bloquantes

### B-01: la relation d'adéquation est mal typée

`TRANSITION_CONTRACT.md:63-71` définit une fonction sur un seul système avec les valeurs `ADEQUATE`, `SEMANTIC_VIOLATION`, `RESOURCE_VIOLATION`, `INCOMPARABLE` et `ABSTAIN`.

- `INCOMPARABLE` est une relation entre au moins deux vecteurs de résultats, pas une propriété d'un système isolé.
- `ABSTAIN` est un statut épistémique de la décision, pas la vérité de l'adéquation.
- un système peut violer simultanément une garantie sémantique et une contrainte de ressource, ce que l'énumération exclusive ne représente pas.

Avant PR, séparer au minimum:

1. `Adeq(I;Omega,G,B)`, vérité ou vecteur de violations;
2. `Cert(I;E) in {PASS, FAIL, UNRESOLVED}`, statut de preuve empirique;
3. `Cmp(I,J) in {DOMINATES, DOMINATED, INCOMPARABLE}`;
4. le statut du sélecteur, notamment `ABSTAIN`.

Cette correction n'affaiblit pas `STOP`. Elle évite de donner au candidat arrêté une définition scientifiquement incorrecte.

### B-02: `T` idéal et estimateur empirique sont confondus

L'issue demande `T(Omega,G,B)`, tandis que `TRANSITION_CONTRACT.md:79` utilise `T(Omega,G,B,E)`. Le handoff formel distingue correctement la relation idéale, le certificat issu des données et un futur estimateur `T_hat`.

Il faut choisir une convention unique:

- `T*` pour la relation idéale définie sur des quantités vraies;
- `T_hat(Omega,G,B;E_cal)` pour l'estimateur entraîné ou calibré;
- `ABSTAIN` comme sortie de `T_hat`, pas comme vérité ontologique de `T*`.

Sans cette séparation, la prétention ex ante est circulaire: l'évidence des résultats peut entrer dans l'objet supposé prédire ces résultats.

### B-03: le théorème de réalisabilité view-only est trop large

Le handoff de réduction affirme qu'un système déterministe view-only existe si et seulement si l'intersection des sorties acceptables est non vide dans chaque classe d'équivalence visuelle.

Cette équivalence est correcte pour des obligations locales, à un pas, séparables par histoire. Elle n'est pas établie telle quelle pour des contrats de traces couplés dans le temps, des propriétés de vivacité, des contraintes cumulatives ou des stratégies interactives. Dans ces cas, une action localement admissible ne garantit pas l'existence d'une stratégie globale cohérente.

Avant PR, restreindre explicitement la proposition aux garanties de sortie à un pas, ou la remplacer par une condition standard de stratégie gagnante sous observation partielle. Le verdict de réduction ne doit pas dépendre de cette proposition; les réductions contractuelles et décisionnelles suffisent.

### B-04: l'inférence de classe dépasse les designs proposés

`F_D=1` signifie qu'au moins un membre d'une classe est adéquat. Inversement, conclure `F_D=0` exige un argument d'impossibilité, pas l'échec d'un ou deux représentants.

Les designs évaluent quelques réalisations. Ils peuvent établir une comparaison d'implémentations ou illustrer une borne informationnelle, mais pas déclarer une classe entière infaisable sauf si l'impossibilité découle des hypothèses d'accès à l'information. Toute conclusion de classe doit donc indiquer clairement si elle est théorique ou empirique.

### B-05: plusieurs usages de « Pareto-préférable » sont incomplets

Une amélioration de qualité non inférieure et un gain sur une seule ressource ne suffisent pas si une autre ressource se dégrade. La dominance exige une absence de dégradation sur tous les axes retenus et une amélioration stricte sur au moins un axe. Sinon, le résultat est `INCOMPARABLE`, sauf préférence gelée avant les résultats.

Cette définition doit être identique dans le contrat, les prédictions, les contre-exemples et les designs.

### B-06: la clôture de recherche ne peut pas encore être cochée

Douze lignes des requêtes enregistrées ont encore `included=PENDING` et `excluded=PENDING`. La conclusion peut rester `STOP`, mais `STATE.md` ne doit pas déclarer le journal complet tant que ces champs ne sont pas résolus ou reclassés comme déviation explicitement bornée.

## 5. Checklist de correction avant PR

### 5.1 `NOVELTY.md`

- [ ] Remplacer le statut de tête `M1_CURRENT_ROUTES_STOPPED_DIRECTIONAL_PIVOT_PENDING_REVIEW` par un statut M1b indiquant `STOP` pour l'article directionnel.
- [ ] Conserver les décisions M0/M1 comme historique, mais marquer clairement le `PIVOT` de la ligne 178 comme autorisation passée d'auditer, non comme décision encore active.
- [ ] Ajouter une section M1b distincte avec la question `Omega/G/B/T`, les résultats des tests anti-réécriture, `0 DISTINCT_CANDIDATE`, le rejet de `P04` comme pivot et la décision `STOP`.
- [ ] Dire explicitement que le corpus permet une synthèse ou une discipline d'évaluation, mais que cette valeur ne satisfait ni le gate d'originalité ni la demande de ne pas réécrire les travaux antérieurs.
- [ ] Ne pas transformer l'absence d'un estimateur cross-family en preuve de nouveauté.
- [ ] Ne pas prétendre à une recherche exhaustive; enregistrer la réduction positive et les limites de clôture.

### 5.2 `STATE.md`

- [ ] Mettre `Current gate` à `M1B STOP PENDING PR` ou un statut équivalent, puis `STOPPED` seulement après merge.
- [ ] Passer l'éligibilité de l'article directionnel de `NOT_ESTABLISHED` à `NOT_ELIGIBLE` sous la formulation M1b auditée.
- [ ] Mettre l'issue `#5` en phase d'intégration, revue et décision, pas en « Search and formal-reduction planning ».
- [ ] Mettre les handoffs Terra et Sol en `COMPLETE`; conserver librarian et QA comme `PENDING` tant qu'ils ne sont pas effectivement intégrés.
- [ ] Ajouter la décision M1b `STOP`, avec `0 DISTINCT_CANDIDATE` et aucun `PIVOT` résiduel.
- [ ] Résoudre ou retirer le blocker `B-009`, puisque l'audit a été exécuté et conclut négativement; ne pas le laisser décrire un travail non commencé.
- [ ] Remplacer `Next authorized action` par: corriger les incohérences, intégrer les revues indépendantes, enregistrer la décision, exécuter CI et ouvrir la PR. Ne pas autoriser validation empirique, implémentation ou manuscrit.
- [ ] Cocher uniquement les éléments M1b réellement achevés. Le log de recherche, la revue bibliographique, la revue sans blocker, la décision, CI et merge ne peuvent pas être cochés prématurément.
- [ ] Après merge, fermer l'issue et le milestone M1b seulement si les règles de gouvernance et la PR le prévoient.

### 5.3 Nouveau decision record

- [ ] Ne pas modifier rétrospectivement la décision 0003, qui est `ACCEPTED` et append-only.
- [ ] Créer une décision 0004 liée à l'issue `#5` et au milestone M1b, supersédant uniquement l'autorisation conditionnelle de la route directionnelle dans 0003.
- [ ] Enregistrer séparément: réduction du contrat, réduction des frontières, statut du résidu validité-avant-calcul, limites de recherche et absence d'expérience.
- [ ] Retourner `STOP` pour l'article directionnel et `NO PIVOT RESIDUAL`; ne pas affirmer que les systèmes gérés sont inférieurs.
- [ ] Interdire explicitement quatre conversions: article d'architecture, manifeste, roadmap/maturity model et publication du cadre de synthèse comme contribution originale.
- [ ] Lier les deux handoffs Terra, le handoff Sol, les registres, la revue bibliographique et la présente revue indépendante.
- [ ] Énoncer la seule condition de réouverture: une nouvelle loi LLM spécifique, mesurable ex ante, avec estimateur gelé, marge, instanciations orthogonales et résultat qui change une décision au-delà de Pareto/VOC. Cette condition n'est pas un `PIVOT` actuel.

### 5.4 `PREDICTION_REGISTER.csv`

- [ ] Normaliser `status` aux quatre classes de l'issue: `ANTICIPATED`, `PARTIAL`, `DISTINCT_CANDIDATE`, `UNSUPPORTED`. Déplacer `UNSUPPORTED_NOT_DISTINCT`, `ANTICIPATED_BY_GENERIC_THEORY` et `ANTICIPATED_OR_TAUTOLOGICAL` dans une colonne de disposition ou de notes.
- [ ] Marquer le registre entier comme artefact de falsifiabilité d'un objet arrêté, pas comme cinq prédictions comptées soutenant un article.
- [ ] Pour `P01`, remplacer `reuse <= 1` par une définition non ambiguë de l'absence de réutilisation, et imposer « aucun axe pire, au moins un strictement meilleur » avant d'écrire Pareto-préférable.
- [ ] Pour `P01`, rendre la colonne `falsification_margin` cohérente avec son nom: préciser la région qui rejette la prédiction, pas seulement les critères de succès.
- [ ] Pour `P02`, remplacer `current-version tolerance >= 99 percent` par un seuil de conformité correctement orienté.
- [ ] Pour `P02`, résoudre la contradiction entre un seuil de 99 % et « one or more verified stale answers »: une violation unique n'est décisive que si la tolérance est zéro ou si le taux franchit le seuil.
- [ ] Pour `P02`, expliciter qu'exposer l'update aux systèmes stateful et le retirer au système view-only teste une borne d'accès à l'information, pas une supériorité d'architecture. Ajouter un service live stateless ou une réinjection de l'update comme contrôle orthogonal si une conclusion de persistance est envisagée.
- [ ] Pour `P03`, remplacer l'AUC d'une difficulté générique par une mesure pré-outcome du gain marginal du traitement « calcul supplémentaire ». La difficulté seule ne garantit pas la valeur de calcul.
- [ ] Pour `P03`, aligner la marge de rejet locale avec le falsificateur: l'échec du gain de 15 % dans le régime préenregistré suffit; exiger une dominance fixe dans trois familles teste une revendication plus forte.
- [ ] Pour `P04`, définir l'estimand d'interaction et sa différence minimale scientifiquement pertinente. `CI excludes zero` n'est pas une marge d'effet.
- [ ] Pour `P04`, séparer réponse-only compute, acquisition/réparation d'état et coût du détecteur de validité.
- [ ] Pour `P05`, définir le score de couverture, le seuil de risque, la méthode d'incertitude, le coût de rejet et le split de calibration. Le seuil de 90 % est autrement arbitraire.
- [ ] Harmoniser toutes les colonnes `falsification_margin` comme critères de rejet quantitatifs, avec unité, direction et niveau d'incertitude.

### 5.5 `COUNTEREXAMPLE_REGISTER.csv`

- [ ] Ajouter un champ distinguant `WITHIN_SUPPORT_FALSIFIER`, `OUT_OF_SUPPORT_NEGATIVE_REGIME`, `ORTHOGONAL_INSTANTIATION` et `INDEPENDENT_CONTRACT_FALSIFIER`.
- [ ] Conserver `C01` comme négatif de `P01`, mais utiliser la définition complète de dominance vectorielle.
- [ ] Retirer `C02` de `P01` ou le classer comme complément hors support: son régime récurrent et stale viole les prémisses short/stable/no-reuse de `P01`.
- [ ] Retargeter `C03`: la fuite ou sycophancy de mémoire ne réfute pas l'impossibilité view-only de `P02` sous update absent; elle réfute une thèse universelle de bénéfice de persistance.
- [ ] Retargeter `C04`: l'infaisabilité de toute classe sous budget ne réfute pas le constat que view-only manque l'update; elle réfute l'existence d'un successeur stateful adéquat ou force `INFEASIBLE/ABSTAIN`.
- [ ] Conserver `C05` comme négatif direct de `P03` sous signal non informatif ou valeur homogène.
- [ ] Reclasser `C06` comme antériorité de non-monotonicité ou construire un vrai falsificateur de `P04` avec état contrôlé, compute answer-only et interaction nulle/inversée.
- [ ] Classer `C07` comme test d'instanciation orthogonale, pas comme contre-exemple au même sens que `C01` ou `C05`.
- [ ] Pour `C08`, remplacer « a single violation » par « une violation au-delà de la tolérance contractuelle ».
- [ ] Ajouter un enregistrement pour le négatif de `P05`, ou expliquer explicitement pourquoi son falsificateur reste seulement dans le prediction register.
- [ ] Remplacer les titres libres de la colonne source par des identifiants stables reliés à l'evidence ledger et à des locators.

### 5.6 `MINIMUM_DISCRIMINATING_DESIGNS.md`

- [ ] Ajouter une table de correspondance entre chaque design, le statut normalisé de sa prédiction et la raison pour laquelle le design est conservé malgré `STOP`.
- [ ] Dans `D01`, définir exactement la dominance Pareto sur qualité et chaque axe de ressource; traiter les autres résultats comme incomparables.
- [ ] Dans `D02`, préciser que l'infaisabilité view-only découle de l'hypothèse d'information absente, pas de l'échec observé d'un seul modèle. Ajouter ou mentionner les contrôles stateless live-input.
- [ ] Dans `D02`, aligner le seuil de currentness/provenance et le nombre de violations décisif avec `P02`.
- [ ] Dans `D03`, entraîner le proxy sur le gain causal du compute supplémentaire, sélectionner le meilleur fixed baseline sur calibration imbriquée, puis geler les seuils avant confirmation.
- [ ] Dans `D03`, prévoir une analyse de puissance pour les marges 15 % et 1 point, au lieu de traiter 400 instances comme justification autonome.
- [ ] Dans `D04`, définir un contraste d'interaction préenregistré et distinguer compute de réponse, détecteur de validité et réparation/acquisition d'état.
- [ ] Aligner `D04` avec le handoff de frontières, qui demande un bras `repair-plus-compute`. Si ce cinquième bras est ajouté à toutes les cellules, recalculer le plancher de `38 400` et le total `131 200`; sinon interdire explicitement toute réparation dans les bras answer-only.
- [ ] Dans `D04`, définir comment l'effet est agrégé ou transporté entre familles, plutôt que de considérer un seul CI non nul comme réplication.
- [ ] Dans `D05`, geler méthode d'abstention, calibration, coût de rejet et jeu de shift. La réutilisation gratuite des logs n'est valide que si toutes les variables ex ante ont été collectées prospectivement.
- [ ] Conserver `NON DISPONIBLE` pour GPU-heures, prix, stockage et énergie tant que modèles et matériel ne sont pas gelés. Ne pas présenter 131 200 comme un coût complet.
- [ ] Ne pas convertir ces designs en agenda expérimental autorisé après `STOP`; une nouvelle issue scientifique serait nécessaire.

## 6. Contrôles transversaux pré-PR

- [ ] Harmoniser `Omega`/`Ω`, `Adeq`, `Cert`, `Cmp`, `T*` et `T_hat` dans tous les artefacts.
- [ ] Réconcilier le grain des classifications: le shell de `T` est `ANTICIPATED`, l'estimateur quantitatif est `UNSUPPORTED`; éviter d'appeler le même objet entier `PARTIAL` ailleurs.
- [ ] Résoudre les 12 paires inclusion/exclusion `PENDING` du journal, ou enregistrer une déviation finale qui interdit toute revendication d'exhaustivité.
- [ ] Intégrer le bibliographic review avec vérification des versions, auteurs, venues et locators décisifs.
- [ ] Étendre la validation de gouvernance aux nouveaux CSV: header, enums, IDs uniques, références prediction-design, cibles de contre-exemples et statuts autorisés. Le validateur actuel ne les inspecte pas.
- [ ] Rejouer cette revue ou une revue RedTeam sur le HEAD exact après corrections. Le statut « no blocking findings » ne peut pas être coché sur le HEAD actuel.
- [ ] Exécuter les tests et le validateur de gouvernance, inspecter le diff et vérifier qu'aucun texte ne transforme le `STOP` en article de synthèse.

## 7. Décision de pré-intégration

| Question | Réponse |
|---|---|
| `STOP` est-il scientifiquement justifié? | `OUI`, confiance élevée |
| Un `DISTINCT_CANDIDATE` survit-il? | `NON` |
| `P04` justifie-t-il `PIVOT`? | `NON`, testable mais générique et sans loi LLM spécifiée |
| La direction demandée par l'utilisateur peut-elle être revendiquée comme contribution sur ce HEAD? | `NON`, elle serait une synthèse/reformulation |
| Le HEAD est-il prêt pour PR? | `NON`, blockers B-01 à B-06 et intégration documentaire incomplète |

La recommandation est d'intégrer `STOP`, de corriger les incohérences sans affaiblir l'historique, puis de soumettre un HEAD cohérent à une dernière revue indépendante. Aucun article, benchmark ou modèle ne doit être ouvert depuis ces objets arrêtés.
