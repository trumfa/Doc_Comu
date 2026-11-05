#!/usr/bin/env python3
"""Genera els índexs a partir de les metadades dels documents (no s'editen a mà).

  python3 scripts/build_index.py [--avui AAAA-MM-DD]

Escriu: catalog.json, INDEX.md, VIGENCIA.md i un INDEX.md a cada carpeta amb documents.
"""
import json, sys, datetime, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, iter_docs, read_doc

AVUI = datetime.date.today().isoformat()
if '--avui' in sys.argv:
    AVUI = sys.argv[sys.argv.index('--avui') + 1]

NOM_CARPETA = {
    'docs': 'Zona de consulta', 'arxiu': 'Arxiu (derogat, substituït, caducat o versions anteriors)',
    'legislacio': 'Legislació (Andorra i internacional)', 'normativa-comu': "Normativa del Comú d'Encamp",
    'actes-consell': 'Actes del Consell de Comú', 'politiques-internes': 'Polítiques internes', 'funcionament': 'Informació de funcionament',
    'constitucio': 'Constitució', 'lleis': 'Lleis (Consell General)', 'convenis-internacionals': 'Convenis internacionals',
    'reglaments-govern': 'Decrets i reglaments del Govern', 'ordinacions': 'Ordinacions comunals', 'reglaments-comu': 'Reglaments del Comú',
    'decrets-comu': 'Decrets del Comú', 'edictes-i-avisos': 'Edictes, avisos i correccions', 'seguretat-informacio': 'Seguretat de la informació',
    'recursos-humans-i-etica': 'Recursos humans i ètica', 'procediments': 'Procediments', 'models': 'Models de documentació'}
ESTAT_ICONA = {'vigent': 'vigent', 'modificat': 'vigent, modificat', 'derogat_parcialment': 'parcialment derogat', 'derogat': 'derogat',
               'substituit': 'substituït', 'versio_anterior': 'versió anterior', 'caducat': 'caducat', 'pendent_entrada_vigor': 'pendent d’entrar en vigor',
               'dubtosa': 'vigència dubtosa', 'no_publicat': 'no publicat', 'n_a': '—'}


def vig(m):
    parts = []
    if m.get('data_entrada_vigor'):
        parts.append(f"des de {m['data_entrada_vigor']}")
    if m.get('data_fi_vigencia'):
        parts.append(f"fins a {m['data_fi_vigencia']}")
    return ' · '.join(parts) or (m.get('entrada_vigor') or '')


def load():
    docs = []
    for zona, p in iter_docs():
        meta, _ = read_doc(p)
        meta = dict(meta)
        meta['path'] = p.relative_to(ROOT).as_posix()
        meta['zona'] = zona
        docs.append(meta)
    return docs


def row(m, base):
    rel = Path(m['path']).relative_to(base).as_posix() if base else m['path']
    avis = []
    if m.get('revisio'):
        avis.append('⚠ revisar')
    if m.get('text_complet') is False:
        avis.append('text parcial')
    extra = (' · ' + ', '.join(avis)) if avis else ''
    return f"| [{m.get('titol', m['id'])}]({rel}) | {m.get('tipus', '')} | {m.get('data_aprovacio', '')} | {ESTAT_ICONA.get(m.get('estat'), m.get('estat', ''))}{extra} | {vig(m)} | {', '.join(m.get('temes', []))} |"


def write_folder_indexes(docs):
    by = collections.defaultdict(list)
    for m in docs:
        by[Path(m['path']).parent].append(m)
    for folder, items in by.items():
        base = ROOT / folder
        items.sort(key=lambda m: (m.get('data_aprovacio') or '0000', m['id']), reverse=True)
        nom = NOM_CARPETA.get(folder.name, folder.name)
        out = [f'# {nom}', '', f'_{len(items)} documents. Índex generat automàticament (scripts/build_index.py); no s\'edita a mà._', '',
               '| Títol | Tipus | Aprovació | Estat | Vigència | Temes |', '|---|---|---|---|---|---|']
        out += [row(m, folder) for m in items]
        (base / 'INDEX.md').write_text('\n'.join(out) + '\n', encoding='utf-8')


def tree_counts(docs, zona):
    c = collections.Counter()
    for m in docs:
        if m['zona'] != zona:
            continue
        parts = Path(m['path']).parent.parts
        for i in range(2, len(parts) + 1):
            c[Path(*parts[:i])] += 1
    return c


