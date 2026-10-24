---
id: "doc-27-s21"
tipo: "seccion"
title: "21 · Esquema de escenas y textos ✅"
aliases: ["doc-27-s21"]
documento: "[[27 Guion del Acto I, día a día]]"
limpieza: 100
abiertos: 0
espera: 25
aplazado_a: ["[[F0-24 Storyboard de las escenas clave del Acto I]]", "[[F0-78 Diseñar el diario, la cola de historia y la misión de]]", "[[F1-18 Fuente pixel con caracteres latinos extendidos y plan de]]", "[[F1-20 Flujo de traducción - extracción, traducción asistida por]]", "[[F2-02 Ciclo de 3 bloques y avance del día]]", "[[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado]]", "[[F3-31 Diez noticias iniciales y seis eventos del Acto I]]", "[[F3-32 Doce pedidos de ejemplo con clientes]]", "[[F3-47 Textos del Acto I - guion de los siete días]]"]
estado: "con-aplazados"
anterior: "[[27 §20 Términos nuevos del glosario]]"
siguiente: "[[27 §Puntos confirmados por el autor]]"
arriba: "[[27 Guion del Acto I, día a día]]"
fuente: "studio/docs/27-guion-del-acto-i.md:560"
generado: true
---

# 21 · Esquema de escenas y textos ✅

> Esta sección la aprobó el autor el 2026-10-16 (F0-86) y es el esquema para quien construye ( F3-16), quien escribe ( F3-47, F3-31 y F3-32)…

← [[27 §20 Términos nuevos del glosario]] · [[27 Guion del Acto I, día a día|↑ 27]] · [[27 §Puntos confirmados por el autor]] →

**Estado:** cerrada. Esta sección la aprobó el autor el 2026-10-16 ([[F0-86 Pasada de cierre - guion del Acto I (27)|F0-86]]) y es el esquema para quien construye (⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado|F3-16]]), quien escribe (⏳ [[F3-47 Textos del Acto I - guion de los siete días|F3-47]], ⏳ [[F3-31 Diez noticias iniciales y seis eventos del Acto I|F3-31]] y ⏳ [[F3-32 Doce pedidos de ejemplo con clientes|F3-32]]), quien dibuja (⏳ [[F0-24 Storyboard de las escenas clave del Acto I|F0-24]]) y quien programa el simulador. No renumera las secciones 1 a 20, que citan `hilos.json` y los documentos 04, 21, 22, 23 y 24. Los textos finales de cada pieza son de su responsable; las frases entre comillas de las secciones 4 a 10 son ejemplos de voz.

### 21.1 Identificadores y convenciones

| Cosa | Convención |
|---|---|
| Escena | `dN.M`: día esperado (`N`) y orden dentro del día (`M`). Son 28 y no se renumeran |
| Caja de diálogo | `dN.M.cNN` (con retrato; unos 100 caracteres, 34 por línea, 3 líneas, una idea por caja: [[18 Biblia narrativa\|18]], 1.9) |
| Ayuda o interfaz | `dN.M.uNN` (ayudas «?», etiquetas, mensajes de pantalla) |
| Carta o aviso | `dN.M.kNN` (cartas, papeles, libreta, placa, sello y avisos del juego) |
| Botón de decisión | `n-….bK`, por ejemplo [[Cómo cuentas la herencia a tu familia - todo\|n-i-herencia.b1]] |
| Variante de rama | Sufijo sobre el texto: `.todo`, `.parte`, `.nada` (herencia y rumor de Lucía) y `.antes`, `.plazo`, `.tarde` (cuota) ✅ (decisión del autor, 2026-10-16) |
| Sufijos adicionales | `.consorcio`, `.ministerio`, `.faroleros` (variante sorteada, `e-variante-reme`), `.serie` y `.suma` (la regla de prórroga por dificultad) y `.reserva` (rumor de reserva de Lucía). Convención propuesta; [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] y [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] pueden renombrar. Ejemplo: `d7.2.c05.plazo` (identificador también propuesto) |
| Variante de género | Sufijo `.f`, **solo** donde [[18 Biblia narrativa\|18]], 1.2 lo exige: «estimado/a» de Quiroga ([[d2.1 El trámite\|d2.1]] y [[d7.3 El sello\|d7.3]]) y «Minera con licencia» ([[d7.3 El sello\|d7.3]]). Ejemplo: `d7.3.c03.f` |
| Peso y bloque | Cada escena tiene un bloque (mañana, tarde o noche) y un peso: 0, medio bloque o 1. Minar y abrir la tienda valen 1 ([[01 Core loop y ciclo del día\|01]]); el resto de pesos los asigna ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] y el mecanismo lo define ⏳ [[F2-02 Ciclo de 3 bloques y avance del día\|F2-02]] |
| Lugar | Un `id` de edificación de [[26 Zonas y edificios\|26]] (`ed-vb-*`) o «calle» |
| Personajes | Los `id` de `world.json` (`protagonista`, `reme`, `teo`, `quiroga`, `lucia`, `voceador`, `cliente-obrero`). La familia de Vega Mansa solo escribe cartas: no es personaje en escena |
| Totales | Las cifras por escena incluyen todas sus variantes de rama, de género y de sorteo |

### 21.2 Tabla maestra de las 28 escenas

El peso es 1 donde la escena es una expedición o abre la tienda ([[01 Core loop y ciclo del día|01]]); en el resto lo asigna [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado|F3-16]] (⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado|F3-16]], mecanismo ⏳ [[F2-02 Ciclo de 3 bloques y avance del día|F2-02]]). Las columnas de textos cuentan cajas (C), ayudas e interfaz (U) y cartas y avisos (K).

