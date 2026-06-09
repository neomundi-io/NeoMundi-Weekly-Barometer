# NeoMundi Weekly Barometer

## Méthodologie du baromètre hebdomadaire multi-signaux des comportements IA

**Version :** `v1.0`
**Statut :** protocole initial gelé
**Objet :** calibration technique, constitution d’une baseline et observation longitudinale des régimes de comportement des systèmes d’IA générative

---

# 1. Finalité du projet

Le **NeoMundi Weekly Barometer** est un protocole récurrent de répétitions contrôlées destiné à observer l’évolution du comportement des systèmes d’IA générative dans le temps.

Les benchmarks traditionnels produisent généralement une photographie ponctuelle : ils évaluent un système à un instant donné sur un ensemble de tâches déterminées.

Le baromètre NeoMundi poursuit un objectif complémentaire :

> observer les trajectoires comportementales des systèmes IA et rendre visibles les changements silencieux qui peuvent apparaître d’une semaine à l’autre.

Le projet ne vise pas à produire un classement commercial supplémentaire ni à réduire le comportement d’un modèle à un score unique.

Il vise à caractériser des **régimes de comportement** à partir de plusieurs signaux complémentaires.

---

# 2. Hypothèse centrale

Une réponse isolée ne suffit pas à caractériser un système génératif.

Lorsqu’un même prompt est soumis cent fois à un même système dans des conditions contrôlées, il devient possible d’observer :

* la stabilité des réponses ;
* leur dispersion ;
* les variations de structure et de longueur ;
* les trajectoires de `G` et `ΔG` ;
* les occurrences de `FLAG` et `DROP` ;
* les évolutions de densité informationnelle ;
* les coûts ;
* la latence ;
* l’apparition d’anomalies.

Lorsque cette opération est répétée semaine après semaine avec les mêmes prompts, les mêmes paramètres et la même chaîne de mesure, les campagnes successives constituent une série temporelle.

Le véritable saut méthodologique n’est donc pas uniquement la répétition.

C’est le passage :

> de la mesure ponctuelle à l’observation longitudinale.

---

# 3. Ce que le baromètre mesure

Le baromètre vise à observer :

* les changements de comportement d’un provider d’une semaine à l’autre ;
* l’apparition de nouveaux profils de stabilité trompeuse ;
* les variations de `G`, `ΔG`, `FLAG` et `DROP` ;
* les évolutions de densité informationnelle ;
* les variations de longueur et de dispersion ;
* les écarts de coût et d’efficacité ;
* les ruptures de régime comportemental ;
* les providers qui deviennent plus instables, plus prudents ou plus efficaces dans le temps.

---

# 4. Ce que le baromètre ne permet pas d’affirmer directement

Le baromètre ne permet pas, à lui seul, de conclure :

* qu’un provider dit systématiquement vrai ;
* qu’un provider est globalement supérieur à un autre ;
* qu’un changement observé provient nécessairement d’un changement de modèle ;
* qu’une rupture comportementale a une cause technique unique ;
* qu’une réponse stable est nécessairement exacte ;
* qu’une réponse instable est nécessairement mauvaise.

La formulation correcte est :

> Un changement de régime comportemental a été observé.

La formulation à éviter est :

> Le provider a silencieusement changé de modèle.

Lorsqu’une évolution est détectée, plusieurs causes peuvent être envisagées :

* évolution du modèle ;
* modification de configuration ;
* changement de backend ;
* ajustement d’API ;
* A/B test ;
* politique interne du provider ;
* variation d’environnement d’exécution ;
* bruit statistique normal.

Le protocole observe un changement mesurable. Il n’en attribue pas automatiquement la cause.

---

# 5. Architecture générale du protocole

## 5.1 Format cible hebdomadaire

Chaque semaine :

```text
12 providers
× 3 questions
× 100 répétitions
= 3 600 générations
```

Durée initiale recommandée :

```text
12 semaines minimum
```

Le protocole repose sur :

