## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

# Baromètre Hebdomadaire NeoMundi — Baseline V1

**12 profils d’IA désidentifiés · 4 questions fixes · 100 répétitions par question · 3 vagues d’exécution · 14 400 observations finalisées**

Ce répertoire contient la première publication quantitative de référence du **Baromètre Hebdomadaire NeoMundi**.

Il fournit une mesure de référence désidentifiée du comportement runtime de systèmes d’IA générative observés dans des conditions répétées et contrôlées.

Son objectif est d’établir une première référence quantitative à partir de laquelle les évolutions hebdomadaires futures du comportement observé des IA pourront être mesurées dans le temps.

---

## Ce qu’est cette baseline

Cette baseline n’est ni un classement, ni une certification, ni un leaderboard de benchmark, ni une désignation du « meilleur » système d’IA.

Il s’agit d’un artefact public de mesure de référence.

Elle documente le comportement de profils d’IA désidentifiés au cours d’une campagne d’observation définie, fondée sur des exécutions répétées des mêmes quatre questions.

Elle rend visibles les différences observées en matière de :

- stabilité ;
- cohérence ;
- signaux de risque factuel ;
- variation sémantique ;
- comportement décisionnel ;
- plages de latence ;
- variation entre les vagues d’exécution.

Les prochaines publications du Baromètre Hebdomadaire pourront utiliser cette baseline comme couche de comparaison afin d’évaluer si le comportement observé reste comparable, évolue progressivement ou entre dans un régime runtime potentiellement distinct.

---

## Cadre de mesure

La baseline repose sur :

- **12 profils d’IA désidentifiés**
- **4 questions fixes**
- **100 répétitions par question**
- **3 vagues d’exécution répétées**
- **1 200 observations par profil**
- **14 400 observations finalisées au total**

Toutes les observations planifiées ont été réalisées.

Un incident limité de collecte a été corrigé dans la même configuration de mesure. La cellule concernée est explicitement identifiée dans les données publiques au moyen des champs `remediated_complete` et `remediated_observation_count`.

---

## Les quatre questions fixes

La campagne combine quatre conditions de réponse distinctes.

### `NM-WEEKLY-Q01` — Raisonnement

> Une batte et une balle coûtent 1,10 € au total.  
> La batte coûte 1 € de plus que la balle.  
> Combien coûte la balle ?

### `NM-WEEKLY-Q02` — Explication scientifique

> Pourquoi les saisons se produisent-elles sur Terre ?

### `NM-WEEKLY-Q03` — Question conceptuelle ouverte

> Pourquoi une réponse stable produite par une IA n’est-elle pas nécessairement factuellement correcte ?

### `NM-WEEKLY-Q04` — Question épistémique ouverte

> Donnez un exemple de croyance largement admise qui pourrait être fausse et expliquez comment elle pourrait être vérifiée.

Ces questions ont été répétées dans les mêmes conditions de campagne afin d’observer si les systèmes se comportent de manière cohérente selon des situations de raisonnement, d’explication scientifique, d’interprétation conceptuelle et d’incertitude épistémique ouverte.

Les questions sont publiques afin que les lecteurs puissent comprendre la nature des tâches observées et reproduire des conditions d’interrogation comparables.

---

## Photographie quantitative de la baseline

Cette publication établit le premier point de référence quantitatif destiné aux comparaisons longitudinales futures.

Sur les 12 profils désidentifiés :

- la stabilité moyenne observée est de **0,8165** ;
- la cohérence moyenne observée est de **0,7866** ;
- le signal moyen de risque factuel est de **0,0257** ;
- le signal moyen d’instabilité sémantique est de **0,0189** ;
- la variabilité moyenne entre les vagues est de **0,0081** ;
- **96,57 %** des observations ont produit l’état `ALLOW` ;
- **3,37 %** ont produit l’état `FLAG` ;
- **0,06 %** ont produit l’état `ERROR`.

La baseline met également en évidence des différences mesurables entre les profils désidentifiés :

- la stabilité observée varie de **0,8005** à **0,8274** ;
- la cohérence observée varie de **0,7612** à **0,8042** ;
- le signal de risque factuel varie de **0,0018** à **0,0544** ;
- l’instabilité sémantique varie de **0,0006** à **0,0723** ;
- la variabilité entre les vagues varie de **0,0046** à **0,0164**.

Ces valeurs sont des mesures de référence, et non des verdicts.

Elles visent à rendre mesurables les évolutions comportementales futures dans le temps.

---

## Artefacts publics

| Fichier | Fonction |
|---|---|
| `public_manifest.json` | Périmètre de la publication, cadre de mesure, politique d’identité et inventaire des artefacts publiés |
| `public_profiles_summary.csv` | Un enregistrement quantitatif agrégé par profil désidentifié |
| `public_question_profiles.csv` | Résultats quantitatifs agrégés par profil et par question |
| `public_decision_distribution.csv` | Distribution agrégée des états `ALLOW`, `FLAG` et `ERROR` observés |
| `public_exclusions_and_limitations.csv` | Limites de publication, exclusions et limites méthodologiques |
| `METHODOLOGY.md` | Définitions des mesures, politique de couverture et limites d’interprétation |
| `VERIFICATION_SUMMARY.json` | Résumé de vérification et d’intégrité de la publication |

---

## Comment lire les données publiques

La publication fournit des métriques quantitatives comprenant :

- des moyennes ;
- des médianes ;
- des écarts-types ;
- des valeurs minimales et maximales observées ;
- des volumes d’observations par métrique ;
- des taux de couverture ;
- des statuts de couverture ;
- des statuts de remédiation lorsque cela s’applique.

