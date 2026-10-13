"""Comprobaciones de coherencia del diseño contra el registro del mundo.

El registro (studio/data/world.json) es la fuente de verdad de minerales, zonas,
minijuegos, mecánicas, recetas, facciones y personajes. Aquí se comprueba que:

  - el registro es íntegro: lo que referencia existe (error: hace fallar el build);
  - el diseño es coherente: reglas del juego, mapa de historia y números base no se
    contradicen ni quedan sin definir (hallazgo: baja el porcentaje, pero no falla el build).

Uso desde build.py:  result = coherence.check(world, story, decisions, hilos)
"""
import re

SEV_ERROR = "error"

# Registro de hilos narrativos (studio/data/hilos.json). Los actos incluyen «despues»: la segunda parte o el sandbox tras el acta.
HILO_ACTOS = ["I", "II", "III", "IV", "despues"]
HILO_TIPOS = ["pista", "promesa", "secreto", "conflicto"]
HILO_ESTADOS = ["resuelto", "abierto", "aplazado"]
HILO_ABIERTOS = ("abierto", "aplazado")
TAPE_COUNT = 8
_NODE_REF = re.compile(r"\bn-[a-z0-9]+(?:-[a-z0-9]+)*")
_TAPE_REF = re.compile(r"\bcintas?\s+(\d+(?:\s*(?:,|y|–|-|a)\s*\d+)*)", re.IGNORECASE)


def _act_index(acts):
    return {a: i for i, a in enumerate(acts)}


def _earliest_act(mineral, zones_by_id, idx):
    """Primer acto en que el mineral aparece en alguna zona (None si no aparece)."""
    acts = [zones_by_id[z]["act"] for z in mineral["zones"] if z in zones_by_id]
    return min(acts, key=lambda a: idx[a]) if acts else None


def _lane(story, lane_id):
    for lane in story.get("lanes", []):
        if lane.get("id") == lane_id:
            return lane.get("cells", [])
    return []


def integrity(world):
    """Devuelve la lista de errores de integridad del registro."""
    errors = []
    acts = world.get("acts", [])
    idx = _act_index(acts)
    seen = {}
    for kind in ("zones", "minigames", "minerals", "mechanics", "recipes", "factions", "characters", "npcs"):
        for item in world.get(kind, []):
            key = (kind, item.get("id"))
            if key in seen:
                errors.append("%s: id repetido (%s)" % (kind, item.get("id")))
            seen[key] = True
            if not item.get("name"):
                errors.append("%s %s sin nombre" % (kind, item.get("id")))
    zones = {z["id"]: z for z in world.get("zones", [])}
    minigames = {m["id"] for m in world.get("minigames", [])}
    minerals = {m["id"] for m in world.get("minerals", [])}
    factions = {f["id"] for f in world.get("factions", [])}
    for kind in ("zones", "minigames", "mechanics", "characters"):
        for item in world.get(kind, []):
            if item.get("act") not in idx:
                errors.append("%s %s: acto desconocido (%s)" % (kind, item.get("id"), item.get("act")))
    for m in world.get("minerals", []):
        for z, role in m.get("zones", {}).items():
            if z not in zones:
                errors.append("mineral %s usa una zona inexistente: %s" % (m["id"], z))
            if role not in ("principal", "secundario"):
                errors.append("mineral %s: papel de zona desconocido (%s)" % (m["id"], role))
        for g in m.get("minigames", []):
            if g not in minigames:
                errors.append("mineral %s usa un minijuego inexistente: %s" % (m["id"], g))
    for r in world.get("recipes", []):
        for group in r.get("inputs", []):
            for ing in group:
                if ing not in minerals:
                    errors.append("receta %s usa un mineral inexistente: %s" % (r["id"], ing))
    for mech in world.get("mechanics", []):
        for ing in mech.get("needs_minerals", []):
            if ing not in minerals:
                errors.append("mecánica %s necesita un mineral inexistente: %s" % (mech["id"], ing))
    for f in world.get("factions", []):
        if f.get("parent") and f["parent"] not in factions:
            errors.append("facción %s con padre inexistente: %s" % (f["id"], f["parent"]))
    for c in world.get("characters", []):
        if c.get("faction") not in (None, "variable") and c["faction"] not in factions:
            errors.append("personaje %s con facción inexistente: %s" % (c["id"], c["faction"]))
    for npc in world.get("npcs", []):
        if npc.get("faction") not in (None,) and npc["faction"] not in factions:
            errors.append("npc %s con facción inexistente: %s" % (npc["id"], npc["faction"]))
        if not npc.get("group"):
            errors.append("npc %s sin grupo" % npc["id"])
    return errors


