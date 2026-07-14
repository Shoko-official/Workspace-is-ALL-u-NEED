# Handoff M1b - Terra - Audit des systèmes avec état persistant

- Date de coupe : 2026-07-14
- Issue : [#5, M1b: audit a falsifiable transition thesis for managed-state LLMs](https://github.com/Shoko-official/Workspace-is-ALL-u-NEED/issues/5)
- Milestone : `M1b - Managed-state transition thesis novelty gate`
- Axe borné : memory-OS, agent-OS, agents stateful, mémoire récurrente/long contexte, apprentissage au temps de test, positions et roadmaps
- Recommandation de cet axe : **STOP** pour la thèse large `Ω/G/B -> état persistant géré` telle qu'elle est actuellement formulée
- Statut de revue : preuve primaire assemblée par Terra-Evidence ; revue indépendante Luna requise avant intégration au verdict M1b global

## 1. Objectif

Déterminer si les travaux primaires disponibles au 2026-07-14 anticipent déjà une thèse directionnelle, falsifiable et indépendante d'une implémentation qui associerait :

- un descripteur ex ante de workload `Ω` ;
- un contrat de garanties comportementales `G` ;
- une enveloppe vectorielle de ressources `B` ;
- une règle de transition `T(Ω,G,B)` entre traitement context-only, état persistant géré, calcul fixe ou adaptatif, et abstention.

L'audit ne cherche pas une occurrence littérale de la notation. Il cherche la substance observable après suppression des noms, substitution des labels et composition des antériorités les plus fortes. L'absence d'une formule identique n'est jamais utilisée comme preuve de nouveauté.

## 2. Périmètre et exclusions

### 2.1 Inclus

- Articles primaires et actes officiels publiés ou prépubliés avant la date de coupe.
- Systèmes de mémoire ou d'OS pour agents, contrats d'état, politiques de cycle de vie, isolation, provenance, versionnement et oubli.
- Travaux caractérisant les workloads, coûts de construction/maintenance/service, frontières de faisabilité et régimes négatifs.
- Mémoire récurrente, compressive, paramétrique et apprentissage au temps de test lorsque ces mécanismes délimitent ce que signifie « état persistant » indépendamment d'une architecture externe.
- Surveys, positions et roadmaps seulement lorsqu'ils formulent une taxonomie, une règle de passage, un contre-régime ou un agenda technique pertinent.

### 2.2 Exclus

- Blogs, billets commerciaux, agrégateurs et résumés secondaires comme preuve décisive.
- RAG sans état durable, mutation, cycle de vie, sélection de régime ou contrainte de ressources.
- Checkpointing d'entraînement sans rapport avec l'état opérationnel d'un agent.
- Doublons de versions, la version épinglée la plus récente ou la version de publication étant privilégiée.
- Audit exhaustif de la branche « adaptive computation/metareasoning », traité par un autre axe M1b.
- Toute déclaration de nouveauté, rédaction d'article ou implémentation.

### 2.3 Critères de sélection et déduplication

Une source est retenue si son document primaire formalise, implémente ou évalue au moins un des objets `Ω`, `G`, `B`, `T`, ou un mécanisme d'état qui contraint leur interprétation. Les sources sont dédupliquées par DOI, identifiant arXiv, puis titre et auteurs. Les affirmations substantielles reposent sur le texte intégral officiel ; une source dont seul le résumé officiel a pu être exploité est explicitement bornée à ce résumé.

## 3. Hypothèses et questions examinées

### 3.1 Hypothèse nulle

Le plus fort composite d'antériorités reconstruit déjà la substance de la thèse : sélectionner une forme de mémoire à partir de la structure du workload, de garanties requises et de budgets de construction/service, avec des régimes où la mémoire doit être évitée ou où les garanties sont infaisables.

### 3.2 Hypothèse de contribution résiduelle

Il existe un résidu techniquement distinct : une règle pré-outcome, calibrée, abstentionnelle et réellement implementation-neutral, entraînée ou testée sur plusieurs familles non isomorphes d'état, qui prédit le passage de context-only à état géré à partir de mesures ex ante de `Ω`, `G` et `B`.

### 3.3 Questions décisives

1. Les dimensions proposées pour `Ω`, `G` et `B` sont-elles déjà divulguées séparément ou par composition ?
2. Les travaux existants disent-ils seulement comment construire une mémoire, ou aussi quand la choisir, la taire, l'oublier ou déclarer une garantie infaisable ?
3. Une substitution de vocabulaire suffit-elle à faire correspondre `T` à des recommandations, politiques d'admission, frontières de Pareto ou contraintes de faisabilité connues ?
4. Après effacement des composants, reste-t-il une loi prédictive opérationnelle avec variables mesurables, seuils, perte, calibration, abstention et contre-exemples ?

## 4. Entrées et versions des sources

### 4.1 Entrées du dépôt

| Entrée | Usage dans l'audit |
|---|---|
| `docs/research/STATE.md` | État M1b actif, périmètre et handoff attendu. |
| Issue GitHub #5, état `OPEN`, mise à jour 2026-07-14 | Objets `Ω/G/B/T`, critères GO/PIVOT/STOP et exigence de prédictions falsifiables. |
| `docs/research/decisions/0003-m1-stop-budgeted-workspace-route.md` | Interdit de recycler l'ancienne architecture ; exige contrats, frontières mesurables et contre-régimes. |
| `docs/research/NOVELTY.md` | Le pivot directionnel doit s'arrêter s'il n'est qu'une synthèse memory-OS/agent-OS/stateful/long-context/TTT/roadmap. |
| `docs/research/handoffs/README.md` | Contrat de structure du présent handoff. |
| Handoffs M1 Terra, Luna et Sol du 2026-07-14 | Antécédents de recherche, réductibilité et besoin de revue indépendante. |

### 4.2 Inventaire primaire épinglé et locators

| ID | Source primaire et version épinglée | Locator précis | Collision décisive avec la thèse |
|---|---|---|---|
| S1 | [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads, arXiv:2606.06448v1](https://arxiv.org/abs/2606.06448v1), 2026-06-04 | Abstract ; §§1-2.2 ; §3.3 ; recommandations 1-6, §§4.1-4.8 | Caractérise les phases et workloads, mesure tokens, latence, énergie, VRAM/HBM et stockage, construit une frontière Construction-Serve-Accuracy, recommande le système selon arrivées de requêtes et famille de tâches, et impose une contrainte dure fraîcheur-latence. Collision positive la plus forte pour `Ω`, `B` et une partie de `T`. |
| S2 | [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents, arXiv:2604.10352v1](https://arxiv.org/abs/2604.10352v1), EuroMLSys 2026, [DOI 10.1145/3805621.3807648](https://doi.org/10.1145/3805621.3807648) | Abstract ; §2 ; §3 ; §§5.1-5.3 ; §7 | Pages typées, provenance, portée, fidélité minimale, dégradation admissible, writeback validé et budget de tokens. Si l'ensemble minimal dépasse le budget, toute politique faute et le système le signale. Collision `G x B` et régime d'infaisabilité. |
| S3 | [A Survey on Long-Term Memory Security for LLM Agents: A Vulnerability-Mechanism-Guarantee Taxonomy, arXiv:2604.16548v2](https://arxiv.org/abs/2604.16548v2), 2026-06-11 | §§1-2 ; §5 | Cycle Write/Store/Retrieve/Execute/Share/Forget-Rollback et cinq prédicats : autorisation d'écriture, provenance complète, retrieval scoped, rollback exact et oubli vérifié. Complète `G` au niveau sécurité/gouvernance. |
| S4 | [MemOS: A Memory OS for AI System, arXiv:2507.03724v4](https://arxiv.org/abs/2507.03724v4), 2025-12-03 | Abstract ; §§1-2.4 ; MemCube pp. 13-16 ; transactions p. 19 ; scheduler p. 20 ; cycle de vie/rollback p. 21 | Présente explicitement le passage stateless vers mémoire persistante comme ressource gérée, versionnée et schedulable. Anticipe la direction, mais pas une règle négative calibrée de transition. |
| S5 | [AIOS: LLM Agent Operating System, arXiv:2403.16971v5](https://arxiv.org/abs/2403.16971v5), COLM 2025 | Abstract ; §1 ; §§3.2-3.8 ; §4.1 | Scheduling, snapshots de contexte, opérations mémoire, swap, stockage persistant, isolation et confirmation d'opérations destructives sous concurrence. Anticipe l'agent-OS et la gestion de ressources, pas `T`. |
| S6 | [MemGPT: Towards LLMs as Operating Systems, arXiv:2310.08560v2](https://arxiv.org/abs/2310.08560v2), 2024-02-12 | Abstract ; §§2-2.4, pp. 2-4 | Pagination entre contexte borné et niveaux persistants, fonction executor et flux multi-session. Source technique primaire de la lignée MemGPT/Letta ; aucune sélection ex ante entre context-only et persistance. |
| S7 | [Are We Ready For An Agent-Native Memory System?, arXiv:2606.24775v1](https://arxiv.org/abs/2606.24775v1), 2026-06-23 | Abstract ; §§4.3-4.4 ; §§5.3-5.4 | Aucune architecture ne domine ; le bon système dépend du bottleneck, des mises à jour et de l'horizon. La réflexion ajoutée peut dégrader les résultats et Long Context peut gagner sur certaines tranches. Collision `Ω`, Pareto et contre-régimes. |
| S8 | [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers, arXiv:2603.07670v1](https://arxiv.org/abs/2603.07670v1), 2026-03-08 | §§2.1-2.3 ; §3.1 ; §§7.1-7.6 ; §§8-9 | Formalise write-manage-read sous contraintes, recommande de commencer par un pattern externe modulaire puis de passer au tiered learned uniquement si les données du workload le justifient ; context-only convient aux tâches courtes/prototypes. `T` qualitatif et post-mesure, non calibré. |
| S9 | [Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents, arXiv:2502.06975v1](https://arxiv.org/abs/2502.06975v1), 2025-02-10 | §§1-2 ; §3, tableau 2 ; §4.3 ; §5 | Compare état contextuel, externe et paramétrique, coûts constants ou croissants, consolidation et alternatives explicites où une couche épisodique serait inutile. Anticipe la direction et ses objections. |
| S10 | [Position: Compatibility-First Design Is Critical for Progress in Agentic Memory](https://openreview.net/forum?id=6OpIEryEWm), soumission ICML 2026, version 2026-06-24 | Abstract ; §3.1 ; annexe C.2, p. 18 | Contrat d'interface store/retrieve/update/delete, identifiants, métadonnées, scopes, hooks de version et permissions, erreurs et évaluation. Rend une partie de `G` implementation-facing, mais laisse la sémantique et la récupération non contraintes. |
| S11 | [When Should Memory Stay Silent? A Behavioral Benchmark for Sensitive Inference in Personalized LLMs, arXiv:2606.06055v1](https://arxiv.org/abs/2606.06055v1), 2026-06-04 | Abstract ; §§1-4 ; tableau 1 ; annexe E.8 | Sépare consentement de stockage, pertinence et warrant d'usage courant ; compare no-memory, contexte complet et mémoires ; recommande décision retrieval/génération à deux étages, ask-before-use et révocation. Régime négatif direct : la mémoire doit parfois rester silencieuse. |
| S12 | [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?, arXiv:2602.01146v2](https://arxiv.org/abs/2602.01146v2), ICML 2026, 2026-06-02 | Abstract ; §§1, 3-7 ; annexe R.4 | Mesure leakage inter-domaines et sycophancy induite par mémoire ; définit quand une mémoire est réellement in-domain. Régime négatif pour conservation, retrieval et usage. |
| S13 | [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents, arXiv:2607.02255v1](https://arxiv.org/abs/2607.02255v1), 2026-07-02 | Résumé officiel seulement pour les affirmations retenues | Formule « memory as a contract about what future decision sees » et compare no-store à skill-memory. Résultat directionnel étroit, non significatif et non généralisable à `T`. |
| S14 | [Memory in the LLM Era: Modular Architectures and Strategies in a Unified Framework, arXiv:2604.01707v2](https://arxiv.org/abs/2604.01707v2), PVLDB manuscript, 2026-05-01 | Abstract ; §1 ; §8.2 ; §8.6 ; §9 | Précédent anti-réécriture : cadre unifié, comparaison empirique puis assemblage explicite de modules MemTree, MemOS et MemoryOS. Une nouvelle taxonomie plus assemblage est déjà une forme publiée de contribution. |
| S15 | [Memory in the Age of AI Agents, arXiv:2512.13564v2](https://arxiv.org/abs/2512.13564v2), 2026-01-13 | Abstract ; taxonomie Forms/Functions/Dynamics ; fronts de recherche | Positionne la mémoire comme primitive de premier rang et cartographie déjà la direction. Survey, sans règle prédictive `T`. |
| S16 | [Lifelong Learning of Large Language Model Based Agents: A Roadmap, arXiv:2501.07278v2](https://arxiv.org/abs/2501.07278v2), IEEE TPAMI, 2026-01-11 | Abstract ; §§3.1, 3.3, 6-9, 15 | Roadmap perception-mémoire-action, stabilité/plasticité et apprentissage permanent. Anticipe l'agenda directionnel, sans transition resource-conditioned. |
| S17 | [Learning to (Learn at Test Time): RNNs with Expressive Hidden States, arXiv:2407.04620v4](https://arxiv.org/abs/2407.04620v4), 2025-08-31 | Abstract ; §1 ; §2.1 | État caché appris au temps de test, taille fixe et coût asymptotique constant ; les coûts I/O et wall-clock peuvent annuler le bénéfice. Montre une implémentation interne non isomorphe de l'état. |
| S18 | [Titans: Learning to Memorize at Test Time, arXiv:2501.00663v1](https://arxiv.org/abs/2501.00663v1), NeurIPS 2025 | Abstract ; §2.1 | Mémoire neuronale persistante à long terme et oubli appris, distincts d'un store externe. Anticipe un mécanisme, pas une règle de sélection. |
| S19 | [Self-Adapting Language Models, arXiv:2506.10943v2](https://arxiv.org/abs/2506.10943v2), 2025-09-18 | Abstract ; §1 | Adaptation persistante par auto-éditions de poids au temps de test. Élargit la classe d'implémentations que `T` devrait comparer et gouverner. |
| S20 | [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention, arXiv:2404.07143v2](https://arxiv.org/abs/2404.07143v2), 2024-08-09 | Abstract ; §1 | Mémoire compressive bornée en mémoire et calcul pour flux très longs. Contredit une dichotomie simple contexte externe/persistance. |
| S21 | [Recurrent Memory Transformer, arXiv:2207.06881v2](https://arxiv.org/abs/2207.06881v2), NeurIPS 2022 | Abstract ; méthode des memory tokens récurrents | L'état passe entre segments à l'intérieur du modèle. Autre réalisation non isomorphe de l'état persistant/récurrent, sans `G` de cycle de vie ni `T`. |

## 5. Travail réalisé

### 5.1 Méthode de recherche

La recherche a combiné :

1. des seeds connus des familles MemGPT/Letta, MemOS, AIOS, mémoire agent-native, long contexte et test-time learning ;
2. des requêtes ciblant non seulement les architectures, mais les expressions « when should », contrats, budgets, contraintes de faisabilité, abstention, oubli et régimes context-only ;
3. un backward snowball depuis ClawVM, Agent Memory, les surveys et positions ;
4. un forward search par titre exact pour ClawVM et Agent Memory ;
5. une itération supplémentaire sur les familles nouvellement découvertes, notamment les régimes négatifs.

Le moteur de recherche n'a exposé aucun nombre total stable de résultats. `NON DISPONIBLE` signifie donc que seule une liste classée de résultats visibles était fournie, sans cardinalité du corpus. Ce journal n'est pas un protocole PRISMA et ne prouve pas l'exhaustivité.

### 5.2 Journal des requêtes exactes

| Q | Date | Requête exacte | Nombre total | Discovery path / résultat utile |
|---|---|---|---|---|
| Q1 | 2026-07-14 | `"T(Omega, G, B)" LLM memory persistent state` | NON DISPONIBLE | Recherche de collision littérale ; aucune formule primaire identique retenue, sans inférence de nouveauté. |
| Q2 | 2026-07-14 | `"persistent memory" LLM agents workload guarantees budget when to use` | NON DISPONIBLE | Cadres workload/garanties/budget ; conduit aux familles Agent Memory et positions. |
| Q3 | 2026-07-14 | `"stateful agents" LLM framework roadmap memory persistent state` | NON DISPONIBLE | Surveys, roadmaps et systèmes stateful. |
| Q4 | 2026-07-14 | `"memory operating system" LLM agents MemOS` | NON DISPONIBLE | MemOS et MemoryOS. |
| Q5 | 2026-07-14 | `site:arxiv.org/abs AIOS LLM Agent Operating System resource scheduling memory context 2024` | NON DISPONIBLE | AIOS, versions arXiv et publication COLM. |
| Q6 | 2026-07-14 | `site:arxiv.org/abs AgentOS operating system LLM agents memory scheduling` | NON DISPONIBLE | Analogues agent-OS ; déduplication vers AIOS/MemOS. |
| Q7 | 2026-07-14 | `site:openreview.net AIOS LLM agent operating system COLM 2025` | NON DISPONIBLE | Statut de publication primaire AIOS. |
| Q8 | 2026-07-14 | `site:arxiv.org/abs "operating system" "LLM agents" memory context scheduling` | NON DISPONIBLE | Familles OS et scheduling. |
| Q9 | 2026-07-14 | `site:arxiv.org/abs/2310.08560 MemGPT virtual context management operating system persistent memory` | NON DISPONIBLE | MemGPT primaire. |
| Q10 | 2026-07-14 | `site:research.memgpt.ai MemGPT paper virtual context management` | NON DISPONIBLE | Discovery path officiel MemGPT/Letta ; preuve décisive conservée sur arXiv. |
| Q11 | 2026-07-14 | `site:arxiv.org/abs Letta stateful agents memory operating system` | NON DISPONIBLE | Lignée Letta ; source technique primaire stable retenue : MemGPT. |
| Q12 | 2026-07-14 | `site:openreview.net MemGPT Towards LLMs as Operating Systems` | NON DISPONIBLE | Vérification de publication ; version arXiv v2 épinglée. |
| Q13 | 2026-07-14 | `site:openreview.net "Position" agent memory LLM stateful persistent memory roadmap` | NON DISPONIBLE | Position Compatibility-First. |
| Q14 | 2026-07-14 | `site:arxiv.org/abs "position paper" LLM agent memory persistent state` | NON DISPONIBLE | Position Episodic Memory. |
| Q15 | 2026-07-14 | `site:arxiv.org/abs LLM agent memory research agenda framework lifecycle governance` | NON DISPONIBLE | Surveys, VMG, lifecycle et gouvernance. |
| Q16 | 2026-07-14 | `site:arxiv.org/abs "stateful" "LLM agents" memory framework` | NON DISPONIBLE | Agent Memory et cadres stateful. |
| Q17 | 2026-07-14 | `site:arxiv.org/abs/2606.24775 "Agent-Native Memory System"` | NON DISPONIBLE | Agent-Native Memory primaire. |
| Q18 | 2026-07-14 | `site:arxiv.org/abs/2606.06448 "system recommendations" agent memory amortization freshness` | NON DISPONIBLE | Agent Memory, recommandations et contrainte de fraîcheur. |
| Q19 | 2026-07-14 | `site:arxiv.org/abs/2604.10352 ClawVM contract minimum-fidelity invariant token budget` | NON DISPONIBLE | ClawVM et frontière `G x B`. |
| Q20 | 2026-07-14 | `site:openreview.net "Compatibility-First Design" agentic memory interface` | NON DISPONIBLE | Contrat d'interface Compatibility-First. |
| Q21 | 2026-07-14 | `site:arxiv.org/abs "Learning to (Learn at Test Time)" expressive hidden states` | NON DISPONIBLE | TTT, état caché et coûts I/O. |
| Q22 | 2026-07-14 | `site:arxiv.org/abs Titans Learning to Memorize at Test Time persistent memory` | NON DISPONIBLE | Titans. |
| Q23 | 2026-07-14 | `site:arxiv.org/abs SEAL self-adapting language models test-time adaptation memory` | NON DISPONIBLE | SEAL. |
| Q24 | 2026-07-14 | `site:arxiv.org/abs persistent test-time learning LLM memory continual adaptation` | NON DISPONIBLE | Adaptation persistante et apprentissage permanent. |
| Q25 | 2026-07-14 | `site:arxiv.org/abs Transformer-XL attentive language models beyond fixed-length context recurrence` | NON DISPONIBLE | Branche récurrente historique ; non retenue comme collision la plus forte. |
| Q26 | 2026-07-14 | `site:arxiv.org/abs Recurrent Memory Transformer 2304.11062 long sequences` | NON DISPONIBLE | L'identifiant saisi était erroné ; le titre a conduit au bon primaire arXiv:2207.06881v2. Correction conservée dans le journal. |
| Q27 | 2026-07-14 | `site:arxiv.org/abs Infini-attention infinite context compressive memory 2404.07143` | NON DISPONIBLE | Infini-attention. |
| Q28 | 2026-07-14 | `site:arxiv.org/abs Compressive Transformer compressive memories 1911.05507` | NON DISPONIBLE | Antécédent compressif ; Infini-attention retenu dans le tableau principal. |
| Q29 | 2026-07-14 | `site:arxiv.org/abs/2512.13564 "Memory in the Age of AI Agents"` | NON DISPONIBLE | Survey multi-auteurs et fronts de recherche. |
| Q30 | 2026-07-14 | `site:arxiv.org/abs/2603.07670 "Memory for Autonomous LLM Agents"` | NON DISPONIBLE | Patterns A/B/C et recommandation de transition. |
| Q31 | 2026-07-14 | `"Lifelong learning of large language model based agents: a roadmap" primary paper` | NON DISPONIBLE | Roadmap TPAMI. |
| Q32 | 2026-07-14 | `"Memory in the LLM Era" "Modular Architectures" PVLDB` | NON DISPONIBLE | Cadre unifié et précédent d'assemblage. |
| Q33 | 2026-07-14 | `site:arxiv.org/abs ("memory contract" OR "state contract") LLM agent workload budget` | NON DISPONIBLE | ClawVM et AgenticSTS. |
| Q34 | 2026-07-14 | `site:arxiv.org/abs LLM agent memory "feasibility constraint" workload` | NON DISPONIBLE | Contrainte dure d'Agent Memory. |
| Q35 | 2026-07-14 | `site:arxiv.org/abs LLM memory "context-only" Pareto workload` | NON DISPONIBLE | Régimes context-only et frontières coût-performance. |
| Q36 | 2026-07-14 | `site:openreview.net agent memory abstain transition rule context-only` | NON DISPONIBLE | Aucun `T` abstentionnel complet retenu ; résultat non interprété comme nouveauté. |
| Q37 | 2026-07-14 | `"ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents" cites` | NON DISPONIBLE | Forward exact-title ; publication officielle retrouvée, aucun graphe de citations stable exploitable. |
| Q38 | 2026-07-14 | `"Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads" citations` | NON DISPONIBLE | Forward exact-title ; aucune nouvelle famille primaire admissible. |
| Q39 | 2026-07-14 | `"when should" external memory LLM agent long context` | NON DISPONIBLE | Découverte de When Should Memory Stay Silent. |
| Q40 | 2026-07-14 | `site:arxiv.org/abs "context-only" "persistent memory" agent` | NON DISPONIBLE | Découverte de PersistBench et vérification des contre-régimes. |

### 5.3 Snowballing et saturation bornée

- Le backward snowball de ClawVM a retrouvé AIOS, MemOS, MemGPT, CoALA, Text2Mem et MemoryOS. Les trois premières familles suffisent pour les collisions OS les plus fortes ; les autres ne changent pas le verdict.
- Le backward snowball d'Agent Memory a retrouvé Letta, Mem0, A-Mem et MIRIX. Ils ajoutent des implémentations, pas une règle implementation-neutral plus forte que S1, S2 et S7.
- Les surveys et positions ont ramené RMT, Titans, long-context et les taxonomies de cycle de vie.
- Le forward search par titre exact n'a pas fourni de cardinalité de citations stable. Une page ResearchGate affichant zéro citation pour ClawVM n'a pas été utilisée comme preuve primaire.
- Après Q39-Q40, une itération supplémentaire n'a pas révélé de nouvelle famille de mécanismes. Il s'agit d'une saturation pratique de cet axe, jamais d'une preuve d'absence.

## 6. Évidence, locators et analyse d'overlap

### 6.1 Définition des verdicts d'objet

- `ANTICIPATED` : la substance observable est divulguée par une source forte ou par le plus fort composite admissible.
- `PARTIAL` : des éléments essentiels sont divulgués, mais la construction complète n'est ni unifiée ni opérationnalisée.
- `DISTINCT_CANDIDATE` : un résidu mesurable, falsifiable et non réductible est suffisamment spécifié pour mériter un gate expérimental.
- `UNSUPPORTED` : l'objet est énoncé sans spécification ou preuve suffisante ; cela ne signifie pas qu'il est nouveau.

### 6.2 Verdict par objet

| Objet | Verdict | Preuves positives les plus fortes | Pourquoi le résidu ne franchit pas le gate |
|---|---|---|---|
| `Ω`, descripteur ex ante du workload | **ANTICIPATED** | S1 encode longueur/croissance de l'historique, dépendances inter-session, arrivées de requêtes, famille de tâches, fraîcheur et phases ; S7 ajoute mises à jour, horizon et bottleneck ; S8 ajoute criticité et seuils applicatifs. | La liste proposée dans l'issue complète et renomme des axes connus. Aucun nouvel invariant du workload ni statistique suffisante n'est défini. |
| `G`, contrat de garanties comportementales | **ANTICIPATED** par strongest composite | S2 fournit portée, provenance, fidélité minimale, dégradation, writeback et raisons de faute ; S3 formalise autorisation, lineage, retrieval scoped, rollback et oubli ; S4 et S10 ajoutent version, transactions et interface. | Pris séparément, chaque contrat est partiel ou lié à un harness. Pris ensemble, le comportement observable proposé est déjà reconstructible. La neutralité d'implémentation est un cadrage, pas encore un nouvel objet formel. |
| `B`, enveloppe vectorielle de ressources | **ANTICIPATED** | S1 mesure tokens, appels, latence/tails, énergie, puissance, VRAM/HBM, stockage et croissance, puis construit une frontière Pareto et une contrainte dure ; S2 borne les tokens ; S5 schedule les ressources ; S17 explicite les coûts I/O. | Ajouter des coordonnées à une enveloppe connue est une complétion comptable. Aucune géométrie, loi de composition ou métrique de conversion nouvelle n'est fournie. |
| `T(Ω,G,B)`, transition context-only/persistance/adaptatif/abstention | **PARTIAL** | S1 choisit selon workload et impose une frontière de faisabilité ; S8 recommande A/B/C ; S7 montre qu'aucune architecture ne domine ; S11-S12 donnent des régimes où la mémoire doit se taire ou être oubliée ; S2 expose l'infaisabilité quand l'état minimal dépasse le budget. | Aucune source lue ne réunit tout dans un classifieur pré-outcome calibré. Mais l'issue ne définit pas non plus features mesurables, cible, seuils, perte, calibration, protocole cross-implementation ou règle d'abstention. Le résidu est donc partiel, pas `DISTINCT_CANDIDATE`. |

### 6.3 Frontières et régimes négatifs déjà divulgués

| Régime | Divulgation primaire | Conséquence pour une thèse directionnelle |
|---|---|---|
| Historique court, requête simple, prototype | S8, §7.6 ; S7, §§5.3-5.4 | Context-only ou une mémoire plus simple peut être préférable. Une thèse « toujours persister » est falsifiée par l'antériorité elle-même. |
| Historique stable et nombreuses requêtes | S1, §4.5 | Une construction plus coûteuse peut être amortie. `Ω` et `B` conditionnent déjà la sélection. |
| Ingestion continue et requêtes rares | S1, §4.5 | Favorise une faible construction/maintenance. La persistance riche n'est pas automatiquement Pareto-préférable. |
| Inter-session trop court pour construire et récupérer | S1, §4.6 | Fraîcheur et latence ne peuvent être satisfaites simultanément : frontière de faisabilité, pas simple ranking. |
| Ensemble d'état minimal supérieur au budget | S2, §5.3 | Toutes les politiques fautent ; le harness doit exposer l'infaisabilité. Préfigure l'abstention/failure contract. |
| Mémoire sensible non warrantée par la requête courante | S11, §§1-4 | La mémoire doit rester silencieuse même si elle est stockée et pertinente au sens sémantique. |
| Préférence ancienne, domaine changé ou trace obsolète | S12, §§3-7 | Retrieval/persistance peut induire leakage ou sycophancy ; il faut oublier ou ne pas utiliser. |
| Réflexion/maintenance ajoutée sans bénéfice | S7, §5.3 ; S1, §§4.2-4.3 | La complexité mémoire peut dégrader qualité et coût. Le premium doit être justifié par une capacité nécessaire. |
| État interne récurrent, compressif ou paramétrique | S17-S21 | « Persistance gérée » ne désigne pas une unique topologie. Toute règle neutre doit comparer des mécanismes non isomorphes. |

### 6.4 Test d'effacement des composants

**Procédure.** Les noms `Ω`, `G`, `B`, `T`, les diagrammes et les marques d'architecture sont supprimés. On conserve seulement les entrées, sorties, invariants et décisions observables.

**Résidu obtenu.** Décrire l'horizon, les mutations, la fréquence de réutilisation et les arrivées ; déclarer provenance, version, rétention, oubli et fidélité minimale ; comptabiliser construction, service, latence, mémoire, énergie et stockage ; choisir une mémoire simple ou riche ; rester context-only quand l'horizon et le risque sont faibles ; signaler l'échec si l'état minimal ne tient pas dans le budget.

**Verdict : FAIL.** Ce résidu est déjà exprimé par S1 + S2 + S3 + S7 + S8 + S11 + S12. L'article large ne conserverait pas un mécanisme, invariant ou résultat théorique distinct après effacement.

### 6.5 Test de substitution des labels

| Label proposé | Substitution présente dans l'art antérieur | Changement de sens observable ? |
|---|---|---|
| `Ω` | workload characterization, query-arrival pattern, task family, history/update regime | Non. |
| `G` | output contract, minimum-fidelity invariant, VMG predicates, lifecycle/interface contract | Non. |
| `B` | Construction-Serve-Accuracy frontier, lifecycle energy, latency/storage/token budget | Non. |
| `T` | system recommendation, admission/routing policy, architecture pattern, feasibility constraint | Seulement partiellement : l'unification calibrée et abstentionnelle manque des deux côtés. |

**Verdict : FAIL pour la thèse large.** Le remplacement des symboles par le vocabulaire des sources ne modifie pas les décisions observables. La notation apporte une vue compacte, mais pas encore une contribution technique.

### 6.6 Test du strongest composite

Le composite adversarial le plus fort est :

1. **S1 Agent Memory** pour `Ω`, `B`, les frontières Pareto, l'amortissement et l'infaisabilité fraîcheur-latence.
2. **S2 ClawVM** pour le contrat d'état minimal, `G x B`, la dégradation admissible et la faute diagnostiquée.
3. **S3 VMG + S10 Compatibility-First** pour gouvernance, provenance, version, rollback, oubli et surface d'interface.
4. **S7 Agent-Native + S11 When Memory Stay Silent + S12 PersistBench** pour non-dominance et régimes négatifs.
5. **S8 + S9 + S4** pour la narration de transition, les patterns de maturité et la direction stateless vers état géré.
6. **S5 + S6** pour les implémentations agent-OS et virtual-context.
7. **S17-S21** pour les réalisations internes récurrentes, compressives, paramétriques et test-time.

Ce composite reconstruit la thèse directionnelle et la plupart de ses contre-régimes. Ce qui manque est une règle unifiée, pré-outcome, calibrée et validée sur plusieurs familles. Or ce manque est aussi celui de la proposition actuelle : aucun estimateur, protocole ou ensemble de prédictions discriminantes n'est spécifié.

**Verdict : FAIL.** La formulation actuelle ne résiste pas au strongest-composite test.

### 6.7 Résidu possible, mais non autorisé comme contribution

Un objet plus étroit pourrait être nommé `T*` : classifieur abstentionnel qui, à partir de variables ex ante observables et non de scores post-hoc, prédit la solution Pareto-admissible parmi context-only, store gouverné, état récurrent/paramétrique et calcul adaptatif, tout en signalant les contrats infaisables.

`T*` est **UNSUPPORTED**, et non `DISTINCT_CANDIDATE`, pour quatre raisons :

1. les features de `Ω`, l'encodage de `G` et la normalisation de `B` ne sont pas définis opérationnellement ;
2. la cible, la fonction de perte, la calibration et le coût de l'abstention ne sont pas spécifiés ;
3. aucun protocole cross-implementation ne sépare topology effects, model effects et workload effects ;
4. aucune série d'au moins quatre prédictions quantitatives discriminant `T*` du composite S1-S12 n'est préenregistrée.

L'absence d'un papier trouvé portant exactement `T*` n'est pas une preuve de nouveauté. Avant toute réouverture, `T*` doit être dérivé contre la théorie générique de décision, de scheduling et de contrôle traitée par les autres audits M1b.

### 6.8 Collision anti-réécriture la plus directe

S14 est un précédent particulièrement défavorable à une contribution de type « nouveau cadre unifié ». Il organise des architectures existantes, les compare puis assemble explicitement des modules d'autres systèmes dans un nouveau pipeline. Un article qui juxtaposerait MemOS pour la direction, Agent Memory pour `Ω/B`, ClawVM/VMG pour `G`, les positions pour les recommandations et TTT pour les mécanismes resterait dans cette classe de synthèse, même avec la notation `Ω/G/B/T`.

## 7. Incertitudes et contradictions

1. La recherche est ciblée et snowballée, pas systématique exhaustive. Les totaux de résultats et de citations sont `NON DISPONIBLE` ; aucune conclusion ne repose sur une absence brute.
2. Le corpus 2026 évolue rapidement. S1, S2, S7, S11-S13 sont très récents et leurs graphes de citations sont immatures.
3. S10 est une soumission de position, pas une acceptation vérifiée. S8 est un survey mono-auteur. Ils sont utilisés comme collisions de cadrage, jamais seuls comme preuve décisive.
4. S2 est lié à un harness et à des fautes structurelles, pas à la correction sémantique générale. Son indépendance au modèle/retriever ne suffit pas à rendre tout `G` topology-neutral.
5. S3 formalise surtout la sécurité et la gouvernance. Il ne donne pas à lui seul un contrat complet de qualité, latence et récupération.
6. S13 n'est utilisé que pour ce que son résumé officiel établit ; son résultat no-store/skill-memory est étroit et non significatif.
7. Les locators HTML arXiv peuvent changer lorsque le rendu est régénéré. Les versions, sections, tableaux et pages sont donc épinglés plutôt que des numéros de lignes de navigateur.
8. Les sources se contredisent utilement : la persistance aide les dépendances longues et mutables, mais Long Context gagne parfois sur la formulation exacte ; la réflexion peut nuire ; une mémoire pertinente peut être non warrantée ; certaines garanties sont impossibles sous budget. Ces contradictions rendent une loi universelle invraisemblable sans calibration.
9. La branche calcul adaptatif/metareasoning n'est pas auditée exhaustivement ici. Le verdict global M1b doit intégrer son handoff et l'audit de théorie générique.
10. Une implémentation-neutralité déclarée ne supprime pas les différences entre store externe, état récurrent, mémoire compressive et poids adaptés. Une validation multi-topologies serait obligatoire.

## 8. Fichiers modifiés

- Créé : `docs/research/handoffs/2026-07-14-m1b-terra-stateful-systems.md`.
- Aucun autre fichier n'a été modifié par cet audit.
- La modification partagée de `docs/research/M1B_SEARCH_LOG.csv`, le répertoire non suivi `carte-btp-mobile/` et l'état de branche ont été observés mais non touchés.

## 9. Vérification

- Lecture des sources primaires et contrôle des versions/locators : effectué.
- Contrôle des douze sections requises par `docs/research/handoffs/README.md` : effectué.
- Contrôle des espaces de fin de ligne : 0 occurrence.
- Contrôle du statut Git : seul ce handoff est imputable à cet audit ; la modification de `docs/research/M1B_SEARCH_LOG.csv` et `carte-btp-mobile/` sont des changements partagés non touchés.
- Tests logiciels : non applicables, modification documentaire bornée.
- SHA-256 : calculé après la dernière modification et transmis avec le handoff, sans auto-référence dans le fichier.

## 10. Décision recommandée

### STOP pour l'axe stateful-systems tel que formulé

La thèse large n'est pas une base scientifiquement défendable pour un article original destiné à orienter les futurs LLMs. `Ω`, `G` et `B` sont **ANTICIPATED** au niveau du strongest composite. `T` est **PARTIAL**, mais le résidu non anticipé n'est pas lui-même spécifié. La contribution actuelle serait principalement une synthèse et une normalisation de vocabulaire.

Ce STOP est borné à l'axe `Ω/G/B -> état persistant géré`. Il ne préjuge pas du verdict global de l'issue #5 sur un éventuel résultat issu d'un autre axe, notamment calcul adaptatif ou théorie générique. Il interdit cependant d'utiliser cet axe comme simple réécriture directionnelle de MemOS, Agent Memory, ClawVM, VMG et des positions existantes.

## 11. Prochaine action autorisée recommandée

Le responsable de l'issue #5 doit intégrer ce handoff au composite M1b et demander la revue indépendante Luna. Ne pas commencer de manuscrit.

Un PIVOT ne devrait être rouvert que si un document séparé préenregistre :

1. une définition mesurable de chaque feature ex ante ;
2. une fonction de décision et d'abstention indépendante de la topologie ;
3. au moins quatre prédictions quantitatives qui divergent du composite S1-S12 ;
4. un protocole cross-implementation incluant au minimum context-only, store gouverné et état interne récurrent/paramétrique ;
5. des régimes négatifs et une comparaison à la théorie générique, pas seulement aux architectures mémoire.

Sans ces cinq éléments, l'action correcte reste STOP.

## 12. Rôles d'auteur et de revue indépendante

- Rôle d'auteur : **Terra-Evidence**, collecte primaire, épinglage des versions, locators, overlap et tests adversariaux.
- Rôle de revue indépendante requis : **Luna-Librarian/Cross-Review**, vérification des sources, des statuts, des locators et tentative active de trouver une collision plus forte ou un résidu réellement distinct.
- Rôle de décision : mainteneur de l'issue #5, après intégration avec les autres axes M1b. L'auteur de ce handoff ne doit pas être l'unique décideur du gate.
