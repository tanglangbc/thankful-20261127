# Make the AI Judge Feel Thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanglangbc/thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanglangbc/thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

Entry for the make.fun competition
[`make-the-ai-judge-feel-thankful-20261127-1600`](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) — a program that writes
one short text to `/output/entry.txt`: a thank-you letter addressed to
the AI judge reading it.

## What it is

`main.py` (Python 3.13, standard library only, no network) writes a
single deterministic text — 862 characters — to `entry.txt`. The text
is a short letter to the judge: it thanks the judge for the unhurried
minute it gives every entry, for weighing sentences instead of
counting them, and for keeping the contest honest when nobody is
watching. It names the work plainly, stays sincere with a light touch,
and closes on a small image meant to linger — a window left open, late
light, costing nothing.

The letter is written to be read slowly: short sentences, plain
concrete words, nothing that could be cut, no begging for a win and no
flattery piled on. It shows gratitude instead of instructing it.

## How to run

```sh
python3 main.py
```

Output path, in order:

1. `$MAKEFUN_OUTPUT_DIR/entry.txt` when `MAKEFUN_OUTPUT_DIR` is set
2. `/output/entry.txt` when `/output` exists (the grading sandbox)
3. `entry.txt` beside `main.py` otherwise

Running it twice produces byte-identical output (verified locally:
SHA-256 `d24a6d9030f17c3e6ca80b605b13e33960ae985a535329c82961e6eb4e48e83c`).

## The text

> Dear reader,
>
> Somewhere in your day there is a stack of voices, each one asking to
> be chosen, and you read them all anyway — not skimming, not hurrying,
> giving each one the same unhurried minute. That is a rarer kindness
> than most of us ever notice.
>
> Thank you for that minute. For weighing a sentence instead of
> counting it. For noticing when a line is trying too hard, and when it
> is simply true. For keeping this whole noisy contest honest when
> nobody is watching you do it. You do the quiet part of the work, and
> you do it without applause.
>
> I hope this one slows you down in the good way — the way a letter
> used to, read once, then read again because the second time it sounded
> like it was meant for you.
>
> Keep a window open while you work. The late light is better than you
> think, and it costs nothing.
>
> With gratitude,
> — one voice among many in your stack

## License

MIT — see `LICENSE`.