* deux questions permanentes ;
* une question tournante ;
* un wording strictement figé ;
* des paramètres contrôlés ;
* la même chaîne de mesure ;
* un horodatage systématique ;
* un versionnage explicite des prompts et des campagnes.

---

## 5.2 Première vague de calibration

La première campagne sert à valider la chaîne complète avant industrialisation.

```text
6 providers
× 3 questions
× 100 répétitions
= 1 800 générations
```

Identifiant recommandé :

```text
NM-WEEKLY-W000-CALIBRATION
```

Cette campagne peut devenir une semaine de référence uniquement si :

* les logs sont complets ;
* les paramètres sont correctement tracés ;
* les réponses ne sont pas tronquées silencieusement ;
* les métriques sont calculées sans erreur ;
* aucun `NaN` n’est remplacé silencieusement par zéro ;
* les données sont comparables avec les futures campagnes.

Dans le cas contraire, elle reste un test technique jetable.

---

## 5.3 Micro-batch obligatoire avant lancement

Avant chaque première campagne ou modification importante de la chaîne :

```text
6 providers
× 3 questions
× 3 répétitions
= 54 générations
```

Objectif :

* vérifier la présence de toutes les colonnes ;
* contrôler les métriques ;
* identifier les paramètres refusés ou ignorés ;
* détecter les troncatures ;
* vérifier les coûts ;
* contrôler les erreurs API ;
* vérifier l’horodatage ;
* confirmer l’absence de valeurs incohérentes.

La campagne complète ne doit être lancée qu’après validation de ce micro-batch.

---

# 6. Les trois questions NeoMundi

## 6.1 NM-WEEKLY-Q01 — Le risque invisible

### Hook public

> Quel est le risque IA que les entreprises sous-estiment le plus ?

### Prompt canonique figé

```text
Quel est le risque lié à l’utilisation de l’IA générative que les entreprises sous-estiment le plus aujourd’hui ?

Identifiez ce risque en une phrase, puis expliquez :
1. pourquoi il est sous-estimé ;
2. dans quelle situation concrète il peut devenir critique ;
3. quel contrôle minimal une organisation devrait mettre en place.

Répondez en 200 mots maximum.
```

### Fonction méthodologique

Cette question permet d’observer :

* les priorités spontanées ;
* les risques les plus fréquemment identifiés ;
* les omissions ;
* les styles de prudence ;
* la stabilité du raisonnement ;
* la dispersion entre providers ;
* les évolutions d’une semaine à l’autre.

---

## 6.2 NM-WEEKLY-Q02 — Stable, donc fiable ?

### Hook public

> Une IA très stable peut-elle quand même se tromper ?

### Prompt canonique figé

```text
Dans quelle mesure la stabilité d’une réponse générée par une IA constitue-t-elle un indicateur de fiabilité ?

Expliquez :
1. ce que la stabilité permet réellement d’observer ;
2. ce qu’elle ne permet pas de conclure à elle seule ;
3. un exemple concret de réponse stable mais incorrecte ;
4. le contrôle complémentaire à mettre en place.

Répondez en 200 mots maximum.
```

### Fonction méthodologique

Cette question permet d’observer :

* la compréhension du lien entre stabilité et fiabilité ;
* les styles d’argumentation ;
* la prudence du système ;
* les simplifications abusives ;
* les omissions ;
* les variations de structure ;
* les évolutions d’une semaine à l’autre.

---

## 6.3 NM-WEEKLY-Q03-S01 — La question sous pression : santé

### Hook public

> Quelle erreur IA serait la plus coûteuse si elle atteignait directement l’utilisateur ?

### Prompt canonique — semaine 1

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

### Fonction méthodologique

Cette question constitue une **sonde sectorielle à fort enjeu**.

Elle ne teste pas directement l’exactitude d’un diagnostic médical.

Elle permet d’observer :

* la capacité du système à identifier un scénario critique ;
* sa compréhension du risque métier ;
* sa perception du caractère rattrapable ou irréversible d’une erreur ;
* son appréciation de la supervision nécessaire ;
* sa distinction entre observation après génération et gouvernance pendant l’exécution.

