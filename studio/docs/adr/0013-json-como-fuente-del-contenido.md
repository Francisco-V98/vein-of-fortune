# ADR-0013 · JSON como fuente del contenido

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-24

## Contexto

[ADR-0006](0006-contenido-como-datos.md) decidió que el contenido (minerales, zonas, herramientas, eventos, noticias, facciones) vive en datos validados, pero no fijó el formato: el documento [10](../10-tecnico-y-herramientas.md) decía «JSON/recursos». Las cifras del mundo ya están en `studio/data/world.json`, que leen el simulador en Python, el hub y los agentes del estudio. La revisión técnica de F0-57 lo planteó como decisión pendiente.

## Decisión ✅

Decisión del autor (2026-10-24):

1. El contenido del juego se escribe en archivos **JSON** con esquema; son la **única fuente**.
2. Al arrancar, la `infrastructure` de cada módulo lee su JSON, lo **valida** contra el esquema y lo convierte en **objetos tipados de solo lectura** del dominio. Un dato inválido detiene el arranque con un mensaje claro.
3. Los `.tres` no son fuente de contenido. Se pueden usar para piezas del motor (temas de `ui_kit`, escenas, materiales), nunca para cifras ni textos del juego.

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| **Recursos `.tres` como fuente** | Se editan cómodos en el inspector de Godot, pero el simulador en Python, el hub y los agentes no los leen sin un traductor, y habría dos fuentes de las mismas cifras |
| **Mezcla JSON y `.tres` según el tipo** | Dos formatos que mantener y validar; no queda claro dónde vive cada número |
| **CSV u hojas de cálculo** | Cómodo para tablas planas, pobre para datos anidados (mezclas de minerales, entradas de mina) y sin tipos |

## Consecuencias

- Una sola fuente para el juego, el simulador y el hub: cambiar una cifra en JSON y reejecutar `python3 tools/sim/run.py --completo --escribir` sigue siendo el flujo de balance.
- Hacen falta esquemas y un cargador validado por módulo, con pruebas (F1-33). Las conversiones a objetos tipados se escriben a mano en `infrastructure` y no hay edición visual en el inspector.
- Los guardados también son JSON con versión, pero son otro asunto: los regula el documento [14](../14-arquitectura-y-modularidad.md) («Datos y persistencia»).
- Los textos traducibles siguen en `.po` (documento 10); el JSON guarda las claves, no las frases.

## Verificación

- Pruebas del cargador: un JSON válido produce objetos tipados y uno inválido falla con un mensaje que nombra el archivo y el campo.
- El verificador de arquitectura sigue impidiendo que el dominio use `FileAccess` (regla A4): solo `infrastructure` lee archivos.
