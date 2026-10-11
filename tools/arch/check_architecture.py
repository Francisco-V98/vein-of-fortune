#!/usr/bin/env python3
"""Verifica que el código de game/ respete la arquitectura modular.

Uso:
    python3 tools/arch/check_architecture.py game

Lee game/architecture.json y revisa todos los .gd de game/src. No tiene
dependencias externas. Sale con código 1 si hay violaciones.

Reglas (ver studio/docs/14-arquitectura-y-modularidad.md):
  A1  Dentro de un módulo, cada capa solo puede usar las capas permitidas.
  A2  Un módulo solo usa a otro mediante su carpeta `api` y si lo declara.
  A3  El dominio no depende de otros módulos, de la plataforma ni de la UI.
  A4  El dominio no usa clases del motor de escenas ni de entrada/archivos.
  A5  `kernel` no depende de nada fuera de `kernel`.
  A6  `platform/adapters` solo lo conoce `app` (la raíz de composición).
  A7  El grafo de dependencias entre módulos no tiene ciclos.
  A8  Los módulos de la carpeta y los declarados en architecture.json coinciden.
  A9  Solo los autoloads permitidos pueden estar en project.godot.
"""
import json
import pathlib
import re
import sys

LAYER_DIRS = ("domain", "application", "infrastructure", "presentation", "api", "data", "tests")
MAX_LINES = 400
REF_RE = re.compile(r"res://src/([^\"'\s)]+)")
IDENT_RE = re.compile(r"\b[A-Za-z_]\w*\b")
CLASS_RE = re.compile(r"^\s*class_name\s+(\w+)")


def code_part(line):
    """Quita el comentario de una línea, respetando las comillas."""
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote and line[i - 1] != "\\":
                quote = None
        elif ch in ("'", '"'):
            quote = ch
        elif ch == "#":
            return line[:i]
    return line


def blank_strings(line):
    """Reemplaza el contenido de las cadenas por espacios."""
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote and line[i - 1] != "\\":
                quote = None
                out.append(ch)
            else:
                out.append(" ")
        else:
            if ch in ("'", '"'):
                quote = ch
            out.append(ch)
    return "".join(out)


def classify(rel):
    """Clasifica una ruta relativa a src/ en (top, module, layer, sub)."""
    parts = rel.split("/")
    info = {"top": parts[0], "module": None, "layer": None, "sub": None, "rel": rel}
    if parts[0] == "modules":
        info["module"] = parts[1] if len(parts) > 1 else None
        info["layer"] = parts[2] if len(parts) > 3 else None
    elif parts[0] == "platform":
        info["sub"] = parts[1] if len(parts) > 2 else None
    return info


def describe(info):
    if info["top"] == "modules":
        return "módulo %s (%s)" % (info["module"], info["layer"] or "sin capa")
    return info["top"] + (("/" + info["sub"]) if info["sub"] else "")


def check_ref(src, dst, cfg):
    """Devuelve un mensaje si src no puede referirse a dst, o None si es válido."""
    top = src["top"]
    if top in ("app", "tests"):
        return None
    if dst["top"] == "kernel":
        return None
    if top == "kernel":
        return "A5 kernel no puede depender de %s" % describe(dst)
    if top == "platform":
        same = dst["top"] == "platform"
        if src["sub"] == "ports" and not (same and dst["sub"] == "ports"):
            return "A6 un puerto de platform solo puede usar kernel y otros puertos"
        if src["sub"] == "adapters" and not (same and dst["sub"] in ("ports", "adapters")):
            return "A6 un adaptador de platform solo puede usar kernel y platform"
        return None
    if top == "ui_kit":
        if dst["top"] == "ui_kit":
            return None
        return "ui_kit solo puede depender de kernel (usa %s)" % describe(dst)
    if top != "modules":
        return "carpeta no declarada en la arquitectura: src/%s" % top
    # origen dentro de un módulo
    module, layer = src["module"], src["layer"]
    if layer is None:
        return "el archivo del módulo %s debe estar dentro de una capa (%s)" % (module, ", ".join(LAYER_DIRS))
    if layer == "tests":
        return None
    if dst["top"] == "platform":
        if dst["sub"] == "ports" and layer != "domain":
            return None
        if dst["sub"] == "ports":
            return "A3 el dominio de %s no puede depender de platform" % module
        return "A6 solo app puede conocer platform/adapters"
    if dst["top"] == "ui_kit":
        return None if layer == "presentation" else "ui_kit solo se usa desde presentation (origen: capa %s de %s)" % (layer, module)
    if dst["top"] != "modules":
        return "dependencia no permitida hacia %s" % describe(dst)
    if dst["module"] == module:
        dlayer = dst["layer"]
        if dlayer is None:
            return "el destino no está dentro de una capa del módulo %s" % module
        if dlayer == "data":
            return None if layer in ("application", "infrastructure") else "A1 la capa %s no puede leer data de %s" % (layer, module)
        if dlayer == layer:
            return None
        if dlayer == "tests":
            return "el código de producción no puede usar tests"
        allowed = cfg["layers"].get(layer, [])
        if dlayer in allowed:
            return None
        return "A1 la capa %s de %s no puede depender de la capa %s" % (layer, module, dlayer)
    # otro módulo
    if layer == "domain":
        return "A3 el dominio de %s no puede depender del módulo %s" % (module, dst["module"])
    if dst["layer"] != "api":
        return "A2 %s usa internos de %s (capa %s); solo puede usar su api" % (module, dst["module"], dst["layer"])
    declared = cfg["modules"].get(module, {}).get("depends_on", [])
    if dst["module"] not in declared:
        return "A2 %s usa la api de %s sin declararlo en depends_on" % (module, dst["module"])
    return None


