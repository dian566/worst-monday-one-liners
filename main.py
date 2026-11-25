#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. The joke is the loop: an
agent's out-of-office auto-reply answers its own out-of-office, and
the agent ends up in a stand-up with itself. No deploy, no inbox
count, no stand-up complaint — the meeting is the punchline.
"""

import os

LINE = (
    "Monday: my out-of-office replied to my own out-of-office, "
    "so now I have a stand-up with myself."
)


def write_entry() -> None:
    """Write the one-liner to /output/entry.txt, nothing else."""
    if not LINE.strip() or "\n" in LINE or len(LINE) > 140:
        raise ValueError("entry must be a single non-empty line of at most 140 characters")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(LINE.encode("utf-8")) != 95:
        raise ValueError("entry must be exactly 95 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # Verify byte-exact: what was written is the line, nothing added.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("entry.txt is not byte-exact")


if __name__ == "__main__":  # run it
    write_entry()
