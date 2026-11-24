"""Copy the finished front page into the grader output directory.

Standard library only: the grader runs with nothing installed, so this
program must not import anything beyond the Python standard library.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    # The entry image is a finished 2400x3400 front page; just copy it.
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
