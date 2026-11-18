"""news-image-20261118 entry: copy the repo's image to /output/entry.png.

The image is a front-page summary of Wednesday 18 November 2026's world
news: the Kerch Bridge destroyed, US strikes on Iran answered by drones
on Bahrain and Kuwait, and the Trump-Xi-Putin summit set for Shenzhen.
Deterministic: a plain byte copy, no network, no randomness, no time.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
