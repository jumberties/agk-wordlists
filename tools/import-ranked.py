#!/usr/bin/env python3
"""Writes dictionaries/wordlist_xx.txt from a list with far more forms than a keyboard should keep, the most useful ones first.

Usage, from the root of the repository:
  tools/import-ranked.py eu LIMIT path/to/eu_ES.dic path/to/eu_ES.aff
  tools/import-ranked.py sv LIMIT path/to/ordlista-sv.txt

LIMIT is the number of forms in the list that the keyboard does not have yet.

Basque: Hunspell chains suffixes, which gives about 2,900 million forms. The endings the shipped text really uses are learnt
from a sample of stems, only those are generated, and the commonest endings go to every stem and the rarer ones only to the
stems the shipped text shows. Forms with a hyphen and proper names with an ending are left out (core/WordShapes.kt
builds the cases of a word it does not know).

Swedish: the list already has every form. First the word families the shipped text shows, then the rest by length, and last
the forms in -s of another form (mostly genitives; core/WordShapes.kt builds the compounds).
"""
import collections
import heapq
import re
import sys

KNOWN_WORDS = ("dictionaries/lexicon_{tag}.tsv", "dictionaries/extra_{tag}.tsv")
SOURCE = "# Original files and licence: https://github.com/jumberties/agk-wordlists\n"
LGPL = "# This list is free software under the GNU Lesser General Public License, version 3 or (Basque) any later version; WITHOUT ANY WARRANTY.\n"
HEADERS = {
    "eu": "# Basque word forms selected from Xuxen 5.4.10, as in Debian hunspell-eu, by tools/import-ranked.py: a modified version of its eu_ES.dic and eu_ES.aff.\n"
          + LGPL + "# Copyright (C) 2006-2007 Eleka Ingeniaritza Linguistikoa S.L. Copyright (C) 2014-2015 Elhuyar Hizkuntza eta Teknologia.\n" + SOURCE
          + "# Changes by A Good Keyboard (2026-11-05): suffix chains applied to give plain forms, and only the forms described in the script kept.\n",
    "sv": "# Swedish word forms selected from ordlista-sv.txt of ordfinnare.se, the forms of SFOL 2.42 (Den Stora Fria Ordlistan), by tools/import-ranked.py: a modified version.\n"
          + LGPL + "# Copyright (C) 2003-2015 Goran Andersson.\n" + SOURCE
          + "# Changes by A Good Keyboard (2026-11-05): only the forms described in the script kept.\n",
}


def known_counts(tag):
    counts = collections.Counter()
    for name in KNOWN_WORDS:
        with open(name.format(tag=tag), encoding="utf-8") as lines:
            for line in lines:
                if "\t" in line and not line.startswith("#"):
                    word, count = line.split("\t")[:2]
                    if count.strip().isdigit():
                        counts[word.lower()] = max(counts[word.lower()], int(count))
    return counts


def beginnings_of(words, shortest=4):
    found = set()
    for word in words:
        found.update(word[:k] for k in range(shortest, len(word) + 1))
    return found


def write_list(tag, forms):
    with open(f"dictionaries/wordlist_{tag}.txt", "w", encoding="utf-8") as out:
        out.write(HEADERS[tag] + "\n".join(sorted(forms)) + "\n")
    print(f"{tag}: {len(forms)} formes")


# Basque.
NEED_AFFIX = "1"
LEARNING_DEPTH = 3
STEMS_TO_LEARN_FROM = 12000
ENDINGS = 500
# The rank of an ending counts this many times more for a stem no text shows.
UNSEEN_STEM = 6


class Suffix:
    __slots__ = ("strip", "add", "flags", "condition")

    def __init__(self, strip, add, flags, condition):
        self.strip, self.add, self.flags, self.condition = strip, add, flags, condition


def read_suffixes(path):
    rules = collections.defaultdict(list)
    with open(path, encoding="utf-8") as lines:
        for line in lines:
            parts = line.split("#")[0].split()
            if len(parts) < 4 or parts[0] != "SFX" or (parts[2] in "YN" and parts[3].isdigit()):
                continue
            add, _, flags = parts[3].partition("/")
            condition = parts[4] if len(parts) > 4 else "."
            rules[parts[1]].append(Suffix("" if parts[2] == "0" else parts[2], "" if add == "0" else add, tuple(flags.split(",")) if flags else (),
                                          None if condition == "." else re.compile(condition + "$")))
    return rules


