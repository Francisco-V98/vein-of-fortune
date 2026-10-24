---
id: "doc-03-mercado-negro-y-vigilancia"
tipo: "seccion"
title: "Mercado negro y vigilancia ✅"
aliases: ["doc-03-mercado-negro-y-vigilancia"]
documento: "[[03 Comercio y mercado]]"
limpieza: 100
abiertos: 0
espera: 15
aplazado_a: ["[[F4-67 Indicador de vigilancia y sus niveles]]", "[[F4-68 Inspecciones y multas]]", "[[F4-69 Redada - confiscación, cierre y arresto]]", "[[F4-70 Formas de bajar la vigilancia - soborno, reputación y]]", "[[F4-72 Mercado negro - operación nocturna con volumen limitado]]", "[[F4-77 Pantalla de facciones y vigilancia]]", "[[F5-07 Ajuste de multas y vigilancia]]"]
estado: "con-aplazados"
anterior: "[[03 §Contratos y pedidos]]"
siguiente: "[[03 §Refinado y valor agregado]]"
arriba: "[[03 Comercio y mercado]]"
fuente: "studio/docs/03-comercio.md:166"
generado: true
---

# Mercado negro y vigilancia ✅

> Estado: confirmado qué es, dónde y cuándo se opera, los cuatro niveles de vigilancia y la redada; las consecuencias de cada nivel F4-67 y…

← [[03 §Contratos y pedidos]] · [[03 Comercio y mercado|↑ 03]] · [[03 §Refinado y valor agregado]] →

**Estado:** confirmado qué es, dónde y cuándo se opera, los cuatro niveles de vigilancia y la redada; las consecuencias de cada nivel ⏳ [[F4-67 Indicador de vigilancia y sus niveles|F4-67]] y ⏳ [[F4-68 Inspecciones y multas|F4-68]]; las cifras base están acordadas ✅ ([[28 Números base de la economía|28]]).

✅ El mercado negro **paga más pero tiene riesgos**. La idea es que no se use siempre, porque repercute. Hay un **indicador de vigilancia** de las autoridades; si el jugador se pasa de listo, se pagan **multas**.

### Qué ofrece ✅

- ✅ Precios mejores que el spot, con una **prima sobre el valor justo** que varía por mineral: carbón y hierro 20 % · cobre 22 % · plata y cuarzo 25 % · oro y Aetherita 30 % · esmeralda 32 % · salitre y diamante 35 % ([[28 Números base de la economía|28]]). Como tampoco paga el 3 % de impuesto, la ganancia real frente al spot es la prima más ≈ 4 %.
- ✅ Ventas **sin impuesto** ([[26 Zonas y edificios|26]], mostrador sin sello del bar: «sin impuesto y con prima de mercado negro, a cambio de vigilancia»).
- ✅ Ventas **sin licencia**.
- ✅ Acceso a bienes restringidos o en cuota (por ejemplo, grandes volúmenes de salitre).
- ✅ **Aetherita en el Acto III:** su precio ya se ve, pero solo se compra aquí, con Casilda, como mercancía escasa. La extracción no ocurre hasta el Acto IV.
- ✅ **Aetherita en el Acto IV (decisión del autor, 2026-10-15 y 2026-10-16):** la que extraes la vendes por un **canal legal con tope**: la **Comisión del Éter** la compra en una **oficina de Puerto Meridiano, siempre abierta**, hasta **5 viales al día**, a valor justo sin prima y con el impuesto de 3 % ([[28 Números base de la economía|28]]). En el mercado negro la Aetherita solo entra como **encargo especial**, con trasfondo e historia: raro (uno cada ≈ 21 días; si Casilda es la compradora elegida en el final, cada ≈ 14 días y con más historia, con la prima en +10 a +15 puntos), de pocos viales (1 o 2), a veces una compra sin mucho detalle, nunca un canal rutinario ni de grandes cantidades. La vigilancia no depende de la Aetherita: sus encargos especiales añaden menos de un tercio de lo que la vigilancia baja sola.
- ✅ **Cuándo y dónde:** se opera **de noche**, en el **Bar del Farol de Salinas Blancas** (viajando hasta allí) y también con la **visita nocturna de Casilda a la tienda**. Esa visita **no es el modo tienda**: la tienda no se abre de noche ([[01 Core loop y ciclo del día|01]]). El volumen es limitado por noche: **3 300 esquirlas de valor en el Acto II, 12 000 en el III y 55 000 en el IV**, ✅. La Aetherita ya no forma parte de las noches negras de rutina: en el Acto IV se vende por el **canal legal de la Comisión del Éter** y en el mercado negro solo aparece como **encargo especial** (ver más abajo). Cuánto cuesta en bloques una noche negra ⏳ [[F4-72 Mercado negro - operación nocturna con volumen limitado|F4-72]]: el simulador da el máximo que compensa, 0,97 bloques en el II, 0,95 en el III y 0,85 en el IV.
- ✅ **Acceso por contacto:** Casilda y Los Faroleros abren el mercado negro en el Acto II. Los Faroleros no tienen medidor propio: se miden por la alianza que elijas ([[07 Sociedad, poder y eventos|07]]).

