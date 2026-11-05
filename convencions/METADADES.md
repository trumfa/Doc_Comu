# Metadades dels documents (frontmatter)

Cada document comença amb un bloc `---` amb una clau per línia. Els valors són cadenes entre cometes, llistes en format JSON (`["a", "b"]`), números, `true/false` o dates `AAAA-MM-DD` sense cometes. Els camps buits s'ometen. L'esquema el comprova `scripts/validate.py`.

## Identificació

| Camp | Obligatori | Descripció |
|---|---|---|
| `id` | sí | Identificador estable i únic; coincideix amb el nom del fitxer. Vegeu [NOMS-I-IDS.md](NOMS-I-IDS.md). **No canvia mai**, encara que el document canviï de carpeta. |
| `titol` | sí | Títol oficial o descriptiu del document. |
| `tipus` | sí | `constitucio`, `conveni-internacional`, `llei`, `decret-govern`, `reglament-govern`, `ordinacio`, `reglament-comu`, `decret-comu`, `edicte`, `avis`, `correccio-errata`, `acta`, `politica`, `protocol`, `cartell`, `procediment`, `manual`, `pla`, `calendari`, `formacio`, `model`, `funcionament`. |
| `ambit` | sí | `comu` (Encamp), `govern`, `estat` (Consell General / general d'Andorra) o `internacional`. |
| `organisme` | no | Qui l'aprova o emet. |
| `numero` | no | Número oficial (`14/2022`, `391/2022`, `7/24` per a actes…). |
| `data_aprovacio` | no | Data d'aprovació o signatura. |
| `data_publicacio` | no | Data de publicació al BOPA, si consta. |
| `referencia` | no | Referència de publicació (`BOPA núm. 22, 14.04.2004`). |
| `tipus_text` | no | `oficial` o `refos-no-oficial` (text consolidat sense caràcter oficial). |
| `sessio`, `versio_text` | no | Només actes: tipus de sessió; `projecte`, `signada` o `acta`. |

## Vigència (vegeu [VIGENCIA.md](VIGENCIA.md))

| Camp | Descripció |
|---|---|
| `estat` | **Obligatori.** `vigent`, `modificat`, `derogat_parcialment`, `derogat`, `substituit`, `versio_anterior`, `caducat`, `pendent_entrada_vigor`, `dubtosa`, `no_publicat`, `n_a`. |
| `estat_font` | D'on surt l'estat: `text`, `nom del fitxer`, `deduït` (inferit del corpus; cal verificar). |
| `entrada_vigor` | Regla d'entrada en vigor, en text (`l'endemà de la publicació al BOPA`, `als 4 mesos…`). |
| `data_entrada_vigor` | Data concreta, només si es pot determinar. |
| `data_fi_vigencia` | Data de fi si la vigència és limitada (any natural, mandat, pla…). |
| `vigencia_nota` | Explicació lliure (condicions, tarifes aplaçades, dubtes). |

## Relacions entre documents (sempre per `id`)

`modifica` / `modificat_per` · `substitueix` / `substituit_per` · `desenvolupa` / `desenvolupat_per` · `versio_de` (còpia o versió d'un altre document) · `conte` (en un BOPA conjunt, les normes que inclou). `refs_externes` llista, en text, normes citades que **no són al repo** (útil per saber què falta).

## Contingut i qualitat

| Camp | Descripció |
|---|---|
| `temes` | Etiquetes temàtiques transversals (`fiscalitat-i-finances`, `urbanisme-i-habitatge`, `personal`…). Permeten trobar documents relacionats entre carpetes. |
| `resum`, `resum_origen` | Resum breu i qui l'ha fet (`auto` o `revisat`). |
| `text_complet` | `false` si el text extret no inclou tot el document. |
| `pagines_sense_text`, `pagines_amb_imatges` | Pàgines del PDF que són imatges (no convertides). |
| `font_original` | Ruta del PDF original a `originals/`. |
| `font_nota` | Observacions sobre l'origen (font no oficial, publicació conjunta…). |
| `revisio` | Llista de punts que cal revisar. Mentre hi sigui, l'índex marca el document amb ⚠. |
