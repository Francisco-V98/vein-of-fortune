---
id: "mem-design-cleanliness-standard"
tipo: "memoria"
title: "Design cleanliness standard"
aliases: ["mem-design-cleanliness-standard"]
nombre: "design-cleanliness-standard"
memoria_tipo: "feedback"
arriba: "[[MOC Memoria]]"
generado: true
---

# Design cleanliness standard

> Standing rule — all design/docs must end up ✅ with no ambiguity; deferred items marked ⏳ with a task; measure and raise a "limpieza" percentage

Everything in the project (design docs, story, brand, tech) must be **✅ acordado** (decided) AND **coherent** (no loose story ends, no contradictions between docs, no numbers that break the economy), unambiguous and connected. Percentages start low and rise as tasks close; the goal is to reach launch as close to 100 % as possible. Only things that depend on something decided later may stay open, and that must be explicit (`⏳ <ID de tarea>`). Each doc has a "limpieza" % = ✅ / (✅+🟡+❓); keep raising it toward 100 % (not absolute, but everything must connect and work). The author said this applies to the whole project, forever.

**Why:** the author wants no loose ends or contradictions between documents; they review and accept in batches and expect a clear measure of how closed the design is.

**How to apply:**
- When writing or editing a doc, don't leave 🟡/❓ that can be decided now: present the open points to the author in a batch, then turn them into ✅. Mark invented details 🟡 until confirmed, then close them.
- Use `⏳ F0-XX` for things that truly depend on a later task; it must name an existing, unfinished task.
- **Defer only what doesn't condition the future** (author rule, 2026-10-12): a point may be `⏳` only if an existing task will resolve it AND nothing written or built before that task depends on the answer. Control question: "if the answer changes later, must something already done be redone?" If yes, decide it now with the author, before producing. The analyst classifies every open point as decide-now or defer-with-task; QA fails a task whose deferral conditions later work. Written in docs 15 and 20, `equipo.json` rules and all 19 agents (task [[F0-76 No aplazar lo que condiciona el futuro|F0-76]]).
- Check the hub panel "Limpieza del diseño" and `python3 studio/hub/build.py --strict` (broken links or task refs fail the build). Don't let a doc's % go down.
- Coherence is a second meter: `studio/data/world.json` (registry of minerals, zones, minigames, recipes, factions, characters) + `studio/hub/coherence.py`; hub view «Coherencia del diseño». Resolve findings by deciding with the author, never by silently editing data to make a check pass.
- Include it in PR checks (template and doc 15 Definition of Done).
- Closing passes per doc are tracked as roadmap tasks; target ≥ 90 % per doc as minimum reference.

Related: [[Author decisions narrative]]

## Relaciones

- **Documentos:** [[15 Flujo de trabajo y calidad]]
- **Tareas:** [[F0-76 No aplazar lo que condiciona el futuro]]
