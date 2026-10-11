# 10 · Técnico y herramientas

## Enfoque ✅

- El proyecto **nace como un proyecto 100 % personal**: se hace para disfrutarlo jugando y construyéndolo. Publicar es una decisión posterior, si el juego resulta divertido.
- Meta inmediata: **algo barato y rápido, aunque no sea bonito, para probar si es divertido**.
- Mobile de verdad (no un port): se diseña para pantalla táctil desde el inicio.
- ✅ **Orientación horizontal (landscape)**. Hay que diseñar la interfaz pensando en los pulgares en los bordes y en la zona segura de la pantalla (muescas, bordes redondeados).

## Plataformas ✅

| Orden | Plataforma | Nota |
|---|---|---|
| 1 | **Android** | Dispositivo propio para pruebas |
| 2 | iOS | Solo si todo va bien. Se puede probar en el simulador de iOS (Xcode) en Mac, pero no reemplaza a un dispositivo real, y publicar requiere cuenta de pago |
| 3 | PC (Steam) | Futuro |
| 4 | Consola | Futuro lejano |

## Motor 🟡 (recomendación, pendiente de confirmar)

**Godot 4.x** con GDScript.

Por qué:

- Proyectos en **texto** (escenas y scripts legibles), lo que facilita que la IA los edite y los revise.
- Excelente para 2D y pixel art, con mucha interfaz.
- Gratis, sin regalías, editor liviano.
- Exporta a Android e iOS, y a PC.

Riesgo asumido: la ruta a consolas es menos directa que en Unity (requiere herramientas o socios de terceros). Se reevalúa si las consolas pasan a ser prioridad.

## Arquitectura 🟡

Separar en capas, con el contenido en datos:

| Capa | Contenido | Nota |
|---|---|---|
| **Núcleo (simulación)** | Mercado, día/bloques, economía, eventos, contratos, vigilancia, empleados | Código sin interfaz, **simulable offline** durante miles de días |
| **Datos** | Minerales, zonas, herramientas, noticias, facciones, textos | Archivos de datos (JSON/recursos); cambiar un precio no toca el código |
| **Interfaz** | Pantallas, minijuegos, HUD | Consume el núcleo, no contiene reglas |
| **Entrada** | Táctil y mando | Capa de acciones (ver abajo) |
| **Guardado** | Persistencia | Versionado, con migraciones |
| **Plataforma** | Android/iOS/PC | Permisos, vibración, ciclo de vida |

Principios:

- **Semilla (seed)** para todo lo procedural, para reproducir partidas y bugs.
- **Pruebas automáticas** del núcleo y **simulador de mercado** que se ejecuta sin abrir el juego, para calibrar precios, volatilidad, multas y sumideros.
- Todo el contenido (minerales, zonas, eventos) en datos desde el inicio.

## Controles ✅

Se juega con **pantalla táctil o con mando**. Cuando hay mando, todo está mapeado y el **HUD táctil se oculta**.

| Aspecto | Regla |
|---|---|
| Capa de acciones | El juego se programa contra **acciones** (aceptar, cancelar, mover, usar, menú) y no contra botones concretos |
| Detección | Detecta el último dispositivo usado (toque o mando) y cambia solo |
| HUD táctil | Visible solo con táctil; se oculta al usar mando |
| Navegación | Todos los menús navegables por **foco** (mando y teclado en PC) |
| Íconos | Los glifos de botones cambian según el tipo de mando |
| Vibración | Háptica en el teléfono; vibración del mando cuando exista |
| Reasignación | Mapeo configurable (a futuro) |

🟡 Minijuegos con mando: Picado y Perforación se juegan con un botón; Cincelado (trazar) y arrastrar mercancía usan un cursor con el stick. Hay que diseñarlos con ambas variantes desde el inicio.

🟡 Probar con un mando Bluetooth en Android antes de dar por buenos los controles.

## Arte y sonido

### Pipeline 🟡

1. **Prototipo (Fase 1):** formas simples y placeholders; sonidos genéricos. Prioridad: probar la diversión.
2. **Guía de estilo:** paleta, resolución base, tamaño de píxel, reglas de contorno y sombreado.
3. **Producción:** mezcla de **arte propio** (el autor tiene conocimientos de diseño), **assets comprados o gratuitos con licencia clara** y **generación con IA** retocada a mano para mantener la coherencia.
4. **Registro de licencias** de todo lo que entra (ver [11](11-legal-y-cumplimiento.md)).

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
| Tienda | Fichas de tienda y capturas en ES y EN |
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

