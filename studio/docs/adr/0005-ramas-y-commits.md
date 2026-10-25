# ADR-0005 · GitHub Flow con ramas de versión y Conventional Commits

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

El autor pide trabajar por ramas, de forma muy organizada. El proyecto lo desarrolla una persona con ayuda de IA y publica en tiendas de aplicaciones.

## Decisión

`main` siempre sana y protegida; ramas cortas `tipo/ID-slug`; todo entra por pull request con integración continua en verde y *merge commit* (enmendado, ver abajo). Ramas `release/X.Y` para estabilizar versiones y `hotfix/X.Y.Z` para urgencias. Commits con la convención Conventional Commits en español y el ID de la tarea.

## Alternativas consideradas

- **Git Flow completo con `develop`:** más fusiones sin beneficio para una persona con integración continua.
- **Trabajo directo sobre `main`:** sin revisión ni trazabilidad.

## Consecuencias

Historial legible (no lineal, ver la enmienda), trazabilidad entre tarea, rama y commit, y `main` siempre publicable. Requiere configurar la protección de rama en GitHub.

## Enmienda (2026-10-25, F0-35 y F0-58)

La decisión original decía *squash*. El autor decidió en F0-35 fusionar con **merge commit**, sin exigir historial lineal: conserva la rama `studio/<ID>-tema` y cada commit `tipo(ámbito): ID descripción`, que la integración continua valida. En GitHub solo está permitido *Allow merge commits*. El 2026-10-25 (F0-58) el autor confirmó además que un commit sin ID de tarea es un error de la integración continua, no un aviso; los commits de fusión y de reversión quedan exentos.
