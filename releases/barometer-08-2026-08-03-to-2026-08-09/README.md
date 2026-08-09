# NeoMundi Weekly Barometer #8 — Public Data Release

[Version française](https://github.com/neomundi-io/NeoMundi-Weekly-Barometer/blob/main/releases/barometer-08-2026-08-03-to-2026-08-09/README_FR.md)

**Campaign:** `BAROMETER_8_2026-08-03_2026-08-09`  
**Observation period:** 2026-08-03 to 2026-08-09  
**Publication form:** Aggregated and de-identified

## Documentation

- [Public methodology — English](https://github.com/neomundi-io/NeoMundi-Weekly-Barometer/blob/main/docs/methodology_public_en.md)
- [Méthodologie publique — Français](https://github.com/neomundi-io/NeoMundi-Weekly-Barometer/blob/main/docs/methodology_public_fr.md)
- [Public baseline](https://github.com/neomundi-io/NeoMundi-Weekly-Barometer/blob/main/docs/public_baseline.md)
- [Repository overview](https://github.com/neomundi-io/NeoMundi-Weekly-Barometer/blob/main/README.md)

## Release snapshot

- Systems observed: 12
- Questions observed: 4
- Executions launched: 4,800
- Fully scored: 4,764
- Coverage: 99.25%
- Duplicate rows: 0

## Observed regime distribution

- Normal signal: 98.02% (4,705 observations)
- Semantic variation: 1.06% (51 observations)
- Factual alert: 0.17% (8 observations)
- Combined alert: 0.00% (0 observations)
- Incomplete measurement: 0.75% (36 observations)

## What this release contains

- `public_overview.json` — campaign totals, public global metrics and data-quality indicators.
- `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — one aggregate row per de-identified question.
- `public_regime_distribution.csv` — observation-level regime shares and definitions.
- `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
- `comparability_report.json` — formal longitudinal comparison with the preceding public release.
- `public_manifest.json` — file inventory, integrity information and release provenance.
- `build_barometer_release.py` — versioned release builder associated with the validation, aggregation, de-identification and generation of this release.

## Longitudinal comparability

**Status:** `COMPARABLE_WITH_RESERVATIONS`

- Previous campaign: `BAROMETER_7_2026-07-27_2026-08-02`
- Common longitudinal profiles: 12
- Current complete perimeter: 12
- Added profiles: 0
- Removed profiles: 0
- Questions unchanged: yes
- Repetitions unchanged: yes
- Published metrics unchanged: yes
- Duplicate observations: 0
- Reservations:
  - `PUBLIC_SCHEMA_VERSION_CHANGED`
  - `CURRENT_CAMPAIGN_INCOMPLETE_MEASUREMENTS`

The detailed comparison is published in `comparability_report.json`.

The public metric contract moved from schema version `1.2.0` to `1.3.0`. The comparison performed for this release did not identify a change in the compared metric definitions themselves.

The second reservation documents the presence of incomplete measurements within the current campaign: 4,764 of 4,800 executions were fully scored, corresponding to a coverage rate of 99.25%.

The comparability status documents protocol and public-release comparability conditions.

It does not validate metric performance, establish causal attribution, transform a measured signal into a verdict or constitute a general judgement about an observed system.

## Public Release 2.3.0 — Canonical workflow improvements

Barometer #8 introduces a new controlled intermediate layer between raw campaign results and the public release: the **canonical dataset**.

The release workflow now separates:

```text
raw results
→ inspection
→ repair plan
→ validated reruns
→ canonical dataset
→ public release
→ longitudinal comparability control
```

The canonical workflow was introduced to reduce manual handling while preserving source-data integrity and traceability.

For this campaign, the canonical dataset was validated against the expected campaign structure:

- 12 observed systems;
- 4 questions;
- 100 repetitions per system and question;
- 4,800 canonical observations;
- 0 duplicate observation keys;
- 0 missing canonical observations;
- validated replacement of only the observations explicitly identified in the repair plan.

Raw campaign files and rerun files remain unchanged.

Only validated replacements identified by the repair plan are incorporated into the canonical dataset.

## Public release builder

The builder associated with Barometer #8 is versioned as:

`2.3.0-canonical`

It operates from the validated canonical dataset rather than directly from the raw campaign directory.

The builder performs structural and integrity controls including:

- validation of the expected number of observed systems;
- validation of the expected number of questions and repetitions;
- validation of the expected number of executions;
- detection of duplicate observations;
- validation of required source columns;
- explicit separation of launched, non-error and fully scored executions;
- stable de-identification through an owner-maintained private profile registry;
- controlled handling of private provider/model aliases before de-identification;
- generation of harmonised aggregated public artefacts;
- generation of the public README, provenance manifest and integrity hashes;
- recording of builder, Python and pandas versions;
- formal longitudinal comparison with the preceding public release;
- automatic cleanup of partial output if generation fails.

Provider-specific identity resolution required before publication remains part of the private preprocessing and governance workflow.

The public release contains only de-identified aggregates.

## What is deliberately not released

Provider and model identifiers, prompts, response content, request IDs, trace IDs, raw payloads, per-response timestamps, debugging material, rerun material, repair plans, canonical private datasets and the private profile-mapping registry are not included.

## Important interpretation constraint

The figures published in this release are measurement outputs.

They must not be interpreted as an overall quality ranking, a safety certification, a truth guarantee or an authorisation to deploy a system in a particular context.

A semantic-variation signal does not, by itself, establish a factual error.

A factual-risk signal is an observed alert requiring contextual interpretation, not a standalone final judgement.

The published regimes describe observed measurement states under the conditions of this campaign.

They do not establish causal attribution or a general judgement about an observed system.

## De-identification

Each observed system is mapped internally to a stable opaque profile identifier (`PROFILE-XXXXXX`) using an owner-maintained private profile registry.

Identifiers are not assigned according to performance, score, alphabetical order or rank.

The mapping file remains private and is excluded from this release.

The same stable public identifiers are retained across comparable weekly campaigns in order to support longitudinal observation without publicly exposing provider or model identities.

## Methodological transition toward Barometer #9

Barometer #8 introduces two major additions to the weekly release workflow:

1. a canonical data layer between raw observations and publication;
2. formal longitudinal comparability control against the preceding public release.

Beginning with Barometer #9, the validated release stages are intended to be orchestrated through a single release launcher.

The target pipeline is:

```text
raw results
→ inspection
→ repair plan
→ validated reruns
→ canonical dataset
→ public release
→ longitudinal comparability control
→ FR/EN visual artefacts
→ FR/EN technical reports
```

The objective is to reduce repeated manual operations while preserving explicit validation gates, source-data immutability, provenance, reproducibility controls and human review before publication.

The visual publication workflow is also being standardised so that weekly maps retain fixed graphical specifications, axes and scales across editions, supporting consistent longitudinal reading.

Automation concerns the execution and publication workflow.

It does not automate scientific interpretation, causal attribution or the final decision to publish.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the published files, the metric contract, the comparability report and the integrity information contained in `public_manifest.json`.

The published builder provides additional transparency regarding the validation, aggregation, de-identification and publication workflow.

Full reproduction from source requires access to:

- the private campaign exports;
- validated rerun material where applicable;
- the canonical preprocessing environment;
- the private profile registry;
- the governed NeoMundi Observatory execution environment.

These elements remain outside the public release.
