---
id: "doc-04-dificultad"
tipo: "seccion"
title: "Dificultad ✅"
aliases: ["doc-04-dificultad"]
documento: "[[04 Progresión y meta]]"
limpieza: 100
abiertos: 0
espera: 3
aplazado_a: ["[[F3-22 Selector de dificultad con parámetros]]", "[[F4-120 Ajuste fino de parámetros por dificultad]]"]
estado: "con-aplazados"
anterior: "[[04 §Logros]]"
siguiente: "[[04 §Hardcore - permadeath]]"
arriba: "[[04 Progresión y meta]]"
fuente: "studio/docs/04-progresion-y-meta.md:179"
generado: true
---

# Dificultad ✅

> Estado: confirmado el selector, que se implementa como parámetros y no como contenido distinto (los siete días del Acto I son los mismos en…

← [[04 §Logros]] · [[04 Progresión y meta|↑ 04]] · [[04 §Hardcore - permadeath]] →

**Estado:** confirmado el selector, que se implementa como parámetros y no como contenido distinto (los siete días del Acto I son los mismos en las cuatro, [[27 Guion del Acto I, día a día|27]], 2.3) y cuánto abarca la pérdida; los valores ⏳ [[F3-22 Selector de dificultad con parámetros|F3-22]].

✅ Selector al inicio: **Novato, Intermedio, Difícil, Hardcore**.

Se implementa como un conjunto de parámetros, no como contenido distinto:

| Parámetro | Novato → Hardcore |
|---|---|
| Volatilidad del mercado | Baja → alta |
| Información visible | Más → menos |
| Desgaste de herramientas | Lento → rápido |
| Pérdida ✅ | Pequeña → grande. Suma la pérdida al perder un encuentro, la **cuota atrasada**, los **eventos** y las **multas** |
| Margen de error en minijuegos | Amplio → estrecho |
| Probabilidades de aparición | Más generosas → más tacañas |

✅ Regla de escala: el **castigo** se multiplica por **0,7 · 1 · 1,4 · 2** (desgaste, multas, pérdida de carga con tope del 75 %, costo de contratar, ruido de los precios ×0,8 · 1 · 1,25 · 1,5 y herida de empleados), y la **ayuda** por 1,15 · 1 · 0,9 · 0,8 (probabilidad de minerales raros). La carga que se pierde es del **25 %** en Novato, **35 %** en Intermedio, **49 %** en Difícil y **70 %** en Hardcore. No cambian con la dificultad el efectivo inicial, la cuota, el capital, el interés ni los precios base; solo el recargo por atraso (4 · 6 · 12 · 18 % por semana) y la mora ([[28 Números base de la economía|28]]). ⏳ [[F3-22 Selector de dificultad con parámetros|F3-22]] Los valores finos por dificultad y ⏳ [[F4-120 Ajuste fino de parámetros por dificultad|F4-120]] su ajuste fino.

## Fuente

`studio/docs/04-progresion-y-meta.md:179`