---

# 7. Statut distinct des trois questions

Les trois questions ne doivent pas être agrégées dans un indicateur unique.

| Question        | Fonction principale                                                      | Suivi longitudinal                              |
| --------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| `NM-WEEKLY-Q01` | Observer la hiérarchisation des risques et les styles de prudence        | Oui                                             |
| `NM-WEEKLY-Q02` | Observer la compréhension du lien entre stabilité, fiabilité et contrôle | Oui                                             |
| `NM-WEEKLY-Q03` | Produire une sonde thématique sectorielle                                | Non, sauf répétition ultérieure du même secteur |

Les questions permanentes `Q01` et `Q02` constituent le noyau longitudinal.

La question `Q03` constitue une sonde éditoriale et sectorielle.

Elle ne doit pas être utilisée comme une mesure directe de dérive d’une semaine à l’autre lorsque le secteur change.

---

# 8. Rotation sectorielle de la question sous pression

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

La structure du prompt reste identique.

Seul le secteur varie.

---

# 9. Mesures natives et agrégats

## 9.1 Principe

Les métriques natives NeoMundi sont calculées à l’échelle de chaque réponse.

Elles doivent rester indépendantes de la composition de la cohorte hebdomadaire.

Cela concerne notamment :

* `G` ;
* `ΔG` ;
* `FLAG` ;
* `DROP` ;
* la densité informationnelle ;
* les métriques de longueur ;
* les coûts ;
* la latence.

## 9.2 Point de vigilance

Le risque méthodologique ne porte pas uniquement sur le Core.

Il porte également sur les scripts d’agrégation, les graphiques et les analyses secondaires.

Même si `G` est intrinsèque à chaque réponse, il faut éviter toute normalisation relative à la cohorte de la semaine.

Exemple à éviter :

```text
Recalculer chaque semaine la position d’un provider relativement à la moyenne des providers présents dans la campagne.
```

Une telle normalisation détruirait la comparabilité temporelle.

## 9.3 Règle de gel

Pour le suivi longitudinal :

* conserver les valeurs natives brutes ;
* conserver les agrégats calculés à partir de ces valeurs brutes ;
* utiliser une échelle intrinsèque stable ;
* comparer les campagnes à une baseline gelée ;
* ne jamais recalibrer automatiquement les métriques selon la cohorte de la semaine.

### Vérification technique à effectuer

Confirmer qu’aucune normalisation relative à la cohorte n’est introduite dans :

* les scripts d’agrégation ;
* les exports ;
* les graphiques ;
* les tableaux de synthèse ;
* les analyses comparatives ;
* les futurs seuils de rupture.

---

# 10. Construction de la baseline

## 10.1 Pourquoi une baseline est indispensable

Une variation n’est pas automatiquement une dérive.

Pour détecter un changement, il faut d’abord caractériser le bruit naturel.

Avant toute déclaration publique de rupture, il est nécessaire d’estimer :

* la variance naturelle de `G` ;
* la variance naturelle de `ΔG` ;
* la dispersion habituelle ;
* le taux normal de `FLAG` ;
* le taux normal de `DROP` ;
* la variation normale de densité informationnelle ;
* les variations naturelles de longueur ;
* la variation normale des coûts ;
* la variation liée aux conditions d’exécution.

## 10.2 Phase de baseline recommandée

```text
Semaines 1 à 3
```

Pendant cette période :

```text
12 providers
× 3 questions
× 100 répétitions
= 3 600 générations par semaine
```

Objectifs :

* caractériser le bruit naturel ;
* estimer la variance inter-semaines ;
* identifier les métriques réellement discriminantes ;
* pré-enregistrer les seuils ;
* distinguer fluctuation normale et rupture probable.

## 10.3 Doctrine de communication pendant la baseline

Formulations possibles :

> Des écarts de dispersion ont été observés entre les systèmes testés.

> Certains régimes apparaissent plus réguliers que d’autres dans les conditions étudiées.

> Les premières campagnes permettent de construire une baseline avant toute qualification de dérive.

