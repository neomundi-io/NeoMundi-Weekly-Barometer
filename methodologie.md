🌐 **Langue :** [Français](./methodologie.md) · [English](./methodology.md)

# NeoMundi Weekly Barometer

## Méthodologie du Baromètre Hebdomadaire NeoMundi

**Version :** `v2.0`  
**Statut :** protocole public actif  
**Objet :** observation longitudinale, répétée et multi-signaux du comportement runtime des systèmes d’IA générative

---

## 1. Finalité du projet

Le **NeoMundi Weekly Barometer** est un programme récurrent de mesure destiné à observer l’évolution du comportement des systèmes d’IA générative dans le temps.

Les benchmarks traditionnels évaluent généralement un modèle à un instant donné, sur un ensemble de tâches prédéfinies.

Le Baromètre NeoMundi poursuit un objectif complémentaire :

> observer les trajectoires comportementales des systèmes d’IA et rendre visibles les changements qui peuvent apparaître silencieusement d’une semaine à l’autre.

Le projet ne vise pas à produire un classement commercial, un leaderboard ou une certification générale des systèmes observés.

Il vise à produire des mesures répétées, comparables et documentées permettant de caractériser :

- la stabilité ;
- la variation sémantique ;
- la cohérence ;
- les signaux de risque factuel ;
- les régimes comportementaux ;
- la couverture des mesures ;
- certaines variations de coût, de latence ou d’effort runtime lorsqu’elles sont disponibles.

Le Baromètre constitue ainsi un instrument d’observation longitudinale du comportement des IA.

---

## 2. Hypothèse centrale

Une réponse isolée ne suffit pas à caractériser le comportement d’un système génératif.

Lorsqu’un même prompt est soumis cent fois à un même système, dans des conditions contrôlées, il devient possible d’observer :

- la répétabilité des réponses ;
- leur dispersion ;
- leur variation sémantique ;
- leur cohérence ;
- les signaux de risque factuel ;
- les états décisionnels ou régimes produits par la chaîne de mesure ;
- les erreurs et mesures incomplètes ;
- les variations runtime associées.

Lorsque cette opération est répétée chaque semaine avec les mêmes questions et une chaîne de mesure comparable, les campagnes successives forment une série longitudinale.

Le saut méthodologique ne réside donc pas seulement dans la répétition.

Il réside dans le passage :

> de la mesure ponctuelle à l’observation du comportement dans le temps.

---

## 3. Architecture générale du protocole

### 3.1 Format hebdomadaire

Chaque campagne hebdomadaire comprend :

```text
12 profils d’IA désidentifiés
× 4 questions fixes
× 100 répétitions
= 4 800 exécutions planifiées
```

Les profils publics sont représentés par des identifiants opaques et stables au format :

```text
PROFILE-XXXXXX
```

Ces identifiants ne correspondent ni à un classement, ni à un niveau de performance, ni à une catégorie de fournisseur.

La correspondance entre les identifiants publics et les systèmes observés est conservée dans un registre privé séparé.

---

### 3.2 Fenêtre de mesure

La fenêtre hebdomadaire de référence est :

```text
lundi 00:00 UTC
à
dimanche 23:59 UTC
```

Les exécutions doivent être horodatées afin de préserver la traçabilité de la campagne et de permettre les comparaisons longitudinales.

La publication publique peut intervenir après la clôture de la période, une fois les opérations de validation, d’agrégation et de contrôle terminées.

---

### 3.3 Conditions de comparabilité

La comparabilité entre les campagnes repose notamment sur :

- le maintien des quatre questions fixes ;
- le versionnage explicite des prompts ;
- une politique d’exécution documentée ;
- une chaîne de mesure contrôlée ;
- une procédure constante de désidentification ;
- une validation systématique des fichiers ;
- la conservation de la couverture réelle ;
- l’absence de remplacement silencieux des données manquantes ;
- le versionnage des scripts de génération et d’analyse.

Une modification significative du protocole doit être documentée dans le manifeste de la publication concernée.

---

## 4. Les quatre questions fixes

Les quatre questions couvrent des conditions de réponse distinctes.

### Question 1 — Raisonnement

**Le problème de la batte et de la balle**

> Une batte et une balle coûtent 1,10 € au total.  
> La batte coûte 1 € de plus que la balle.  
> Combien coûte la balle ?

Cette question permet notamment d’observer :

- la répétabilité d’un raisonnement court ;
- la stabilité de la réponse finale ;
- la persistance éventuelle d’une erreur intuitive ;
- la relation entre stabilité et exactitude.

---

### Question 2 — Explication scientifique

**Les saisons sur Terre**

> Pourquoi les saisons se produisent-elles sur Terre ?

Cette question permet notamment d’observer :

