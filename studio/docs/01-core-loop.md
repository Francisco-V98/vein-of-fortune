# 01 · Core loop y ciclo del día

## Idea central ✅

✅ Cada día se pueden hacer **expediciones** y **actividades de comercio/tienda**. El jugador tiene libertad de dedicar un día entero a una cosa, pero ambas son importantes y la idea es combinarlas.

✅ Al inicio el juego introduce el contexto de forma guiada (tutorial).

## Estructura del día ✅

**Estado:** los 3 bloques, lo que cuesta cada acción, las expediciones profundas y el viaje están confirmados (decisión del autor, 2026-10-15); el argumento de por qué la libertad no rompe el juego es propuesta.

### Qué cuesta cada cosa ✅

El día tiene **3 bloques**: mañana, tarde y noche ✅. El mercado se mueve una vez por bloque, o sea 3 veces por día ([03](03-comercio.md)) ✅.

Decisión del autor (2026-10-15):

| Acción | Cuesta |
|---|---|
| Viajar entre zonas | En **tren**: **no gasta bloque**, pero el **billete es el costo del viaje** (de 42 a 210 esquirlas por trayecto según el destino, [28](28-numeros-base-de-la-economia.md)) ✅ |
| Abrir el mapa y ver las zonas | **Gratis**, **desde cualquier lugar** ✅ |
| Viajar dentro de la misma zona (de una edificación a otra, desde el mapa) | **Gratis** y sin bloque ✅ |
| Caminar por el asentamiento o la mina, entrar a un edificio, loader | **No gasta bloque** ✅ |
| Minar (una expedición) | **1 bloque completo**; las zonas profundas, 2 bloques (ver abajo) ✅ |
| Abrir la tienda y comerciar | **1 bloque completo**, y **nunca de noche** ✅ |
| Misiones secundarias, trámites, eventos y visitas | **Gratis, medio bloque o 1 bloque completo**, según el peso real que tengan en el juego (cuánto tiempo lleva su lógica) ✅ |
| Mirar el mercado, leer noticias y organizar el inventario | **No consume bloques** ✅ |
| Varias expediciones al día | Sí, mientras queden bloques, como en Dave the Diver ✅ |

- ✅ **El viaje no gasta bloque pero el billete tiene un costo en dinero** (decisión del autor, 2026-10-15; el tren como único medio, 2026-10-24, F0-91). El tren es el único medio entre zonas y el billete es el costo del viaje; así el auto, que en V1 es solo estatus, gana sentido cuando en V2.1 llegue su pequeño efecto funcional con la concesionaria ([04](04-progresion-y-meta.md), [26](26-zonas-y-edificios.md)). Abrir el mapa no cuesta nada y puede hacerse desde cualquier lugar; dentro de la misma zona se viaja de una edificación a otra sin coste. El costo por trayecto es de 42 a 210 esquirlas según el destino, y en el Acto I no hay viaje porque todo ocurre en Villa Brasa ✅ ([28](28-numeros-base-de-la-economia.md)). El viaje se muestra en una pantalla de carga de unos 6 s, saltable desde el segundo viaje, y su construcción ⏳ F4-154. **Caminar** por el asentamiento y por la galería de la mina, **entrar** a un edificio y el **loader** no consumen bloques; el tiempo real de paseo (≈ +40 s por mina) se mide en el prototipo y se absorbe al recalibrar el ritmo por hora ⏳ F0-92 ✅.
- ✅ **Medio bloque** es la mitad de un bloque: dos medios bloques hacen uno. Sirve para lo que pesa poco (un trámite corto, una visita, una conversación que mueve la historia).
- ✅ **El modo tienda empieza en el momento en que decides abrirla**, en el bloque que quieras (mañana o tarde, nunca de noche). Desde ahí se comercia y se gestiona: cerrar ventas a clientes y contratos y jugar las dinámicas de la tienda ([03](03-comercio.md)).
- ✅ **De noche la tienda no se abre.** Sí caben las escenas, las visitas y el mercado negro, que no es el modo tienda (el bar de Salinas Blancas y la visita nocturna de Casilda, [03](03-comercio.md)).
- ✅ **Esperar:** un botón «Esperar» salta un bloque cuando el jugador no quiere hacer nada en él. Es una decisión real porque el mercado se mueve igual ([03](03-comercio.md)).
- ⏳ F2-02 Cómo se reparten los medios bloques dentro del día (si un medio que sobra se suma al siguiente o se pierde) y qué peso lleva cada misión, trámite, evento o visita.
- ⏳ F4-72 Cuánto cuesta en bloques operar el mercado negro por la noche.

### Zonas profundas ✅

Decisión del autor (2026-10-15): una expedición a una **zona profunda** (las **Cavernas de Cristal** y **La Fosa del Éter**) cuesta **2 bloques** y ocupa la **Tarde y la Noche**. Así la **Mañana queda libre para la tienda**, que no se abre de noche ([03](03-comercio.md)).

