---
name: modo-conciso
description: Reglas para gastar menos tokens en este proyecto: formato corto de informes de subagentes, encargos mínimos, lectura parcial y lotes. Úsala al lanzar o resumir subagentes, al escribir un encargo largo o cuando el contexto de la sesión sea grande.
---

# Modo conciso del proyecto

Aplícala al coordinar subagentes y a los informes que vuelven al hilo principal. Con el autor sigue hablando en español claro, sin recortar las decisiones ni las preguntas.

## Encargo a un subagente
1. Rol y etapa: una línea. Modelo y esfuerzo según `studio/data/equipo.json`.
2. Si el contexto pasa de ~25 líneas, guárdalo en un archivo del scratchpad y escribe solo: «Lee <ruta>. Tu parte: <archivos>. No toques: <archivos>».
3. Pide el entregable concreto y el formato del informe (abajo). No pegues documentos ni repitas decisiones que el agente puede leer en el briefing.

## Formato del informe (máx. 60 líneas / 6.000 caracteres)
```
Resultado: <2 líneas: hecho / con fallos / bloqueado>
Archivos: <rutas>
Hallazgos o cambios:
| archivo:línea | qué | acción |
Dudas para el autor: <lista corta, con recomendación>
```
- Analista: añade la clasificación SIN PREGUNTAR / DECIDIR AHORA / APLAZAR ⏳ ID en la misma tabla, no en prosa.
- QA: «aprobado» o «con fallos» y la lista `archivo:línea`; nada de repetir lo que pasó.

## Lectura
- `grep -n` y rangos antes de leer; `tools/consulta.py` cuando exista; nunca `data.js` ni `resultados.json` enteros.
- Una lectura completa por documento grande y por agente, como mucho.

## Lotes y sesión
- Agentes independientes: se lanzan juntos y se resumen juntos.
- Cada hand-back que llega al hilo principal cuesta un turno con todo el contexto: pide informes cortos y procésalos en bloque.
- Al fusionar la tarea: `/compact` o sesión nueva.
