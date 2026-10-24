---
id: "sim-D2"
tipo: "regla-sim"
title: "Agotamiento de las zonas"
aliases: ["sim-D2"]
grupo: "D · Zonas"
estado: "pasa"
origen: "doc"
valor: 7.6121
unidad: "%"
documentos: ["[[01 Core loop y ciclo del día]]", "[[02 Extracción]]", "[[28 §3 Los diez minerales]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:310"
generado: true
---

# Agotamiento de las zonas

> D · Zonas · pasa · 59 · 65 · 94 % ±5 pp · repetir pierde ≥ 5 %

**Grupo:** D · Zonas · **Origen del umbral:** documento aprobado

## Qué mide

riqueza media al salir de la zona y pérdida de quien repite una sola zona

## Umbral

59 · 65 · 94 % ±5 pp · repetir pierde ≥ 5 %

## Resultado

Estado: **pasa**. pérdida de quien repite una sola zona (acto con menor pérdida): **7.6121 %** (IC95 –, n = 12).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 1.7795 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| riqueza media al salir, desviación frente al objetivo (Acto II) | 1.7795 pp | [1.7795, 1.7795] | … a 5 | pasa |
| riqueza media al salir, desviación frente al objetivo (Acto III) | 1.3593 pp | [1.0911, 1.6274] | … a 5 | pasa |
| riqueza media al salir, desviación frente al objetivo (Acto IV) | 0.2154 pp | [0.2154, 1.0527] | … a 5 | pasa |
| pérdida de quien repite una sola zona (acto con menor pérdida) | 7.6121 % | [7.6121, 7.6121] | 5 a … | pasa |

## Criterio

- **pp_max:** 5
- **perdida_min:** 5

## Requisitos que protege

- Ninguna zona es siempre la óptima ([[02 Extracción]])

## Mutaciones de prueba

- Las zonas no se regeneran
  - `economy.expedition.zone_wealth.per_day` = 0

## Relaciones

- **Documentos:** [[01 Core loop y ciclo del día]], [[02 Extracción]], [[28 §3 Los diez minerales]]
- **Bloques de economía:** [[Expediciones]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:310`
