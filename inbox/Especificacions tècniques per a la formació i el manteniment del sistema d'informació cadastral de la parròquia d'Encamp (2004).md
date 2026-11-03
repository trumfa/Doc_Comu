> Butlletí Oficial del Principat d’Andorra · Núm. 22 - any 16 - 14.4.2004

Especificacions tècniques per a la formació i el manteniment del sistema d’informació cadastral de la parròquia d’Encamp

Vist l’article 80.h de la Constitució Andorrana del 13 de març de 1993, vist l’article 4.3 de la Llei Qualificada de Delimitació de Competències dels Comuns del 4 de novembre de 1993 i vista l’Ordinació General de Regulació del Cadastre Comunal del 7 d’abril del 2004, el Comú d’Encamp, en la Sessió Ordinària del Consell de Comú celebrada el dia 7 d’abril del 2004, ha aprovat les presents Especificacions Tècniques per la formació i el manteniment del Sistema d’Informació Cadastral de la Parròquia d’Encamp:

## Índex

## Capítol I. Disposicions generals

## Capítol II. Determinació de la referència cadastral

## Capítol III. Estructura de les bases de dades

## Secció 1. Sistema d’informació cadastral (SIC)

## Secció 2. Bases de dades gràfiques

## Annex 1. Bases de dades gràfiques

## Secció 3. Bases de dades alfanumèriques

## Annex 2. Descripció de l’estructura BdD.

## Annex 3. Bases de dades auxiliars (BDAX)

## Annex 4. Relació entre les BdD.

## Disposició final

## Capítol I. Disposicions generals

Especificació 1. L’objecte del present document és establir les bases per la creació del Sistema d’Informació Cadastral (SIC).

Especificació 2. Les bases de dades i aplicacions que permetin la seva creació i posterior manteniment hauran de tenir present totes les especificacions tècniques per la formació i manteniment del Cadastre del Comú d’Encamp.

Especificació 3. Qualsevol canvi referent a aquest document, sempre que suposi una millora degudament justificada, necessitarà rebre autorització expressa del Registre del Cadastre del Comú d’Encamp.

Especificació 4. Els noms i acrònims assignats a la base de dades i variables, hauran de ser, dins del possible, respectats. Un cop s’hagin dissenyat en la seva totalitat, el Registre del Cadastre del Comú aprovarà definitivament la descripció detallada de tota l’estructura d’aquestes bases i variables que composen el SIC.

Especificació 5. Tota la informació continguda en el Cadastre s’estructura en bases de dades gràfiques i alfanumèriques (subdividides en bàsiques i auxiliars) interrelacionades entre elles.

Especificació 6. El SIC s’estructura de manera que es puguin establir permisos, de consulta i edició de les diferents informacions contingudes, als usuaris. Per aquests usuaris s’establirà un sistema jeràrquic de la forma següent:

Administradors: Accés total. Usuaris: Permisos consulta i/o edició.

Especificació 7. Tota la nomenclatura referent a la denominació de vies públiques, denominació per plantes, destins, etc., serà la que s’utilitzarà. En el cas d’haver de recórrer a una nova nomenclatura no definida, se sol·licitarà al Registre del Cadastre del Comú d’Encamp.

Especificació 8. Per tal d’evitar repeticions en l’enregistrament de les dades, totes aquelles que es puguin calcular a partir de les bases de dades gràfiques, com per exemple la referència cadastral, superfícies, etc., i hagin de figurar en les bases de dades alfanumèriques, s’obtindran partint de les primeres, i no es podran editar per part dels usuaris, amb permisos d’edició, des de la base de dades alfanumèrica.

Especificació 9. El Sistema d’Informació Cadastral es dissenyarà de manera que permeti el manteniment d’un fitxer històric del Cadastre, és a dir, de tots aquells moviments que es produeixen, de forma que es pugi reproduir l’estat de les dades, tant gràfiques com alfanumèriques, en una data determinada.

Especificació 10. El Sistema d’Informació Cadastral disposarà d’un sistema de protecció de dades, de manera que sense la preceptiva autorització no es podran extreure dades de totes o d’alguna de les bases de dades que configuren el sistema, fent servir sistemes “d’encriptació” de dades o les tècniques que es considerin més convenients, posant especial cura en les mesures de seguretat en quant a les dades considerades de caràcter personal.

Especificació 11. Es disposarà d’una eina que permeti el coneixement, per part de l’administrador del sistema, de totes les consultes realitzades sobre les bases de dades gràfiques i alfanumèriques per part dels usuaris.

Especificació 12. Es dissenyarà un sistema d’importació i exportació de dades, tant de les bases de dades gràfiques com alfanumèriques, a fi i efecte de poder afegir dades de procedència externa, o bé facilitar-les a altres administracions o particulars que així ho sol·licitin. Aquests sistemes d’importació/exportació permetran l’elecció de dades a exportar o importar.

Especificació 13. Com a norma general:

En dades numèriques: La informació es justificarà a la dreta. Les posicions o camps sense informació s’ompliran amb zeros.

En dades alfanumèriques: La informació es justificarà a l’esquerra. Les posicions o camps sense informació s’ompliran amb blancs. La informació alfanumèrica es complementarà amb majúscules.

Especificació 14. Es podrà utilitzar software comercial com a suport pel desenvolupament de les diferents aplicacions que composin el SIC, prèvia autorització expressa del Registre del Cadastre del Comú d’Encamp. En tot cas sempre haurà de ser compatible amb el software present actualment en la xarxa informàtica del Comú.

