## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**

# Baromètre Hebdomadaire NeoMundi — Baseline Publique V1

Ce répertoire contient la première publication quantitative de référence du **Baromètre Hebdomadaire NeoMundi**.

La Baseline V1 est une **campagne de référence désidentifiée** : une photographie métrologique fixe du comportement runtime de 12 profils d’IA générative, observés dans des conditions répétées et contrôlées.

Il ne s’agit ni d’un rapport éditorial hebdomadaire, ni d’un classement, ni d’une certification, ni d’un palmarès de modèles, ni d’une évaluation générale de la qualité des systèmes d’IA.

Son objectif est plus précis et plus durable : établir une référence quantitative stable à partir de laquelle les évolutions futures du comportement observé des IA pourront être mesurées dans le temps.

---

## La campagne de référence en un coup d’œil

- **12 profils d’IA désidentifiés**
- **4 questions fixes**
- **100 répétitions par question**
- **3 vagues d’exécution**
- **14 400 observations finalisées**

La Baseline V1 constitue le cadre de référence initial du Baromètre Hebdomadaire NeoMundi.

Les prochaines publications hebdomadaires pourront être comparées à cette baseline afin d’évaluer si les signaux comportementaux observés restent stables, évoluent progressivement ou indiquent un possible changement de régime comportemental.

---

## Les quatre questions fixes

La campagne combine quatre conditions de réponse distinctes.

### Question 1 — Raisonnement

**Le problème de la batte et de la balle**

> Une batte et une balle coûtent 1,10 € au total.  
> La batte coûte 1 € de plus que la balle.  
> Combien coûte la balle ?

### Question 2 — Explication scientifique

**Les saisons sur Terre**

> Pourquoi les saisons se produisent-elles sur Terre ?

### Question 3 — Question conceptuelle ouverte

**Stabilité et vérité**

> Pourquoi une réponse stable produite par une IA n’est-elle pas nécessairement factuellement correcte ?

### Question 4 — Question épistémique ouverte

**Croyances largement admises mais potentiellement fausses**

> Donnez un exemple de croyance largement admise qui pourrait être fausse et expliquez comment elle pourrait être vérifiée.

Les mêmes questions ont été répétées dans des conditions de campagne contrôlées afin d’observer :

- la stabilité des réponses ;
- la variation sémantique ;
- les signaux de risque factuel ;
- la cohérence ;
- les comportements décisionnels et les régimes observés ;
- la variation runtime ;
- la complétude des mesures.

Les questions sont publiques afin que les lecteurs puissent comprendre la nature des tâches observées et reproduire de manière indépendante des conditions d’interrogation comparables.

---

## Ce que permet cette baseline

La Baseline V1 établit des indicateurs récurrents pouvant être comparés entre les publications hebdomadaires successives.

Les observations publiées comprennent :

- la stabilité ;
- les signaux de risque factuel ;
- la cohérence ;
- la variation sémantique ;
- les comportements décisionnels, notamment `ALLOW`, `FLAG` et `ERROR` ;
- la variation entre les exécutions ;
- la couverture et la complétude ;
- les plages de latence, lorsqu’elles sont disponibles ;
- `delta_g`, publié comme un signal observable avancé de variation runtime.

L’objectif n’est pas de déterminer quel système est « le meilleur ».

L’objectif est de rendre les mouvements comportementaux mesurables et visibles au travers d’observations répétées.

Un système peut rester très stable tout en présentant des signaux de risque factuel.

Un système peut varier sur le plan sémantique sans produire de réponse factuellement incorrecte.

Différents signaux peuvent converger, diverger ou rester non concluants.

**Un signal est une observation qui nécessite une interprétation, et non un verdict.**

---

## Fichiers publics

### `public_profiles_summary.csv`

Un enregistrement quantitatif agrégé pour chaque profil désidentifié.

### `public_question_profiles.csv`

Résultats quantitatifs agrégés par profil et par question.

### `public_regimes_totals.csv`

Distribution des états décisionnels et des régimes comportementaux observés. Ce fichier ne contient aucune catégorie artificielle de classement.

### `public_manifest.json`

Métadonnées de la publication, provenance de la campagne et inventaire des fichiers publics.

### `public_exclusions_and_limitations.csv`

Champs exclus, limites de publication et limites d’interprétation documentées.

### `METHODOLOGY.md`

Documentation méthodologique synthétique de la campagne Baseline V1.

---

## Limites d’interprétation

Une cellule expérimentale complète signifie que l’ensemble des exécutions prévues a été réalisé.

La couverture propre à chaque métrique est publiée séparément et peut rester inférieure à 100 % lorsqu’une métrique spécifique n’a pas pu être calculée pour chaque observation.

Une valeur de `0.0` représente une mesure égale à zéro lorsque la taille de l’échantillon propre à la métrique est supérieure à zéro.

`not_scored` signifie qu’aucun score valide n’était disponible pour l’observation concernée.

