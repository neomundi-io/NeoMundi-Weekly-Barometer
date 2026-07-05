#!/usr/bin/env python3
"""
NeoMundi Baromètre — Générateur de cartographie interactive
============================================================
Usage :
    python generate_carto.py --input public_profiles_summary.csv --week 2
    python generate_carto.py --input public_profiles_summary.csv --week 2 --output carto_w2.html

Schéma CSV source officiel NeoMundi (public_profiles_summary.csv) :
    profile_id, executions_total, executions_fully_scored, coverage_rate,
    stability_mean, validity_signal_mean, factual_risk_mean,
    semantic_variation_rate, coherence_mean, flag_rate, error_rate,
    dominant_regime

Mapping vers les valeurs graphiques (conversion effectuée dans ce script
uniquement — le CSV source n'est jamais modifié) :
    factual_risk_mean   × 100  →  factual_risk_pct   (axe X, 0–2,5 %)
    semantic_variation_rate × 100  →  semantic_variation_pct  (axe Y, 0–12 %)

Le numéro de baromètre est fourni via --week (non requis dans le CSV).

Spécification graphique : chart_spec.json (même répertoire que ce script).
La source de vérité graphique est le JSON. Ce script ne modifie jamais les axes.
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime
from html import escape
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SPEC_FILE  = SCRIPT_DIR / "chart_spec.json"


# ── Chargement de la spécification ──────────────────────────────────────────

def load_spec(spec_path: Path) -> dict:
    if not spec_path.exists():
        sys.exit(f"[ERREUR] Fichier de spécification introuvable : {spec_path}")
    with open(spec_path, encoding="utf-8") as f:
        return json.load(f)


# ── Chargement et validation du CSV ─────────────────────────────────────────

# Colonnes requises dans le schéma officiel public_profiles_summary.csv
REQUIRED_COLUMNS = {
    "profile_id",
    "factual_risk_mean",
    "semantic_variation_rate",
}

# Colonnes présentes dans le schéma complet (pour information dans les erreurs)
FULL_SCHEMA = {
    "profile_id", "executions_total", "executions_fully_scored", "coverage_rate",
    "stability_mean", "validity_signal_mean", "factual_risk_mean",
    "semantic_variation_rate", "coherence_mean", "flag_rate", "error_rate",
    "dominant_regime",
}


def load_data(csv_path: Path, week: int) -> list[dict]:
    """
    Lit le CSV officiel NeoMundi public_profiles_summary.csv.
    Convertit les proportions décimales en pourcentages graphiques.
    Ne modifie jamais le fichier source.
    """
    if not csv_path.exists():
        sys.exit(f"[ERREUR] Fichier CSV introuvable : {csv_path}")

    rows = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        actual_cols = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - actual_cols
        if missing:
            sys.exit(
                f"[ERREUR] Colonnes manquantes dans le CSV source :\n"
                f"  Absentes   : {', '.join(sorted(missing))}\n"
                f"  Trouvées   : {', '.join(sorted(actual_cols))}\n"
                f"  Requises   : {', '.join(sorted(REQUIRED_COLUMNS))}\n"
                f"  Schéma complet attendu : {', '.join(sorted(FULL_SCHEMA))}"
            )

        for i, row in enumerate(reader, start=2):
            try:
                # Lecture des proportions décimales (0–1)
                fact_prop = float(row["factual_risk_mean"])
                sem_prop  = float(row["semantic_variation_rate"])
            except ValueError as e:
                sys.exit(
                    f"[ERREUR] Ligne {i} — valeur non numérique dans "
                    f"'factual_risk_mean' ou 'semantic_variation_rate' : {e}"
                )

            # Validation des plages décimales attendues
            for col_name, val in [("factual_risk_mean", fact_prop),
                                   ("semantic_variation_rate", sem_prop)]:
                if not (0.0 <= val <= 1.0):
                    sys.exit(
                        f"[ERREUR] Ligne {i} — '{col_name}' = {val} hors plage [0, 1].\n"
                        f"  Ce fichier attend des proportions décimales, pas des pourcentages.\n"
                        f"  Si votre CSV contient déjà des pourcentages (valeurs > 1), "
                        f"il ne correspond pas au schéma officiel."
                    )

            # Conversion en pourcentage graphique — uniquement ici, jamais dans le CSV
            rows.append({
                "profile_id":            row["profile_id"].strip(),
                "factual_risk_pct":      round(fact_prop * 100, 6),
                "semantic_variation_pct": round(sem_prop  * 100, 6),
                "barometer_week":        week,
            })

    if not rows:
        sys.exit(f"[ERREUR] Le CSV ne contient aucune ligne de données.")
    return rows


# ── Projection coordonnées ───────────────────────────────────────────────────

def project(spec: dict, fact: float, sem: float) -> tuple[float, float]:
    ax  = spec["axes"]["x"]
    ay  = spec["axes"]["y"]
    can = spec["canvas"]
    cx = can["plot_x_min_px"] + fact * ax["px_per_unit"]
    cy = can["plot_y_min_px"] - sem  * ay["px_per_unit"]
    return round(cx, 2), round(cy, 2)


def is_x_outlier(spec: dict, fact: float) -> bool:
    return fact > spec["axes"]["x"]["domain_max"]

def is_y_outlier(spec: dict, sem: float) -> bool:
    return sem > spec["axes"]["y"]["domain_max"]


# ── Génération SVG des points ────────────────────────────────────────────────


def render_points(spec: dict, profiles: list[dict], marker_id: str = "arrOutlier") -> tuple[str, str]:
    """
    Returns (points_inside_plot, off_scale_profile_rail).

    Axis bounds remain unchanged across releases. Profiles beyond the main
    horizontal scale are displayed in a side rail, preserving their actual
    value and vertical position without crowding the plot.
    """
    C = spec["colors"]
    V = spec["vocabulary"]
    UI = spec.get("ui", {})
    lang = UI.get("html_lang", "fr").lower()

    ax = spec["axes"]["x"]
    ay = spec["axes"]["y"]
    can = spec["canvas"]

    decimal_separator = "." if lang == "en" else ","
    if lang == "en":
        outlier_title = "Beyond the main scale"
        outlier_subtitle = "more than {cutoff} % of responses need verification"
        responses_label = "responses needing more verification"
        semantic_label = "change in response meaning"
    else:
        outlier_title = "Au-delà de l’échelle principale"
        outlier_subtitle = "plus de {cutoff} % de réponses à vérifier"
        responses_label = "réponses à vérifier"
        semantic_label = "variation du sens"

    normal_pts = []
    outliers = []

    for p in profiles:
        pid = escape(p["profile_id"])
        fact = p["factual_risk_pct"]
        sem = p["semantic_variation_pct"]
        fact_fmt = f"{fact:.2f}".replace(".", decimal_separator)
        sem_fmt = f"{sem:.2f}".replace(".", decimal_separator)

        if is_x_outlier(spec, fact):
            _, actual_cy = project(spec, ax["domain_max"], sem)
            actual_cy = max(
                can["plot_y_max_px"] + 6,
                min(can["plot_y_min_px"] - 6, actual_cy),
            )
            outliers.append(
                {
                    "pid": pid,
                    "fact": fact,
                    "sem": sem,
                    "fact_fmt": fact_fmt,
                    "sem_fmt": sem_fmt,
                    "actual_cy": actual_cy,
                }
            )
        elif is_y_outlier(spec, sem):
            cx, _ = project(spec, fact, ay["domain_max"])
            cy = can["plot_y_max_px"]
            normal_pts.append(f"""
  <circle class="pt" cx="{cx}" cy="{cy}" r="6" fill="{C['point_fill']}"
          data-id="{pid}" data-fact="{fact_fmt}" data-sem="{sem_fmt}"/>
  <text x="{cx + 8}" y="{cy - 4}" font-size="10" fill="{C['annotation_text']}">{sem_fmt} %↑</text>""")
        else:
            cx, cy = project(spec, fact, sem)
            normal_pts.append(f"""
  <circle class="pt" cx="{cx}" cy="{cy}" r="6" fill="{C['point_fill']}"
          data-id="{pid}" data-fact="{fact_fmt}" data-sem="{sem_fmt}"/>""")

    rail = []
    if outliers:
        outliers.sort(key=lambda item: item["fact"], reverse=True)

        rail_x = can["plot_x_max_px"] + 28
        rail_w = 210
        card_h = 60
        card_gap = 14
        rail_top = can["plot_y_max_px"] + 28
        edge_x = can["plot_x_max_px"]
        cutoff = f"{ax['domain_max']:.1f}".replace(".", decimal_separator)

        rail.append(f"""
  <line x1="{edge_x + 7}" y1="{can['plot_y_max_px']}" x2="{edge_x + 7}" y2="{can['plot_y_min_px']}"
        stroke="{C['outlier_arrow']}" stroke-width="1.2" stroke-dasharray="3 4" opacity="0.65"/>
  <text x="{rail_x}" y="{rail_top - 18}" font-size="12" fill="{C['annotation_text']}" font-weight="600">
    {outlier_title}
  </text>
  <text x="{rail_x}" y="{rail_top - 4}" font-size="10.5" fill="{C['annotation_text']}">
    {outlier_subtitle.format(cutoff=cutoff)}
  </text>""")

        for index, item in enumerate(outliers):
            card_y = rail_top + index * (card_h + card_gap)
            rail.append(f"""
  <circle class="pt" cx="{edge_x}" cy="{item['actual_cy']}" r="6"
          fill="{C['outlier_arrow']}"
          data-id="{item['pid']}" data-fact="{item['fact_fmt']}" data-sem="{item['sem_fmt']}"/>
  <rect x="{rail_x}" y="{card_y}" width="{rail_w}" height="{card_h}" rx="5"
        fill="{C['outlier_badge_fill']}"/>
  <rect x="{rail_x}" y="{card_y}" width="5" height="{card_h}" rx="2"
        fill="{C['outlier_arrow']}"/>
  <text x="{rail_x + 16}" y="{card_y + 17}" font-size="11"
        fill="{C['outlier_badge_text']}" font-weight="650">{item['pid']}</text>
  <text x="{rail_x + 16}" y="{card_y + 37}" font-size="18"
        fill="{C['outlier_badge_text']}" font-weight="700">{item['fact_fmt']} %</text>
  <text x="{rail_x + 80}" y="{card_y + 35}" font-size="10.5"
        fill="{C['outlier_badge_text']}">{responses_label}</text>
  <text x="{rail_x + 16}" y="{card_y + 52}" font-size="10.5"
        fill="{C['outlier_badge_text']}">{semantic_label}: {item['sem_fmt']} %</text>""")

    return "\n".join(normal_pts), "\n".join(rail)

# ── Génération des graduations ───────────────────────────────────────────────


def render_ticks(spec: dict) -> str:
    ax = spec["axes"]["x"]
    ay = spec["axes"]["y"]
    can = spec["canvas"]
    C = spec["colors"]
    lang = spec.get("ui", {}).get("html_lang", "fr").lower()
    decimal_separator = "." if lang == "en" else ","
    lines = []

    # X ticks
    for v in ax["ticks"]:
        cx = can["plot_x_min_px"] + v * ax["px_per_unit"]
        label = str(v).replace(".", decimal_separator) if v != int(v) else str(int(v))
        if v > 0:
            lines.append(
                f'<line x1="{cx:.1f}" y1="{can["plot_y_max_px"]}" x2="{cx:.1f}" y2="{can["plot_y_min_px"]}" '
                f'stroke="{C["gridline_stroke"]}" stroke-width="0.5" stroke-dasharray="4 3"/>'
            )
        lines.append(
            f'<text x="{cx:.1f}" y="{can["plot_y_min_px"] + 17}" '
            f'text-anchor="middle" font-size="{spec["typography"]["axis_tick_font_size"]}" '
            f'fill="{C["axis_stroke"]}">{label}</text>'
        )

    # Y ticks
    for v in ay["ticks"]:
        cy = can["plot_y_min_px"] - v * ay["px_per_unit"]
        if v > 0:
            lines.append(
                f'<line x1="{can["plot_x_min_px"]}" y1="{cy:.1f}" x2="{can["plot_x_max_px"]}" y2="{cy:.1f}" '
                f'stroke="{C["gridline_stroke"]}" stroke-width="0.5" stroke-dasharray="4 3"/>'
            )
        lines.append(
            f'<text x="{can["plot_x_min_px"] - 8}" y="{cy + 4:.1f}" '
            f'text-anchor="end" font-size="{spec["typography"]["axis_tick_font_size"]}" '
            f'fill="{C["axis_stroke"]}">{v}</text>'
        )

    return "\n".join(lines)

# ── Génération des libellés de zone ──────────────────────────────────────────

def render_zone_labels(spec: dict) -> str:
    C   = spec["colors"]
    V   = spec["vocabulary"]
    T   = spec["typography"]
    ax  = spec["axes"]["x"]
    ay  = spec["axes"]["y"]
    can = spec["canvas"]
    mid_x = (can["plot_x_min_px"] + can["plot_x_max_px"]) // 2

    z1_x = can["plot_x_min_px"] + 80
    z1_y = can["plot_y_max_px"] + 54
    line1, line2 = V["zone_high_sem_low_fact"].split(", ", 1)

    z2_x = mid_x + 20
    z2_y = can["plot_y_min_px"] - 54

    z3_x = mid_x + 30
    z3_y = can["plot_y_max_px"] + 90

    return f"""
  <text x="{z1_x}" y="{z1_y}" font-size="{T['zone_label_font_size']}" fill="{C['zone_label_high_sem']}">{escape(line1)},</text>
  <text x="{z1_x}" y="{z1_y + 16}" font-size="{T['zone_label_font_size']}" fill="{C['zone_label_high_sem']}">{escape(line2)}</text>
  <text x="{z2_x}" y="{z2_y}" font-size="{T['zone_label_font_size']}" fill="{C['zone_label_high_fact']}">{escape(V['zone_low_sem_high_fact'].split(', ')[0])},</text>
  <text x="{z2_x}" y="{z2_y + 16}" font-size="{T['zone_label_font_size']}" fill="{C['zone_label_high_fact']}">{escape(V['zone_low_sem_high_fact'].split(', ')[1])}</text>
  <text x="{z3_x}" y="{z3_y}" font-size="11" fill="{C['zone_label_empty']}">{escape(V['zone_empty_corner'].split(' : ')[0])} :</text>
  <text x="{z3_x}" y="{z3_y + 14}" font-size="11" fill="{C['zone_label_empty']}">{escape(V['zone_empty_corner'].split(' : ')[1])}</text>"""


# ── Template HTML complet ────────────────────────────────────────────────────

# ── Fragment WordPress (sans <html>, <head> ni <body>) ────────────────────────

WP_FRAGMENT_TEMPLATE = """\
<div class="neomundi-carto-block" id="cartoWrap_{uid}">
  <style>
    #cartoWrap_{uid}{{position:relative;width:100%;max-width:1180px;margin:0 auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#0b0b0b}}
    #cartoWrap_{uid} .meta{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#888780;margin:0 0 1rem 0}}
    #cartoWrap_{uid} .sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}}
    #cartoWrap_{uid} svg{{display:block;width:100%;height:auto}}
    #cartoWrap_{uid} .pt{{cursor:pointer;transition:stroke-width .1s}}
    #cartoWrap_{uid} .pt:hover{{stroke:#26215C;stroke-opacity:.22;stroke-width:9}}
    #cartoWrap_{uid} .carto-tip{{position:absolute;display:none;pointer-events:none;background:#fff;border:.5px solid #c3c2b7;border-radius:6px;padding:8px 10px;font-size:12px;line-height:1.5;color:#0b0b0b;max-width:210px;z-index:5;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
    @media (max-width:640px){{
      #cartoWrap_{uid} .meta{{font-size:9px;line-height:1.45}}
    }}
  </style>
  <p class="meta">{meta_text}</p>
  <h2 class="sr-only">{screen_reader_text}</h2>
  <svg viewBox="0 0 920 492" xmlns="http://www.w3.org/2000/svg" width="100%"
       role="img" aria-label="{aria_label}">
    <defs>
      <clipPath id="plotClip_{uid}">
        <rect x="{plot_x_min}" y="{plot_y_max}" width="{plot_w}" height="{plot_h}"/>
      </clipPath>
      <marker id="arrOutlier_{uid}" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="{outlier_arrow}"/>
      </marker>
    </defs>

    <line x1="{plot_x_min}" y1="{plot_y_min}" x2="{plot_x_max}" y2="{plot_y_min}"
          stroke="{axis_stroke}" stroke-width="1"/>
    <line x1="{plot_x_min}" y1="{plot_y_min}" x2="{plot_x_min}" y2="{plot_y_max}"
          stroke="{axis_stroke}" stroke-width="1"/>