Especificació 15. La interfície del SIC disposarà:

D’un entorn de treball amb diferents finestres de forma que sigui possible la visualització de les dades gràfiques i alfanumèriques a l’hora. De menús d’ajuda.

D’una eina que permeti la visualització de les fotografies de l’immoble. D’un menú per a la visualització i impressió de la distribució dels locals en cada una de les plantes. També contindrà formats d’impressió predefinits per les certificacions cadastrals de la unitat cadastral considerada.

Especificació 16. Les característiques del sistema gràfic seran:

Disposarà d’un menú d’eines de dibuix que facilitaran de forma senzilla la manipulació i edició dels objectes gràfics. Recerca i localització de parcel·les mitjançant les següents variables:

Referència cadastral. Codi via pública, nom via pública, número atribuït pel Comú. Número d’identificació del titular, cognoms i nom. Número seqüencial.

Disposarà d’una funció que permeti la visualització, o no, de diferents capes d’informació.

Especificació 17. Les característiques del sistema alfanumèric seran:

Per l’enregistrament de dades, en aquells casos que el valor ja estigui contingut en les taules auxiliars, es disposarà de menús desplegables que facilitin la dada a consignar. La validació dels valors introduïts en els diferents camps de la interfície pels operadors es farà en temps real.

Especificació 18. El SIC estarà dotat d’un servidor de dades i mapes que permetrà la distribució de la informació, tant per la xarxa interna com en la seva sortida a Internet, amb els corresponents dispositius de seguretat i mecanismes necessaris per a suportar els continguts que tingui a bé situar-hi la Web del Registre del Cadastre i altres departaments del Comú.

Especificació 19. Per garantir el correcte servei de manteniment s’integrarà un aplicatiu de gestió que, tot incorporant els diferents procediments de tràmits que es dissenyaran conjuntament amb el Servei de Qualitat, faciliti el seu control, seguiment d’expedients, estadístiques i temàtics, tot preveient una eventual certificació ISO.

Especificació 20. El programari que s’integri en l’aplicació del SIC estarà dotat d’interfícies amigables i de senzilla utilització per part dels usuaris i serà fàcilment accessible pel Servei d’Informàtica del Comú.

## Capítol II. Determinació de la referència cadastral

Tal i com apareix en el gràfic 1, els límits aproximatius de la Parròquia d’Encamp resten compresos, en la Projecció Lambert, enmig de 534.800 i 555.800 segons la coordenada (X) i entre 21.000 i 33.000 en la coordenada (Y).

Gràfic 1. Límits aproximats de la Parròquia d’Encamp.

Per la determinació de la referència cadastral s’ha optat per considerar el centroide de la parcel·la com el seu identificador, més un número seqüencial que representi, dins de la pròpia parcel·la, la distribució de la propietat.

Per poder definir de forma inequívoca la coordenada (X) del centroide de la parcel·la, amb precisió de metre, són necessaris 5 dígits, sense que es produeixin duplicitats. Ara bé, per definir la coordenada (Y) del centroide de la parcel·la en les mateixes condicions, només són necessaris 4 dígits.

De tota manera, per coherència amb la proposta d’assignació de referència cadastral de l’Ordinació General de Regulació del Cadastre Comunal i a fi que el número de dígits que defineixen les coordenades dels centroides de les parcel·les siguin els mateixos, es prendran tant per la coordenada (X) com per la (Y) cinc dígits.

El número seqüencial vindrà a ser com la “matrícula” de la parcel·la o de qualsevol entitat, en el cas de propietats en règim de divisions per quotes o parcel·lacions cúbiques. El número seqüencial serà constant mentre no esdevingui una alteració d’ordre físic o de titularitat i portarà associades les dates d’alta i baixa, per tal de conservar un arxiu històric dels moviments que s’hagin produït en cada propietat.

Amb aquest sistema de referenciació cadastral es pretén que els accessos es puguin efectuar emprant dos mètodes diferents, bé pels 10 dígits que identifiquen les coordenades (X-Y) dels centroides (consultes principalment sobre les bases de dades gràfiques), o bé pel número seqüencial (consultes sobre les bases de dades alfanumèriques).

Especificació 21. La referència cadastral estarà formada per cinc blocs d’informació, amb un total de 18 dígits.

Codi de parròquia o sector (A). Coordenada X del centroide de la parcel·la (BCDEF). Coordenada Y del centroide de la parcel·la (GHIJK). Número seqüencial que serà únic per cada parcel·la o entitat (LMNOPQ). Dígit de control calculat sobre el número seqüencial (R).

El primer bloc estarà constituït per 1 dígit que identificarà la Parròquia d’Encamp o un sector o zona del mateix.

El segon bloc, format per 5 dígits, correspondrà a la coordenada X del centroide de la parcel·la.

El tercer bloc, format per 5 dígits, correspondrà a la coordenada Y del centroide de la parcel·la.

El quart bloc, format per 6 dígits, serà un número seqüencial que identificarà a la parcel·la o, en el cas de comunitats per quotes, la distribució de la propietat dins de la parcel·la.

El cinquè bloc, format per 1 dígit, serà de control, calculat a partir de les xifres contingudes en el quart bloc, és a dir, del número seqüencial.