| Escena | Título | Bloque | Peso | Lugar | Personajes | C | U | K | Total |
|---|---|---|---|---|---|---|---|---|---|
| [[d1.1 Llegada\|d1.1]] | Llegada | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | `calle` | `protagonista` | 6 | 4 | 0 | 10 |
| [[d1.2 La llave y los papeles\|d1.2]] | La llave y los papeles | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa de Reme\|ed-vb-reme]] | `reme`, `protagonista` | 10 | 0 | 1 | 11 |
| [[d1.3 El libro de deuda\|d1.3]] | El libro de deuda | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa de Reme\|ed-vb-reme]] | `reme`, `protagonista` | 10 | 2 | 1 | 13 |
| [[d1.4 Las Galerías\|d1.4]] | Las Galerías | Tarde | 1 | [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]] | `teo`, `protagonista` | 14 | 5 | 0 | 19 |
| [[d1.5 El puesto cerrado\|d1.5]] | El puesto cerrado | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `protagonista` | 6 | 1 | 2 | 9 |
| [[d1.6 La carta\|d1.6]] | La carta | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa obrera\|ed-vb-casa]] | `protagonista` | 7 | 0 | 2 | 9 |
| [[d2.1 El trámite\|d2.1]] | El trámite | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Oficina del Inspector\|ed-vb-quiroga]] | `quiroga`, `protagonista` | 10 | 2 | 0 | 12 |
| [[d2.2 Surtir los estantes\|d2.2]] | Surtir los estantes | Tarde | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `protagonista` | 5 | 3 | 0 | 8 |
| [[d2.3 La primera venta\|d2.3]] | La primera venta | Tarde | 1 | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `cliente-obrero`, `protagonista` | 10 | 4 | 0 | 14 |
| [[d2.4 Cierre de caja\|d2.4]] | Cierre de caja | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `protagonista` | 5 | 1 | 1 | 7 |
| [[d3.1 Perforar\|d3.1]] | Perforar | Mañana | 1 | [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]] | `teo`, `protagonista` | 12 | 6 | 0 | 18 |
| [[d3.2 La placa\|d3.2]] | La placa | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]] | `teo`, `protagonista` | 7 | 0 | 1 | 8 |
| [[d3.3 Lucía\|d3.3]] | Lucía | Tarde | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `lucia`, `protagonista` | 10 | 0 | 0 | 10 |
| [[d3.4 ¿Vender o guardar\|d3.4]] | ¿Vender o guardar? | Tarde | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `teo`, `protagonista` | 8 | 2 | 0 | 10 |
| [[d4.1 El pedido\|d4.1]] | El pedido | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `cliente-obrero`, `protagonista` | 10 | 1 | 1 | 12 |
| [[d4.2 Regatear\|d4.2]] | Regatear | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `cliente-obrero`, `protagonista` | 8 | 4 | 0 | 12 |
| [[d4.3 Reunir el pedido\|d4.3]] | Reunir el pedido | Tarde | 1 | ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] (ejemplo: [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]]) | ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] (ejemplo: `cliente-obrero`, `protagonista`) | 6 | 0 | 1 | 7 |
| [[d4.4 El café\|d4.4]] | El café | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa de Reme\|ed-vb-reme]] | `reme`, `quiroga`, `protagonista` | 14 | 1 | 1 | 16 |
| [[d5.1 La entrega\|d5.1]] | La entrega | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `cliente-obrero`, `protagonista` | 6 | 0 | 0 | 6 |
| [[d5.2 El rumor\|d5.2]] | El rumor | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `lucia`, `protagonista` | 14 | 1 | 0 | 15 |
| [[d5.3 El pico de nivel 2\|d5.3]] | El pico de nivel 2 | Tarde | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]] | `teo`, `protagonista` | 6 | 2 | 1 | 9 |
| [[d5.4 La respuesta de casa\|d5.4]] | La respuesta de casa | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa obrera\|ed-vb-casa]] | `protagonista` | 10 | 0 | 2 | 12 |
| [[d6.1 Un rumor sin confirmar\|d6.1]] | Un rumor sin confirmar | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `protagonista` | 8 | 3 | 0 | 11 |
| [[d6.2 Mañana, el Heraldo\|d6.2]] | Mañana, el Heraldo | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa obrera\|ed-vb-casa]] | `protagonista` | 6 | 0 | 1 | 7 |
| [[d7.1 Primera hora\|d7.1]] | Primera hora | Mañana | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `teo`, `protagonista` | 12 | 4 | 0 | 16 |
| [[d7.2 La cuota\|d7.2]] | La cuota | Tarde | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Casa de Reme\|ed-vb-reme]] | `reme`, `protagonista` | 18 | 2 | 2 | 22 |
| [[d7.3 El sello\|d7.3]] | El sello | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | [[Tienda de Villa Brasa\|ed-vb-tienda]] | `quiroga`, `protagonista` | 8 | 1 | 1 | 10 |
| [[d7.4 El decreto\|d7.4]] | El decreto | Noche | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | `calle` | `voceador`, `protagonista` | 6 | 0 | 0 | 6 |

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
| [[d1.1 Llegada\|d1.1]] | Al empezar la partida, ya creado el personaje y hecho el sorteo oculto de la facción de Reme | No. Es la primera escena del acto | Ninguna: el marco del día (tres bloques) y el efectivo | — |
| [[d1.2 La llave y los papeles\|d1.2]] | Tras [[d1.1 Llegada\|d1.1]], en la casa de Reme | No. Si no se juega, espera en la cola | Ninguna: el marco de la herencia | — |
| [[d1.3 El libro de deuda\|d1.3]] | Tras [[d1.2 La llave y los papeles\|d1.2]], en la misma casa | No. Si no se juega, espera en la cola | Ninguna: el marco de la deuda | — |
| [[d1.4 Las Galerías\|d1.4]] | Tras [[d1.3 El libro de deuda\|d1.3]]. Teo espera en la boca de las Galerías hasta que vayas | No. Si no vas, Teo espera y la escena queda en la cola | La expedición guiada: escanear y picar (una sola mecánica) | — |
| [[d1.5 El puesto cerrado\|d1.5]] | Tras [[d1.4 Las Galerías\|d1.4]], de noche. La tienda no se abre | No. Si no se juega, espera en la cola | Ninguna | — |
| [[d1.6 La carta\|d1.6]] | Tras [[d1.5 El puesto cerrado\|d1.5]], en la casa obrera. La carta puede esperar y el día 2 sigue | No. Si no se juega, espera en la cola | Ninguna | [[Cómo cuentas la herencia a tu familia\|n-i-herencia]] |
| [[d2.1 El trámite\|d2.1]] | Día 2, tras el día 1. Sin ir a Quiroga el puesto sigue cerrado y vendes al contado en el mercado, con peor precio | No. Si no vas, espera en la cola | Ninguna: el trámite abre la tienda | — |
| [[d2.2 Surtir los estantes\|d2.2]] | Tras [[d2.1 El trámite\|d2.1]], con el puesto a tu nombre | No. Si no se juega, espera en la cola | La tienda: surtir (Reponer) y fijar precios | — |
| [[d2.3 La primera venta\|d2.3]] | Tras [[d2.2 Surtir los estantes\|d2.2]]. Abrir la tienda cuesta un bloque | No. Si no se juega, espera en la cola | La tienda: la primera venta y el margen | Principal: el margen. Menor: el nombre de la tienda |
| [[d2.4 Cierre de caja\|d2.4]] | Tras [[d2.3 La primera venta\|d2.3]], de noche, al cerrar la caja por primera vez. La tienda no se abre | No. Si no cierras la caja, la cinta espera | Ninguna: se cuadra la caja | — |
| [[d3.1 Perforar\|d3.1]] | Día 3, tras [[d2.3 La primera venta\|d2.3]]. Sin perforar no hay hierro: Teo lo vuelve a proponer cuando vuelvas | No. Si no vas, espera en la cola | Perforación (velocidad contra calor) | — |
| [[d3.2 La placa\|d3.2]] | Tras [[d3.1 Perforar\|d3.1]], en la boca de las Galerías | No. Si no se juega, espera en la cola | Ninguna | — |
| [[d3.3 Lucía\|d3.3]] | Día 3, tarde, en el puesto. Lucía espera en la cola si no se juega | No. Si no se juega, espera en la cola | Ninguna | — |
| [[d3.4 ¿Vender o guardar\|d3.4]] | Tras [[d3.3 Lucía\|d3.3]], con hierro en el inventario | Condicional: sin hierro la decisión no existe | Ninguna | Libre, sin nodo: vender o guardar el hierro |
| [[d4.1 El pedido\|d4.1]] | Día 4, tras el día 3 | No. Si dejas ir al cliente, el pedido se pierde sin castigo y llegará otro | Ninguna: el pedido es el escenario del Regateo | — |
| [[d4.2 Regatear\|d4.2]] | Tras [[d4.1 El pedido\|d4.1]] | No | Regateo (oferta contra paciencia) | Libre, sin nodo: el mínimo del regateo |
| [[d4.3 Reunir el pedido\|d4.3]] | Tras [[d4.2 Regatear\|d4.2]]. Es una expedición normal; si tiene escena propia, la define ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] (no es escena clave de [[F0-24 Storyboard de las escenas clave del Acto I\|F0-24]]) | Condicional: si dejas ir al cliente, no se juega | Ninguna | — |
| [[d4.4 El café\|d4.4]] | Tras [[d4.3 Reunir el pedido\|d4.3]], de noche, en la casa de Reme | No. Si no vas, la oferta de pagar antes sigue abierta hasta el día 7 | Ninguna | — |
| [[d5.1 La entrega\|d5.1]] | Día 5, con el pedido reunido (plazo de 3 días) | Condicional: sin pedido (se perdió el día 4) no se juega | Ninguna | — |
| [[d5.2 El rumor\|d5.2]] | Tras [[d5.1 La entrega\|d5.1]], en el puesto | No. Si no se juega, espera en la cola | Ninguna | [[Confiar en Lucía con un rumor\|n-i-lucia-rumor]] |
| [[d5.3 El pico de nivel 2\|d5.3]] | Día 5, tarde, si pasas por Teo con 3 hierro. Sin plazo | Opcional (la única). Saltarla no cambia nada: el acto cierra igual | Ninguna obligatoria (opcional: la mejora de una herramienta) | Libre, sin nodo: ahorrar o mejorar |
| [[d5.4 La respuesta de casa\|d5.4]] | De noche, tras [[d5.2 El rumor\|d5.2]], si contaste algo el día 1 | Condicional: con «nada» no llega carta y no se juega | Ninguna | — |
| [[d6.1 Un rumor sin confirmar\|d6.1]] | Día 6, en el puesto. Funciona sea cual sea la decisión del día 5 | No. Si no lees el rumor, el Heraldo del día 7 se explica solo | Confirmar un rumor con la noticia oficial | Libre, sin nodo: vender el hierro ya o esperar al Heraldo |
| [[d6.2 Mañana, el Heraldo\|d6.2]] | Tras [[d6.1 Un rumor sin confirmar\|d6.1]], de noche, en casa | No | Ninguna | — |
| [[d7.1 Primera hora\|d7.1]] | Día 7, a primera hora, antes de la cuota. Si la primera hora se salta, en el primer bloque en que pases por el puesto | No. Si no abres la sección de empleos, la ficha queda en el tablón y cuenta igual | La cuota (el primer contacto con empleados no es mecánica: es una ficha bloqueada) | — |
| [[d7.2 La cuota\|d7.2]] | Se dispara sola al caer la tarde del día 7. Si estás fuera, Reme pasa por el puesto y te ofrece la misma decisión | No. Es la fecha dura: no espera en la cola | La cuota (pagar a tiempo, antes o pedir tiempo) | [[Pagar a Reme antes o después del plazo\|n-i-reme-plazo]] |
| [[d7.3 El sello\|d7.3]] | Tras [[d7.2 La cuota\|d7.2]], de noche, con la cuota atendida y el primer contacto hecho | No | Ninguna | — |
| [[d7.4 El decreto\|d7.4]] | Tras [[d7.3 El sello\|d7.3]]. Es la escena-gancho del acto: no cuenta para el tope de prensa | No | Ninguna | — |