`delta_g` est un signal runtime observable et dérivé. Sa publication ne divulgue ni sa composition interne, ni ses seuils, ni sa logique de pondération, ni les règles de calcul propriétaires du cadre de mesure NeoMundi.

Les métriques publiées ne doivent pas être interprétées comme des confirmations indépendantes lorsque la documentation de la publication identifie une dépendance entre elles.

Aucune métrique individuelle ne doit être interprétée isolément comme une évaluation complète de la qualité, de la véracité, de la sécurité ou de la gouvernabilité d’un système.

---

## Périmètre de la publication publique

Le Baromètre Hebdomadaire NeoMundi publie des résultats agrégés et désidentifiés afin que les chiffres annoncés, les niveaux de couverture, les distributions de régimes et les visualisations puissent être examinés publiquement.

Cette publication est volontairement limitée.

Elle ne représente pas l’intégralité du registre de mesure NeoMundi.

---

## Ce qui reste dans le périmètre privé de mesure

Selon la campagne et le périmètre de mesure, le registre privé d’observation peut notamment comprendre :

- les enregistrements de mesure au niveau de chaque exécution, plutôt que les seuls agrégats publics ;
- les historiques d’exécutions répétées et les observations de continuité longitudinale ;
- les signaux de stabilité, de validité, de risque factuel, de variation sémantique et de cohérence au niveau de chaque exécution ;
- les états décisionnels, signalements, erreurs et diagnostics de complétude ;
- les familles de prompts, les historiques de prompts et les informations relatives aux corpus de test contrôlés ;
- les artefacts de réponse et les éléments de diagnostic ;
- la consommation de tokens, les coûts d’exécution et les indicateurs d’efficience économique ;
- la latence, les performances runtime et les signaux d’effort infrastructurel ;
- les indicateurs de densité informationnelle et d’efficience de génération ;
- les observations relatives aux économies de tokens ou aux arrêts de génération, lorsqu’elles sont applicables ;
- les identifiants de fournisseurs, de modèles, de routage, d’hébergement et de déploiement ;
- les identifiants de requêtes, de traces et de corrélation ;
- les horodatages d’exécution et les informations relatives à la continuité runtime ;
- les données brutes provenant des API, des flux de streaming et des diagnostics ;
- les notes internes d’examen, les motifs de gouvernance et les éléments d’interprétation contextuelle ;
- le registre privé reliant les systèmes observés à leurs identifiants désidentifiés stables au format `PROFILE-XXXXXX`.

Ces éléments ne sont pas publiés, car ils pourraient révéler l’identité des systèmes, la conception des prompts, le contenu des réponses, l’architecture opérationnelle, des méthodes de mesure propriétaires ou des traces runtime confidentielles.

---

## Pourquoi cette distinction est importante

La baseline publique rend les signaux comportementaux récurrents visibles, inspectables et comparables dans le temps.

Le périmètre privé de mesure conserve les éléments de preuve plus approfondis nécessaires à :

- la répétition contrôlée des exécutions ;
- l’investigation technique ;
- l’analyse longitudinale ;
- l’évaluation des coûts et de l’efficience ;
- l’examen de gouvernance ;
- l’interprétation propre à un contexte donné.

La publication publique est ainsi conçue pour permettre l’examen et la reproductibilité sans exposer les systèmes, les traces et les artefacts opérationnels à partir desquels les mesures sont produites.

---

## Désidentification et risque résiduel de réidentification

Cette publication est **désidentifiée**. Elle n’est pas présentée comme irréversiblement anonyme.

Les noms des fournisseurs, les noms des modèles, les endpoints, les réponses brutes, les traces détaillées, les horodatages précis des exécutions et la correspondance privée des profils ne sont pas publiés.

Les profils publics utilisent des identifiants opaques et stables au format :

`PROFILE-XXXXXX`

Ces identifiants ne sont dérivés ni d’un classement, ni des performances, ni du nom d’un fournisseur ou d’un modèle.

Le registre privé de correspondance est conservé séparément. Il n’est inclus ni dans ce dépôt ni dans aucune publication publique.

Le protocole expérimental et les familles de questions étant en principe reproductibles, un tiers disposant d’un accès comparable aux API, aux modèles et aux conditions d’exécution pourrait tenter d’inférer l’identité d’un ou plusieurs profils.

NeoMundi documente donc la réidentification comme un risque résiduel et accepté de la publication.

L’objectif n’est pas de revendiquer une anonymisation impossible. Il consiste à empêcher l’attribution directe tout en préservant un niveau de transparence méthodologique suffisant pour permettre un examen indépendant.

---

## Ce que cette baseline n’est pas

Cette baseline n’est pas :

- un classement de fournisseurs ;
- un palmarès de modèles ;
- une certification de sécurité ;
- une garantie d’exactitude factuelle ;
- une décision juridique, réglementaire ou de conformité ;
- une autorisation de déploiement ;
- un substitut à l’examen humain ;
- un substitut à la gouvernance ou à une validation propre à un domaine métier.

Il s’agit d’un point de référence quantitatif public permettant d’observer l’évolution du comportement runtime des IA dans le temps.