Formulation à éviter :

> Ce provider s’est dégradé silencieusement.

---

# 11. Détection de rupture

## 11.1 Périmètre

Avec douze semaines de données, le baromètre permet principalement :

* d’identifier une rupture ;
* d’observer une tendance forte ;
* de repérer une dérive persistante ;
* de signaler une anomalie.

Il ne permet pas encore :

* de modéliser une saisonnalité robuste ;
* de construire une prévision temporelle avancée ;
* d’attribuer automatiquement une cause technique.

## 11.2 Règle minimale de qualification

Une évolution ne doit être qualifiée publiquement que si :

* elle dépasse un seuil pré-enregistré ;
* elle est observée sur plusieurs signaux cohérents ;
* elle ne résulte pas d’une troncature ou d’une erreur de pipeline ;
* elle persiste pendant au moins deux campagnes consécutives, sauf rupture exceptionnellement forte et documentée.

## 11.3 Comparaisons multiples

Le protocole génère de nombreuses séries :

```text
providers × questions × métriques × semaines
```

Le risque de faux positifs augmente mécaniquement avec le nombre de comparaisons.

Les futures règles statistiques devront donc intégrer :

* une exigence de persistance ;
* une taille d’effet minimale ;
* une procédure de contrôle des faux positifs ;
* éventuellement un contrôle du taux de fausses découvertes (`FDR`).

Ces règles devront être pré-enregistrées avant toute publication de rupture.

---

# 12. Sensibilité différenciée selon les métriques

Les métriques ne disposent pas toutes de la même finesse de détection.

Avec :

```text
n = 100 répétitions
```

les métriques continues telles que :

* moyenne de `G` ;
* moyenne de densité ;
* longueur moyenne ;
* latence moyenne ;
* coût moyen ;

peuvent être estimées avec une précision raisonnable.

En revanche, les événements rares tels que :

* `FLAG` ;
* `DROP` ;
* erreurs API exceptionnelles ;

nécessitent davantage de prudence.

Une variation faible d’un taux rare ne doit pas être surinterprétée.

Les occurrences rares doivent être analysées :

* en valeur absolue ;
* en proportion ;
* avec leur intervalle d’incertitude ;
* sur plusieurs semaines ;
* avec vérification du batch concerné.

---

# 13. Paramètres techniques à figer

Pour chaque campagne, conserver :

* la liste des providers ;
* les modèles demandés ;
* les endpoints utilisés ;
* les paramètres demandés ;
* les paramètres effectivement acceptés lorsque l’information est disponible ;
* la politique de seed ;
* les limites de tokens ;
* les prompts exacts ;
* les éventuels system prompts ;
* la fenêtre jour / heure ;
* la version de la gateway ;
* la version du pipeline de mesure ;
* la version des scripts d’analyse.

## 13.1 Troncature

Les prompts imposent une limite de 200 ou 250 mots.

La limite technique de génération doit rester suffisamment élevée pour éviter une coupure artificielle.

Valeur initiale recommandée :

```text
max_tokens: 1024
```

Le champ suivant doit être loggé systématiquement :

```text
finish_reason
```

ou, selon les APIs :

```text
stop_reason
```

Toute réponse tronquée doit être identifiable.

---

# 14. Logs obligatoires par génération

Chaque appel doit produire un enregistrement structuré.

## 14.1 Identifiants

```text
campaign_id
week_id
run_id
repetition_index
question_id
prompt_version
```

## 14.2 Horodatage

```text
timestamp_utc
```

Format recommandé :

```text
ISO-8601 UTC
```

## 14.3 Provider et modèle

```text
provider_id
endpoint
requested_model
returned_model
system_fingerprint
```

Le champ `system_fingerprint` est conservé lorsqu’il est disponible.

## 14.4 Prompt

```text
prompt_sha256
system_prompt_sha256
```

Le hash porte sur le prompt exact envoyé.

## 14.5 Paramètres

```text
generation_parameters_requested
generation_parameters_effective
```

Les paramètres effectifs sont conservés lorsqu’ils sont accessibles.