Especificació 22. El centroide de la parcel·la serà calculat automàticament quan es generi el recinte en la parcel·la. La referència cadastral variarà quan es produeixi una alteració dels límits del recinte parcel·la als següents casos:

Agrupació de parcel·les. Segregació de parcel·les. Cessió de part de parcel·la per vialitat.

En el cas de modificació dels contorns del recinte produïda per reclamació del titular cadastral, excepcionalment la referència cadastral (coordenades X-Y del centroide de la parcel·la) no variarà sempre que el centroide segueixi estant situat encara dins del contorn del recinte.

Núm. 22 - any 16 - 14.4.2004 Butlletí Oficial del Principat d’Andorra 1011

A B C D E F G H I J K L M N O P Q R

Especificació 23. El dígit de control es calcularà de la següent forma:

1) Se sumaran els dígits que ocupen una posició parell i el resultat es multiplicarà per 3.

2) Se sumaran els dígits que ocupen posició senar.

3) Se sumarà el resultat de 1) i 2).

4) El número de control serà el mínim número que s’hagi de sumar al resultat de 3) per què sigui múltiple de 10.

Exemple d’assignació de referència cadastral (18 dígits)

Codi: Codi de Parròquia, sector o zona. Centroide X: Coordenada X del centroide de la parcel·la. Centroide Y: Coordenada Y del centroide de la parcel·la. Numero seqüencial: Número seqüencial que serà únic per cada parcel·la o entitat dins d’una mateixa parcel·la. Control: Dígit de control calculat sobre el número seqüencial.

1012 Butlletí Oficial del Principat d’Andorra Núm. 22 - any 16 - 14.4.2004

1 4 2 4 4 6 2 5 4 2 6 0 0 0 6 2 5 5

Codi Centroide (X) Centroide (Y) Número seqüencial Control

## Capítol III. Estructura de les bases de dades

En aquest capítol es pretén descriure de forma bàsica les diferents taules que han de conformar el Sistema d’Informació Cadastral del Comú d’Encamp, tot tenint en compte que l’empresa adjudicatària del desenvolupament del “Soft” completarà, amb aquelles taules i variables que consideri necessàries, l’estructura mínima aquí establerta.

## Secció 1. Sistema d’informació cadastral (SIC)

Especificació 24. El Sistema d’Informació Cadastral (SIC) s’estructurarà en bases de dades gràfiques i alfanumèriques i aquestes, al seu torn, en bàsiques i auxiliars.

Especificació 25. Les bases de dades gràfiques i alfanumèriques estaran relacionades.

## Secció 2. Bases de dades gràfiques

Especificació 26. Les bases de dades gràfiques del Cadastre recolliran tota la informació relativa a les característiques físiques de les parcel·les i de tots els elements constructius.

Especificació 27. Tota la informació gràfica que representi illes, parcel·les o construccions, s’estructurarà en recintes o regions.

Especificació 28. Qualsevol recinte vindrà determinat per una línia poligonal tancada en la que els punts d’inflexió seran els nodes, que hauran de coincidir en totes les capes gràfiques d’informació.

Especificació 29. L’esquema de la informació cadastral gràfica seguirà la següent estructura:

Illa: És el recinte bàsic a partir del qual es generen, subdividint aquest recinte, recintes parcel·les.

Parcel·la: No pot existir parcel·la sense illa definida, i els seus límits no poden quedar fora del contorn del recinte illa. A partir de la subdivisió d’aquest recinte es generen recintes construcció.

Construcció: No pot existir recinte construcció sense l’existència prèvia de recinte illa i recinte parcel·la, i els contorns d’aquests recintes no poden quedar fora del recinte parcel·la excepte en els següents casos: Balcons o terrasses sobre via pública. Elements constructius maclats (locals que s’introdueixen en parcel·les contigües).

El sistema d’informació de la construcció es dividirà en:

Informació general de la construcció existent sobre una parcel·la (planta general de l’edificació en la que únicament s’associen atributs de volumetria).

Informació particularitzada de la propietat i usos existents dins de l’edifici. Aquesta informació es recollirà per plantes. Es crearan tants recintes constructius com locals d’ús privatiu existents i dins d’ells per cada ús diferent que hi hagi, que en el cas de recintes d’ús comunitari també es diferenciaran.

Especificació 30. Per determinar la referència cadastral, un cop s’hagi subdividit el recinte illa, es calcularà el centroide de cadascun dels recintes que constitueixen les parcel·les. Qualsevol recinte que es dibuixi sobre el recinte parcel·la heretarà els atributs de la referència de la parcel·la.

Especificació 31. En el cas de balcons que quedin situats fora del recinte parcel·la, per projectar-se sobre la via pública, heretaran els mateixos atributs de la parcel·la.

Especificació 32. En el sistema gràfic s’hauran de reflectir per cada planta tots els recintes independents i dintre d’ells es diferenciaran els usos distints als que es destina l’edificació.

## Annex 1 Bases de dades gràfiques

El sistema gràfic del Cadastre s’estructurarà en les següents bases de dades gràfiques:

BDGR_ILLA

Aquesta capa d’informació està formada pels recintes que composen totes les illes de la Parròquia d’Encamp, entenent per “illa” el recinte de sol d’ús privatiu delimitat per vies públiques (carrers o camins).

Els valors de les variables ILCENX, ILCENY i ILAREA, hauran de ser calculats automàticament i no podran ser manipulats en les bases de dades alfanumèriques.

