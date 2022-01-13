import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

_font_mono = "Inconsolata"
_font_serif = "Canela Desk"
_font_sans = "Gill Sans Nova"

sns.set_theme(style="whitegrid",
              context="paper",
              font_scale=1.0,
              rc={
                  "figure.figsize": (10.5, 4.5),
                  "figure.dpi": 300,
                  "grid.alpha": 0.1,
                  "grid.color": "#1b262c",
                  "grid.linewidth": 0.5,
                  "font.family": _font_mono,
                  "lines.solid_capstyle": "projecting",
                  "lines.solid_joinstyle": "bevel",
              })

_30k = ["#202f66", "#ff7048", "#7f68d0", "#f3d36e", "#d869ab", "#48ADA9", "#1b262c"]
sns.set_palette(_30k)

import warnings

warnings.filterwarnings('ignore')