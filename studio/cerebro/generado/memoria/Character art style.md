---
id: "mem-character-art-style"
tipo: "memoria"
title: "Character art style"
aliases: ["mem-character-art-style"]
nombre: "character-art-style"
memoria_tipo: "feedback"
arriba: "[[MOC Memoria]]"
generado: true
---

# Character art style

> Author's approved art style for character sheets — chunky chibi pixel art like the minister sprite for model/poses, detailed portraits for expressions

For character sheets (studio/assets-ref/personajes/<id>/):
- **Model sheet and poses sheet**: chunky low-res chibi pixel art copying the approved minister sprite (`studio/assets-ref/prueba-de-estilo-2/ministro-corregido.png`): ~100 px tall, big visible pixels, flat 2–3 tone colors, thick black outline, NO fine texture/hair strands/gradients, big simple eyes with one white highlight, head ~40 % of height. The author rejected the more detailed/painterly versions.
- **Expressions sheet**: detailed portrait style (like retratos-a/b), 6 common expressions (default per personality, feliz, triste, enojo, susto, cansancio). Expressions must be subtle, not exaggerated: cansancio = heavy eyelids/dark circles/relaxed mouth (no yawn), clearly different from triste (tear).
- **Production order**: model sheet first (it defines the full aesthetic, approved by the author); then the poses sheet generated with the model sheet as the ONLY reference; expressions in detailed style from portrait + model. Author rejected poses made with other references because they drifted from the model.
- **NPC group sheets**: the approved reference for style, proportions and layout is the Consorcio Arvel sheet (`studio/assets-ref/npc/consorcio.webp`, 3 types × FRENTE/LADO/ESPALDA/CARA). The author rejected NPC sheets where characters had inconsistent proportions between rows (helmet/visor, realistic heads): every NPC in a sheet must have the same height and the same big chibi head with the same big dark eyes, even with helmets/visors (push visors up). Use the Consorcio sheet as the first reference for all NPC sheets.
- Pipeline: reference images are uploaded to the image service (works once permissions granted), generate with `gpt_image_2_5` quality medium / 2k / 16:9 (≈1 credit each), save with `tools/art/guardar_hoja.py` as WebP. Keep model and poses at the same proportions.

**Why:** the author wants all characters consistent and ready to become game sprites; they gave this feedback while reviewing Reme's pilot ([[F0-60 Piloto - tres hojas de Reme|F0-60]]).

**How to apply:** use the minister sprite as the first style reference in every model/poses generation; edit only the panels that need change in expression sheets; review each sheet with the author before moving to the next character.

Related: [[Design cleanliness standard]]

## Relaciones

- **Tareas:** [[F0-60 Piloto - tres hojas de Reme]]