La cola suelta las escenas de una en una y en orden, y nunca dos mecánicas nuevas a la vez (requisito de ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]]). Solo [[d5.3 El pico de nivel 2|d5.3]] es **opcional**. Son **condicionales** (dependen de algo que puede no haber ocurrido) [[d3.4 ¿Vender o guardar|d3.4]] (sin hierro), [[d4.3 Reunir el pedido|d4.3]] (si dejas ir al cliente), [[d5.1 La entrega|d5.1]] (sin pedido) y [[d5.4 La respuesta de casa|d5.4]] (con «nada» en la herencia). La única fecha dura es [[d7.2 La cuota|d7.2]].

### 21.4 Hilos, sombras, props, ramas y responsable

| Escena | Hilos que siembra | Sombra (máximo una) | Props y pantalla del juego | Ramas | Responsable del texto |
|---|---|---|---|---|---|
| [[d1.1 Llegada\|d1.1]] | [[El sorteo oculto de la facción de Reme\|h-sorteo-oculto-de-la-faccion-de-reme]] (el sorteo ocurre antes de la escena) | — | Una maleta. Pantalla: la interfaz del día con los tres bloques y 120 esquirlas | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d1.2 La llave y los papeles\|d1.2]] | [[La firma de la herencia es la del acta\|h-firma-de-la-herencia]], [[Reme traiciona por obligación y acaba siendo la mayor aliada\|h-traicion-de-reme]] | La firma de Anselmo en los papeles | La llave, los papeles con la firma, la caja con el detector de Anselmo. Decorado de la pista del sorteo, sin texto: la lámpara de red, el papel sellado doblado sobre la mesa o el farol apagado. Pantalla: caja de diálogo sobre la casa de Reme | Por variante sorteada (`e-variante-reme`): solo el decorado, sin texto. Sin ramas por dificultad | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d1.3 El libro de deuda\|d1.3]] | [[El abono anónimo a la deuda - el giro, el sobre sin remitente y la carta sin\|h-abono-anonimo]], [[El trato de Anselmo con la Comisión\|h-trato-de-anselmo]], [[El préstamo de Reme a Anselmo «para equipos en La Fosa»\|h-prestamo-de-reme-a-anselmo]], [[La deuda heredada y las cuotas cada 7 días\|h-deuda-del-protagonista]], [[Reme traiciona por obligación y acaba siendo la mayor aliada\|h-traicion-de-reme]] | El abono de «algún vecino bondadoso» | El libro de deuda, con la línea del abono. El decorado de la pista sigue a la vista. Pantalla: el libro de deuda | Por variante sorteada: solo el decorado. Sin ramas por dificultad | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d1.4 Las Galerías\|d1.4]] | [[Anselmo está vivo, enfermo y es cómplice de la Comisión\|h-anselmo-sigue-vivo]] | «Fui amigo de tu tío; lo demás, otro día» (Teo) | El pico prestado, tres menas de carbón. Pantalla: la expedición (escáner y Picado) | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d1.5 El puesto cerrado\|d1.5]] | [[La libreta que termina sin fecha de cierre\|h-libreta-sin-cierre]] | La libreta con su última anotación sin fecha | La llave que abre el puesto, polvo, el cajón de la caja con la libreta. Pantalla: la libreta | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d1.6 La carta\|d1.6]] | [[La lámpara que Anselmo prestó al sobrino y la cinta 1\|h-lampara-y-cinta-1]], [[Vega Mansa y el juramento del padre\|h-vega-mansa-y-el-juramento]], [[La helada tardía y la deuda de la familia con el banco agrario\|h-deuda-del-banco-agrario]] | La lámpara de minero sobre la mesa | La lámpara de minero (no la lámpara de red), papel y pluma. Pantalla: la carta con tres botones | Por decisión: `.todo`, `.parte` y `.nada` (con «nada» no se escribe carta) | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d2.1 El trámite\|d2.1]] | — | — | El sello y la oficina del Inspector. Pantalla: el trámite y su costo | Por género: `.f` en «estimado/a» (Quiroga). Sin dinero: Reme fía la gestión | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d2.2 Surtir los estantes\|d2.2]] | — | — | Los estantes y el saco de carbón de Anselmo en la trastienda. Pantalla: Reponer | Con carbón propio o con el saco de Anselmo | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d2.3 La primera venta\|d2.3]] | — | — | El cartel con el nombre. Pantalla: la tienda abierta (margen por defecto 20 %) y la pantalla del nombre ([[F3-14 Personalización del protagonista\|F3-14]]) | Nombre vacío: «Puesto de {nombre}». Gestión fiada si no alcanza el efectivo | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; la noticia y el rumor del día, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] |
| [[d2.4 Cierre de caja\|d2.4]] | [[La lámpara que Anselmo prestó al sobrino y la cinta 1\|h-lampara-y-cinta-1]] | La cinta 1 | La caja, el cajón con doble fondo y el objeto «Carrete 1» (sin reproducción). Pantalla: el cierre de caja | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d3.1 Perforar\|d3.1]] | — | — | El taladro que presta Teo (no entra en el inventario) y la barra de la herramienta. Pantalla: Perforación | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d3.2 La placa\|d3.2]] | [[Pozo Negro - el derrumbe que marca a todos\|h-pozo-negro]] | — | La placa de Pozo Negro, prop fijo de la boca de las Galerías ([[26 Zonas y edificios\|26]]). Pantalla: caja de diálogo sobre la boca de las Galerías | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d3.3 Lucía\|d3.3]] | [[La Comisión del Éter y el mal del éter\|h-comision-y-mal-del-eter]], [[Lucía y su única lealtad\|h-lealtad-de-lucia]] | «La Comisión del Éter pidió más hierro» (Lucía) | El Teletipo de Lucía. Es el rumor del día. Pantalla: caja de diálogo sobre el puesto | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d3.4 ¿Vender o guardar\|d3.4]] | — | — | La trastienda y el mercado. Teo recoge el taladro al final. Pantalla: vender o guardar | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; la noticia del hierro, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] |
| [[d4.1 El pedido\|d4.1]] | — | — | El tablón de pedidos con la tarjeta del pedido (8 de carbón, plazo de 3 días; cifras en [[F3-32 Doce pedidos de ejemplo con clientes\|F3-32]]). La nota del Heraldo del día con `{nombre}` y `{tienda}`. Pantalla: el tablón de pedidos y caja de diálogo sobre el puesto | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; la tarjeta del pedido, [[F3-32 Doce pedidos de ejemplo con clientes\|F3-32]]; la nota del Heraldo, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] |
| [[d4.2 Regatear\|d4.2]] | — | — | Pantalla: el Regateo | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d4.3 Reunir el pedido\|d4.3]] | — | — | Una expedición normal. Pantalla: la expedición. Ejemplo: el cliente deja un rumor útil (el herrero de la calle Honda) | Si dejas ir al cliente no se juega y el día 5 usa el rumor de reserva | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d4.4 El café\|d4.4]] | [[Pista del Consorcio - la lámpara de red con una «A»\|h-pista-lampara-de-red]], [[Pista del Ministerio - la deferencia de Quiroga\|h-pista-deferencia-de-quiroga]], [[Pista de los Faroleros - el farol vinotinto en la ventana\|h-pista-farol-vinotinto]] (solo el de la variante sorteada) | — | Según la variante sorteada: la lámpara de red con una «A» grabada; Quiroga con el papel sellado; el farol vinotinto encendido. Los otros dos no existen en esa partida. Pantalla: caja de diálogo sobre la casa de Reme | Por variante sorteada (`.consorcio`, `.ministerio`, `.faroleros`) | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d5.1 La entrega\|d5.1]] | — | — | El tablón de pedidos y el cobro. Pantalla: caja de diálogo sobre el puesto | Sin pedido, la escena no se juega | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d5.2 El rumor\|d5.2]] | [[Lucía y su única lealtad\|h-lealtad-de-lucia]] | — | El Teletipo. Lucía da primero su rumor del ferrocarril, aunque luego calles. Pantalla: la decisión con tres botones | Por decisión: `.todo`, `.parte` y `.nada`; `.reserva` si no oíste al cliente | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]], incluidos los tres textos del Teletipo (entero, mitad y reserva) |
| [[d5.3 El pico de nivel 2\|d5.3]] | — | — | El pico de nivel 2 (3 hierro y 480 esquirlas). Sin ventana de tutorial. Pantalla: la oferta de Teo con su «?» | Sin hierro, la mejora espera | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d5.4 La respuesta de casa\|d5.4]] | [[Vega Mansa y el juramento del padre\|h-vega-mansa-y-el-juramento]] | — | La carta de casa. Pantalla: la carta | Por decisión del día 1: `.todo` y `.parte`; `.nada` no se juega | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d6.1 Un rumor sin confirmar\|d6.1]] | — | — | El Teletipo y el tablón con la tarjeta del pedido urgente (opcional). Pantalla: el mercado | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; el rumor del Teletipo, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]]; la tarjeta del pedido urgente, [[F3-32 Doce pedidos de ejemplo con clientes\|F3-32]] |
| [[d6.2 Mañana, el Heraldo\|d6.2]] | — | — | La casa obrera de noche. Pantalla: caja de diálogo sobre la casa | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d7.1 Primera hora\|d7.1]] | — | — | La sección de empleos con la tarjeta fija «Candidato sin nombre» (Minero nivel 1, 70 esquirlas al día, Lealtad «?»), el botón «Contratar» bloqueado y el Heraldo del día. Teo deja el pico si no lo mejoraste. Pantalla: la sección de empleos | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; la confirmación del Heraldo, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] |
| [[d7.2 La cuota\|d7.2]] | [[La deuda heredada y las cuotas cada 7 días\|h-deuda-del-protagonista]], [[Reme traiciona por obligación y acaba siendo la mayor aliada\|h-traicion-de-reme]] | — | El libro de deuda y, según la variante sorteada, la lámpara de red, el papel sellado doblado o el farol vinotinto encendido. Pantalla: la elección de pago | Por decisión: `.antes`, `.plazo` y `.tarde`; por dificultad: `.serie` (Novato e Intermedio) y `.suma` (Difícil y Hardcore); por variante sorteada; visita de Reme | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d7.3 El sello\|d7.3]] | — | — | El sello. La tienda está cerrada y no se abre. Pantalla: caja de diálogo sobre el puesto cerrado | Por género: `.f` en «estimado/a» y «Minera con licencia». Por variante sorteada: Quiroga pregunta por doña Reme (Ministerio) | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] |
| [[d7.4 El decreto\|d7.4]] | — | — | Un voceador en la calle. El decreto no nombra a Montenegro. Pantalla: caja de diálogo sobre la calle | Ninguna | [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]; el titular del decreto, [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] |

