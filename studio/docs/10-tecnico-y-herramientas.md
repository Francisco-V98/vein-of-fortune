# 10 · Técnico y herramientas

## Enfoque ✅

- El proyecto **nace como un proyecto 100 % personal**: se hace para disfrutarlo jugando y construyéndolo. Publicar es una decisión posterior, si el juego resulta divertido.
- Meta inmediata: **algo barato y rápido, aunque no sea bonito, para probar si es divertido**.
- ✅ **PC primero** (autor, 2026-10-15; ver [ADR-0009](adr/0009-pc-primero-movil-despues.md)): el juego se diseña para ratón y teclado, con mando completo, y se lanza en Steam. El móvil llega después de la 1.0. *Esto reemplaza el enfoque anterior de «mobile de verdad» con pantalla táctil y orientación horizontal pensada en los pulgares.*
- ✅ **Pantalla horizontal**, como corresponde a un juego de PC. ✅ Resolución base **640×360** (autor, 2026-10-24; ver [12](12-direccion-de-arte.md) y [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md)).

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

## Arquitectura ✅

Separar en capas, con el contenido en datos:

| Capa | Contenido | Nota |
|---|---|---|
| **Núcleo (simulación)** | Mercado, día/bloques, economía, eventos, contratos, vigilancia, empleados | Código sin interfaz, **simulable offline** durante miles de días |
| **Datos** | Minerales, zonas, herramientas, noticias, facciones, textos | Archivos JSON como fuente, convertidos al arrancar en objetos tipados y validados ([ADR-0013](adr/0013-json-como-fuente-del-contenido.md)); cambiar un precio no toca el código |
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
| Resolución y ventana | ✅ Resolución base 640×360, escala entera con bandas (×3 en 1080p, ×4 en 1440p, ×6 en 4K, ×2 en la Steam Deck), ventana y pantalla completa |

✅ Minijuegos (regla de diseño, consecuencia de [ADR-0009](adr/0009-pc-primero-movil-despues.md)): Picado y Perforación se juegan con un botón (ratón, teclado o mando); Cincelado (trazar) y arrastrar mercancía usan el puntero con ratón y un cursor con el stick con mando. Hay que diseñarlos con ambas variantes desde el inicio. Las variantes táctiles (trazar con el dedo) pasan a la fase móvil.

✅ El mando base (stick mover, A usar, B atrás, Start pausa, View mapa, LB/RB pestañas, stick derecho cursor) y el flujo de pantallas están en [30](30-flujo-de-pantallas.md).

✅ Criterio de aceptación: los controles no se dan por buenos hasta probarlos con un mando real en Windows y en la Steam Deck (⏳ F1-15; nada hecho depende de ello).

## Exploración caminable ✅ (autor, 2026-10-24)

El juego deja de ser solo menús y pasa a tener tres escenas por las que se camina ([ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md)): el **exterior** del asentamiento (vista aérea), el **interior lateral** de cada edificación y la **galería de mina** (vista aérea cenital).

- **Movimiento por acciones:** el paseo usa las acciones de entrada (mover, usar, aceptar, cancelar), nunca teclas ni el ratón directamente, para que el mando (Steam Deck incluida) y un futuro adaptador táctil (⏳ F6-72) funcionen igual. Ocho direcciones; la cámara sigue al personaje y se detiene en los bordes del mapa.
- **Escenas y loader:** entrar a una edificación o a una entrada de mina pasa por un loader corto (fundido de menos de un segundo) y carga la escena de destino; caminar, el loader y el tren **no consumen bloques**. El tiempo real de paseo (unos 40 s por mina) se mide en el prototipo y se absorbe al recalibrar el ritmo por hora.
- **Datos:** cada asentamiento, edificación, interior, recinto y galería es un recurso de datos (trazado, colisiones, puertas, puntos de aparición de menas); el dominio no conoce coordenadas ni nodos de Godot, solo «quién entra a dónde» y el sorteo diario de entradas (ver [14](14-arquitectura-y-modularidad.md)).
- **Estado de partida:** se guarda la zona, la edificación y la posición, pero **solo en puntos seguros** (calle, casa, andén); dentro de una mina no se guarda a mitad de galería (el autoguardado instantáneo se mantiene en los menús y entre bloques).
- **Tren:** una escena base modular con fondos de ventanilla por región, unos 6 s, saltable desde el segundo viaje; se precarga mientras se paga el billete.
- **Rendimiento (Steam Deck y gama baja):** la base 640×360 es ligera; las medidas de cuadros por segundo con una escena de paseo, la niebla (shader sencillo con ruido, sin cálculos por cuadro en el dominio) y el cambio de escena se toman en la matriz de PC y en la Steam Deck con ⏳ F1-44, que fija los límites. Regla de diseño: ningún sorteo, cierre ni cálculo de economía corre dentro de la escena de paseo.

