# 14 · Arquitectura y modularidad

## Requisitos del autor ✅

El proyecto debe ser **muy modular**, sin dependencias directas entre partes, **escalable**, con una buena estructura de *scaffolding*, **independencia** (cambiar algo sin romper otra cosa) y las **mejores prácticas** en diseño y desarrollo, con clean code.

Todo lo que sigue es la forma de cumplirlo. Los principios son requisitos y el diseño concreto está aceptado en los ADR ([0003](adr/0003-arquitectura-modular.md), [0004](adr/0004-comunicacion-entre-modulos.md), [0006](adr/0006-contenido-como-datos.md), [0009](adr/0009-pc-primero-movil-despues.md), [0011](adr/0011-exploracion-caminable-tren-y-minas.md), [0012](adr/0012-modulo-tutorial-y-logros-en-progression.md) y [0013](adr/0013-json-como-fuente-del-contenido.md)). Validarlo con código real es trabajo de la Fase 1 (F1-28, F1-30 y F1-33): es una verificación, no una decisión pendiente, y si el código obliga a cambiar algo se hace con un ADR nuevo.

## Principios ✅

1. **Regla de dependencia:** las dependencias apuntan hacia el dominio. El dominio no conoce a nadie.
2. **Alta cohesión, bajo acoplamiento:** cada módulo hace una cosa y se conecta con otros por contratos pequeños.
3. **Dependencias explícitas:** nada se busca en un global; todo se entrega desde fuera (inyección de dependencias).
4. **Datos antes que código:** el contenido (minerales, zonas, eventos, textos) vive en datos validados, no en el código.
5. **Determinismo:** la simulación usa una semilla y un reloj inyectados, para reproducir partidas y errores. El dominio no llama al azar global (`randi`, `randf`, `randomize`) ni a `Time`: usa el azar con semilla del `kernel` y el puerto de reloj (el verificador lo vigila, regla A4).
6. **Una razón para cambiar:** una clase, una responsabilidad; un módulo, un propósito.
7. **Composición sobre herencia:** se combinan piezas pequeñas.
8. **Verificación automática:** las reglas se comprueban en CI; lo que no se verifica se erosiona.

## Estructura de `game/` ✅

```
game/
├── project.godot
├── architecture.json          módulos y dependencias permitidas (lo lee el verificador)
├── src/
│   ├── kernel/                tipos base compartidos: Result, ids, eventos, azar con semilla
│   ├── platform/
│   │   ├── ports/             contratos: entrada, almacenamiento, audio, idioma, reloj, háptica, tienda, pantalla
│   │   └── adapters/          implementaciones (ratón y teclado, mando, Steam, PC, pruebas; después táctil y móvil); solo `app` las conoce
│   ├── ui_kit/                tema, tokens de diseño y componentes de interfaz reutilizables
│   ├── modules/
│   │   └── <módulo>/
│   │       ├── domain/            reglas puras (RefCounted/Resource); sin nodos ni UI
│   │       ├── application/       casos de uso y servicios; define los puertos que necesita
│   │       ├── infrastructure/    adaptadores del módulo (carga de datos, persistencia)
│   │       ├── presentation/      escenas y presentadores (interfaz)
│   │       ├── api/               lo único que otros módulos pueden usar (fachada y eventos)
│   │       ├── data/              definiciones de contenido del módulo
│   │       └── tests/
│   └── app/                   raíz de composición: arranque, registro de módulos, navegación
├── assets/                    arte, audio y fuentes con convención de nombres
├── locales/                   traducciones .po (ES, EN)
└── tests/                     pruebas de integración entre módulos
```

Adoptada tal cual por el autor (2026-10-24); es la que ya usan `game/architecture.json` y el verificador. Durante la Fase 1, cualquier cambio de carpetas va por ADR. Dentro de `app/`, la carpeta `puentes/` aloja los puentes de composición ([ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md)).

## Capas dentro de un módulo ✅

```
presentation ─┐
              ├─► application ─► domain
infrastructure┘                  ▲
   (implementa los puertos que declara application)
```

| Capa | Puede usar | No puede usar |
|---|---|---|
| `domain` | solo `kernel` y su propio dominio | nodos, UI, archivos, entrada, otros módulos, plataforma |
| `application` | `domain`, `kernel`, puertos de `platform`, `data` | `presentation`, `infrastructure` |
| `infrastructure` | `application`, `domain`, `kernel`, puertos, `data` | `presentation` |
| `presentation` | `application`, `domain`, `kernel`, `ui_kit`, puertos | `infrastructure` |
| `api` | `application`, `domain` | `presentation`, `infrastructure` |

