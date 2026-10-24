---
id: "sim-C3"
tipo: "regla-sim"
title: "Reparar cuesta 7–9 % del valor bruto"
aliases: ["sim-C3"]
grupo: "C · Herramientas"
estado: "pasa"
origen: "doc"
valor: 7.5284
unidad: "%"
documentos: ["[[28 §5 Herramientas]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:254"
generado: true
---

# Reparar cuesta 7–9 % del valor bruto

> C · Herramientas · pasa · 6–10 %

**Grupo:** C · Herramientas · **Origen del umbral:** documento aprobado

## Qué mide

coste de reparar sobre el valor bruto de la expedición en cada acto de la campaña del jugador medio

## Umbral

6–10 %

## Resultado

Estado: **pasa**. reparación sobre el valor bruto de la expedición (Acto II): **7.5284 %** (IC95 [7.3621, 7.6948], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 7.5284 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| reparación sobre el valor bruto de la expedición (Acto II) | 7.5284 % | [7.3621, 7.6948] | 6 a 10 | pasa |
| reparación sobre el valor bruto de la expedición (Acto III) | 7.7695 % | [7.6286, 7.9104] | 6 a 10 | pasa |
| reparación sobre el valor bruto de la expedición (Acto IV) | 7.6718 % | [7.4278, 7.9158] | 6 a 10 | pasa |

## Criterio

- **rep_min:** 6
- **rep_max:** 10

## Requisitos que protege

- Sumideros por acto y recurrentes (prensa, licencias, viaje, reparación, renta) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Reparación a un 45 % del precio actual
  - `economy.tools.repair.money_per_point` = 1.4, 2.3, 9, 38, 108

## Relaciones

- **Documentos:** [[28 §5 Herramientas]]
- **Bloques de economía:** [[Herramientas]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:254`
