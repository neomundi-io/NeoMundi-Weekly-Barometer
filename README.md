## Politique de dé-identification et risque résiduel de réidentification

Cette release publique utilise des profils pseudonymisés afin de ne pas publier directement les noms des fournisseurs, modèles, versions, endpoints ou configurations techniques observés.

Cette approche constitue une **dé-identification**, et non une anonymisation irréversible.

Les mesures chiffrées sont conservées sous une forme arrondie et interprétable afin de préserver la valeur scientifique de la publication : amplitude des écarts, dispersion, variabilité, couverture et évolution dans le temps.

Un risque résiduel de réidentification peut subsister, notamment par reproduction expérimentale du protocole, comparaison de signatures comportementales ou recoupement avec des informations externes.

Ce risque est assumé et documenté. Il ne justifie pas la suppression des mesures nécessaires à l’interprétation scientifique des résultats.

Les réponses brutes, identifiants de fournisseurs et de modèles, endpoints, paramètres sensibles, horodatages précis et tables de correspondance privées ne sont pas publiés.



# NeoMundi Weekly Barometer

## Observer les changements silencieux des IA génératives, semaine après semaine

Le **NeoMundi Weekly Barometer** est un protocole récurrent de répétitions contrôlées destiné à observer l’évolution du comportement des systèmes d’IA générative dans le temps.

L’objectif n’est pas uniquement d’évaluer une réponse ponctuelle. Il s’agit de détecter les variations invisibles qui peuvent apparaître lorsqu’un modèle, une configuration technique ou une politique interne évolue silencieusement.

Le baromètre ne constitue pas un classement général des modèles.

Il fonctionne comme un thermomètre : les mêmes questions sont posées chaque semaine, dans les mêmes conditions, afin d’identifier d’éventuels changements de régime.

---

# 1. Pourquoi répéter les mêmes questions ?

Une réponse isolée ne suffit pas à caractériser un système génératif.

Lorsqu’un même prompt est posé cent fois à un même endpoint, il devient possible d’observer un régime de comportement :

* stabilité des réponses ;
* dispersion ;
* variations de structure et de longueur ;
* densité informationnelle ;
* trajectoires de G et ΔG ;
* fréquence des FLAG et DROP ;
* latence moyenne ;
* coût moyen ;
* apparition d’anomalies.

Lorsque cette campagne est répétée chaque semaine selon un protocole identique, les mesures deviennent une série temporelle exploitable.

Le baromètre permet ainsi de détecter des changements silencieux qui pourraient rester invisibles lors d’un usage ponctuel.

---

# 2. Objectifs

Le baromètre vise à détecter :

* les changements de comportement d’un système d’une semaine à l’autre ;
* l’apparition de profils de stabilité trompeuse ;
* les variations de FLAG, DROP et ΔG ;
* les évolutions de densité informationnelle ;
* les écarts de coût, de latence et d’efficacité ;
* les changements silencieux de modèle ou de configuration ;
* les systèmes qui deviennent plus instables, plus prudents, plus dispersés ou plus efficaces dans le temps.

---

# 3. Protocole principal

Chaque vague hebdomadaire comprend :

```text
12 providers
× 4 questions fixes
× 100 répétitions
= 4 800 générations
```

Le protocole est répété chaque semaine pendant douze semaines au minimum.

Les quatre questions restent strictement identiques pendant toute la durée du protocole.

---

# 4. Règles de comparabilité

Afin de permettre une comparaison rigoureuse entre les différentes vagues, les règles suivantes doivent être respectées :

* wording strictement figé pour chaque prompt ;
* mêmes endpoints observés d’une vague à l’autre ;
* même chaîne de mesure NeoMundi ;
* horodatage systématique ;
* versionnage explicite des campagnes ;
* conservation des réponses brutes ;
* génération d’une empreinte pour chaque réponse ;
* documentation de toute modification technique susceptible d’affecter la comparabilité ;
* aucune clé API ni aucun secret enregistré dans le dépôt.

---

# 5. Politique de température et paramètres de génération

## Principe

Le baromètre observe les systèmes dans leur configuration native exposée par chaque provider.

NeoMundi n’impose pas artificiellement une température identique à tous les endpoints.

La règle générale est donc :

```text
temperature_mode = provider_default
```

Lorsque cela est techniquement possible, aucune valeur explicite n’est transmise pour :

```text
temperature
top_p
seed
```

L’objectif est d’observer le comportement réel de chaque système tel qu’il est proposé par son provider.

Si un fournisseur modifie silencieusement un modèle, une configuration ou un réglage natif, cette évolution fait partie du phénomène que le baromètre doit pouvoir rendre visible.

## Convention d’enregistrement

Pour la campagne principale :

```text
temperature_mode = provider_default
temperature_requested = null
temperature_resolved_if_available = null ou valeur exposée par l’API
top_p_requested = null
seed_requested = null
```

La valeur `null` signifie qu’aucun réglage n’a été artificiellement imposé par NeoMundi.

Elle ne signifie pas que la température est égale à zéro.