Tots els recintes estaran associats a una base de dades alfanumèrica amb la següent estructura:

ILCENX numèric (5): Coordenada X del centroide del recinte.

ILCENY numèric (5): Coordenada Y del centroide del recinte.

ILAREA numèric (10): Superfície del recinte, en m

.

BDGR_PARC

Aquesta capa estarà formada pels recintes que composen totes les parcel·les, entenent la parcel·la com la unitat de terreny que disposa de característiques físiques de superfície i que queda perfectament delimitada perimetralment en tot el seu contorn.

Els valors de les variables PACENX, PA- CENY i PAAREA, seran calculats automàticament i no podran ser manipulats en les bases de dades alfanumèriques.

Tots els recintes hauran d’estar associats a una base de dades alfanumèrica amb la següent estructura:

PACENX numèric (5): Coordenada X del centroide del recinte.

PACENY numèric (5): Coordenada Y del centroide del recinte.

PAAREA numèric (10): Superfície del recinte, en m

.

Informació general de la construcció

BDGR_CONS

Aquesta capa estarà formada pels recintes o regions que defineixen les diferents alçades dels elements constructius d’un immoble. El recinte construcció es defineix com qualsevol superfície interior a la parcel·la, tal com pati (interior o exterior), volum edificat (sobre o sota rasant), solar, cobert, etc. i, encara que no hi hagi subdivisió en una parcel·la, es considerarà un sol recinte que ocupa en superfície la totalitat de la parcel·la. Tots els recintes estaran associats a una base de dades alfanumèrica amb la següent estructura:

COCENX numèric (6): Coordenada X del centroide del recinte.

COCENY numèric (6): Coordenada Y del centroide del recinte.

COAREA numèric (10): Superfície del recinte, en m

.

COATRI caràcter (20): Denominació de la volumetria.

Denominació de la volumetria que representa el recinte segons la següent codificació:

Taula de codificació de volums:

1, 2, 3,...Volums sota rasant (1, 2 alçades) I, II, III,...: Volums sobre rasant (1, 2 alçades) BAL: Balcó (Terrassa coberta) TRI: Tribuna (balcó cobert i tancat en el seu perímetre) TER: Terrassa POR: Porxo SOP: Soportal MAR: Marquesina COB: Cobert ALT: Altell PIS: Piscina TEN: Pista de tennis EST: Estany SOL: Solar PRG: Pèrgola DIP: Dipòsit ESC: Escala TRF: Transformador JAR: Jardí FUT: Camp de futbol ZES: Zona esportiva ARC: Arcades

Qualsevol altra nomenclatura no recollida en la relació anterior haurà de ser autoritzada pel Registre del Cadastre.

1) Tots els caràcters que formen la nomenclatura es complimentaran en majúscules.

2) Les altures d’edificació de volums sobre rasant es definiran amb números romans, mentre que els volums d’edificació sota rasant es definiran con números aràbics.

3) En volums en els que només hi hagi altures sobre rasant es definirà el número de plantes amb nomenclatura romana.

Exemple: I, II, III,...., VIII, IX,....

4) En volums en els que només hi ha altures sota rasant es definirà el número amb nomenclatura aràbiga.

Exemple: 1, 2, 3,...

5) Quan coexisteixin dins d’un volum alçades sobre i sota rasant es definirà el número de plantes sota rasant. A continuació un signe (+) seguit pel número de plantes sobre rasant.

Exemple: 1+I, 2+II, 3+V,...

6) Quan algun volum/buit tingui un número determinat de terrasses o balcons o tribunes, aquestes es definiran anteposant a la nomenclatura el número d’unitats en xifres romanes.

Exemple: IIITER (3 terrasses) IVB (4 balcons)

7) Si s’hagués de definir una terrassa o balcó en una planta determinada, s’anteposarà la nomenclatura a la planta.

Exemple: TERIII (terrassa en la planta

3) BALIV (balcó en la planta 4)

8) Però si la terrassa sols fos de remat d’un volum d’un número determinat d’altures, es concretarà el seu número posant a continuació la nomenclatura de TER i un signe (+) entre ambdues.

Exemple: III+TER (3 alçades més terrassa)

Informació particularitzada de la propietat i usos

Per cada planta de l’edifici es dibuixaran la distribució de la propietat i els usos.

S’hauran de tenir en compte les següents capes d’informació:

BDGR_PS-3: Planta soterrani -3 BDGR_PS-2: Planta soterrani -2 BDGR_PS-1: Planta soterrani -1 BDGR_PLBA: Planta baixa BDGR_PLEN: Planta entresòl BDGR_PL01: Planta primera BDGR_PL02: Planta segona BDGR_PL03: Planta tercera ....... BDGR_PL11: Planta onzena BDGR_PLAT: Planta àtic BDGR_PLCO: Planta coberta

L’estructura d’aquestes bases de dades serà:

COCENX numèric (6): Coordenada X del centroide del recinte.

COCENY numèric (6): Coordenada Y del centroide del recinte.

COAREA numèric (10): Superfície del recinte, en m

.

CODEST caràcter (3): Destí al que es dedica el recinte.

Es consideren els següents destins:

REC: Residencial col·lectiu REU: Residencial unifamiliar COM: Comercial amb activitat CSA: Comercial sense activitat OFI: Oficines APA: Aparcament MAG: Magatzems HOT: Hoteler REL: Religiós ENS: Ensenyament ALT: Altres usos no tipificats

