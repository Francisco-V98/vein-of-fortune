# 10 · Técnico y herramientas

## Enfoque ✅

- El proyecto **nace como un proyecto 100 % personal**: se hace para disfrutarlo jugando y construyéndolo. Publicar es una decisión posterior, si el juego resulta divertido.
- Meta inmediata: **algo barato y rápido, aunque no sea bonito, para probar si es divertido**.
- ✅ **PC primero** (autor, 2026-10-15; ver [ADR-0009](adr/0009-pc-primero-movil-despues.md)): el juego se diseña para ratón y teclado, con mando completo, y se lanza en Steam. El móvil llega después de la 1.0. *Esto reemplaza el enfoque anterior de «mobile de verdad» con pantalla táctil y orientación horizontal pensada en los pulgares.*
- ✅ **Pantalla horizontal**, como corresponde a un juego de PC. Resolución y modo ventana: ⏳ F1-06.

## Plataformas ✅

Decisión del autor (2026-10-15), con su ADR en [ADR-0009](adr/0009-pc-primero-movil-despues.md):

| Orden | Plataforma | Nota |
|---|---|---|
| 1 | **Windows** y **Linux** (PC) | Lanzamiento de la 1.0. Steam como meta; itch.io para builds de prueba. GOG y Epic quedan fuera de la 1.0 |
| 1 | **Steam Deck** | Se apunta a *Verified*: mando completo, sin HUD táctil, texto legible en 1280×800 |
| 2 | macOS | Después de la 1.0 |
| 3 | **Móvil** (Android e iOS) | Empieza cuando la 1.0 esté publicada y estable en Steam; ver «Fase móvil (después de la 1.0)». Las actualizaciones V2.x (casino, casas, pesca) pueden seguir en PC o ir también a móvil |
| 4 | Consola | Futuro lejano |

Pruebas ✅: en un **PC Windows real** (el autor lo tiene o lo consigue) y en la Steam Deck si la hay. Es un requisito de F1; el autor trabaja en Mac y no basta con probar allí.

## Motor ✅ (confirmado el 2026-10-11)

**Godot 4.x** con GDScript.

Por qué:

- Proyectos en **texto** (escenas y scripts legibles), lo que facilita que la IA los edite y los revise.
- Excelente para 2D y pixel art, con mucha interfaz.
- Gratis, sin regalías, editor liviano.
- Exporta a Windows y Linux (la 1.0), y más adelante a macOS, Android e iOS.

Riesgo asumido: la ruta a consolas es menos directa que en Unity (requiere herramientas o socios de terceros). Se reevalúa si las consolas pasan a ser prioridad.

## Arquitectura 🟡

Separar en capas, con el contenido en datos:

| Capa | Contenido | Nota |
|---|---|---|
| **Núcleo (simulación)** | Mercado, día/bloques, economía, eventos, contratos, vigilancia, empleados | Código sin interfaz, **simulable offline** durante miles de días |
| **Datos** | Minerales, zonas, herramientas, noticias, facciones, textos | Archivos de datos (JSON/recursos); cambiar un precio no toca el código |
| **Interfaz** | Pantallas, minijuegos, HUD | Consume el núcleo, no contiene reglas |
| **Entrada** | Ratón y teclado, y mando; el táctil queda como adaptador futuro | Capa de acciones (ver abajo) |
| **Guardado** | Persistencia | Versionado, con migraciones. Punto de control al iniciar cada acción y hasta 5 partidas guardables a elegir ✅ ([01](01-core-loop.md)) |
| **Plataforma** | Windows y Linux (Steam); móvil más adelante | Tienda (logros, nube, actualizaciones), pantalla (resolución, ventana), ciclo de vida |

Principios:

- **Semilla (seed)** para todo lo procedural, para reproducir partidas y bugs.
- **Pruebas automáticas** del núcleo y **simulador de mercado** que se ejecuta sin abrir el juego, para calibrar precios, volatilidad, multas y sumideros.
- Todo el contenido (minerales, zonas, eventos) en datos desde el inicio.

## Controles ✅

Decisión del autor (2026-10-15): **ratón y teclado son los controles principales** (hover, tooltips, atajos y ventanas de información densas) y el **mando está completo** (necesario para la Steam Deck *Verified*). La interfaz táctil queda como un **adaptador futuro** para el móvil; **no se construye HUD táctil ahora**.

