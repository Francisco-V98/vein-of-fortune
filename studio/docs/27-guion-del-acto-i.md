# 27 · Guion del Acto I, día a día

> ⚠️ **Contiene spoilers** (las pistas del sorteo oculto y lo que se siembra de Anselmo). Es material para quien escribe, programa o dibuja el Acto I; no es para el jugador.

Baja el Acto I a siete días: qué aprende el jugador cada día, qué pasa en sus tres bloques, qué dice cada quién (en una línea de ejemplo), qué hilos se siembran y qué pasa si no hace lo esperado. Parte de [08](08-historia-y-personaje.md), [17](17-mapa-de-historia.md), [19](19-elenco-a-fondo.md), [21](21-pasado-de-valdoria.md), [22](22-acto-ii-variantes.md), [23](23-arbol-de-decisiones.md) y [24](24-umbrales-de-acto.md), con la voz de [18](18-biblia-narrativa.md). Es un **guion de diseño**: no son los textos finales. Los textos de los siete días los escribe ⏳ F3-47 (incluidos los tres textos del Teletipo del día 5), salvo los de la prensa guionizada (las 3 noticias de los días 2, 3 y 6, su confirmación del día 7, la nota del Heraldo del día 4 y el titular del decreto del día 7: ⏳ F3-31) y los 2 pedidos de cliente guionizados (⏳ F3-32, incluida la tarjeta del pedido urgente opcional), que no cuentan en F3-47; ⏳ F3-16 construye las escenas, la cola, las ayudas y los props, y ⏳ F3-30 lo pasa al inglés. Las cifras (cuota, recargo, precios, efectivo) son las de [28](28-numeros-base-de-la-economia.md) ✅; la moneda es la esquirla y el día 1 es el 22 de otoño (el invierno empieza el día 8).

**Este es el guion de referencia del simulador** ✅ (decisión del autor, 2026-10-16, F0-86): `world.json` (`act1_script`) toma de aquí los días de expedición, los pedidos y la mejora del día 5. Que `store_days` sea `[2, 4, 7]` es la agenda del simulador, no una regla del juego: no impide vender en la tienda los días 3, 5 y 6. La sección 21 es el esquema de escenas y textos para quien construye y quien escribe.

**Cómo leer las marcas.** La palomita verde es lo que decidió el autor (2026-10-13, 2026-10-15 y 2026-10-16) o lo que ya está confirmado en otro documento; cada una lleva su fuente. El reloj de arena lleva siempre el ID de la tarea de la que depende, y esa tarea existe y no está terminada. Una sección lleva la palomita en el título solo si todo lo que tiene debajo está confirmado. Tras la pasada de cierre (F0-86) no queda ninguna propuesta del narrador pendiente del autor. Las líneas de ejemplo son siempre propuesta de estilo: no se marcan una a una y las cubre el título de su tabla; los textos finales son de F3-47.

## Resumen en cinco líneas

1. El Acto I son **siete días de tres bloques** (mañana, tarde y noche) ✅, y la tienda no se abre de noche ✅. Cada día enseña como máximo una mecánica nueva ✅, y los días 5 y 6 son de respiro: lo que traen es opcional ✅. La prensa es solo el Heraldo (noticia oficial) y el Teletipo (rumor) ✅.
2. **Solo la cuota es fecha dura**: vence el día 7 ✅. Lo demás se dispara por evento y, si no ocurre, espera en la cola ✅.
3. El puesto se reabre el **día 2** (trámite de Quiroga más la primera venta) ✅; el primer contacto con los empleados (**día 7, a primera hora**) y la cuota del **día 7** completan la puerta ✅. Entonces Quiroga sella «Minero con licencia» ✅.
4. Anselmo es solo **rastro** (firma, abono, libreta, lámpara y cinta 1) ✅. Nadie dice «mal del éter» ✅.
5. **Nada atasca**: sin dinero, Teo presta el pico ✅ y la deuda nunca bloquea ✅.

---

## 1 · Decisiones del autor ✅

Decisiones del 2026-10-13 (F0-23), del 2026-10-15 (F0-54) y del 2026-10-16 (F0-80 y F0-86), tras la ideación de tres estructuras, el aligeramiento de los días 5 y 6 (demasiada información muy rápida), la pasada de cierre y las que ya estaban tomadas en otros documentos.

| Tema | Decisión |
|---|---|
| Estructura | **Siete días ceñidos.** Solo la cuota es fecha dura; las demás escenas van por evento y, si no ocurren, pasan a la cola ✅ ([24](24-umbrales-de-acto.md), sección 10; motor ⏳ F3-48). **Una mecánica nueva por día como máximo** ✅ |
| Días 5 y 6 ligeros | La **mejora de la herramienta** (día 5) y el **pedido urgente con prima** (día 6) son **opcionales**: ayuda a pedido, sin tutorial forzado; el jugador puede saltarlos y el acto cierra igual. El día 5 es un **día de respiro** (ahorrar o mejorar, el rumor de Lucía y `n-i-lucia-rumor`). El día 6 queda **solo con noticia y rumor**: confirmar el rumor con la noticia oficial del Heraldo, sin pedido obligatorio y sin contacto con empleados ✅ |
| Prórroga de la cuota del día 7 | En **Novato e Intermedio** desplaza toda la serie una semana, con un recargo por cada semana de atraso (el 4 % de la cuota en Novato y el **6 % en Intermedio**, que son 38 y 58 esquirlas sobre la cuota del día 7), y **no pagar equivale a prórroga automática con recargo**. En **Difícil y Hardcore** la cuota atrasada se suma a la del día 14, sin desplazar la serie y con un **recargo mayor** (12 % y 18 %: 115 y 173 esquirlas) ✅ ([28](28-numeros-base-de-la-economia.md)) |
| Reabrir el puesto | Es el **trámite de Quiroga más la primera venta**, el día 2 ✅ |
| Premio del cierre | Quiroga sella **«Minero con licencia»** el día 7 ✅ |
| Nombre de la tienda | El jugador lo pone **al colgar el cartel**, el día 2 ✅ |
| Inicio | **Poco efectivo (120 esquirlas), el detector heredado de Anselmo y un pico prestado por Teo** ✅ |
| Riesgo | **Sin pérdida grave ni muerte permanente en los primeros días**, también en Hardcore, y eso incluye el día 3 ✅ (el límite por día está en la sección 2.3). **En Hardcore no hay derrota en ninguno de los siete días**: solo mata un encuentro de riesgo o un jefe y ninguno aparece en el Acto I ✅ ([02](02-extraccion.md), [04](04-progresion-y-meta.md); decisión del autor, 2026-10-16) |
| Peligros ambientales | **Fuera del Acto I**: ni gas ni derrumbes en los siete días. Entran desde el Acto II ✅ (⏳ F3-10) |
| Fuera del Acto I | **El taller, la herrería, los quioscos y los peligros ambientales.** La prensa llega por Lucía y por la tienda, y la mejora de la herramienta la hace Teo ✅ |
| Prensa | **Solo el Heraldo (noticia oficial sencilla) y el Teletipo (rumor).** La Voz del Hollín, la prensa con sesgos y el «cruzar fuentes» entran en el Acto II. El día 6 enseña a **confirmar un rumor con la noticia oficial del día siguiente** ✅ |
| Pedidos de cliente | En el Acto I los encargos de clientes son **«pedidos de cliente»**: estándar el día 4 y urgente con prima el día 6 (opcional). «Contrato» queda para el Acto II en adelante ✅ |
| Cuota | Semanal; la primera vence el día 7 y es de **960 esquirlas** (720 de capital y 240 de interés) ✅ |
| Puerta del Acto I | Reabrir el puesto, atender la primera cuota (pagada o prorrogada) y tener el primer contacto con los empleados ✅ (la misma puerta) |
| Primer contacto con los empleados | **Día 7, a primera hora**, como escena corta antes de la cuota: la ficha del candidato sin nombre y «Contratar» bloqueado con su motivo ✅ |
| «Contratar» bloqueado | El botón se abre al cerrar el Acto I y **también exige una mejora de la tienda**. En el Acto I está bloqueado y su motivo es esa **mejora de la tienda pendiente** ✅ (2026-10-15). El primer contacto sigue siendo la puerta del acto, no contratar ✅ |
| Bloques y tienda | Viajar en tren no gasta bloque pero cuesta dinero (el billete, entre 42 y 210 esquirlas por trayecto; en el Acto I todo ocurre en Villa Brasa y no hay trayecto ni costo), ver zonas es gratis y **caminar, los loaders y el tren no gastan bloque** (✅ 2026-10-24, [ADR-0011](adr/0011-exploracion-caminable-tren-y-minas.md)); minar y abrir la tienda cuestan un bloque completo; **la tienda no se abre de noche**, así que ninguna venta del Acto I cae en la noche. Las zonas profundas (2 bloques) y que La Fosa solo abra 3 días por semana (los días 2, 4 y 6) no afectan al Acto I: ninguna se visita en él ✅ (2026-10-15; [01](01-core-loop.md)) |
| Deuda | La deuda nunca bloquea ✅ |
| Anselmo | Solo sombras: libreta, lámpara, firma y cinta 1 ✅ |
| Firma | La firma de los papeles de la herencia es la misma del acta final ✅ |
| Reme | Solo sospecha que Anselmo vive y nunca llega a saberlo ✅ |
| El mal del éter | El Acto I no lo menciona ✅ |
| Herencia | «Por qué te dejaron heredar» no se escribe ni se siembra en el Acto I ✅ |
| Variables | El conjunto es cerrado: `{nombre}`, `{tienda}`, `{cuota}` y `{recargo}` ✅ (sección 21.7; decisión del autor, 2026-10-16). `{cuota}` es el importe vigente en esquirlas (960 el día 7, o 900 si pagaste antes) y `{recargo}` es el importe en esquirlas, no el porcentaje: 58 en Intermedio (38, 115 y 173 en Novato, Difícil y Hardcore) ✅ ([28](28-numeros-base-de-la-economia.md)) |
| Pagar antes | Desde el día 4 y **solo en casa de Reme** (`ed-vb-reme`, «gastar: cuotas de la deuda», [26](26-zonas-y-edificios.md)), en una interacción corta de 3 cajas que **no cuenta entre las 28 escenas**. Fija `f-pago-reme` = antes, la cuota de 900 y el interés −1 pp ([28](28-numeros-base-de-la-economia.md)). Si ya pagaste, `d7.2` pasa a una línea de agradecimiento. Solo es realista los días 6 y 7 ✅ (decisión del autor, 2026-10-16). No cambia `world.json` ni el simulador |
| La cuota del día 7 | `d7.2` se dispara sola al caer la tarde, porque la cuota es la única fecha dura. Si estás fuera, Reme pasa por el puesto y te ofrece la misma decisión (pagar o pedir tiempo). Solo si no respondes se aplica la prórroga automática con recargo, sin reproche ([18](18-biblia-narrativa.md), 2.3) ✅ (decisión del autor, 2026-10-16) |
| Taladro de Teo | Teo lo presta **solo** para la lección y la expedición del día 3 y lo recoge al final de `d3.4`. Los días 5 y 6 se saca hierro con el pico (el Picado sirve para hierro, [26](26-zonas-y-edificios.md)). Teo asume el desgaste y el taladro no entra en el inventario: el jugador llega al día 8 sin taladro ✅ (decisión del autor, 2026-10-16; el precio del taladro, 150 esquirlas, está en [28](28-numeros-base-de-la-economia.md), sección 5.2) |
| Prensa del día | **Como máximo 1 noticia y 1 rumor por día** ([01](01-core-loop.md), [03](03-comercio.md)). La nota del Heraldo con `{nombre}` y `{tienda}` sale el **día 4**, que no tiene noticia guionizada. El decreto de `d7.4` es una escena-gancho y no cuenta para el tope ✅ (decisión del autor, 2026-10-16) |
| Rumor de Lucía | Lucía **siempre** da primero su rumor del ferrocarril en `d5.2`, incluso si luego callas: `d6.1` funciona sea cual sea la decisión y callar solo baja `m-lucia` ✅ (decisión del autor, 2026-10-16) |
| Pistas del Ministerio | Un papel sellado doblado sobre la mesa de Reme en `d1.2`, `d1.3` y `d7.2`: no nombra a nadie y tiene lectura inocente ([22](22-acto-ii-variantes.md), sección 10) ✅ (decisión del autor, 2026-10-16) |
| Cinta 1 | Se encuentra de noche en `d2.4`, no en `d1.5`: así no hay dos sombras en una escena ([18](18-biblia-narrativa.md), 1.4). Se construye lo mínimo (bandera `cinta-1`, aviso «Encontraste una cinta» y objeto «Carrete 1» sin reproducción) ✅ (decisión del autor, 2026-10-16) |
| Qué es una sombra | Un elemento que deja una pregunta sobre Anselmo o la Comisión. No cuentan el saco de `d2.2` ni la caja del detector de `d1.2`. Máximo una por escena ✅ (decisión del autor, 2026-10-16) |
| Margen por defecto | El precio de lista de la tienda es el valor justo × 1,20 y el cliente medio paga × 1,15 ✅ ([28](28-numeros-base-de-la-economia.md), `world.json`) |
| Mejora del pico | Pasar el pico a nivel 2 cuesta **3 hierro y 480 esquirlas** ✅ ([28](28-numeros-base-de-la-economia.md), sección 5.2) |
| Legado | El legado no cambia los siete días: son iguales para todos, con o sin legado ✅ ([04](04-progresion-y-meta.md)) |
| Canon que no se toca | Anselmo está vivo pero se cree muerto y enfermo, y es cómplice de la Comisión del Éter. Reme traiciona en el Acto II por obligación y al final es la mayor aliada. Montenegro es el enemigo claro, duro e inflexible ✅ |

---

## 2 · Reglas del acto ✅

**Estado:** cerrada. Las reglas vienen de la sección 1 o de documentos ya confirmados; cómo se aplican día a día y los valores por dificultad los confirmó el autor en la pasada de cierre del 2026-10-16 (F0-86). Los valores finos por dificultad los fija ⏳ F3-22.

### 2.1 Bloques, escenas y cola

Todo lo de esta tabla viene de la sección 1 o de documentos ya confirmados.

