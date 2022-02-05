# My Python code snippets

## visualisation - matplotlib (-30k)

see more: [-30k theme](/snippets/matplotlib-theme/README.md) | [-30k.mplstyle](https://github.com/chuan-khuna/my-python-snippets/blob/main/snippets/matplotlib-theme/-30k.mplstyle)

```py
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib
from matplotlib import patheffects

import seaborn as sns

_30k_main = {
    "blue": "#202F66",
    "orange": "#FF7048",
    "purple": "#8B87EA",
    "pink": "#D869AB",
    "cyan": "#54C9B9",
    "yellow": "#F3D36E",
}

_30k_danger_safe = {
    "danger": "#FF4F72",
    "safe": "#58EDB9",
}

_30k_text = {
    "text_black": "#32363A",
    "text_lighter1": "#6F7273",
    "text_lighter2": "#8B8E8F",
    "grey1": "#aeb7bc",
    "grey2": "#c3cace",
    "grey3": "#d9dde0",
    "bg_cream": "#FAF7F4"
}

_font_mono = "Inconsolata"
_font_serif = "Canela Text"
_font_sans = "Gill Sans"

plt.style.use("-30k.mplstyle")

_30k = list(_30k_main.values())
sns.set_palette(_30k)

# ← → ↓ ↑


def _30k_path_effects(linewidth=2.5, foreground=_30k_text['bg_cream'], alpha=0.8, **kwargs):
    return [patheffects.withStroke(linewidth=linewidth, foreground=foreground, alpha=alpha, **kwargs)]

import warnings

warnings.filterwarnings('ignore')
```

## `.gitignore`

```txt
.DS_Store
.ipynb_checkpoints
*.pyc

Untitled.ipynb
Untitled[a-zA-Z0-9].ipynb
```

## matplotlib `-30k.mplstyle`

```txt
## Colour Palette
## Accent Colours
# blue: #202F66
# orange: #FF7048
# purple: #8B87EA
# yellow: #F3D36E
# pink: #D869AB
# cyan: #54C9B9
## Text and background colour
# text_black: #32363A,
# text_lighter1: #6F7273
# text_lighter2: #8B8E8F
# text_lighter3_ui: #B3B5B6
# bg_cream: #FAF7F4
# grey1: #aeb7bc
# grey2: #c3cace
# grey3: #d9dde0
## Typography
# font_main: Inconsolata
# font_sans: Metric
# font_serif: Canela Text
# font_mono: Inconsolata
## Base font size for 5 inches height figure
# the annotation text of FT use around 5% of vertical space
# matpltolib base font size: 14
# customised base font size: 14 (scale=1.25)
# [ 7.2,  9. , 11.2, 14. , 17.5, 21.9, 27.3]
## Figure ratio
# based on 21:9 (2.33:1) but a little wider for sup_title offset


# Figure
figure.figsize : 12.5, 5
figure.dpi : 300.0
figure.facecolor : FAF7F4
axes.facecolor : FAF7F4
savefig.dpi : 300.0
savefig.facecolor : FAF7F4
savefig.bbox : tight
savefig.pad_inches : 0.1

# Grid
grid.alpha : 0.1
grid.color : 32363A
grid.linewidth : 0.5
grid.linestyle: - 

# Axes
axes.edgecolor : B3B5B6
axes.grid : True
axes.linewidth : 0.5
axes.spines.left : True
axes.spines.bottom : True
axes.spines.top : False
axes.spines.right : False
axes.axisbelow : True 

# Tick
xtick.direction : out
ytick.direction : out
xtick.color : B3B5B6
ytick.color : B3B5B6
xtick.labelcolor : 32363A
ytick.labelcolor : 32363A
xtick.major.size : 3.5
xtick.major.width : 0.5
ytick.major.size : 3.5
ytick.major.width : 0.5
xtick.labelsize : small
ytick.labelsize : small

# Line
lines.solid_capstyle : projecting
lines.solid_joinstyle : bevel
lines.linewidth : 2
lines.markeredgewidth : 0.75
lines.markersize : 7.2


## Typography
font.family : MetricHPEXS
font.size : 14
text.color: 32363A

# Title
axes.titlelocation : left
axes.titlesize : 14
axes.titlecolor : 32363A
axes.titlepad : 9
axes.labelpad : 5.0
figure.titlesize : 17.5

# Legend
# Remove the box edge colour
legend.shadow : False
legend.edgecolor : None

# Patches
patch.linewidth : 0
patch.edgecolor : None
```
