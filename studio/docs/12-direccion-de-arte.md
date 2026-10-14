# 12 · Dirección de arte

## Dirección acordada ✅

| Aspecto | Decisión |
|---|---|
| Paleta | **Colores fríos** (azules pizarra, grises azulados, tonos hielo) |
| Acento principal | **Vinotinto**, usado en detalles y resaltados; es el color "marca" del proyecto |
| Estética | **Industrial y retrofuturista** (atompunk), lúgubre pero colorido |
| Técnica | Pixel art, cosas más bien estáticas |
| Referencia de paleta | Imagen aportada por el autor (portada de *Cult of the Lamb*): tonos fríos con un detalle rojo de contraste. Se toma como **referencia de paleta**, no se copian sus personajes ni su arte |

## Paleta propuesta 🟡 (valores aproximados, a afinar)

| Rol | Nombre | Hex orientativo |
|---|---|---|
| Fondo | Abismo | `#0E161D` |
| Fondo | Pizarra oscura | `#17232C` |
| Base | Pizarra | `#22333F` |
| Base | Acero azul | `#36505F` |
| Medio | Azul grisáceo | `#5B7C8C` |
| Luz | Hielo medio | `#8FB0BA` |
| Luz | Hielo claro | `#C9DCDF` |
| **Acento** | Vinotinto oscuro | `#6E1A2B` |
| **Acento** | Vinotinto (principal) | `#9A2640` |
| **Acento** | Vinotinto resalte / alerta | `#C23B55` |
| **Acento secundario** ✅ | Latón (detalles mínimos: remaches, marcos, monedas) | `#B8893A` |
| Luz cálida ✅ | Ámbar (brillo de lámparas) | `#E3B25C` |
| Éter ✅ | Rojo-rosado emisivo (solo Aetherita) | `#E0365A` |
| Éter ✅ | Aura cian pálida (solo Aetherita) | `#7FE3E8` |
| Lujo | Oro (excepción cálida controlada) | `#D9A93A` |

### Reglas de uso 🟡

- ~80 % neutros fríos, ~15 % tonos medios y materiales, **menos de 5 % vinotinto**.
- Vinotinto: botones de acción, estatus, peligro, cables, detalles del mundo. Si se usa en todo, pierde fuerza.
- **Aetherita** ✅: cristal **vinotinto translúcido con brillo rojo-rosado y aura cian**. Es el mineral más llamativo del juego a propósito. Para conservar su rareza, el rojo-rosado **brillante** queda reservado a la Aetherita; el resto del juego usa el vinotinto **mate**.
- Latón/ámbar ✅: detalles mínimos (remaches, marcos, monedas, luz de lámparas); es el "complemento cálido" del vinotinto.
- Oro: excepción controlada para oro y lujo.
- **Accesibilidad:** no depender de rojo/verde para señalar subida o bajada; usar flechas, formas y **azul hielo** (sube) vs. vinotinto (baja).
- ✅ **Cian y rojo-rosado son solo de la Aetherita.** La flecha de subida de los gráficos va en azul hielo, nunca en cian.
- ✅ **El farol de Los Faroleros** es vinotinto mate con luz ámbar, nunca rojo emisivo.

## Prueba de estilo ✅ (realizada)

Cuatro imágenes generadas con IA (modelo `gpt_image_2_5`, calidad baja, ~0,25 créditos cada una). Están en `studio/assets-ref/prueba-de-estilo/`:

| Archivo | Qué prueba |
|---|---|
| `mina.png` | Escena de la mina |
| `personajes.png` | Protagonista hombre y mujer |
| `minerales.png` | Los 10 minerales en una cuadrícula |
| `mercado.png` | Pantalla de escritorio con monitor, teletipo y periódico |

### Resultado

**Lo que funciona:**

- La dirección **fría + vinotinto + atompunk** se ve bien y es reconocible.
- El hombre y la mujer salen **coherentes entre sí** (misma ropa, misma paleta, mismo estilo).
- Los 10 minerales salen con un estilo bastante consistente.
- La pantalla de mercado transmite justo el aire de "Papers, Please" retrofuturista.

**Lo que preocupa:**