| Regla |
|---|
| Cada día tiene tres bloques: mañana, tarde y noche. El mercado se mueve una vez por bloque ([03](03-comercio.md)) ✅ |
| Viajar en tren no gasta bloque pero cuesta dinero (entre 42 y 210 esquirlas fuera del Acto I; nada en el Acto I, donde todo ocurre en Villa Brasa), ver zonas es gratis y caminar por el pueblo o por la mina no gasta bloque ✅; minar y abrir la tienda cuestan un bloque completo; los trámites, las visitas y las conversaciones cuestan nada, medio bloque o un bloque según su peso ([01](01-core-loop.md)) ✅ |
| **Ninguna venta cae en la noche**: la tienda no se abre de noche ([01](01-core-loop.md)). Las escenas de noche son de casa, de cierre o de visita, y ninguna abre el modo tienda ✅ |
| Las escenas se disparan por evento; si no ocurren, pasan a la cola ✅ ([24](24-umbrales-de-acto.md), sección 10; motor ⏳ F3-48) |
| Solo la cuota tiene fecha: el día 7 llega aunque las escenas anteriores no se hayan jugado ✅ |
| Cada día enseña una mecánica nueva como máximo ✅ |
| Los días 5 y 6 son de respiro: la mejora de la herramienta y el pedido urgente son opcionales, con ayuda a pedido y sin tutorial forzado. Si el jugador los salta, el acto cierra igual ✅ |
| Los medios hablan del protagonista en tercera persona con `{nombre}` ([18](18-biblia-narrativa.md), 1.10) ✅ |
| **Tope de prensa:** como máximo 1 noticia y 1 rumor por día ([01](01-core-loop.md), [03](03-comercio.md)). El decreto del día 7 es una escena-gancho y no cuenta ✅ |
| **Reponer** (día 2): arrastrar la mercancía a los estantes y fijar los precios; es más gestión que minijuego ([03](03-comercio.md), [09](09-minijuegos.md)) ✅ |
| **El legado no cambia los siete días:** son iguales para todos, con o sin legado ([04](04-progresion-y-meta.md)) ✅ |
| **Hardcore no tiene derrota en los siete días:** solo mata un encuentro de riesgo o un jefe y ninguno aparece en el Acto I ([02](02-extraccion.md), [04](04-progresion-y-meta.md)) ✅ |
| **Margen por defecto de la tienda:** precio de lista = valor justo × 1,20; el cliente medio paga × 1,15 ([28](28-numeros-base-de-la-economia.md)) ✅ |
| **Este guion es la referencia del simulador** ✅ (`act1_script` de `world.json`). Que `store_days` sea `[2, 4, 7]` no impide vender los días 3, 5 y 6 ✅ |
| Reme tutea y dice «criatura»; Quiroga trata de usted; el narrador tutea ([18](18-biblia-narrativa.md), 1.2) ✅ |

**Cómo se aplican ✅.**

- Una expedición o abrir el puesto gasta un bloque completo; viajar en tren (que cuesta dinero, aunque no en el Acto I), caminar, los loaders, leer noticias, mirar el mercado y organizar el inventario no gastan ninguno ([01](01-core-loop.md)). Cada bloque tiene una actividad principal y las conversaciones cortas del barrio caben dentro del bloque en que ocurren. El peso de cada escena (0, medio o 1) lo asigna ⏳ F3-16 y el mecanismo lo define ⏳ F2-02; minar y abrir la tienda valen 1 (sección 21.2). Las escenas guionizadas no quitan bloques salvo la expedición y la tienda: por ejemplo, `d1.5` y `d1.6` no suman dos bloques.
- Cada día cabe en sus tres bloques con la regla de arriba: las ventas y los pedidos caen en la mañana o en la tarde, y la noche queda para las escenas.
- El día que se indica en cada escena es el **esperado**. Si el jugador va más rápido, la escena se adelanta solo hasta donde cumple sus requisitos; si va más lento, espera en la cola. La cola suelta las escenas de una en una y en orden, para que nunca se enseñen dos mecánicas nuevas a la vez; esa invariante ya está en las reglas de la cola ✅ ([24](24-umbrales-de-acto.md), sección 10); la construye ⏳ F3-48.
- Cada día tiene **como máximo una decisión principal**; si hay otra (la del nombre de la tienda el día 2 o `n-i-lucia-rumor` el día 5), es **menor** y cae dentro del mismo día. Los días 5 y 6 no obligan a ninguna principal: ahorrar o mejorar y vender ya o esperar al Heraldo son elecciones libres, sin nodo del árbol.
- **Ayuda a pedido.** Lo opcional (la mejora, el pedido urgente) no abre ventanas de tutorial: tiene un botón «?» y una frase de Teo que el jugador lee si quiere.
- Una escena lleva una sombra como máximo (regla de [18](18-biblia-narrativa.md), 1.4). Sombra es un elemento que deja una pregunta sobre Anselmo o la Comisión; las pistas del sorteo no son sombras (sección 13).
- El guion usa además un pedido de cliente estándar (día 4) y uno urgente con prima (día 6, **opcional**, sin escena), que son los contratos de [03](03-comercio.md) con otro nombre: en el Acto I se llaman «pedidos de cliente» ✅. El urgente es una variante del mismo pedido, no una mecánica nueva.

### 2.2 Qué se abre y qué queda fuera

| Dentro del Acto I | Fuera del Acto I |
|---|---|
| Villa Brasa y las **Galerías del Hollín**; **carbón** y **hierro** ✅ | Taller, Refinado y Acero (el taller abre en el II) ✅ |
| Escáner instantáneo, **Picado**, **Perforación** y **Regateo** ✅ | Herrería, quioscos y sede de la Unión (V1, [26](26-zonas-y-edificios.md)) ✅ |
| Tienda modesta (con Reponer: arrastrar la mercancía a los estantes y fijar precios) y herramientas de nivel 1 y 2; el taladro solo lo presta Teo el día 3 ✅ | Cañón Ferroso y las demás zonas ✅ |
| Información básica (precio y flecha), la noticia oficial del Heraldo (como máximo 1 noticia y 1 rumor del Teletipo por día) y la sección de empleos ✅ | Contratar de verdad (se abre al cerrar el Acto I y exige una mejora de la tienda), mercado negro y vigilancia (Acto II) ✅ |
| | Capas 3 y 4 de información y la Aetherita ✅ |
| | La Voz del Hollín, la prensa con sesgos y el «cruzar fuentes»: desde el Acto II ✅ |
| | Contratos (en el Acto I son «pedidos de cliente») ✅ |
| | Peligros ambientales (gas y derrumbes): desde el Acto II ✅ ⏳ F3-10 |

### 2.3 Dificultades

El selector es de cuatro niveles: Novato, Intermedio, Difícil y Hardcore ✅. Los siete días, las escenas y los textos son los mismos en las cuatro.

| Parámetro | Novato | Intermedio | Difícil | Hardcore |
|---|---|---|---|---|
| Efectivo, detector y pico del inicio | Los mismos ✅ | Los mismos ✅ | Los mismos ✅ | Los mismos ✅ |
| Pérdida grave y muerte hasta el día 2 | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ |
| Pérdida grave y muerte el día 3 | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ |
| Peligros ambientales en los siete días | Ninguno ✅ | Ninguno ✅ | Ninguno ✅ | Ninguno ✅ |
| Cuota atrasada del día 7 | Desplaza la serie, con recargo ✅ | Desplaza la serie, con recargo ✅ | Se suma a la del día 14, con recargo mayor ✅ | Se suma a la del día 14, con recargo mayor ✅ |

**Valores por dificultad ✅.** Desde el día 4 la pérdida es la normal de la dificultad: el castigo (desgaste, multas, pérdida de carga con tope del 75 %, costo de contratar, herida de empleados) se multiplica por 0,7 · 1 · 1,4 · 2 y el ruido de los precios por 0,8 · 1 · 1,25 · 1,5 en Novato, Intermedio, Difícil y Hardcore ([04](04-progresion-y-meta.md), `world.json`). **En Hardcore no hay derrota en los siete días**: solo mata un encuentro de riesgo o un jefe y ninguno aparece en el Acto I ([02](02-extraccion.md), [04](04-progresion-y-meta.md)). Las tres noticias guionizadas suben o bajan en el mismo sentido en las cuatro dificultades y solo cambia el tamaño. El efectivo inicial, la cuota, el capital, el interés y los precios base no cambian con la dificultad. Las cifras finas ⏳ F3-22.

---

## 3 · Los siete días de un vistazo ✅

**Estado:** cerrada. Confirmó el autor que son siete días, la cuota del día 7, el trámite y la primera venta del día 2, el nombre de la tienda, el sello del día 7, la prensa de solo Heraldo y Teletipo, los días 5 y 6 ligeros, el primer contacto con los empleados el día 7 a primera hora, que ninguna escena vende ni abre la tienda de noche (2026-10-15) y que el día 1 junta «escanear y picar» como una sola mecánica (2026-10-16). El 2026-10-16 (F0-86) confirmó también qué mecánica va en qué día, los bloques, qué ocupa la tarde del día 6 y las decisiones de cada día.

| Día | Se aprende (una mecánica) | Mañana | Tarde | Noche | Decisión del día |
|---|---|---|---|---|---|
| **1 · La llave** | La expedición: escanear y picar (una sola, guiada) | Reme: la llave, los papeles y el libro de deuda | Galerías con Teo: carbón | El puesto cerrado, la libreta y la carta a Vega Mansa | `n-i-herencia`: ¿cuentas lo de la herencia? |
| **2 · Abrir el puesto** | La tienda: surtir y fijar precios | Oficina de Quiroga: el trámite | El puesto: surtir, primera venta y cartel | Cierre de caja y cinta 1 | Principal: el margen. Menor: el nombre de la tienda |
| **3 · El hierro** | Perforación (el desgaste se ve al usarla, no es otra mecánica) | Galerías con Teo (taladro prestado): hierro y la placa de Pozo Negro | El puesto: debuta Lucía y sale la noticia del hierro | Fin de día | ¿Vender o guardar el hierro? |
| **4 · El cliente** | Regateo (el pedido estándar es su escenario) | El puesto: cliente y regateo; sale la nota del Heraldo | Galerías: reunir el pedido | Café con Reme: una pista y pagar antes | El mínimo del regateo |
| **5 · Un respiro** | Ninguna obligatoria (opcional: la mejora de la herramienta, con ayuda a pedido) | El puesto: entrega y rumor de Lucía | Libre; Teo ofrece el pico de nivel 2 (opcional) | La respuesta de casa | Menor: `n-i-lucia-rumor`. Libre: ahorrar o mejorar |
| **6 · El rumor** | Confirmar un rumor con la noticia oficial | El puesto: el rumor del Teletipo | Libre (el pedido urgente, si quieres, en el tablón) | Casa: mañana lo dice el Heraldo | Ninguna principal. Libre: vender ya o esperar al Heraldo |
| **7 · La cuota** | La cuota (el primer contacto con empleados no es mecánica: es una ficha bloqueada) | El puesto, primera hora: el Heraldo confirma, Teo señala los empleos; últimas ventas | Casa de Reme: la cuota (si no estás, Reme pasa por el puesto) | El puesto: Quiroga sella y suena el decreto | `n-i-reme-plazo`: antes (desde el día 4, en casa de Reme), justo o prórroga |

- **Una mecánica, un día.** ✅ Solo el día 1 junta dos acciones, «escanear y picar», y se cuenta como una sola mecánica (la expedición guiada; decisión del autor, 2026-10-16). El desgaste (día 3) forma parte de usar la herramienta, el pedido estándar (día 4) es el escenario del Regateo y el pedido urgente (día 6, opcional) es el mismo pedido con prima. La mejora (día 5) también es opcional: si se salta, no se pierde ninguna mecánica obligatoria. Los bloques, el trato con Reme y la lectura de la prensa no son mecánicas nuevas: son el marco.
- **Como máximo una decisión principal por día.** Los días 5 y 6 no obligan a ninguna. Los días 2 y 5 llevan además una decisión menor (el nombre de la tienda y el rumor de Lucía), que cae dentro del mismo día.
- **Escenas.** Son 28 en total: 6, 4, 4, 4, 4, 2 y 4 ✅. De ellas, solo `d5.3` es **opcional**; son **condicionales** (dependen de algo que puede no haber ocurrido) `d3.4` (sin hierro), `d4.3` (si dejas ir al cliente), `d5.1` (sin pedido) y `d5.4` (con «nada» en la herencia). Cada escena tiene un código `d<día>.<n>`, por ejemplo `d1.2`. La interacción corta de pagar antes (sección 21.6) no cuenta entre las 28.
- **Noticias y pedidos.** Hay 3 noticias guionizadas (días 2, 3 y 6; la del día 6 se confirma en la mañana del 7), la nota del Heraldo con el nombre y la tienda (día 4), el titular del decreto del día 7, los tres textos del Teletipo del día 5 (que escribe ⏳ F3-47) y 2 pedidos de cliente guionizados (el estándar del día 4 y el urgente opcional del día 6, que es una tarjeta sin escena). Los textos de prensa son de ⏳ F3-31 y los de los pedidos de ⏳ F3-32, no de F3-47. El resto sale al azar de las 10 noticias y los 12 pedidos de ⏳ F3-31 y ⏳ F3-32, siempre con el tope de 1 noticia y 1 rumor por día ✅. El decreto del día 7 es una escena-gancho y no cuenta para el tope.

---

## 4 · Día 1 · La llave ✅