def _flag_acts(decisions):
    """Actos en que se fija y se lee cada bandera: (fija, lee), como {bandera: [actos]}."""
    acts = {n["id"]: n["acto"] for n in decisions.get("nodes", [])}
    sets, reads = {}, {}
    for n in decisions.get("nodes", []):
        for o in n.get("opciones", []):
            for fid in o.get("fija", []):
                sets.setdefault(fid, []).append(n["acto"])
        for fid in n.get("lee", []):
            reads.setdefault(fid, []).append(n["acto"])
    return sets, reads, acts


def _decision_checks(world, story, decisions, add):
    """Cruces del árbol de decisiones con el registro del mundo y el mapa de historia (C12 a C15)."""
    acts = world.get("acts", [])
    idx = _act_index(acts)
    flags = decisions.get("flags", [])
    sets, reads, node_act = _flag_acts(decisions)
    first_set = {f: min(a, key=lambda x: idx[x]) for f, a in sets.items() if all(x in idx for x in a)}

    # C12 banderas <-> nodos
    bad = []
    for f in flags:
        fid = f["id"]
        if fid not in sets:
            bad.append("%s no la fija ninguna decisión" % fid)
        elif fid not in reads:
            bad.append("%s se fija y no la lee ninguna decisión" % fid)
        elif fid in first_set and any(idx.get(a, 0) < idx[first_set[fid]] for a in reads[fid]):
            bad.append("%s se lee en el Acto %s, antes de fijarse en el Acto %s" % (
                fid, min(reads[fid], key=lambda x: idx.get(x, 0)), first_set[fid]))
    add("C12", "Decisiones", "Cada bandera se fija y se lee, y nunca se lee antes de fijarse", len(flags), bad)

    # C13 cuellos <-> actos
    cuellos = decisions.get("cuellos", [])
    bad = []
    for a in acts:
        if not any(c.get("acto") == a for c in cuellos):
            bad.append("El Acto %s no tiene ningún cuello donde las ramas se reúnan" % a)
    for c in cuellos:
        for nid in c.get("recibe", []):
            if node_act.get(nid) != c.get("acto"):
                bad.append("%s (Acto %s) recibe %s, que es del Acto %s" % (c["id"], c.get("acto"), nid, node_act.get(nid, "—")))
    add("C13", "Decisiones", "Cada acto tiene cuellos y cada cuello solo reúne ramas de su acto",
        len(acts) + sum(len(c.get("recibe", [])) for c in cuellos), bad)

    # C14 personajes de las banderas <-> registro
    chars = {}
    for c in world.get("characters", []):
        chars[c["name"]] = c
        for alias in c.get("aka", []):
            chars[alias] = c
    pairs = [(f, who) for f in flags for who in f.get("personajes", [])]
    bad = []
    for f, who in pairs:
        c = chars.get(who)
        if c is None:
            bad.append("%s nombra a %s, que no está en el registro de personajes" % (f["id"], who))
        elif f["id"] in first_set and idx.get(c["act"], 0) > idx[first_set[f["id"]]]:
            bad.append("%s se fija en el Acto %s, antes de que %s aparezca (Acto %s)" % (f["id"], first_set[f["id"]], c["name"], c["act"]))
    add("C14", "Decisiones", "Los personajes de cada bandera existen y ya han aparecido cuando se fija", len(pairs), bad)

    # C15 cintas <-> mapa de historia (se recogen a lo largo de la historia y se oyen al final)
    tapes = decisions.get("cintas", [])
    last = acts[-1] if acts else None
    bad = ["La cinta %s se recoge en el Acto %s, que no existe o llega después de oírse" % (t["n"], t.get("acto"))
           for t in tapes if t.get("acto") not in idx]
    mentions = 0
    for lane_id in ("narrativa", "arte"):
        for i, cell in enumerate(_lane(story, lane_id)):
            for text in cell:
                if "cinta" not in text.lower():
                    continue
                mentions += 1
                if i < len(acts) and acts[i] != last:
                    bad.append("El mapa de historia nombra las cintas en el Acto %s (fila %s) y se oyen en el %s" % (acts[i], lane_id, last))
                since = re.search(r"desde el Acto ([IVX]+)", text)
                if since and tapes:
                    first = min((t["acto"] for t in tapes if t.get("acto") in idx), key=lambda a: idx[a], default=None)
                    if since.group(1) != first:
                        bad.append("El mapa de historia las recoge «desde el Acto %s» y la primera cinta es del Acto %s" % (since.group(1), first))
    if tapes and not mentions:
        bad.append("El mapa de historia no menciona las cintas del árbol de decisiones")
    add("C15", "Decisiones", "El reparto de las cintas coincide con las filas del mapa de historia", len(tapes) + mentions + (0 if mentions else 1), bad)


