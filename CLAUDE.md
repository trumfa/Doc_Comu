# Instruccions per a Claude Code en aquest repositori

@AGENTS.md

(`AGENTS.md` s'importa sempre: és el protocol de consulta i de vigència.)

- **Per respondre preguntes sobre la documentació**: segueix [`AGENTS.md`](AGENTS.md) (índexs primer, `docs/` com a zona de consulta, comprova sempre la vigència).
- **Per incorporar o reorganitzar documents**: segueix [`convencions/CURACIO.md`](convencions/CURACIO.md). Resum:
  1. Els documents nous arriben a `inbox/` (`.md` i el `.pdf` original amb el mateix nom).
  2. Executa `python3 scripts/find_duplicates.py` per detectar duplicats, versions i substitucions.
  3. Proposa nom, carpeta i metadades (esquema a [`convencions/METADADES.md`](convencions/METADADES.md)) i **espera l'aprovació** de la persona responsable.
  4. No reescriguis el text legal: només el format. Les dades dubtoses es marquen a `revisio`, no s'inventen.
  5. Regenera els índexs (`scripts/build_index.py`) i valida (`scripts/validate.py`) abans de fer commit.
- Idioma: català.