### Indicador de vigilancia ✅

**Estado:** confirmado el indicador global, los cuatro niveles, la redada y que suspender la licencia no baja el estatus; las consecuencias de cada nivel y cómo se muestra ⏳ [[F4-67 Indicador de vigilancia y sus niveles|F4-67]], ⏳ [[F4-68 Inspecciones y multas|F4-68]] y ⏳ [[F4-77 Pantalla de facciones y vigilancia|F4-77]].

✅ Es **un solo indicador global**, de 0 a 100, que **sube** con cada operación negra (según volumen y valor) y **baja** con el tiempo. Los cambios se escriben «vigilancia +10» o «vigilancia −15» (nunca «puntos» a secas); el «%» solo sirve para el ritmo con que sube o baja por sí solo. Cada operación negra sube la vigilancia entre **+4 y +12**, según su valor frente al volumen máximo de la noche, y la vigilancia **baja sola 2 al día** (también los días con operación) ✅. La alianza con Los Faroleros hace que suba un 20 % más despacio. No hay un indicador por lugar.

✅ Tiene **cuatro niveles, sin solaparse** (decisión del autor, 2026-10-15). Se llaman «niveles», porque «tramo» es de los medidores de relación ([[24 Umbrales de acto|24]]):

| Nivel | Rango | Consecuencias |
|---|---|---|
| Tranquilo | 0–29 ✅ | Nada |
| Observado | 30–59 ✅ | Inspecciones ocasionales, multas leves |
| Vigilado | 60–84 ✅ | Inspecciones frecuentes, multas fuertes, contratos oficiales bloqueados |
| Bajo investigación | 85–100 ✅ | Redada (abajo) |

Cifras base de cada nivel ✅ ([[28 Números base de la economía|28]]):

- **Observado:** cada operación negra tiene un 20 % de inspección; la multa leve es el **1 % del patrimonio** (mínimo 60 esquirlas).
- **Vigilado:** 50 % de inspección; la multa fuerte es el **3 % del patrimonio** (mínimo 300) más el decomiso del 25 % del lote.
- **Bajo investigación:** redada (abajo).

⏳ [[F4-67 Indicador de vigilancia y sus niveles|F4-67]] El indicador y sus niveles, y ⏳ [[F4-68 Inspecciones y multas|F4-68]] las inspecciones y multas de cada uno.

✅ Llegar a «Bajo investigación» es la **redada**: no es una falla de la partida. Tras una redada la vigilancia **baja a 60** (el primer valor de Vigilado) y el **mercado negro cierra 7 días** ✅. Además hay confiscación del lote de esa noche y del stock negro, una **multa del 6 % del patrimonio** (mínimo 600) y la **tienda cerrada 2 días** ✅; la licencia en riesgo y el posible arresto (1 día perdido, con un 25 % de probabilidad en Difícil y Hardcore) ⏳ [[F4-69 Redada - confiscación, cierre y arresto|F4-69]].

✅ **Suspender la licencia no baja el estatus** ([[24 Umbrales de acto|24]]).

✅ Aplicación del pilar «la información es poder»: al principio solo ves el nivel de forma vaga, sin la cifra, y el valor exacto se descubre con fuentes (Quiroga, Lucía). ⏳ [[F4-67 Indicador de vigilancia y sus niveles|F4-67]] Cómo se muestra y se descubre; ⏳ [[F4-77 Pantalla de facciones y vigilancia|F4-77]] su pantalla.

### Cómo bajar la vigilancia ✅

- ✅ **Esperar:** baja sola con el tiempo.
- ✅ **Sobornar al Inspector Quiroga.** Cada soborno cuesta más que el anterior (**(500 + 0,8 % del patrimonio) × 1,35 por cada soborno ya hecho**) y baja la vigilancia **15**; el contador de sobornos baja 1 cada 56 días ✅. **No hay medidor de «corrupción»**: el costo creciente es el único freno ⏳ [[F4-70 Formas de bajar la vigilancia - soborno, reputación y|F4-70]].
- ⏳ [[F4-70 Formas de bajar la vigilancia - soborno, reputación y|F4-70]] Las demás formas: decisiones de la historia que la bajan (por ejemplo, conseguirle el retiro a Quiroga, [[23 Árbol de decisiones y consecuencias|23]]), pagar a Los Faroleros (que alivian inspecciones) y contratar guardias (cada guardia baja la vigilancia 0,25 más al día, hasta 3 guardias ✅).

### Multas ✅

✅ Las multas escalan con la dificultad: se multiplican por **0,7 en Novato, 1 en Intermedio, 1,4 en Difícil y 2 en Hardcore** ✅. Su valor y frecuencia son los de arriba ([[28 Números base de la economía|28]]); su construcción ⏳ [[F4-68 Inspecciones y multas|F4-68]] y su ajuste ⏳ [[F5-07 Ajuste de multas y vigilancia|F5-07]].

## Fuente

`studio/docs/03-comercio.md:166`
