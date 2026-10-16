# 06 · Roadmap, ideas futuras y pendientes

## Fases tentativas 🟡

> **Reemplazado por el roadmap detallado**: `studio/data/roadmap.json` (se ve en el hub, sección Roadmap). Tiene fases F0 a F6, hitos, tareas con horas, objetivo (MVP, Release 1, Evolutivo) y estado. La tabla de abajo es el borrador original.

Borrador para ordenar el trabajo; se afinará cuando se fije el prototipo.

✅ **PC primero** (decisión del autor, 2026-10-15): el proyecto Godot corre en PC (Windows y Linux) desde la F1, la F5 lanza en Steam y el móvil (Android e iOS) es una fase propia posterior a la F6, cuando la 1.0 esté publicada y estable. Las horas y los IDs de tareas los reordena el roadmap, no este borrador.

| Fase | Objetivo | Contenido |
|---|---|---|
| 0 · Diseño | Cerrar base de diseño | Estos documentos, lore, tabla de minerales/zonas |
| 1 · Prototipo del núcleo | Probar que el loop es divertido | 1–2 zonas, 3–4 minerales, detector instantáneo, 3 minijuegos (Picado, Perforación, Regateo), mercado simple, tienda básica, ciclo de día |
| 2 · Vertical slice | Calidad de juego real | Información por capas, noticias, herramientas con desgaste, encuentros, almacén con costos |
| 3 · Contenido | Llegar al alcance de v1 | 10 minerales, 5–6 zonas, catálogo de minijuegos, dificultad, logros, estilo de vida |
| 4 · Pulido y lanzamiento en Steam | Publicar | Tutorial, balance, guardado, rendimiento, Steam Deck, página y lanzamiento en Steam |
| 5 · Después | Crecer | Capa de imperio, casino y, como fase propia, el móvil (Android e iOS); consolas evaluadas aparte |

## Ideas futuras (fuera de v1)

- **Casino** ✅ (idea del autor): tragamonedas, ruleta, blackjack, quizás minijuegos de azar. Dinero del juego solamente. Es la V2.0 y se llama Salón del Farol (decisión del autor, 2026-10-13; [26](26-zonas-y-edificios.md)).
- **Estilo de vida ampliado** ✅ (idea del autor): casas y mansiones por zona, joyería comprable, vehículos, ropa y decoración, y mar e inversiones. Casas, mansiones, decoración, joyería, concesionaria y sastrería van en la V2.1; mar e inversiones, en la V2.2 (decisión del autor, 2026-10-13; [26](26-zonas-y-edificios.md)).
  - 🟡 Nota: los juegos de azar simulados afectan la clasificación por edad en las tiendas (Steam y, después, las de apps); revisar requisitos antes.
- Capa de imperio: sucursales, otras ciudades, plantillas más grandes de empleados. (Los empleados básicos entran a mitad del juego, no aquí.)
- Eventos de temporada.
- **Evolutivo ✅ (decisión del autor, 2026-10-15):** consumibles de recarga de energía y similares: versiones futuras, mucho después de la V1, sin tarea ni fecha.
- Calidad de minerales (común, buena, excelente) y requisitos de calidad en contratos.
- PvP asíncrono (descartado por ahora).
- Móvil (Android e iOS) ✅, después de la 1.0 publicada y estable en Steam, con un adaptador táctil (2026-10-15). Consolas: se evalúan aparte, sin compromiso.

## Preguntas abiertas

1. Logotipo, wordmark e ícono (ver [13](13-marca-e-identidad.md)).
2. Guion del Acto I ✅: aprobado por el autor el 2026-10-13 y con sus propuestas confirmadas el 2026-10-16, sin ninguna pendiente ([27](27-guion-del-acto-i.md)). Las variantes del Acto II están en [22](22-acto-ii-variantes.md).
3. Fichas completas de cada zona (⏳ F2-10 y ⏳ F4-02 a ⏳ F4-22) y de cada mineral (plantilla en 05).
4. Tutorial: cómo se enseña a leer el mercado.
5. Motor y arquitectura técnica (decisión posterior).
6. Estilo visual concreto: referencias de arte.

Resueltas el 2026-10-15: las stats del jugador ([04](04-progresion-y-meta.md)), el legado (aplica a todas las dificultades) y cómo se salta un bloque (botón «Esperar», [01](01-core-loop.md)).

## Registro de decisiones

