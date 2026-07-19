# Baromètre Hebdomadaire NeoMundi

🌐 **Langue :** [Français](./README.fr.md) · [English](./README.md)

🌍 **NeoMundi :** [Site français](https://neomundi.org/) · [English website](https://neomundi.org/en/home)

Le **Baromètre Hebdomadaire NeoMundi** est un programme public de mesure longitudinale conçu pour observer l’évolution du comportement des systèmes d’IA générative dans des conditions répétées et contrôlées.

Il ne classe ni les fournisseurs ni les modèles.

Il produit des mesures runtime désidentifiées, comparables et documentées afin de rendre visibles les évolutions comportementales au fil des campagnes successives.

> Les benchmarks photographient les systèmes d’IA à un instant donné.  
> NeoMundi observe leurs trajectoires.

---

## Structure du programme

Le dépôt comprend quatre composantes principales :

- **Baseline Publique V1** — la première campagne quantitative de référence ;
- **publications hebdomadaires** — les campagnes récurrentes de mesure publique ;
- **méthodologie** — le protocole actif et le cadre d’interprétation ;
- **calibration** — la procédure de validation technique utilisée avant toute modification significative du protocole ou du pipeline.

---

## Protocole hebdomadaire actif

Chaque campagne hebdomadaire repose sur :

```text
12 profils d’IA désidentifiés
× 4 questions fixes
× 100 répétitions
= 4 800 exécutions planifiées
```

La fenêtre de mesure de référence est :

```text
lundi 00:00 UTC
à
dimanche 23:59 UTC
```

Les mêmes quatre questions sont répétées dans des conditions comparables afin de permettre l’analyse longitudinale.

---

## Les quatre questions fixes

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

Ces questions couvrent des conditions de réponse distinctes et ne doivent pas être réduites à un score universel unique.

---

## Baseline Publique V1

La **Baseline Publique V1** établit le premier cadre quantitatif de référence du Baromètre Hebdomadaire NeoMundi.

Elle comprend :

```text
12 profils d’IA désidentifiés
× 4 questions fixes
× 100 répétitions
× 3 vagues d’exécution
= 14 400 observations finalisées
```

La baseline n’est pas une publication hebdomadaire ordinaire.

Il s’agit d’une campagne de référence élargie utilisée pour établir un point de comparaison fixe destiné aux futures observations longitudinales.

Accéder à la baseline :

- [Baseline V1 — Français](./baseline/README.fr.md)
- [Baseline V1 — English](./baseline/README.md)

---

## Publications hebdomadaires

Les publications récurrentes du Baromètre sont disponibles dans :

- [Publications hebdomadaires](./releases/)

Chaque publication peut notamment comprendre :

- des données agrégées et désidentifiées ;
- des indicateurs par profil et par question ;
- des informations de couverture ;
- des distributions de régimes ou d’états décisionnels ;
- des visualisations ;
- des limites méthodologiques ;
- des manifestes publics et des artefacts de vérification.

---

## Méthodologie

Le protocole actif est documenté dans :

- [Méthodologie — Français](./methodologie.md)
- [Methodology — English](./methodology.md)

Ces documents définissent :

- l’architecture hebdomadaire de mesure ;
- les quatre questions fixes ;
- les principaux signaux publics ;
- les principes de comparaison longitudinale ;
- les exigences de validation ;
- les limites d’interprétation ;
- les frontières de désidentification et de publication.

---

## Calibration

Le protocole de calibration est documenté dans :

- [Protocole de calibration — Français](./CALIBRATION.fr.md)
- [Calibration protocol — English](./CALIBRATION.md)

La calibration valide le processus de mesure avant une campagne publique ou toute modification significative du protocole, du pipeline de scoring, de la logique d’agrégation ou de la structure des exports publics.

> La calibration valide le processus de mesure. Elle ne valide pas le système d’IA lui-même.

---

## Familles de signaux observés

Selon la campagne et la couverture disponible, le Baromètre peut publier ou documenter :

- la stabilité ;
- la variation sémantique ;
- la cohérence ;
- les signaux de risque factuel ;
- les comportements décisionnels ou régimes observés ;
- la variation entre les exécutions ;
- la couverture et la complétude ;
- les plages de latence ;
- les indicateurs de coût et d’effort runtime lorsqu’ils sont disponibles ;
- `delta_g`, publié comme un signal observable avancé de variation runtime.

Aucun indicateur individuel ne doit être interprété isolément comme une évaluation complète de la qualité, de la véracité, de la sécurité ou de la gouvernabilité d’un système.

---

## Doctrine d’interprétation

Le Baromètre suit une règle fondamentale :

> Un signal est une observation qui nécessite une interprétation, et non un verdict.

Un changement observé ne permet pas, à lui seul, d’établir :

- une mise à jour du modèle ;
- une modification du côté du fournisseur ;
- une dégradation ;
- une amélioration ;
- une conformité réglementaire ;
- une aptitude au déploiement ;
- la supériorité d’un système sur un autre.

La formulation appropriée est :

> Un changement de comportement a été observé dans les conditions de la campagne.

L’attribution d’une cause nécessite des éléments de preuve complémentaires.

---

## Périmètre de la publication publique

Le Baromètre Hebdomadaire NeoMundi publie des résultats agrégés et désidentifiés afin que les chiffres, niveaux de couverture, distributions et visualisations puissent être examinés publiquement.

Les publications publiques ne représentent pas l’intégralité du registre de mesure NeoMundi.

Selon la campagne, le périmètre privé de mesure peut notamment comprendre :

- les observations au niveau de chaque exécution ;
- les réponses brutes ;
- les traces runtime détaillées ;
- les identifiants des fournisseurs et modèles ;
- les horodatages précis ;
- les données de tokens et de coût ;
- les diagnostics internes ;
- les notes d’examen ;
- le registre privé de correspondance des profils ;
- la logique de calcul propriétaire.

Cette séparation permet l’examen public sans exposer des informations opérationnelles ou identifiantes confidentielles.

---

## Désidentification

Les profils publics utilisent des identifiants opaques et stables au format :

```text
PROFILE-XXXXXX
```

Ces identifiants ne sont dérivés ni d’un classement, ni des performances, ni du nom d’un fournisseur ou d’un modèle.

La correspondance privée entre les profils publics et les systèmes observés est conservée séparément.

Les publications sont **désidentifiées**. Elles ne sont pas présentées comme irréversiblement anonymes.

Le risque résiduel de réidentification est documenté comme une limite de publication.

---

## Ce que ce programme n’est pas

Le Baromètre Hebdomadaire NeoMundi n’est pas :

- un classement de fournisseurs ;
- un leaderboard de modèles ;
- une certification de sécurité ;
- une garantie d’exactitude factuelle ;
- une décision juridique, réglementaire ou de conformité ;
- une autorisation de déploiement ;
- un substitut à l’examen humain ;
- un substitut à la gouvernance ou à une validation propre à un domaine métier.

Il constitue un instrument métrologique public destiné à observer l’évolution du comportement runtime des systèmes d’IA dans le temps.

---

## Principes scientifiques

Le programme suit six principes :

1. **Mesurer avant d’interpréter.**
2. **Répéter avant de généraliser.**
3. **Caractériser la variation avant de déclarer une dérive.**
4. **Ne jamais confondre stabilité et vérité.**
5. **Distinguer l’observation, l’interprétation et l’attribution causale.**
6. **Considérer chaque signal comme un élément de preuve, et non comme un verdict.**

---

## Navigation dans le dépôt

| Ressource | Français | English |
|---|---|---|
| Présentation du programme | [README.fr.md](./README.fr.md) | [README.md](./README.md) |
| Méthodologie active | [methodologie.md](./methodologie.md) | [methodology.md](./methodology.md) |
| Protocole de calibration | [CALIBRATION.fr.md](./CALIBRATION.fr.md) | [CALIBRATION.md](./CALIBRATION.md) |
| Baseline Publique V1 | [baseline/README.fr.md](./baseline/README.fr.md) | [baseline/README.md](./baseline/README.md) |
| Méthodologie de la baseline | [baseline/METHODOLOGY.fr.md](./baseline/METHODOLOGY.fr.md) | [baseline/METHODOLOGY.md](./baseline/METHODOLOGY.md) |
| Publications hebdomadaires | [releases/](./releases/) | [releases/](./releases/) |

---

**Baromètre Hebdomadaire NeoMundi**  
*Mesurer le runtime avant toute conclusion de gouvernance.*
