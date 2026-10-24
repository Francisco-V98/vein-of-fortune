---
id: "doc-10-cerebro-del-proyecto-en-obsidian"
tipo: "seccion"
title: "Cerebro del proyecto en Obsidian ✅"
aliases: ["doc-10-cerebro-del-proyecto-en-obsidian"]
documento: "[[10 Técnico y herramientas]]"
abiertos: 0
espera: 1
aplazado_a: ["[[F0-88 Consulta del estudio sin leer documentos enteros]]"]
estado: "con-aplazados"
anterior: "[[10 §Trabajar con IA]]"
siguiente: "[[10 §Pendiente]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:223"
generado: true
---

# Cerebro del proyecto en Obsidian ✅

← [[10 §Trabajar con IA]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Pendiente]] →

- **Qué es:** un vault de Obsidian **generado** desde el repo (documentos, datos, tareas, equipo y memoria) en `studio/cerebro/`, ignorado por git, de solo lectura y con unas 2.000 notas atómicas enlazadas (una por sección «##» de cada documento y una por entidad: tareas, personajes, minerales, zonas, edificaciones, decisiones, hilos, escenas, finales, términos del glosario, casos de QA, reglas del simulador, piezas de arte). Decisión del autor del 2026-10-23.
- **Cómo se alimenta:** `python3 studio/hub/build.py` lo regenera entero en cada ejecución (menos de un segundo; `--sin-cerebro` lo salta). Los documentos y datos siguen siendo la fuente de verdad: lo que se cambie dentro de `generado/` se pierde. Tus notas van en `mis-notas/` y la configuración en `.obsidian/`; el generador nunca las toca.
- **Cómo se usa:** abre la carpeta `studio/cerebro` como vault en Obsidian y empieza por la nota «00 Inicio». Cada nota guarda su `id` estable y su nombre legible; el grafo tiene colores por tipo y una vista guardada que oculta el backlog de F1 a F6. El código está en `tools/cerebro/` (ver su README).
- Ahorra poco o nada en tokens: sirve para ver y navegar el proyecto. Para consultar sin leer documentos enteros se usa `tools/consulta.py` (⏳ [[F0-88 Consulta del estudio sin leer documentos enteros|F0-88]]).

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:223`
