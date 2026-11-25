"""The One-Line Cat Joke That Lands — the hand-in program (Python 3.13).

One joke about cats, at most 200 characters, written to
/output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output
locally). The cat reviews its human's code the way cats do — by
walking across the keyboard — and the twist is that it produced
the only bug-free commit of the week, plus three files named asdf.
"""
import os
from pathlib import Path

FILES = "three new files named \u2018asdf\u2019"
PARTS = [
    "My cat reviewed my code by walking across the keyboard \u2014 ",
    "it was the only commit that week with no bugs ",
    f"and {FILES}.",
]


def main() -> None:
    line = "".join(PARTS)
    assert 1 <= len(line) <= 200, len(line)
    assert "\n" not in line
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
