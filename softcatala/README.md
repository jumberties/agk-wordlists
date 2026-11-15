# Catalan: verb forms from Softcatalà's dictionary

[`verb_forms_ca.txt`](verb_forms_ca.txt) holds 12,363 Catalan verb forms taken from **Softcatalà's Catalan dictionary**
(`catalan-dict-tools`, by Jaume Ortolà and Softcatalà, https://github.com/Softcatala/catalan-dict-tools), the dictionary behind
Softcatalà's verb conjugator and the LanguageTool checker. The copy used is the one published at
[softcatala/catalan-dictionary](https://huggingface.co/datasets/softcatala/catalan-dictionary) (`data.zip`, `diccionari.txt` of
2026-07-29), read on 2026-11-15; it is kept unchanged in [`../sources/ca_softcatala/`](../sources/ca_softcatala/), with its README
and tagset (sha256 of `data.zip`: `47ab7e719fd1432ba84bd42a481ffeca66e3949f18a5ba037ac5db68678c8695`).

The original is distributed under the **GNU LGPL 2.1** and the **GNU GPL 2.0**. **This list is shared under the GNU LGPL 2.1**
([`../licenses/LGPL-2.1.txt`](../licenses/LGPL-2.1.txt), with [`../licenses/GPL-2.0.txt`](../licenses/GPL-2.0.txt)), and so is
[`../tools/build-softcatala.py`](../tools/build-softcatala.py), which makes it. It comes without warranty. A Good Keyboard uses it
so that it knows the forms of common verbs its own Catalan text never showed (subjunctives such as "suggereixi", "distingeixi").

[`verb_forms_ca_balearic.txt`](verb_forms_ca_balearic.txt) holds 1,655 more forms that are only Balearic (variant tags B and Z, and the
subjunctives such as "cantàs", "cantàssim"): the keyboard adds them only when its Balearic option is on.

## What was changed

Only verbs were taken, and of each verb only the forms the keyboard's Catalan dictionary lacked, when that dictionary has the verb's
infinitive 10 times or more. Only the general and central variants (variant tags 0, C, X and Y, and the subjunctives in -és and
-essis); forms that are only Balearic, only Valencian, northern or old were left out. Lemmas and tags were dropped: the list is the
forms alone, in lower case, one per line. Because the choice depends on the keyboard's own word counts, the list here is the reference.

In the keyboard the list is **a file of its own** (`ca.softcatala.lexicon`), never mixed into the other Catalan data; the keyboard
adds it to the dictionary in memory, with the lowest frequency.
