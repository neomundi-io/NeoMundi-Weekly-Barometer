# NeoMundi Weekly Barometer #7 — Public Data Release

[Version française](README_FR.md)

**Campaign:** `BAROMETER_7_2026-07-27_2026-08-02`  
**Observation period:** 2026-07-27 to 2026-08-02  
**Publication form:** Aggregated and de-identified

## Documentation

- [Public methodology — English](../../docs/methodology_public_en.md)
- [Méthodologie publique — Français](../../docs/methodology_public_fr.md)
- [Public baseline](../../docs/public_baseline.md)
- [Repository overview](../../README.md)

## Release snapshot

- Systems observed: 12
- Questions observed: 4
- Executions launched: 4,800
- Fully scored: 4,774
- Coverage: 99.46%
- Duplicate rows: 0

## Observed regime distribution

- Normal signal: 97.25% (4,668 observations)
- Semantic variation: 1.29% (62 observations)
- Factual alert: 0.65% (31 observations)
- Combined alert: 0.27% (13 observations)
- Incomplete measurement: 0.54% (26 observations)

## What this release contains

- `public_overview.json` — campaign totals, public global metrics and data-quality indicators.
- `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — one aggregate row per de-identified question.
- `public_regime_distribution.csv` — observation-level regime shares and definitions.
- `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
- `public_manifest.json` — file inventory, integrity information and release provenance.
- `build_public_barometer_release.py` — versioned public builder associated with the validation, aggregation and generation of this release.

## Public release builder

The public builder associated with Barometer #7 is included in this release to document the validation, aggregation and publication workflow used for this campaign.

The script performs structural and integrity controls, including:

- validation of the expected number of observed systems;
- validation of the expected number of questions and repetitions;
- validation of the expected number of executions;
- detection of duplicate observations;
- validation of required source columns;
- explicit separation of launched, non-error and fully scored executions;
- stable de-identification through an owner-maintained private profile registry;
- generation of harmonised aggregated public artefacts;
- generation of the public README, provenance manifest and integrity hashes;
- recording of builder, Python and pandas versions;
- automatic cleanup of partial output if generation fails.

The published builder contains no provider-specific or model-specific aliases.

Any exceptional identity mapping required before publication remains part of the private preprocessing and governance workflow.

The README and other documentation files may subsequently receive editorial clarifications without changing the source runtime observations or the published aggregate results.

## What is deliberately not released

Provider and model identifiers, prompts, response content, request IDs, trace IDs,
raw payloads, per-response timestamps, debugging material and the private
profile-mapping registry are not included.

## Important interpretation constraint

The figures published in this release are measurement outputs. They must not be
interpreted as an overall quality ranking, a safety certification, a truth guarantee
or an authorisation to deploy a system in a particular context.

A semantic-variation signal does not, by itself, establish a factual error.

A factual-risk signal is an observed alert requiring contextual interpretation,
not a standalone final judgement.

The published regimes describe observed measurement states under the conditions
of this campaign. They do not establish causal attribution or a general judgement
about an observed system.

## Public Release 2.1.0 improvements

Compared with the previous public release workflow, Barometer #7 strengthens:

- validation of systems, questions, repetitions and duplicate observations;
- explicit separation of launched, non-error and fully scored executions;
- stable de-identification through an owner-maintained private profile registry;
- use of a canonical public metric contract;
- harmonisation of profile, question and regime aggregate files;
- automatic generation of the release README;
- automatic generation of the provenance manifest;
- generation of SHA-256 integrity hashes;
- recording of the builder version;
- recording of the Python and pandas versions;
- automatic cleanup of partial output if generation fails.

These improvements concern release integrity, traceability, consistency and auditability.

They do not alter the source runtime observations and do not constitute a new scientific validation of the published metrics.

## Methodological transition toward Barometer #8

Barometer #7 marks a transition between the consolidation of the public release workflow and the introduction of a formal longitudinal comparability control.

Beginning with Barometer #8, the publication pipeline is planned to include an automated comparison between the current campaign protocol and the preceding campaign.

The planned control will examine, where applicable:

- the question corpus;
- the expected number of repetitions;
- the common observed-system perimeter;
- the complete observed-system perimeter;
- the published metrics;
- the aggregation rules;
- changes to the public release pipeline;
- missing observations;
- execution errors;
- additions to or removals from the observed cohort.

The planned output will distinguish between:

- `DIRECTLY_COMPARABLE`;
- `COMPARABLE_WITH_RESERVATIONS`;
- `NOT_DIRECTLY_COMPARABLE`.

The comparison will also distinguish:

1. the stable longitudinal perimeter shared by the two campaigns;
2. the complete perimeter of the current campaign.

This future addition concerns the traceability of longitudinal interpretation.

It will not:

- validate the scientific performance of an individual metric;
- establish causal attribution;
- transform a measured signal into a verdict;
- provide a general quality ranking of observed systems.

The implementation used for Barometer #8 will be versioned and published with that release.

## De-identification

Each observed system is mapped internally to a stable opaque profile identifier
(`PROFILE-XXXXXX`) using an owner-maintained private profile registry.

Identifiers are not assigned according to performance, score, alphabetical order
or rank.

The mapping file remains private and is excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the published
files and integrity information contained in `public_manifest.json`.

The published builder provides additional transparency regarding the validation,
aggregation and publication workflow.

Full reproduction from source requires access to the private campaign exports,
the private profile registry and the governed preprocessing environment under
the NeoMundi Observatory governance process.
