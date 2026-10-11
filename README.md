# Veta de Fortuna · Vein of Fortune

Juego de gestión, minería y comercio para móvil (Android primero), en pixel art, horizontal, de un jugador y pago único. Español e inglés desde el inicio.

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

Abre `studio/hub/index.html` en el navegador. No necesita servidor ni internet.

Después de cambiar documentos o datos, se regenera con:

```bash
python3 studio/hub/build.py
```

## Calidad y flujo de trabajo

El proyecto se trabaja **por ramas**, con **arquitectura modular verificada automáticamente** y **QA como etapa del flujo** (`backlog → sprint → doing → review → qa → done`). Resumen en [CONTRIBUTING.md](CONTRIBUTING.md); detalle en `studio/docs/` (documentos 14, 15 y 16 y decisiones en `adr/`).

## Estado

Fase 0 (diseño) casi completa. Siguiente: marca, storyboard y preparación técnica. Detalle en el hub, sección Roadmap.

## Derechos

Todos los derechos reservados por ahora. El arte de referencia está generado con IA y sus términos de uso comercial están por revisar antes de publicar.
