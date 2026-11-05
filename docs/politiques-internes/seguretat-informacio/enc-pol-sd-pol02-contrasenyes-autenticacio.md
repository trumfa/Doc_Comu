---
id: "enc-pol-sd-pol02-contrasenyes-autenticacio"
titol: "POL02_Contrasenyes i autenticació"
tipus: "politica"
ambit: "comu"
organisme: "Comú d'Encamp"
tipus_text: "oficial"
estat: "vigent"
estat_font: "deduït"
temes: ["dades-i-seguretat-informacio"]
text_complet: true
pagines_sense_text: [1]
font_original: "originals/politiques-internes/seguretat-informacio/enc-pol-sd-pol02-contrasenyes-autenticacio.pdf"
---

# POL02_Contrasenyes i autenticació

> ⚠ Pàgines del PDF sense text extret (només imatges): 1. Consulta el PDF original.

Contrasenyes i autenticació

COMÚ D’ENCAMP

Document confidencial. Tots els drets reservats. Queda prohibida la reproducció, la comunicació o l'accés a tercers no autoritzats.

Control de versió

Control del document

|  | Nom | Classificació | Data |
| --- | --- | --- | --- |
| Fet per: | Var Group | Política | 20-06-2025 |
| Autoritzat per: | Departament de Sistemes d'Informació | Política | 01-08-2025 |
| Aprovat per: | Comitè de seguretat de la informació | Política | 23-09-2025 |
| Ratificat per: | Junta de Govern | Política | 15-10-2025 |

Registre de canvis

| Revisió | Versió | Descripció del canvi | Modificat per |
| --- | --- | --- | --- |
| Oct-2025 | 1.1. | S'hi afegeixen aportacions de protecció de dades personals per part del DPD | Delegat de protecció de dades |

Document confidencial. Tots els drets reservats. Queda prohibida la reproducció, la comunicació o l'accés a tercers no autoritzats.

## Índex

1

Introducció .............................................................................................. 3 2

Objectius ................................................................................................ 3 3

Abast ..................................................................................................... 3 4

Normativa de referència ............................................................................ 3 5

Contrasenyes i autenticació ....................................................................... 4 5.1

Política de contrasenyes .................................................................... 4 5.1.1

Longitud mínima ............................................................................ 4 5.1.2

Complexitat .................................................................................. 4 5.1.3

Prohibició de contrasenyes comunes i de reutilització .......................... 4 5.1.4

Caducitat de contrasenyes .............................................................. 4 5.1.5

Autenticació multifactor (MFA) ......................................................... 4 5.1.6

Gestors de contrasenyes ................................................................ 4

Document confidencial. Tots els drets reservats. Queda prohibida la reproducció, la comunicació o l'accés a tercers no autoritzats.

## 1 Introducció

La seguretat de la informació és un pilar fonamental per a la protecció dels actius digitals i la continuïtat operativa del Comú d’Encamp.

En aquest context, l’ús adequat de contrasenyes i mecanismes d’autenticació representa una de les primeres línies de defensa davant d’accessos no autoritzats, fuites d’informació i ciberatacs.

## 2 Objectius

Aquesta política pretén establir els criteris mínims i les bones pràctiques que cal observar en la creació, l'ús, l'emmagatzematge i la renovació de contrasenyes, així com en la implementació de mètodes d'autenticació segurs.

La seva aplicació busca garantir la integritat, la confidencialitat i la disponibilitat dels sistemes d'informació, alineant-se amb els estàndards internacionals de ciberseguretat i les disposicions legals vigents.

## 3 Abast

Aquest document és aplicable a tots els sistemes d’informació del Comú d’Encamp (també anomenat, “l’Entitat”), ha de ser comunicat a tot el personal de l'Entitat i ha d'estar permanentment a disposició dels empleats.

La infracció d’aquest document serà sancionada conforme al règim disciplinari de l’Entitat, sense perjudici de les responsabilitats administratives, civils o penals que d'aquest incompliment poguessin derivar-se.

