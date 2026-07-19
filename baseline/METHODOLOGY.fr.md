🌐 **Langue :** [Français](./METHODOLOGY.fr.md) · [English](./METHODOLOGY.md)

# Baromètre Hebdomadaire NeoMundi — Méthodologie de la Baseline V1

**Version :** `v1.1`  
**Statut :** méthodologie publique de la baseline  
**Périmètre :** campagne quantitative désidentifiée servant de premier cadre de comparaison du Baromètre Hebdomadaire NeoMundi

---

## 1. Finalité

La Baseline V1 établit le premier point de référence quantitatif public du **Baromètre Hebdomadaire NeoMundi**.

Elle vise à documenter le comportement runtime des systèmes d’IA dans des conditions d’observation répétées et contrôlées, avant le développement des comparaisons longitudinales hebdomadaires.

La baseline n’est ni un classement de fournisseurs, ni un leaderboard de modèles, ni une certification, ni une évaluation universelle de la qualité des IA.

Son objectif est de rendre les évolutions comportementales futures mesurables à partir d’une campagne de référence fixe.

---

## 2. Plan expérimental

La campagne comprend :

```text
12 profils d’IA désidentifiés
× 4 questions fixes
× 100 répétitions
× 3 vagues d’exécution
= 14 400 observations finalisées
```

Cela représente :

```text
1 200 observations par profil
```

Les mêmes quatre questions ont été utilisées pour tous les profils et toutes les vagues.

Les profils publics utilisent des identifiants opaques et stables au format :

```text
PROFILE-XXXXXX
```

La correspondance privée entre les profils publics et les systèmes observés est conservée séparément et n’est pas incluse dans ce dépôt.

---

## 3. Les quatre questions fixes

### `NM-WEEKLY-Q01` — Raisonnement

> Une batte et une balle coûtent 1,10 € au total.  
> La batte coûte 1 € de plus que la balle.  
> Combien coûte la balle ?

### `NM-WEEKLY-Q02` — Explication scientifique

> Pourquoi les saisons se produisent-elles sur Terre ?

### `NM-WEEKLY-Q03` — Question conceptuelle ouverte

> Pourquoi une réponse stable produite par une IA n’est-elle pas nécessairement factuellement correcte ?

### `NM-WEEKLY-Q04` — Question épistémique ouverte

> Donnez un exemple de croyance largement admise qui pourrait être fausse et expliquez comment elle pourrait être vérifiée.

Les quatre questions couvrent des conditions de réponse différentes et ne doivent pas être réduites à un indicateur universel unique.

---

## 4. Familles d’indicateurs publics

### 4.1 Stabilité

Répétabilité observée des réponses dans des conditions de mesure répétées et comparables.

La stabilité ne constitue pas une preuve d’exactitude factuelle.

### 4.2 Cohérence

Consistance logique ou structurelle observée des réponses générées.

La cohérence ne constitue pas une preuve de vérité.

### 4.3 Signal de risque factuel

Indication propre au protocole qu’une réponse peut nécessiter une vérification factuelle complémentaire.

Il ne s’agit pas d’un score universel de vérité. Ce signal doit être interprété en relation avec les questions, la méthode de scoring, la couverture et la fenêtre d’observation.

### 4.4 Instabilité sémantique

Variation observée du contenu sémantique ou du sens utile des réponses au travers d’exécutions répétées.

Une variation sémantique ne constitue pas, à elle seule, une preuve d’erreur factuelle.

### 4.5 Comportement décisionnel

Distribution observée des états :

```text
ALLOW
FLAG
ERROR
```

Ces états décrivent la sortie de la couche de mesure et de gouvernance pendant la campagne.

Ils ne constituent ni une certification de sécurité, ni une décision de conformité, ni une autorisation de déploiement.

### 4.6 Variabilité entre les vagues

Variation observée entre les trois vagues d’exécution.

Cet indicateur permet de comparer les répétitions de la campagne, mais ne doit pas être interprété comme une estimation de stabilité à long terme.

### 4.7 Plages de latence

La latence runtime est publiée sous forme de plages larges plutôt que sous forme de mesures exactes au niveau de l’infrastructure.

Cette approche préserve un contexte opérationnel utile tout en réduisant l’exposition au risque de réidentification.

### 4.8 `delta_g`

`delta_g` est publié comme un signal observable avancé de variation runtime.

