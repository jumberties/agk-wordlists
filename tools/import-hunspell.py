#!/usr/bin/env python3
"""Expands a Hunspell .dic and .aff into the plain forms of dictionaries/wordlist_xx.txt.

Usage, from the root of the repository: tools/import-hunspell.py an path/to/an_ES.dic path/to/an_ES.aff
The rules of each language are in LANGUAGES. Only what is needed is understood: SET, PFX and SFX with their
conditions and cross products. Continuation classes are not followed: in Aragonese they only give pronouns,
which the keyboard builds by itself, and a diminutive of a diminutive (casetota). Forms with an apostrophe or
a hyphen are left out too (see core/Enclitics.kt and the elisions of core/Language.kt).
"""
import re
import sys
import unicodedata


class Rule:
    def __init__(self, flag, strip, add, flags, condition, cross):
        self.flag, self.strip, self.add, self.flags, self.cross = flag, strip, add, flags, cross
        self.condition = condition


def read_affixes(path):
    text = open(path, "rb").read()
    encoding = re.search(rb"^SET\s+(\S+)", text, re.M).group(1).decode()
    prefixes, suffixes = {}, {}
    crosses = {}
    for line in text.decode(encoding).split("\n"):
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
        (prefixes if kind == "PFX" else suffixes).setdefault(flag, []).append(Rule(flag, strip, add, flags, pattern, crosses.get(flag, False)))
    return encoding, prefixes, suffixes


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


def expand(word, flags, prefixes, suffixes, skip, keep=lambda word, rule: True):
    """The word and every form its flags give. [skip]: flags of forms the keyboard builds by itself; [keep]: which rules apply."""
    forms = {word}
    suffixed = []
    for flag in flags:
        if flag in skip:
            continue
        for rule in suffixes.get(flag, ()):
            form = apply_suffix(word, rule) if keep(word, rule) else None
            if form:
                forms.add(form)
                suffixed.append((form, rule.cross))
    for flag in flags:
        if flag in skip:
            continue
        for rule in prefixes.get(flag, ()):
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


def all_forms(dic_path, aff_path, skip=frozenset(), names_bare=True, respell=(), keep=lambda word, rule: True):
    encoding, prefixes, suffixes = read_affixes(aff_path)
    result = {}
    with open(dic_path, encoding=encoding) as lines:
        next(lines)
        for line in lines:
            line = line.strip().split("\t")[0]
            if not line or line.startswith("#"):
                continue
            word, _, flags = line.partition("/")
            for ending, general, spelled in respell:
                if word.endswith(ending):
                    flags = flags.replace(general, spelled)
            # The plural of a name is not worth a form: Fernández, not Fernándezs.
            bare = names_bare and word[0].isupper()
            # Abbreviations and Roman numerals (AEA, XII): a keyboard does not need to suggest them.
            if len(word) > 1 and word.isupper():
                continue
            for form in ({word} if bare else expand(word, flags, prefixes, suffixes, skip, keep)):
                result.setdefault(unicodedata.normalize("NFC", form), word)
    return result


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


LANGUAGES = {
    "an": {
        # C, D: pronouns after the verb. E, F, V: elided before or after a word.
        "skip": frozenset("CDEFV"),
        # Verbs in -car and -zar with the general flag A would give "buscé" and "comenzé": M and S are the rules with the spelling.
        "respell": (("car", "A", "M"), ("zar", "A", "S")),
        "keep": aragonese_rule,
        "header": """# Aragonese word forms expanded from an_ES 0.3.0 (Hunspell), by tools/import-hunspell.py: a Modification of its an_ES.dic and an_ES.aff.
# This file is available under the Mozilla Public License Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at http://www.mozilla.org/MPL/
# Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express
# or implied. See the License for the specific language governing rights and limitations under the License.
# Copyright (C) 2011 Santiago Paricio. Copyright (C) 2011-2026 Juan Pablo Martínez. See README_an_ES.txt. Source: https://github.com/jumberties/agk-wordlists
# Changes by A Good Keyboard (2026-11-04): the affix rules applied to give plain forms, without forms with an apostrophe or
# a hyphen, abbreviations, the plurals of proper names, diminutives and most feminines made from a consonant, and verbs in
# -car and -zar with the rules M and S instead of A.
""",
    },
}


def main(tag, dic_path, aff_path):
    settings = LANGUAGES[tag]
    forms = all_forms(dic_path, aff_path, settings["skip"], respell=settings["respell"], keep=settings["keep"])
    # Only letters: no apostrophes or hyphens, nor the addresses and codes some lists have (3xl.net).
    kept = sorted(form for form in forms if form.isalpha())
    with open(f"dictionaries/wordlist_{tag}.txt", "w", encoding="utf-8") as out:
        out.write(settings["header"] + "\n".join(kept) + "\n")
    print(f"{tag}: {len(kept)} formes de {len(forms)}")


if __name__ == "__main__":
    main(*sys.argv[1:])
