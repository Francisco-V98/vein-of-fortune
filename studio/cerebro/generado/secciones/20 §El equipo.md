---
id: "doc-20-el-equipo"
tipo: "seccion"
title: "El equipo ✅"
aliases: ["doc-20-el-equipo"]
documento: "[[20 Equipo y flujo de agentes]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[20 §Etapas del flujo]]"
siguiente: "[[20 §Modelo y esfuerzo por rol]]"
arriba: "[[20 Equipo y flujo de agentes]]"
fuente: "studio/docs/20-equipo-y-flujo-de-agentes.md:27"
generado: true
---

# El equipo ✅

> El autor pidió analizar qué empleados necesita de verdad el proyecto. Salen 21 roles en 7 departamentos (19 agentes, el autor y el…

← [[20 §Etapas del flujo]] · [[20 Equipo y flujo de agentes|↑ 20]] · [[20 §Modelo y esfuerzo por rol]] →

El autor pidió analizar qué empleados necesita de verdad el proyecto. Salen **21 roles en 7 departamentos** (19 agentes, el autor y el coordinador), pensados a partir de las fases del roadmap: diseño y mundo (F0), preparación técnica (F1), prototipo y vertical slice (F2 y F3), contenido (F4), pulido y lanzamiento (F5) y evolutivo (F6). Cada rol se **incorpora en su fase**; antes de eso queda en reserva.

| Departamento | Rol | Tipo | Se une en | Hace |
|---|---|---|---|---|
| Dirección | **Coordinador (Claude)** | Principal | F0 | Reparte el trabajo entre los especialistas, mantiene el roadmap, genera las imágenes, fusiona y cierra las tareas. |
| Dirección | **Fran (autor)** | Humano | F0 | Revisa los entregables y los PR, juega y prueba el juego (diversión, detalles visuales, tono), y aprueba o devuelve. |
| Estrategia y análisis | **Ideador e investigador** | Agente (`ideador`) | F0 | Explora opciones y referencias (juegos parecidos, mercado) y propone al menos tres alternativas con una recomendación. |
| Estrategia y análisis | **Analista de coherencia** | Agente (`analista`) | F0 | Cruza lo propuesto con los documentos y el registro del mundo; revisa números, riesgos y dependencias; fija los criterios de aceptación. |
| Estrategia y análisis | **Asesor legal y de licencias** | Agente (`asesor-legal`) | F0 | Vigila la licencia de cada fuente, imagen y sonido, la privacidad, las reglas de las tiendas y la clasificación por edades. |
| Estrategia y análisis | **Responsable de lanzamiento** | Agente (`responsable-lanzamiento`) | F5 | Prepara la ficha de tienda, el kit de prensa, las capturas, la comunidad y las métricas en producción. |
| Diseño | **Diseñador de sistemas** | Agente (`disenador-sistemas`) | F0 | Escribe y edita el diseño del juego: bucle central, progresión, riesgo y el registro del mundo. |
| Diseño | **Economista y balance** | Agente (`economista`) | F0 | Modela precios, demanda, mercado y recompensas, y comprueba con simulaciones que la economía no se rompa. |
| Diseño | **Diseñador de contenido** | Agente (`disenador-contenido`) | F0 | Diseña zonas, minerales, eventos, empleados y encuentros con sus parámetros. |
| Diseño | **Diseñador UI/UX** | Agente (`disenador-ui-ux`) | F0 | Diseña pantallas, flujos, información por capas y accesibilidad en PC y Steam Deck (la fase móvil se suma después). |
| Narrativa y lenguaje | **Narrador** | Agente (`narrador`) | F0 | Escribe la historia, los personajes y los diálogos con la voz acordada, sin romper el canon. |
| Narrativa y lenguaje | **Localizador ES/EN** | Agente (`localizador`) | F0 | Mantiene el glosario y adapta los textos entre español neutro con tuteo e inglés cercano. |
| Arte y sonido | **Director de arte** | Agente (`director-arte`) | F0 | Escribe los encargos de arte y revisa cada imagen contra el estilo acordado. |
| Arte y sonido | **Diseñador de sonido** | Agente (`disenador-sonido`) | F1 | Planifica efectos, voces en blips y música, y su licencia. |
| Ingeniería | **Arquitecto de software** | Agente (`arquitecto`) | F0 | Define módulos, capas, datos y decisiones de arquitectura (ADR) y vigila la deuda técnica. |
| Ingeniería | **Desarrollador de juego** | Agente (`desarrollador-juego`) | F1 | Programa el juego en Godot con código limpio, modular y probado. |
| Ingeniería | **Desarrollador de herramientas** | Agente (`desarrollador-herramientas`) | F0 | Mantiene el hub, la integración continua y los mods del estudio. |
| Ingeniería | **Ingeniero de seguridad** | Agente (`ingeniero-seguridad`) | F1 | Revisa la seguridad, la integridad de los datos guardados y la privacidad. |
| Calidad | **Revisor de código** | Agente (`revisor-codigo`) | F1 | Revisa cada cambio de código antes de que llegue al autor: errores, claridad y arquitectura. |
| Calidad | **QA técnico** | Agente (`qa`) | F0 | Ejecuta el build estricto, las pruebas y las comprobaciones, y reporta sin editar nada. |
| Calidad | **Diseñador de pruebas** | Agente (`disenador-pruebas`) | F0 | Prepara los casos de prueba y las guías de playtest para que el autor pruebe con método. |

Cada agente tiene su definición en `.claude/agents/<agente>.md`, con las herramientas que puede usar y las reglas del proyecto que cumple. Los que solo revisan (analista, QA, revisor de código, seguridad) no editan archivos. El generador de imágenes lo usa solo el coordinador, para controlar los créditos; el director de arte escribe el encargo y revisa el resultado.

**Por qué estos y no menos:** economía, localización, UI/UX, sonido, legal, seguridad, revisión de código y diseño de pruebas aparecen como tareas propias en el roadmap (balance económico, localización ES/EN, flujo de pantallas, sonido y música, legal y tienda, QA y seguridad, tutorial y accesibilidad, lanzamiento). Juntarlos en un solo «diseñador» o «desarrollador» haría que nadie los vigilara.

## Fuente

`studio/docs/20-equipo-y-flujo-de-agentes.md:27`
