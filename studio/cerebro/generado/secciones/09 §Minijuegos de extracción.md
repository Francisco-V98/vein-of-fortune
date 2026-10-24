---
id: "doc-09-minijuegos-de-extraccion"
tipo: "seccion"
title: "Minijuegos de extracción ✅"
aliases: ["doc-09-minijuegos-de-extraccion"]
documento: "[[09 Minijuegos]]"
limpieza: 80
abiertos: 1
espera: 5
aplazado_a: ["[[F2-14 Picado (fuerza y precisión)]]", "[[F2-15 Perforación (velocidad y calor)]]", "[[F4-44 Cincelado - implementación y variante con mando]]", "[[F4-46 Cribado - implementación y variante con mando]]", "[[F4-48 Detonación - implementación y variante con mando]]"]
estado: "con-abiertos"
anterior: "[[09 §Automatización de minijuegos (a probar en prototipo)]]"
siguiente: "[[09 §Escáner]]"
arriba: "[[09 Minijuegos]]"
fuente: "studio/docs/09-minijuegos.md:42"
generado: true
---

# Minijuegos de extracción ✅

> Estado: confirmados los nombres, la herramienta y el acto de entrada de cada minijuego (registro del mundo world.json y glosario, 18…

← [[09 §Automatización de minijuegos (a probar en prototipo)]] · [[09 Minijuegos|↑ 09]] · [[09 §Escáner]] →

**Estado:** confirmados los nombres, la herramienta y el acto de entrada de cada minijuego (registro del mundo `world.json` y glosario, [[18 Biblia narrativa|18]], 6.10); la columna «Cómo se juega» se fija al construir cada uno (abajo).

| # | Minijuego | Herramienta | Parámetros | Cómo se juega |
|---|---|---|---|---|
| 1 | **Picado** | Pico | Fuerza ↔ Precisión | Mantienes pulsado para cargar fuerza mientras un marcador oscila sobre la mena. Sueltas cuando ambos están en zona. Las menas duras necesitan 2–3 golpes. ✅ Sirve para carbón, hierro, cobre, plata y oro (decisión del autor, 2026-10-16) |
| 2 | **Perforación** | Taladro | Velocidad ↔ Calor | Mantener pulsado avanza más rápido pero sube el calor; soltar enfría. Llegar al fondo sin sobrecalentar |
| 3 | **Cincelado** | Cincel | Precisión pura | Trazar con el cursor, con el botón izquierdo pulsado (o con el stick del mando), una línea sobre la gema sin salirse del margen. Un error agrieta la pieza y pierdes fragmentos 🟡 (con ratón; el dedo queda para la variante móvil) |
| 4 | **Cribado** | Criba | Inclinación ↔ Caudal | Dos deslizadores que mantienen un indicador de flotación en zona mientras la carga cambia |
| 5 | **Detonación** | Explosivo | Potencia ↔ Ubicación | Ubicar la carga en la fisura y elegir potencia. Mucho rompe la mena; poco la deja atascada. Alto rendimiento, alto riesgo (puede provocar derrumbes). El explosivo es consumible ([[02 Extracción\|02]]) |

⏳ [[F2-14 Picado (fuerza y precisión)|F2-14]] y ⏳ [[F2-15 Perforación (velocidad y calor)|F2-15]] La implementación de Picado y Perforación; ⏳ [[F4-44 Cincelado - implementación y variante con mando|F4-44]] la del Cincelado, ⏳ [[F4-46 Cribado - implementación y variante con mando|F4-46]] la del Cribado y ⏳ [[F4-48 Detonación - implementación y variante con mando|F4-48]] la de la Detonación.

### Asignación a minerales ✅

Coincide con el registro del mundo y con los minijuegos de cada boca de mina ([[26 Zonas y edificios|26]]), salvo la ampliación del **Picado** a cobre, plata y oro (decisión del autor, 2026-10-16). La **Detonación** también se juega en las **Galerías del Hollín** (decisión del autor, 2026-10-15), con el carbón.

| Mineral | Minijuego principal |
|---|---|
| Carbón | Picado / Detonación |
| Hierro | Picado / Perforación |
| Cobre | Picado / Perforación |
| Salitre | Cribado |
| Plata | Picado / Perforación / Cribado |
| Oro | Picado / Cribado (aluvial) / Perforación (veta) |
| Cuarzo | Cincelado |
| Esmeralda | Cincelado |
| Diamante | Cincelado de alto nivel |
| Aetherita | **Contención** (especial) |

### Contención (Aetherita) ✅

Minijuego propio para el final del juego: mantener una energía inestable entre **presión** y **resonancia**. Cada extracción acumula **exposición**, que enferma al jugador («mal del éter») y baja temporalmente sus stats. **El mal del éter no mata** ([[04 Progresión y meta|04]]). Introduce el secreto de la Aetherita antes de revelarlo y es una decisión real: ¿vale la pena extraer más? (Ver [[08 Historia y personaje|08]].) ✅ Lo extraído se vende por la Comisión del Éter, un canal legal con tope diario, y solo en encargos especiales raros por el mercado negro, así que la decisión de extraer más no se resuelve vendiendo sin límite ([[03 Comercio y mercado|03]], [[28 Números base de la economía|28]]).

## Fuente

`studio/docs/09-minijuegos.md:42`
