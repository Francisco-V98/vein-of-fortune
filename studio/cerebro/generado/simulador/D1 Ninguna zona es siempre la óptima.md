---
id: "sim-D1"
tipo: "regla-sim"
title: "Ninguna zona es siempre la óptima"
aliases: ["sim-D1"]
grupo: "D · Zonas"
estado: "pasa"
origen: "doc"
valor: 3
unidad: "zonas"
documentos: ["[[02 Extracción]]", "[[28 §3 Los diez minerales]]", "[[28 §13 Validación con el simulador (F0-53)]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:295"
generado: true
---

# Ninguna zona es siempre la óptima

> D · Zonas · pasa · mejor zona ≤ 65 % · mejor fija ≤ 100 % de la adaptativa · ≥ 3 zonas con ≥ 15 % de uso

**Grupo:** D · Zonas · **Origen del umbral:** documento aprobado

## Qué mide

reparto de la política adaptativa y rendimiento de la mejor zona fija (cuadrícula nivel × Aguante × acto)

## Umbral

mejor zona ≤ 65 % · mejor fija ≤ 100 % de la adaptativa · ≥ 3 zonas con ≥ 15 % de uso

## Resultado

Estado: **pasa**. zonas con uso ≥ 15 % (mínimo de los actos): **3 zonas** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 41.0182 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mejor zona: parte de las expediciones de la política adaptativa | 41.0182 % | [41.0182, 41.0182] | … a 65 | pasa |
| mejor zona fija frente a la adaptativa (peor caso) | 97.1841 % | [95.0335, 99.3347] | … a 100 | pasa |
| zonas con uso ≥ 15 % (mínimo de los actos) | 3 zonas | [3, 3] | 3 a … | pasa |

### Datos adicionales

- **reparto:**
  - **II/2/30/medio:**
    - **galerias-hollin:** 19.2
    - **canon-ferroso:** 19.4
    - **sierra-alta:** 20.4
    - **salares:** 41
  - **II/2/40/medio:**
    - **galerias-hollin:** 19.7
    - **canon-ferroso:** 19.6
    - **sierra-alta:** 20.3
    - **salares:** 40.4
  - **II/3/30/lento:**
    - **galerias-hollin:** 19.6
    - **canon-ferroso:** 20.8
    - **sierra-alta:** 31.8
    - **salares:** 27.8
  - **II/3/30/medio:**
    - **galerias-hollin:** 19.3
    - **canon-ferroso:** 19.5
    - **sierra-alta:** 32.5
    - **salares:** 28.7
  - **II/3/30/rapido:**
    - **galerias-hollin:** 18.9
    - **canon-ferroso:** 19
    - **sierra-alta:** 34.1
    - **salares:** 28.1
  - **II/3/40/lento:**
    - **galerias-hollin:** 20.1
    - **canon-ferroso:** 21.1
    - **sierra-alta:** 31.4
    - **salares:** 27.4
  - **II/3/40/medio:**
    - **galerias-hollin:** 19.6
    - **canon-ferroso:** 19.6
    - **sierra-alta:** 33
    - **salares:** 27.8
  - **II/3/40/rapido:**
    - **galerias-hollin:** 18.9
    - **canon-ferroso:** 19
    - **sierra-alta:** 36
    - **salares:** 26
  - **III/3/40/medio:**
    - **galerias-hollin:** 2.6
    - **canon-ferroso:** 21.1
    - **sierra-alta:** 25.3
    - **salares:** 25.5
    - **cavernas:** 25.5
  - **III/3/62/medio:**
    - **galerias-hollin:** 2.5
    - **canon-ferroso:** 21.5
    - **sierra-alta:** 25.2
    - **salares:** 25.5
    - **cavernas:** 25.2
  - **III/4/40/lento:**
    - **galerias-hollin:** 6.9
    - **canon-ferroso:** 8.9
    - **sierra-alta:** 27.7
    - **salares:** 27.5
    - **cavernas:** 28.9
  - **III/4/40/medio:**
    - **galerias-hollin:** 2.5
    - **canon-ferroso:** 7.6
    - **sierra-alta:** 27.6
    - **salares:** 27.6
    - **cavernas:** 34.8
  - **III/4/40/rapido:**
    - **galerias-hollin:** 0.6
    - **canon-ferroso:** 6.7
    - **sierra-alta:** 27.2
    - **salares:** 27.4
    - **cavernas:** 38.1
  - **III/4/62/lento:**
    - **galerias-hollin:** 7.3
    - **canon-ferroso:** 8.5
    - **sierra-alta:** 27.6
    - **salares:** 27.3
    - **cavernas:** 29.2
  - **III/4/62/medio:**
    - **galerias-hollin:** 2.5
    - **canon-ferroso:** 7.4
    - **sierra-alta:** 27.5
    - **salares:** 27.6
    - **cavernas:** 35
  - **III/4/62/rapido:**
    - **galerias-hollin:** 0.5
    - **canon-ferroso:** 7.1
    - **sierra-alta:** 27.1
    - **salares:** 27.2
    - **cavernas:** 38
  - **IV/4/62/medio:**
    - **galerias-hollin:** 2.3
    - **canon-ferroso:** 3.7
    - **sierra-alta:** 24.1
    - **salares:** 16.6
    - **cavernas:** 31.3
    - **fosa:** 21.9
  - **IV/4/80/medio:**
    - **galerias-hollin:** 2.4
    - **canon-ferroso:** 3.5
    - **sierra-alta:** 24
    - **salares:** 17.3
    - **cavernas:** 31.1
    - **fosa:** 21.8
  - **IV/5/62/lento:**
    - **galerias-hollin:** 6.4
    - **canon-ferroso:** 7.8
    - **sierra-alta:** 24.8
    - **salares:** 20.1
    - **cavernas:** 23.5
    - **fosa:** 17.4
  - **IV/5/62/medio:**
    - **galerias-hollin:** 2.3
    - **canon-ferroso:** 3.2
    - **sierra-alta:** 24.9
    - **salares:** 18.5
    - **cavernas:** 29.9
    - **fosa:** 21.2
  - **IV/5/62/rapido:**
    - **galerias-hollin:** 0.5
    - **canon-ferroso:** 1
    - **sierra-alta:** 25
    - **salares:** 19.9
    - **cavernas:** 30.6
    - **fosa:** 23
  - **IV/5/80/lento:**
    - **galerias-hollin:** 6.5
    - **canon-ferroso:** 7.8
    - **sierra-alta:** 24.7
    - **salares:** 19.5
    - **cavernas:** 23.8
    - **fosa:** 17.6
  - **IV/5/80/medio:**
    - **galerias-hollin:** 2.2
    - **canon-ferroso:** 3.1
    - **sierra-alta:** 25
    - **salares:** 19.2
    - **cavernas:** 29.5
    - **fosa:** 20.9
  - **IV/5/80/rapido:**
    - **galerias-hollin:** 0.5
    - **canon-ferroso:** 0.9
    - **sierra-alta:** 25.2
    - **salares:** 20.6
    - **cavernas:** 30.1
    - **fosa:** 22.7

## Criterio

- **zona_max:** 65
- **fija_max:** 100
- **uso_min:** 15
- **zonas_min:** 3

## Requisitos que protege

- Ninguna zona es siempre la óptima ([[02 Extracción]])

## Mutaciones de prueba

- Las zonas no se agotan: una zona domina
  - `economy.expedition.zone_wealth.per_expedition` = 0

## Relaciones

- **Documentos:** [[02 Extracción]], [[28 §3 Los diez minerales]], [[28 §13 Validación con el simulador (F0-53)]]
- **Bloques de economía:** [[Expediciones]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:295`
