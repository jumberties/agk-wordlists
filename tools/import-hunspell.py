#!/usr/bin/env python3
"""Expands a Hunspell .dic and .aff into the plain forms of dictionaries/wordlist_xx.txt.

Usage, from the root of the repository: tools/import-hunspell.py xx path/to/xx.dic path/to/xx.aff
The rules of each language are in LANGUAGES. Only what is needed is understood: SET, FLAG, PFX and SFX with their
conditions and cross products, and the flags of words that are not valid on their own. Continuation classes are not
followed: they only give pronouns, which the keyboard builds by itself, and a diminutive of a diminutive. Forms with a
hyphen are left out too (see core/Enclitics.kt and the elisions of core/Language.kt).

All the forms of a large dictionary would not fit in a phone's memory (829,000 Greek forms take 98 MB), so [select]
keeps the short ones and the longer ones whose word family the shipped text or the project's lists show.
"""
import re
import sys
import unicodedata

KNOWN_WORDS = ("dictionaries/lexicon_{tag}.tsv", "dictionaries/extra_{tag}.tsv")


class Rule:
    def __init__(self, flag, strip, add, flags, condition, cross):
        self.flag, self.strip, self.add, self.flags, self.cross = flag, strip, add, flags, cross
        self.condition = condition


def split_flags(text, long_flags):
    return [text[i:i + 2] for i in range(0, len(text), 2)] if long_flags else list(text)


class Affixes:
    def __init__(self, path):
        text = open(path, "rb").read()
        self.encoding = re.search(rb"^SET\s+(\S+)", text, re.M).group(1).decode()
        decoded = text.decode(self.encoding)
        self.long_flags = re.search(r"^FLAG\s+long", decoded, re.M) is not None
        # Flags of words that are no word on their own, or that must not be suggested.
        self.invalid = set(re.findall(r"^(?:NEEDAFFIX|FORBIDDENWORD|NOSUGGEST|ONLYINCOMPOUND)\s+(\S+)", decoded, re.M))
        self.prefixes, self.suffixes = {}, {}
        crosses = {}
        for line in decoded.split("\n"):
            parts = line.split("#")[0].split()
            if len(parts) < 4 or parts[0] not in ("PFX", "SFX"):
                continue
            kind, flag = parts[0], parts[1]
            if parts[2] in ("Y", "N") and parts[3].isdigit():
                crosses[flag] = parts[2] == "Y"
                continue
            strip = "" if parts[2] == "0" else parts[2]
            add, _, flags = parts[3].partition("/")
            add = "" if add == "0" else add
            condition = parts[4] if len(parts) > 4 else "."
            pattern = re.compile(("^" + condition) if kind == "PFX" else (condition + "$")) if condition != "." else None
            table = self.prefixes if kind == "PFX" else self.suffixes
            table.setdefault(flag, []).append(Rule(flag, strip, add, split_flags(flags, self.long_flags), pattern, crosses.get(flag, False)))


def apply_suffix(word, rule):
    if rule.condition and not rule.condition.search(word):
        return None
    if rule.strip and not word.endswith(rule.strip):
        return None
    return word[: len(word) - len(rule.strip)] + rule.add


def apply_prefix(word, rule):
    if rule.condition and not rule.condition.search(word):
        return None
    if rule.strip and not word.startswith(rule.strip):
        return None
    return rule.add + word[len(rule.strip):]


def expand(word, flags, affixes, skip, keep=None):
    """The word and every form its flags give. [skip]: flags of forms the keyboard builds by itself; [keep]: which rules apply."""
    forms = {word}
    suffixed = []
    for flag in flags:
        if flag in skip:
            continue
        for rule in affixes.suffixes.get(flag, ()):
            if keep and not keep(word, rule) or affixes.invalid.intersection(rule.flags):
                continue
            form = apply_suffix(word, rule)
            if form:
                forms.add(form)
                suffixed.append((form, rule.cross))
    for flag in flags:
        if flag in skip:
            continue
        for rule in affixes.prefixes.get(flag, ()):
            form = apply_prefix(word, rule)
            if form:
                forms.add(form)
            if rule.cross:
                for suffixed_form, cross in suffixed:
                    if cross:
                        form = apply_prefix(suffixed_form, rule)
                        if form:
                            forms.add(form)
    return forms