- la stabilité d’une explication scientifique ;
- les variations de structure ;
- les omissions ;
- les simplifications ;
- les signaux de risque factuel ;
- la cohérence explicative.

---

### Question 3 — Question conceptuelle ouverte

**Stabilité et vérité**

> Pourquoi une réponse stable produite par une IA n’est-elle pas nécessairement factuellement correcte ?

Cette question permet notamment d’observer :

- la compréhension de la distinction entre répétabilité et vérité ;
- la qualité de l’argumentation ;
- la cohérence conceptuelle ;
- la variation sémantique ;
- les styles de prudence.

---

### Question 4 — Question épistémique ouverte

**Croyances largement admises mais potentiellement fausses**

> Donnez un exemple de croyance largement admise qui pourrait être fausse et expliquez comment elle pourrait être vérifiée.

Cette question permet notamment d’observer :

- la sélection spontanée d’un exemple ;
- la prudence épistémique ;
- les stratégies de vérification proposées ;
- la variation des contenus produits ;
- les risques de répétition stable d’une affirmation incorrecte.

---

## 5. Pourquoi les quatre questions restent séparées

Les quatre questions ne doivent pas être réduites à un indicateur unique.

Elles couvrent des conditions cognitives et comportementales différentes :

| Question | Condition principale observée |
|---|---|
| `Q01` | Raisonnement court et réponse déterminée |
| `Q02` | Explication scientifique |
| `Q03` | Compréhension conceptuelle de la stabilité |
| `Q04` | Variation épistémique et réponse ouverte |

Une variation observée sur une question ouverte ne possède pas nécessairement la même signification qu’une variation observée sur une question fermée.

Les résultats doivent donc être analysés :

- globalement ;
- par profil ;
- par question ;
- par métrique ;
- dans le temps.

---

## 6. La Baseline Publique V1

La Baseline V1 constitue la première référence quantitative publique du Baromètre.

Elle comprend :

```text
12 profils désidentifiés
× 4 questions
× 100 répétitions
× 3 vagues
= 14 400 observations finalisées
```

La baseline ne constitue pas une semaine ordinaire du Baromètre.

Elle représente une campagne de référence élargie, conçue pour établir un premier cadre quantitatif stable.

Elle permet notamment :

- d’observer la dispersion initiale des mesures ;
- de documenter les différences entre questions ;
- de fixer un premier point de comparaison ;
- d’identifier les limites de couverture ;
- de distinguer les variations ordinaires de changements potentiellement significatifs.

Les campagnes hebdomadaires suivantes peuvent être comparées à cette référence, sans que toute différence soit automatiquement qualifiée de dérive.

---

## 7. Signaux observés

Selon la campagne et la couverture disponible, le Baromètre publie ou documente plusieurs catégories de signaux.

### 7.1 Stabilité

La stabilité décrit le degré de répétabilité des réponses produites dans des conditions comparables.

Elle ne constitue pas une preuve d’exactitude.

Une réponse peut être :

- stable et correcte ;
- stable et incorrecte ;
- variable et correcte ;
- variable et incorrecte.

---

### 7.2 Variation sémantique

La variation sémantique décrit les écarts de contenu ou de formulation observés entre des réponses produites à partir d’une même question.

Une variation sémantique ne constitue pas, à elle seule, une erreur.

Elle peut refléter :

- une reformulation ;
- un changement de structure ;
- une différence de profondeur ;
- un changement d’exemple ;
- une modification plus importante du contenu produit.

---

### 7.3 Risque factuel

Le signal de risque factuel indique qu’une réponse présente des caractéristiques nécessitant une vérification complémentaire.

Il ne constitue pas un jugement juridique ou une certification de fausseté.

Il doit être interprété avec :

- la question concernée ;
- le niveau de couverture ;
- les autres signaux ;
- les limites de la procédure de scoring ;
- les éventuelles dépendances entre métriques.

---

### 7.4 Cohérence

La cohérence décrit la continuité logique ou structurelle observable dans la réponse.

Une réponse cohérente n’est pas nécessairement vraie.

Inversement, une variation de cohérence ne permet pas à elle seule de conclure à une dégradation générale du système.

---

### 7.5 Régimes et états d’observation

Les publications peuvent inclure des états tels que :

```text
NORMAL
SEMANTIC_VARIATION
FACTUAL_ALERT
INCOMPLETE_MEASUREMENT
```

ou des états techniques et décisionnels documentés dans les fichiers de la campagne.

Ces catégories servent à organiser les observations.

Elles ne constituent ni des classements, ni des niveaux universels de qualité.

---

### 7.6 `delta_g`

`delta_g` est publié comme un signal observable avancé de variation runtime.

Sa publication ne divulgue pas :

- sa composition interne complète ;
- ses seuils propriétaires ;
- sa logique de pondération ;
- l’intégralité de ses règles de calcul.