| Aspecto | Regla |
|---|---|
| Capa de acciones | El juego se programa contra **acciones** (aceptar, cancelar, mover, usar, menú) y no contra botones concretos |
| Adaptadores | Ratón y teclado, y mando; el táctil se añadirá en la fase móvil sin tocar módulos ([14](14-arquitectura-y-modularidad.md)) |
| Detección | Detecta el último dispositivo usado (ratón y teclado, o mando) y cambia solo |
| Hover y tooltips | Información secundaria al pasar el cursor y atajos de teclado; **nada esencial depende solo del hover**, porque con mando no existe |
| Navegación | Todos los menús navegables por **foco** (teclado y mando) |
| Íconos | Los glifos de botones cambian según el dispositivo y el tipo de mando |
| Vibración | Vibración del mando cuando exista |
| Reasignación | Mapeo configurable (a futuro) |
| Resolución y ventana | Resolución base, escala entera con bandas, ventana y pantalla completa: ⏳ F1-06 |

🟡 Minijuegos: Picado y Perforación se juegan con un botón (ratón, teclado o mando); Cincelado (trazar) y arrastrar mercancía usan el puntero con ratón y un cursor con el stick con mando. Hay que diseñarlos con ambas variantes desde el inicio. Las variantes táctiles (trazar con el dedo) pasan a la fase móvil.

🟡 Probar con un mando real en Windows y en la Steam Deck antes de dar por buenos los controles (F1-15).

## Arte y sonido

### Pipeline 🟡

1. **Prototipo y vertical slice:** formas simples, referencias y sonidos genéricos, todo **provisional** ✅ (política del autor, 2026-10-13). Prioridad: probar la diversión y fallar barato.
2. **Guía de estilo:** paleta, resolución base, tamaño de píxel, reglas de contorno y sombreado.
3. **Producción definitiva:** pixel art con **PixelLab**, voces y audio finales, solo después de que el vertical slice pase las pruebas y la Puerta B ✅. Los assets comprados o gratuitos, si se usan, llevan licencia clara.
4. **Registro de licencias** de todo lo que entra, incluido lo provisional (ver [11](11-legal-y-cumplimiento.md)).

Detalle de la política y del flujo en [12](12-direccion-de-arte.md), sección «Assets provisionales y definitivos».

### Prueba de estilo ✅ (realizada; ver [12](12-direccion-de-arte.md))

Antes de comprometerse con un estilo: una pantalla de mina, un personaje, 5 íconos de minerales y un teletipo de mercado. Se evalúan coherencia, calidad y costo de producir en serie.

### Audio 🟡

- Referencia sonora: Balatro.
- Voces: sonidos cortos tipo "blip" por personaje; voces reales como mejora futura.
- Revisar los términos de uso comercial de cada herramienta o banco de sonidos.

## Localización (español e inglés desde el inicio) ✅

El juego se hace en **español e inglés desde el principio**, con un marco que permita sumar más idiomas sin tocar el código.

| Aspecto | Decisión |
|---|---|
| Voz | Español neutro latinoamericano con **tuteo**; en inglés, tono igual de cercano |
| Formato de traducciones 🟡 | Archivos `.po` (gettext) que Godot soporta de forma nativa, con contexto y plurales |
| Cadenas | **Ninguna cadena fija** en el código ni dentro del arte; el arte no lleva texto incrustado |
| Variables | Marcadores con nombre (por ejemplo `{nombre}`), no posicionales; el género gramatical se resuelve con textos neutros y variantes solo cuando haga falta |
| Longitud | El español ocupa entre 20 y 30 % más que el inglés; la interfaz debe tolerarlo (prueba con pseudo-localización) |
| Fuentes | Pixel con caracteres latinos extendidos (á, ñ, ¿, ¡) y **fuentes de respaldo por idioma** para el futuro |
| Números y fechas | Formato según el idioma |
| Flujo 🟡 | Extraer cadenas, traducir con asistencia de IA, revisar con un glosario ES/EN y compilar |
| Herramientas 🟡 | Edición de `.po` con un editor como Poedit; una plataforma de traducción (por ejemplo Weblate o Crowdin) solo si más adelante hay colaboradores |
| Idiomas futuros | Portugués, francés, alemán u otros. Los idiomas de derecha a izquierda exigen espejar la interfaz y quedan fuera de alcance por ahora |
| Tienda | Ficha de Steam y capturas en ES y EN |
| Documentos de `studio/` | Siguen en español; solo el juego y la ficha de tienda son bilingües |

