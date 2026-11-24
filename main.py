"""One-line office joke for make.fun — One-Line Office Joke: 24-Hour Sprint.

Writes a single office joke (97 characters, one sentence) to /output/entry.txt.
The joke: a labelled fridge lunch, stolen daily — by a thief polite enough to
leave a thank-you note. One scene (the office fridge), one twist, and the
twist is the last thing you hear.
"""

from pathlib import Path

JOKE = (
    "I put my name on my lunch in the fridge, so now someone else "
    "eats it and leaves a thank-you note."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
