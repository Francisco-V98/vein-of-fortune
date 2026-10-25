# 15 · Flujo de trabajo y calidad

## Requisito del autor ✅

Trabajar **por ramas**, de forma **muy organizada**, cumpliendo la metodología de **clean code**. Este documento define cómo. El modelo de ramas está confirmado ([ADR-0005](adr/0005-ramas-y-commits.md), enmendado el 2026-10-25 a *merge commit*).

## Modelo de ramas ✅

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

## Commits ✅

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
- Se verifica con `tools/ci/check_commits.py`. **El ID de la tarea es obligatorio:** un commit sin él es un error de la integración continua (decisión del autor, 2026-10-25). Los commits de fusión («Merge …») y de reversión quedan exentos, y solo se revisa el rango del PR, no la historia anterior de `main`.

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
9. Si QA aprueba, el autor hace el **merge** (merge commit), borra la rama y la tarea pasa a **`done`** con la referencia del commit y la evidencia de QA.
10. Si QA falla, la tarea vuelve a **`doing`** y el error se registra con su severidad.

Las tareas que no producen comportamiento (documentos, decisiones, estudio) pasan de `review` a `done` y lo dicen en su nota.

El estado de la tarea refleja siempre el de su rama, y queda registrado en el historial con el campo `ref` (rama, PR o commit).

Dentro de estos estados, cada tarea recorre un flujo por etapas con un equipo de especialistas (ideación, análisis, producción, QA técnico, revisión y prueba del autor, y cierre); está descrito en [20](20-equipo-y-flujo-de-agentes.md).

## Pull requests ✅

- **Pequeños:** idealmente menos de ~400 líneas de cambio. Es una guía, no bloquea el PR (práctica habitual: los PR de menos de 400 líneas se revisan mejor); si se pasa, el PR explica por qué no se divide.
- **Título** con la misma convención que los commits (el CI lo verifica en cada commit del PR).
- **Plantilla** con qué, por qué, cómo se probó, evidencias y lista de verificación (`.github/pull_request_template.md`).
- Se **fusionan con merge commit** (no squash ni rebase): conserva la rama `studio/<ID>-tema` y los commits `tipo(ámbito): ID descripción`, que el CI valida. Decisión del autor en F0-35: no se exige historial lineal.

### Lista de revisión ✅

- **Arquitectura:** ¿respeta capas y módulos? ¿pasa el verificador? ¿algo debería estar en otro módulo?
- **Claridad:** nombres, funciones cortas, sin duplicación ni código comentado.
- **Pruebas:** el dominio y los casos de uso nuevos tienen pruebas; los errores corregidos, una prueba que los reproduce.
- **Datos:** el contenido nuevo está en datos validados y no en el código.
- **Textos:** pasan por traducción (ES y EN); nada incrustado en el arte.
- **Seguridad y privacidad:** sin secretos, sin datos personales en telemetría, entradas validadas.
- **Rendimiento:** sin trabajo costoso en cada cuadro; sin asignaciones innecesarias.
- **Accesibilidad:** no depende solo del color; funciona con ratón y teclado y con mando (el táctil, en la fase móvil).
- **Tutorial y compuerta:** si el cambio introduce algo de primera vez u obligatorio, trae su tutorial guiado y su compuerta, sin saltos ni softlock ([ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md), [27](27-guion-del-acto-i.md)).
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

## Definición de listo y de terminado ✅

**Lista para empezar (Definition of Ready):** tiene descripción y "listo cuando", prioridad, estimación de hasta 20 horas (hoy ninguna tarea del roadmap la supera) y no depende de algo sin resolver.

**Terminada (Definition of Done):**

- [ ] Cumple su "listo cuando".
- [ ] Respeta la arquitectura (verificador en verde).
- [ ] Tiene pruebas y pasan.
- [ ] Pasó **QA**: casos de prueba aprobados, sin errores S1 o S2 abiertos, y resultado registrado.
- [ ] Formato y lint sin avisos.
- [ ] Textos en ES y EN; sin cadenas fijas.
- [ ] Documentación y registro de decisiones al día si corresponde.
- [ ] Si toca algo de primera vez para el jugador u obligatorio para avanzar: tiene tutorial guiado y compuerta, sin saltos ni softlock ([ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md)); QA lo verifica ([16](16-calidad-y-qa.md)).
- [ ] Si toca documentos de diseño: la limpieza no baja respecto de `main` (se comprueba a mano con el panel del hub hasta que exista ⏳ F1-47), lo que queda sin cerrar está marcado como diferido, con su tarea, y no hay conexiones rotas (hub, «Limpieza del diseño»).
- [ ] Si crea imágenes o audio de prueba: van marcados como provisionales en `studio/data/assets.json` (campo `estado`) y no se pulen ([12](12-direccion-de-arte.md)).
- [ ] Evidencia en la tarea (captura, resultado de pruebas o nota).
- [ ] PR revisado y fusionado.

