---
id: "doc-10-localizacion-espanol-e-ingles-desde-el-i"
tipo: "seccion"
title: "Localización (español e inglés desde el inicio) ✅"
aliases: ["doc-10-localizacion-espanol-e-ingles-desde-el-i"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 0
abiertos: 3
espera: 0
estado: "con-abiertos"
anterior: "[[10 §Arte y sonido]]"
siguiente: "[[10 §Estructura del repositorio]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:97"
generado: true
---

# Localización (español e inglés desde el inicio) ✅

> El juego se hace en español e inglés desde el principio, con un marco que permita sumar más idiomas sin tocar el código.

← [[10 §Arte y sonido]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Estructura del repositorio]] →

El juego se hace en **español e inglés desde el principio**, con un marco que permita sumar más idiomas sin tocar el código.

| Aspecto | Decisión |
|---|---|
| Voz | Español neutro latinoamericano con **tuteo**; en inglés, tono igual de cercano |
| Formato de traducciones 🟡 | Archivos `.po` (gettext) que Godot soporta de forma nativa, con contexto y plurales |
| Cadenas | **Ninguna cadena fija** en el código ni dentro del arte; el arte no lleva texto incrustado |
| Variables | Marcadores con nombre (por ejemplo `{nombre}`), no posicionales; el género gramatical se resuelve con textos neutros y variantes solo cuando haga falta |
| Longitud | El español ocupa entre 20 y 30 % más que el inglés; la interfaz debe tolerarlo (prueba con pseudo-localización) |
| Fuentes | Pixel con caracteres latinos extendidos (á, ñ, ¿, ¡) y **fuentes de respaldo por idioma** para el futuro |
| Números y fechas | Formato según el idioma |
| Flujo 🟡 | Extraer cadenas, traducir con asistencia de IA, revisar con un glosario ES/EN y compilar |
| Herramientas 🟡 | Edición de `.po` con un editor como Poedit; una plataforma de traducción (por ejemplo Weblate o Crowdin) solo si más adelante hay colaboradores |
| Idiomas futuros | Portugués, francés, alemán u otros. Los idiomas de derecha a izquierda exigen espejar la interfaz y quedan fuera de alcance por ahora |
| Tienda | Ficha de Steam y capturas en ES y EN |
| Documentos de `studio/` | Siguen en español; solo el juego y la ficha de tienda son bilingües |

Los sonidos "blip" de los personajes no dependen del idioma, lo que facilita la localización.

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:97`
