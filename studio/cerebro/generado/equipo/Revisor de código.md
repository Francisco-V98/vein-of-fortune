---
id: "rol-revisor"
tipo: "rol"
title: "Revisor de código"
aliases: ["rol-revisor"]
rol: "revisor"
rol_tipo: "agente"
departamento: "[[Departamento Calidad]]"
desde: "[[F1 Preparación técnica]]"
especialista: false
agente: "revisor-codigo"
modelo: "sonnet"
esfuerzo: "medium"
arriba: "[[Departamento Calidad]]"
fuente: "studio/data/equipo.json"
generado: true
---

# Revisor de código

> Revisa cada cambio de código antes de que llegue al autor: errores, claridad y arquitectura.

**Entrega:** Revisión de código

**Agente** (`.claude/agents/revisor-codigo.md`): Revisor de código del estudio de Veta de Fortuna. Úsalo antes de QA cuando una tarea cambia código: errores, claridad, modularidad y estilo. No edita archivos.

**Herramientas:** Read, Grep, Glob, Bash

## Relaciones

- **Etapas:** [[Etapa QA]]
- **Documento:** [[20 Equipo y flujo de agentes]]
- **Tareas con su participación:** [[F0-81 Mod de consumo de tokens (vf-consumo)]]

## Fuente

`studio/data/equipo.json`
