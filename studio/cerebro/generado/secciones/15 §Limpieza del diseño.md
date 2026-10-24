---
id: "doc-15-limpieza-del-diseno"
tipo: "seccion"
title: "Limpieza del diseño ✅"
aliases: ["doc-15-limpieza-del-diseno"]
documento: "[[15 Flujo de trabajo y calidad]]"
limpieza: 50
abiertos: 6
espera: 0
aplazado_a: ["[[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y]]"]
estado: "con-abiertos"
anterior: "[[15 §Definición de listo y de terminado]]"
siguiente: "[[15 §Pruebas]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:129"
generado: true
---

# Limpieza del diseño ✅

> Requisito del autor: todo debe quedar acordado, sin ambigüedades, y todo debe conectar y funcionar bien. Solo puede quedar sin cerrar lo…

← [[15 §Definición de listo y de terminado]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Pruebas]] →

**Requisito del autor:** todo debe quedar **✅ acordado**, sin ambigüedades, y todo debe **conectar y funcionar bien**. Solo puede quedar sin cerrar lo que depende de algo que se verá después, y eso debe quedar **dicho de forma explícita**. Aplica a todo el proyecto, para siempre. No hace falta un 100 % absoluto, pero sí acercarse lo más posible.

**Cómo se mide:**

| Qué | Regla |
|---|---|
| **Limpieza** de un documento | ✅ ÷ (✅ + 🟡 + ❓), en porcentaje. También se calcula para todo el diseño |
| **Diferido** | `⏳ F2-04` marca algo que depende de una tarea posterior. No resta, pero debe nombrar una tarea que exista y que no esté terminada; si la tarea se termina, el punto debe resolverse |
| **Conexión** | Los enlaces entre documentos y las tareas citadas deben existir. Una conexión rota es un error del build |
| **Meta** | 🟡 Como mínimo 90 % por documento (umbral propuesto) y acercarse al 100 % |

**Qué se puede aplazar ✅** (regla del autor, 2026-10-12)

Solo se aplaza un punto abierto (`⏳`) si cumple las dos condiciones:

1. **Una tarea existente lo va a resolver** y se sabe cuál es (`⏳ F2-04`).
2. **Nada que se escriba o construya antes de esa tarea depende de la respuesta.**

Pregunta de control: *«si la respuesta cambia después, ¿hay que rehacer algo ya hecho?»* Si la respuesta es sí, el punto **se decide ahora con el autor, antes de producir**. Si es no, se aplaza con su tarea.

| Se aplaza | No se aplaza |
|---|---|
| Fórmulas del modelo de precios (las construye [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y\|F2-04]]) | Quién publica la verdad o si un personaje muere (los finales leen esas banderas) |
| Traducción al inglés de términos ([[F1-20 Flujo de traducción - extracción, traducción asistida por\|F1-20]]) | El medidor de un personaje que usarán los umbrales y los epílogos |
| Textos finales y voces de las cintas ([[F4-151 Ocho cintas - guion y sonido\|F4-151]]) | Lo que otro documento ya cita como hecho |

Cada aplazamiento queda justificado en el informe del analista y lo comprueba QA.

**Cómo se atiende:**

1. Un documento nuevo no se da por terminado mientras tenga puntos 🟡 o ❓ que se puedan decidir ya. Lo que no se puede decidir todavía se marca como diferido, con la tarea de la que depende.
2. Los puntos abiertos se cierran en **pasadas de cierre por documento**: se presentan al autor, se decide, y se convierten en ✅. Cada pasada tiene su tarea en el roadmap.
3. El panel **Limpieza del diseño** del hub muestra el porcentaje de cada documento, la lista de puntos por cerrar y las conexiones rotas. `python3 studio/hub/build.py --strict` informa el resumen y falla si hay conexiones rotas.
4. 🟡 Más adelante la integración continua impedirá que la limpieza de un documento baje respecto de `main`.

**Coherencia ✅:** además de decidido, el diseño debe ser **coherente**: sin cabos sueltos en la historia, sin contradicciones entre documentos y sin números que rompan la economía. Es una segunda medida, independiente de la limpieza:

| Qué | Cómo |
|---|---|
| **Registro del mundo** | `studio/data/world.json` es la fuente de verdad de minerales, zonas, minijuegos, mecánicas, recetas, facciones y personajes |
| **Integridad** | Lo que el registro referencia debe existir. Un error hace fallar el build |
| **Comprobaciones de coherencia** | Reglas del diseño, mapa de historia y números base se contrastan con el registro. Cada incumplimiento es un hallazgo: baja el porcentaje, no falla el build, y se resuelve decidiendo o corrigiendo |
| **Dónde se ve** | Hub, «Coherencia del diseño» |
| **Próximos pasos** | Hilos narrativos y cabos sueltos ([[F0-51 Registro de hilos narrativos y cabos sueltos\|F0-51]]), números base de la economía (ya acordados) y simulador de equilibrio ([[F0-53 Simulador de economía y progresión con reglas de equilibrio\|F0-53]]) |

Es normal que ambos porcentajes empiecen bajos: suben a medida que se cierran las tareas y se profundiza el diseño. La meta es llegar al lanzamiento lo más cerca posible del 100 %.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:129`
