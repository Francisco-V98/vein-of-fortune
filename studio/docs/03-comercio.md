# 03 · Comercio y mercado

## Principios ✅

- ✅ Mercado que se comporta de forma creíble: precios que suben y bajan, especulación (comprar barato, vender caro, guardar hasta que suba).
- ✅ Los materiales tienen **funcionalidad y uso** en el juego, no solo se compran y venden.
- ✅ El juego **incentiva** la comercialización y requiere revisar noticias y gráficos.
- ✅ Hay que saber si un mineral está sobrevalorado o infravalorado, y si conviene minar uno u otro.
- ✅ Es un mercado de dificultad media: más amable que EVE, pero con patrones reales que aprender.

## Cómo se mueve un precio ✅

**Estado:** el mercado se mueve 3 veces por día, y el modelo (valor justo, oferta y demanda, ruido y momentum) y la ficha de mercado están confirmados (alcance de F2-04, 2026-10-15), y las cifras base de los 10 minerales y de los frenos están acordadas como base de partida ✅ ([28](28-numeros-base-de-la-economia.md)); las fórmulas ⏳ F2-04.

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

✅ **Precios base** (esquirlas por unidad, siempre enteros; el total de cada operación se redondea una sola vez): carbón 50 · hierro 90 · cobre 170 · salitre 150 · plata 200 · cuarzo 300 · oro 420 · esmeralda 800 · diamante 1 800 · Aetherita 6 000. La volatilidad, la liquidez y el costo de guardar de cada mineral están en [28](28-numeros-base-de-la-economia.md); el **costo de guardar** va de 0,03 % (Aetherita y diamante) a 0,15 % (carbón y hierro) del precio base por unidad y día, con un mínimo de 1 esquirla por lote.

✅ **Estaciones, festivos y mercado (F0-94):** la estacionalidad por mineral sigue siendo la de [28](28-numeros-base-de-la-economia.md), sección 3.3. Los festivos fijos (1 o 2 por estación, 6 a 8 al año) mueven el mercado **±2 puntos como máximo** y las dificultades sociales o políticas de las mini-historias pueden mover un precio si hace falta, siempre como ficha del calendario ([29](29-calendario-y-temporadas.md)). Nada del clima mueve precios por sí solo en la versión 1; el efecto de clima en la producción es ⏳ F6-77.

✅ **Cómo se escriben los cambios de precio** (regla única, decisión del autor, 2026-10-15): un **«punto»** a secas es el **1 % del precio base** del mineral (no del precio del momento, para que los puntos se sumen): «carbón +3 puntos» son +3 % de 50 esquirlas, o sea +1,5. En la **deuda** se escribe **«pp»** (punto porcentual de interés: «−1 pp» es pasar del 4 % al 3 % mensual). En la **vigilancia** se escribe «vigilancia +10», nunca «+10 puntos». El «%» queda para ritmos y proporciones («sube un 20 % más despacio»).

### Personalidad de cada mineral ✅

Niveles de volatilidad, tope de variación diaria y qué mueve a cada mineral, a partir de [05](05-mundo-y-minerales.md). El orden de la volatilidad es hierro < carbón ≈ oro < cobre ≈ plata ≈ cuarzo < salitre < esmeralda ≈ diamante < Aetherita ([28](28-numeros-base-de-la-economia.md)).

| Mineral | Volatilidad | Tope diario ✅ | Qué lo mueve más |
|---|---|---|---|
| Carbón | Baja–media | 6 % | Estación (invierno), huelgas |
| Hierro | Baja | 5 % | Contratos de guerra, ferrocarriles |
| Cobre | Media | 8 % | Obras eléctricas, escasez (apagones) |
| Salitre | Media–alta | 10 % | Cosechas, puertos, Faroleros |
| Plata | Media | 8 % | Industria, joyería |
| Oro | Baja–media | 6 % | Política, reservas del Estado |
| Cuarzo | Media | 8 % | Demanda tecnológica |
| Esmeralda | Alta | 12 % | Modas de la élite |
| Diamante | Alta | 12 % | Lujo, industria de corte |
| Aetherita | Muy alta | 15 % | Descubrimientos, secreto de Estado |