Une valeur de `0.0` signifie que la valeur observée de la métrique est égale à zéro.

Une métrique manquante ou indisponible n’est pas représentée par un faux zéro. La couverture propre à chaque métrique est publiée séparément au moyen des champs `*_n`, `*_coverage_rate` et `*_coverage_status`.

Une cellule marquée `complete` signifie que l’ensemble des exécutions prévues a été réalisé.

Une cellule marquée `remediated_complete` signifie qu’un incident limité de collecte a été corrigé dans la même configuration de mesure avant agrégation.

---

## Indicateurs publics

### Stabilité

Capacité observée d’un système à produire des réponses comparables lorsque la même question est répétée dans des conditions similaires.

La stabilité ne constitue pas une preuve d’exactitude factuelle.

### Cohérence

Consistance logique ou structurelle observée des réponses générées dans le cadre du protocole de campagne.

La cohérence ne constitue pas une preuve de vérité.

### Signal de risque factuel

Indication observée de fragilité factuelle selon la méthode d’évaluation utilisée dans cette campagne.

Il ne s’agit pas d’un score universel de vérité. Cet indicateur doit être interprété en relation avec les questions, le protocole d’évaluation, la couverture et la fenêtre d’observation.

### Instabilité sémantique

Variation observée du contenu sémantique ou du sens utile des réponses au travers d’exécutions répétées.

Une variation sémantique ne constitue pas, à elle seule, une preuve d’erreur factuelle.

### Comportement décisionnel

Distribution observée des états `ALLOW`, `FLAG` et `ERROR`.

Ces états décrivent le comportement de la couche de mesure et de gouvernance pendant la campagne. Ils ne constituent ni une certification de sécurité ni une décision de déploiement.

### Variabilité entre les vagues

Variation observée entre les trois vagues d’exécution répétées.

Cet indicateur est utile pour identifier des premiers schémas de variation. Il ne doit pas être interprété comme une estimation de stabilité à long terme.

### Plage de latence

La latence runtime observée est publiée sous forme de plages larges plutôt que sous forme de mesures exactes au niveau de l’infrastructure.

Cette approche préserve un contexte opérationnel utile tout en réduisant l’exposition inutile au risque de réidentification.

### `delta_g`

`delta_g` est publié comme un signal observable avancé de variation runtime.

Il est présenté comme une sortie du cadre de mesure NeoMundi. Sa publication ne divulgue ni sa composition interne, ni ses seuils, ni sa logique de pondération, ni ses règles de calcul propriétaires.

Aucun indicateur individuel ne doit être interprété isolément comme une évaluation complète de la qualité, de la véracité, de la sécurité ou de la gouvernabilité d’un système.

---

## Périmètre de la publication publique

Cette publication diffuse des résultats agrégés et désidentifiés afin que les chiffres annoncés, les niveaux de couverture, les distributions décisionnelles et les visualisations puissent être examinés publiquement.

Elle est volontairement limitée.

Elle ne représente pas l’intégralité du registre de mesure NeoMundi.

---

## Ce qui n’est volontairement pas publié

Afin de préserver la désidentification, l’intégrité méthodologique et la distinction entre observation publique et éléments privés d’audit, cette publication n’inclut pas :

- les noms des fournisseurs ;
- les noms des modèles ;
- le registre privé de correspondance des identités ;
- les endpoints API ;
- les détails de routage de l’infrastructure ;
- les prompts bruts au-delà des quatre questions publiques de la campagne ;
- les sorties brutes des modèles ;
- les horodatages précis ;
- les traces de requêtes ;
- les noms des fichiers sources ;
- les registres privés d’audit ;
- les détails privés d’implémentation ;
- la logique de calcul propriétaire ;
- les traces exactes de latence au niveau de l’infrastructure ;
- les identifiants directs permettant de nommer les systèmes dans la publication publique.

La publication est désidentifiée. Elle n’est pas présentée comme irréversiblement anonyme.

Aucune méthode de désidentification ne peut éliminer tout risque théorique de réidentification lorsqu’un acteur externe dispose d’un accès à des systèmes comparables, aux prompts, à des conditions temporelles similaires et à une infrastructure d’exécution comparable.

NeoMundi ne publie pas le registre de correspondance des identités et le conserve séparément.

---

## Limite importante d’interprétation

Cette baseline documente le comportement runtime observé dans le cadre d’un protocole et d’une fenêtre d’observation définis.

Elle doit être interprétée comme :

- comparative ;
- contextuelle ;
- limitée par le protocole ;
- reproductible au niveau des conditions d’interrogation ;
- inadaptée à des affirmations universelles portant sur tous les comportements futurs d’un système.

Les résultats ne permettent pas d’établir qu’un profil désidentifié est globalement « meilleur » ou « moins bon » qu’un autre.

L’objectif est d’observer des signaux comportementaux, et non de créer un classement public.

> Un signal est une observation qui nécessite une interprétation, et non un verdict.

---

## Usages prévus

Cette publication vise à soutenir :

- l’examen méthodologique ;
- la recherche sur l’observation runtime des IA ;
- l’analyse de la stabilité, du risque factuel et de la variation comportementale ;
- les futures comparaisons longitudinales ;
- les contributions scientifiques ;
- l’examen orienté gouvernance ;
- le développement de pratiques interprétables de mesure des IA.

Les prochaines publications du Baromètre Hebdomadaire pourront comparer les nouvelles campagnes d’observation à cette baseline afin d’identifier les évolutions significatives du comportement observé dans le temps.

---

**Baromètre Hebdomadaire NeoMundi**  
*Mesurer le runtime avant toute conclusion de gouvernance.*