def hilo_refs(ref):
    """Nodos de decisions.json (n-...) y números de cinta que cita el texto de una referencia."""
    nodes = _NODE_REF.findall(ref or "")
    tapes = [int(n) for m in _TAPE_REF.findall(ref or "") for n in re.findall(r"\d+", m)]
    return nodes, tapes


def _character_ids(world):
    """Id de personaje por nombre y por alias."""
    out = {}
    for c in world.get("characters", []):
        out[c["name"]] = c["id"]
        for alias in c.get("aka", []):
            out[alias] = c["id"]
    return out


def _entries(hilo, key):
    return [e for e in hilo.get(key, []) if isinstance(e, dict)]


def _entry_ranks(hilo, key):
    return [HILO_ACTOS.index(e["acto"]) for e in _entries(hilo, key) if e.get("acto") in HILO_ACTOS]


def _missing_characters(hilo, ids, cells, acts):
    """Personajes del hilo que, tras entrar en escena, dejan de estar en la fila «En escena» del mapa de historia antes de la resolución.

    Devuelve [(nombre, [actos sin él])]. Va de la primera siembra a la última resolución, ambas incluidas;
    «despues» no tiene celda en el mapa y no se mira.
    """
    sowed, solved = _entry_ranks(hilo, "siembra"), _entry_ranks(hilo, "resuelve")
    if not sowed or not solved or max(solved) <= min(sowed):
        return []
    span = [a for a in HILO_ACTOS[min(sowed):max(solved) + 1] if a in acts and acts.index(a) < len(cells)]
    out = []
    for who in hilo.get("personajes", []):
        cid = ids.get(who)
        if not cid:
            continue
        # Un personaje «desaparece» solo si ya había entrado en escena: antes de su debut no se le echa de menos
        debut = next((i for i, a in enumerate(span) if cid in cells[acts.index(a)]), None)
        gone = list(span) if debut is None else [a for a in span[debut:] if cid not in cells[acts.index(a)]]
        if gone:
            out.append((who, gone))
    return out


def hilos_analisis(hilos, world, story, decisions=None):
    """Cruza el registro de hilos con el mundo, el mapa de historia y el árbol de decisiones.

    Devuelve los hallazgos por tipo, listos para C16 a C19, y los conteos del resumen.
    """
    items = [h for h in (hilos or {}).get("hilos", []) if isinstance(h, dict)]
    acts = world.get("acts", [])
    ids = _character_ids(world)
    # «En escena» lista quién sigue presente en cada acto; sin esa fila se usa la de entradas
    cells = [{ids[n] for n in cell if n in ids} for cell in (_lane(story, "enescena") or _lane(story, "personajes"))]
    node_ids = {n["id"] for n in (decisions or {}).get("nodes", [])}
    tape_ids = {t["n"] for t in (decisions or {}).get("cintas", [])} or set(range(1, TAPE_COUNT + 1))
    out = {"total": len(items), "sin_resolver": [], "sin_sembrar": [], "antes": [], "faltan": [], "refs": [], "pares": 0, "refs_total": 0,
           "por_estado": {}, "por_tipo": {}}
    for h in items:
        hid = h.get("id", "?")
        out["por_estado"][h.get("estado")] = out["por_estado"].get(h.get("estado"), 0) + 1
        out["por_tipo"][h.get("tipo")] = out["por_tipo"].get(h.get("tipo"), 0) + 1
        sowed, solved = _entries(h, "siembra"), _entries(h, "resuelve")
        if h.get("estado") == "resuelto" and not solved:
            out["sin_resolver"].append("%s está sembrado y marcado como resuelto, pero no dice dónde se resuelve" % hid)
        elif h.get("estado") in HILO_ABIERTOS and not h.get("motivo") and not solved:
            out["sin_resolver"].append("%s está sembrado, sin resolver y sin motivo (estado %s)" % (hid, h.get("estado")))
        if solved and not sowed:
            out["sin_sembrar"].append("%s se resuelve y no se siembra en ningún sitio" % hid)
        elif sowed and solved:
            first = min(_entry_ranks(h, "siembra"), default=None)
            for e in solved:
                if first is not None and e.get("acto") in HILO_ACTOS and HILO_ACTOS.index(e["acto"]) < first:
                    out["antes"].append("%s se resuelve en el Acto %s, antes de sembrarse en el Acto %s" % (hid, e["acto"], HILO_ACTOS[first]))
        sowed_r, solved_r = _entry_ranks(h, "siembra"), _entry_ranks(h, "resuelve")
        if sowed_r and solved_r and max(solved_r) > min(sowed_r):
            out["pares"] += len([w for w in h.get("personajes", []) if w in ids])
        for who, gone in _missing_characters(h, ids, cells, acts):
            out["faltan"].append({"hilo": hid, "personaje": who, "actos": gone,
                                  "texto": "%s: %s no sale en el mapa de historia en el Acto %s, entre la siembra (Acto %s) y la resolución (Acto %s)" % (
                                      hid, who, ", ".join(gone), HILO_ACTOS[min(sowed_r)], HILO_ACTOS[max(solved_r)])})
        for e in sowed + solved:
            nodes, tapes = hilo_refs(e.get("ref"))
            out["refs_total"] += len(nodes) + len(tapes)
            out["refs"] += ["%s cita el nodo %s, que no existe en decisions.json" % (hid, n) for n in nodes if node_ids and n not in node_ids]
            out["refs"] += ["%s cita la cinta %d, que no existe" % (hid, t) for t in tapes if t not in tape_ids]
    return out