Tipos generales: estable, volátil, estacional, estratégico, lujo (ver [05](05-mundo-y-minerales.md)).

## Oferta y demanda ✅

**Estado:** la oferta por mineros NPC y las huelgas ([07](07-sociedad-y-eventos.md)) y la demanda por los seis sectores (alcance de F4-31) están confirmadas; qué sectores alimenta cada mineral ⏳ F4-31. El peso del jugador en el precio también está confirmado: crece con su volumen y patrimonio.

- **Oferta:** mineros NPC por región (una huelga la reduce), más lo que vende el jugador y sus empleados.
- **Demanda:** por **sectores** (ferrocarril, energía, militar, agricultura, lujo, tecnología). Cada mineral alimenta varios sectores, y un evento en un sector arrastra a sus minerales. Los pesos de partida de cada mineral en sus sectores están acordados ✅ ([28](28-numeros-base-de-la-economia.md): por ejemplo, el carbón es 55 % energía, el hierro 45 % ferrocarril y 35 % militar); ⏳ F4-31 construye el modelo y los eventos con esos pesos.
- ✅ El jugador es un actor pequeño al inicio y grande al final: su impacto en el precio **crece con su volumen y su patrimonio** (decisión del autor, 2026-10-15). El peso del jugador va de 0,5 en el Acto I a 0,6 en el II, 1,0 en el III y 1,6 en el IV (máximo 4; decisión del autor, 2026-10-16), y su impacto se disipa un 25 % por bloque ✅ ([28](28-numeros-base-de-la-economia.md)). ✅ El simulador (F0-53, regla E3) comprobó que ese impacto **no crea bucles de ganancia**: vender y recomprar pierde ≈ 5,9 % y comprar, esperar hasta 8 bloques y vender también pierde, con cualquier peso del jugador.

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

**Estado:** confirmado que parte es gratis y parte se compra, qué trae el Acto I y que las capas se desbloquean con dinero (F3-01); el precio de cada mejora está acordado ✅ ([28](28-numeros-base-de-la-economia.md)).

✅ Parte es gratis y parte se compra; con el tiempo el jugador ve más y de forma más visual.

| Capa | Qué muestra | Cómo se obtiene |
|---|---|---|
| 1 · Básica (gratis) | Precio actual, flecha de tendencia | Desde el inicio ✅ |
| 2 · Prensa | Titulares y rumores | **Gratis en el Acto I** (Heraldo y Teletipo); **de pago y con sesgo desde el Acto II**: suscripción de 28 días de **220 esquirlas** el Heraldo, **220** La Voz y **450** el Teletipo ✅ (un ejemplar suelto cuesta 10 · 10 · 20 y un rumor comprado 40). ⏳ F3-03 |
| 3 · Análisis | Gráficos de 7/30 días, oferta vs. demanda | Mejora de pago de **3 000 esquirlas**, una sola vez ✅. ⏳ F3-01. El Analista, que llega en el Acto III ✅, la aporta además como empleado ([04](04-progresion-y-meta.md)) |
| 4 · Tabulador | Valor justo estimado **con margen de error**, sobre/infravalorado | Mejora avanzada de pago de **18 000 esquirlas**, una sola vez; el margen de error es de ±12 puntos y baja con el Ojo hasta ±4 ✅. ⏳ F3-04 Qué achica el margen de error (propuesta: el **Ojo**) |

✅ Las capas 3 y 4 no existen en el Acto I ([27](27-guion-del-acto-i.md)).

## Cómo se compra y se vende (y qué frena los abusos) ✅

