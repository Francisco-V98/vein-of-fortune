# studio/

Todo lo que sirve para **gestionar** el proyecto, separado del juego.

```
studio/
├── docs/          documentos de diseño (00 a 13)
├── data/          roadmap, actividad de tareas, assets, paleta y configuración
│   ├── roadmap.json
│   ├── tasks/     un archivo por tarea con historial, comentarios y evidencias
│   ├── assets.json
│   ├── palette.json
│   └── config.json
├── evidence/      archivos de evidencia, una carpeta por tarea (evidence/F0-15/…)
├── assets-ref/    arte de referencia y pruebas (no son assets finales del juego)
└── hub/           el sitio (index.html, app.js, styles.css) y su build.py
```

## Abrir el hub

`hub/data.js` es un archivo **generado** y no se versiona: después de clonar o de traer cambios, créalo con `python3 studio/hub/build.py`.

Luego abre `studio/hub/index.html` en el navegador. Funciona sin servidor ni internet.

Si prefieres un servidor local (solo escucha en tu equipo):

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

ejecutado desde la **raíz del repositorio**, y abre `http://localhost:8765/studio/hub/`.

## Regenerar los datos

Después de cambiar documentos, roadmap, tareas o assets:

```bash
python3 studio/hub/build.py            # genera hub/data.js y muestra avisos
python3 studio/hub/build.py --strict   # falla si hay incoherencias
```

## Campos de una tarea en `roadmap.json`

| Campo | Significado |
|---|---|
| `id` | Identificador (por ejemplo `F4-12`) |
| `title`, `desc`, `done_when` | Qué es y cuándo se considera lista (desde F4 se detallan antes de entrar a la fase) |
| `est` | Horas base del autor; **máximo 20 por tarea** (si es más, se desglosa) |
| `prio` | `P0` indispensable, `P1` importante, `P2` deseable, `P3` opcional |
| `status` | `backlog`, `sprint`, `doing`, `review`, `done`, `dropped` |
| `target` | Solo si difiere del de la fase (`MVP`, `Release 1`, `Evolutivo`) |

El orden de las tareas en el archivo es el **orden del plan**: la línea de tiempo del hub las coloca una detrás de otra según ese orden.

## Cómo funcionan las tareas

**El estado se guarda en el código y solo lo cambia Claude al trabajar.** El hub solo muestra; no tiene botones que cambien estados.

- `roadmap.json` guarda el plan y el **estado actual** de cada tarea (`backlog`, `sprint`, `doing`, `review`, `done`, `dropped`).
- `tasks/<ID>.json` guarda el **historial** (cada movimiento con fecha, autor y nota), los **comentarios** y las **evidencias**.
- Regla de coherencia, validada en el build: si una tarea no está en `backlog`, debe tener historial y su último movimiento debe llevar al estado actual. Que una tarea esté «En proceso» implica que se editaron sus datos.
- Evidencias: imágenes, archivos, enlaces, notas o enlaces a documentos. Los archivos van en `evidence/<ID>/`.
- Comentarios: se le dicen a Claude, que los registra con el autor y la fecha.
- Con GitHub, el historial de commits es la bitácora de cada cambio.

Formato de `tasks/<ID>.json`:

```json
{
  "id": "F0-15",
  "history": [
    { "at": "2026-10-11", "from": "backlog", "to": "doing", "by": "claude", "note": "Se empieza." }
  ],
  "comments": [
    { "at": "2026-10-11", "by": "autor", "text": "Comentario." }
  ],
  "evidence": [
    { "at": "2026-10-11", "type": "image", "title": "Captura", "path": "evidence/F0-15/captura.jpg", "note": "" },
    { "at": "2026-10-11", "type": "doc", "title": "Documento", "doc": "03-comercio" },
    { "at": "2026-10-11", "type": "link", "title": "Fuente", "url": "https://example.com" },
    { "at": "2026-10-11", "type": "note", "title": "Nota", "text": "Texto libre." },
    { "at": "2026-10-11", "type": "file", "title": "Archivo", "path": "data/roadmap.json" }
  ]
}
```

## Separar `studio/` del juego

Reglas que lo hacen posible: `game/` no depende de `studio/` y `studio/` no importa nada de `game/`.

**Ignorarlo** (por ejemplo en un clon dedicado al juego):

```bash
git sparse-checkout set game
```

**Extraerlo con su historial** a otro repositorio:

```bash
git subtree split --prefix=studio -b studio-solo
git push <url-del-nuevo-repositorio> studio-solo:main
```

Después, en el repositorio original, se puede quitar con `git rm -r studio`.

> Estado: **probado en local el 2026-10-11** con el historial del repositorio. `git subtree split` produjo una rama cuya raíz es el contenido de `studio/` (sin `game/`) y con su historial; `git sparse-checkout set game` dejó un clon con solo `game/`. Falta probar el `git push` de la rama extraída a un repositorio distinto.

## Qué edita cada cosa

| Quiero cambiar | Archivo |
|---|---|
| Documentos de diseño | `docs/NN-….md` |
| Fases, hitos y tareas | `data/roadmap.json` |
| Historial, comentarios y evidencias | `data/tasks/<ID>.json` y `evidence/<ID>/` |
| Imágenes y notas de arte | `data/assets.json` |
| Colores | `data/palette.json` |
| Título y etiquetas | `data/config.json` |
| Audio de referencia | `assets-ref/audio/` |
