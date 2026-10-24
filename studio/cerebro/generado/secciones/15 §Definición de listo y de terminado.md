---
id: "doc-15-definicion-de-listo-y-de-terminado"
tipo: "seccion"
title: "Definición de listo y de terminado 🟡"
aliases: ["doc-15-definicion-de-listo-y-de-terminado"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Integración continua]]"
siguiente: "[[15 §Limpieza del diseño]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:111"
generado: true
---

# Definición de listo y de terminado 🟡

> Lista para empezar (Definition of Ready): tiene descripción y "listo cuando", prioridad, estimación de hasta 20 horas y no depende de algo…

← [[15 §Integración continua]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Limpieza del diseño]] →

**Lista para empezar (Definition of Ready):** tiene descripción y "listo cuando", prioridad, estimación de hasta 20 horas y no depende de algo sin resolver.

**Terminada (Definition of Done):**

- [ ] Cumple su "listo cuando".
- [ ] Respeta la arquitectura (verificador en verde).
- [ ] Tiene pruebas y pasan.
- [ ] Pasó **QA**: casos de prueba aprobados, sin errores S1 o S2 abiertos, y resultado registrado.
- [ ] Formato y lint sin avisos.
- [ ] Textos en ES y EN; sin cadenas fijas.
- [ ] Documentación y registro de decisiones al día si corresponde.
- [ ] Si toca documentos de diseño: la limpieza no baja, lo que queda sin cerrar está marcado como diferido, con su tarea, y no hay conexiones rotas (hub, «Limpieza del diseño»).
- [ ] Si crea imágenes o audio de prueba: van marcados como provisionales en `studio/data/assets.json` (campo `estado`) y no se pulen ([[12 Dirección de arte|12]]).
- [ ] Evidencia en la tarea (captura, resultado de pruebas o nota).
- [ ] PR revisado y fusionado.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:111`