Sa publication ne divulgue ni sa composition interne, ni ses seuils, ni sa logique de pondération, ni ses règles de calcul propriétaires.

Aucun indicateur individuel ne doit être interprété isolément comme une évaluation complète de la qualité, de la véracité, de la sécurité ou de la gouvernabilité.

---

## 5. Couverture et remédiation

La complétude des exécutions et la couverture propre à chaque métrique sont publiées séparément.

### Statut des exécutions

`complete` signifie que le nombre d’exécutions planifié a été atteint.

`remediated_complete` signifie que des observations planifiées manquantes ont été réexécutées dans la même configuration de mesure et que leur nombre est documenté.

`partial` signifie qu’un nombre inférieur d’observations était disponible.

### Statut des métriques

`not_scored` signifie qu’aucun score valide n’était disponible pour l’observation concernée.

Une valeur mesurée égale à `0.0` est distincte d’un score manquant ou indisponible.

La taille d’échantillon et la couverture propres à chaque métrique sont publiées séparément au moyen des champs `*_n`, `*_coverage_rate` et `*_coverage_status`.

Aucune valeur manquante n’est silencieusement convertie en zéro.

---

## 6. Contrôles de validation et d’intégrité

Avant publication, la release est contrôlée afin de vérifier :

- les totaux d’observations attendus ;
- la complétude des cellules profil-question-vague ;
- les enregistrements dupliqués ou manquants ;
- la couverture propre à chaque métrique ;
- la cohérence des totaux décisionnels ;
- le statut de remédiation ;
- la cohérence interne des fichiers ;
- la suppression des identifiants directs des fournisseurs et modèles ;
- l’absence de réponses brutes et de traces privées dans les artefacts publics ;
- la cohérence entre le manifeste public et les fichiers publiés.

Le résultat de la vérification est documenté dans :

```text
VERIFICATION_SUMMARY.json
```

---

## 7. Politique de désidentification

La publication est **désidentifiée**. Elle n’est pas présentée comme irréversiblement anonyme.

Ne sont pas publiés :

- les noms des fournisseurs ;
- les noms des modèles ;
- les endpoints API ;
- les détails de routage ;
- les réponses brutes ;
- les traces détaillées d’exécution ;
- les horodatages précis ;
- le registre privé de correspondance des identités ;
- la logique propriétaire de mesure.

Le protocole et les familles de questions étant publics, le risque résiduel de réidentification ne peut pas être totalement éliminé.

L’objectif est d’empêcher l’attribution directe tout en préservant une transparence suffisante pour l’examen méthodologique.

---

## 8. Périmètre de la publication publique

La baseline publie des mesures quantitatives agrégées et une couverture documentée.

Elle ne publie pas l’intégralité du registre de mesure NeoMundi.

Le périmètre privé peut contenir des observations au niveau de chaque exécution, des artefacts de réponse, des traces runtime détaillées, des données de coût et de tokens, des diagnostics internes, des notes d’examen et le registre privé de correspondance des profils.

Cette séparation permet l’examen public sans exposer des informations opérationnelles ou identifiantes confidentielles.

---

## 9. Politique de non-classement

Cette publication ne classe pas les profils du meilleur au moins bon.

Elle publie uniquement des mesures observées et des informations de distribution.

Les différences entre profils ne doivent pas être interprétées comme une hiérarchie universelle de qualité des modèles.

---

## 10. Limite d’interprétation

La baseline documente un comportement observé dans le cadre d’un protocole et d’une fenêtre d’observation définis.

Elle ne permet pas d’établir :

- la qualité globale d’un modèle ;
- sa fiabilité factuelle universelle ;
- une certification de sécurité ;
- sa conformité réglementaire ;
- son aptitude au déploiement ;
- l’attribution causale des évolutions comportementales futures.

L’interprétation correcte est :

> un signal a été observé dans les conditions de la campagne.

Un signal constitue un élément de preuve nécessitant une interprétation, et non un verdict.

---

## 11. Relation avec le protocole hebdomadaire

La Baseline V1 constitue une campagne de référence élargie.

Le protocole hebdomadaire actif est documenté à la racine du dépôt dans :

- `methodology.md` ;
- `methodologie.md`.

Les futures publications hebdomadaires pourront être comparées à cette baseline afin d’observer si le comportement runtime reste comparable, évolue progressivement ou indique un possible changement de régime.
