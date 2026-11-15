---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- ca
license:
- gpl-2.0
- lgpl-2.1
multilinguality:
- monolingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: catalan-dictionary
---

# Dataset Card for ca-text-corpus

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Descripció (ca)

En aquest repositori s'apleguen llistes de paraules etiquetades amb la categoria gramatical, usades per a construir eines com correctors ortogràfics i gramaticals.


## Dataset Description

- **Homepage:**
- **Repository:** https://github.com/Softcatala/catalan-dict-tools
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Catalan word lists with part of speech labeling curated by humans. Contains 1 180 773 forms including verbs, nouns, adjectives, names or toponyms. These word lists are used to build applications like Catalan spellcheckers or verb querying applications.

### Supported Tasks and Leaderboards

This dataset can be used for Catalan morphological lookup, spell-checking resources, grammar-checking resources, lexicon construction, and linguistic preprocessing. It is not associated with a public leaderboard.

### Languages

Catalan (`ca`).

## Dataset Structure

The dataset contains 3 columns:
* Form (e.g. cantaré)
* Lemma (e.g. cantar)
* POS tag (e.g. VMIF1S00)

You can have the meaning of the POS tag [here](./tagset.md).

### Data Instances

Each instance represents a Catalan word form with its lemma and part-of-speech or morphological tag. For example, an entry may contain an inflected form, the corresponding lemma, and a POS tag in the tagset used by the source dictionary tooling.

### Data Fields

The logical fields are:

* `form`: surface form.
* `lemma`: base form or lemma.
* `pos_tag`: part-of-speech or morphological tag.

Depending on how the dataset is loaded, each row may be exposed as a raw text line containing these three values.

### Data Splits

The dataset provides a single `train` split.

## Dataset Creation

### Curation Rationale

The data is maintained as a reusable Catalan lexical and morphological resource for building spell checkers, grammar checkers, and related language tools.

### Source Data

#### Initial Data Collection and Normalization

The source repository contains the root dictionary data used by Softcatala to build Catalan dictionaries for Hunspell and LanguageTool. The root dictionary is organized by grammatical categories. Some files contain pseudodictionary information for inflection, while others use the LanguageTool/Freeling-style tag format.

#### Who are the source language producers?

The lexical data is maintained by Softcatala contributors and dictionary maintainers.

### Annotations

#### Annotation process

Entries are manually curated with lemma and part-of-speech or morphological information. The tags follow the conventions used by the source Catalan dictionary tooling and related LanguageTool/Freeling resources.

#### Who are the annotators?

Softcatala contributors and dictionary maintainers.

### Personal and Sensitive Information

The dataset is a lexical resource. It may include proper names and toponyms as dictionary entries, but it does not contain definitions or user-generated personal records.

## Considerations for Using the Data

### Social Impact of Dataset

The dataset supports Catalan spell checking, grammar checking, morphological processing, and other Catalan language technology.

### Discussion of Biases

Coverage reflects the editorial and practical goals of the source dictionary tools. Some domains, named entities, dialectal forms, or neologisms may be underrepresented or absent.

### Other Known Limitations

The dataset is not a semantic dictionary and does not provide definitions, examples of use, frequency information, or complete syntactic behavior. Reusers need to understand the POS tagset to interpret the tags correctly.

## Additional Information

### Dataset Curators

Softcatala and Jaume Ortola.

### Licensing Information

[LGPL 2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

[GPL 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

### Citation Information

If you use this dataset, cite the dataset repository and source tooling:

`Softcatala/catalan-dictionary` and `Softcatala/catalan-dict-tools: https://github.com/Softcatala/catalan-dict-tools`

### Contributions

Softcatalà

Jaume Ortolà
