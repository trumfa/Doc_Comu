# Proposta de classificació del primer bolcat

Aquesta branca (`claude/gracious-hawking-sz6kxm`) conté la **proposta ja aplicada** sobre la bústia `inbox/`: cada document té el seu nom normalitzat, la seva carpeta i les metadades (inclosa la vigència). **`main` no s'ha tocat**: el que veus aquí no és definitiu fins que es fusioni.

## Resum

- **193 documents** a la zona de consulta (`docs/`) i **12** a `arxiu/`.
- **17 duplicats** eliminats (text idèntic o quasi idèntic), 3 documents nous creats en dividir un BOPA conjunt, 1 fitxer que proposo **descartar** (`inbox/2737E`).
- **16 documents** amb algun punt a revisar (marcats ⚠ als índexs).
- Tots els PDF originals són a `originals/` amb el mateix nom que el seu `.md`.

## Estructura

Vegeu [`convencions/TAXONOMIA.md`](../convencions/TAXONOMIA.md) i l'índex general [`INDEX.md`](../INDEX.md).

| Carpeta | Documents |
|---|---|
| `arxiu/legislacio/lleis` | 5 |
| `arxiu/normativa-comu/decrets-comu` | 2 |
| `arxiu/normativa-comu/ordinacions` | 3 |
| `arxiu/normativa-comu/reglaments-comu` | 1 |
| `arxiu/politiques-internes/recursos-humans-i-etica` | 1 |
| `docs/actes-consell/2024` | 12 |
| `docs/actes-consell/2025` | 11 |
| `docs/actes-consell/2026` | 9 |
| `docs/funcionament` | 6 |
| `docs/legislacio/constitucio` | 1 |
| `docs/legislacio/convenis-internacionals` | 2 |
| `docs/legislacio/lleis` | 30 |
| `docs/legislacio/reglaments-govern` | 24 |
| `docs/normativa-comu/decrets-comu` | 23 |
| `docs/normativa-comu/edictes-i-avisos` | 3 |
| `docs/normativa-comu/ordinacions` | 40 |
| `docs/normativa-comu/reglaments-comu` | 21 |
| `docs/politiques-internes/procediments` | 1 |
| `docs/politiques-internes/recursos-humans-i-etica` | 4 |
| `docs/politiques-internes/seguretat-informacio` | 6 |

## Per decidir

1. **Actes** (32): les he posades a `docs/actes-consell/<any>/` com a categoria nova (no era a la llista inicial). 10 són *projectes d'acta* (no signats). Voleu mantenir-los tots, o només els signats?
2. **Textos refosos de la web del Consell General** («Text refós sense caràcter oficial») i el cas de la *Llei 31/2021*, *Llei 32/2017*, *LGOTU*: he conservat el refós més recent com a text principal i he mogut l'original/anterior a `arxiu/`. Us sembla bé?
3. **`inbox/2737E`**: anunci d'una plaça del 2002 sense valor normatiu. Proposo descartar-lo (esborrar-lo).
4. **Moratòria de parcs solars** i **Decret de fitxers de dades personals**: no puc saber si continuen vigents (vegeu «Vigència dubtosa»).
5. **BOPA conjunt del 2015** (5 ordinacions): he creat 3 documents nous (cabanes, terrasses, rètols). Voleu mantenir també el BOPA conjunt sencer?
6. **Resums**: les actes porten l'ordre del dia com a resum (automàtic). Per a la resta de documents el camp `resum` és buit; es pot omplir en una segona passada (amb la IA a la pàgina de pujada) un cop aprovada l'estructura.

## Duplicats eliminats

