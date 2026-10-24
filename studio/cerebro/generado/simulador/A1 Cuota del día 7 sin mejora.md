---
id: "sim-A1"
tipo: "regla-sim"
title: "Cuota del día 7 sin mejora"
aliases: ["sim-A1"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 99.6167
unidad: "%"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[28 §13 Validación con el simulador (F0-53)]]", "[[27 Guion del Acto I, día a día]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:6"
generado: true
---

# Cuota del día 7 sin mejora

> A · Acto I y deuda · pasa · pago 95–99,9 % · margen 30–75 % de la cuota

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

pago a tiempo y margen del jugador medio con 5 expediciones (4 000 corridas)

## Umbral

pago 95–99,9 % · margen 30–75 % de la cuota

## Resultado

Estado: **pasa**. pago a tiempo: **99.6167 %** (IC95 [99.4254, 99.7444], n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 99.6167 | [99.4254, 99.7444] | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| pago a tiempo | 99.6167 % | [99.4254, 99.7444] | 95 a 99.9 | pasa |
| margen sobre la cuota | 71.8541 % | [71.1652, 72.543] | 30 a 75 | pasa |

## Criterio

- **pago_min:** 95
- **pago_max:** 99.9
- **margen_min:** 30
- **margen_max:** 75

## Requisitos que protege

- La cuota del día 7 (960) se paga con 5 expediciones y el margen es real ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- El Aguante del Acto I sube de 25 a 27: el medio paga casi siempre
  - `economy.energy.per_act.I` = 27, 30

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[28 §13 Validación con el simulador (F0-53)]], [[27 Guion del Acto I, día a día]]
- **Bloques de economía:** [[Deuda del Acto I]], [[Energía]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:6`
