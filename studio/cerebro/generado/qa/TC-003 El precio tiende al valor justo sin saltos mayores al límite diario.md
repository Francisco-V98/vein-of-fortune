---
id: "qa-TC-003"
tipo: "caso-qa"
title: "El precio tiende al valor justo sin saltos mayores al límite diario"
aliases: ["qa-TC-003", "TC-003"]
area: "Mercado"
tipo_prueba: "simulación"
nivel: "integración"
automatizable: true
prio: "P0"
estado: "sin ejecutar"
tareas: ["[[F2-08 Simulador por consola de miles de días]]"]
arriba: "[[MOC QA]]"
tags: ["estado/pendiente", "prio/P0"]
fuente: "studio/data/qa/cases.json:86"
generado: true
---

# El precio tiende al valor justo sin saltos mayores al límite diario

> Mercado · P0 · simulación · sin ejecutar

**Área:** Mercado · **Tipo:** simulación · **Nivel:** integración · **Automatizable:** sí · **Prioridad:** P0

## Pasos

1. Simular 10.000 días
2. Medir variación diaria y distancia al valor justo

## Resultado esperado

Ninguna variación diaria supera el límite y el precio vuelve al valor justo a largo plazo.

## Última ejecución

Estado: **sin ejecutar**

## Relaciones

- **Tareas:** [[F2-08 Simulador por consola de miles de días]]
- **Documento:** [[16 Calidad y QA]]

## Fuente

`studio/data/qa/cases.json:86`