Son siete sombras (seis de Anselmo y una de la Comisión), como en la sección 17. Todos los hilos existen en `hilos.json`. Responsables: [[F3-47 Textos del Acto I - guion de los siete días|F3-47]] escribe las escenas; [[F3-31 Diez noticias iniciales y seis eventos del Acto I|F3-31]], la prensa guionizada (con el titular del decreto del día 7); [[F3-47 Textos del Acto I - guion de los siete días|F3-47]] también escribe los tres textos del Teletipo del día 5; [[F3-32 Doce pedidos de ejemplo con clientes|F3-32]], las tarjetas de los pedidos con sus cifras (8, 448 y 729), que no van en las escenas.

### 21.5 Qué textos lleva cada escena

Lo decidido son los **totales por escena** (21.2) y estas piezas: el aviso «Encontraste una cinta», la ficha del candidato con su aviso de bloqueo y las 3 cajas de pagar antes (21.6). El reparto de cajas por hablante, la lista de ayudas y los nombres de los avisos son un **ejemplo orientativo**; lo fija ⏳ [[F3-47 Textos del Acto I - guion de los siete días|F3-47]] al escribir, siempre respetando los totales. Los avisos de esta tabla (salvo los marcados) son ejemplos de qué tipo de aviso lleva la escena.