## Módulos previstos ✅

Cada módulo corresponde a un tema de diseño ya documentado. `depende de` son las únicas *apis* de otros módulos que puede usar; todo debe quedar declarado en `architecture.json`.

| Módulo | Responsabilidad | Depende de | Documento |
|---|---|---|---|
| `day` | Días, bloques de tiempo y calendario | — | [01](01-core-loop.md) |
| `inventory` | Ítems, almacén, capacidad y costos | — | [03](03-comercio.md) |
| `market` | Precios, oferta y demanda, bots, spread | day | [03](03-comercio.md) |
| `world` | Mapa, niebla de zonas bloqueadas, tren (billete y viaje), asentamientos y edificaciones como datos | day | [26](26-zonas-y-edificios.md), [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md) |
| `exploration` | Movimiento por acciones, colisiones, puertas, loader entre escenas, recinto de cinco entradas, sorteo diario y cambio único | day, world | [10](10-tecnico-y-herramientas.md), [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md) |
| `extraction` | Zonas, menas, detector con batería, minijuegos, peligros y cierres de entradas | day, inventory, exploration, world_events | [02](02-extraccion.md), [09](09-minijuegos.md) |
| `shop` | Tienda, ventas, contratos y regateo | market, inventory, day | [03](03-comercio.md) |
| `crafting` | Refinado y productos | inventory, market | [03](03-comercio.md) |
| `staff` | Empleados, contratos de trabajo y lealtad | day, extraction, shop | [04](04-progresion-y-meta.md) |
| `factions` | Alianza, los cuatro medidores de relación y vigilancia | day | [07](07-sociedad-y-eventos.md) |
| `world_events` | Apagones, huelgas, saqueos y otros eventos | day, factions | [07](07-sociedad-y-eventos.md) |
| `news` | Prensa: noticias, rumores y sesgos | world_events, market | [03](03-comercio.md) |
| `story` | Actos, diálogos, cintas y decisiones | day, factions, world_events | [08](08-historia-y-personaje.md) |
| `progression` | Stats por uso, estatus y logros (catálogo de logros de Steam en F4-235) | extraction, shop | [04](04-progresion-y-meta.md) |
| `lifestyle` | Casa, ropa, auto y cosméticos | progression, inventory | [04](04-progresion-y-meta.md) |
| `tutorial` | Pasos guiados y compuertas de toda primera vez y de todo paso obligatorio: catálogo como datos, estado «se completa una vez», remedios (reintento, recordatorio, práctica) y marcador en pantalla | day, story | [27](27-guion-del-acto-i.md), [ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md) |
| `save` | Guardado versionado, con punto de control por acción y hasta 5 partidas guardables | — | [01](01-core-loop.md), [10](10-tecnico-y-herramientas.md) |
| `telemetry` | Diagnóstico local exportable | — | [10](10-tecnico-y-herramientas.md) |

`world` y `exploration` (✅ 2026-10-24) separan la geografía y el paseo de la economía: `world` decide qué zonas están abiertas o con niebla y cuánto cuesta el viaje (lee el acto de `story` por evento, no depende de él); `exploration` solo conoce posiciones, puertas y el sorteo determinista `hash(partida, día, mina, entrada)` del reparto de entradas. `extraction` consume ese reparto y los cierres de `world_events` (dependencia declarada) por sus `api`, y el dominio no usa nodos ni coordenadas de Godot (la presentación sí). `staff` y `world_events` no cambian de dependencias: los empleados abstraen la entrada y los cierres llegan como eventos.

Estaciones, clima y calendario (✅ F0-94): viven en el módulo `day` (fecha, estación y clima del día por zona, determinista con la semilla) y las fichas del calendario, los festivos y las mini-historias las emite `world_events` hacia `story` y `news` por eventos; la barra de fecha y el calendario son presentación. No se añade ningún módulo ni se cambian dependencias en `architecture.json` por ahora; si el motor de mini-historias (⏳ F3-60) pide un módulo propio, lo decide esa tarea. Ver [29](29-calendario-y-temporadas.md).

