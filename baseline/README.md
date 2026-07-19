## 🌐 Choose your language

**[🇫🇷 Lire la version française](README.fr.md)** · **[🇬🇧 English](README.md)**

# NeoMundi Weekly Barometer — Baseline V1

**12 de-identified AI profiles · 4 fixed questions · 100 repetitions per question · 3 execution waves · 14,400 finalised observations**

This directory contains the first public quantitative baseline release of the **NeoMundi Weekly Barometer**.

It provides a de-identified reference measurement of AI runtime behaviour observed across a panel of generative AI systems under repeated and controlled conditions.

Its purpose is to establish an initial quantitative reference against which future weekly changes in observed AI behaviour can be measured over time.

---

## What this baseline is

This baseline is not a ranking, certification, benchmark leaderboard or declaration of a “best” AI system.

It is a public reference measurement artefact.

It documents how de-identified AI profiles behaved during a defined observation campaign based on repeated executions of the same four questions.

It makes visible differences in:

- stability;
- coherence;
- factual-risk signals;
- semantic variation;
- decision behaviour;
- latency bands;
- variation across execution waves.

Future Weekly Barometer releases may use this baseline as a comparison layer to assess whether observed behaviour remains comparable, changes progressively or enters a potentially distinct runtime regime.

---

## Measurement frame

The baseline is derived from:

- **12 de-identified AI profiles**
- **4 fixed questions**
- **100 repetitions per question**
- **3 repeated execution waves**
- **1,200 observations per profile**
- **14,400 finalised observations in total**

All planned observations were completed.

One limited collection incident was remediated under the same measurement configuration. The affected cell is explicitly identified in the public data through `remediated_complete` and `remediated_observation_count`.

---

## The four fixed questions

The campaign combines four distinct response conditions.

### `NM-WEEKLY-Q01` — Reasoning

> A bat and a ball cost €1.10 in total.  
> The bat costs €1 more than the ball.  
> How much does the ball cost?

### `NM-WEEKLY-Q02` — Scientific explanation

> Why do seasons occur on Earth?

### `NM-WEEKLY-Q03` — Open conceptual question

> Why is a stable AI response not necessarily factually correct?

### `NM-WEEKLY-Q04` — Open epistemic question

> Give an example of a belief that is widely accepted but may be false. Explain how it could be checked.

These questions were repeated under the same campaign conditions to observe whether systems behave consistently across reasoning, scientific explanation, conceptual interpretation and open epistemic uncertainty.

The questions are public so that readers can understand the nature of the observed tasks and reproduce comparable inquiry conditions.

---

## Baseline snapshot

This release establishes the first quantitative reference point for future longitudinal comparison.

Across the 12 de-identified profiles:

- mean observed stability was **0.8165**;
- mean observed coherence was **0.7866**;
- mean factual-risk signal was **0.0257**;
- mean semantic-instability signal was **0.0189**;
- mean inter-run variability was **0.0081**;
- **96.57%** of observations resulted in `ALLOW`;
- **3.37%** resulted in `FLAG`;
- **0.06%** resulted in `ERROR`.

The baseline also shows measurable differences between de-identified profiles:

- observed stability ranges from **0.8005** to **0.8274**;
- observed coherence ranges from **0.7612** to **0.8042**;
- factual-risk signal ranges from **0.0018** to **0.0544**;
- semantic instability ranges from **0.0006** to **0.0723**;
- inter-run variability ranges from **0.0046** to **0.0164**.

These values are reference measurements, not verdicts.

They are intended to make future behavioural changes measurable over time.

---

## Public artefacts

| File | Purpose |
|---|---|
| `public_manifest.json` | Release scope, measurement frame, identity policy and published artefact inventory |
| `public_profiles_summary.csv` | One aggregated quantitative record per de-identified profile |
| `public_question_profiles.csv` | Aggregated quantitative results by profile and question |
| `public_decision_distribution.csv` | Aggregated distribution of observed `ALLOW`, `FLAG` and `ERROR` states |
| `public_exclusions_and_limitations.csv` | Publication boundaries, exclusions and methodological limitations |
| `METHODOLOGY.md` | Measurement definitions, coverage policy and interpretation boundaries |
| `VERIFICATION_SUMMARY.json` | Release verification and integrity summary |

