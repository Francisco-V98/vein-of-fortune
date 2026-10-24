---
id: "doc-14-estructura-de-game"
tipo: "seccion"
title: "Estructura de `game/` 🟡"
aliases: ["doc-14-estructura-de-game"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Principios]]"
siguiente: "[[14 §Capas dentro de un módulo]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:20"
generado: true
---

# Estructura de `game/` 🟡

← [[14 §Principios]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Capas dentro de un módulo]] →

```
game/
├── project.godot
├── architecture.json          módulos y dependencias permitidas (lo lee el verificador)
├── src/
│   ├── kernel/                tipos base compartidos: Result, ids, eventos, azar con semilla
│   ├── platform/
│   │   ├── ports/             contratos: entrada, almacenamiento, audio, idioma, reloj, háptica, tienda, pantalla
│   │   └── adapters/          implementaciones (ratón y teclado, mando, Steam, PC, pruebas; después táctil y móvil); solo `app` las conoce
│   ├── ui_kit/                tema, tokens de diseño y componentes de interfaz reutilizables
│   ├── modules/
│   │   └── <módulo>/
│   │       ├── domain/            reglas puras (RefCounted/Resource); sin nodos ni UI
│   │       ├── application/       casos de uso y servicios; define los puertos que necesita
│   │       ├── infrastructure/    adaptadores del módulo (carga de datos, persistencia)
│   │       ├── presentation/      escenas y presentadores (interfaz)
│   │       ├── api/               lo único que otros módulos pueden usar (fachada y eventos)
│   │       ├── data/              definiciones de contenido del módulo
│   │       └── tests/
│   └── app/                   raíz de composición: arranque, registro de módulos, navegación
├── assets/                    arte, audio y fuentes con convención de nombres
├── locales/                   traducciones .po (ES, EN)
└── tests/                     pruebas de integración entre módulos
```

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:20`
