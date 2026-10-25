# F0-24 · Prompts del storyboard del Acto I (15 imágenes, provisionales)

Reglas generales: 16:9, calidad baja, sin texto en la imagen (excepciones: la «A» grabada y el «1» del carrete, solo en la hoja de props y como glifo diminuto en la escena), protagonista hombre, arte provisional (no se pule). Rutas de referencia relativas a `studio/assets-ref/`.

## Prompt base de estilo (se antepone a TODOS los prompts)

```
Chunky pixel art, 16:9 landscape, 640x360 base resolution upscaled with large crisp square pixels on a fixed grid, no anti-aliasing, no gradients, no fine texture. Cold palette: slate blues and blue-greys (#0E161D, #17232C, #22333F, #36505F, #5B7C8C, #8FB0BA, #C9DCDF) with matte wine-red / vinotinto accents (#6E1A2B, #9A2640) under 5% of the image, and small brass (#B8893A) and amber lamp-light (#E3B25C) details. Industrial retro-futuristic (atompunk), gloomy but colorful. Characters are chunky chibi sprites like the reference minister: head about 40% of body height, 2-3 flat tones per material, thick black outline, big dark eyes with one highlight dot, tiny mouth, subtle expressions. Hard-edged simple shading. Pink-red or cyan glowing "ether" colors must NOT appear anywhere. NO text, NO letters, NO numbers, NO signs, NO watermark, NO UI, NO frame, NO photorealism, NO smooth painterly rendering.
```

Cámara: interiores = corte transversal lateral plano (Pet Society, ver `prueba-de-estilo-2/ui-tienda.png` solo como pauta de corte, sin su interfaz ni toldo); exteriores = vista aérea o lateral tipo Stardew.

## 1 · Mapa de Valdoria sin rótulos (mapa-valdoria-niebla)
Referencias: `prueba-de-estilo-2/mapa-valdoria.png` (composición y regiones), paleta de `prueba-de-estilo-2/paleta-laton.png`.
```
[BASE] Top-down illustrated fantasy-industrial map of the country of Valdoria, same composition as the reference map (reproduce its layout, borders and rails), with NO compass text and NO labels. Six regions: Hollín (south-west, coal smoke, chimneys, small mining town of Villa Brasa) is fully OPEN and clearly visible with a station dot and rail lines. The other five regions are covered by a dense dark near-opaque slate fog, each leaving ONE recognizable detail poking through: Sierra Alta (north-west) a snowy mountain peak; Salares del Litoral (north-east) a lighthouse and pier tip; Cavernas de Cristal (center-left) a faint cave mouth with a pale crystal tip (blue-white, no pink); La Fosa (center-right) the dark rim of a crater with a rusty fence (no glow); Puerto Meridiano (south-east, the capital) the tallest city tower silhouette. Do NOT show Cumbre Clara or any sanatorium. Keep rail lines as thin dark vinotinto lines between regions, visible only faintly through fog. Riveted brass-and-iron border without text.
```

## 2 · Hoja de props (props-hoja)
Referencias: `prueba-de-estilo-2/ui-tienda.png` (lámparas), `npc/faroleros.webp` (farol vinotinto).
```
[BASE] Prop sheet on a flat dark slate background, six items evenly spaced in two rows, each isolated with generous margin, no labels: (1) an electric "network lamp" street-style desk lamp, brass base with a tiny engraved capital letter A on the base, cold white-amber bulb, a cable running out; (2) a miner's lamp, hand-held carbide lantern, dented brass with a hook and a small flame, clearly different silhouette from item 1 (no cable, no glass globe); (3) a small matte wine-red lantern, UNLIT (dark glass); (4) the same wine-red lantern LIT with warm amber light (amber glow, never red-pink); (5) a folded paper with a wine-red wax seal, no writing; (6) a small tape reel on a spindle with a tiny numeral 1 on its label.
```

