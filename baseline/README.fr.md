# NeoMundi Weekly Barometer — Baseline V1

## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

Ce dossier contient la première release publique de baseline du **NeoMundi Weekly Barometer**.

Elle propose une cartographie anonymisée des comportements observés en conditions d’exécution répétées sur un panel de 12 systèmes d’IA générative.

## Ce qu’est cette baseline

La baseline est le point de référence utilisé pour interpréter les futures observations du Weekly Barometer.

Elle ne classe pas les modèles, ne certifie pas les systèmes et ne désigne pas une IA comme universellement « meilleure ».

Son objectif est de rendre visibles des régimes de comportement différents en conditions d’exécution répétées. Des systèmes peuvent présenter des profils distincts en matière de stabilité, cohérence, risque sémantique, fiabilité factuelle, latence et variation entre vagues de mesure.

## Cadre de mesure

Cette baseline publique est issue de :

* **12 profils de systèmes anonymisés** ;
* **3 vagues de mesure répétées** ;
* **4 identifiants de prompts fixes** (`Q01` à `Q04`) ;
* **100 répétitions par prompt et par vague** ;
* **14 400 observations au total**.

Le contenu des prompts, l’identité des modèles et fournisseurs, les horodatages, les sorties brutes ainsi que les mesures exactes à haute précision ne sont pas publiés dans cette release.

## Artefacts publics

| Fichier                                 | Rôle                                                                                          |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `public_manifest.json`                  | Cadre de la release, protocole de mesure, politique d’identité et liste des artefacts publiés |
| `public_profiles_summary.csv`           | Un profil comportemental anonymisé par système observé                                        |
| `public_question_profiles.csv`          | Le comportement de chaque profil sur les quatre identifiants de prompts                       |
| `public_regimes_totals.csv`             | Distribution agrégée des bandes publiques et des tendances de décision                        |
| `public_exclusions_and_limitations.csv` | Limites méthodologiques, exclusions et frontières de publication                              |

## Comment lire les bandes

Les valeurs publiées sont exprimées sous la forme de cinq **bandes de position relative au sein du panel** :

* `lowest_panel_band`
* `low_panel_band`
* `mid_panel_band`
* `high_panel_band`
* `highest_panel_band`

Ces bandes décrivent la position relative d’un profil dans cette cohorte spécifique.

Elles ne constituent **ni des seuils absolus de sûreté**, ni des notes de qualité, ni des affirmations universelles de performance.

Par exemple, une `highest_panel_band` pour `semantic_risk_position_band` signifie que le profil présente une valeur comparativement plus élevée pour cette métrique au sein du panel étudié. Cela ne permet pas, à lui seul, d’établir une propriété générale ou permanente du système.

## Ce qui n’est volontairement pas publié

Afin de préserver l’intégrité méthodologique, de limiter les risques de réidentification inutile et d’éviter de transformer l’Observatoire en leaderboard public, cette release ne publie pas :

* les noms des fournisseurs ou des modèles ;
* le mapping privé entre identités réelles et profils ;
* les observations brutes ;
* le contenu des prompts ;
* les horodatages exacts ;
* les noms des fichiers sources ;
* les valeurs précises de latence ou de coût ;
* les scores à haute précision ;
* les détails d’API, d’endpoint ou d’infrastructure.

## Note importante d’interprétation

Cette baseline est un artefact de mesure, pas un verdict.

Elle documente des comportements runtime observés selon un protocole et une fenêtre de mesure définis. Les résultats doivent être interprétés comme comparatifs, contextuels et exploratoires.

La variabilité entre vagues est estimée à partir de trois vagues de mesure répétées. Elle est utile pour détecter des premiers motifs de variation, mais ne doit pas être interprétée comme une estimation de stabilité sur le long terme.

## Remédiation et intégrité de l’audit

Un nombre limité d’échecs non sémantiques de collecte a été remédié avec la même configuration de mesure avant l’agrégation publique.

Les enregistrements d’origine sont conservés dans le corpus privé d’audit. La frontière de traitement est documentée dans `public_exclusions_and_limitations.csv`.

## Usages prévus

Cette release est destinée à soutenir :

* la revue méthodologique ;
* la discussion sur l’observabilité runtime des IA ;
* l’exploration de régimes comportementaux ;
* les comparaisons longitudinales futures ;
* les contributions scientifiques et orientées gouvernance.

Les futurs baromètres hebdomadaires utiliseront cette baseline comme couche de référence afin d’identifier les évolutions significatives du comportement observé dans le temps.

---

**NeoMundi Weekly Barometer**
*Observer l’exécution avant de prétendre gouverner.*