def find_cycle(modules):
    """Devuelve un ciclo (lista de módulos) o None."""
    state = {}

    def visit(node, path):
        state[node] = 1
        for nxt in modules.get(node, {}).get("depends_on", []):
            if state.get(nxt) == 1:
                return path[path.index(nxt):] + [nxt] if nxt in path else [node, nxt]
            if state.get(nxt) is None and nxt in modules:
                cyc = visit(nxt, path + [nxt])
                if cyc:
                    return cyc
        state[node] = 2
        return None

    for name in modules:
        if state.get(name) is None:
            cyc = visit(name, [name])
            if cyc:
                return cyc
    return None


def check(game_dir):
    """Devuelve (errores, avisos). Cada elemento es un texto."""
    game = pathlib.Path(game_dir)
    errors, warnings = [], []
    cfg_path = game / "architecture.json"
    if not cfg_path.exists():
        return ["falta %s" % cfg_path], warnings
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    # A7 y A8 (parte de configuración): se validan aunque todavía no haya código
    cyc = find_cycle(cfg["modules"])
    if cyc:
        errors.append("A7 ciclo de dependencias entre módulos: %s" % " -> ".join(cyc))
    for name, spec in cfg["modules"].items():
        for dep in spec.get("depends_on", []):
            if dep not in cfg["modules"]:
                errors.append("A8 %s depende de %s, que no está declarado" % (name, dep))

    src_root = game / cfg.get("root", "src")
    if not src_root.exists():
        return errors, ["todavía no hay código en %s" % src_root]

    # A8: módulos declarados vs carpetas
    modules_dir = src_root / "modules"
    on_disk = sorted(p.name for p in modules_dir.iterdir() if p.is_dir()) if modules_dir.exists() else []
    for name in on_disk:
        if name not in cfg["modules"]:
            errors.append("A8 el módulo %s existe en el código pero no está declarado en architecture.json" % name)
    for name in cfg["modules"]:
        if name not in on_disk:
            warnings.append("el módulo %s está declarado pero todavía no existe en el código" % name)

    files = sorted(src_root.rglob("*.gd"))
    class_map = {}
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            m = CLASS_RE.match(line)
            if m:
                class_map[m.group(1)] = f.relative_to(src_root).as_posix()

    forbidden = [re.compile(r"\b%s\b" % re.escape(s)) for s in cfg.get("domain_forbidden_symbols", [])]

    for f in files:
        rel = f.relative_to(src_root).as_posix()
        src = classify(rel)
        lines = f.read_text(encoding="utf-8").splitlines()
        if len(lines) > MAX_LINES:
            warnings.append("%s tiene %d líneas (máximo recomendado %d): conviene dividirlo" % (rel, len(lines), MAX_LINES))
        for n, raw in enumerate(lines, start=1):
            code = code_part(raw)
            seen = set()
            for m in REF_RE.finditer(code):
                dst_rel = m.group(1)
                if dst_rel in seen:
                    continue
                seen.add(dst_rel)
                msg = check_ref(src, classify(dst_rel), cfg)
                if msg:
                    errors.append("%s:%d %s [usa res://src/%s]" % (rel, n, msg, dst_rel))
            blanked = blank_strings(code)
            for tok in set(IDENT_RE.findall(blanked)):
                dst_rel = class_map.get(tok)
                if dst_rel and dst_rel != rel and dst_rel not in seen:
                    seen.add(dst_rel)
                    msg = check_ref(src, classify(dst_rel), cfg)
                    if msg:
                        errors.append("%s:%d %s [usa la clase %s]" % (rel, n, msg, tok))
            if src["top"] == "modules" and src["layer"] == "domain":
                for rx in forbidden:
                    hit = rx.search(blanked)
                    if hit:
                        errors.append("%s:%d A4 el dominio no puede usar '%s'" % (rel, n, hit.group(0)))

    # A9: autoloads
    project = game / "project.godot"
    if project.exists():
        allowed = set(cfg.get("allowed_autoloads", []))
        in_autoload = False
        for n, line in enumerate(project.read_text(encoding="utf-8").splitlines(), start=1):
            s = line.strip()
            if s.startswith("["):
                in_autoload = s == "[autoload]"
                continue
            if in_autoload and "=" in s:
                name = s.split("=", 1)[0].strip()
                if name not in allowed:
                    errors.append("project.godot:%d A9 autoload no permitido: %s" % (n, name))
    return errors, warnings


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    errors, warnings = check(argv[1])
    for w in warnings:
        print("AVISO:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print("\n%d violación(es) de arquitectura." % len(errors))
        return 1
    print("Arquitectura OK (%d aviso(s))." % len(warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
