---
id: "F0-88"
tipo: "tarea"
title: "F0-88 Consulta del estudio sin leer documentos enteros (tools/consulta.py)"
aliases: ["F0-88"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P1"
est: 5
status: "backlog"
version: "MVP"
docs: ["[[10 Técnico y herramientas]]", "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"]
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/pendiente", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:902"
generado: true
---

# F0-88 Consulta del estudio sin leer documentos enteros (tools/consulta.py)

> Fase 2 del plan de ahorro de tokens. Herramienta de consulta (limpieza por documento, puntos abiertos con línea, índice de encabezados…

Fase 2 del plan de ahorro de tokens. Herramienta de consulta (limpieza por documento, puntos abiertos con línea, índice de encabezados, fichas de 10 a 20 líneas, tareas y datos del mundo por ruta) para que los agentes dejen de leer documentos enteros; se cita en CLAUDE.md y en los prompts de los agentes. Decisión del autor del 2026-10-23: optimizar el consumo de tokens con modelo y esfuerzo por agente, autorización de Fable 5.1 y un modo conciso (plan en tres fases).

## Hecha cuando

Los comandos de consulta coinciden con el build, tienen pruebas y los agentes los usan en lugar de leer documentos completos.

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]
- **Documentos:** [[10 Técnico y herramientas]], [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]
- **Citada en:** [[10 §Cerebro del proyecto en Obsidian]], [[10 Técnico y herramientas]], [[ADR-0010 §Consecuencias]], [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]

## Fuente

`studio/data/roadmap.json:902`