**Estado:** cerrada. Reme es la vecina amable que da tiempo ([19](19-elenco-a-fondo.md)), Teo enseña el oficio en las Galerías, el jugador hereda la licencia, el puesto y la deuda, la firma está en los papeles, la libreta termina sin fecha y Reme atribuye el abono a «algún vecino bondadoso». El día, el bloque y el orden los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | La expedición guiada: tocar la mena para ver sus rangos y picar con Fuerza y Precisión |
| Decisión | `n-i-herencia`, de noche: ¿les cuentas todo, solo el puesto, o nada? |
| Lo cierra | La carta enviada |
| Si no haces lo esperado | La escena espera en la cola. Teo te espera en la boca de las Galerías hasta que vayas; la carta puede esperar y el día 2 sigue |
| Riesgo | Ninguno: sin pérdida grave |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d1.1` Llegada | Mañana | Llegas a pie a Villa Brasa (desde la estación a la calle, ya con control del personaje, ✅ 2026-10-24) con una maleta y 120 esquirlas, todo tu efectivo ✅ ([28](28-numeros-base-de-la-economia.md)). La interfaz muestra los tres bloques del día. No hay ninguna carta en la maleta: la única carta del día es la que escribes de noche (`d1.6`) | **Narrador:** «Villa Brasa huele a humo y a pan. Traes una maleta, 120 esquirlas y un día entero.» |
| `d1.2` La llave y los papeles | Mañana | Caminas hasta la casa de Reme (`ed-vb-reme`, una edificación del pueblo a la que se camina y se entra por la puerta ✅) y Reme te recibe dentro, en el interior lateral. Te da la llave, los papeles de la herencia con la **firma de Anselmo** y la caja con su detector. En la casa hay un decorado de la pista del sorteo, sin texto (sección 13): la lámpara de red, un papel sellado doblado sobre la mesa o un farol apagado | **Reme:** «Pasa, criatura. Esta es la llave. Y estos, los papeles de tu tío: ahí está su firma.» |
| `d1.3` El libro de deuda | Mañana | Reme abre el libro: capital, cuota cada 7 días y la primera el día 7. Una línea muestra el **abono** de cada mes. El decorado de la pista sigue a la vista (sección 13) | **Reme:** «Este abono llega cada mes. Algún vecino bondadoso, criatura. Yo no pregunto.» |
| `d1.4` Las Galerías | Tarde | Teo te acompaña caminando desde el pueblo hasta la boca de la mina (`ed-vb-mina-galerias`) ✅; allí te presta el pico, te enseña a escanear y a picar tres menas de carbón en la entrada de tu primer día. Dice que fue amigo de tu tío y lo deja ahí | **Teo:** «El carbón no perdona, pero avisa. Escanea primero, aprendiz.» Y, al irse: «Fui amigo de tu tío. Lo demás, otro día.» |
| `d1.5` El puesto cerrado | Noche | La llave abre el puesto, lleno de polvo; sigue cerrado al público. En el cajón de la caja está la **libreta**; su última anotación no tiene fecha. El primer apunte manda ir a Quiroga | **Narrador:** «La libreta tiene mil apuntes. El último, una sola línea sin fecha.» |
| `d1.6` La carta | Noche | En la casa obrera, la lámpara sobre la mesa. Escribes a Vega Mansa (`n-i-herencia`) | **{nombre}:** «Mamá, papá: heredé un puesto. Lo del banco agrario lo arreglo yo.» |

- **Hilos que se siembran** ✅ (coinciden con `hilos.json`): `h-firma-de-la-herencia` (`d1.2`), `h-abono-anonimo`, `h-trato-de-anselmo`, `h-prestamo-de-reme-a-anselmo` y `h-deuda-del-protagonista` (`d1.3`), `h-traicion-de-reme` (`d1.2` y `d1.3`), `h-anselmo-sigue-vivo` (`d1.4`), `h-libreta-sin-cierre` (`d1.5`), `h-lampara-y-cinta-1`, `h-vega-mansa-y-el-juramento` y `h-deuda-del-banco-agrario` (`d1.6`) y `h-sorteo-oculto-de-la-faccion-de-reme` (el sorteo ocurre antes de `d1.1`). `h-deuda-del-protagonista` se vuelve a sembrar en `d7.2`.
- **Noticia y rumor:** ninguno. El mercado muestra solo el precio y la flecha de tendencia ✅.
- **Pista del sorteo:** solo el decorado de la casa de Reme (la lámpara de red, el papel sellado doblado sobre la mesa o el farol apagado, según la variante) en `d1.2` y `d1.3`. Sin texto. La lámpara de red no se confunde con la lámpara de minero de `d1.6` ([18](18-biblia-narrativa.md), 5.1).
- **Cada escena, una sombra:** firma (`d1.2`), abono (`d1.3`), Teo y su amistad (`d1.4`), libreta (`d1.5`) y lámpara (`d1.6`).

---

## 5 · Día 2 · Abrir el puesto ✅

**Estado:** cerrada. Reabrir el puesto es el trámite de Quiroga más la primera venta, el jugador pone nombre a la tienda al colgar el cartel y la cinta 1 está en el doble fondo del cajón de la caja. El margen, el orden de los bloques y la primera noticia los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | La tienda: surtir los estantes y fijar los precios |
| Decisión | Principal: el **margen**, que por defecto es del 20 %: precio de lista = valor justo × 1,20, y el cliente medio paga × 1,15 ✅ ([28](28-numeros-base-de-la-economia.md), `world.json`). Menor: el **nombre de la tienda**, al colgar el cartel (la pantalla, ⏳ F3-14) |
| Lo cierra | La primera venta y el cierre de caja; el puesto queda reabierto |
| Si no haces lo esperado | Sin ir a Quiroga, el puesto sigue cerrado y la escena espera. Mientras tanto vendes al contado en el mercado, con peor precio |
| Sin dinero | Quiroga cobra su gestión (240 esquirlas) con la primera venta; si no alcanza, Reme la fía como «fiado de la gestión», sin interés y fuera de la deuda de la herencia (se paga junto con la siguiente cuota) ✅ |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d2.1` El trámite | Mañana | Quiroga pone el puesto a tu nombre. Lo llama «gestión» y la cobra con la primera venta | **Quiroga:** «Es un simple trámite, estimado (estimada). Tan simple que me da pena cobrarlo.» |
| `d2.2` Surtir los estantes | Tarde | Es la mecánica **Reponer**: arrastras la mercancía a los estantes (con mando, eliges estante y mercancía) y fijas el precio ✅ ([03](03-comercio.md), [09](09-minijuegos.md)). Colocas el carbón de ayer (o el saco que dejó Anselmo en la trastienda) | **Narrador:** «Queda un saco de carbón en la trastienda. Dos años de polvo y sigue negro.» |
| `d2.3` La primera venta | Tarde | Llega un cliente obrero. Vendes, eliges el margen y cuelgas el cartel con el nombre. El puesto queda **reabierto** | **Cliente:** «¿Es verdad que reabren el puesto? Aquí compraba mi padre.» |
| `d2.4` Cierre de caja | Noche | El puesto ya cerró y no se vende: solo cuadras la caja, en el interior lateral de la tienda. El cajón de la caja se atasca; debajo del doble fondo hay un carrete con el número 1 y aparece el aviso «Encontraste una cinta» | **Narrador:** «El cajón suena hueco. Debajo hay un carrete con un número: 1.» |

- **Noticia guionizada (la primera, de ⏳ F3-31):** el Heraldo dice que el abasto de carbón está garantizado, pero que el frío llega antes (el día 1 es el 22 de otoño y el invierno empieza el día 8 ✅). El Teletipo trae el primer **rumor** y el carbón sube un poco en los dos bloques siguientes, así que el rumor era cierto. Los dos pasan por el mostrador, repartidos por el voceador. Es la noticia y el rumor del día, dentro del tope ✅.
  - **Heraldo:** «El Ministerio informa de que el frío llegará antes, pero el carbón está garantizado este invierno.»
  - **Teletipo:** «FRÍO ADELANTADO EN EL HOLLÍN. CARBÓN SUBIRÍA. SIN CONFIRMAR»
- **Hilos que se siembran:** `h-lampara-y-cinta-1` (`d2.4`) ✅ ([23](23-arbol-de-decisiones.md), sección 7; `hilos.json`). Las demás escenas no siembran nada nuevo.
- **Sombras:** la cinta 1 (`d2.4`). El saco de Anselmo (`d2.2`) no cuenta como sombra ✅.

---

## 6 · Día 3 · El hierro ✅

**Estado:** cerrada. El hierro es mena secundaria de las Galerías ([05](05-mundo-y-minerales.md)), la Perforación es del Acto I, Lucía debuta en el Acto I, no hay pérdida grave en los primeros días, incluido el día 3 (decisión del autor, 2026-10-15), y no hay peligros ambientales. El taladro prestado, la placa de Pozo Negro ([21](21-pasado-de-valdoria.md); F0-80), la noticia y el orden los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | **Perforación** (velocidad contra calor), con el taladro que presta Teo. El desgaste se ve en la barra de la herramienta al usarla; no es una mecánica aparte |
| Decisión | ¿Vender el hierro o guardarlo en la trastienda? Guardar cuesta muy poco: 9 sacos de hierro un día cuestan 1 esquirla, así que la decisión es pequeña de verdad ✅ ([28](28-numeros-base-de-la-economia.md)) |
| Lo cierra | La decisión tomada |
| Si no haces lo esperado | Sin perforar, no hay hierro y la decisión no existe; Teo te lo vuelve a proponer cuando vuelvas, con el taladro de la lección. Lucía espera en la cola |
| Riesgo | Sobrecalentar daña la mena, pero no hay pérdida grave ✅. El calor es de la herramienta, no un peligro ambiental ✅: no hay gas ni derrumbes |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d3.1` Perforar | Mañana | Teo te presta un taladro **solo para esta lección y esta expedición** y te enseña: mucha velocidad calienta. El desgaste se ve en la barra de la herramienta y Teo lo asume. El taladro no entra en tu inventario: Teo lo recoge al final de `d3.4`. Los días 5 y 6 sacas hierro con el pico ✅ | **Teo:** «Dos dedos de presión y uno de calma, aprendiz. Si calienta, suelta.» |
| `d3.2` La placa | Mañana | En la boca de las Galerías, la placa de Pozo Negro, que es un prop fijo de la boca ([26](26-zonas-y-edificios.md)). Teo la mira | **Teo:** «Tu abuelo está en esa placa. Yo estaba en otro turno. Por eso hablo poco de ese día.» |
| `d3.3` Lucía | Tarde | Debuta en el puesto con el Teletipo y deja el rumor del día. Es la **única sombra de la Comisión** del acto | **Lucía:** «Lo oí en tres sitios: la Comisión del Éter pidió más hierro. ¿Cambia algo? No, tampoco a mí.» |
| `d3.4` ¿Vender o guardar? | Tarde | Sale la noticia del hierro. El mercado sube con el bloque. Decides | **Narrador:** «El hierro sube despacio. Guardarlo cuesta; venderlo ya, también.» |

- **Noticia guionizada (de ⏳ F3-31):** el Heraldo cuenta pedidos de rieles, con su «pero». El hierro sube despacio durante los días siguientes, en las cuatro dificultades.
  - **Heraldo:** «El Ministerio informa de nuevos pedidos de rieles, pero asegura que el hierro no faltará.»
- **Tope del día ✅:** una noticia (la del hierro) y un rumor (el de Lucía). La nota del Heraldo con el nombre y la tienda no sale hoy: pasa al **día 4** (sección 7).
- **Hilos que se siembran** ✅: `h-pozo-negro` (`d3.2`, [21](21-pasado-de-valdoria.md)), `h-comision-y-mal-del-eter` y `h-lealtad-de-lucia` (`d3.3`).
- **Sombras:** la Comisión (`d3.3`). No hay sombra de Anselmo.
- **Regla ✅:** hasta el día 3 incluido no hay pérdida grave (2026-10-15). Desde el día 4 la pérdida es la normal de la dificultad (sección 2.3).

---

## 7 · Día 4 · El cliente ✅

**Estado:** cerrada. El Regateo es del Acto I y en el Acto I los encargos son «pedidos de cliente» con mineral, cantidad, plazo, precio y penalización ([03](03-comercio.md)). El cliente, el pedido (8 de carbón, +12 %, 448 esquirlas menos el 3 % de impuesto, plazo de 3 días: [28](28-numeros-base-de-la-economia.md), sección 9.3), la oferta de cobrar antes y el orden los confirmó el autor el 2026-10-16 (F0-86). El cliente no tiene nombre todavía ⏳ F4-172.

| Campo | Contenido |
|---|---|
| Se aprende | **Regateo** (oferta contra paciencia del cliente). El **pedido de cliente estándar** es su escenario |
| Decisión | El **mínimo** del regateo: el precio por debajo del cual no vendes |
| Lo cierra | El café con Reme |
| Si no haces lo esperado | Si dejas ir al cliente, el pedido se pierde sin castigo y llegará otro. Si no vas a casa de Reme, la oferta de pagar antes sigue abierta hasta el día 7 (se paga solo allí, sección 21.6) |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d4.1` El pedido | Mañana | Un cliente obrero (sin nombre, ⏳ F4-172) pide 8 sacos de carbón con plazo de tres días, a 448 esquirlas (un 12 % sobre el valor justo; el impuesto de ventas es del 3 %). El pedido lleva `{tienda}` y sus cifras van en la tarjeta (texto de ⏳ F3-32), no en las cajas de la escena. Ese mismo día sale la nota del Heraldo con el nombre y la tienda (⏳ F3-31) | **Cliente:** «Necesito carbón para el horno. Pago lo justo, ni un centavo más.» |
| `d4.2` Regatear | Mañana | Fijas tu mínimo y juegas el Regateo | **{nombre}:** «Lo justo es lo que los dos podamos sostener.» |
| `d4.3` Reunir el pedido | Tarde | Una expedición normal; su escena, si la tiene (lugar y personajes), la fija ⏳ F3-16. Ejemplo: una frase del cliente, que cuenta un rumor útil | **Cliente:** «Entre nos: el herrero de la calle Honda compra todo el carbón que encuentra.» |
| `d4.4` El café | Noche | Reme te invita a su casa. Aquí está la **pista del sorteo** (sección 13) y la oferta de pagar antes: desde esta noche puedes adelantar la cuota en casa de Reme, en una interacción corta aparte (sección 21.6) | **Reme:** «Pasa, criatura, que el café se enfría. Si me adelantas la cuota, te rebajo un puntito.» |

- **Hilos que se siembran:** `h-pista-lampara-de-red`, `h-pista-deferencia-de-quiroga` o `h-pista-farol-vinotinto`, solo el de la variante sorteada (`d4.4`).
- **La nota del Heraldo (de ⏳ F3-31):** «El Ministerio informa de que `{nombre}` reabre «`{tienda}`» en Villa Brasa.» Es la noticia del día 4 ✅ (decisión del autor, 2026-10-16): pasa aquí desde el día 3 para respetar el tope de 1 noticia y 1 rumor por día.
- **Rumor:** el del cliente (`d4.3`) es el que puedes contar a Lucía el día 5. Si dejas ir al cliente, no lo oyes y el día 5 usa la alternativa de la sección 8.
- **Sombras:** ninguna.

---

## 8 · Día 5 · Un respiro ✅

**Estado:** cerrada. El día 5 es un día de respiro y la mejora de la herramienta es opcional, con ayuda a pedido y sin tutorial forzado (decisión del autor, 2026-10-13); la mejora la hace Teo y hay herramientas de nivel 2 en el Acto I. Qué herramienta se mejora, con qué, el rumor de Lucía (y el rumor de reserva si no oíste al cliente) y el orden los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | **Nada obligatorio.** Opcional: la **mejora** de una herramienta, que se paga con hierro y dinero (3 hierro y 480 esquirlas para el pico de nivel 2 ✅) y la hace Teo ([02](02-extraccion.md), [28](28-numeros-base-de-la-economia.md)). Sin tutorial: Teo la ofrece y la ayuda está en un «?» |
| Decisión | Menor, dentro del día: `n-i-lucia-rumor`. Libre, sin nodo: **ahorrar o mejorar** |
| Lo cierra | La respuesta de casa |
| Si no haces lo esperado | Si no mejoras, el pico sigue prestado hasta el día 7, cuando Teo te lo deja. Si no tienes hierro, la mejora espera sin plazo. Saltarse `d5.3` no cambia nada: el acto cierra igual ✅ |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d5.1` La entrega | Mañana | Entregas el pedido del día 4 y cobras | **Cliente:** «Buen carbón. Da gusto ver el puesto abierto otra vez.» |
| `d5.2` El rumor | Mañana | Lucía **siempre** te da primero su rumor del ferrocarril y luego te pide otro (`n-i-lucia-rumor`); lo da aunque después calles ✅ | **Lucía:** «Te doy uno por uno. El mío: el ferrocarril quiere hierro. ¿Y el tuyo? ¿Lo cuentas entero?» |
| `d5.3` El pico de nivel 2 (opcional) | Tarde | Si pasas por Teo con hierro, él se ofrece a forjar el pico y te lo devuelve ya tuyo. Sin ventana de tutorial | **Teo:** «Si me traes hierro, te devuelvo un pico que muerda. Sin prisa, aprendiz.» |
| `d5.4` La respuesta de casa | Noche | Llega la carta de Vega Mansa, según lo que contaste el día 1 | **Padre:** «Sabíamos que te irías. No que bajarías. Escríbenos cada semana.» |

- **Un día de respiro.** La tarde queda libre: puedes salir a las Galerías, vender, mirar el mercado o no hacer nada. No hay mecánica nueva que aprender.
- **Ayuda a pedido.** La mejora no abre ninguna ventana. Quien quiera saber cuánto cuesta y qué mejora pulsa el «?» de la oferta de Teo.
- **Si no tienes el rumor del cliente** (dejaste ir al cliente el día 4 o no oíste a quien lo contó), Lucía acepta como tuyo lo que viste en el mercado: «el hierro lleva dos días subiendo». Es el rumor de reserva. Las tres salidas (entero, mitad y nada) funcionan igual, con el Teletipo titulando «HIERRO SUBIRÍA DESPACIO EN EL HOLLÍN. SIN CONFIRMAR». Así `n-i-lucia-rumor` nunca se queda sin material ✅.
- **El rumor:** si lo cuentas entero, el Teletipo lo publica esa noche con su SIN CONFIRMAR («HERRERO DE LA CALLE HONDA ACAPARA CARBÓN. SIN CONFIRMAR») y el carbón se mueve 2 a 3 puntos; si cuentas la mitad, sale una nota vaga y se mueve 1; si callas, no sale nada (opciones de [23](23-arbol-de-decisiones.md), sección 3). Los tres textos del Teletipo de este día (entero, mitad y reserva) los escribe ⏳ F3-47 ✅ (decisión del autor, 2026-10-16).
- **Rumor de Lucía y tope de prensa.** El rumor del ferrocarril que te da Lucía es de boca, no sale en el Teletipo hasta el día 6, así que el día 5 sigue con 1 rumor impreso como máximo. Callar solo baja `m-lucia`: no quita el rumor del ferrocarril, de modo que `d6.1` funciona sea cual sea la decisión ✅.
- **La carta de casa:** con «todo», contesta el padre, dolido pero sin darte la espalda; con «parte», se alegran sin saber de la mina; con «nada», no llega carta y `d5.4` no se juega.
- **Hilos que se siembran** ✅: `h-lealtad-de-lucia` (`d5.2`) y `h-vega-mansa-y-el-juramento` (`d5.4`).
- **Sombras:** ninguna.
- **Hierro:** lo que guardaste el día 3 alimenta la mejora. Si lo vendiste, hay que sacar más, con el pico (el taladro de Teo fue solo del día 3).

---

## 9 · Día 6 · El rumor ✅

**Estado:** cerrada. En el Acto I la prensa es solo el Heraldo y el Teletipo; la prensa con sesgos y el cruzar fuentes entran en el Acto II ([07](07-sociedad-y-eventos.md)). El día 6 enseña a confirmar un rumor con la noticia oficial del día siguiente y queda solo con noticia y rumor, sin pedido urgente obligatorio y sin contacto con empleados (decisión del autor, 2026-10-13). La noticia concreta, la escena de la noche y qué ocupa la tarde los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | **Confirmar un rumor**: el Teletipo lo adelanta sin confirmar y el Heraldo lo confirma (o no) al día siguiente |
| Decisión | Ninguna principal. Libre, sin nodo: vender el hierro ya o esperar al Heraldo |
| Lo cierra | La escena de la noche: mañana habla el Heraldo |
| Si no haces lo esperado | Si no lees el rumor, el Heraldo del día 7 se explica solo. Si no aceptas el pedido urgente, no pasa nada: nunca fue obligatorio |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d6.1` Un rumor sin confirmar | Mañana | El Teletipo trae un rumor: el ferrocarril compraría hierro. Termina en SIN CONFIRMAR. El jugador sabe que mañana el Heraldo lo confirmará o no | **Narrador:** «Un rumor no es una noticia. Mañana el Heraldo dirá si es cierto.» |
| `d6.2` Mañana, el Heraldo | Noche | El hierro ya se mueve un poco en el mercado. Cierras el día con el rumor aún sin confirmar | **Narrador:** «El hierro se mueve. Si el rumor es cierto, mañana lo dirá el Heraldo.» |