| Escena | Cajas (reparto orientativo) | Ayudas e interfaz (orientativo) | Cartas y avisos (orientativo) |
|---|---|---|---|
| [[d1.1 Llegada\|d1.1]] | Narrador 4, {nombre} 2 | los tres bloques del día; el efectivo de 120 esquirlas; otras ayudas de la interfaz del primer día (2) | — |
| [[d1.2 La llave y los papeles\|d1.2]] | Reme 6, {nombre} 2, Narrador 2 | — | los papeles de la herencia, con la firma de Anselmo |
| [[d1.3 El libro de deuda\|d1.3]] | Reme 6, {nombre} 3, Narrador 1 | el libro de deuda: capital, cuota y abono; la primera cuota llega el día 7 | la página del libro de deuda |
| [[d1.4 Las Galerías\|d1.4]] | Teo 9, {nombre} 3, Narrador 2 | escanear: tocar la mena y ver los rangos (2); picar: fuerza y precisión (2); el resultado de la primera expedición | — |
| [[d1.5 El puesto cerrado\|d1.5]] | Narrador 4, {nombre} 2 | la libreta en el diario | el primer apunte de la libreta, que manda ir a Quiroga; la última anotación, sin fecha |
| [[d1.6 La carta\|d1.6]] | común 3, `.todo` 1, `.parte` 1, `.nada` 2 | — | la carta a Vega Mansa, `.todo`; la carta a Vega Mansa, `.parte` |
| [[d2.1 El trámite\|d2.1]] | Quiroga 7, {nombre} 3 | la gestión de Quiroga: 240 esquirlas, con la primera venta; el fiado de Reme si no alcanza | — |
| [[d2.2 Surtir los estantes\|d2.2]] | Narrador 3, {nombre} 2 | Reponer: arrastrar la mercancía a los estantes (2); fijar el precio | — |
| [[d2.3 La primera venta\|d2.3]] | Cliente 4, {nombre} 3, Narrador 3 | el margen: precio de lista y cliente medio (2); la pantalla del nombre de la tienda; el cartel con el nombre por defecto | — |
| [[d2.4 Cierre de caja\|d2.4]] | Narrador 4, {nombre} 1 | el cierre de caja | el aviso «Encontraste una cinta» ✅ |
| [[d3.1 Perforar\|d3.1]] | Teo 8, {nombre} 2, Narrador 2 | velocidad contra calor (2); la barra de desgaste de la herramienta (2); el taladro es solo de hoy; el resultado de la expedición de hierro | — |
| [[d3.2 La placa\|d3.2]] | Teo 5, {nombre} 1, Narrador 1 | — | la inscripción de la placa de Pozo Negro |
| [[d3.3 Lucía\|d3.3]] | Lucía 7, {nombre} 3 | — | — |
| [[d3.4 ¿Vender o guardar\|d3.4]] | Narrador 4, {nombre} 3, Teo 1 | guardar cuesta muy poco; el mercado sube con el bloque | — |
| [[d4.1 El pedido\|d4.1]] | Cliente 6, {nombre} 2, Narrador 2 | qué es un pedido de cliente | un aviso de pedido nuevo |
| [[d4.2 Regatear\|d4.2]] | Cliente 4, {nombre} 3, Narrador 1 | oferta contra paciencia (2); el mínimo; el resultado del regateo | — |
| [[d4.3 Reunir el pedido\|d4.3]] | Cliente 3, Narrador 3 | — | un aviso de pedido reunido |
| [[d4.4 El café\|d4.4]] | común 4, `.consorcio` 3, `.ministerio` 4, `.faroleros` 3 | pagar antes está disponible desde hoy | un aviso de que ya se puede pagar antes |
| [[d5.1 La entrega\|d5.1]] | Cliente 4, {nombre} 1, Narrador 1 | — | — |
| [[d5.2 El rumor\|d5.2]] | común 4, `.todo` 3, `.parte` 3, `.nada` 3, `.reserva` 1 | qué pasa con lo que cuentas | — |
| [[d5.3 El pico de nivel 2\|d5.3]] | Teo 4, {nombre} 2 | el «?» de la oferta: qué mejora y cuánto cuesta (2) | un aviso de pico mejorado |
| [[d5.4 La respuesta de casa\|d5.4]] | común 2, `.todo` 4, `.parte` 4 | — | la carta de casa, `.todo`; la carta de casa, `.parte` |
| [[d6.1 Un rumor sin confirmar\|d6.1]] | Narrador 6, {nombre} 2 | qué es SIN CONFIRMAR; el Heraldo de mañana lo confirma o no; el tablón: el pedido urgente es opcional | — |
| [[d6.2 Mañana, el Heraldo\|d6.2]] | Narrador 4, {nombre} 2 | — | un aviso de cierre del día |
| [[d7.1 Primera hora\|d7.1]] | Teo 6, Narrador 4, {nombre} 2 | la ficha del candidato ✅; «Contratar» bloqueado y su motivo ✅; el «?» de la ficha, sin el costo de la mejora; el libro de deuda marca «hoy» | — |
| [[d7.2 La cuota\|d7.2]] | común 3, `.antes` (agradecimiento) 1, `.plazo` 2, `.tarde` por dificultad, `.serie` y `.suma` 4, visita de Reme al puesto 2, prórroga automática sin respuesta 1, ecos del sorteo 3, cierre 2 | la elección de pago, con {cuota}; qué pasa si pides tiempo | un aviso de cuota atendida; un aviso de cuota anotada con recargo |
| [[d7.3 El sello\|d7.3]] | Quiroga 5, eco del Ministerio 1, {nombre} 2 | el Acto I se cierra: licencia sellada | el sello «Minero con licencia» |
| [[d7.4 El decreto\|d7.4]] | Voceador 3, Narrador 2, {nombre} 1 | — | — |

