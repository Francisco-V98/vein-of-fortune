---
id: "sim-G4"
tipo: "regla-sim"
title: "El Dependiente aporta, pero poco"
aliases: ["sim-G4"]
grupo: "G · Empleados"
estado: "pasa"
origen: "prop."
valor: 4.1453
unidad: "%"
documentos: ["[[28 §8 Empleados]]", "[[04 Progresión y meta]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:553"
generado: true
---

# El Dependiente aporta, pero poco

> G · Empleados · pasa · > 0 y ≤ 35 % (II y III)

**Grupo:** G · Empleados · **Origen del umbral:** propuesta del simulador

## Qué mide

aporte neto del Dependiente simulado sobre el ingreso diario del jugador

## Umbral

> 0 y ≤ 35 % (II y III)

## Resultado

Estado: **pasa**. aporte neto del Dependiente sobre el ingreso del jugador (Acto II): **4.1453 %** (IC95 [3.1473, 5.1434], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 4.1453 | [3.1473, 5.1434] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| aporte neto del Dependiente en esquirlas por día (Acto II) | 72.1415 esq/día | [54.8365, 89.4465] | 0 a … | pasa |
| aporte neto del Dependiente sobre el ingreso del jugador (Acto II) | 4.1453 % | [3.1473, 5.1434] | … a 35 | pasa |
| aporte neto del Dependiente en esquirlas por día (Acto III) | 227.3048 esq/día | [165.4579, 289.1517] | 0 a … | pasa |
| aporte neto del Dependiente sobre el ingreso del jugador (Acto III) | 3.355 % | [2.4477, 4.2623] | … a 35 | pasa |

## Criterio

- **max_pct:** 35
- **actos:** II, III

## Requisitos que protege

- El empleado no domina (salario, plantilla, ausencia, Dependiente) ([[04 Progresión y meta]])

## Mutaciones de prueba

- Dependiente por 10 al día
  - `economy.employees.support_salary_per_day.dependiente.II` = 10
  - `economy.employees.support_salary_per_day.dependiente.III` = 10
  - `economy.employees.support_salary_per_day.dependiente.IV` = 10

## Relaciones

- **Documentos:** [[28 §8 Empleados]], [[04 Progresión y meta]]
- **Bloques de economía:** [[Empleados]], [[Mejoras de la tienda]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:553`
