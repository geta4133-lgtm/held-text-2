#!/usr/bin/env python3
"""Writes one short, quiet text to /output/entry.txt.

The task: make the reader feel held. The text does not ask anything of
its reader and does not try to be clever; it just describes a small,
warm scene and lets the silence do the work. 254 characters.
"""

ENTRY = (
    "Nothing here is left to fix. The kettle has clicked off; steam rises "
    "and forgets itself. The cups are already warm. Whatever you were "
    "weighing can rest on the counter, beside the honey jar. Stay as long "
    "as you like. The light moves slower than you think."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
