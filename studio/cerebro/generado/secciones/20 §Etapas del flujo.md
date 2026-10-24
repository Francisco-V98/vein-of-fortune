---
id: "doc-20-etapas-del-flujo"
tipo: "seccion"
title: "Etapas del flujo ✅"
aliases: ["doc-20-etapas-del-flujo"]
documento: "[[20 Equipo y flujo de agentes]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[20 §Requisito del autor]]"
siguiente: "[[20 §El equipo]]"
arriba: "[[20 Equipo y flujo de agentes]]"
fuente: "studio/docs/20-equipo-y-flujo-de-agentes.md:7"
generado: true
---

# Etapas del flujo ✅

> Toda tarea recorre estas etapas en orden. Las que no hacen falta se marcan omitidas; nunca se borran.

← [[20 §Requisito del autor]] · [[20 Equipo y flujo de agentes|↑ 20]] · [[20 §El equipo]] →

Toda tarea recorre estas etapas en orden. Las que no hacen falta se marcan **omitidas**; nunca se borran.

| # | Etapa | Quién | Qué entrega |
|---|---|---|---|
| 1 | **Ideación** | Ideador | Tres o más opciones con ventajas y riesgos, y una recomendación |
| 2 | **Análisis** | Analista | Informe de coherencia, riesgos, dependencias y criterios de aceptación |
| 3 | **Producción** | El especialista que toque: diseñador de sistemas, narrador, director de arte o desarrollador | El trabajo en sí: documento, texto, arte o código |
| 4 | **QA técnico** | QA | Informe aprobado o con fallos: build estricto, pruebas, enlaces, coherencia |
| 5 | **Revisión del autor** | Fran (el autor) | Aprobación o devolución con comentarios |
| 6 | **Prueba del autor** | Fran (el autor) | Jugar y probar: que sea divertido, que se vea bien, que el tono funcione. Se omite si aún no hay nada que probar |
| 7 | **Cierre** | Coordinador (Claude) | Fusión, tarea cerrada, ramas limpias y registro al día |

Reglas ✅ del flujo, en `studio/data/equipo.json`:
- Una etapa pasa a **hecha** solo cuando entrega lo que dice su rol; la siguiente no empieza antes.
- Si el autor devuelve una tarea, vuelve a **Producción** con el comentario.
- Nada cierra sin QA técnico aprobado, salvo tareas de solo decisión, que pasan directo a la revisión del autor.
- Solo se aplaza un punto abierto si una tarea ya existente lo va a resolver y nada de lo que se hace antes depende de la respuesta (regla completa en [[15 Flujo de trabajo y calidad|15]]). El **analista** clasifica cada punto abierto como «decidir ahora» o «aplazar con su tarea»; los de «decidir ahora» se presentan al autor en lote antes de producir; el **narrador y los demás productores** no aplazan lo que el analista marcó como «decidir ahora»; **QA** devuelve la tarea si hay un aplazamiento que condiciona trabajo posterior.

## Fuente

`studio/docs/20-equipo-y-flujo-de-agentes.md:7`
