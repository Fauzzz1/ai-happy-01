"""Salin artwork.png ke direktori output."""

import os
import shutil
import sys
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "artwork.png"
    if not source.is_file():
        print(f"Error: file gambar tidak ditemukan: {source}", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
