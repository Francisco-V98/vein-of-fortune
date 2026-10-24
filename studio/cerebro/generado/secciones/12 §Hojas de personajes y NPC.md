---
id: "doc-12-hojas-de-personajes-y-npc"
tipo: "seccion"
title: "Hojas de personajes y NPC ✅"
aliases: ["doc-12-hojas-de-personajes-y-npc"]
documento: "[[12 Dirección de arte]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[12 §Segunda ronda de pruebas (horizontal)]]"
siguiente: "[[12 §Assets provisionales y definitivos]]"
arriba: "[[12 Dirección de arte]]"
fuente: "studio/docs/12-direccion-de-arte.md:126"
generado: true
---

# Hojas de personajes y NPC ✅

> Requisito del autor: tener de cada personaje el material más detallado posible, porque de ahí parte el arte definitivo. Se generan con IA a…

← [[12 §Segunda ronda de pruebas (horizontal)]] · [[12 Dirección de arte|↑ 12]] · [[12 §Assets provisionales y definitivos]] →

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

**Jefes de zona ✅:** un jefe humano por zona (tabla del [[02 Extracción|documento 02]]), con una hoja por jefe de frente, de lado, de espalda, predeterminada y enojo, en el mismo estilo chibi. Sus fichas están en el registro del mundo y se ven en la galería del hub (`#/personajes`).

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

## Fuente

`studio/docs/12-direccion-de-arte.md:126`
