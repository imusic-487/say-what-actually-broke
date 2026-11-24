# Say What Actually Broke

[![Competition](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/imusic-487/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/imusic-487/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard)

## The entry

> Your file didn't save — we ran out of disk space. Yes, really. Hit retry; we've bought more disk and a little shame.

One line, 116 characters. It names the real failure in plain words — the file didn't save because the server ran out of disk space — says what to do next (hit retry), and lands the joke on a single read: "Yes, really." and "a little shame". Shippable in a real error dialog.

## What this repo does

This is an entry for the make.fun bounty
[u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the copy differs
in size or bytes, or if the text is not 1–200 characters, is only white
space, or is not a single line. Nothing else: no network, no randomness,
no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