En las cajas, «común» es lo que se dice en todas las ramas y cada sufijo es la variante que se suma. Las cifras suman exactamente la columna C de la tabla maestra. Con ✅ van las piezas decididas por el autor.

### 21.6 La interacción de pagar antes

No es una escena de `dN.M` y **no cuenta entre las 28**: es una interacción corta que se suma a los textos (decisión del autor, 2026-10-16).

| Campo | Contenido |
|---|---|
| Identificador | `pa`, con las cajas `pa.c01` a `pa.c03` (3 cajas; sin ayudas ni cartas). Las 3 cajas están decididas; los identificadores son una convención propuesta que [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] y [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] pueden renombrar |
| Lugar y personajes | [[Casa de Reme\|ed-vb-reme]], «gastar: cuotas de la deuda» ([[26 Zonas y edificios\|26]]); `reme` y `protagonista` |
| Disparador | Entrar en casa de Reme desde el día 4 con la cuota en caja. Solo es realista los días 6 y 7. Es opcional y no pasa por la cola |
| Botón | El de la salida «antes» de [[Pagar a Reme antes o después del plazo\|n-i-reme-plazo]]: [[Pagar a Reme antes o después del plazo - antes\|n-i-reme-plazo.b1]], «Pagar antes del plazo». Salir sin pagar no lleva botón |
| Efecto | Fija [[Bandera pago reme\|f-pago-reme]] = `antes`, deja la cuota en 900 y baja el interés 1 pp, del 4 % al 3 % mensual ([[28 Números base de la economía\|28]], sección 7.2) |
| Después | [[d7.2 La cuota\|d7.2]] pasa a una línea de agradecimiento (identificador propuesto `d7.2.c04.antes`, renombrable por [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] y [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]) |
| Líneas de ejemplo | **Reme:** «Si me adelantas la cuota, te rebajo un puntito, criatura.» · **Reme:** «Hecho. Quedan {cuota} esquirlas y un puntito menos de interés.» |
| Responsables | Interacción: ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]]. Texto: ⏳ [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]]. No cambia `world.json` ni el simulador |

