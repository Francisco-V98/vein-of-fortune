# 16 · Calidad y QA

## Requisito del autor ✅

El **QA es un proceso dentro del flujo de trabajo**: revisiones, pruebas funcionales, pruebas en general, seguridad y lo que haga falta. No es una fase al final: acompaña a cada tarea.

Los principios son requisitos; los umbrales y los detalles están marcados 🟡 y se afinan con el prototipo ([ADR-0008](adr/0008-qa-como-etapa-del-flujo.md)).

## Principios ✅

1. **Calidad desde el principio:** se previene antes de detectar. La arquitectura modular y las pruebas del dominio son la primera defensa ([14](14-arquitectura-y-modularidad.md)).
2. **Automatizar lo repetible:** lo que se puede verificar sin una persona se verifica en cada cambio.
3. **Probar donde se juega:** un **PC Windows real** manda (el autor trabaja en Mac y eso no basta); la Steam Deck, si la hay, también. Máquinas virtuales y emuladores no lo reemplazan.
4. **Cada verificación deja evidencia:** un resultado, una captura o una nota en la tarea.
5. **Separar quien construye de quien aprueba:** Claude construye y verifica técnicamente; el autor acepta jugando en PC.
6. **Un error corregido deja una prueba:** no vuelve a pasar sin que algo lo detecte.

## El QA en el flujo ✅

```
backlog → sprint → doing → review → qa → done
                              │      │
                              │      └─ falla: vuelve a doing (con el error anotado)
                              └─ cambios pedidos: vuelve a doing
```

| Estado | Qué se verifica | Quién | Entrada | Salida |
|---|---|---|---|---|
| `review` | **Código y arquitectura:** claridad, capas y módulos, pruebas escritas, seguridad, lista de revisión de [15](15-flujo-de-trabajo-y-calidad.md) | Claude (auto-revisión) y autor (PR) | PR abierto y CI en verde | Revisión aprobada |
| `qa` | **Comportamiento:** casos de prueba de la tarea, regresión, pruebas en el PC de pruebas, seguridad y rendimiento que apliquen | Claude (automáticas) y autor (aceptación) | Revisión aprobada | Casos aprobados y sin errores S1 o S2 abiertos |
| `done` | Fusionada en `main` con evidencia | Autor | QA aprobado | — |

- Una tarea **no pasa a `done` sin QA**, salvo las que no producen comportamiento (documentos, decisiones, estudio), que pasan de `review` a `done` y lo dicen en su nota.
- Si QA falla, la tarea vuelve a `doing` y el error se registra con su severidad.
- El resultado de QA queda en el historial de la tarea y en el catálogo de casos.

## Tipos de verificación 🟡

| Tipo | Qué busca | Cómo |
|---|---|---|
| **Revisión de código** | Claridad, arquitectura, deuda | PR con lista de revisión y `/code-review` |
| **Unitarias** | Reglas del dominio correctas y deterministas | GUT, sin interfaz |
| **De integración** | Módulos juntos a través de sus `api` y eventos | GUT con dobles de plataforma |
| **Funcionales / de aceptación** | Que lo diseñado funciona como se describió | Casos de prueba ejecutados en el PC de pruebas |
| **De regresión** | Que lo anterior sigue funcionando | Casos automáticos en CI y rondas manuales por bloque |
| **Exploratorias** | Lo que nadie pensó | Sesiones con un objetivo y tiempo limitado |
| **Simulación y economía** | Mercado sin trucos, inflación y estrategias dominantes | Simulador de 10.000 días y partidas completas |
| **Rendimiento** | Cuadros por segundo, memoria, arranque, tamaño | Medición en la matriz de PC contra presupuestos |
| **Compatibilidad** | Gamas de PC, resoluciones, Windows y Linux, Steam Deck, mandos | Matriz de PC |
| **Accesibilidad** | Daltonismo, tamaño de texto, contraste, teclado (TC-050), mando (TC-038) | Lista de verificación y pruebas manuales |
| **Localización** | ES y EN completos, textos que no se cortan, formatos | Pseudo-localización y revisión por pantalla |
| **Guardado y actualización** | Integridad, corrupción, migración entre versiones | Casos automáticos y manuales |
| **Instalación** | Instalar desde Steam, abrir, actualizar sin perder la partida; sincronización de la nube | Pruebas en el PC de pruebas |
| **Usabilidad** | Si se entiende y se disfruta | Playtest con personas externas |
| **Seguridad** | Ver sección siguiente | Lista de verificación y análisis estático |
| **Privacidad** | Que la telemetría no filtre datos | Revisión de lo que se guarda y exporta |
| **Contenido** | Datos válidos, textos faltantes, referencias rotas | Validación de datos en CI |

