---
id: "doc-25-s06"
tipo: "seccion"
title: "6 · Cobertura de combinaciones ✅"
aliases: ["doc-25-s06"]
documento: "[[25 Finales y epílogos]]"
limpieza: 100
abiertos: 0
espera: 4
aplazado_a: ["[[F1-23 Consola y atajos de depuración - saltar día, dar dinero]]", "[[F4-210 Motor de epílogos por piezas]]", "[[F4-61 Modelo de los cuatro medidores de relación]]"]
estado: "con-aplazados"
anterior: "[[25 §5 Las 54 piezas]]"
siguiente: "[[25 §7 Hilos abiertos y hilos que se cierran]]"
arriba: "[[25 Finales y epílogos]]"
fuente: "studio/docs/25-finales-y-epilogos.md:250"
generado: true
---

# 6 · Cobertura de combinaciones ✅

> Estado: que cada combinación del Acto IV debe tener pieza, que ninguna salida es la correcta y los casos ES-04 y QU-02 son decisión del…

← [[25 §5 Las 54 piezas]] · [[25 Finales y epílogos|↑ 25]] · [[25 §7 Hilos abiertos y hilos que se cierran]] →

**Estado:** que cada combinación del Acto IV debe tener pieza, que ninguna salida es la correcta y los casos ES-04 y QU-02 son decisión del autor (2026-10-12); las demás reglas de cruce y los caminos de prueba los confirmó el 2026-10-16 ([[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]).

### 6.1 · De los 81 caminos del II a las piezas

Los 81 caminos del Acto II (3 variantes × 3 respuestas a la orden × 3 bandos en la huelga × 3 alianzas, [[22 Acto II - las tres variantes de Reme|22]]) llegan al epílogo solo por tres vías: la **variante oculta** (3), la **alianza** (3) y los **medidores**. La orden de Reme, el bando de la huelga y el pago ya se absorbieron en los medidores; el epílogo no los lee. Quedan **9 pares** (variante, alianza). Multiplicados por las **5 salidas** (revelar, callar y vender a cada uno de los tres compradores) hacen **45 combinaciones** que la consola de depuración debe recorrer ⏳ [[F1-23 Consola y atajos de depuración - saltar día, dar dinero|F1-23]].

### 6.2 · Garantías

Los estados válidos de las variables de selección son una estimación del narrador, del orden de 459.000 (con el aval ligado a Esteban en tramo alto). La regla es que en todos ellos cada tema devuelve exactamente una pieza (Montenegro, dos si revelas), no se repite ninguna y las 54 son alcanzables. La enumeración exacta la comprueba el motor con banderas forzadas ⏳ [[F4-210 Motor de epílogos por piezas|F4-210]] y la recorre la consola ⏳ [[F1-23 Consola y atajos de depuración - saltar día, dar dinero|F1-23]].

**Estados que no existen**, para no escribir piezas de más:

- [[Bandera entrada|f-entrada]] = aval implica Esteban en tramo alto ([[24 Umbrales de acto|24]], sección 5).
- [[Bandera comprador|f-comprador]] solo existe si [[Bandera destino|f-destino]] = vender; en los demás casos es nulo.
- Teo «se va» exige revisión y tramo bajo; sin revisión, muere, sea cual sea el tramo.
- DU-01 exige comprador Ministerio; DU-04 exige revelar.

### 6.3 · Pares que podían contradecirse

| Par | Problema | Resolución |
|---|---|---|
| Esteban en tramo alto y comprador Consorcio | Rompió con su casa, y su casa paga el silencio del protagonista | ES-04 manda sobre ES-01 con una línea propia para el tramo alto ✅ |
| Comprador Ministerio y [[Bandera archivo\|f-archivo]] = proteger | [[23 Árbol de decisiones y consecuencias\|23]] decía que se queda «con tu archivo» | Se queda con **tu prueba** (los comprobantes y las cintas que usas), no con el archivo de Quiroga ✅; QU-01 sigue en pie. Corregido en 23 y en `decisions.json` |
| Quiroga: usar el archivo y [[Bandera quiroga salida\|f-quiroga-salida]] | «Cae, salvo que le cumpliste la salida» | QU-02 tiene dos líneas: sin retiro cae, con retiro se salva ✅ |
| [[Medidor Unión\|m-union]] fuera de «revelar» | Sin pieza si callas o vendes | UN-01 a UN-03 llevan una línea para cada caso |
| Lucía al callar o vender | Sin pieza | LU-04, con filtración si el tramo es bajo y silencio si es medio o alto |
| Teo muere y piezas de la Unión | La Unión «lo recuerda» | UN-0x no nombra a Teo; solo TE-03 lo hace |
| Reme protegida y misma facción aliada | La facción de Reme se enemista con tu alianza | FC-0x no promete buena relación sin matiz: usa «mantiene» y «se espera» |
| Montenegro amenaza y Reme protegida | «Pierde fuerza» | DU-03 no nombra a nadie |
| Revelas y Lucía publica | El Teletipo publica pero no puede confirmar | LU-01 sigue terminando en SIN CONFIRMAR |
| Anselmo | Una tarjeta podría delatarlo | Ninguna lo nombra vivo ni cita el acta (sección 2) |

### 6.4 · Ocho caminos de prueba

Cubren las 54 piezas y las dos líneas de las piezas que las tienen. Los tramos son alcanzables según [[24 Umbrales de acto|24]], sección 6; su alcance conjunto ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]].

