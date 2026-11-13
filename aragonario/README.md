# Aragonese: files derived from the Aragonario

These files are made from the **Aragonario**, the Spanish-Aragonese, Aragonese-Spanish and Aragonese definitions dictionary of the
Gobierno de Aragón (Proyecto Linguatec), https://aragonario.aragon.es. Its content is under the **Creative Commons Attribution-ShareAlike 4.0
International** licence (CC BY-SA 4.0), as its legal notice says: https://aragonario.aragon.es/aviso-legal/

© Gobierno de Aragón, Proyecto Linguatec. The licence: https://creativecommons.org/licenses/by-sa/4.0/ (full text in
[`../licenses/CC-BY-SA-4.0.txt`](../licenses/CC-BY-SA-4.0.txt)). The material comes without warranty.

**These derived files are shared under the same licence, CC BY-SA 4.0.** A Good Keyboard uses them to suggest Aragonese words.

## What they are

The dictionary was read on 2026-11-13 through its public API (`https://aragonario.aragon.es/api/words/`, 105,398 entries, one request a second).

| File | What it holds |
|---|---|
| [`map_es_an.tsv`](map_es_an.tsv) | 149,476 Spanish words, each with up to 3 Aragonese forms, the standard ones first. A form weighs more when the general entry gives it, when many varieties (Tensino, Ansotano, Cheso, Bajorribagorzano, Benasqués, Belsetán, Chistabín, Somontanos…) do, when the dictionary gives the pair the other way round too, and when it is in the Aragonese text. |
| [`overrides_es_an.tsv`](overrides_es_an.tsv) | The most frequent Spanish words, where the many senses made the ranking unreliable: forms proposed by the keyboard's author and kept only where the Aragonario has them. They replace the same words in the map. |
| [`words_an.tsv`](words_an.tsv) | 178,215 Aragonese forms (word, 1), with the verb forms of every conjugation table. Regular verbs take the table of their model verb with their own stem. |
| [`sentences_an.txt`](sentences_an.txt) | 21,412 Aragonese sentences: the examples and the Aragonese definitions. 5% of them are kept apart to measure with, and are not here. |
| [`counts_ngrams_an.tsv`](counts_ngrams_an.tsv), [`counts_lexicon_an.tsv`](counts_lexicon_an.tsv) | Counts of words and of sequences of 2 or 3 words that the keyboard adds to its Aragonese ones: those of the sentences, plus the counts of Spanish projected through the map (4% of them). |

## What was changed

Words and sentences were selected; the forms were split by variety; verb forms were derived from the conjugation tables and from the models; Aragonese
forms were lined up with Spanish ones (the map); sentences and Spanish counts were turned into word counts. The originals are not redistributed: read them
from the API above.

The forms have **not been reviewed by Aragonese speakers**. Varieties differ a great deal, so the map keeps several forms per word.
