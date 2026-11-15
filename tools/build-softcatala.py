#!/usr/bin/env python3
"""Catalan verb forms from Softcatalà's dictionary (catalan-dict-tools, LGPL 2.1 / GPL 2.0) -> the layer ca_softcatala.

The corpus shows only some forms of each verb ("predir" had no "predigui", test log of 2026-11-15). Softcatalà's dictionary
lists every form of every verb with its tag (VMSP3S0Y: subjunctive present, 3rd singular, central and Balearic). This
keeps the forms the Catalan dictionary lacks of the verbs it has (infinitive seen --min times or more), only of the
general and central variants (0, C, X, Y and the subjunctives -és, -essis), at the lowest frequency. Balearic-only,
Valencian-only, northern and old forms are left out. See dictionaries/softcatala/LICENCE.md.

Usage: python3 -I tools/build-softcatala.py diccionari.txt [--min 3] [--out dictionaries/layers/ca_softcatala]
"""
import argparse
import collections
import os

KEPT_VARIANTS = set("0CXY12")
COUNT = 3


def read_counts(path):
    counts = {}
    if not os.path.exists(path):
        return counts
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2 and parts[1].strip().lstrip("-").isdigit():
                counts[parts[0].lower()] = max(counts.get(parts[0].lower(), 0), int(parts[1]))
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary")
    parser.add_argument("--min", type=int, default=3)
    parser.add_argument("--dictionaries", default="dictionaries")
    parser.add_argument("--out", default="dictionaries/layers/ca_softcatala")
    args = parser.parse_args()

    lexicon = read_counts(os.path.join(args.dictionaries, "lexicon_ca.tsv"))
    present = set(lexicon)
    for name in ("extra_ca.tsv", "compounds_ca.tsv", "contributed_ca.tsv"):
        present |= set(read_counts(os.path.join(args.dictionaries, name)))

    lemmas = collections.defaultdict(set)
    with open(args.dictionary, encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if len(parts) != 3 or not parts[2].startswith("V") or len(parts[2]) < 8 or parts[2][7] not in KEPT_VARIANTS:
                continue
            form = parts[0].lower()
            if form.isalpha() or all(c.isalpha() or c == "·" for c in form):
                lemmas[form].add(parts[1].lower())

    forms = sorted(form for form, of in lemmas.items()
                   if form not in present and any(lexicon.get(lemma, 0) >= args.min for lemma in of))
    os.makedirs(args.out, exist_ok=True)
    header = "# Softcatalà's Catalan dictionary (catalan-dict-tools, LGPL 2.1 / GPL 2.0): verb forms, see tools/build-softcatala.py and dictionaries/softcatala/LICENCE.md.\n"
    with open(os.path.join(args.out, "lexicon.tsv"), "w", encoding="utf-8") as out:
        out.write(header)
        for form in forms:
            out.write(f"{form}\t{COUNT}\n")
    with open(os.path.join(args.out, "ngrams.tsv"), "w", encoding="utf-8") as out:
        out.write(header)
    print(f"{len(forms)} formes -> {args.out}/lexicon.tsv")


if __name__ == "__main__":
    main()
