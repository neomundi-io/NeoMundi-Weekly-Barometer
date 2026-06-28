# NeoMundi Weekly Barometer #2 — Public Data Release

**Campaign:** `neomundi_barometer_2026_w26`
**Observation period:** 22 June 2026 to 29 June 2026
**Publication form:** aggregated and de-identified
**Scope:** 12 de-identified profiles · 4 fixed question families · 100 repetitions per cell · 4,800 executions launched

## Overview

This release contains the public, aggregated and de-identified data for NeoMundi Weekly Barometer #2.

The Barometer observes the behaviour of AI systems under comparable execution conditions. Its purpose is not to rank systems or identify “best” and “worst” models. It is designed to make observable patterns visible over time: stability, semantic variation, factual-risk signals, measurement coverage and changes in observed regime.

For this campaign:

* **4,800 executions** were launched;
* **4,773 executions** were fully scored;
* analytical coverage reached **99.44%**;
* **27 executions** were incomplete;
* the observed panel contains **12 de-identified profiles**;
* the protocol uses **4 fixed question families** and **100 repetitions per profile-question cell**.

## Public files

* `public_overview.json`
  Campaign totals, global metrics, coverage information and score-dependency disclosures.

* `public_profiles_summary.csv`
  Aggregated results for each de-identified profile (`PROFILE-XXXXXX`).

* `public_questions_summary.csv`
  Aggregated results by question family.

* `public_regime_distribution.csv`
  Distribution of observed regimes: normal signal, semantic variation, factual alert, combined alert and incomplete measurement.

* `public_metric_contract.json`
  Definitions, intended meanings and interpretation limits for the published metrics.

* `public_manifest.json`
  Release inventory, integrity hashes and campaign provenance information.

## What is deliberately not published

This public release does **not** include:

* provider or model identifiers;
* prompts or prompt identifiers;
* model responses;
* request IDs, trace IDs or raw payloads;
* per-response timestamps;
* debugging material;
* the private profile-mapping registry.

Observed systems are represented through stable opaque identifiers in the format `PROFILE-XXXXXX`.

These identifiers are maintained through a private registry and are not assigned according to performance, alphabetical order, score or rank.

## Interpretation boundary

The figures in this release are measurement outputs. They are not an overall quality verdict, a safety certification, a truth guarantee or an authorisation to use a system in a particular context.

For this campaign, `stability_score`, `v_score` and `factual_hallucination_score` are empirically linked through the same measurement chain. They must therefore not be presented as independent confirmations of the same result.

A semantic-variation signal does not, by itself, establish a factual error. Likewise, a factual-risk signal should be interpreted as a measured alert requiring contextual reading, not as a standalone final judgement.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the file hashes provided in `public_manifest.json`.

Reproducing the campaign from source requires access to the private exports and remains subject to NeoMundi Observatory governance safeguards.

## Related resources

* NeoMundi Weekly Barometer baseline: public reference campaign built from 14,400 finalised observations.
* NeoMundi Observatory methodology.
* Barometer #2 publication article.
