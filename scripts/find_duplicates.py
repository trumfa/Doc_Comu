#!/usr/bin/env python3
"""Detecta duplicats i versions entre els documents de inbox/ i el repositori.

  python3 scripts/find_duplicates.py [carpeta]      (per defecte: inbox/)

Compara el text normalitzat dels .md:
  - IDÈNTIC: mateix text (duplicat exacte)
  - VERSIÓ:  molt semblant (>= 35 % de Jaccard o >= 60 % de contenció): versions o fitxers que se superposen
"""
import re, sys, zlib, itertools
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, iter_docs, read_doc


def norm(text):
    text = re.sub(r'^>.*$', '', text, flags=re.M)
    return re.sub(r'\W+', ' ', text.lower()).strip()


def shingles(t, k=6, mod=16):
    w = t.split()
    return {h for i in range(len(w) - k + 1) if (h := zlib.crc32(' '.join(w[i:i + k]).encode())) % mod == 0}


def main():
    src = ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'inbox')
    items = {}
    for p in sorted(src.glob('*.md')):
        items[p.relative_to(ROOT).as_posix()] = norm(p.read_text(encoding='utf-8', errors='replace'))
    base = {}
    for zona, p in iter_docs():
        meta, body = read_doc(p)
        base[f"{p.relative_to(ROOT).as_posix()} ({meta.get('id', '')})"] = norm(body)
    allitems = {**items, **base}
    sh = {k: shingles(v) for k, v in allitems.items()}
    found = 0
    for a, b in itertools.combinations(allitems, 2):
        if a in base and b in base:
            continue                                  # només interessen parelles amb algun fitxer de la bústia
        if allitems[a] and allitems[a] == allitems[b]:
            print(f'IDÈNTIC  {a}\n         {b}'); found += 1; continue
        sa, sb = sh[a], sh[b]
        if min(len(sa), len(sb)) < 8:
            continue
        i = len(sa & sb); j = i / len(sa | sb); c = i / min(len(sa), len(sb))
        if j >= 0.35 or c >= 0.6:
            print(f'VERSIÓ   J={j:.2f} C={c:.2f}  {a}\n         {b}'); found += 1
    print(f'{found} coincidències.')


if __name__ == '__main__':
    main()
