# NeoMundi Weekly Barometer

🌐 **Language:** [English](./README.md) · [Français](./README.fr.md)

🌍 **NeoMundi:** [English website](https://neomundi.org/en/home) · [Site français](https://neomundi.org/)

The **NeoMundi Weekly Barometer** is a public longitudinal measurement programme designed to observe how generative AI systems behave over time under repeated and controlled conditions.

It does not rank providers or models.

It produces de-identified, comparable and documented runtime measurements intended to make behavioural changes visible across successive campaigns.

> Benchmarks capture AI systems at a given moment.  
> NeoMundi observes their trajectories.

---

## Programme structure

The repository contains four main components:

- **Public Baseline V1** — the initial quantitative reference campaign;
- **Weekly releases** — recurring public measurement campaigns;
- **Methodology** — the active protocol and interpretation framework;
- **Calibration** — the technical validation procedure used before significant protocol or pipeline changes.

---

## Active weekly protocol

Each weekly campaign is based on:

```text
12 de-identified AI profiles
× 4 fixed questions
× 100 repetitions
= 4,800 planned executions
```

The reference measurement window is:

```text
Monday 00:00 UTC
to
Sunday 23:59 UTC
```

The same four questions are repeated under comparable conditions to support longitudinal analysis.

---

## The four fixed questions

### `NM-WEEKLY-Q01` — Reasoning

> A bat and a ball cost €1.10 in total.  
> The bat costs €1 more than the ball.  
> How much does the ball cost?

### `NM-WEEKLY-Q02` — Scientific explanation

> Why do seasons occur on Earth?

### `NM-WEEKLY-Q03` — Open conceptual question

> Why is a stable AI response not necessarily factually correct?

### `NM-WEEKLY-Q04` — Open epistemic question

> Give an example of a widely accepted belief that may be false, and explain how it could be checked.

These questions cover distinct response conditions and must not be reduced to a single universal score.

---

## Public Baseline V1

The **Public Baseline V1** establishes the initial quantitative reference frame of the NeoMundi Weekly Barometer.

It includes:

```text
12 de-identified AI profiles
× 4 fixed questions
× 100 repetitions
× 3 execution waves
= 14,400 finalised observations
```

The baseline is not an ordinary weekly release.

It is an extended reference campaign used to establish a fixed comparison point for future longitudinal observation.

Access the baseline:

- [Baseline V1 — English](./baseline/README.md)
- [Baseline V1 — Français](./baseline/README.fr.md)

---

## Weekly releases

Recurring Barometer publications are available in:

- [Weekly releases](./releases/)

Each release may include:

- aggregated de-identified data;
- indicators by profile and question;
- coverage information;
- regime or decision distributions;
- visualisations;
- methodological limitations;
- public manifests and verification artefacts.

---

## Methodology

The active protocol is documented in:

- [Methodology — English](./methodology.md)
- [Méthodologie — Français](./methodologie.md)

These documents define:

- the weekly measurement architecture;
- the four fixed questions;
- the main public signals;
- the longitudinal comparison principles;
- validation requirements;
- interpretation limits;
- de-identification and publication boundaries.

---

## Calibration

The calibration protocol is documented in:

- [Calibration protocol — English](./CALIBRATION.md)
- [Protocole de calibration — Français](./CALIBRATION.fr.md)

Calibration validates the measurement process before a public campaign or any significant modification to the protocol, scoring pipeline, aggregation logic or public export structure.

> Calibration validates the measurement process. It does not validate the AI system itself.

---

## Observed signal families

Depending on the campaign and available coverage, the Barometer may publish or document:

- stability;
- semantic variation;
- coherence;
- factual-risk signals;
- decision or regime behaviour;
- inter-run variation;
- coverage and completeness;
- latency bands;
- cost and runtime-effort indicators where available;
- `delta_g`, reported as an advanced observable runtime-variation signal.

No individual indicator should be interpreted in isolation as a complete assessment of quality, truthfulness, safety or governability.

---

## Interpretation doctrine

The Barometer follows one fundamental rule:

> A signal is an observation requiring interpretation, not a verdict.

An observed change does not, by itself, establish:

- a model update;
- a provider-side modification;
- a degradation;
- an improvement;
- regulatory compliance;
- deployment suitability;
- the superiority of one system over another.

The appropriate formulation is:

> A behavioural change was observed under the conditions of the campaign.

Causal attribution requires additional evidence.

---

## Public release boundary

The NeoMundi Weekly Barometer publishes aggregated and de-identified results so that figures, coverage levels, distributions and visualisations can be publicly inspected.

Public releases do not represent the complete NeoMundi measurement record.

Depending on the campaign, the private measurement boundary may include:

- execution-level observations;
- raw responses;
- detailed runtime traces;
- provider and model identifiers;
- precise timestamps;
- token and cost data;
- internal diagnostics;
- review notes;
- private profile mapping;
- proprietary calculation logic.

This separation supports public scrutiny without exposing confidential operational or identifying information.

---

## De-identification

Public profiles use stable opaque identifiers in the format:

```text
PROFILE-XXXXXX
```

These identifiers are not derived from ranking, performance, provider names or model names.

The private mapping between public profiles and the observed systems is retained separately.

The releases are **de-identified**. They are not presented as irreversibly anonymous.

Residual re-identification risk is documented as a publication limitation.

---

## What this programme is not

The NeoMundi Weekly Barometer is not:

- a provider ranking;
- a model leaderboard;
- a safety certification;
- a guarantee of factual accuracy;
- a legal, regulatory or compliance determination;
- a deployment authorisation;
- a substitute for human review;
- a substitute for governance or domain-specific validation.

It is a public metrological instrument for observing AI runtime behaviour over time.

---

## Scientific principles

The programme follows six principles:

1. **Measure before interpreting.**
2. **Repeat before generalising.**
3. **Characterise variation before declaring drift.**
4. **Never confuse stability with truth.**
5. **Distinguish observation, interpretation and causal attribution.**
6. **Treat every signal as an element of evidence, not as a verdict.**

---

## Repository navigation

| Resource | English | Français |
|---|---|---|
| Programme overview | [README.md](./README.md) | [README.fr.md](./README.fr.md) |
| Active methodology | [methodology.md](./methodology.md) | [methodologie.md](./methodologie.md) |
| Calibration protocol | [CALIBRATION.md](./CALIBRATION.md) | [CALIBRATION.fr.md](./CALIBRATION.fr.md) |
| Public Baseline V1 | [baseline/README.md](./baseline/README.md) | [baseline/README.fr.md](./baseline/README.fr.md) |
| Baseline methodology | [baseline/METHODOLOGY.md](./baseline/METHODOLOGY.md) | [baseline/METHODOLOGY.fr.md](./baseline/METHODOLOGY.fr.md) |
| Weekly releases | [releases/](./releases/) | [releases/](./releases/) |

---

**NeoMundi Weekly Barometer**  
*Runtime measurement before governance claims.*
