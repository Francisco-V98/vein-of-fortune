# 12 · Dirección de arte

## Dirección acordada ✅

| Aspecto | Decisión |
|---|---|
| Paleta | **Colores fríos** (azules pizarra, grises azulados, tonos hielo) |
| Acento principal | **Vinotinto**, usado en detalles y resaltados; es el color "marca" del proyecto |
| Estética | **Industrial y retrofuturista** (atompunk), lúgubre pero colorido |
| Técnica | Pixel art; los escenarios y la interfaz son más bien estáticos, y los personajes caminan (cambio del 2026-10-24, ver «Animación») |
| Referencia de paleta | Imagen aportada por el autor (portada de *Cult of the Lamb*): tonos fríos con un detalle rojo de contraste. Se toma como **referencia de paleta**, no se copian sus personajes ni su arte |

## Paleta ✅ (autor, 2026-10-24)

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

### Reglas de uso ✅ (autor, 2026-10-24)

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

## Pipeline ✅ (actualizado el 2026-10-13; aprobado por el autor el 2026-10-24)

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
| `edificios.png` | 9 edificios (tienda, taller, almacén, casa, Ministerio, Consorcio, Unión, bar, periódico) | ✅ Consistentes entre sí. Eran isométricos: tras el cambio del 2026-10-24 quedan como referencia de estilo y de piezas, y los exteriores definitivos se rehacen en vista aérea cenital (ver «Perspectivas, mapa con niebla y tren») |
| `mapa-valdoria.png` | Mapa ilustrado con las 6 regiones y vías de tren | ✅ Muy bueno; viable como **imagen estática con zonas tocables**. Con el cambio del 2026-10-24 es la base del mapa con niebla y de los trayectos del tren |
| `zonas.png` | 6 fondos de zonas de minado | ✅ Cada zona tiene identidad propia; La Fosa conecta con el color de la Aetherita |
| `minijuegos.png` | Maquetas de Picado, Perforación y Regateo | ✅ Sirven de guía de interfaz |
| `mina-horizontal.png` | Galerías del Hollín en horizontal | ✅ La favorita del autor, ahora en formato correcto |
| `paleta-laton.png`, `paleta-verdigris.png`, `paleta-oxido.png` | Tres opciones de acento secundario | Ver abajo |

### Acento secundario: comparación

| Opción | Efecto | Veredicto |
|---|---|---|
| **Latón / ámbar** | Aporta luz cálida, es muy industrial y combina con monedas, remaches y lámparas | ✅ **Elegida** |
| Verdigrís (cobre oxidado) | Sutil, se mezcla con el frío; poco contraste como complemento | ✅ Reservado para detalles de cobre y tecnología, sin añadir color a la paleta (autor, 2026-10-24) |
| Naranja óxido | Más energía pero se lee como "peligro" | ❌ No como secundario general |

### Lo que se aprendió

- La IA da muy buen material de **referencia y de dirección**; las composiciones completas (mapa, zonas, tienda) pueden usarse como **imagen estática** con zonas tocables. Desde el 2026-10-24 solo el mapa y las pantallas de interfaz siguen siendo imagen estática; los exteriores, las minas y los interiores son escenas por las que se camina.
- Para sprites, íconos y UI el arte definitivo **reconstruye y separa piezas** en pixel art con PixelLab, después de la Puerta B (ver pipeline arriba). Lo generado en estas rondas es provisional.
- La paleta funciona en todos los tipos de imagen: personajes, minerales, edificios, interfaz y mapa.
- El vinotinto está presente en casi todas las imágenes; hay que **controlar su dosis** para que no pierda fuerza y para que la Aetherita siga siendo especial.

## Hojas de personajes y NPC ✅

**Requisito del autor:** tener de cada personaje el material más detallado posible, porque de ahí parte el arte definitivo. Se generan con IA a partir de los retratos y sprites aprobados y se guardan en `studio/assets-ref/personajes/<id>/`. ✅ Estas hojas son **provisionales**: sirven de referencia de diseño y se rehacen en pixel art con PixelLab en la producción definitiva (ver la sección «Assets provisionales y definitivos»).

