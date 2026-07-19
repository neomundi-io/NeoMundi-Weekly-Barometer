🌐 **Language:** [English](./CALIBRATION.md) · [Français](./CALIBRATION.fr.md)

# NeoMundi Weekly Barometer

## Calibration Protocol

**Version:** `v1.0`  
**Status:** active technical support document  
**Purpose:** validate the measurement pipeline before a public campaign or any significant protocol change

---

## 1. Purpose of calibration

Calibration is a technical validation phase performed before:

- the first use of a measurement pipeline;
- the introduction of a new provider or model;
- a major change to prompts or parameters;
- a modification of the scoring pipeline;
- a change to aggregation or publication scripts;
- any protocol evolution that may affect longitudinal comparability.

Its purpose is to confirm that the measurement chain produces complete, traceable and interpretable records under controlled conditions.

Calibration is not, by default, a public Barometer release.

---

## 2. Relationship with the active protocol

The active NeoMundi Weekly Barometer protocol is defined in:

- `methodology.md` — English version;
- `methodologie.md` — French version.

The active weekly format is:

```text
12 de-identified AI profiles
× 4 fixed questions
× 100 repetitions
= 4,800 planned executions
```

The Public Baseline V1 is a separate extended reference campaign comprising:

```text
12 de-identified profiles
× 4 questions
× 100 repetitions
× 3 waves
= 14,400 finalised observations
```

Calibration must not introduce a competing protocol description.

---

## 3. Historical exploratory design

An earlier exploratory design considered:

- three fixed questions;
- one rotating sector-specific probe;
- one lightweight current-events probe.

This design was not adopted as the active public weekly protocol.

It may remain relevant as a future experimental extension, provided that it is:

- explicitly versioned;
- documented separately;
- not confused with the active four-question weekly protocol;
- analysed outside the canonical longitudinal series unless comparability is demonstrated.

---

## 4. Calibration objectives

A calibration run should verify:

- that all required fields are present;
- that prompts and parameters are correctly versioned;
- that the expected number of executions is produced;
- that no responses are silently truncated;
- that API errors are preserved and identifiable;
- that missing values are not silently converted to zero;
- that metrics are computed without unintended failures;
- that timestamps are coherent;
- that profile de-identification is applied correctly;
- that public exports contain no private identifiers;
- that aggregation scripts reproduce expected totals;
- that publication files remain internally consistent.

---

## 5. Recommended calibration format

The exact size of a calibration run may vary according to the change being tested.

A minimal technical calibration should remain small enough to inspect manually while covering every profile, question and pipeline branch concerned.

A recommended pattern is:

```text
all affected profiles
× all affected questions
× 3 repetitions
```

For the active weekly format, a complete micro-batch may therefore use:

```text
12 profiles
× 4 questions
× 3 repetitions
= 144 executions
```

A smaller subset may be used for a narrowly scoped technical change, provided that the limitation is documented.

---

## 6. Mandatory checks

### 6.1 Execution integrity

Verify:

- expected execution count;
- unique repetition indexes;
- no undocumented duplicates;
- no missing profile-question cells;
- complete campaign identifiers;
- coherent timestamps.

### 6.2 Prompt integrity

Verify:

- exact prompt text;
- prompt version;
- prompt hash where applicable;
- system prompt version where applicable;
- no undocumented wording variation.

### 6.3 Provider and runtime integrity

Verify, where available:

- requested model;
- returned model;
- endpoint;
- accepted parameters;
- `finish_reason` or `stop_reason`;
- token usage;
- latency;
- cost;
- provider-side errors.

### 6.4 Measurement integrity

Verify:

- expected metrics are present;
- failed scores remain identifiable;
- `not_scored` is distinct from a measured zero;
- metric-level coverage is computed correctly;
- dependencies between metrics are documented;
- no cohort-relative normalisation is introduced unintentionally.

### 6.5 Publication integrity

Verify:

- stable `PROFILE-XXXXXX` identifiers;
- no provider or model names in public outputs;
- no raw responses in public outputs;
- no precise execution timestamps in public outputs;
- public totals match validated private totals;
- exclusions and limitations are documented;
- manifest and file inventory are complete.

---

## 7. Acceptance criteria

A calibration may be accepted when:

- the expected execution set is complete or all deviations are documented;
- no critical traceability field is missing;
- errors and exclusions remain visible;
- scoring coverage is understood;
- public aggregates reproduce validated source totals;
- no private identifiers leak into public files;
- the change does not silently break longitudinal comparability.

If these conditions are not met, the calibration remains a technical test and must not be used as a public reference campaign.

---

## 8. Calibration record

Each calibration should retain, at minimum:

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

Recommended acceptance states:

```text
ACCEPTED
ACCEPTED_WITH_LIMITATIONS
REJECTED
```

---

## 9. Changes requiring recalibration

Recalibration is required when a change may affect:

- execution behaviour;
- response length or truncation;
- prompt interpretation;
- metric computation;
- regime classification;
- profile mapping;
- aggregation totals;
- public export structure;
- longitudinal comparability.

Examples include:

- adding or removing a model;
- changing generation parameters;
- modifying a fixed question;
- changing the scoring logic;
- updating the aggregation pipeline;
- changing de-identification rules;
- modifying public schemas.

---

## 10. Interpretation boundary

Calibration validates the technical reliability of the measurement chain.

It does not establish:

- the truthfulness of a system;
- the safety of a model;
- regulatory compliance;
- deployment suitability;
- the superiority of one provider over another.

Calibration confirms that the instrument is operating as intended within the tested scope.

> Calibration validates the measurement process. It does not validate the AI system itself.
