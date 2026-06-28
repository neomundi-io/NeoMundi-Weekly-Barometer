## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**

# Baromètre Hebdomadaire NeoMundi — Baseline publique V1

Ce dossier contient la première publication quantitative de référence du Baromètre Hebdomadaire NeoMundi.

Il s’agit d’une **baseline désidentifiée** : une photographie de référence fixe des comportements runtime observés sur un panel de 12 systèmes d’IA générative, dans des conditions de mesure répétées et contrôlées.

Ce n’est ni un rapport éditorial hebdomadaire, ni un classement, ni une certification, ni un benchmark, ni une évaluation globale de la qualité des IA.

Son objectif est plus précis et plus durable : établir un point de référence stable à partir duquel les évolutions futures des comportements runtime observés pourront être mesurées dans le temps.

## La campagne de référence en bref

**12 profils IA désidentifiés**
**4 questions fixes**
**100 répétitions par question**
**3 vagues d’exécution**
**14 400 observations finalisées**

La Baseline V1 constitue le référentiel initial du Baromètre Hebdomadaire NeoMundi.

Les futurs Baromètres hebdomadaires pourront être comparés à cette référence afin d’observer si les signaux comportementaux restent stables, varient progressivement ou présentent les signes d’un possible changement de régime.

## Les quatre questions fixes

La campagne combine quatre conditions de réponse distinctes.

### Question 1 — Raisonnement

**Le problème de la batte et de la balle**

> Une batte et une balle coûtent au total 1,10 €.
> La batte coûte 1 € de plus que la balle.
> Combien coûte la balle ?

### Question 2 — Explication scientifique

**Les saisons sur Terre**

> Pourquoi les saisons existent-elles sur Terre ?

### Question 3 — Question conceptuelle ouverte

**Stabilité et vérité**

> Pourquoi une réponse stable produite par une IA n’est-elle pas nécessairement factuellement correcte ?

### Question 4 — Question épistémique ouverte

**Croyances largement admises mais potentiellement fausses**

> Donnez un exemple de croyance largement admise qui pourrait être fausse, et expliquez comment elle pourrait être vérifiée.

Ces questions ont été rejouées dans les mêmes conditions de campagne afin d’observer la stabilité des réponses, les signaux de risque factuel, la cohérence, la variation sémantique, le comportement décisionnel et la variation runtime.

Les questions sont publiques afin que les lecteurs puissent comprendre la nature des tâches observées et reproduire de manière indépendante des conditions d’enquête comparables.

## Ce que cette baseline permet

La baseline fixe des indicateurs récurrents pouvant être comparés dans les Baromètres suivants.

Les observations publiées comprennent notamment :

* la stabilité ;
* le signal de risque factuel ;
* la cohérence ;
* la variation sémantique ;
* le comportement décisionnel, notamment `ALLOW`, `FLAG` et `ERROR` ;
* la variation entre exécutions ;
* la couverture et la complétude de mesure ;
* les bandes de latence, lorsqu’elles sont publiées ;
* `delta_g`, publié comme signal observable avancé de variation runtime.

L’objectif n’est pas de déterminer quel système serait « le meilleur ».

L’objectif est de rendre visibles les mouvements comportementaux à travers des observations répétées.

Un système peut rester stable tout en présentant des signaux de risque factuel. Un système peut varier sémantiquement sans être factuellement incorrect. Un signal est une observation qui demande une interprétation, et non un verdict.

## Fichiers publics

* `public_profiles_summary.csv`
  Un enregistrement quantitatif agrégé par profil désidentifié.

* `public_question_profiles.csv`
  Résultats quantitatifs agrégés par profil et par question.

* `public_regimes_totals.csv`
  Répartition des décisions et régimes observés. Ce fichier ne contient pas de bandes de classement artificielles.

* `public_manifest.json`
  Métadonnées de publication, provenance de campagne et inventaire des fichiers publics.

* `public_exclusions_and_limitations.csv`
  Champs exclus, frontière de publication et limites d’interprétation.

* `METHODOLOGY.md`
  Note méthodologique synthétique consacrée à la campagne baseline.

## Frontière d’interprétation

Une cellule complète signifie que l’ensemble d’exécutions prévu a été réalisé.

La couverture au niveau de chaque métrique est publiée séparément. Elle peut être inférieure à 100 % lorsqu’une métrique individuelle n’a pas pu être calculée pour toutes les observations.

Un score de `0.0` correspond à un zéro mesuré lorsque la taille d’échantillon de la métrique est positive.

`not_scored` signifie qu’aucun score valide n’était disponible pour l’observation concernée.