def read_stems(path):
    with open(path, encoding="utf-8") as lines:
        next(lines)
        for line in lines:
            word, _, flags = line.strip().partition("/")
            if word and "-" not in word and word.isalpha():
                yield word, flags.split(",") if flags else []


def chains(rules, word, flags, depth, ending, usable, alive=None):
    """(form, the letters the suffixes added) of every word the rules make from [word]. [usable]: the rules of a flag worth trying after
    an ending; [alive]: a form that can still lead somewhere."""
    for flag in flags:
        if flag == NEED_AFFIX:
            continue
        for rule in usable(flag, ending):
            if rule.condition and not rule.condition.search(word) or rule.strip and not word.endswith(rule.strip):
                continue
            form = word[: len(word) - len(rule.strip)] + rule.add
            if alive is not None and form not in alive:
                continue
            whole = ending + rule.add
            if NEED_AFFIX not in rule.flags:
                yield form, whole
            if depth > 1 and rule.flags:
                yield from chains(rules, form, rule.flags, depth - 1, whole, usable, alive)


def learn_endings(rules, stems, counts):
    """The endings of the words the text shows, the most used first. Only chains that are the beginning of one of those words."""
    beginnings = beginnings_of(counts, 3)
    seen = [stem for stem in stems if stem[0][0].islower() and stem[0] in beginnings]
    weights = collections.Counter()
    for word, flags in seen[:: max(1, len(seen) // STEMS_TO_LEARN_FROM)]:
        for form, ending in chains(rules, word, flags, LEARNING_DEPTH, "", lambda flag, _: rules.get(flag, ()), beginnings):
            count = counts.get(form)
            if count:
                weights[ending] += count
    return [ending for ending, _ in weights.most_common(ENDINGS)]


def basque(limit, dic_path, aff_path):
    counts = known_counts("eu")
    rules = read_suffixes(aff_path)
    stems = list(read_stems(dic_path))
    endings = learn_endings(rules, stems, counts)
    rank = {ending: position for position, ending in enumerate(endings)}
    wanted = {ending[:k] for ending in endings for k in range(len(ending) + 1)}
    kept = {}

    def usable(flag, ending):
        """The rules of a flag that can still give one of the endings: a class can have thousands, and few are of any use."""
        found = kept.get((flag, ending))
        if found is None:
            found = [rule for rule in rules.get(flag, ()) if ending + rule.add in wanted]
            kept[(flag, ending)] = found
        return found

    beginnings = beginnings_of(counts, 4)
    best = {}
    names = 0
    for word, flags in stems:
        if not word[0].islower():
            # A name, without endings: the keyboard builds the cases by itself.
            if NEED_AFFIX not in flags and not word.isupper():
                names += 1
                best[word] = len(endings) * UNSEEN_STEM
            continue
        cost = 1 if word in beginnings or word[:-1] in beginnings else UNSEEN_STEM
        if NEED_AFFIX not in flags:
            best[word] = min(best.get(word, 1 << 30), 0)
        for form, ending in chains(rules, word, flags, LEARNING_DEPTH, "", usable):
            place = rank.get(ending)
            if place is not None and form not in counts:
                value = place * cost
                if value < best.get(form, 1 << 30):
                    best[form] = value
    print(f"eu: {len(stems)} arrels, {len(endings)} terminacions, {len(best)} formes candidates, {names} noms")
    print("eu: terminacions:", " ".join(ending or "∅" for ending in endings[:40]))
    return {form for form in heapq.nsmallest(limit, best, key=best.get)}


# Swedish.
def swedish_tier(word, words, beginnings):
    derived = word.endswith("s") and word[:-1] in words
    length = len(word)
    shown = word[: max(4, length - 4)] in beginnings
    if not derived and shown:
        return 0, length
    if not derived and length <= 9:
        return 1, length
    if derived and shown and length <= 10 and not word.endswith(("ornas", "arnas", "ernas", "ens", "ets")):
        return 2, length
    if not derived:
        return 3, length
    return 4, length


def swedish(limit, list_path):
    counts = known_counts("sv")
    beginnings = beginnings_of(counts, 4)
    with open(list_path, encoding="utf-8") as lines:
        words = {line.strip() for line in lines if line.strip()}
    new = [word for word in words if word not in counts]
    return set(heapq.nsmallest(limit, new, key=lambda word: swedish_tier(word, words, beginnings) + (word,)))


def main(tag, limit, *paths):
    limit = int(limit)
    write_list(tag, basque(limit, *paths) if tag == "eu" else swedish(limit, *paths))


if __name__ == "__main__":
    main(*sys.argv[1:])