## 3 · d1.2 base: casa de Reme (casa-reme-base)
Referencias: `prueba-de-estilo-2/ui-tienda.png` (corte), `personajes/reme/modelo.webp`, `personajes/protagonista-hombre/modelo.webp`, imagen 2 (lámpara de red).
```
[BASE] Side cross-section interior of a cosy worn working-class house in a coal town, morning, grey daylight through a window on the left. Plain flat floor for side-scrolling. Table with a few papers and an old detector box, a kettle, a small stove, shelves, a bed corner. Reme (elderly woman, reference sheet) stands behind the table giving a brass key to the protagonist (young man, reference sheet) standing on the right. On the table: the electric network lamp with brass base (as in the prop sheet), lit cold white-amber. Wine-red only in the rug and a curtain, small. Window sill is EMPTY (no lantern). No text on the papers.
```

## 4 · d1.2 edición: papel sellado (variante B)
Referencia: imagen 3 (obligatoria), props (imagen 2).
Instrucción de edición:
```
Edit the reference image: keep everything identical (room, characters, poses, colors, camera). Remove the network lamp from the table (no other lamp in its place) and place a small folded paper with a wine-red wax seal on the table, no writing. Change nothing else.
```

## 5 · d1.2 edición: farol apagado (variante C)
Referencia: imagen 3 (obligatoria), props (imagen 2).
Instrucción de edición:
```
Edit the reference image: keep everything identical. Remove the network lamp from the table (table stays with papers only). Put a small matte wine-red lantern, UNLIT, dark glass, on the window sill. Change nothing else.
```

## 6 · d4.4 variante A: lámpara de red (cafe-lampara)
Referencias: imagen 3 (decorado), `personajes/reme/modelo.webp`, `personajes/protagonista-hombre/modelo.webp`.
```
[BASE] Same house as the reference image, now at NIGHT: dark blue window, warm amber interior light. Reme and the protagonist sit at the table sharing a cup of coffee, small steam. The electric network lamp with brass base (tiny engraved A) glows on the table as the clearly visible gift-like object. Calm, friendly expressions. Window sill empty, no sealed paper.
```

## 7 · d4.4 variante B: Quiroga y el papel (cafe-quiroga)
Referencias: imagen 6 (obligatoria), `personajes/quiroga/modelo.webp`.
Instrucción de edición:
```
Edit the reference image: keep room, night lighting and Reme. Remove the network lamp and replace it with a plain tea cup. Add Quiroga (reference sheet, official in dark coat, civil-servant look, no religious symbols) entering through the door on the right, head slightly bowed in a respectful greeting to Reme, handing back a folded paper with a wine-red wax seal that Reme holds. Protagonist still seated. No text.
```

## 8 · d4.4 variante C: farol vinotinto (cafe-farol)
Referencias: imagen 6 (obligatoria), props (imagen 2, farol encendido).
Instrucción de edición:
```
Edit the reference image: keep room, night lighting and both characters. Remove the network lamp (table has only cups). Add a small matte wine-red lantern LIT with warm amber light on the window sill, visible against the dark night window. No pink or red glow, only amber. No quiroga.
```

## 9 · d7.2 decorado A: lámpara de red (cuota-lampara)
Referencias: imagen 3 (obligatoria), `personajes/reme/expresiones.webp`.
Instrucción de edición:
```
Edit the reference image: change time to late afternoon (low warm amber sun through the window, long soft shadows). Replace the key hand-over with Reme sitting at the table with a small closed ledger and the protagonist standing opposite holding a few coins, discreet pay-or-ask-for-time moment, calm expressions. Keep the network lamp (A on base) on the table. Window sill empty.
```

## 10 · d7.2 decorado B: papel sellado (cuota-papel)
Referencias: imagen 9 (obligatoria), imagen 4.
Instrucción de edición:
```
Edit the reference image: keep late afternoon, room and characters identical. Remove the network lamp; put the folded paper with wine-red wax seal (no writing) on the table beside the ledger. Window sill empty.
```

