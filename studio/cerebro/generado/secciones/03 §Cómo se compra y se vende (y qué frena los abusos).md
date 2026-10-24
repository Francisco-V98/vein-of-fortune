---
id: "doc-03-como-se-compra-y-se-vende-y-que-frena-lo"
tipo: "seccion"
title: "Cómo se compra y se vende (y qué frena los abusos) ✅"
aliases: ["doc-03-como-se-compra-y-se-vende-y-que-frena-lo"]
documento: "[[03 Comercio y mercado]]"
limpieza: 100
abiertos: 0
espera: 1
aplazado_a: ["[[F2-07 Spread, slippage y límite de variación diaria]]"]
estado: "con-aplazados"
anterior: "[[03 §Información por capas]]"
siguiente: "[[03 §Canales de venta y compra]]"
arriba: "[[03 Comercio y mercado]]"
fuente: "studio/docs/03-comercio.md:111"
generado: true
---

# Cómo se compra y se vende (y qué frena los abusos) ✅

> Estado: la lista de frenos y el tope diario más amplio de la Aetherita están confirmados (F2-07 los construye); las cifras base están…

← [[03 §Información por capas]] · [[03 Comercio y mercado|↑ 03]] · [[03 §Canales de venta y compra]] →

**Estado:** la lista de frenos y el tope diario más amplio de la Aetherita están confirmados ([[F2-07 Spread, slippage y límite de variación diaria|F2-07]] los construye); las cifras base están acordadas ✅ ([[28 Números base de la economía|28]]).

El mayor riesgo del mercado simulado es que el jugador encuentre un truco para hacerse rico sin esfuerzo. Frenos:

| Freno | Efecto |
|---|---|
| **Spread** | Comprar cuesta más de lo que se vende; evita arbitraje infinito |
| **Slippage** | Vender mucho de golpe baja el precio; hay que vender en tandas |
| **Costo de almacén** | Guardar cuesta, así que especular tiene riesgo real |
| **Impuestos y licencias** | Un porcentaje se va al Ministerio |
| **Límite de variación diaria** | El precio no se mueve más de **5–15 % por día** según el mineral (hierro 5 %, carbón y oro 6 %, esmeralda y diamante 12 %). En la Aetherita el tope es **más amplio** (15 %) ✅, porque es el mineral más volátil |
| **Tope diario por comprador** | Cada comprador NPC absorbe solo cierto volumen |

Cifras base ✅ ([[28 Números base de la economía|28]]):

- **Spread:** 2 a 8 % de ida y vuelta según el mineral (carbón, hierro, cobre y oro 2 %; salitre, plata y cuarzo 3 %; esmeralda y diamante 5 %; Aetherita 8 %). Se compra a valor justo × (1 + s/2) y se vende a × (1 − s/2).
- **Impuesto de ventas:** **3 %** en el mercado spot, la tienda y los pedidos y contratos; **0 %** en el mercado negro. La Bolsa de Puerto Meridiano (Acto III) cobra la mitad de spread y ningún impuesto de venta.
- **Slippage:** el precio cae según las unidades que vendes frente a la liquidez del mineral (de 10 unidades por −1 % en el carbón a 0,8 en la Aetherita) y a los compradores del mundo (2, 3, 5 y 8 por acto). Se recupera un 25 % por bloque.
- **Tope diario por comprador:** unas 3 veces la liquidez por día y por comprador (de 30 unidades de carbón a 2 de Aetherita).
- **Marketplace:** comprar lo que falta cuesta el valor justo × 1,18.
- **Almacén:** capacidad y renta, en «Almacén» más abajo.
- **Licencias** (renovación cada 28 días): Minero con licencia 150 · Comerciante 900 · Empresario 4 500 · Magnate 17 000 esquirlas (decisión del autor, 2026-10-16).

⏳ [[F2-07 Spread, slippage y límite de variación diaria|F2-07]] Su construcción.

## Fuente

`studio/docs/03-comercio.md:111`
