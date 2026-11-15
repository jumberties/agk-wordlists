# Occitan: word counts derived from Jornalet

These files are made from news of **Jornalet, gaseta occitana d'informacions** (https://www.jornalet.com/), published by the
Associacion entara Difusion d'Occitània en Catalonha (ADÒC). Its legal notice says Jornalet "es editat en regim de dreches Creative
Commons (CC-BY) (Atribucion, partatge dins las meteissa condicions 3.0)", that is **CC BY-SA 3.0**; photographs, opinion articles,
linked blogs and contributed materials are not under that licence and were not used.

**What was used:** 1,528 news articles, from 2012 to 2026, saved from the website by the author of A Good Keyboard on 2026-11-15, without
opinion, blogs or contributions. Every article is listed in [`documents.tsv.gz`](documents.tsv.gz) with its address, date and author (when
the page names one; otherwise it is by Jornalet's newsroom).

**These counts are shared under CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/, full text in
[`../licenses/CC-BY-SA-4.0.txt`](../licenses/CC-BY-SA-4.0.txt); version 3.0 allows a later version with the same elements). They come
without warranty. A Good Keyboard uses them to suggest Occitan words.

| File | What it holds |
|---|---|
| [`documents.tsv.gz`](documents.tsv.gz) | Every article used: address, date and author. |
| [`counts_lexicon_oc.tsv.gz`](counts_lexicon_oc.tsv.gz) | 31,396 words with how often they appear (at least twice). |
| [`counts_ngrams_oc.tsv.gz`](counts_ngrams_oc.tsv.gz) | 92,117 sequences of 2 or 3 words seen at least twice, with their counts (`<s>` marks the start of a sentence). |

## What was changed

The articles were split into paragraphs. Paragraphs found in three articles or more (the website's own texts, such as the call for
donations) and those that share six words in a row with the text the keyboard keeps apart to measure itself were dropped; the
typographic apostrophe became the straight one; the rest was turned into counts. The text itself is not redistributed: read it at the
addresses above.

In the keyboard these counts are **two files of their own** (`oc.jornalet.lexicon` and `oc.jornalet.ngrams`), never mixed into the
files that hold the other Occitan lists and texts; the keyboard puts them together in memory when it loads the language. No technical
measure restricts their use.