{ticks}

    <text x="360" y="452" text-anchor="middle" font-size="{axis_label_size}" fill="{annot}">{x_label}</text>
    <text x="360" y="469" text-anchor="middle" font-size="{tick_size}" fill="{axis_stroke}">{x_sublabel}</text>
    <text x="20" y="220" text-anchor="middle" font-size="{axis_label_size}" fill="{annot}"
          transform="rotate(-90 20 220)">{y_label}</text>
    <text x="36" y="220" text-anchor="middle" font-size="{tick_size}" fill="{axis_stroke}"
          transform="rotate(-90 36 220)">{y_sublabel}</text>

{zone_labels}

    <g clip-path="url(#plotClip_{uid})">
{normal_pts}
    </g>

{outlier_rail}
  </svg>
  <div class="carto-tip" id="tip_{uid}"></div>
</div>
<script>
(function(){{
  var wrap = document.getElementById('cartoWrap_{uid}');
  var tip = document.getElementById('tip_{uid}');
  if (!wrap || !tip) return;
  var V_FACT = {v_fact_json};
  var V_SEM = {v_sem_json};
  function show(e){{
    var el = e.currentTarget;
    var r = wrap.getBoundingClientRect();
    tip.innerHTML = '<strong style="font-weight:500">' + el.dataset.id + '</strong>'
      + '<br>' + V_FACT + ' : ' + el.dataset.fact + '\u202f%'
      + '<br>' + V_SEM + ' : ' + el.dataset.sem + '\u202f%';
    tip.style.display = 'block';
    var x = e.clientX - r.left + 14, y = e.clientY - r.top + 14;
    if (x + 220 > r.width) x = r.width - 220;
    if (x < 0) x = 4;
    tip.style.left = x + 'px';
    tip.style.top = y + 'px';
  }}
  function hide(){{ tip.style.display = 'none'; }}
  wrap.querySelectorAll('.pt').forEach(function(el){{
    el.addEventListener('mouseenter', show);
    el.addEventListener('mousemove', show);
    el.addEventListener('mouseleave', hide);
    el.addEventListener('click', show);
  }});
  wrap.addEventListener('click', function(e){{
    if (!e.target.classList.contains('pt')) hide();
  }});
}})();
</script>
<!-- NeoMundi cartography fragment | spec_version: {spec_version} -->
"""
HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#fff;color:#0b0b0b;padding:2rem clamp(1rem,3vw,3rem)}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}}
.wrap{{position:relative;width:100%;max-width:1180px;margin:0 auto}}
.meta{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#888780;margin:0 0 1rem 0}}
svg{{display:block;width:100%;height:auto}}
.pt{{cursor:pointer;transition:stroke-width .1s}}
.pt:hover{{stroke:#26215C;stroke-opacity:.22;stroke-width:9}}
.carto-tip{{position:absolute;display:none;pointer-events:none;background:#fff;border:.5px solid #c3c2b7;
  border-radius:6px;padding:8px 10px;font-size:12px;line-height:1.5;color:#0b0b0b;max-width:210px;z-index:5;
  box-shadow:0 2px 8px rgba(0,0,0,.08)}}
@media (max-width:640px){{
  body{{padding:1rem .75rem}}
  .meta{{font-size:9px;line-height:1.45}}
}}
</style>
</head>
<body>
<div class="wrap" id="cartoWrap_{uid}">
  <p class="meta">{meta_text}</p>
  <h2 class="sr-only">{screen_reader_text}</h2>
  <svg viewBox="0 0 920 492" xmlns="http://www.w3.org/2000/svg" width="100%"
       role="img" aria-label="{aria_label}">
    <defs>
      <clipPath id="plotClip_{uid}">
        <rect x="{plot_x_min}" y="{plot_y_max}" width="{plot_w}" height="{plot_h}"/>
      </clipPath>
      <marker id="arrOutlier" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="{outlier_arrow}"/>
      </marker>
    </defs>

    <!-- Axes -->
    <line x1="{plot_x_min}" y1="{plot_y_min}" x2="{plot_x_max}" y2="{plot_y_min}"
          stroke="{axis_stroke}" stroke-width="1"/>
    <line x1="{plot_x_min}" y1="{plot_y_min}" x2="{plot_x_min}" y2="{plot_y_max}"
          stroke="{axis_stroke}" stroke-width="1"/>

    <!-- Graduations et grille -->
{ticks}

    <!-- Libellés d'axes -->
    <text x="360" y="452" text-anchor="middle" font-size="{axis_label_size}" fill="{annot}">{x_label}</text>
    <text x="360" y="469" text-anchor="middle" font-size="{tick_size}" fill="{axis_stroke}">{x_sublabel}</text>
    <text x="20" y="220" text-anchor="middle" font-size="{axis_label_size}" fill="{annot}"
          transform="rotate(-90 20 220)">{y_label}</text>
    <text x="36" y="220" text-anchor="middle" font-size="{tick_size}" fill="{axis_stroke}"
          transform="rotate(-90 36 220)">{y_sublabel}</text>

    <!-- Libellés de zone -->
{zone_labels}

    <!-- Points normaux (dans le cadre) -->
    <g clip-path="url(#plotClip_{uid})">
{normal_pts}
    </g>

    <!-- Outliers (hors cadre) -->
{outlier_rail}

  </svg>
  <div class="carto-tip" id="tip_{uid}"></div>
</div>
<script>
(function(){{
  var wrap = document.getElementById('cartoWrap_{uid}');
  var tip  = document.getElementById('tip_{uid}');
  var V_FACT = {v_fact_json};
  var V_SEM  = {v_sem_json};
  function show(e){{
    var el = e.currentTarget;
    var r  = wrap.getBoundingClientRect();
    tip.innerHTML = '<strong style="font-weight:500">' + el.dataset.id + '</strong>'
      + '<br>' + V_FACT + ' : ' + el.dataset.fact + '\u202f%'
      + '<br>' + V_SEM  + ' : ' + el.dataset.sem  + '\u202f%';
    tip.style.display = 'block';
    var x = e.clientX - r.left + 14, y = e.clientY - r.top + 14;
    if (x + 220 > r.width) x = r.width - 220;
    if (x < 0) x = 4;
    tip.style.left = x + 'px';
    tip.style.top  = y + 'px';
  }}
  function hide(){{ tip.style.display = 'none'; }}
  wrap.querySelectorAll('.pt').forEach(function(el){{
    el.addEventListener('mouseenter', show);
    el.addEventListener('mousemove',  show);
    el.addEventListener('mouseleave', hide);
    el.addEventListener('click',      show);
  }});
  wrap.addEventListener('click', function(e){{
    if (!e.target.classList.contains('pt')) hide();
  }});
}})();
</script>
<!-- spec_version: {spec_version} | visual specification -->
</body>
</html>
"""


