# Mods de Claude Code para Veta de Fortuna

Dos mods, en un marketplace local llamado `vein-mods`. Documentación del equipo y del flujo: `studio/docs/20-equipo-y-flujo-de-agentes.md`.

| Mod | Comando | Para qué |
|---|---|---|
| `vf-estado` | `/estado` | Panel de progreso y estadísticas del proyecto |
| `vf-equipo` | `/equipo` | La oficina del estudio: quién trabaja en qué, los traspasos de cada tarea y lo que te toca a ti |

## Seguridad

Un mod corre con tus mismos permisos y sin aislamiento. Lee el código antes de instalarlo: está en `hooks/register.js` de cada mod. Estos dos solo leen archivos del repositorio y ejecutan `python3 studio/hub/build.py`, `git` y `gh pr list` (`vf-estado`). Los botones de `vf-equipo` envían un mensaje con tu nombre solo cuando los pulsas, y `gh pr list` lo ejecuta para ver los PR abiertos.

## Instalar

Desde la raíz del repositorio, con Claude Code 2.1.287 o la app de escritorio 2.1.286 o más reciente:

```bash
claude plugin marketplace add ./tools/mods --scope project
claude plugin install vf-estado@vein-mods --scope project
claude plugin install vf-equipo@vein-mods --scope project
```

Después, en una sesión: `/reload-plugins`, y `/estado` o `/equipo`. Para quitarlos: `/plugin` y desactivar o desinstalar.

## Probar y validar

```bash
cd tools/mods/vf-estado && claude plugin validate . && claude plugin test
cd ../vf-equipo && claude plugin validate . && claude plugin test
```
