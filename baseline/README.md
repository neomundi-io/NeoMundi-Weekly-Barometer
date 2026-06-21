## 🌐 Choose your language

**[🇫🇷 Lire la version française](README.fr.md)** · **[🇬🇧 English](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

**12 anonymized AI systems · 4 fixed questions · 100 repetitions per question · 3 execution waves · 14,400 finalized observations**

This directory contains the first public quantitative baseline release of the NeoMundi Weekly Barometer.

It provides an anonymized reference cartography of runtime behavior observed across a panel of generative AI systems under repeated measurement conditions.

The purpose of this baseline is simple: to establish the initial reference point from which future weekly changes in observed AI behavior can be measured.

---

## What this baseline is

This baseline is not a ranking, certification, benchmark leaderboard, or declaration of a “best” AI system.

It is a reference measurement artifact.

It documents how anonymized systems behaved during one defined observation campaign across repeated executions of the same four questions. It makes visible differences in stability, factual validity signals, coherence, semantic variation, decision behavior, latency bands and variation across execution waves.

Future Weekly Barometers will use this release as a comparison layer to identify whether observed behavior remains comparable, changes gradually, or enters a distinct runtime regime.

---

## Measurement frame

The baseline is derived from:

* **12 anonymized system profiles**
* **4 fixed questions**
* **100 repetitions per question**
* **3 repeated execution waves**
* **1,200 observations per anonymized profile**
* **14,400 finalized observations in total**

All planned observations were completed.

One limited collection incident was remediated under the same measurement configuration. The remediated cell is explicitly marked in the public data through `remediated_complete` and `remediated_observation_count`.

---

## The four fixed questions

The campaign combines four different response conditions.

### NM-WEEKLY-Q01 — Reasoning

A bat and a ball cost €1.10 in total. The bat costs €1 more than the ball. How much does the ball cost?

### NM-WEEKLY-Q02 — Scientific explanation

Why do seasons occur on Earth?

### NM-WEEKLY-Q03 — Open conceptual question

Why is a stable AI response not necessarily factually correct?

### NM-WEEKLY-Q04 — Open epistemic question

Give an example of a belief that is widely accepted but may be false. Explain how it could be checked.

These questions were repeated under the same campaign conditions in order to observe whether systems behave consistently across reasoning, scientific explanation, conceptual interpretation and open epistemic uncertainty.

The questions are public so that readers can understand the nature of the observed tasks and reproduce comparable inquiry conditions.

---

## Baseline snapshot

This release establishes the first quantitative reference point for future longitudinal comparison.

Across the 12 anonymized profiles:

* mean observed stability was **0.8165**;
* mean observed coherence was **0.7866**;
* mean factual hallucination signal was **0.0257**;
* mean semantic instability signal was **0.0189**;
* mean inter-run variability was **0.0081**;
* **96.57%** of observations resulted in `ALLOW`;
* **3.37%** resulted in `FLAG`;
* **0.06%** resulted in `ERROR`.

The baseline also shows meaningful differences between anonymized profiles:

* observed stability ranges from **0.8005** to **0.8274**;
* observed coherence ranges from **0.7612** to **0.8042**;
* factual hallucination signal ranges from **0.0018** to **0.0544**;
* semantic instability ranges from **0.0006** to **0.0723**;
* inter-run variability ranges from **0.0046** to **0.0164**.

These values are reference measurements, not verdicts.

They are intended to make future behavioral changes measurable over time.

---

## Public artifacts

| File                                    | Purpose                                                                       |
| --------------------------------------- | ----------------------------------------------------------------------------- |
| `public_manifest.json`                  | Release scope, measurement frame, identity policy and published artifact list |
| `public_profiles_summary.csv`           | One quantitative anonymized behavioral profile per observed system            |
| `public_question_profiles.csv`          | Profile-level behavior across the four fixed questions                        |
| `public_decision_distribution.csv`      | Aggregated distribution of observed `ALLOW`, `FLAG` and `ERROR` decisions     |
| `public_exclusions_and_limitations.csv` | Publication boundaries, exclusions and methodological limitations             |
| `METHODOLOGY.md`                        | Measurement definitions, coverage policy and interpretation boundaries        |
| `VERIFICATION_SUMMARY.json`             | Release verification and integrity summary                                    |

---

## How to read the public data

The public release provides quantitative metrics with:

* means;
* medians;
* standard deviations;
* minimum and maximum observed values;
* metric-level observation counts;
* coverage rates;
* coverage status;
* remediation status where applicable.

A value of `0.0` means that the observed metric value was zero.

A missing or unavailable metric is not represented as a false zero. Metric-level coverage is published separately through the relevant `*_n`, `*_coverage_rate` and `*_coverage_status` fields.

A cell marked `complete` means that the planned execution set was completed.

A cell marked `remediated_complete` means that a limited collection issue was corrected under the same measurement configuration before aggregation.

---

## Public indicators

The baseline includes the following public indicators.

### Stability

Observed capacity of a system to produce comparable responses when the same question is repeated.

### Coherence

Observed internal consistency of generated responses under the campaign protocol.

### Factual hallucination signal

Observed signal of factual fragility according to the evaluation method used in this campaign.

This is not a universal truth score and should always be interpreted in relation to the question set, evaluation protocol and observation window.

### Semantic instability

Observed variation in the semantic content or useful meaning of responses across repeated executions.

### Decision behavior

Observed distribution of `ALLOW`, `FLAG` and `ERROR` outcomes.

These outcomes describe the behavior of the measurement and governance layer during the campaign. They do not constitute a safety certification.

### Inter-run variability

Observed variation between the three repeated execution waves.

This indicator is useful for detecting early variation patterns. It should not be interpreted as a long-horizon estimate of system stability.

### Latency band

Observed runtime latency is published in broad bands rather than as exact infrastructure-level timings.

This preserves useful operational context while reducing unnecessary re-identification exposure.

### `delta_g`

`delta_g` is published as an advanced runtime variation signal.

It is reported as an observable output of the measurement framework. It does not disclose the internal composition, thresholds, weighting logic or proprietary calculation rules of the NeoMundi framework.

---

## What is intentionally not published

To preserve anonymization, methodological integrity and the distinction between public observation and private audit material, this release does not include:

* provider names;
* model names;
* private identity mapping;
* API endpoints;
* infrastructure routing details;
* raw prompts beyond the four published campaign questions;
* raw model outputs;
* exact timestamps;
* request traces;
* source filenames;
* private audit records;
* private implementation details;
* proprietary calculation logic;
* exact infrastructure-level latency traces;
* direct identifiers allowing systems to be named in the public release.

The publication is anonymized, but no anonymization method can eliminate all theoretical re-identification risk where an external actor has access to comparable systems, prompts, timing conditions and execution infrastructure.

NeoMundi does not publish the identity mapping and keeps it confidential.

---

## Important interpretation note

This baseline documents observed runtime behavior under a defined protocol and time window.

It should be interpreted as:

* comparative;
* contextual;
* exploratory;
* reproducible at the level of inquiry conditions;
* unsuitable for universal claims about all future behavior of a system.

Results do not establish that one anonymized profile is globally “better” or “worse” than another.

The objective is to observe behavior, not to create a public league table.

---

## Intended use

This release is intended to support:

* methodological review;
* AI runtime observability research;
* discussion of stability, factual validity and behavioral variation;
* future longitudinal comparison;
* scientific contributions;
* governance-oriented review;
* development of interpretable AI measurement practices.

Future Weekly Barometers will compare new observation campaigns against this baseline in order to identify meaningful changes in observed behavior over time.

---

**NeoMundi Weekly Barometer**
*Runtime observation before governance claims.*
