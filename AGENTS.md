# Guia per a agents: com consultar aquest repositori

Aquest repositori és la base documental del **Comú d'Encamp** (Andorra): normativa pròpia i general, actes del Consell de Comú, polítiques internes i informació de funcionament. Tot és Markdown amb metadades al capdamunt de cada fitxer (frontmatter).

## 1. On buscar (i on NO buscar)

| Zona | Per a què | Quan llegir-la |
|---|---|---|
| [`docs/`](docs/) | **Zona de consulta.** Documents vigents o d'interès actual. | Sempre. |
| [`arxiu/`](arxiu/) | Normes derogades, substituïdes, caducades i versions anteriors. | Només si et pregunten per la història o per una data passada. |
| [`originals/`](originals/) | PDF originals de cada document. | Només per verificar un dubte concret del text. |
| [`inbox/`](inbox/) | Pendent de processar. | **Mai**: ignora-ho. |
| `scripts/`, `convencions/`, `proposta/` | Per a qui cura el repositori. | No per respondre preguntes. |

**No facis cerques per tot el repositori.** Segueix aquest camí:

1. Llegeix [`INDEX.md`](INDEX.md) i tria les carpetes que encaixen amb la pregunta.
2. Obre l'`INDEX.md` d'aquestes carpetes: cada fila diu títol, tipus, data, **estat**, vigència i temes.
3. Obre **només** els documents que l'índex et assenyala. Pots usar [`catalog.json`](catalog.json) per filtrar per `tema`, `tipus`, `estat` o dates.
4. Per a preguntes que creuen àmbits (p. ex. una taxa, la llei que la permet i la política que l'aplica), combina documents de diferents carpetes seguint els camps `modifica`, `modificat_per`, `desenvolupa` i `temes`.

## 2. La vigència és l'important

Abans de respondre amb una norma, mira sempre l'`estat` i les dates del seu frontmatter:

- `vigent`: aplicable. `modificat`: aplicable **però** té modificacions (camp `modificat_per`): llegeix també aquestes modificacions, que poden canviar el que diu el text base.
- `pendent_entrada_vigor`: aprovada però **encara no aplicable**; mira `entrada_vigor` i `data_entrada_vigor`.
- `data_fi_vigencia`: si ja ha passat, la norma és caducada (p. ex. pressupostos i preus d'un any). Compara-la amb la data d'avui.
- `dubtosa`: no es pot assegurar que continuï vigent; digues-ho a l'usuari.
- `derogat_parcialment`: algun article no s'aplica; digues-ho. `no_publicat`: no ha entrat en vigor.
- `substituit`, `versio_anterior`, `caducat`, `derogat`: són a `arxiu/`; no les presentis com a vigents.
- [`VIGENCIA.md`](VIGENCIA.md) resumeix els casos especials (data de fi, pendents, dubtosos).

## 3. Com citar i què avisar

- Cita sempre el **títol, la referència** (`referencia`, `numero`, `data_aprovacio`) i, si cal, l'article.
- El text és una conversió automàtica del PDF: pot tenir errors puntuals (paraules tallades, l'exponent dels m², taules, pàgines que només són imatges). Si `text_complet: false` o hi ha `pagines_sense_text`, **avisa** que part del contingut només és al PDF original (`font_original`).
- `tipus_text: refos-no-oficial` vol dir que és un text consolidat sense caràcter oficial: el text oficial és el publicat al BOPA.
- Si la informació és crítica (sancions, terminis, imports), recomana comprovar el PDF original i la versió oficial al BOPA.
- Si no trobes la resposta als documents, **digues-ho**; no la inventis.

## 4. Si has de modificar el repositori

Llegeix [`convencions/CURACIO.md`](convencions/CURACIO.md) i [`CLAUDE.md`](CLAUDE.md). Els índexs es generen amb `python3 scripts/build_index.py`; no s'editen a mà. Valida amb `python3 scripts/validate.py`.