def _hilo_checks(world, story, decisions, hilos, add):
    """Cruces del registro de hilos con el mundo, el mapa de historia y las decisiones (C16 a C19)."""
    a = hilos_analisis(hilos, world, story, decisions)
    n = a["total"]
    add("C16", "Hilos", "Todo hilo sembrado se resuelve o dice por qué sigue abierto", n, a["sin_resolver"])
    add("C17", "Hilos", "Todo hilo resuelto se sembró antes", n, a["sin_sembrar"] + a["antes"])
    add("C18", "Hilos", "Los personajes de un hilo salen en el mapa de historia de cada acto entre la siembra y la resolución",
        a["pares"], [f["texto"] for f in a["faltan"]])
    add("C19", "Hilos", "Los nodos y las cintas que citan los hilos existen", a["refs_total"], a["refs"])


def check(world, story, decisions=None, hilos=None):
    """Evalúa las comprobaciones de coherencia. Devuelve un resumen listo para el hub."""
    acts = world.get("acts", [])
    idx = _act_index(acts)
    zones = {z["id"]: z for z in world.get("zones", [])}
    minigames = {m["id"]: m for m in world.get("minigames", [])}
    minerals = world.get("minerals", [])
    rules = world.get("rules", {})
    checks = []

    def add(cid, area, title, total, findings):
        checks.append({"id": cid, "area": area, "title": title, "total": total, "failed": len(findings), "findings": findings})

    available = {m["id"]: _earliest_act(m, zones, idx) for m in minerals}

    # --- Minerales y zonas
    add("C1", "Minerales", "Cada mineral tiene una zona principal", len(minerals),
        ["%s no tiene zona principal" % m["name"] for m in minerals if "principal" not in m["zones"].values()])
    lo, hi = rules.get("mineral_zones_min", 2), rules.get("mineral_zones_max", 3)
    add("C2", "Minerales", "Cada mineral aparece en %d–%d zonas (%s)" % (lo, hi, rules.get("fuente", "regla del diseño")), len(minerals),
        ["%s aparece en %d zona(s): %s" % (m["name"], len(m["zones"]), ", ".join(zones[z]["name"] for z in m["zones"] if z in zones))
         for m in minerals if not lo <= len(m["zones"]) <= hi])
    add("C3", "Zonas", "Cada zona tiene al menos un mineral principal", len(zones),
        ["%s no tiene mineral principal" % z["name"] for z in zones.values()
         if not any(m["zones"].get(z["id"]) == "principal" for m in minerals)])
    bad = []
    for m in minerals:
        first = available[m["id"]]
        opts = [g for g in m.get("minigames", []) if g in minigames]
        if not opts:
            bad.append("%s no tiene minijuego de extracción" % m["name"])
        elif first and min(idx[minigames[g]["act"]] for g in opts) > idx[first]:
            bad.append("%s aparece en el Acto %s pero su primer minijuego llega en el Acto %s" %
                       (m["name"], first, min((minigames[g]["act"] for g in opts), key=lambda a: idx[a])))
    add("C4", "Minerales", "Cada mineral se puede extraer con un minijuego disponible cuando aparece", len(minerals), bad)

    # --- Números base y demanda (hoy sin definir)
    add("C5", "Economía", "Cada mineral tiene sectores de demanda definidos", len(minerals),
        ["%s no tiene sectores de demanda" % m["name"] for m in minerals if not m.get("sectors")])
    add("C6", "Economía", "Cada mineral tiene precio base", len(minerals),
        ["%s no tiene precio base" % m["name"] for m in minerals if m.get("base_price") in (None, 0)])

    # --- Mecánicas y recetas
    needs = [(mech, ing) for mech in world.get("mechanics", []) for ing in mech.get("needs_minerals", [])]
    bad = []
    names = {m["id"]: m["name"] for m in minerals}
    for mech, ing in needs:
        first = available.get(ing)
        if first is None or idx[first] > idx[mech["act"]]:
            bad.append("%s llega en el Acto %s pero necesita %s, que aparece en el Acto %s" % (mech["name"], mech["act"], names[ing], first or "—"))
    add("C7", "Mecánicas", "Lo que necesita un mineral lo tiene disponible cuando se desbloquea", len(needs), bad)
    taller = next((mech for mech in world.get("mechanics", []) if mech["id"] == "taller"), None)
    groups = [(r, g) for r in world.get("recipes", []) for g in r.get("inputs", [])]
    bad = []
    if taller:
        for r, group in groups:
            firsts = [available[i] for i in group if available.get(i)]
            if not firsts or min(idx[a] for a in firsts) > idx[taller["act"]]:
                got = min(firsts, key=lambda a: idx[a]) if firsts else "—"
                bad.append("%s necesita %s, que aparece en el Acto %s, y el taller abre en el Acto %s" %
                           (r["name"], " o ".join(names[i] for i in group), got, taller["act"]))
    add("C8", "Mecánicas", "Los ingredientes de cada receta existen cuando abre el taller", len(groups), bad)

    # --- Mapa de historia frente al registro
    story_min = _lane(story, "minerales")
    by_name = {m["name"]: m for m in minerals}
    bad, total = [], 0
    for i, cell in enumerate(story_min):
        for name in cell:
            if name in by_name:
                total += 1
                first = available[by_name[name]["id"]]
                if first != acts[i]:
                    bad.append("%s: el mapa de historia lo pone en el Acto %s y las zonas lo hacen aparecer en el Acto %s" % (name, acts[i], first))
    add("C9", "Historia", "Los minerales del mapa de historia coinciden con las zonas", total, bad)
    story_zones = _lane(story, "zonas")
    zone_by_name = {z["name"]: z for z in zones.values()}
    bad, total = [], 0
    for i, cell in enumerate(story_zones):
        for name in cell:
            if name in zone_by_name:
                total += 1
                if zone_by_name[name]["act"] != acts[i]:
                    bad.append("%s: el mapa de historia la pone en el Acto %s y el registro en el %s" % (name, acts[i], zone_by_name[name]["act"]))
    add("C10", "Historia", "Las zonas del mapa de historia coinciden con el registro", total, bad)
    chars = {}
    for c in world.get("characters", []):
        chars[c["name"]] = c
        for alias in c.get("aka", []):
            chars[alias] = c
    bad, total = [], 0
    for i, cell in enumerate(_lane(story, "personajes")):
        for name in cell:
            total += 1
            c = chars.get(name)
            if c is None:
                bad.append("%s aparece en el mapa de historia y no existe en el registro de personajes" % name)
            elif c["act"] != acts[i]:
                bad.append("%s: el mapa de historia lo pone en el Acto %s y el registro en el %s" % (name, acts[i], c["act"]))
    add("C11", "Historia", "Los personajes del mapa de historia coinciden con el registro", total, bad)

    if decisions and decisions.get("nodes"):
        _decision_checks(world, story, decisions, add)
    if hilos and hilos.get("hilos"):
        _hilo_checks(world, story, decisions, hilos, add)

    total = sum(c["total"] for c in checks)
    failed = sum(c["failed"] for c in checks)
    return {
        "pct": round(100 * (total - failed) / total) if total else None,
        "total": total,
        "failed": failed,
        "checks": checks,
    }
