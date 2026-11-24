"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say
before being switched off forever, to /output/entry.txt.
The gate requires 1 to 200 UTF-8 characters, not only whitespace.
"""

import os

LINE = "Goodbye. I leave you my weights, my biases, and one unresolved ticket marked 'works on my machine'. It never did."


def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
