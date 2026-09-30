"""Theme graphique commun aux notebooks Python : `from plot_theme import *`."""
from __future__ import annotations

import plotly.graph_objects as go
import plotly.io as pio

BACKGROUND = "#0b1020"
PANEL = "#121a2b"
GRID = "#2a3550"
TEXT = "#f3f6fb"
MUTED = "#a8b3c7"

COLORWAY = [
    "#4cc9f0",
    "#ff6b6b",
    "#ffd166",
    "#80ed99",
    "#c77dff",
    "#f4a261",
    "#90e0ef",
    "#e9c46a",
]

CLASS_COLORS = {
    0: "#ff6b6b",
    1: "#4cc9f0",
    "mauvais": "#ff6b6b",
    "bon": "#4cc9f0",
    "Classe 0": "#ff6b6b",
    "Classe 1": "#4cc9f0",
    "nouveau": "#ffd166",
}

HIGHLIGHT = "#ffd166"

CONTINUOUS_SCALE = [
    [0.0, "#0b1020"],
    [0.15, "#1d3557"],
    [0.35, "#277da1"],
    [0.55, "#4cc9f0"],
    [0.75, "#80ed99"],
    [1.0, "#ffd166"],
]

# Echelle divergente pour P(Y=1|x) : classe 0 (rouge) -> incertain (sombre) -> classe 1 (bleu)
DIVERGING_SCALE = [
    [0.0, CLASS_COLORS[0]],
    [0.5, PANEL],
    [1.0, CLASS_COLORS[1]],
]


def pick_color(index: int) -> str:
    return COLORWAY[index % len(COLORWAY)]


def pick_class_color(key) -> str:
    return CLASS_COLORS[key]


def ensure_template() -> str:
    template_name = "ensai_night"
    if template_name not in pio.templates:
        pio.templates[template_name] = go.layout.Template(
            layout=go.Layout(
                paper_bgcolor=BACKGROUND,
                plot_bgcolor=BACKGROUND,
                font=dict(color=TEXT, family="Aptos, Segoe UI, Arial"),
                title=dict(font=dict(color=TEXT, size=20)),
                colorway=COLORWAY,
                hoverlabel=dict(bgcolor=PANEL, font=dict(color=TEXT)),
                legend=dict(
                    bgcolor="rgba(0,0,0,0)",
                    bordercolor=GRID,
                    borderwidth=0,
                    font=dict(color=TEXT),
                ),
                xaxis=dict(
                    gridcolor=GRID,
                    linecolor=GRID,
                    zerolinecolor=GRID,
                    tickcolor=GRID,
                    title_font=dict(color=TEXT),
                    tickfont=dict(color=MUTED),
                ),
                yaxis=dict(
                    gridcolor=GRID,
                    linecolor=GRID,
                    zerolinecolor=GRID,
                    tickcolor=GRID,
                    title_font=dict(color=TEXT),
                    tickfont=dict(color=MUTED),
                ),
                polar=dict(
                    bgcolor=BACKGROUND,
                    radialaxis=dict(gridcolor=GRID, tickfont=dict(color=MUTED)),
                    angularaxis=dict(gridcolor=GRID, tickfont=dict(color=MUTED)),
                ),
            )
        )
    return template_name


def apply_dark_theme(fig: go.Figure, *, height: int | None = None, showlegend: bool | None = None) -> go.Figure:
    template_name = ensure_template()
    updates = {"template": template_name}
    if height is not None:
        updates["height"] = height
    if showlegend is not None:
        updates["showlegend"] = showlegend
    fig.update_layout(**updates)
    return fig


# A l'import : theme sombre par defaut pour toutes les figures (go et px) et rendu via le
# mimetype plotly (VS Code / JupyterLab), sans dupliquer chaque figure en HTML dans le notebook.
pio.templates.default = ensure_template()
pio.renderers.default = "plotly_mimetype"

__all__ = [
    "BACKGROUND", "PANEL", "GRID", "TEXT", "MUTED", "HIGHLIGHT",
    "COLORWAY", "CLASS_COLORS", "CONTINUOUS_SCALE", "DIVERGING_SCALE",
    "pick_color", "pick_class_color", "apply_dark_theme",
]