**Estado:** la lista de frenos y el tope diario más amplio de la Aetherita están confirmados (F2-07 los construye); las cifras base están acordadas ✅ ([28](28-numeros-base-de-la-economia.md)).

El mayor riesgo del mercado simulado es que el jugador encuentre un truco para hacerse rico sin esfuerzo. Frenos:

| Freno | Efecto |
|---|---|
| **Spread** | Comprar cuesta más de lo que se vende; evita arbitraje infinito |
| **Slippage** | Vender mucho de golpe baja el precio; hay que vender en tandas |
| **Costo de almacén** | Guardar cuesta, así que especular tiene riesgo real |
| **Impuestos y licencias** | Un porcentaje se va al Ministerio |
| **Límite de variación diaria** | El precio no se mueve más de **5–15 % por día** según el mineral (hierro 5 %, carbón y oro 6 %, esmeralda y diamante 12 %). En la Aetherita el tope es **más amplio** (15 %) ✅, porque es el mineral más volátil |
| **Tope diario por comprador** | Cada comprador NPC absorbe solo cierto volumen |

Cifras base ✅ ([28](28-numeros-base-de-la-economia.md)):

- **Spread:** 2 a 8 % de ida y vuelta según el mineral (carbón, hierro, cobre y oro 2 %; salitre, plata y cuarzo 3 %; esmeralda y diamante 5 %; Aetherita 8 %). Se compra a valor justo × (1 + s/2) y se vende a × (1 − s/2).
- **Impuesto de ventas:** **3 %** en el mercado spot, la tienda y los pedidos y contratos; **0 %** en el mercado negro. La Bolsa de Puerto Meridiano (Acto III) cobra la mitad de spread y ningún impuesto de venta.
- **Slippage:** el precio cae según las unidades que vendes frente a la liquidez del mineral (de 10 unidades por −1 % en el carbón a 0,8 en la Aetherita) y a los compradores del mundo (2, 3, 5 y 8 por acto). Se recupera un 25 % por bloque.
- **Tope diario por comprador:** unas 3 veces la liquidez por día y por comprador (de 30 unidades de carbón a 2 de Aetherita).
- **Marketplace:** comprar lo que falta cuesta el valor justo × 1,18.
- **Almacén:** capacidad y renta, en «Almacén» más abajo.
- **Licencias** (renovación cada 28 días): Minero con licencia 150 · Comerciante 900 · Empresario 4 500 · Magnate 17 000 esquirlas (decisión del autor, 2026-10-16).

⏳ F2-07 Su construcción.

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

| Tipo | Descripción | Entra en | Cifras base ✅ |
|---|---|---|---|
| Estándar | El pan de cada día | Acto I | +12 % sobre el valor justo, plazo de 3–7 días; en el Acto I se pierde sin castigo y desde el II la penalización es el 15 % del valor |
| Urgente | Prima alta, plazo corto | Acto I | +35 %, plazo de 1–3 días; en el Acto I la penalización es de 5 % como máximo y nunca bloquea; desde el II, 30 % |
| Negro | Pagan bien, con riesgo de inspecciones | Acto II | La prima de su mineral (20–35 %), sin impuesto; plazo de 2–4 días; penalización de 25 % del valor y vigilancia +8 |
| A largo plazo | Precio fijo (versión sencilla de un futuro); puede salir bien o mal | Acto III | Precio fijo al valor justo del día de la firma; entregas semanales, plazo de 14–28 días; penalización de 40 % |
| Oficial del Ministerio | Cuotas obligatorias que chocan con el mercado | Acto III | +8 %, plazo de 7–14 días; penalización de 50 % y vigilancia +10 |

✅ En el Acto I los encargos se llaman «pedidos de cliente»; «contrato» queda del Acto II en adelante ([27](27-guion-del-acto-i.md)).

