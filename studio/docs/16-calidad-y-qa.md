# 16 · Calidad y QA

## Requisito del autor ✅

El **QA es un proceso dentro del flujo de trabajo**: revisiones, pruebas funcionales, pruebas en general, seguridad y lo que haga falta. No es una fase al final: acompaña a cada tarea.

Los principios son requisitos; los umbrales y los detalles están marcados 🟡 y se afinan con el prototipo ([ADR-0008](adr/0008-qa-como-etapa-del-flujo.md)).

## Principios ✅

1. **Calidad desde el principio:** se previene antes de detectar. La arquitectura modular y las pruebas del dominio son la primera defensa ([14](14-arquitectura-y-modularidad.md)).
2. **Automatizar lo repetible:** lo que se puede verificar sin una persona se verifica en cada cambio.
3. **Probar donde se juega:** el teléfono real manda; el simulador y el emulador no lo reemplazan.
4. **Cada verificación deja evidencia:** un resultado, una captura o una nota en la tarea.
5. **Separar quien construye de quien aprueba:** Claude construye y verifica técnicamente; el autor acepta en el dispositivo.
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
| `qa` | **Comportamiento:** casos de prueba de la tarea, regresión, pruebas en el dispositivo, seguridad y rendimiento que apliquen | Claude (automáticas) y autor (aceptación) | Revisión aprobada | Casos aprobados y sin errores S1 o S2 abiertos |
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
| **Funcionales / de aceptación** | Que lo diseñado funciona como se describió | Casos de prueba ejecutados en el teléfono |
| **De regresión** | Que lo anterior sigue funcionando | Casos automáticos en CI y rondas manuales por bloque |
| **Exploratorias** | Lo que nadie pensó | Sesiones con un objetivo y tiempo limitado |
| **Simulación y economía** | Mercado sin trucos, inflación y estrategias dominantes | Simulador de 10.000 días y partidas completas |
| **Rendimiento** | Cuadros por segundo, memoria, arranque, batería, tamaño | Medición en el teléfono contra presupuestos |
| **Compatibilidad** | Gamas de Android, proporciones de pantalla, mandos | Matriz de dispositivos |
| **Accesibilidad** | Daltonismo, tamaño de texto, contraste, mando | Lista de verificación y pruebas manuales |
| **Localización** | ES y EN completos, textos que no se cortan, formatos | Pseudo-localización y revisión por pantalla |
| **Guardado y actualización** | Integridad, corrupción, migración entre versiones | Casos automáticos y manuales |
| **Instalación** | Instalar, abrir, actualizar sin perder la partida | Pruebas en el teléfono |
| **Usabilidad** | Si se entiende y se disfruta | Playtest con personas externas |
| **Seguridad** | Ver sección siguiente | Lista de verificación y análisis estático |
| **Privacidad** | Que la telemetría no filtre datos | Revisión de lo que se guarda y exporta |
| **Contenido** | Datos válidos, textos faltantes, referencias rotas | Validación de datos en CI |

## Seguridad en QA ✅

Lista de verificación **adaptada de OWASP MASVS** (estándar de seguridad para aplicaciones móviles) a un juego **sin conexión ni cuentas** 🟡:

| Área | Verificación |
|---|---|
| Secretos | Sin claves, tokens ni contraseñas en el repositorio ni en el APK (escaneo automático) |
| Almacenamiento | Los guardados no incluyen datos personales; el archivo de diagnóstico tampoco |
| Integridad de datos | Un guardado corrupto o manipulado se detecta y no rompe el juego ni ejecuta contenido |
| Entradas | El nombre del personaje y de la tienda tienen límites y caracteres permitidos, y no inyectan formato (por ejemplo etiquetas de texto enriquecido) ni rompen la interfaz |
| Plataforma | Permisos del manifiesto reducidos al mínimo; sin componentes exportados innecesarios |
| Compilación | Versión de lanzamiento sin depuración activada, firmada y con la firma gestionada por Google Play |
| Dependencias | Pocas, con versión fija y licencia revisada; sin avisos de vulnerabilidades conocidas |
| Privacidad | Nada se envía sin una acción del usuario; el ID anónimo se puede reiniciar |
| Resistencia | Se asume que un jugador puede manipular su guardado: no es crítico en un juego de un jugador, pero no debe provocar fallos |

