# Baromètre IA #13 — édition sous couverture insuffisante

*Édition exceptionnelle — 7 au 13 septembre 2026 (UTC) — statut : COUVERTURE INSUFFISANTE*

> **Cette semaine, 10 systèmes sur 12 ont pu être pleinement observés. Deux flux n'ont pas fourni une couverture exploitable. NeoMundi publie l'état mesuré sans compléter, masquer ni extrapoler les données absentes.**

---

## Pourquoi cette édition est différente

Le Baromètre IA NeoMundi repose sur une règle simple et non négociable : une édition n'est publiée dans sa forme standard que si au moins 90 % des mesures prévues sur les 12 systèmes ont été pleinement scorées. Cette semaine, la couverture réelle s'établit à **82,9 %** (3 981 mesures pleinement scorées sur 4 800 prévues sur l'ensemble des 12 systèmes). Le seuil de publication standard n'a été ni abaissé, ni contourné : la release standard du Baromètre #13 reste bloquée.

Plutôt que de retarder indéfiniment la publication ou de masquer le problème, NeoMundi publie cette **édition exceptionnelle**, clairement distincte de la chaîne standard, qui présente honnêtement ce qui a été mesuré, ce qui ne l'a pas été, et pourquoi.

## Ce qui a été mesuré

10 des 12 systèmes officiels ont produit une observation complète et exploitable : 400 exécutions prévues, 400 exécutions lancées, avec un taux de couverture individuel compris entre 99,0 % et 100 % selon le système. Ces dix systèmes représentent 4 000 des 4 800 observations prévues cette semaine.

Les chiffres ci-dessous portent **uniquement sur ces 10 systèmes mesurés** — aucune agrégation ni moyenne n'inclut les deux systèmes en donnée insuffisante, et aucune agrégation globale à 12 systèmes n'est présentée comme valide dans cette édition.

| Indicateur | Valeur (10 systèmes mesurés) |
|---|---|
| Exécutions lancées | 4 000 |
| Exécutions pleinement scorées | 3 981 |
| Couverture (10 systèmes) | 99,53 % |

Le détail par système et par question figure dans `public_profiles_summary.csv`, `public_questions_summary.csv` et `public_regime_distribution.csv`.

## Ce qui n'a pas pu être mesuré

Deux systèmes officiels n'ont produit **aucune observation exploitable** durant toute la fenêtre de collecte : chaque tentative a échoué avec exactement le même message technique, sur 100 % des requêtes tentées, à quatre reprises distinctes — y compris après une rotation des identifiants d'accès API destinée à écarter l'hypothèse d'une clé expirée ou invalide.

Ces deux systèmes sont marqués **`insufficient_data`** dans le tableau public des 12 systèmes (`public_systems_status.csv`) — ni mesurés, ni estimés, ni comblés par une donnée de substitution. Aucune valeur historique, aucune moyenne d'autres systèmes, aucune extrapolation n'a été utilisée pour combler ce manque : les 800 observations prévues pour ces deux systèmes restent **absentes (null)**.

Le détail factuel complet de l'incident (endpoint concerné, message d'erreur exact, chronologie des tentatives, statut de résolution) figure dans la note d'incident séparée et dans `incident_report.json`.

## Statut des 12 systèmes

| Profil | Statut | Prévues | Lancées | Pleinement scorées | Couverture |
|---|---|---|---|---|---|
| PROFILE-161CC5 | mesuré | 400 | 400 | 399 | 99,75 % |
| PROFILE-212079 | mesuré | 400 | 400 | 396 | 99,00 % |
| PROFILE-486F91 | mesuré | 400 | 400 | 397 | 99,25 % |
| PROFILE-48C581 | mesuré | 400 | 400 | 400 | 100,00 % |
| PROFILE-59664C | mesuré | 400 | 400 | 398 | 99,50 % |
| PROFILE-5A5C60 | **données insuffisantes** | 400 | 0 | 0 | — |
| PROFILE-5B3BB7 | mesuré | 400 | 400 | 396 | 99,00 % |
| PROFILE-638E26 | mesuré | 400 | 400 | 399 | 99,75 % |
| PROFILE-739F7C | mesuré | 400 | 400 | 400 | 100,00 % |
| PROFILE-B912EA | mesuré | 400 | 400 | 399 | 99,75 % |
| PROFILE-DEA9C5 | mesuré | 400 | 400 | 397 | 99,25 % |
| PROFILE-F5FF91 | **données insuffisantes** | 400 | 0 | 0 | — |

*Conformément à la méthodologie NeoMundi, l'identité réelle de chaque système reste privée ; seul un identifiant opaque `PROFILE-XXXXXX` est publié — y compris pour les deux systèmes en donnée insuffisante.*

## Comparabilité avec le Baromètre #12

**Statut : `NOT_COMPARABLE`.** Le Baromètre #12 avait mesuré 12 systèmes sur 12 ; cette édition en mesure 10 sur 12. Aucune évolution chiffrée, aucune tendance, aucun classement comparatif n'est calculé ou suggéré entre les deux éditions. Toute lecture de cette édition comme une évolution du Baromètre #12 serait une interprétation non fondée sur les données publiées.

## Limites méthodologiques de cette édition

- Aucune imputation, aucune donnée de remplacement, aucun report de valeur historique.
- Aucune moyenne ni indicateur global calculé sur les 12 systèmes attendus.
- Aucune conclusion de tendance, de fiabilité générale ou de classement entre fournisseurs.
- Les valeurs absentes des deux systèmes en incident restent nulles, jamais estimées.
- Cette édition est structurellement distincte de la release standard et n'est pas indexée comme telle dans l'historique des releases comparables.

## Prochaines étapes

La release standard du Baromètre #13 reste en attente : elle sera publiée seulement si la couverture des 12 systèmes atteint 90 % après résolution de l'incident technique décrit ci-dessus. Le Baromètre #14 suivra ensuite la chaîne scientifique normale, avec le même seuil de 90 % inchangé.

---

*Lire ces chiffres avec leur couverture et les réserves méthodologiques ci-dessus. Détail technique complet : `incident_report.json`, `public_manifest.json`, `public_systems_status.csv`.*