| Fecha | Decisión |
|---|---|
| 2026-10-10 | ~~Mobile primero; futuro PC/consola~~ (reemplazada el 2026-10-15: PC primero, móvil después) |
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
| 2026-10-11 | ~~Android primero; iOS solo si todo va bien~~ (reemplazada el 2026-10-15: PC primero, móvil después) |
| 2026-10-11 | Soporte de mando con mapeo completo (se mantiene); ~~el HUD táctil se oculta al usar mando~~ (sin HUD táctil en la 1.0, 2026-10-15) |
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
| 2026-10-11 | Telemetría por capas aprobada: local exportable, Google Play Vitals y envío opcional futuro (la capa de la tienda deja de ser Google Play Vitals desde el 2026-10-15; ver doc 10) |
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
| 2026-10-12 | Cuota de la deuda del Acto I cada 7 días, la primera el día 7; si no puedes pagarla, una semana más con un pequeño recargo (montos: cuota de 960 esquirlas el día 7 y recargo de 58 en Intermedio, [28](28-numeros-base-de-la-economia.md)) |
| 2026-10-12 | Aetherita en el Acto III: precio visible y compra solo en el mercado negro (Casilda), como mercancía escasa; la extracción llega en el IV |
| 2026-10-12 | El Acto I empieza con un detector básico heredado de Anselmo; el cuarzo lo mejora más adelante |
| 2026-10-12 | Vigilancia: un indicador global de 0 a 100 que sube con las operaciones negras; los cambios se escriben «vigilancia +N» |
| 2026-10-12 | Escalera de estatus: el primer escalón se llama «Heredero» (*Heir*) y los cinco nombres quedan decididos |
| 2026-10-12 | Colores: la subida de los gráficos va en azul hielo y el farol de Los Faroleros es vinotinto mate con luz ámbar; el cian y el rojo-rosado son solo de la Aetherita |
| 2026-10-13 | Mapa vivo: la región es la zona, con un asentamiento y la boca de mina como una edificación más; estructura mapa, zona y edificación (ver 26) |
| 2026-10-13 | V1 con unos 22 edificios: los 9 del roadmap, la Bolsa, los de historia y 6 comercios (herrería, economato, platería, lonja y salitre, tasadores y Casa Ormeño), con casa mejorable, ropa por estatus y un auto |
| 2026-10-13 | Casa Ormeño es una tienda insignia sin dueño ni medidor; la joyería comprable es otra, pequeña, y llega en la V2.1 |
| 2026-10-13 | El juego no se dirige a menores; el casino va en la V2 con moneda del juego, probabilidades visibles, tope diario e interruptor para ocultar el azar |
| 2026-10-13 | Todo el arte actual, logo incluido, es provisional; el definitivo se hace en pixel art con PixelLab tras la Puerta B (ver [12](12-direccion-de-arte.md), «Assets provisionales y definitivos») |
| 2026-10-13 | Nombres: Altafría (pueblo de empresa de Sierra Alta, *Highchill*) y Salinas Blancas (puerto de los Salares, *White Salt Flats*) |
| 2026-10-15 | Bloques: viajar y ver zonas es gratis; minar y abrir la tienda cuestan un bloque completo; la tienda y el comercio nunca se abren de noche; misiones, trámites, eventos y visitas cuestan nada, medio bloque o un bloque según su peso (ver 01) |
| 2026-10-15 | Guardado: punto de control al iniciar cada acción y hasta 5 partidas guardables a elegir (ver 01) |
| 2026-10-15 | Herramientas: 5 tipos por 5 niveles, el explosivo es consumible y reparar cuesta dinero y materiales; el salitre y la Aetherita son excepciones a la regla de «más de una zona» (ver 02) |
| 2026-10-15 | Derrota: sin energía vuelves con carga parcial; en Hardcore solo mata un encuentro de riesgo o un jefe; el mal del éter no mata; el día 3 del Acto I no hay pérdida grave |
| 2026-10-15 | Legado en todas las dificultades (menor fuera de Hardcore, mayor en Hardcore); «partida terminada» es la muerte en Hardcore o el cierre del acta; las ayudas llegan desde A1 del Acto II |
| 2026-10-15 | Prensa gratis en el Acto I y de pago y con sesgo desde el Acto II; variación por semilla de probabilidades, precios iniciales, eventos sueltos y algunos nombres |
| 2026-10-15 | Taller: se construye en el MVP y se abre en el Acto II. Vigilancia en cuatro niveles sin solape (0–29, 30–59, 60–84, 85–100); tras una redada baja a unos 60 |
| 2026-10-15 | Mercado negro en el Bar del Farol de Salinas Blancas y con la visita nocturna de Casilda, que no es el modo tienda |
| 2026-10-15 | Los empleados solo leen el tramo de la Unión; «Contratar» se abre al cerrar el Acto I y exige una mejora de la tienda (en el Acto I está bloqueado por ese motivo) |
| 2026-10-15 | **PC primero, móvil después:** el juego se lanza primero en PC, compatible y preparado para Steam; el móvil (Android e iOS) llega cuando el juego esté completo en PC, es decir, con la 1.0 publicada y estable en Steam. Motor Godot 4.x sin cambios |
| 2026-10-15 | Plataformas de la 1.0: Windows y Linux; macOS queda para después de la 1.0. Steam Deck Verified como meta: mando completo, sin HUD táctil y texto legible en 1280×800 |
| 2026-10-15 | Tiendas: Steam como meta e itch.io para builds de prueba; GOG y Epic quedan fuera de la 1.0 |
| 2026-10-15 | Controles: ratón y teclado como principales (cursor, información al pasar el cursor, atajos y ventanas de información densas) con mando completo. La interfaz táctil queda como adaptador futuro del móvil; no se construye HUD táctil ahora |
| 2026-10-15 | Página de Steam («Próximamente») al final de la F4, con el juego casi completo y con arte definitivo (la regla «nada provisional llega a la tienda» se mantiene) |
| 2026-10-15 | Nube y partidas: Steam Auto-Cloud con una carpeta de guardados pequeños y hasta 5 partidas; en Hardcore manda el guardado local (no se restaura desde la nube tras morir) |
| 2026-10-15 | Fases: la F1 deja un proyecto Godot que corre en PC; la F5 lanza en Steam; la F6 es posterior al lanzamiento. El móvil es una fase propia después, y las actualizaciones V2.x pueden seguir en PC o ir también al móvil |
| 2026-10-15 | Pruebas en un PC Windows real y, si hay una, en la Steam Deck: requisito de la F1. El autor trabaja en Mac |
| 2026-10-15 | Sin cambio: pago único sin anuncios ni compras, autoguardado instantáneo (la Steam Deck suspende y no se quiere perder progreso) y las cifras base de la economía |
| 2026-10-15 | 🟡 Propuestas aplazadas a su tarea: resolución base y modo de ventana ⏳ F1-06; precio y DLC (pago único, sin DLC de pago en la v1) ⏳ F5-33, ⏳ F6-01, ⏳ F6-61; demo con el Acto I ⏳ F3-23; declaración de IA de Steam y términos de PixelLab ⏳ F4-227, ⏳ F5-30; casino solo con moneda del juego y cuestionario de Steam sin azar en la v1 ⏳ F6-13 |
| 2026-10-15 | Economía (F0-52): moneda «esquirlas»; día de 12–15 min con tres bloques de unos 4–5 min; semana, mes y estación de 28 días (el día 1 es el 22 de otoño y el invierno empieza el día 8); contratos de 7, 14 y 30 días; La Fosa abre los días 2, 4 y 6 (ver [28](28-numeros-base-de-la-economia.md)) |
| 2026-10-15 | Economía (F0-52): escala con carbón a 50, deuda de la herencia de 24.000 y cuota del día 7 de 960; «punto» de mercado = 1 % del precio base, «pp» para el interés y «vigilancia +N»; el abono anónimo solo paga intereses y la vía de deuda mide el capital que pagas de tu bolsillo (25 % y 50 % de 24.000), con el Consorcio hasta un 30 % |
| 2026-10-15 | Economía (F0-52): la energía se rellena en cada expedición (2 a 3 menas al inicio, crece con skills y herramientas); un nivel de herramienta es un paquete (5 niveles, regla del nivel anterior); la Aetherita pide taladro o cincel de nivel 5 con filtro; explosivo desde el Acto III; la Bolsa cobra medio spread y no tiene impuesto de venta; los empleados tienen un papel residual en el Acto IV; los sobornos a Quiroga se recuperan 1 cada 56 días |
| 2026-10-16 | Pasada de cierre (F0-80): Acto I confirmado. Las tres decisiones pequeñas (herencia, plazo de Reme y rumor de Lucía) quedan como están; el día 1 junta «escanear y picar» en una sola mecánica; las tres pistas del sorteo caen el día 4 por la noche, con ecos los días 1 y 7 ([27](27-guion-del-acto-i.md)). No queda ninguna propuesta pendiente |
| 2026-10-16 | Pasada de cierre (F0-80): la carta de familia de los finales ya no depende del estatus al entrar al acta, sino del patrimonio: «se paga» si llega al piso de Magnate (≈ 250 000, [28](28-numeros-base-de-la-economia.md); umbral final ⏳ F4-109) y «se alivia» si no ([25](25-finales-y-epilogos.md), [19](19-elenco-a-fondo.md)) |
| 2026-10-16 | Pasada de cierre (F0-80): el alcance incluye los documentos 20 (equipo y flujo: siete etapas y 21 roles confirmados, con economista y diseñador de sonido) y 26 (zonas y edificios), además de la biblia y los documentos 21 a 25; el guion del Acto I (27) se cierra aparte en ⏳ F0-86 |
| 2026-10-16 | Pasada de cierre (F0-80): excepción de la Aetherita en joyería. Puede aparecer, casi nunca, en prendas de joyería (un collar o similar), muy raras y extremadamente caras, hechas con los materiales más caros y súper limitadas; no va en casas, decoración ni premios y la Celda de éter sigue siendo su único uso rutinario ([03](03-comercio.md), [26](26-zonas-y-edificios.md)) |