1. **No es pixel art "real".** Son ilustraciones de aspecto pixelado a alta resolución. Los píxeles no son de tamaño uniforme ni están alineados a una cuadrícula. Un juego de pixel art necesita una resolución base fija (por ejemplo ×4 o ×6 al escalar) con píxeles consistentes.
2. **Son composiciones completas, no assets.** Un juego necesita sprites separados, fondos por capas, tiles que encajen y marcos de animación. Una imagen completa se usa como **referencia visual**, no como pieza del juego.
3. **Legibilidad de los minerales.** Cuarzo, salitre y plata se parecen demasiado a tamaño pequeño; las siluetas deben distinguirse. El contorno vinotinto aparece en todos los íconos y diluye la regla del acento.
4. **Texto.** La IA generó "pseudo-texto". En el juego todo el texto será real, con una fuente pixel.
5. **El oro** sale cálido y rompe la paleta fría. Está permitido como excepción.

### Qué sirve y qué no

| Uso | Veredicto |
|---|---|
| Tablero de inspiración y dirección de arte | ✅ Muy útil |
| Guía de estilo y paleta | ✅ |
| Bocetos de pantallas y UI | ✅ Como referencia |
| Íconos de minerales | ✅ Referencia de siluetas y colores para el pixel art definitivo; no se pulen (ver la sección «Assets provisionales y definitivos») |
| Personajes y escenas | ✅ Referencia de diseño para el pixel art definitivo; no se reconstruyen a mano |
| Assets directos del juego | ❌ No: lo generado con IA en las rondas de prueba es provisional |

## Pipeline 🟡 (actualizado el 2026-10-13)

1. La IA genera **referencias** e ideas (rápido y barato). Son **provisionales** ✅.
2. El prototipo y el vertical slice usan esas referencias tal cual (o formas simples con los colores de la paleta). No se limpian ni se reconstruyen ✅.
3. Solo después de que el vertical slice pase las pruebas y la Puerta B, y cuando el autor lo autorice, el **arte definitivo** se produce en pixel art con **PixelLab**, sobre una cuadrícula fija y con la paleta bloqueada, tomando lo provisional como referencia.
4. Lo definitivo se separa en piezas: sprites, fondos por capas, íconos, marcos de interfaz.
5. Todo se guarda con su registro de licencia (ver [11](11-legal-y-cumplimiento.md)).

Para el **prototipo** (F2) y el **vertical slice** (F3): formas simples y referencias provisionales con los colores de la paleta; el arte definitivo llega después de la Puerta B. El detalle está en la sección «Assets provisionales y definitivos», más abajo.

## Segunda ronda de pruebas ✅ (horizontal)

El juego es **horizontal (landscape)**. Catorce imágenes en `studio/assets-ref/prueba-de-estilo-2/`:

| Archivo | Qué es | Veredicto |
|---|---|---|
| `minerales-v2.png` | 10 minerales corregidos | ✅ Siluetas y colores distintos; **Aetherita** vinotinto cristalina destaca claramente |
| `retratos-a.png`, `retratos-b.png` | Retratos de diálogo: Reme, Teo, Quiroga, Lucía, Esteban, Casilda, Ministro Montenegro y foto de Anselmo | ✅ Muy buenos; expresivos, coherentes y con la paleta |
| `sprites.png` → `sprites-corregido.png` | Sprites pequeños tipo Stardew (protagonistas hombre y mujer y elenco) | ✅ Funcionan como guía. El ministro original parecía un sacerdote (estola con cruces); se reemplazó por un funcionario severo de abrigo azul marino y faja vinotinto, sin símbolos religiosos (`ministro-corregido.png`) |
| `ui-mercado.png` → `ui-mercado-corregido.png` | Terminal de mercado (lista, gráfico, teletipo, bloques del día) | ✅ Buen punto de partida. Las flechas rojo/verde se cambiaron por ▲ cian (sube) y ▼ vinotinto (baja), que cumple la regla de accesibilidad. ✅ La regla vigente cambia la subida a azul hielo, porque el cian es solo de la Aetherita; la imagen se conserva como referencia de composición |
| `ui-tienda.png` | Pantalla de la tienda con corte transversal | ✅ Muy buena base; comunica el "taller + mostrador + almacén" |
| `edificios.png` | 9 edificios (tienda, taller, almacén, casa, Ministerio, Consorcio, Unión, bar, periódico) | ✅ Consistentes entre sí; en isométrica |
| `mapa-valdoria.png` | Mapa ilustrado con las 6 regiones y vías de tren | ✅ Muy bueno; viable como **imagen estática con zonas tocables** |
| `zonas.png` | 6 fondos de zonas de minado | ✅ Cada zona tiene identidad propia; La Fosa conecta con el color de la Aetherita |
| `minijuegos.png` | Maquetas de Picado, Perforación y Regateo | ✅ Sirven de guía de interfaz |
| `mina-horizontal.png` | Galerías del Hollín en horizontal | ✅ La favorita del autor, ahora en formato correcto |
| `paleta-laton.png`, `paleta-verdigris.png`, `paleta-oxido.png` | Tres opciones de acento secundario | Ver abajo |

