---
id: "mem-links-to-new-pages"
tipo: "memoria"
title: "Links to new pages"
aliases: ["mem-links-to-new-pages"]
nombre: "links-to-new-pages"
memoria_tipo: "feedback"
arriba: "[[MOC Memoria]]"
generado: true
---

# Links to new pages

> When adding a new hub page or visible feature, give the author the link to open it in the browser

Whenever a new page, view or visible feature is added (hub views like `#/limpieza`, new docs), tell the author how to open it in the browser with the exact URL, e.g. `http://localhost:8765/studio/hub/#/coherencia`.

**Why:** the author reviews by looking at the hub and wants to jump straight to what was added.

**How to apply:** end the turn with a short list of links (view name → URL) for everything new. The hub runs from the repo root with `python3 -m http.server 8765` (see `.claude/launch.json`, server name `hub`), and it shows the files of the currently checked-out branch, so mention which branch has it if relevant. Remember that `data.js` must be regenerated (`python3 studio/hub/build.py --strict`).

Related: [[Design cleanliness standard]]
