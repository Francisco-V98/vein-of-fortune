# 20 · Equipo y flujo de agentes

## Requisito del autor ✅

Tener un **equipo de especialistas** (ideador, analista, diseñador, desarrollador, QA y los que convengan) y poder **ver cómo cada uno le pasa el trabajo al siguiente** hasta que la tarea queda cerrada, sin cabos sueltos. Según la tarea, algunos especialistas no actúan. El **autor también está en el flujo**: revisa los entregables y juega y prueba el juego (diversión, detalles visuales, tono).

## Etapas del flujo 🟡

Toda tarea recorre estas etapas en orden. Las que no hacen falta se marcan **omitidas**; nunca se borran.

| # | Etapa | Quién | Qué entrega |
|---|---|---|---|
| 1 | **Ideación** | Ideador | Tres o más opciones con ventajas y riesgos, y una recomendación |
| 2 | **Análisis** | Analista | Informe de coherencia, riesgos, dependencias y criterios de aceptación |
| 3 | **Producción** | El especialista que toque: diseñador de sistemas, narrador, director de arte o desarrollador | El trabajo en sí: documento, texto, arte o código |
| 4 | **QA técnico** | QA | Informe aprobado o con fallos: build estricto, pruebas, enlaces, coherencia |
| 5 | **Revisión del autor** | Francisco | Aprobación o devolución con comentarios |
| 6 | **Prueba del autor** | Francisco | Jugar y probar: que sea divertido, que se vea bien, que el tono funcione. Se omite si aún no hay nada que probar |
| 7 | **Cierre** | Coordinador (Claude) | Fusión, tarea cerrada, ramas limpias y registro al día |

Reglas ✅ del flujo, en `studio/data/equipo.json`:
- Una etapa pasa a **hecha** solo cuando entrega lo que dice su rol; la siguiente no empieza antes.
- Si el autor devuelve una tarea, vuelve a **Producción** con el comentario.
- Nada cierra sin QA técnico aprobado, salvo tareas de solo decisión, que pasan directo a la revisión del autor.

## El equipo 🟡

| Rol | Tipo | Agente | Hace |
|---|---|---|---|
| Ideador | Agente | `ideador` | Explora opciones y recomienda; no edita archivos |
| Analista | Agente | `analista` | Cruza con documentos y registro del mundo; revisa números y riesgos; fija criterios; no edita |
| Diseñador de sistemas | Agente | `disenador-sistemas` | Documentos de diseño, economía y registro del mundo |
| Narrador | Agente | `narrador` | Historia, personajes, diálogos y biblia narrativa, respetando el canon |
| Director de arte | Agente | `director-arte` | Encargos de arte y revisión contra el estilo; no genera imágenes ni gasta créditos |
| Desarrollador | Agente | `desarrollador` | Hub, herramientas y, más adelante, el juego, con código limpio y pruebas |
| QA | Agente | `qa` | Ejecuta las comprobaciones y reporta; no edita |
| Francisco (autor) | Humano | — | Revisa, juega, prueba, aprueba o devuelve |
| Coordinador | Principal | — | Claude: reparte el trabajo, mantiene el roadmap, fusiona y cierra |

Cada agente tiene su definición en `.claude/agents/<agente>.md`, con las herramientas que puede usar y las reglas del proyecto que cumple. El generador de imágenes lo usa solo el coordinador, para controlar los créditos.

## Cómo se registra el avance ✅

La fuente de verdad del equipo y las etapas es `studio/data/equipo.json`. El avance de cada tarea va en su archivo de actividad `studio/data/tasks/<ID>.json`, en un bloque opcional:

```json
"pipeline": {
  "especialista": "narrador",
  "etapas": [
    { "etapa": "ideacion", "estado": "hecha", "at": "2026-10-12", "nota": "Tres opciones" },
    { "etapa": "analisis", "estado": "activa" }
  ]
}
```

Los estados de una etapa son `pendiente`, `activa`, `hecha` y `omitida`. Si una tarea no trae `pipeline`, los mods lo infieren del estado del roadmap: `doing` es producción activa, `review` es la revisión del autor, `qa` es la prueba del autor y `done` es todo hecho. `build.py` valida el bloque y avisa si una etapa, un estado o un especialista no existen.

Relación con el flujo de [15](15-flujo-de-trabajo-y-calidad.md): los estados del roadmap (`doing`, `review`, `qa`, `done`) siguen igual; el flujo por etapas detalla lo que pasa dentro de ellos.

## Los mods de Claude Code ✅

Dos mods del repositorio, en `tools/mods/` (un marketplace local llamado `vein-mods`):

| Mod | Comando | Qué muestra |
|---|---|---|
| `vf-estado` | `/estado` | Avance del roadmap por fase, hito y estado; limpieza y coherencia del diseño; tareas en curso; rama y PR abiertos |
| `vf-equipo` | `/equipo` | El flujo por etapas con cuántas tareas hay en cada una, quién trabaja ahora, el equipo y el detalle de cada tarea, con los botones del autor para aprobar o devolver |

- Los botones del autor envían un mensaje como si lo escribiera él; los mods **no modifican archivos** por su cuenta.
- Un mod corre con los mismos permisos del usuario y sin aislamiento. Por eso solo se instalan los de este repositorio, tras revisar el código. Cada uno se valida con `claude plugin validate` y se prueba con `claude plugin test`.
- Instalación y uso en `tools/mods/README.md`.

## Pendiente

- ❓ Confirmar con el autor las etapas y los roles propuestos 🟡 y si falta algún especialista (por ejemplo, de economía o de sonido).
- ⏳ F0-74 Mostrar el flujo de cada tarea en la vista de tarea del hub.
