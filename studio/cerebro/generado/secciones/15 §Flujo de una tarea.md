---
id: "doc-15-flujo-de-una-tarea"
tipo: "seccion"
title: "Flujo de una tarea ✅"
aliases: ["doc-15-flujo-de-una-tarea"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Commits]]"
siguiente: "[[15 §Pull requests]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:57"
generado: true
---

# Flujo de una tarea ✅

> 1. Elegir la tarea del Sprint y moverla a doing registrando la rama en el historial.

← [[15 §Commits]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Pull requests]] →

```
backlog → sprint → doing → review → qa → done
```

1. **Elegir la tarea** del Sprint y moverla a `doing` registrando la rama en el historial.
2. **Crear la rama** desde `main` actualizado.
3. **Trabajar en commits pequeños.** Dominio y pruebas primero.
4. **Verificar en local:** formato, lint, arquitectura, pruebas, mensajes de commit.
5. **Subir la rama y abrir el PR** con la plantilla.
6. **Integración continua en verde** y auto-revisión con la lista de abajo. Revisión asistida con `/code-review`.
7. La tarea pasa a **`review`** con el enlace al PR: el autor revisa el código y la arquitectura.
8. Con la revisión aprobada, pasa a **`qa`**: se ejecutan los casos de prueba de la tarea, la regresión, y las pruebas de seguridad y rendimiento que apliquen ([[16 Calidad y QA|16]]).
9. Si QA aprueba, el autor hace el **merge** (squash), borra la rama y la tarea pasa a **`done`** con la referencia del commit y la evidencia de QA.
10. Si QA falla, la tarea vuelve a **`doing`** y el error se registra con su severidad.

Las tareas que no producen comportamiento (documentos, decisiones, estudio) pasan de `review` a `done` y lo dicen en su nota.

El estado de la tarea refleja siempre el de su rama, y queda registrado en el historial con el campo `ref` (rama, PR o commit).

Dentro de estos estados, cada tarea recorre un flujo por etapas con un equipo de especialistas (ideación, análisis, producción, QA técnico, revisión y prueba del autor, y cierre); está descrito en [[20 Equipo y flujo de agentes|20]].

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:57`