**Tres hojas por personaje principal** (protagonista hombre y mujer, y los 8 del elenco):

| Hoja | Contenido |
|---|---|
| **Modelo** | **Chibi pixel art** como el sprite del ministro: cuerpo entero y pose estática, en **8 direcciones** (frente, tres cuartos, lados y espalda) |
| **Expresiones** | **Estilo detallado** como los retratos de diálogo. Seis, **iguales para todos**: la **por defecto** según su personalidad, feliz, triste (llorando), enojo, susto y cansancio (bostezando, no triste) |
| **Poses** | **Chibi pixel art** de cuerpo entero: estático con respiración y caminando, en **8 direcciones** (los cuadros de cada animación se fijan al producirla), más gestos al hablar y las animaciones específicas de cada escena |

**Orden de producción ✅:** de cada personaje se hace primero la **hoja de modelo**, que **define la estética completa** (rasgos, colores, tamaño de píxel y proporciones). Después se hace la hoja de **poses usando la de modelo como única referencia**, para que sea el mismo diseño. Las **expresiones** se hacen en estilo detallado a partir del retrato y del modelo. Una hoja no se da por buena hasta que el autor la aprueba.

**Tres tipos de arte por personaje ✅ (autor, 2026-10-24):** reabren el criterio de «dos tipos de personaje» (2026-10-11) y el chibi de ~100 px de arriba. Cada personaje, también los PNJ, tiene:

| Tipo | Uso | Detalle |
|---|---|---|
| **Sprite de vista aérea** (tipo Stardew) | Pasear por el exterior de los asentamientos, la mina cenital y el mapa | 32–48 px de alto; **8 direcciones** con **caminar** y un **estado estático con respiración** |
| **Sprite de vista lateral plana** (tipo Pet Society) | Pasear por los interiores de las edificaciones en corte transversal | Mismas animaciones (caminar y reposo con respiración), vista lateral; las 8 direcciones se reducen a las que la vista pide |
| **Retrato detallado** | Diálogos y expresiones (las seis de siempre) | Chibi detallado en pixel art, aparte de los sprites; es donde van los rasgos finos |

Los tres comparten diseño, paleta y proporciones, y se generan con PixelLab (8 direcciones y animación de caminar). Muchos personajes llevan además animaciones específicas por escena (se piden por escena en la producción; el flujo con PixelLab lo fija ⏳ F4-227).

**Estética chibi de referencia ✅:** el sprite del ministro (`ministro-corregido.png`). Todos los personajes del modelo y las poses llevan esa estética: píxeles grandes y claramente visibles (✅ el sprite de paseo mide **32–48 px de alto** sobre la resolución base 640×360; el chibi de unos 100 px de las hojas de referencia queda superado y los detalles finos pasan al retrato), colores planos con 2 a 3 tonos por material, sombreado simple de bordes duros, contorno negro grueso, **sin textura fina, sin hebras de pelo y sin degradados**, ojos grandes y sencillos con un solo punto de brillo, boca pequeña, cabeza de cerca del 40 % de la altura y cuerpo compacto. El modelo y las poses de un mismo personaje tienen las mismas proporciones.

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

**Animación ✅ (reabierta por el autor el 2026-10-24):** como el jugador camina por exteriores, minas e interiores, la regla anterior («casi estáticos», sin ciclos de caminar para PNJ y enemigos) queda **superada**.
- **Todos los personajes** (protagonista, elenco, PNJ y enemigos humanos) llevan **caminar** y un **estado estático con respiración**, en **8 direcciones**, tanto en vista aérea como en vista lateral.
- Muchos llevan **animaciones específicas por escena** (por ejemplo, atender el mostrador o mirar el reloj); se piden por escena, no de forma genérica.
- Los retratos de diálogo siguen con expresiones estáticas.
- Las criaturas de La Fosa y los jefes siguen el mismo criterio en cuanto aparezcan en una escena por la que se camine.
- Costo: es el cambio de mayor impacto en las horas de arte (F4-227, F4-233 y F4-190 a F4-193; ver [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md)).

