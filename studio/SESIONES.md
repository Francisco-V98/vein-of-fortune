# Registro de sesiones

Generado por `python3 tools/sesion.py md` desde `studio/data/sesiones.json`; no lo edites a mano.
Para saber qué se hizo en una sesión: `python3 tools/sesion.py ver N` o `buscar <tarea, PR o texto>`.

| Sesión | Fecha | Tareas | PR | Qué hizo |
|---|---|---|---|---|
| S-01 · F0-85 a F0-94 Diseño de exploración, simulador y calendario | 2026-10-24 | F0-91, F0-92, F0-93, F0-94, F0-95, F0-96 | #60, #62, #63, #64, #65, #67 | Rediseñó la exploración (mapa con niebla, tren, asentamientos y minas caminables, ADR-0011), recalibró el simulador de minas, batería y cierres, creó el calendario con estaciones, clima y mini-historias (documento 29), el registro de sesiones y arregló el CI del simulador. |
| S-02 · F0-25 Flujo de pantallas | 2026-10-24 | F0-25, F2-41, F0-97 | #66, #68 | Definió el flujo de pantallas: documento 30 con 18 nodos, transiciones con coste, mapa por estado, guardado y mando; añadió la tarea F2-41 (título, selector de 5 partidas y pausa) y alineó docs 01, 02, 10, 26, 27 y el ADR-0011. |
| S-03 · F0-24 Storyboard del Acto I | 2026-10-24 | F0-24, F2-08 | — | F0-24: storyboard (15 imágenes), vista Semana 1 del hub con 28 escenas ilustradas (7 + 21 nuevas, medio 1k, ~11 créditos; total tarea ≈26,8) y 6 decisiones del autor aplicadas en docs 23, 27 y 30 F2-08 30 23 |

## S-01 · F0-85 a F0-94 Diseño de exploración, simulador y calendario
- Documentos: 26, 28, 29
- El tren es el único medio entre zonas
- Boca de mina = recinto de 5 entradas a ciegas
- Estaciones y clima por tinte de paleta, sin hojas nuevas

## S-02 · F0-25 Flujo de pantallas
- Documentos: 30
- Menús D: libreta de consulta global + pausa aparte
- Mercado al contado solo en edificios
- Mapa bloqueado en mina, minijuego, loader y tren; salto a la puerta
- Minijuegos como capa sobre la escena
- Detector con mando LB/RB + X
- Bloque de expedición al cruzar la entrada, se devuelve si no picas
- Esperar en la barra superior con confirmación

## S-03 · F0-24 Storyboard del Acto I
- Documentos: 27, 30, 23
- opción C: panel base y variantes editadas
- protagonista hombre como ejemplo
- encuadre de la cámara real del juego
- ramas de d7.2 en tabla HTML
- capital = Puerto Meridiano
- la cola no suelta d7.3 sin d1.6 y d5.2
- callar con rumor de reserva también publica el titular
- margen y gestión contra efectivo total
- sin mapa interno en el MVP
- pedido de 8 sacos y hierro de la mejora a F2-08
