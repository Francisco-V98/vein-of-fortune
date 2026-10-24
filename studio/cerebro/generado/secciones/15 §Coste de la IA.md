---
id: "doc-15-coste-de-la-ia"
tipo: "seccion"
title: "Coste de la IA ✅"
aliases: ["doc-15-coste-de-la-ia"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Trabajo con IA]]"
siguiente: "[[15 §Ajustes de GitHub que hace el autor]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:220"
generado: true
---

# Coste de la IA ✅

> Decisión del autor (2026-10-23, ADR-0010). Las reglas completas están en CLAUDE.md; este es el resumen:

← [[15 §Trabajo con IA]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Ajustes de GitHub que hace el autor]] →

Decisión del autor (2026-10-23, [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|ADR-0010]]). Las reglas completas están en `CLAUDE.md`; este es el resumen:

- **Modelo y esfuerzo:** cada agente lleva los de su rol en `studio/data/equipo.json` (tabla en [[20 Equipo y flujo de agentes|20]]). Los cambios por tarea llevan su motivo; Fable 5.1 exige la autorización del autor.
- **Informes cortos:** encargo mínimo y informe de máximo 60 líneas o 6.000 caracteres (resultado, archivos tocados, hallazgos con `archivo:línea`, dudas para el autor).
- **Lectura parcial:** `grep -n` y rangos en lugar de documentos enteros; los archivos generados grandes no se leen.
- **Lotes:** los agentes independientes se lanzan juntos y sus informes se procesan juntos.
- **Cierre de sesión:** al fusionar el PR de una tarea se cierra la sesión o se compacta, para no arrastrar un contexto grande a la tarea siguiente.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:220`
