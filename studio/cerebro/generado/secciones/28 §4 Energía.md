---
id: "doc-28-s04"
tipo: "seccion"
title: "4 · Energía ✅"
aliases: ["doc-28-s04"]
documento: "[[28 Números base de la economía]]"
limpieza: 50
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[28 §3 Los diez minerales]]"
siguiente: "[[28 §5 Herramientas]]"
arriba: "[[28 Números base de la economía]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:215"
generado: true
---

# 4 · Energía ✅

> Comprobación del arranque del guion: con 28 de energía, el carbón (8) da 3 menas y el hierro (10) da 2: «2 a 3 menas». Una expedición de…

← [[28 §3 Los diez minerales]] · [[28 Números base de la economía|↑ 28]] · [[28 §5 Herramientas]] →

| Concepto | Valor |
|---|---|
| **Aguante base** (energía máxima por expedición; se rellena entera al empezar) | **28** (decisión del autor, 2026-10-16) |
| Objetivo por acto (curva de [[F3-11 Stats por uso e hitos (5 stats)\|F3-11]]) | I: 28–30 · II: 40 · III: 62 · IV: 80. 🟡 La curva sube linealmente desde el valor del acto anterior y llega al objetivo al **70 % del acto** (`ramp_fraction_of_act`) |
| Casa mejor (sube un poco la energía inicial) | **+2 por nivel de casa** (casas 1 a 4: +2, +4, +6, +8) |
| Menas por expedición | `floor(Aguante / (energía de la mena × multiplicador de herramienta))` |
| Multiplicador de energía por nivel de herramienta | 1,00 · 0,90 · 0,80 · 0,70 · 0,60 |
| Expedición profunda | **energía ×1,8 y carga ×1,5** (cuesta 2 bloques; rinde ≈ 0,9 de un bloque normal por bloque, compensado por la mena más valiosa) |
| Energía en 0 | vuelves con **carga parcial**; nunca se toca el almacén |
| **Carga que se pierde** (Intermedio) | **35 %** de las unidades de esa expedición (al azar entre las que llevas) |
| Regla por dificultad | `pérdida = min(75 %, 35 % × f)` con f = 0,7 · 1 · 1,4 · 2 → **Novato 25 % · Intermedio 35 % · Difícil 49 % · Hardcore 70 %** |
| Objeto de seguro ([[F3-09 Encuentros por eventos con decisión\|F3-09]]) | reduce la pérdida a la mitad; precio ≈ 6 % del valor medio de una expedición de su acto |

Comprobación del arranque del guion: con 28 de energía, el carbón (8) da 3 menas y el hierro (10) da 2: «2 a 3 menas». Una expedición de carbón del Acto I vale ≈ 255 esquirlas y una de hierro ≈ 305, con resultados medios.

**Consumibles de recarga de energía y otros ✅:** son una versión futura, mucho después de la V1, sin cifra; viven en la tabla de evolutivos de [[06 Roadmap, ideas futuras y pendientes|06]].

---

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:215`
