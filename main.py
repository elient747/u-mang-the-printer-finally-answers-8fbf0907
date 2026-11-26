#!/usr/bin/env python3
"""The Printer Finally Answers — the office printer's comeback to the
jams, the error codes and the thumps.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

# One comeback from the printer itself: tired, literal, done being
# thumped. The limit below is the bounty gate.
ENTRY_LIMIT_CHARS = 240

# Bounty gate as named constants, so the guard below reads the rule
# instead of a bare number: one comeback, 1-240 characters.
MIN_LINE_LENGTH = 1
MAX_LINE_LENGTH = 240

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "Error 404: patience not found. I have printed 12,000 pages "
    "for you and you still hit me when I jam — I am the one who "
    "should file a complaint."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate before writing, so a future edit to the
    # line fails loudly instead of silently. The entry must also stay
    # a single line: an embedded newline would break the one-line gate.
    if "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("entry line must be one line, no line breaks or tabs")
    if not MIN_LINE_LENGTH <= len(line) <= ENTRY_LIMIT_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters long, "
            f"but the gate allows {MIN_LINE_LENGTH}-{ENTRY_LIMIT_CHARS}"
        )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