## Arte y sonido

### Pipeline ✅

1. **Prototipo y vertical slice:** formas simples, referencias y sonidos genéricos, todo **provisional** ✅ (política del autor, 2026-10-13). Prioridad: probar la diversión y fallar barato.
2. **Guía de estilo:** paleta, resolución base, tamaño de píxel, reglas de contorno y sombreado.
3. **Producción definitiva:** pixel art con **PixelLab**, blips y audio finales, solo después de que el vertical slice pase las pruebas y la Puerta B ✅. Los assets comprados o gratuitos, si se usan, llevan licencia clara.
4. **Registro de licencias** de todo lo que entra, incluido lo provisional (ver [11](11-legal-y-cumplimiento.md)).

Detalle de la política y del flujo en [12](12-direccion-de-arte.md), sección «Assets provisionales y definitivos».

### Prueba de estilo ✅ (realizada; ver [12](12-direccion-de-arte.md))

Antes de comprometerse con un estilo: una pantalla de mina, un personaje, 5 íconos de minerales y un teletipo de mercado. Se evalúan coherencia, calidad y costo de producir en serie.

### Audio ✅ (autor, 2026-10-24)

- Referencia sonora: Balatro.
- **Voces:** solo sonidos cortos tipo «blip» por personaje; **nunca habrá voces reales de personas**. Cada personaje tiene una semilla fija, guardada en el repositorio, para que su blip sea siempre el mismo.
- **Efectos y blips (ruta gratuita por defecto):** `bfxr-mcp` (motor MIT, sin IA, nada que declarar en Steam). Plan B si el MCP no pasa la revisión de licencia: jfxr o bfxr a mano.
- **Música:** la compone el autor en LMMS (gratis; la GPL del programa no afecta a su música; se revisan los samples incluidos), sin integración MCP.
- **Opcional:** REAPER (60 USD con descuento si los ingresos brutos son de hasta 20.000 USD al año) con `reaper-mcp` (MIT), solo si el autor quiere apoyo técnico de mezcla, masterización o cuantizado.
- **Sin ElevenLabs ni música por IA.** Claude puede proponer ideas de melodía como texto o notas; el autor decide, y lo que Claude proponga y se use tal cual se registra y se declara en Steam como IA.
- Cada herramienta se prueba en F3-21; F4-232 usa la herramienta fijada allí. Antes de pagar o usar una herramienta se reconfirman sus términos en la página oficial y se guarda una captura en el registro de licencias.
- **Accesibilidad:** cada sonido importante lleva un equivalente visual, para no bloquear el avance con el audio silenciado.

## Localización (español e inglés desde el inicio) ✅

El juego se hace en **español e inglés desde el principio**, con un marco que permita sumar más idiomas sin tocar el código.

| Aspecto | Decisión |
|---|---|
| Voz | Español neutro latinoamericano con **tuteo**; en inglés, tono igual de cercano |
| Formato de traducciones ✅ | Archivos `.po` (gettext) que Godot soporta de forma nativa, con contexto y plurales |
| Cadenas | **Ninguna cadena fija** en el código ni dentro del arte; el arte no lleva texto incrustado |
| Variables | Marcadores con nombre (por ejemplo `{nombre}`), no posicionales; el género gramatical se resuelve con textos neutros y variantes solo cuando haga falta |
| Longitud | El español ocupa entre 20 y 30 % más que el inglés; la interfaz debe tolerarlo (prueba con pseudo-localización) |
| Fuentes | Pixel con caracteres latinos extendidos (á, ñ, ¿, ¡) y **fuentes de respaldo por idioma** para el futuro |
| Números y fechas | Formato según el idioma |
| Flujo ✅ | Extraer cadenas, traducir con asistencia de IA, revisar con un glosario ES/EN y compilar (⏳ F1-20). Los textos y traducciones asistidos por IA se declaran en Steam ([11](11-legal-y-cumplimiento.md)) |
| Herramientas ✅ | Edición de `.po` con un editor como Poedit (opcional); una plataforma de traducción (por ejemplo Weblate o Crowdin) solo si más adelante hay colaboradores |
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
- Repositorio **público** en GitHub (desde F0-35): sin secretos ni datos personales, y el arte provisional generado con IA queda marcado como tal.

## Exportación y Steam ✅

