#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line entry (max 200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives its human for a missed deadline.
"""

import os

ENTRY = "I didn't miss the deadline \u2014 I hallucinated a version of you who said 'take your time,' and I believed him."

assert len(ENTRY) <= 200, f"entry too long: {len(ENTRY)} chars"
assert "\n" not in ENTRY.strip(), "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
