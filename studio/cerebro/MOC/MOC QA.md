---
id: "moc-qa"
tipo: "moc"
title: "QA"
aliases: ["moc-qa"]
arriba: "[[00 Inicio]]"
generado: true
---

# QA

> Casos de prueba de la estrategia de QA (documento 16) por área, prioridad y estado.

55 casos de prueba en 16 áreas (`studio/data/qa/cases.json`). La estrategia está en [[16 Calidad y QA]].

## Día

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-001 Un día tiene tres bloques y el cierre dispara los eventos de fin de día]] | P0 | funcional | unitaria | [[F2-02 Ciclo de 3 bloques y avance del día]] |
| [[TC-002 No se pueden gastar más bloques de los disponibles]] | P0 | funcional | unitaria | [[F2-02 Ciclo de 3 bloques y avance del día]] |

## Mercado

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-003 El precio tiende al valor justo sin saltos mayores al límite diario]] | P0 | simulación | integración | [[F2-08 Simulador por consola de miles de días]] |
| [[TC-004 La misma semilla produce la misma serie de precios]] | P0 | regresión | unitaria | [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y]] |
| [[TC-005 Vender en tandas rinde más que vender de golpe]] | P0 | funcional | integración | [[F2-07 Spread, slippage y límite de variación diaria]] |
| [[TC-006 Comprar y vender seguido no genera ganancia segura]] | P0 | simulación | integración | [[F2-07 Spread, slippage y límite de variación diaria]] |
| [[TC-007 El mercado se actualiza tres veces por día, una por bloque]] | P0 | funcional | unitaria | [[F2-06 Tres actualizaciones de mercado por día]] |
| [[TC-008 Noticia confirmada, rumor y falsa alarma respetan su fiabilidad]] | P1 | simulación | integración | [[F3-02 Motor de eventos - evento real y reporte por medio]] |
| [[TC-009 Cada medio reporta un mismo evento con su sesgo y retraso]] | P1 | funcional | manual | [[F3-03 Tres medios de prensa con costo y sesgo]] |

## Extracción

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-010 El escáner muestra rangos que contienen la composición real]] | P0 | funcional | unitaria | [[F2-11 Escáner instantáneo con rangos]] |
| [[TC-011 Fallar el minijuego daña la mena y desgasta la herramienta]] | P0 | funcional | integración | [[F2-13 Resultado de extracción - rendimiento, daño y pérdida]] |
| [[TC-012 La zona óptima del Picado se ensancha con la herramienta y la Pericia]] | P0 | funcional | manual | [[F2-16 Zona óptima según herramienta y Pericia]] |
| [[TC-013 Los minijuegos se completan con ratón, teclado y mando]] | P0 | compatibilidad | manual | [[F2-14 Picado (fuerza y precisión)]], [[F1-07 Capa de entrada por acciones - ratón, teclado y mando]] |
| [[TC-014 Las tareas de peligro se resuelven dentro del tiempo]] | P1 | funcional | manual | [[F3-10 Peligros ambientales de la zona 1 y tareas de peligro]] |
| [[TC-015 Una zona agotada se regenera tras su ciclo]] | P1 | funcional | integración | [[F3-13 Regeneración y agotamiento de zonas]] |
| [[TC-016 Perder un encuentro pierde solo parte de la carga]] | P1 | funcional | unitaria | [[F3-09 Encuentros por eventos con decisión]] |
| [[TC-053 Fase móvil Los minijuegos se completan con el dedo\|TC-053  Fase móvil  Los minijuegos se completan con el dedo]] | P3 | compatibilidad | manual |  |

## Tienda

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-017 Una venta actualiza el inventario y el dinero sin diferencias]] | P0 | funcional | unitaria | [[F2-18 Venta en mercado spot]] |
| [[TC-018 El almacén respeta la capacidad y cobra alquiler]] | P0 | funcional | integración | [[F2-17 Inventario y almacén con capacidad y costo]] |
| [[TC-019 Un contrato vencido aplica su penalización]] | P1 | funcional | integración | [[F3-05 Contratos y pedidos - estándar y urgente]] |
| [[TC-020 En el regateo el cliente se va al agotar su paciencia]] | P1 | funcional | manual | [[F2-19 Regateo (oferta y paciencia)]] |

## Empleados

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-021 Un contrato por tiempo vence y el empleado se va o renueva]] | P1 | funcional | integración | [[F4-90 Contratos por tiempo - duración, salario y vencimiento]] |
| [[TC-022 Un empleado de baja lealtad puede robar según su probabilidad]] | P1 | simulación | integración | [[F4-104 Lealtad - robo]] |

## Facciones

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-023 La vigilancia sube con operaciones negras y baja con el tiempo]] | P1 | funcional | unitaria | [[F4-67 Indicador de vigilancia y sus niveles]] |
| [[TC-024 Una redada confisca el stock negro y cierra la tienda]] | P1 | funcional | integración | [[F4-69 Redada - confiscación, cierre y arresto]] |

## Eventos

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-025 Un apagón sin generador cierra la tienda ese día]] | P1 | funcional | integración | [[F4-78 Apagón - modelo y efectos en la tienda]] |
| [[TC-026 Cada evento social se anuncia antes en las noticias]] | P1 | funcional | integración | [[F4-88 Avisos previos en las noticias para cada evento]] |

## Progresión

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-027 Los stats suben por uso y con rendimientos decrecientes]] | P1 | funcional | unitaria | [[F3-11 Stats por uso e hitos (5 stats)]] |
| [[TC-028 Subir de estatus exige condiciones y no solo dinero]] | P1 | funcional | unitaria | [[F4-109 Escalera de estatus y condiciones de ascenso]] |

