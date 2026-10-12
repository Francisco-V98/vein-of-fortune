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

## El equipo ✅

El autor pidió analizar qué empleados necesita de verdad el proyecto. Salen **21 roles en 7 departamentos** (19 agentes, el autor y el coordinador), pensados a partir de las fases del roadmap: diseño y mundo (F0), preparación técnica (F1), prototipo y vertical slice (F2 y F3), contenido (F4), pulido y lanzamiento (F5) y evolutivo (F6). Cada rol se **incorpora en su fase**; antes de eso queda en reserva.

| Departamento | Rol | Tipo | Se une en | Hace |
|---|---|---|---|---|
| Dirección | **Coordinador (Claude)** | Principal | F0 | Reparte el trabajo entre los especialistas, mantiene el roadmap, genera las imágenes, fusiona y cierra las tareas. |
| Dirección | **Francisco (autor)** | Humano | F0 | Revisa los entregables y los PR, juega y prueba el juego (diversión, detalles visuales, tono), y aprueba o devuelve. |
| Estrategia y análisis | **Ideador e investigador** | Agente (`ideador`) | F0 | Explora opciones y referencias (juegos parecidos, mercado) y propone al menos tres alternativas con una recomendación. |
| Estrategia y análisis | **Analista de coherencia** | Agente (`analista`) | F0 | Cruza lo propuesto con los documentos y el registro del mundo; revisa números, riesgos y dependencias; fija los criterios de aceptación. |
| Estrategia y análisis | **Asesor legal y de licencias** | Agente (`asesor-legal`) | F0 | Vigila la licencia de cada fuente, imagen y sonido, la privacidad, las reglas de las tiendas y la clasificación por edades. |
| Estrategia y análisis | **Responsable de lanzamiento** | Agente (`responsable-lanzamiento`) | F5 | Prepara la ficha de tienda, el kit de prensa, las capturas, la comunidad y las métricas en producción. |
| Diseño | **Diseñador de sistemas** | Agente (`disenador-sistemas`) | F0 | Escribe y edita el diseño del juego: bucle central, progresión, riesgo y el registro del mundo. |
| Diseño | **Economista y balance** | Agente (`economista`) | F0 | Modela precios, demanda, mercado y recompensas, y comprueba con simulaciones que la economía no se rompa. |
| Diseño | **Diseñador de contenido** | Agente (`disenador-contenido`) | F0 | Diseña zonas, minerales, eventos, empleados y encuentros con sus parámetros. |
| Diseño | **Diseñador UI/UX** | Agente (`disenador-ui-ux`) | F0 | Diseña pantallas, flujos, información por capas y accesibilidad para móvil. |
| Narrativa y lenguaje | **Narrador** | Agente (`narrador`) | F0 | Escribe la historia, los personajes y los diálogos con la voz acordada, sin romper el canon. |
| Narrativa y lenguaje | **Localizador ES/EN** | Agente (`localizador`) | F0 | Mantiene el glosario y adapta los textos entre español neutro con tuteo e inglés cercano. |
| Arte y sonido | **Director de arte** | Agente (`director-arte`) | F0 | Escribe los encargos de arte y revisa cada imagen contra el estilo acordado. |
| Arte y sonido | **Diseñador de sonido** | Agente (`disenador-sonido`) | F1 | Planifica efectos, voces en blips y música, y su licencia. |
| Ingeniería | **Arquitecto de software** | Agente (`arquitecto`) | F0 | Define módulos, capas, datos y decisiones de arquitectura (ADR) y vigila la deuda técnica. |
| Ingeniería | **Desarrollador de juego** | Agente (`desarrollador-juego`) | F1 | Programa el juego en Godot con código limpio, modular y probado. |
| Ingeniería | **Desarrollador de herramientas** | Agente (`desarrollador-herramientas`) | F0 | Mantiene el hub, la integración continua y los mods del estudio. |
| Ingeniería | **Ingeniero de seguridad** | Agente (`ingeniero-seguridad`) | F1 | Revisa la seguridad, la integridad de los datos guardados y la privacidad. |
| Calidad | **Revisor de código** | Agente (`revisor-codigo`) | F1 | Revisa cada cambio de código antes de que llegue al autor: errores, claridad y arquitectura. |
| Calidad | **QA técnico** | Agente (`qa`) | F0 | Ejecuta el build estricto, las pruebas y las comprobaciones, y reporta sin editar nada. |
| Calidad | **Diseñador de pruebas** | Agente (`disenador-pruebas`) | F0 | Prepara los casos de prueba y las guías de playtest para que el autor pruebe con método. |

