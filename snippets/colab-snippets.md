# Install TF

```txt
# !pip3 install tensorflow==2.8.2 tensorflow-gpu==2.8.2 tensorflow-datasets -U
# !pip3 install -U seaborn matplotlib
```

# numpy and pandas

```py
import numpy as np
import pandas as pd

# visualisation
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import patheffects
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
```


# Google Drive

```py
import os
from google.colab import drive
drive.mount('/content/gdrive')
google_drive_path = "/content/gdrive/MyDrive/"
```


# Tensorflow

```py
# modelling utils
import tensorflow as tf
import tensorflow_datasets as tfds

# set seed
seed_ = 1607
tf.random.set_seed(seed_)
np.random.seed(seed_)

# tensorflow image utils
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import confusion_matrix, classification_report
```


# Visualisation

```py
# Visualisation setting

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

dataset_dir = google_drive_path + "/model_race/"
plt.style.use(f"{dataset_dir}/-30k.mplstyle")

_30k = list(_30k_main.values())
sns.set_palette(_30k)

# ← → ↓ ↑

def _30k_path_effects(linewidth=2.5, foreground=_30k_text['bg_cream'], alpha=1.0, **kwargs):
    return [patheffects.withStroke(linewidth=linewidth, foreground=foreground, alpha=alpha, **kwargs)]
```

```py
# load fonts
font_dir = [f"{google_drive_path}/code_assets/fonts/"]
for font in matplotlib.font_manager.findSystemFonts(font_dir):
    matplotlib.font_manager.fontManager.addfont(font)

# Override Metric with Google Outfit
# matplotlib.rcParams['font.family'] = 'outfit'
```

# Set project path

```py
# change directory to the project path
# os.chdir()
```
