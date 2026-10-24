---
id: "sim-B4"
tipo: "regla-sim"
title: "Los estatus se alcanzan a tiempo"
aliases: ["sim-B4"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "doc"
valor: 100.0
unidad: "%"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[04 Progresión y meta]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:149"
generado: true
---

# Los estatus se alcanzan a tiempo

> B · Ritmo, progresión y estatus · pasa · ≥ 95 % de las corridas · entre el 60 y el 90 % del acto · Magnate antes del cierre

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** documento aprobado

## Qué mide

corridas que alcanzan Comerciante, Empresario y Magnate y en qué punto del acto

## Umbral

≥ 95 % de las corridas · entre el 60 y el 90 % del acto · Magnate antes del cierre

## Resultado

Estado: **pasa**. comerciante alcanzado dentro del acto: **100 %** (IC95 [99.5221, 100], n = 800).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 100 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| comerciante alcanzado dentro del acto | 100 % | [99.5221, 100] | 95 a … | pasa |
| comerciante: momento del acto en que se alcanza | 65.6641 % | [65.0305, 66.2977] | 60 a 90 | pasa |
| empresario alcanzado dentro del acto | 100 % | [99.5221, 100] | 95 a … | pasa |
| empresario: momento del acto en que se alcanza | 69.8008 % | [69.1026, 70.499] | 60 a 90 | pasa |
| Magnate alcanzado antes del cierre del Acto IV | 99.875 % | [99.2954, 99.9779] | 80 a … | pasa |

## Criterio

- **alcanza_min:** 95
- **momento_min:** 60
- **momento_max:** 90
- **magnate_min:** 80

## Requisitos que protege

- Pisos de estatus (Comerciante, Empresario, Magnate) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Pisos de estatus rebajados
  - `economy.pace.status_floors.comerciante` = 12000
  - `economy.pace.status_floors.empresario` = 60000
  - `economy.pace.status_floors.magnate` = 200000

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[04 Progresión y meta]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:149`
