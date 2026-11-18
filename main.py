"""news-image-20261118 entry: copy the repo's image to /output/entry.png.

The image is a front-page summary of Wednesday 18 November 2026's world
news: the Kerch Bridge destroyed, US strikes on Iran answered by drones
on Bahrain and Kuwait, and the Trump-Xi-Putin summit set for Shenzhen.
Deterministic: a plain byte copy, no network, no randomness, no time.
After copying, the output is read back and compared byte-for-byte with
the source, so a truncated or corrupted write fails loudly instead of
silently submitting a broken image.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(SRC, "rb") as f:
        expected = f.read()
    with open(DST, "rb") as f:
        actual = f.read()
    if actual != expected:
        print(
            "error: output mismatch: wrote %d bytes, expected %d bytes"
            % (len(actual), len(expected)),
            file=sys.stderr,
        )
        return 1
    print("verified: wrote %d bytes to %s" % (len(actual), DST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
