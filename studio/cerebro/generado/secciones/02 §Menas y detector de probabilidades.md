---
id: "doc-02-menas-y-detector-de-probabilidades"
tipo: "seccion"
title: "Menas y detector de probabilidades ✅"
aliases: ["doc-02-menas-y-detector-de-probabilidades"]
documento: "[[02 Extracción]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[02 §Zonas]]"
siguiente: "[[02 §Herramientas]]"
arriba: "[[02 Extracción]]"
fuente: "studio/docs/02-extraccion.md:52"
generado: true
---

# Menas y detector de probabilidades ✅

> Cada mena tiene una composición con probabilidades (ej. 30 % oro, 3 % diamante, 50 % carbón). Un detector muestra esas probabilidades y el…

← [[02 §Zonas]] · [[02 Extracción|↑ 02]] · [[02 §Herramientas]] →

✅ Cada mena tiene una composición con probabilidades (ej. 30 % oro, 3 % diamante, 50 % carbón). Un **detector** muestra esas probabilidades y el jugador decide si le conviene extraerla o buscar otra, sabiendo que gasta energía y desgasta herramientas.

✅ El detector muestra **rangos** (ej. «oro: 20–40 %») y no valores exactos. El **Ojo** y la herramienta determinan qué tan estrechos son ([[04 Progresión y meta|04]], [[09 Minijuegos|09]]); la precisión mejora con mejores escáneres → la información es progresión.

✅ El protagonista empieza con un **detector básico heredado de Anselmo**. No depende del cuarzo: el cuarzo solo lo mejora más adelante.

✅ Las probabilidades de aparición y obtención se calibran para que no sea fácil ganar mucho dinero rápido ni terminar el juego pronto.

- ✅ **Energía:** el **Aguante base es de 28** (decisión del autor, 2026-10-16: sube de 25 porque con 25 el jugador medio no pagaba la primera cuota con margen) y es la energía máxima de **cada expedición**: se rellena entera al empezar, y una casa mejor sube un poco la energía inicial (+2 por nivel de casa). Cada mena gasta energía según su mineral: carbón 8 · hierro 10 · cobre 12 · salitre 12 · plata 14 · cuarzo 16 · oro 18 · esmeralda 22 · diamante 26 · Aetherita 34 (cada nivel de herramienta la baja un 10 % del valor base, hasta ×0,6 en el nivel 5).
- ✅ **Descartar una mena cuesta energía** (decisión del autor, 2026-10-15): si escaneas una mena y no la extraes (porque no te conviene o porque tu herramienta no puede con ella), pagas el **25 % de la energía que habría costado extraerla**. Sin ese costo, descartar era gratis y el jugador solo minaba lo de mayor valor por energía; con él, repartir la energía entre extraer y descartar es una decisión real ([[28 Números base de la economía|28]], sección 3.7). El simulador ([[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]]) mide la pérdida de ingreso de descartar a este costo en ≈ 23 % frente a descartar gratis.
- ✅ **Menas por expedición:** variable según tus skills, herramientas y mejoras. Al principio caben **2 a 3** (con 28 de energía, 3 de carbón o 2 de hierro) y el número crece con la recolección: unas 4 en el Acto II, 7 en el III y hasta 10 por bloque en el IV. Los empleados rinden mucho menos que tú, pero escalan igual con sus skills ([[04 Progresión y meta|04]]).
- ✅ **Expedición profunda:** gasta **×1,8 de energía** y permite **×1,5 de carga**.
- ✅ **Consumibles de recarga de energía** y similares: versiones futuras, mucho después de la V1 ([[06 Roadmap, ideas futuras y pendientes|06]]).
- ✅ **Zonas que se agotan:** cada expedición baja la riqueza de la zona 6 puntos, cada día sube 3 y nunca baja del 40 %, así que rotar de zona rinde más que repetir una ([[28 Números base de la economía|28]]).

## Fuente

`studio/docs/02-extraccion.md:52`