## Seguridad en QA ✅

Lista de verificación **adaptada de OWASP MASVS** (estándar de seguridad para aplicaciones móviles, que sigue siendo una buena guía) a un juego de PC **sin conexión ni cuentas propias** 🟡:

| Área | Verificación |
|---|---|
| Secretos | Sin claves, tokens ni contraseñas en el repositorio ni en las builds de Windows y Linux (escaneo automático) |
| Almacenamiento | Los guardados no incluyen datos personales; el archivo de diagnóstico tampoco |
| Integridad de datos | Un guardado corrupto o manipulado se detecta y no rompe el juego ni ejecuta contenido |
| Entradas | El nombre del personaje y de la tienda tienen límites y caracteres permitidos, y no inyectan formato (por ejemplo etiquetas de texto enriquecido) ni rompen la interfaz |
| Plataforma | El juego solo escribe en su carpeta de guardados y diagnóstico; sin ejecutables ni librerías sin explicar en la build |
| Compilación | Versión de lanzamiento sin depuración activada y con las credenciales de Steam fuera del repositorio |
| Dependencias | Pocas, con versión fija y licencia revisada; sin avisos de vulnerabilidades conocidas |
| Privacidad | Nada se envía sin una acción del usuario; el ID anónimo se puede reiniciar |
| Resistencia | Se asume que un jugador puede manipular su guardado: no es crítico en un juego de un jugador, pero no debe provocar fallos |

Cada punto tiene un caso de prueba en el catálogo (área **Seguridad** y **Privacidad**). Las comprobaciones de APK, manifiesto y firma de Google Play pasan a la fase móvil (ver más abajo).

## Casos de prueba ✅

- Viven en `studio/data/qa/cases.json` y se ven en el hub (sección **QA**).
- Cada caso tiene: identificador, área, tipo, nivel (unitaria, integración o manual), si es automático, prioridad, pasos, resultado esperado, tareas relacionadas y último resultado.
- **Resultados:** `not-run`, `pass`, `fail`, `blocked`, `skipped`; cada resultado lleva fecha, versión probada y quién lo ejecutó.
- El catálogo inicial tenía **49 casos** derivados de lo diseñado; con el cambio a PC primero ([ADR-0009](adr/0009-pc-primero-movil-despues.md)) suma **55**: accesibilidad por teclado (TC-050), Steam Auto-Cloud (TC-051), pantallas de PC (TC-052) y tres casos con la etiqueta **[Fase móvil]** (TC-053 a TC-055, prioridad P3) que conservan lo táctil y lo de Android. Se amplía cada vez que una tarea introduce comportamiento.
- Los casos automáticos se convierten en pruebas del repositorio; los manuales se ejecutan en el PC de pruebas.

## Errores ✅

Cada error es un archivo en `studio/data/qa/bugs/BUG-NNNN.json` con título, severidad, estado, versión donde apareció, pasos para reproducirlo, resultado esperado y real, y evidencias.

### Severidad 🟡

| Nivel | Significado | Ejemplo | Regla |
|---|---|---|---|
| **S1 · Crítico** | Pérdida de datos, cierre del juego, bloqueo total | Se pierde la partida al guardar | Detiene todo; se corrige primero |
| **S2 · Grave** | Función principal rota sin atajo | No se puede vender | Se corrige antes de la siguiente versión |
| **S3 · Moderado** | Falla con alternativa o efecto limitado | Un texto se corta | Se planifica |
| **S4 · Menor** | Cosmético o muy poco probable | Un píxel desalineado | Cuando haya tiempo |

### Ciclo de vida

`abierto → triaje → en corrección → corregido → verificado → cerrado`, o `no se corrige` con su motivo. Todo error corregido incorpora una **prueba de regresión**.

## Criterios de salida de una versión 🟡

- 0 errores **S1** y **S2** abiertos.
- Casos de prioridad **P0** aprobados (automáticos y manuales).
- Matriz de PC recorrida.
- Lista de seguridad completa.
- Presupuestos de rendimiento cumplidos.
- Informe de QA de la versión redactado (`studio/qa/reports/`).

## Plan de QA por fase 🟡