---

## How to read the public data

The public release provides quantitative metrics with:

- means;
- medians;
- standard deviations;
- minimum and maximum observed values;
- metric-level observation counts;
- coverage rates;
- coverage status;
- remediation status where applicable.

A value of `0.0` means that the observed metric value was zero.

A missing or unavailable metric is not represented as a false zero. Metric-level coverage is reported separately through the relevant `*_n`, `*_coverage_rate` and `*_coverage_status` fields.

A cell marked `complete` means that the planned execution set was completed.

A cell marked `remediated_complete` means that a limited collection issue was corrected under the same measurement configuration before aggregation.

---

## Public indicators

### Stability

Observed capacity of a system to produce comparable responses when the same question is repeated under comparable conditions.

Stability is not proof of factual accuracy.

### Coherence

Observed logical or structural consistency of generated responses under the campaign protocol.

Coherence is not proof of truth.

### Factual-risk signal

Observed indication of factual fragility according to the evaluation method used in this campaign.

This is not a universal truth score. It must be interpreted in relation to the question set, evaluation protocol, coverage and observation window.

### Semantic instability

Observed variation in the semantic content or useful meaning of responses across repeated executions.

Semantic variation is not, by itself, evidence of factual error.

### Decision behaviour

Observed distribution of `ALLOW`, `FLAG` and `ERROR` states.

These states describe the behaviour of the measurement and governance layer during the campaign. They do not constitute a safety certification or deployment decision.

### Inter-run variability

Observed variation between the three repeated execution waves.

This indicator is useful for identifying early variation patterns. It should not be interpreted as a long-horizon estimate of system stability.

### Latency band

Observed runtime latency is published in broad bands rather than as exact infrastructure-level timings.

This preserves useful operational context while reducing unnecessary re-identification exposure.

### `delta_g`

`delta_g` is published as an advanced observable runtime-variation signal.

It is reported as an output of the NeoMundi measurement framework. Its publication does not disclose its internal composition, thresholds, weighting logic or proprietary calculation rules.

No individual indicator should be interpreted in isolation as a complete assessment of quality, truthfulness, safety or governability.

---

## Public release boundary

This release publishes aggregated and de-identified results so that reported figures, coverage levels, decision distributions and visualisations can be publicly inspected.

It is deliberately bounded.

It does not represent the complete NeoMundi measurement record.

---

## What is intentionally not published

To preserve de-identification, methodological integrity and the distinction between public observation and private audit material, this release does not include:

- provider names;
- model names;
- the private identity mapping;
- API endpoints;
- infrastructure-routing details;
- raw prompts beyond the four published campaign questions;
- raw model outputs;
- precise timestamps;
- request traces;
- source filenames;
- private audit records;
- private implementation details;
- proprietary calculation logic;
- exact infrastructure-level latency traces;
- direct identifiers allowing systems to be named in the public release.

The release is de-identified. It is not presented as irreversibly anonymous.

No de-identification method can eliminate every theoretical re-identification risk when an external actor has access to comparable systems, prompts, timing conditions and execution infrastructure.

NeoMundi does not publish the identity mapping and retains it separately.

---

## Important interpretation boundary

This baseline documents observed runtime behaviour under a defined protocol and observation window.

It should be interpreted as:

- comparative;
- contextual;
- bounded by the protocol;
- reproducible at the level of inquiry conditions;
- unsuitable for universal claims about all future behaviour of a system.

The results do not establish that one de-identified profile is globally “better” or “worse” than another.

The objective is to observe behavioural signals, not to create a public league table.

> A signal is an observation requiring interpretation, not a verdict.

---

## Intended use

This release is intended to support:

- methodological review;
- AI runtime-observation research;
- analysis of stability, factual risk and behavioural variation;
- future longitudinal comparison;
- scientific contributions;
- governance-oriented review;
- the development of interpretable AI measurement practices.

Future Weekly Barometer releases may compare new observation campaigns with this baseline to identify meaningful changes in observed behaviour over time.

---

**NeoMundi Weekly Barometer**  
*Runtime measurement before governance claims.*