NUMLOC caràcter (4): Número de propietari.

Identificarà el número del local dins de l’immoble, i s’emprarà per enllaçar el local amb el seu titular. Haurà d’ésser assignat automàticament i no es permetrà la seva edició. En el cas de ser un element comú s’identificarà com “ELCO”.

REFPAR caràcter (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral ( X del centroide + Y del centroide).

Exemple:

El primer pas serà la creació del recinte illa on ens apareixeran els nodes (punts d’inflexió de la línia poligonal tancada que delimita el recinte illa), segons s’estableix en el gràfic 2.

Gràfic 2. Delimitació del recinte illa

Al procedir a la subdivisió del recinte illa per la creació dels recintes parcel·les apareixeran nous nodes que s’hauran de reflectir en el recinte illa (gràfic 3).

Gràfic 3. Nous nodes que apareixen sobre el recinte illa

En el següent pas es procedeix a la creació dels recintes construcció, per dibuixar la planta general de l’immoble. Això provocarà l’aparició de nous nodes sobre la línia perimetral del recinte illa i sobre la línia perimetral del recinte parcel·la.

Gràfic 4. Nous nodes sobre el recinte illa i parcel·la

A mesura que anem dibuixant els recintes construcció de cada una de les plantes de l’immoble, la resta dels recintes aniran heretant aquests nodes, així s’aconseguirà la coherència gràfica entre tots els recintes.

Al final el recinte illa o qualsevol altre haurà d’haver heretat els nodes situats en línies perimetrals dels recintes coincidents (Gràfic 4)

Gràfic 5. Resultat final del recinte illa un cop ha heretat diferents nodes d’altres recintes.

Gràfic 6. Resultat final del recinte parcel·la un cop ha heretat diferents nodes d’altres recintes.

## Secció 3. Bases de dades alfanumèriques

Les bases de dades alfanumèriques estaran compostes com a mínim per les següents taules:

Bases de dades bàsiques (BDBA_): BDBA_VIA: Contindrà totes les vies públiques que existeixin en el territori. BDBA_PARCEL·LA: Contindrà totes les dades generals de les parcel·les. BDBA_URBANISME: Contindrà dades relatives a les qualificacions, usos, edificabilitats permeses pel planejament urbanístic. BDBA_CONSTRUCCIO: Contindrà dades relatives a les construccions existents sobre la parcel·la. Existirà un registre com a mínim per a cada una de les plantes i, dins de cada planta, per a cada local d’ús independent o per a cada destí diferent. BDBA_UNITAT: Contindrà la informació necessària per associar els recintes constructius al titular corresponent. BDBA_TITULAR: Contindrà les dades relatives a la titularitat.

Bases de dades auxiliars (BDAX_): BDAX_TIPVIA: Descripció tipus de via. BDAX_XARCLA: Descripció xarxa de clavegueram. BDAX_XARAIG: Descripció xarxa d’aigua. BDAX_PAVVIA: Descripció pavimentació de la via pública. BDAX_XARELE: Descripció xarxa de subministrament elèctric. BDAX_NPLANT: Descripció plantes d’un edifici. BDAX_NPORTA: Descripció portes. BDAX_DESLOC: Descripció destins.

## Annex 2 Descripció de l’estructura de cada una de les taules que contindran les bases de dades alfanumèriques

BDBA_VIA

Base de Dades que contindrà totes les vies públiques existents en el territori.

CODVIA numèric (5): Codi de la via.

TIPVIA text (4): Tipus de via.

Els diferents tipus de vies que s’admetran seran els que es relacionen tot seguit:

PG: Passeig CR: Carrer CM: Camí PL: Plaça PTGE: Passatge CTRA: Carretera AV: Avinguda CRO: Carreró TOR: Torrent RDA: Ronda BDA: Baixada RBLA: Rambla TRV: Travessera PARC: Parc ESC: Escala MERC: Mercat MOLL: Moll VIA: Via TRVS: Travessia JRDI: Jardí

NOMVIA text (25): Nom de la via pública.

Nom de la via pública segons denominació oficial del Comú d’Encamp.

BDBA_PARCELA

Base de dades que contindrà totes les dades generals de les parcel·les.

DADES DE SITUACIÓ: Dades de localització de la parcel·la.

En el cas de parcel·les amb més d’un accés a via pública, existirà un registre de dades de situació per cadascun dels accessos. Això facilitarà la localització de la parcel·la, en el cas de recerca per nom de via pública i nom.

PARCEL1 numèric (3): Número d’ordre del registre.

REFPAR text (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral (X+ Y del centroide).

CODVIA numèric (5): Codi de la via pública.

NUMPO1 numèric (3): Número atribuït pel Comú.

NUMDP1 text (1): Duplicat del número atribuït pel Comú.

DENBLO caràcter (10): Denominació del bloc.

DENLLO caràcter (25): Denominació del lloc.

LONGF1 decimal (10,2): Longitud de la façana.

Aquesta longitud de façana serà la descrita en la variable CODVIA.

DADES FÍSIQUES: Dades físiques de la parcel·la.

En el cas de parcel·les amb més d’un accés a via pública, les dades físiques únicament hauran d’indicar-se en el primer registre de la parcel·la, deixant a zero la resta de registres referents a dades físiques.

SUPPAR numèric (10): Superfície de la parcel·la.

S’expressarà en m

. La superfície de la parcel·la serà una dada que es calcularà a partir del sistema gràfic i no es podrà actualitzar des de les bases de dades alfanumèriques.

SUPCON numèric (10): Superfície construïda.

S’expressarà en m

. Per tal de determinar la superfície construïda total d’un edifici, es tindrà en compte tota aquella superfície que disposi de forjat i tingui una alçada lliure superior a 1,5 metres. En el cas que es tracti de terrasses la superfície es computarà al 100%.

La superfície total construïda de la parcel·la serà una dada que es calcularà a partir del sistema gràfic, no podent-se actualitzar des de les bases de dades alfanumèriques.

SUPOCU numèric (10): Superfície ocupada per l’edificació.

S’expressarà en m

 i es correspondrà amb la projecció de l’edifici sobre el terreny. En el cas d’existència de terrasses, tribunes i altres elements volants sobre vies públiques, aquests també s’inclouran encara que la superfície ocupada sigui superior a la de la parcel·la.

La superfície ocupada per la construcció serà una dada que s’haurà de calcular a partir del sistema gràfic i tampoc es podrà actualitzar des de les bases de dades alfanumèriques.

Serà necessari que correspongui amb la suma de la de tots els recintes, inclosos en la planta general de la parcel·la i que es considerin construïts.

SUPSRA numèric (10): Superfície construïda sobre rasant.

S’expressarà en m

, i es correspondrà amb la superfície construïda de la planta que es consideri com planta baixa, més la superfície construïda de totes les plantes que estiguin per sobre d’ella.

SUPSOR numèric (10): Superfície construïda sota rasant.

S’expressarà en m

, i serà la suma de la superfície construïda de totes aquelles plantes que estiguin per sota de la planta considerada com planta baixa.

LONGF2 decimal (10,2): Longitud de la façana.

Si es tracta de parcel·les amb front a diferents vies públiques, la longitud serà la suma de totes elles. S’expressarà en metres amb dos decimals i coincidirà amb la suma de les diferents longituds de façana contingudes en els registres de situació.

XARCLA caràcter (1): Xarxa de clavegueram.

Existència de xarxa de clavegueram.

S SI N NO

XARAIG caràcter (1): Xarxa d’aigua.

Existència xarxa d’aigua.

S SI N NO

PAVVIA caràcter (1): Pavimentació de la via pública.

Existència pavimentació de la via pública.

S SI N NO

XARELE caràcter (1): Xarxa de transport d’energia elèctrica.

Existència xarxa subministrament elèctric.

S SI N NO

BDBA_URBANISME

BDBA que contindrà dades relatives a les qualificacions, usos i edificabilitats permeses pel planejament urbanístic.

L’estructura d’aquesta base de dades haurà de ser realitzada per l’empresa adjudicatària del “soft” en funció de les característiques del planejament vigent.

Existirà un registre per cadascuna de les diferents qualificacions, usos o edificabilitats que es trobin en la parcel·la.

URBAN1 numèric (3): Número de la subparcel·la.

REFPAR text (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral (X - Y del centroide).

CALIFI caràcter (25): Qualificació urbanística.

SOSTRE numèric (10): Sostre edificable sobre la subparcel·la.

BDBA_CONSTRUCCIO

BDBA que contindrà dades relatives a les construccions existents sobre la parcel·la. Existirà un registre com a mínim per cadascuna de les plantes i dins de cada planta per cada local d’ús independent o per cada destí diferent.

CONST1 numèric (3): Número seqüencial.

REFPAR text (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral (X -Y del centroide).

NUMLOC caràcter (4): Número d’identificació.

Identificarà el número del local dins de l’immoble, i servirà per enllaçar el local amb el seu titular. Serà assignat automàticament i no es permetrà la seva edició. En el cas de ser un element comú s’identificarà com “ELCO”.

NPLANT caràcter (2): Planta.

Planta en la que es troba situat el local considerat. Els diferents tipus de codis de planta que s’admetran seran:

S9: Soterrani 9 S8: Soterrani 8 ....................... ....................... S1: Soterrani 1 SS: Planta semisoterrani PB: Planta baixa EN: Planta entresòl AL: Planta altell 01: Planta primera 02: Planta segona ........................ ........................ 10: Planta desena AT: Planta àtic SA: Planta sobre àtic ......................... SC: Planta sota coberta PC: Planta coberta (S’utilitzarà pel cas de construccions en la planta coberta, torre de la caixa d’escala o ascensor, coberts d’instal·lacions, etc.)

NPORTA caràcter (3): Porta.

Porta que identifica el local en la planta en la que es troba. En el cas de places d’aparcament s’utilitzarà aquest camp per denominar el número de la plaça.

Adoptarà un dels següents valors:

001: Porta primera 002: Porta segona 003: Porta tercera 004: Porta quarta 005: Porta cinquena ................................... ................................... 010: Porta desena ................................... ESQ: Porta esquerra DRE: Porta dreta A__: Porta A B__: Porta B ................................... Z__: Porta Z

SUPLOC numèric (10): Superfície construïda del local.

S’expressarà en m

.

DESLOC caràcter (3): Destí del local.

Es consideren els següents destins:

REC: Residencial col·lectiu REU: Residencial unifamiliar COM: Comercial amb activitat CSA: Comercial sense activitat OFI: Oficines APA: Aparcament MAG: Magatzems HOT: Hoteler REL: Religiós ENS: Ensenyament ALT: Altres usos no tipificats

SUPTER numèric: Superfície construïda de les terrasses.

Superfície construïda de les terrasses, si existeixen, i que estiguin vinculades al local considerat (s’expressarà en m

). Es considerarà terrassa, tota superfície construïda que no disposi de tancament.

ANYCON numèric (4): Any de construcció.

ANYREF numèric (4): Any de reforma.

GRAURE numèric (3): Grau de reforma.

S’expressarà el percentatge de la reforma.

BDBA_UNITA

TBDBA que conté la informació necessària per associar els recintes constructius al titular corresponent.

REFCAT caràcter (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral ( X - Y del centroide)

NUMLOC caràcter (4): Número d’identificació.

Identificarà el número del local dins de l’immoble i es farà servir per enllaçar el local amb el seu titular.

COEFPR decimal (5,2): Coeficient de propietat.

En el cas de propietats dividides per quotes.

CODPAR caràcter (1): Referència cadastral.

Primer bloc de la referència cadastral.

NUMSEC caràcter (6): Referència cadastral.

Quart bloc de la referència cadastral.

DIGSEC numèric (1): Dígit de control al número seqüencial.

El dígit de control es calcularà de la següent manera:

1) Se sumaran els dígits que ocupen una posició parell i el resultat es multiplicarà per 3 (Exemple numsec= 000625; 0+6+5=11; 11x 3 = 33).

2) Se sumaran els dígits que ocupen posició senar (exemple 0+0+2 = 2).

3) Se sumarà el resultat de 1) i 2) (exemple 33 + 2 = 35).