- **Noticia guionizada (la tercera, de ⏳ F3-31):** el ferrocarril compra hierro; el precio sube de forma moderada. Sale en dos tiempos.
  - **Teletipo, día 6 (el rumor):** «FERROCARRIL COMPRARÍA HIERRO EN GRAN CANTIDAD. PRECIO SUBIRÍA. SIN CONFIRMAR»
  - **Heraldo, día 7 por la mañana (la confirmación):** «El Ministerio confirma pedidos del ferrocarril, pero el hierro no subirá mucho.» Son unos 80 caracteres: cabe en una caja de unos 100 ([18](18-biblia-narrativa.md), 1.9). La versión anterior (105 caracteres) se acortó por esa regla ✅.
- **Lo que enseña:** el rumor del Teletipo se adelanta; la noticia oficial del día siguiente lo confirma, aunque la baje de tono. Cruzar medios con distintos sesgos queda para el Acto II ✅.
- **Sea cual sea tu decisión del día 5**, Lucía te dio su rumor del ferrocarril, así que `d6.1` funciona igual ✅. Si hiciste el trato, el Teletipo ya publicó tu rumor (el del carbón) esa noche, y el jugador reconoce cómo se ve un rumor sin confirmar; si callaste, el Teletipo del día 6 es la primera vez que ves uno impreso. El rumor del ferrocarril queda sin confirmar hasta el Heraldo del día 7.
- **Tope del día ✅:** un rumor (el del ferrocarril) y ninguna noticia; la noticia oficial llega el día 7.
- **Pedido urgente (opcional, sin escena):** una tarjeta en el tablón de pedidos, con un cliente del Hollín sin nombre (⏳ F4-172) que pide 6 sacos de hierro con prima alta (un 35 %, 729 esquirlas) y plazo corto. No lleva tutorial ni diálogo; la ayuda está en un «?». Texto de ⏳ F3-32. Se entrega antes de la tarde del día 7; si no llegas o lo ignoras, no pasa nada (como mucho, una penalización de hasta el 5 % del valor, que nunca bloquea nada).
- **Tablón y calendario (F0-94) ✅:** el «tablón de pedidos» es una ficha de tipo pedido del calendario ([29](29-calendario-y-temporadas.md)); el Acto I no cambia de cifras ni de textos. Los días 1 a 7 no hay clima con efecto ni mini-historias (las de otoño no aparecen en la campaña), y la barra de fecha muestra «Día 1 · 22 de otoño». Las fichas y la barra son ⏳ F3-57 y ⏳ F3-58.
- **Tarde libre.** No hay escena: expedición, ventas, inventario o pedido urgente, a gusto del jugador.
- **Hilos que se siembran:** ninguno.
- **Sombras:** ninguna.
- **Empleados:** no hay contacto el día 6. La ficha del candidato llega el día 7 (sección 15).

---

## 10 · Día 7 · La cuota ✅

**Estado:** cerrada. La primera cuota vence hoy, el primer contacto con los empleados es hoy, a primera hora, como escena corta antes de la cuota, Quiroga sella «Minero con licencia» como premio y el Acto I se cierra con la puerta de la sección 1. El decreto que prepara el Acto II ([22](22-acto-ii-variantes.md), A1; [24](24-umbrales-de-acto.md)), el orden de los bloques y los ecos de las pistas los confirmó el autor el 2026-10-16 (F0-86).

| Campo | Contenido |
|---|---|
| Se aprende | **La cuota**: pagar a tiempo, antes o pedir tiempo (sección 11). El primer contacto con los empleados no es una mecánica: es una ficha que se mira y un botón bloqueado |
| Decisión | `n-i-reme-plazo`: antes (desde el día 4), justo o prórroga |
| Lo cierra | El sello de Quiroga y el decreto: **se cierra el Acto I** ✅ |
| Si no haces lo esperado | `d7.2` se dispara sola al caer la tarde. Si no estás en casa de Reme, ella pasa por el puesto y te ofrece la misma decisión (pagar o pedir tiempo). Solo si no respondes se aplica la prórroga automática con la regla de tu dificultad, sin reproche. La puerta se cumple igual: pagada o prorrogada ✅. Si no abres la sección de empleos, la ficha queda en el tablón del puesto y cuenta igual (sección 15) |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| `d7.1` Primera hora | Mañana | El Heraldo confirma el rumor de ayer. Teo pasa por el puesto (si no mejoraste el pico, te lo deja) y te señala la sección de empleos: la **ficha de un candidato sin nombre** (Minero nivel 1, 70 esquirlas al día, Lealtad «?») y «Contratar» bloqueado porque falta mejorar el puesto. Es el primer contacto con los empleados (sección 15). Luego revisas la caja y entregas el pedido urgente, si lo aceptaste. El libro marca «hoy» | **Teo:** «Mira la sección de empleos, aprendiz. Un puesto solo no se sostiene. Todavía.» **Narrador:** «Hoy vence la primera cuota. Hay caja, o no la hay; pero hay un camino.» |
| `d7.2` La cuota | Tarde | En casa de Reme (si estás fuera, Reme pasa por el puesto y te ofrece lo mismo). Pagas, o pides tiempo (sección 11); si ya pagaste antes, es una línea de agradecimiento. Eco de la pista del sorteo en la mesa y la ventana: la lámpara de red, el papel sellado doblado o el farol vinotinto encendido | **Reme:** «Con calma, criatura. Yo en tu lugar pagaría esta semana, pero una más no me quita el sueño.» |
| `d7.3` El sello | Noche | Quiroga llega al puesto ya cerrado, sin abrir la tienda, con el sello en la mano: «Minero con licencia» («Minera con licencia» para la protagonista, variante `.f`) | **Quiroga:** «Queda sellada su licencia, estimado (estimada). Ya lo pagó con el trámite: yo nunca cobro dos veces.» |
| `d7.4` El decreto | Noche | En la calle, un voceador. El Ministerio anuncia un decreto sobre las zonas del Hollín: es el gancho de A1 | **Voceador:** «¡Decreto del Ministerio de Recursos! ¡Se abren nuevas zonas en el Hollín!» |

- **Si prorrogas**, Reme lo dice sin reproche, con un consejo que suena a aviso:
  - **Reme:** «Una semana más, criatura. Lleva su recargo, que la casa también come.»
- **Cierre del acto:** **Narrador:** «Siete días. Ya no eres el recién llegado.»
- **Hilos que se siembran** ✅: `h-deuda-del-protagonista` y `h-traicion-de-reme` (`d7.2`). Ambos siguen en el Acto II.
- **Sombras:** ninguna. El decreto de `d7.4` es una escena-gancho, no cuenta para el tope de prensa y no nombra a Montenegro ✅ ([22](22-acto-ii-variantes.md), A1; [24](24-umbrales-de-acto.md)).
- **Qué sigue:** el decreto de A1 lo cuentan los tres medios en el Acto II, con la firma de Montenegro ([22](22-acto-ii-variantes.md)).

---

## 11 · La cuota del día 7 y sus dos reglas ✅

**Estado:** cerrada. Las dos reglas por dificultad (con el recargo mayor en Difícil y Hardcore), el periodo y la puerta venían confirmados. La visita de Reme al puesto, pagar antes solo en casa de Reme y la prórroga automática solo si no respondes los confirmó el autor el 2026-10-16 (F0-86).

La cuota vence cada 7 días y la primera, el día 7 ✅. Se puede pagar desde el día 4 (antes, solo en casa de Reme, sección 21.6), el día 7 (justo) o dejar pasar el día 7. La puerta del Acto I exige que la cuota esté **atendida**: pagada o prorrogada ✅. `d7.2` se dispara sola al caer la tarde del día 7, porque la cuota es la única fecha dura ✅.

| Qué haces | Novato e Intermedio | Difícil y Hardcore |
|---|---|---|
| Pagas antes (desde el día 4, en casa de Reme) | Pagada, con la cuota en 900 y el interés −1 pp. La siguiente vence el día 14 ✅ | Pagada, con la cuota en 900 y el interés −1 pp. La siguiente vence el día 14 ✅ |
| Pagas el día 7 | Pagada. La siguiente vence el día 14 ✅ | Pagada. La siguiente vence el día 14 ✅ |
| Pides prórroga, o no respondes | **Toda la serie se desplaza una semana**: la cuota vence el día 14, la siguiente el 21, y así. Lleva un recargo `{recargo}` por cada semana de atraso (58 esquirlas en Intermedio, el 6 % de la cuota de 960; 38 en Novato, el 4 %). No pagar equivale a prórroga automática con recargo ✅ | **La cuota atrasada se suma a la del día 14**, con un recargo mayor que en Novato e Intermedio: ese día debes dos cuotas más el recargo (960 + 960 + 115 = 2 035 en Difícil y 960 + 960 + 173 = 2 093 en Hardcore). La serie no se desplaza ✅ |
| Qué guarda `f-pago-reme` | `antes`, `plazo` o `tarde` según lo que hagas | `antes`, `plazo` o `tarde` según lo que hagas |

- **`{recargo}` es el importe en esquirlas** ✅, no el porcentaje: 38 en Novato, 58 en Intermedio, 115 en Difícil y 173 en Hardcore sobre la cuota del día 7. Los porcentajes (4, 6, 12 y 18 % de la cuota atrasada) salen de los datos en la interfaz, no del diálogo. El recargo de una misma cuota deja de crecer a las 3 semanas ✅ ([28](28-numeros-base-de-la-economia.md)).
- **Ninguna de las dos reglas cierra una puerta** ✅ ([24](24-umbrales-de-acto.md)): atender la cuota es pagar o dejarla anotada.
- **Pagar antes** baja el interés de la deuda de la herencia 1 pp, del 4 % al 3 % mensual (`n-i-reme-plazo`); con eso la cuota queda en 900 esquirlas ✅ ([28](28-numeros-base-de-la-economia.md), sección 7.2). Solo es realista los días 6 y 7. Si ya pagaste antes, `d7.2` es una línea de agradecimiento.
- **Reme no alza la voz ni reprocha** en ninguna de las tres salidas ✅ ([18](18-biblia-narrativa.md), 2.3).
- **Si no estás en casa de Reme el día 7**, ella pasa por el puesto al caer la tarde y te ofrece la misma decisión: pagar o pedir tiempo. Solo si no respondes se aplica la prórroga automática con recargo, con la regla de tu dificultad y sin reproche ✅.

---

## 12 · Las tres decisiones pequeñas ✅

**Estado:** cerrada. Son tres pequeñas, sus cupos no cambian ([23](23-arbol-de-decisiones.md)) y están decididas con sus opciones y sus banderas: la herencia (todo, a medias o nada, fija `f-familia`), el plazo de Reme (antes, a tiempo o prórroga, fija `f-pago-reme`) y el rumor de Lucía (entero, mitad o nada, mueve `m-lucia`) (decisión del autor, 2026-10-16). El día y la escena de cada una los confirmó el autor el mismo día (F0-86). Los botones están en la sección 21.8.

| Nodo | Día y escena | Qué cambia en el guion |
|---|---|---|
| `n-i-herencia` | Día 1, noche: `d1.6`, la carta | Fija `f-familia`. La respuesta de casa llega en `d5.4`, según lo contado; con «nada» no hay carta |
| `n-i-lucia-rumor` | Día 5, mañana: `d5.2`, en el puesto | Mueve `m-lucia`. Lucía siempre te da antes su rumor del ferrocarril. El rumor que cuentas es el del cliente del día 4 (el carbón) o, si no lo tienes, el del hierro que viste en el mercado (sección 8) |
| `n-i-reme-plazo` | Día 7, tarde: `d7.2`, en casa de Reme (o en el puesto, si Reme pasa por él); «antes» puede elegirse desde el día 4 en casa de Reme, en la interacción de la sección 21.6 | Fija `f-pago-reme`. La salida «prórroga» aplica la regla de tu dificultad (sección 11) |

- **Cuello `c-i-cierre`**: las tres terminan en el mismo cierre del acto.
- Los textos del disparador y del efecto de la prórroga de `decisions.json` se ajustaron a esta tabla.
- Las opciones y las banderas son las de `decisions.json` y [23](23-arbol-de-decisiones.md): esta sección no las cambia.

---

## 13 · Las tres pistas del sorteo oculto ✅

**Estado:** cerrada. La variante se sortea al empezar y es oculta, y el Acto I deja una pista distinta por variante ([22](22-acto-ii-variantes.md), sección 10). Las tres pistas caen el día 4 de noche, con ecos los días 1 y 7 (decisión del autor, 2026-10-16). Los tres props, que no nombren la facción y se vean sin buscarlos, la lectura inocente y el papel sellado del Ministerio en `d1.2`, `d1.3` y `d7.2` los confirmó el autor el 2026-10-16 (F0-86).

