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
- **Accesibilidad:** no depender de rojo/verde para señalar subida o bajada; usar flechas, formas y cian vs. vinotinto.

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
| Íconos de minerales | 🟡 Utilizables tras reducir, limpiar y fijar la paleta |
| Personajes y escenas | 🟡 Como base; hay que reconstruir con cuadrícula coherente |
| Assets directos del juego | ❌ No sin trabajo de limpieza |

## Pipeline propuesto 🟡

1. La IA genera **referencias** e ideas (rápido y barato).
2. El autor (diseñador) **limpia y reconstruye** sobre una cuadrícula fija, con la paleta bloqueada, para obtener píxeles consistentes.
3. Los elementos se separan en piezas: sprites, fondos por capas, íconos, marcos de interfaz.
4. Todo se guarda con su registro de licencia (ver [11](11-legal-y-cumplimiento.md)).

Para el **prototipo (Fase 1)**: formas simples y colores de la paleta; el arte final llega en la Fase 2.

## Segunda ronda de pruebas ✅ (horizontal)

El juego es **horizontal (landscape)**. Catorce imágenes en `studio/assets-ref/prueba-de-estilo-2/`:

| Archivo | Qué es | Veredicto |
|---|---|---|
| `minerales-v2.png` | 10 minerales corregidos | ✅ Siluetas y colores distintos; **Aetherita** vinotinto cristalina destaca claramente |
| `retratos-a.png`, `retratos-b.png` | Retratos de diálogo: Reme, Teo, Quiroga, Lucía, Esteban, Casilda, Ministro Dueñas y foto de Anselmo | ✅ Muy buenos; expresivos, coherentes y con la paleta |
| `sprites.png` → `sprites-corregido.png` | Sprites pequeños tipo Stardew (protagonistas hombre y mujer y elenco) | ✅ Funcionan como guía. El ministro original parecía un sacerdote (estola con cruces); se reemplazó por un funcionario severo de abrigo azul marino y faja vinotinto, sin símbolos religiosos (`ministro-corregido.png`) |
| `ui-mercado.png` → `ui-mercado-corregido.png` | Terminal de mercado (lista, gráfico, teletipo, bloques del día) | ✅ Buen punto de partida. Las flechas rojo/verde se cambiaron por ▲ cian (sube) y ▼ vinotinto (baja), que cumple la regla de accesibilidad |
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
- Para sprites, íconos y UI hay que **reconstruir y separar piezas** (ver pipeline arriba).
- La paleta funciona en todos los tipos de imagen: personajes, minerales, edificios, interfaz y mapa.
- El vinotinto está presente en casi todas las imágenes; hay que **controlar su dosis** para que no pierda fuerza y para que la Aetherita siga siendo especial.

## Hojas de personajes y NPC ✅

**Requisito del autor:** tener de cada personaje el material más detallado posible, porque de ahí parte el arte final. Se generan con IA a partir de los retratos y sprites aprobados y se guardan en `studio/assets-ref/personajes/<id>/`.

**Tres hojas por personaje principal** (protagonista hombre y mujer, y los 8 del elenco):

| Hoja | Contenido |
|---|---|
| **Modelo** | **Chibi pixel art** como el sprite del ministro: cuerpo entero y pose estática, de frente, tres cuartos, ambos lados y espalda |
| **Expresiones** | **Estilo detallado** como los retratos de diálogo. Seis, **iguales para todos**: la **por defecto** según su personalidad, feliz, triste (llorando), enojo, susto y cansancio (bostezando, no triste) |
| **Poses** | **Chibi pixel art** de cuerpo entero: estático, caminando (ciclo de 4 fotogramas de lado, más de frente y de espalda) y gestos al hablar |

**Orden de producción ✅:** de cada personaje se hace primero la **hoja de modelo**, que **define la estética completa** (rasgos, colores, tamaño de píxel y proporciones). Después se hace la hoja de **poses usando la de modelo como única referencia**, para que sea el mismo diseño. Las **expresiones** se hacen en estilo detallado a partir del retrato y del modelo. Una hoja no se da por buena hasta que el autor la aprueba.

