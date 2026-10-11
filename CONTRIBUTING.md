# Cómo trabajar en este repositorio

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
6. **Fusión con squash** y borrado de la rama.

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
