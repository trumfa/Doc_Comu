# Taxonomia: on va cada document

```
docs/                         ZONA DE CONSULTA
├── legislacio/
│   ├── constitucio/
│   ├── lleis/                  lleis i textos refosos del Consell General
│   ├── convenis-internacionals/
│   └── reglaments-govern/      decrets i reglaments del Govern
├── normativa-comu/
│   ├── ordinacions/            ordinacions comunals
│   ├── reglaments-comu/
│   ├── decrets-comu/           decrets del Comú (estructura, comissions, reglaments aprovats per decret…)
│   └── edictes-i-avisos/       edictes, avisos, correccions d'errates
├── actes-consell/<any>/        actes i projectes d'acta del Consell de Comú
├── politiques-internes/
│   ├── seguretat-informacio/
│   ├── recursos-humans-i-etica/
│   └── procediments/
├── funcionament/               manuals, plans, calendaris, formació
└── models/                     plantilles i models de documentació
arxiu/                        derogat, substituït, caducat o versió anterior (mateixa estructura)
originals/                    PDF originals (mateixa estructura que docs/ i arxiu/)
inbox/                        pendent de processar
```

## Criteris

- **Àmbit abans que tipus**: el que aprova el Comú d'Encamp va a `normativa-comu/`; el que aprova el Govern o el Consell General, a `legislacio/`.
- Un **decret amb número** (`Decret 391/2022`) és del Govern; un **«Decret del 18-1-2024…»** és del Comú.
- Les **modificacions** viuen al costat de la norma que modifiquen (mateixa carpeta, relació `modifica`).
- Un text que només es pot **consultar a l'arxiu** (derogat, substituït, caducat, versió anterior) va a `arxiu/` amb la mateixa subcarpeta.
- Quan una carpeta es faci massa gran o un grup de documents no encaixi, es **replanteja** l'estructura: es mouen els fitxers (`git mv`), els `id` no canvien i es regeneren els índexs.
