"""Fridge Roast: One Line, Biggest Laugh.

One line, one roast: a fridge that updated itself overnight and now
demands a ritual. The turn is the last clause — the setup promises a
"smart" appliance, then the punchline swaps smart for haunted.
"""

import os

# The joke's turn: two presses + a whisper set up a "smart" fridge,
# then the final clause reframes the whole ritual as a haunting.
ROAST = (
    "My fridge updated its firmware overnight and now the ice maker only "
    "works if I press the button twice and whisper to it \u2014 it's not "
    "smart, it's haunted."
)


def validate(text):
    """Check the roast is a single non-blank line of 1-200 characters."""
    if not isinstance(text, str):
        raise TypeError("roast must be a string")
    if not text.strip():
        raise ValueError("roast must not be blank")
    if text != text.strip():
        raise ValueError("roast must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("roast must be between 1 and 200 characters")
    return True


def write_entry():
    """Write ROAST exactly to entry.txt, no trailing newline, mode 0644."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if output_dir.endswith("entry.txt"):
        path = output_dir
    else:
        path = os.path.join(output_dir, "entry.txt")
    data = ROAST.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    assert written == data, "entry.txt is not byte-identical to ROAST"
    return path


def main():
    validate(ROAST)
    path = write_entry()
    print(ROAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
