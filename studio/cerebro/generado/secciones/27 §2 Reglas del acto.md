---
id: "doc-27-s02"
tipo: "seccion"
title: "2 · Reglas del acto ✅"
aliases: ["doc-27-s02"]
documento: "[[27 Guion del Acto I, día a día]]"
limpieza: 100
abiertos: 0
espera: 7
aplazado_a: ["[[F0-78 Diseñar el diario, la cola de historia y la misión de]]", "[[F2-02 Ciclo de 3 bloques y avance del día]]", "[[F3-10 Peligros ambientales de la zona 1 y tareas de peligro]]", "[[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado]]", "[[F3-22 Selector de dificultad con parámetros]]"]
estado: "con-aplazados"
anterior: "[[27 §1 Decisiones del autor]]"
siguiente: "[[27 §3 Los siete días de un vistazo]]"
arriba: "[[27 Guion del Acto I, día a día]]"
fuente: "studio/docs/27-guion-del-acto-i.md:66"
generado: true
---

# 2 · Reglas del acto ✅

> Las reglas vienen de la sección 1 o de documentos ya confirmados; cómo se aplican día a día y los valores por dificultad los confirmó el…

← [[27 §1 Decisiones del autor]] · [[27 Guion del Acto I, día a día|↑ 27]] · [[27 §3 Los siete días de un vistazo]] →

**Estado:** cerrada. Las reglas vienen de la sección 1 o de documentos ya confirmados; cómo se aplican día a día y los valores por dificultad los confirmó el autor en la pasada de cierre del 2026-10-16 ([[F0-86 Pasada de cierre - guion del Acto I (27)|F0-86]]). Los valores finos por dificultad los fija ⏳ [[F3-22 Selector de dificultad con parámetros|F3-22]].

### 2.1 Bloques, escenas y cola

Todo lo de esta tabla viene de la sección 1 o de documentos ya confirmados.

| Regla |
|---|
| Cada día tiene tres bloques: mañana, tarde y noche. El mercado se mueve una vez por bloque ([[03 Comercio y mercado\|03]]) ✅ |
| Viajar no gasta bloque pero cuesta dinero (entre 42 y 210 esquirlas fuera del Acto I; nada en el Acto I, donde todo ocurre en Villa Brasa) y ver zonas es gratis; minar y abrir la tienda cuestan un bloque completo; los trámites, las visitas y las conversaciones cuestan nada, medio bloque o un bloque según su peso ([[01 Core loop y ciclo del día\|01]]) ✅ |
| **Ninguna venta cae en la noche**: la tienda no se abre de noche ([[01 Core loop y ciclo del día\|01]]). Las escenas de noche son de casa, de cierre o de visita, y ninguna abre el modo tienda ✅ |
| Las escenas se disparan por evento; si no ocurren, pasan a la cola (⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de\|F0-78]]) ✅ |
| Solo la cuota tiene fecha: el día 7 llega aunque las escenas anteriores no se hayan jugado ✅ |
| Cada día enseña una mecánica nueva como máximo ✅ |
| Los días 5 y 6 son de respiro: la mejora de la herramienta y el pedido urgente son opcionales, con ayuda a pedido y sin tutorial forzado. Si el jugador los salta, el acto cierra igual ✅ |
| Los medios hablan del protagonista en tercera persona con `{nombre}` ([[18 Biblia narrativa\|18]], 1.10) ✅ |
| **Tope de prensa:** como máximo 1 noticia y 1 rumor por día ([[01 Core loop y ciclo del día\|01]], [[03 Comercio y mercado\|03]]). El decreto del día 7 es una escena-gancho y no cuenta ✅ |
| **Reponer** (día 2): arrastrar la mercancía a los estantes y fijar los precios; es más gestión que minijuego ([[03 Comercio y mercado\|03]], [[09 Minijuegos\|09]]) ✅ |
| **El legado no cambia los siete días:** son iguales para todos, con o sin legado ([[04 Progresión y meta\|04]]) ✅ |
| **Hardcore no tiene derrota en los siete días:** solo mata un encuentro de riesgo o un jefe y ninguno aparece en el Acto I ([[02 Extracción\|02]], [[04 Progresión y meta\|04]]) ✅ |
| **Margen por defecto de la tienda:** precio de lista = valor justo × 1,20; el cliente medio paga × 1,15 ([[28 Números base de la economía\|28]]) ✅ |
| **Este guion es la referencia del simulador** ✅ (`act1_script` de `world.json`). Que `store_days` sea `[2, 4, 7]` no impide vender los días 3, 5 y 6 ✅ |
| Reme tutea y dice «criatura»; Quiroga trata de usted; el narrador tutea ([[18 Biblia narrativa\|18]], 1.2) ✅ |

**Cómo se aplican ✅.**