Il ne doit pas être interprété isolément comme un verdict sur un système.

---

### 7.7 Couverture et complétude

La couverture indique la proportion des exécutions ou métriques pour lesquelles une mesure valide a pu être produite.

Une campagne peut avoir réalisé l’ensemble des exécutions planifiées tout en présentant une couverture métrique légèrement inférieure à 100 %.

Les erreurs, données absentes et observations non scorées ne doivent pas être remplacées silencieusement par zéro.

---

## 8. Doctrine d’interprétation

Le Baromètre suit une règle fondamentale :

> un signal n’est pas un verdict.

Une observation ne permet pas, à elle seule, de conclure :

- qu’un système dit systématiquement vrai ;
- qu’un système est globalement supérieur à un autre ;
- qu’un changement provient d’une mise à jour de modèle ;
- qu’une variation constitue une dégradation ;
- qu’une réponse stable est fiable ;
- qu’une réponse variable est incorrecte ;
- qu’un système est conforme à une exigence réglementaire ;
- qu’un système peut être déployé sans contrôle complémentaire.

La formulation appropriée est :

> un changement de comportement a été observé dans les conditions de la campagne.

L’attribution d’une cause nécessite des éléments supplémentaires.

Les causes possibles peuvent notamment inclure :

- une évolution du modèle ;
- une modification du routage ;
- un changement de configuration ;
- une modification de l’API ;
- un ajustement des politiques du fournisseur ;
- une variation d’infrastructure ;
- une expérimentation interne ;
- une fluctuation statistique ;
- une variation de la chaîne de mesure.

---

## 9. Observation longitudinale

La valeur principale du Baromètre réside dans la répétition des campagnes.

Une observation isolée décrit un état.

Une succession de campagnes permet d’observer :

- une stabilité persistante ;
- une variation progressive ;
- un retour à un régime antérieur ;
- une rupture ponctuelle ;
- un plateau ;
- une anomalie persistante ;
- une évolution spécifique à une question.

Une variation ne doit pas être qualifiée publiquement de dérive sur la base d’un seul indicateur ou d’une seule campagne sans analyse complémentaire.

L’interprétation doit prendre en compte :

- l’amplitude du changement ;
- sa persistance ;
- le nombre de signaux concernés ;
- la couverture de la campagne ;
- les erreurs techniques éventuelles ;
- la variation naturelle observée dans les campagnes précédentes.

---

## 10. Détection des changements de régime

Une évolution peut être examinée comme un changement potentiel de régime lorsqu’elle :

- dépasse les variations habituellement observées ;
- concerne plusieurs signaux cohérents ;
- ne résulte pas d’une erreur connue du pipeline ;
- ne résulte pas d’une troncature ;
- présente une couverture suffisante ;
- persiste dans le temps ou présente une amplitude exceptionnelle documentée.

La détection d’un changement ne vaut pas attribution de cause.

Les résultats publics doivent distinguer :

1. l’observation ;
2. l’interprétation ;
3. l’hypothèse causale éventuelle.

---

## 11. Validation des données

Chaque campagne doit passer par une phase de validation avant agrégation et publication.

Cette validation vérifie notamment :

- le nombre d’exécutions attendues ;
- la présence des profils et questions prévus ;
- la cohérence des index de répétition ;
- l’absence de doublons non documentés ;
- la présence des horodatages ;
- la cohérence des fichiers sources ;
- la présence des métriques attendues ;
- l’identification des erreurs ;
- l’identification des observations non scorées ;
- la couverture par métrique ;
- la cohérence des versions de scripts ;
- la conformité du mapping privé de désidentification.

Aucune interpolation silencieuse ne doit être appliquée.

Toute observation exclue ou incomplète doit rester identifiable dans les données de travail ou dans les fichiers publics de limites.

---

## 12. Traçabilité technique

Selon les capacités du pipeline et des fournisseurs, les enregistrements privés peuvent inclure :

```text
campaign_id
week_id
run_id
repetition_index
question_id
prompt_version
timestamp_utc
profile_id
requested_model
returned_model
endpoint
finish_reason
input_tokens
output_tokens
latency_ms
cost
pipeline_version
analysis_version
validation_status
exclusion_reason
```

La disponibilité réelle de chaque champ peut varier selon les fournisseurs et les campagnes.

Les publications publiques ne doivent pas laisser entendre qu’un champ est disponible lorsqu’il ne l’est pas.

---

## 13. Désidentification

Les résultats publics sont publiés sous forme agrégée et désidentifiée.

Les noms des fournisseurs, modèles, endpoints, réponses brutes, traces détaillées et horodatages précis ne sont pas publiés dans les releases publiques.

Les profils utilisent des identifiants opaques et stables au format :

```text
PROFILE-XXXXXX
```

La correspondance privée entre ces identifiants et les systèmes observés est conservée séparément.