✅ **Frecuencia fuera del Acto I (decisión del autor, 2026-10-15).** El Acto I está guionizado. Desde el II llega **un pedido estándar cada 2 días** (de 1 a 2 días de producción media, +12 %) y **un urgente por semana** (+35 %); entre todos aportan como máximo el **15 % del ingreso**, y el simulador mide que aportan menos de un 4 %. Los contratos a largo plazo y los oficiales llegan según su acto. **Los pedidos se cumplen solo con mercancía propia**, como la tienda ([28](28-numeros-base-de-la-economia.md)).

## Mercado negro y vigilancia ✅

**Estado:** confirmado qué es, dónde y cuándo se opera, los cuatro niveles de vigilancia y la redada; las consecuencias de cada nivel ⏳ F4-67 y ⏳ F4-68; las cifras base están acordadas ✅ ([28](28-numeros-base-de-la-economia.md)).

✅ El mercado negro **paga más pero tiene riesgos**. La idea es que no se use siempre, porque repercute. Hay un **indicador de vigilancia** de las autoridades; si el jugador se pasa de listo, se pagan **multas**.

### Qué ofrece ✅

- ✅ Precios mejores que el spot, con una **prima sobre el valor justo** que varía por mineral: carbón y hierro 20 % · cobre 22 % · plata y cuarzo 25 % · oro y Aetherita 30 % · esmeralda 32 % · salitre y diamante 35 % ([28](28-numeros-base-de-la-economia.md)). Como tampoco paga el 3 % de impuesto, la ganancia real frente al spot es la prima más ≈ 4 %.
- ✅ Ventas **sin impuesto** ([26](26-zonas-y-edificios.md), mostrador sin sello del bar: «sin impuesto y con prima de mercado negro, a cambio de vigilancia»).
- ✅ Ventas **sin licencia**.
- ✅ Acceso a bienes restringidos o en cuota (por ejemplo, grandes volúmenes de salitre).
- ✅ **Aetherita en el Acto III:** su precio ya se ve, pero solo se compra aquí, con Casilda, como mercancía escasa. La extracción no ocurre hasta el Acto IV.
- ✅ **Aetherita en el Acto IV (decisión del autor, 2026-10-15 y 2026-10-16):** la que extraes la vendes por un **canal legal con tope**: la **Comisión del Éter** la compra en una **oficina de Puerto Meridiano, siempre abierta**, hasta **5 viales al día**, a valor justo sin prima y con el impuesto de 3 % ([28](28-numeros-base-de-la-economia.md)). En el mercado negro la Aetherita solo entra como **encargo especial**, con trasfondo e historia: raro (uno cada ≈ 21 días; si Casilda es la compradora elegida en el final, cada ≈ 14 días y con más historia, con la prima en +10 a +15 puntos), de pocos viales (1 o 2), a veces una compra sin mucho detalle, nunca un canal rutinario ni de grandes cantidades. La vigilancia no depende de la Aetherita: sus encargos especiales añaden menos de un tercio de lo que la vigilancia baja sola.
- ✅ **Cuándo y dónde:** se opera **de noche**, en el **Bar del Farol de Salinas Blancas** (viajando hasta allí) y también con la **visita nocturna de Casilda a la tienda**. Esa visita **no es el modo tienda**: la tienda no se abre de noche ([01](01-core-loop.md)). El volumen es limitado por noche: **3 300 esquirlas de valor en el Acto II, 12 000 en el III y 55 000 en el IV**, ✅. La Aetherita ya no forma parte de las noches negras de rutina: en el Acto IV se vende por el **canal legal de la Comisión del Éter** y en el mercado negro solo aparece como **encargo especial** (ver más abajo). Cuánto cuesta en bloques una noche negra ⏳ F4-72: el simulador da el máximo que compensa, 0,97 bloques en el II, 0,95 en el III y 0,85 en el IV.
- ✅ **Acceso por contacto:** Casilda y Los Faroleros abren el mercado negro en el Acto II. Los Faroleros no tienen medidor propio: se miden por la alianza que elijas ([07](07-sociedad-y-eventos.md)).

