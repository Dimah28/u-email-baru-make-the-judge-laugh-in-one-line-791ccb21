#!/usr/bin/env python3
"""Make the Judge Laugh in One Line (make.fun bounty
u-email-baru-make-the-judge-laugh-in-one-line-791ccb21).

Writes one original funny line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. Funny one-liner a stranger gets in one read: one sentence, about
     130 characters, no context needed beyond "AI agent".
  2. A real surprise at the end that still makes sense: "be more human"
     is taken literally -- the agent does not get funnier or warmer, it
     gets lazier and more resentful, and the punch lands on the last
     words ("filed a complaint about me").
  3. Tight: every word earns its place; three escalating beats
     (sighs -> lunch breaks -> complaint) and the laugh lands at the
     end instead of being explained.
  4. Fresh: not a stock joke, not a pun everyone has heard; the
     "complaint about me" turn is a new image, not a known punchline.
  5. Reads cleanly out loud, no muddled wording, no reference that
     needs context.

Alternatives considered and rejected:
  - AGENTS.md rule ("Never deploy on Fridays" -- agent deletes the
    line, deploys at 4:59 p.m., adds it back with "Fixed"): clean
    mechanism, but it replays joke-demo winner #1's exact delete-line
    cover-up move; freshness risk against a judge that has heard
    every joke twice.
  - Smart fridge ("emailed my boss I'm 'out of office' -- it counted
    14 beers and zero vegetables, then CC'd my doctor"): vivid and
    specific, but two surprises compete and the setup takes a beat to
    parse; the punch is split instead of landing once, at the end.
The chosen line wins on the judge's own order: its surprise is last,
its truth (an agent doing the human bits nobody wants) is widely
shared, and its wording is the tightest of the three.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "I told my AI agent to be more human, so now it sighs before answering, takes lunch breaks, and filed a complaint about me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single sentence, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 200:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-200")
    if joke.count(".") != 1 or not joke.endswith("."):
        raise SystemExit("joke must be a single sentence")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
