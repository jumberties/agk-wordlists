# Occitan: word counts derived from Wikipedia

These files are made from sentences of the **Occitan Wikipedia** (https://oc.wikipedia.org), written by its contributors and published under
**Creative Commons Attribution-ShareAlike** (3.0 and 4.0). The sentences are the 100,000 of the Occitan Wikipedia corpus of the
**Leipzig Corpora Collection** (Goldhahn, Eckart and Quasthoff, "Building Large Monolingual Dictionaries at the Leipzig Corpora Collection:
From 100 to 200 Languages", LREC 2012), as published in **OcWikiAnnot v1.0** (Aleksandra Miletić, University of Helsinki, 2023,
https://doi.org/10.5281/zenodo.7777340, under CC BY 4.0). Read on 2026-11-15; only the `# text =` line of each sentence was used.

**These counts are shared under CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/, full text in
[`../licenses/CC-BY-SA-4.0.txt`](../licenses/CC-BY-SA-4.0.txt)). They come without warranty. A Good Keyboard uses them to suggest Occitan words.

| File | What it holds |
|---|---|
| [`counts_lexicon_oc.tsv.gz`](counts_lexicon_oc.tsv.gz) | 61,493 words with how often they appear (at least 3 times). |
| [`counts_ngrams_oc.tsv.gz`](counts_ngrams_oc.tsv.gz) | The 39,996 commonest sequences of 2 or 3 words, with their counts (`<s>` marks the start of a sentence). |

## What was changed

The typographic apostrophe became the straight one; the one sentence that shares six words in a row with a text the keyboard keeps apart
to measure itself was dropped; the rest was turned into counts. Then 135 words that the rest of the keyboard's Occitan dictionary writes
with more accents and at least 20 times as often ("escola" for "escòla", "esser" for "èsser") were left out, with the sequences that
contain them: Wikipedia has such forms in names and quotations, and they would stop the keyboard from correcting the slip. The text itself
is not redistributed.

In the keyboard these counts are **two files of their own** (`oc.viquipedia.lexicon` and `oc.viquipedia.ngrams`), never mixed into the
files that hold the other Occitan lists and texts; the keyboard puts them together in memory when it loads the language. No technical
measure restricts their use.
