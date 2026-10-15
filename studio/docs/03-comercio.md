# 03 · Comercio y mercado

## Principios ✅

- ✅ Mercado que se comporta de forma creíble: precios que suben y bajan, especulación (comprar barato, vender caro, guardar hasta que suba).
- ✅ Los materiales tienen **funcionalidad y uso** en el juego, no solo se compran y venden.
- ✅ El juego **incentiva** la comercialización y requiere revisar noticias y gráficos.
- ✅ Hay que saber si un mineral está sobrevalorado o infravalorado, y si conviene minar uno u otro.
- ✅ Es un mercado de dificultad media: más amable que EVE, pero con patrones reales que aprender.

## Cómo se mueve un precio ✅

**Estado:** el mercado se mueve 3 veces por día, y el modelo (valor justo, oferta y demanda, ruido y momentum) y la ficha de mercado están confirmados (alcance de F2-04 y lista de cifras de F0-52, 2026-10-15); las fórmulas ⏳ F2-04 y los valores ⏳ F0-52.

Cada mineral tiene un **valor justo**, que se ajusta cada día según oferta, demanda y eventos. El precio real lo persigue **con retraso**, con **ruido** y **momentum**. Resumen: *el precio tiende hacia el valor justo, pero tarda, se pasa y se agita*. Genera tendencias y rebotes que se pueden aprender a leer sin ser predecibles. Las fórmulas concretas ⏳ F2-04.

✅ El mercado se mueve **3 veces por día**, una por bloque (mañana, tarde, noche). Esperar al bloque siguiente para vender es una decisión real, y el botón «Esperar» salta un bloque ([01](01-core-loop.md)).

### Ficha de mercado por mineral ✅

| Parámetro | Qué controla |
|---|---|
| Precio base | Nivel de referencia |
| Volatilidad | Cuánto se agita |
| Liquidez | Cuánto cae el precio al vender mucho |
| Estacionalidad | Si sube o baja por épocas |
| Sensibilidad a eventos | Qué tipo de noticias lo mueven |
| Costo de guardar | Cuánto cuesta tenerlo en el almacén (la mercancía **no se deteriora** ✅) |

⏳ F0-52 Precio base, volatilidad, liquidez y costo de guardar de los 10 minerales.

### Personalidad de cada mineral ⏳ F0-52

Niveles orientativos de volatilidad y qué mueve a cada mineral, a partir de [05](05-mundo-y-minerales.md). La volatilidad de cada uno de los 10 minerales la fija F0-52.

| Mineral | Volatilidad | Qué lo mueve más |
|---|---|---|
| Carbón | Baja–media | Estación (invierno), huelgas |
| Hierro | Baja | Contratos de guerra, ferrocarriles |
| Cobre | Media | Obras eléctricas, escasez (apagones) |
| Salitre | Media–alta | Cosechas, puertos, Faroleros |
| Plata | Media | Industria, joyería |
| Oro | Baja–media | Política, reservas del Estado |
| Cuarzo | Media | Demanda tecnológica |
| Esmeralda | Alta | Modas de la élite |
| Diamante | Alta | Lujo, industria de corte |
| Aetherita | Muy alta | Descubrimientos, secreto de Estado |

Tipos generales: estable, volátil, estacional, estratégico, lujo (ver [05](05-mundo-y-minerales.md)).

## Oferta y demanda ✅

**Estado:** la oferta por mineros NPC y las huelgas ([07](07-sociedad-y-eventos.md)) y la demanda por los seis sectores (alcance de F4-31) están confirmadas; qué sectores alimenta cada mineral ⏳ F4-31. El peso del jugador en el precio también está confirmado: crece con su volumen y patrimonio.

- **Oferta:** mineros NPC por región (una huelga la reduce), más lo que vende el jugador y sus empleados.
- **Demanda:** por **sectores** (ferrocarril, energía, militar, agricultura, lujo, tecnología). Cada mineral alimenta varios sectores, y un evento en un sector arrastra a sus minerales. ⏳ F4-31 Qué sectores alimenta cada mineral.
- ✅ El jugador es un actor pequeño al inicio y grande al final: su impacto en el precio **crece con su volumen y su patrimonio** (decisión del autor, 2026-10-15). ⏳ F0-53 El simulador debe comprobar que ese impacto no crea bucles de ganancia; ⏳ F0-52 los valores.