4) El número de control serà el mínim número que s’hagi de sumar al resultat de 3) per què sigui múltiple de 10 (exemple dígit de control =5; 35+5=40 (múltiple de 10)).

BDTITULAR

BDBA que contindrà les dades relatives a la titularitat de la parcel·la o dels locals d’ús privatiu, en el cas de propietat per quotes.

REFCAT caràcter (10): Referència cadastral.

Segon més tercer bloc de la referència cadastral ( X - Y del centroide).

NUMSEC caràcter (6): Referència cadastral.

Quart bloc de la referència cadastral.

DIGSEC numèric (1): Dígit de control al número seqüencial.

Cinquè bloc de la Referència Cadastral.

El dígit de control es calcularà com s’ha indicat anteriorment.

TIPTIT caràcter (1): Tipus de relació amb la propietat.

S’utilitzarà la següent nomenclatura:

P: Propietari D: Titular d’un dret real sobre la propietat R: Representant

NUMIDE caràcter (12): Número d’identificació, passaport.

NOMTIT caràcter (30): Nom del titular cadastral.

Aquest camp només es podrà omplir amb lletres i números, no podent-se utilitzar cap accent, símbol o abreviatura.

CODVIA numèric (4): Codi de la via de notificació.

Únicament es farà servir si el domicili de notificació està situat a Encamp.