- Una expedición o abrir el puesto gasta un bloque completo; viajar (que cuesta dinero, aunque no en el Acto I), leer noticias, mirar el mercado y organizar el inventario no gastan ninguno ([[01 Core loop y ciclo del día|01]]). Cada bloque tiene una actividad principal y las conversaciones cortas del barrio caben dentro del bloque en que ocurren. El peso de cada escena (0, medio o 1) lo asigna ⏳ [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado|F3-16]] y el mecanismo lo define ⏳ [[F2-02 Ciclo de 3 bloques y avance del día|F2-02]]; minar y abrir la tienda valen 1 (sección 21.2). Las escenas guionizadas no quitan bloques salvo la expedición y la tienda: por ejemplo, [[d1.5 El puesto cerrado|d1.5]] y [[d1.6 La carta|d1.6]] no suman dos bloques.
- Cada día cabe en sus tres bloques con la regla de arriba: las ventas y los pedidos caen en la mañana o en la tarde, y la noche queda para las escenas.
- El día que se indica en cada escena es el **esperado**. Si el jugador va más rápido, la escena se adelanta solo hasta donde cumple sus requisitos; si va más lento, espera en la cola. La cola suelta las escenas de una en una y en orden, para que nunca se enseñen dos mecánicas nuevas a la vez; esa invariante es un requisito de ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]], que diseña la cola.
- Cada día tiene **como máximo una decisión principal**; si hay otra (la del nombre de la tienda el día 2 o [[Confiar en Lucía con un rumor|n-i-lucia-rumor]] el día 5), es **menor** y cae dentro del mismo día. Los días 5 y 6 no obligan a ninguna principal: ahorrar o mejorar y vender ya o esperar al Heraldo son elecciones libres, sin nodo del árbol.
- **Ayuda a pedido.** Lo opcional (la mejora, el pedido urgente) no abre ventanas de tutorial: tiene un botón «?» y una frase de Teo que el jugador lee si quiere.
- Una escena lleva una sombra como máximo (regla de [[18 Biblia narrativa|18]], 1.4). Sombra es un elemento que deja una pregunta sobre Anselmo o la Comisión; las pistas del sorteo no son sombras (sección 13).
- El guion usa además un pedido de cliente estándar (día 4) y uno urgente con prima (día 6, **opcional**, sin escena), que son los contratos de [[03 Comercio y mercado|03]] con otro nombre: en el Acto I se llaman «pedidos de cliente» ✅. El urgente es una variante del mismo pedido, no una mecánica nueva.

### 2.2 Qué se abre y qué queda fuera

| Dentro del Acto I | Fuera del Acto I |
|---|---|
| Villa Brasa y las **Galerías del Hollín**; **carbón** y **hierro** ✅ | Taller, Refinado y Acero (el taller abre en el II) ✅ |
| Escáner instantáneo, **Picado**, **Perforación** y **Regateo** ✅ | Herrería, quioscos y sede de la Unión (V1, [[26 Zonas y edificios\|26]]) ✅ |
| Tienda modesta (con Reponer: arrastrar la mercancía a los estantes y fijar precios) y herramientas de nivel 1 y 2; el taladro solo lo presta Teo el día 3 ✅ | Cañón Ferroso y las demás zonas ✅ |
| Información básica (precio y flecha), la noticia oficial del Heraldo (como máximo 1 noticia y 1 rumor del Teletipo por día) y la sección de empleos ✅ | Contratar de verdad (se abre al cerrar el Acto I y exige una mejora de la tienda), mercado negro y vigilancia (Acto II) ✅ |
| | Capas 3 y 4 de información y la Aetherita ✅ |
| | La Voz del Hollín, la prensa con sesgos y el «cruzar fuentes»: desde el Acto II ✅ |
| | Contratos (en el Acto I son «pedidos de cliente») ✅ |
| | Peligros ambientales (gas y derrumbes): desde el Acto II ✅ ⏳ [[F3-10 Peligros ambientales de la zona 1 y tareas de peligro\|F3-10]] |

### 2.3 Dificultades

El selector es de cuatro niveles: Novato, Intermedio, Difícil y Hardcore ✅. Los siete días, las escenas y los textos son los mismos en las cuatro.

| Parámetro | Novato | Intermedio | Difícil | Hardcore |
|---|---|---|---|---|
| Efectivo, detector y pico del inicio | Los mismos ✅ | Los mismos ✅ | Los mismos ✅ | Los mismos ✅ |
| Pérdida grave y muerte hasta el día 2 | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ |
| Pérdida grave y muerte el día 3 | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ | Ninguna ✅ |
| Peligros ambientales en los siete días | Ninguno ✅ | Ninguno ✅ | Ninguno ✅ | Ninguno ✅ |
| Cuota atrasada del día 7 | Desplaza la serie, con recargo ✅ | Desplaza la serie, con recargo ✅ | Se suma a la del día 14, con recargo mayor ✅ | Se suma a la del día 14, con recargo mayor ✅ |

**Valores por dificultad ✅.** Desde el día 4 la pérdida es la normal de la dificultad: el castigo (desgaste, multas, pérdida de carga con tope del 75 %, costo de contratar, herida de empleados) se multiplica por 0,7 · 1 · 1,4 · 2 y el ruido de los precios por 0,8 · 1 · 1,25 · 1,5 en Novato, Intermedio, Difícil y Hardcore ([[04 Progresión y meta|04]], `world.json`). **En Hardcore no hay derrota en los siete días**: solo mata un encuentro de riesgo o un jefe y ninguno aparece en el Acto I ([[02 Extracción|02]], [[04 Progresión y meta|04]]). Las tres noticias guionizadas suben o bajan en el mismo sentido en las cuatro dificultades y solo cambia el tamaño. El efectivo inicial, la cuota, el capital, el interés y los precios base no cambian con la dificultad. Las cifras finas ⏳ [[F3-22 Selector de dificultad con parámetros|F3-22]].

---

## Fuente

`studio/docs/27-guion-del-acto-i.md:66`
