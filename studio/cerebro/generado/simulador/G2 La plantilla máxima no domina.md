---
id: "sim-G2"
tipo: "regla-sim"
title: "La plantilla máxima no domina"
aliases: ["sim-G2"]
grupo: "G · Empleados"
estado: "pasa"
origen: "doc"
valor: 67.9403
unidad: "%"
documentos: ["[[04 Progresión y meta]]", "[[28 §8 Empleados]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:526"
generado: true
---

# La plantilla máxima no domina

> G · Empleados · pasa · bruto ≤ 70 % · neto ≤ 45 % del jugador solo

**Grupo:** G · Empleados · **Origen del umbral:** documento aprobado

## Qué mide

aporte bruto y neto de la plantilla máxima (Mineros y Dependiente) con el jugador presente

## Umbral

bruto ≤ 70 % · neto ≤ 45 % del jugador solo

## Resultado

Estado: **pasa**. aporte bruto de la plantilla máxima sobre el jugador solo (peor: Acto III): **67.9403 %** (IC95 [66.5879, 69.2928], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 41.5605 | [40.3364, 42.7847] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| aporte bruto de la plantilla máxima sobre el jugador solo (peor: Acto III) | 67.9403 % | [66.5879, 69.2928] | … a 70 | pasa |
| aporte neto de la plantilla máxima sobre el jugador solo (peor: Acto III) | 41.5605 % | [40.3364, 42.7847] | … a 45 | pasa |

## Criterio

- **bruto_max:** 70
- **neto_max:** 45

## Requisitos que protege

- El empleado no domina (salario, plantilla, ausencia, Dependiente) ([[04 Progresión y meta]])

## Mutaciones de prueba

- Eficiencia de N4 y N5 de 5 %
  - `economy.employees.levels.3.efficiency_pct` = 5
  - `economy.employees.levels.4.efficiency_pct` = 5

## Relaciones

- **Documentos:** [[04 Progresión y meta]], [[28 §8 Empleados]]
- **Bloques de economía:** [[Empleados]], [[Mejoras de la tienda]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:526`
