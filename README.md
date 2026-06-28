## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**


# NeoMundi Weekly Barometer — Public Baseline V1

This directory contains the first public quantitative reference release for the NeoMundi Weekly Barometer.

It is a **de-identified baseline**: a fixed reference photograph of observed AI runtime behaviour across a panel of 12 generative AI systems under repeated and controlled measurement conditions.

It is not a weekly editorial report, a leaderboard, a certification, a benchmark ranking or a global assessment of AI quality.

Its purpose is narrower and more durable: to establish a stable reference point from which future changes in observed runtime behaviour can be measured over time.

## Reference campaign at a glance

**12 de-identified AI profiles**
**4 fixed questions**
**100 repetitions per question**
**3 execution waves**
**14,400 finalised observations**

The Baseline V1 is the initial reference frame of the NeoMundi Weekly Barometer.

Future weekly Barometer releases can be compared against this reference in order to observe whether behavioural signals remain stable, vary gradually or show evidence of a possible regime change.

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

These questions were repeated under the same campaign conditions in order to observe response stability, factual-risk signals, coherence, semantic variation, decision behaviour and runtime variation.

The questions are public so that readers can understand the nature of the observed tasks and independently reproduce comparable inquiry conditions.

## What this baseline enables

The baseline fixes recurring indicators that can be compared in subsequent Barometers.

Published observations include:

* stability;
* factual-risk signal;
* coherence;
* semantic variation;
* decision behaviour, including `ALLOW`, `FLAG` and `ERROR`;
* inter-run variation;
* coverage and completeness;
* latency bands where applicable;
* `delta_g`, reported as an observable advanced runtime-variation signal.

The purpose is not to determine which system is “best”.

The purpose is to make behavioural movement visible across repeated observations.

A system can remain stable while showing factual-risk signals. A system can vary semantically without being factually incorrect. A signal is an observation requiring interpretation, not a verdict.

## Public files

* `public_profiles_summary.csv`
  One aggregated quantitative record per de-identified profile.

* `public_question_profiles.csv`
  Aggregated quantitative results by profile and question.

* `public_regimes_totals.csv`
  Distribution of observed decision and regime outcomes. It does not contain artificial rank bins.

* `public_manifest.json`
  Release metadata, campaign provenance and public-file inventory.

* `public_exclusions_and_limitations.csv`
  Excluded fields, publication boundaries and interpretation limits.

* `METHODOLOGY.md`
  Concise methodological note for the baseline campaign.

## Interpretation boundary

A complete cell means that the planned execution set was completed.

Metric-level coverage is reported separately and may be below 100% where an individual metric could not be computed for every observation.

A score of `0.0` is a measured zero when its metric-level sample size is positive.

`not_scored` means that no valid score was available for the relevant observation.

`delta_g` is an observable derived runtime signal. Its publication does not disclose the internal composition, thresholds, weighting logic or proprietary calculation rules of the NeoMundi measurement framework.

Published metrics must not be interpreted as independent confirmations where the release documents a dependency between them.

## Public release boundary

The NeoMundi Weekly Barometer publishes aggregated and de-identified results so that reported figures, coverage, regime distributions and visualisations can be inspected publicly.

The public release is deliberately bounded.

It is not the full NeoMundi measurement record.

## What remains within the private measurement boundary

Depending on the campaign and measurement scope, the private observation record may include:

* execution-level measurement records rather than public aggregates;
* repeated-run histories and continuity observations;
* stability, validity, factual-risk, semantic-variation and coherence signals at execution level;
* decision states, flags, errors and completeness diagnostics;
* prompt families, prompt-level histories and controlled test-corpus information;
* response-level artefacts and diagnostic material;
* token consumption, execution cost and cost-efficiency indicators;
* latency, runtime-performance and infrastructure-effort signals;
* information-density and generation-efficiency indicators;
* token-saving or generation-stop observations where applicable;
* provider, model, routing, hosting and deployment identifiers;
* request, trace and correlation identifiers;
* execution timestamps and runtime continuity information;
* raw API, streaming and diagnostic payloads;
* internal review notes, governance reasons and contextual interpretation records;
* the private registry linking observed systems to stable de-identified `PROFILE-XXXXXX` identifiers.

These materials are not published because they could disclose system identities, prompt designs, response content, operational architecture, measurement methods or confidential runtime traces.

## Why this distinction matters

The public baseline makes recurring behavioural signals visible and comparable.

The private measurement boundary preserves the deeper evidence required for controlled replay, technical review, cost and efficiency analysis, governance assessment and context-specific investigation.

The public release is therefore designed to be inspectable without exposing the systems, operational traces and artefacts from which it is derived.

## De-identification and residual re-identification risk

This release is **de-identified**. It is not presented as irreversibly anonymous.

Provider names, model names, endpoints, prompts, raw responses, detailed traces, precise execution timestamps and the private profile mapping are not published.

Public profiles use stable opaque identifiers in the format `PROFILE-XXXXXX`.

These identifiers are not derived from ranking, performance, provider names or model names.

The private mapping is retained separately and is not included in this repository or in any public release.

Because the experimental protocol and question families are reproducible in principle, a third party with comparable API access, model availability and execution conditions may attempt to infer the identity of one or more profiles.

NeoMundi therefore documents re-identification as a residual and accepted publication risk.

The objective is not to claim impossible anonymity. It is to prevent direct attribution while preserving enough methodological transparency for independent scrutiny.

## What this baseline is not

This baseline is not:

* a provider ranking;
* a model leaderboard;
* a safety certification;
* a guarantee of factual truth;
* a legal, regulatory or compliance determination;
* a deployment authorisation;
* a substitute for human review, governance or domain-specific validation.

It is a public reference point for observing AI runtime behaviour over time.
