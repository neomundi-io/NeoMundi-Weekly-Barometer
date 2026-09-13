# Technical incident note — Barometer 13 / v1/govern/stream

**Incident ID:** B13-STREAM-ENDPOINT-GOOGLE-OPENAI
**Status:** UNRESOLVED at the time of this exceptional edition
**Scope:** 2 of the 12 official Barometer 13 systems (public profile ids `PROFILE-5A5C60` and `PROFILE-F5FF91`; see `public_systems_status.csv` — real system identity is private per standard de-identification policy)
**Affected endpoint:** `https://api.neomundi.io/v1/govern/stream`

## Symptom

Every request to the affected systems' response-generation endpoint returned an HTTP-level success, but with no usable LLM response text. The client-side runner surfaced this as:

```
error_phase: stream
error: "The /stream endpoint returned no LLM response text."
decision: ERROR
```

This affected 100% of attempted requests for both systems, across every collection attempt.

## Timeline

| Attempt (UTC) | Scope | Rows usable | Note |
|---|---|---|---|
| 2026-09-11 ~23:39 | Full planned run (400 rows/system) | 0 / 800 | Initial wave; both systems errored identically on every row. |
| 2026-09-13 ~06:40 | Retry (interrupted) | 0 | Identical error from the first row. |
| 2026-09-13 ~08:08 | Retry (interrupted) | 0 | Identical error from the first row. |
| 2026-09-13 ~10:04 | Retry (interrupted), **after API credential rotation** | 0 | Identical error from the first row, immediately after both providers' API keys were rotated in the encrypted secrets store. |

## What this timeline rules out

Because the exact same failure persisted **after** a full credential rotation for both providers, an expired or invalid API key is very unlikely to be the sole cause. The evidence points to a gateway-side issue on the `/v1/govern/stream` route — most likely in how it routes or is configured for these two specific provider/model integrations — rather than the underlying provider APIs themselves. This has not been independently confirmed against NeoMundi's gateway-side logs; it is the most consistent explanation given the data collected from the client side.

## What was NOT done

- No provider was rerun in full beyond the four documented attempts above.
- No row was fabricated, imputed, or backfilled from a previous Barometer edition for these two systems.
- No coverage threshold was lowered or bypassed to work around this incident. The standard 90% publication gate in `build_barometer_release.py` was left unmodified, and the standard Barometer 13 release remains blocked as a direct result of this incident (real 12-system coverage: 82.9%, versus a required 90%).

## Data integrity

All four collection attempts for the affected systems were archived unmodified under `results/failed_runs/` (per-attempt audit manifests, byte-for-byte original files). None of that archived data was used as a substitute for real observations anywhere in this exceptional edition or in the (still-blocked) standard release.

## Recommended next steps (outside the scope of this repository's automation)

1. Verify GOOGLE_API_KEY and OPENAI_API_KEY validity directly against each provider's own API, independent of the NeoMundi gateway.
2. Check NeoMundi gateway-side routing/configuration for the `gemini-2.5-flash` and `gpt-4o-2024-11-20` model entries on the `/v1/govern/stream` route.
3. Once resolved, re-run only the two affected systems (400 observations each) through the standard supervised pipeline; do not re-run the 10 systems that already measured successfully.
4. Once combined 12-system coverage reaches 90%, the standard Barometer 13 release can be built and published through the normal, unmodified pipeline.
