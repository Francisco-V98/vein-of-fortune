# Mods de Claude Code para Veta de Fortuna

Tres mods, en un marketplace local llamado `vein-mods`. Documentación del equipo y del flujo: `studio/docs/20-equipo-y-flujo-de-agentes.md`.

| Mod | Comando | Para qué |
|---|---|---|
| `vf-estado` | `/estado` | Panel de progreso y estadísticas del proyecto |
| `vf-equipo` | `/equipo` | La oficina del estudio: quién trabaja en qué, los traspasos de cada tarea y lo que te toca a ti |
| `vf-consumo` | `/consumo` | Consumo de tokens: ventana de cinco horas y semanal, tokens por prompt e historial por día, modelo y subagentes |

## Seguridad

Un mod corre con tus mismos permisos y sin aislamiento. Lee el código antes de instalarlo: está en `hooks/register.js` de cada mod. `vf-consumo` no lee ni ejecuta nada fuera de Claude Code: solo guarda en el almacén propio del mod, en tu carpeta de configuración, el texto de cada prompt (recortado a 200 caracteres), la carpeta del proyecto, los tokens y los porcentajes de las ventanas; no envía nada a ninguna parte. `vf-estado` solo lee archivos del repositorio y ejecuta `python3 studio/hub/build.py`, `git` y `gh pr list`. `vf-equipo` lee archivos del repositorio, ejecuta `gh pr list` y `git branch --show-current`, y sus botones envían un mensaje con tu nombre solo cuando los pulsas.

### Qué lee y qué intercepta `vf-equipo` sobre `Agent`

`vf-equipo` aplica la política de modelos y esfuerzo por agente (`studio/data/equipo.json`, campos `modelo`, `esfuerzo` y `politica_modelos`; lógica en `vf-equipo/hooks/politica.js`). Para eso engancha dos eventos:

- **`tool.call` de la herramienta `Agent`** (cada vez que Claude lanza un subagente, también desde otro subagente). Lee el `subagent_type`, la `description` y el `prompt` del encargo, y `studio/data/equipo.json`. Si el encargo no trae `model` o `effort`, los rellena con los de la tabla del rol; lo que Claude fija a propósito se respeta. No cambia el prompt, ni las herramientas, ni los permisos del subagente. Si el modelo final es **Fable 5.1**, abre el diálogo de preguntas del motor (`$.ui.ask`) y solo lo deja pasar si lo autorizas: «Aprobar para esta tarea» (vale 8 horas para esa tarea; la tarea se identifica por el ID `F0-87` del encargo o, si no hay, por la rama git), «Aprobar solo este», o «Usar otro modelo» (Opus, Sonnet o Haiku). Es un diálogo de dos pasos porque el del motor admite como máximo cuatro opciones. El texto libre del diálogo solo vale si nombra un modelo; cualquier otra cosa, cancelar, un error o una sesión sin interfaz (`-p`) deniegan el lanzamiento con «Fable no autorizado». Si `equipo.json` no se puede leer no bloquea nada, salvo que el modelo sea Fable.
- **`agent.spawn`**. No cambia ni deniega nada: solo apunta, por `agentId`, el rol, el modelo, el esfuerzo, el motivo (defecto o ajuste), la tarea y si Fable estaba autorizado. Se guarda en el almacén del mod (hasta 500 entradas), junto con las aprobaciones por tarea, y alimenta la pestaña «Equipo». No guarda prompts.

Límites: solo se pregunta por lo que pasa por la herramienta `Agent`; un lanzamiento de otro mod (`$.agent.spawn`), un workflow o un equipo de teammates no pasa por el diálogo. Un fallo inesperado del hook deja pasar el lanzamiento, salvo que el encargo pida Fable de forma explícita. Los botones «Cambiar modelo» y «Cambiar esfuerzo» no editan nada: envían a Claude un mensaje con tu nombre pidiéndole que cambie `equipo.json`.

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

## Versión mínima y riesgo sin comprobar

`vf-equipo` usa `tool.call` sobre `Agent` (con `model` y `effort`), `agent.spawn` y `$.ui.ask`. Sus pruebas pasan con Claude Code 2.1.295 y 2.1.299 (`claude plugin test`), y los tipos de la 2.1.299 los traen; no hay forma de comprobarlo con la 2.1.287, la mínima declarada arriba, porque no hay un binario de esa versión a mano. Si en esa versión falta alguno, el hook no se carga y la política de modelos no se aplica (el resto del mod sigue funcionando); en ese caso hay que subir el mínimo.

## Consumo de tokens (`/consumo`)

El panel tiene tres pestañas:

- **Ahora:** las ventanas de cinco horas y semanal con su porcentaje y cuándo se reinician, lo gastado hoy, cuántos tokens nuevos valen un punto de cada ventana (estimado con lo que el mod vio gastar) y los últimos prompts. La ventana de uso es de **cinco** horas, no seis.
- **Prompts:** todos los prompts guardados, recientes o más caros primero; al pulsar uno se ve el detalle: tokens de entrada, salida y caché, cuánto fue del hilo principal y cuánto de subagentes, qué modelos y cuántos puntos subió cada ventana.
- **Días:** los últimos 14 días, el gasto de la semana por modelo y los prompts más caros.

Un prompt es un turno del hilo principal. Los subagentes que lanza cuentan dentro de ese prompt. «Tokens nuevos» es entrada, salida y caché escrita; la caché leída se muestra aparte porque pesa mucho menos. El historial se guarda en el almacén del mod: hasta 3.000 prompts y un resumen por día sin límite. En la línea de estado aparece el porcentaje de cada ventana. El porcentaje solo existe con una suscripción de Claude y el motor lo informa en puntos enteros, así que un prompt pequeño puede mostrar +0 puntos.