## Bots y mercado interno ✅

**Estado:** el mercado interno con «IA», Esteban como rival y los cuatro arquetipos (industrial, especulador, acaparador y pánico) están confirmados (alcance de F3-06); el comportamiento fino de cada uno ⏳ F3-06 y su ajuste con los 10 minerales ⏳ F4-39.

✅ Mercado interno con «IA»: clientes con requisitos, bots que participan.

✅ No requiere IA real. Se simula de forma agregada con 4 arquetipos (F3-06, «Bots agregados»):

| Arquetipo | Comportamiento |
|---|---|
| Industrial | Compra constante según su sector; da estabilidad |
| Especulador | Sigue la tendencia; amplifica subidas y caídas |
| Acaparador | Compra en bajas y retiene; reduce la oferta |
| Pánico | Vende cuando cae; acelera las caídas |

✅ Esteban Arvel puede actuar como rival nominal que compite por contratos y compras grandes ([19](19-elenco-a-fondo.md)).

## Noticias: el motor de información ✅

**Estado:** las noticias, la prensa del Acto I, el modelo de evento real y medio con sesgo, y que el jugador cruza fuentes están confirmados ([07](07-sociedad-y-eventos.md), «Prensa»; [18](18-biblia-narrativa.md), 1.10). Las noticias de cada categoría ⏳ F4-33, ⏳ F4-34, ⏳ F4-35, ⏳ F4-36 y ⏳ F4-37, y los avisos previos de los eventos ⏳ F4-88.

✅ Anuncian cosas como que el precio de un mineral va a subir en cierta fecha.

✅ **En el Acto I la prensa es solo el Heraldo (noticia oficial) y el Teletipo (rumor)**, con un tope de 1 noticia y 1 rumor por día ([27](27-guion-del-acto-i.md)). La prensa con sesgos y el cruzar fuentes entran en el Acto II.

Separan **lo que pasa** de **lo que se publica**:

1. El sistema crea un **evento real** (huelga, descubrimiento, decreto) con fecha y magnitud.
2. Cada medio lo **reporta con su sesgo, retraso y ruido** (el Heraldo minimiza lo laboral, La Voz exagera, el Teletipo se adelanta pero a veces se equivoca; ver [07](07-sociedad-y-eventos.md)).
3. El jugador cruza fuentes y decide.

Cada noticia tiene nivel de confianza: **confirmada**, **rumor** o **falsa alarma**. Los tipos de evento tienen **firmas reconocibles** para que se pueda aprender.

Categorías: producción, política, laboral, tecnológico, clima, guerra/exterior, moda de lujo, descubrimiento.

## Información por capas ✅

**Estado:** confirmado que parte es gratis y parte se compra, qué trae el Acto I y que las capas se desbloquean con dinero (F3-01); el precio de cada mejora ⏳ F0-52.

✅ Parte es gratis y parte se compra; con el tiempo el jugador ve más y de forma más visual.

| Capa | Qué muestra | Cómo se obtiene |
|---|---|---|
| 1 · Básica (gratis) | Precio actual, flecha de tendencia | Desde el inicio ✅ |
| 2 · Prensa | Titulares y rumores | **Gratis en el Acto I** (Heraldo y Teletipo); **de pago y con sesgo desde el Acto II**, cada medio cuesta ✅ ⏳ F3-03 |
| 3 · Análisis | Gráficos de 7/30 días, oferta vs. demanda | Mejora de pago ✅ ⏳ F3-01. El Analista, que llega en el Acto III ✅, la aporta además como empleado ([04](04-progresion-y-meta.md)) |
| 4 · Tabulador | Valor justo estimado **con margen de error**, sobre/infravalorado | Mejora avanzada de pago ✅. ⏳ F3-04 Qué achica el margen de error (propuesta: el **Ojo**) |

✅ Las capas 3 y 4 no existen en el Acto I ([27](27-guion-del-acto-i.md)).

## Cómo se compra y se vende (y qué frena los abusos) ✅

**Estado:** la lista de frenos y el tope diario más amplio de la Aetherita están confirmados (lista de cifras de F0-52 acordada el 2026-10-15; F2-07 los construye); las cifras ⏳ F0-52.

El mayor riesgo del mercado simulado es que el jugador encuentre un truco para hacerse rico sin esfuerzo. Frenos:

