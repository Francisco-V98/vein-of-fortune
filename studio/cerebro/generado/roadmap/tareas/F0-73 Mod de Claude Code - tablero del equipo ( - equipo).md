---
id: "F0-73"
tipo: "tarea"
title: "F0-73 Mod de Claude Code: tablero del equipo (/equipo)"
aliases: ["F0-73"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P2"
est: 6
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: hecha", "cierre: hecha"]
especialista: "[[Desarrollador de herramientas]]"
docs: []
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P2", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:776"
generado: true
---

# F0-73 Mod de Claude Code: tablero del equipo (/equipo)

> Tablero con las etapas del flujo, el número de tareas en cada una, quién trabaja ahora y los botones del autor para aprobar o devolver.

Tablero con las etapas del flujo, el número de tareas en cada una, quién trabaja ahora y los botones del autor para aprobar o devolver.

## Hecha cuando

Mod validado, con pruebas en verde y aprobado por el autor.

## Flujo por etapas

Especialista de producción: [[Desarrollador de herramientas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-12 | Diseño del panel y de los botones del autor |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | Los botones envían mensajes y no tocan archivos |
| [[Etapa Producción\|produccion]] | hecha | [[Desarrollador de herramientas]] | 2026-10-12 | Segunda versión: diagrama de traspasos, bandeja del autor y actualización automática |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-12 | claude plugin validate y ocho pruebas en verde |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-12 | Aprobado por el autor con «Todo bien» y «Terminé mi parte» |
| [[Etapa Prueba del autor\|playtest]] | hecha |  | 2026-10-12 | El autor probó el panel en la app y lo aprobó |
| [[Etapa Cierre\|cierre]] | hecha |  | 2026-10-12 | Tarea cerrada y PR #32 fusionado |

### Hallazgos

- [[Fran (autor)]] (autor, resuelto):  → resuelto por [[Desarrollador de herramientas]]: Diagrama de traspasos con hallazgos y resoluciones
- [[Fran (autor)]] (autor, resuelto):  → resuelto por [[Desarrollador de herramientas]]: Actualización automática y bandeja «Te toca a ti» con Todo bien, Salieron ajustes y Terminé mi parte
- [[Fran (autor)]] (autor, resuelto):  → resuelto por [[Desarrollador de herramientas]]: Dibujos con clave estable y animación sincronizada con el reloj; el detalle se abre con un clic (tarjeta con ✕ para cerrar), porque el ratón no muestra los globos en la app

## Traspasos

- 2026-10-12 · [[Ideador e investigador]] → [[Analista de coherencia]] (entrega): Un panel con flujo, equipo y botones
- 2026-10-12 · [[Analista de coherencia]] → [[Desarrollador de herramientas]] (entrega): Criterio: nada se escribe sin que el autor lo pida
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): Mod /equipo v1 con pestañas Flujo, Equipo y Tarea
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y cinco pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Desarrollador de herramientas]] (devolucion): La estética no gusta: quiere un diagrama de traspasos con hallazgos, actualización automática y botones del autor
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): v2 con diagrama de traspasos, bandeja del autor y actualización automática
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y ocho pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Desarrollador de herramientas]] (devolucion): Quiere una oficina animada tipo juego de gestión y un equipo más real
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): v3 con oficina animada y 21 roles
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y diez pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Desarrollador de herramientas]] (devolucion): La animación se reinicia al hacer scroll; quiere información al pasar el ratón, el historial por línea y el identificador de Fran
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): v4 con globos de información, historial por línea, marca de Fran y dibujos con clave estable
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Desarrollador de herramientas]] (devolucion): El hover no funciona: quiere que todo el detalle se abra con un clic y se cierre con una ✕
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): v5: detalle con clic en personas, traspasos y hallazgos, con tarjeta que se cierra con ✕
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y catorce pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Desarrollador de herramientas]] (devolucion): Quiere la ventana flotante dentro del entorno animado, al tocar un personaje o una línea
- 2026-10-12 · [[Desarrollador de herramientas]] → [[QA técnico]] (entrega): v6: ventana flotante dentro del plano, anclada a lo que se toca
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: validación y catorce pruebas en verde
- 2026-10-12 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: «Terminé mi parte» sin ajustes

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza tras la petición del autor de crear mods para el proyecto. (rama studio/F0-71-mods-panel-y-equipo)
- 2026-10-12 · doing → review · claude: Mod /equipo escrito, validado y con cinco pruebas en verde. (rama studio/F0-71-mods-panel-y-equipo)
- 2026-10-12 · review → done · claude: El autor aprobó la tarea desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Comentarios

