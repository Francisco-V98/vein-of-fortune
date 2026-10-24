# 14 · Arquitectura y modularidad

## Requisitos del autor ✅

El proyecto debe ser **muy modular**, sin dependencias directas entre partes, **escalable**, con una buena estructura de *scaffolding*, **independencia** (cambiar algo sin romper otra cosa) y las **mejores prácticas** en diseño y desarrollo, con clean code.

Todo lo que sigue es la forma de cumplirlo. Los principios son requisitos; el diseño concreto está marcado 🟡 y se confirma con los ADR (ver [ADR-0003](adr/0003-arquitectura-modular.md)).

## Principios ✅

1. **Regla de dependencia:** las dependencias apuntan hacia el dominio. El dominio no conoce a nadie.
2. **Alta cohesión, bajo acoplamiento:** cada módulo hace una cosa y se conecta con otros por contratos pequeños.
3. **Dependencias explícitas:** nada se busca en un global; todo se entrega desde fuera (inyección de dependencias).
4. **Datos antes que código:** el contenido (minerales, zonas, eventos, textos) vive en datos validados, no en el código.
5. **Determinismo:** la simulación usa una semilla y un reloj inyectados, para reproducir partidas y errores.
6. **Una razón para cambiar:** una clase, una responsabilidad; un módulo, un propósito.
7. **Composición sobre herencia:** se combinan piezas pequeñas.
8. **Verificación automática:** las reglas se comprueban en CI; lo que no se verifica se erosiona.

## Estructura de `game/` 🟡

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

## Capas dentro de un módulo 🟡

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

## Módulos previstos 🟡

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
| `progression` | Stats por uso, estatus y logros | extraction, shop | [04](04-progresion-y-meta.md) |
| `lifestyle` | Casa, ropa, auto y cosméticos | progression, inventory | [04](04-progresion-y-meta.md) |
| `save` | Guardado versionado, con punto de control por acción y hasta 5 partidas guardables | — | [01](01-core-loop.md), [10](10-tecnico-y-herramientas.md) |
| `telemetry` | Diagnóstico local exportable | — | [10](10-tecnico-y-herramientas.md) |

`world` y `exploration` (✅ 2026-10-24) separan la geografía y el paseo de la economía: `world` decide qué zonas están abiertas o con niebla y cuánto cuesta el viaje (lee el acto de `story` por evento, no depende de él); `exploration` solo conoce posiciones, puertas y el sorteo determinista `hash(partida, día, mina, entrada)` del reparto de entradas. `extraction` consume ese reparto y los cierres de `world_events` (dependencia declarada) por sus `api`, y el dominio no usa nodos ni coordenadas de Godot (la presentación sí). `staff` y `world_events` no cambian de dependencias: los empleados abstraen la entrada y los cierres llegan como eventos.

El casino y los logros entrarán más adelante creando su propio módulo, sin tocar los demás. Los logros llegan a Steam a través del puerto de tienda.

El grafo es **acíclico**: ningún módulo puede depender, directa o indirectamente, de sí mismo (regla A7).

## Cómo se comunican los módulos 🟡

| Mecanismo | Cuándo | Ejemplo |
|---|---|---|
| **API pública** (`api/`) | Pregunta síncrona: "dame un dato ahora" | `shop` pide a `market` el precio de venta actual |
| **Eventos de dominio** | Aviso: "pasó algo", sin saber quién escucha | `market` publica `PrecioCambiado`; `news` lo escucha |

Reglas de los eventos:

- Los define el módulo que los publica, dentro de su `api/`. Quien los escucha depende de esa `api`.
- Son **inmutables**, con nombre en pasado (`DiaAvanzado`, `HuelgaIniciada`) y llevan solo datos.
- Se entregan por un bus pequeño del `kernel`. No se usan para órdenes ("haz esto"): eso va por la API.
- Un evento nunca devuelve resultados a quien lo publica.

## Presentación 🟡

- Las escenas son **tontas**: muestran datos y emiten señales; no tienen reglas del juego.
- Cada pantalla tiene un **presentador** que traduce entre el caso de uso y la vista.
- "Las señales suben, las llamadas bajan": un nodo hijo emite señales; el padre le llama.
- Los textos siempre pasan por el sistema de traducción (ver [10](10-tecnico-y-herramientas.md)).
- La apariencia sale del **tema** de `ui_kit` y de los tokens de diseño derivados de la paleta ([12](12-direccion-de-arte.md)), no de valores sueltos en cada escena.

## Datos y persistencia 🟡

- El contenido se define en archivos de datos con **esquema y validación**; cargar un dato inválido falla de forma clara al arrancar.
- Los identificadores de contenido son **cadenas estables** (`mineral.hierro`), nunca posiciones.
- El guardado usa **DTO versionados** con migraciones, un **punto de control al iniciar cada acción** y hasta **5 partidas guardables** que el jugador elige ([01](01-core-loop.md)). Cada módulo ofrece `snapshot()` y `restore()`; el módulo `save` los reúne a través de la raíz de composición, sin conocerlos.

## Plataforma 🟡

El juego se lanza **primero en PC (Windows y Linux, con Steam)** y el móvil llega después de la 1.0 ([ADR-0009](adr/0009-pc-primero-movil-despues.md)). La arquitectura ya lo prevé: la plataforma son **puertos** con adaptadores intercambiables, así que llevar el juego a otro lugar es añadir adaptadores, no modificar módulos.

