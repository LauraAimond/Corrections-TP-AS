# Apprentissage supervisé — ENSAI 2A

Corrections des travaux pratiques du cours **Apprentissage supervisé** (ENSAI, 2ᵉ année). Chaque TP est
corrigé **deux fois**, avec les mêmes questions, les mêmes conclusions et les mêmes annexes :

- en **Python** (`scikit-learn`, `plotly`) : `TPx/TPx_correction.ipynb` ;
- en **R** (`caret`, `rpart`, `ranger`, `pROC`, `plotly`) : `TPx/TPx_correction_R.ipynb`.

Chaque notebook commence par un **brief de démarrage** (les outils du TP en quelques lignes), rappelle le
cours avant chaque partie et se termine par des **annexes** qui approfondissent la théorie (démonstrations,
illustrations graphiques, rôle des hyperparamètres).

## Contenu des TP

| TP | Thème | Données | Notions clés |
|---|---|---|---|
| **TP1** | Règle de Bayes et k plus proches voisins | simulations, `Vehicle` (mlbench / OpenML) | risque de Bayes, compromis biais–variance, choix de $k$, standardisation |
| **TP2** | Modèles de discrimination | vins rouges (`wine-quality-red`) | Naive Bayes (gaussien / à noyau), LDA, QDA, k-NN, AUC vs accuracy |
| **TP3** | Arbres CART et forêts aléatoires | vins rouges (régression de la note) | coupures, surrogate splits, instabilité, élagage, bagging, OOB, importances, UMAP (bonus) |
| TP4 *(à venir)* | Évaluation et comparaison de classifieurs | `spambase` | matrice de confusion, courbe ROC, AUC, coûts asymétriques et choix du seuil |

Les énoncés sont dans chaque dossier (`TPx - Supervised learning.pdf`).

## Organisation

```
plot_theme.py      # thème graphique commun (Python) : couleurs, échelles, thème plotly sombre
plot_theme.R       # équivalent R + charger_packages() qui installe/charge les packages manquants
pyproject.toml     # dépendances Python (gérées avec uv)
TP1/ … TP3/        # énoncé + corrections Python et R
```

**Conventions communes aux notebooks**

- **Couleurs** : aucun code couleur n'est écrit dans les TP ; tout vient de `plot_theme.py` / `plot_theme.R`
  (`COLORWAY`, `CLASS_COLORS`, `MUTED`, `HIGHLIGHT`, `CONTINUOUS_SCALE`, `DIVERGING_SCALE`, `pick_color()`…).
  Modifier le thème à un seul endroit met à jour tous les graphiques.
- **Reproductibilité** : la graine est posée **une seule fois**, en tête de chaque TP
  (`np.random.seed(SEED)` en Python, `set.seed(SEED)` en R) ; aucun `random_state` n'est passé aux fonctions.
  Les résultats sont identiques à condition d'exécuter le notebook **de haut en bas**.
- **Données** : téléchargées automatiquement (OpenML en Python, UCI / packages R en R) — une connexion
  internet est nécessaire à la première exécution.

## Lancer les notebooks Python

Prérequis : [uv](https://docs.astral.sh/uv/) et Python ≥ 3.11.

```bash
uv sync                 # crée .venv et installe les dépendances (plotly, scikit-learn, umap-learn, …)
uv run jupyter lab      # ou ouvrir les notebooks dans VS Code avec l'interpréteur .venv
```

> Si le projet est dans un dossier synchronisé (OneDrive…), la synchronisation peut corrompre `.venv`.
> On peut placer l'environnement ailleurs : `UV_PROJECT_ENVIRONMENT=<chemin_local> uv sync`.

## Lancer les notebooks R

Prérequis : R ≥ 4.3 et le noyau Jupyter **IRkernel** :

```r
install.packages("IRkernel"); IRkernel::installspec()
```

Rien d'autre à installer à la main : la première cellule de chaque notebook exécute
`source("../plot_theme.R")` puis `charger_packages(c(...))`, qui **installe les packages manquants** depuis le
CRAN (binaires sous Windows) et les charge silencieusement. Le bonus UMAP du TP3 nécessite en plus
`reticulate` et le module Python `umap-learn` ; il est simplement ignoré s'ils sont absents.

Les graphiques `plotly` s'affichent dans VS Code et JupyterLab (rendu `application/vnd.plotly.v1+json`),
sans embarquer la bibliothèque JavaScript dans chaque sortie : les notebooks restent légers.

## Exécuter tous les notebooks en ligne de commande

```bash
uv run jupyter nbconvert --to notebook --execute --inplace TP*/TP*_correction.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=ir TP*/TP*_correction_R.ipynb
```

## Gestion des dépendances Python

- Ajouter un package : `uv add nom-du-package` (ou `uv add --dev …` pour un outil de développement)
- Mettre à jour le lockfile : `uv lock`
