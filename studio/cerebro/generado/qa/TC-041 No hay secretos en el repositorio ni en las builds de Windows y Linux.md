---
id: "qa-TC-041"
tipo: "caso-qa"
title: "No hay secretos en el repositorio ni en las builds de Windows y Linux"
aliases: ["qa-TC-041", "TC-041"]
area: "Seguridad"
tipo_prueba: "seguridad"
nivel: "unitaria"
automatizable: true
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F1-42 Escaneo de secretos en integración continua]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:987"
generado: true
---

# No hay secretos en el repositorio ni en las builds de Windows y Linux

> Seguridad · P0 · seguridad · sin ejecutar

**Área:** Seguridad · **Tipo:** seguridad · **Nivel:** unitaria · **Automatizable:** sí · **Prioridad:** P0

## Pasos

1. Ejecutar el escaneo de secretos sobre el repositorio y sobre las builds exportadas

## Resultado esperado

El escaneo no encuentra claves, tokens ni contraseñas.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F1-42 Escaneo de secretos en integración continua]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:987`
