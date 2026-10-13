# Mods de Claude Code para Veta de Fortuna

Tres mods, en un marketplace local llamado `vein-mods`. Documentación del equipo y del flujo: `studio/docs/20-equipo-y-flujo-de-agentes.md`.

| Mod | Comando | Para qué |
|---|---|---|
| `vf-estado` | `/estado` | Panel de progreso y estadísticas del proyecto |
| `vf-equipo` | `/equipo` | La oficina del estudio: quién trabaja en qué, los traspasos de cada tarea y lo que te toca a ti |
| `vf-consumo` | `/consumo` | Consumo de tokens: ventana de cinco horas y semanal, tokens por prompt e historial por día, modelo y subagentes |

## Seguridad

Un mod corre con tus mismos permisos y sin aislamiento. Lee el código antes de instalarlo: está en `hooks/register.js` de cada mod. `vf-consumo` no lee ni ejecuta nada fuera de Claude Code: solo guarda en el almacén propio del mod, en tu carpeta de configuración, el texto de cada prompt (recortado a 200 caracteres), la carpeta del proyecto, los tokens y los porcentajes de las ventanas; no envía nada a ninguna parte. Los otros dos solo leen archivos del repositorio y ejecutan `python3 studio/hub/build.py`, `git` y `gh pr list` (`vf-estado`). Los botones de `vf-equipo` envían un mensaje con tu nombre solo cuando los pulsas, y `gh pr list` lo ejecuta para ver los PR abiertos.

## Instalar

Desde la raíz del repositorio, con Claude Code 2.1.287 o la app de escritorio 2.1.286 o más reciente:

```bash
claude plugin marketplace add ./tools/mods --scope project
claude plugin install vf-estado@vein-mods --scope project
claude plugin install vf-equipo@vein-mods --scope project
claude plugin install vf-consumo@vein-mods --scope project
```

Después, en una sesión: `/reload-plugins`, y `/estado`, `/equipo` o `/consumo`. Para quitarlos: `/plugin` y desactivar o desinstalar.

## Probar y validar

```bash
cd tools/mods/vf-estado && claude plugin validate . && claude plugin test
cd ../vf-equipo && claude plugin validate . && claude plugin test
cd ../vf-consumo && claude plugin validate . && claude plugin test
```

## Consumo de tokens (`/consumo`)

El panel tiene tres pestañas:

- **Ahora:** las ventanas de cinco horas y semanal con su porcentaje y cuándo se reinician, lo gastado hoy, cuántos tokens nuevos valen un punto de cada ventana (estimado con lo que el mod vio gastar) y los últimos prompts. La ventana de uso es de **cinco** horas, no seis.
- **Prompts:** todos los prompts guardados, recientes o más caros primero; al pulsar uno se ve el detalle: tokens de entrada, salida y caché, cuánto fue del hilo principal y cuánto de subagentes, qué modelos y cuántos puntos subió cada ventana.
- **Días:** los últimos 14 días, el gasto de la semana por modelo y los prompts más caros.

Un prompt es un turno del hilo principal. Los subagentes que lanza cuentan dentro de ese prompt. «Tokens nuevos» es entrada, salida y caché escrita; la caché leída se muestra aparte porque pesa mucho menos. El historial se guarda en el almacén del mod: hasta 3.000 prompts y un resumen por día sin límite. En la línea de estado aparece el porcentaje de cada ventana. El porcentaje solo existe con una suscripción de Claude y el motor lo informa en puntos enteros, así que un prompt pequeño puede mostrar +0 puntos.
