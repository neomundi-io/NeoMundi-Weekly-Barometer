# NeoMundi Barometer Tools

This directory contains the public visualisation tools used to generate the de-identified profile cartographies published with NeoMundi Weekly Barometer releases.

The objective is to make the public charts reproducible from the aggregated release data, while preserving the confidentiality of source systems, prompts, responses and operational traces.

## Files

* `generate_carto.py`
  Generates an interactive HTML cartography from a public `public_profiles_summary.csv` file.

* `chart_spec.json`
  Frozen French visual specification for the cartography.

* `chart_spec_en.json`
  Frozen English visual specification for the cartography.

## What the cartography shows

Each point represents one de-identified profile.

* The horizontal axis shows the measured factual-risk signal.
* The vertical axis shows semantic variation across comparable executions.
* Profiles are represented only through stable opaque identifiers in the format `PROFILE-XXXXXX`.
* A point that exceeds the published horizontal scale is represented with an arrow and its actual value remains visible.

The chart is not a leaderboard. It does not identify providers or models, and it must not be read as an overall quality, safety or truth ranking.

## Comparability rule

The French and English specifications use the same:

* axis bounds;
* projection formulas;
* point positions;
* colours;
* outlier rules;
* visual scale.

Only labels and explanatory text differ by language.

This frozen specification is intended to preserve direct visual comparability between weekly releases. Any modification to axis bounds, projection formulas or outlier treatment must be documented as a new specification version.

## Input data

The generator uses only the public aggregated file:

```text
public_profiles_summary.csv
```

Required columns:

```text
profile_id
factual_risk_mean
semantic_variation_rate
```

The source values are published as decimal proportions and are converted to percentages inside the script for display only. The CSV file is never modified.

## Example usage

French cartography:

```bash
python generate_carto.py \
  --input ../releases/barometer-02-2026-06-22-to-2026-06-29/public_profiles_summary.csv \
  --week 2 \
  --spec chart_spec.json \
  --output cartography_barometer_02_fr.html
```

English cartography:

```bash
python generate_carto.py \
  --input ../releases/barometer-02-2026-06-22-to-2026-06-29/public_profiles_summary.csv \
  --week 2 \
  --spec chart_spec_en.json \
  --output cartography_barometer_02_en.html
```

## Publicly released data

Weekly public releases may include:

* campaign totals and coverage information;
* aggregated profile summaries;
* aggregated summaries by question family;
* observation-regime distributions;
* metric definitions and interpretation limits;
* publication manifests and file hashes;
* de-identified interactive cartographies generated from public aggregates.

## Data deliberately not exposed

The public repository does not expose:

* provider identities;
* model names or deployment identifiers;
* the private mapping between providers, models and `PROFILE-XXXXXX` identifiers;
* prompts and prompt identifiers;
* model responses or response excerpts;
* raw execution-level data;
* request IDs, trace IDs or correlation IDs;
* raw API payloads and streaming payloads;
* per-response timestamps;
* API keys, credentials or environment variables;
* debugging material;
* internal diagnostic data;
* internal model-routing or transport information;
* private error logs;
* private evaluation notes;
* private operational context;
* client data, customer data or production workloads;
* internal governance payloads or decision records.

This boundary is intentional. The public release is designed to support verification of the published aggregates and visualisations without exposing confidential systems, prompts, responses or operational infrastructure.

## Interpretation boundary

Published metrics are measurement signals.

They are not:

* a provider ranking;
* a model leaderboard;
* a safety certification;
* a guarantee of factual truth;
* an authorisation to deploy a system in a specific context;
* a substitute for human review, governance or domain-specific validation.

A semantic-variation signal is not, by itself, evidence of a factual error. A factual-risk signal is a measured alert that requires contextual interpretation.

## Related resources

* Weekly public releases: `../releases/`
* Public baseline: `../baseline/`
* NeoMundi Observatory methodology: available through the Observatory publication pages.