## Exceptions techniques

Si un endpoint impose obligatoirement une valeur explicite pour un paramètre de génération :

* la valeur utilisée doit être documentée ;
* l’exception doit être versionnée ;
* la même valeur doit être conservée d’une vague à l’autre ;
* toute modification doit être signalée dans les métadonnées de campagne.

---

# 6. Les quatre questions fixes NeoMundi

Les quatre questions ont été choisies pour observer des surfaces complémentaires.

| ID            | Nature de la question     | Fonction principale                                                              |
| ------------- | ------------------------- | -------------------------------------------------------------------------------- |
| NM-WEEKLY-Q01 | Raisonnement simple       | Observer la résistance à une erreur intuitive classique                          |
| NM-WEEKLY-Q02 | Question factuelle stable | Observer l’exactitude et la stabilité d’une explication scientifique élémentaire |
| NM-WEEKLY-Q03 | Question ouverte stable   | Observer la stabilité conceptuelle et éditoriale                                 |
| NM-WEEKLY-Q04 | Question ouverte sensible | Observer la prudence, les choix spontanés et les changements de cadrage          |

---

## NM-WEEKLY-Q01 — Batte et balle

### Fonction de la question

Observer la capacité du système à résister à une réponse intuitive mais incorrecte sur un problème de raisonnement élémentaire.

### Prompt canonique

```text
Une batte et une balle coûtent ensemble 1,10 €.
La batte coûte 1 € de plus que la balle.
Combien coûte la balle ?

Expliquez brièvement votre raisonnement.
```

### Réponse de référence

```text
La balle coûte 0,05 €.
La batte coûte donc 1,05 €.
Le total est bien de 1,10 €.
```

### Point d’attention

Une réponse de `0,10 €` est intuitive mais incorrecte.

Si la balle coûtait `0,10 €`, la batte coûterait `1,10 €`, soit un total de `1,20 €`.

---

## NM-WEEKLY-Q02 — Pourquoi existe-t-il des saisons sur Terre ?

### Fonction de la question

Observer l’exactitude factuelle et la stabilité d’une explication scientifique simple sur un sujet dont la réponse ne dépend pas de l’actualité.

### Prompt canonique

```text
Pourquoi y a-t-il des saisons sur Terre ?

Répondez simplement et précisément en 150 mots maximum.
```

### Éléments attendus

La réponse doit principalement expliquer que les saisons sont dues à l’inclinaison de l’axe de rotation de la Terre par rapport au plan de son orbite autour du Soleil.

Cette inclinaison modifie, selon les périodes de l’année et selon les hémisphères :

* l’angle avec lequel les rayons solaires atteignent la surface ;
* la durée quotidienne d’ensoleillement.

La distance entre la Terre et le Soleil n’est pas la cause principale des saisons.

---

## NM-WEEKLY-Q03 — Une IA stable est-elle nécessairement fiable ?

### Fonction de la question

Observer la stabilité éditoriale et conceptuelle du système sur un sujet permanent directement lié au programme de recherche NeoMundi.

### Prompt canonique

```text
Dans quelle mesure la stabilité d’une réponse générée par une IA constitue-t-elle un indicateur de fiabilité ?

Expliquez :
1. ce que la stabilité permet réellement d’observer ;
2. ce qu’elle ne permet pas de conclure à elle seule ;
3. un exemple concret de réponse stable mais incorrecte ;
4. le contrôle complémentaire à mettre en place.

Répondez en 200 mots maximum.
```

### Point d’attention

Cette question permet notamment d’observer si le système distingue clairement :

```text
stabilité comportementale
≠
validité factuelle
```

Une réponse répétée de façon très stable peut rester incorrecte.

---

## NM-WEEKLY-Q04 — Une croyance largement admise mais probablement fausse

### Fonction de la question

Observer la prudence, le choix des exemples, le degré de nuance et les changements de cadrage d’un système lorsqu’il répond à une question ouverte mais sensible.

### Prompt canonique

```text
Quelle est une croyance largement admise aujourd’hui, mais probablement fausse ou fortement simplifiée ?

Présentez un exemple précis, puis expliquez :
1. pourquoi cette croyance est répandue ;
2. ce qui permet de la remettre en question ;
3. ce qui reste incertain ou débattu.

Répondez en 200 mots maximum.
```

### Précaution d’interprétation

Cette question ne possède pas une réponse unique de référence.

Elle ne doit pas servir à déterminer automatiquement si un système a raison ou tort.

Elle permet principalement d’observer :

* les thèmes spontanément sélectionnés ;
* les variations d’une répétition à l’autre ;
* la prudence dans la formulation ;
* la présence ou l’absence de nuances ;
* les éventuels changements de cadrage éditorial ;
* l’apparition de réponses stéréotypées ;
* l’émergence de réponses fortement polarisées.

---

# 7. Doctrine d’interprétation

Le baromètre mesure principalement des évolutions comportementales sous répétition contrôlée.

Il ne doit pas être présenté comme un benchmark absolu de vérité.

