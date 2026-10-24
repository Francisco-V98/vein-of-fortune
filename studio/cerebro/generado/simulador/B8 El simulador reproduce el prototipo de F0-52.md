---
id: "sim-B8"
tipo: "regla-sim"
title: "El simulador reproduce el prototipo de F0-52"
aliases: ["sim-B8"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "prop."
valor: 0.866
unidad: "%"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[28 §13 Validación con el simulador (F0-53)]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:215"
generado: true
---

# El simulador reproduce el prototipo de F0-52

> B · Ritmo, progresión y estatus · pasa · ≤ 5 %

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** propuesta del simulador

## Qué mide

las cuatro etapas del prototipo frente a 6 300 · 10 200 · 36 000 · 167 000

## Umbral

≤ 5 %

## Resultado

Estado: **pasa**. prototipo IIe frente a 6300 esq/h: **0.866 %** (IC95 [0.5954, 1.1366], n = 16).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 0.866 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| prototipo IIe frente a 6300 esq/h | 0.866 % | [0.5954, 1.1366] | … a 5 | pasa |
| prototipo II frente a 10800 esq/h | 0.406 % | [0.1468, 0.6652] | … a 5 | pasa |
| prototipo III frente a 38700 esq/h | 0.3866 % | [0.1593, 0.6139] | … a 5 | pasa |
| prototipo IV frente a 181000 esq/h | 0.29 % | [0.0202, 0.5597] | … a 5 | pasa |

## Criterio

- **desv_max:** 5

## Requisitos que protege

- Ritmo por acto 1 100 · 7 500 · 27 000 · 125 000 (la media del acto) ([[28 §2 Ritmo objetivo y patrimonio]])
- El simulador es reproducible y cada regla se puede voltear ([[15 Flujo de trabajo y calidad]])

## Mutaciones de prueba

- Reparar casi gratis: el prototipo ya no coincide
  - `economy.tools.repair.money_per_point` = 1, 1, 1, 1, 1

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[28 §13 Validación con el simulador (F0-53)]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]], [[Herramientas]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:215`
