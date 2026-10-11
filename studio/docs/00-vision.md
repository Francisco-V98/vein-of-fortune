# 00 · Visión

**Título:** *Veta de Fortuna* (español) · *Vein of Fortune* (inglés). El mundo se llama **Valdoria**. Ver [13](13-marca-e-identidad.md).

## Concepto

Juego de gestión y comercio de minerales con dos mitades que se alimentan entre sí:

1. **Extracción**: explorar zonas, evaluar menas, minar con minijuegos, gestionar herramientas y riesgos.
2. **Comercio**: leer un mercado simulado, especular, vender, cumplir pedidos, gestionar una tienda y un almacén, y construir un imperio.

El jugador empieza con poco y crece: mejores herramientas, mejores zonas, mejor información, mejor tienda y mejor estilo de vida.

## Enfoque del proyecto ✅

El juego **nace como un proyecto 100 % personal**: se hace para disfrutarlo jugando y construyéndolo. Si resulta divertido y todo va bien, se publica en Android y luego iOS (y, más adelante, PC/consola). Se empieza con un prototipo barato y rápido para comprobar si es divertido, aunque no sea bonito.

## Pilares de diseño

1. **La información es poder** ✅ — saber qué hay en una mena, qué hará el mercado o qué peligro tiene una zona tiene valor y se progresa en ello.
2. **Dos mitades, un solo juego** ✅ — lo que ocurre en las minas mueve el mercado y lo que pide el mercado dirige a dónde ir a minar.
3. **Decisiones con riesgo** ✅ — energía, desgaste de herramientas, peligros y pérdida parcial de carga obligan a elegir.
4. **Cada partida distinta** ✅ — mundo, mercado y eventos procedurales; reglas fijas.
5. **Libertad con consecuencias** ✅ — el jugador decide cómo usar su día, pero descuidar una mitad se paga.

## Plataforma y modelo

| Aspecto | Decisión |
|---|---|
| Plataforma inicial | ✅ Mobile, **Android primero**; iOS después si todo va bien |
| Orientación | ✅ **Horizontal (landscape)** |
| Controles | ✅ Táctil y mando; con mando, el HUD táctil se oculta (ver [10](10-tecnico-y-herramientas.md)) |
| Futuro | ✅ Posible PC (Steam) y consola si el proyecto funciona |
| Modo | ✅ Single-player, mercado simulado (sin servidores en v1) |
| Modelo de negocio | ✅ Pago único. Sin dinero real dentro del juego |
| Moneda | ✅ Una sola moneda interna |
| Duración | ✅ Sin final fijo: dura lo que el jugador quiera, construyendo su imperio |

## Público

✅ Para todos, pensado para quien disfruta de gestión/comercio. Complejidad media: profundidad sin saturar. La dificultad ajustable cubre el rango.

## Estética

✅ Sencilla: **pixel art** al estilo de Dave the Diver, con cosas más bien estáticas. Sin gráficos ni movimientos complejos. Conviene para mobile y para un desarrollo realista.

✅ Referencias de estilo:

- **Fallout**: retrofuturismo; algo lúgubre pero colorido.
- **Papers, Please**: estética de escritorio/documentos, UI con carácter.
- **Dave the Diver**: pixel art y presentación.
- **Balatro**: diseño de sonido.
- **Voces estilo Dave the Diver** 🟡: para el MVP, sonidos cortos tipo "blips" por personaje (como Papers, Please o Balatro), que son baratos; voces reales quedan como mejora futura.

## Referencias

| Juego | Qué tomamos |
|---|---|
| Dave the Diver | Ciclo de expedición + negocio, varios minijuegos, varias salidas por día |
| EVE Online | Mercado, especulación, información como ventaja |
| Moonlighter | Aventura + tienda, riesgo de perder botín |
| Offworld Trading Company | Oferta/demanda, mercado como sistema |
| Balatro | Desbloqueos persistentes entre partidas (legado) |
| Stardew Valley | Minijuego de pesca (equilibrar dos parámetros) |
| Among Us | Minijuegos cortos de tareas |
| FTL / Reigns | Encuentros por eventos con decisión |

## Alcance

- **MVP** (a definir en el roadmap): 1–2 zonas, 3–4 minerales, 1 tienda, mercado simple, 3 minijuegos (Picado, Perforación, Regateo).
- **Meta de la primera versión completa:** mínimo 10 minerales con lore, 5–6 zonas, minijuegos variados, mercado con noticias, tienda con dinámicas, 4 niveles de dificultad, árbol de logros.
- Detalle por fases: ver [06-roadmap-y-pendientes.md](06-roadmap-y-pendientes.md).