def write_root(docs):
    nd = sum(1 for m in docs if m['zona'] == 'docs')
    na = len(docs) - nd
    out = ["# Repositori de documentació del Comú d'Encamp", '',
           "Normativa (lleis, ordinacions, reglaments, decrets), actes, polítiques internes i informació de funcionament, en Markdown i amb metadades.",
           '**Agents: llegiu primer [AGENTS.md](AGENTS.md).**', '',
           f"_Índex generat automàticament el {AVUI}. {nd} documents a la zona de consulta i {na} a l'arxiu._", '',
           '## Zona de consulta (`docs/`)', '']
    counts = tree_counts(docs, 'docs')
    for folder in sorted(counts, key=lambda p: p.as_posix()):
        depth = len(folder.parts) - 2
        if depth > 1:
            continue
        out.append(f"{'  ' * depth}- [{NOM_CARPETA.get(folder.name, folder.name)}]({folder.as_posix()}/INDEX.md) — {counts[folder]} documents")
    out += ['', '## Altres zones', '',
            '- [`arxiu/`](arxiu/): normes derogades, substituïdes, caducades i versions anteriors. Només per a consultes històriques.',
            '- [`originals/`](originals/): PDF originals, per verificar un dubte concret sobre el text.',
            '- [`VIGENCIA.md`](VIGENCIA.md): normes amb data de fi, pendents d\'entrar en vigor o amb vigència dubtosa.',
            '- [`catalog.json`](catalog.json): totes les metadades en un sol fitxer.', '',
            '## Tipus de document (zona de consulta)', '', '| Tipus | Documents |', '|---|---|']
    ct = collections.Counter(m.get('tipus') for m in docs if m['zona'] == 'docs')
    out += [f'| {t} | {n} |' for t, n in ct.most_common()]
    (ROOT / 'INDEX.md').write_text('\n'.join(out) + '\n', encoding='utf-8')


def write_vigencia(docs):
    def sect(title, items, note=''):
        o = [f'## {title}', '']
        if note:
            o += [note, '']
        if not items:
            return o + ['_Cap._', '']
        o += ['| Document | Estat | Vigència | Nota |', '|---|---|---|---|']
        for m in items:
            o.append(f"| [{m.get('titol', m['id'])}]({m['path']}) | {ESTAT_ICONA.get(m.get('estat'), '')} | {vig(m)} | {m.get('vigencia_nota', '')} |")
        return o + ['']
    live = [m for m in docs if m['zona'] == 'docs']
    pend = [m for m in live if m.get('estat') == 'pendent_entrada_vigor']
    fin = sorted([m for m in live if m.get('data_fi_vigencia') and m.get('estat') not in ('caducat',)], key=lambda m: m['data_fi_vigencia'])
    expired = [m for m in fin if m['data_fi_vigencia'] < AVUI]
    soon = [m for m in fin if AVUI <= m['data_fi_vigencia']]
    dub = [m for m in live if m.get('estat') in ('dubtosa', 'derogat_parcialment', 'no_publicat')]
    rev = [m for m in live if m.get('revisio')]
    out = ['# Vigència', '', f'_Informe generat automàticament amb data {AVUI} (scripts/build_index.py)._', '']
    out += sect("Pendents d'entrar en vigor", pend, "Aprovats però encara no aplicables (entrada en vigor aplaçada).")
    out += sect('Amb data de fi propera o futura', soon, 'Vigència limitada (any natural, mandat, pla…).')
    out += sect('Amb data de fi ja passada però encara a la zona de consulta', expired, 'Possiblement caducats: confirmeu-ne l\'estat.')
    out += sect('Vigència dubtosa, parcial o no publicats', dub)
    out += ['## Documents amb revisió pendent', '']
    for m in rev:
        out.append(f"- [{m.get('titol', m['id'])}]({m['path']}): " + ' · '.join(m['revisio']))
    (ROOT / 'VIGENCIA.md').write_text('\n'.join(out) + '\n', encoding='utf-8')


def main():
    docs = load()
    docs.sort(key=lambda m: m['id'])
    (ROOT / 'catalog.json').write_text(json.dumps(docs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    write_folder_indexes(docs)
    write_root(docs)
    write_vigencia(docs)
    print(f'{len(docs)} documents indexats ({sum(1 for m in docs if m["zona"] == "docs")} a docs/, {sum(1 for m in docs if m["zona"] == "arxiu")} a arxiu/).')


if __name__ == '__main__':
    main()
