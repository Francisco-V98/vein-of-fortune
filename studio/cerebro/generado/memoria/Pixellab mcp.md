---
id: "mem-pixellab-mcp"
tipo: "memoria"
title: "Pixellab mcp"
aliases: ["mem-pixellab-mcp"]
nombre: "pixellab-mcp"
memoria_tipo: "reference"
arriba: "[[MOC Memoria]]"
generado: true
---

# Pixellab mcp

> PixelLab (pixel-art generation) is the tool for the final art; MCP at api.pixellab.ai/mcp, docs at /mcp/docs; author has no subscription yet; never store or commit the Bearer token

PixelLab is the planned tool for the game's **final pixel art** (see [[Provisional art policy]]). It has a Claude Code MCP server: `claude mcp add pixellab https://api.pixellab.ai/mcp -t http -H "Authorization: Bearer <token>"`; tool overview at `https://api.pixellab.ai/mcp/docs`. As of 2026-10-13 the author has **no subscription yet** and shared a token in chat.

What the docs list (read 2026-10-13): characters with 8 directions and animations (up to 128 px standard/pro, 256 px v3), top-down and isometric tiles, map objects, building kits, UI panels, portraits and talking/lip-sync, pixel fonts, normal maps, `image_to_pixelart`, project asset management. Billed in "generations" (standard character 1, pro 10–25, objects 10–25, pixflux images 1). The docs page showed **no licensing or commercial-use statement**: must be verified before final production (roadmap task [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio|F4-227]] "Prueba de PixelLab").

**Why:** the author wants real pixel assets only after tests pass; PixelLab is that final step.

**How to apply:**
- Never write the Bearer token into any file, memory, commit or PR. If it must be added, the author runs `claude mcp add` in their own terminal WITHOUT `--scope project` (project scope writes `.mcp.json` into the repo).
- Do not call PixelLab tools until the author confirms the subscription and authorizes final production; tell them the generation count first, like with Higgsfield.
- Verify commercial-use terms and costs in [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio|F4-227]] before any production.

## Relaciones

- **Tareas:** [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio]]
