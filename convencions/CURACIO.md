# Procés de curació: incorporar documents nous

Objectiu: que cada document nou quedi classificat, amb metadades fiables i sense duplicar ni deixar normes obsoletes a la zona de consulta.

## 1. Entrada
Els documents arriben a `inbox/` com a parella `Nom.md` + `Nom.pdf` (amb la pàgina de pujada, que converteix els PDF i els envia al repo).

## 2. Anàlisi
1. `python3 scripts/find_duplicates.py` compara la bústia amb el repo i entre si: **duplicats exactes**, **versions** (mateix text amb diferències) i fitxers que **contenen** un altre.
2. Identifica el document: títol, tipus, àmbit, data, referència (BOPA). El nom del fitxer indica de quina norma es tracta; el que el PDF porti d'altres normes (fragments) s'ignora.
3. Comprova la **vigència** (vegeu [VIGENCIA.md](VIGENCIA.md)): entrada en vigor, data de fi, normes que modifica, substitueix o deroga. Cerca a `catalog.json` les normes relacionades.
4. **Substitucions**: si el document nou reemplaça un d'anterior (p. ex. el pressupost del 2027 vs. el del 2026), proposa passar l'anterior a `arxiu/` (`estat: substituit`, `substituit_per`), arxivar-lo o mantenir-lo; **decideix la persona responsable**.
5. Decideix carpeta i `id` ([TAXONOMIA.md](TAXONOMIA.md), [NOMS-I-IDS.md](NOMS-I-IDS.md)).

## 3. Proposta i revisió
Es presenta la proposta (nom, carpeta, metadades, duplicats, substitucions, dubtes). **Res es mou fins que la persona responsable l'aprova** o l'edita. Els dubtes es deixen a `revisio`, no s'inventen dades.

## 4. Aplicació
- El text legal **no es reescriu**; només el format (paraules tallades, títols, llistes).
- Escriu el `.md` amb frontmatter a `docs/…` (o `arxiu/…`), mou el PDF a `originals/…`, esborra els duplicats.
- `python3 scripts/build_index.py` (índexs i informe de vigència) i `python3 scripts/validate.py`.
- Commit amb un missatge clar.

## 5. Reestructurar
Si l'entrada de documents nous obliga a canviar l'estructura, es fa un pla de moviments, es revisa i s'aplica amb `git mv`. Com que les relacions van per `id`, no es trenquen.

## 6. Verificació periòdica
`VIGENCIA.md` s'ha de revisar sovint: normes amb data de fi passada, pendents que ja han entrat en vigor, vigències dubtoses.