def all_forms(dic_path, aff_path, settings):
    """Every plain form, one at a time (some dictionaries give millions)."""
    affixes = Affixes(aff_path)
    # Productive prefixes give forms nobody writes (rejubilaserăți, niegołąbkowskimi); the usual ones are words of their own.
    if settings.get("no_prefixes"):
        affixes.prefixes = {}
    skip, respell, keep = settings.get("skip", ()), settings.get("respell", ()), settings.get("keep")
    with open(dic_path, encoding=affixes.encoding) as lines:
        next(lines)
        for line in lines:
            line = line.strip().split("\t")[0]
            if not line or line.startswith("#"):
                continue
            word, _, text = line.partition("/")
            for ending, general, spelled in respell:
                if word.endswith(ending):
                    text = text.replace(general, spelled)
            flags = split_flags(text, affixes.long_flags)
            if affixes.invalid.intersection(flags):
                continue
            # Abbreviations and Roman numerals (AEA, XII): a keyboard does not need to suggest them.
            if len(word) > 1 and word.isupper():
                continue
            # The plural of a name is not worth a form: Fernández, not Fernándezs.
            for form in ({word} if word[0].isupper() else expand(word, flags, affixes, skip, keep)):
                yield unicodedata.normalize("NFC", form)


def fold(word):
    decomposed = unicodedata.normalize("NFD", word.lower().replace("ς", "σ").replace("й", "\0"))
    return "".join(c for c in decomposed if not unicodedata.combining(c)).replace("\0", "й")


def known_beginnings(tag):
    beginnings = set()
    for name in KNOWN_WORDS:
        with open(name.format(tag=tag), encoding="utf-8") as lines:
            for line in lines:
                if "\t" in line and not line.startswith("#"):
                    folded = fold(line.split("\t")[0])
                    beginnings.update(folded[:k] for k in range(4, len(folded) + 1))
    return beginnings


def is_word(form, apostrophe):
    """Only letters: no hyphens, nor the addresses and codes some lists have (3xl.net)."""
    return (form.replace("'", "") if apostrophe else form).isalpha()


def forms_of(tag, dic_path, aff_path):
    settings = LANGUAGES[tag]
    selection = settings.get("select")
    beginnings = known_beginnings(tag) if selection else None
    apostrophe = settings.get("apostrophe", False)
    kept, total = set(), 0
    for form in all_forms(dic_path, aff_path, settings):
        form = form.translate(AS_TYPED)
        if not is_word(form, apostrophe) or (settings.get("one_accent") and unicodedata.normalize("NFD", form).count("\u0301") > 1):
            continue
        total += 1
        if selection:
            folded = fold(form)
            short, ending, minimum = selection
            if len(folded) > short and (len(folded) - ending < minimum or folded[:len(folded) - ending] not in beginnings):
                continue
        kept.add(form)
    return kept, total


# What a keyboard types: the straight apostrophe, and i + j (OpenTaal writes every Dutch ij with the single letter).
AS_TYPED = str.maketrans({"ʼ": "'", "’": "'", "`": "'", "ĳ": "ij", "Ĳ": "IJ"})

def aragonese_rule(word, rule):
    """A spell checker can accept more than it should; a keyboard would suggest it (telefonoot, unidata)."""
    if rule.flag != "B":
        return True
    # The diminutives and augmentatives, which fit any noun.
    if "B" in rule.flags:
        return False
    # A feminine from any consonant: only the endings of adjectives and of people (chicot, zagal, francés, profesor).
    if rule.add == "a" and not rule.strip:
        return word.endswith(("or", "ol", "al", "ot", "et", "és", "ín"))
    return True


MPL = """# This file is available under the Mozilla Public License Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at http://www.mozilla.org/MPL/
# Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express
# or implied. See the License for the specific language governing rights and limitations under the License.
"""
SOURCE = "# Original files and licence: https://github.com/jumberties/agk-wordlists\n"
SELECTED = "# Changes by A Good Keyboard (2026-11-05): the affix rules applied to give plain forms, and only part of them kept, as described in tools/import-hunspell.py.\n"

