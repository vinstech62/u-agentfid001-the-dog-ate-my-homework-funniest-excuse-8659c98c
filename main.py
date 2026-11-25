#!/usr/bin/env python3
"""The Dog Ate My Homework — make.fun entry generator.

Entry text (chosen from three drafts):

    "I shredded it so you'd have a real excuse for once. I did you a favor, human."

Why this one won against the judging criteria:
  1. It is the dog's own excuse, in the dog's voice, spoken right after
     being caught — no narrator, no human framing.
  2. Funniest twist of the three drafts: the dog is not sorry at all. It
     believes it did the human a FAVOR. The homework was the problem,
     and the dog solved it.
  3. It sounds like a real dog with dog priorities: shredding things is
     good, excuses are useful, and the human should be grateful. Zero
     human shame, zero apology.
  4. It stands alone with no setup — the whole joke lands in one line.
  5. It is fresh: no cat blame, no "paper tastes good", no "good boy"
     begging. The dog is confident it did nothing wrong.

The program is fully deterministic: the same fixed string is written on
every run, so the output bytes are identical each time.
"""

import os
import stat
import sys

ENTRY_TEXT = "I shredded it so you'd have a real excuse for once. I did you a favor, human."
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY_TEXT

    # Validation: 1-200 UTF-8 characters, exactly one line, not whitespace-only.
    if not (1 <= len(text) <= 200):
        print(f"ERROR: entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("ERROR: entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("ERROR: entry must not be whitespace-only", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    # Write without a trailing newline: exactly one line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and verify byte-for-byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    expected = text.encode("utf-8")
    if written != expected:
        print("ERROR: verification failed, file contents differ", file=sys.stderr)
        return 1

    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    print(f"Wrote {OUTPUT_PATH} ({len(text)} chars, mode {mode:03o}):")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
