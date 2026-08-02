# Baromètre hebdomadaire des IA NeoMundi #6 — Publication des données publiques

[English version](README.md)

**Campagne :** `BAROMETER_6_2026-07-20_2026-07-26`  
**Période d’observation :** du 20 juillet 2026 au 26 juillet 2026  
**Forme de publication :** données agrégées et désidentifiées

## Documentation

- [Méthodologie publique — English](../../docs/methodology_public_en.md)
- [Méthodologie publique — Français](../../docs/methodology_public_fr.md)
- [Baseline publique](../../docs/public_baseline.md)
- [Présentation du repository](../../README.md)

## Contenu de cette release

- `public_overview.json` — totaux de la campagne, métriques globales, indicateurs de qualité des données et informations relatives aux dépendances observées.
- `public_profiles_summary.csv` — une ligne agrégée par profil désidentifié (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — une ligne agrégée par question désidentifiée.
- `public_regime_distribution.csv` — répartition des régimes au niveau des observations et définitions associées.
- `public_metric_contract.json` — définitions des métriques publiées, limites d’interprétation et champs privés exclus.
- `public_manifest.json` — inventaire des fichiers, informations d’intégrité et provenance de la release.
- `build_public_barometer_release.py` — builder public associé à la validation, à l’agrégation et à la génération de cette release.

## Builder de la release publique

Le builder public associé au Baromètre #6 est inclus dans cette release afin de documenter le processus de publication disponible au moment de la campagne.

Le script réalise notamment les contrôles structurels et d’intégrité suivants :

- validation du nombre attendu de systèmes observés ;
- validation du nombre attendu de questions et d’exécutions ;
- détection des observations dupliquées ;
- validation des colonnes sources obligatoires ;
- désidentification stable à l’aide d’un registre privé de profils maintenu par NeoMundi ;
- génération des artefacts publics agrégés ;
- génération du manifeste de la release publique et des empreintes d’intégrité.

Le script documente la logique de construction de la release utilisée pour cette campagne.

Le README et les autres fichiers de documentation peuvent recevoir ultérieurement des clarifications éditoriales, sans modification des observations runtime sources ni des résultats agrégés publiés.

## Éléments volontairement non publiés

Les identifiants des providers et des modèles, les prompts, le contenu des réponses, les identifiants de requête, les identifiants de trace, les payloads bruts, les horodatages individuels des réponses, les éléments de débogage et le registre privé de correspondance des profils ne sont pas inclus.

## Contrainte importante d’interprétation

Les chiffres publiés dans cette release sont des résultats de mesure. Ils ne doivent pas être interprétés comme un classement global de qualité, une certification de sécurité, une garantie de vérité ou une autorisation de déployer un système dans un contexte particulier.

Pour cette campagne, la release documente une dépendance observée entre `stability_score`, `v_score` et `factual_hallucination_score`.

Ces valeurs ne doivent pas être considérées comme des confirmations indépendantes. L’objectif de cette release est d’exposer cette limite méthodologique plutôt que de la dissimuler.

Un signal de variation sémantique ne permet pas, à lui seul, d’établir l’existence d’une erreur factuelle. Un signal de risque factuel constitue une alerte observée nécessitant une interprétation contextuelle, et non un jugement final autonome.

Le `coherence_score` s’est révélé non discriminant au cours de cette campagne et ne doit pas être interprété comme la preuve que toutes les réponses observées étaient substantiellement cohérentes.

## Désidentification

Chaque système observé est associé en interne à un identifiant de profil opaque et stable (`PROFILE-XXXXXX`) au moyen d’un registre privé maintenu par NeoMundi.

Les identifiants ne sont pas attribués en fonction des performances, des scores, de l’ordre alphabétique ou d’un classement. Le fichier de correspondance reste privé et est exclu de cette release.

## Périmètre de reproductibilité

La cohérence interne des artefacts publics peut être vérifiée à partir des fichiers publiés et des informations d’intégrité contenues dans `public_manifest.json`.

La publication du builder apporte une transparence supplémentaire sur le processus de validation, d’agrégation et de publication.

La reproduction complète à partir des données sources nécessite toujours l’accès aux exports privés de la campagne et au registre privé des profils, dans le cadre du processus de gouvernance de l’Observatoire NeoMundi.
