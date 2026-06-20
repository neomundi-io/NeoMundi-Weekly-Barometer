## 🌐 Choose your language

**[🇫🇷 Lire la version française](README.fr.md)** · **[🇬🇧 English](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

This directory contains the first public baseline release of the NeoMundi Weekly Barometer.

It provides an anonymized cartography of runtime behavior observed across a panel of 12 generative AI systems under repeated measurement conditions.

## What this baseline is

The baseline is the reference point used to interpret future Weekly Barometer observations.

It does not rank models, certify systems, or declare a universal “best” AI.

Its purpose is to make visible that systems can occupy different behavioral regimes under repeated execution: they may differ in stability, coherence, semantic risk, factual reliability, latency, and variation across repeated measurement waves.

## Measurement frame

This public baseline is derived from:

* **12 anonymized system profiles**
* **3 repeated measurement waves**
* **4 fixed prompt identifiers** (`Q01` to `Q04`)
* **100 repetitions per prompt, per wave**
* **14,400 total observations**

Prompt contents, model identities, provider identities, timestamps, raw outputs, and exact high-precision measurements are not published in this release.

## Public artifacts

| File                                    | Purpose                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------ |
| `public_manifest.json`                  | Release scope, measurement frame, identity policy, and published artifact list |
| `public_profiles_summary.csv`           | One anonymized behavioral profile per observed system                          |
| `public_question_profiles.csv`          | Profile-level behavior across the four prompt identifiers                      |
| `public_regimes_totals.csv`             | Aggregated distribution of observed public bands and decision patterns         |
| `public_exclusions_and_limitations.csv` | Publication boundaries, exclusions, and methodological limitations             |

## How to read the bands

Published values are expressed as five **relative panel-position bands**:

* `lowest_panel_band`
* `low_panel_band`
* `mid_panel_band`
* `high_panel_band`
* `highest_panel_band`

These bands describe the relative position of a profile within this specific observed panel.

They are **not absolute safety thresholds**, quality grades, or universal performance claims.

For example, a `highest_panel_band` on `semantic_risk_position_band` means that the profile showed a comparatively higher value for that metric within this measurement cohort. It does not, by itself, establish a general or permanent property of that system.

## What is intentionally not published

To preserve methodological integrity, reduce unnecessary re-identification risk, and avoid turning the Observatory into a public leaderboard, this release does not include:

* provider or model names;
* the private identity mapping;
* raw observations;
* prompt contents;
* exact timestamps;
* source filenames;
* exact latency or cost values;
* high-precision metric values;
* API, infrastructure, or endpoint details.

## Important interpretation note

The baseline is a measurement artifact, not a verdict.

It documents observed runtime behavior under a defined protocol and time window. Results should be interpreted as comparative, contextual, and exploratory.

Inter-wave variability is estimated from three repeated measurement waves. It is useful for identifying early variation patterns, but it should not be interpreted as a long-horizon stability estimate.

## Remediation and audit integrity

A limited non-semantic collection failure was remediated under the same measurement configuration before public aggregation.

The original records remain preserved in the private audit corpus. The public release documents the treatment boundary in `public_exclusions_and_limitations.csv`.

## Intended use

This release is intended to support:

* methodological review;
* discussion of runtime AI observability;
* exploration of behavioral regimes;
* future longitudinal comparison;
* scientific and governance-oriented contributions.

Future weekly barometers will use this baseline as a reference layer to identify meaningful changes in observed behavior over time.

---

**NeoMundi Weekly Barometer**
Runtime observation before governance claims.
