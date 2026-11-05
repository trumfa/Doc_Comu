#!/usr/bin/env python3
"""Valida les metadades i la coherència del repositori. Surt amb codi 1 si hi ha errors."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, iter_docs, read_doc, TIPUS, ESTATS, ESTATS_ARXIU

DATA = re.compile(r'^\d{4}-\d{2}-\d{2}$')
REQUERITS = ['id', 'titol', 'tipus', 'ambit', 'estat']
REL = ['modifica', 'modificat_per', 'substitueix', 'substituit_per', 'desenvolupa', 'desenvolupat_per']


def main():
    errors, warns = [], []
    docs = {}
    for zona, p in iter_docs():
        meta, body = read_doc(p)
        rel = p.relative_to(ROOT).as_posix()
        docs[meta.get('id', rel)] = (zona, rel, meta)
    ids = set(docs)
    seen = {}
    for i, (zona, rel, m) in docs.items():
        e = lambda msg: errors.append(f'{rel}: {msg}')
        for k in REQUERITS:
            if not m.get(k):
                e(f'falta «{k}»')
        if m.get('id') and Path(rel).stem != m['id']:
            e(f"el nom del fitxer no coincideix amb l'id ({m['id']})")
        if m.get('tipus') and m['tipus'] not in TIPUS:
            e(f"tipus desconegut «{m['tipus']}»")
        if m.get('estat') and m['estat'] not in ESTATS:
            e(f"estat desconegut «{m['estat']}»")
        for k in ('data_aprovacio', 'data_publicacio', 'data_entrada_vigor', 'data_fi_vigencia'):
            if m.get(k) and not DATA.match(str(m[k])):
                e(f'{k} no és una data AAAA-MM-DD: {m[k]!r}')
        if m.get('data_entrada_vigor') and m.get('data_fi_vigencia') and m['data_fi_vigencia'] < m['data_entrada_vigor']:
            e('la data de fi és anterior a l\'entrada en vigor')
        if zona == 'docs' and m.get('estat') in ESTATS_ARXIU:
            warns.append(f"{rel}: estat «{m['estat']}» però és a docs/ (hauria d'anar a arxiu/)")
        if zona == 'arxiu' and m.get('estat') not in ESTATS_ARXIU:
            warns.append(f"{rel}: és a arxiu/ amb estat «{m.get('estat')}»")
        if m.get('estat') == 'pendent_entrada_vigor' and not (m.get('entrada_vigor') or m.get('data_entrada_vigor')):
            e("«pendent_entrada_vigor» sense entrada_vigor ni data_entrada_vigor")
        for k in REL:
            for ref in m.get(k, []):
                if ref not in ids:
                    e(f'{k} apunta a un id inexistent: {ref}')
        if m.get('versio_de') and m['versio_de'] not in ids:
            e(f"versio_de apunta a un id inexistent: {m['versio_de']}")
        fo = m.get('font_original')
        if fo and not (ROOT / fo).exists():
            e(f'font_original no existeix: {fo}')
        if m.get('id') in seen:
            e(f"id duplicat (també a {seen[m['id']]})")
        seen[m.get('id')] = rel
    for line in warns:
        print('AVÍS  ', line)
    for line in errors:
        print('ERROR ', line)
    print(f'{len(docs)} documents validats: {len(errors)} errors, {len(warns)} avisos.')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