SIGNOT caràcter (4): Sigles de la via pública.

Sigles de la via pública del domicili de notificació.

VIANOT caràcter (25): Nom de la via pública.

Nom de la via pública de notificació.

NUMNOT numèric (5): Número atribuït pel Comú.

Número del domicili de notificació.

DUPNOT caràcter (1): Duplicat al número atribuït pel Comú.

Duplicat al número del domicili de notificació.

CIUNOT caràcter (25): Ciutat, poble, del domicili de notificació.

PAINOT caràcter (25): País del domicili de notificació.

LIBNOT caràcter (25): Text lliure.

Text lliure per definir amb precisió, si cal, el domicili de notificació.

## Annex 3 Bases de dades auxiliars (BDAX)

Les bases de dades auxiliars contindran tots aquells valors que han de prendre les variables que tinguin valors predeterminats. No es permetrà que aquestes variables, que s’utilitzen en les bases del SIC, adoptin valors diferents dels aquí definits.

Aquestes bases de dades podran ser alimentades per noves descripcions no contingudes en elles, sempre que s’hagi obtingut l’autorització del Registre del Cadastre del Comú.

BDAX_TIPVIA

Base de dades que contindrà els diferents tipus de via admesos en el SIC.

TIPVIA caràcter (4): Sigles via pública.

Sigles a utilitzar per la descripció del tipus de via pública:

PG: Passeig CR: Carrer CM: Camí PL: Plaça PTGE: Passatge CTRA: Carretera AV: Avinguda CRO: Carreró TOR: Torrent RDA: Ronda BDA: Baixada RBLA: Rambla TRV: Travessera PARC: Parc ESC: Escala MERC: Mercat MOLL: Moll VIA: Via TRVS: Travessia JRDI: Jardí

TIPDES caràcter (50): Descripció de la sigla.

Exemple:

PG Passeig CR Carrer CM Camí

BDAX_XARCLA

Base de dades que descriu el grau d’urbanització pel que respecta al clavegueram.

XARCLA caràcter (1): Xarxa de clavegueram.

S SI N NO

CLADE1 caràcter (2): Descripció reduïda de XARCLA.

CLADE2 caràcter (50): Descripció extensa de XARCLA.

Exemple:

S SI Existeix xarxa de clavegueram N NO No existeix xarxa de clavegueram

BDAX_XARAIG

Base de dades que descriu el grau d’urbanització pel que respecta a l’existència de xarxa d’aigua.

