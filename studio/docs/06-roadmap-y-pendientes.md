# 06 · Roadmap, ideas futuras y pendientes

## Fases tentativas 🟡

> **Reemplazado por el roadmap detallado**: `studio/data/roadmap.json` (se ve en el hub, sección Roadmap). Tiene fases F0 a F6, hitos, tareas con horas, objetivo (MVP, Release 1, Evolutivo) y estado. La tabla de abajo es el borrador original.

Borrador para ordenar el trabajo; se afinará cuando se fije el prototipo.

| Fase | Objetivo | Contenido |
|---|---|---|
| 0 · Diseño | Cerrar base de diseño | Estos documentos, lore, tabla de minerales/zonas |
| 1 · Prototipo del núcleo | Probar que el loop es divertido | 1–2 zonas, 3–4 minerales, detector instantáneo, 3 minijuegos (Picado, Perforación, Regateo), mercado simple, tienda básica, ciclo de día |
| 2 · Vertical slice | Calidad de juego real | Información por capas, noticias, herramientas con desgaste, encuentros, almacén con costos |
| 3 · Contenido | Llegar al alcance de v1 | 10 minerales, 5–6 zonas, catálogo de minijuegos, dificultad, logros, estilo de vida |
| 4 · Pulido y lanzamiento mobile | Publicar | Tutorial, balance, guardado, rendimiento, tiendas de apps |
| 5 · Después | Crecer | Capa de imperio, casino, PC/consola |

## Ideas futuras (fuera de v1)

- **Casino** ✅ (idea del autor): tragamonedas, ruleta, blackjack, quizás minijuegos de azar. Dinero del juego solamente.
  - 🟡 Nota: los juegos de azar simulados afectan la clasificación por edad en las tiendas de apps; revisar requisitos antes.
- Capa de imperio: sucursales, otras ciudades, plantillas más grandes de empleados. (Los empleados básicos entran a mitad del juego, no aquí.)
- Eventos de temporada.
- Calidad de minerales (común, buena, excelente) y requisitos de calidad en contratos.
- PvP asíncrono (descartado por ahora).
- Port a PC y consola.

## Preguntas abiertas

1. Logotipo, wordmark e ícono (ver [13](13-marca-e-identidad.md)).
2. Guion del Acto I ⏳ F0-23. Las variantes del Acto II están en [22](22-acto-ii-variantes.md).
3. Fichas completas de cada zona y de cada mineral (plantillas en 02 y 05).
4. Stats del jugador: cuáles y cómo se suben.
5. Tutorial: cómo se enseña a leer el mercado.
6. ¿Legado aplica a todas las dificultades o solo hardcore?
7. Motor y arquitectura técnica (decisión posterior).
8. Estilo visual concreto: referencias de arte.
9. Cómo se maneja "saltar" un bloque de tiempo.

## Registro de decisiones

