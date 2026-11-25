#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. The joke is the pile-up: a deploy fails, its rollback fails a minute
later, and stand-up burns an hour deciding whose fault the first
failure was. The one-minute gap is the twist — the rollback did not
even get a chance to be slow, it failed faster than the deploy.
"""

import os

LINE = (
    "Monday: my deploy failed at 9:03, the rollback failed at 9:04, "
    "and stand-up spent an hour deciding it was my fault."
)


def write_entry() -> None:
    """Write the one-liner to /output/entry.txt, nothing else."""
    if not LINE.strip() or "\n" in LINE or len(LINE) > 140:
        raise ValueError("entry must be a single non-empty line of at most 140 characters")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(LINE.encode("utf-8")) != 115:
        raise ValueError("entry must be exactly 115 bytes")
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
