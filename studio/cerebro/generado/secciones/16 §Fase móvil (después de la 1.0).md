---
id: "doc-16-fase-movil-despues-de-la-1-0"
tipo: "seccion"
title: "Fase móvil (después de la 1.0)"
aliases: ["doc-16-fase-movil-despues-de-la-1-0"]
documento: "[[16 Calidad y QA]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[16 §Presupuestos de rendimiento (a medir en PC F1-44)]]"
siguiente: "[[16 §Métricas de calidad]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:150"
generado: true
---

# Fase móvil (después de la 1.0)

> Se conserva lo previsto para Android y se retoma cuando empiece el móvil (10, «Fase móvil»).

← [[16 §Presupuestos de rendimiento (a medir en PC F1-44)]] · [[16 Calidad y QA|↑ 16]] · [[16 §Métricas de calidad]] →

Se conserva lo previsto para Android y se retoma cuando empiece el móvil ([[10 Técnico y herramientas|10]], «Fase móvil»).

| Tema | Contenido previsto |
|---|---|
| Gamas y versiones | Android de gama baja, media y alta; la versión más reciente y la mínima soportada (a decidir) |
| Proporciones | 16:9, 19.5:9 y 20:9 con zona segura |
| Entrada | Táctil y mando Bluetooth |
| Rendimiento | Arranque en frío ≤ 5 s en gama media; 60 cuadros por segundo en interfaz y mínimo 30 en minijuegos; descarga ≤ 150 MB; batería y calor a medir (los números del plan anterior son 🟡 y se revisan entonces) |
| Telemetría | Android vitals de Google Play ([[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro\|ADR-0007]]) |
| Seguridad | APK, manifiesto con permisos mínimos y firma gestionada por Google Play |
| Pruebas | Android del autor, emuladores y equipos prestados; iOS con su propia tarea |
| Casos | Los casos de toque se mantienen en el catálogo con la etiqueta «fase móvil» |

## Fuente

`studio/docs/16-calidad-y-qa.md:150`
