---
id: "doc-01-estructura-del-dia"
tipo: "seccion"
title: "Estructura del día ✅"
aliases: ["doc-01-estructura-del-dia"]
documento: "[[01 Core loop y ciclo del día]]"
limpieza: 96
abiertos: 1
espera: 4
aplazado_a: ["[[F2-02 Ciclo de 3 bloques y avance del día]]", "[[F4-154 Viaje entre regiones - costo en dinero y zonas profundas]]", "[[F4-72 Mercado negro - operación nocturna con volumen limitado]]"]
estado: "con-abiertos"
anterior: "[[01 §Idea central]]"
siguiente: "[[01 §Ritmo de sesión y guardado]]"
arriba: "[[01 Core loop y ciclo del día]]"
fuente: "studio/docs/01-core-loop.md:9"
generado: true
---

# Estructura del día ✅

> Estado: los 3 bloques, lo que cuesta cada acción, las expediciones profundas y el viaje están confirmados (decisión del autor, 2026-10-15)…

← [[01 §Idea central]] · [[01 Core loop y ciclo del día|↑ 01]] · [[01 §Ritmo de sesión y guardado]] →

**Estado:** los 3 bloques, lo que cuesta cada acción, las expediciones profundas y el viaje están confirmados (decisión del autor, 2026-10-15); el argumento de por qué la libertad no rompe el juego es propuesta.

### Qué cuesta cada cosa ✅

El día tiene **3 bloques**: mañana, tarde y noche ✅. El mercado se mueve una vez por bloque, o sea 3 veces por día ([[03 Comercio y mercado|03]]) ✅.

Decisión del autor (2026-10-15):

| Acción | Cuesta |
|---|---|
| Viajar entre zonas | **No gasta bloque**, pero cuesta **un poco de dinero** (billete o combustible; de 42 a 210 esquirlas por trayecto según el destino, [[28 Números base de la economía\|28]]) ✅ |
| Ver las zonas en el mapa | **Gratis** ✅ |
| Minar (una expedición) | **1 bloque completo**; las zonas profundas, 2 bloques (ver abajo) ✅ |
| Abrir la tienda y comerciar | **1 bloque completo**, y **nunca de noche** ✅ |
| Misiones secundarias, trámites, eventos y visitas | **Gratis, medio bloque o 1 bloque completo**, según el peso real que tengan en el juego (cuánto tiempo lleva su lógica) ✅ |
| Mirar el mercado, leer noticias y organizar el inventario | **No consume bloques** ✅ |
| Varias expediciones al día | Sí, mientras queden bloques, como en Dave the Diver ✅ |

- ✅ **El viaje no gasta bloque pero tiene un pequeño costo en dinero** (decisión del autor, 2026-10-15): el billete o el combustible. Así el auto, que en V1 es solo estatus, gana sentido cuando en V2.1 llegue su pequeño efecto funcional con la concesionaria ([[04 Progresión y meta|04]], [[26 Zonas y edificios|26]]). Ver las zonas en el mapa no cuesta nada. El costo por trayecto es de 42 a 210 esquirlas según el destino, y en el Acto I no hay viaje porque todo ocurre en Villa Brasa ✅ ([[28 Números base de la economía|28]]); su construcción y los tiempos del trayecto ⏳ [[F4-154 Viaje entre regiones - costo en dinero y zonas profundas|F4-154]].
- ✅ **Medio bloque** es la mitad de un bloque: dos medios bloques hacen uno. Sirve para lo que pesa poco (un trámite corto, una visita, una conversación que mueve la historia).
- ✅ **El modo tienda empieza en el momento en que decides abrirla**, en el bloque que quieras (mañana o tarde, nunca de noche). Desde ahí se comercia y se gestiona: cerrar ventas a clientes y contratos y jugar las dinámicas de la tienda ([[03 Comercio y mercado|03]]).
- ✅ **De noche la tienda no se abre.** Sí caben las escenas, las visitas y el mercado negro, que no es el modo tienda (el bar de Salinas Blancas y la visita nocturna de Casilda, [[03 Comercio y mercado|03]]).
- ✅ **Esperar:** un botón «Esperar» salta un bloque cuando el jugador no quiere hacer nada en él. Es una decisión real porque el mercado se mueve igual ([[03 Comercio y mercado|03]]).
- ⏳ [[F2-02 Ciclo de 3 bloques y avance del día|F2-02]] Cómo se reparten los medios bloques dentro del día (si un medio que sobra se suma al siguiente o se pierde) y qué peso lleva cada misión, trámite, evento o visita.
- ⏳ [[F4-72 Mercado negro - operación nocturna con volumen limitado|F4-72]] Cuánto cuesta en bloques operar el mercado negro por la noche.

### Zonas profundas ✅

Decisión del autor (2026-10-15): una expedición a una **zona profunda** (las **Cavernas de Cristal** y **La Fosa del Éter**) cuesta **2 bloques** y ocupa la **Tarde y la Noche**. Así la **Mañana queda libre para la tienda**, que no se abre de noche ([[03 Comercio y mercado|03]]).

- ✅ **El juego lo recomienda antes de salir:** «Esta expedición ocupa Tarde y Noche; la tienda queda para la Mañana».
- ✅ **Las Cavernas están siempre abiertas.** Las demás zonas de minado cuestan 1 bloque.
- ✅ **La Fosa solo abre 3 días por semana**, los días de calibración de la Comisión ([[24 Umbrales de acto|24]], [[26 Zonas y edificios|26]]). Los días son el **2, el 4 y el 6 de cada semana** (la semana empieza el día 1 y el día 7 queda libre para la cuota) ✅ ([[28 Números base de la economía|28]]). Esto no afecta al Acto I: la Fosa no se visita hasta el Acto IV ([[17 Mapa de historia|17]]).
- ⏳ [[F2-02 Ciclo de 3 bloques y avance del día|F2-02]] Qué pasa si el jugador sale a una zona profunda con la Tarde ya gastada (si puede salir con un solo bloque libre o debe esperar al día siguiente).

### Por qué la libertad no rompe el juego 🟡

**Estado:** propuesta del diseñador; cada punto se apoya en una regla ya confirmada ([[02 Extracción|02]], [[03 Comercio y mercado|03]]).

Para que ninguna mitad domine, la otra se vuelve necesaria:

- Solo minar: el almacén se llena, cuesta mantenerlo y no se vende → pérdidas.
- Solo comerciar: sin mercancía no hay qué vender. ✅ La tienda y los pedidos solo aceptan **mercancía propia** (extraída o refinada por ti): no se revende lo comprado. Comprar para revender solo se puede en el mercado spot, la Bolsa y el mercado negro, cada uno con sus frenos (decisión del autor, 2026-10-16; [[03 Comercio y mercado|03]], [[28 Números base de la economía|28]]).
- Los contratos tienen plazo; el mercado se mueve en cada bloque; las menas de las zonas se agotan y regeneran en ciclos.

## Fuente

`studio/docs/01-core-loop.md:9`
