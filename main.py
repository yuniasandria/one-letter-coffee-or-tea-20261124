#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry A (coffee).

Writes exactly one byte, "A", to /output/entry.txt: no newline,
no whitespace, no other content. Coffee wins on the judge's own
order — vivid first, then funny: dark, strong, aromatic, with a
caffeine kick and far more joke energy than the quieter tea.
A single byte also keeps the entry minimal for the size tie-break.
"""

import os


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(b"A")


if __name__ == "__main__":
    main()
