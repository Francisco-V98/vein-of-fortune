---
id: "qa-TC-046"
tipo: "caso-qa"
title: "Un guardado manipulado no ejecuta contenido ni rompe invariantes"
aliases: ["qa-TC-046", "TC-046"]
area: "Seguridad"
tipo_prueba: "seguridad"
nivel: "integración"
automatizable: true
prio: "P1"
estado: "sin ejecutar"
tareas: ["[[F2-37 Pruebas de guardado - corrupción y migración]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P1"]
fuente: "studio/data/qa/cases.json:1103"
generado: true
---

# Un guardado manipulado no ejecuta contenido ni rompe invariantes

> Seguridad · P1 · seguridad · sin ejecutar

**Área:** Seguridad · **Tipo:** seguridad · **Nivel:** integración · **Automatizable:** sí · **Prioridad:** P1

## Pasos

1. Editar valores imposibles en el guardado
2. Cargar

## Resultado esperado

Los valores imposibles se rechazan o se corrigen; no hay efectos inesperados.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F2-37 Pruebas de guardado - corrupción y migración]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:1103`
