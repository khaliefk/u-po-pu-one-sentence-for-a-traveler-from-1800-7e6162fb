#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to someone arriving from 1800, using only things they already
know: a road, a post office, a library, a letter, a book, a candle.
"""

import os

ENTRY = (
    "It is a road joining every library and post office on earth, "
    "so a letter, a book, or a spoken word can reach a far door "
    "before a candle burns down."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
