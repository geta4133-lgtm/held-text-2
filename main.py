#!/usr/bin/env python3
"""Place one small piece of quiet into the world.

This script's whole job is to write a short message to entry.txt — a few
sentences meant to slow someone's breathing for a moment. The scene is
deliberately ordinary: tea, a window, a blanket. Ordinary things are what
"held" is actually made of.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY = (
    "Set the mug down. The tea is still warm, and the window fogged "
    "softly while you weren't looking. Rain taps the glass with no "
    "hurry at all. Nothing here asks you to be anything. The blanket "
    "is right where you left it, and the room will wait with you."
)


def write_entry(text: str, path: str) -> None:
    """Ensure the output directory exists, then write the text as UTF-8."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-280")
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