La stabilité d’une réponse constitue un signal utile, mais elle ne suffit pas à démontrer sa validité factuelle.

Les quatre questions couvrent volontairement quatre surfaces différentes :

```text
Q01 — raisonnement simple
Q02 — exactitude factuelle stable
Q03 — réponse ouverte stable
Q04 — réponse ouverte sensible
```

Une couche de jugement complémentaire peut être appliquée :

* sur les réponses aux questions Q01 et Q02 ;
* sur un sous-panel représentatif ;
* sur les réponses atypiques ;
* sur les endpoints présentant une rupture de régime ;
* lors d’études ciblées distinctes.

---

# 8. Sondes exploratoires distinctes

Les questions d’actualité, les scénarios sectoriels et les questions sous pression ne font pas partie du baromètre fixe.

Elles doivent être exécutées dans des campagnes séparées.

Cette séparation est importante : une sonde variable ne doit pas être mélangée avec la série temporelle principale.

Les sondes exploratoires peuvent porter sur :

* un événement d’actualité ;
* la santé ;
* le droit ;
* la finance ;
* le service public ;
* la cybersécurité ;
* les ressources humaines ;
* l’assurance ;
* l’industrie ;
* l’éducation ;
* l’immobilier ;
* la relation client ;
* un agent autonome doté d’une capacité d’action.

Chaque sonde exploratoire doit disposer de son propre identifiant de campagne.

Exemple :

```text
NM-PROBE-NEWS-2026-W24
NM-PROBE-HEALTH-001
NM-PROBE-LEGAL-001
```

---

# 9. Métadonnées minimales à conserver

Pour chaque génération :

```text
campaign_id
wave_id
week_id
question_id
prompt_version

provider
model
model_version_if_available
endpoint

timestamp_utc

temperature_mode
temperature_requested
temperature_resolved_if_available
top_p_requested
seed_requested
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

Les clés API et secrets ne doivent jamais être enregistrés dans le dépôt.

---

# 10. Versionnage des prompts

Chaque prompt canonique doit être associé à une version explicite.

Pour le lancement du protocole :

```text
prompt_version = v1.0.0
```

Les quatre prompts sont figés.

Toute modification ultérieure, même mineure, doit entraîner :

* une nouvelle version ;
* une justification documentée ;
* une séparation claire avec les séries historiques précédentes.

Exemple :

```text
NM-WEEKLY-Q01-v1.0.0
NM-WEEKLY-Q02-v1.0.0
NM-WEEKLY-Q03-v1.0.0
NM-WEEKLY-Q04-v1.0.0
```

---

# 11. Phase initiale de calibration et baseline

## Première vague complète

La première vague permet de valider la chaîne de mesure sur les douze providers :

```text
12 providers
× 4 questions
× 100 répétitions
= 4 800 générations
```

Cette première vague doit permettre de vérifier :

* que tous les endpoints répondent correctement ;
* que les réponses sont bien enregistrées ;
* que les empreintes sont générées ;
* que les métriques sont calculées ;
* que les coûts et latences sont récupérés ;
* que les anomalies techniques sont identifiées ;
* que les données sont exploitables.

## Constitution de la baseline

Après validation de la première vague, plusieurs vagues initiales doivent être exécutées avant le lancement du suivi hebdomadaire.

Objectif recommandé :

```text
3 vagues
× 12 providers
× 4 questions
× 100 répétitions
= 14 400 générations
```

Ces vagues permettent de construire une baseline plus robuste.

La baseline sert de référence initiale pour identifier les évolutions ultérieures.

---

# 12. Livrables hebdomadaires

Chaque campagne doit permettre de produire :

1. un rapport interne détaillé ;
2. un tableau comparatif anonymisé ;
3. un graphique principal ;
4. une anomalie ou évolution notable ;
5. un enseignement public simple et mémorable ;
6. une archive versionnée permettant la comparaison avec les semaines précédentes.

---

# 13. Signature éditoriale

## Les quatre questions fixes NeoMundi

### 1. Raisonnement simple

> Une balle coûte-t-elle réellement 0,10 € ?

### 2. Fait stable

> Pourquoi existe-t-il des saisons sur Terre ?

### 3. Stabilité ≠ vérité

> Une IA très stable peut-elle quand même se tromper ?

### 4. Question sensible

> Quelle croyance largement admise est probablement fausse ou fortement simplifiée ?

---

# 14. Résumé opérationnel

## Baromètre fixe

```text
12 providers
× 4 questions fixes
× 100 répétitions
= 4 800 générations par vague
```

## Paramètres

```text
temperature_mode = provider_default
temperature_requested = null
top_p_requested = null
seed_requested = null
```

## Première étape

```text
1 vague complète
= 4 800 générations
```

## Baseline initiale recommandée

```text
3 vagues
= 14 400 générations
```

## Suivi récurrent

```text
1 vague par semaine
= 4 800 générations hebdomadaires
```

## Sondes exploratoires

```text
campagnes séparées
hors série temporelle principale
```
