# 15 · Flujo de trabajo y calidad

## Requisito del autor ✅

Trabajar **por ramas**, de forma **muy organizada**, cumpliendo la metodología de **clean code**. Este documento define cómo. El modelo concreto de ramas está marcado 🟡 hasta que lo confirmes ([ADR-0005](adr/0005-ramas-y-commits.md)).

## Modelo de ramas 🟡

**GitHub Flow con ramas de versión.** `main` siempre está sano; todo el trabajo entra por ramas cortas y *pull requests*.

| Rama | Para qué | Vida | Sale de | Entra en |
|---|---|---|---|---|
| `main` | Estado estable y publicable | permanente | — | — |
| `feat/ID-slug` | Funcionalidad nueva | corta | `main` | `main` |
| `fix/ID-slug` | Corrección de un error | corta | `main` | `main` |
| `refactor/ID-slug` | Reorganizar sin cambiar comportamiento | corta | `main` | `main` |
| `test/ID-slug` | Pruebas | corta | `main` | `main` |
| `docs/ID-slug` | Documentación | corta | `main` | `main` |
| `studio/ID-slug` | Roadmap, tareas, hub y arte de referencia | corta | `main` | `main` |
| `chore/ID-slug` | Herramientas, CI y mantenimiento | corta | `main` | `main` |
| `release/X.Y` | Estabilizar una versión antes de publicarla (solo correcciones) | semanas | `main` | `main` + etiqueta |
| `hotfix/X.Y.Z` | Corrección urgente de una versión publicada | horas | etiqueta | `main` + etiqueta |

- **Nombre:** `tipo/ID-descripcion-corta` en minúsculas con guiones, por ejemplo `feat/F2-04-modelo-de-precio`.
- **Una rama, una tarea** (o varias muy pequeñas del mismo hito). Si la rama crece, se divide.
- **Vida corta:** idealmente una sesión de trabajo; se actualiza con `main` antes de abrir el PR.
- **`main` está protegida:** nadie sube directamente; todo entra por PR con la integración continua en verde.
- **Por qué no Git Flow completo:** una rama `develop` añade fusiones y no aporta nada a un proyecto de una persona con integración continua. Si prefieres Git Flow, se cambia con un ADR.

## Commits ✅ / 🟡

Convención **Conventional Commits** en español, con el ID de la tarea:

```
tipo(ámbito): ID descripción breve en imperativo

Cuerpo opcional: qué y por qué (no cómo).

Co-Authored-By: …
```

| Tipo | Uso |
|---|---|
| `feat` | Funcionalidad nueva |
| `fix` | Corrección de un error |
| `refactor` | Cambio interno sin cambiar el comportamiento |
| `perf` | Mejora de rendimiento |
| `test` | Pruebas |
| `docs` | Documentación |
| `studio` | Roadmap, tareas, hub y arte de referencia |
| `chore`, `ci`, `build`, `style`, `revert` | Mantenimiento, integración continua, empaquetado, formato, reversión |

- **Ámbito:** el módulo (`market`, `shop`…) o el área (`ci`, `roadmap`, `hub`).
- Asunto de **hasta 100 caracteres**, sin punto final. Un commit = un cambio con sentido, que compila y pasa las pruebas.
- Se verifica con `tools/ci/check_commits.py`. Un commit sin ID de tarea da aviso.

## Flujo de una tarea ✅

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
8. Con la revisión aprobada, pasa a **`qa`**: se ejecutan los casos de prueba de la tarea, la regresión, y las pruebas de seguridad y rendimiento que apliquen ([16](16-calidad-y-qa.md)).
9. Si QA aprueba, el autor hace el **merge** (squash), borra la rama y la tarea pasa a **`done`** con la referencia del commit y la evidencia de QA.
10. Si QA falla, la tarea vuelve a **`doing`** y el error se registra con su severidad.

Las tareas que no producen comportamiento (documentos, decisiones, estudio) pasan de `review` a `done` y lo dicen en su nota.

El estado de la tarea refleja siempre el de su rama, y queda registrado en el historial con el campo `ref` (rama, PR o commit).

Dentro de estos estados, cada tarea recorre un flujo por etapas con un equipo de especialistas (ideación, análisis, producción, QA técnico, revisión y prueba del autor, y cierre); está descrito en [20](20-equipo-y-flujo-de-agentes.md).

