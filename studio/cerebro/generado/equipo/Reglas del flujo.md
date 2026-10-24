---
id: "equipo-reglas"
tipo: "regla"
title: "Reglas del flujo"
aliases: ["equipo-reglas"]
arriba: "[[MOC Equipo]]"
fuente: "studio/data/equipo.json"
generado: true
---

# Reglas del flujo

> Reglas que cumple cada tarea al pasar por las etapas.

Fuente de verdad del equipo y del flujo de cada tarea. La leen el mod /equipo de Claude Code y build.py. Cada rol de tipo agente tiene su definición en .claude/agents/<agente>.md. «desde» es la fase en la que el rol se incorpora al estudio.

- Cada tarea elige qué etapas aplican; las que no hacen falta se marcan como omitidas, nunca se borran.
- Una etapa pasa a hecha solo cuando entrega lo que dice su rol; la siguiente no empieza antes.
- Producción la hace el especialista que corresponda a la tarea.
- El autor aprueba o devuelve; si devuelve, la tarea vuelve a Producción con el comentario.
- La prueba del autor se omite en las tareas que no tienen nada que probar todavía; si la hay, el diseñador de pruebas le prepara la guía.
- Nada cierra sin QA técnico aprobado, salvo tareas de solo decisión; si hay código, antes lo revisa el revisor de código.
- Un rol se incorpora al estudio en su fase («desde»); antes de eso queda en reserva.
- Solo se aplaza un punto abierto si una tarea ya existente lo va a resolver y nada de lo que se hace antes depende de la respuesta; lo que condiciona el futuro se decide con el autor antes de producir.

## Relaciones

- **Documento:** [[20 Equipo y flujo de agentes]]

## Fuente

`studio/data/equipo.json`