### Acento secundario: comparación

| Opción | Efecto | Veredicto |
|---|---|---|
| **Latón / ámbar** | Aporta luz cálida, es muy industrial y combina con monedas, remaches y lámparas | ✅ **Elegida** |
| Verdigrís (cobre oxidado) | Sutil, se mezcla con el frío; poco contraste como complemento | 🟡 Reservar para detalles de cobre y tecnología |
| Naranja óxido | Más energía pero se lee como "peligro" | ❌ No como secundario general |

### Lo que se aprendió

- La IA da muy buen material de **referencia y de dirección**; las composiciones completas (mapa, zonas, tienda) pueden usarse como **imagen estática** con zonas tocables, lo cual encaja con la estética estática.
- Para sprites, íconos y UI el arte definitivo **reconstruye y separa piezas** en pixel art con PixelLab, después de la Puerta B (ver pipeline arriba). Lo generado en estas rondas es provisional.
- La paleta funciona en todos los tipos de imagen: personajes, minerales, edificios, interfaz y mapa.
- El vinotinto está presente en casi todas las imágenes; hay que **controlar su dosis** para que no pierda fuerza y para que la Aetherita siga siendo especial.

## Hojas de personajes y NPC ✅

**Requisito del autor:** tener de cada personaje el material más detallado posible, porque de ahí parte el arte definitivo. Se generan con IA a partir de los retratos y sprites aprobados y se guardan en `studio/assets-ref/personajes/<id>/`. ✅ Estas hojas son **provisionales**: sirven de referencia de diseño y se rehacen en pixel art con PixelLab en la producción definitiva (ver la sección «Assets provisionales y definitivos»).

**Tres hojas por personaje principal** (protagonista hombre y mujer, y los 8 del elenco):

| Hoja | Contenido |
|---|---|
| **Modelo** | **Chibi pixel art** como el sprite del ministro: cuerpo entero y pose estática, de frente, tres cuartos, ambos lados y espalda |
| **Expresiones** | **Estilo detallado** como los retratos de diálogo. Seis, **iguales para todos**: la **por defecto** según su personalidad, feliz, triste (llorando), enojo, susto y cansancio (bostezando, no triste) |
| **Poses** | **Chibi pixel art** de cuerpo entero: estático, caminando (ciclo de 4 fotogramas de lado, más de frente y de espalda) y gestos al hablar |

**Orden de producción ✅:** de cada personaje se hace primero la **hoja de modelo**, que **define la estética completa** (rasgos, colores, tamaño de píxel y proporciones). Después se hace la hoja de **poses usando la de modelo como única referencia**, para que sea el mismo diseño. Las **expresiones** se hacen en estilo detallado a partir del retrato y del modelo. Una hoja no se da por buena hasta que el autor la aprueba.

**Estética chibi de referencia ✅:** el sprite del ministro (`ministro-corregido.png`). Todos los personajes del modelo y las poses llevan esa estética: píxeles grandes y claramente visibles (cada personaje de unos 100 píxeles de alto), colores planos con 2 a 3 tonos por material, sombreado simple de bordes duros, contorno negro grueso, **sin textura fina, sin hebras de pelo y sin degradados**, ojos grandes y sencillos con un solo punto de brillo, boca pequeña, cabeza de cerca del 40 % de la altura y cuerpo compacto. El modelo y las poses de un mismo personaje tienen las mismas proporciones.

