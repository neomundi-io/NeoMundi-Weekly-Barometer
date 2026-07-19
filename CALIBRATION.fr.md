# Baromètre Hebdomadaire NeoMundi

## Protocole de calibration

**Version :** `v1.0`  
**Statut :** document technique actif  
**Objet :** valider la chaîne de mesure avant une campagne publique ou toute modification significative du protocole

---

## 1. Finalité de la calibration

La calibration est une phase de validation technique réalisée avant :

- la première utilisation d’une chaîne de mesure ;
- l’intégration d’un nouveau fournisseur ou modèle ;
- une modification importante des prompts ou paramètres ;
- une évolution du pipeline de scoring ;
- une modification des scripts d’agrégation ou de publication ;
- toute évolution susceptible d’affecter la comparabilité longitudinale.

Son objectif est de confirmer que la chaîne de mesure produit des enregistrements complets, traçables et interprétables dans des conditions contrôlées.

Une calibration ne constitue pas, par défaut, une publication publique du Baromètre.

---

## 2. Relation avec le protocole actif

Le protocole actif du Baromètre Hebdomadaire NeoMundi est défini dans :

- `methodology.md` — version anglaise ;
- `methodologie.md` — version française.

Le format hebdomadaire actif est :

```text
12 profils d’IA désidentifiés
× 4 questions fixes
× 100 répétitions
= 4 800 exécutions planifiées
```

La Baseline Publique V1 constitue une campagne de référence élargie distincte :

```text
12 profils désidentifiés
× 4 questions
× 100 répétitions
× 3 vagues
= 14 400 observations finalisées
```

Le document de calibration ne doit pas introduire une description concurrente du protocole.

---

## 3. Architecture exploratoire historique

Une première architecture exploratoire envisageait :

- trois questions fixes ;
- une sonde sectorielle tournante ;
- une sonde légère d’actualité.

Cette architecture n’a pas été retenue comme protocole public hebdomadaire actif.

Elle peut rester pertinente comme future extension expérimentale, à condition d’être :

- explicitement versionnée ;
- documentée séparément ;
- distinguée du protocole hebdomadaire canonique à quatre questions ;
- analysée hors de la série longitudinale principale, sauf démonstration de comparabilité.

---

## 4. Objectifs de la calibration

Une calibration doit notamment vérifier :

- la présence de tous les champs requis ;
- le bon versionnage des prompts et paramètres ;
- la production du nombre d’exécutions attendu ;
- l’absence de troncature silencieuse ;
- la conservation et l’identification des erreurs API ;
- l’absence de conversion silencieuse des valeurs manquantes en zéro ;
- le calcul correct des métriques ;
- la cohérence des horodatages ;
- l’application correcte de la désidentification ;
- l’absence d’identifiants privés dans les exports publics ;
- la reproduction des totaux attendus par les scripts d’agrégation ;
- la cohérence interne des fichiers de publication.

---

## 5. Format recommandé

La taille exacte d’une calibration peut varier selon le changement testé.

Une calibration technique minimale doit rester suffisamment petite pour permettre une inspection manuelle, tout en couvrant chaque profil, question et branche de pipeline concernée.

Un format recommandé est :

```text
tous les profils concernés
× toutes les questions concernées
× 3 répétitions
```

Pour le protocole hebdomadaire actif, un micro-batch complet peut donc comprendre :

```text
12 profils
× 4 questions
× 3 répétitions
= 144 exécutions
```

Un sous-ensemble plus restreint peut être utilisé pour une modification technique ciblée, à condition que cette limitation soit documentée.

---

## 6. Contrôles obligatoires

### 6.1 Intégrité des exécutions

Vérifier :

- le nombre d’exécutions attendu ;
- l’unicité des index de répétition ;
- l’absence de doublons non documentés ;
- l’absence de cellule profil-question manquante ;
- la présence des identifiants de campagne ;
- la cohérence des horodatages.

### 6.2 Intégrité des prompts

Vérifier :

- le texte exact des prompts ;
- leur version ;
- leur hash, lorsqu’il est utilisé ;
- la version du system prompt, lorsqu’il existe ;
- l’absence de variation de formulation non documentée.

### 6.3 Intégrité fournisseur et runtime

Vérifier, lorsque ces informations sont disponibles :

- le modèle demandé ;
- le modèle retourné ;
- l’endpoint ;
- les paramètres acceptés ;
- `finish_reason` ou `stop_reason` ;
- l’usage des tokens ;
- la latence ;
- le coût ;
- les erreurs côté fournisseur.

### 6.4 Intégrité de la mesure

Vérifier :

- la présence des métriques attendues ;
- l’identification des échecs de scoring ;
- la distinction entre `not_scored` et un zéro mesuré ;
- le calcul correct de la couverture par métrique ;
- la documentation des dépendances entre métriques ;
- l’absence de normalisation relative à la cohorte introduite involontairement.

### 6.5 Intégrité de la publication

Vérifier :

- l’utilisation d’identifiants stables `PROFILE-XXXXXX` ;
- l’absence de noms de fournisseurs ou modèles dans les fichiers publics ;
- l’absence de réponses brutes dans les fichiers publics ;
- l’absence d’horodatages précis dans les fichiers publics ;
- la concordance entre totaux publics et totaux privés validés ;
- la documentation des exclusions et limites ;
- la complétude du manifeste et de l’inventaire des fichiers.

---

## 7. Critères d’acceptation

Une calibration peut être acceptée lorsque :

- l’ensemble attendu des exécutions est complet ou que tous les écarts sont documentés ;
- aucun champ critique de traçabilité ne manque ;
- les erreurs et exclusions restent visibles ;
- la couverture du scoring est comprise ;
- les agrégats publics reproduisent les totaux sources validés ;
- aucun identifiant privé n’apparaît dans les fichiers publics ;
- la modification ne rompt pas silencieusement la comparabilité longitudinale.

Lorsque ces conditions ne sont pas remplies, la calibration reste un test technique et ne doit pas être utilisée comme campagne publique de référence.

---

## 8. Registre de calibration

Chaque calibration doit conserver, au minimum :

```text
calibration_id
date_utc
scope
profiles_tested
questions_tested
repetitions
pipeline_version
analysis_version
change_under_test
expected_executions
completed_executions
coverage_rate
known_errors
acceptance_status
reviewer
```

États d’acceptation recommandés :

```text
ACCEPTED
ACCEPTED_WITH_LIMITATIONS
REJECTED
```

---

## 9. Modifications nécessitant une recalibration

Une recalibration est nécessaire lorsqu’une modification peut affecter :

- le comportement d’exécution ;
- la longueur ou la troncature des réponses ;
- l’interprétation d’un prompt ;
- le calcul des métriques ;
- la classification des régimes ;
- le mapping des profils ;
- les totaux d’agrégation ;
- la structure des exports publics ;
- la comparabilité longitudinale.

Exemples :

- ajout ou retrait d’un modèle ;
- modification des paramètres de génération ;
- modification d’une question fixe ;
- évolution de la logique de scoring ;
- mise à jour du pipeline d’agrégation ;
- modification des règles de désidentification ;
- évolution des schémas publics.

---

## 10. Limite d’interprétation

La calibration valide la fiabilité technique de la chaîne de mesure.

Elle ne permet pas de conclure :

- à la véracité d’un système ;
- à la sécurité d’un modèle ;
- à sa conformité réglementaire ;
- à son aptitude au déploiement ;
- à la supériorité d’un fournisseur.

La calibration confirme que l’instrument fonctionne comme prévu dans le périmètre testé.

> La calibration valide le processus de mesure. Elle ne valide pas le système d’IA lui-même.
