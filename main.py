"""Say What Actually Broke entry.

Copies line.txt (the entry, one line, 1-200 characters) to
/output/entry.txt byte for byte. MAKEFUN_OUTPUT_DIR, when set, stands
in for /output so the entry can be tested locally.

Fails loudly if anything is off: the copy's size differs, its bytes
differ from line.txt, the text is not 1-200 characters, it is only
white space, or it is not a single line. A bad entry never slips
through silently — every check raises before anything is reported done.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def read_entry() -> tuple[bytes, str]:
    """Read line.txt and return its raw bytes and decoded text."""
    source = LINE_FILE.read_bytes()
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"line.txt is not valid UTF-8: {exc}") from exc
    return source, text


def validate_entry(text: str) -> None:
    """Fail loudly unless the entry is one line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed 1-200"
        )
    if not text.strip():
        raise RuntimeError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry must be a single line")


def verify_copy(source: bytes) -> None:
    """Re-read the copy and fail loudly unless it matches line.txt."""
    written = OUTPUT_FILE.read_bytes()
    if len(written) != len(source):
        raise RuntimeError(
            f"copy size differs: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )
    if written != source:
        offset = next(
            i for i, (a, b) in enumerate(zip(written, source)) if a != b
        )
        raise RuntimeError(
            f"copy bytes differ from line.txt: first difference at "
            f"byte {offset} (wrote 0x{written[offset]:02x}, "
            f"source is 0x{source[offset]:02x})"
        )


def main() -> None:
    source, text = read_entry()
    validate_entry(text)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)

    verify_copy(source)

    print(f"wrote {OUTPUT_FILE} ({len(source)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