| Fitxer eliminat | Es conserva |
|---|---|
| `733D2 (3)` | [Ordinació de modificació del Reglament d'organització i funcionament dels Comuns (2011)](docs/normativa-comu/ordinacions/enc-ord-20111109-organitzacio-funcionament-comuns.md) |
| `ActadesessioCC19122024CC001320241734990024504 (1)` | [Acta del Consell de Comú, sessió ordinària 13/24 (19-12-2024)](docs/actes-consell/2024/enc-acta-20241219-cc-13-24.md) |
| `Decret 11-1-2023, d’aprovació del Reglament de modificació del Reglament relatiu a la video` | [Decret 10/2023, de l'11-1-2023, de modificació del Reglament relatiu a la instal·lació de sistemes de videovig](docs/legislacio/reglaments-govern/and-decret-20230111-relatiu-instal-lacio-sistemes-videovigilancia.md) |
| `Decret del 27-3-2025 de modificació del Decret d'estructura organitzativa del Comú d'Encamp` | [Decret del 27-3-2025 de modificació del Decret d'estructura organitzativa](docs/normativa-comu/decrets-comu/enc-decret-20250327-estructura-organitzativa.md) |
| `L19931104F (5)` | [Llei qualificada de delimitació de competències dels Comuns, del 4 de novembre de 1993](docs/legislacio/lleis/and-llei-19931104-qualificada-delimitacio-competencies-comuns.md) |
| `QEO20151109_15_25_29` | [Decret del 5-11-2015 d'aprovació de cinc ordinacions comunals (Medi Ambient i Via Pública, aigua potable, caba](docs/normativa-comu/decrets-comu/enc-decret-20151105-cinc-ordinacions-comunals-medi-ambient-via-publica.md) |
| `QEO20211217_12_11_06 (2)` | [Ordinació del 23-12-2021 de modificació de l'Ordinació del Comú d'Encamp d'organització funcionament dels Comu](docs/normativa-comu/ordinacions/enc-ord-20211223-organitzacio-funcionament-comuns-2011.md) |
| `QEO20211224_10_59_49` | [Ordinació del 24-12-2021 de modificació de l'Ordinació de Medi Ambient i Via Pública del 5 de novembre del 201](docs/normativa-comu/ordinacions/enc-ord-20211224-medi-ambient-via-publica-2015.md) |
| `QEO20221125_10_11_03 (1)` | [Ordinació del 25.11.2022 reguladora de l'Administració electrònica](docs/normativa-comu/ordinacions/enc-ord-20221125-reguladora-administracio-electronica.md) |
| `QEO_2023_07_27_11_37_25` | [Ordinació del 28-7-2023 del Codi de conducta i bones pràctiques dels cònsols i dels consellers de Comú](docs/normativa-comu/ordinacions/enc-ord-20230728-codi-conducta-bones-practiques-consols-consellers.md) |
| `QEO_2023_07_27_11_37_25 (1)` | [Ordinació del 28-7-2023 del Codi de conducta i bones pràctiques dels cònsols i dels consellers de Comú](docs/normativa-comu/ordinacions/enc-ord-20230728-codi-conducta-bones-practiques-consols-consellers.md) |
| `QEO_2023_09_26_15_06_33` | [Decret del 28-9-2023 d'aprovació del Reglament que regula la formació del personal del Comú d'Encamp](docs/normativa-comu/decrets-comu/enc-decret-20230928-regula-formacio-personal.md) |
| `QEO_2025_01_15_11_51_08` | [Decret del 15-1-2025 d'aprovació del Reglament intern de protocol, cerimonial i d'honors i distincions atorgat](docs/normativa-comu/decrets-comu/enc-decret-20250115-intern-protocol-cerimonial-honors-distincions-ator.md) |
| `QEO_2025_12_23_10_50_57` | [Ordinació del 18-12-2025 de modificació de l'Ordinació del 29-7-2025, de la funció pública del Comú d'Encamp i](docs/normativa-comu/ordinacions/enc-ord-20251218-funcio-publica-publicacio-text-consolidat.md) |
| `R20220928B` | [Decret 391/2022, del 28 de setembre del 2022 del Reglament de protecció de dades](docs/legislacio/reglaments-govern/and-decret-20220928-proteccio-dades.md) |
| `Reglament de creació i regulació del Consell Consultiu dels jardins d'infants del Comú d'Encamp (2004) (2)` | [Reglament de creació i regulació del Consell Consultiu dels jardins d'infants del Comú d'Encamp (2004)](docs/normativa-comu/reglaments-comu/enc-reg-20040708-creacio-regulacio-consell-consultiu-jardins-infant.md) |
| `Reglament general relatiu a fires, atraccions i parades` | [Reglament relatiu a fires atraccions i parades (1998)](docs/normativa-comu/reglaments-comu/enc-reg-19980819-relatiu-fires-atraccions-parades.md) |

## Versions i documents arxivats

| Document | Estat | Motiu |
|---|---|---|
| [Text refòs de la Llei general d'ordenació del territori i urbanisme, del 29.12.2000](arxiu/legislacio/lleis/and-llei-20001229-text-refos-general-ordenacio-territori-urbanisme.md) | versio_anterior |  |
| [Llei 32/2017, del 20 de desembre, de col·laboració entre l'Administració general i els comuns, i entre els com](arxiu/legislacio/lleis/and-llei-2017-032-col-laboracio-entre-administracio-general-comuns-e.md) | versio_anterior |  |
| [Llei 31/2021, del 22 de novembre, de text consolidat qualificada de seguretat pública](arxiu/legislacio/lleis/and-llei-2021-031-text-consolidat-qualificada-seguretat-publica.md) | versio_anterior |  |
| [Llei 4/2022, del 31 de gener, del pressupost per a l'exercici del 2022](arxiu/legislacio/lleis/and-llei-2022-004-pressupost-exercici-2022.md) | caducat | Pressupost de l'exercici 2022 (vigència anual, exhaurida). |
| [Llei 1/2024, de l'1 de febrer, del pressupost per a l'exercici del 2024](arxiu/legislacio/lleis/and-llei-2024-001-pressupost-exercici-2024.md) | caducat | Pressupost de l'exercici 2024 (vigència anual, exhaurida). |
| [Decret del 24-12-2021 de modificació del Decret del 25-6-2021 que regula la moratòria d'autoritzacions de cons](arxiu/normativa-comu/decrets-comu/enc-decret-20211224-regula-moratoria-autoritzacions-construccions-parc.md) | caducat | Primera ampliació de la moratòria (2021); substituïda per decrets posteriors. |
| [Decret del 13-2-2023 de modificació del Decret d'estructura organitzativa del Comú d'Encamp](arxiu/normativa-comu/decrets-comu/enc-decret-20230213-estructura-organitzativa.md) | substituit | Substituït pel Decret d'estructura organitzativa del 18-1-2024. |
| [Ordinació de Cabanes (2015)](arxiu/normativa-comu/ordinacions/enc-ord-20151105-cabanes.md) | substituit | Substituïda per l'Ordinació del 23-12-2021 de Cabanes. |
| [Ordinació del 20-5-2022 per la qual s'acorda modificar l'Ordinació tributària per a l'any 2022](arxiu/normativa-comu/ordinacions/enc-ord-20220520-qual-s-acorda-modificar-tributaria.md) | caducat | Modifica l'ordinació tributària de l'any 2022 (vigència anual, exhaurida). |
| [Ordinació del 28-9-2023 de la funció pública del Comú d'Encamp](arxiu/normativa-comu/ordinacions/enc-ord-20230928-funcio-publica.md) | substituit | Substituïda per l'Ordinació del 29-7-2025 de la funció pública i pel seu text consolidat (Ordinació del 18-12-2025). |
| [Reglament de la biblioteca comunal d'Encamp (2003)](arxiu/normativa-comu/reglaments-comu/enc-reg-20030912-biblioteca-comunal.md) | substituit | Derogat pel Reglament de les biblioteques del 29-11-2024. |
| [Protocol de mesures preventives i d'abordatge de les conductes d'assetjament sexual, per raó de sexe i altres ](arxiu/politiques-internes/recursos-humans-i-etica/enc-protocol-sd-protocol-mesures-preventives-abordatge-conductes-a.md) | versio_anterior | Versió anterior del Protocol contra l'assetjament sexual (nom del fitxer erroni: «Decret… permisos administratius (2)»). |

## Vigència: casos especials

**Pendent d'entrar en vigor**

- [Llei 18/2026, del 15 de juliol, qualificada del Codi penal](docs/legislacio/lleis/and-llei-2026-018-qualificada-codi-penal.md): Aprovada el 15-7-2026. Entra en vigor als 4 mesos de la publicació al BOPA (data de publicació no consta al text); la DF 2a als 6 mesos i el règim de responsabilitat penal de les persones jurídiques a l'any.

**Amb data de fi (vigència limitada)**

- `2005-08-31` [Reglament de creació i regulació del Consell Consultiu dels jardins d'infants del Comú d'Encamp (2004)](docs/normativa-comu/reglaments-comu/enc-reg-20040708-creacio-regulacio-consell-consultiu-jardins-infant.md)
- `2024-12-22` [Decret del 21-12-2023 de modificació del Decret del 22 de desembre del 2022 que regula la moratòria d'autoritz](docs/normativa-comu/decrets-comu/enc-decret-20231221-2022-regula-moratoria-autoritzacions-construccions.md)
- `2026-12-31` [Calendari de dies festius i horari intensiu oficines parròquia d'Encamp](docs/funcionament/enc-calendari-20251121-calendari-dies-festius-horari-intensiu-oficines.md)
- `2026-12-31` [Pla d'igualtat del Comú d'Encamp 2023-2026](docs/funcionament/enc-pla-2023-pla-igualtat-2023-2026.md)
- `2026-12-31` [Avís del 7-8-2026 pel qual es publica l'actualització de les taules salarials anuals del Comú d'Encamp per a l](docs/normativa-comu/edictes-i-avisos/enc-avis-20260807-avis-qual-publica-actualitzacio-taules-salarials-a.md)
- `2026-12-31` [Ordinació del 18-12-2025 del pressupost per a l'exercici 2026](docs/normativa-comu/ordinacions/enc-ord-20251218-pressupost-exercici-2026.md)
- `2026-12-31` [Ordinació del 18-12-2025 de preus públics del Comú d'Encamp per l'any 2026](docs/normativa-comu/ordinacions/enc-ord-20251218-preus-publics-2026.md)
- `2026-12-31` [Ordinació del 18-12-2025 tributària de la parròquia d'Encamp per l'any 2026](docs/normativa-comu/ordinacions/enc-ord-20251218-tributaria-2026.md)
- `2026-12-31` [Ordinació del 24-4-2026 per la qual s'acorda modificar l'Ordinació del 18-12-2025 de preus públics del Comú d'](docs/normativa-comu/ordinacions/enc-ord-20260424-qual-s-acorda-modificar-preus-publics.md)
- `2026-12-31` [Ordinació del 24-4-2026 per la qual s'acorda modificar l'Ordinació del 18-12-2025 tributària de la parròquia d](docs/normativa-comu/ordinacions/enc-ord-20260424-qual-s-acorda-modificar-tributaria.md)
- `2026-12-31` [Ordinació del 22-5-2026 per la qual s'acorda modificar l'Ordinació del 18-12-2025 de preus públics del Comú d'](docs/normativa-comu/ordinacions/enc-ord-20260522-qual-s-acorda-modificar-preus-publics.md)
- `2027-12-31` [Edicte de l'1-3-2024 aprovació del marc pressupostari del Comú d'Encamp per al mandat 2024-2027](docs/normativa-comu/edictes-i-avisos/enc-edicte-20240301-edicte-pressupostari-mandat-2027.md)

**Vigència dubtosa, parcial o no publicats** (cal que decidiu o confirmeu)

- [Decret que regula els fitxers de dades personals del Comú d'Encamp (2013)](docs/normativa-comu/decrets-comu/enc-decret-20130218-regula-fitxers-dades-personals.md) — _dubtosa_: Regula els fitxers de dades personals del Comú (2013, modificat 2020 i 2021). Pot haver quedat superat per la Llei 29/2021 de protecció de dades.
- [Decret del 9-10-2020 de modificació del Decret del 4-2-2013, que regula els fitxers de dades personals del Com](docs/normativa-comu/decrets-comu/enc-decret-20201009-regula-fitxers-dades-personals.md) — _dubtosa_: Modifica el Decret de fitxers de dades personals (2013), possiblement superat per la Llei 29/2021.
- [Decret del 26-2-2021 de modificació del Decret del 4-2-2013, que regula els fitxers de dades personals del Com](docs/normativa-comu/decrets-comu/enc-decret-20210226-regula-fitxers-dades-personals.md) — _dubtosa_: Modifica el Decret de fitxers de dades personals (2013), possiblement superat per la Llei 29/2021.
- [Decret del 21-12-2023 de modificació del Decret del 22 de desembre del 2022 que regula la moratòria d'autoritz](docs/normativa-comu/decrets-comu/enc-decret-20231221-2022-regula-moratoria-autoritzacions-construccions.md) — _dubtosa_: Amplia la suspensió d'autoritzacions de parcs solars 12 mesos «fins que el Comú publiqui una nova normativa». La darrera ampliació present al repo acaba cap al 22-12-2024.
- [Ordinació de modificació de l'Ordinació de Medi Ambient i Via Pública (2017)](docs/normativa-comu/ordinacions/enc-ord-20171215-medi-ambient-via-publica.md) — _derogat_parcialment_: El nom original del fitxer indica «DEROGADA PARCIALMENT».
- [Reglament de creació i regulació del Consell Consultiu dels jardins d'infants del Comú d'Encamp (2004)](docs/normativa-comu/reglaments-comu/enc-reg-20040708-creacio-regulacio-consell-consultiu-jardins-infant.md) — _dubtosa_: La durada del Consell era «fins el 31 d'agost del 2005, sense perjudici de la seva reelecció».
- [Reglament de funcionament del consell dels infants-unicef (no publicat)](docs/normativa-comu/reglaments-comu/enc-reg-sd-funcionament-consell-infants-unicef-no-publicat.md) — _no_publicat_: El nom original del fitxer indica «no publicat».

## Normes citades que no són al repositori

Si les teniu, pugeu-les: completarien les cadenes de modificacions.

- Llei 12/2004, del 30 de juny, de propietat horitzontal
- Directrius d'ordenació del territori (text base)
- Reglament de permisos administratius, del 6-11-2014 (derogat), i la seva modificació del 31-7-2014/2015
- Decret del 22-12-2022 que regula la moratòria d'autoritzacions de construccions de parcs solars (no és al repo)
- Decret d'estructura organitzativa anterior (substituït pel de 2024)
- Ordinació de Cabanes de 2015 (és dins el BOPA conjunt del 18.11.2015)
- Ordinació de la Mútua dels empleats del Comú d'Encamp (text base)
- Ordinació del 29-7-2025 de la funció pública del Comú d'Encamp (text base)
- Decret d'estructura organitzativa anterior al 2023
- Ordinació tributària per a l'any 2022

## Actes: sessions que falten i versions

- 2024: sessions [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13] → **falten**: [12]
- 2025: sessions [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (sense forats)
- 2026: sessions [1, 2, 3, 4, 5, 6, 7, 8, 9] (sense forats)

- Hi ha actes en versió *projecte* (no signada) a: 2024-07, 2024-09, 2024-10, 2025-01, 2025-02, 2025-03, 2025-04, 2025-05, 2025-12, 2026-03.

## Qualitat del text

- **Pàgines que només són imatges** (no convertides, només al PDF):
  - [Manual de bones pràctiques en edificació](docs/funcionament/enc-manual-sd-manual-bones-practiques-edificacio.md): pàgines [1, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
  - [Manual de noves funcionalitats de l'aplicació GI (versions 4.9 a 4.9.9)](docs/funcionament/enc-manual-sd-manual-noves-funcionalitats-aplicacio-gi-versions.md): pàgines [53, 54, 81]
  - [Conveni internacional de Viena, del 8 de novembre de 1968, sobre la senyalització viària](docs/legislacio/convenis-internacionals/int-conveni-19681108-conveni-internacional-viena-senyalitzacio-via.md): pàgines [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
  - [Reglament de les guarderies infantils (2005)](docs/legislacio/reglaments-govern/and-reglament-20050427-guarderies-infantils.md): pàgines [10]
  - [Especificacions tècniques de cartografia cadastral de la parròquia d'Encamp (2004)](docs/normativa-comu/ordinacions/enc-ord-20040407-especificacions-tecniques-cartografia-cadastral-20.md): pàgines [4, 5, 6, 9, 10, 11, 12]
  - [Ordinació de senyalització d'itineraris d'iniciativa privada (2011)](docs/normativa-comu/ordinacions/enc-ord-20111124-senyalitzacio-itineraris-iniciativa-privada.md): pàgines [6, 7, 10, 16]
  - [Ordinació de modificació de l'Ordinació sobre la instal·lació de terrasses (2019)](docs/normativa-comu/ordinacions/enc-ord-20190402-instal-lacio-terrasses.md): pàgines [8, 9]
  - [Reglament del sistema d'avaluació de l'acompliment (2004)](docs/normativa-comu/reglaments-comu/enc-reg-20040729-sistema-avaluacio-acompliment.md): pàgines [3]
  - [Protocol contra l'assetjament sexual del Comú d'Encamp (versió 21-05-2026)](docs/politiques-internes/recursos-humans-i-etica/enc-protocol-20260521-protocol-contra-assetjament-sexual-versio.md): pàgines [1, 39, 40, 51]
  - [NOR01_Creació del Comitè i rols de Seguretat de la Informació](docs/politiques-internes/seguretat-informacio/enc-pol-sd-nor01-creacio-comite-rols-seguretat-informacio.md): pàgines [1]
  - [POL01_Política de Seguretat de la Informació](docs/politiques-internes/seguretat-informacio/enc-pol-sd-pol01-politica-seguretat-informacio.md): pàgines [1]
  - [POL02_Contrasenyes i autenticació](docs/politiques-internes/seguretat-informacio/enc-pol-sd-pol02-contrasenyes-autenticacio.md): pàgines [1]
  - [PROC01_NOR04_Codi de bones pràctiques d'ús dels recursos TIC](docs/politiques-internes/seguretat-informacio/enc-pol-sd-proc01-nor04-codi-bones-practiques-us-recursos.md): pàgines [1]
  - [PROC02_NOR04_Classificació i tractament de la informació](docs/politiques-internes/seguretat-informacio/enc-pol-sd-proc02-nor04-classificacio-tractament-informacio.md): pàgines [1]
  - [Llei 4/2022, del 31 de gener, del pressupost per a l'exercici del 2022](arxiu/legislacio/lleis/and-llei-2022-004-pressupost-exercici-2022.md): pàgines [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]
  - [Protocol de mesures preventives i d'abordatge de les conductes d'assetjament sexual, per raó de sexe i altres ](arxiu/politiques-internes/recursos-humans-i-etica/enc-protocol-sd-protocol-mesures-preventives-abordatge-conductes-a.md): pàgines [1, 34, 35, 46]
- **Textos refosos sense caràcter oficial**: 20 documents (la majoria baixats de la web del Consell General o de LesLleis.com). El text oficial és el del BOPA; el camp `tipus_text: refos-no-oficial` ho indica.

## Documents a revisar

- [Decret del 13-2-2023 de modificació del Decret d'estructura organitzativa del Comú d'Encamp](arxiu/normativa-comu/decrets-comu/enc-decret-20230213-estructura-organitzativa.md)
  - Verifiqueu que el decret del 18-1-2024 el deroga expressament.
- [Reglament de la biblioteca comunal d'Encamp (2003)](arxiu/normativa-comu/reglaments-comu/enc-reg-20030912-biblioteca-comunal.md)
  - Data d'entrada en vigor detectada (2003-09-08) anterior a l'aprovació (2003-09-12); s'ha descartat. Reviseu-la.
- [Acta del Consell de Comú, sessió ordinària 7/24 (30-5-2024)](docs/actes-consell/2024/enc-acta-20240530-cc-07-24.md)
  - El nom del fitxer diu «7-27» però és la sessió 7/24 del 30-5-2024 (error al nom).
- [Projecte d’acta del Consell de Comú, sessió ordinària 11/25 (18-12-2025)](docs/actes-consell/2025/enc-acta-20251218-cc-11-25.md)
  - El nom diu «signada» però el text es titula «PROJECTE ACTA»: comproveu si és la versió signada.
- [Acta del Consell de Comú, sessió ordinària 5/26 (23-4-2026)](docs/actes-consell/2026/enc-acta-20260423-cc-05-26.md)
  - No porta «signada» al nom: comproveu si és la versió aprovada.
- [Llei 18/2026, del 15 de juliol, qualificada del Codi penal](docs/legislacio/lleis/and-llei-2026-018-qualificada-codi-penal.md)
  - Consulteu la data de publicació al BOPA per fixar les dates d'entrada en vigor (4 mesos / 6 mesos / 1 any).
- [Decret que regula els fitxers de dades personals del Comú d'Encamp (2013)](docs/normativa-comu/decrets-comu/enc-decret-20130218-regula-fitxers-dades-personals.md)
  - Possible superació per la Llei 29/2021 i el seu reglament; confirmeu-ne la vigència.
- [Decret del 5-11-2015 d'aprovació de cinc ordinacions comunals (Medi Ambient i Via Pública, aigua potable, caba](docs/normativa-comu/decrets-comu/enc-decret-20151105-cinc-ordinacions-comunals-medi-ambient-via-publica.md)
  - BOPA conjunt amb 5 ordinacions: només 2 (Medi Ambient i Via Pública, aigua potable) existeixen també soltes. Es proposa crear-ne 3 documents més (cabanes, terrasses, rètols).
- [Decret del 21-12-2023 de modificació del Decret del 22 de desembre del 2022 que regula la moratòria d'autoritz](docs/normativa-comu/decrets-comu/enc-decret-20231221-2022-regula-moratoria-autoritzacions-construccions.md)
  - Moratòria ampliada per 12 mesos; no hi ha cap ampliació posterior ni normativa nova al repo. Confirmeu si continua vigent.
- [Especificacions tècniques de cartografia cadastral de la parròquia d'Encamp (2004)](docs/normativa-comu/ordinacions/enc-ord-20040407-especificacions-tecniques-cartografia-cadastral-20.md)
  - Retallat el final de l'Ordinació del cadastre (norma anterior, fragment).
- [Ordinació general de regulació del cadastre comunal (2004)](docs/normativa-comu/ordinacions/enc-ord-20040407-general-regulacio-cadastre-comunal.md)
  - Retallat el principi de les Especificacions de cartografia (norma següent, fragment).
- [Ordinació de modificació de l'Ordinació de Medi Ambient i Via Pública (2017)](docs/normativa-comu/ordinacions/enc-ord-20171215-medi-ambient-via-publica.md)
  - Quins articles estan derogats? Cal indicar-ho.
- [Ordinació del 18-2-2026 de mesures urgents de caràcter tributari i econòmic per pal·liar els efectes del trame](docs/normativa-comu/ordinacions/enc-ord-20260218-mesures-urgents-caracter-tributari-economic-pal-li.md)
  - Vigència condicionada al tancament de l'RN20: confirmeu quan es reobre per fixar la data de fi.
- [Reglament de l'Arxiu del Comú d'Encamp (2003)](docs/normativa-comu/reglaments-comu/enc-reg-20030917-arxiu.md)
  - Data d'entrada en vigor detectada (2003-09-08) anterior a l'aprovació (2003-09-17); s'ha descartat. Reviseu-la.
- [Reglament de creació i regulació del Consell Consultiu dels jardins d'infants del Comú d'Encamp (2004)](docs/normativa-comu/reglaments-comu/enc-reg-20040708-creacio-regulacio-consell-consultiu-jardins-infant.md)
  - Mandat del Consell fins al 31-8-2005 (reelegible); no consta que continuï.
- [Reglament de subvencions per a l'embelliment de façanes (2006)](docs/normativa-comu/reglaments-comu/enc-reg-20060609-subvencions-embelliment-facanes.md)
  - Retallat el principi del Reglament de subvenció agrícola (altra norma, fragment tallat a l'art. 8).

## On ha anat cada fitxer?

[`PLA.csv`](PLA.csv) té, per a cada fitxer original de `inbox/`, l'acció, el nou `id` i la nova ruta.

## Com demanar canvis

Digueu-me què voleu canviar (carpetes, noms, estats, duplicats que no ho són…). Es modifica el pla (`PLA.json`) i es torna a aplicar sobre l'`inbox/` original, o es mouen fitxers amb `git mv` sense canviar-ne l'`id`.