## 11 · d7.2 decorado C: farol encendido (cuota-farol)
Referencias: imagen 9 (obligatoria), imagen 5, props (farol encendido).
Instrucción de edición:
```
Edit the reference image: keep late afternoon, room and characters identical. Remove the network lamp (table has ledger and coins only). On the window sill place the small matte wine-red lantern now LIT with warm amber light (amber only, no pink/red glow), visible even in daylight.
```
Nota: las ramas por dificultad de d7.2 (pagar / pedir tiempo / agradecimiento si ya pagó) son de diálogo y UI, no cambian el decorado: no requieren imágenes extra. La imagen sirve para las tres.

## 12 · d1.6 la carta (carta-casa-obrera)
Referencias: imagen 3 (estilo interior), `personajes/protagonista-hombre/modelo.webp`, props (lámpara de minero).
```
[BASE] Side cross-section interior of a small bare working-class miner's house, NIGHT, dark blue window. A narrow bed, a trunk and a suitcase on the floor, a small table. On the table a dented brass MINER'S lamp (carbide lantern with a small flame, no cable, no electric globe) casts amber light. The protagonist (young man, reference sheet) sits writing a letter with a pen, thoughtful subtle expression. Lonely, quiet mood. No text on the paper.
```

## 13 · d2.4 cierre de caja (cierre-caja)
Referencias: `prueba-de-estilo-2/ui-tienda.png` (corte y mostrador), `personajes/protagonista-hombre/modelo.webp`, props (carrete).
```
[BASE] Side cross-section interior of a small mining-goods shop, NIGHT, shop closed, dim amber lamp. Counter with an old brass cash register whose drawer is jammed open; the protagonist (young man, reference sheet) kneels behind it lifting a false bottom, finding a tape reel with a tiny numeral 1 on its label. Surprised but subtle expression. Shelves with mineral crates in the background, cold slate palette. No text elsewhere, no ether glow.
```

## 14 · d3.2 la placa (placa-galerias)
Referencias: `prueba-de-estilo-2/mina-horizontal.png` y `prueba-de-estilo-2/zonas.png` (Hollín), `personajes/teo/modelo.webp`, `personajes/protagonista-hombre/modelo.webp`.
```
[BASE] Side-view exterior of the mouth of the Galerías del Hollín coal mine, morning, grey smoky sky, timber-framed tunnel entrance with rails. Next to the entrance a fixed dark metal commemorative plaque on the rock wall, with rows of tiny blank engraved lines (no readable text). Teo (veteran miner, reference sheet) stands looking at the plaque with a grave, subtle expression; the protagonist (young man, reference sheet) beside him. Coal piles, a mine cart. No text.
```

## 15 · d7.4 el decreto (decreto-voceador)
Referencias: `npc/empleados-2-voceador.webp`, `prueba-de-estilo-2/edificios.png` (piezas de calle), `personajes/protagonista-hombre/modelo.webp`.
```
[BASE] Aerial three-quarter-down view (Stardew-style) of a main street in Villa Brasa at NIGHT, lit by amber street lamps, cobblestones, smoky chimneys, wine-red banners. In the center a newspaper crier (voceador, reference sheet) stands on a crate holding up a folded newspaper with an open mouth shouting, a small crowd of townsfolk and the protagonist (young man) listening with subtle surprised faces. No text on the newspaper or banners. No ether glow.
```

## Orden y costo recomendados
1) 1, 2, 3, 12, 13, 14, 15 (siete generaciones desde cero). 2) Ediciones 4, 5 (sobre 3), 6 (desde 3 con repintado nocturno), 7 y 8 (sobre 6), 9 (sobre 3), 10 y 11 (sobre 9). Si la IA deforma personajes al editar, regenerar con la referencia de personaje en vez de reintentar la edición.
