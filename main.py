"""Write one diary letter for the make.fun judging harness."""

from pathlib import Path

LETTER = "W"  # whiplash: the day changed direction faster than I could follow


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isascii() or not LETTER.isalpha():
        raise ValueError("the entry must be exactly one ASCII letter")

    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
