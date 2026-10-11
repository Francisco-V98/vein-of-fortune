# Registro de errores

Cada error es un archivo `BUG-NNNN.json`. Ejemplo:

```json
{
  "id": "BUG-0001",
  "title": "Se pierde la partida al guardar con el almacén lleno",
  "severity": "S1",
  "status": "abierto",
  "found_in": "0.1.0",
  "task": "F2-03",
  "steps": ["Llenar el almacén", "Guardar y cerrar", "Abrir el juego"],
  "expected": "La partida se conserva.",
  "actual": "La partida aparece vacía.",
  "evidence": [{"at": "2026-10-11", "type": "note", "title": "Notas", "text": "…"}],
  "history": [{"at": "2026-10-11", "from": "abierto", "to": "triaje", "by": "claude", "note": "Reproducido."}]
}
```

- **Severidad:** `S1` crítico, `S2` grave, `S3` moderado, `S4` menor.
- **Estados:** `abierto`, `triaje`, `en-correccion`, `corregido`, `verificado`, `cerrado`, `no-se-corrige`.
- Todo error corregido incorpora una prueba de regresión (un caso en `../cases.json`).

Procedimiento completo en `docs/16-calidad-y-qa.md`.
