---
id: "sim-F2"
tipo: "regla-sim"
title: "Barrido de políticas del mercado negro"
aliases: ["sim-F2"]
grupo: "F · Mercado negro y vigilancia"
estado: "pasa"
origen: "doc"
valor: 8.9692
unidad: "%"
documentos: ["[[03 Comercio y mercado]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:446"
generado: true
---

# Barrido de políticas del mercado negro

> F · Mercado negro y vigilancia · pasa · ≤ +12 %

**Grupo:** F · Mercado negro y vigilancia · **Origen del umbral:** documento aprobado

## Qué mide

mayor ganancia entre umbrales, sobornos, guardias, Faroleros y compra para llenar el lote

## Umbral

≤ +12 %

## Resultado

Estado: **pasa**. mayor ganancia semanal entre 60 políticas (acto II, umbral 45): **8.9692 %** (IC95 [7.9227, 10.0156], n = 30).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 8.9692 | [7.9227, 10.0156] | 30 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mayor ganancia semanal entre 60 políticas (acto II, umbral 45) | 8.9692 % | [7.9227, 10.0156] | … a 12 | pasa |

### Datos adicionales

- **politica_peor:**
  - **umbral:** 45
  - **comprar:** sí

## Criterio

- **max:** 12

## Requisitos que protege

- El mercado negro es un complemento moderado, no una estrategia dominante ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Tope nocturno gigante y prima negra de 90 %
  - `economy.surveillance.night_volume_cap.II` = 500000
  - `economy.surveillance.night_volume_cap.III` = 2000000
  - `economy.surveillance.night_volume_cap.IV` = 5000000
  - `minerals.carbon.black_premium` = 90
  - `minerals.hierro.black_premium` = 90
  - `minerals.cobre.black_premium` = 90
  - `minerals.salitre.black_premium` = 90
  - `minerals.plata.black_premium` = 90
  - `minerals.cuarzo.black_premium` = 90
  - `minerals.oro.black_premium` = 90
  - `minerals.esmeralda.black_premium` = 90
  - `minerals.diamante.black_premium` = 90

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §10 Vigilancia, multas, mercado negro y mora]]
- **Bloques de economía:** [[Vigilancia]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:446`
