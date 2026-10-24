---
id: "doc-12-prueba-de-estilo-realizada"
tipo: "seccion"
title: "Prueba de estilo ✅ (realizada)"
aliases: ["doc-12-prueba-de-estilo-realizada"]
documento: "[[12 Dirección de arte]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[12 §Paleta propuesta (valores aproximados, a afinar)]]"
siguiente: "[[12 §Pipeline (actualizado el 2026-10-13)]]"
arriba: "[[12 Dirección de arte]]"
fuente: "studio/docs/12-direccion-de-arte.md:44"
generado: true
---

# Prueba de estilo ✅ (realizada)

> Cuatro imágenes generadas con IA (modelo gptimage25, calidad baja, ~0,25 créditos cada una). Están en studio/assets-ref/prueba-de-estilo/:

← [[12 §Paleta propuesta (valores aproximados, a afinar)]] · [[12 Dirección de arte|↑ 12]] · [[12 §Pipeline (actualizado el 2026-10-13)]] →

Cuatro imágenes generadas con IA (modelo `gpt_image_2_5`, calidad baja, ~0,25 créditos cada una). Están en `studio/assets-ref/prueba-de-estilo/`:

| Archivo | Qué prueba |
|---|---|
| `mina.png` | Escena de la mina |
| `personajes.png` | Protagonista hombre y mujer |
| `minerales.png` | Los 10 minerales en una cuadrícula |
| `mercado.png` | Pantalla de escritorio con monitor, teletipo y periódico |

### Resultado

**Lo que funciona:**

- La dirección **fría + vinotinto + atompunk** se ve bien y es reconocible.
- El hombre y la mujer salen **coherentes entre sí** (misma ropa, misma paleta, mismo estilo).
- Los 10 minerales salen con un estilo bastante consistente.
- La pantalla de mercado transmite justo el aire de "Papers, Please" retrofuturista.

**Lo que preocupa:**

1. **No es pixel art "real".** Son ilustraciones de aspecto pixelado a alta resolución. Los píxeles no son de tamaño uniforme ni están alineados a una cuadrícula. Un juego de pixel art necesita una resolución base fija (por ejemplo ×4 o ×6 al escalar) con píxeles consistentes.
2. **Son composiciones completas, no assets.** Un juego necesita sprites separados, fondos por capas, tiles que encajen y marcos de animación. Una imagen completa se usa como **referencia visual**, no como pieza del juego.
3. **Legibilidad de los minerales.** Cuarzo, salitre y plata se parecen demasiado a tamaño pequeño; las siluetas deben distinguirse. El contorno vinotinto aparece en todos los íconos y diluye la regla del acento.
4. **Texto.** La IA generó "pseudo-texto". En el juego todo el texto será real, con una fuente pixel.
5. **El oro** sale cálido y rompe la paleta fría. Está permitido como excepción.

### Qué sirve y qué no

| Uso | Veredicto |
|---|---|
| Tablero de inspiración y dirección de arte | ✅ Muy útil |
| Guía de estilo y paleta | ✅ |
| Bocetos de pantallas y UI | ✅ Como referencia |
| Íconos de minerales | ✅ Referencia de siluetas y colores para el pixel art definitivo; no se pulen (ver la sección «Assets provisionales y definitivos») |
| Personajes y escenas | ✅ Referencia de diseño para el pixel art definitivo; no se reconstruyen a mano |
| Assets directos del juego | ❌ No: lo generado con IA en las rondas de prueba es provisional |

## Fuente

`studio/docs/12-direccion-de-arte.md:44`
