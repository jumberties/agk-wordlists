# Tatoeba sentences used by A Good Keyboard

A Good Keyboard builds its dictionaries and next-word counts, and trains small neural networks, partly
from sentences of [Tatoeba](https://tatoeba.org), which are under
[CC BY 2.0 FR](https://creativecommons.org/licenses/by/2.0/fr/). The app contains no sentences: only
word counts, counts of 2–3 word sequences and network weights computed from them. The app's credits
name Tatoeba; this folder adds, for each sentence used, its number and its author, so every
contributor can be credited and each sentence found at `https://tatoeba.org/sentences/show/<sentence_id>`.

| Language | File | Sentences | Authors | Without an author in the export |
|---|---|--:|--:|--:|
| Catalan | [`tatoeba_ca.tsv.gz`](tatoeba_ca.tsv.gz) | 10,745 | 182 | 47 |
| Spanish | [`tatoeba_es.tsv.gz`](tatoeba_es.tsv.gz) | 441,176 | 1,953 | 62 |
| English | [`tatoeba_en.tsv.gz`](tatoeba_en.tsv.gz) | 1,998,780 | 6,815 | 43,482 |
| French | [`tatoeba_fr.tsv.gz`](tatoeba_fr.tsv.gz) | 714,609 | 1,990 | 362 |
| German | [`tatoeba_de.tsv.gz`](tatoeba_de.tsv.gz) | 769,017 | 1,732 | 107 |
| Italian | [`tatoeba_it.tsv.gz`](tatoeba_it.tsv.gz) | 970,657 | 733 | 0 |
| Portuguese | [`tatoeba_pt.tsv.gz`](tatoeba_pt.tsv.gz) | 436,611 | 1,320 | 856 |
| Galician | [`tatoeba_gl.tsv.gz`](tatoeba_gl.tsv.gz) | 8,049 | 75 | 21 |
| Basque | [`tatoeba_eu.tsv.gz`](tatoeba_eu.tsv.gz) | 6,304 | 212 | 55 |
| Asturian | [`tatoeba_ast.tsv.gz`](tatoeba_ast.tsv.gz) | 807 | 14 | 7 |
| Aragonese | [`tatoeba_an.tsv.gz`](tatoeba_an.tsv.gz) | 102 | 3 | 98 |
| Occitan | [`tatoeba_oc.tsv.gz`](tatoeba_oc.tsv.gz) | 24,832 | 25 | 8 |
| Dutch | [`tatoeba_nl.tsv.gz`](tatoeba_nl.tsv.gz) | 197,433 | 434 | 25 |
| Polish | [`tatoeba_pl.tsv.gz`](tatoeba_pl.tsv.gz) | 134,432 | 770 | 76 |
| Romanian | [`tatoeba_ro.tsv.gz`](tatoeba_ro.tsv.gz) | 40,720 | 191 | 156 |
| Swedish | [`tatoeba_sv.tsv.gz`](tatoeba_sv.tsv.gz) | 55,727 | 314 | 257 |
| Czech | [`tatoeba_cs.tsv.gz`](tatoeba_cs.tsv.gz) | 88,260 | 217 | 1 |
| Hungarian | [`tatoeba_hu.tsv.gz`](tatoeba_hu.tsv.gz) | 434,536 | 497 | 2,104 |
| Russian | [`tatoeba_ru.tsv.gz`](tatoeba_ru.tsv.gz) | 1,209,010 | 1,573 | 47 |
| Ukrainian | [`tatoeba_uk.tsv.gz`](tatoeba_uk.tsv.gz) | 184,934 | 293 | 31 |
| Greek | [`tatoeba_el.tsv.gz`](tatoeba_el.tsv.gz) | 42,107 | 184 | 467 |

Each file is a gzipped TSV: `sentence_id`, `author` (the Tatoeba username; empty when the export gives
none, `?` when the sentence is no longer in the export), `uses`:

* `d`: counted in the dictionary and the next-word counts of that language;
* `n`: also used to train that language's neural network (Catalan, Spanish and English); the Spanish and
  English networks read a share of these, picked at random, so a listed sentence may not have been read;
* `t`: a Spanish sentence translated into Catalan by machine (the [Softcatalà](https://github.com/Softcatala/nmt-models)
  Spanish→Catalan model, MIT) to train the Catalan network. A translation is a change to the sentence.

**Changes made to every sentence:** split into words and lower-cased; punctuation, digits and symbols
dropped; apostrophe forms such as "l'home" split in two. In the dictionaries each sentence is counted three times.

**Snapshots:** the sentences are those of the keyboard's own copies of Tatoeba (26 October 2026; 4 November
for Dutch, Polish, Romanian, Swedish, Occitan, Asturian, Aragonese, Czech, Hungarian, Russian, Ukrainian and
Greek). The authors come from Tatoeba's detailed exports of 10 November 2026. Made with
[`../../tools/tatoeba-attributions.py`](../../tools/tatoeba-attributions.py).
