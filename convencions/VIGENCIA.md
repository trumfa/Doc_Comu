# Vigència: estats i dates

La vigència és el que més pot fer errar una resposta. Cada document en porta l'estat i les dates rellevants.

| `estat` | Significat | On va |
|---|---|---|
| `vigent` | Aplicable. | `docs/` |
| `modificat` | Aplicable, però altres documents la modifiquen (`modificat_per`). | `docs/` |
| `pendent_entrada_vigor` | Aprovada, **encara no aplicable** (entrada en vigor aplaçada). | `docs/` |
| `derogat_parcialment` | Algun article no s'aplica. | `docs/` |
| `dubtosa` | No es pot afirmar que continuï vigent (cal verificar). | `docs/` |
| `no_publicat` | No ha entrat en vigor. | `docs/` |
| `substituit` | Una altra norma la reemplaça (`substituit_per`). | `arxiu/` |
| `versio_anterior` | Text anterior d'una norma vigent (`versio_de`). | `arxiu/` |
| `caducat` | Venciment pel pas del temps (any natural, mandat, termini). | `arxiu/` |
| `derogat` | Derogada. | `arxiu/` |
| `n_a` | No aplica (actes, manuals, material informatiu…). | `docs/` |

## Dates i regles

- `entrada_vigor` explica la regla (`l'endemà de la publicació al BOPA`, `als 15 dies`, `als 4 mesos`…). `data_entrada_vigor` només s'omple si la data es pot determinar (data explícita, o regla + data de publicació coneguda).
- `data_fi_vigencia` s'omple quan la vigència és limitada: pressupostos, preus i ordinacions fiscals d'un any, plans, mandats, moratòries.
- **Entrada en vigor aplaçada**: `estat: pendent_entrada_vigor` fins a la data; passat el termini, canvia a `vigent`. L'informe `VIGENCIA.md` els destaca.
- **Textos refosos**: cada modificació té la seva entrada en vigor; no s'hi posa data única.
- Una norma que **substitueix** una altra no s'esborra: la substituïda passa a `arxiu/` amb `estat: substituit` i el camp `substituit_per`.
- `estat_font: deduït` vol dir que l'estat s'ha inferit del corpus (p. ex. una norma posterior que la reemplaça) i convé verificar-lo.
- **Limitació**: només es pot saber què diuen els documents que són al repo. Una norma pot estar derogada per una altra que no hi és; per això es marquen les relacions amb `refs_externes` i els casos dubtosos.