| Camino | Salida | Unión / Esteban / Lucía / Teo | Alianza, entrada y archivo | Piezas |
|---|---|---|---|---|
| 1 | Revelar | alto / alto / alto / alto | Consorcio, aval, proteger; Reme proteger; monopolio rechazado; familia todo | H-01 RE-01 ES-01 CA-04 QU-01 LU-01 TE-01 DU-02 DU-04 UN-01 FC-01 FC-04 FC-06 MU-01 MU-02 ME-01 ME-04 FM-01 |
| 2 | Revelar | bajo / bajo / medio / bajo | Ministerio, sello, usar con retiro; Reme dejar; monopolio aceptado; familia nada | H-02 RE-03 ES-03 CA-03 QU-02 LU-03 TE-02 DU-03 DU-04 UN-03 FC-02 FC-03 FC-06 MU-01 MU-02 ME-01 ME-05 FM-03 |
| 3 | Revelar, sin revisión de Teo | medio / medio / bajo / medio | Faroleros, presión, usar sin retiro; Reme saldar; monopolio compartido; familia a medias | H-02 RE-02 ES-02 CA-02 QU-02 LU-02 TE-03 DU-03 DU-04 UN-02 FC-02 FC-04 FC-05 MU-01 MU-02 ME-01 ME-04 FM-02 |
| 4 | Callar | alto / medio / bajo / alto | Consorcio, sello, vender; Reme saldar; monopolio aceptado; familia todo | H-03 RE-02 ES-02 CA-03 QU-03 LU-04 TE-01 DU-02 UN-01 FC-01 FC-04 FC-06 MU-03 MU-04 ME-02 ME-04 FM-01 |
| 5 | Vender a Casilda | medio / alto / alto / medio | Faroleros, aval, proteger; Reme dejar; monopolio rechazado; familia a medias | H-04 RE-03 ES-01 CA-01 QU-01 LU-04 TE-01 DU-03 UN-02 FC-02 FC-04 FC-05 MU-05 MU-06 ME-03 ME-04 FM-02 |
| 6 | Vender al Consorcio | bajo / alto / medio / alto | Ministerio, aval, proteger; Reme proteger; monopolio compartido; familia nada | H-05 RE-01 ES-04 CA-03 QU-01 LU-04 TE-01 DU-03 UN-03 FC-02 FC-03 FC-06 MU-05 MU-06 ME-03 ME-04 FM-03 |
| 7 | Vender al Consorcio | bajo / medio / alto / alto | Faroleros, sello, vender; Reme dejar; monopolio rechazado; familia todo | H-05 RE-03 ES-04 CA-02 QU-03 LU-04 TE-01 DU-03 UN-03 FC-02 FC-04 FC-05 MU-05 MU-06 ME-03 ME-04 FM-01 |
| 8 | Vender al Ministerio | alto / medio / bajo / alto | Consorcio, presión, usar con retiro; Reme saldar; monopolio aceptado; familia a medias | H-06 RE-02 ES-02 CA-03 QU-02 LU-04 TE-01 DU-01 UN-01 FC-01 FC-04 FC-06 MU-05 MU-06 ME-03 ME-04 FM-02 |

---

## Fuente

`studio/docs/25-finales-y-epilogos.md:250`
