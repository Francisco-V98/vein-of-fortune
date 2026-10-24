---
id: "doc-23-s10"
tipo: "seccion"
title: "10 · Riesgos de combinatoria"
aliases: ["doc-23-s10"]
documento: "[[23 Árbol de decisiones y consecuencias]]"
limpieza: 100
abiertos: 0
espera: 5
aplazado_a: ["[[F1-23 Consola y atajos de depuración - saltar día, dar dinero]]", "[[F4-128 Acto II - guion y escenas]]", "[[F4-135 Acto III - guion y escenas]]", "[[F4-142 Acto IV - guion y escenas]]", "[[F4-210 Motor de epílogos por piezas]]"]
estado: "con-aplazados"
anterior: "[[23 §9 Banderas - quién las fija y quién las lee]]"
siguiente: "[[23 §11 Criterios cumplidos]]"
arriba: "[[23 Árbol de decisiones y consecuencias]]"
fuente: "studio/docs/23-arbol-de-decisiones.md:393"
generado: true
---

# 10 · Riesgos de combinatoria

> Estado: estimaciones del narrador. Los recorridos y las combinaciones se comprueban con la consola F1-23 y el motor de epílogos F4-210.

← [[23 §9 Banderas - quién las fija y quién las lee]] · [[23 Árbol de decisiones y consecuencias|↑ 23]] · [[23 §11 Criterios cumplidos]] →

**Estado:** estimaciones del narrador. Los recorridos y las combinaciones se comprueban con la consola ⏳ [[F1-23 Consola y atajos de depuración - saltar día, dar dinero|F1-23]] y el motor de epílogos ⏳ [[F4-210 Motor de epílogos por piezas|F4-210]].

| Riesgo | Por qué importa | Cómo se contiene |
|---|---|---|
| Demasiados caminos | 13 banderas de tres valores y una de dos son unos 3 millones de combinaciones nominales | Se prueban por **cuello de botella**, no por camino. Los recorridos principales son 81: 3 variantes por 3 alianzas por 3 entradas por 3 destinos |
| Variantes de Reme por alianza | El costo de Reme cambia con su facción y con tu alianza: 9 casos, y se muestra antes de elegir ([[22 Acto II - las tres variantes de Reme\|22]], sección 9) | Una sola escena A6 con tres capas |
| Medidores sin tramo | Sin umbrales, [[Esteban descubre el fondo reservado\|n-iv-esteban]], [[Quién publica\|n-iv-lucia-publica]] y [[El destino de Teo\|n-iv-teo]] no se pueden probar | Tres tramos por medidor (bajo, medio, alto) ✅ y caminos a cada uno en [[24 Umbrales de acto\|24]], sección 6 |
| Textos que se multiplican | Cada pequeña añade un diálogo por opción | Las pequeñas cambian una frase o un medidor, no una escena |
| Opciones largas | Unas 30 de las 81 opciones de `decisions.json` pasan de 28 caracteres | Son descripciones para el equipo, no el texto del botón; el botón final se escribe al guionizar y respeta el límite de [[18 Biblia narrativa\|18]], 1.9 ⏳ [[F4-128 Acto II - guion y escenas\|F4-128]], ⏳ [[F4-135 Acto III - guion y escenas\|F4-135]] y ⏳ [[F4-142 Acto IV - guion y escenas\|F4-142]] |
| Muertes que parecen injustas | Teo muere si no hubo revisión, también si aceptas su no | Avisos antes, incluido en la opción respetuosa (sección 2.4), y una sola regla que lo decide |
| Epílogos por camino | Un epílogo por cada combinación no se puede escribir | Epílogos **por piezas** que leen las banderas ✅ ([[25 Finales y epílogos\|25]]: 54 piezas, unas 17 por partida) |
| Ramas que se contradicen | Una decisión del I cambia algo en el IV | Cada decisión solo lee lo fijado antes; el hub comprueba que toda bandera se fija y se lee |

---

## Fuente

`studio/docs/23-arbol-de-decisiones.md:393`