| Puerto | Qué cubre | Adaptadores |
|---|---|---|
| Entrada | Acciones (aceptar, cancelar, mover, usar, menú) y detección del último dispositivo | **Ratón y teclado** y **mando** (Steam Deck incluida); **táctil**: adaptador futuro, fase móvil |
| Almacenamiento | Guardados, carpeta de guardados y diagnóstico local | Archivos locales; Steam Auto-Cloud sincroniza esa carpeta (hasta 5 partidas; en Hardcore manda el guardado local) |
| **Plataforma / tienda** | Logros, nube y actualizaciones | Steam (🟡 GodotSteam, [10](10-tecnico-y-herramientas.md)); un adaptador **nulo** para itch.io y pruebas, de modo que el juego corra sin Steam |
| **Pantalla** | Resolución, modo ventana y pantalla completa, escala | Adaptador de PC; ✅ resolución base 640×360 y escala entera con bandas ([10](10-tecnico-y-herramientas.md)) |
| Audio, idioma, reloj | Reproducción, idioma activo, tiempo inyectado | Adaptadores de PC y dobles de pruebas |
| Háptica | Vibración | Vibración del mando; en la fase móvil, la del teléfono |

Reglas:

- Los módulos solo hablan con los **puertos**; el dominio no usa `Input`, `OS` ni `DisplayServer` (símbolos prohibidos que ya vigila el verificador, regla A4).
- Los logros los define el módulo que los otorga y los emite como datos; solo el adaptador de tienda los envía a Steam.
- Nada del dominio sabe que existe Steam. Si Steam no está, el adaptador nulo responde sin hacer nada.
- Los controles (ratón y teclado, mando) viven detrás del puerto de entrada ([10](10-tecnico-y-herramientas.md)).
- El **camino al móvil** consiste en escribir el adaptador táctil, la háptica del teléfono y los de almacenamiento y ciclo de vida de Android e iOS. Para no cerrarlo, ninguna interfaz nueva depende solo del hover.

## Raíz de composición 🟡

`app/` es el único lugar que conoce las implementaciones concretas: crea los módulos, conecta puertos con adaptadores y arranca el juego. Los autoloads se limitan a uno (`App`); el resto se entrega por parámetro.

## Clean code en GDScript ✅

Requisito del autor; el detalle de umbrales es 🟡.

- **Tipado estático en todo:** variables, parámetros y retornos.
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

## Qué se prohíbe 🟡

- Singletons y estado global (salvo `App`).
- Que un módulo use las carpetas internas de otro.
- Lógica de juego en las escenas.
- Que el dominio use `Node`, `Input`, archivos o el árbol de escenas.
- Números y textos del juego escritos dentro del código.
- Clases "dios" y utilidades genéricas sin dueño.
- Dependencias circulares.

## Verificación automática ✅

| Regla | Qué comprueba | Herramienta |
|---|---|---|
| A1 | Capas dentro de un módulo | `tools/arch/check_architecture.py` |
| A2 | Un módulo solo usa la `api` de otro y si lo declara | ídem |
| A3 | El dominio no depende de otros módulos ni de la plataforma | ídem |
| A4 | El dominio no usa clases del motor, entrada ni archivos | ídem |
| A5 | `kernel` no depende de nada fuera de `kernel` | ídem |
| A6 | Solo `app` conoce `platform/adapters` | ídem |
| A7 | El grafo de módulos no tiene ciclos | ídem |
| A8 | Los módulos del código y los declarados coinciden | ídem |
| A9 | Solo los autoloads permitidos | ídem |
| Estilo | Formato y lint de GDScript | `gdformat` y `gdlint` (se instalan en F1-32) |
| Pruebas | Dominio y aplicación, sin interfaz | GUT con Godot sin interfaz (F1-33) |
| Convención | Mensajes de commit | `tools/ci/check_commits.py` |
| Datos | Estado de tareas coherente con su historial | `studio/hub/build.py --strict` |

El verificador de arquitectura ya tiene **22 pruebas automáticas** sobre estructuras de ejemplo. Falta ejecutarlo contra código real de GDScript, que empieza en F1.

## Añadir un módulo 🟡

1. Declararlo en `game/architecture.json` con sus `depends_on` (y su ADR si introduce una decisión nueva).
2. Crear su estructura de carpetas con el generador (tarea F1-28).
3. Escribir primero el dominio y sus pruebas; luego aplicación; después infraestructura y presentación.
4. Exponer solo lo necesario en `api/`.
5. Registrarlo en la raíz de composición.
6. Ejecutar el verificador de arquitectura y las pruebas.

## Límites conocidos ❓

- **GDScript no tiene interfaces.** Los puertos se implementan como clases base abstractas con `assert`/`push_error` y se prueban con dobles. Hay que validar el patrón en Godot real.
- El verificador es **estático y aproximado**: detecta rutas `res://` y nombres de clase; no ve referencias dinámicas (`load(variable)`). Por eso se prohíben las rutas construidas en tiempo de ejecución dentro de `src/`.
- Todo esto se valida con código real a partir de la Fase 1.
