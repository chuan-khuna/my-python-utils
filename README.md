# My Python code snippets

## visualisatoin - matplotlib (-30k)

see more: [-30k theme](/snippets/matplotlib-theme/README.md)

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
    "bg_cream": "#FAF7F4"
}

_font_mono = "Inconsolata"
_font_serif = "Canela Text"
_font_sans = "Gill Sans"
_path_effects = [patheffects.Stroke(linewidth=2.5, foreground="white", alpha=0.8), patheffects.Normal()]

plt.style.use("-30k.mplstyle")

_30k = list(_30k_main.values())
sns.set_palette(_30k)
# ← → ↓ ↑


import warnings
warnings.filterwarnings('ignore')
```

## gitignore

a simple `.gitignore` for jupyter notebook repositories

```txt
.DS_Store
.ipynb_checkpoints
*.pyc

Untitled.ipynb
Untitled[a-zA-Z0-9].ipynb
```

## Theme Configuration

file: `-30k.mplstyle`

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

## visualisation - matplotlib (seaborn version)

```py
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

_30k_main_palette_dict = {
    "blue": "#202F66",
    "orange": "#FF7048",
    "purple": "#8B87EA",
    "pink": "#D869AB",
    "cyan": "#54C9B9",
    "yellow": "#F3D36E",
}

_30k_danger_safe_palette_dict = {
    "danger": "#FF4F72",
    "safe": "#58EDB9",
}

_30k_text_palette_dict = {
    "text_black": "#32363A",
    "text_lighter1": "#6F7273",
    "text_lighter2": "#8B8E8F",
    "bg_cream": "#FAF7F4"
}

_font_mono = "Inconsolata"
_font_serif = "Canela Text"
_font_sans = "Gill Sans"

sns.set_theme(style="whitegrid",
              context="paper",
              font_scale=1.0,
              rc={
                  "figure.figsize": (10.5, 4.5),
                  "figure.dpi": 300,
                  "savefig.dpi": 300,
                  "grid.alpha": 0.1,
                  "grid.color": "#1b262c",
                  "grid.linewidth": 0.5,
                  "font.family": _font_mono,
                  "lines.solid_capstyle": "projecting",
                  "lines.solid_joinstyle": "bevel",
                  "axes.facecolor": "#FAF7F4",
                  "figure.facecolor": "#FAF7F4",
                  "savefig.facecolor": "#FAF7F4",
                  "savefig.bbox": "tight",
                  "savefig.pad_inches": 0.1,
              })

_30k = list(_30k_main_palette_dict.values())
sns.set_palette(_30k)

import warnings

warnings.filterwarnings('ignore')
```