| Freno | Efecto |
|---|---|
| **Spread** | Comprar cuesta más de lo que se vende; evita arbitraje infinito |
| **Slippage** | Vender mucho de golpe baja el precio; hay que vender en tandas |
| **Costo de almacén** | Guardar cuesta, así que especular tiene riesgo real |
| **Impuestos y licencias** | Un porcentaje se va al Ministerio |
| **Límite de variación diaria** | El precio no se mueve más de X % por día. En la Aetherita el tope es **más amplio** ✅, porque es el mineral más volátil |
| **Tope diario por comprador** | Cada comprador NPC absorbe solo cierto volumen |

⏳ F0-52 Spread, slippage, tope diario, renta del almacén, costo de guardar e impuestos. ⏳ F2-07 Su construcción.

## Canales de venta y compra ✅

| Canal | Descripción |
|---|---|
| Mercado spot | Precio de mercado, con slippage y spread |
| Pedidos y contratos | ✅ Requisitos de clientes con precio, plazo y penalización |
| Trueque / canje | ✅ Intercambiar con comerciantes (relaciones y reputación) |
| Marketplace | ✅ Para comprar los materiales que faltan |
| **Mercado negro** | ✅ Paga más pero tiene riesgos (ver abajo) |

## Contratos y pedidos ✅

✅ Cada contrato tiene: mineral, cantidad, plazo, precio (prima o descuento sobre el mercado) y penalización por fallar. (La **calidad** como requisito queda para después del MVP.)

✅ Qué tipos hay y cuándo entra cada uno (decisión del autor, 2026-10-15):

| Tipo | Descripción | Entra en |
|---|---|---|
| Estándar | El pan de cada día | Acto I |
| Urgente | Prima alta, plazo corto | Acto I |
| Negro | Pagan bien, con riesgo de inspecciones | Acto II |
| A largo plazo | Precio fijo (versión sencilla de un futuro); puede salir bien o mal | Acto III |
| Oficial del Ministerio | Cuotas obligatorias que chocan con el mercado | Acto III |

✅ En el Acto I los encargos se llaman «pedidos de cliente»; «contrato» queda del Acto II en adelante ([27](27-guion-del-acto-i.md)).

## Mercado negro y vigilancia ✅

**Estado:** confirmado qué es, dónde y cuándo se opera, los cuatro niveles de vigilancia y la redada; las consecuencias de cada nivel ⏳ F4-67 y ⏳ F4-68; las cifras ⏳ F0-52.

✅ El mercado negro **paga más pero tiene riesgos**. La idea es que no se use siempre, porque repercute. Hay un **indicador de vigilancia** de las autoridades; si el jugador se pasa de listo, se pagan **multas**.

### Qué ofrece ✅

- ✅ Precios mejores que el spot. Cuánto más ⏳ F0-52 (rango orientativo +20–40 %, variable por mineral).
- ✅ Ventas **sin impuesto** ([26](26-zonas-y-edificios.md), mostrador sin sello del bar: «sin impuesto y con prima de mercado negro, a cambio de vigilancia»).
- ✅ Ventas **sin licencia**.
- ✅ Acceso a bienes restringidos o en cuota (por ejemplo, grandes volúmenes de salitre).
- ✅ **Aetherita en el Acto III:** su precio ya se ve, pero solo se compra aquí, con Casilda, como mercancía escasa. La extracción no ocurre hasta el Acto IV.
- ✅ **Cuándo y dónde:** se opera **de noche**, en el **Bar del Farol de Salinas Blancas** (viajando hasta allí) y también con la **visita nocturna de Casilda a la tienda**. Esa visita **no es el modo tienda**: la tienda no se abre de noche ([01](01-core-loop.md)). El volumen es limitado por noche ⏳ F0-52, y cuánto cuesta en bloques ⏳ F4-72.
- ✅ **Acceso por contacto:** Casilda y Los Faroleros abren el mercado negro en el Acto II. Los Faroleros no tienen medidor propio: se miden por la alianza que elijas ([07](07-sociedad-y-eventos.md)).

### Indicador de vigilancia ✅

**Estado:** confirmado el indicador global, los cuatro niveles, la redada y que suspender la licencia no baja el estatus; las consecuencias de cada nivel y cómo se muestra ⏳ F4-67, ⏳ F4-68 y ⏳ F4-77.

