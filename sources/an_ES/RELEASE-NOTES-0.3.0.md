# Corrector ortografico aragonés 0.3.0

Versión 0.3.0 · 13 d'octubre de 2026.

## Presentación

Esta versión actualiza lo corrector aragonés Hunspell a la ortografía de l'Academia Aragonesa de la Lengua (AAL). Recupera lo desembolique encetau en 2011 y enampla la cobertura de vocabulario y formas gramaticals, incluyindo variants expresament revisadas. Esta versión reúne l'adaptación ortografica y las milloras revisadas en 2026.

La versión 0.3.0 contiene 21.060 dentradas de diccionario, a partir d'as cualas las reglas d'afixación cheneran formas adicionals. Ye escrita en UTF-8.

## Principals novedaz

- Adaptación d'as grafías antiguas: finals en -tz y derivaus revisaus; qua/qüe/qüi/quo pasan a cua/cue/cui/cuo, con as excepciones lexicas d'a Ortografía de l'Aragonés.
- Revisión de l'accentuación verbal y nominal: charrábaz, comésez, vivíbanos; plurales como chóvens y exámens; árbol/árbols y otras palabras planas agora accentuadas. Los derivaus se tractan seguntes los casos revisaus.
- Corrección d'a conchugación de verbos en -cuar y ampliación u revisión de paradigmas regulars y irregulars, incluyius dar, estar, decir, fer, venir, tener, salir y poder.
- Incorporación de variants aprebadas: cherundios en -nd chunto a -ndo, primeras personas d'o plural orientals y pasaus breus como cantón, bebión y salión, amás de variants lexicas, pronombres, articlos y nombres propios.
- Admisión de s'i y d'as combinacions con 'n dimpués de me, te, se, no, lo, le, li, la, bi y i. Se conserva lo refuso que'n.
- Prioridat a las sucherencias que corrichen tildes, tz → z/c y finals verbals con toz dos cambios; metesetz proposa metésez dinantes que alternativas menos probables.
- Equivalencia d'o apóstrofo dreito (') y tipografico (’), sin redefinir per completo las reglas lingüisticas d'apostrofación.
- Eliminación de 518 linias lexicas exactament duplicadas, cuatro copias de reglas d'afixación y una copia de REP z Z. Corrección de flags y de dentradas mal representadas; incorporación de REP k K.

## Validación feita

- 46 prebas de regresión y 6 prebas d'o chenerador morfolochico superadas.
- Comparanzas nativas d'acceptación y sucherencias pa las limpiezas tecnicas.
- Cobertura inicial d'o corpus: **80,36 %**; cobertura final: **88,66 %**, una millora de **8,30 puntos percentuals**.
- **Cobertura final de Common Voice: 88,66 % d'as ocurrencias avaluadas**, con 76.941 reconoixidas d'un total de 86.783. Quedan 9.842 ocurrencias sin reconoixer (11,34 %). Lo percentache conta las repeticions y usa la segmentación de l'executable Hunspell 1.7.2 (`-G` y `-l`); excluye numeros y signos que ixes modos no reportan como parolas. Las formas con apostrofo pueden segmentarse.
- Analís de 10.460 linias d'o corpus de Common Voice. Las ocurrencias de parolas no reconoixidas pasan de 17.048 en a primera execución a 9.842: reducción neta de 7.206, aproximadament lo 42,3 %.

Estes recuentos describen la cobertura d'o corrector en ixe corpus; las parolas no reconoixidas no son necesariament errors ortograficas. Tampoco no miden per ellas solas l'acceptación indebida de formas incorrectas.

## Alcanz y limitacions

Lo corrector compreba parolas; no fa una revisión gramatical d'as frases ni garantiza l'adecuación contextual d'as variants. La cobertura sigue estando incompleta. L'apostrofación y cualques derivacions heredadas requieren treballo posterior. Las variants incorporadas corresponden a las decisions presas entre esta revisión; no constituyen una cobertura completa de tota la morfolochía dialectal.

Lo diccionario y las zagueras milloras d'apostrofación y sucherencias s'han prebau satisfactoriament en LibreOffice, Firefox y Thunderbird. S'incluye lo paquet `corrector-ortografico-aragones.0.3.0.oxt`.

## Creditos

Santiago Paricio: autor orichinal (versión 0.1).
Juan Pablo Martínez: colaborador dende la versión 0.2 y responsable de la revisión lingüistica, adaptación AAL y ampliacions d'esta 0.3.0.

Copyright (C) 2011 Santiago Paricio.
Copyright (C) 2011–2026 Juan Pablo Martínez.

## Licencia

Lo diccionario (`.dic`) y lo fichero d'afixos (`.aff`) d'a versión 0.3.0 se distribuyen baixo una **trilicencia alternativa**: lo destinatario puet triar **MPL 1.1, GPL 3.0 u posterior, u LGPL 3.0 u posterior**. No ye menister cumplir las tres de vez.

Identificador SPDX: `MPL-1.1 OR GPL-3.0-or-later OR LGPL-3.0-or-later`.

Se conservan los creditos y copyrights de Santiago Paricio y Juan Pablo Martínez. Los textos completos d'as tres licencias s'incluyen en `licenses/`.