Los sonidos "blip" de los personajes no dependen del idioma, lo que facilita la localización.

## Estructura del repositorio ✅

Un solo repositorio con dos mundos separados:

```
<nombre>/
├── game/       el juego (proyecto Godot)
├── studio/     documentos, roadmap, tareas, evidencias, hub y métricas
└── README.md
```

- `game/` **compila sin** `studio/`, y `studio/` **no importa** nada de `game/` (solo lee archivos de diagnóstico exportados).
- `studio/` se puede **ignorar** con una línea en `.gitignore` o **extraer con su historial** a otro repositorio con `git subtree split`.
- Repositorio **privado** en GitHub.

## Exportación y Steam 🟡

| Tema | Propuesta |
|---|---|
| Exportación | Plantillas de Godot para Windows y Linux, generadas por línea de comandos (sin abrir el editor), con build reproducible: misma fuente y misma versión de Godot, mismo resultado (F1-26) |
| Steamworks | **GodotSteam** detrás del puerto de plataforma/tienda ([14](14-arquitectura-y-modularidad.md)); sin Steam el juego debe arrancar igual (itch.io y pruebas) |
| Nube | Steam Auto-Cloud ✅ (ver «Seguridad y protección de datos») |
| Logros | Se conectan al módulo de logros por el puerto de tienda; el módulo no conoce a Steam |
| Subida de builds | Herramienta de línea de comandos de Steam (`steamcmd`) desde un equipo de publicación; las credenciales fuera del repositorio |

🟡 Falta una tarea del roadmap que integre Steamworks y fije la herramienta exacta (GodotSteam u otra); hay que crearla antes de la página de Steam (final de F4). Hasta que exista, esta propuesta sigue abierta y no se aplaza a ninguna tarea.

## Fase móvil (después de la 1.0)

Empieza cuando la 1.0 esté publicada y estable en Steam ([ADR-0009](adr/0009-pc-primero-movil-despues.md)). Todo lo que sigue se conserva del plan anterior de «Android primero» y se retoma entonces.

| Tema | Contenido |
|---|---|
| Exportación a Android | Instalar **JDK** y **Android SDK**, crear una **keystore** de debug y configurar la exportación; generar el **APK** (y el paquete de tienda) por línea de comandos |
| Versionado | `versionCode` que solo crece y `versionName` igual a la versión del juego ([15](15-flujo-de-trabajo-y-calidad.md)) |
| Pantalla | Orientación horizontal, interfaz con los pulgares en los bordes y **zona segura** (muescas, bordes redondeados, proporciones como 20:9) |
| Entrada | Adaptador **táctil** con HUD táctil que se oculta al usar mando; minijuegos con el dedo (trazar, arrastrar) y háptica |
| Permisos | Los mínimos posibles (idealmente solo vibración) |
| Copias de seguridad | Decidir de forma consciente si los guardados entran en el backup de Android |
| Firma | La clave de firma se respalda **fuera del repo**; perderla puede impedir actualizaciones. Usar la firma gestionada por Google Play |
| Telemetría | **Google Play Vitals** como capa B del móvil (cierres, arranque, batería, renderizado lento) |
| iOS | Solo si todo va bien. Se puede probar en el simulador de Xcode en Mac, pero no reemplaza a un dispositivo real, y publicar requiere cuenta de pago |
| Idioma | Idioma inicial según el del dispositivo |
| Pruebas | Dispositivo Android propio, tres gamas y mandos Bluetooth ([16](16-calidad-y-qa.md), «Fase móvil») |

## Telemetría por capas ✅

Se puede medir un juego sin conexión. Tres capas, en este orden:

| Capa | Cómo | Cuándo |
|---|---|---|
| **A · Local y exportable** | El juego guarda rendimiento, errores y eventos en un archivo local sin datos personales; el probador lo exporta y se carga en el panel de `studio/` | Desde la Fase 2 |
| **B · Steam** 🟡 | Lo que entregue Steam sobre cierres y rendimiento, sin SDK propio en el juego; el alcance real se verifica en la fuente vigente en F5-40. *Antes era Google Play Vitals, que pasa a la fase móvil* ([ADR-0007](adr/0007-telemetria-por-capas.md)) | Al publicar o en pruebas |
| **C · Envío opcional** | Con consentimiento explícito y datos anónimos, a un servidor propio | Idea futura; cambia la política de privacidad y los formularios |