## Limpieza del diseño ✅

**Requisito del autor:** todo debe quedar **✅ acordado**, sin ambigüedades, y todo debe **conectar y funcionar bien**. Solo puede quedar sin cerrar lo que depende de algo que se verá después, y eso debe quedar **dicho de forma explícita**. Aplica a todo el proyecto, para siempre. No hace falta un 100 % absoluto, pero sí acercarse lo más posible.

**Cómo se mide:**

| Qué | Regla |
|---|---|
| **Limpieza** de un documento | puntos cerrados ÷ puntos totales (cerrados más abiertos y dudas), en porcentaje. También se calcula para todo el diseño |
| **Diferido** | `⏳ F2-04` marca algo que depende de una tarea posterior. No resta, pero debe nombrar una tarea que exista y que no esté terminada; si la tarea se termina, el punto debe resolverse |
| **Conexión** | Los enlaces entre documentos y las tareas citadas deben existir. Una conexión rota es un error del build |
| **Meta** ✅ | Mínimo 90 % por documento; meta 100 %. Meta de la fase F0 (decisión del autor, 2026-10-25): ningún punto abierto en ningún documento; las dudas solo se admiten con un diferido válido y con el mínimo del 90 % |

**Qué se puede aplazar ✅** (regla del autor, 2026-10-12)

Solo se aplaza un punto abierto (`⏳`) si cumple las dos condiciones:

1. **Una tarea existente lo va a resolver** y se sabe cuál es (`⏳ F2-04`).
2. **Nada que se escriba o construya antes de esa tarea depende de la respuesta.**

Pregunta de control: *«si la respuesta cambia después, ¿hay que rehacer algo ya hecho?»* Si la respuesta es sí, el punto **se decide ahora con el autor, antes de producir**. Si es no, se aplaza con su tarea.

| Se aplaza | No se aplaza |
|---|---|
| Fórmulas del modelo de precios (las construye F2-04) | Quién publica la verdad o si un personaje muere (los finales leen esas banderas) |
| Traducción al inglés de términos (F1-20) | El medidor de un personaje que usarán los umbrales y los epílogos |
| Textos finales y voces de las cintas (F4-151) | Lo que otro documento ya cita como hecho |

Cada aplazamiento queda justificado en el informe del analista y lo comprueba QA.

**Cómo se atiende:**

1. Un documento nuevo no se da por terminado mientras tenga puntos abiertos o dudas que se puedan decidir ya. Lo que no se puede decidir todavía se marca como diferido, con la tarea de la que depende.
2. Los puntos abiertos se cierran en **pasadas de cierre por documento**: se presentan al autor, se decide, y se convierten en ✅. Cada pasada tiene su tarea en el roadmap.
3. El panel **Limpieza del diseño** del hub muestra el porcentaje de cada documento, la lista de puntos por cerrar y las conexiones rotas. `python3 studio/hub/build.py --strict` informa el resumen y falla si hay conexiones rotas.
4. ⏳ F1-47: la integración continua impedirá que la limpieza de un documento baje respecto de `main`. Mientras tanto la regla es manual y está en la definición de terminado.

**Coherencia ✅:** además de decidido, el diseño debe ser **coherente**: sin cabos sueltos en la historia, sin contradicciones entre documentos y sin números que rompan la economía. Es una segunda medida, independiente de la limpieza:

| Qué | Cómo |
|---|---|
| **Registro del mundo** | `studio/data/world.json` es la fuente de verdad de minerales, zonas, minijuegos, mecánicas, recetas, facciones y personajes |
| **Integridad** | Lo que el registro referencia debe existir. Un error hace fallar el build |
| **Comprobaciones de coherencia** | Reglas del diseño, mapa de historia y números base se contrastan con el registro. Cada incumplimiento es un hallazgo: baja el porcentaje, no falla el build, y se resuelve decidiendo o corrigiendo |
| **Dónde se ve** | Hub, «Coherencia del diseño» |
| **Próximos pasos** | Hilos narrativos y cabos sueltos (F0-51), números base de la economía (ya acordados) y simulador de equilibrio (F0-53) |

Es normal que ambos porcentajes empiecen bajos: suben a medida que se cierran las tareas y se profundiza el diseño. La meta es llegar al lanzamiento lo más cerca posible del 100 %.

