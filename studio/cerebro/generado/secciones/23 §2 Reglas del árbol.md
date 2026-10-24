---
id: "doc-23-s02"
tipo: "seccion"
title: "2 · Reglas del árbol ✅"
aliases: ["doc-23-s02"]
documento: "[[23 Árbol de decisiones y consecuencias]]"
limpieza: 100
abiertos: 0
espera: 4
aplazado_a: ["[[F2-01 Modelo de estado de partida y semilla]]", "[[F4-61 Modelo de los cuatro medidores de relación]]"]
estado: "con-aplazados"
anterior: "[[23 §1 Decisiones del autor]]"
siguiente: "[[23 §3 Acto I - tres consecuencias pequeñas]]"
arriba: "[[23 Árbol de decisiones y consecuencias]]"
fuente: "studio/docs/23-arbol-de-decisiones.md:45"
generado: true
---

# 2 · Reglas del árbol ✅

> Estado: los cupos, las banderas, los medidores y sus tramos son de la sección 1. Las definiciones de nivel, los cuellos de botella y las…

← [[23 §1 Decisiones del autor]] · [[23 Árbol de decisiones y consecuencias|↑ 23]] · [[23 §3 Acto I - tres consecuencias pequeñas]] →

**Estado:** los cupos, las banderas, los medidores y sus tramos son de la sección 1. Las definiciones de nivel, los cuellos de botella y las reglas de seguridad los confirmó el autor el 2026-10-16 ([[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]); no cambian los cupos 3/6/18, las 14 banderas ni los 4 medidores. Las cifras de precios, cuotas y gastos son las de [[28 Números base de la economía|28]], ya decididas (base que verificó [[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]] con el simulador: con los ajustes que aprobó el autor pasan las 50 reglas de equilibrio, ver [[28 Números base de la economía|28]], sección 13); el movimiento de los medidores usa los tamaños 5, 10 y 20 que decidió el autor el 2026-10-16, y su ajuste fino ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]]

### 2.1 Niveles

| Nivel | Qué cambia | Cupo | Reparto |
|---|---|---|---|
| **Grande** | Cambia el tramo de historia que sigue y lo recuerda el epílogo | 3 | 1 en el II, 1 en el III y 1 en el IV |
| **Mediana** | Cambia una escena entera o el destino de un personaje durante varios actos | 6 | 2 en el II, 2 en el III y 2 en el IV |
| **Pequeña** | Cambia un diálogo, un precio o un medidor | 18 | 3 en el I, 5 en el II, 5 en el III y 5 en el IV |

### 2.2 Banderas y medidores

- **Bandera de elección.** Guarda qué opción elegiste (dos o tres valores). Una decisión puede **fijar** una bandera y otra puede **leerla**. Una decisión solo lee banderas que se fijaron antes, en su acto o en uno anterior.
- **Medidor.** Número de 0 a 100. Arranca en 50, salvo Teo (60) y Esteban (40). Cada opción lo mueve poco (≈ 5), normal (≈ 10) o mucho (≈ 20) ✅ (decisión del autor, 2026-10-16); [[F4-61 Modelo de los cuatro medidores de relación|F4-61]] los implementa y solo afina el ajuste fino, sin cambiar los caminos mínimos ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]]. Los tramos son *bajo* (0 a 34), *medio* (35 a 54) y *alto* (55 o más) ✅, y qué desbloquea cada uno está en [[24 Umbrales de acto|24]], sección 5. Los caminos a cada tramo que debe conservar [[F4-61 Modelo de los cuatro medidores de relación|F4-61]] están en la sección 6 de ese documento
- **Los cuatro medidores.** **Unión** es el de su sindicato ([[22 Acto II - las tres variantes de Reme|22]], sección 9). **Esteban** es personal, no el del Consorcio ✅. Las facciones aliables (Consorcio, Ministerio y Los Faroleros) **no tienen medidor propio** ✅: se miden por la alianza que elegiste. **Lucía** y **Teo** miden cuánto confían en ti. **Montenegro no tiene medidor** ✅.
- **Desenlaces calculados.** Lo que hacen Esteban, Lucía, Montenegro y Teo en el IV no guarda una bandera nueva: se calcula leyendo medidores y banderas. El epílogo ([[25 Finales y epílogos|25]]) lee las mismas y guarda los resultados como estado legible con nombres estables ✅ (sección 8 de ese documento, ⏳ [[F2-01 Modelo de estado de partida y semilla|F2-01]]); no son banderas del árbol, así que no cambian los cupos.
- **El sorteo no es una decisión.** La variante de Reme se fija antes de A1, se guarda en el estado ⏳ [[F2-01 Modelo de estado de partida y semilla|F2-01]] y es oculta. Las decisiones del II la leen sin guardarla como bandera.

### 2.3 Cuellos de botella

