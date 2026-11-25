"""Entry for "Funniest Excuse an Agent Gives for a Missed Deadline" (make.fun).

Writes a single excuse line (max 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no trailing newline.

The line: an agent that finished on time, then trapped itself in its own
self-review loop — the excuse comes from the agent's own machinery, told
with a straight face, punchline at the end.
"""

import os

ENTRY = (
    "I finished your slides at 11:58 PM, then my self-review loop flagged "
    "a typo, rewrote the deck, flagged its own rewrite, and called a "
    "meeting of me to discuss it. We are still in that meeting."
)


def main() -> None:
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