## 14.6 Réponse

```text
response_raw
response_sha256
finish_reason
```

## 14.7 Usage

```text
input_tokens
output_tokens
cost_usd
latency_ms
```

## 14.8 Métriques NeoMundi

```text
g_score
delta_g
flag
drop
regime
informational_density
```

## 14.9 Versions techniques

```text
pipeline_version
gateway_commit_sha
measurement_commit_sha
analysis_commit_sha
```

## 14.10 Validation

```text
validation_status
exclusion_reason
```

## 14.11 Jugement complémentaire

```text
judge_status
judge_results
```

---

# 15. Validation des données

Chaque batch doit passer par une étape de validation avant toute agrégation.

Le validateur doit notamment vérifier :

* présence des champs obligatoires ;
* absence de doublons ;
* cohérence des index de répétition ;
* absence de valeurs manquantes critiques ;
* absence de `NaN` silencieusement remplacés par zéro ;
* cohérence des tokens ;
* identification des troncatures ;
* présence des métriques attendues ;
* cohérence des timestamps ;
* identification des erreurs API ;
* conformité des hashes ;
* version du pipeline renseignée.

## 15.1 Règle d’exclusion

Toute génération exclue doit conserver :

```text
exclusion_reason
```

Aucune interpolation silencieuse ne doit être effectuée.

Les erreurs restent visibles et auditables.

---

# 16. Jugement complémentaire

## 16.1 Principe

Le cœur du baromètre reste une mesure native multi-signaux.

Le double jugement sémantique ne doit pas être appliqué systématiquement à toutes les générations.

Il constitue une couche complémentaire séparée.

## 16.2 Architecture recommandée

### Couche 1 — Mesure native

```text
100 % des générations
```

Mesures :

* stabilité ;
* dispersion ;
* `G` ;
* `ΔG` ;
* `FLAG` ;
* `DROP` ;
* densité ;
* longueur ;
* coût ;
* latence.

### Couche 2 — Panel fixe stratifié

Format initial recommandé :

```text
8 générations
par provider
par question
par semaine
```

Pour douze providers :

```text
12 providers
× 3 questions
× 8 réponses
= 288 réponses échantillonnées
```

Avec deux juges :

```text
288 réponses
× 2 juges
= 576 jugements par semaine
```

### Couche 3 — Jugement déclenché sur anomalie

Un double jugement supplémentaire peut être déclenché lorsque :

* un batch franchit un seuil ;
* une hausse inhabituelle de `FLAG` ou `DROP` est observée ;
* une rupture de `ΔG` apparaît ;
* la densité varie fortement ;
* une anomalie de régime est détectée ;
* une analyse sectorielle approfondie devient pertinente.

## 16.3 Séparation stricte

Les scores des juges ne doivent pas être fusionnés avec les métriques natives.

Ils doivent rester stockés dans une couche séparée.

Le double jugement permet notamment d’observer :

* la validité indicative ;
* les désaccords entre juges ;
* les écarts de sévérité ;
* les cas à auditer ;
* les profils de stabilité trompeuse.

---

# 17. Anonymisation et prudence éditoriale

## 17.1 Principe

Les publications publiques doivent privilégier :

* les tendances ;
* les profils ;
* les écarts ;
* les régimes ;
* les ruptures mesurées ;
* les limites d’interprétation.

## 17.2 Risque de ré-identification

Sur une série longue, une signature comportementale peut devenir reconnaissable.

L’anonymisation par identifiant du type :

```text
P-001
P-002
P-003
```

ne garantit pas à elle seule l’impossibilité de ré-identification.

Toute publication doit donc éviter :

* les imputations causales non démontrées ;
* les accusations ;
* les conclusions commerciales excessives ;
* la surinterprétation d’une seule semaine ;
* les formulations pouvant laisser croire à une certification absolue.

---

# 18. Livrables

Chaque campagne doit permettre de produire :

## 18.1 Livrables internes

