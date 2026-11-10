"""Per-sentence attribution of the Tatoeba sentences A Good Keyboard counts (dictionaries, n-grams) and
trains its neural networks on. Writes OUT/tatoeba_<lang>.tsv.gz: sentence_id, author, uses.
Authors come from Tatoeba's detailed exports of 10/11/2026 (the user's corpus cache, and agk-corpus/tatoeba-detailed
for cs hu ru uk el); AGK's own copy (26/10 or 04/11) has no authors. Read-only on every input.

    attributions.py OUT
"""
import bz2, gzip, os, re, sys
from collections import defaultdict
HOME = os.path.expanduser("~")
MNT = "/mnt/dec33760-501f-47b1-995f-7035aae179d9"
CACHE = f"{MNT}/multilingual_keyboard_corpus/cache/processed/tatoeba"
EXTRA = f"{MNT}/agk-corpus/tatoeba-detailed"
ISO = dict(ca="cat", es="spa", en="eng", fr="fra", de="deu", it="ita", pt="por", gl="glg", eu="eus", ast="ast", an="arg", oc="oci",
           nl="nld", pl="pol", ro="ron", sv="swe", cs="ces", hu="hun", ru="rus", uk="ukr", el="ell")
NETWORK = {"ca", "es", "en"}  # languages with a shipped network trained on their Tatoeba text (docs/XARXA_NEURONAL.md)
out = sys.argv[1]
os.makedirs(out, exist_ok=True)


def agk_copy(lang):
    p = f"{HOME}/agk-corpus/tatoeba/{ISO[lang]}_sentences.tsv"
    f = open(p, encoding="utf-8") if os.path.exists(p) else bz2.open(f"{MNT}/agk-corpus/tatoeba/{ISO[lang]}_sentences.tsv.bz2", "rt", encoding="utf-8")
    for line in f:
        p = line.rstrip("\n").split("\t")
        if len(p) >= 3:
            yield p[0], p[2]


def authors(lang):
    p = f"{CACHE}/{lang}_sentences_detailed.tsv"
    f = open(p, encoding="utf-8") if os.path.exists(p) else bz2.open(f"{EXTRA}/{ISO[lang]}_sentences_detailed.tsv.bz2", "rt", encoding="utf-8")
    a = {}
    for line in f:
        p = line.rstrip("\n").split("\t")
        if len(p) >= 4:
            a[p[0]] = p[3] if p[3] and p[3] != "\\N" else ""
    return a


def translated_ids():
    """The Spanish sentences tools/nn/translate.py turned into Catalan: same order, unique texts, at most 25 words, the first 352,820."""
    seen, ids = set(), []
    for sid, text in agk_copy("es"):
        text = text.strip()
        if not text or text in seen or len(text.split()) > 25:
            continue
        seen.add(text); ids.append(sid)
        if len(ids) == 352820:
            break
    return ids


summary = []
extra_uses = defaultdict(set)
for sid in translated_ids():
    extra_uses[sid].add("t")
for lang in ISO:
    used_texts = set(l.rstrip("\n") for l in open(f"{HOME}/agk-corpus/split/{lang}/train/tatoeba-x3.txt", encoding="utf-8"))
    who = authors(lang)
    rows, unknown = [], 0
    for sid, text in agk_copy(lang):
        uses = set()
        if text in used_texts:
            uses.add("d")
            if lang in NETWORK:
                uses.add("n")
        if lang == "es":
            uses |= extra_uses.get(sid, set())
        if not uses:
            continue
        author = who.get(sid)
        if author is None:
            unknown += 1; author = "?"
        rows.append((int(sid), author or "", "".join(sorted(uses))))
    rows.sort()
    path = f"{out}/tatoeba_{lang}.tsv.gz"
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=9) as w:
        w.write("sentence_id\tauthor\tuses\n")
        for r in rows:
            w.write(f"{r[0]}\t{r[1]}\t{r[2]}\n")
    n_authors = len(set(r[1] for r in rows if r[1] not in ("", "?")))
    summary.append((lang, len(rows), n_authors, sum(1 for r in rows if r[1] == ""), unknown, os.path.getsize(path)))
    print(*summary[-1], flush=True)
with open(f"{out}/summary.tsv", "w", encoding="utf-8") as w:
    w.write("language\tsentences\tauthors\twithout_author\tno_longer_at_tatoeba\tbytes\n")
    for s in summary:
        w.write("\t".join(map(str, s)) + "\n")