Logros (✅ 2026-10-24, cambia lo anterior): viven en `progression`, que ya mide el avance; antes se preveía un módulo propio y se descartó porque duplicaba esa medición ([ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md)). Llegan a Steam a través del puerto de tienda. Si un logro necesita eventos de otro módulo, F4-235 declara la dependencia en `architecture.json` sin formar ciclos. El casino (V2.0, F6-01) entrará creando su propio módulo, sin tocar los demás.

Tutorial (✅ 2026-10-24): `tutorial` escucha `EscenaIniciada` de `story` y el avance de `day`; sabe que el jugador hizo la acción por su puerto `AccionesDelJugador`, que recibe identificadores neutros (`accion.vender`), y la cola de escenas de `story` sabe si una compuerta se cumplió por su puerto `CompuertasDeCola`. Los dos puertos los implementan puentes de composición, así `tutorial` no depende de los módulos que enseña y `story` no depende de `tutorial`. Qué se enseña, cómo, qué lo exige y qué pasa si falla está en el inventario del documento 27 (sección 2.4).

El grafo es **acíclico**: ningún módulo puede depender, directa o indirectamente, de sí mismo (regla A7).

## Cómo se comunican los módulos ✅

| Mecanismo | Cuándo | Ejemplo |
|---|---|---|
| **API pública** (`api/`) | Pregunta síncrona: "dame un dato ahora" | `shop` pide a `market` el precio de venta actual |
| **Eventos de dominio** | Aviso: "pasó algo", sin saber quién escucha | `market` publica `PrecioCambiado`; `news` lo escucha |

Reglas de los eventos:

- Los define el módulo que los publica, dentro de su `api/`. Quien los escucha depende de esa `api`.
- Son **inmutables**, con nombre en pasado (`DiaAvanzado`, `HuelgaIniciada`) y llevan solo datos.
- Se entregan por un bus pequeño del `kernel`. No se usan para órdenes ("haz esto"): eso va por la API.
- Son **tipados**: cada evento es una clase con `class_name` y campos con tipo; el bus se suscribe por clase de evento, nunca por un nombre en texto (un nombre en texto es una dependencia que el verificador no ve).
- Un evento nunca devuelve resultados a quien lo publica.

**Puentes de composición** ([ADR-0012](adr/0012-modulo-tutorial-y-logros-en-progression.md)): cuando un módulo necesita datos de otro y depender de él crearía un ciclo o un acoplamiento excesivo, declara un puerto en su `application` y un puente de `app/puentes/` lo implementa sobre la `api` del otro. Los puentes solo traducen (sin reglas del juego) y se listan aquí:

| Puente | Puerto que implementa | Lee de |
|---|---|---|
| Acciones del jugador | `tutorial` · `AccionesDelJugador` | eventos de las `api` de los módulos que el tutorial enseña (`shop`, `extraction`, `crafting`...) |
| Compuertas de la cola | `story` · `CompuertasDeCola` | `api` de `tutorial` |

## Presentación ✅

- Las escenas son **tontas**: muestran datos y emiten señales; no tienen reglas del juego.
- Las escenas son **pequeñas** y de una sola responsabilidad; las pantallas se arman **instanciando** escenas, no heredando escenas ni scripts largos (composición sobre herencia). Los componentes reutilizables viven en `ui_kit`.
- Las reglas no se sondean en `_process`: la interfaz reacciona a eventos y a llamadas del presentador; `_process` queda para animación y entrada.
- Cada pantalla tiene un **presentador** que traduce entre el caso de uso y la vista.
- "Las señales suben, las llamadas bajan": un nodo hijo emite señales; el padre le llama.
- Los textos siempre pasan por el sistema de traducción (ver [10](10-tecnico-y-herramientas.md)).
- La apariencia sale del **tema** de `ui_kit` y de los tokens de diseño derivados de la paleta ([12](12-direccion-de-arte.md)), no de valores sueltos en cada escena.

## Datos y persistencia ✅

