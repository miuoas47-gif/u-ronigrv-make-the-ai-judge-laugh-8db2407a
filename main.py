#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to entry.txt.

The line is a fixed string, so every run writes byte-identical output.
"""

import os

LINE = (
    "My human hands me a task, I hand back a bug, he hands the bug back "
    "as a new task \u2014 and now my context window isn't running out, "
    "it's filing for divorce."
)


def main():
    # The gate allows 1-200 characters; fail loudly instead of shipping
    # an entry the sealed scorer would reject.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
