---
id: "qa-TC-051"
tipo: "caso-qa"
title: "Steam Auto-Cloud sincroniza hasta 5 partidas y en Hardcore manda el guardado local"
aliases: ["qa-TC-051", "TC-051"]
area: "Guardado"
tipo_prueba: "guardado"
nivel: "manual"
automatizable: false
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F5-50 Pruebas de instalación y actualización]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:1223"
generado: true
---

# Steam Auto-Cloud sincroniza hasta 5 partidas y en Hardcore manda el guardado local

> Guardado · P0 · guardado · sin ejecutar

**Área:** Guardado · **Tipo:** guardado · **Nivel:** manual · **Automatizable:** no · **Prioridad:** P0

## Pasos

1. Crear 5 partidas y sincronizarlas con Steam Auto-Cloud
2. Restaurar en otro equipo
3. En Hardcore, morir e intentar restaurar la partida desde la nube

## Resultado esperado

Las 5 partidas se sincronizan; en Hardcore no se recupera la partida muerta desde la nube porque manda el guardado local.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F5-50 Pruebas de instalación y actualización]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:1223`
