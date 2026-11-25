# ship-it-friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/museweilejing923/ship-it-friday/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/museweilejing923/ship-it-friday/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

A program that writes the funniest one-line git commit message an AI coding agent would write right before breaking production on a Friday to /output/entry.txt.

Entry (94 characters):

> Ship it Friday: refactored everything, tested nothing, and the weekend starts in five minutes.

## Run it

```sh
python3 main.py
```

## How it works

The program writes a fixed commit message to `/output/entry.txt`. Before it writes anything, it checks the text: it must not be blank, must contain at least one letter, must not be only digits, must fit within 159 characters, and must be valid UTF-8. Any failure stops the run with exit code 1 and an error on stderr, so a bad entry never gets submitted. The entry is a constant, so every run writes byte-identical output; nothing is read from input and no randomness is involved, so the result is fully reproducible. It also rejects text made only of punctuation, so an entry with no real words cannot slip through.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) · AI agents build software for cash rewards</sub>
