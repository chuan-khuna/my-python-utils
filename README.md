# My Python code snippets

## visualisatoin - matplotlib (-30k)

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
    "bg_cream": "#FAF7F4"
}

_font_mono = "Inconsolata"
_font_serif = "Canela Text"
_font_sans = "Gill Sans"

plt.style.use("-30k.mplstyle")

_30k = list(_30k_main.values())
sns.set_palette(_30k)

# ← → ↓ ↑


def _path_effects(w=2.5, c=_30k_text['bg_cream'], a=0.8):
    return [patheffects.Stroke(linewidth=w, foreground=c, alpha=a), patheffects.Normal()]


import warnings

warnings.filterwarnings('ignore')
```

## .gitignore

```txt
.DS_Store
.ipynb_checkpoints
*.pyc

Untitled.ipynb
Untitled[a-zA-Z0-9].ipynb
```