**Expresiones ✅:** retrato de busto en pixel art con la estética del modelo: ojos grandes y expresivos, sombreado plano suave y el mismo tamaño de píxel, como en las hojas del protagonista y de Reme. Las seis tienen los mismos gestos para todos, sutiles y legibles: la **predeterminada** según la personalidad, feliz (riendo), triste (con una lágrima), enojo, susto y cansancio. El **cansancio** es discreto (párpados pesados, ojeras leves, boca relajada), no exagerado y distinto de triste.

**Ministro Montenegro, versión canónica ✅:** la del retrato aprobado: pelo blanco peinado hacia atrás, gafas redondas de latón, **sin barba**, guerrera azul marino de cuello alto con laureles dorados, charreteras, faja vinotinto y blanca, tres medallas y la carpeta. Reemplaza la barba y el abrigo largo del sprite que sirvió para fijar el estilo de los modelos.

**Hojas de NPC ✅:** los 35 tipos están en el registro del mundo (`studio/data/world.json`). Formato mixto:

| Grupos | Formato |
|---|---|
| Ministerio, Comisión del Éter, Consorcio Arvel, Unión, Los Faroleros, prensa, empleados y civiles (26 tipos) | **Hoja de grupo** con 2 o 3 tipos: cada uno de frente, de lado, de espalda y una cara con su expresión predeterminada, en chibi pixel art con la estética del modelo |
| Enemigos humanos y criaturas de La Fosa (9 tipos) | **Una hoja por tipo**: de frente, de lado, de espalda y dos expresiones, porque son los que más se ven |

**Jefes de zona ✅:** un jefe humano por zona (tabla del [documento 02](02-extraccion.md)), con una hoja por jefe de frente, de lado, de espalda, predeterminada y enojo, en el mismo estilo chibi. Sus fichas están en el registro del mundo y se ven en la galería del hub (`#/personajes`).

| Zona | Jefe | Rasgos que lo hacen reconocible |
|---|---|---|
| Galerías del Hollín | Capataz Mayor | Bombín con lámpara de latón, bigote gris, chaleco vinotinto, silbato y bastón con punta de hierro |
| Cañón Ferroso | Cabecilla de la banda rival | Pañuelo rojo, gabán naranja óxido, hombreras de hierro remachadas, cinturón de cadena y garrote liso en la mano derecha apoyado en el suelo |
| Minas de Sierra Alta | Jefe de seguridad del Consorcio | Abrigo azul pizarra con cuello de piel, gorra con gafas de aviador subidas, brazalete vinotinto y porra |
| Salares del Litoral | Aduanero Mayor | Uniforme beige manchado de sal, banda vinotinta, medalla de latón, libro de registro y sello |
| Cavernas de Cristal | Cazarrecompensas Mayor | Gabán carbón, sombrero con medallón de latón, grilletes en el cinturón, espuelas y, en el collar, una cápsula de cristal sellada con un fragmento de Aetherita a la vista |
| La Fosa del Éter | Coronel de la Comisión | Capote verde oliva oscuro, banda vinotinta, charreteras doradas, gorra con estrella dorada de metal, guantes blancos y bastón negro |

✅ **Regla del éter en el arte:** el éter nunca va suelto sobre el cuerpo de un personaje sano. Solo aparece contenido en una cápsula de cristal sellada, o en los mutados de La Fosa. El cian de la paleta es el aura del éter, así que tampoco se usa en adornos de personajes sanos.

El ministro Montenegro sigue siendo el antagonista narrativo y no tiene duelo de jefe.

**Calidad de las hojas de referencia:** generación en calidad media a 2K, que equilibra detalle y costo. Se revisa y aprueba cada hoja antes de pasar a la siguiente. Las hojas nuevas que hagan falta para pruebas se generan en calidad baja (ver reglas de uso de la sección siguiente).

**Animación ✅:** el movimiento se define según la necesidad y casi todo el tiempo los personajes son **estáticos**.
- **Versión 1:** sprites estáticos y retratos con expresiones en los diálogos. Como mucho, alguna caminata suelta del protagonista; casi no hay caminatas.
- **Después de la versión 1:** el protagonista podrá tener algunos movimientos en ciertas zonas o escenas, buscando un punto medio entre costo y vida en pantalla.
- Los NPC y los enemigos no llevan ciclos de caminar; si más adelante hace falta movimiento en alguno, se pide como tarea aparte.
- Las poses de caminar de las hojas quedan como referencia para cuando se decida animar.