| Tema | Propuesta |
|---|---|
| Exportación | Plantillas de Godot para Windows y Linux, generadas por línea de comandos (sin abrir el editor), con build reproducible: misma fuente y misma versión de Godot, mismo resultado (F1-26) |
| Steamworks | **GodotSteam** (decisión del autor, 2026-10-24; licencia verificada en F1-45) detrás del puerto de plataforma/tienda ([14](14-arquitectura-y-modularidad.md)); sin Steam el juego debe arrancar igual (itch.io y pruebas): el adaptador nulo siempre está disponible |
| Nube | Steam Auto-Cloud ✅ (ver «Seguridad y protección de datos») |
| Logros | Se conectan al módulo de logros por el puerto de tienda; el módulo no conoce a Steam |
| Subida de builds | Herramienta de línea de comandos de Steam (`steamcmd`) desde un equipo de publicación; las credenciales fuera del repositorio |

✅ La integración de Steamworks ya tiene tareas: ⏳ F1-45 (GodotSteam y su licencia), F4-234, F4-235 (logros), F4-236, F4-239 (Steam Deck: texto de al menos 6 px de fuente base, ×2 = 12 px; también en F1-44), F5-22 y F5-40. Nada hecho depende de ellas.

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
| **B · Steam** ✅ | Lo que entregue Steam sobre cierres y rendimiento, sin SDK propio en el juego; el alcance real se verifica en la fuente vigente en F5-40. *Antes era Google Play Vitals, que pasa a la fase móvil* ([ADR-0007](adr/0007-telemetria-por-capas.md)) | Al publicar o en pruebas |
| **C · Envío opcional** | Con consentimiento explícito y datos anónimos, a un servidor propio | Idea futura; cambia la política de privacidad y los formularios |

Reglas de la capa A:

- ID anónimo y reiniciable; **sin** nombre del jugador ni de la tienda.
- Nada se envía automáticamente.
- Detalle ampliado solo en versiones de pruebas.
- Un cierre nativo no puede registrarse a sí mismo: se detecta con una **marca de cierre no limpio** al siguiente arranque.

Qué muestra el panel: rendimiento por equipo, errores, estabilidad, economía (curva de dinero, abandono por día, éxito en minijuegos, muertes en hardcore) e informes del simulador de mercado.

## Seguridad y protección de datos ✅

Principio: **reducir la superficie de ataque y los datos que se manejan**.

### Decisiones para la v1 ✅

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
| Repositorio | Público (F0-35), sin secretos; copias de respaldo |

### Si en el futuro hay nube o cuentas ✅ (regla de contingencia; la v1 no tiene cuentas)

- Usar el inicio de sesión de la plataforma (Steam; en el móvil, Google Play Games o Sign in with Apple); **no guardar contraseñas propias**.
- Cifrado en tránsito, mínimo de datos, política de privacidad actualizada.
- Ampliar la revisión legal ([11](11-legal-y-cumplimiento.md)).

## Calidad y pruebas

- **Núcleo:** pruebas automáticas y simulaciones de balance.
- **Interfaz y minijuegos:** pruebas manuales en un PC Windows real y, si la hay, en la Steam Deck; una lista de verificación por versión.
- **Integración continua:** exportación a Windows y Linux ✅ y build reproducible por línea de comandos (F1-26); el detalle está en [15](15-flujo-de-trabajo-y-calidad.md).
- **Control de versiones:** Git, repositorio público (sin secretos), commits frecuentes.

## Trabajar con IA ✅

- Presupuesto: plan Max de Claude como base (confirmado por el autor, 2026-10-24); el ahorro de tokens sigue [ADR-0010](adr/0010-politica-de-modelos-y-autorizacion-de-fable.md); ampliar si el proyecto avanza.
- Por eso conviene dividir el trabajo en **tareas pequeñas y bien definidas** (ver el tablero de tareas): menos contexto por sesión, menos consumo, mejores resultados.
- Yo escribo y reviso el código; **el jugador valida la diversión y el "feel"** jugando en PC.

## Cerebro del proyecto en Obsidian ✅

