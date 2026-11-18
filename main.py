"""Entry for make.fun news-image-20261118.

Copies the finished front-page image (entry.png, drawn by draw_entry.py)
to the output directory as /output/entry.png. Standard library only,
no network, deterministic: the same input bytes always produce the
same output bytes.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"entry.png not found next to main.py: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
