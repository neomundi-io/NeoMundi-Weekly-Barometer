# NeoMundi Weekly Barometer — Public Data Release

**Campaign:** `neomundi_barometer_2026_04`  
**Observation period:** 2026-07-07 to 2026-07-13  
**Publication form:** aggregated and de-identified

## What this release contains

- `public_overview.json` — campaign totals, global metrics, data-quality and dependency disclosures.
- `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — one aggregate row per de-identified question.
- `public_regime_distribution.csv` — observation-level regime shares and definitions.
- `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
- `public_manifest.json` — file inventory and release provenance.

## What is deliberately not released

Provider/model identifiers, prompts, response content, request IDs, trace IDs, raw payloads,
per-response timestamps and debugging material are not included.

## Important interpretation constraint

For this campaign, the release documents an observed dependency among `stability_score`,
`v_score` and `factual_hallucination_score`. These figures must not be treated as independent
confirmations. The purpose of the release is to expose this limitation rather than conceal it.

## Anonymisation

Each observed system is mapped internally to a stable opaque profile identifier (`PROFILE-XXXXXX`)
using an owner-maintained private profile registry. Identifiers are not assigned by performance, score, alphabetical order,
or rank. The mapping file is private and excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency. Reproduction from source requests
access to the private campaign exports under the Observatory's governance process.
