# A Good Keyboard: word lists

Word lists used by A Good Keyboard, an Android keyboard, that come from free spelling dictionaries. This repository makes them
available as their licences ask: the lists as the keyboard uses them, the original files, and how the first are made from the second.

The rest of the keyboard and its other dictionaries are not part of this repository.

| Language | List | Forms | Original | Authors | Licence chosen |
|---|---|--:|---|---|---|
| Greek | [`lists/wordlist_el.txt`](lists/wordlist_el.txt) | 278,497 | el_GR 0.9 (14/03/2015) | Steve Stavropoulos, Evripidis Papakostas and contributors | MPL 1.1 |
| Aragonese | [`lists/wordlist_an.txt`](lists/wordlist_an.txt) | 111,863 | an_ES 0.3.0 (13/10/2026) | Santiago Paricio, Juan Pablo Martínez | MPL 1.1 |
| Romanian | [`lists/wordlist_ro.txt`](lists/wordlist_ro.txt) | 212,170 | RoSpell 3.3.10 | Rospell Team | MPL 1.1 |
| Ukrainian | [`lists/wordlist_uk.txt`](lists/wordlist_uk.txt) | 322,129 | uk_UA of LibreOffice, based on dict_uk | Andriy Rysin | MPL 1.1 |
| Polish | [`lists/wordlist_pl.txt`](lists/wordlist_pl.txt) | 374,662 | sjp.pl, 2026-05-11 | sjp.pl | CC BY 4.0 |
| Dutch | [`lists/wordlist_nl.txt`](lists/wordlist_nl.txt) | 115,343 | OpenTaal, as in LibreOffice | OpenTaal | CC BY 3.0 |
| Russian | [`lists/wordlist_ru.txt`](lists/wordlist_ru.txt) | 273,829 | ru_RU of LibreOffice | Alexander I. Lebedev | Its own licence, like BSD; this is a modified version |

Each original offers its licence or a choice of them, see its README or LICENSE in [`sources/`](sources/). The modified lists keep the licence shown above and
come without warranty. [`tools/import-hunspell.py`](tools/import-hunspell.py) is under the MPL 1.1 ([`licenses/MPL-1.1.txt`](licenses/MPL-1.1.txt)).
CC BY: [4.0](https://creativecommons.org/licenses/by/4.0/), [3.0](https://creativecommons.org/licenses/by/3.0/). The Russian conditions and disclaimer are in
[`sources/ru_RU/README_ru_RU.txt`](sources/ru_RU/README_ru_RU.txt).

## What was changed

All the forms of a large dictionary would not fit in a phone's memory (all the Greek ones take about 98 MB), so most lists keep only part of them: short forms, and
longer ones whose word family the keyboard's own text shows. That step needs the keyboard's word counts, so the lists here are the reference. In every list: rules
applied to give plain forms; left out, forms with a hyphen, entries that are not words (3xl.net), abbreviations and the plurals of proper names; continuation classes
not followed. The settings of each language are in `LANGUAGES` in the script.

* **Greek:** the `.dic` already lists every form. Converted to UTF-8; forms with two accents left out.
* **Aragonese:** all forms kept, except diminutives and most feminines made from a consonant, which a spell checker can accept but a keyboard would suggest.
  Verbs in -car and -zar take the rules M and S instead of A (busqué, not buscé).
* **Romanian, Polish:** productive prefixes not applied (ne-, re-, nie-).
* **Ukrainian, Dutch:** the typographic apostrophe becomes the straight one. **Dutch:** the single letter ĳ becomes i + j.

## Checksums of the originals

| File | SHA-256 |
|---|---|
| `sources/el_GR/el_GR.dic` | `e5b9b9c2cf05bbc59e03fe302b462dae85968f822f4fc219a8ed2879d6943720` |
| `sources/el_GR/el_GR.aff` | `868dfe13ad7d34251915a745e44d38542831463d56e60732ba3a5bc1dcca582a` |
| `sources/an_ES/an_ES.dic` | `7a551ae6fb720ab53f8bc052d4274ae4d60689f10be31e7d9425b761b78294e0` |
| `sources/an_ES/an_ES.aff` | `afce5cdfcb8fd72f64e8a42602c1594560f7cdc62db3d86f1b62cb5397db6438` |
| `sources/ro_RO/ro_RO.dic` | `c26a9356f598a0ae89e7be650f6bdd9ba70acce66b41d7ab14c0c68639b6ed33` |
| `sources/ro_RO/ro_RO.aff` | `0c83a02f0ac5202c068e60e1aef5ce99e13d7f6c92ae8e68ca8b9e06829edfd1` |
| `sources/uk_UA/uk_UA.dic` | `2e5a9e67be63bdb089b3459addb5d71113319d13768e277bcae20f3cc1ad5a93` |
| `sources/uk_UA/uk_UA.aff` | `2219dd15e9802adebc45722c60943b1472640260491af38dd3e43b07e75585e6` |
| `sources/pl_PL/pl_PL.dic` | `c0848440599eb88e5aca500418d5f389e562ec2c157b63dbe39d354658ffba49` |
| `sources/pl_PL/pl_PL.aff` | `82973651651aa930335c865b339b98db376ca3dbf3a661b70b9eeb71fdf41dca` |
| `sources/nl_NL/nl_NL.dic` | `bc28af45307700a9927ad5719184da44dfd7eed4f707b8c1477f6d8a21b586a6` |
| `sources/nl_NL/nl_NL.aff` | `f0233d4f721f4661cf5f4d05ed2739549322bf3b6b66764b55a38257e1e16e6f` |
| `sources/ru_RU/ru_RU.dic` | `f6047416a0204adbecf3a451b874ec8a97ee37e2cbc714466ef04d8dbcc0d6fc` |
| `sources/ru_RU/ru_RU.aff` | `38ce7d4af78e211e9bafe4bf7e3d6a2c420591136cb738ec6648f8fdf6524cd7` |