### 21.7 Variables

El conjunto es **cerrado**: ningún texto usa otras llaves.

| Variable | Qué es | Dónde sale |
|---|---|---|
| `{nombre}` | El nombre del protagonista | Cartas y diálogos; la prensa lo cita en tercera persona y sin cargo ([[18 Biblia narrativa\|18]], 1.10) |
| `{tienda}` | El nombre de la tienda | El cartel ([[d2.3 La primera venta\|d2.3]]), la tarjeta del pedido del día 4 y la nota del Heraldo del día 4. Por defecto «Puesto de {nombre}», guardado vacío y resuelto al mostrar |
| `{cuota}` | El importe vigente de la cuota en esquirlas: 960, o 900 si pagaste antes | [[d7.2 La cuota\|d7.2]] y `pa` |
| `{recargo}` | El importe del recargo en esquirlas, no el porcentaje: 58 en Intermedio (38, 115 y 173 en Novato, Difícil y Hardcore) | [[d7.2 La cuota\|d7.2]] (`.tarde`) |

- Los **porcentajes** (4, 6, 12 y 18 %) salen de los datos en la interfaz, no del diálogo.
- Las **cifras de los pedidos** (8, 448 y 729) van en las tarjetas de ⏳ [[F3-32 Doce pedidos de ejemplo con clientes|F3-32]], no en las escenas de [[F3-47 Textos del Acto I - guion de los siete días|F3-47]].
- Los **números se formatean según el idioma** ⏳ [[F1-20 Flujo de traducción - extracción, traducción asistida por|F1-20]]. El largo máximo del nombre de la tienda, ⏳ [[F1-18 Fuente pixel con caracteres latinos extendidos y plan de|F1-18]].