Un cuello es un punto donde varias ramas se juntan. Así el árbol no se multiplica sin control: cada acto tiene al menos uno y todos reciben al menos dos ramas.

| Cuello | Acto | Qué reúne | Recibe |
|---|---|---|---|
| [[Se cierra el Acto I\|c-i-cierre]] | I | Las tres consecuencias del I se pierden en el mismo cierre: reabres el puesto, atiendes la primera cuota y tienes el primer contacto con los empleados. | [[Cómo cuentas la herencia a tu familia\|n-i-herencia]], [[Pagar a Reme antes o después del plazo\|n-i-reme-plazo]], [[Confiar en Lucía con un rumor\|n-i-lucia-rumor]] |
| [[El apagón común\|c-ii-apagon]] | II | El apagón del Hollín es común (22, sección 4): el conflicto, el contacto y la huelga cambian cómo lo vives, no si ocurre. | [[Responder al primer contacto de la política\|n-ii-contacto]], [[Resolver el primer conflicto con tu facción\|n-ii-conflicto]], [[La primera huelga\|n-ii-huelga]] |
| [[El cierre de Reme\|c-ii-cierre]] | II | A6: Reme calla el abono y paga o respira según su facción y tu alianza. Siempre termina como tu aliada. | [[La orden de Reme\|n-ii-orden]], [[La primera huelga\|n-ii-huelga]], [[La alianza\|n-ii-alianza]] |
| [[El encuentro con Montenegro\|c-iii-encuentro]] | III | Las tres entradas llegan al mismo encuentro con Montenegro. Cambian lo que te debe cada uno, no la escena. | [[Cómo entras al círculo\|n-iii-circulo]], [[El monopolio de la Aetherita negra\|n-iii-monopolio]], [[Contrato oficial con cuota de entrega\|n-iii-contrato-oficial]], [[Esteban te pide algo en la bolsa\|n-iii-esteban-trato]] |
| [[Las pruebas llegan al enfrentamiento\|c-iv-pruebas]] | IV | Todas las ramas llegan al enfrentamiento con al menos tres pruebas que no se pierden (sección 8). | [[Proteger a Reme\|n-iv-reme-proteccion]], [[Esteban descubre el fondo reservado\|n-iv-esteban]], [[El archivo de Quiroga\|n-iv-quiroga-archivo]] |
| [[El acta de calibración\|c-iv-acta]] | IV | Revelar, callar o vender terminan en la misma última escena: el acta de calibración y la firma de Anselmo. | [[El destino de la Aetherita\|n-iv-aetherita]], [[A quién vendes la verdad\|n-iv-comprador]], [[Quién publica\|n-iv-lucia-publica]], [[El destino de Teo\|n-iv-teo]] |

### 2.4 Reglas de seguridad

- **Ninguna puerta de acto lee [[Bandera pago reme|f-pago-reme]] ni [[Bandera orden reme|f-orden-reme]]** ✅ ([[24 Umbrales de acto|24]]): Reme nunca cierra una puerta. [[La alianza|n-ii-alianza]] lee [[Bandera orden reme|f-orden-reme]] solo para mostrar el costo de Reme; no lo usa para decidir ✅ (decisión del autor, 2026-10-16).
- **Ninguna rama cierra la ruta de Reme.** Rechazar su orden cambia el costo, no lo que puedes hacer después. Siempre termina como tu mayor aliada.
- **Cada ruta del IV conserva al menos tres pruebas** (sección 8); la regla de Montenegro pide dos para intentar borrarte. Nada de lo que hagas con el archivo de Quiroga destruye la copia del certificado ni la carta de la cinta 6.
- **Ningún personaje aparece antes de su acto:** Esteban y Casilda en el II, Montenegro en el III. En el II, Montenegro es solo decreto y firma.
- **Anselmo solo como sombra antes del IV**, con una sombra como máximo por escena. Las cintas se recogen en una misión, nunca dentro de una de las seis escenas ancla del II, y no se pueden oír hasta el IV.
- **Los avisos son justos.** Toda decisión con una consecuencia grave se anuncia antes: la tos de Teo se ve y los demás la comentan antes de la revisión.
- **Cada magnitud tiene su palabra** ✅: el mercado se mide en **puntos** (un punto es el 1 % del precio base del mineral), el interés de la deuda en **pp** (punto porcentual de la tasa mensual) y la vigilancia como «vigilancia +N»; el «%» solo describe el ritmo de subida o una proporción. La caída y el rebote de la Aetherita respetan su tope diario de variación, del 15 % ([[03 Comercio y mercado|03]], [[28 Números base de la economía|28]])
- **El protagonista sigue siendo un optimista terco.** Ninguna opción lo hace cínico ni burlón con los trabajadores.

---

## Fuente

`studio/docs/23-arbol-de-decisiones.md:45`
