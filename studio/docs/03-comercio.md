# 03 · Comercio y mercado

## Principios

- ✅ Mercado que se comporta de forma creíble: precios que suben y bajan, especulación (comprar barato, vender caro, guardar hasta que suba).
- ✅ Los materiales tienen **funcionalidad y uso** en el juego, no solo se compran y venden.
- ✅ El juego **incentiva** la comercialización y requiere revisar noticias y gráficos.
- ✅ Hay que saber si un mineral está sobrevalorado o infravalorado, y si conviene minar uno u otro.
- ✅ Es un mercado de dificultad media: más amable que EVE, pero con patrones reales que aprender.

## Cómo se mueve un precio

🟡 Cada mineral tiene un **valor justo**, que se ajusta cada día según oferta, demanda y eventos. El precio real lo persigue **con retraso**, con **ruido** y **momentum**. Resumen: *el precio tiende hacia el valor justo, pero tarda, se pasa y se agita*. Genera tendencias y rebotes que se pueden aprender a leer sin ser predecibles.

✅ El mercado se mueve **3 veces por día**, una por bloque (mañana, tarde, noche). Esperar al bloque siguiente para vender es una decisión real.

### Ficha de mercado por mineral 🟡

| Parámetro | Qué controla |
|---|---|
| Precio base | Nivel de referencia |
| Volatilidad | Cuánto se agita |
| Liquidez | Cuánto cae el precio al vender mucho |
| Estacionalidad | Si sube o baja por épocas |
| Sensibilidad a eventos | Qué tipo de noticias lo mueven |
| Almacenabilidad | Si se deteriora o es costoso guardarlo |

### Personalidad de cada mineral 🟡

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

## Oferta y demanda 🟡

- **Oferta:** mineros NPC por región (una huelga la reduce), más lo que vende el jugador y sus empleados.
- **Demanda:** por **sectores** (ferrocarril, energía, militar, agricultura, lujo, tecnología). Cada mineral alimenta varios sectores, y un evento en un sector arrastra a sus minerales.
- El jugador es un actor pequeño al inicio y grande al final: su impacto en el precio crece con él.

## Bots y mercado interno

✅ Mercado interno con "IA": clientes con requisitos, bots que participan.

🟡 No requiere IA real. Se simula de forma agregada con 4 arquetipos:

| Arquetipo | Comportamiento |
|---|---|
| Industrial | Compra constante según su sector; da estabilidad |
| Especulador | Sigue la tendencia; amplifica subidas y caídas |
| Acaparador | Compra en bajas y retiene; reduce la oferta |
| Pánico | Vende cuando cae; acelera las caídas |

Esteban Arvel puede actuar como rival nominal que compite por contratos y compras grandes.

## Noticias: el motor de información

✅ Anuncian cosas como que el precio de un mineral va a subir en cierta fecha.

🟡 Separan **lo que pasa** de **lo que se publica**:

1. El sistema crea un **evento real** (huelga, descubrimiento, decreto) con fecha y magnitud.
2. Cada medio lo **reporta con su sesgo, retraso y ruido** (el Heraldo minimiza lo laboral, La Voz exagera, el Teletipo se adelanta pero a veces se equivoca; ver [07](07-sociedad-y-eventos.md)).
3. El jugador cruza fuentes y decide.

Cada noticia tiene nivel de confianza: **confirmada**, **rumor** o **falsa alarma**. Los tipos de evento tienen **firmas reconocibles** para que se pueda aprender.

Categorías: producción, política, laboral, tecnológico, clima, guerra/exterior, moda de lujo, descubrimiento.

## Información por capas

✅ Parte es gratis y parte se compra; con el tiempo el jugador ve más y de forma más visual.

| Capa | Qué muestra | Cómo se obtiene 🟡 |
|---|---|---|
| 1 · Básica (gratis) | Precio actual, flecha de tendencia | Desde el inicio |
| 2 · Prensa | Titulares y rumores | Periódico / suscripción (cada medio cuesta) |
| 3 · Análisis | Gráficos de 7/30 días, oferta vs. demanda | Analista / mejoras |
| 4 · Tabulador | Valor justo estimado **con margen de error**, sobre/infravalorado | Mejoras avanzadas; el error se achica con **Ojo** |

## Cómo se compra y se vende (y qué frena los abusos)

🟡 El mayor riesgo del mercado simulado es que el jugador encuentre un truco para hacerse rico sin esfuerzo. Frenos:

| Freno | Efecto |
|---|---|
| **Spread** | Comprar cuesta más de lo que se vende; evita arbitraje infinito |
| **Slippage** | Vender mucho de golpe baja el precio; hay que vender en tandas |
| **Costo de almacén** | Guardar cuesta, así que especular tiene riesgo real |
| **Impuestos y licencias** | Un porcentaje se va al Ministerio |
| **Límite de variación diaria** | El precio no se mueve más de X % por día (menos en Aetherita) |
| **Tope diario por comprador** | Cada comprador NPC absorbe solo cierto volumen |

## Canales de venta y compra

| Canal | Descripción |
|---|---|
| Mercado spot | Precio de mercado, con slippage y spread |
| Pedidos y contratos | ✅ Requisitos de clientes con precio, plazo y penalización |
| Trueque / canje | ✅ Intercambiar con comerciantes (relaciones y reputación) |
| Marketplace | ✅ Para comprar los materiales que faltan |
| **Mercado negro** | ✅ Paga más pero tiene riesgos (ver abajo) |

## Contratos y pedidos

✅ Cada contrato tiene: mineral, cantidad, plazo, precio (prima o descuento sobre el mercado) y penalización por fallar. (La **calidad** como requisito queda para después del MVP.)

