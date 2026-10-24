---
id: "doc-03-oferta-y-demanda"
tipo: "seccion"
title: "Oferta y demanda ✅"
aliases: ["doc-03-oferta-y-demanda"]
documento: "[[03 Comercio y mercado]]"
limpieza: 100
abiertos: 0
espera: 2
aplazado_a: ["[[F4-31 Sectores de demanda - ferrocarril, energía, militar]]"]
estado: "con-aplazados"
anterior: "[[03 §Cómo se mueve un precio]]"
siguiente: "[[03 §Bots y mercado interno]]"
arriba: "[[03 Comercio y mercado]]"
fuente: "studio/docs/03-comercio.md:53"
generado: true
---

# Oferta y demanda ✅

> Estado: la oferta por mineros NPC y las huelgas (07) y la demanda por los seis sectores (alcance de F4-31) están confirmadas; qué sectores…

← [[03 §Cómo se mueve un precio]] · [[03 Comercio y mercado|↑ 03]] · [[03 §Bots y mercado interno]] →

**Estado:** la oferta por mineros NPC y las huelgas ([[07 Sociedad, poder y eventos|07]]) y la demanda por los seis sectores (alcance de [[F4-31 Sectores de demanda - ferrocarril, energía, militar|F4-31]]) están confirmadas; qué sectores alimenta cada mineral ⏳ [[F4-31 Sectores de demanda - ferrocarril, energía, militar|F4-31]]. El peso del jugador en el precio también está confirmado: crece con su volumen y patrimonio.

- **Oferta:** mineros NPC por región (una huelga la reduce), más lo que vende el jugador y sus empleados.
- **Demanda:** por **sectores** (ferrocarril, energía, militar, agricultura, lujo, tecnología). Cada mineral alimenta varios sectores, y un evento en un sector arrastra a sus minerales. Los pesos de partida de cada mineral en sus sectores están acordados ✅ ([[28 Números base de la economía|28]]: por ejemplo, el carbón es 55 % energía, el hierro 45 % ferrocarril y 35 % militar); ⏳ [[F4-31 Sectores de demanda - ferrocarril, energía, militar|F4-31]] construye el modelo y los eventos con esos pesos.
- ✅ El jugador es un actor pequeño al inicio y grande al final: su impacto en el precio **crece con su volumen y su patrimonio** (decisión del autor, 2026-10-15). El peso del jugador va de 0,5 en el Acto I a 0,6 en el II, 1,0 en el III y 1,6 en el IV (máximo 4; decisión del autor, 2026-10-16), y su impacto se disipa un 25 % por bloque ✅ ([[28 Números base de la economía|28]]). ✅ El simulador ([[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]], regla E3) comprobó que ese impacto **no crea bucles de ganancia**: vender y recomprar pierde ≈ 5,9 % y comprar, esperar hasta 8 bloques y vender también pierde, con cualquier peso del jugador.

## Fuente

`studio/docs/03-comercio.md:53`
