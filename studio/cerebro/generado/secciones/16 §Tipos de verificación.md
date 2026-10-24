---
id: "doc-16-tipos-de-verificacion"
tipo: "seccion"
title: "Tipos de verificación 🟡"
aliases: ["doc-16-tipos-de-verificacion"]
documento: "[[16 Calidad y QA]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[16 §El QA en el flujo]]"
siguiente: "[[16 §Seguridad en QA]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:37"
generado: true
---

# Tipos de verificación 🟡

← [[16 §El QA en el flujo]] · [[16 Calidad y QA|↑ 16]] · [[16 §Seguridad en QA]] →

| Tipo | Qué busca | Cómo |
|---|---|---|
| **Revisión de código** | Claridad, arquitectura, deuda | PR con lista de revisión y `/code-review` |
| **Unitarias** | Reglas del dominio correctas y deterministas | GUT, sin interfaz |
| **De integración** | Módulos juntos a través de sus `api` y eventos | GUT con dobles de plataforma |
| **Funcionales / de aceptación** | Que lo diseñado funciona como se describió | Casos de prueba ejecutados en el PC de pruebas |
| **De regresión** | Que lo anterior sigue funcionando | Casos automáticos en CI y rondas manuales por bloque |
| **Exploratorias** | Lo que nadie pensó | Sesiones con un objetivo y tiempo limitado |
| **Simulación y economía** | Mercado sin trucos, inflación y estrategias dominantes | Simulador de 10.000 días y partidas completas |
| **Rendimiento** | Cuadros por segundo, memoria, arranque, tamaño | Medición en la matriz de PC contra presupuestos |
| **Compatibilidad** | Gamas de PC, resoluciones, Windows y Linux, Steam Deck, mandos | Matriz de PC |
| **Accesibilidad** | Daltonismo, tamaño de texto, contraste, teclado (TC-050), mando (TC-038) | Lista de verificación y pruebas manuales |
| **Localización** | ES y EN completos, textos que no se cortan, formatos | Pseudo-localización y revisión por pantalla |
| **Guardado y actualización** | Integridad, corrupción, migración entre versiones | Casos automáticos y manuales |
| **Instalación** | Instalar desde Steam, abrir, actualizar sin perder la partida; sincronización de la nube | Pruebas en el PC de pruebas |
| **Usabilidad** | Si se entiende y se disfruta | Playtest con personas externas |
| **Seguridad** | Ver sección siguiente | Lista de verificación y análisis estático |
| **Privacidad** | Que la telemetría no filtre datos | Revisión de lo que se guarda y exporta |
| **Contenido** | Datos válidos, textos faltantes, referencias rotas | Validación de datos en CI |

## Fuente

`studio/docs/16-calidad-y-qa.md:37`
