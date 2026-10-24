---
id: "sim-E6"
tipo: "regla-sim"
title: "Tope por comprador y capacidad del almacén"
aliases: ["sim-E6"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 1.0
unidad: ""
documentos: ["[[28 §3 Los diez minerales]]", "[[28 §6 Frenos de mercado]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:405"
generado: true
---

# Tope por comprador y capacidad del almacén

> E · Mercado y bucles · pasa · ±10 % del ritmo

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

cambio del ritmo al aplicar el tope por comprador y el almacén; el excedente se vende con descuento

## Umbral

±10 % del ritmo

## Resultado

Estado: **pasa**. el excedente sobre el tope se vende más barato (1 = sí): **1 ** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| cambio del ritmo con tope por comprador y almacén (Acto III) | 1.1062 % | [0.1403, 2.0721] | … a 10 | pasa |
| cambio del ritmo con tope por comprador y almacén (Acto IV) | 1.3359 % | [0, 2.7436] | … a 10 | pasa |
| el excedente sobre el tope se vende más barato (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |

## Criterio

- **cambio_max:** 10

## Requisitos que protege

- Tope por comprador y capacidad del almacén ([[28 §6 Frenos de mercado]])

## Mutaciones de prueba

- Tienda de 1 unidad y tope por comprador de 1
  - `economy.store_upgrades.0.units_per_block` = 1
  - `economy.store_upgrades.1.units_per_block` = 1
  - `economy.store_upgrades.2.units_per_block` = 1
  - `economy.store_upgrades.3.units_per_block` = 1
  - `economy.store_upgrades.4.units_per_block` = 1
  - `economy.market.store.units_per_block` = 1, 1, 1, 1, 1
  - `minerals.carbon.buyer_cap` = 1
  - `minerals.hierro.buyer_cap` = 1
  - `minerals.cobre.buyer_cap` = 1
  - `minerals.salitre.buyer_cap` = 1
  - `minerals.plata.buyer_cap` = 1
  - `minerals.cuarzo.buyer_cap` = 1
  - `minerals.oro.buyer_cap` = 1
  - `minerals.esmeralda.buyer_cap` = 1
  - `minerals.diamante.buyer_cap` = 1

## Relaciones

- **Documentos:** [[28 §3 Los diez minerales]], [[28 §6 Frenos de mercado]]
- **Bloques de economía:** [[Mercado]], [[Deriva guionizada del Acto I]], [[Mejoras de la tienda]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:405`
