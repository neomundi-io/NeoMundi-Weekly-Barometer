# NeoMundi Weekly Barometer — Baseline V1 Methodology

**Version:** `v1.1`  
**Status:** public baseline methodology  
**Scope:** quantitative, de-identified reference campaign used to establish the initial comparison frame of the NeoMundi Weekly Barometer

---

## 1. Purpose

Baseline V1 establishes the first public quantitative reference point of the **NeoMundi Weekly Barometer**.

It is designed to document AI runtime behaviour under repeated and controlled observation conditions before longitudinal weekly comparison begins.

The baseline is not a provider ranking, a model leaderboard, a certification or a universal assessment of AI quality.

Its purpose is to make future behavioural changes measurable against a fixed reference campaign.

---

## 2. Experimental design

The campaign includes:

```text
12 de-identified AI profiles
× 4 fixed questions
× 100 repetitions
× 3 execution waves
= 14,400 finalised observations
```

This represents:

```text
1,200 observations per profile
```

The same four questions were used across all profiles and waves.

Public profile identifiers use the stable opaque format:

```text
PROFILE-XXXXXX
```

The private mapping between public profiles and the observed systems is retained separately and is not included in this repository.

---

## 3. The four fixed questions

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

The four questions cover different response conditions and must not be reduced to a single universal indicator.

---

## 4. Public indicator families

### 4.1 Stability

Observed repeatability of responses under repeated and comparable measurement conditions.

Stability is not proof of factual accuracy.

### 4.2 Coherence

Observed logical or structural consistency of generated responses.

Coherence is not proof of truth.

### 4.3 Factual-risk signal

Protocol-specific indication that a response may require additional factual verification.

This is not a universal truth score and must be interpreted in relation to the question set, scoring method, coverage and observation window.

### 4.4 Semantic instability

Observed variation in the semantic content or useful meaning of responses across repeated executions.

Semantic variation is not, by itself, evidence of factual error.

### 4.5 Decision behaviour

Observed distribution of:

```text
ALLOW
FLAG
ERROR
```

These states describe the output of the measurement and governance layer during the campaign.

They do not constitute a safety certification, a compliance decision or a deployment authorisation.

### 4.6 Inter-run variability

Observed variation between the three execution waves.

This indicator supports comparison across repeated campaign runs but should not be interpreted as a long-term estimate of system stability.

### 4.7 Latency bands

Runtime latency is published in broad bands rather than as exact infrastructure-level timings.

This preserves operational context while reducing unnecessary re-identification exposure.

### 4.8 `delta_g`

`delta_g` is published as an advanced observable runtime-variation signal.

Its publication does not disclose its internal composition, thresholds, weighting logic or proprietary calculation rules.

No individual indicator should be interpreted in isolation as a complete assessment of quality, truthfulness, safety or governability.

---

## 5. Coverage and remediation

Execution-level completeness and metric-level coverage are reported separately.

### Execution status

`complete` means that the planned execution count was reached.

`remediated_complete` means that missing planned observations were later re-executed under the same measurement configuration and that the remediation count is reported.

`partial` means that fewer observations than planned were available.

### Metric status

`not_scored` means that no valid score was available for the relevant observation.

A measured value of `0.0` is distinct from a missing or unavailable score.

Metric-level sample size and coverage are published independently through the relevant `*_n`, `*_coverage_rate` and `*_coverage_status` fields.

No missing value is silently converted to zero.

---

## 6. Validation and integrity controls

Before publication, the release is checked for:

- expected observation totals;
- profile-question-wave completeness;
- duplicate or missing records;
- metric-level coverage;
- consistency of decision totals;
- remediation status;
- internal file consistency;
- removal of direct provider and model identifiers;
- absence of raw responses and private traces in public artefacts;
- consistency between the public manifest and the released files.

The verification result is documented in:

```text
VERIFICATION_SUMMARY.json
```

---

## 7. De-identification policy

The release is **de-identified**. It is not presented as irreversibly anonymous.

The following are not published:

- provider names;
- model names;
- API endpoints;
- routing details;
- raw responses;
- detailed execution traces;
- precise timestamps;
- private identity mapping;
- proprietary measurement logic.

Because the protocol and question families are public, residual re-identification risk cannot be eliminated entirely.

The objective is to prevent direct attribution while preserving sufficient transparency for methodological scrutiny.

---

## 8. Public release boundary

The baseline publishes aggregated quantitative measurements and documented coverage.

It does not publish the complete NeoMundi measurement record.

The private measurement boundary may contain execution-level observations, response artefacts, detailed runtime traces, cost and token data, internal diagnostics, review notes and the private profile mapping.

This separation supports public inspection without exposing confidential operational or identifying information.

---

## 9. No-ranking policy

This release does not order profiles from best to worst.

It publishes observed measurements and distributional information only.

Differences between profiles must not be interpreted as a universal hierarchy of model quality.

---

## 10. Interpretation boundary

The baseline documents behaviour observed under a defined protocol and observation window.

It does not establish:

- global model quality;
- universal factual reliability;
- safety certification;
- regulatory compliance;
- deployment suitability;
- causal attribution for future behavioural changes.

The correct interpretation is:

> a signal was observed under the conditions of the campaign.

A signal is an element of evidence requiring interpretation, not a verdict.

---

## 11. Relationship with the weekly protocol

Baseline V1 is an extended reference campaign.

The active weekly protocol is documented at the repository root in:

- `methodology.md`;
- `methodologie.md`.

Future weekly releases may be compared with this baseline to observe whether runtime behaviour remains comparable, varies progressively or indicates a potential regime change.