## Assets provisionales y definitivos ✅

### Política del autor ✅ (2026-10-13)

- ✅ Todo lo gráfico que existe hoy, **hasta el logo**, se rehará después: personajes, minerales, escenas, ambiente y animaciones.
- ✅ Todo el arte definitivo se hará en **pixel art con la herramienta PixelLab**.
- ✅ Lo que hay ahora sirve de **referencia o de uso interno**. Se reemplaza por cosas reales después de hacer pruebas y comprobar que todo funciona a la perfección.
- ✅ Habrá un momento en que se necesiten los assets reales (píxeles, imágenes, voces, etc.) para la **producción final**, no para pruebas y testeos. Antes de ese momento, el objetivo es **fallar barato y rápido**.
- ✅ Para el storyboard del Acto I (F0-24): los personajes ya hechos y los minerales se reutilizan como referencia; los escenarios y los momentos se rehacen de forma barata.

### Qué es provisional y qué es definitivo ✅

| | Provisional | Definitivo |
|---|---|---|
| Para qué sirve | Referencia, pruebas, prototipo, vertical slice, storyboard y uso interno | Producción final del juego y de la tienda |
| Cómo se hace | Generado barato (calidad baja, pocas iteraciones), a partir de las referencias aprobadas | Pixel art con PixelLab; voces y audio finales |
| Acabado | Sin pulir; no se limpia ni se reconstruye | Revisado por el director de arte y aprobado por el autor |
| Cuánto se invierte | Lo mínimo: ni tiempo ni créditos de más | Presupuesto de producción propio, estimado tras la prueba de PixelLab |
| Cómo se marca | `estado: provisional` en `studio/data/assets.json` | `estado: definitivo` en `studio/data/assets.json` |
| Cuándo | Desde ya hasta la Puerta B | Solo después de que el vertical slice pase las pruebas y la Puerta B, y cuando el autor lo autorice |
| Llega a la tienda | ❌ Nunca | ✅ Sí |

### Qué es provisional hoy ✅

| Asset | Dónde está | Estado | En pruebas y storyboards |
|---|---|---|---|
| Hojas de personajes y NPC (modelo, expresiones y poses; protagonistas, elenco, 35 NPC y jefes) | `studio/assets-ref/personajes/`, `npc/` | Provisional ✅ | ✅ Se reutilizan como referencia |
| Minerales (`minerales-v2.png`) | `studio/assets-ref/prueba-de-estilo-2/` | Provisional ✅ | ✅ Se reutilizan como referencia |
| Retratos y sprites de la prueba de estilo | `prueba-de-estilo-2/` | Provisional ✅ | ✅ Referencia de diseño |
| Pruebas de estilo (rondas 1 y 2) y su paleta | `prueba-de-estilo/`, `prueba-de-estilo-2/` | Provisional ✅ | ✅ Referencia de dirección; la paleta de este documento sigue vigente |
| Escenarios (mina, zonas, edificios, tienda, interfaz de mercado y minijuegos) | `prueba-de-estilo-2/` | Provisional ✅ | ✅ Solo referencia de atmósfera; los del storyboard se generan nuevos y baratos |
| Momentos (escenas clave del Acto I) | No existen aún | — | ✅ Se generan nuevos y baratos para el storyboard |
| Mapa de Valdoria (`mapa-valdoria.png`) | `prueba-de-estilo-2/` | Provisional ✅ | Se regenera ahora, barato y con las zonas actuales (Altafría, Salinas Blancas y la capital) ✅ (decisión del autor, 2026-10-13); el definitivo se rehace en pixel art ⏳ F4-233 |
| Logo y wordmark, íconos de app | `studio/assets-ref/marca/` | Provisional ✅ | ✅ Uso interno (hub, README y pruebas) |
| Íconos (minerales, herramientas, interfaz) | Recortes de las rondas de prueba | Provisional ✅ | ✅ Referencia de siluetas y colores |
| Ambiente y animaciones (ciclos de caminar de las hojas de poses) | Hojas de poses | Provisional ✅ | ✅ Referencia de movimiento |
| Audio y voces | Aún no hay | — | Todo lo que se haga de prueba es provisional |

