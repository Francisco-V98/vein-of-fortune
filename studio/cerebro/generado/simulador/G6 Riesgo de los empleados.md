---
id: "sim-G6"
tipo: "regla-sim"
title: "Riesgo de los empleados"
aliases: ["sim-G6"]
grupo: "G · Empleados"
estado: "pasa"
origen: "prop."
valor: 98.1921
unidad: "%"
documentos: ["[[28 §8 Empleados]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:580"
generado: true
---

# Riesgo de los empleados

> G · Empleados · pasa · informativa (≤ 100 % del aporte)

**Grupo:** G · Empleados · **Origen del umbral:** propuesta del simulador

## Qué mide

pérdida esperada de un Minero por herida, pérdida de carga y robo (informativa)

## Umbral

informativa (≤ 100 % del aporte)

## Resultado

Estado: **pasa**. pérdida esperada de un Minero por riesgo (peor zona: fosa), en % del aporte: **98.1921 %** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| pérdida esperada de un Minero por riesgo (peor zona: fosa), en % del aporte | 98.1921 % | [98.1921, 98.1921] | … a 100 | pasa |

## Criterio

- **max:** 100
- **informativa:** sí

## Requisitos que protege

- Riesgo de los empleados (herida, pérdida de carga, robo) ([[28 §8 Empleados]])

## Mutaciones de prueba

- La Fosa hiere al 100 % con 30 días de baja
  - `economy.employees.risk.by_zone.fosa.injury_pct` = 100
  - `economy.employees.risk.by_zone.fosa.sick_days` = 30

## Relaciones

- **Documentos:** [[28 §8 Empleados]]
- **Bloques de economía:** [[Empleados]], [[Mejoras de la tienda]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:580`
