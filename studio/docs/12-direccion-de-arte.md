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
| `sprites.png` | Sprites pequeños tipo Stardew (protagonistas hombre y mujer y elenco) | 🟡 Funcionan como guía; el ministro salió parecido a un sacerdote (estola con cruces) y hay que corregirlo |
| `ui-mercado.png` | Terminal de mercado (lista, gráfico, teletipo, bloques del día) | 🟡 Buen punto de partida; usa flechas rojo/verde, que va contra la regla de accesibilidad |
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

**Estética chibi de referencia ✅:** el sprite del ministro (`ministro-corregido.png`). Todos los personajes del modelo y las poses llevan esa estética: píxeles grandes y claramente visibles (cada personaje de unos 100 píxeles de alto), colores planos con 2 a 3 tonos por material, sombreado simple de bordes duros, contorno negro grueso, **sin textura fina, sin hebras de pelo y sin degradados**, ojos grandes y sencillos con un solo punto de brillo, boca pequeña, cabeza de cerca del 40 % de la altura y cuerpo compacto. El modelo y las poses de un mismo personaje tienen las mismas proporciones.

**Expresiones ✅:** las seis tienen los mismos gestos para todos, sutiles y legibles. El **cansancio** es discreto (párpados pesados, ojeras leves, boca relajada), no exagerado y distinto de triste.

**Hojas de NPC:** una por tipo (frente, espalda, un lado y dos expresiones). Los 35 tipos están en el registro del mundo (`studio/data/world.json`): Ministerio, Comisión del Éter, Consorcio Arvel, Unión, Los Faroleros, prensa, empleados, civiles, enemigos humanos y criaturas de La Fosa. Los jefes de zona quedan diferidos (⏳ F0-69).

**Calidad:** generación en calidad media a 2K, que equilibra detalle y costo. Se revisa y aprueba cada hoja antes de pasar a la siguiente.

**Animación:** ⏳ F0-70 Si los personajes llevarán animación de movimiento en el juego se decide más adelante; las poses de caminar sirven de referencia en cualquier caso.

## Decisiones técnicas de arte pendientes

- ❓ **Resolución base (horizontal).** Sugerencia a probar: **480×270** (escala ×4 hasta 1920×1080); alternativa 384×216 (×5). Hay que cuidar el escalado entero y las distintas proporciones de pantalla de Android (por ejemplo 20:9): diseñar el contenido importante en una zona 16:9 y extender el fondo hacia los bordes. Las primeras pruebas eran verticales y quedan superadas.
- ✅ **Perspectiva.** Los **edificios van en isométrica** (mapa de ciudad) y, al entrar, se muestra su **vista interior** en corte transversal, como la tienda. Las escenas de mina y zonas siguen en vista lateral.
- ❓ **Nivel de "pixel estricto".** Los retratos son muy detallados (ilustración pixelada) y los sprites son más cercanos a Stardew. Decidir si se mantienen así o se unifican.
- ❓ Tamaño de íconos (por ejemplo 32×32 o 48×48) y de sprites de personaje.
- ❓ Fuente pixel para el texto, con licencia clara.
- ❓ Herramienta de edición de pixel art.
- ❓ Cuántos cuadros de animación se permiten (el estilo es estático; probablemente pocos).
- ❓ Si el vinotinto exacto es el de la tabla o se prefiere otro tono.
