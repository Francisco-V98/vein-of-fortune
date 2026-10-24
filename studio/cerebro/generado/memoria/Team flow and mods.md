---
id: "mem-team-flow-and-mods"
tipo: "memoria"
title: "Team flow and mods"
aliases: ["mem-team-flow-and-mods"]
nombre: "team-flow-and-mods"
memoria_tipo: "project"
arriba: "[[MOC Memoria]]"
generado: true
---

# Team flow and mods

> How the studio team flow works — 21 roles/19 subagents, per-task pipeline in tasks/<ID>.json, the /equipo and /estado mods, and what to do when the author presses «Terminé mi parte»

Since 2026-10-12 the studio runs a staged flow per task (docs/20, `studio/data/equipo.json`): ideación → análisis → producción → QA técnico → revisión del autor → prueba del autor → cierre, with 21 roles in 7 departments (19 subagents in `.claude/agents/`, the author "Fran", and me as coordinator). Roles join in their phase (`desde`). Mods `vf-estado` (/estado), `vf-equipo` (/equipo) and `vf-consumo` (/consumo: token use per prompt, 5-hour and weekly rate-limit windows, daily history; installed 2026-10-13, history starts from install) live in `tools/mods/`, installed from the local marketplace `vein-mods` (project scope).

**How to apply:**
- Keep each in-flight task's `pipeline` block in `studio/data/tasks/<ID>.json` current: stages with `estado`/`entrega`/`hallazgos`, `especialista`, and the chronological `traspasos` log (`de`, `a`, `que`, `at`, `tipo: entrega|devolucion`). Every handoff or return gets a log entry; build.py validates it.
- The author's panel buttons send chat messages as the user. "Terminé mi parte en <ID>: … aprobado" → advance the task (autor hecha, playtest hecha/omitida, cierre hecha), set status done in roadmap.json with a history entry, then merge the PR if all its tasks are approved. "…dejé ajustes en el chat" → read their comments above, assign the right specialist, log a `devolucion` traspaso, and return the task to producción.
- Use the real subagents for task work (first real use planned for [[F0-41 Biblia narrativa - estructura, voz y glosario|F0-41]]); until then pipeline notes must say the coordinator did it. Only the coordinator generates images (credit control).
- Mods run unsandboxed with the user's permissions; only install mods from this repo after the author reviews the code. Test with `claude plugin validate` and `claude plugin test` using the desktop-bundled binary (`~/Library/Application Support/Claude/claude-code/<ver>/.../claude`).
- The app renders mod SVGs as images: no hover tooltips and no clicks from inside the drawing; detail opens via buttons and an in-scene floating window.

**Why:** the author wants every task visibly handed from specialist to specialist with no loose ends, and wants to review, test and approve through the panel.

Related: [[Design cleanliness standard]], [[Brand logo direction]]

## Relaciones

- **Documentos:** [[20 Equipo y flujo de agentes]]
- **Tareas:** [[F0-41 Biblia narrativa - estructura, voz y glosario]]
