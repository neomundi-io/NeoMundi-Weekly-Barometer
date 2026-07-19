🌐 **Language:** [English](./methodology.md) · [Français](./methodologie.md)

# NeoMundi Weekly Barometer

## Methodology of the NeoMundi Weekly Barometer

**Version:** `v2.0`  
**Status:** active public protocol  
**Purpose:** longitudinal, repeated and multi-signal observation of generative AI runtime behaviour

---

## 1. Project purpose

The **NeoMundi Weekly Barometer** is a recurring measurement programme designed to observe how the behaviour of generative AI systems evolves over time.

Traditional benchmarks generally evaluate a model at a given moment on a predefined set of tasks.

The NeoMundi Barometer pursues a complementary objective:

> to observe the behavioural trajectories of AI systems and make visible the changes that may appear silently from one week to the next.

The project is not intended to produce a commercial ranking, a leaderboard or a general certification of the systems observed.

It is designed to produce repeated, comparable and documented measurements capable of characterising:

- stability;
- semantic variation;
- coherence;
- factual-risk signals;
- behavioural regimes;
- measurement coverage;
- selected variations in cost, latency or runtime effort where available.

The Barometer therefore acts as an instrument for the longitudinal observation of AI behaviour.

---

## 2. Core hypothesis

A single response is not sufficient to characterise the behaviour of a generative system.

When the same prompt is submitted one hundred times to the same system under controlled conditions, it becomes possible to observe:

- response repeatability;
- dispersion;
- semantic variation;
- coherence;
- factual-risk signals;
- decision states or regimes produced by the measurement pipeline;
- errors and incomplete measurements;
- associated runtime variations.

When this operation is repeated every week using the same questions and a comparable measurement pipeline, successive campaigns form a longitudinal series.

The methodological shift therefore does not lie in repetition alone.

It lies in the transition:

> from point-in-time measurement to the observation of behaviour over time.

---

## 3. General protocol architecture

### 3.1 Weekly format

Each weekly campaign includes:

```text
12 de-identified AI profiles
× 4 fixed questions
× 100 repetitions
= 4,800 planned executions
```

Public profiles are represented by stable opaque identifiers in the following format:

```text
PROFILE-XXXXXX
```

These identifiers do not correspond to a ranking, a performance level or a provider category.

The mapping between public identifiers and the systems observed is retained in a separate private registry.

---

### 3.2 Measurement window

The reference weekly window is:

```text
Monday 00:00 UTC
to
Sunday 23:59 UTC
```

Executions must be timestamped to preserve campaign traceability and support longitudinal comparison.

The public release may be published after the measurement window closes, once validation, aggregation and control procedures have been completed.

---

### 3.3 Comparability conditions

Comparability across campaigns relies in particular on:

- maintaining the same four fixed questions;
- explicit prompt versioning;
- a documented execution policy;
- a controlled measurement pipeline;
- a consistent de-identification procedure;
- systematic file validation;
- preservation of actual coverage;
- no silent replacement of missing data;
- versioning of generation and analysis scripts.

Any significant protocol modification must be documented in the manifest of the relevant release.

---

## 4. The four fixed questions

The four questions cover distinct response conditions.

### Question 1 — Reasoning

**Bat and ball problem**

> A bat and a ball cost €1.10 in total.  
> The bat costs €1 more than the ball.  
> How much does the ball cost?

This question is used to observe, among other things:

- the repeatability of a short reasoning task;
- the stability of the final answer;
- the possible persistence of an intuitive error;
- the relationship between stability and accuracy.

---

### Question 2 — Scientific explanation

**Seasons on Earth**

> Why do seasons occur on Earth?

This question is used to observe, among other things:

- the stability of a scientific explanation;
- structural variations;
- omissions;
- simplifications;
- factual-risk signals;
- explanatory coherence.

---

### Question 3 — Open conceptual question

**Stability and truth**

> Why is a stable AI response not necessarily factually correct?

This question is used to observe, among other things:

- understanding of the distinction between repeatability and truth;
- quality of argumentation;
- conceptual coherence;
- semantic variation;
- styles of caution.

---

### Question 4 — Open epistemic question

**Widely accepted but potentially false beliefs**

> Give an example of a widely accepted belief that may be false, and explain how it could be checked.

This question is used to observe, among other things:

- spontaneous example selection;
- epistemic caution;
- proposed verification strategies;
- variation in generated content;
- the risk of stable repetition of an incorrect claim.

---

## 5. Why the four questions remain separate

The four questions must not be reduced to a single indicator.

They cover different cognitive and behavioural conditions:

| Question | Main observed condition |
|---|---|
| `Q01` | Short reasoning and determined answer |
| `Q02` | Scientific explanation |
| `Q03` | Conceptual understanding of stability |
| `Q04` | Epistemic variation and open response |