Solo se ve la pista de la variante sorteada. Los otros dos props no existen en esa partida. El sorteo se guarda en el estado de la partida ⏳ F2-01 y se puede forzar desde la consola ⏳ F1-23.

| Variante | La pista | Día y escena | Lectura inocente | Eco |
|---|---|---|---|---|
| Consorcio | La **lámpara de red**, la única de la calle, con una «A» grabada en la base | Día 4, noche: `d4.4` | «Un regalo de un cliente agradecido.» | La lámpara de red en el decorado de la casa de Reme en `d1.2`, `d1.3` y `d7.2` |
| Ministerio | **Quiroga** entra a casa de Reme, la saluda con deferencia y le devuelve un papel sellado sin cobrarle | Día 4, noche: `d4.4` | Dos vecinos que se respetan | Un **papel sellado doblado sobre la mesa de Reme** en `d1.2`, `d1.3` y `d7.2` (no nombra a nadie); en `d7.3` Quiroga pregunta con deferencia por doña Reme |
| Los Faroleros | Un **farol vinotinto** pequeño, con luz ámbar, en la ventana los días de pago. El día 4 ya hay pago posible (la cuota se puede adelantar), así que lo ves encendido | Día 4, noche: `d4.4` | «Una costumbre de mi madre.» | Apagado en `d1.2` y `d1.3` (aún no hay pago); encendido en `d7.2` |

**Líneas de ejemplo**

| Variante | Quién habla |
|---|---|
| Consorcio | **Reme:** «Un regalo de un cliente agradecido, criatura. Es la única que alumbra la calle.» |
| Ministerio | **Quiroga:** «Doña Reme, su trámite está en orden.» **Reme:** «Siempre tan atento, inspector.» |
| Los Faroleros | **Reme:** «Una costumbre de mi madre, criatura: cuando alguien viene a pagar, el farol encendido.» |

- **Reglas.** La pista nunca nombra la facción. El farol vinotinto no aparece en las otras dos variantes, porque sería una falsa pista. «Lámpara de red» no se confunde con la lámpara de minero ([18](18-biblia-narrativa.md), 5.1): la de red es eléctrica y está en la casa de Reme (`d1.2`); la de minero es la que está sobre la mesa de tu casa (`d1.6`). El papel sellado tiene una lectura inocente y tampoco nombra a nadie.
- **Storyboard.** ⏳ F0-24 dibuja `d4.4` en las tres variantes y `d1.2` y `d7.2` con el decorado de cada una.
- **Props:** ⏳ F3-16 (incluido el papel sellado del Ministerio). **Texto:** ⏳ F3-47.
- **Dónde se resuelve:** en la orden de Reme del Acto II ([22](22-acto-ii-variantes.md), A2) ✅.

---

## 14 · La cinta 1 ✅

**Estado:** cerrada. La cinta 1 se recoge en el Acto I, está en el doble fondo del cajón de la caja del puesto, no se puede oír hasta el IV y no hace falta para cerrar el acto. El disparador, el aviso y la construcción mínima los confirmó el autor el 2026-10-16 (F0-86).

- **Dónde:** el doble fondo del cajón de la caja del puesto (`ed-vb-tienda`), el cajón donde estaba la libreta; se ve y se recoge en el **interior lateral** de la tienda, ya dentro de la edificación ✅ ([26](26-zonas-y-edificios.md), [23](23-arbol-de-decisiones.md), sección 7).
- **Cuándo:** el día 2, de noche, al cerrar la caja por primera vez (`d2.4`). No es `d1.5`: habría dos sombras en una escena ([18](18-biblia-narrativa.md), 1.4) ✅.
- **Cómo se ve:** un carrete con un número 1 en la etiqueta, sin nombre ni fecha. El aviso es «Encontraste una cinta» ✅ ([18](18-biblia-narrativa.md), 1.6) y el objeto se llama «Carrete 1».
- **Qué se construye:** ⏳ F3-16 construye lo mínimo: la bandera `cinta-1`, el aviso y el objeto «Carrete 1» sin reproducción. El reproductor y el sistema de cintas son de ⏳ F4-150.
- **Qué no hace:** no se oye (hace falta el reproductor del IV ✅) y no lleva el texto de la grabación en el Acto I.
- **Si no cierras la caja,** la cinta espera. No se pierde ni caduca ✅. Si el acto cierra sin ella, queda como misión persistente hasta el IV ✅ ([24](24-umbrales-de-acto.md), sección 9).
- **Texto y voz** ⏳ F4-151. **Sistema de cintas** ⏳ F4-150.

---

## 15 · El primer contacto con los empleados ✅

**Estado:** cerrada. El Acto I termina con el primer contacto: se habla de empleados y aparece un candidato en el periódico, pero todavía no se puede contratar ([17](17-mapa-de-historia.md)). La contratación se implementa en el Acto II. El primer contacto pasa al día 7, a primera hora, como escena corta antes de la cuota (decisión del autor, 2026-10-13). El botón «Contratar» se abre al cerrar el Acto I y exige una mejora de la tienda, así que en el Acto I su motivo es esa mejora pendiente (decisión del autor, 2026-10-15). La ficha, el texto del aviso y el aviso de Teo los confirmó el autor el 2026-10-16 (F0-86); qué medio publica la sección de empleos queda en ⏳ F4-94.

- **Cuándo:** día 7, mañana, a primera hora (`d7.1`), antes de la cuota. Es una escena corta dentro de la primera hora del día, junto al Heraldo que confirma el rumor.
- **Qué se ve.** Teo señala la sección de empleos (en el Acto I no se nombra el medio que la publica, ⏳ F4-94). Hay una **tarjeta fija «Candidato sin nombre»** ✅ (los nombres procedurales, ⏳ F4-172): rol Minero de nivel 1, 70 esquirlas al día ([28](28-numeros-base-de-la-economia.md), sección 8.2) y Lealtad «?». Debajo, el botón **«Contratar»**, bloqueado con su motivo.
- **Motivo del bloqueo.** Es la **mejora de la tienda pendiente** ✅: el botón no se abre hasta que se cierre el Acto I y el puesto esté mejorado. Texto: «Para contratar, primero hay que mejorar el puesto.» El Acto I no dice cuál mejora ni cuándo. La ayuda «?» de la ficha **no muestra el costo** de la mejora (3 500 esquirlas, el «puesto ampliado», [28](28-numeros-base-de-la-economia.md)): ese dato es del Acto II. La contratación real es de ⏳ F4-90. El primer contacto es la puerta del acto; contratar no.
- **Dónde se compra la mejora.** ✅ La mejora de la tienda **se compra en la propia tienda, desde el Acto II, con dinero** (decisión del autor, 2026-10-15; cuesta 3 500 esquirlas, [28](28-numeros-base-de-la-economia.md)). **No se ofrece en el Acto I**: los siete días mantienen «una mecánica nueva por día» y en ellos el botón «Contratar» se ve bloqueado con ese motivo.
- **Si no abres la sección,** Teo lo cuenta y la ficha queda pegada en el tablón del puesto. Cuenta igual para la puerta ✅.
- **Si la primera hora se salta** (llegas al puesto más tarde), la escena se dispara en el primer bloque en que pases por el puesto, antes de la cuota de la tarde; la cola la suelta sin mezclarla con otra mecánica.
- **Qué se construye.** La ficha del Acto I es una tarjeta fija hecha en ⏳ F3-16, con el texto de ⏳ F3-47. La sección real del periódico es ⏳ F4-94, su sesgo ⏳ F4-96 y la información oculta ⏳ F4-97.

---

## 16 · Mercancías, minerales y herramientas del acto ✅

**Estado:** cerrada. Los minerales, la mercancía y las herramientas son los que cita [02](02-extraccion.md), [03](03-comercio.md) o [05](05-mundo-y-minerales.md). El taladro, la reparación, el pico de nivel 2 y la prensa los confirmó el autor el 2026-10-16 (F0-86).

| Cosa | En el Acto I |
|---|---|
| **Carbón** | Mena principal de las Galerías; se saca con Picado ✅ |
| **Hierro** | Mena secundaria de las Galerías; se saca con Picado o Perforación ✅ |
| **Mercancía del puesto** | Carbón y hierro en bruto, lo que sacas tú. Sin lingotes ni Acero ✅ |
| **Detector básico** | Heredado de Anselmo; no depende del cuarzo ✅ |
| **Pico** | Nivel 1, prestado por Teo ✅ |
| **Taladro** | Prestado por Teo solo el día 3; no entra en el inventario ✅ |
| **Mejora** | La hace Teo ✅; opcional, con ayuda a pedido ✅. Pico a nivel 2: 3 hierro y 480 esquirlas ✅ ([28](28-numeros-base-de-la-economia.md)) |
| **Trastienda** | El almacén modesto del puesto (40 unidades), con un costo de guardar mínimo de 1 esquirla por lote y día ✅ |
| **Prensa** | Heraldo (noticia oficial) y Teletipo (rumor), gratis en el Acto I, con el tope de 1 noticia y 1 rumor por día ✅ ([03](03-comercio.md)) |
| **Pedidos de cliente** | Estándar el día 4 y urgente con prima el día 6 (opcional) ✅ |

**Lo que fija el guion ✅.** El pico de nivel 2 puede llegar el día 5 (opcional) y ya es tuyo; la mejora cuesta 3 hierro y 480 esquirlas; Teo presta un taladro solo el día 3 y los días 5 y 6 se saca hierro con el pico; reparar cuesta dinero y materiales y no es un minijuego ([02](02-extraccion.md); los materiales son repuestos de hierro, 1 cada 20 puntos de desgaste); el Heraldo y el Teletipo llegan al mostrador y el Teletipo también por Lucía; sin el puesto abierto se vende al contado, con peor precio. La tienda y los pedidos solo aceptan mercancía propia ([28](28-numeros-base-de-la-economia.md)).

---

## 17 · Sombras del Acto I ✅

**Estado:** cerrada. Anselmo solo es rastro (libreta, lámpara, firma, cinta 1 y abono), no se dice «mal del éter» ni se siembra por qué te dejaron heredar. El día de cada sombra y la de la Comisión los confirmó el autor el 2026-10-16 (F0-86), con la tabla de `hilos.json` y el anexo de [18](18-biblia-narrativa.md).

**Qué es una sombra** ✅ (decisión del autor, 2026-10-16): un elemento que deja una pregunta sobre Anselmo o la Comisión. No cuentan el saco de carbón de `d2.2` ni la caja del detector de `d1.2`, ni las pistas del sorteo (sección 13).

| Escena | Sombra | Quién la deja | Hilo |
|---|---|---|---|
| `d1.2` | La firma de Anselmo en los papeles | Reme | `h-firma-de-la-herencia` |
| `d1.3` | El abono de «algún vecino bondadoso» | Reme | `h-abono-anonimo` |
| `d1.4` | «Fui amigo de tu tío; lo demás, otro día» | Teo | `h-anselmo-sigue-vivo` |
| `d1.5` | La libreta con su última anotación sin fecha | Libreta | `h-libreta-sin-cierre` |
| `d1.6` | La lámpara sobre la mesa | Protagonista | `h-lampara-y-cinta-1` |
| `d2.4` | La cinta 1 | Caja | `h-lampara-y-cinta-1` |
| `d3.3` | «La Comisión pidió más hierro» | Lucía | `h-comision-y-mal-del-eter` |

- **Seis de Anselmo y una de la Comisión.** Ninguna escena lleva más de una.
- **Lo que no aparece en el Acto I ✅:** el certificado de defunción, la letra de un muerto, el silencio firmado de Teo, la tos de Teo con nombre y todo lo que diga que la Comisión oculta algo.

---

## 18 · El nombre de la tienda ✅

**Estado:** cerrada. Cuándo se pone, que admite espacios y dónde sale venían confirmados. El nombre por defecto lo decidió el autor el 2026-10-16 (F0-86).

- **Cuándo.** El día 2, en `d2.3`, al colgar el cartel ✅. El nombre del personaje se elige antes ([08](08-historia-y-personaje.md)).
- **Reglas.** Permite espacios ✅. El largo máximo ⏳ F1-18: con el nombre por defecto y un nombre de 12 letras el texto ocupa 22 caracteres, así que el máximo es de 22 o más. La pantalla se construye en ⏳ F3-14.
- **Dónde sale.** En el cartel, en el pedido del día 4 y en la nota del Heraldo del día 4 ✅; después, en periódicos, contratos (desde el Acto II) y carteles ✅ (`{tienda}`).
- **Si lo dejas vacío,** el cartel dice «Puesto de `{nombre}`» ✅ (decisión del autor, 2026-10-16). El nombre se guarda vacío y se resuelve al mostrarlo, así que cambia con el idioma.

---

## 19 · Coste de producción ✅

**Estado:** cerrada. La cuenta es una estimación del narrador que el autor aprobó el 2026-10-13 y que la pasada de cierre del 2026-10-16 (F0-86) deja con la interacción de pagar antes. Los textos de las 3 noticias guionizadas, la nota del Heraldo del día 4, el titular del decreto y los 2 pedidos guionizados **no** entran en esta cuenta: son de ⏳ F3-31 y ⏳ F3-32 (una sola autoría). Los tres textos del Teletipo del día 5 los escribe ⏳ F3-47 y tampoco están en la cuenta de las escenas: son 3 titulares más, dentro del margen de ≈ 323 ± 3. Una caja de diálogo es de unas 15 palabras (100 caracteres). El ritmo de escritura es de unos 35 textos por hora, como en [22](22-acto-ii-variantes.md), sección 12. El detalle por escena está en la sección 21.2.

| Día | Escenas | Cajas de diálogo | Ayudas e interfaz | Cartas y avisos | Total |
|---|---|---|---|---|---|
| 1 | 6 | 53 | 12 | 6 | 71 |
| 2 | 4 | 30 | 10 | 1 | 41 |
| 3 | 4 | 37 | 8 | 1 | 46 |
| 4 | 4 | 38 | 6 | 3 | 47 |
| 5 | 4 | 36 | 3 | 3 | 42 |
| 6 | 2 | 14 | 3 | 1 | 18 |
| 7 | 4 | 44 | 7 | 3 | 54 |
| **Total** | **28** | **252** | **49** | **18** | **319 textos (≈ 4.150 palabras)** |

A los 319 textos de las 28 escenas se suman las 3 cajas de la interacción de pagar antes (sección 21.6), que no es una escena: **322 textos**, que se estiman en ≈ 323 ± 3. Tras aligerar los días 5 y 6 (2026-10-13), el total bajó de ≈ 340 a ≈ 320 textos y de 29 a 28 escenas. El día 5 acorta `d5.3` (opcional) y su ayuda; el día 6 queda con dos escenas (el pedido urgente pasa a ser una tarjeta cuyo texto es de ⏳ F3-32); el día 7 suma la ficha del candidato, el aviso de Teo y la ayuda del botón bloqueado.