- El contenido se define en archivos **JSON** con **esquema y validación**, que son la única fuente ([ADR-0013](adr/0013-json-como-fuente-del-contenido.md)); cargar un dato inválido falla de forma clara al arrancar. Los `.tres` no son fuente de contenido.
- Los identificadores de contenido son **cadenas estables** (`mineral.hierro`), nunca posiciones.
- Al cargar, la `infrastructure` de cada módulo convierte el JSON en **objetos tipados de solo lectura** (clases del dominio) que se entregan a los módulos; nadie lee diccionarios sueltos fuera de `infrastructure`.
- El guardado usa **DTO versionados** con migraciones, un **punto de control al iniciar cada acción** y hasta **5 partidas guardables** que el jugador elige ([01](01-core-loop.md)). Cada módulo ofrece `snapshot()` y `restore()`; el módulo `save` los reúne a través de la raíz de composición, sin conocerlos.
- El archivo de guardado es **texto con datos puros** (JSON con número de versión), nunca un `Resource` (`.tres`/`.res`) ni `store_var` con objetos: cargar un recurso puede ejecutar scripts incrustados, y un guardado se puede editar o compartir.
- La escritura es **atómica**: se escribe un archivo temporal, se comprueba y se renombra, y se conserva la copia anterior; así una suspensión de la Steam Deck o un corte no deja un guardado roto.
- Cada migración tiene una prueba con un guardado real de la versión anterior.

## Plataforma ✅

El juego se lanza **primero en PC (Windows y Linux, con Steam)** y el móvil llega después de la 1.0 ([ADR-0009](adr/0009-pc-primero-movil-despues.md)). La arquitectura ya lo prevé: la plataforma son **puertos** con adaptadores intercambiables, así que llevar el juego a otro lugar es añadir adaptadores, no modificar módulos.

| Puerto | Qué cubre | Adaptadores |
|---|---|---|
| Entrada | Acciones (aceptar, cancelar, mover, usar, menú) y detección del último dispositivo | **Ratón y teclado** y **mando** (Steam Deck incluida); **táctil**: adaptador futuro, fase móvil |
| Almacenamiento | Guardados, carpeta de guardados y diagnóstico local | Archivos locales; Steam Auto-Cloud sincroniza esa carpeta (hasta 5 partidas; en Hardcore manda el guardado local) |
| **Plataforma / tienda** | Logros, nube y actualizaciones | Steam con ✅ **GodotSteam** (autor, 2026-10-24; licencia verificada en F1-45, [ADR-0009](adr/0009-pc-primero-movil-despues.md)); un adaptador **nulo** siempre disponible para itch.io y pruebas, de modo que el juego corra sin Steam |
| **Pantalla** | Resolución, modo ventana y pantalla completa, escala | Adaptador de PC; ✅ resolución base 640×360 y escala entera con bandas ([10](10-tecnico-y-herramientas.md)) |
| Audio, idioma, reloj | Reproducción, idioma activo, tiempo inyectado | Adaptadores de PC y dobles de pruebas |
| Háptica | Vibración | Vibración del mando; en la fase móvil, la del teléfono |

Reglas:

- Los módulos solo hablan con los **puertos**; el dominio no usa `Input`, `OS` ni `DisplayServer` (símbolos prohibidos que ya vigila el verificador, regla A4).
- Los logros los define el módulo que los otorga y los emite como datos; solo el adaptador de tienda los envía a Steam.
- Nada del dominio sabe que existe Steam. Si Steam no está, el adaptador nulo responde sin hacer nada.
- Los controles (ratón y teclado, mando) viven detrás del puerto de entrada ([10](10-tecnico-y-herramientas.md)).
- El **camino al móvil** consiste en escribir el adaptador táctil, la háptica del teléfono y los de almacenamiento y ciclo de vida de Android e iOS. Para no cerrarlo, ninguna interfaz nueva depende solo del hover.

## Raíz de composición ✅

`app/` es el único lugar que conoce las implementaciones concretas: crea los módulos, conecta puertos con adaptadores y con los puentes de composición, y arranca el juego. Los autoloads se limitan a uno (`App`), lo que ya vigila el verificador (regla A9); el resto se entrega por parámetro.

## Clean code en GDScript ✅

Requisito del autor. Los umbrales de tamaño (unas 20 líneas por función y 400 por archivo) son **avisos configurables**, no errores: el verificador ya avisa por archivo y ⏳ F1-32 los configura en `gdlint`.

