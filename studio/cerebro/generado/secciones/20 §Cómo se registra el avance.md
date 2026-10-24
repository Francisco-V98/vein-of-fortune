---
id: "doc-20-como-se-registra-el-avance"
tipo: "seccion"
title: "Cómo se registra el avance ✅"
aliases: ["doc-20-como-se-registra-el-avance"]
documento: "[[20 Equipo y flujo de agentes]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[20 §Modelo y esfuerzo por rol]]"
siguiente: "[[20 §Cómo participa el autor]]"
arriba: "[[20 Equipo y flujo de agentes]]"
fuente: "studio/docs/20-equipo-y-flujo-de-agentes.md:90"
generado: true
---

# Cómo se registra el avance ✅

> La fuente de verdad del equipo y las etapas es studio/data/equipo.json. El avance de cada tarea va en su archivo de actividad…

← [[20 §Modelo y esfuerzo por rol]] · [[20 Equipo y flujo de agentes|↑ 20]] · [[20 §Cómo participa el autor]] →

La fuente de verdad del equipo y las etapas es `studio/data/equipo.json`. El avance de cada tarea va en su archivo de actividad `studio/data/tasks/<ID>.json`, en un bloque opcional:

```json
"pipeline": {
  "especialista": "narrador",
  "etapas": [
    {
      "etapa": "analisis", "estado": "hecha", "at": "2026-10-12",
      "nota": "Cruzado con los documentos 08, 17 y 19",
      "entrega": "Informe y criterios de aceptación",
      "hallazgos": [
        { "de": "analista", "texto": "Anselmo aparece en dos actos distintos", "estado": "resuelto",
          "resuelto_por": "narrador", "como": "Se fija en el Acto I y se actualiza el mapa" }
      ]
    },
    { "etapa": "produccion", "estado": "activa" }
  ]
}
```

- Los estados de una etapa son `pendiente`, `activa`, `hecha` y `omitida`.
- `entrega` es lo que esa etapa le pasa a la siguiente. `por` permite indicar un rol distinto del habitual.
- Un **hallazgo** lo deja un rol (`de`) y lo resuelve otro (`resuelto_por`, con `como`); mientras no esté resuelto queda `abierto`. Así se ve qué encontró cada especialista y cómo lo solucionó el que correspondía.
- `traspasos` es el registro cronológico de cada vez que el trabajo pasó de un rol a otro: `{ "de", "a", "que", "at", "tipo" }`, con `tipo` `entrega` (por defecto) o `devolucion`. Si una línea se recorre varias veces, el panel las numera (1.ª, 2.ª pasada…), las cuenta en el plano (×N) y las lista en el historial. Sin registro, se deriva de las etapas hechas.
- Si una tarea no trae `pipeline`, los mods lo infieren del estado del roadmap: `doing` es producción activa, `review` es la revisión del autor, `qa` es la prueba del autor y `done` es todo hecho.
- `build.py` valida el bloque y avisa si una etapa, un estado, un rol o un hallazgo no existen.

Relación con el flujo de [[15 Flujo de trabajo y calidad|15]]: los estados del roadmap (`doing`, `review`, `qa`, `done`) siguen igual; el flujo por etapas detalla lo que pasa dentro de ellos.

## Fuente

`studio/docs/20-equipo-y-flujo-de-agentes.md:90`