| Fase | Foco |
|---|---|
| F1 · Preparación | Verificación de herramientas; plan de pruebas, matriz de PC, el PC Windows de pruebas, lista de seguridad y escaneo de secretos |
| F2 · Prototipo | Automatizar los casos del mercado y del día; ronda funcional en el PC de pruebas; guardado y corrupción |
| F3 · Vertical slice | QA del Acto I: seguridad, accesibilidad, localización, rendimiento y compatibilidad (incluida la Steam Deck); playtest externo; informe |
| F4 · Contenido | QA continuo: automatización y regresión después de cada bloque; seguridad; playtest |
| F5 · Lanzamiento | Instalación y actualización desde Steam, seguridad final, privacidad, accesibilidad completa, builds de prueba en itch.io o Steam y decisión de lanzamiento |

## Matriz de PC 🟡

Decisión del autor (2026-10-15): se prueba en un **PC Windows real** y en la Steam Deck si la hay ([ADR-0009](adr/0009-pc-primero-movil-despues.md)). Es un requisito de F1.

| Dimensión | Cobertura mínima |
|---|---|
| Gama del equipo | Gama baja y **GPU integrada**; un equipo medio o alto como referencia |
| Sistema operativo | **Windows** y **Linux** |
| Steam Deck | 1280×800 con mando, sin HUD táctil y texto legible (objetivo *Verified*) |
| Resolución | 1080p, 1440p y 4K |
| Proporción de pantalla | 16:9 y **ultrapanorámico**; cómo se escala lo decide ⏳ F1-06 |
| Entrada | Ratón y teclado, y mando (incluido el de la Deck) |
| Equipo real | Un **PC Windows real** de pruebas |
| macOS | Después de la 1.0 |

❓ Falta definir los equipos reales: el autor trabaja en Mac, así que el PC Windows (que tiene o consigue) y la Steam Deck, si la hay, son la base; el resto de la matriz se completa con máquinas virtuales (Linux) y equipos prestados si hace falta.

## Presupuestos de rendimiento 🟡 (a medir en PC · ⏳ F1-44)

No hay cifras definitivas: se miden en la matriz de PC con la tarea F1-44 y recién entonces se fijan los límites.

| Medida | Objetivo inicial |
|---|---|
| Arranque en frío (gama baja de PC) | ⏳ F1-44 |
| Cuadros por segundo | ⏳ F1-44 (interfaz y minijuegos; se mide también en Steam Deck y GPU integrada) |
| Tamaño de la instalación | ⏳ F1-44 |
| Memoria | ⏳ F1-44 |
| Estabilidad | 60 minutos de juego sin cierres (se conserva el objetivo del plan anterior) |

## Fase móvil (después de la 1.0)

Se conserva lo previsto para Android y se retoma cuando empiece el móvil ([10](10-tecnico-y-herramientas.md), «Fase móvil»).

| Tema | Contenido previsto |
|---|---|
| Gamas y versiones | Android de gama baja, media y alta; la versión más reciente y la mínima soportada (a decidir) |
| Proporciones | 16:9, 19.5:9 y 20:9 con zona segura |
| Entrada | Táctil y mando Bluetooth |
| Rendimiento | Arranque en frío ≤ 5 s en gama media; 60 cuadros por segundo en interfaz y mínimo 30 en minijuegos; descarga ≤ 150 MB; batería y calor a medir (los números del plan anterior son 🟡 y se revisan entonces) |
| Telemetría | Android vitals de Google Play ([ADR-0007](adr/0007-telemetria-por-capas.md)) |
| Seguridad | APK, manifiesto con permisos mínimos y firma gestionada por Google Play |
| Pruebas | Android del autor, emuladores y equipos prestados; iOS con su propia tarea |
| Casos | Los casos de toque se mantienen en el catálogo con la etiqueta «fase móvil» |

## Métricas de calidad 🟡

Aprobación de casos, errores por severidad, errores que llegaron a una versión, cobertura del dominio, sesiones sin cierres y tiempo de corrección. Se ven en el hub y en el informe de cada versión.

## Responsabilidades ✅

| Quién | Hace |
|---|---|
| **Claude** | Diseña los casos, escribe y ejecuta las pruebas automáticas, revisa código y arquitectura, ejecuta análisis estáticos y simulaciones, registra resultados y errores |
| **Autor** | Ejecuta las pruebas de aceptación y exploratorias en el PC de pruebas, decide severidades y criterios de salida, y aprueba |

**Límite honesto:** Claude no puede jugar en el PC de pruebas ni sentir si algo es divertido o fluido. Esa parte de QA es del autor.

## Pendiente ❓

- Definir los equipos reales de la matriz de PC (incluido el PC Windows de pruebas).
- ⏳ F1-44 · Medir los presupuestos de rendimiento en PC.
- Elegir la herramienta de escaneo de secretos (tarea F1-42).
- Ejecutar la primera ronda de casos cuando exista el prototipo.
