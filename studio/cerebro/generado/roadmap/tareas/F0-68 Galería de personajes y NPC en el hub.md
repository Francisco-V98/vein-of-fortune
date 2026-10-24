---
id: "F0-68"
tipo: "tarea"
title: "F0-68 Galería de personajes y NPC en el hub"
aliases: ["F0-68"]
fase: "[[F0 Diseño]]"
hito: "[[F0.13 Personajes - hojas de modelo y NPC]]"
prio: "P1"
est: 5
status: "done"
version: "MVP"
docs: []
arriba: "[[F0.13 Personajes - hojas de modelo y NPC]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:725"
generado: true
---

# F0-68 Galería de personajes y NPC en el hub

> Vista del hub con todas las hojas por personaje y por grupo de NPC, y registro de las imágenes en assets.json.

Vista del hub con todas las hojas por personaje y por grupo de NPC, y registro de las imágenes en assets.json.

## Hecha cuando

Galería visible en el hub con todas las hojas.

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza la galería en el hub, rama apilada sobre F0-67. (rama studio/F0-68-galeria-personajes-hub)
- 2026-10-12 · doing → review · claude: Vista «Personajes y NPC» del hub con las 48 hojas. (rama studio/F0-68-galeria-personajes-hub)
- 2026-10-12 · review → done · claude: El autor revisó y aprobó la galería de personajes y NPC en el hub. (aprobación del autor en la conversación)

## Comentarios

- 2026-10-12 · claude: Vista nueva del hub en #/personajes: 10 personajes (modelo, poses y expresiones) y 18 hojas de NPC agrupadas en facciones, empleados y civiles, enemigos humanos y criaturas. Cada imagen abre el visor grande con flechas, y hay un índice por sección. Los nombres, facciones y actos salen de world.json; studio/data/galeria.json solo dice qué hoja cubre a quién y build.py avisa si falta un personaje, un NPC o una imagen. Probada en escritorio y en móvil (375 px) sin errores en consola.

## Relaciones

- **Hito:** [[F0.13 Personajes - hojas de modelo y NPC]]

## Fuente

`studio/data/roadmap.json:725`
