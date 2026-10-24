---
id: "doc-12-segunda-ronda-de-pruebas-horizontal"
tipo: "seccion"
title: "Segunda ronda de pruebas ✅ (horizontal)"
aliases: ["doc-12-segunda-ronda-de-pruebas-horizontal"]
documento: "[[12 Dirección de arte]]"
limpieza: 92
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[12 §Pipeline (actualizado el 2026-10-13)]]"
siguiente: "[[12 §Hojas de personajes y NPC]]"
arriba: "[[12 Dirección de arte]]"
fuente: "studio/docs/12-direccion-de-arte.md:93"
generado: true
---

# Segunda ronda de pruebas ✅ (horizontal)

> El juego es horizontal (landscape). Catorce imágenes en studio/assets-ref/prueba-de-estilo-2/:

← [[12 §Pipeline (actualizado el 2026-10-13)]] · [[12 Dirección de arte|↑ 12]] · [[12 §Hojas de personajes y NPC]] →

El juego es **horizontal (landscape)**. Catorce imágenes en `studio/assets-ref/prueba-de-estilo-2/`:

| Archivo | Qué es | Veredicto |
|---|---|---|
| `minerales-v2.png` | 10 minerales corregidos | ✅ Siluetas y colores distintos; **Aetherita** vinotinto cristalina destaca claramente |
| `retratos-a.png`, `retratos-b.png` | Retratos de diálogo: Reme, Teo, Quiroga, Lucía, Esteban, Casilda, Ministro Montenegro y foto de Anselmo | ✅ Muy buenos; expresivos, coherentes y con la paleta |
| `sprites.png` → `sprites-corregido.png` | Sprites pequeños tipo Stardew (protagonistas hombre y mujer y elenco) | ✅ Funcionan como guía. El ministro original parecía un sacerdote (estola con cruces); se reemplazó por un funcionario severo de abrigo azul marino y faja vinotinto, sin símbolos religiosos (`ministro-corregido.png`) |
| `ui-mercado.png` → `ui-mercado-corregido.png` | Terminal de mercado (lista, gráfico, teletipo, bloques del día) | ✅ Buen punto de partida. Las flechas rojo/verde se cambiaron por ▲ cian (sube) y ▼ vinotinto (baja), que cumple la regla de accesibilidad. ✅ La regla vigente cambia la subida a azul hielo, porque el cian es solo de la Aetherita; la imagen se conserva como referencia de composición |
| `ui-tienda.png` | Pantalla de la tienda con corte transversal | ✅ Muy buena base; comunica el "taller + mostrador + almacén" |
| `edificios.png` | 9 edificios (tienda, taller, almacén, casa, Ministerio, Consorcio, Unión, bar, periódico) | ✅ Consistentes entre sí; en isométrica |
| `mapa-valdoria.png` | Mapa ilustrado con las 6 regiones y vías de tren | ✅ Muy bueno; viable como **imagen estática con zonas tocables** |
| `zonas.png` | 6 fondos de zonas de minado | ✅ Cada zona tiene identidad propia; La Fosa conecta con el color de la Aetherita |
| `minijuegos.png` | Maquetas de Picado, Perforación y Regateo | ✅ Sirven de guía de interfaz |
| `mina-horizontal.png` | Galerías del Hollín en horizontal | ✅ La favorita del autor, ahora en formato correcto |
| `paleta-laton.png`, `paleta-verdigris.png`, `paleta-oxido.png` | Tres opciones de acento secundario | Ver abajo |

### Acento secundario: comparación

| Opción | Efecto | Veredicto |
|---|---|---|
| **Latón / ámbar** | Aporta luz cálida, es muy industrial y combina con monedas, remaches y lámparas | ✅ **Elegida** |
| Verdigrís (cobre oxidado) | Sutil, se mezcla con el frío; poco contraste como complemento | 🟡 Reservar para detalles de cobre y tecnología |
| Naranja óxido | Más energía pero se lee como "peligro" | ❌ No como secundario general |

### Lo que se aprendió

- La IA da muy buen material de **referencia y de dirección**; las composiciones completas (mapa, zonas, tienda) pueden usarse como **imagen estática** con zonas tocables, lo cual encaja con la estética estática.
- Para sprites, íconos y UI el arte definitivo **reconstruye y separa piezas** en pixel art con PixelLab, después de la Puerta B (ver pipeline arriba). Lo generado en estas rondas es provisional.
- La paleta funciona en todos los tipos de imagen: personajes, minerales, edificios, interfaz y mapa.
- El vinotinto está presente en casi todas las imágenes; hay que **controlar su dosis** para que no pierda fuerza y para que la Aetherita siga siendo especial.

## Fuente

`studio/docs/12-direccion-de-arte.md:93`
