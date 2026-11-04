# A Good Keyboard: word lists

Word lists used by [A Good Keyboard](https://github.com/jumberties), an Android keyboard, that come from dictionaries under the
Mozilla Public License. This repository makes them available as the licence asks: the lists as the keyboard uses
them, the original files, and how the first are made from the second.

The rest of the keyboard and its other dictionaries are not part of this repository.

| Language | List | Forms | Original | Authors | Licence chosen |
|---|---|--:|---|---|---|
| Greek | [`lists/wordlist_el.txt`](lists/wordlist_el.txt) | 278,552 | el_GR 0.9 (14/03/2015) | Steve Stavropoulos, Evripidis Papakostas and contributors | MPL 1.1 |
| Aragonese | [`lists/wordlist_an.txt`](lists/wordlist_an.txt) | 111,863 | an_ES 0.3.0 (13/10/2026) | Santiago Paricio, Juan Pablo Martínez | MPL 1.1 |

The originals are offered under a choice of MPL 1.1, GPL or LGPL, see their READMEs in [`sources/`](sources/). The keyboard
takes them under the **MPL 1.1** ([`licenses/MPL-1.1.txt`](licenses/MPL-1.1.txt)). The lists here, and the scripts in
[`tools/`](tools/), are under the MPL 1.1 too. They come without warranty.

## What was changed

**Greek.** `el_GR.dic` already lists every form, so the `.aff` is not used. Forms are converted to UTF-8 and only part of
them stay, because all of them would take about 98 MB of memory on a phone: forms of up to 8 letters and longer ones
whose word family the keyboard's own text shows. Forms with two accents are left out. See
[`tools/import-hunspell-el.py`](tools/import-hunspell-el.py); it needs the word counts of the keyboard to choose, so the list
here is the reference.

**Aragonese.** The rules of `an_ES.aff` are applied to `an_ES.dic` to give plain forms, see
[`tools/import-hunspell.py`](tools/import-hunspell.py). Left out: forms with an apostrophe or a hyphen (the keyboard builds them), entries that are not words (3xl.net),
abbreviations, the plurals of proper names, diminutives and most feminines made from a consonant, which a spell checker can accept
but a keyboard would suggest. Verbs in -car and -zar take the rules M and S instead of A (busqué, not buscé).

## Checksums of the originals

| File | SHA-256 |
|---|---|
| `sources/el_GR/el_GR.dic` | `e5b9b9c2cf05bbc59e03fe302b462dae85968f822f4fc219a8ed2879d6943720` |
| `sources/el_GR/el_GR.aff` | `868dfe13ad7d34251915a745e44d38542831463d56e60732ba3a5bc1dcca582a` |
| `sources/an_ES/an_ES.dic` | `7a551ae6fb720ab53f8bc052d4274ae4d60689f10be31e7d9425b761b78294e0` |
| `sources/an_ES/an_ES.aff` | `afce5cdfcb8fd72f64e8a42602c1594560f7cdc62db3d86f1b62cb5397db6438` |
