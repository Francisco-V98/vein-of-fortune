# ADR-0011 · Exploración caminable, tren y minas con entradas

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-24

## Contexto

Hasta ahora el mundo era un mapa de zonas con edificios isométricos que, al tocarlos, abrían directamente su vista interior; la expedición era un bloque con Aguante y 2 o 3 menas elegidas al inicio, y viajar era una elección de menú. El autor pidió el 2026-10-24 más dinamismo («no importa el tiempo ni el costo»): caminar por los asentamientos, entrar a las edificaciones, caminar por la mina y viajar en tren. Es un ajuste que toca el diseño de [01](../01-core-loop.md), [02](../02-extraccion.md), [09](../09-minijuegos.md), [12](../12-direccion-de-arte.md), [26](../26-zonas-y-edificios.md), [28](../28-numeros-base-de-la-economia.md), el simulador y el roadmap.

## Decisión ✅

Decisiones del autor (2026-10-24):

1. **Tres vistas:** exterior de los asentamientos en **vista aérea** (tipo Stardew, se rodean las edificaciones); **interior** de cada edificación en corte transversal con **desplazamiento lateral plano** (tipo Pet Society); **mina** en **vista aérea cenital**. Entrar o salir pasa por un loader corto.
2. **Edificaciones:** las 46 deben poder entrarse a futuro; se construyen las necesarias y las demás muestran «puerta cerrada».
3. **Minas:** la boca de mina es una edificación; el recinto tiene **5 entradas** (2 escasas, 2 medias, 1 abundante), sorteadas cada día **a ciegas** con una semilla determinista `hash(partida, día, mina, entrada)`. Cada entrada es una galería de 2 a 3 pantallas con el doble de menas visibles que de picables (Acto I 5–6, II 8, III 14, IV 18; cifras de partida).
4. **Detector con batería:** un clic en una mena gasta 1 carga y muestra el rango de composición con promedio (desplazado respecto al valor real), el rango de cantidad y un color (gris, ámbar o verde). Batería de 6, 8, 11 y 14 cargas según el nivel; recarga entera y gratis cada noche; pilas opcionales desde el Acto II (máximo 1 al día).
5. **Cambio de entrada:** una vez por mina y día, sin devolver la batería gastada. La calidad de la entrada cambia solo las cantidades (×0,7, ×1,0, ×1,6; en el Acto I abanico estrecho 0,85/1,0/1,3) y no la mezcla de minerales.
6. **Herramienta:** el desgaste actual se mantiene y por debajo del 20 % de integridad queda «mellada» (margen del minijuego −30 %); el descarte al 25 % desaparece (lo sustituye la carga del detector).
7. **Cierres:** un problema social o político cierra 1, 2 o 3 entradas de la mina afectada (orden abundante, media, escasa; siempre al menos 2 abiertas), con presión sobre las abiertas (×0,95, ×0,88, ×0,75). Cierre total solo como excepción de guion.
8. **Mapa, niebla y tren:** el mapa se abre desde cualquier lugar; la niebla cubre las zonas bloqueadas hasta que el acto las abre; el tren es el único medio entre zonas (billete de 42 a 210 esquirlas) con una escena modular de unos 6 s, saltable desde el segundo viaje. Caminar, loader y tren no consumen bloques.
9. **Técnica y arte:** resolución base **640×360** (cierra F1-06), sprite de paseo de 32 a 48 px, tres tipos de arte por personaje y caminar con reposo con respiración en 8 direcciones. Módulos nuevos `world` y `exploration` ([14](../14-arquitectura-y-modularidad.md)). Guardado solo en puntos seguros. Móvil y táctil: ⏳ F6-72.

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| **Isométrico con vista fija** (lo anterior) | Descartada por el autor: no permite caminar ni rodear las edificaciones; no da el dinamismo pedido |
| **Minas laterales** (galerías en corte como `mina-horizontal.png`) | El autor reserva la vista lateral plana para los interiores; la mina cenital deja caminar entre varias menas, como en Stardew |
| **Pisos tipo Stardew** (la mina como pisos que se bajan) | Se parece a otro juego y rompe el recinto de cinco entradas con reparto a ciegas y cambio único; el recinto da la decisión de riesgo |
| **Tren por andén obligatorio** (caminar hasta el andén y subir) | Alarga el viaje sin decisión nueva; las estaciones quedan como referencia y la mecánica se reevalúa en otra versión si al jugar no resulta fastidiosa |

## Consecuencias

- **Arte:** los edificios isométricos F4-155 y F4-156 se cancelan y se rehacen como exteriores cenitales; hacen falta interiores laterales, el recinto de cinco entradas, 30 trazados de mina (5 por mina), una escena de tren con fondos de ventanilla por región y la niebla. El personaje pasa de «casi estático» a caminar en 8 direcciones ([12](../12-direccion-de-arte.md)), lo que sube F4-227, F4-233 y F4-190 a F4-193.
- **Horas:** unas +380 a +550 h en total (F0 +40–60, F1 +15–22, F2 +30–45, F3 +65–95, F4 +230–330), con tareas nuevas de motor de paseo, interiores, recinto y sorteo, detector y batería, generador de menas, tren, niebla, cierres, estado de partida, simulador y QA.
- **Simulador y economía:** `economy.expedition`, `zone_mix` (media de las cinco entradas), `economy.energy` (desaparece el descarte) y `economy.tools.detector` (batería) se rehacen en ⏳ F0-92; hasta entonces `world.json` no cambia las claves que lee el simulador y las cifras nuevas viven en claves que no lee. Reglas nuevas previstas: más cierres rinden menos, cambiar de entrada da entre +5 y +10 %, la batería se queda corta entre el 30 y el 60 % de los días, los empleados rinden la media de las abiertas y el tiempo de paseo no mueve el ingreso por hora más de ±20 %.
- **Riesgos:** tres límites a la vez (Aguante, batería y desgaste), más varianza por el sorteo a ciegas, 46 interiores laterales y un Acto I con paseo libre que puede perder al jugador (cola de escenas y diario, F3-48).
- **Rendimiento:** la base 640×360 es ligera; se mide en Steam Deck con ⏳ F1-44.

## Verificación

- Casos de QA de colisión, loader, sorteo diario, cambio único, batería, cierres, niebla y tren ([16](../16-calidad-y-qa.md)).
- `python3 tools/sim/run.py --completo --escribir` reejecutado con las cifras nuevas (⏳ F0-92) y simulador «50 de 50 · vigente».
- `python3 studio/hub/build.py --strict` sin avisos de coherencia ni bajada de limpieza.
- Prototipo: el tiempo real de paseo (unos 40 s por mina) se mide y se absorbe al recalibrar el ritmo por hora.