Cada agente tiene su definición en `.claude/agents/<agente>.md`, con las herramientas que puede usar y las reglas del proyecto que cumple. Los que solo revisan (analista, QA, revisor de código, seguridad) no editan archivos. El generador de imágenes lo usa solo el coordinador, para controlar los créditos; el director de arte escribe el encargo y revisa el resultado.

**Por qué estos y no menos:** economía, localización, UI/UX, sonido, legal, seguridad, revisión de código y diseño de pruebas aparecen como tareas propias en el roadmap (balance económico, localización ES/EN, flujo de pantallas, sonido y música, legal y tienda, QA y seguridad, tutorial y accesibilidad, lanzamiento). Juntarlos en un solo «diseñador» o «desarrollador» haría que nadie los vigilara.

## Cómo se registra el avance ✅

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

Relación con el flujo de [15](15-flujo-de-trabajo-y-calidad.md): los estados del roadmap (`doing`, `review`, `qa`, `done`) siguen igual; el flujo por etapas detalla lo que pasa dentro de ellos.

## Cómo participa el autor ✅

Las etapas «Revisión del autor» y «Prueba del autor» son tuyas. En el panel `/equipo`, la bandeja **Te toca a ti** muestra, con su etiqueta, lo que tienes pendiente: **Revisar entregable**, **Revisar PR** (con el enlace) o **Probar el juego**. Cada acción sigue el mismo recorrido:

1. Haces tu revisión o tu prueba.
2. Dices cómo salió: **Todo bien** o **Salieron ajustes**. Si hay ajustes, me los comentas por el chat.
3. Pulsas **Terminé mi parte**. El panel envía un mensaje a la conversación y la acción queda como enviada.
4. El coordinador decide: si todo se aprobó, la tarea sigue su flujo; si hubo ajustes, los asigna al especialista que corresponda, el trabajo vuelve a la etapa que toque y, al terminar, vuelve a tu bandeja.

El panel **se actualiza solo**: mira los datos cada pocos segundos, los PR cada rato y también al terminar cada turno. Tu personaje en la oficina se llama **Fran**: lleva la etiqueta «TÚ» y una estrella en la placa. Todo el detalle se abre **con un clic**, sin depender del ratón: en la pestaña Oficina, los botones de Personas, Traspasos y Hallazgos abren una tarjeta con la información (qué hace cada uno, qué pasó de quién a quién y en qué pasada), resaltan en el plano lo que implica y se cierran con la ✕.

## Los mods de Claude Code ✅

Dos mods del repositorio, en `tools/mods/` (un marketplace local llamado `vein-mods`):

| Mod | Comando | Qué muestra |
|---|---|---|
| `vf-estado` | `/estado` | Avance del roadmap por fase, hito y estado; limpieza y coherencia del diseño; tareas en curso; rama y PR abiertos |
| `vf-equipo` | `/equipo` | **Oficina:** el estudio en planta, con cada empleado en su escritorio (trabajando, libre o en reserva), paquetes que viajan entre ellos y banderas con los hallazgos, más la bandeja «Te toca a ti» con los botones del autor. **Traspasos:** el detalle de cada tarea. **Equipo:** todos los roles por departamento |

- Los botones del autor envían un mensaje como si lo escribiera él, solo cuando los pulsa; los mods **no modifican archivos** por su cuenta.
- Un mod corre con los mismos permisos del usuario y sin aislamiento. Por eso solo se instalan los de este repositorio, tras revisar el código. Cada uno se valida con `claude plugin validate` y se prueba con `claude plugin test`.
- Instalación y uso en `tools/mods/README.md`.

## Pendiente

- ❓ Confirmar con el autor las etapas y los roles propuestos 🟡 y si falta algún especialista (por ejemplo, de economía o de sonido).
- ⏳ F0-74 Mostrar el flujo de cada tarea en la vista de tarea del hub.
