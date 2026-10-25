# Cómo trabajar en este repositorio

> El repositorio es público solo para consulta (ver [LICENSE](LICENSE)); por ahora no se aceptan PR externos.

Resumen. El detalle está en `studio/docs/`:

- **Arquitectura y modularidad:** `14-arquitectura-y-modularidad.md`
- **Flujo de trabajo y calidad:** `15-flujo-de-trabajo-y-calidad.md`
- **QA:** `16-calidad-y-qa.md`
- **Decisiones:** `adr/`

## En una página

1. **Una tarea, una rama** desde `main`: `tipo/ID-descripcion-corta` (por ejemplo `feat/F2-04-modelo-de-precio`). Nadie sube directamente a `main`.
2. **Commits pequeños** con la convención `tipo(ámbito): ID descripción`.
3. **Verificar en local** antes de subir:

```bash
python3 tools/arch/check_architecture.py game
python3 -m unittest discover -s tools/arch
python3 -m unittest discover -s tools/ci
python3 studio/hub/build.py --strict
python3 tools/ci/check_commits.py origin/main..HEAD
```

4. **Pull request** con la plantilla. La integración continua debe estar en verde.
5. **Flujo de la tarea:** `backlog → sprint → doing → review → qa → done`. La revisión verifica código y arquitectura; QA verifica el comportamiento con casos de prueba.
6. **Fusión con merge commit** (sin squash ni rebase) y borrado de la rama.

## Primeros pasos: correr el proyecto en tu máquina

Sirve para quien se sume como colaborador (hoy el repositorio es solo de consulta; ver [LICENSE](LICENSE)).

**Requisitos:** `git` y Python 3.9 o superior (el CI usa 3.11). No hay que instalar paquetes: las herramientas usan solo la biblioteca estándar. Godot 4.x (GDScript) hará falta cuando exista `game/project.godot` (aún no).

```bash
git clone https://github.com/Francisco-V98/vein-of-fortune.git
cd vein-of-fortune
python3 studio/hub/build.py --strict     # genera el hub y valida roadmap, tareas y documentos
python3 -m http.server 8765 --bind 127.0.0.1
```

Abre <http://127.0.0.1:8765/studio/hub/index.html> para ver el hub (roadmap, documentos, storyboard, vista Semana 1). `studio/hub/data.js` se genera en cada build y no se versiona: si falta, la página sale vacía; vuelve a ejecutar el build. Tras cambiar `studio/`, repite el build y refresca.

**Comprobar que todo está bien** (lo mismo que hace el CI):

```bash
python3 -m unittest discover -s tools/arch
python3 -m unittest discover -s tools/ci
python3 tools/arch/check_architecture.py game
```

Para trabajar, crea una rama desde `main` y sigue los pasos de arriba. Windows: usa `py -3` en lugar de `python3`.

## Reglas que no se negocian

- El dominio no depende de nada: ni nodos, ni interfaz, ni otros módulos.
- Un módulo solo usa la `api` de otro y debe declararlo en `game/architecture.json`.
- Sin números ni textos del juego dentro del código: van en datos.
- Sin secretos, claves ni contraseñas en el repositorio.
- Todo error corregido deja una prueba de regresión.

## Cuando se cambia el estudio

`studio/` (documentos, roadmap, tareas, hub) sigue el mismo flujo. Después de cambiarlo:

```bash
python3 studio/hub/build.py --strict
```
