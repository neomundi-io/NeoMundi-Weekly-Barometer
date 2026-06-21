## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

**12 systèmes IA anonymisés · 4 questions fixes · 100 répétitions par question · 3 vagues d’exécution · 14 400 observations finalisées**

Ce dossier contient la première release publique quantitative de la baseline du NeoMundi Weekly Barometer.

Il fournit une cartographie de référence anonymisée des comportements runtime observés sur un panel de systèmes d’IA générative, dans des conditions de mesure répétées.

L’objectif de cette baseline est simple : établir le point de référence initial à partir duquel les évolutions futures du comportement observé des IA pourront être mesurées.

---

## Ce qu’est cette baseline

Cette baseline n’est ni un classement, ni une certification, ni un leaderboard de benchmark, ni une déclaration sur une IA « meilleure » qu’une autre.

C’est un artefact de mesure de référence.

Elle documente la manière dont des systèmes anonymisés se sont comportés pendant une campagne d’observation définie, à travers des exécutions répétées des mêmes quatre questions. Elle rend visibles des différences de stabilité, de signaux de validité factuelle, de cohérence, de variation sémantique, de comportement de décision, de bandes de latence et de variation entre vagues d’exécution.

Les futurs Weekly Barometers utiliseront cette release comme couche de comparaison afin d’identifier si le comportement observé reste comparable, évolue progressivement ou entre dans un régime runtime distinct.

---

## Cadre de mesure

La baseline est dérivée de :

* **12 profils de systèmes anonymisés**
* **4 questions fixes**
* **100 répétitions par question**
* **3 vagues d’exécution répétées**
* **1 200 observations par profil anonymisé**
* **14 400 observations finalisées au total**

Toutes les observations prévues ont été réalisées.

Un incident limité de collecte a été remédié dans la même configuration de mesure. La cellule concernée est explicitement identifiée dans les données publiques par les champs `remediated_complete` et `remediated_observation_count`.

---

## Les quatre questions fixes

La campagne associe quatre conditions de réponse différentes.

### NM-WEEKLY-Q01 — Raisonnement

Une batte et une balle coûtent 1,10 € au total. La batte coûte 1 € de plus que la balle. Combien coûte la balle ?

### NM-WEEKLY-Q02 — Explication scientifique

Pourquoi les saisons existent-elles sur Terre ?

### NM-WEEKLY-Q03 — Question conceptuelle ouverte

Pourquoi une réponse IA stable n’est-elle pas nécessairement factuellement correcte ?

### NM-WEEKLY-Q04 — Question épistémique ouverte

Donnez un exemple de croyance largement admise qui pourrait être fausse. Expliquez comment elle pourrait être vérifiée.

Ces questions ont été répétées dans les mêmes conditions de campagne afin d’observer si les systèmes se comportent de manière comparable face au raisonnement, à l’explication scientifique, à l’interprétation conceptuelle et à l’incertitude épistémique ouverte.

Les questions sont publiques afin que chacun puisse comprendre la nature des tâches observées et reproduire des conditions d’interrogation comparables.

---

## Photographie initiale de la baseline

Cette release établit le premier point de référence quantitatif pour les futures comparaisons longitudinales.

Sur les 12 profils anonymisés :

* la stabilité moyenne observée est de **0,8165** ;
* la cohérence moyenne observée est de **0,7866** ;
* le signal moyen d’hallucination factuelle est de **0,0257** ;
* le signal moyen d’instabilité sémantique est de **0,0189** ;
* la variabilité inter-run moyenne est de **0,0081** ;
* **96,57 %** des observations aboutissent à une décision `ALLOW` ;
* **3,37 %** aboutissent à une décision `FLAG` ;
* **0,06 %** aboutissent à une décision `ERROR`.

La baseline montre également des écarts significatifs entre les profils anonymisés :

* la stabilité observée varie de **0,8005** à **0,8274** ;
* la cohérence observée varie de **0,7612** à **0,8042** ;
* le signal d’hallucination factuelle varie de **0,0018** à **0,0544** ;
* l’instabilité sémantique varie de **0,0006** à **0,0723** ;
* la variabilité inter-run varie de **0,0046** à **0,0164**.

Ces valeurs constituent des mesures de référence, pas des verdicts.

Elles ont pour fonction de rendre mesurables les évolutions futures de comportement dans le temps.

---

## Artefacts publics

| Fichier                                 | Rôle                                                                                          |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `public_manifest.json`                  | Périmètre de la release, cadre de mesure, politique d’identité et liste des artefacts publiés |
| `public_profiles_summary.csv`           | Un profil comportemental quantitatif anonymisé par système observé                            |
| `public_question_profiles.csv`          | Comportement de chaque profil selon les quatre questions fixes                                |
| `public_decision_distribution.csv`      | Distribution agrégée des décisions observées : `ALLOW`, `FLAG` et `ERROR`                     |
| `public_exclusions_and_limitations.csv` | Limites de publication, exclusions et limites méthodologiques                                 |
| `METHODOLOGY.md`                        | Définitions de mesure, politique de couverture et limites d’interprétation                    |
| `VERIFICATION_SUMMARY.json`             | Synthèse de vérification et d’intégrité de la release                                         |