## Pruebas ✅

| Nivel | Proporción orientativa | Qué cubre |
|---|---|---|
| Unitarias del dominio | ~70 % | Reglas puras, deterministas, sin Godot de por medio |
| Casos de uso con dobles | ~20 % | Servicios de `application` con puertos falsos |
| Integración y manuales | ~10 % | Varios módulos juntos y sensaciones en el dispositivo |

- Las proporciones son una guía (pirámide de pruebas), no una cuota.
- Meta de cobertura del dominio: **80 % o más**, exigible solo desde la F2 (decisión del autor, 2026-10-25); antes no hay código de dominio que medir. Se mide con GUT desde ⏳ F1-33.
- Las pruebas son parte de cada tarea (están incluidas en sus horas) y su resultado se registra en el catálogo de QA ([16](16-calidad-y-qa.md)).
- Simulaciones largas del mercado (10.000 días) se ejecutan bajo demanda y antes de cada versión.
- Un error corregido incorpora una prueba que lo reproduce.

## Versionado y publicación ✅

- **SemVer** `MAJOR.MINOR.PATCH` para el juego, con etiquetas `vX.Y.Z` en `main`.
- **`CHANGELOG.md`** en formato *Keep a Changelog*, derivado de los commits.
- Steam: la versión del juego (`vX.Y.Z`) se registra en cada build subida. Fase móvil (después de la 1.0): en Android, `versionCode` que solo crece y `versionName` igual a la versión del juego ([10](10-tecnico-y-herramientas.md)).
- **Antes de la 1.0** las versiones son `0.x.y` (prototipo, vertical slice y contenido); `1.0.0` es el lanzamiento en Steam. Las builds de Steam salen a la rama `beta` para probar y pasan a `default` solo al publicar una versión aprobada por QA.
- Se corta `release/X.Y` cuando una versión está completa; allí solo entran correcciones.

## Decisiones de arquitectura (ADR) ✅

Toda decisión que afecte la estructura, una dependencia o un proceso se registra en `studio/docs/adr/NNNN-titulo.md` con contexto, decisión, alternativas y consecuencias. Estados: **Propuesta**, **Aceptada**, **Reemplazada**. Se leen en el hub, sección *Decisiones de arquitectura*.

## Deuda técnica ✅

- Se registra como tarea de tipo `refactor`, nunca como un `TODO` suelto.
- Cada fase incluye una **revisión de arquitectura y deuda técnica** con horas reservadas: el **10 %** de las horas de la fase se dedican a refactor y deuda (decisión del autor, 2026-10-25).
- Regla del boy scout: se deja el código un poco mejor de como se encontró.

## Seguridad en el flujo ✅

- Ningún secreto, clave de firma ni contraseña en el repositorio (`.gitignore` y revisión).
- Acciones de GitHub fijadas por versión y, más adelante, por hash (tarea F1-35).
- Dependencias pocas, con versión fija y licencia revisada.

## Trabajo con IA ✅

- Cada sesión de trabajo empieza **creando una rama**; Claude no sube directamente a `main` ni fuerza subidas.
- Claude abre cada cambio como rama y deja el PR listo; el autor revisa y fusiona.
- Cada tarea documenta su evidencia y su referencia (`ref`) en el hub.

## Sesiones por bloques ✅

Decisión del autor (2026-10-25). Una sesión puede abarcar varias tareas:

- **Bloque:** las tareas pequeñas o del mismo ámbito o de los mismos archivos (un grupo de la misma fase o del mismo documento) se hacen en una sola sesión, una tras otra.
- **Sesión propia:** solo una tarea grande o densa (muchas decisiones del autor o contexto pesado).
- **Nada cambia en el flujo:** una tarea = una rama = un PR, y cada tarea tiene su cierre.
- **Tras fusionar** el PR, la sesión sigue con la tarea siguiente del bloque. Se compacta o se cierra al terminar el bloque o al pasar de unos 200 k tokens de contexto.
- **Título:** `S-NN · <bloque o tema> (<IDs>)`, que se registra con `tools/sesion.py nueva`.

## Coste de la IA ✅

Decisión del autor (2026-10-23, [ADR-0010](adr/0010-politica-de-modelos-y-autorizacion-de-fable.md)). Las reglas completas están en `CLAUDE.md`; este es el resumen:

