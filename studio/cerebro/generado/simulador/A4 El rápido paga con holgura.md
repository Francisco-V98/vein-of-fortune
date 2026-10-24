---
id: "sim-A4"
tipo: "regla-sim"
title: "El rápido paga con holgura"
aliases: ["sim-A4"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 100.0
unidad: "%"
documentos: ["[[28 §13 Validación con el simulador (F0-53)]]", "[[27 Guion del Acto I, día a día]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:52"
generado: true
---

# El rápido paga con holgura

> A · Acto I y deuda · pasa · pago ≥ 99,9 % · margen 100–300 %

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

pago y margen del rápido con 9 expediciones

## Umbral

pago ≥ 99,9 % · margen 100–300 %

## Resultado

Estado: **pasa**. pago a tiempo: **100 %** (IC95 [99.936, 100], n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Rápido\|rapido]] | 100 | [99.936, 100] | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| pago a tiempo | 100 % | [99.936, 100] | 99.9 a … | pasa |
| margen sobre la cuota | 235.9571 % | [235.0913, 236.8228] | 100 a 300 | pasa |

## Criterio

- **pago_min:** 99.9
- **margen_min:** 100
- **margen_max:** 300

## Requisitos que protege

- La cuota del día 7 (960) se paga con 5 expediciones y el margen es real ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- Cuota de 4 000: ni el rápido paga
  - `economy.debt.first_payment` = 4000

## Relaciones

- **Documentos:** [[28 §13 Validación con el simulador (F0-53)]], [[27 Guion del Acto I, día a día]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:52`