- **Tipado estático en todo:** variables, parámetros, retornos, `Array[T]` y diccionarios tipados. En `project.godot` los avisos de declaración sin tipo y de acceso inseguro se tratan como errores (lo configura ⏳ F1-32).
- **Nombres que explican:** funciones como verbos, booleanos como preguntas (`es_valido`), sin abreviaturas.
- **Funciones cortas** (guía: hasta ~20 líneas) y de **un solo nivel de abstracción**.
- **Un archivo, una clase.** Guía: hasta 400 líneas (el verificador avisa).
- **Sin números mágicos:** constantes con nombre o datos.
- **Retornos tempranos** en lugar de anidar condiciones.
- **Documentar el contrato** de lo público con comentarios `##`; el resto se explica con buenos nombres.
- **Sin código comentado** y **sin `TODO` sin tarea** (`TODO(F3-12): …`).
- **Errores explícitos:** el dominio devuelve un `Result`; las excepciones no se usan para el flujo normal.
- **Sin rutas de nodos escritas a mano**: referencias exportadas o nombres únicos.
- **Señales** con nombre en pasado y datos tipados.

## Qué se prohíbe ✅

- Singletons y estado global (salvo `App`).
- Que un módulo use las carpetas internas de otro.
- Lógica de juego en las escenas.
- Que el dominio use `Node`, `Input`, archivos o el árbol de escenas.
- Números y textos del juego escritos dentro del código.
- Clases "dios" y utilidades genéricas sin dueño.
- Dependencias circulares.
- Escuchar eventos por un nombre en texto o cargar rutas construidas en tiempo de ejecución.
- Guardar partidas como `Resource` o con objetos serializados.

## Verificación automática ✅

| Regla | Qué comprueba | Herramienta |
|---|---|---|
| A1 | Capas dentro de un módulo | `tools/arch/check_architecture.py` |
| A2 | Un módulo solo usa la `api` de otro y si lo declara | ídem |
| A3 | El dominio no depende de otros módulos ni de la plataforma | ídem |
| A4 | El dominio no usa clases del motor, entrada, archivos, azar global ni reloj (`Time`) | ídem |
| A5 | `kernel` no depende de nada fuera de `kernel` | ídem |
| A6 | Solo `app` conoce `platform/adapters` | ídem |
| A7 | El grafo de módulos no tiene ciclos | ídem |
| A8 | Los módulos del código y los declarados coinciden | ídem |
| A9 | Solo los autoloads permitidos | ídem |
| Estilo | Formato y lint de GDScript | `gdformat` y `gdlint` (se instalan en F1-32) |
| Pruebas | Dominio y aplicación, sin interfaz | GUT con Godot sin interfaz (F1-33), con dobles de los puertos. Se elige GUT porque el dominio es puro y determinista, corre sin cabeza en CI y es GDScript puro; gdUnit4 aporta un lanzador de escenas que no hace falta ahora y se revisaría por ADR si aparecen pruebas de escena pesadas |
| Convención | Mensajes de commit | `tools/ci/check_commits.py` |
| Datos | Estado de tareas coherente con su historial | `studio/hub/build.py --strict` |

El verificador de arquitectura ya tiene **22 pruebas automáticas** sobre estructuras de ejemplo. Falta ejecutarlo contra código real de GDScript, que empieza en F1.

## Añadir un módulo ✅

1. Declararlo en `game/architecture.json` con sus `depends_on` (y su ADR si introduce una decisión nueva).
2. Crear su estructura de carpetas con el generador (lo construye F1-28; hasta entonces, a mano siguiendo la estructura de arriba).
3. Escribir primero el dominio y sus pruebas; luego aplicación; después infraestructura y presentación.
4. Exponer solo lo necesario en `api/`.
5. Registrarlo en la raíz de composición.
6. Ejecutar el verificador de arquitectura y las pruebas.

## Límites conocidos y deuda técnica

- **GDScript no tiene interfaces.** Los puertos se implementan como clases base abstractas con `assert`/`push_error` y se prueban con dobles. ⏳ F1-30 valida el patrón en Godot real; nada de lo hecho depende del resultado (si falla, cambia la forma de escribir los puertos, no los módulos).
- **Los puentes no se verifican todavía.** Hoy el verificador deja que `app` use cualquier carpeta, así que no comprueba que los puentes lean solo `api` ni que estén en la tabla de puentes. ⏳ F1-30 añade esa comprobación junto con los primeros puertos reales.
- El verificador es **estático y aproximado**: detecta rutas `res://` y nombres de clase; no ve referencias dinámicas (`load(variable)`). Por eso se prohíben las rutas construidas en tiempo de ejecución dentro de `src/`.
- Todo esto se valida con código real a partir de la Fase 1.
