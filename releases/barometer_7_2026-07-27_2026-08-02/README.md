# NeoMundi Weekly Barometer #7 — Public Data Release

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

## Public Release 2.1.0 improvements

This release strengthens the publication workflow through:

- strict validation of systems, questions, repetitions and duplicate observations;
- explicit separation of launched, non-error and fully scored executions;
- stable de-identification through an owner-maintained private profile registry;
- a canonical public metric contract and harmonised aggregate files;
- automatic generation of the release README, provenance manifest and integrity hashes;
- recorded builder, Python and pandas versions;
- automatic cleanup of partial output if generation fails.

These improvements concern release integrity, traceability and consistency.
They do not alter the source runtime observations.

## De-identification

Each observed system is mapped internally to a stable opaque profile identifier
(`PROFILE-XXXXXX`) using an owner-maintained private profile registry.

Identifiers are not assigned according to performance, score, alphabetical order
or rank. The mapping file remains private and is excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the published
files and integrity information contained in `public_manifest.json`.

Full reproduction from source requires access to the private campaign exports under
the NeoMundi Observatory governance process.