- **Modelo y esfuerzo:** cada agente lleva los de su rol en `studio/data/equipo.json` (tabla en [20](20-equipo-y-flujo-de-agentes.md)). Los cambios por tarea llevan su motivo; Fable 5.1 exige la autorización del autor.
- **Informes cortos:** encargo mínimo y informe de máximo 60 líneas o 6.000 caracteres (resultado, archivos tocados, hallazgos con `archivo:línea`, dudas para el autor).
- **Lectura parcial:** `grep -n` y rangos en lugar de documentos enteros; los archivos generados grandes no se leen.
- **Lotes:** los agentes independientes se lanzan juntos y sus informes se procesan juntos.
- **Cierre de sesión:** al fusionar el PR de una tarea se cierra la sesión o se compacta, para no arrastrar un contexto grande a la tarea siguiente.

## Ajustes de GitHub que hace el autor ✅

Tarea F0-35. Decisiones del autor (2026-10-24): el repositorio se hace **público** (el plan gratuito no permite proteger ramas en repos privados), licencia propietaria de solo consulta (`LICENSE`), merge commit sin historial lineal, las 5 comprobaciones requeridas y reglas también para admins. Se acepta que el correo `frncsico@gmail.com` quede visible en 188 commits antiguos.

### Guía paso a paso (repositorio `Francisco-V98/vein-of-fortune`)

Haz los pasos en este orden, después de fusionar el PR de F0-35 (así `LICENSE`, el aviso del README y los `timeout` ya están en `main`). Las rutas son de la web de GitHub.

1. **Correo (antes de publicar).** Tu avatar → *Settings → Emails*: marca **Keep my email addresses private** y **Block command line pushes that expose my email**. En local: `git config user.email "<ID>+Francisco-V98@users.noreply.github.com"` (el ID está en *Emails*).
2. **Revisar tu equipo.** Antes de cualquier `git add`, comprueba que no hay `.mcp.json` ni claves de PixelLab o Higgsfield dentro del repo (`.gitignore` ya los excluye).
3. **Hacer público el repo.** *Settings → General → Danger Zone → Change visibility → Make public*. Escribe el nombre para confirmar.
4. **Ramas.** *Settings → General → Pull Requests*: deja marcado solo **Allow merge commits**; desmarca *Allow squash merging* y *Allow rebase merging*; marca **Automatically delete head branches**.
5. **Protección de `main`.** *Settings → Rules → Rulesets → New ruleset → New branch ruleset*:
   - Name: `main protegida`; Enforcement status: **Active**; Bypass list: **vacía** (aplica también a ti).
   - Target branches: *Add target → Include default branch*.
   - Marca: **Restrict deletions**, **Block force pushes**, **Require a pull request before merging** (approvals: 0, eres el único autor) y **Require status checks to pass**.
   - En *Require status checks* pulsa *Add checks* y añade estos 5 nombres exactos (aparecen tras la primera ejecución del CI):
     `Estudio (roadmap, tareas, QA y hub)` · `Pruebas de las herramientas` · `Convención de commits` · `Arquitectura modular de game/` · `Juego (formato, lint y pruebas)`.
   - Deja **sin marcar** *Require linear history*. Guarda con *Create*.
6. **Actions.** *Settings → Actions → General*: *Fork pull request workflows* → **Require approval for all outside collaborators**; *Workflow permissions* → **Read repository contents permissions** y sin «Allow GitHub Actions to create and approve pull requests».
7. **Seguridad.** *Settings → Advanced Security* (o *Code security*): activa **Private vulnerability reporting**, **Dependabot alerts**, **Secret scanning** y **Push protection**.
8. **Comprobar.** Abre un PR de prueba: el botón de fusionar debe esperar a las 5 comprobaciones; un `git push origin main` directo debe ser rechazado.

Si algo falla, el nombre de una comprobación en la regla debe coincidir con el `name:` del job en `.github/workflows/ci.yml`. Si cambias el nombre de un job, cámbialo también en la regla.

### Riesgos aceptados al publicar

- Términos comerciales de Higgsfield y del modelo de las imágenes provisionales: la ayuda de Higgsfield (cláusula 4.4) dice que no reclama la propiedad y no restringe el uso comercial; falta leer los Términos completos ⏳ F5-26.
- Marca del título visible antes de la búsqueda formal ⏳ F5-29.
- Acciones del CI por etiqueta y no por hash ⏳ F1-35.

## QA en el flujo ✅

El QA es una etapa propia, entre la revisión y el cierre. Procedimiento completo, tipos de prueba, seguridad, errores y criterios de salida en [16 · Calidad y QA](16-calidad-y-qa.md).

## Pendiente ✅

- Instalar `gdtoolkit` y el marco de pruebas cuando exista el proyecto Godot ⏳ F1-33.
