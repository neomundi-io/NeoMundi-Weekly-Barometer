# NeoMundi Weekly Barometer #5 — Public Data Release

**Campaign:** `neomundi_barometer_05_2026-07-13_to_2026-07-19`
**Observation period:** 2026-07-13 to 2026-07-19
**Publication form:** Aggregated and de-identified

## Documentation

* [Public methodology — English](../../methodology.md)
* [Méthodologie publique — Français](../../methodologie.md)
* [Public baseline](../../baseline/)
* [Repository overview](../../README.md)

## What this release contains

* `public_overview.json` — campaign totals, global metrics, data-quality and dependency disclosures.
* `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
* `public_questions_summary.csv` — one aggregate row per de-identified question.
* `public_regime_distribution.csv` — observation-level regime shares and definitions.
* `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
* `public_manifest.json` — file inventory, integrity information and release provenance.

## What is deliberately not released

Provider and model identifiers, prompts, response content, request IDs, trace IDs, raw payloads, per-response timestamps, debugging material and the private profile-mapping registry are not included.

## Important interpretation constraint

The figures published in this release are measurement outputs. They must not be interpreted as an overall quality ranking, a safety certification, a truth guarantee or an authorisation to deploy a system in a particular context.

For this campaign, the release documents an observed dependency among `stability_score`, `v_score` and `factual_hallucination_score`.

These figures must not be treated as independent confirmations. The purpose of the release is to expose this methodological limitation rather than conceal it.

A semantic-variation signal does not, by itself, establish a factual error. A factual-risk signal is an observed alert requiring contextual interpretation, not a standalone final judgement.

## De-identification

Each observed system is mapped internally to a stable opaque profile identifier (`PROFILE-XXXXXX`) using an owner-maintained private profile registry.

Identifiers are not assigned according to performance, score, alphabetical order or rank. The mapping file remains private and is excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the published files and integrity information contained in `public_manifest.json`.

Full reproduction from source requires access to the private campaign exports under the NeoMundi Observatory governance process.
