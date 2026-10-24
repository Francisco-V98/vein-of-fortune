---
id: "sim-H6"
tipo: "regla-sim"
title: "Misión de rescate: horas de juego"
aliases: ["sim-H6"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "prop."
valor: 13.5
unidad: "h"
documentos: ["[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:665"
generado: true
---

# Misión de rescate: horas de juego

> H · Deuda, mora y rescate · pasa · entrega de la cifra (informativa)

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** propuesta del simulador

## Qué mide

1,25 × p95 de las horas del lento para cumplir la parte económica de cada puerta, redondeado a 0,5 h

## Umbral

entrega de la cifra (informativa)

## Resultado

Estado: **pasa**. horas de la misión de rescate para la puerta A5 (1,25 × p95 del lento, a 0,5 h): **13.5 h** (IC95 –, n = 160).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 26.5 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| horas de la misión de rescate para la puerta A5 (1,25 × p95 del lento, a 0,5 h) | 13.5 h | [13.5, 13.5] | 0 a 100 | pasa |
| horas de la misión de rescate para la puerta circulo (1,25 × p95 del lento, a 0,5 h) | 26.5 h | [26.5, 26.5] | 0 a 100 | pasa |

### Datos adicionales

- **puertas:**
  - **A5:**
    - **p95:** 10.6167
    - **rescate:** 13.5
  - **circulo:**
    - **p95:** 21.0167
    - **rescate:** 26.5

## Criterio

- **margen:** 1.25
- **paso:** 0.5
- **max:** 100
- **informativa:** sí
- **percentil:** 0.95

## Requisitos que protege

- Misión de rescate: cuánto tiempo sin avanzar, en horas de juego ([[24 Umbrales de acto]])

## Mutaciones de prueba

- Piso de Comerciante de 500 000
  - `economy.pace.status_floors.comerciante` = 500000

## Relaciones

- **Documentos:** [[24 Umbrales de acto]]
- **Bloques de economía:** [[Ritmo objetivo]]
- **Perfiles:** [[Perfil Lento]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:665`
