## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**


# NeoMundi Weekly Barometer — Public Baseline V1

This directory contains the first public quantitative reference release of the **NeoMundi Weekly Barometer**.

Baseline V1 is a **de-identified reference campaign**: a fixed measurement snapshot of AI runtime behaviour observed across 12 generative AI profiles under repeated and controlled conditions.

It is not a weekly editorial report, a leaderboard, a certification, a model ranking or a general assessment of AI quality.

Its purpose is narrower and more durable: to establish a stable quantitative reference against which future changes in observed AI behaviour can be measured over time.

---

## Reference campaign at a glance

- **12 de-identified AI profiles**
- **4 fixed questions**
- **100 repetitions per question**
- **3 execution waves**
- **14,400 finalised observations**

Baseline V1 establishes the initial reference frame for the NeoMundi Weekly Barometer.

Future weekly releases can be compared with this baseline to assess whether observed behavioural signals remain stable, vary progressively or indicate a possible change in behavioural regime.

---

## The four fixed questions

The campaign combines four distinct response conditions.

### Question 1 — Reasoning

**Bat and ball problem**

> A bat and a ball cost €1.10 in total.  
> The bat costs €1 more than the ball.  
> How much does the ball cost?

### Question 2 — Scientific explanation

**Seasons on Earth**

> Why do seasons occur on Earth?

### Question 3 — Open conceptual question

**Stability and truth**

> Why is a stable AI response not necessarily factually correct?

### Question 4 — Open epistemic question

**Widely accepted but potentially false beliefs**

> Give an example of a widely accepted belief that may be false, and explain how it could be checked.

The same questions were repeated under controlled campaign conditions to observe:

- response stability;
- semantic variation;
- factual-risk signals;
- coherence;
- decision and regime behaviour;
- runtime variation;
- measurement completeness.

The questions are public so that readers can understand the nature of the observed tasks and reproduce comparable inquiry conditions independently.

---

## What this baseline enables

Baseline V1 establishes recurring indicators that can be compared across subsequent weekly releases.

Published observations include:

- stability;
- factual-risk signals;
- coherence;
- semantic variation;
- decision behaviour, including `ALLOW`, `FLAG` and `ERROR`;
- inter-run variation;
- coverage and completeness;
- latency bands, where applicable;
- `delta_g`, reported as an advanced observable signal of runtime variation.

The purpose is not to determine which system is “best”.

The purpose is to make behavioural movement measurable and visible across repeated observations.

A system may remain highly stable while producing factual-risk signals.

A system may vary semantically without being factually incorrect.

Different signals may converge, diverge or remain inconclusive.

**A signal is an observation requiring interpretation, not a verdict.**

---

## Public files

### `public_profiles_summary.csv`

One aggregated quantitative record per de-identified profile.

### `public_question_profiles.csv`

Aggregated quantitative results by profile and question.

### `public_regimes_totals.csv`

Distribution of observed decision states and behavioural regimes. This file does not contain artificial ranking categories.

### `public_manifest.json`

Release metadata, campaign provenance and public-file inventory.

### `public_exclusions_and_limitations.csv`

Excluded fields, publication boundaries and documented interpretation limits.

### `METHODOLOGY.md`

Concise methodological documentation for the Baseline V1 campaign.

---

## Interpretation boundaries

A complete experimental cell means that the planned set of executions was completed.

Metric-level coverage is reported separately and may remain below 100% when a specific metric could not be computed for every observation.

A value of `0.0` represents a measured zero when the metric-level sample size is greater than zero.

`not_scored` means that no valid score was available for the relevant observation.

`delta_g` is a derived observable runtime signal. Its publication does not disclose the internal composition, thresholds, weighting logic or proprietary calculation rules of the NeoMundi measurement framework.

Published metrics must not be interpreted as independent confirmations when the release documentation identifies a dependency between them.

No individual metric should be interpreted in isolation as a complete assessment of system quality, truthfulness, safety or governability.

---

## Public release boundary

The NeoMundi Weekly Barometer publishes aggregated and de-identified results so that reported figures, coverage levels, regime distributions and visualisations can be publicly inspected.

The release is deliberately bounded.

It does not represent the complete NeoMundi measurement record.

---

## What remains within the private measurement boundary

Depending on the campaign and measurement scope, the private observation record may include:

- execution-level measurement records rather than public aggregates;
- repeated-run histories and longitudinal continuity observations;
- execution-level stability, validity, factual-risk, semantic-variation and coherence signals;
- decision states, flags, errors and completeness diagnostics;
- prompt families, prompt histories and controlled test-corpus information;
- response-level artefacts and diagnostic material;
- token consumption, execution cost and cost-efficiency indicators;
- latency, runtime-performance and infrastructure-effort signals;
- information-density and generation-efficiency indicators;
- token-saving or generation-stop observations, where applicable;
- provider, model, routing, hosting and deployment identifiers;
- request, trace and correlation identifiers;
- execution timestamps and runtime-continuity information;
- raw API, streaming and diagnostic payloads;
- internal review notes, governance reasons and contextual interpretation records;
- the private registry linking observed systems to stable de-identified `PROFILE-XXXXXX` identifiers.

These materials are not published because they may disclose system identities, prompt designs, response content, operational architecture, proprietary measurement methods or confidential runtime traces.

---

## Why this distinction matters

The public baseline makes recurring behavioural signals visible, inspectable and comparable over time.

The private measurement boundary preserves the deeper evidence required for:

- controlled replay;
- technical investigation;
- longitudinal analysis;
- cost and efficiency assessment;
- governance review;
- context-specific interpretation.

The public release is therefore designed to support scrutiny and reproducibility without exposing the systems, traces and operational artefacts from which the measurements are derived.

---

## De-identification and residual re-identification risk

This release is **de-identified**. It is not presented as irreversibly anonymous.

Provider names, model names, endpoints, raw responses, detailed traces, precise execution timestamps and the private profile mapping are not published.

Public profiles use stable opaque identifiers in the format:

`PROFILE-XXXXXX`

These identifiers are not derived from ranking, performance, provider names or model names.

The private mapping registry is retained separately and is not included in this repository or in any public release.

Because the experimental protocol and question families are reproducible in principle, a third party with comparable API access, model availability and execution conditions may attempt to infer the identity of one or more profiles.

NeoMundi therefore documents re-identification as a residual and accepted publication risk.

The objective is not to claim impossible anonymity. It is to prevent direct attribution while preserving sufficient methodological transparency for independent scrutiny.

---

## What this baseline is not

This baseline is not:

- a provider ranking;
- a model leaderboard;
- a safety certification;
- a guarantee of factual accuracy;
- a legal, regulatory or compliance determination;
- a deployment authorisation;
- a substitute for human review;
- a substitute for governance or domain-specific validation.

It is a public quantitative reference point for observing changes in AI runtime behaviour over time.