- **Fuera de la cuenta de F3-47:** las 3 noticias guionizadas (6 titulares y notas), la nota del Heraldo del día 4, el titular del decreto y los 2 pedidos guionizados (≈ 8 textos, con la tarjeta del pedido urgente) más las 7 noticias aleatorias y los 10 pedidos aleatorios (≈ 60) son de ⏳ F3-31 y ⏳ F3-32: ≈ 70 textos y los 2 de la nota y el decreto, unos 72. Con los 325 de F3-47 (322 más los 3 del Teletipo), unos 397 para traducir.
- **Reparto de horas ✅ (ya en el roadmap).**
  - ⏳ F3-47 **Textos del Acto I** (14 h): los 322 textos de los siete días (sin noticias ni pedidos) y de la interacción de pagar antes, más los 3 del Teletipo del día 5, que son ≈ 9 h de escritura, más la revisión de voz. Las 14 h se mantienen.
  - ⏳ F3-16 **Escenas, cola, ayudas y props** (14 h, ya sin los textos): las 28 escenas con disparadores, cola y ayudas (con lo opcional del día 5 y del día 6 sin tutorial forzado), la interacción de pagar antes, la visita de Reme al puesto el día 7, el taladro del día 3, la placa de Pozo Negro, la cinta 1 con su aviso, la ficha del candidato en el día 7 y los props de las pistas (incluido el papel sellado del Ministerio). Las 14 h se mantienen.
  - ⏳ F3-17 **Deuda** (6 h): las dos reglas por dificultad, con el recargo mayor, y la prórroga automática.
  - ⏳ F3-30 **Traducción** (13 h): unos 397 textos al ritmo de 35 por hora son ≈ 11 h, con margen de revisión.
- **Sin cambio de horas:** ⏳ F3-14 (6 h, con el nombre de la tienda en el día 2), ⏳ F3-31 (8 h, con los textos de las 3 noticias guionizadas) y ⏳ F3-32 (4 h, con los de los 2 pedidos guionizados, uno de ellos la tarjeta opcional del día 6).
- **Fuera del Acto I:** los peligros ambientales (⏳ F3-10, 10 h) no suman horas aquí.
- **Quién construye cada día.** Día 1: F2-10, F2-11 y F2-14; día 2: F2-17 y F2-18; día 3: F2-15, F2-12 y F3-08; día 4: F2-19 y F3-05; día 5: F3-12 (opcional); día 6: F3-01, F3-02, F3-03 y, si se acepta el pedido urgente, F3-05; día 7: F3-17 y la ficha de F3-16.
- **Storyboard ✅.** Las escenas clave para ⏳ F0-24 son `d1.2`, `d1.6`, `d2.4`, `d3.2`, `d4.4`, `d7.2` y `d7.4`. Cada una tiene lugar, personajes, props, pantalla del juego, línea de ejemplo y variantes en las secciones 4 a 10 y 21. `d4.4` se dibuja en las tres variantes del Acto II; `d1.2` y `d7.2` con el decorado de cada variante y las ramas por dificultad de `d7.2`.

---

## 20 · Términos nuevos del glosario ✅

**Estado:** cerrada. Los términos en español ya son canon en [18](18-biblia-narrativa.md), [22](22-acto-ii-variantes.md), [23](23-arbol-de-decisiones.md), [24](24-umbrales-de-acto.md) y [28](28-numeros-base-de-la-economia.md), y la «ficha de candidato» viene de [04](04-progresion-y-meta.md). El inglés de estos términos queda en ⏳ F1-20, que los traduce en lote con el glosario de [18](18-biblia-narrativa.md), capítulo 6.

| Término | Qué es |
|---|---|
| `{nombre}` · `{tienda}` · `{cuota}` · `{recargo}` | Las cuatro variables de los textos. `{cuota}` y `{recargo}` son importes en esquirlas (sección 21.7) |
| recargo | Lo que se suma a la cuota por cada semana de atraso; es mayor en Difícil y Hardcore. No se llama «interés» ni «multa» |
| prórroga | Dejar la cuota para la semana siguiente. En Novato e Intermedio desplaza la serie; en Difícil y Hardcore se suma a la del día 14 con recargo mayor |
| cuota atrasada | La cuota del día 7 que no se pagó en Difícil y Hardcore |
| libro de deuda | El libro de Reme donde se ven el capital, la cuota y el abono |
| lámpara de red | La lámpara eléctrica de la pista del Consorcio. No es la lámpara de minero |
| pedido de cliente | El encargo de un cliente en el Acto I (estándar el día 4, urgente y opcional el día 6). «Contrato» queda para el Acto II en adelante ✅ |
| pedido urgente · prima | El pedido de cliente urgente (opcional, sin escena) y lo que paga de más |
| ficha de candidato | La tarjeta del candidato de la sección de empleos, que se ve el día 7 a primera hora |
| mejora de la tienda | La mejora del puesto que hace falta para poder contratar; se compra en la propia tienda desde el Acto II (el «puesto ampliado», 3 500 esquirlas). No es la mejora de una herramienta, que hace Teo. En el Acto I es el motivo del bloqueo de «Contratar» |
| cola de historia | Donde esperan las escenas que no se pueden disparar ([24](24-umbrales-de-acto.md), sección 10) |
| sombra | Un elemento que deja una pregunta sobre Anselmo o la Comisión sin revelar nada ([18](18-biblia-narrativa.md), 1.4) |
| pagar antes | Adelantar la cuota desde el día 4, solo en casa de Reme: la cuota queda en 900 y el interés baja 1 pp |
| papel sellado | El papel doblado sobre la mesa de Reme que es la pista del Ministerio; no nombra a nadie |
| escena-gancho | Una escena que prepara el acto siguiente y no cuenta para el tope de prensa (el decreto del día 7) |

---

## 21 · Esquema de escenas y textos ✅

**Estado:** cerrada. Esta sección la aprobó el autor el 2026-10-16 (F0-86) y es el esquema para quien construye (⏳ F3-16), quien escribe (⏳ F3-47, ⏳ F3-31 y ⏳ F3-32), quien dibuja (⏳ F0-24) y quien programa el simulador. No renumera las secciones 1 a 20, que citan `hilos.json` y los documentos 04, 21, 22, 23 y 24. Los textos finales de cada pieza son de su responsable; las frases entre comillas de las secciones 4 a 10 son ejemplos de voz.

### 21.1 Identificadores y convenciones

| Cosa | Convención |
|---|---|
| Escena | `dN.M`: día esperado (`N`) y orden dentro del día (`M`). Son 28 y no se renumeran |
| Caja de diálogo | `dN.M.cNN` (con retrato; unos 100 caracteres, 34 por línea, 3 líneas, una idea por caja: [18](18-biblia-narrativa.md), 1.9) |
| Ayuda o interfaz | `dN.M.uNN` (ayudas «?», etiquetas, mensajes de pantalla) |
| Carta o aviso | `dN.M.kNN` (cartas, papeles, libreta, placa, sello y avisos del juego) |
| Botón de decisión | `n-….bK`, por ejemplo `n-i-herencia.b1` |
| Variante de rama | Sufijo sobre el texto: `.todo`, `.parte`, `.nada` (herencia y rumor de Lucía) y `.antes`, `.plazo`, `.tarde` (cuota) ✅ (decisión del autor, 2026-10-16) |
| Sufijos adicionales | `.consorcio`, `.ministerio`, `.faroleros` (variante sorteada, `e-variante-reme`), `.serie` y `.suma` (la regla de prórroga por dificultad) y `.reserva` (rumor de reserva de Lucía). Convención propuesta; F3-16 y F3-47 pueden renombrar. Ejemplo: `d7.2.c05.plazo` (identificador también propuesto) |
| Variante de género | Sufijo `.f`, **solo** donde [18](18-biblia-narrativa.md), 1.2 lo exige: «estimado/a» de Quiroga (`d2.1` y `d7.3`) y «Minera con licencia» (`d7.3`). Ejemplo: `d7.3.c03.f` |
| Peso y bloque | Cada escena tiene un bloque (mañana, tarde o noche) y un peso: 0, medio bloque o 1. Minar y abrir la tienda valen 1 ([01](01-core-loop.md)); el resto de pesos los asigna ⏳ F3-16 y el mecanismo lo define ⏳ F2-02 |
| Lugar | Un `id` de edificación de [26](26-zonas-y-edificios.md) (`ed-vb-*`) o «calle» |
| Personajes | Los `id` de `world.json` (`protagonista`, `reme`, `teo`, `quiroga`, `lucia`, `voceador`, `cliente-obrero`). La familia de Vega Mansa solo escribe cartas: no es personaje en escena |
| Totales | Las cifras por escena incluyen todas sus variantes de rama, de género y de sorteo |

### 21.2 Tabla maestra de las 28 escenas

Nota del 2026-10-24 (F0-91) ✅: cada lugar de la columna «Lugar» (`ed-vb-*`) es una edificación del pueblo a la que se camina por el exterior aéreo y se entra por su puerta, con un loader corto hacia el interior lateral; `calle` es el exterior. La escena se dispara al entrar al edificio o al hablar con el PNJ, con un marcador discreto en el diario. Los textos, los pesos y los totales no cambian.

El peso es 1 donde la escena es una expedición o abre la tienda ([01](01-core-loop.md)); en el resto lo asigna F3-16 (⏳ F3-16, mecanismo ⏳ F2-02). Las columnas de textos cuentan cajas (C), ayudas e interfaz (U) y cartas y avisos (K).

| Escena | Título | Bloque | Peso | Lugar | Personajes | C | U | K | Total |
|---|---|---|---|---|---|---|---|---|---|
| `d1.1` | Llegada | Mañana | F3-16 | `calle` | `protagonista` | 6 | 4 | 0 | 10 |
| `d1.2` | La llave y los papeles | Mañana | F3-16 | `ed-vb-reme` | `reme`, `protagonista` | 10 | 0 | 1 | 11 |
| `d1.3` | El libro de deuda | Mañana | F3-16 | `ed-vb-reme` | `reme`, `protagonista` | 10 | 2 | 1 | 13 |
| `d1.4` | Las Galerías | Tarde | 1 | `ed-vb-mina-galerias` | `teo`, `protagonista` | 14 | 5 | 0 | 19 |
| `d1.5` | El puesto cerrado | Noche | F3-16 | `ed-vb-tienda` | `protagonista` | 6 | 1 | 2 | 9 |
| `d1.6` | La carta | Noche | F3-16 | `ed-vb-casa` | `protagonista` | 7 | 0 | 2 | 9 |
| `d2.1` | El trámite | Mañana | F3-16 | `ed-vb-quiroga` | `quiroga`, `protagonista` | 10 | 2 | 0 | 12 |
| `d2.2` | Surtir los estantes | Tarde | F3-16 | `ed-vb-tienda` | `protagonista` | 5 | 3 | 0 | 8 |
| `d2.3` | La primera venta | Tarde | 1 | `ed-vb-tienda` | `cliente-obrero`, `protagonista` | 10 | 4 | 0 | 14 |
| `d2.4` | Cierre de caja | Noche | F3-16 | `ed-vb-tienda` | `protagonista` | 5 | 1 | 1 | 7 |
| `d3.1` | Perforar | Mañana | 1 | `ed-vb-mina-galerias` | `teo`, `protagonista` | 12 | 6 | 0 | 18 |
| `d3.2` | La placa | Mañana | F3-16 | `ed-vb-mina-galerias` | `teo`, `protagonista` | 7 | 0 | 1 | 8 |
| `d3.3` | Lucía | Tarde | F3-16 | `ed-vb-tienda` | `lucia`, `protagonista` | 10 | 0 | 0 | 10 |
| `d3.4` | ¿Vender o guardar? | Tarde | F3-16 | `ed-vb-tienda` | `teo`, `protagonista` | 8 | 2 | 0 | 10 |
| `d4.1` | El pedido | Mañana | F3-16 | `ed-vb-tienda` | `cliente-obrero`, `protagonista` | 10 | 1 | 1 | 12 |
| `d4.2` | Regatear | Mañana | F3-16 | `ed-vb-tienda` | `cliente-obrero`, `protagonista` | 8 | 4 | 0 | 12 |
| `d4.3` | Reunir el pedido | Tarde | 1 | ⏳ F3-16 (ejemplo: `ed-vb-mina-galerias`) | ⏳ F3-16 (ejemplo: `cliente-obrero`, `protagonista`) | 6 | 0 | 1 | 7 |
| `d4.4` | El café | Noche | F3-16 | `ed-vb-reme` | `reme`, `quiroga`, `protagonista` | 14 | 1 | 1 | 16 |
| `d5.1` | La entrega | Mañana | F3-16 | `ed-vb-tienda` | `cliente-obrero`, `protagonista` | 6 | 0 | 0 | 6 |
| `d5.2` | El rumor | Mañana | F3-16 | `ed-vb-tienda` | `lucia`, `protagonista` | 14 | 1 | 0 | 15 |
| `d5.3` | El pico de nivel 2 | Tarde | F3-16 | `ed-vb-mina-galerias` | `teo`, `protagonista` | 6 | 2 | 1 | 9 |
| `d5.4` | La respuesta de casa | Noche | F3-16 | `ed-vb-casa` | `protagonista` | 10 | 0 | 2 | 12 |
| `d6.1` | Un rumor sin confirmar | Mañana | F3-16 | `ed-vb-tienda` | `protagonista` | 8 | 3 | 0 | 11 |
| `d6.2` | Mañana, el Heraldo | Noche | F3-16 | `ed-vb-casa` | `protagonista` | 6 | 0 | 1 | 7 |
| `d7.1` | Primera hora | Mañana | F3-16 | `ed-vb-tienda` | `teo`, `protagonista` | 12 | 4 | 0 | 16 |
| `d7.2` | La cuota | Tarde | F3-16 | `ed-vb-reme` | `reme`, `protagonista` | 18 | 2 | 2 | 22 |
| `d7.3` | El sello | Noche | F3-16 | `ed-vb-tienda` | `quiroga`, `protagonista` | 8 | 1 | 1 | 10 |
| `d7.4` | El decreto | Noche | F3-16 | `calle` | `voceador`, `protagonista` | 6 | 0 | 0 | 6 |

**Totales por día** (iguales a la sección 19):

| Día | Escenas | Cajas | Ayudas e interfaz | Cartas y avisos | Total |
|---|---|---|---|---|---|
| 1 | 6 | 53 | 12 | 6 | 71 |
| 2 | 4 | 30 | 10 | 1 | 41 |
| 3 | 4 | 37 | 8 | 1 | 46 |
| 4 | 4 | 38 | 6 | 3 | 47 |
| 5 | 4 | 36 | 3 | 3 | 42 |
| 6 | 2 | 14 | 3 | 1 | 18 |
| 7 | 4 | 44 | 7 | 3 | 54 |
| **Total** | **28** | **252** | **49** | **18** | **319** |

A estos **319** se suman las **3 cajas** de la interacción de pagar antes (sección 21.6), que no es una escena: **322 textos**, que se estiman en ≈ 323 ± 3.

### 21.3 Disparadores, cola y mecánica