XARAIG caràcter (1): Xarxa d’aigua.

S SI N NO

CLAAI1caràcter (2): Descripció reduïda de XARAIG.

CLAAI2 caràcter (50): Descripció extensa de XARAIG.

Exemple:

S SI Existeix xarxa d’aigua N NO No existeix xarxa d’aigua

BDAX_PAVVIA

Base de dades que descriu el grau d’urbanització pel que respecta a la pavimentació de la via pública.

PAVVIA caràcter (1): Pavimentació de la via pública.

S SI N NO

CLAVI1 caràcter (2): Descripció reduïda de PAVVIA

CLAVI2 caràcter (50): Descripció extensa de PAVVIA

Exemple:

S SI Existeix pavimentació N NO No existeix pavimentació

BDAX_XARELE

Base de dades que descriu el grau d’urbanització pel que respecta a l’existència de xarxa de subministrament elèctric.

XARELE caràcter (1): Xarxa de subministrament elèctric.

S SI N NO

CLAEL1 caràcter (2): Descripció reduïda de XARELE

CLAEL2 caràcter (50): Descripció extensa de XARELE

Exemple:

S SI Existeix xarxa de subministrament elèctric N NO No existeix xarxa de subministrament elèctric

BDAX_NPLANT

Base de dades que descriu els diferents tipus de denominació de les plantes d’un edifici.

NPLANT caràcter (2): Plantes d’un edifici.

Es faran servir els següents valors:

S9: Soterrani 9

S8: Soterrani 8 ....................... ....................... S1: Soterrani 1 SS: Planta semisoterrani PB: Planta baixa EN: Planta entresòl AL: Planta altell 01: Planta primera 02: Planta segona ........................ ........................ 10: Planta desena A : Planta àtic SA: Planta sobre àtic ......................... SC: Planta sota coberta PC: Planta coberta (S’utilitzarà en el cas de construccions en la planta coberta, torre de la caixa d’escala o ascensor, habitacions d’instal·lacions, etc.)

DESNPL caràcter (25): Descripció de NPLANT

Exemple:

S1 Primera planta soterrani 02 Segona planta PC Planta coberta

BDAX_NPORTA

Base de dades que descriu la nomenclatura per les diferents denominacions de les portes d’un immoble.

NPORTA caràcter (C3): Portes d’un edifici.

001: Porta primera 002: Porta segona 003: Porta tercera 004: Porta quarta 005: Porta cinquena ................................... ................................... 010: Porta desena ................................... ESQ: Porta esquerra DRE: Porta dreta A__: Porta A B__: Porta B ................................... Z__: Porta Z

DESNPO caràcter (25): Descripció de NPORTA

Exemple:

001 Porta 1 DRE Porta dreta A__ Porta A

BDAX_DESLOC

Base de dades que descriu el destí del local considerat.

DESLOC caràcter (3): Destí del local.

Es consideren els següents destins:

REC: Residencial col·lectiu REU: Residencial unifamiliar COM: Comercial amb activitat CSA: Comercial sense activitat OFI: Oficines APA: Aparcament MAG: Magatzems HOT: Hoteler REL: Religiós ENS: Ensenyament ALT: Altres usos no tipificats

DESLO 1 caràcter (25):Descripció reduïda de DESLOC.

DESLO 2 caràcter (50): Descripció extensa de DESLOC.

## Annex 4. Relació entre les bases de dades alfanumèriques

## Disposició final

Les presents Especificacions Tècniques entraran en vigor als quinze dies de la seva publicació en el Butlletí Oficial del Principat d’Andorra.

Cosa que es fa pública per a coneixement general.

Encamp, 7 d’abril del 2004

Cònsol major Miquel Alís Font

1020 Butlletí Oficial del Principat d’Andorra Núm. 22 - any 16 - 14.4.2004

Valors admesos BDBA_VIA BDBA_PARCEL.LA BDBA_URBANISME BDBA_CONSTRUCCIÓ BDBA_UNITAT BDBA_TITULAR CODVIA (N5) X X X BDAX_TIPVIA TIPVIA (C4) X NOMVIA (C25) X PARCEL1 (N3) X REFPAR (C10) X X X X X NUMPO1 (N3) X NUMDP1 (C1) X DENBLO (10) X DENLLO (25) X LONGF1 (D4,2) X SUPPAR N(10) X SUPCON (N10) X SUPOCU (N10) X SUPSRA (N10) X SUPSOR (N10) X LONGF2 (D10,2) X BDAX_XARCLA XARCLA (C1) X BDAX_XARAIG XARAIG (C1) X BDAX_PAVVIA PAVVIA (C1) X BDAX_XARELE XARELE C1) X URBAN1 (N3) X CALIFI (C25) X SOSTRE (N10) X CONST1 (N3) X NUMLOC (C4) X X BDAX_NPLANT NPLANT (C2) X BDAX_NPORTA NPORTA (C3) X SUPLOC (N10) X BDAX_DESLOC DESLOC (C3) X ANYCON (N4) X ANYREF (N4) X GRAURE (N3) X COEFPR (D5,2) CODPAR (C1) X X NUMSEC (N6) X X DIGSEC (N1) X X TIPTIT (C1) X NUMIDE (C12) X NOMTIT (C30) X SIGNOT (C4) X VIANOT (C25) X NUMNOT (N5) X DUPNOT (C1) X COPNOT (C10) X CIUNOT (C25) X