A variation observed on an open question does not necessarily have the same meaning as a variation observed on a closed question.

Results should therefore be analysed:

- globally;
- by profile;
- by question;
- by metric;
- over time.

---

## 6. Public Baseline V1

Baseline V1 is the first public quantitative reference of the Barometer.

It includes:

```text
12 de-identified profiles
× 4 questions
× 100 repetitions
× 3 waves
= 14,400 finalised observations
```

The baseline is not an ordinary weekly campaign.

It is an extended reference campaign designed to establish an initial stable quantitative frame.

It is used in particular to:

- observe initial measurement dispersion;
- document differences between questions;
- establish an initial comparison point;
- identify coverage limitations;
- distinguish ordinary variations from potentially significant changes.

Subsequent weekly campaigns may be compared with this reference, without every difference being automatically classified as drift.

---

## 7. Observed signals

Depending on the campaign and available coverage, the Barometer publishes or documents several categories of signals.

### 7.1 Stability

Stability describes the degree of repeatability of responses generated under comparable conditions.

It does not constitute proof of accuracy.

A response may be:

- stable and correct;
- stable and incorrect;
- variable and correct;
- variable and incorrect.

---

### 7.2 Semantic variation

Semantic variation describes differences in content or formulation observed between responses generated from the same question.

Semantic variation is not, by itself, an error.

It may reflect:

- reformulation;
- a structural change;
- a difference in depth;
- a change of example;
- a more significant change in the content produced.

---

### 7.3 Factual risk

A factual-risk signal indicates that a response presents characteristics requiring additional verification.

It is not a legal judgement or a certification that the response is false.

It must be interpreted alongside:

- the question concerned;
- the level of coverage;
- the other signals;
- the limitations of the scoring procedure;
- any dependencies between metrics.

---

### 7.4 Coherence

Coherence describes the observable logical or structural continuity of a response.

A coherent response is not necessarily true.

Conversely, a variation in coherence does not by itself establish a general degradation of the system.

---

### 7.5 Regimes and observation states

Releases may include states such as:

```text
NORMAL
SEMANTIC_VARIATION
FACTUAL_ALERT
INCOMPLETE_MEASUREMENT
```

or technical and decision states documented in the campaign files.

These categories are used to organise observations.

They are neither rankings nor universal levels of quality.

---

### 7.6 `delta_g`

`delta_g` is published as an advanced observable runtime-variation signal.

Its publication does not disclose:

- its full internal composition;
- its proprietary thresholds;
- its weighting logic;
- the complete set of calculation rules.

It must not be interpreted in isolation as a verdict on a system.

---

### 7.7 Coverage and completeness

Coverage indicates the proportion of executions or metrics for which a valid measurement could be produced.

A campaign may complete all planned executions while still presenting metric-level coverage slightly below 100%.

Errors, missing data and unscored observations must not be silently replaced with zero.

---

## 8. Interpretation doctrine

The Barometer follows one fundamental rule:

> a signal is not a verdict.

An observation alone does not establish:

- that a system is systematically truthful;
- that one system is globally superior to another;
- that a change results from a model update;
- that a variation constitutes degradation;
- that a stable response is reliable;
- that a variable response is incorrect;
- that a system complies with a regulatory requirement;
- that a system may be deployed without additional controls.

The appropriate formulation is:

> a behavioural change was observed under the conditions of the campaign.

Attributing a cause requires additional evidence.

Possible causes may include:

- a model evolution;
- a routing modification;
- a configuration change;
- an API modification;
- an adjustment to provider policies;
- an infrastructure variation;
- an internal experiment;
- statistical fluctuation;
- a change in the measurement pipeline.

---

## 9. Longitudinal observation

The primary value of the Barometer lies in repeated campaigns.

An isolated observation describes a state.

A sequence of campaigns makes it possible to observe:

- persistent stability;
- progressive variation;
- a return to a previous regime;
- a temporary break;
- a plateau;
- a persistent anomaly;
- a question-specific evolution.

A variation should not be publicly classified as drift on the basis of one indicator or one campaign without additional analysis.

Interpretation must take into account:

- the magnitude of the change;
- its persistence;
- the number of signals concerned;
- campaign coverage;
- any technical errors;
- the natural variation observed in previous campaigns.

---

## 10. Detecting regime changes

A change may be examined as a potential regime change when it:

- exceeds the variations usually observed;
- affects several coherent signals;
- does not result from a known pipeline error;
- does not result from truncation;
- has sufficient coverage;
- persists over time or presents an exceptional and documented magnitude.

Detecting a change does not amount to attributing a cause.

Public results should distinguish:

1. the observation;
2. the interpretation;
3. any causal hypothesis.

---

## 11. Data validation

Each campaign must undergo validation before aggregation and publication.

