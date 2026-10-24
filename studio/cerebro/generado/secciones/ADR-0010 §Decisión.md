---
id: "adr-0010-decision"
tipo: "seccion"
title: "Decisión ✅"
aliases: ["adr-0010-decision"]
documento: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0010 §Contexto]]"
siguiente: "[[ADR-0010 §Alternativas descartadas]]"
arriba: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
fuente: "studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:16"
generado: true
---

# Decisión ✅

> Decisiones del autor (2026-10-23):

← [[ADR-0010 §Contexto]] · [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|↑ ADR-0010]] · [[ADR-0010 §Alternativas descartadas]] →

Decisiones del autor (2026-10-23):

1. **Tabla por rol:** `studio/data/equipo.json` fija el modelo y el esfuerzo por defecto de cada agente (tabla en [[20 Equipo y flujo de agentes|20]]). Opus con esfuerzo alto para ideación y arquitectura; Sonnet para el resto; esfuerzo bajo para QA, localización y diseño de pruebas.
2. **Ajuste por tarea:** el coordinador puede subir o bajar el modelo o el esfuerzo en una tarea, con el motivo en una línea.
3. **Fable 5.1 solo con autorización del autor:** el mod `vf-equipo` abre un diálogo en `/equipo` con las opciones «aprobar para esta tarea», Opus, Sonnet, Haiku u otro. La aprobación vale para una tarea.
4. **Modo conciso:** agentes y encargos siguen la skill `modo-conciso`: encargo mínimo, informe de máximo 60 líneas o 6.000 caracteres, lectura parcial, lotes y cierre de sesión al fusionar (reglas en `CLAUDE.md` y [[15 Flujo de trabajo y calidad|15]]).

## Fuente

`studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:16`
