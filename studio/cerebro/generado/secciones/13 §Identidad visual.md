---
id: "doc-13-identidad-visual"
tipo: "seccion"
title: "Identidad visual"
aliases: ["doc-13-identidad-visual"]
documento: "[[13 Marca e identidad]]"
limpieza: 80
abiertos: 2
espera: 1
aplazado_a: ["[[F1-18 Fuente pixel con caracteres latinos extendidos y plan de]]"]
estado: "con-abiertos"
anterior: "[[13 §Frase de marca]]"
siguiente: "[[13 §Reglas de escritura]]"
arriba: "[[13 Marca e identidad]]"
fuente: "studio/docs/13-marca-e-identidad.md:84"
generado: true
---

# Identidad visual

> Paleta fría con vinotinto como acento principal y latón como detalle mínimo. Reglas completas en 12. El rojo-rosado brillante es solo de la…

← [[13 §Frase de marca]] · [[13 Marca e identidad|↑ 13]] · [[13 §Reglas de escritura]] →

### Colores ✅

Paleta fría con **vinotinto** como acento principal y **latón** como detalle mínimo. Reglas completas en [[12 Dirección de arte|12]]. El rojo-rosado brillante es solo de la Aetherita.

### Símbolo ✅

**La moneda de minero** (elegida por el autor el 2026-10-12): una moneda de latón con aro grueso y, dentro, tres ideas del juego en una sola imagen:
- **Lámpara:** un casco de minero de latón con una lámpara redonda de borde de acero al frente.
- **Éter:** en la lente de la lámpara, tres puntas de Aetherita en vinotinto con un contorno cian fino; es el único cian y rosado de la marca porque es la propia Aetherita.
- **Comercio:** tres barras escalonadas (acero, vinotinto y ámbar) bajo el casco, como un gráfico que sube.

Funciona sola, sin el texto (icono de app y firma pequeña), y con el nombre debajo. Se evita el farol porque es el emblema de Los Faroleros (vinotinto mate con luz ámbar, nunca rojo emisivo ✅). Las piezas están en `studio/assets-ref/marca/`.

### Logotipo ✅ (versión provisional)

| Pieza | Archivo |
|---|---|
| Logo apilado (icono grande y nombre debajo) | `logo-apilado-es.webp`, `logo-apilado-en.webp` |
| Logo horizontal (icono y nombre al lado) | `logo-horizontal-es.webp`, `logo-horizontal-en.webp` |
| Icono solo | `icono-moneda.webp` |
| Icono de app (cuadrado redondeado) | `icono-app.webp` |
| Tableros de presentación | `logo-tablero-es.webp`, `logo-tablero-en.webp` |

- **Nombre:** letras de pixel art macizas, en un azul acero pálido (cerca de *Hielo medio*, no blanco puro), con contorno azul marino y una sombra de un píxel. Una versión por idioma con la misma estructura (*Veta de Fortuna* y *Vein of Fortune*).
- **Provisional ✅:** el logo y el wordmark son provisionales hasta la producción definitiva en pixel art con PixelLab, después de la Puerta B (política del autor del 2026-10-13, ver [[12 Dirección de arte|12]]). Son la versión de trabajo para el hub, el README y las pruebas; el logo definitivo y el arte de la pantalla de título son [[F4-230 Logo y wordmark definitivos en pixel art|F4-230]] y [[F4-231 Ícono de la app y pantalla de título definitivos|F4-231]].

### Tipografía

- ✅ **Fuente pixel candidata: Pixelify Sans** (licencia abierta OFL, con á é í ó ú ñ ¿ ¡ y varios pesos), elegida por el autor el 2026-10-12 para probar primero en títulos y textos del juego.
- ⏳ [[F1-18 Fuente pixel con caracteres latinos extendidos y plan de|F1-18]]: verificar la licencia, probar los glifos en el motor y fijar las fuentes de respaldo por idioma. Si falla una prueba se vuelve a *Jersey 10* o *Silkscreen*, que eran las otras candidatas.
- ✅ **Interfaz del estudio (hub):** sans legible del sistema; no es parte de la marca del juego.
- ✅ Todo el texto del juego es texto real con esta fuente, nunca texto dentro de imágenes (regla de escritura 2).

### Guía visual 🟡 ([[F0-20 Guía visual de marca - colores, tipografías candidatas y|F0-20]])

**Colores de marca.** Fondo pizarra (`#17232C` o `#0E161D`), latón (`#B8893A`) y ámbar (`#E3B25C`) para la moneda, vinotinto (`#9A2640`) como acento y azul acero pálido para el nombre. El vinotinto no pasa del 5 % de cualquier pieza. El rojo-rosado y el cian solo aparecen en el cristal del icono, que es la Aetherita.

**Símbolo (moneda de minero).**
- Pixel art con píxeles visibles; se escala solo por múltiplos enteros (×2, ×3, ×4).
- Área libre alrededor: la mitad del ancho del aro. Tamaño mínimo: 32 px de alto en pantalla.
- El casco, la lámpara, el cristal y las tres barras siempre van juntos; no se quita ninguno.
- Nunca en rojo ni con un farol en lugar de la lámpara.

**Nombre.** Pixel art macizo, en la versión de cada idioma. Se usa sobre fondos oscuros; en un fondo claro se coloca sobre una placa pizarra.

**Texto del juego.** Pixelify Sans en títulos y botones; el nombre del logo es un dibujo, no la fuente.

### Usos incorrectos 🟡

- No usar el rojo-rosado brillante fuera de la Aetherita.
- No estirar, rotar ni suavizar el pixel art, ni escalar por valores no enteros.
- No colocar el logotipo sobre fondos que reduzcan su contraste.
- No mezclar los dos idiomas en un mismo logotipo.
- No poner el símbolo en rojo ni cambiar la lámpara por un farol.
- No añadir degradados, brillos ni partículas al logo, ni más detalle al cristal.
- No volver el nombre blanco puro ni cambiar su color.

## Fuente

`studio/docs/13-marca-e-identidad.md:84`