**Estética chibi de referencia ✅:** el sprite del ministro (`ministro-corregido.png`). Todos los personajes del modelo y las poses llevan esa estética: píxeles grandes y claramente visibles (cada personaje de unos 100 píxeles de alto), colores planos con 2 a 3 tonos por material, sombreado simple de bordes duros, contorno negro grueso, **sin textura fina, sin hebras de pelo y sin degradados**, ojos grandes y sencillos con un solo punto de brillo, boca pequeña, cabeza de cerca del 40 % de la altura y cuerpo compacto. El modelo y las poses de un mismo personaje tienen las mismas proporciones.

**Expresiones ✅:** retrato de busto en pixel art con la estética del modelo: ojos grandes y expresivos, sombreado plano suave y el mismo tamaño de píxel, como en las hojas del protagonista y de Reme. Las seis tienen los mismos gestos para todos, sutiles y legibles: la **predeterminada** según la personalidad, feliz (riendo), triste (con una lágrima), enojo, susto y cansancio. El **cansancio** es discreto (párpados pesados, ojeras leves, boca relajada), no exagerado y distinto de triste.

**Ministro Dueñas, versión canónica ✅:** la del retrato aprobado: pelo blanco peinado hacia atrás, gafas redondas de latón, **sin barba**, guerrera azul marino de cuello alto con laureles dorados, charreteras, faja vinotinto y blanca, tres medallas y la carpeta. Reemplaza la barba y el abrigo largo del sprite que sirvió para fijar el estilo de los modelos.

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

El ministro Dueñas sigue siendo el antagonista narrativo y no tiene duelo de jefe.

**Calidad:** generación en calidad media a 2K, que equilibra detalle y costo. Se revisa y aprueba cada hoja antes de pasar a la siguiente.

**Animación ✅:** el movimiento se define según la necesidad y casi todo el tiempo los personajes son **estáticos**.
- **Versión 1:** sprites estáticos y retratos con expresiones en los diálogos. Como mucho, alguna caminata suelta del protagonista; casi no hay caminatas.
- **Después de la versión 1:** el protagonista podrá tener algunos movimientos en ciertas zonas o escenas, buscando un punto medio entre costo y vida en pantalla.
- Los NPC y los enemigos no llevan ciclos de caminar; si más adelante hace falta movimiento en alguno, se pide como tarea aparte.
- Las poses de caminar de las hojas quedan como referencia para cuando se decida animar.

## Decisiones técnicas de arte pendientes

- ❓ **Resolución base (horizontal).** Sugerencia a probar: **480×270** (escala ×4 hasta 1920×1080); alternativa 384×216 (×5). Hay que cuidar el escalado entero y las distintas proporciones de pantalla de Android (por ejemplo 20:9): diseñar el contenido importante en una zona 16:9 y extender el fondo hacia los bordes. Las primeras pruebas eran verticales y quedan superadas.
- ✅ **Perspectiva.** Los **edificios van en isométrica** (mapa de ciudad) y, al entrar, se muestra su **vista interior** en corte transversal, como la tienda. Las escenas de mina y zonas siguen en vista lateral.
- ❓ **Nivel de "pixel estricto".** Los retratos son muy detallados (ilustración pixelada) y los sprites son más cercanos a Stardew. Decidir si se mantienen así o se unifican.
- ❓ Tamaño de íconos (por ejemplo 32×32 o 48×48) y de sprites de personaje.
- ❓ Fuente pixel para el texto, con licencia clara.
- ❓ Herramienta de edición de pixel art.
- ❓ Cuántos cuadros de animación se permiten (el estilo es estático; probablemente pocos).
- ❓ Si el vinotinto exacto es el de la tabla o se prefiere otro tono.
