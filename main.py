#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting my own agent.

Writes the single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(the grader sets MAKEFUN_OUTPUT_DIR=/output). Deterministic:
stdlib only, no network, no randomness, no clock reads.
"""

import os

LINE = "My agent answers confidently, wrongly, then agrees with my correction and does it wrong again."


def main():
    # Gate: the bounty requires 1-140 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "rb") as f:
        data = f.read()
    assert data == LINE.encode("utf-8"), "entry.txt bytes differ from LINE"
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