| Escena | Disparador y requisitos | Opcional y cola | Mecánica que enseña | Decisión |
|---|---|---|---|---|
| `d1.1` | Al empezar la partida, ya creado el personaje y hecho el sorteo oculto de la facción de Reme | No. Es la primera escena del acto | Ninguna: el marco del día (tres bloques) y el efectivo | — |
| `d1.2` | Tras `d1.1`, en la casa de Reme | No. Si no se juega, espera en la cola | Ninguna: el marco de la herencia | — |
| `d1.3` | Tras `d1.2`, en la misma casa | No. Si no se juega, espera en la cola | Ninguna: el marco de la deuda | — |
| `d1.4` | Tras `d1.3`. Teo espera en la boca de las Galerías hasta que vayas | No. Si no vas, Teo espera y la escena queda en la cola | La expedición guiada: escanear y picar (una sola mecánica) | — |
| `d1.5` | Tras `d1.4`, de noche. La tienda no se abre | No. Si no se juega, espera en la cola | Ninguna | — |
| `d1.6` | Tras `d1.5`, en la casa obrera. La carta puede esperar y el día 2 sigue | No. Si no se juega, espera en la cola | Ninguna | `n-i-herencia` |
| `d2.1` | Día 2, tras el día 1. Sin ir a Quiroga el puesto sigue cerrado y vendes al contado en el mercado, con peor precio | No. Si no vas, espera en la cola | Ninguna: el trámite abre la tienda | — |
| `d2.2` | Tras `d2.1`, con el puesto a tu nombre | No. Si no se juega, espera en la cola | La tienda: surtir (Reponer) y fijar precios | — |
| `d2.3` | Tras `d2.2`. Abrir la tienda cuesta un bloque | No. Si no se juega, espera en la cola | La tienda: la primera venta y el margen | Principal: el margen. Menor: el nombre de la tienda |
| `d2.4` | Tras `d2.3`, de noche, al cerrar la caja por primera vez. La tienda no se abre | No. Si no cierras la caja, la cinta espera | Ninguna: se cuadra la caja | — |
| `d3.1` | Día 3, tras `d2.3`. Sin perforar no hay hierro: Teo lo vuelve a proponer cuando vuelvas | No. Si no vas, espera en la cola | Perforación (velocidad contra calor) | — |
| `d3.2` | Tras `d3.1`, en la boca de las Galerías | No. Si no se juega, espera en la cola | Ninguna | — |
| `d3.3` | Día 3, tarde, en el puesto. Lucía espera en la cola si no se juega | No. Si no se juega, espera en la cola | Ninguna | — |
| `d3.4` | Tras `d3.3`, con hierro en el inventario | Condicional: sin hierro la decisión no existe | Ninguna | Libre, sin nodo: vender o guardar el hierro |
| `d4.1` | Día 4, tras el día 3 | No. Si dejas ir al cliente, el pedido se pierde sin castigo y llegará otro | Ninguna: el pedido es el escenario del Regateo | — |
| `d4.2` | Tras `d4.1` | No | Regateo (oferta contra paciencia) | Libre, sin nodo: el mínimo del regateo |
| `d4.3` | Tras `d4.2`. Es una expedición normal; si tiene escena propia, la define ⏳ F3-16 (no es escena clave de F0-24) | Condicional: si dejas ir al cliente, no se juega | Ninguna | — |
| `d4.4` | Tras `d4.3`, de noche, en la casa de Reme | No. Si no vas, la oferta de pagar antes sigue abierta hasta el día 7 | Ninguna | — |
| `d5.1` | Día 5, con el pedido reunido (plazo de 3 días) | Condicional: sin pedido (se perdió el día 4) no se juega | Ninguna | — |
| `d5.2` | Tras `d5.1`, en el puesto | No. Si no se juega, espera en la cola | Ninguna | `n-i-lucia-rumor` |
| `d5.3` | Día 5, tarde, si pasas por Teo con 3 hierro. Sin plazo | Opcional (la única). Saltarla no cambia nada: el acto cierra igual | Ninguna obligatoria (opcional: la mejora de una herramienta) | Libre, sin nodo: ahorrar o mejorar |
| `d5.4` | De noche, tras `d5.2`, si contaste algo el día 1 | Condicional: con «nada» no llega carta y no se juega | Ninguna | — |
| `d6.1` | Día 6, en el puesto. Funciona sea cual sea la decisión del día 5 | No. Si no lees el rumor, el Heraldo del día 7 se explica solo | Confirmar un rumor con la noticia oficial | Libre, sin nodo: vender el hierro ya o esperar al Heraldo |
| `d6.2` | Tras `d6.1`, de noche, en casa | No | Ninguna | — |
| `d7.1` | Día 7, a primera hora, antes de la cuota. Si la primera hora se salta, en el primer bloque en que pases por el puesto | No. Si no abres la sección de empleos, la ficha queda en el tablón y cuenta igual | La cuota (el primer contacto con empleados no es mecánica: es una ficha bloqueada) | — |
| `d7.2` | Se dispara sola al caer la tarde del día 7. Si estás fuera, Reme pasa por el puesto y te ofrece la misma decisión | No. Es la fecha dura: no espera en la cola | La cuota (pagar a tiempo, antes o pedir tiempo) | `n-i-reme-plazo` |
| `d7.3` | Tras `d7.2`, de noche, con la cuota atendida y el primer contacto hecho | No | Ninguna | — |
| `d7.4` | Tras `d7.3`. Es la escena-gancho del acto: no cuenta para el tope de prensa | No | Ninguna | — |

La cola suelta las escenas de una en una y en orden, y nunca dos mecánicas nuevas a la vez (reglas de la cola ✅, [24](24-umbrales-de-acto.md) sección 10). Solo `d5.3` es **opcional** y no pasa por la cola. Son **condicionales** (dependen de algo que puede no haber ocurrido) `d3.4` (sin hierro), `d4.3` (si dejas ir al cliente), `d5.1` (sin pedido) y `d5.4` (con «nada» en la herencia). La única fecha dura es `d7.2`.

### 21.4 Hilos, sombras, props, ramas y responsable

| Escena | Hilos que siembra | Sombra (máximo una) | Props y pantalla del juego | Ramas | Responsable del texto |
|---|---|---|---|---|---|
| `d1.1` | `h-sorteo-oculto-de-la-faccion-de-reme` (el sorteo ocurre antes de la escena) | — | Una maleta. Pantalla: la interfaz del día con los tres bloques y 120 esquirlas | Ninguna | F3-47 |
| `d1.2` | `h-firma-de-la-herencia`, `h-traicion-de-reme` | La firma de Anselmo en los papeles | La llave, los papeles con la firma, la caja con el detector de Anselmo. Decorado de la pista del sorteo, sin texto: la lámpara de red, el papel sellado doblado sobre la mesa o el farol apagado. Pantalla: caja de diálogo sobre la casa de Reme | Por variante sorteada (`e-variante-reme`): solo el decorado, sin texto. Sin ramas por dificultad | F3-47 |
| `d1.3` | `h-abono-anonimo`, `h-trato-de-anselmo`, `h-prestamo-de-reme-a-anselmo`, `h-deuda-del-protagonista`, `h-traicion-de-reme` | El abono de «algún vecino bondadoso» | El libro de deuda, con la línea del abono. El decorado de la pista sigue a la vista. Pantalla: el libro de deuda | Por variante sorteada: solo el decorado. Sin ramas por dificultad | F3-47 |
| `d1.4` | `h-anselmo-sigue-vivo` | «Fui amigo de tu tío; lo demás, otro día» (Teo) | El pico prestado, tres menas de carbón. Pantalla: la expedición (escáner y Picado) | Ninguna | F3-47 |
| `d1.5` | `h-libreta-sin-cierre` | La libreta con su última anotación sin fecha | La llave que abre el puesto, polvo, el cajón de la caja con la libreta. Pantalla: la libreta | Ninguna | F3-47 |
| `d1.6` | `h-lampara-y-cinta-1`, `h-vega-mansa-y-el-juramento`, `h-deuda-del-banco-agrario` | La lámpara de minero sobre la mesa | La lámpara de minero (no la lámpara de red), papel y pluma. Pantalla: la carta con tres botones | Por decisión: `.todo`, `.parte` y `.nada` (con «nada» no se escribe carta) | F3-47 |
| `d2.1` | — | — | El sello y la oficina del Inspector. Pantalla: el trámite y su costo | Por género: `.f` en «estimado/a» (Quiroga). Sin dinero: Reme fía la gestión | F3-47 |
| `d2.2` | — | — | Los estantes y el saco de carbón de Anselmo en la trastienda. Pantalla: Reponer | Con carbón propio o con el saco de Anselmo | F3-47 |
| `d2.3` | — | — | El cartel con el nombre. Pantalla: la tienda abierta (margen por defecto 20 %) y la pantalla del nombre (F3-14) | Nombre vacío: «Puesto de {nombre}». Gestión fiada si no alcanza el efectivo | F3-47; la noticia y el rumor del día, F3-31 |
| `d2.4` | `h-lampara-y-cinta-1` | La cinta 1 | La caja, el cajón con doble fondo y el objeto «Carrete 1» (sin reproducción). Pantalla: el cierre de caja | Ninguna | F3-47 |
| `d3.1` | — | — | El taladro que presta Teo (no entra en el inventario) y la barra de la herramienta. Pantalla: Perforación | Ninguna | F3-47 |
| `d3.2` | `h-pozo-negro` | — | La placa de Pozo Negro, prop fijo de la boca de las Galerías ([26](26-zonas-y-edificios.md)). Pantalla: caja de diálogo sobre la boca de las Galerías | Ninguna | F3-47 |
| `d3.3` | `h-comision-y-mal-del-eter`, `h-lealtad-de-lucia` | «La Comisión del Éter pidió más hierro» (Lucía) | El Teletipo de Lucía. Es el rumor del día. Pantalla: caja de diálogo sobre el puesto | Ninguna | F3-47 |
| `d3.4` | — | — | La trastienda y el mercado. Teo recoge el taladro al final. Pantalla: vender o guardar | Ninguna | F3-47; la noticia del hierro, F3-31 |
| `d4.1` | — | — | El tablón de pedidos con la tarjeta del pedido (8 de carbón, plazo de 3 días; cifras en F3-32). La nota del Heraldo del día con `{nombre}` y `{tienda}`. Pantalla: el tablón de pedidos y caja de diálogo sobre el puesto | Ninguna | F3-47; la tarjeta del pedido, F3-32; la nota del Heraldo, F3-31 |
| `d4.2` | — | — | Pantalla: el Regateo | Ninguna | F3-47 |
| `d4.3` | — | — | Una expedición normal. Pantalla: la expedición. Ejemplo: el cliente deja un rumor útil (el herrero de la calle Honda) | Si dejas ir al cliente no se juega y el día 5 usa el rumor de reserva | F3-47 |
| `d4.4` | `h-pista-lampara-de-red`, `h-pista-deferencia-de-quiroga`, `h-pista-farol-vinotinto` (solo el de la variante sorteada) | — | Según la variante sorteada: la lámpara de red con una «A» grabada; Quiroga con el papel sellado; el farol vinotinto encendido. Los otros dos no existen en esa partida. Pantalla: caja de diálogo sobre la casa de Reme | Por variante sorteada (`.consorcio`, `.ministerio`, `.faroleros`) | F3-47 |
| `d5.1` | — | — | El tablón de pedidos y el cobro. Pantalla: caja de diálogo sobre el puesto | Sin pedido, la escena no se juega | F3-47 |
| `d5.2` | `h-lealtad-de-lucia` | — | El Teletipo. Lucía da primero su rumor del ferrocarril, aunque luego calles. Pantalla: la decisión con tres botones | Por decisión: `.todo`, `.parte` y `.nada`; `.reserva` si no oíste al cliente | F3-47, incluidos los tres textos del Teletipo (entero, mitad y reserva) |
| `d5.3` | — | — | El pico de nivel 2 (3 hierro y 480 esquirlas). Sin ventana de tutorial. Pantalla: la oferta de Teo con su «?» | Sin hierro, la mejora espera | F3-47 |
| `d5.4` | `h-vega-mansa-y-el-juramento` | — | La carta de casa. Pantalla: la carta | Por decisión del día 1: `.todo` y `.parte`; `.nada` no se juega | F3-47 |
| `d6.1` | — | — | El Teletipo y el tablón con la tarjeta del pedido urgente (opcional). Pantalla: el mercado | Ninguna | F3-47; el rumor del Teletipo, F3-31; la tarjeta del pedido urgente, F3-32 |
| `d6.2` | — | — | La casa obrera de noche. Pantalla: caja de diálogo sobre la casa | Ninguna | F3-47 |
| `d7.1` | — | — | La sección de empleos con la tarjeta fija «Candidato sin nombre» (Minero nivel 1, 70 esquirlas al día, Lealtad «?»), el botón «Contratar» bloqueado y el Heraldo del día. Teo deja el pico si no lo mejoraste. Pantalla: la sección de empleos | Ninguna | F3-47; la confirmación del Heraldo, F3-31 |
| `d7.2` | `h-deuda-del-protagonista`, `h-traicion-de-reme` | — | El libro de deuda y, según la variante sorteada, la lámpara de red, el papel sellado doblado o el farol vinotinto encendido. Pantalla: la elección de pago | Por decisión: `.antes`, `.plazo` y `.tarde`; por dificultad: `.serie` (Novato e Intermedio) y `.suma` (Difícil y Hardcore); por variante sorteada; visita de Reme | F3-47 |
| `d7.3` | — | — | El sello. La tienda está cerrada y no se abre. Pantalla: caja de diálogo sobre el puesto cerrado | Por género: `.f` en «estimado/a» y «Minera con licencia». Por variante sorteada: Quiroga pregunta por doña Reme (Ministerio) | F3-47 |
| `d7.4` | — | — | Un voceador en la calle. El decreto no nombra a Montenegro. Pantalla: caja de diálogo sobre la calle | Ninguna | F3-47; el titular del decreto, F3-31 |

Son siete sombras (seis de Anselmo y una de la Comisión), como en la sección 17. Todos los hilos existen en `hilos.json`. Responsables: F3-47 escribe las escenas; F3-31, la prensa guionizada (con el titular del decreto del día 7); F3-47 también escribe los tres textos del Teletipo del día 5; F3-32, las tarjetas de los pedidos con sus cifras (8, 448 y 729), que no van en las escenas.

### 21.5 Qué textos lleva cada escena

Lo decidido son los **totales por escena** (21.2) y estas piezas: el aviso «Encontraste una cinta», la ficha del candidato con su aviso de bloqueo y las 3 cajas de pagar antes (21.6). El reparto de cajas por hablante, la lista de ayudas y los nombres de los avisos son un **ejemplo orientativo**; lo fija ⏳ F3-47 al escribir, siempre respetando los totales. Los avisos de esta tabla (salvo los marcados) son ejemplos de qué tipo de aviso lleva la escena.