## Pull requests 🟡

- **Pequeños:** idealmente menos de ~400 líneas de cambio.
- **Título** con la misma convención que los commits (se usa al hacer *squash*).
- **Plantilla** con qué, por qué, cómo se probó, evidencias y lista de verificación (`.github/pull_request_template.md`).
- Se **fusionan con squash** para mantener `main` lineal y legible.

### Lista de revisión 🟡

- **Arquitectura:** ¿respeta capas y módulos? ¿pasa el verificador? ¿algo debería estar en otro módulo?
- **Claridad:** nombres, funciones cortas, sin duplicación ni código comentado.
- **Pruebas:** el dominio y los casos de uso nuevos tienen pruebas; los errores corregidos, una prueba que los reproduce.
- **Datos:** el contenido nuevo está en datos validados y no en el código.
- **Textos:** pasan por traducción (ES y EN); nada incrustado en el arte.
- **Seguridad y privacidad:** sin secretos, sin datos personales en telemetría, entradas validadas.
- **Rendimiento:** sin trabajo costoso en cada cuadro; sin asignaciones innecesarias.
- **Accesibilidad:** no depende solo del color; funciona con táctil y con mando.
- **Documentación:** actualizada si cambió el comportamiento o la arquitectura.

## Integración continua ✅

Se ejecuta en cada PR y en cada cambio de `main` (`.github/workflows/ci.yml`):

| Trabajo | Qué hace |
|---|---|
| `studio` | Valida roadmap, tareas, catálogo de QA y registro de errores (`build.py --strict`); el archivo generado `hub/data.js` no se versiona |
| `tools` | Pruebas de las herramientas de verificación |
| `commits` | Convención de mensajes de commit del PR |
| `architecture` | Verificador de arquitectura sobre `game/` |
| `game` | Formato, lint y pruebas de GDScript (se activa cuando exista `project.godot`) |

## Definición de listo y de terminado 🟡

**Lista para empezar (Definition of Ready):** tiene descripción y "listo cuando", prioridad, estimación de hasta 20 horas y no depende de algo sin resolver.

**Terminada (Definition of Done):**

- [ ] Cumple su "listo cuando".
- [ ] Respeta la arquitectura (verificador en verde).
- [ ] Tiene pruebas y pasan.
- [ ] Pasó **QA**: casos de prueba aprobados, sin errores S1 o S2 abiertos, y resultado registrado.
- [ ] Formato y lint sin avisos.
- [ ] Textos en ES y EN; sin cadenas fijas.
- [ ] Documentación y registro de decisiones al día si corresponde.
- [ ] Si toca documentos de diseño: la limpieza no baja, lo que queda sin cerrar está marcado como diferido, con su tarea, y no hay conexiones rotas (hub, «Limpieza del diseño»).
- [ ] Evidencia en la tarea (captura, resultado de pruebas o nota).
- [ ] PR revisado y fusionado.

## Limpieza del diseño ✅

**Requisito del autor:** todo debe quedar **✅ acordado**, sin ambigüedades, y todo debe **conectar y funcionar bien**. Solo puede quedar sin cerrar lo que depende de algo que se verá después, y eso debe quedar **dicho de forma explícita**. Aplica a todo el proyecto, para siempre. No hace falta un 100 % absoluto, pero sí acercarse lo más posible.

**Cómo se mide:**

| Qué | Regla |
|---|---|
| **Limpieza** de un documento | ✅ ÷ (✅ + 🟡 + ❓), en porcentaje. También se calcula para todo el diseño |
| **Diferido** | `⏳ F0-52` marca algo que depende de una tarea posterior. No resta, pero debe nombrar una tarea que exista y que no esté terminada; si la tarea se termina, el punto debe resolverse |
| **Conexión** | Los enlaces entre documentos y las tareas citadas deben existir. Una conexión rota es un error del build |
| **Meta** | 🟡 Como mínimo 90 % por documento (umbral propuesto) y acercarse al 100 % |

**Qué se puede aplazar ✅** (regla del autor, 2026-10-12)

Solo se aplaza un punto abierto (`⏳`) si cumple las dos condiciones:

1. **Una tarea existente lo va a resolver** y se sabe cuál es (`⏳ F0-52`).
2. **Nada que se escriba o construya antes de esa tarea depende de la respuesta.**

