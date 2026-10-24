---
id: "doc-03-como-se-mueve-un-precio"
tipo: "seccion"
title: "Cómo se mueve un precio ✅"
aliases: ["doc-03-como-se-mueve-un-precio"]
documento: "[[03 Comercio y mercado]]"
limpieza: 100
abiertos: 0
espera: 2
aplazado_a: ["[[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y]]"]
estado: "con-aplazados"
anterior: "[[03 §Principios]]"
siguiente: "[[03 §Oferta y demanda]]"
arriba: "[[03 Comercio y mercado]]"
fuente: "studio/docs/03-comercio.md:11"
generado: true
---

# Cómo se mueve un precio ✅

> Estado: el mercado se mueve 3 veces por día, y el modelo (valor justo, oferta y demanda, ruido y momentum) y la ficha de mercado están…

← [[03 §Principios]] · [[03 Comercio y mercado|↑ 03]] · [[03 §Oferta y demanda]] →

**Estado:** el mercado se mueve 3 veces por día, y el modelo (valor justo, oferta y demanda, ruido y momentum) y la ficha de mercado están confirmados (alcance de [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]], 2026-10-15), y las cifras base de los 10 minerales y de los frenos están acordadas como base de partida ✅ ([[28 Números base de la economía|28]]); las fórmulas ⏳ [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]].

Cada mineral tiene un **valor justo**, que se ajusta cada día según oferta, demanda y eventos. El precio real lo persigue **con retraso**, con **ruido** y **momentum**. Resumen: *el precio tiende hacia el valor justo, pero tarda, se pasa y se agita*. Genera tendencias y rebotes que se pueden aprender a leer sin ser predecibles. Las fórmulas concretas ⏳ [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]].

✅ El mercado se mueve **3 veces por día**, una por bloque (mañana, tarde, noche). Esperar al bloque siguiente para vender es una decisión real, y el botón «Esperar» salta un bloque ([[01 Core loop y ciclo del día|01]]).

### Ficha de mercado por mineral ✅

| Parámetro | Qué controla |
|---|---|
| Precio base | Nivel de referencia |
| Volatilidad | Cuánto se agita |
| Liquidez | Cuánto cae el precio al vender mucho |
| Estacionalidad | Si sube o baja por épocas |
| Sensibilidad a eventos | Qué tipo de noticias lo mueven |
| Costo de guardar | Cuánto cuesta tenerlo en el almacén (la mercancía **no se deteriora** ✅) |

✅ **Precios base** (esquirlas por unidad, siempre enteros; el total de cada operación se redondea una sola vez): carbón 50 · hierro 90 · cobre 170 · salitre 150 · plata 200 · cuarzo 300 · oro 420 · esmeralda 800 · diamante 1 800 · Aetherita 6 000. La volatilidad, la liquidez y el costo de guardar de cada mineral están en [[28 Números base de la economía|28]]; el **costo de guardar** va de 0,03 % (Aetherita y diamante) a 0,15 % (carbón y hierro) del precio base por unidad y día, con un mínimo de 1 esquirla por lote.

✅ **Cómo se escriben los cambios de precio** (regla única, decisión del autor, 2026-10-15): un **«punto»** a secas es el **1 % del precio base** del mineral (no del precio del momento, para que los puntos se sumen): «carbón +3 puntos» son +3 % de 50 esquirlas, o sea +1,5. En la **deuda** se escribe **«pp»** (punto porcentual de interés: «−1 pp» es pasar del 4 % al 3 % mensual). En la **vigilancia** se escribe «vigilancia +10», nunca «+10 puntos». El «%» queda para ritmos y proporciones («sube un 20 % más despacio»).

### Personalidad de cada mineral ✅

Niveles de volatilidad, tope de variación diaria y qué mueve a cada mineral, a partir de [[05 Mundo y minerales|05]]. El orden de la volatilidad es hierro < carbón ≈ oro < cobre ≈ plata ≈ cuarzo < salitre < esmeralda ≈ diamante < Aetherita ([[28 Números base de la economía|28]]).

| Mineral | Volatilidad | Tope diario ✅ | Qué lo mueve más |
|---|---|---|---|
| Carbón | Baja–media | 6 % | Estación (invierno), huelgas |
| Hierro | Baja | 5 % | Contratos de guerra, ferrocarriles |
| Cobre | Media | 8 % | Obras eléctricas, escasez (apagones) |
| Salitre | Media–alta | 10 % | Cosechas, puertos, Faroleros |
| Plata | Media | 8 % | Industria, joyería |
| Oro | Baja–media | 6 % | Política, reservas del Estado |
| Cuarzo | Media | 8 % | Demanda tecnológica |
| Esmeralda | Alta | 12 % | Modas de la élite |
| Diamante | Alta | 12 % | Lujo, industria de corte |
| Aetherita | Muy alta | 15 % | Descubrimientos, secreto de Estado |

Tipos generales: estable, volátil, estacional, estratégico, lujo (ver [[05 Mundo y minerales|05]]).

## Fuente

`studio/docs/03-comercio.md:11`
