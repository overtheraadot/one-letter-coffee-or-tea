#!/usr/bin/env python3
"""One Letter: Coffee or Tea entry (make.fun program/v1).

Writes exactly one letter to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``): "A" for coffee.

The competition takes exactly one letter and nothing else: A for coffee,
B for tea, with no word, no explanation and no punctuation. Coffee is the
honest answer here — the letter A stands on its own as the whole reply.
"""

import os

LETTER = "A"  # A for coffee, B for tea.

def main():
    # Gate guard: the entry must be exactly one letter, A for coffee or
    # B for tea, and nothing else. Refuse to write anything that fails it.
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise SystemExit("refusing to write: entry must be exactly one letter, A or B")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
