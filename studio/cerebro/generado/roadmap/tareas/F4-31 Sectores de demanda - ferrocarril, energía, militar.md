---
id: "F4-31"
tipo: "tarea"
title: "F4-31 Sectores de demanda: ferrocarril, energía, militar, agricultura, lujo y tecnología"
aliases: ["F4-31"]
fase: "[[F4 Contenido v1]]"
hito: "[[F4.2 Mercado completo]]"
prio: "P0"
est: 8
status: "backlog"
version: "Release 1"
docs: ["[[28 Números base de la economía]]", "[[03 Comercio y mercado]]", "[[26 Zonas y edificios]]"]
arriba: "[[F4.2 Mercado completo]]"
tags: ["estado/pendiente", "prio/P0", "fase/F4", "backlog/futuro", "version/Release-1"]
fuente: "studio/data/roadmap.json:2551"
generado: true
---

# F4-31 Sectores de demanda: ferrocarril, energía, militar, agricultura, lujo y tecnología

> Construir el modelo de demanda por sectores (ferrocarril, energía, militar, agricultura, lujo y tecnología): cada mineral reparte su…

Construir el modelo de demanda por sectores (ferrocarril, energía, militar, agricultura, lujo y tecnología): cada mineral reparte su demanda entre sectores con los pesos del documento 28 (ya cargados en el registro del mundo) y los eventos sectoriales mueven al mineral según su peso. Los pesos los fijó [[F0-52 Modelo económico - números base|F0-52]]; esta tarea implementa el modelo y los eventos.

## Hecha cuando

Un evento sectorial mueve cada mineral según su peso en ese sector y las pruebas lo comprueban con los pesos del registro del mundo.

## Relaciones

- **Hito:** [[F4.2 Mercado completo]]
- **Documentos:** [[28 Números base de la economía]], [[03 Comercio y mercado]], [[26 Zonas y edificios]]
- **Citada en:**
  - [[03 §Oferta y demanda]]
  - [[03 Comercio y mercado]]
  - [[26 §6 Vehículos, ropa, embarcaciones, pesca e inversiones]]
  - [[26 Zonas y edificios]]
  - [[28 §3 Los diez minerales]]
  - [[28 §13 Validación con el simulador (F0-53)]]
  - [[28 Números base de la economía]]

## Fuente

`studio/data/roadmap.json:2551`
