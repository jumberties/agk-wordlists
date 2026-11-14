# Basque: word counts derived from EusCrawl

These files are made from **EusCrawl v2**, the corpus of Basque websites published under Creative Commons licences, by the HiTZ Center
and the IXA group of the University of the Basque Country (UPV/EHU): Artetxe, Aldabe, Agerri, Perez-de-Viñaspre and Soroa,
"Does Corpus Quality Really Matter for Low-Resource Languages?", EMNLP 2022, https://www.ixa.eus/euscrawl/. The part used is
`euscrawl-v2-free/train_00000.jsonl.gz` of [HiTZ/latxa-corpus-v2](https://huggingface.co/datasets/HiTZ/latxa-corpus-v2), read on 2026-11-14.

Each EusCrawl document states its licence. **Only the documents under Creative Commons Attribution-ShareAlike (3.0, 4.0 or no version
given) were used**; those under non-commercial or no-derivatives licences (Hitza, Bilbo Hiria) and those without one were left out.
Of the CC BY-SA ones, 39% were taken at random: 57,783 articles, 11.8 million words, by their authors at Berria (14,287), Goiena,
Kronika, Ataria, Erran, Guaixe, Anboto, Aiaraldea, Uztarria, Aiurri, Hiruka, Euskalerria Irratia, Alea, Txintxarri, Noaua, Argia (1,157),
Maxixatzen, Plaentxia, Zarauzko Hitza, Karkara, Geuria, Aikor, Amezti, Sarean and the Basque Wikipedia.

**These counts are shared under CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/, full text in
[`../licenses/CC-BY-SA-4.0.txt`](../licenses/CC-BY-SA-4.0.txt); version 3.0 allows a later version with the same elements). They come
without warranty. A Good Keyboard uses them to suggest Basque words.

| File | What it holds |
|---|---|
| [`documents.tsv.gz`](documents.tsv.gz) | Every article used: EusCrawl id, website, author (when the website gives one), licence and address. |
| [`counts_lexicon_eu.tsv.gz`](counts_lexicon_eu.tsv.gz) | 171,844 words with how often they appear (at least 3 times). |
| [`counts_ngrams_eu.tsv.gz`](counts_ngrams_eu.tsv.gz) | The 1,400,000 commonest sequences of 2 or 3 words, with their counts (`<s>` marks the start of a sentence). |

## What was changed

The articles were split into paragraphs; the paragraphs that share six words in a row with the text the keyboard keeps apart to
measure itself were dropped (6 of them); the rest was turned into counts. The text itself is not redistributed: read it from the
address above.

In the keyboard these counts are **two files of their own** (`eu.euscrawl.lexicon` and `eu.euscrawl.ngrams`), never mixed into the
files that hold the other Basque lists and texts; the keyboard puts them together in memory when it loads the language. No technical
measure restricts their use.