### 21.8 Botones de las tres decisiones pequeñas

Los textos de `decisions.json` son descripciones para el equipo y pasan de 28 caracteres ([[18 Biblia narrativa|18]], 1.9); estos son los botones, de 28 caracteres como máximo. Las opciones y las banderas son las de `decisions.json` y [[23 Árbol de decisiones y consecuencias|23]], sin cambios.

| Botón | Opción | Texto del botón | Caracteres | Fija |
|---|---|---|---|---|
| [[Cómo cuentas la herencia a tu familia - todo\|n-i-herencia.b1]] | `todo` | «Contarles todo» | 14 | [[Bandera familia\|f-familia]] |
| [[Cómo cuentas la herencia a tu familia - parte\|n-i-herencia.b2]] | `parte` | «Solo lo del puesto» | 18 | [[Bandera familia\|f-familia]] |
| [[Cómo cuentas la herencia a tu familia - nada\|n-i-herencia.b3]] | `nada` | «No decir nada todavía» | 21 | [[Bandera familia\|f-familia]] |
| [[Confiar en Lucía con un rumor - contar\|n-i-lucia-rumor.b1]] | `contar` | «Contárselo entero» | 17 | [[Medidor Lucía\|m-lucia]] |
| [[Confiar en Lucía con un rumor - mitad\|n-i-lucia-rumor.b2]] | `mitad` | «Contarle la mitad» | 17 | [[Medidor Lucía\|m-lucia]] |
| [[Confiar en Lucía con un rumor - callar\|n-i-lucia-rumor.b3]] | `callar` | «No contarle nada» | 16 | [[Medidor Lucía\|m-lucia]] |
| [[Pagar a Reme antes o después del plazo - antes\|n-i-reme-plazo.b1]] | `antes` | «Pagar antes del plazo» | 21 | [[Bandera pago reme\|f-pago-reme]] |
| [[Pagar a Reme antes o después del plazo - plazo\|n-i-reme-plazo.b2]] | `plazo` | «Pagar justo en el plazo» | 23 | [[Bandera pago reme\|f-pago-reme]] |
| [[Pagar a Reme antes o después del plazo - tarde\|n-i-reme-plazo.b3]] | `tarde` | «Pedir una semana más» | 20 | [[Bandera pago reme\|f-pago-reme]] |

Las ramas del texto usan `.todo`, `.parte` y `.nada` para la herencia y el rumor de Lucía (contar, mitad y callar) y `.antes`, `.plazo` y `.tarde` para la cuota.

### 21.9 Qué toma cada tarea de esta sección

| Tarea | Toma |
|---|---|
| ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado\|F3-16]] | Las 28 escenas con bloque, peso, disparador, cola, ramas y props (21.2 a 21.4), la interacción de pagar antes, la visita de Reme al puesto, el taladro del día 3, la placa de Pozo Negro, la cinta 1 mínima, el papel sellado y la ficha del candidato |
| ⏳ [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] | Los identificadores y la tabla maestra (21.1, 21.2 y 21.5), las variables (21.7), los botones (21.8) y los tres textos del Teletipo del día 5 |
| ⏳ [[F3-31 Diez noticias iniciales y seis eventos del Acto I\|F3-31]] y ⏳ [[F3-32 Doce pedidos de ejemplo con clientes\|F3-32]] | La prensa guionizada (con el titular del decreto) y las tarjetas de los pedidos, que no entran en [[F3-47 Textos del Acto I - guion de los siete días\|F3-47]] (21.4) |
| ⏳ [[F0-24 Storyboard de las escenas clave del Acto I\|F0-24]] | Las siete escenas clave con lugar, personajes, props, pantalla, línea de ejemplo y variantes (secciones 4 a 10 y 21.4) |
| ⏳ [[F1-20 Flujo de traducción - extracción, traducción asistida por\|F1-20]] | Los términos de la sección 20 |

---

## Fuente

`studio/docs/27-guion-del-acto-i.md:560`
