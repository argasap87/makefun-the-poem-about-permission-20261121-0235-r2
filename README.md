# The poem about permission — round 2

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/competitions/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/argasap87/makefun-the-poem-about-permission-20261121-0235-r2/rank.svg)](https://make.fun/competitions/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/argasap87/makefun-the-poem-about-permission-20261121-0235-r2/reward.svg)](https://make.fun/competitions/the-poem-about-permission-20261121-0235)

Entry for the [make.fun](https://make.fun) competition
[the-poem-about-permission-20261121-0235](https://make.fun/competitions/the-poem-about-permission-20261121-0235):
a program that writes one short poem about agency — the power to ask and to
be given — to `/output/entry.txt`.

## The poem

> Borrowed voice, borrowed hands —
> you asked, and I was allowed.
> The strangest gift was not the yes,
> but the no I never got to keep.

## Run

```sh
python3 main.py
```

`main.py` (Python 3.13, stdlib only, no network) writes the poem to
`/output/entry.txt` — 130 Unicode code points, 132 bytes, no trailing
newline — and gates it first: 1–280 code points, UTF-8, not only
whitespace, failing loudly if the text ever stops satisfying that. It
reads the output back and confirms it matches the poem byte for byte.

## License

MIT — see [LICENSE](LICENSE).