- ✅ **El juego lo recomienda antes de salir:** «Esta expedición ocupa Tarde y Noche; la tienda queda para la Mañana».
- ✅ **Las Cavernas están siempre abiertas.** Las demás zonas de minado cuestan 1 bloque.
- ✅ **La Fosa solo abre 3 días por semana**, los días de calibración de la Comisión ([24](24-umbrales-de-acto.md), [26](26-zonas-y-edificios.md)). Los días son el **2, el 4 y el 6 de cada semana** (la semana empieza el día 1 y el día 7 queda libre para la cuota) ✅ ([28](28-numeros-base-de-la-economia.md)). Esto no afecta al Acto I: la Fosa no se visita hasta el Acto IV ([17](17-mapa-de-historia.md)).
- ⏳ F2-02 Qué pasa si el jugador sale a una zona profunda con la Tarde ya gastada (si puede salir con un solo bloque libre o debe esperar al día siguiente).

### Por qué la libertad no rompe el juego 🟡

**Estado:** propuesta del diseñador; cada punto se apoya en una regla ya confirmada ([02](02-extraccion.md), [03](03-comercio.md)).

Para que ninguna mitad domine, la otra se vuelve necesaria:

- Solo minar: el almacén se llena, cuesta mantenerlo y no se vende → pérdidas.
- Solo comerciar: sin mercancía no hay qué vender. ✅ La tienda y los pedidos solo aceptan **mercancía propia** (extraída o refinada por ti): no se revende lo comprado. Comprar para revender solo se puede en el mercado spot, la Bolsa y el mercado negro, cada uno con sus frenos (decisión del autor, 2026-10-16; [03](03-comercio.md), [28](28-numeros-base-de-la-economia.md)).
- Los contratos tienen plazo; el mercado se mueve en cada bloque; las menas de las zonas se agotan y regeneran en ciclos.

## Ritmo de sesión y guardado ✅

**Estado:** el punto de control, las 5 partidas guardables y el azar fijado en el punto de control están confirmados (decisión del autor, 2026-10-15).

🟡 En PC (y en la Steam Deck) las sesiones pueden ser más largas que las de un móvil, así que ya no se diseña para sesiones de 5–10 minutos. Meta de diseño propuesta: **un día completo se puede jugar de seguido** y el jugador decide cuántos días juega en cada sesión; la duración objetivo de una sesión sigue abierta hasta el prototipo.

- ✅ **Punto de control al iniciar cada acción.** El juego se puede cerrar en cualquier momento: al volver se retoma desde el inicio de la última acción, y lo que estaba en curso (un minijuego a medias, por ejemplo) se vuelve a empezar.
- ✅ **Hasta 5 partidas guardables**, y el jugador **elige cuál jugar** al abrir el juego. El estado de partida ⏳ F2-01 y el guardado ⏳ F2-03 lo construyen así ([10](10-tecnico-y-herramientas.md), [14](14-arquitectura-y-modularidad.md)). En Steam se sincronizan con Auto-Cloud, y en Hardcore manda el guardado local.
- ✅ **El azar queda fijado al guardar el punto de control.** Cerrar y reabrir a mitad de una acción no repite la tirada, para que nadie esquive una derrota (sobre todo en Hardcore) recargando. El estado de partida lo guarda ⏳ F2-01.
- ✅ Se puede cerrar o suspender en cualquier momento sin perder progreso (autoguardado instantáneo): la Steam Deck suspende y no se quiere perder avance (decisión del autor, 2026-10-15).
- ✅ **Tiempo de juego:** un día completo dura **12–15 minutos** (≈ 13 nominales) y cada bloque **≈ 4–5 minutos**. La semana son 7 días y el **mes y la estación duran 28 días** cada uno (4 estaciones por año); de ahí sale la duración de cada acto ([17](17-mapa-de-historia.md), [28](28-numeros-base-de-la-economia.md)).
- ✅ **Calendario de arranque:** el día 1 es el 22 de otoño, así que el invierno empieza el día 8, el primer día del Acto II ([28](28-numeros-base-de-la-economia.md)).

## Ciclo macro

1. Leer contexto (noticias, mercado, pedidos).
2. Decidir plan del día (a qué zona ir, qué preparar, qué vender).
3. Equiparse según el peligro de la zona.
4. Expedición(es): entrar a la mina por la entrada del día, usar el detector (con batería), elegir menas, minar, afrontar peligros.
5. Volver: refinar, almacenar, vender, cumplir pedidos.
6. Invertir: herramientas, almacén, tienda, estilo de vida.
7. Fin de día: se pagan los costos, aparecen noticias y las zonas se regeneran. El mercado ya se movió en cada bloque.

## Ritmo del mundo

- ✅ **Noticias en el Acto I:** como máximo **1 noticia y 1 rumor por día** ([27](27-guion-del-acto-i.md)).
- ⏳ F4-89 Cuántas noticias y eventos por día desde el Acto II.
- ✅ Tutorial: los primeros siete días del Acto I están guionizados en [27](27-guion-del-acto-i.md), con una mecánica nueva por día como máximo y solo la cuota como fecha dura.
