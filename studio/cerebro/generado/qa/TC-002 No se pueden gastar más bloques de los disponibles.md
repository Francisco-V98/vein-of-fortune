---
id: "qa-TC-002"
tipo: "caso-qa"
title: "No se pueden gastar más bloques de los disponibles"
aliases: ["qa-TC-002", "TC-002"]
area: "Día"
tipo_prueba: "funcional"
nivel: "unitaria"
automatizable: true
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F2-02 Ciclo de 3 bloques y avance del día]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:62"
generado: true
---

# No se pueden gastar más bloques de los disponibles

> Día · P0 · funcional · sin ejecutar

**Área:** Día · **Tipo:** funcional · **Nivel:** unitaria · **Automatizable:** sí · **Prioridad:** P0

## Pasos

1. Gastar los tres bloques
2. Intentar una cuarta acción con bloque

## Resultado esperado

La acción se rechaza con un mensaje claro y el estado no cambia.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F2-02 Ciclo de 3 bloques y avance del día]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:62`
