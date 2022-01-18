# My Python code snippets

## visualisatoin - matplotlib (-30k)

see more: [-30k theme](/snippets/matplotlib-theme/README.md)

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
_font_serif = "Canela"
_font_sans = "Gill Sans Nova"

plt.style.use("-30k.mplstyle")

_30k = list(_30k_main_palette_dict.values())
sns.set_palette(_30k)

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
_font_serif = "Canela"
_font_sans = "Gill Sans Nova"

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