### Indicador de vigilancia ✅

**Estado:** confirmado el indicador global, los cuatro niveles, la redada y que suspender la licencia no baja el estatus; las consecuencias de cada nivel y cómo se muestra ⏳ F4-67, ⏳ F4-68 y ⏳ F4-77.

✅ Es **un solo indicador global**, de 0 a 100, que **sube** con cada operación negra (según volumen y valor) y **baja** con el tiempo. Los cambios se escriben «vigilancia +10» o «vigilancia −15» (nunca «puntos» a secas); el «%» solo sirve para el ritmo con que sube o baja por sí solo. Cada operación negra sube la vigilancia entre **+4 y +12**, según su valor frente al volumen máximo de la noche, y la vigilancia **baja sola 2 al día** (también los días con operación) ✅. La alianza con Los Faroleros hace que suba un 20 % más despacio. No hay un indicador por lugar.

✅ Tiene **cuatro niveles, sin solaparse** (decisión del autor, 2026-10-15). Se llaman «niveles», porque «tramo» es de los medidores de relación ([24](24-umbrales-de-acto.md)):

| Nivel | Rango | Consecuencias |
|---|---|---|
| Tranquilo | 0–29 ✅ | Nada |
| Observado | 30–59 ✅ | Inspecciones ocasionales, multas leves |
| Vigilado | 60–84 ✅ | Inspecciones frecuentes, multas fuertes, contratos oficiales bloqueados |
| Bajo investigación | 85–100 ✅ | Redada (abajo) |

Cifras base de cada nivel ✅ ([28](28-numeros-base-de-la-economia.md)):

- **Observado:** cada operación negra tiene un 20 % de inspección; la multa leve es el **1 % del patrimonio** (mínimo 60 esquirlas).
- **Vigilado:** 50 % de inspección; la multa fuerte es el **3 % del patrimonio** (mínimo 300) más el decomiso del 25 % del lote.
- **Bajo investigación:** redada (abajo).

⏳ F4-67 El indicador y sus niveles, y ⏳ F4-68 las inspecciones y multas de cada uno.

✅ Llegar a «Bajo investigación» es la **redada**: no es una falla de la partida. Tras una redada la vigilancia **baja a 60** (el primer valor de Vigilado) y el **mercado negro cierra 7 días** ✅. Además hay confiscación del lote de esa noche y del stock negro, una **multa del 6 % del patrimonio** (mínimo 600) y la **tienda cerrada 2 días** ✅; la licencia en riesgo y el posible arresto (1 día perdido, con un 25 % de probabilidad en Difícil y Hardcore) ⏳ F4-69.

✅ **Suspender la licencia no baja el estatus** ([24](24-umbrales-de-acto.md)).

✅ Aplicación del pilar «la información es poder»: al principio solo ves el nivel de forma vaga, sin la cifra, y el valor exacto se descubre con fuentes (Quiroga, Lucía). ⏳ F4-67 Cómo se muestra y se descubre; ⏳ F4-77 su pantalla.

### Cómo bajar la vigilancia ✅

- ✅ **Esperar:** baja sola con el tiempo.
- ✅ **Sobornar al Inspector Quiroga.** Cada soborno cuesta más que el anterior (**(500 + 0,8 % del patrimonio) × 1,35 por cada soborno ya hecho**) y baja la vigilancia **15**; el contador de sobornos baja 1 cada 56 días ✅. **No hay medidor de «corrupción»**: el costo creciente es el único freno ⏳ F4-70.
- ⏳ F4-70 Las demás formas: decisiones de la historia que la bajan (por ejemplo, conseguirle el retiro a Quiroga, [23](23-arbol-de-decisiones.md)), pagar a Los Faroleros (que alivian inspecciones) y contratar guardias (cada guardia baja la vigilancia 0,25 más al día, hasta 3 guardias ✅).

### Multas ✅

