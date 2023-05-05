import os
from pathlib import Path

import matplotlib as mpl

mpl.rcParams["axes.spines.top"] = False
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["text.usetex"] = False

ROOTDIR = Path(os.path.dirname(__file__)) / ".."
RAWDIR = ROOTDIR / "data" / "raw"
INTDIR = ROOTDIR / "data" / "interim"
REFDIR = ROOTDIR / "references"
FIGDIR = ROOTDIR / "figures"
