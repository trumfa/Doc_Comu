#!/usr/bin/env python3
"""Aplica el pla de classificació (proposta/PLA.json) a la carpeta inbox/.

  python3 scripts/apply_plan.py            # aplica el pla
  python3 scripts/apply_plan.py --dry-run  # només mostra què faria

Per a cada document: escriu el .md amb metadades a docs/ o arxiu/, mou el PDF original
a originals/, esborra els duplicats i crea els documents resultants de dividir un BOPA conjunt.
Només cal executar-lo un cop, des d'un inbox/ intacte (després el pla és «historial»).
"""
import json, re, shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, dump_frontmatter

DRY = '--dry-run' in sys.argv
INBOX = ROOT / 'inbox'


def lead_notes(text):
    """Separa les línies inicials d'avís del convertidor (> ...) del cos del text."""
    lines = text.split('\n')
    i = 0
    while i < len(lines) and (lines[i].startswith('>') or not lines[i].strip()):
        i += 1
    return '\n'.join(lines[:i]).strip(), '\n'.join(lines[i:])


def apply_retall(rest, retall):
    if retall.get('inici_a'):
        m = re.search(retall['inici_a'], rest)
        if not m:
            raise SystemExit(f"retall: no es troba l'inici {retall['inici_a']!r}")
        rest = rest[m.start():]
    if retall.get('final_despres'):
        m = re.search(retall['final_despres'], rest)
        if not m:
            raise SystemExit(f"retall: no es troba el final {retall['final_despres']!r}")
        rest = rest[:m.end()]
    return rest


def compose(meta, body):
    return f"{dump_frontmatter(meta)}\n\n# {meta['titol']}\n\n{body.strip()}\n"


def write(path, content):
    if DRY:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def move(src, dst):
    if DRY:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))


def main():
    plan = json.loads((ROOT / 'proposta' / 'PLA.json').read_text(encoding='utf-8'))
    sources = {}
    for it in plan:                                   # llegeix tots els orígens abans de moure res
        o = it.get('origen') or it.get('origen_divisio', {}).get('nom')
        if o and o not in sources:
            sources[o] = (INBOX / f'{o}.md').read_text(encoding='utf-8')
    n = {'escrits': 0, 'pdf': 0, 'duplicats': 0, 'fills': 0}
    for it in plan:
        acc = it['accio']
        if acc == 'proposta_descartar':
            continue
        if acc == 'eliminar_duplicat':
            for ext in ('md', 'pdf'):
                f = INBOX / f"{it['origen']}.{ext}"
                if f.exists() and not DRY:
                    f.unlink()
            n['duplicats'] += 1
            continue
        meta = it['meta']
        if acc == 'crear_per_divisio':
            od = it['origen_divisio']
            lines = sources[od['nom']].split('\n')
            r = od['rang']
            assert lines[r['inici']].strip().startswith(r['primera'][:25]), f"divisió: línia {r['inici']} no coincideix amb {r['primera']!r}"
            body = '\n'.join(lines[r['inici']:r['fi']] if r['fi'] else lines[r['inici']:])
            write(ROOT / it['path'], compose(meta, body))
            n['fills'] += 1
            continue
        head, rest = lead_notes(sources[it['origen']])
        if it.get('retall'):
            rest = apply_retall(rest, it['retall'])
        write(ROOT / it['path'], compose(meta, (head + '\n\n' if head else '') + rest))
        n['escrits'] += 1
        if meta.get('font_original'):
            move(INBOX / f"{it['origen']}.pdf", ROOT / meta['font_original'])
            n['pdf'] += 1
        if not DRY:
            (INBOX / f"{it['origen']}.md").unlink()
    print(('[simulació] ' if DRY else '') + f"documents escrits: {n['escrits']} · PDF moguts: {n['pdf']} · duplicats esborrats: {n['duplicats']} · documents nous per divisió: {n['fills']}")
    left = sorted(p.name for p in INBOX.glob('*') if p.is_file() and p.name != '.gitkeep') if INBOX.exists() else []
    print('Queda a inbox/:', left if left else 'res')


if __name__ == '__main__':
    main()