### Reglas de uso 🟡

1. **No se invierte tiempo ni créditos en pulir lo provisional.** Si no sirve para la prueba, se genera otro barato o se usa una forma simple con los colores de la paleta ✅.
2. **Todo asset nuevo de prueba se marca provisional** en `studio/data/assets.json` con el campo `estado` (`provisional` o `definitivo`). Lo que no tenga el campo cuenta como provisional (`estado_por_defecto`).
3. **Nada provisional llega a la tienda**: ni capturas, ni ícono de la app, ni arte clave, ni kit de prensa ✅.
4. **La producción definitiva empieza cuando el autor la autoriza**, después de que el vertical slice pase las pruebas y la Puerta B (F3-23). Antes no se produce arte final, voces ni audio final.
5. **Lo provisional también cumple las reglas de dirección de arte**: paleta, regla del éter, accesibilidad sin rojo y verde, y nada de texto dentro del arte, salvo el wordmark del logo. Así el reemplazo no cambia el diseño.
6. **Lo provisional se conserva como referencia** (rasgos, siluetas y colores) y no se edita a mano. Al reemplazarlo, el definitivo toma su lugar en el juego y el provisional queda en `studio/assets-ref/` como histórico.
7. **El registro de licencias incluye lo provisional**, porque sigue siendo contenido generado por IA ([11](11-legal-y-cumplimiento.md)).

### De la prueba barata a lo definitivo 🟡

1. **Generar barato**: calidad baja, a partir de las referencias aprobadas.
2. **Marcar** `estado: provisional` en `assets.json`.
3. **Probar** en el prototipo, el vertical slice o el storyboard.
4. **Puerta B** (F3-23): el vertical slice pasa las pruebas y el autor decide seguir.
5. **Autorización del autor** para empezar la producción definitiva.
6. **Prueba de PixelLab** con un personaje, un mineral y un fondo: flujo, estilo, paleta, tamaños y precio.
7. **Producción por lotes** en PixelLab, con lo provisional como referencia.
8. **Revisión** del director de arte contra este documento y aprobación del autor.
9. **Reemplazo**: se marca `estado: definitivo`, se registra la licencia y se sustituye lo provisional en el juego.

### PixelLab, herramienta del arte definitivo ✅

PixelLab es la herramienta del arte definitivo por decisión del autor. Su flujo de trabajo, estilo, paleta, tamaños y precio se prueban en la **primera tarea de producción definitiva** (paso 6 del flujo). 🟡 Hasta entonces no se contrata ni se gastan créditos en ella. Los tamaños de personajes, íconos y fondos quedan 🟡 hasta esa prueba; los valores actuales (unos 100 píxeles de alto por personaje, ver «Estética chibi de referencia») son los de las referencias, no los del arte definitivo.

## Decisiones técnicas de arte pendientes

- ❓ **Resolución base (horizontal).** Sugerencia a probar: **480×270** (escala ×4 hasta 1920×1080); alternativa 384×216 (×5). Hay que cuidar el escalado entero y las distintas proporciones de pantalla de Android (por ejemplo 20:9): diseñar el contenido importante en una zona 16:9 y extender el fondo hacia los bordes. Las primeras pruebas eran verticales y quedan superadas.
- ✅ **Perspectiva.** Los **edificios van en isométrica** (mapa de ciudad) y, al entrar, se muestra su **vista interior** en corte transversal, como la tienda. Las escenas de mina y zonas siguen en vista lateral.
- ❓ **Nivel de "pixel estricto".** Los retratos son muy detallados (ilustración pixelada) y los sprites son más cercanos a Stardew. Decidir si se mantienen así o se unifican.
- ❓ Tamaño de íconos (por ejemplo 32×32 o 48×48) y de sprites de personaje. Para el arte definitivo se prueba con PixelLab (ver «Assets provisionales y definitivos»).
- ❓ Fuente pixel para el texto, con licencia clara.
- ✅ Herramienta de pixel art del arte definitivo: **PixelLab** (autor, 2026-10-13).
- ❓ Cuántos cuadros de animación se permiten (el estilo es estático; probablemente pocos).
- ❓ Si el vinotinto exacto es el de la tabla o se prefiere otro tono.