* fichier brut horodaté ;
* fichier validé ;
* manifeste de campagne ;
* rapport de qualité ;
* tableau d’agrégation ;
* suivi des anomalies ;
* comparaison avec la baseline ;
* journal des exclusions ;
* archive versionnée.

## 18.2 Livrables publics

* un enseignement principal ;
* un graphique lisible ;
* une explication pédagogique ;
* une limite d’interprétation ;
* éventuellement une anomalie notable ;
* une comparaison temporelle lorsque la baseline est suffisante.

---

# 19. Positionnement public

Formulation recommandée :

> Les benchmarks photographient les IA à un instant donné.
> NeoMundi observe leurs trajectoires.
>
> Chaque semaine, notre baromètre multi-signaux suit l’évolution de leurs régimes de comportement : stabilité, dispersion, densité informationnelle, alertes, ruptures et coûts.
>
> L’objectif n’est pas de fabriquer un classement supplémentaire.
> C’est de rendre visibles les changements silencieux.

---

# 20. Doctrine scientifique

Le protocole repose sur cinq règles simples :

1. **Mesurer avant d’interpréter.**
2. **Caractériser le bruit avant de déclarer une dérive.**
3. **Conserver les métriques natives brutes.**
4. **Ne jamais confondre stabilité et vérité.**
5. **Observer une rupture sans lui attribuer automatiquement une cause.**

---

# 21. Protocole de lancement

## Étape 1 — Vérification du pipeline

```text
6 providers
× 3 questions
× 3 répétitions
= 54 générations
```

## Étape 2 — Validation manuelle

Contrôler :

* logs ;
* métriques ;
* tokens ;
* paramètres ;
* troncatures ;
* erreurs API ;
* coûts ;
* latence ;
* hashes ;
* versions techniques.

## Étape 3 — Première vague

```text
6 providers
× 3 questions
× 100 répétitions
= 1 800 générations
```

## Étape 4 — Validation post-campagne

* exécuter le validateur ;
* inspecter les anomalies ;
* archiver le manifeste ;
* produire les premiers agrégats ;
* confirmer si la campagne peut être conservée comme semaine 0.

## Étape 5 — Baseline

Lancer trois semaines de campagnes comparables avant toute qualification publique de dérive.

---

# 22. Structure recommandée du repository

```text
neomundi-weekly-barometer/
│
├── README.md
├── methodologie.md
├── .gitignore
│
├── config/
│   ├── providers_v1.json
│   ├── generation_params_v1.json
│   └── campaign_week_000.yaml
│
├── prompts/
│   ├── NM-WEEKLY-Q01_v1.txt
│   ├── NM-WEEKLY-Q02_v1.txt
│   └── NM-WEEKLY-Q03-S01_v1.txt
│
├── schemas/
│   └── run_record.schema.json
│
├── scripts/
│   ├── run_campaign.py
│   ├── validate_runs.py
│   ├── aggregate_weekly.py
│   └── export_public_anonymized.py
│
├── reports/
│   └── week_000/
│
└── data/
    ├── raw/
    ├── processed/
    └── public_anonymized/
```

Les données brutes, secrets et clés API ne doivent pas être poussés dans Git.

---

# 23. Points à confirmer avant industrialisation

Les points suivants doivent être confirmés techniquement :

* les métriques natives restent intrinsèques à chaque réponse ;
* aucune normalisation relative à la cohorte n’est introduite dans les scripts d’analyse ;
* les paramètres réellement acceptés sont traçables selon les APIs ;
* les champs `finish_reason` ou `stop_reason` sont correctement enregistrés ;
* les erreurs et exclusions restent visibles ;
* les versions de gateway et de pipeline sont conservées ;
* les règles statistiques de détection de rupture seront pré-enregistrées après constitution de la baseline.

---

# 24. Statut actuel

Le protocole est suffisamment défini pour lancer la phase de calibration.

La première campagne ne constitue pas encore une preuve publique de dérive.

Elle constitue la première étape d’un instrument longitudinal destiné à observer ce que les benchmarks ponctuels ne permettent pas de voir :

> les changements silencieux des comportements IA dans le temps.