| Tipo 🟡 | Descripción |
|---|---|
| Estándar | El pan de cada día |
| Urgente | Prima alta, plazo corto |
| A largo plazo | Precio fijo (versión sencilla de un futuro); puede salir bien o mal |
| Oficial del Ministerio | Cuotas obligatorias que chocan con el mercado |
| Negro | Pagan bien, con riesgo de inspecciones |

## Mercado negro y vigilancia

✅ El mercado negro **paga más pero tiene riesgos**. La idea es que no se use siempre, porque repercute. Hay un **indicador de vigilancia** de las autoridades; si el jugador se pasa de listo, se pagan **multas**.

### Qué ofrece 🟡

- Precios mejores que el spot (rango orientativo +20–40 %, variable por mineral).
- Ventas **sin impuesto** y sin licencia.
- Acceso a bienes restringidos o en cuota (por ejemplo Aetherita o grandes volúmenes de salitre).
- Se opera principalmente en el **bloque de noche**, con un contacto y volumen limitado por noche.
- Acceso mediante reputación con Los Faroleros o contactos.

### Indicador de vigilancia 🟡

Un medidor de 0 a 100 que **sube** con cada operación negra (según volumen y valor) y **baja** con el tiempo.

| Nivel | Rango | Consecuencias |
|---|---|---|
| Tranquilo | 0–30 | Nada |
| Observado | 30–60 | Inspecciones ocasionales, multas leves |
| Vigilado | 60–85 | Inspecciones frecuentes, multas fuertes, contratos oficiales bloqueados |
| Bajo investigación | 85+ | Redada: confiscación del stock negro, cierre temporal de la tienda, licencia en riesgo, posible arresto (pierde días) |

Cómo bajarlo: esperar, **sobornar al Inspector Quiroga** (a cambio de más corrupción y dependencia), tener buena reputación con el Ministerio, pagar a Los Faroleros (que alivian inspecciones pero suben tu deuda con ellos), contratar guardias.

Aplicación del pilar "la información es poder": al principio solo ves el nivel de forma vaga (bajo / medio / alto) y el valor exacto se descubre con fuentes (Quiroga, Lucía).

Las multas escalan con la dificultad.

## Refinado y valor agregado ✅ (entra en la primera versión)

Mena → lingote (+valor) → producto. Productos que alimentan a las industrias:

| Producto | Ingredientes |
|---|---|
| Acero | Hierro + carbón |
| Conductor | Cobre + plata |
| Oscilador | Cuarzo (clave del detector y las radios) |
| Joyería | Oro/plata + gemas |
| Pólvora | Salitre + carbón |
| Celda de éter | Aetherita + cuarzo |

🟡 Se hace en el **taller** de la tienda. Un lote tarda un tiempo y se recoge después; el empleado Refinador acelera. El minijuego de refinado es de dos parámetros: temperatura ↔ tiempo (ver [01](01-core-loop.md) y [02](02-extraccion.md)).

Da utilidad real a cada mineral y evita que todo sea "extraer y vender crudo".

## Tienda

✅ El jugador tiene una tienda que empieza modesta y mejora (espacio, stock, almacenamiento).

### Dinámicas de la tienda (días de comercio) 🟡

Inspiradas en cómo Dave the Diver sirve comidas. Los empleados pueden automatizarlas (ver [04](04-progresion-y-meta.md)).

| Dinámica | Mecánica |
|---|---|
| Reponer estantes | Arrastrar mercancía a los estantes y fijar precios |
| Atender clientes / regatear | Minijuego de dos parámetros: oferta del cliente vs. margen / paciencia del cliente |
| Tasar menas | Evaluar la calidad de lo que compras o recibes |
| Refinar / fundir | Minijuego de temperatura ↔ tiempo |
| Cumplir un pedido | Reunir y entregar a tiempo |

## Almacén

✅ Inventario de almacén con capacidad limitada, mejorable.

✅ Costos de almacenamiento y regulación de costos.

🟡 Alquiler/mantenimiento del almacén y quizás deterioro en algunos materiales → hacen que especular tenga un costo real.

## Utilidad de los minerales

- **Refinado:** mena → lingote → producto.
- **Mejora de herramientas y equipo** (ver [02](02-extraccion.md)).
- **Demanda de industrias NPC.**
- **Lujo / estatus** (ligado al estilo de vida).

## Sumideros de dinero 🟡

Mantenimiento de herramientas, alquiler del almacén, impuestos/licencias, salarios, multas, estilo de vida. Evitan que el dinero pierda sentido a largo plazo.

## Procedural

✅ Las partidas son distintas: se usan elementos procedurales.

🟡 **Reglas fijas, mundo variable.** Varían: qué zonas tienen qué, el perfil del mercado, el calendario de eventos, nombres de NPC. El jugador aprende las reglas, no memoriza un mapa.

## Fuera de la primera versión

- **Calidad de minerales** (común, buena, excelente): ✅ idea aceptada, para después del MVP. El resultado del minijuego daría una calidad que multiplica el precio y cumple requisitos de contratos.

## Nota técnica 🟡

El mercado debe construirse como un **módulo independiente que se pueda simular offline durante miles de días**, para balancearlo antes de depender de la interfaz.

## Pendiente

- ❓ Fórmulas concretas del modelo de precios (cuando pasemos a prototipo).
- ❓ Números base: precios, volatilidades, spreads, impuestos.
- ❓ Precios de las mejoras de información.
- ❓ Valor y frecuencia de multas del mercado negro.
- ❓ Receta detallada del refinado (tiempos, rendimiento, cantidades).