## Perspectivas, mapa con niebla y tren ✅ (autor, 2026-10-24)

Cambio de diseño F0-91; el detalle de las zonas está en [26](26-zonas-y-edificios.md) y el razonamiento en [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md).

| Pieza | Decisión de arte |
|---|---|
| **Exterior** | Vista aérea tipo Stardew sobre la resolución 640×360; cada edificación se ve por fuera con su puerta o entrada; cielo y calle dan la identidad de la región. Las 46 edificaciones deben poder entrarse a futuro: se dibujan primero las necesarias y las demás muestran la puerta cerrada |
| **Interior** | Corte transversal con desplazamiento lateral plano (Pet Society); un interior reservado por edificación |
| **Mina** | Recinto con cinco entradas y galerías de 2 a 3 pantallas en vista aérea cenital; las menas se leen por color y silueta, y el color de la lectura del detector (gris, ámbar, verde) respeta la paleta y la regla de accesibilidad |
| **Mapa** | Imagen estática del mapa de Valdoria con las zonas tocables y las vías de tren (base: `mapa-valdoria.png`); se abre desde cualquier lugar |
| **Niebla** | Las zonas aún bloqueadas se cubren con una **niebla densa y oscura** (casi opaca) que deja asomar **un detalle reconocible** (cima de montaña, muelle, torre de la ciudad). Se levanta con una animación breve cuando el acto abre la zona. La niebla es pura presentación, no cambia reglas |
| **Tren** | Pantalla de carga a pantalla completa tipo time-lapse: el personaje sentado junto a la ventanilla y el paisaje pasando de la zona A a la B. **Una escena base modular** reutilizable con **fondos de ventanilla por región**, unos 6 s, saltable desde el segundo viaje |

Las estaciones y los andenes se dibujan como referencia; la mecánica de viajar andando por la estación queda para otras versiones (ver [26](26-zonas-y-edificios.md)).

### Estaciones y clima en el arte ✅ (autor, 2026-10-24, F0-94)

Las estaciones y el clima se resuelven con un **tinte y una superposición de paleta** sobre las escenas ya hechas (mapa, asentamientos, minas y la ventanilla del tren) y con decoración de festivos; **no se dibujan hojas de sprites nuevas** por estación. Cuatro tintes (primavera, verano, otoño, invierno) y cuatro climas por zona (despejado, lluvia, nieve, niebla) con partículas ligeras; los tintes mantienen legibles los colores del detector (gris, ámbar, verde) y la niebla del mapa. Todo es arte provisional hasta la Puerta B (política de assets, más abajo). El trabajo de arte es ⏳ F4-261, junto con ⏳ F4-217, ⏳ F4-165 y ⏳ F4-248. Detalle de reglas en [29](29-calendario-y-temporadas.md).

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

### Reglas de uso ✅ (autor, 2026-10-24)

1. **No se invierte tiempo ni créditos en pulir lo provisional.** Si no sirve para la prueba, se genera otro barato o se usa una forma simple con los colores de la paleta ✅.
2. **Todo asset nuevo de prueba se marca provisional** en `studio/data/assets.json` con el campo `estado` (`provisional` o `definitivo`). Lo que no tenga el campo cuenta como provisional (`estado_por_defecto`).
3. **Nada provisional llega a la tienda**: ni capturas, ni ícono de la app, ni arte clave, ni kit de prensa ✅.
4. **La producción definitiva empieza cuando el autor la autoriza**, después de que el vertical slice pase las pruebas y la Puerta B (F3-23). Antes no se produce arte final, voces ni audio final.
5. **Lo provisional también cumple las reglas de dirección de arte**: paleta, regla del éter, accesibilidad sin rojo y verde, y nada de texto dentro del arte, salvo el wordmark del logo. Así el reemplazo no cambia el diseño.
6. **Lo provisional se conserva como referencia** (rasgos, siluetas y colores) y no se edita a mano. Al reemplazarlo, el definitivo toma su lugar en el juego y el provisional queda en `studio/assets-ref/` como histórico.
7. **El registro de licencias incluye lo provisional**, porque sigue siendo contenido generado por IA ([11](11-legal-y-cumplimiento.md)).

