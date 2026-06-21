## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

Ce dossier contient la release publique quantitative de référence du NeoMundi Weekly Barometer.

Il s’agit d’une baseline anonymisée : une photographie initiale et fixe de comportements runtime observés sur un panel de 12 systèmes d’IA générative dans des conditions de mesure répétées. Ce document n’est ni un baromètre hebdomadaire éditorial, ni un classement, ni une certification.

## La campagne de référence en bref

**12 systèmes IA anonymisés · 4 questions fixes · 100 répétitions par question · 3 vagues d’exécution · 14 400 observations finalisées**

Cette baseline constitue le point de référence initial du NeoMundi Weekly Barometer. Elle permet de mesurer, semaine après semaine, l’évolution éventuelle du comportement runtime des systèmes observés.

### Les quatre questions fixes

La campagne associe quatre conditions de réponse différentes :

1. **Raisonnement — problème de la batte et de la balle**
   Une batte et une balle coûtent 1,10 € au total. La batte coûte 1 € de plus que la balle. Combien coûte la balle ?

2. **Explication scientifique — les saisons sur Terre**
   Pourquoi les saisons existent-elles sur Terre ?

3. **Question conceptuelle ouverte — stabilité et vérité**
   Pourquoi une réponse IA stable n’est-elle pas nécessairement factuellement correcte ?

4. **Question épistémique ouverte — croyances largement admises mais potentiellement fausses**
   Donnez un exemple de croyance largement admise qui pourrait être fausse, puis expliquez comment elle pourrait être vérifiée.

Ces questions ont été répétées dans les mêmes conditions de campagne afin d’observer la stabilité des réponses, les signaux de validité factuelle, la cohérence, la variabilité sémantique, le comportement de décision et les variations runtime.

Les questions sont publiques afin que chacun puisse comprendre la nature des tâches observées et reproduire des conditions d’interrogation comparables.

## Ce que permet cette baseline

Elle fixe les indicateurs récurrents qui pourront être comparés dans les baromètres suivants :

- stabilité ;
- signal d’hallucination factuelle ;
- cohérence ;
- instabilité sémantique ;
- comportement de décision (`ALLOW`, `FLAG`, `ERROR`) ;
- variabilité inter-run ;
- bande de latence ;
- `delta_g`, signal avancé de variation runtime observée.

## Fichiers

- `public_profiles_summary.csv` — une ligne quantitative par profil pseudonymisé.
- `public_question_profiles.csv` — résultats quantitatifs par profil et par question.
- `public_regimes_totals.csv` — distribution directe des issues de décision ; aucun binning de rang artificiel.
- `public_manifest.json` — métadonnées de release et politique de champs.
- `public_exclusions_and_limitations.csv` — exclusions et limites d’interprétation.
- `METHODOLOGY.md` — note méthodologique courte.

## Limite d’interprétation

Le statut `complete` signifie que le jeu d’exécutions prévu a été réalisé. La couverture de chaque métrique est publiée séparément et peut être inférieure à 100 % si une métrique individuelle n’a pas pu être calculée pour toutes les observations.

Un score `0.0` est un vrai zéro mesuré lorsque le `n` de cette métrique est positif. `not_scored` signifie qu’aucun score valide n’était disponible.

`delta_g` est un signal runtime dérivé et observable. Sa publication ne divulgue ni la composition interne, ni les seuils, ni les pondérations, ni les règles de calcul propriétaires du cadre de mesure NeoMundi.

## Désidentification et risque résiduel de réidentification

Cette publication est désidentifiée ; elle ne prétend pas garantir un anonymat irréversible.

Les noms des fournisseurs, les noms des modèles, les endpoints, les prompts, les réponses brutes, les traces détaillées, les horodatages précis d’exécution ainsi que le mapping privé des profils ne sont pas publiés.

Les profils publics utilisent des identifiants opaques et stables (`PROFILE-XXXXXX`). Ils ne sont dérivés ni d’un classement, ni d’une performance, ni du nom d’un fournisseur ou d’un modèle. Le mapping privé est conservé séparément et n’est inclus ni dans ce dépôt ni dans les releases publiques.

Le protocole expérimental et les familles de prompts restant, en principe, reproductibles, un tiers disposant d’un accès API comparable, de modèles disponibles et de conditions d’exécution proches pourrait tenter d’inférer l’identité d’un ou plusieurs profils.

NeoMundi documente donc la réidentification comme un risque résiduel et assumé de publication. L’objectif n’est pas de prétendre à un anonymat impossible, mais d’empêcher l’attribution directe tout en préservant un niveau de transparence méthodologique suffisant pour permettre un examen indépendant.
