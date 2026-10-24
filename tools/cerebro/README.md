# Cerebro del proyecto (F0-90)

Genera un **vault de Obsidian** en `studio/cerebro/` (git-ignored) a partir de los documentos y los datos del repo. Es de solo
lectura: los documentos y los datos siguen siendo la fuente de verdad. Se regenera entero en cada
`python3 studio/hub/build.py` (opción `--sin-cerebro` para saltarlo) o a mano con `python3 tools/cerebro/generar.py [--destino DIR]`.
Solo biblioteca estándar; tarda menos de un segundo.

## Estructura del vault

```
studio/cerebro/
  00 Inicio.md        entrada: mapas, cifras por tipo, cómo moverse
  MOC/                mapas de contenido (se borra y se reescribe)
  generado/<tipo>/    notas generadas (se borra y se reescribe): docs, secciones, adr, roadmap, equipo, memoria, ...
  mis-notas/          del autor: el generador NUNCA la toca (se crea con un README)
  .obsidian/          plantilla de tools/cerebro/obsidian/, copiada solo en lo que falte (nunca se pisa)
```

El generador borra solo `generado/`, `MOC/` y los `.md` con `generado: true`. Escribe únicamente lo que cambia.

## Código

| Archivo | Qué hace |
|---|---|
| `nucleo.py` | `Registro` de notas (ID estable, nombre de archivo legible y único, alias, tipo, carpeta, propiedades), marcadores de enlace, resolución contra la tabla de IDs, avisos, `escribir` y `preparar_vault` |
| `texto.py` | Convierte Markdown del repo a texto de Obsidian (`convertir`), resumen de una línea (`primera_frase`), `slug` |
| `generar.py` | Orquestador: `MODULOS`, `generar_vault(repo, destino)`; un módulo que falla solo avisa |
| `mod_documentos.py` | Documentos 00 a 28 y ADR: índice por documento y una nota por sección «##» |
| `mod_tareas.py` | Fases, hitos y tareas (flujo por etapas, traspasos, historial, documentos relacionados) |
| `mod_equipo.py` | Roles (agente, modelo, esfuerzo), departamentos, etapas y reglas |
| `mod_memoria.py` | Memoria del proyecto (se omite si la carpeta no existe) |
| `mod_mundo.py`, `mod_narrativa.py`, `mod_qa.py`, `mod_simulador.py`, `mod_glosario.py`, `mod_arte.py` | **Stubs** de la parte 2 |
| `obsidian/` | Plantilla `.obsidian` (`graph.json` con colores por carpeta y por estado de tarea, `bookmarks.json` con vistas guardadas del grafo) |

## Interfaz para un módulo nuevo

Un módulo es `mod_<nombre>.py` con `generar(registro, repo)` (`repo` es un `pathlib.Path` a la raíz del repo). Los stubs ya
están en `MODULOS` (en `generar.py`), después de documentos, tareas, equipo y memoria, así que pueden enlazar a sus IDs.

```python
from .nucleo import ref, ref_suave

def generar(registro, repo):
    registro.moc("moc-mundo", "Mundo", "Entidades del mundo.", orden=60)   # carpeta MOC/, lista sola a sus hijos
    n = registro.nueva(
        "min-carbon", "mineral", "Carbón", "mundo/minerales",              # id, tipo, título, carpeta (dentro de generado/)
        sufijo="mineral",                       # solo se usa si «Carbón» ya existe: «Carbón (mineral)»
        alias=["carbon"],                       # también resuelven enlaces (útil para `d1.2` -> `esc-d1.1`)
        props={"zonas": [ref("zona-galerias-hollin")]},   # propiedades YAML; las cadenas con ref() pasan a [[enlaces]]
        resumen="Mena básica del Hollín.", cuerpo="Texto con " + ref("rec-acero") + ".",
        arriba="moc-mundo",                     # obligatorio salvo en MOC: su padre; evita notas huérfanas
        tags=["estado/hecho"], fuente="studio/data/world.json:12")
    n.relacion("Recetas", [ref("rec-acero")])   # sección «Relaciones»
```

- **Enlaces:** `ref(id, texto=None)` es obligatorio (si no resuelve, hay aviso); `ref_suave(id, visible, respaldo)` es opcional (deja
  `respaldo` sin avisar); `ref_ruta("studio/docs/27-....md")` apunta a un archivo del repo. Se resuelven al final, así que se puede
  enlazar a notas que otro módulo crea después. En tablas la barra se escapa sola.
- **Texto del repo:** `texto.convertir(md, "ruta/del/archivo.md")` cambia `[NN](….md)`, IDs entre comillas invertidas e IDs de tarea por
  marcadores (los que no resuelven quedan como estaban). Devuelve `(texto, citas)`.
- **Consultas:** `registro.existe(id)`, `registro.nota(id)`, `registro.hijos(id)`, `registro.por_tipo(tipo)`,
  `registro.indice_referencias().a(id)` (quién enlaza a `id`), `registro.avisos` / `registro.aviso(msg)`, `registro.info`
  (líneas informativas), `registro.opciones` (para pruebas).
- **Reglas:** IDs ASCII (`[A-Za-z0-9._-]`), únicos; nada de escribir archivos; sin `datetime.now()` ni aleatoriedad (la salida debe ser
  idéntica entre pasadas). Las propiedades `id, tipo, title, aliases, arriba, tags, fuente, generado` las pone el núcleo.
- **Graph View:** `graph.json` colorea por carpeta (`generado/mundo`, `generado/economia`, `generado/narrativa`, `generado/qa`,
  `generado/simulador`, `generado/arte`, `generado/glosario`); usa esas carpetas o añade un grupo a la plantilla.
- **Avisos:** enlaces sin resolver y notas huérfanas salen en `Resultado.avisos`; `build.py` los pasa a `warn()` (con `--strict` fallan).

Pruebas: `python3 -m unittest discover -s tools/ci -p "test_cerebro.py" -v`.

Módulos de la parte 2: `mod_mundo.py`, `mod_economia.py`, `mod_qa.py`, `mod_simulador.py`, `mod_arte.py` (con `ayudas.py`: lectura de JSON, menciones por texto, `id_doc("28 §7.2")` → `doc-28-s07`), y `mod_narrativa.py`, `mod_glosario.py` (con `narr_fuentes.py`: tablas Markdown de los documentos 23, 25, 26 y 27 y análisis del `ref` de los hilos).
Pruebas: `test_cerebro.py`, `test_cerebro_mundo.py` y `test_cerebro_narrativa.py`.
