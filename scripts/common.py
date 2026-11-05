"""Utilitats compartides: lectura i escriptura de metadades (frontmatter) sense dependències externes.

El frontmatter és YAML vàlid però restringit: una clau per línia; els valors són cadenes
entre cometes dobles, llistes en format JSON, números, booleans o dates sense cometes.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

KEY_ORDER = ['id', 'titol', 'tipus', 'ambit', 'organisme', 'numero', 'data_aprovacio', 'data_publicacio', 'referencia',
             'tipus_text', 'sessio', 'versio_text',
             'estat', 'estat_font', 'entrada_vigor', 'data_entrada_vigor', 'data_fi_vigencia', 'vigencia_nota',
             'modifica', 'modificat_per', 'substitueix', 'substituit_per', 'desenvolupa', 'desenvolupat_per', 'versio_de',
             'refs_externes', 'conte', 'temes', 'resum', 'resum_origen',
             'text_complet', 'pagines_sense_text', 'pagines_amb_imatges', 'font_original', 'font_nota', 'revisio']

TIPUS = {'constitucio', 'conveni-internacional', 'llei', 'decret-govern', 'reglament-govern', 'ordinacio', 'reglament-comu',
         'decret-comu', 'edicte', 'avis', 'correccio-errata', 'oferta-ocupacio', 'acta', 'politica', 'protocol', 'cartell',
         'procediment', 'manual', 'pla', 'calendari', 'formacio', 'model', 'funcionament'}
ESTATS = {'vigent', 'modificat', 'derogat_parcialment', 'derogat', 'substituit', 'versio_anterior', 'caducat',
          'pendent_entrada_vigor', 'dubtosa', 'no_publicat', 'n_a'}
ESTATS_ARXIU = {'derogat', 'substituit', 'versio_anterior', 'caducat'}


def fmt(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return json.dumps(v, ensure_ascii=False)
    s = str(v)
    return s if re.fullmatch(r'\d{4}-\d{2}-\d{2}', s) else json.dumps(s, ensure_ascii=False)


def dump_frontmatter(meta):
    keys = [k for k in KEY_ORDER if k in meta] + sorted(k for k in meta if k not in KEY_ORDER)
    lines = ['---'] + [f'{k}: {fmt(meta[k])}' for k in keys if meta[k] not in (None, '', [])] + ['---']
    return '\n'.join(lines)


def parse_value(raw):
    raw = raw.strip()
    if raw[:1] in '"[{' or raw in ('true', 'false', 'null') or re.fullmatch(r'-?\d+(\.\d+)?', raw):
        try:
            return json.loads(raw)
        except ValueError:
            pass
    return raw


def split_frontmatter(text):
    """Retorna (metadades, cos). Si no hi ha frontmatter, ({}, text)."""
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n', 4)
    if end < 0:
        return {}, text
    meta = {}
    for line in text[4:end].split('\n'):
        m = re.match(r'^([A-Za-z_][\w]*):\s*(.*)$', line)
        if m:
            meta[m.group(1)] = parse_value(m.group(2))
    return meta, text[end + 5:]


def read_doc(path):
    text = Path(path).read_text(encoding='utf-8')
    meta, body = split_frontmatter(text)
    return meta, body


def iter_docs(zones=('docs', 'arxiu')):
    for z in zones:
        base = ROOT / z
        if base.exists():
            for p in sorted(base.rglob('*.md')):
                if p.name.upper() in ('INDEX.MD', 'README.MD'):
                    continue
                yield z, p
