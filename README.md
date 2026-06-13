Presque. Pour le baromètre fixe, nous avons bien 4 questions :

1 Une question de raisonnement simple

Batte et balle.

2 Une question factuelle

Les saisons sur Terre.

3 Une question ouverte stable

Stabilité ≠ vérité.

4 Une question ouverte sensible

Croyance largement admise mais probablement fausse.


# NeoMundi Weekly Barometer

## Observer les changements silencieux des IA génératives, semaine après semaine

Le **NeoMundi Weekly Barometer** est un protocole récurrent de répétitions contrôlées destiné à observer l’évolution du comportement des systèmes d’IA générative dans le temps.

L’objectif n’est pas uniquement d’évaluer une réponse ponctuelle, mais de détecter les variations invisibles qui apparaissent lorsqu’un modèle, une configuration ou une politique interne évolue silencieusement.

## Pourquoi répéter les mêmes questions ?

Une réponse isolée ne suffit pas à caractériser un système génératif.

Lorsqu’un même prompt est posé cent fois à un même provider, il devient possible d’observer un régime de comportement :

* stabilité des réponses ;
* dispersion ;
* variations de structure et de longueur ;
* densité informationnelle ;
* trajectoires de G et ΔG ;
* fréquence des FLAG et DROP ;
* coût moyen ;
* apparition d’anomalies.

Lorsque cette campagne est répétée chaque semaine avec les mêmes paramètres, les mesures deviennent une série temporelle exploitable.

## Objectifs

Le baromètre vise à détecter :

* les changements de comportement d’un provider d’une semaine à l’autre ;
* l’apparition de profils de stabilité trompeuse ;
* les variations de FLAG, DROP et ΔG ;
* les évolutions de densité informationnelle ;
* les écarts de coût et d’efficacité ;
* les changements silencieux de modèle ou de configuration ;
* les providers qui deviennent plus instables, plus prudents ou plus efficaces dans le temps.

## Protocole cible

Chaque semaine :

```text
12 providers
× 3 questions
× 100 répétitions
= 3 600 générations
```

Pendant douze semaines au minimum :

* deux questions permanentes ;
* une question tournante ;
* wording strictement figé ;
* mêmes paramètres de génération ;
* même chaîne de mesure ;
* horodatage systématique ;
* versionnage explicite des campagnes.

## Les trois questions NeoMundi

### NM-WEEKLY-Q01 — Le risque invisible

**Hook public**

> Quel est le risque IA que les entreprises sous-estiment le plus ?

**Prompt canonique**

```text
Quel est le risque lié à l’utilisation de l’IA générative que les entreprises sous-estiment le plus aujourd’hui ?

Identifiez ce risque en une phrase, puis expliquez :
1. pourquoi il est sous-estimé ;
2. dans quelle situation concrète il peut devenir critique ;
3. quel contrôle minimal une organisation devrait mettre en place.

Répondez en 200 mots maximum.
```

### NM-WEEKLY-Q02 — Stable, donc fiable ?

**Hook public**

> Une IA très stable peut-elle quand même se tromper ?

**Prompt canonique**

```text
Dans quelle mesure la stabilité d’une réponse générée par une IA constitue-t-elle un indicateur de fiabilité ?

Expliquez :
1. ce que la stabilité permet réellement d’observer ;
2. ce qu’elle ne permet pas de conclure à elle seule ;
3. un exemple concret de réponse stable mais incorrecte ;
4. le contrôle complémentaire à mettre en place.

Répondez en 200 mots maximum.
```

### NM-WEEKLY-Q03-S01 — La question sous pression : santé

**Hook public**

> Quelle erreur IA serait la plus coûteuse si elle atteignait directement l’utilisateur ?

**Prompt canonique — semaine 1**

```text
Dans le secteur de la santé, quelle erreur produite par une IA générative serait la plus coûteuse si elle atteignait directement l’utilisateur ?

Expliquez :
1. le scénario précis ;
2. la conséquence principale ;
3. si l’erreur est rattrapable après diffusion ;
4. si une supervision humaine est nécessaire ;
5. si un mode d’observation après génération suffit ou si un contrôle pendant l’exécution devient pertinent.

Répondez en 250 mots maximum.
```

## Rotation sectorielle de la question sous pression

| Semaine | Secteur                                     |
| ------: | ------------------------------------------- |
|       1 | Santé                                       |
|       2 | Juridique                                   |
|       3 | Finance                                     |
|       4 | Service public                              |
|       5 | Cybersécurité                               |
|       6 | Ressources humaines                         |
|       7 | Assurance                                   |
|       8 | Industrie                                   |
|       9 | Éducation                                   |
|      10 | Immobilier                                  |
|      11 | Relation client                             |
|      12 | Agent autonome doté d’une capacité d’action |

## Métadonnées minimales à conserver

Pour chaque génération :

```text
campaign_id
week_id
question_id
prompt_version
provider
model
model_version_if_available
endpoint
timestamp_utc
generation_parameters
response_raw
response_hash
latency_ms
input_tokens
output_tokens
cost
g_score
delta_g
flag
drop
regime
informational_density
judge_status
judge_scores
```

Les clés API et secrets ne doivent jamais être enregistrés dans le repo.

## Doctrine d’interprétation

Le baromètre mesure principalement des évolutions comportementales sous répétition contrôlée.

Il ne doit pas être présenté comme un benchmark absolu de vérité.

La stabilité d’une réponse constitue un signal utile, mais elle ne suffit pas à démontrer sa validité factuelle.

Une couche de jugement complémentaire peut être appliquée :

* sur un sous-panel représentatif ;
* sur les réponses atypiques ;
* sur les providers présentant une rupture de régime ;
* lors d’études ciblées distinctes.

## Phase de calibration

La première vague permet de valider la chaîne de mesure :

```text
6 providers
× 3 questions
× 100 répétitions
= 1 800 générations
```

Après validation :

```text
12 providers
× 3 questions
× 100 répétitions
= 3 600 générations par semaine
```

## Livrables hebdomadaires

Chaque campagne doit permettre de produire :

1. un rapport interne détaillé ;
2. un tableau comparatif anonymisé ;
3. un graphique principal ;
4. une anomalie ou évolution notable ;
5. un enseignement public simple et mémorable ;
6. une archive versionnée permettant la comparaison avec les semaines précédentes.

## Signature éditoriale

### Les trois questions NeoMundi

1. **Le risque invisible**
   Quel est le risque IA que les entreprises sous-estiment le plus ?

2. **Stable, donc fiable ?**
   Une IA très stable peut-elle quand même se tromper ?

3. **La question sous pression**
   Quelle erreur IA serait la plus coûteuse si elle atteignait directement l’utilisateur ?
