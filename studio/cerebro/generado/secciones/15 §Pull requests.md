---
id: "doc-15-pull-requests"
tipo: "seccion"
title: "Pull requests 🟡"
aliases: ["doc-15-pull-requests"]
documento: "[[15 Flujo de trabajo y calidad]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[15 §Flujo de una tarea]]"
siguiente: "[[15 §Integración continua]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:80"
generado: true
---

# Pull requests 🟡

← [[15 §Flujo de una tarea]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Integración continua]] →

- **Pequeños:** idealmente menos de ~400 líneas de cambio.
- **Título** con la misma convención que los commits (se usa al hacer *squash*).
- **Plantilla** con qué, por qué, cómo se probó, evidencias y lista de verificación (`.github/pull_request_template.md`).
- Se **fusionan con squash** para mantener `main` lineal y legible.

### Lista de revisión 🟡

- **Arquitectura:** ¿respeta capas y módulos? ¿pasa el verificador? ¿algo debería estar en otro módulo?
- **Claridad:** nombres, funciones cortas, sin duplicación ni código comentado.
- **Pruebas:** el dominio y los casos de uso nuevos tienen pruebas; los errores corregidos, una prueba que los reproduce.
- **Datos:** el contenido nuevo está en datos validados y no en el código.
- **Textos:** pasan por traducción (ES y EN); nada incrustado en el arte.
- **Seguridad y privacidad:** sin secretos, sin datos personales en telemetría, entradas validadas.
- **Rendimiento:** sin trabajo costoso en cada cuadro; sin asignaciones innecesarias.
- **Accesibilidad:** no depende solo del color; funciona con ratón y teclado y con mando (el táctil, en la fase móvil).
- **Documentación:** actualizada si cambió el comportamiento o la arquitectura.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:80`