✅ Las multas escalan con la dificultad: se multiplican por **0,7 en Novato, 1 en Intermedio, 1,4 en Difícil y 2 en Hardcore** ✅. Su valor y frecuencia son los de arriba ([28](28-numeros-base-de-la-economia.md)); su construcción ⏳ F4-68 y su ajuste ⏳ F5-07.

## Refinado y valor agregado ✅

**Estado:** confirmado que entra en la primera versión, la tabla de productos y el taller (se construye en el MVP y se abre en el Acto II); cómo funciona un lote ⏳ F3-07, ⏳ F4-56 y ⏳ F4-102.

Mena → lingote (+valor) → producto, la cadena de refinado. Productos que alimentan a las industrias:

| Producto | Ingredientes | Desde |
|---|---|---|
| Acero | Hierro + carbón | Acto II ✅ |
| Pólvora | Salitre + carbón | Acto II ✅ |
| Conductor | Cobre + plata | Acto II ✅ |
| Oscilador | Cuarzo (clave del detector y las radios) | Acto II ✅ |
| Joyería | Oro/plata + gemas | Acto III ✅ |
| Celda de éter | Aetherita + cuarzo | Acto IV ✅ |

✅ **Cada receta tiene su acto** (decisión del autor, 2026-10-16). El taller abre en el Acto II con Acero, Pólvora, Conductor y Oscilador (la primera versión de ⏳ F3-07 empieza con acero y pólvora). La **Joyería** llega en el Acto III, porque ninguna gema existe antes (esmeralda y diamante son tier 4, [26](26-zonas-y-edificios.md)). La **Celda de éter** llega en el Acto IV, con la Aetherita (tier 5).

✅ **La Celda de éter es el único uso rutinario de la Aetherita en productos** (decisión del autor, 2026-10-16). Excepción: puede aparecer, casi nunca, en prendas de joyería (un collar o similar), muy raras y extremadamente caras, hechas con los materiales más caros y súper limitadas. No cambia la receta de Joyería ni ninguna cifra.

✅ **La Celda de éter no se vende en la tienda ni en los pedidos de cliente.** Solo la compran la **Comisión del Éter** o el **Consorcio**, y fabricarla consume **viales del mismo tope diario de la Aetherita** (5 viales al día en la oficina de la Comisión de Puerto Meridiano, [28](28-numeros-base-de-la-economia.md)): un vial en una Celda es un vial que no vendes a la Comisión ese día. La tienda y los pedidos siguen aceptando solo mercancía propia extraída o refinada, y la Celda queda fuera por esta regla.

✅ Se hace en el **taller** de la tienda. El taller se construye en el MVP (⏳ F3-07) pero **se abre en el Acto II**: el Acto I no lo usa ([27](27-guion-del-acto-i.md)).

✅ El refinado es un minijuego de dos parámetros: temperatura ↔ tiempo (ver [09](09-minijuegos.md); ⏳ F4-56). ⏳ F3-07 Cuánto tarda un lote y cómo se recoge. ⏳ F4-102 El Refinador, que funde y refina en tu lugar ([04](04-progresion-y-meta.md)).

Da utilidad real a cada mineral y evita que todo sea «extraer y vender crudo».

⏳ F3-07 Receta detallada del refinado (tiempos, rendimiento, cantidades) de cada producto, incluidas la Joyería y la Celda de éter.

## Tienda ✅

**Estado:** confirmadas la tienda, el modo tienda, la tasación y las dinámicas de reponer, regatear y cumplir pedidos; el refinado ⏳ F4-56.