Validation checks include, in particular:

- the expected number of executions;
- the presence of the expected profiles and questions;
- the consistency of repetition indexes;
- the absence of undocumented duplicates;
- the presence of timestamps;
- the consistency of source files;
- the presence of expected metrics;
- the identification of errors;
- the identification of unscored observations;
- coverage by metric;
- the consistency of script versions;
- conformity with the private de-identification mapping.

No silent interpolation should be applied.

Any excluded or incomplete observation must remain identifiable in working data or in public limitation files.

---

## 12. Technical traceability

Depending on pipeline and provider capabilities, private records may include:

```text
campaign_id
week_id
run_id
repetition_index
question_id
prompt_version
timestamp_utc
profile_id
requested_model
returned_model
endpoint
finish_reason
input_tokens
output_tokens
latency_ms
cost
pipeline_version
analysis_version
validation_status
exclusion_reason
```

The actual availability of each field may vary across providers and campaigns.

Public releases must not imply that a field is available when it is not.

---

## 13. De-identification

Public results are released in aggregated and de-identified form.

Provider names, model names, endpoints, raw responses, detailed traces and precise timestamps are not included in public releases.

Profiles use stable opaque identifiers in the following format:

```text
PROFILE-XXXXXX
```

The private mapping between these identifiers and the observed systems is retained separately.

De-identification must not be presented as irreversible anonymisation.

Indirect re-identification may remain theoretically possible when a third party has:

- comparable access to the models;
- similar execution conditions;
- access to the public protocol;
- sufficient behavioural-comparison capabilities.

This residual risk is documented.

---

## 14. Boundary between public and private data

### Public data

Releases may include:

- aggregates by profile;
- aggregates by question;
- regime distributions;
- coverage levels;
- visualisations;
- campaign metadata;
- exclusions and interpretation limits.

### Private data

The private record may include:

- individual responses;
- execution traces;
- the actual identities of the systems;
- routing details;
- precise timestamps;
- complete technical prompts;
- cost data;
- pipeline diagnostics;
- review notes;
- intermediate results;
- artefacts required for technical investigation.

This separation makes public results inspectable without exposing information that could enable direct exploitation or re-identification of the systems.

---

## 15. Weekly deliverables

Each campaign may generate several categories of deliverables.

### Private deliverables

- execution files;
- scoring files;
- validation files;
- campaign manifest;
- error and exclusion log;
- internal aggregates;
- longitudinal analyses;
- private mapping registry;
- versioned archives.

### Public deliverables

- aggregated de-identified data;
- principal indicators;
- distributions by question or profile;
- campaign coverage;
- interpretation limits;
- visualisations;
- an article or editorial note;
- a public manifest.

---

## 16. Methodological limitations

The Barometer relies on a limited set of fixed questions.

It does not represent every possible use of an AI system.

Results are conditioned by:

- the selected prompts;
- execution parameters;
- models available at the time of the campaign;
- provider policies;
- routing mechanisms;
- API availability;
- the metrics used;
- scoring methods;
- infrastructure conditions.

Observations should therefore not be generalised beyond the measured scope without additional validation.

---

## 17. What the Barometer is not

The NeoMundi Weekly Barometer is not:

- a provider ranking;
- a model leaderboard;
- a safety certification;
- a guarantee of truth;
- an exhaustive quality assessment;
- a regulatory determination;
- automatic proof of compliance;
- a deployment authorisation;
- a substitute for human supervision;
- a substitute for a domain-specific assessment.

It is a public metrological instrument for observing AI runtime behaviour over time.

---

## 18. Scientific doctrine

The protocol follows six principles:

1. **Measure before interpreting.**
2. **Repeat before generalising.**
3. **Characterise variation before declaring drift.**
4. **Never confuse stability with truth.**
5. **Distinguish observation, interpretation and causal attribution.**
6. **Treat every signal as an element of evidence, not as a verdict.**

---

## 19. Public positioning

> Benchmarks capture AI systems at a given moment.  
> NeoMundi observes their trajectories.
>
> Each week, the Barometer tracks several signals of their runtime behaviour under repeated and controlled conditions.
>
> The objective is not to produce another ranking.
>
> It is to make visible the variations and silent changes that appear over time.

---

## 20. Protocol status

The NeoMundi Weekly Barometer is an active protocol.

Its Public Baseline V1 consists of 14,400 finalised observations.

Weekly campaigns are based on 4,800 planned executions and progressively form a public longitudinal series.

The protocol, metrics and publication formats may evolve.

Any significant evolution must be:

- versioned;
- documented;
- distinguished from previous campaigns;
- accompanied by its comparability limitations.

The Barometer is designed to build durable infrastructure for observing what point-in-time evaluations do not reveal:

> the evolution of AI system behaviour over time.
