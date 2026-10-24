---
id: "doc-02-herramientas"
tipo: "seccion"
title: "Herramientas ✅"
aliases: ["doc-02-herramientas"]
documento: "[[02 Extracción]]"
limpieza: 100
abiertos: 0
espera: 3
aplazado_a: ["[[F4-114 Proveedores desbloqueables por estatus]]", "[[F4-213 Licencias - sello, revisión, ampliación y suspensión]]", "[[F4-60 Ajuste de los 5 niveles de cada herramienta]]"]
estado: "con-aplazados"
anterior: "[[02 §Menas y detector de probabilidades]]"
siguiente: "[[02 §Fallos y daño a la mena]]"
arriba: "[[02 Extracción]]"
fuente: "studio/docs/02-extraccion.md:69"
generado: true
---

# Herramientas ✅

> Estilo Minecraft:

← [[02 §Menas y detector de probabilidades]] · [[02 Extracción|↑ 02]] · [[02 §Fallos y daño a la mena]] →

✅ Estilo Minecraft:

- Las herramientas **se desgastan** con el uso.
- Cada herramienta sirve para ciertos materiales; los materiales de mayor nivel requieren herramientas mejores.
- Mejor herramienta → minijuego más fácil / zona óptima más amplia / más probabilidad de obtención.

✅ **Los niveles de herramienta por acto son una guía, no un tope** (decisión del autor, 2026-10-15): Acto I 1–2 · II 2–3 · III 3–4 · IV 4–5 indican el nivel con el que se espera llegar a cada acto; si un jugador compra antes un nivel que se lo puede permitir, puede. Si el simulador ([[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]]) ve que el optimizador llega demasiado pronto a un nivel, propone subir el costo de ese nivel y el autor decide.

✅ Lo que mejora el jugador al ir comprando: más resistencia, más almacenamiento (carga), mejor minado, mejor información (escáner). Son los cuatro componentes de **cada nivel**: un nivel de herramienta es un paquete que mejora las cuatro cosas a la vez, no cuatro escaleras separadas ✅.

### Modelo de herramientas ✅

Decisión del autor (2026-10-15):

| Pieza | Regla |
|---|---|
| Tipos | **5 tipos**: pico, taladro, cincel, criba y explosivo (los de [[09 Minijuegos\|09]]); cada uno cubre un tipo de minijuego ✅ |
| Niveles | **5 niveles por herramienta**, y los minerales de mayor nivel exigen herramientas de mayor nivel ✅ (a revisar si en el prototipo hace falta ampliar, ⏳ [[F4-60 Ajuste de los 5 niveles de cada herramienta\|F4-60]]) |
| Explosivo | Es **consumible**: se gasta con cada uso en lugar de desgastarse ✅ |
| Reparar | Cuesta **dinero y materiales** ✅. Es otro sumidero de dinero. Los materiales son **1 repuesto por cada 20 puntos de desgaste**: de hierro en los niveles 1–2, de cobre en el 3, de plata en el 4 y de oro en el 5 ✅ |
| Mejorar | Requiere **minerales específicos** (ej. hierro para el pico, diamante para el cincel, cuarzo para mejorar el detector). Así los minerales tienen utilidad real ✅ |
| Qué mineral | El mineral que sube una herramienta al nivel *k* se extrae con una herramienta de nivel *k*−1 ✅. Así nunca hace falta lo que aún no se puede sacar |
| Facciones | Mejorar es **neutral entre facciones** ✅ |
| Requisitos | Los niveles altos requieren **estatus, licencia o contacto** (influencia), no solo dinero ✅ (⏳ [[F4-114 Proveedores desbloqueables por estatus\|F4-114]] proveedores por estatus, ⏳ [[F4-213 Licencias - sello, revisión, ampliación y suspensión\|F4-213]] licencias) |

- ✅ **Costo de mejorar** (un costo en dinero y un mineral por nivel; las cifras del pico, y los otros tipos cuestan ×1,1 la criba, ×1,25 el taladro y ×1,5 el cincel): subir al nivel 2 cuesta **480 esquirlas**, al 3 **1 100**, al 4 **13 000** y al 5 **40 000**, más el mineral de cada subida (3 hierro para el nivel 2, cobre para el 3, plata para el 4 y esmeralda para el 5 en el pico). La mejor mejora de cada nivel se paga en pocas expediciones: 1,0 en el nivel 2 (el pico a 480 se paga en 1,04), 3,4 en el 3, 7,1 en el 4 y 3,2 en el 5 ([[28 Números base de la economía|28]] §5.2). El detalle por tipo y mineral está en [[28 Números base de la economía|28]].
- ✅ **Costo de reparar:** dinero por punto de desgaste según el nivel (3 · 5 · 20 · 85 · 240 esquirlas, por el factor del tipo) más los repuestos de arriba; en total, **7–9 % del valor bruto de una expedición** en todos los actos.
- ✅ **Explosivo:** consumible con **5 potencias** (cada una sirve para los minerales de un nivel) que cuestan **15 · 50 · 130 · 330 · 900 esquirlas**; entra en el Acto III. El **detector** se mejora aparte con cuarzo ([[28 Números base de la economía|28]]).

## Fuente

`studio/docs/02-extraccion.md:69`