| Fecha | Decisión |
|---|---|
| 2026-10-10 | Mobile primero; futuro PC/consola |
| 2026-10-10 | Single-player con mercado simulado |
| 2026-10-10 | Pago único |
| 2026-10-10 | Mínimo 10 minerales con lore y utilidad |
| 2026-10-10 | Información por capas (gratis → pago, cada vez más visual) |
| 2026-10-10 | Zonas con probabilidades y peligros propios, desbloqueo por etapas |
| 2026-10-10 | Encuentros con decisión + peligros ambientales |
| 2026-10-10 | Una sola moneda; sin final fijo; árbol de logros |
| 2026-10-10 | Dificultades: novato, intermedio, difícil, hardcore (permadeath) |
| 2026-10-10 | Legado tipo Balatro + salón de la fama |
| 2026-10-10 | Ambientación: era industrial con toque fantástico |
| 2026-10-10 | Casino: versión futura |
| 2026-10-10 | Día de 3 bloques (mañana, tarde, noche) |
| 2026-10-10 | Mundo: nación en revolución industrial con varias regiones |
| 2026-10-10 | Sociedad dura: poder, corrupción, extorsión; política influye en la partida |
| 2026-10-10 | Tono serio y realista; protagonista optimista |
| 2026-10-10 | Eventos sociales: apagones, huelgas, saqueos |
| 2026-10-10 | Estilo visual: pixel art tipo Dave the Diver, estética Papers Please, retrofuturismo tipo Fallout |
| 2026-10-10 | Sonido: referencia Balatro |
| 2026-10-10 | Época: retrofuturismo industrial, sin apocalipsis (reemplaza "industrial con toque fantástico") |
| 2026-10-10 | Nación: República de Valdoria; 5 regiones + capital |
| 2026-10-10 | 6 zonas de minado y 10 minerales con distribución por zona |
| 2026-10-10 | 5 facciones aceptadas (hoy 6 en el registro, con la Comisión del Éter dentro del Ministerio; ver 07) |
| 2026-10-10 | Historia en 4 actos, luego sandbox; sin final definitivo |
| 2026-10-10 | Gancho: heredar licencia, puesto y deuda de un tío (hoy: que murió en público hace dos años; ver 08) |
| 2026-10-10 | Facciones con nombre: Ministerio de Recursos, Consorcio Arvel, la Unión, Los Faroleros; tres medios de prensa |
| 2026-10-10 | Tío Anselmo Vidal con cintas de grabación; Doña Reme, que cobra en nombre de una facción que cambia según la partida |
| 2026-10-10 | Elenco de 7 personajes; MVP con 4 |
| 2026-10-10 | Verdad de la Aetherita (enferma a quien la extrae) con 3 salidas en el Acto IV |
| 2026-10-10 | La historia cambia según las decisiones del jugador |
| 2026-10-11 | Tres ejes de progreso: capacidad, habilidad, influencia |
| 2026-10-11 | 5 stats (Aguante, Pericia, Ojo, Temple, Labia) que suben por uso, hitos y acciones; sin reparto manual |
| 2026-10-11 | 5 niveles por herramienta (revisable en prototipo) |
| 2026-10-11 | Empleados desde mitad del juego (mineros y dependientes, con stats mejorables) |
| 2026-10-11 | Empleados con malos stats son contraproducentes (robo, soborno, daños) |
| 2026-10-11 | Empleados con contrato por tiempo: despido, vencimiento o renovación |
| 2026-10-11 | Contratación vía periódicos (empleos y anuncios), con sesgo político de cada medio |
| 2026-10-11 | El mercado se mueve 3 veces por día (una por bloque) |
| 2026-10-11 | Calidad de minerales: después del MVP |
| 2026-10-11 | Refinado en la primera versión |
| 2026-10-11 | Mercado negro como canal propio, con indicador de vigilancia y multas |
| 2026-10-11 | Contratos de distintos tipos (estándar, urgente, largo plazo, oficial, negro) |
| 2026-10-11 | Automatización de minijuegos solo en etapas avanzadas, a probar en prototipo |
| 2026-10-11 | Escáner instantáneo en el MVP |
| 2026-10-11 | Aetherita con minijuego propio (Contención) y exposición que enferma |
| 2026-10-11 | MVP de minijuegos: Picado, Perforación, Regateo |
| 2026-10-11 | Todo se desarrolla con IA (código, arte, audio); el autor aporta diseño y pruebas |
| 2026-10-11 | Android primero; iOS solo si todo va bien |
| 2026-10-11 | Soporte de mando con mapeo completo; el HUD táctil se oculta al usar mando |
| 2026-10-11 | Proyecto personal primero; prototipo barato y rápido para probar la diversión |
| 2026-10-11 | Seguridad: sin cuentas, anuncios ni analíticas en la v1; guardado seguro |
| 2026-10-11 | Legal: lista de verificación por etapas (ver 11) |
| 2026-10-11 | Hub visual de documentación y tablero de tareas con estados y objetivos (MVP, Release 1, Evolutivo) |
| 2026-10-11 | ~~Tablero en Trello~~ **descartado**: el tablero de tareas es interno, dentro del hub |
| 2026-10-11 | Hub visual de documentación: **sitio local** |
| 2026-10-11 | Paleta: fríos con **vinotinto** como acento principal; industrial retrofuturista |
| 2026-10-11 | Prueba de estilo realizada (ver 12): dirección válida, pero la IA da referencias, no assets directos |
| 2026-10-11 | El juego es horizontal (landscape) |
| 2026-10-11 | Aetherita: cristal vinotinto translúcido con brillo rojo-rosado; es el mineral más llamativo |
| 2026-10-11 | Dos tipos de personaje: retrato detallado de diálogo y sprite pequeño tipo Stardew |
| 2026-10-11 | Acento secundario: latón/ámbar (elegido) |
| 2026-10-11 | Edificios en isométrica con vista interior en corte transversal |
| 2026-10-11 | Hub visual local construido (carpeta `studio/hub/`) y roadmap detallado en `studio/data/roadmap.json` |
| 2026-10-11 | Fases F0 a F6 con objetivos MVP, Release 1 y Evolutivo; estimación de F4 subida a 350–650 h tras el desglose |
| 2026-10-11 | Sin librerías de terceros en el hub (renderizador de markdown propio) |
| 2026-10-11 | Valdoria se mantiene como nombre del mundo; el título del juego será un nombre distinto, válido o traducible en español e inglés |
| 2026-10-11 | Juego en español e inglés desde el inicio, con marco de traducción para más idiomas |
| 2026-10-11 | Voz: español neutro latinoamericano con tuteo; inglés igual de cercano |
| 2026-10-11 | Estructura aprobada: `game/` y `studio/` en un repositorio; `studio/` ignorable o extraíble |
| 2026-10-11 | Telemetría por capas aprobada: local exportable, Google Play Vitals y envío opcional futuro |
| 2026-10-11 | Se añaden storytelling y storyboard (story map, guion del Acto I, paneles, flujo de pantallas) |
| 2026-10-11 | Estimación total revisada a unas 850–1.450 h por idiomas, marca, storyboard y métricas |
| 2026-10-11 | Casino: primera actualización tras el lanzamiento, integrado de forma suave (tragamonedas, ruleta y blackjack); el autor acepta la clasificación por edad que corresponda |
| 2026-10-11 | El título debe orbitar la idea de "fortuna" (suerte y riqueza); candidato inicial: Veta de Fortuna / Vein of Fortune |
| 2026-10-11 | **Título elegido:** Veta de Fortuna (ES) / Vein of Fortune (EN), localizado por idioma |
| 2026-10-11 | Reorganización en `game/` y `studio/`; el hub pasa a `studio/hub/` |
| 2026-10-11 | Tareas con historial, comentarios y evidencias; el estado solo lo cambia Claude y el build valida su coherencia |
| 2026-10-11 | **Motor confirmado:** Godot 4.x con GDScript |
| 2026-10-11 | Extracción de `studio/` probada en local con `git subtree split` y `git sparse-checkout` |
| 2026-10-11 | Backlog desglosado de 190 a 423 tareas de 2 a 20 horas, con prioridad P0 a P3 |
| 2026-10-11 | Prioridades: P0 indispensable, P1 importante, P2 deseable, P3 opcional; el hub permite recortar el alcance y ver la línea de tiempo en horas |
| 2026-10-11 | **Estimación revisada al desglosar:** unas 2.200 h base hasta el lanzamiento (rango 1.700–3.050 h); solo P0 son unas 750 h y P0 con P1, unas 1.850 h. Reemplaza la cifra de 850–1.450 h |
| 2026-10-11 | **Requisito:** trabajo por ramas, clean code, arquitectura muy modular sin dependencias directas, escalable, con scaffolding y buenas prácticas |
| 2026-10-11 | Arquitectura por módulos con capas, api pública, eventos de dominio y puertos/adaptadores, verificada automáticamente (ADR-0003, 0004, 0006: propuestas) |
| 2026-10-11 | Flujo de ramas GitHub Flow con ramas de versión y Conventional Commits con ID de tarea (ADR-0005: propuesta) |
| 2026-10-11 | **QA como etapa del flujo:** `backlog → sprint → doing → review → qa → done`; catálogo de 49 casos de prueba, registro de errores por severidad y criterios de salida (ADR-0008: propuesta) |
| 2026-10-11 | Estimación revisada: unas 2.480 h base hasta el lanzamiento (P0 947 h, P0 y P1 2.131 h); la metodología, el scaffolding y el QA suman unas 280 h. Puertas de decisión en la hora 485 y la 840 |
| 2026-10-11 | El archivo generado `hub/data.js` deja de versionarse (evita conflictos entre PR); se crea con `build.py` |
| 2026-10-11 | El modelo de ramas (ADR-0005) queda **aceptado** por el autor; el resto de propuestas, de acuerdo con el plan |
| 2026-10-11 | **Aceptados** los ADR 0003, 0004, 0005, 0006 y 0008 al fusionar el PR #2 |
| 2026-10-11 | Fusionados en main los PR #3 (herramientas y CI), #2 (documentos) y #1 (estado QA y catálogo); la CI de GitHub pasa en todos |
| 2026-10-11 | CLI de GitHub instalada y autenticada; los PR se crean desde la terminal |
| 2026-10-10 | Personaje personalizable: nombre de una palabra, tienda con espacios, hombre o mujer (1 modelo de cada uno en v1) |
| 2026-10-12 | Medidores de relación: solo cuatro (Unión, Esteban, Lucía y Teo); el Consorcio, el Ministerio y Los Faroleros se miden por la alianza elegida |
| 2026-10-12 | Cuota de la deuda del Acto I cada 7 días, la primera el día 7; si no puedes pagarla, una semana más con un pequeño recargo (montos ⏳ F0-52) |
| 2026-10-12 | Aetherita en el Acto III: precio visible y compra solo en el mercado negro (Casilda), como mercancía escasa; la extracción llega en el IV |
| 2026-10-12 | El Acto I empieza con un detector básico heredado de Anselmo; el cuarzo lo mejora más adelante |
| 2026-10-12 | Vigilancia: un indicador global de 0 a 100 que sube con las operaciones negras; los cambios se cuentan en puntos |
| 2026-10-12 | Escalera de estatus: el primer escalón se llama «Heredero» (*Heir*) y los cinco nombres quedan decididos |
| 2026-10-12 | Colores: la subida de los gráficos va en azul hielo y el farol de Los Faroleros es vinotinto mate con luz ámbar; el cian y el rojo-rosado son solo de la Aetherita |
