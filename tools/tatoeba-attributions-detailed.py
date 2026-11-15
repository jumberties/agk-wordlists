"""Per-sentence attribution of the Tatoeba sentences A Good Keyboard counts, for the languages whose text comes straight from
Tatoeba's detailed exports (Finnish, Turkish, Lithuanian, Esperanto, Kabyle, Berber, Tatar and Hebrew, 15/11/2026; their
dictionaries are made by tools/build-split.py of the keyboard's repository, which cleans the sentences the same way as here).
Writes OUT/tatoeba_<lang>.tsv.gz: sentence_id, author, uses (always "d": no network is trained on them).

    tatoeba-attributions-detailed.py OUT LANG...
"""
import bz2, gzip, os, sys, unicodedata

MNT = "/mnt/dec33760-501f-47b1-995f-7035aae179d9"
DETAILED = f"{MNT}/agk-corpus/tatoeba-detailed"
ISO = dict(fi="fin", tr="tur", lt="lit", eo="epo", kab="kab", ber="ber", tt="tat", he="heb")
LATIN = {"fi", "tr", "lt", "eo", "kab", "ber"}
LOOK_ALIKES = str.maketrans({"ε": "ɛ", "γ": "ɣ", "Ε": "Ɛ", "Γ": "Ɣ"})


def clean(text, lang):
    text = " ".join(unicodedata.normalize("NFC", text).split())
    return text.translate(LOOK_ALIKES) if lang in LATIN else text


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for lang in sys.argv[2:]:
    used = set(line.rstrip("\n") for line in open(os.path.expanduser(f"~/agk-corpus/split/{lang}/train/tatoeba-x3.txt"), encoding="utf-8"))
    rows, authors, without = [], set(), 0
    with bz2.open(f"{DETAILED}/{ISO[lang]}_sentences_detailed.tsv.bz2", "rt", encoding="utf-8") as lines:
        for line in lines:
            cells = line.rstrip("\n").split("\t")
            if len(cells) < 4:
                continue
            text = clean(cells[2], lang)
            if text in used:
                used.discard(text)  # the first sentence with that text is the one counted
                author = cells[3] if cells[3] and cells[3] != "\\N" else ""
                rows.append((cells[0], author))
                authors.add(author) if author else None
                without += not author
    with gzip.open(f"{out}/tatoeba_{lang}.tsv.gz", "wt", encoding="utf-8") as w:
        w.write("sentence_id\tauthor\tuses\n")
        for sid, author in rows:
            w.write(f"{sid}\t{author}\td\n")
    print(f"{lang}\t{len(rows)}\t{len(authors)}\t{without}\t0\t{os.path.getsize(f'{out}/tatoeba_{lang}.tsv.gz')}", flush=True)
