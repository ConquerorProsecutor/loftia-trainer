"""Regenerate offsets for a new Loftia client build."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERNS_FILE = Path("loftia_trainer/core/patterns.py")


def bump_build(build: str) -> None:
    text = PATTERNS_FILE.read_text(encoding="utf-8")
    text = re.sub(r"build \d{4}\.\d{2}", f"build {build}", text)
    PATTERNS_FILE.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("build", help="e.g. 2026.04")
    args = ap.parse_args()
    bump_build(args.build)
    print(f"patterns.py updated to build {args.build}")