Pregunta de control: *«si la respuesta cambia después, ¿hay que rehacer algo ya hecho?»* Si la respuesta es sí, el punto **se decide ahora con el autor, antes de producir**. Si es no, se aplaza con su tarea.

| Se aplaza | No se aplaza |
|---|---|
| Cifras de precios y cuotas (las fija la economía en F0-52) | Quién publica la verdad o si un personaje muere (los finales leen esas banderas) |
| Traducción al inglés de términos (F1-20) | El medidor de un personaje que usarán los umbrales y los epílogos |
| Textos finales y voces de las cintas (F4-151) | Lo que otro documento ya cita como hecho |

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
| **Próximos pasos** | Hilos narrativos y cabos sueltos (F0-51), números base de la economía (F0-52) y simulador de equilibrio (F0-53) |

Es normal que ambos porcentajes empiecen bajos: suben a medida que se cierran las tareas y se profundiza el diseño. La meta es llegar al lanzamiento lo más cerca posible del 100 %.

## Pruebas 🟡

| Nivel | Proporción orientativa | Qué cubre |
|---|---|---|
| Unitarias del dominio | ~70 % | Reglas puras, deterministas, sin Godot de por medio |
| Casos de uso con dobles | ~20 % | Servicios de `application` con puertos falsos |
| Integración y manuales | ~10 % | Varios módulos juntos y sensaciones en el dispositivo |

- Meta de cobertura del dominio: **80 % o más**.
- Las pruebas son parte de cada tarea (están incluidas en sus horas) y su resultado se registra en el catálogo de QA ([16](16-calidad-y-qa.md)).
- Simulaciones largas del mercado (10.000 días) se ejecutan bajo demanda y antes de cada versión.
- Un error corregido incorpora una prueba que lo reproduce.

## Versionado y publicación 🟡

- **SemVer** `MAJOR.MINOR.PATCH` para el juego, con etiquetas `vX.Y.Z` en `main`.
- **`CHANGELOG.md`** en formato *Keep a Changelog*, derivado de los commits.
- Android: `versionCode` que solo crece; `versionName` igual a la versión del juego.
- Se corta `release/X.Y` cuando una versión está completa; allí solo entran correcciones.

## Decisiones de arquitectura (ADR) ✅

Toda decisión que afecte la estructura, una dependencia o un proceso se registra en `studio/docs/adr/NNNN-titulo.md` con contexto, decisión, alternativas y consecuencias. Estados: **Propuesta**, **Aceptada**, **Reemplazada**. Se leen en el hub, sección *Decisiones de arquitectura*.

## Deuda técnica 🟡

- Se registra como tarea de tipo `refactor`, nunca como un `TODO` suelto.
- Cada fase incluye una **revisión de arquitectura y deuda técnica** con horas reservadas.
- Regla del boy scout: se deja el código un poco mejor de como se encontró.

## Seguridad en el flujo ✅

- Ningún secreto, clave de firma ni contraseña en el repositorio (`.gitignore` y revisión).
- Acciones de GitHub fijadas por versión y, más adelante, por hash (tarea F1-35).
- Dependencias pocas, con versión fija y licencia revisada.

## Trabajo con IA ✅

- Cada sesión de trabajo empieza **creando una rama**; Claude no sube directamente a `main` ni fuerza subidas.
- Claude abre cada cambio como rama y deja el PR listo; el autor revisa y fusiona.
- Cada tarea documenta su evidencia y su referencia (`ref`) en el hub.

## Ajustes de GitHub que hace el autor 🟡

En *Settings → Branches → Branch protection rule* para `main`:

- Requerir *pull request* antes de fusionar.
- Requerir que pasen las comprobaciones de la integración continua.
- Requerir historial lineal (squash).
- No permitir subidas forzadas ni borrar la rama.
- En *General*: borrar ramas automáticamente al fusionar.

## QA en el flujo ✅

El QA es una etapa propia, entre la revisión y el cierre. Procedimiento completo, tipos de prueba, seguridad, errores y criterios de salida en [16 · Calidad y QA](16-calidad-y-qa.md).

## Pendiente ❓

- Confirmar el modelo de ramas (ADR-0005) y el QA como etapa (ADR-0008).
- Ejecutar la integración continua por primera vez en GitHub y corregir lo que aparezca.
- Instalar `gdtoolkit` y el marco de pruebas cuando exista el proyecto Godot.
