# Veta de Fortuna · Vein of Fortune

Juego de gestión, minería y comercio para PC (Steam, Windows y Linux; el móvil llega después de la 1.0), en pixel art, horizontal, de un jugador y pago único. Español e inglés desde el inicio.

Un optimista hereda una deuda, una licencia y un puesto de mercado en **Valdoria**, una nación dura donde el poder, la política y la corrupción mandan. Mina, lee el mercado, negocia y asciende sin cambiar el país, pero cambiando su lugar en él.

## Estructura

```
.
├── game/      el juego (proyecto Godot, aún vacío)
├── studio/    todo lo de gestión del proyecto: diseño, roadmap, tareas, arte de referencia, hub
└── README.md
```

- `game/` compila **sin** `studio/`; `studio/` no importa nada de `game/`.
- `studio/` se puede ignorar o extraer a otro repositorio con su historial. Ver [studio/README.md](studio/README.md).

## Ver el estudio (documentos, roadmap, tablero, arte)

Primero genera los datos (el archivo `studio/hub/data.js` no se versiona) y luego abre `studio/hub/index.html` en el navegador. No necesita servidor ni internet.

Después de cambiar documentos o datos, se regenera con:

```bash
python3 studio/hub/build.py
```

## Calidad y flujo de trabajo

El proyecto se trabaja **por ramas**, con **arquitectura modular verificada automáticamente** y **QA como etapa del flujo** (`backlog → sprint → doing → review → qa → done`). Resumen en [CONTRIBUTING.md](CONTRIBUTING.md); detalle en `studio/docs/` (documentos 14, 15 y 16 y decisiones en `adr/`).

## Estado

Fase 0 (diseño) casi completa. Siguiente: marca, storyboard y preparación técnica. Detalle en el hub, sección Roadmap.

## Derechos

Código y diseño visibles solo para consulta. **Todos los derechos reservados** (ver [LICENSE](LICENSE)): no se permite usar, copiar ni redistribuir nada de este repositorio. No se aceptan contribuciones externas por ahora.

El arte de referencia está generado con IA (gpt_image_2_5 vía Higgsfield), es **provisional** y no está licenciado para uso; se rehará en pixel art con PixelLab. Problemas de seguridad: [SECURITY.md](SECURITY.md).
