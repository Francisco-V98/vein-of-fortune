---
id: "sim-E5"
tipo: "regla-sim"
title: "Volatilidad y topes diarios"
aliases: ["sim-E5"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 1.0
unidad: ""
documentos: ["[[28 §3 Los diez minerales]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:391"
generado: true
---

# Volatilidad y topes diarios

> E · Mercado y bucles · pasa · ±10 % · orden respetado · ≤ 6 % de los días en el tope

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

desviación diaria de cada mineral frente a la de la tabla, orden entre minerales y días en el tope

## Umbral

±10 % · orden respetado · ≤ 6 % de los días en el tope

## Resultado

Estado: **pasa**. orden de volatilidad entre minerales respetado (1 = sí): **1 ** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mayor desviación de la volatilidad diaria frente a la objetivo (diamante) | 4.4046 % | [1.6179, 7.1914] | … a 10 | pasa |
| orden de volatilidad entre minerales respetado (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |
| días en el tope diario (peor mineral) | 4.8 % | [4.8, 4.8] | … a 6 | pasa |

### Datos adicionales

- **desv_diaria:**
  - **carbon:** 2.4402
  - **hierro:** 1.8593
  - **cobre:** 2.9644
  - **salitre:** 3.7088
  - **plata:** 3.081
  - **oro:** 2.2824
  - **cuarzo:** 3.0729
  - **esmeralda:** 4.3442
  - **diamante:** 4.4894
  - **aetherita:** 5.6743

## Criterio

- **desv_max:** 10
- **tope_max:** 6
- **eps_tope:** 0.05

## Requisitos que protege

- Volatilidad, topes diarios y orden entre minerales ([[28 §3 Los diez minerales]])

## Mutaciones de prueba

- Carbón con ruido de 5 puntos
  - `minerals.carbon.sigma` = 5

## Relaciones

- **Documentos:** [[28 §3 Los diez minerales]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:391`
