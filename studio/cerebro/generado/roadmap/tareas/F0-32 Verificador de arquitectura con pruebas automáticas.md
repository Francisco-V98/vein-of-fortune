---
id: "F0-32"
tipo: "tarea"
title: "F0-32 Verificador de arquitectura con pruebas automáticas"
aliases: ["F0-32"]
fase: "[[F0 Diseño]]"
hito: "[[F0.9 Metodología, calidad y QA]]"
prio: "P0"
est: 8
status: "done"
version: "MVP"
docs: []
arriba: "[[F0.9 Metodología, calidad y QA]]"
tags: ["estado/hecho", "prio/P0", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:368"
generado: true
---

# F0-32 Verificador de arquitectura con pruebas automáticas

> Comprueba capas, módulos, dominio puro, plataforma, ciclos y autoloads.

Comprueba capas, módulos, dominio puro, plataforma, ciclos y autoloads.

## Hecha cuando

22 pruebas pasan; falta ejecutarlo con código real en la Fase 1.

## Historial

- 2026-10-11 · backlog → doing · claude: Se construye el verificador con reglas A1 a A9. (rama chore/F0-34-herramientas-ci-y-convenciones · PR #3)
- 2026-10-11 · doing → review · claude: 22 pruebas automáticas pasan. Una prueba reveló un defecto real (no validaba ciclos sin código) y se corrigió. (rama chore/F0-34-herramientas-ci-y-convenciones · PR #3)
- 2026-10-11 · review → qa · claude: QA: 22 pruebas del verificador pasan en la CI de GitHub, también sobre main. (PR #3 · fusionado en main (4ec1f16))
- 2026-10-11 · qa → done · claude: Fusionado. Pendiente de validar con código GDScript real en la Fase 1. (PR #3 · fusionado en main (4ec1f16))

## Comentarios

- 2026-10-11 · claude: Límite honesto: es un análisis estático aproximado de rutas res:// y nombres de clase; no ve referencias dinámicas. Falta probarlo con GDScript real en la Fase 1.

## Evidencias

- file: Verificador
- file: Pruebas

## Relaciones

- **Hito:** [[F0.9 Metodología, calidad y QA]]

## Fuente

`studio/data/roadmap.json:368`
