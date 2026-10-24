---
id: "sim-H3"
tipo: "regla-sim"
title: "Abonos anónimos y Consorcio"
aliases: ["sim-H3"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "doc"
valor: 30.0
unidad: "%"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[28 §7 Deuda del Acto I y sus nombres]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:619"
generado: true
---

# Abonos anónimos y Consorcio

> H · Deuda, mora y rescate · pasa · mismo capital · abono < interés · Consorcio ≤ 30 % de K y queda ≥ 50 %

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** documento aprobado

## Qué mide

capital con y sin abono; abono frente a interés; asunción del Consorcio

## Umbral

mismo capital · abono < interés · Consorcio ≤ 30 % de K y queda ≥ 50 %

## Resultado

Estado: **pasa**. capital máximo que asume el Consorcio frente a K: **30 %** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| diferencia de capital pagado con y sin abono (esquirlas) | 0 esq | [0, 0] | … a 0.5 | pasa |
| abono mensual frente al interés mensual con el 50 % pagado | 83.3333 % | [83.3333, 83.3333] | … a 100 | pasa |
| capital máximo que asume el Consorcio frente a K | 30 % | [30, 30] | … a 30 | pasa |
| capital que queda tras la asunción del Consorcio frente a K | 70 % | [70, 70] | 50 a … | pasa |

## Criterio

- **semanas:** 20
- **abono_max:** 100
- **queda_min:** 50

## Requisitos que protege

- Los abonos anónimos y el Consorcio no hacen inalcanzable la vía ([[24 Umbrales de acto]])

## Mutaciones de prueba

- Abono anónimo de 2 000 al mes
  - `economy.debt.anonymous_payment.amount_per_month` = 2000

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:619`