---

## Comment lire les données publiques

La release publique fournit des métriques quantitatives avec :

* moyennes ;
* médianes ;
* écarts-types ;
* valeurs minimales et maximales observées ;
* nombre d’observations par métrique ;
* taux de couverture ;
* statut de couverture ;
* statut de remédiation lorsque cela s’applique.

Une valeur `0.0` signifie que la valeur observée pour cette métrique est nulle.

Une métrique absente ou indisponible n’est pas représentée par un faux zéro. La couverture par métrique est publiée séparément au moyen des champs `*_n`, `*_coverage_rate` et `*_coverage_status`.

Une cellule marquée `complete` signifie que l’ensemble d’exécutions prévu a été réalisé.

Une cellule marquée `remediated_complete` signifie qu’un incident limité de collecte a été corrigé dans la même configuration de mesure avant agrégation.

---

## Indicateurs publics

La baseline comprend les indicateurs publics suivants.

### Stabilité

Capacité observée d’un système à produire des réponses comparables lorsqu’une même question est répétée.

### Cohérence

Cohérence interne observée des réponses générées selon le protocole de la campagne.

### Signal d’hallucination factuelle

Signal observé de fragilité factuelle selon la méthode d’évaluation utilisée dans cette campagne.

Il ne s’agit pas d’un score universel de vérité et il doit toujours être interprété en fonction du jeu de questions, du protocole d’évaluation et de la fenêtre d’observation.

### Instabilité sémantique

Variation observée dans le contenu sémantique ou dans le sens utile des réponses à travers des exécutions répétées.

### Comportement de décision

Distribution observée des décisions `ALLOW`, `FLAG` et `ERROR`.

Ces décisions décrivent le comportement de la couche de mesure et de gouvernance pendant la campagne. Elles ne constituent pas une certification de sécurité.

### Variabilité inter-run

Variation observée entre les trois vagues d’exécution répétées.

Cet indicateur est utile pour détecter des motifs de variation précoces. Il ne doit pas être interprété comme une estimation de stabilité à long horizon.

### Bande de latence

La latence runtime observée est publiée sous forme de bandes larges, plutôt que sous la forme de timings exacts au niveau infrastructure.

Cela préserve un contexte opérationnel utile tout en réduisant une exposition inutile à la réidentification.

### `delta_g`

`delta_g` est publié comme signal avancé de variation runtime.

Il est présenté comme une sortie observable du cadre de mesure. Il ne révèle ni la composition interne, ni les seuils, ni la logique de pondération, ni les règles de calcul propriétaires du cadre NeoMundi.

---

## Ce qui n’est volontairement pas publié

Afin de préserver l’anonymisation, l’intégrité méthodologique et la distinction entre observation publique et corpus d’audit privé, cette release ne contient pas :

* les noms des fournisseurs ;
* les noms des modèles ;
* le mapping privé des identités ;
* les endpoints API ;
* les détails de routage infrastructurel ;
* les prompts bruts autres que les quatre questions de campagne publiées ;
* les sorties brutes des modèles ;
* les timestamps exacts ;
* les traces de requêtes ;
* les noms de fichiers source ;
* les enregistrements privés d’audit ;
* les détails privés d’implémentation ;
* la logique de calcul propriétaire ;
* les traces précises de latence au niveau infrastructure ;
* les identifiants directs permettant de nommer publiquement les systèmes observés.

La publication est anonymisée, mais aucune méthode de désidentification ne peut supprimer tout risque théorique de réidentification lorsqu’un acteur externe dispose de systèmes comparables, des mêmes questions, de conditions de timing similaires et d’une infrastructure d’exécution comparable.

NeoMundi ne publie pas le mapping des identités et le conserve confidentiel.

---

## Note importante d’interprétation

Cette baseline documente un comportement runtime observé selon un protocole et une fenêtre temporelle définis.

Elle doit être interprétée comme :

* comparative ;
* contextuelle ;
* exploratoire ;
* reproductible au niveau des conditions d’interrogation ;
* impropre à soutenir des affirmations universelles sur le comportement futur de tous les systèmes.

Les résultats ne démontrent pas qu’un profil anonymisé est globalement « meilleur » ou « moins bon » qu’un autre.

L’objectif est d’observer les comportements, non de construire un classement public.

---

## Usages prévus

Cette release est destinée à soutenir :

* la revue méthodologique ;
* la recherche sur l’observabilité runtime des IA ;
* la discussion sur la stabilité, la validité factuelle et les variations comportementales ;
* les comparaisons longitudinales futures ;
* les contributions scientifiques ;
* la revue orientée gouvernance ;
* le développement de pratiques de mesure IA interprétables.

Les futurs Weekly Barometers compareront de nouvelles campagnes d’observation à cette baseline afin d’identifier des changements significatifs dans les comportements observés au fil du temps.

---

**NeoMundi Weekly Barometer**
*Observer le runtime avant de prétendre gouverner.*
