---
id: "doc-20-los-mods-de-claude-code"
tipo: "seccion"
title: "Los mods de Claude Code ✅"
aliases: ["doc-20-los-mods-de-claude-code"]
documento: "[[20 Equipo y flujo de agentes]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[20 §Cómo participa el autor]]"
siguiente: "[[20 §Pendiente]]"
arriba: "[[20 Equipo y flujo de agentes]]"
fuente: "studio/docs/20-equipo-y-flujo-de-agentes.md:132"
generado: true
---

# Los mods de Claude Code ✅

> Tres mods del repositorio, en tools/mods/ (un marketplace local llamado vein-mods):

← [[20 §Cómo participa el autor]] · [[20 Equipo y flujo de agentes|↑ 20]] · [[20 §Pendiente]] →

Tres mods del repositorio, en `tools/mods/` (un marketplace local llamado `vein-mods`):

| Mod | Comando | Qué muestra |
|---|---|---|
| `vf-estado` | `/estado` | Avance del roadmap por fase, hito y estado; limpieza y coherencia del diseño; tareas en curso; rama y PR abiertos |
| `vf-consumo` | `/consumo` | Consumo de tokens: ventana de cinco horas y semanal, tokens por prompt e historial por día, modelo y subagentes |
| `vf-equipo` | `/equipo` | **Oficina:** el estudio en planta, con cada empleado en su escritorio (trabajando, libre o en reserva), paquetes que viajan entre ellos y banderas con los hallazgos, más la bandeja «Te toca a ti» con los botones del autor. **Traspasos:** el detalle de cada tarea. **Equipo:** todos los roles por departamento |

- Los botones del autor envían un mensaje como si lo escribiera él, solo cuando los pulsa; los mods **no modifican archivos** por su cuenta. La excepción aparente es el hook de `vf-equipo` sobre la herramienta `Agent`: reescribe la llamada (fija el modelo y el esfuerzo del rol y pide la autorización de Fable), pero no escribe ni cambia ningún archivo del repositorio.
- Un mod corre con los mismos permisos del usuario y sin aislamiento. Por eso solo se instalan los de este repositorio, tras revisar el código. Cada uno se valida con `claude plugin validate` y se prueba con `claude plugin test`.
- Instalación y uso en `tools/mods/README.md`.

## Fuente

`studio/docs/20-equipo-y-flujo-de-agentes.md:132`