### De la prueba barata a lo definitivo ✅ (autor, 2026-10-24)

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

PixelLab es la herramienta del arte definitivo por decisión del autor. Su flujo de trabajo, estilo, paleta y precio se prueban en la **primera tarea de producción definitiva** (paso 6 del flujo, F4-227); hasta entonces no se contrata ni se gastan créditos en ella. El sprite de personaje mide **32–48 px de alto** ✅ (el «unos 100 píxeles» de las referencias provisionales no es el definitivo). Los tamaños de fondos y marcos de interfaz se fijan en esa prueba ⏳ F4-227.

## Decisiones técnicas de arte pendientes

- ✅ **Resolución base 640×360** (autor, 2026-10-24; cierra F1-06). Con el enfoque de PC primero ([ADR-0009](adr/0009-pc-primero-movil-despues.md)): escala **entera con bandas** (1080p ×3, 1440p ×4, 4K ×6; en la Steam Deck 1280×800 ×2 con bandas), ventana y pantalla completa, y ultrapanorámico con bandas laterales. El sprite de paseo mide 32–48 px (de 9 a 13 % del alto) y los retratos de diálogo se dibujan aparte. La zona segura 20:9 era una pregunta móvil y pasa a la fase móvil.
- ✅ **Perspectiva** (autor, 2026-10-24; sustituye a «edificios en isométrica»). Tres vistas: el **exterior de los asentamientos** es una **vista aérea** tipo Stardew por la que se camina y se puede rodear cada edificación (exploración mínima), con la puerta de cada una visible; el **interior** de cada edificación es un **corte transversal con desplazamiento lateral plano** tipo Pet Society (la tienda es la referencia); y la **mina** es una galería caminable en **vista aérea cenital**. Al entrar o salir hay un loader corto. No importa el tiempo ni el costo: es para dar dinamismo. Los edificios isométricos F4-155 y F4-156 se cancelan y se rehacen como exteriores cenitales.
- ✅ **Nivel de «pixel estricto»** (autor, 2026-10-24): se mantienen los tres niveles (retrato detallado, sprite de vista aérea y sprite de vista lateral). Regla común: paleta bloqueada, contornos y sombreado de bordes duros, píxeles reales, sin degradados ni suavizado. Los retratos llevan más detalle, los sprites quedan en 32–48 px.
- ✅ **Tamaño de íconos** (autor, 2026-10-24): 32×32 provisional (9 % del alto de 360 px, como los sprites); 48×48 si la prueba de PixelLab lo pide ⏳ F4-227.
- ✅ **Fuente pixel para el texto:** Pixelify Sans (ver [13](13-marca-e-identidad.md)); la licencia y los glifos se verifican en ⏳ F1-18, que absorbe la elección de F1-12 (autor, 2026-10-24).
- ✅ Herramienta de pixel art del arte definitivo: **PixelLab** (autor, 2026-10-13).
- ✅ **Cuadros de animación** (autor, 2026-10-24): todo personaje se mueve en **8 direcciones** con **caminar** y **estado de reposo**. Cuántos cuadros lleva cada animación se decide al producirla (prueba de ⏳ F4-227), no antes.
- ✅ **Vinotinto** (autor, 2026-10-24): se conservan `#6E1A2B` (sombra), `#9A2640` (principal) y `#C23B55` (resalte). Regla de contraste: el texto sobre vinotinto va en Hielo claro (5,43:1 con el principal) y el vinotinto nunca es el único portador de información sobre fondo oscuro (ningún tono llega a 4,5:1 sobre Abismo o Pizarra); el peligro lleva además forma o texto.