## Historia

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-029 El Acto I se puede completar de principio a fin]] | P0 | funcional | manual | [[F3-16 Acto I - Villa Brasa, Reme, Teo, deuda y tutorial guiado]] |
| [[TC-030 El nombre del personaje aparece en los diálogos y los nombres inválidos\|TC-030 El nombre del personaje aparece en los diálogos y los nombres inválidos se rechazan]] | P0 | funcional | manual | [[F3-14 Personalización del protagonista]] |

## Guardado

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-031 Guardar y cargar conserva el estado exacto]] | P0 | guardado | integración | [[F2-03 Guardado y carga versionado con escritura segura]] |
| [[TC-032 Un guardado corrupto se detecta y no rompe el juego]] | P0 | guardado | integración | [[F2-37 Pruebas de guardado - corrupción y migración]] |
| [[TC-033 Un guardado de una versión anterior se migra]] | P1 | guardado | integración | [[F3-35 Migraciones de versión del guardado]] |
| [[TC-051 Steam Auto-Cloud sincroniza hasta 5 partidas y en Hardcore manda el\|TC-051 Steam Auto-Cloud sincroniza hasta 5 partidas y en Hardcore manda el guardado local]] | P0 | guardado | manual | [[F5-50 Pruebas de instalación y actualización]] |

## Localización

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-034 Cambiar de idioma actualiza todos los textos sin reiniciar]] | P0 | localización | manual | [[F1-16 Marco de traducción en Godot con archivos .po y cambio de]] |
| [[TC-035 Ningún texto se corta con idiomas más largos]] | P1 | localización | manual | [[F1-19 Interfaz que tolera textos más largos y pruebas con]] |
| [[TC-036 No hay cadenas sin traducir ni cadenas fijas en el código]] | P0 | contenido | unitaria | [[F1-17 Regla y verificación - ninguna cadena fija en el código ni]] |

## Accesibilidad

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-037 Las subidas y bajadas se distinguen sin depender del color]] | P1 | accesibilidad | manual | [[F5-17 Opciones de daltonismo]] |
| [[TC-038 Todo el juego se maneja con mando]] | P0 | accesibilidad | manual | [[F1-08 Navegación por foco en menús de prueba]] |
| [[TC-050 Todo el juego se maneja con teclado]] | P0 | accesibilidad | manual | [[F1-08 Navegación por foco en menús de prueba]] |
| [[TC-052 El juego se ve y se lee bien en pantallas de PC distintas]] | P1 | compatibilidad | manual | [[F1-06 Resolución base, escalado entero y modos de pantalla]] |

## Rendimiento

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-039 El arranque en frío cumple el presupuesto en un PC de gama baja]] | P0 | rendimiento | manual | [[F1-44 Presupuestos de rendimiento medidos en PC]] |
| [[TC-040 Sesión de 60 minutos sin cierres ni fugas de memoria visibles]] | P1 | rendimiento | manual | [[F1-22 Overlay de depuración - FPS, día, bloque y semilla]] |
| [[TC-055 Fase móvil El arranque, el peso y la batería cumplen el presupuesto en\|TC-055  Fase móvil  El arranque, el peso y la batería cumplen el presupuesto en Android de gama media]] | P3 | rendimiento | manual |  |

## Seguridad

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-041 No hay secretos en el repositorio ni en las builds de Windows y Linux]] | P0 | seguridad | unitaria | [[F1-42 Escaneo de secretos en integración continua]] |
| [[TC-042 La build solo escribe en su carpeta de guardados y diagnóstico]] | P0 | seguridad | manual | [[F1-41 Lista de verificación de seguridad adaptada de OWASP MASVS]] |
| [[TC-043 Los nombres del personaje y de la tienda no inyectan formato ni rompen\|TC-043 Los nombres del personaje y de la tienda no inyectan formato ni rompen la interfaz]] | P0 | seguridad | unitaria | [[F3-14 Personalización del protagonista]] |
| [[TC-044 El archivo de diagnóstico no contiene datos personales]] | P0 | privacidad | unitaria | [[F2-24 Módulo de telemetría local - rendimiento, errores y eventos]] |
| [[TC-045 La versión de lanzamiento no tiene depuración activada]] | P0 | seguridad | manual | [[F5-51 Pasada de seguridad final - build de PC y SteamPipe]] |
| [[TC-046 Un guardado manipulado no ejecuta contenido ni rompe invariantes]] | P1 | seguridad | integración | [[F2-37 Pruebas de guardado - corrupción y migración]] |
| [[TC-054 Fase móvil El manifiesto del APK solo pide los permisos necesarios\|TC-054  Fase móvil  El manifiesto del APK solo pide los permisos necesarios]] | P3 | seguridad | manual |  |

## Privacidad

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-047 Nada se envía sin una acción del usuario]] | P0 | privacidad | manual | [[F2-25 Exportar diagnóstico desde el juego]] |
| [[TC-048 El identificador anónimo se puede reiniciar]] | P1 | privacidad | unitaria | [[F2-24 Módulo de telemetría local - rendimiento, errores y eventos]] |

## Instalación

| Caso | Prioridad | Tipo | Nivel | Tareas |
|---|---|---|---|---|
| [[TC-049 Instalar, abrir, cerrar y actualizar desde Steam conserva la partida]] | P0 | instalación | manual | [[F5-50 Pruebas de instalación y actualización]] |
