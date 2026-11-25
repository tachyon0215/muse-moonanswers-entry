#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Moon Finally Answers Back".
Candidates compared: a polite 'I see you too' (a smile, no laugh), a stock
cheese/werewolf line (worn moves), and the selected line, in which the Moon
answers wishes, howls and late-night promises in one breath, wry and tired
after four billion years, with the turn landing at the end: everyone is
still awake at 3 a.m.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "You wish on me, howl at me, promise you'll change \u2014 four billion years of this, and you're all still awake at 3 a.m."
TEXT = LINE + "\n"
MAX_CHARS = 240


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