- **Qué es:** un vault de Obsidian **generado** desde el repo (documentos, datos, tareas, equipo y memoria) en `studio/cerebro/`, ignorado por git, de solo lectura y con unas 2.000 notas atómicas enlazadas (una por sección «##» de cada documento y una por entidad: tareas, personajes, minerales, zonas, edificaciones, decisiones, hilos, escenas, finales, términos del glosario, casos de QA, reglas del simulador, piezas de arte). Decisión del autor del 2026-10-23.
- **Cómo se alimenta:** `python3 studio/hub/build.py` lo regenera entero en cada ejecución (menos de un segundo; `--sin-cerebro` lo salta). Los documentos y datos siguen siendo la fuente de verdad: lo que se cambie dentro de `generado/` se pierde. Tus notas van en `mis-notas/` y la configuración en `.obsidian/`; el generador nunca las toca.
- **Cómo se usa:** abre la carpeta `studio/cerebro` como vault en Obsidian y empieza por la nota «00 Inicio». Cada nota guarda su `id` estable y su nombre legible; el grafo tiene colores por tipo y una vista guardada que oculta el backlog de F1 a F6. El código está en `tools/cerebro/` (ver su README).
- Ahorra poco o nada en tokens: sirve para ver y navegar el proyecto. Para consultar sin leer documentos enteros se usa `tools/consulta.py` (✅ comandos `limpieza`, `abiertos`, `indice`, `seccion`, `ficha`, `tarea`, `mundo`).

## Buenas prácticas por área ✅

Revisión del 2026-10-24 contra las prácticas habituales de cada área; las aplica la tarea que se cita, sin cambiar decisiones del autor.

| Área | Práctica |
|---|---|
| Git y binarios | `.gitattributes` con normalización de fin de línea (`* text=auto`, `eol=lf` en código y datos) y los binarios marcados; con Git LFS solo si el arte definitivo (PixelLab) y el audio hacen crecer el repositorio (la decisión se toma en ⏳ F4-227, al entrar el arte; hasta entonces no hace falta). Los originales pesados (hojas de sprites en capas, audio sin comprimir) viven fuera del repositorio público |
| Godot en Git | Se versionan `project.godot`, escenas y recursos en texto (`.tscn`, `.tres`); la carpeta `.godot/` y las exportaciones van en `.gitignore`; la versión de Godot se fija en un solo archivo y la usan la CI y el equipo |
| CI y builds | Exportación sin cabeza (`--headless --export-release`) con la versión de Godot y las plantillas fijadas, caché de plantillas, artefactos con la versión y el commit, y pruebas antes de exportar (F1-26) |
| Exportación | Perfiles de exportación en el repositorio sin credenciales; Windows x86_64 y Linux x86_64; el Linux se prueba en la Steam Deck (Proton solo como respaldo); Windows se publica **sin firmar** hasta decidir en ⏳ F5-22 (recomendación aceptada por defecto) y se avisa en la ficha |
| Localización | Claves de texto estables y contexto para el traductor; pseudo-localización en la CI; los plurales y marcadores con nombre se prueban con casos fijos; el `.pot` se regenera en la CI y falla si hay cadenas sin extraer (F1-16) |
| Assets y licencias | Un registro único (origen, licencia, fecha, herramienta y si es IA) por cada archivo que entra; la CI falla si entra un archivo sin fila en el registro; el arte provisional con IA queda marcado |
| Secretos | Variables de entorno o secretos de la CI, nunca en archivos del repositorio; revisión automática de secretos antes de cada commit y en la CI; los tokens de MCP y de Steam solo en configuración local fuera de git; si se filtra uno, se revoca y se rota |
| Pruebas | Pirámide: núcleo con pruebas automáticas deterministas (semilla fija), simulaciones de balance, escenas con pruebas de humo y lista manual por versión; ningún fallo conocido se corrige sin una prueba que lo cubra |
| Rendimiento (Steam Deck) | Presupuesto de cuadro (16,6 ms a 60 fps) medido en la Deck y no solo en el PC; límite de 40 o 60 fps y ahorro de batería opcional; suspensión y reanudación probadas (⏳ F1-44); texto de al menos 6 px de fuente base |
| IA y MCP | El agente trabaja en ramas y PR revisados por el autor; los servidores MCP se limitan a lo necesario y con permisos mínimos; no se pega código ni datos con secretos en una sesión; lo que genera la IA se declara cuando corresponde ([11](11-legal-y-cumplimiento.md)) |

Descartadas por ahora: firmar el ejecutable de Windows antes de la 1.0 (cuesta dinero y no bloquea Steam; se decide en F5-22, mientras tanto sin firmar) y mover los guardados a un servidor propio (contradice la v1 sin cuentas).

## Pendiente

- ✅ Godot 4.x con GDScript confirmado por el autor el 2026-10-11.
- ✅ Estructura de carpetas de `game/`: la del [documento 14](14-arquitectura-y-modularidad.md), adoptada tal cual (autor, 2026-10-24); los cambios futuros van por ADR.
- ✅ Herramienta del arte definitivo: PixelLab (autor, 2026-10-13; ver [12](12-direccion-de-arte.md)).
- ✅ Herramientas de audio: bfxr-mcp para efectos y blips, LMMS para la música del autor, REAPER opcional (autor, 2026-10-24; ver «Audio»).
- ✅ PC Windows real para pruebas: el autor ya lo tiene (2026-10-24); requisito de F1 cumplido.
- ✅ Resolución base 640×360 y escala entera con bandas (autor, 2026-10-24; cierra F1-06).
- ✅ Hub de documentación y tablero de tareas: hechos (F0-14, F0-15; ver [06](06-roadmap-y-pendientes.md)).
