# Noms de fitxer i identificadors

El nom del fitxer és l'`id`: `<àmbit>-<tipus>-<data>-<paraules>.md`.

- **àmbit**: `enc` (Comú d'Encamp), `and` (Govern / Consell General / Andorra), `int` (internacional).
- **tipus**: `llei`, `decret`, `reglament`, `ord`, `reg`, `acta`, `pol`, `protocol`, `manual`, `pla`, `calendari`…
- **data**: `AAAAMMDD` (aprovació); `AAAA` si només es coneix l'any; `AAAA-NNN` per a les lleis (any i número); `sd` si no hi ha data.
- **paraules**: fins a 7 paraules significatives del títol, en minúscules i sense accents.

Exemples: `and-llei-2022-014-contractacio-publica`, `enc-ord-20251218-preus-publics-2026`, `enc-acta-20250925-cc-08-25`.

## Regles

- L'`id` **no canvia mai**. Si un document es mou de carpeta, canvia el camí però no l'`id`; les relacions (`modifica`, `substitueix`…) usen l'`id`.
- El PDF original té el mateix nom: `originals/<mateixa-ruta>/<id>.pdf`.
- Si dos documents generen el mateix `id`, el segon porta el sufix `-2`.