✅ Es **un solo indicador global**, de 0 a 100, que **sube** con cada operación negra (según volumen y valor) y **baja** con el tiempo. Los cambios se cuentan en **puntos** (por ejemplo, «vigilancia +10»); el «%» solo sirve para el ritmo con que sube o baja por sí solo, y las cifras ⏳ F0-52. No hay un indicador por lugar.

✅ Tiene **cuatro niveles, sin solaparse** (decisión del autor, 2026-10-15). Se llaman «niveles», porque «tramo» es de los medidores de relación ([24](24-umbrales-de-acto.md)):

| Nivel | Rango | Consecuencias |
|---|---|---|
| Tranquilo | 0–29 ✅ | Nada |
| Observado | 30–59 ✅ | Inspecciones ocasionales, multas leves |
| Vigilado | 60–84 ✅ | Inspecciones frecuentes, multas fuertes, contratos oficiales bloqueados |
| Bajo investigación | 85–100 ✅ | Redada (abajo) |

⏳ F0-52 Las cifras exactas de cada nivel y el ritmo de subida y bajada. ⏳ F4-67 El indicador y sus niveles, y ⏳ F4-68 las inspecciones y multas de cada uno.

✅ Llegar a «Bajo investigación» es la **redada**: no es una falla de la partida. Tras una redada la vigilancia **baja a unos 60** y el **mercado negro cierra unos días** ⏳ F0-52. Además hay confiscación del stock negro, cierre temporal de la tienda, licencia en riesgo y posible arresto (pierde días) ⏳ F4-69.

✅ **Suspender la licencia no baja el estatus** ([24](24-umbrales-de-acto.md)).

✅ Aplicación del pilar «la información es poder»: al principio solo ves el nivel de forma vaga, sin la cifra, y el valor exacto se descubre con fuentes (Quiroga, Lucía). ⏳ F4-67 Cómo se muestra y se descubre; ⏳ F4-77 su pantalla.

### Cómo bajar la vigilancia ✅

- ✅ **Esperar:** baja sola con el tiempo.
- ✅ **Sobornar al Inspector Quiroga.** Cada soborno cuesta más que el anterior y **no hay medidor de «corrupción»**: el costo creciente es el único freno ⏳ F4-70.
- ⏳ F4-70 Las demás formas: decisiones de la historia que la bajan (por ejemplo, conseguirle el retiro a Quiroga, [23](23-arbol-de-decisiones.md)), pagar a Los Faroleros (que alivian inspecciones) y contratar guardias.

### Multas ✅

✅ Las multas escalan con la dificultad. Su valor y frecuencia ⏳ F0-52, su construcción ⏳ F4-68 y su ajuste ⏳ F5-07.

## Refinado y valor agregado ✅

**Estado:** confirmado que entra en la primera versión, la tabla de productos y el taller (se construye en el MVP y se abre en el Acto II); cómo funciona un lote ⏳ F3-07, ⏳ F4-56 y ⏳ F4-102.

Mena → lingote (+valor) → producto. Productos que alimentan a las industrias:

| Producto | Ingredientes |
|---|---|
| Acero | Hierro + carbón |
| Conductor | Cobre + plata |
| Oscilador | Cuarzo (clave del detector y las radios) |
| Joyería | Oro/plata + gemas |
| Pólvora | Salitre + carbón |
| Celda de éter | Aetherita + cuarzo |

✅ Se hace en el **taller** de la tienda. El taller se construye en el MVP (⏳ F3-07) pero **se abre en el Acto II**: el Acto I no lo usa ([27](27-guion-del-acto-i.md)).

✅ El refinado es un minijuego de dos parámetros: temperatura ↔ tiempo (ver [09](09-minijuegos.md); ⏳ F4-56). ⏳ F3-07 Cuánto tarda un lote y cómo se recoge. ⏳ F4-102 El Refinador, que funde y refina en tu lugar ([04](04-progresion-y-meta.md)).

Da utilidad real a cada mineral y evita que todo sea «extraer y vender crudo».

⏳ F3-07 Receta detallada del refinado (tiempos, rendimiento, cantidades).

## Tienda ✅

**Estado:** confirmadas la tienda, el modo tienda, la tasación y las dinámicas de reponer, regatear y cumplir pedidos; el refinado ⏳ F4-56.

