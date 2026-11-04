#!/usr/bin/env python3
"""Writes dictionaries/wordlist_el.txt from the el_GR.dic of Hunspell (el_GR 0.9, used under the MPL 1.1).

The .dic lists every form in ISO 8859-7 and needs no .aff. All of it would take about 98 MB of memory on
the phone, so only part stays: forms of up to 8 letters, and longer ones whose word family the shipped text
or the project's lists show (the same letters but for the last 4). Forms with two accents (περίβλημά, only
before a pronoun) are left out. Usage, from the root of the repository: tools/import-hunspell-el.py el_GR.dic
"""
import sys
import unicodedata

MAX_SHORT = 8
ENDING = 4
HEADER = """# Greek word forms selected from el_GR 0.9 (Hunspell), by tools/import-hunspell-el.py: a Modification of its el_GR.dic.
# The contents of this file are subject to the Mozilla Public License Version 1.1 (the "License"); you may not use this
# file except in compliance with the License. You may obtain a copy of the License at http://www.mozilla.org/MPL/
# Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express
# or implied. See the License for the specific language governing rights and limitations under the License.
# Original authors: Steve Stavropoulos, Evripidis Papakostas and the contributors in README_el_GR.txt. Source: https://github.com/jumberties/agk-wordlists
# Changes by A Good Keyboard (2026-11-04): forms left out as described in tools/import-hunspell-el.py, converted to UTF-8.
"""


def fold(word):
    decomposed = unicodedata.normalize("NFD", word.lower().replace("ς", "σ"))
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def accents(word):
    return unicodedata.normalize("NFD", word).count("́")


def known_words():
    for name in ("dictionaries/lexicon_el.tsv", "dictionaries/extra_el.tsv"):
        with open(name, encoding="utf-8") as lines:
            for line in lines:
                if "\t" in line and not line.startswith("#"):
                    yield line.split("\t")[0]


def main(path):
    beginnings = set()
    for word in known_words():
        folded = fold(word)
        beginnings.update(folded[:k] for k in range(4, len(folded) + 1))
    with open(path, encoding="iso8859-7") as lines:
        forms = [line.strip() for line in lines][1:]
    kept = []
    for form in forms:
        folded = fold(form)
        if form and accents(form) <= 1 and (len(folded) <= MAX_SHORT or folded[:max(4, len(folded) - ENDING)] in beginnings):
            kept.append(form)
    with open("dictionaries/wordlist_el.txt", "w", encoding="utf-8") as out:
        out.write(HEADER + "\n".join(kept) + "\n")
    print(f"{len(kept)} formes de {len(forms)}")


if __name__ == "__main__":
    main(sys.argv[1])