## Telemetría por capas ✅

Se puede medir un juego sin conexión. Tres capas, en este orden:

| Capa | Cómo | Cuándo |
|---|---|---|
| **A · Local y exportable** | El juego guarda rendimiento, errores y eventos en un archivo local sin datos personales; el probador lo exporta y se carga en el panel de `studio/` | Desde la Fase 2 |
| **B · Google Play Vitals** | Cierres, bloqueos, arranque, batería y renderizado lento los entrega Google Play, sin SDK en el juego | Al publicar o en pruebas cerradas |
| **C · Envío opcional** | Con consentimiento explícito y datos anónimos, a un servidor propio | Idea futura; cambia la política de privacidad y los formularios |

Reglas de la capa A:

- ID anónimo y reiniciable; **sin** nombre del jugador ni de la tienda.
- Nada se envía automáticamente.
- Detalle ampliado solo en versiones de pruebas.
- Un cierre nativo no puede registrarse a sí mismo: se detecta con una **marca de cierre no limpio** al siguiente arranque.

Qué muestra el panel: rendimiento por dispositivo, errores, estabilidad, economía (curva de dinero, abandono por día, éxito en minijuegos, muertes en hardcore) e informes del simulador de mercado.

## Seguridad y protección de datos ✅

Principio: **reducir la superficie de ataque y los datos que se manejan**.

### Decisiones para la v1 🟡

| Tema | Decisión |
|---|---|
| Cuentas y autenticación | **Sin cuentas en la v1**: juego offline, sin servidores propios. Nada que autenticar |
| Datos personales | Casi ninguno: el nombre del personaje y de la tienda son locales y no salen del dispositivo |
| Anuncios y analíticas de terceros | **Ninguno en la v1** (pago único); cada SDK trae recolección de datos y obligaciones |
| Guardado | Formato versionado, escritura segura (archivo temporal y reemplazo), copia de respaldo y verificación de integridad para detectar corrupción |
| Trampas | En un juego de un jugador no es prioridad. Una verificación ligera solo evita corrupción accidental |
| Validación de entradas | Nombre y tienda con límite de longitud, caracteres permitidos y filtro de palabras ofensivas |
| Permisos de Android | El mínimo posible (idealmente solo vibración) |
| Copias de seguridad de Android | Decidir de forma consciente si los guardados entran en el backup del sistema |
| Dependencias | Pocas, con versión fijada, de fuentes confiables; revisar licencias |
| Secretos | **Nunca en el repositorio** (claves, tokens, contraseñas) |
| Firma de la app | La clave de firma se respalda **fuera del repo**; perderla puede impedir actualizaciones. Usar la firma gestionada por Google Play |
| Compra del juego | Gestionada por la tienda (pago único); no se implementa validación propia |
| Repositorio | Privado, con copias de respaldo |

### Si en el futuro hay nube o cuentas 🟡

- Usar el inicio de sesión de la plataforma (Google Play Games, Sign in with Apple); **no guardar contraseñas propias**.
- Cifrado en tránsito, mínimo de datos, política de privacidad actualizada.
- Ampliar la revisión legal ([11](11-legal-y-cumplimiento.md)).

## Calidad y pruebas

- **Núcleo:** pruebas automáticas y simulaciones de balance.
- **Interfaz y minijuegos:** pruebas manuales en el dispositivo Android; una lista de verificación por versión.
- **Control de versiones:** Git, repositorio privado, commits frecuentes.

## Trabajar con IA 🟡

- Presupuesto: plan Max de Claude; ampliar si el proyecto avanza.
- Por eso conviene dividir el trabajo en **tareas pequeñas y bien definidas** (ver el tablero de tareas): menos contexto por sesión, menos consumo, mejores resultados.
- Yo escribo y reviso el código; **el jugador valida la diversión y el "feel"** en el dispositivo.

## Pendiente

- ❓ Confirmar Godot.
- ❓ Estructura de carpetas del proyecto del juego.
- ❓ Herramientas concretas de arte y audio (después de la prueba de estilo).
- ❓ Hub de documentación y tablero de tareas (ver [06](06-roadmap-y-pendientes.md)).