Reglas de la capa A:

- ID anónimo y reiniciable; **sin** nombre del jugador ni de la tienda.
- Nada se envía automáticamente.
- Detalle ampliado solo en versiones de pruebas.
- Un cierre nativo no puede registrarse a sí mismo: se detecta con una **marca de cierre no limpio** al siguiente arranque.

Qué muestra el panel: rendimiento por equipo, errores, estabilidad, economía (curva de dinero, abandono por día, éxito en minijuegos, muertes en hardcore) e informes del simulador de mercado.

## Seguridad y protección de datos ✅

Principio: **reducir la superficie de ataque y los datos que se manejan**.

### Decisiones para la v1 🟡

| Tema | Decisión |
|---|---|
| Cuentas y autenticación | **Sin cuentas en la v1**: juego offline, sin servidores propios. Nada que autenticar |
| Datos personales | Casi ninguno: el nombre del personaje y de la tienda son locales y no salen del equipo (Steam Auto-Cloud sincroniza los guardados con la cuenta de Steam, no con servidores propios) |
| Anuncios y analíticas de terceros | **Ninguno en la v1** (pago único); cada SDK trae recolección de datos y obligaciones |
| Guardado | Formato versionado, escritura segura (archivo temporal y reemplazo), copia de respaldo y verificación de integridad para detectar corrupción. **Autoguardado instantáneo**: la Steam Deck suspende el juego en cualquier momento. Cada una de las hasta 5 partidas guardables tiene su propio archivo y su punto de control ✅ ([01](01-core-loop.md)) |
| Nube y partidas ✅ | **Steam Auto-Cloud** con una carpeta de guardados pequeños y hasta **5 partidas**. En **Hardcore manda el guardado local**: no se puede restaurar desde la nube tras morir |
| Trampas | En un juego de un jugador no es prioridad. Una verificación ligera solo evita corrupción accidental |
| Validación de entradas | Nombre y tienda con límite de longitud, caracteres permitidos y filtro de palabras ofensivas |
| Permisos y acceso a archivos | El juego solo escribe en su carpeta de guardados y de diagnóstico |
| Dependencias | Pocas, con versión fijada, de fuentes confiables; revisar licencias |
| Secretos | **Nunca en el repositorio** (claves, tokens, contraseñas) |
| Claves de Steam | Las claves de Steamworks y cualquier credencial de publicación **no entran en el repositorio** |
| Compra del juego | Gestionada por Steam (pago único); no se implementa validación propia |
| Repositorio | Privado, con copias de respaldo |

### Si en el futuro hay nube o cuentas 🟡

- Usar el inicio de sesión de la plataforma (Steam; en el móvil, Google Play Games o Sign in with Apple); **no guardar contraseñas propias**.
- Cifrado en tránsito, mínimo de datos, política de privacidad actualizada.
- Ampliar la revisión legal ([11](11-legal-y-cumplimiento.md)).

## Calidad y pruebas

- **Núcleo:** pruebas automáticas y simulaciones de balance.
- **Interfaz y minijuegos:** pruebas manuales en un PC Windows real y, si la hay, en la Steam Deck; una lista de verificación por versión.
- **Integración continua:** exportación a Windows y Linux 🟡 y build reproducible por línea de comandos (F1-26); el detalle está en [15](15-flujo-de-trabajo-y-calidad.md).
- **Control de versiones:** Git, repositorio privado, commits frecuentes.

## Trabajar con IA 🟡

- Presupuesto: plan Max de Claude; ampliar si el proyecto avanza.
- Por eso conviene dividir el trabajo en **tareas pequeñas y bien definidas** (ver el tablero de tareas): menos contexto por sesión, menos consumo, mejores resultados.
- Yo escribo y reviso el código; **el jugador valida la diversión y el "feel"** jugando en PC.

## Pendiente

- ✅ Godot 4.x con GDScript confirmado por el autor el 2026-10-11.
- ❓ Estructura de carpetas del proyecto del juego.
- ✅ Herramienta del arte definitivo: PixelLab (autor, 2026-10-13; ver [12](12-direccion-de-arte.md)).
- ❓ Herramientas concretas de audio.
- ❓ Un PC Windows real para pruebas (requisito de F1): el autor lo tiene o lo consigue.
- ⏳ F1-06 · Resolución base y modo ventana.
- ❓ Hub de documentación y tablero de tareas (ver [06](06-roadmap-y-pendientes.md)).