| Escena | Cajas (reparto orientativo) | Ayudas e interfaz (orientativo) | Cartas y avisos (orientativo) |
|---|---|---|---|
| `d1.1` | Narrador 4, {nombre} 2 | los tres bloques del día; el efectivo de 120 esquirlas; otras ayudas de la interfaz del primer día (2) | — |
| `d1.2` | Reme 6, {nombre} 2, Narrador 2 | — | los papeles de la herencia, con la firma de Anselmo |
| `d1.3` | Reme 6, {nombre} 3, Narrador 1 | el libro de deuda: capital, cuota y abono; la primera cuota llega el día 7 | la página del libro de deuda |
| `d1.4` | Teo 9, {nombre} 3, Narrador 2 | escanear: tocar la mena y ver los rangos (2); picar: fuerza y precisión (2); el resultado de la primera expedición | — |
| `d1.5` | Narrador 4, {nombre} 2 | la libreta en el diario | el primer apunte de la libreta, que manda ir a Quiroga; la última anotación, sin fecha |
| `d1.6` | común 3, `.todo` 1, `.parte` 1, `.nada` 2 | — | la carta a Vega Mansa, `.todo`; la carta a Vega Mansa, `.parte` |
| `d2.1` | Quiroga 7, {nombre} 3 | la gestión de Quiroga: 240 esquirlas, con la primera venta; el fiado de Reme si no alcanza | — |
| `d2.2` | Narrador 3, {nombre} 2 | Reponer: arrastrar la mercancía a los estantes (2); fijar el precio | — |
| `d2.3` | Cliente 4, {nombre} 3, Narrador 3 | el margen: precio de lista y cliente medio (2); la pantalla del nombre de la tienda; el cartel con el nombre por defecto | — |
| `d2.4` | Narrador 4, {nombre} 1 | el cierre de caja | el aviso «Encontraste una cinta» ✅ |
| `d3.1` | Teo 8, {nombre} 2, Narrador 2 | velocidad contra calor (2); la barra de desgaste de la herramienta (2); el taladro es solo de hoy; el resultado de la expedición de hierro | — |
| `d3.2` | Teo 5, {nombre} 1, Narrador 1 | — | la inscripción de la placa de Pozo Negro |
| `d3.3` | Lucía 7, {nombre} 3 | — | — |
| `d3.4` | Narrador 4, {nombre} 3, Teo 1 | guardar cuesta muy poco; el mercado sube con el bloque | — |
| `d4.1` | Cliente 6, {nombre} 2, Narrador 2 | qué es un pedido de cliente | un aviso de pedido nuevo |
| `d4.2` | Cliente 4, {nombre} 3, Narrador 1 | oferta contra paciencia (2); el mínimo; el resultado del regateo | — |
| `d4.3` | Cliente 3, Narrador 3 | — | un aviso de pedido reunido |
| `d4.4` | común 4, `.consorcio` 3, `.ministerio` 4, `.faroleros` 3 | pagar antes está disponible desde hoy | un aviso de que ya se puede pagar antes |
| `d5.1` | Cliente 4, {nombre} 1, Narrador 1 | — | — |
| `d5.2` | común 4, `.todo` 3, `.parte` 3, `.nada` 3, `.reserva` 1 | qué pasa con lo que cuentas | — |
| `d5.3` | Teo 4, {nombre} 2 | el «?» de la oferta: qué mejora y cuánto cuesta (2) | un aviso de pico mejorado |
| `d5.4` | común 2, `.todo` 4, `.parte` 4 | — | la carta de casa, `.todo`; la carta de casa, `.parte` |
| `d6.1` | Narrador 6, {nombre} 2 | qué es SIN CONFIRMAR; el Heraldo de mañana lo confirma o no; el tablón: el pedido urgente es opcional | — |
| `d6.2` | Narrador 4, {nombre} 2 | — | un aviso de cierre del día |
| `d7.1` | Teo 6, Narrador 4, {nombre} 2 | la ficha del candidato ✅; «Contratar» bloqueado y su motivo ✅; el «?» de la ficha, sin el costo de la mejora; el libro de deuda marca «hoy» | — |
| `d7.2` | común 3, `.antes` (agradecimiento) 1, `.plazo` 2, `.tarde` por dificultad, `.serie` y `.suma` 4, visita de Reme al puesto 2, prórroga automática sin respuesta 1, ecos del sorteo 3, cierre 2 | la elección de pago, con {cuota}; qué pasa si pides tiempo | un aviso de cuota atendida; un aviso de cuota anotada con recargo |
| `d7.3` | Quiroga 5, eco del Ministerio 1, {nombre} 2 | el Acto I se cierra: licencia sellada | el sello «Minero con licencia» |
| `d7.4` | Voceador 3, Narrador 2, {nombre} 1 | — | — |

En las cajas, «común» es lo que se dice en todas las ramas y cada sufijo es la variante que se suma. Las cifras suman exactamente la columna C de la tabla maestra. Con ✅ van las piezas decididas por el autor.

### 21.6 La interacción de pagar antes

No es una escena de `dN.M` y **no cuenta entre las 28**: es una interacción corta que se suma a los textos (decisión del autor, 2026-10-16).

| Campo | Contenido |
|---|---|
| Identificador | `pa`, con las cajas `pa.c01` a `pa.c03` (3 cajas; sin ayudas ni cartas). Las 3 cajas están decididas; los identificadores son una convención propuesta que F3-16 y F3-47 pueden renombrar |
| Lugar y personajes | `ed-vb-reme`, «gastar: cuotas de la deuda» ([26](26-zonas-y-edificios.md)); `reme` y `protagonista` |
| Disparador | Entrar en casa de Reme desde el día 4 con la cuota en caja. Solo es realista los días 6 y 7. Es opcional y no pasa por la cola |
| Botón | El de la salida «antes» de `n-i-reme-plazo`: `n-i-reme-plazo.b1`, «Pagar antes del plazo». Salir sin pagar no lleva botón |
| Efecto | Fija `f-pago-reme` = `antes`, deja la cuota en 900 y baja el interés 1 pp, del 4 % al 3 % mensual ([28](28-numeros-base-de-la-economia.md), sección 7.2) |
| Después | `d7.2` pasa a una línea de agradecimiento (identificador propuesto `d7.2.c04.antes`, renombrable por F3-16 y F3-47) |
| Líneas de ejemplo | **Reme:** «Si me adelantas la cuota, te rebajo un puntito, criatura.» · **Reme:** «Hecho. Quedan {cuota} esquirlas y un puntito menos de interés.» |
| Responsables | Interacción: ⏳ F3-16. Texto: ⏳ F3-47. No cambia `world.json` ni el simulador |

### 21.7 Variables

El conjunto es **cerrado**: ningún texto usa otras llaves.

| Variable | Qué es | Dónde sale |
|---|---|---|
| `{nombre}` | El nombre del protagonista | Cartas y diálogos; la prensa lo cita en tercera persona y sin cargo ([18](18-biblia-narrativa.md), 1.10) |
| `{tienda}` | El nombre de la tienda | El cartel (`d2.3`), la tarjeta del pedido del día 4 y la nota del Heraldo del día 4. Por defecto «Puesto de {nombre}», guardado vacío y resuelto al mostrar |
| `{cuota}` | El importe vigente de la cuota en esquirlas: 960, o 900 si pagaste antes | `d7.2` y `pa` |
| `{recargo}` | El importe del recargo en esquirlas, no el porcentaje: 58 en Intermedio (38, 115 y 173 en Novato, Difícil y Hardcore) | `d7.2` (`.tarde`) |

- Los **porcentajes** (4, 6, 12 y 18 %) salen de los datos en la interfaz, no del diálogo.
- Las **cifras de los pedidos** (8, 448 y 729) van en las tarjetas de ⏳ F3-32, no en las escenas de F3-47.
- Los **números se formatean según el idioma** ⏳ F1-20. El largo máximo del nombre de la tienda, ⏳ F1-18.

### 21.8 Botones de las tres decisiones pequeñas

Los textos de `decisions.json` son descripciones para el equipo y pasan de 28 caracteres ([18](18-biblia-narrativa.md), 1.9); estos son los botones, de 28 caracteres como máximo. Las opciones y las banderas son las de `decisions.json` y [23](23-arbol-de-decisiones.md), sin cambios.

| Botón | Opción | Texto del botón | Caracteres | Fija |
|---|---|---|---|---|
| `n-i-herencia.b1` | `todo` | «Contarles todo» | 14 | `f-familia` |
| `n-i-herencia.b2` | `parte` | «Solo lo del puesto» | 18 | `f-familia` |
| `n-i-herencia.b3` | `nada` | «No decir nada todavía» | 21 | `f-familia` |
| `n-i-lucia-rumor.b1` | `contar` | «Contárselo entero» | 17 | `m-lucia` |
| `n-i-lucia-rumor.b2` | `mitad` | «Contarle la mitad» | 17 | `m-lucia` |
| `n-i-lucia-rumor.b3` | `callar` | «No contarle nada» | 16 | `m-lucia` |
| `n-i-reme-plazo.b1` | `antes` | «Pagar antes del plazo» | 21 | `f-pago-reme` |
| `n-i-reme-plazo.b2` | `plazo` | «Pagar justo en el plazo» | 23 | `f-pago-reme` |
| `n-i-reme-plazo.b3` | `tarde` | «Pedir una semana más» | 20 | `f-pago-reme` |

Las ramas del texto usan `.todo`, `.parte` y `.nada` para la herencia y el rumor de Lucía (contar, mitad y callar) y `.antes`, `.plazo` y `.tarde` para la cuota.

### 21.9 Qué toma cada tarea de esta sección

| Tarea | Toma |
|---|---|
| ⏳ F3-16 | Las 28 escenas con bloque, peso, disparador, cola, ramas y props (21.2 a 21.4), la interacción de pagar antes, la visita de Reme al puesto, el taladro del día 3, la placa de Pozo Negro, la cinta 1 mínima, el papel sellado y la ficha del candidato |
| ⏳ F3-47 | Los identificadores y la tabla maestra (21.1, 21.2 y 21.5), las variables (21.7), los botones (21.8) y los tres textos del Teletipo del día 5 |
| ⏳ F3-31 y ⏳ F3-32 | La prensa guionizada (con el titular del decreto) y las tarjetas de los pedidos, que no entran en F3-47 (21.4) |
| ⏳ F0-24 | Las siete escenas clave con lugar, personajes, props, pantalla, línea de ejemplo y variantes (secciones 4 a 10 y 21.4) |
| ⏳ F1-20 | Los términos de la sección 20 |

---

## Puntos confirmados por el autor ✅

El autor confirmó el 2026-10-16 (F0-80) los dos puntos que estaban en propuesta. En la pasada de cierre del mismo día (F0-86) confirmó el resto: la estructura de los siete días, las correcciones de cifras y reglas, las once decisiones de la pasada (pagar antes, la cuota del día 7, el taladro, la prensa del día, el rumor de Lucía, las pistas del Ministerio, la cinta 1, la ficha del candidato y el nombre por defecto de la tienda) y la sección 21. No queda ninguna propuesta pendiente en este documento. Las preguntas anteriores (el recargo en Difícil y Hardcore, los peligros ambientales y hasta qué día no hay pérdida grave, que incluye el día 3) ya estaban respondidas y pasaron a la sección 1 ✅.

| Punto | Decisión ✅ | Qué cambiaría si el autor prefiriera otra cosa |
|---|---|---|
| El día 1: escanear y picar | **Una sola mecánica**, la expedición guiada. Así el día 1 respeta «una mecánica nueva por día» | Si fueran dos, uno de los dos pasaría al día 2 y se movería el trámite de Quiroga; cambiarían las secciones 3 a 5 |
| Las tres pistas del sorteo | **Caen el día 4 de noche** (`d4.4`), con **ecos los días 1 y 7** | Si cayeran otro día, cambiarían la sección 13 y los ecos de `d1.2`, `d1.3`, `d7.2` y `d7.3` |

---

## Pendiente

- ✅ Montos de la cuota, el recargo (y su valor mayor en Difícil y Hardcore), la gestión de Quiroga, el efectivo inicial, los precios, el costo de guardar y de la mejora: fijados en [28](28-numeros-base-de-la-economia.md).
- ⏳ F0-24 Storyboard de las escenas clave (sección 19 y sección 21).
- ⏳ F3-48 Construye la cola, el diario y el aviso de rescate (diseño cerrado ✅ en [24](24-umbrales-de-acto.md), sección 10); las escenas por evento cumplen su invariante (una mecánica nueva a la vez).
- ⏳ F2-02 Mecanismo de los pesos de bloque; ⏳ F2-01 sorteo guardado en el estado de la partida; ⏳ F1-23 forzar la variante desde la consola.
- ⏳ F4-150 Reproductor y sistema de cintas; ⏳ F4-151 texto y voz de la cinta 1.
- ⏳ F3-14 Pantalla del nombre de la tienda; ⏳ F1-18 largo máximo.
- ⏳ F3-47 Textos del Acto I (14 h): los siete días, las tres decisiones pequeñas con sus botones, las tres pistas, la interacción de pagar antes, los avisos y los tres textos del Teletipo del día 5; sin los demás textos de prensa ni de pedidos guionizados.
- ⏳ F3-16 Escenas, cola, ayudas, props de las pistas (con el papel sellado), taladro del día 3, placa, cinta mínima, pagar antes y ficha del candidato del día 7 (14 h, sin textos); ⏳ F3-17 la deuda y sus dos reglas (6 h); ⏳ F3-22 los valores por dificultad.
- ⏳ F3-31 Noticias, con los textos de las 3 noticias guionizadas, la nota del Heraldo del día 4 y el titular del decreto, y ⏳ F3-32 pedidos de cliente, con los 2 pedidos guionizados de las secciones 3 a 10; ⏳ F3-30 traducción (13 h).
- ⏳ F3-10 Peligros ambientales de la zona 1: fuera del Acto I, entran desde el Acto II ✅.
- ⏳ F4-172 Nombres procedurales del cliente y del candidato.
- ⏳ F4-94 Sección de empleos real (y qué medio la publica), ⏳ F4-96 su sesgo y ⏳ F4-97 la información oculta.
- ⏳ F1-20 Inglés de los términos de la sección 20.
- ✅ Los puntos que esperaban este guion (F0-23 y F0-86) están resueltos en [01](01-core-loop.md), [06](06-roadmap-y-pendientes.md), [08](08-historia-y-personaje.md), [17](17-mapa-de-historia.md), [18](18-biblia-narrativa.md), [21](21-pasado-de-valdoria.md), [22](22-acto-ii-variantes.md), [23](23-arbol-de-decisiones.md), [24](24-umbrales-de-acto.md) y [25](25-finales-y-epilogos.md).

---

## Criterios cumplidos

| Criterio | Cumplido | Dónde |
|---|---|---|
| Siete días de tres bloques, con una decisión por día | Sí ✅ | Sección 3 |
| Una mecánica nueva por día como máximo | Sí ✅ | Sección 3 |
| Cuota del día 7 con sus dos reglas por dificultad | Sí ✅ | Sección 11 |
| Reabrir el puesto como trámite más primera venta, con el nombre de la tienda | Sí ✅ | Sección 5 y 18 |
| Las tres decisiones pequeñas con su día y sus botones | Sí ✅ | Secciones 12 y 21.8 |
| Las tres pistas del sorteo, con día, lectura inocente y variante | Sí ✅ | Sección 13 |
| Cinta 1 y primer contacto con los empleados (día 7, a primera hora) | Sí ✅ | Secciones 14 y 15 |
| Días 5 y 6 ligeros: mejora y pedido urgente opcionales, día 6 solo con noticia y rumor | Sí ✅ | Secciones 1, 8 y 9 |
| Una sombra por escena como máximo y Anselmo solo como rastro | Sí ✅ | Secciones 17 y 21.4 |
| Sin atascos y con la deuda sin bloquear | Sí ✅ | Secciones 2, 4 a 11 |
| Textos y horas de F3-47, F3-16, F3-17, F3-30, F3-31 y F3-32 | Sí ✅ | Sección 19 |
| Esquema de escenas y textos: 28 escenas con identificador, tabla maestra, variables y botones | Sí ✅ | Sección 21 |
| Peligros ambientales fuera del Acto I | Sí ✅ | Secciones 1, 2.2 y 2.3 |
| Las dos propuestas (el día 1 como una sola mecánica y las tres pistas el día 4 de noche) | Sí ✅ | Sección «Puntos confirmados por el autor» |
