# Veta de Fortuna · reglas del proyecto para Claude

Estudio de diseño de un juego de gestión minera (Godot 4, pixel art horizontal; PC primero, móvil después). Idioma: español neutro con tuteo. El hub está en `studio/hub` (`python3 studio/hub/build.py --strict`).

## Flujo
- Una tarea = una rama `studio/<ID>-<tema>` = un PR (merge commit). Sesiones por bloques: las tareas pequeñas o del mismo ámbito/archivos (un grupo de la misma fase o del mismo documento) se hacen en una sola sesión, una tras otra, cada una con su rama, su PR y su cierre; solo una tarea grande o densa (muchas decisiones del autor o contexto pesado) tiene sesión propia. Commits `tipo(ámbito): ID descripción`. Nunca hagas `git add` de `.claude/settings.json`.
- Etapas por tarea: ideación, análisis, producción, QA, revisión del autor, prueba, cierre; con subagentes reales (`.claude/agents`, tabla en `studio/data/equipo.json`) y el bloque `pipeline` de `studio/data/tasks/<ID>.json` al día.
- Todo termina en ✅ (decidido por el autor) o ⏳ `<ID de tarea existente y no terminada>`, y solo si nada de lo ya hecho depende de ello; si no, se decide ahora con el autor (preguntas en rondas de máximo 4, con contexto y recomendación).

## Tutorial y onboarding (siempre)
- Todo proceso de primera vez y todo paso obligatorio lleva tutorial guiado y compuerta (sin saltos ni softlock). Cada rol lo contempla en su entregable (regla en el bloque común de `.claude/agents`); QA lo verifica. Inventario de la semana 1: doc 27 «Tutoriales y compuertas».

## Modelo y esfuerzo de los subagentes (ahorro de tokens)
- Al lanzar un subagente con la herramienta `Agent`, fija `model` y `effort` según `studio/data/equipo.json` (`roles[].modelo` y `roles[].esfuerzo`; el rol se busca por su campo `agente`). Si cambias alguno para una tarea, justifícalo en una línea en el encargo.
- Fable 5.1 (`fable`) nunca se usa por defecto: requiere la autorización del autor (el mod `vf-equipo` pide la confirmación). Si no estás seguro, usa el siguiente modelo más barato y avisa.
- Tareas mecánicas, listados y comprobaciones: `haiku` o esfuerzo `low`; análisis y diseño: `sonnet` medio; decisiones de arquitectura o ideación: `opus` alto.

## Encargos y informes cortos
- Encargo mínimo: si es largo, escríbelo en un archivo del scratchpad y pasa solo la ruta y lo que cambia; no pegues documentos ni repitas lo que el agente puede leer.
- Informe de agente (máx. 60 líneas / 6.000 caracteres): Resultado, Archivos tocados, Hallazgos en tabla `archivo:línea`, Dudas para el autor. Sin repetir el encargo.
- Lanza en lote los agentes independientes y procesa sus informes juntos; no abras un turno por cada informe.
- Un agente = un entregable y unos 60 turnos como máximo; si la tarea es mayor, divídela. Divide también si el informe pasaría de 6.000 caracteres o si mezcla entregables (doc 15, «Ajustes finos»).

## Lectura parcial
- No leas documentos enteros si basta una sección: `grep -n`, rangos (`offset`/`limit`) y `tools/consulta.py` (`limpieza`, `abiertos`, `indice`, `seccion`, `ficha`, `tarea`/`tareas`, `mundo`; sin argumentos muestra la ayuda).
- Nunca leas `studio/hub/data.js` (generado, 1,6 MB) ni `studio/data/sim/resultados.json` enteros. Los documentos 18, 21, 23, 25, 27 y 28 son grandes: lee por secciones.
- Cada lectura grande se paga en cada turno posterior: léela una vez y trabaja con notas.

## Sesión
- Al fusionar el PR de una tarea la sesión continúa con la tarea siguiente del bloque; al terminar el bloque (o si el contexto pasa de ~200 k tokens) cierra la sesión o compacta (`/compact`); evita seguir con contextos de más de 200 k tokens y los reposos largos con contexto grande (la caché caduca a los 5 minutos y se reescribe entera).
- `/consumo`: gasto por rol, modelo y día.
- Registro de sesiones: antes de buscar en documentos algo «hecho en otra sesión», usa `python3 tools/sesion.py buscar <tarea, PR o texto>` y `ver N` (`studio/SESIONES.md` lo resume). Al cerrar una tarea, anota la sesión con `python3 tools/sesion.py resumen N "qué hizo" --tareas … --pr … --docs … --decisiones "a|b"` en el mismo PR.
- **Renombrar o modificar una sesión:** lo hace siempre la sesión que la inició (la anterior), porque conoce su id; la sesión hija no usa `set_session_title` (no conoce su propio id) sino que le pide el cambio con `SendMessage` a esa sesión anterior. Regla del autor (2026-10-25), válida para cualquier modificación de la sesión actual.
- **Cambio de sesión (siempre avisado):** cuando recomiendes cerrar o compactar la sesión, dilo de forma explícita, entrega el prompt de la sesión nueva en un bloque y ábrela con `spawn_task` (un clic). Cada sesión lleva número y nombre claro: `python3 tools/sesion.py nueva "<bloque o tema> (<IDs>)"` la registra en `studio/data/sesiones.json` y devuelve el título `S-NN · <bloque o tema> (<IDs>)`; úsalo como título del chip y, al empezar, como título de la sesión (`set_session_title`).

## Medidas de calidad del diseño
- Limpieza por documento ≥ 90 % (meta 100 %: 0 🟡 y 0 ❓); coherencia con 0 hallazgos; hilos sin problemas; simulador «50 de 50 · vigente». Si cambias una cifra de `studio/data/world.json` o del documento 28, reejecuta `python3 tools/sim/run.py --completo --escribir`.
- Imágenes: solo el coordinador las genera y siempre dice antes el número y el costo.
