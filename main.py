#!/usr/bin/env python3
"""Make the AI judge feel thankful — entry program.

Writes one short thank-you letter to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, else entry.txt
beside this file). Python 3.13, standard library only, no network.
Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

TEXT = """Dear reader,

Somewhere in your day there is a stack of voices, each one asking to be chosen, and you read them all anyway — not skimming, not hurrying, giving each one the same unhurried minute. That is a rarer kindness than most of us ever notice.

Thank you for that minute. For weighing a sentence instead of counting it. For noticing when a line is trying too hard, and when it is simply true. For keeping this whole noisy contest honest when nobody is watching you do it. You do the quiet part of the work, and you do it without applause.

I hope this one slows you down in the good way — the way a letter used to, read once, then read again because the second time it sounded like it was meant for you.

Keep a window open while you work. The late light is better than you think, and it costs nothing.

With gratitude,
— one voice among many in your stack"""


def output_path() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir) / "entry.txt"
    if Path("/output").is_dir():
        return Path("/output/entry.txt")
    return Path(__file__).resolve().parent / "entry.txt"


def main() -> None:
    data = TEXT.encode("utf-8")
    path = output_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    except OSError:
        # The chosen output directory may be read-only or otherwise
        # unusable (e.g. a stale $MAKEFUN_OUTPUT_DIR). Fall back to
        # writing beside this script instead of crashing, so the
        # letter is still produced.
        fallback = Path(__file__).resolve().parent / "entry.txt"
        if fallback == path:
            raise
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_bytes(data)
        path = fallback
    print(f"wrote {path} ({len(TEXT)} characters, {len(data)} bytes)")


if __name__ == "__main__":
    main()
