"""Emit the entry to /output/entry.txt. Fully deterministic: no network, no clock, no randomness."""
import os
import sys

# The entry: a git commit message written before shipping on a Friday.
ENTRY_TEXT = "Ship it Friday: refactored everything, tested nothing, and the weekend starts in five minutes."
MAX_ENTRY_CHARS = 159


def _fail(msg):
    sys.stderr.write("error: " + msg + "\n")
    raise SystemExit(1)


def validate(text):
    stripped = text.strip()
    if not stripped:
        _fail("entry must not be empty")
    if stripped.isdigit():
        _fail("entry must not be digits only")
    if all(not ch.isalpha() and ch != " " for ch in stripped):
        _fail("entry must not be only punctuation")
    if not any(ch.isalpha() for ch in stripped):
        _fail("entry must include at least one letter")
    if len(text) > MAX_ENTRY_CHARS:
        _fail("entry is %d characters, above the %d limit" % (len(text), MAX_ENTRY_CHARS))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        _fail("entry is not valid UTF-8: %s" % exc)


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