# ── Assemblage final ─────────────────────────────────────────────────────────

def generate(spec: dict, profiles: list[dict], week: int, output_path: Path, fragment: bool = False) -> None:
    ax  = spec["axes"]["x"]
    ay  = spec["axes"]["y"]
    can = spec["canvas"]
    C   = spec["colors"]
    T   = spec["typography"]
    V   = spec["vocabulary"]
    UI  = spec.get("ui", {})

    uid = f"w{week}"
    template_vars = {
        "week": week,
        "n_profiles": len(profiles),
        "generated": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    html_lang = UI.get("html_lang", "fr")
    page_title = UI.get("page_title", "NeoMundi Baromètre #{week} — Cartographie").format(**template_vars)
    meta_text = UI.get("meta_template", "Baromètre NeoMundi · semaine {week} · {n_profiles} profils dé-identifiés · généré le {generated}").format(**template_vars)
    screen_reader_text = UI.get("screen_reader_template", "Cartographie de {n_profiles} profils.").format(**template_vars)
    aria_label = UI.get("aria_template", "Nuage de {n_profiles} profils — semaine {week}").format(**template_vars)
    marker_id = f"arrOutlier_{uid}" if fragment else "arrOutlier"
    normal_pts, outlier_rail = render_points(spec, profiles, marker_id=marker_id)
    ticks       = render_ticks(spec)
    zone_labels = render_zone_labels(spec)

    plot_x_min = can["plot_x_min_px"]
    plot_x_max = can["plot_x_max_px"]
    plot_y_min = can["plot_y_min_px"]
    plot_y_max = can["plot_y_max_px"]

    template = WP_FRAGMENT_TEMPLATE if fragment else HTML_TEMPLATE
    html = template.format(
        week=week,
        uid=uid,
        n_profiles=len(profiles),
        generated=template_vars["generated"],
        html_lang=html_lang,
        page_title=page_title,
        meta_text=meta_text,
        screen_reader_text=screen_reader_text,
        aria_label=aria_label,
        spec_version=spec["spec_version"],

        plot_x_min=plot_x_min,
        plot_x_max=plot_x_max,
        plot_y_min=plot_y_min,
        plot_y_max=plot_y_max,
        plot_w=plot_x_max - plot_x_min,
        plot_h=plot_y_min - plot_y_max,

        ticks=ticks,
        zone_labels=zone_labels,
        normal_pts=normal_pts,
        outlier_rail=outlier_rail,

        axis_stroke=C["axis_stroke"],
        annot=C["annotation_text"],
        outlier_arrow=C["outlier_arrow"],
        tick_size=T["axis_tick_font_size"],
        axis_label_size=T["axis_label_font_size"],

        x_label=escape(ax["label"]),
        x_sublabel=escape(ax["sublabel"]),
        y_label=escape(ay["label"]),
        y_sublabel=escape(ay["sublabel"]),

        v_fact_json=json.dumps(V["factual_risk_tooltip_label"]),
        v_sem_json=json.dumps(V["semantic_variation_tooltip_label"]),
    )

    output_path.write_text(html, encoding="utf-8")
    kind = "fragment WordPress" if fragment else "page HTML complète"
    print(f"[OK] Cartographie générée ({kind}) : {output_path}")

    # Processing report
    outliers_x = [p for p in profiles if is_x_outlier(spec, p["factual_risk_pct"])]
    outliers_y = [p for p in profiles if is_y_outlier(spec, p["semantic_variation_pct"])]
    lang = UI.get("html_lang", "fr").lower()
    decimal_separator = "." if lang == "en" else ","

    if lang == "en":
        print(f"[INFO] {len(profiles)} profiles processed, {len(profiles) - len(outliers_x) - len(outliers_y)} inside the main plot.")
    else:
        print(f"[INFO] {len(profiles)} profils traités, {len(profiles) - len(outliers_x) - len(outliers_y)} dans le cadre.")

    if outliers_x:
        for p in outliers_x:
            factual = f"{p['factual_risk_pct']:.2f}".replace(".", decimal_separator)
            maximum = f"{ax['domain_max']:.1f}".replace(".", decimal_separator)
            if lang == "en":
                print(f"[OUTLIER-X] {p['profile_id']} — {factual} % responses needing more verification "
                      f"(main scale maximum: {maximum} %) → side rail.")
            else:
                print(f"[OUTLIER-X] {p['profile_id']} — réponses à vérifier davantage {factual} % "
                      f"(max échelle : {maximum} %) → rail latéral.")

    if outliers_y:
        for p in outliers_y:
            semantic = f"{p['semantic_variation_pct']:.2f}".replace(".", decimal_separator)
            maximum = f"{ay['domain_max']:.1f}".replace(".", decimal_separator)
            if lang == "en":
                print(f"[OUTLIER-Y] {p['profile_id']} — {semantic} % change in response meaning "
                      f"(main scale maximum: {maximum} %) → top-edge clamp.")
            else:
                print(f"[OUTLIER-Y] {p['profile_id']} — variation du sens des réponses {semantic} % "
                      f"(max échelle : {maximum} %) → clamp bord supérieur.")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Générateur de cartographie NeoMundi Baromètre — schéma officiel public_profiles_summary.csv."
    )
    parser.add_argument("--input",  "-i", required=True,
                        help="Chemin vers public_profiles_summary.csv")
    parser.add_argument("--week",   "-w", type=int, required=True,
                        help="Numéro du baromètre (ex. : 2)")
    parser.add_argument("--output", "-o", default=None,
                        help="Chemin du fichier HTML de sortie (auto-nommé si absent)")
    parser.add_argument("--spec",   "-s", default=str(SPEC_FILE),
                        help=f"Chemin vers chart_spec.json (défaut : {SPEC_FILE})")
    parser.add_argument("--fragment", action="store_true",
                        help="Produit un bloc WordPress insérable : sans <html>, <head> ni <body>.")
    args = parser.parse_args()

    spec      = load_spec(Path(args.spec))
    csv_path  = Path(args.input)
    profiles  = load_data(csv_path, week=args.week)

    if args.output:
        output_path = Path(args.output)
    else:
        suffix = "_fragment.html" if args.fragment else ".html"
        output_path = csv_path.parent / f"carto_barometer_week{args.week}{suffix}"

    generate(spec, profiles, args.week, output_path, fragment=args.fragment)


if __name__ == "__main__":
    main()
