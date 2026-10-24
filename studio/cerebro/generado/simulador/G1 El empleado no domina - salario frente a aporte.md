---
id: "sim-G1"
tipo: "regla-sim"
title: "El empleado no domina: salario frente a aporte"
aliases: ["sim-G1"]
grupo: "G · Empleados"
estado: "pasa"
origen: "doc"
valor: 43.3295
unidad: "%"
documentos: ["[[04 Progresión y meta]]", "[[28 §8 Empleados]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:508"
generado: true
---

# El empleado no domina: salario frente a aporte

> G · Empleados · pasa · pares previstos 40–60 % (N2 del II; N4 y N5 del III) · todos ≤ 100 % (también N1) · 7 días

**Grupo:** G · Empleados · **Origen del umbral:** documento aprobado

## Qué mide

salario dividido por el aporte de un Minero por nivel y acto, con contratos de 7, 14 y 30 días

## Umbral

pares previstos 40–60 % (N2 del II; N4 y N5 del III) · todos ≤ 100 % (también N1) · 7 días ≤ 85 % · aporte neto en el IV ≤ 0

## Resultado

Estado: **pasa**. salario ÷ aporte, par previsto más bajo (III N4): **43.3295 %** (IC95 [41.4681, 45.3659], n = 60).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| salario ÷ aporte, par previsto más bajo (III N4) | 43.3295 % | [41.4681, 45.3659] | 40 a … | pasa |
| salario ÷ aporte, par previsto más alto (II N2) | 50.2618 % | [46.4981, 54.6884] | … a 60 | pasa |
| salario ÷ aporte, el peor de todos los pares | 58.6113 % | [53.3086, 65.0854] | … a 100 | pasa |
| con contrato de 7 días, el peor cociente | 76.1947 % | [76.1947, 76.1947] | … a 85 | pasa |
| aporte neto de un Minero en el Acto IV (esquirlas por día) | -9584.9929 esq/día | [-10045.1636, -9124.8222] | … a 0 | pasa |

### Datos adicionales

- **pares:**
  - **II/N2:**
    - **aporte:** 179.1
    - **sueldo:** 90
    - **cociente:** 50.3
  - **III/N4:**
    - **aporte:** 1384.7
    - **sueldo:** 600
    - **cociente:** 43.3
  - **III/N5:**
    - **aporte:** 1558.7
    - **sueldo:** 720
    - **cociente:** 46.2
  - **IV/N4:**
    - **aporte:** -8985
    - **sueldo:** 600
    - **cociente:** 1000000000
  - **IV/N5:**
    - **aporte:** -9999.7
    - **sueldo:** 720
    - **cociente:** 1000000000
  - **II/N1:**
    - **aporte:** 119.4
    - **sueldo:** 70
    - **cociente:** 58.6
  - **III/N2:**
    - **aporte:** 396.5
    - **sueldo:** 90
    - **cociente:** 22.7

## Criterio

- **previstos:** II, 2, III, 4, III, 5
- **siempre:** IV, 4, IV, 5
- **otros:** II, 1, III, 2
- **prev_min:** 40
- **prev_max:** 60
- **todos_max:** 100
- **siete_max:** 85

## Requisitos que protege

- El empleado no domina (salario, plantilla, ausencia, Dependiente) ([[04 Progresión y meta]])

## Mutaciones de prueba

- Salario del N2 de 500
  - `economy.employees.levels.1.salary_per_day` = 500

## Relaciones

- **Documentos:** [[04 Progresión y meta]], [[28 §8 Empleados]]
- **Bloques de economía:** [[Empleados]], [[Mejoras de la tienda]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:508`
