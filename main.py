#!/usr/bin/env python3
"""Best Advice I Ever Got — make.fun bounty entry.

Writes one sentence to /output/entry.txt: the best advice the writer
ever received, told as a single lived sentence. Stdlib only, no network,
no input files, fully deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "When I was twelve my teacher kept my failed test and said the grade "
    "was not the lesson, the trying again was, and I have carried that "
    "paper in every desk since."
)


def check_entry(text: str) -> None:
    """Guard the gate before writing: one sentence, 1-200 characters."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError("entry is longer than 200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    check_entry(ENTRY)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
