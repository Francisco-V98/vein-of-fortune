---
id: "qa-TC-042"
tipo: "caso-qa"
title: "La build solo escribe en su carpeta de guardados y diagnóstico"
aliases: ["qa-TC-042", "TC-042"]
area: "Seguridad"
tipo_prueba: "seguridad"
nivel: "manual"
automatizable: false
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F1-41 Lista de verificación de seguridad adaptada de OWASP MASVS]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:1010"
generado: true
---

# La build solo escribe en su carpeta de guardados y diagnóstico

> Seguridad · P0 · seguridad · sin ejecutar

**Área:** Seguridad · **Tipo:** seguridad · **Nivel:** manual · **Automatizable:** no · **Prioridad:** P0

## Pasos

1. Jugar una sesión con un monitor de archivos y revisar qué carpetas toca la build de Windows y de Linux

## Resultado esperado

El juego solo escribe en su carpeta de guardados y de diagnóstico; no hay ejecutables ni librerías sin explicar en la build.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F1-41 Lista de verificación de seguridad adaptada de OWASP MASVS]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:1010`