✅ El jugador tiene una tienda que empieza modesta y mejora (espacio, stock, almacenamiento). **Una mejora de la tienda es condición para poder contratar empleados** ([04](04-progresion-y-meta.md)). Se compra en la propia tienda, desde el Acto II, con dinero; en el Acto I el botón «Contratar» se ve bloqueado con ese motivo. Cuál y cuánto cuesta ⏳ F0-52.

✅ **Modo tienda.** Empieza en el momento en que decides abrirla, en el bloque que quieras (mañana o tarde, nunca de noche) y cuesta un bloque completo ([01](01-core-loop.md)). Ahí se comercia y se gestiona.

### Dinámicas del modo tienda ✅

Inspiradas en cómo Dave the Diver sirve comidas. Los empleados pueden automatizarlas (ver [04](04-progresion-y-meta.md)).

| Dinámica | Mecánica |
|---|---|
| Reponer estantes | ✅ Arrastrar mercancía a los estantes y fijar precios ([26](26-zonas-y-edificios.md), tienda del puesto; [27](27-guion-del-acto-i.md), día 2) |
| Atender clientes / regatear | ✅ Minijuego de dos parámetros: tu oferta ↔ paciencia del cliente ([09](09-minijuegos.md); ⏳ F2-19) |
| Tasar | ✅ Detectar gemas falsas ([09](09-minijuegos.md)) |
| Refinar / fundir | Minijuego de temperatura ↔ tiempo ⏳ F4-56 (desde el Acto II) |
| Cumplir un pedido | ✅ Reunir y entregar a tiempo (pedido de cliente, [27](27-guion-del-acto-i.md); ⏳ F3-05) |

## Almacén ✅

✅ Inventario de almacén con capacidad limitada, mejorable.

✅ Costos de almacenamiento y regulación de costos.

✅ Hay **renta** del almacén y un **costo de guardar**; **la mercancía no se deteriora**, así que especular tiene un costo real sin riesgo de que se pudra. Las cifras ⏳ F0-52.

## Utilidad de los minerales ✅

- **Refinado:** mena → lingote → producto.
- **Mejora de herramientas y equipo** (ver [02](02-extraccion.md)).
- **Demanda de industrias NPC.**
- **Lujo / estatus** (ligado al estilo de vida).

## Sumideros de dinero ✅

Reparar herramientas (dinero y materiales), renta del almacén y costo de guardar, impuestos y licencias, **impuesto predial** (de las casas, [26](26-zonas-y-edificios.md)), **mora** (lo que pasa si no pagas; nunca cierra una puerta, [24](24-umbrales-de-acto.md)), salarios, multas y estilo de vida. Evitan que el dinero pierda sentido a largo plazo. Las cifras ⏳ F0-52.

## Procedural ✅

✅ Las partidas son distintas: se usan elementos procedurales. **Reglas fijas, mundo variable**: el jugador aprende las reglas, no memoriza un mapa.

✅ Decisión del autor (2026-10-15). Con la semilla de la partida **varían** las probabilidades de hallazgo, los precios iniciales, los eventos sueltos y algunos nombres. **No varían** el mineral de cada zona ni las noticias guionizadas del Acto I. La facción de Reme se sortea aparte ([22](22-acto-ii-variantes.md)). ⏳ F4-168

## Fuera de la primera versión ✅

- **Calidad de minerales** (común, buena, excelente): idea aceptada, para después del MVP. El resultado del minijuego daría una calidad que multiplica el precio y cumple requisitos de contratos.

## Nota técnica ✅

El mercado debe construirse como un **módulo independiente que se pueda simular offline durante miles de días**, para balancearlo antes de depender de la interfaz ([10](10-tecnico-y-herramientas.md), [14](14-arquitectura-y-modularidad.md)).

## Pendiente

- ⏳ F2-04 Fórmulas concretas del modelo de precios.
- ⏳ F0-52 Números base: precios, volatilidades, spreads, impuestos y el resto de las cifras de este documento. ⏳ F4-68 y ⏳ F5-07 El valor y la frecuencia de las multas del mercado negro.
- ⏳ F0-52 Precios de las mejoras de información.
- ⏳ F3-07 Receta detallada del refinado (tiempos, rendimiento, cantidades).
