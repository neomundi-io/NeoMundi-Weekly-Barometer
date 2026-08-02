# Baromètre hebdomadaire des IA NeoMundi #7 — Publication des données publiques

[English version](README.md)

**Campagne :** `BAROMETER_7_2026-07-27_2026-08-02`  
**Période d’observation :** du 27 juillet 2026 au 2 août 2026  
**Forme de publication :** données agrégées et désidentifiées

## Documentation

- [Méthodologie publique — English](../../docs/methodology_public_en.md)
- [Méthodologie publique — Français](../../docs/methodology_public_fr.md)
- [Baseline publique](../../docs/public_baseline.md)
- [Présentation du repository](../../README.md)

## Synthèse de la release

- Systèmes observés : 12
- Questions observées : 4
- Exécutions lancées : 4 800
- Exécutions entièrement scorées : 4 774
- Couverture : 99,46 %
- Lignes dupliquées : 0

## Répartition des régimes observés

- Signal normal : 97,25 % — 4 668 observations
- Variation sémantique : 1,29 % — 62 observations
- Alerte factuelle : 0,65 % — 31 observations
- Alerte combinée : 0,27 % — 13 observations
- Mesure incomplète : 0,54 % — 26 observations

## Contenu de cette release

- `public_overview.json` — totaux de la campagne, métriques globales publiques et indicateurs de qualité des données.
- `public_profiles_summary.csv` — une ligne agrégée par profil désidentifié (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — une ligne agrégée par question désidentifiée.
- `public_regime_distribution.csv` — répartition des régimes au niveau des observations et définitions associées.
- `public_metric_contract.json` — définitions des métriques publiées, limites d’interprétation et champs privés exclus.
- `public_manifest.json` — inventaire des fichiers, informations d’intégrité et provenance de la release.
- `build_public_barometer_release.py` — builder public versionné associé à la validation, à l’agrégation et à la génération de cette release.

## Builder de la release publique

Le builder public associé au Baromètre #7 est inclus dans cette release afin de documenter le processus de validation, d’agrégation et de publication utilisé pour cette campagne.

Le script réalise notamment les contrôles structurels et d’intégrité suivants :

- validation du nombre attendu de systèmes observés ;
- validation du nombre attendu de questions et de répétitions ;
- validation du nombre attendu d’exécutions ;
- détection des observations dupliquées ;
- validation des colonnes sources obligatoires ;
- séparation explicite entre les exécutions lancées, les exécutions sans erreur et les exécutions entièrement scorées ;
- désidentification stable à l’aide d’un registre privé de profils maintenu par NeoMundi ;
- génération d’artefacts publics agrégés et harmonisés ;
- génération du README public, du manifeste de provenance et des empreintes d’intégrité ;
- enregistrement des versions du builder, de Python et de pandas ;
- suppression automatique des sorties partielles en cas d’échec de la génération.

Le builder publié ne contient aucun alias spécifique à un provider ou à un modèle.

Toute correspondance exceptionnelle nécessaire avant la publication reste intégrée au processus privé de prétraitement et de gouvernance.

Le README et les autres fichiers de documentation peuvent recevoir ultérieurement des clarifications éditoriales, sans modification des observations runtime sources ni des résultats agrégés publiés.

## Éléments volontairement non publiés

Les identifiants des providers et des modèles, les prompts, le contenu des réponses,
les identifiants de requête, les identifiants de trace, les payloads bruts,
les horodatages individuels des réponses, les éléments de débogage et le registre
privé de correspondance des profils ne sont pas inclus.

## Contrainte importante d’interprétation

Les chiffres publiés dans cette release sont des résultats de mesure.

Ils ne doivent pas être interprétés comme :

- un classement global de qualité ;
- une certification de sécurité ;
- une garantie de vérité ;
- une autorisation de déployer un système dans un contexte particulier.

Un signal de variation sémantique ne permet pas, à lui seul, d’établir l’existence d’une erreur factuelle.

Un signal de risque factuel constitue une alerte observée nécessitant une interprétation contextuelle, et non un jugement final autonome.

Les régimes publiés décrivent des états de mesure observés dans les conditions de cette campagne.

Ils n’établissent pas une causalité ni un jugement général sur un système observé.

## Améliorations de la release publique 2.1.0

Par rapport au processus de publication publique précédent, le Baromètre #7 renforce :

- la validation des systèmes, des questions, des répétitions et des observations dupliquées ;
- la séparation explicite entre les exécutions lancées, les exécutions sans erreur et les exécutions entièrement scorées ;
- la désidentification stable à l’aide d’un registre privé maintenu par NeoMundi ;
- l’utilisation d’un contrat canonique des métriques publiques ;
- l’harmonisation des fichiers agrégés par profil, par question et par régime ;
- la génération automatique du README de la release ;
- la génération automatique du manifeste de provenance ;
- la génération d’empreintes d’intégrité SHA-256 ;
- l’enregistrement de la version du builder ;
- l’enregistrement des versions de Python et de pandas ;
- la suppression automatique des sorties partielles en cas d’échec de la génération.

Ces améliorations concernent l’intégrité, la traçabilité, la cohérence et l’auditabilité de la release.

Elles ne modifient pas les observations runtime sources et ne constituent pas une nouvelle validation scientifique des métriques publiées.

## Transition méthodologique vers le Baromètre #8

Le Baromètre #7 constitue une transition entre la consolidation du processus de publication publique et l’introduction d’un contrôle formalisé de la comparabilité longitudinale.

À partir du Baromètre #8, le pipeline de publication doit intégrer une comparaison automatisée entre le protocole de la campagne courante et celui de la campagne précédente.

Le contrôle prévu examinera notamment, lorsque les informations sont disponibles :

- le corpus de questions ;
- le nombre attendu de répétitions ;
- le périmètre commun des systèmes observés ;
- le périmètre complet des systèmes observés ;
- les métriques publiées ;
- les règles d’agrégation ;
- les modifications du pipeline de publication publique ;
- les observations manquantes ;
- les erreurs d’exécution ;
- les ajouts ou retraits au sein de la cohorte observée.

Le résultat prévu distinguera trois statuts :

- `DIRECTLY_COMPARABLE` — directement comparable ;
- `COMPARABLE_WITH_RESERVATIONS` — comparable avec réserves ;
- `NOT_DIRECTLY_COMPARABLE` — non directement comparable.

La comparaison distinguera également :

1. le périmètre longitudinal stable commun aux deux campagnes ;
2. le périmètre complet de la campagne courante.

Cette future évolution concerne la traçabilité de l’interprétation longitudinale.

Elle ne permettra pas :

- de valider la performance scientifique d’une métrique individuelle ;
- d’établir une attribution causale ;
- de transformer un signal mesuré en verdict ;
- de produire un classement général de qualité des systèmes observés.

L’implémentation utilisée pour le Baromètre #8 sera versionnée et publiée avec cette release.

## Désidentification

Chaque système observé est associé en interne à un identifiant de profil opaque et stable
(`PROFILE-XXXXXX`) au moyen d’un registre privé maintenu par NeoMundi.

Les identifiants ne sont pas attribués en fonction des performances, des scores,
de l’ordre alphabétique ou d’un classement.

Le fichier de correspondance reste privé et est exclu de cette release.

## Périmètre de reproductibilité

La cohérence interne des artefacts publics peut être vérifiée à partir des fichiers publiés
et des informations d’intégrité contenues dans `public_manifest.json`.

La publication du builder apporte une transparence supplémentaire sur le processus
de validation, d’agrégation et de publication.

La reproduction complète à partir des données sources nécessite l’accès aux exports privés
de la campagne, au registre privé des profils et à l’environnement gouverné de prétraitement,
dans le cadre du processus de gouvernance de l’Observatoire NeoMundi.
