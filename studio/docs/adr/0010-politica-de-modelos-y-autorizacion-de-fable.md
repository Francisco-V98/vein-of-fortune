# ADR-0010 · Política de modelos por rol y autorización de Fable 5.1

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-23

## Contexto

El consumo de tokens del estudio crecía más rápido que el trabajo hecho. Los datos medidos con el mod `vf-consumo`:

- El **contexto mediano** de una sesión era de **436 k tokens**, y se relee completo en cada turno.
- El **56 %** de los tokens frescos se gastaba en **subagentes**.
- Los informes de los agentes llegaban a **43 k caracteres**, que luego se pagaban en cada turno del coordinador.
- Hubo **335 lecturas completas** de documentos, cuando casi siempre bastaba una sección.

Además, todos los agentes usaban el mismo modelo y esfuerzo sin importar la tarea, y el modelo más caro (Fable 5.1) podía usarse sin que el autor lo supiera.

## Decisión ✅

Decisiones del autor (2026-10-23):

1. **Tabla por rol:** `studio/data/equipo.json` fija el modelo y el esfuerzo por defecto de cada agente (tabla en [20](../20-equipo-y-flujo-de-agentes.md)). Opus con esfuerzo alto para ideación y arquitectura; Sonnet para el resto; esfuerzo bajo para QA, localización y diseño de pruebas.
2. **Ajuste por tarea:** el coordinador puede subir o bajar el modelo o el esfuerzo en una tarea, con el motivo en una línea.
3. **Fable 5.1 solo con autorización del autor:** el mod `vf-equipo` abre un diálogo en `/equipo` con las opciones «aprobar para esta tarea», Opus, Sonnet, Haiku u otro. La aprobación vale para una tarea.
4. **Modo conciso:** agentes y encargos siguen la skill `modo-conciso`: encargo mínimo, informe de máximo 60 líneas o 6.000 caracteres, lectura parcial, lotes y cierre de sesión al fusionar (reglas en `CLAUDE.md` y [15](../15-flujo-de-trabajo-y-calidad.md#coste-de-la-ia-)).

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| **Un solo modelo para todos los agentes** (la situación anterior) | Paga modelos caros en tareas mecánicas como QA o listados |
| **Fable 5.1 por defecto en los roles críticos** | El autor no quiere el modelo más caro sin su autorización expresa |
| **Elegir el modelo caso por caso sin tabla** | Depende de que el coordinador lo recuerde; la tabla lo hace repetible y auditable |
| **Solo pedir informes cortos, sin cambiar modelos** | Ataca el contexto pero no el 56 % que gastan los subagentes |
| **Bloquear Fable del todo** | Perdería la opción de usarlo en una decisión que lo justifique |

## Consecuencias

- El coordinador debe fijar `model` y `effort` en cada llamada a `Agent`; el hook de `vf-equipo` sobre `Agent` reescribe la llamada con los valores del rol y pide la autorización de Fable, sin modificar archivos.
- Se añade el campo `politica_modelos` y los campos `modelo` y `esfuerzo` en `equipo.json`; el hub los valida.
- Las tareas de seguimiento son ✅ F0-88 (`tools/consulta.py`, consulta del estudio sin leer documentos enteros) y ⏳ F0-89 (ajustes finos y `/consumo` por rol, con la medición antes y después).
- Riesgo: un modelo más barato puede dar peor calidad en un rol concreto; se corrige subiéndolo en la tabla o en la tarea.

## Verificación

- `python3 studio/hub/build.py --strict` valida la tabla.
- `/consumo` muestra el gasto por modelo, ventana y día; la reducción de los cuatro datos del contexto se compara en ⏳ F0-89 con tareas comparables.