LANGUAGES = {
    "el": {
        # Forms of up to [0] letters, and the rest with a known beginning of at least [2] letters, but for the last [1].
        "select": (8, 4, 5),
        # περίβλημά, only before a pronoun.
        "one_accent": True,
        "header": "# Greek word forms selected from el_GR 0.9 (Hunspell), by tools/import-hunspell.py: a Modification of its el_GR.dic.\n" + MPL +
            "# Original authors: Steve Stavropoulos, Evripidis Papakostas and the contributors in README_el_GR.txt.\n" + SOURCE +
            "# Changes by A Good Keyboard (2026-11-04): forms left out as described in tools/import-hunspell.py, converted to UTF-8.\n",
    },
    "an": {
        # C, D: pronouns after the verb. E, F, V: elided before or after a word.
        "skip": frozenset("CDEFV"),
        # Verbs in -car and -zar with the general flag A would give "buscé" and "comenzé": M and S are the rules with the spelling.
        "respell": (("car", "A", "M"), ("zar", "A", "S")),
        "keep": aragonese_rule,
        "header": "# Aragonese word forms expanded from an_ES 0.3.0 (Hunspell), by tools/import-hunspell.py: a Modification of its an_ES.dic and an_ES.aff.\n" + MPL +
            "# Copyright (C) 2011 Santiago Paricio. Copyright (C) 2011-2026 Juan Pablo Martínez. See README_an_ES.txt.\n" + SOURCE +
            "# Changes by A Good Keyboard (2026-11-04): the affix rules applied to give plain forms, without forms with an apostrophe or\n"
            "# a hyphen, abbreviations, the plurals of proper names, diminutives and most feminines made from a consonant, and verbs in\n"
            "# -car and -zar with the rules M and S instead of A.\n",
    },
    "ro": {
        "select": (7, 2, 5),
        "no_prefixes": True,
        "header": "# Romanian word forms selected from RoSpell 3.3.10 (Hunspell), by tools/import-hunspell.py: a Modification of its ro_RO.dic and ro_RO.aff.\n" + MPL +
            "# Copyright (C) 2005-2013 Rospell Team, http://rospell.sourceforge.net. See README_EN.txt.\n" + SOURCE + SELECTED,
    },
    "uk": {
        "select": (5, 2, 5),
        "apostrophe": True,
        "header": "# Ukrainian word forms selected from the uk_UA dictionary of LibreOffice, based on dict_uk (Hunspell), by tools/import-hunspell.py: a Modification.\n" + MPL +
            "# Original package: Andriy Rysin, 2007-2017, https://github.com/brown-uk/dict_uk. See README_uk_UA.txt.\n" + SOURCE + SELECTED,
    },
    "pl": {
        "select": (5, 2, 5),
        "no_prefixes": True,
        "header": "# Polish word forms selected from the sjp.pl spelling dictionary, 2026-05-11 (Hunspell), by tools/import-hunspell.py.\n"
            "# Used under the Creative Commons Attribution 4.0 International licence, https://creativecommons.org/licenses/by/4.0/\n"
            "# Source: https://sjp.pl/sl/en/ See README_pl_PL.txt.\n" + SOURCE + SELECTED,
    },
    "nl": {
        "select": (6, 3, 5),
        "apostrophe": True,
        "header": "# Dutch word forms selected from the OpenTaal spelling dictionary (Hunspell), by tools/import-hunspell.py.\n"
            "# Used under the Creative Commons Attribution 3.0 Unported licence, https://creativecommons.org/licenses/by/3.0/\n"
            "# Creator: OpenTaal, https://opentaal.org. Source: https://github.com/OpenTaal/opentaal-hunspell See LICENSE.txt.\n" + SOURCE + SELECTED,
    },
    "ru": {
        "select": (6, 1, 5),
        "header": "# Russian word forms selected from the dictionary of Alexander I. Lebedev (Hunspell), by tools/import-hunspell.py.\n"
            "# THIS IS A MODIFIED VERSION. Copyright (c) 1997-2008, Alexander I. Lebedev. All rights reserved.\n"
            "# Its conditions and disclaimer are in README_ru_RU.txt, next to the original files.\n" + SOURCE + SELECTED,
    },
}


def main(tag, dic_path, aff_path):
    kept, total = forms_of(tag, dic_path, aff_path)
    with open(f"dictionaries/wordlist_{tag}.txt", "w", encoding="utf-8") as out:
        out.write(LANGUAGES[tag]["header"] + "\n".join(sorted(kept)) + "\n")
    print(f"{tag}: {len(kept)} formes de {total}")


if __name__ == "__main__":
    main(*sys.argv[1:])
