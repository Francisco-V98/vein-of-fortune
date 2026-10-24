---
id: "sim-G3"
tipo: "regla-sim"
title: "El jugador ausente rinde menos"
aliases: ["sim-G3"]
grupo: "G · Empleados"
estado: "pasa"
origen: "prop."
valor: 63.4597
unidad: "%"
documentos: ["[[04 Progresión y meta]]", "[[28 §8 Empleados]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:539"
generado: true
---

# El jugador ausente rinde menos

> G · Empleados · pasa · plantilla sola ≤ 65 % · jugador + plantilla ≥ solo + 5 %

**Grupo:** G · Empleados · **Origen del umbral:** propuesta del simulador

## Qué mide

ingreso de la plantilla sola y ganancia de jugador + plantilla

## Umbral

plantilla sola ≤ 65 % · jugador + plantilla ≥ solo + 5 %

## Resultado

Estado: **pasa**. ingreso de la plantilla sola frente al jugador solo (peor: Acto III): **63.4597 %** (IC95 [62.6588, 64.2606], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 10.6584 | [9.7409, 11.5758] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| ingreso de la plantilla sola frente al jugador solo (peor: Acto III) | 63.4597 % | [62.6588, 64.2606] | … a 65 | pasa |
| ganancia neta de jugador + plantilla frente al jugador solo (peor: Acto II) | 10.6584 % | [9.7409, 11.5758] | 5 a … | pasa |

## Criterio

- **ausente_max:** 65
- **conjunto_min:** 5
- **actos_conjunto:** II, III

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

`studio/data/sim/reglas.json:539`
