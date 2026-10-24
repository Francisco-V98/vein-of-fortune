---
id: "doc-15-pruebas"
tipo: "seccion"
title: "Pruebas 🟡"
aliases: ["doc-15-pruebas"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Limpieza del diseño]]"
siguiente: "[[15 §Versionado y publicación]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:178"
generado: true
---

# Pruebas 🟡

← [[15 §Limpieza del diseño]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Versionado y publicación]] →

| Nivel | Proporción orientativa | Qué cubre |
|---|---|---|
| Unitarias del dominio | ~70 % | Reglas puras, deterministas, sin Godot de por medio |
| Casos de uso con dobles | ~20 % | Servicios de `application` con puertos falsos |
| Integración y manuales | ~10 % | Varios módulos juntos y sensaciones en el dispositivo |

- Meta de cobertura del dominio: **80 % o más**.
- Las pruebas son parte de cada tarea (están incluidas en sus horas) y su resultado se registra en el catálogo de QA ([[16 Calidad y QA|16]]).
- Simulaciones largas del mercado (10.000 días) se ejecutan bajo demanda y antes de cada versión.
- Un error corregido incorpora una prueba que lo reproduce.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:178`