- 2026-10-12 · claude: El mod vf-equipo abre con /equipo un panel con tres pestañas: Flujo (dibujo con las siete etapas y el número de tareas en cada una en la app de escritorio, quién trabaja ahora según los subagentes activos y las tareas por etapa), Equipo (cada rol, lo que hace y en qué está) y Tarea (el flujo de una tarea y, si te toca, los botones Aprobar y Devolver, que envían un mensaje como si lo escribieras tú). Los mods no escriben archivos. Falta instalarlo y verlo en la app.
- 2026-10-12 · autor: Quiero que la visual del equipo sea como un diagrama: quién le pasa a quién, cómo se hizo, qué tarea se ejecuta ahora, los hallazgos de cada uno y cómo los soluciona quien corresponde. Que se actualice sola y que yo tenga botones para decir que terminé mi parte: revisar, aprobar un PR o probar a mano, ya sea aprobando o con ajustes que te comento por el chat.
- 2026-10-12 · claude: Segunda versión del mod: diagrama de traspasos con las entregas, los hallazgos y quién los resolvió; actualización automática (mira los datos cada 3 segundos, los PR cada 45 y también al terminar cada turno); y la bandeja «Te toca a ti» con tus tareas en revisión o prueba y los PR abiertos. Cada una sigue el recorrido Todo bien o Salieron ajustes (los ajustes los comentas por el chat) y Terminé mi parte, que envía el mensaje y deja la acción como enviada hasta que el coordinador la mueva.
- 2026-10-12 · autor: La estética de /estado me gustó muchísimo, la de /equipo no: la quiero más dinámica y estética, con animaciones, como un jueguito automático de gestión pero muy simple.
- 2026-10-12 · claude: /equipo pasa a una pestaña Oficina: el estudio en planta con siete salas, un escritorio por empleado y personajes que teclean cuando trabajan, duermen cuando están libres y quedan en sombra si aún no se incorporan. Los paquetes viajan por el recorrido de la tarea, las banderas llevan los hallazgos de quien los dejó a quien los resolvió y un globo muestra en qué tarea trabaja cada uno. El detalle pasó a la pestaña Traspasos y el reparto de roles a Equipo.
- 2026-10-12 · autor: Me gusta la animación; solo que al hacer scroll se reinicia. Quiero información al pasar el ratón: en las líneas qué le pasó a quién, en los personajes qué hacen, en las banderas de qué le pasará a quién; y si un flujo pasó varias veces por la misma línea, que diga en qué pasada fue. Además quiero un identificador de «Fran» para saber cuál es mi personaje.
- 2026-10-12 · claude: Cada línea del plano guarda ahora su historial de pasadas (1.ª, 2.ª…) con la fecha y lo que se entregó, y muestra un contador ×N cuando se repite; en la pestaña Oficina hay además una lista con ese historial. Los personajes y las banderas llevan un globo con su información. Los dibujos tienen clave estable para que el scroll no reinicie la animación. Tu personaje se llama Fran, lleva la etiqueta TÚ y una estrella en la placa. Falta confirmar en la app que el globo aparece al pasar el ratón: depende de que se muestren los títulos del SVG; si no, lo pasamos a botones.
- 2026-10-12 · autor: El hover no funciona. Mejor con clic, y que el mensaje que salga se pueda cerrar con una ✕, para no depender del hover.
- 2026-10-12 · claude: En la pestaña Oficina hay ahora tres filas de botones: Personas, Traspasos y Hallazgos. Al tocar uno se resalta en el plano lo que implica (el resto se atenúa) y se abre una tarjeta con su detalle y una ✕ Cerrar (tecla x); tocar el mismo botón otra vez también la cierra. Los globos del ratón quedan en el dibujo por si algún día la app los muestra.
- 2026-10-12 · autor: Me parece bien, pero me refería a una ventana flotante dentro del entorno animado: que al tocar un personaje, una línea o algo así salga qué significa cada uno.
- 2026-10-12 · claude: El detalle sale ahora como ventana flotante dentro del plano, anclada junto al empleado, la línea o el hallazgo elegido, con su título, su texto, una ✕ y un cable que la une a lo que se tocó. El plano resalta lo implicado y atenúa el resto. Los botones de Personas, Traspasos y Hallazgos siguen siendo la forma de abrirla, porque la app no envía clics desde dentro del dibujo; se cierra con el botón «✕ Cerrar ventana» (tecla x) o volviendo a tocar el mismo botón.
- 2026-10-12 · autor: Terminé mi parte: revisé el entregable y está aprobado. Pásala a la siguiente etapa del flujo.

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]

## Fuente

`studio/data/roadmap.json:776`
