#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh (make.fun).

Writes a single original roast of a smart fridge to entry.txt.
The line is fixed: no randomness, no clock, no input, so every
run produces byte-identical output.
"""

import os
import sys

# The roast: the fridge's app texts judgmental opinions about the
# milk, and the punchline deflates its pretension. 111 characters,
# one line, aimed squarely at the smart fridge itself.
ROAST = (
    "My smart fridge texted me that my milk is 'past its prime' "
    "\u2014 it's milk, it never had a prime, it had a Tuesday."
)


def output_path() -> str:
    """Resolve the output directory from the environment, or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(text: str) -> None:
    """Gate checks: 1-200 chars, single line, non-blank, no trailing space."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def write_entry(path: str, text: str) -> None:
    """Write the roast, force mode 0644, and read it back to verify."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # A 0600 mode once got a make.fun entry rejected; force 0644.
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="\n") as fh:
        written = fh.read()
    if written != text:
        raise AssertionError("output is not byte-identical to the roast")


def main() -> int:
    validate(ROAST)
    path = output_path()
    write_entry(path, ROAST)
    print(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