Els usuaris d´aquest document són els membres del Comú d’Encamp, així com empleats i parts interessades (que, encara que no estiguin directament involucrats, han de respectar les indicacions assenyalades en el document).

## 4 Normativa de referència

Per confeccionar el document actual s’han pres com a base les referències següents:

•

UNE ISO/IEC 27001 (Sistemes de Gestió de la Seguretat de la Informació (SGSI). •

UNE ISO/IEC 27002 (Codi de bones pràctiques per a la Gestió de la Seguretat de la Informació). •

Llei 22/2022, del 9 de juny, de mesures per a la seguretat de les xarxes i dels sistemes d’informació (en endavant NIS-AD). •

Llei 29/2021, del 28 d’octubre, qualificada de protecció de dades personals (LQPD). •

Resolucions, guies, recomanacions i instruccions de l’APDA (Agència Andorrana de Protecció de Dades). •

Decret 346/2021, del 20 d’octubre del 2021, de creació de l’Agència Nacional de Ciberseguretat. •

Decret 417/2022, del 12-10-2022, pel qual s’aprova el Reglament de l’Esquema nacional de seguretat del Principat d’Andorra (en endavant ENS-AD).

Document confidencial. Tots els drets reservats. Queda prohibida la reproducció, la comunicació o l'accés a tercers no autoritzats.

•

Decret 418/2022, del 12-10-2022, pel qual s’aprova el Reglament d’infraestructures crítiques del Principat d’Andorra (en endavant RIC-AD). •

Altres normatives d’àmbit europeu (INCIBE, CCN CERT, NIST Cybersecurity Framework).

## 5 Contrasenyes i autenticació

### 5.1 Política de contrasenyes

#### 5.1.1 Longitud mínima

Les contrasenyes han de tenir almenys 8 caràcters (es recomana una longitud de 12 caràcters o més per a més seguretat).

#### 5.1.2 Complexitat

No es requereix obligatòriament l'ús de majúscules, números o símbols si es fa servir una contrasenya llarga i difícil d'endevinar. No obstant això, es recomana que les contrasenyes:

•

Evitin paraules comunes o patrons predictibles.

•

No contingueu el nom d'usuari ni parts del nom complet de l'usuari.

•

Sigueu úniques per a cada servei.

#### 5.1.3 Prohibició de contrasenyes comunes i de reutilització

El sistema ha de bloquejar l'ús de contrasenyes que formen part d'una llista de contrasenyes compromeses o utilitzades comunament, i no s'han de reutilitzar cap de les darreres 5 contrasenyes utilitzades al compte.

Addicionalment, es recomana implementar un verificador de contrasenyes compromeses (com per exemple, el servei de Microsoft “banned password list”).

#### 5.1.4 Caducitat de contrasenyes

Per a tots els usuaris d’alt risc (administradors de sistemes i comptes privilegiats), les contrasenyes tindran una durada mínima de 30 dies i màxima de 90 dies.

No es recomana el canvi periòdic de contrasenyes de la resta dels usuaris sense motiu (com una bretxa de seguretat), ja que fomenta contrasenyes febles o predictibles. En lloc d'això, es recomana:

•

Implementar autenticació multifactor (MFA).

•

Forçar el canvi només en cas d’activitat sospitosa o filtració.

#### 5.1.5 Autenticació multifactor (MFA)

S'ha d'exigir l’ autenticació multifactor per accedir a informació sensible o serveis crítics.

Per a més informació sobre els mecanismes d’autenticació, veure el Procediment de gestió d’usuaris.

Per a tots els usuaris d’alt risc (administradors de sistemes i comptes privilegiats), les contrasenyes tindran una durada mínima de 30 dies i màxima de 90 dies.

Document confidencial. Tots els drets reservats. Queda prohibida la reproducció, la comunicació o l'accés a tercers no autoritzats.

#### 5.1.6 Gestors de contrasenyes

El Comú d’Encamp utilitza un gestor de contrasenyes segur (gestor de contrasenyes corporatiu) per generar i emmagatzemar contrasenyes úniques i robustes. Quedant prohibida la utilització de gestors personals o no autoritzats pel l’Àrea de Transformació Digital.