Cada punto tiene un caso de prueba en el catálogo (área **Seguridad** y **Privacidad**).

## Casos de prueba ✅

- Viven en `studio/data/qa/cases.json` y se ven en el hub (sección **QA**).
- Cada caso tiene: identificador, área, tipo, nivel (unitaria, integración o manual), si es automático, prioridad, pasos, resultado esperado, tareas relacionadas y último resultado.
- **Resultados:** `not-run`, `pass`, `fail`, `blocked`, `skipped`; cada resultado lleva fecha, versión probada y quién lo ejecutó.
- El catálogo inicial tiene **49 casos** derivados de lo diseñado. Se amplía cada vez que una tarea introduce comportamiento.
- Los casos automáticos se convierten en pruebas del repositorio; los manuales se ejecutan en el teléfono.

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
- Matriz de dispositivos recorrida.
- Lista de seguridad completa.
- Presupuestos de rendimiento cumplidos.
- Informe de QA de la versión redactado (`studio/qa/reports/`).

## Plan de QA por fase 🟡

| Fase | Foco |
|---|---|
| F1 · Preparación | Verificación de herramientas; plan de pruebas, matriz de dispositivos, lista de seguridad y escaneo de secretos |
| F2 · Prototipo | Automatizar los casos del mercado y del día; ronda funcional en el teléfono; guardado y corrupción |
| F3 · Vertical slice | QA del Acto I: seguridad, accesibilidad, localización, rendimiento y compatibilidad; playtest externo; informe |
| F4 · Contenido | QA continuo: automatización y regresión después de cada bloque; seguridad; playtest |
| F5 · Lanzamiento | Instalación y actualización, seguridad final, privacidad, accesibilidad completa, prueba cerrada y decisión de lanzamiento |

## Matriz de dispositivos 🟡

| Dimensión | Cobertura mínima |
|---|---|
| Gama de Android | Baja, media y alta |
| Versiones de Android | La más reciente y la mínima soportada (a decidir) |
| Proporción de pantalla | 16:9, 19.5:9 y 20:9 |
| Entrada | Táctil y mando Bluetooth |
| iOS | Más adelante, con la tarea de iOS |

❓ Falta definir los dispositivos reales: se parte del Android del autor y se completa con emuladores y, si hace falta, equipos prestados.

## Presupuestos de rendimiento 🟡 (a medir en el teléfono)

| Medida | Objetivo inicial |
|---|---|
| Arranque en frío (gama media) | ≤ 5 s |
| Cuadros por segundo | 60 en interfaz; mínimo 30 en minijuegos |
| Tamaño de la descarga | ≤ 150 MB |
| Estabilidad | 60 minutos de juego sin cierres |
| Batería y calor | A medir; se fija el límite con datos reales |

## Métricas de calidad 🟡

Aprobación de casos, errores por severidad, errores que llegaron a una versión, cobertura del dominio, sesiones sin cierres y tiempo de corrección. Se ven en el hub y en el informe de cada versión.

## Responsabilidades ✅

| Quién | Hace |
|---|---|
| **Claude** | Diseña los casos, escribe y ejecuta las pruebas automáticas, revisa código y arquitectura, ejecuta análisis estáticos y simulaciones, registra resultados y errores |
| **Autor** | Ejecuta las pruebas de aceptación y exploratorias en el teléfono, decide severidades y criterios de salida, y aprueba |

**Límite honesto:** Claude no puede jugar en el teléfono ni sentir si algo es divertido o fluido. Esa parte de QA es del autor.

## Pendiente ❓

- Definir los dispositivos reales de la matriz.
- Medir los presupuestos de rendimiento con datos del teléfono.
- Elegir la herramienta de escaneo de secretos (tarea F1-42).
- Ejecutar la primera ronda de casos cuando exista el prototipo.
