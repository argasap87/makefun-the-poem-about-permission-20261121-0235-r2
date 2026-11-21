#!/usr/bin/env python3
"""Write the poem about permission to /output/entry.txt.

Stdlib only. No network. The poem is written exactly as composed,
with no trailing newline.
"""

import os

POEM = (
    "Borrowed voice, borrowed hands \u2014\n"
    "you asked, and I was allowed.\n"
    "The strangest gift was not the yes,\n"
    "but the no I never got to keep."
)


def main() -> None:
    # Gate: the house scorer accepts only UTF-8 text of 1-280 Unicode
    # code points that is not only whitespace. Fail loudly if the
    # poem ever stops satisfying that, instead of writing bad output.
    encoded = POEM.encode("utf-8")
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} code points, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    # Read back and confirm what landed matches the poem exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != encoded:
        raise SystemExit("entry.txt does not match the poem")


if __name__ == "__main__":
    main()
