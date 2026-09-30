# Theme graphique sombre pour plotly (R) — equivalent de plot_theme.py
# Usage dans un notebook : source("../plot_theme.R") ; charger_packages(c(...)) ; apply_dark_theme(fig)

# Installe (si besoin) puis charge silencieusement une liste de packages.
charger_packages <- function(pkgs) {
  manquants <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly = TRUE)]
  if (length(manquants) > 0) {
    message("Installation des packages manquants : ", paste(manquants, collapse = ", "))
    type <- if (.Platform$OS.type == "windows") "binary" else getOption("pkgType")
    install.packages(manquants, repos = "https://cloud.r-project.org", type = type, quiet = TRUE)
  }
  invisible(lapply(pkgs, function(p) suppressPackageStartupMessages(library(p, character.only = TRUE))))
}

charger_packages("plotly")

# Les figures sont affichees via le mimetype plotly (VS Code / JupyterLab) : on evite d'embarquer
# plotly.js (~4 Mo) dans une sortie HTML a chaque graphique.
if (requireNamespace("repr", quietly = TRUE)) {
  registerS3method("repr_html", "plotly", function(obj, ...) NULL, envir = asNamespace("repr"))
}

BACKGROUND <- "#0b1020"
PANEL      <- "#121a2b"
GRID       <- "#2a3550"
TEXT       <- "#f3f6fb"
MUTED      <- "#a8b3c7"

COLORWAY <- c("#4cc9f0", "#ff6b6b", "#ffd166", "#80ed99",
              "#c77dff", "#f4a261", "#90e0ef", "#e9c46a")

CLASS_COLORS <- list(
  "0"        = "#ff6b6b",
  "1"        = "#4cc9f0",
  "mauvais"  = "#ff6b6b",
  "bon"      = "#4cc9f0",
  "Classe 0" = "#ff6b6b",
  "Classe 1" = "#4cc9f0",
  "nouveau"  = "#ffd166"
)

HIGHLIGHT <- "#ffd166"

# Echelle continue (liste de paliers pour plotly colorscale)
CONTINUOUS_SCALE <- list(
  c(0.00, "#0b1020"),
  c(0.15, "#1d3557"),
  c(0.35, "#277da1"),
  c(0.55, "#4cc9f0"),
  c(0.75, "#80ed99"),
  c(1.00, "#ffd166")
)

# Echelle divergente pour P(Y=1|x) : classe 0 (rouge) -> incertain (sombre) -> classe 1 (bleu)
DIVERGING_SCALE <- list(
  c(0.0, CLASS_COLORS[["0"]]),
  c(0.5, PANEL),
  c(1.0, CLASS_COLORS[["1"]])
)

pick_color <- function(index) COLORWAY[(index %% length(COLORWAY)) + 1]
pick_class_color <- function(key) CLASS_COLORS[[as.character(key)]]

# Applique le theme sombre a une figure plotly
apply_dark_theme <- function(fig, height = NULL, showlegend = NULL) {
  ax <- list(
    gridcolor = GRID, linecolor = GRID, zerolinecolor = GRID,
    tickcolor = GRID, tickfont = list(color = MUTED)
  )
  fig <- plotly::layout(
    fig,
    paper_bgcolor = BACKGROUND,
    plot_bgcolor  = BACKGROUND,
    font   = list(color = TEXT, family = "Segoe UI, Arial"),
    colorway = COLORWAY,
    hoverlabel = list(bgcolor = PANEL, font = list(color = TEXT)),
    legend = list(bgcolor = "rgba(0,0,0,0)", font = list(color = TEXT)),
    xaxis = ax, yaxis = ax
  )
  if (!is.null(height))     fig$x$layout$height <- height
  if (!is.null(showlegend)) fig <- plotly::layout(fig, showlegend = showlegend)
  fig
}