✅ El jugador tiene una tienda que empieza modesta y mejora (espacio, stock, almacenamiento). **Una mejora de la tienda es condición para poder contratar empleados** ([04](04-progresion-y-meta.md)). Se compra en la propia tienda, desde el Acto II, con dinero; en el Acto I el botón «Contratar» se ve bloqueado con ese motivo. La mejora es el **Puesto ampliado** y cuesta **3 500 esquirlas** ✅: sube las unidades por bloque de tienda de 16 a 40 y permite 2 empleados (1 Minero) ([28](28-numeros-base-de-la-economia.md)); ⏳ F4-245 la construye. En la tienda, el precio de lista es el valor justo × 1,20 y el cliente medio paga × 1,15, sin slippage, y las unidades por bloque según el nivel de la tienda son 16 · 40 · 60 · 80 · 100 ✅. **La tienda y los pedidos solo aceptan mercancía propia** (extraída o refinada) ✅ (decisión del autor, 2026-10-15): lo que compras en el mercado o en el marketplace sirve para mejorar herramientas, no para revenderlo en la tienda ni en un pedido. Sin esa regla, comprar al spot y revender en la tienda (×1,15 menos 3 % de impuesto, sin slippage) dejaba entre +7,5 y +10,6 % por vuelta.

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

✅ Hay **renta** del almacén y un **costo de guardar**; **la mercancía no se deteriora**, así que especular tiene un costo real sin riesgo de que se pudra. Cifras base ✅ ([28](28-numeros-base-de-la-economia.md)): la trastienda del Acto I guarda **40 unidades** sin renta; los cinco niveles del almacén guardan 120 · 300 · 700 · 1 600 · 3 500 unidades, con renta de 15 · 50 · 150 · 450 · 1 200 esquirlas al día, y la mejora cuesta 1 500 · 7 000 · 35 000 · 160 000 · 600 000.

## Utilidad de los minerales ✅

- **Refinado:** mena → lingote → producto.
- **Mejora de herramientas y equipo** (ver [02](02-extraccion.md)).
- **Demanda de industrias NPC.**
- **Lujo / estatus** (ligado al estilo de vida).

## Sumideros de dinero ✅

Reparar herramientas (dinero y materiales), renta del almacén y costo de guardar, impuestos y licencias, **impuesto predial** (de las casas, [26](26-zonas-y-edificios.md)), **mora** (lo que pasa si no pagas; nunca cierra una puerta, [24](24-umbrales-de-acto.md)), salarios, multas y estilo de vida. Evitan que el dinero pierda sentido a largo plazo. Las cifras base ya están acordadas ✅ ([28](28-numeros-base-de-la-economia.md)); por ejemplo, la reparación cuesta el 7–9 % del valor de una expedición y el impuesto predial es el 1 % al mes del valor de la casa.

## Procedural ✅

✅ Las partidas son distintas: se usan elementos procedurales. **Reglas fijas, mundo variable**: el jugador aprende las reglas, no memoriza un mapa.

✅ Decisión del autor (2026-10-15). Con la semilla de la partida **varían** las probabilidades de hallazgo, los precios iniciales, los eventos sueltos y algunos nombres. **No varían** el mineral de cada zona ni las noticias guionizadas del Acto I. La facción de Reme se sortea aparte ([22](22-acto-ii-variantes.md)). ⏳ F4-168

## Fuera de la primera versión ✅

- **Calidad de minerales** (común, buena, excelente): idea aceptada, para después del MVP. El resultado del minijuego daría una calidad que multiplica el precio y cumple requisitos de contratos.

## Nota técnica ✅

El mercado debe construirse como un **módulo independiente que se pueda simular offline durante miles de días**, para balancearlo antes de depender de la interfaz ([10](10-tecnico-y-herramientas.md), [14](14-arquitectura-y-modularidad.md)).

## Pendiente

- ⏳ F2-04 Fórmulas concretas del modelo de precios.
- ⏳ F4-68 y ⏳ F5-07 La construcción y el ajuste de las multas del mercado negro (las cifras base ya están acordadas, [28](28-numeros-base-de-la-economia.md)).
- ⏳ F3-07 Receta detallada del refinado (tiempos, rendimiento, cantidades) de cada producto, incluidas la Joyería y la Celda de éter.
