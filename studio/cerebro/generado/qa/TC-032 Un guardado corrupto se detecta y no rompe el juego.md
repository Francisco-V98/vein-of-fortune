---
id: "qa-TC-032"
tipo: "caso-qa"
title: "Un guardado corrupto se detecta y no rompe el juego"
aliases: ["qa-TC-032", "TC-032"]
area: "Guardado"
tipo_prueba: "guardado"
nivel: "integración"
automatizable: true
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F2-37 Pruebas de guardado - corrupción y migración]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:775"
generado: true
---

# Un guardado corrupto se detecta y no rompe el juego

> Guardado · P0 · guardado · sin ejecutar

**Área:** Guardado · **Tipo:** guardado · **Nivel:** integración · **Automatizable:** sí · **Prioridad:** P0

## Pasos

1. Alterar bytes del archivo
2. Cargar

## Resultado esperado

El juego detecta la corrupción, ofrece la copia de respaldo y no se cierra.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F2-37 Pruebas de guardado - corrupción y migración]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:775`
