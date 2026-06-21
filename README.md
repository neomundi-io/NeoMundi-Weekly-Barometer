## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

Ce dossier contient la release publique quantitative de référence du NeoMundi Weekly Barometer.

Il s’agit d’une baseline anonymisée : une photographie initiale et fixe de comportements runtime observés sur un panel de 12 systèmes d’IA générative dans des conditions de mesure répétées. Ce document n’est ni un baromètre hebdomadaire éditorial, ni un classement, ni une certification.

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

## Anonymisation et risque résiduel de réidentification

Les fournisseurs, modèles, endpoints, prompts, réponses brutes, traces détaillées, timestamps précis et mapping privé ne sont pas publiés.

Le protocole et les familles de prompts restent reproductibles en principe. Un tiers disposant d’un accès API comparable et de conditions expérimentales proches peut tenter d’inférer certaines identités. NeoMundi ne publie pas le mapping et documente ce risque comme résiduel plutôt que de prétendre à une anonymisation irréversible.