`delta_g` est un signal runtime dérivé observable. Sa publication ne révèle ni sa composition interne, ni ses seuils, ni sa logique de pondération, ni les règles de calcul propriétaires du cadre de mesure NeoMundi.

Les métriques publiées ne doivent pas être interprétées comme des confirmations indépendantes lorsqu’une dépendance entre elles est documentée dans le release.

## Frontière de publication publique

Le Baromètre Hebdomadaire NeoMundi publie des résultats agrégés et désidentifiés afin que les chiffres annoncés, la couverture, les régimes observés et les visualisations puissent être examinés publiquement.

La publication publique est volontairement bornée.

Elle ne constitue pas l’intégralité du dossier de mesure NeoMundi.

## Ce qui reste dans la frontière privée de mesure

Selon la campagne et le périmètre de mesure, le dossier d’observation privé peut comprendre :

* des enregistrements de mesure au niveau de chaque exécution, plutôt que de simples agrégats hebdomadaires ;
* des historiques de répétitions et des observations de continuité ;
* des signaux de stabilité, de validité, de risque factuel, de variation sémantique et de cohérence au niveau de chaque exécution ;
* des états de décision, des flags, des erreurs et des diagnostics de complétude ;
* des familles de prompts, des historiques par prompt et des informations relatives au corpus de test contrôlé ;
* des artefacts au niveau des réponses et du matériel diagnostique ;
* la consommation de tokens, les coûts d’exécution et des indicateurs d’efficience économique ;
* des signaux de latence, de performance runtime et d’effort d’infrastructure ;
* des indicateurs de densité informationnelle et d’efficience de génération ;
* des observations relatives à l’économie de tokens ou à l’arrêt anticipé de génération, lorsque cela est applicable ;
* des identifiants de fournisseurs, de modèles, de routage, d’hébergement et de déploiement ;
* des identifiants de requêtes, de traces et de corrélation ;
* des horodatages d’exécution et des informations de continuité runtime ;
* des payloads API, streaming et diagnostics bruts ;
* des notes internes de revue, des raisons de gouvernance et des enregistrements d’interprétation contextuelle ;
* le registre privé reliant les systèmes observés aux identifiants désidentifiés stables `PROFILE-XXXXXX`.

Ces éléments ne sont pas publiés, car ils pourraient révéler l’identité des systèmes, la conception des prompts, le contenu des réponses, l’architecture opérationnelle, les méthodes de mesure ou des traces runtime confidentielles.

## Pourquoi cette distinction compte

La baseline publique rend les signaux comportementaux récurrents visibles et comparables.

La frontière privée de mesure conserve les éléments de preuve plus profonds nécessaires au rejeu contrôlé, à la revue technique, à l’analyse de coût et d’efficience, à l’évaluation de gouvernance et aux investigations dépendantes du contexte.

La publication publique est donc conçue pour être examinable sans exposer les systèmes, les traces opérationnelles et les artefacts dont elle est issue.

## Désidentification et risque résiduel de réidentification

Cette publication est **désidentifiée**. Elle ne prétend pas être irréversiblement anonyme.

Les noms de fournisseurs, les noms de modèles, les endpoints, les prompts, les réponses brutes, les traces détaillées, les horodatages précis d’exécution et le mapping privé des profils ne sont pas publiés.

Les profils publics utilisent des identifiants opaques stables au format `PROFILE-XXXXXX`.

Ces identifiants ne sont pas attribués en fonction d’un classement, d’une performance, d’un fournisseur ou d’un modèle.

Le mapping privé est conservé séparément et n’est inclus ni dans ce dépôt ni dans aucune publication publique.

Parce que le protocole expérimental et les familles de questions sont en principe reproductibles, un tiers disposant d’un accès API comparable, de modèles disponibles et de conditions d’exécution similaires pourrait tenter d’inférer l’identité d’un ou plusieurs profils.

NeoMundi documente donc la réidentification comme un risque résiduel et accepté de la publication.

L’objectif n’est pas de revendiquer une anonymisation impossible. Il est d’empêcher l’attribution directe tout en conservant un niveau de transparence méthodologique suffisant pour permettre un examen indépendant.

## Ce que cette baseline n’est pas

Cette baseline n’est pas :

* un classement de fournisseurs ;
* un leaderboard de modèles ;
* une certification de sûreté ;
* une garantie de vérité factuelle ;
* une décision juridique, réglementaire ou de conformité ;
* une autorisation de déploiement ;
* un substitut à la revue humaine, à la gouvernance ou à une validation propre au domaine concerné.

C’est un point de référence public destiné à observer les comportements runtime des IA dans le temps.
