---
id: "sim-G5"
tipo: "regla-sim"
title: "Entrenar y ascender no es un bucle"
aliases: ["sim-G5"]
grupo: "G · Empleados"
estado: "pasa"
origen: "prop."
valor: 1.0
unidad: ""
documentos: ["[[28 §8 Empleados]]", "[[04 Progresión y meta]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:566"
generado: true
---

# Entrenar y ascender no es un bucle

> G · Empleados · pasa · retorno ≥ 5 días, sin máximo

**Grupo:** G · Empleados · **Origen del umbral:** propuesta del simulador

## Qué mide

días que tarda en recuperarse el entrenamiento de un nivel al siguiente; el salario sigue al nivel

## Umbral

retorno ≥ 5 días, sin máximo

## Resultado

Estado: **pasa**. el salario sigue al nivel (1 = sí): **1 ** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| días para recuperar el entrenamiento de N1 a N2 (Acto II) | 18.1673 días | [18.1673, 18.1673] | 5 a 100000 | pasa |
| días para recuperar el entrenamiento de N3 a N4 (Acto III) | 7.0306 días | [7.0306, 7.0306] | 5 a 100000 | pasa |
| días para recuperar el entrenamiento de N4 a N5 (Acto III) | 106.7602 días | [106.7602, 106.7602] | 5 a 100000 | pasa |
| el salario sigue al nivel (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |

## Criterio

- **min:** 5
- **max:** 100000
- **niveles:** II, 1, II, 2, III, 3, III, 4, III, 5

## Requisitos que protege

- Entrenamiento y ascenso: el salario sigue al nivel ([[28 §8 Empleados]])

## Mutaciones de prueba

- Todos los salarios a 1
  - `economy.employees.levels.0.salary_per_day` = 1
  - `economy.employees.levels.1.salary_per_day` = 1
  - `economy.employees.levels.2.salary_per_day` = 1
  - `economy.employees.levels.3.salary_per_day` = 1
  - `economy.employees.levels.4.salary_per_day` = 1

## Relaciones

- **Documentos:** [[28 §8 Empleados]], [[04 Progresión y meta]]
- **Bloques de economía:** [[Empleados]], [[Mejoras de la tienda]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:566`
