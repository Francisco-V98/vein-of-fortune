---
id: "sim-A6"
tipo: "regla-sim"
title: "Cuota del día 14 y recargos en las cuatro dificultades"
aliases: ["sim-A6"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 0.4
unidad: "esq"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[27 Guion del Acto I, día a día]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:78"
generado: true
---

# Cuota del día 14 y recargos en las cuatro dificultades

> A · Acto I y deuda · pasa · Novato e Intermedio ≤ 30 % · Difícil ≤ 55 % · Hardcore ≤ 60 %

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

peso de la cuota del día 14 sobre el ingreso de la semana 2

## Umbral

Novato e Intermedio ≤ 30 % · Difícil ≤ 55 % · Hardcore ≤ 60 %

## Resultado

Estado: **pasa**. recargo de Intermedio menos 6 % de la cuota (esquirlas): **0.4 esq** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 20.0073 | [18.3094, 21.7052] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| peso de la cuota del día 14 (novato) | 19.6298 % | [17.9639, 21.2957] | … a 30 | pasa |
| peso de la cuota del día 14 (intermedio) | 20.0073 % | [18.3094, 21.7052] | … a 30 | pasa |
| peso de la cuota del día 14 (dificil) | 40.0146 % | [36.6187, 43.4105] | … a 55 | pasa |
| peso de la cuota del día 14 (hardcore) | 41.1471 % | [37.6551, 44.6391] | … a 60 | pasa |
| recargo de Intermedio menos 6 % de la cuota (esquirlas) | 0.4 esq | [0.4, 0.4] | … a 0.5 | pasa |

## Criterio

- **leve_max:** 30
- **dificil_max:** 55
- **duro_max:** 60

## Requisitos que protege

- Cuota del día 14 y recargos en las cuatro dificultades ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- Cuota de 4 000: la cuota del día 14 aplasta la semana
  - `economy.debt.first_payment` = 4000

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[27 Guion del Acto I, día a día]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:78`
