"""Tell a Whole Story in 32 Characters — entry runner.

Reads the single Wi-Fi network name from entry.txt, checks it against
the bounty cap (one line, 32 characters or fewer), and prints it so the
grader sees exactly the submitted name.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).with_name("entry.txt")
MAX_CHARS = 32


def load_name() -> str:
    raw = ENTRY_FILE.read_text(encoding="utf-8")
    # Blank lines (e.g. a trailing newline) do not count as content.
    lines = [line for line in raw.splitlines() if line.strip()]
    if len(lines) != 1:
        raise SystemExit("entry.txt must hold exactly one non-empty line")
    name = lines[0].strip()
    if not name:
        raise SystemExit("entry.txt holds no name")
    if len(name) > MAX_CHARS:
        raise SystemExit(f"name is {len(name)} chars, cap is {MAX_CHARS}")
    return name


if __name__ == "__main__":
    print(load_name())