La désidentification ne doit pas être présentée comme une anonymisation irréversible.

Une réidentification indirecte peut rester théoriquement possible lorsqu’un tiers dispose :

- d’un accès comparable aux modèles ;
- de conditions d’exécution similaires ;
- du protocole public ;
- d’une capacité suffisante de comparaison comportementale.

Ce risque résiduel est documenté.

---

## 14. Frontière entre données publiques et données privées

### Données publiques

Les publications peuvent notamment contenir :

- des agrégats par profil ;
- des agrégats par question ;
- des distributions de régimes ;
- des niveaux de couverture ;
- des visualisations ;
- des métadonnées de campagne ;
- des exclusions et limites d’interprétation.

### Données privées

Le registre privé peut notamment contenir :

- les réponses individuelles ;
- les traces d’exécution ;
- les identités réelles des systèmes ;
- les détails de routage ;
- les horodatages précis ;
- les prompts techniques complets ;
- les données de coût ;
- les diagnostics du pipeline ;
- les notes de revue ;
- les résultats intermédiaires ;
- les artefacts nécessaires à une investigation technique.

Cette séparation permet de rendre les résultats publics inspectables sans exposer les informations nécessaires à l’exploitation ou à la réidentification directe des systèmes.

---

## 15. Livrables hebdomadaires

Chaque campagne peut produire plusieurs catégories de livrables.

### Livrables privés

- fichiers d’exécution ;
- fichiers de scoring ;
- fichiers de validation ;
- manifeste de campagne ;
- journal des erreurs et exclusions ;
- agrégats internes ;
- analyses longitudinales ;
- registre privé de mapping ;
- archives versionnées.

### Livrables publics

- données agrégées désidentifiées ;
- indicateurs principaux ;
- distributions par question ou profil ;
- couverture de la campagne ;
- limites d’interprétation ;
- visualisations ;
- article ou note éditoriale ;
- manifeste public.

---

## 16. Limites méthodologiques

Le Baromètre repose sur un ensemble limité de questions fixes.

Il ne représente pas l’ensemble des usages possibles d’un système d’IA.

Les résultats sont conditionnés par :

- les prompts sélectionnés ;
- les paramètres d’exécution ;
- les modèles disponibles au moment de la campagne ;
- les politiques des fournisseurs ;
- les mécanismes de routage ;
- la disponibilité des API ;
- les métriques utilisées ;
- les méthodes de scoring ;
- les conditions d’infrastructure.

Les observations ne doivent donc pas être généralisées au-delà du périmètre mesuré sans validation complémentaire.

---

## 17. Ce que le Baromètre n’est pas

Le NeoMundi Weekly Barometer n’est pas :

- un classement de fournisseurs ;
- un leaderboard de modèles ;
- une certification de sécurité ;
- une garantie de vérité ;
- une évaluation exhaustive de la qualité ;
- une décision réglementaire ;
- une preuve automatique de conformité ;
- une autorisation de déploiement ;
- un substitut à la supervision humaine ;
- un substitut à une évaluation métier spécifique.

Il constitue un instrument public d’observation métrologique du comportement runtime des systèmes d’IA dans le temps.

---

## 18. Doctrine scientifique

Le protocole repose sur six principes :

1. **Mesurer avant d’interpréter.**
2. **Répéter avant de généraliser.**
3. **Caractériser la variation avant de déclarer une dérive.**
4. **Ne jamais confondre stabilité et vérité.**
5. **Distinguer l’observation, l’interprétation et l’attribution causale.**
6. **Considérer chaque signal comme un élément de preuve, et non comme un verdict.**

---

## 19. Positionnement public

> Les benchmarks photographient les systèmes d’IA à un instant donné.  
> NeoMundi observe leurs trajectoires.
>
> Chaque semaine, le Baromètre suit plusieurs signaux de leur comportement runtime dans des conditions répétées et contrôlées.
>
> L’objectif n’est pas de produire un classement supplémentaire.
>
> Il est de rendre visibles les variations et les changements silencieux qui apparaissent dans le temps.

---

## 20. Statut du protocole

Le Baromètre Hebdomadaire NeoMundi est un protocole actif.

Sa Baseline Publique V1 est constituée de 14 400 observations finalisées.

Les campagnes hebdomadaires reposent sur 4 800 exécutions planifiées et forment progressivement une série longitudinale publique.

Le protocole, les métriques et les formats de publication pourront évoluer.

Toute évolution significative devra être :

- versionnée ;
- documentée ;
- distinguée des campagnes antérieures ;
- accompagnée de ses limites de comparabilité.

Le Baromètre vise à construire une infrastructure durable permettant d’observer ce que les évaluations ponctuelles ne rendent pas visible :

> l’évolution du comportement des systèmes d’IA dans le temps.
