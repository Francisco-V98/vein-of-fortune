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

# Economía (F0-52): ids de sector, orden de las etiquetas de volatilidad y umbrales de vigilancia (ids ASCII como en world.json)
SECTORS = ["ferrocarril", "energia", "militar", "agricultura", "lujo", "tecnologia"]
VOLATILITY_ORDER = ["baja", "baja-media", "media", "media-alta", "alta", "muy alta"]
TIER_MIN, TIER_MAX = 1, 5
SURVEILLANCE_RANGE = (0, 100)
_WAIT_REF = re.compile(r"\u23f3\s*([A-Z]\d+-\d+)")
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
        if r.get("act") is not None and r["act"] not in idx:
            errors.append("receta %s: acto desconocido (%s)" % (r["id"], r["act"]))
        for b in r.get("buyers", []):
            if b not in factions:
                errors.append("receta %s tiene un comprador inexistente: %s" % (r["id"], b))
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


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def _by_int_key(d):
    """Pares (nivel, valor) de un objeto cuyas claves son niveles en texto («2», «3»...), ordenados por nivel."""
    return sorted(((int(k), v) for k, v in (d or {}).items() if str(k).isdigit()), key=lambda p: p[0])


def _strings(obj):
    """Todos los textos de una estructura JSON anidada."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)


def _has_economy(world):
    return "economy" in world or any("tier" in m or "daily_cap" in m for m in world.get("minerals", []))


def _economy_mineral_checks(world, add):
    """Campos económicos de cada mineral (C20 a C26)."""
    minerals = world.get("minerals", [])
    n = len(minerals)
    prices = [(m, m.get("base_price")) for m in minerals]

    # C20 precio base entero positivo y no todos iguales
    bad = ["%s: el precio base debe ser un entero mayor que 0 (es %r)" % (m["name"], p) for m, p in prices if not _int(p) or p <= 0]
    valid = [p for _, p in prices if _int(p) and p > 0]
    if len(valid) > 1 and len(set(valid)) == 1:
        bad.append("Todos los minerales tienen el mismo precio base (%d)" % valid[0])
    add("C20", "Economía", "El precio base de cada mineral es un entero mayor que 0 y no son todos iguales", n, bad)

    # C21 el precio sube con el nivel de herramienta; la Aetherita es lo más caro y el carbón lo más barato
    bad, tiers = [], {}
    for m, p in prices:
        if _int(p) and _int(m.get("tier")):
            tiers.setdefault(m["tier"], []).append((p, m["name"]))
    ordered = sorted(tiers)
    for lo, hi in zip(ordered, ordered[1:]):
        top, low_name = max(tiers[lo])
        bottom, high_name = min(tiers[hi])
        if bottom <= top:
            bad.append("%s (nivel %d, %d esquirlas) no vale más que %s (nivel %d, %d esquirlas)" % (high_name, hi, bottom, low_name, lo, top))
    by_id = {m["id"]: m for m in minerals}
    ranked = sorted((p, m["name"]) for m, p in prices if _int(p))
    for mid, word, pick in (("carbon", "barato", ranked[:2]), ("aetherita", "caro", ranked[-2:][::-1])):
        if mid in by_id and len(ranked) > 1:
            best, other = pick
            if by_id[mid].get("base_price") != best[0] or best[0] == other[0]:
                bad.append("%s debe ser el mineral más %s, y el más %s es %s" % (by_id[mid]["name"], word, word, best[1]))
    add("C21", "Economía", "El precio base sube con el nivel de herramienta; el carbón es lo más barato y la Aetherita lo más caro", n, bad)

    # C22 nivel de herramienta entre 1 y 5
    add("C22", "Economía", "Cada mineral tiene un nivel de herramienta entre %d y %d" % (TIER_MIN, TIER_MAX), n,
        ["%s: nivel de herramienta fuera de %d–%d (%r)" % (m["name"], TIER_MIN, TIER_MAX, m.get("tier"))
         for m in minerals if not _int(m.get("tier")) or not TIER_MIN <= m["tier"] <= TIER_MAX])

    # C23 sectores válidos, al menos 2, pesos enteros positivos que suman 100
    bad = []
    for m in minerals:
        sec = m.get("sectors")
        if not isinstance(sec, dict):
            bad.append("%s: los sectores deben ser un objeto sector → peso" % m["name"])
            continue
        unknown = [k for k in sec if k not in SECTORS]
        if unknown:
            bad.append("%s: sectores desconocidos (%s)" % (m["name"], ", ".join(unknown)))
        if len(sec) < 2:
            bad.append("%s: tiene %d sector(es) y debe tener al menos 2" % (m["name"], len(sec)))
        if any(not _int(w) or w <= 0 for w in sec.values()):
            bad.append("%s: los pesos de sector deben ser enteros mayores que 0" % m["name"])
        elif sum(sec.values()) != 100:
            bad.append("%s: los pesos de sector suman %d y deben sumar 100" % (m["name"], sum(sec.values())))
    add("C23", "Economía", "Cada mineral tiene al menos 2 sectores válidos, con pesos enteros que suman 100", n, bad)

    # C24 todo sector tiene al menos un mineral
    used = {k for m in minerals if isinstance(m.get("sectors"), dict) for k in m["sectors"]}
    add("C24", "Economía", "Cada sector de demanda tiene al menos un mineral", len(SECTORS),
        ["El sector %s no tiene ningún mineral" % s for s in SECTORS if s not in used])

    # C25 tope diario y volatilidad numérica ordenados como la etiqueta; la Aetherita con el mayor tope
    bad, rank = [], {}
    for m in minerals:
        if m.get("volatility") not in VOLATILITY_ORDER:
            bad.append("%s: etiqueta de volatilidad desconocida (%r)" % (m["name"], m.get("volatility")))
        else:
            rank[m["id"]] = VOLATILITY_ORDER.index(m["volatility"])
    for field, label in (("daily_cap", "tope diario"), ("volatility_num", "volatilidad numérica")):
        for m in minerals:
            if not _num(m.get(field)) or m[field] <= 0:
                bad.append("%s: %s debe ser un número mayor que 0 (es %r)" % (m["name"], label, m.get(field)))
        ok = [m for m in minerals if m["id"] in rank and _num(m.get(field)) and m[field] > 0]
        for a in ok:
            for b in ok:
                if rank[a["id"]] < rank[b["id"]] and a[field] > b[field]:
                    bad.append("%s (%s) tiene %s mayor que %s (%s)" % (a["name"], a["volatility"], label, b["name"], b["volatility"]))
    if "aetherita" in by_id:
        caps = [m.get("daily_cap") for m in minerals if m["id"] != "aetherita" and _num(m.get("daily_cap"))]
        cap = by_id["aetherita"].get("daily_cap")
        if caps and (not _num(cap) or cap <= max(caps)):
            bad.append("La Aetherita debe tener el mayor tope diario (%r frente a %r)" % (cap, max(caps)))
    add("C25", "Economía", "El tope diario y la volatilidad numérica crecen con la etiqueta de volatilidad; la Aetherita tiene el mayor tope",
        n * 2 + 1, bad)

    # C26 liquidez positiva
    add("C26", "Economía", "Cada mineral tiene liquidez mayor que 0", n,
        ["%s: la liquidez debe ser un número mayor que 0 (es %r)" % (m["name"], m.get("liquidity"))
         for m in minerals if not _num(m.get("liquidity")) or m["liquidity"] <= 0])


def _economy_zone_checks(world, add):
    """Mezcla de menas de cada zona (C30)."""
    zones = world.get("zones", [])
    bad = []
    for z in zones:
        mix = z.get("zone_mix")
        if not isinstance(mix, dict) or not mix:
            bad.append("%s no tiene mezcla de menas" % z["name"])
            continue
        if any(not _num(v) or v <= 0 for v in mix.values()):
            bad.append("%s: los porcentajes de la mezcla deben ser mayores que 0" % z["name"])
        elif abs(sum(mix.values()) - 100) > 1e-9:
            bad.append("%s: la mezcla de menas suma %s y debe sumar 100" % (z["name"], sum(mix.values())))
        here = {m["id"] for m in world.get("minerals", []) if z["id"] in m.get("zones", {})}
        extra, missing = sorted(set(mix) - here), sorted(here - set(mix))
        if extra:
            bad.append("%s: la mezcla incluye minerales que no son de la zona (%s)" % (z["name"], ", ".join(extra)))
        if missing:
            bad.append("%s: faltan en la mezcla minerales de la zona (%s)" % (z["name"], ", ".join(missing)))
    add("C30", "Economía", "La mezcla de menas de cada zona suma 100 y solo lleva minerales de esa zona", len(zones), bad)


def _economy_tool_checks(world, add):
    """Mejoras de herramientas (C27 y C28)."""
    tools = world.get("economy", {}).get("tools", {})
    tiers = {m["id"]: m.get("tier") for m in world.get("minerals", [])}

    # C27 regla k−1: el mineral de la mejora al nivel k es de nivel ≤ k−1
    bad, total = [], 0
    for kind, steps in tools.get("upgrade_minerals", {}).items():
        for level, step in _by_int_key(steps):
            total += 1
            mineral, qty = step.get("mineral"), step.get("qty")
            if mineral not in tiers:
                bad.append("%s al nivel %d usa un mineral inexistente (%s)" % (kind, level, mineral))
            elif not _int(tiers[mineral]) or tiers[mineral] > level - 1:
                bad.append("%s al nivel %d usa %s, de nivel %s: debe ser como mucho %d" % (kind, level, mineral, tiers[mineral], level - 1))
            if not _int(qty) or qty <= 0:
                bad.append("%s al nivel %d: la cantidad de %s debe ser un entero mayor que 0" % (kind, level, mineral))
    if not total:
        bad.append("economy.tools.upgrade_minerals no define ninguna mejora")
    add("C27", "Economía", "El mineral de cada mejora de herramienta es de nivel ≤ nivel−1", total or 1, bad)

    # C28 costos estrictamente crecientes por nivel (herramientas y detector)
    bad, total = [], 0
    series = [("la herramienta " + kind, [(lv, c) for lv, c in _by_int_key(costs)]) for kind, costs in tools.get("upgrade_cost", {}).items()]
    detector = tools.get("detector", {}).get("levels", [])
    if detector:
        series.append(("el detector", [(d.get("level"), d.get("cost")) for d in detector if _int(d.get("level")) and d["level"] > 1]))  # el nivel 1 es el de partida
    for label, costs in series:
        total += 1
        values = [c for _, c in costs]
        if any(not _num(c) or c <= 0 for c in values):
            bad.append("%s: todos los costos de mejora deben ser números mayores que 0" % label)
        elif any(b <= a for a, b in zip(values, values[1:])):
            bad.append("%s: los costos de mejora no crecen estrictamente por nivel (%s)" % (label, ", ".join(str(c) for c in values)))
    if not total:
        bad.append("economy.tools.upgrade_cost no define ningún costo de mejora")
    add("C28", "Economía", "Los costos de mejora crecen estrictamente con el nivel", total or 1, bad)


def _economy_other_checks(world, add, task_status):
    """Vigilancia (C29), salarios (C31) y marcas de espera (C32)."""
    econ = world.get("economy", {})

    # C29 umbrales de vigilancia consecutivos, sin huecos ni solapes
    levels = econ.get("surveillance", {}).get("levels", [])
    bad = []
    lo, hi = SURVEILLANCE_RANGE
    if not levels:
        bad.append("economy.surveillance.levels no define ningún umbral")
    else:
        expect = lo
        for lv in levels:
            a, b = lv.get("min"), lv.get("max")
            if not _int(a) or not _int(b) or a > b:
                bad.append("%s: umbral inválido (%r–%r)" % (lv.get("id"), a, b))
                continue
            if a != expect:
                bad.append("%s empieza en %d y debería empezar en %d (%s)" % (lv.get("id"), a, expect, "solape" if a < expect else "hueco"))
            expect = b + 1
        if expect != hi + 1:
            bad.append("Los umbrales terminan en %d y deben terminar en %d" % (expect - 1, hi))
    add("C29", "Economía", "Los umbrales de vigilancia cubren %d–%d en orden y sin solapes" % (lo, hi), len(levels) or 1, bad)

    # C31 salarios positivos y coherentes
    emp = econ.get("employees", {})
    bad, total = [], 0
    sal = [(lv.get("level"), lv.get("salary_per_day")) for lv in emp.get("levels", [])]
    total += len(sal)
    if any(not _num(s) or s <= 0 for _, s in sal):
        bad.append("Los salarios de los empleados deben ser números mayores que 0")
    elif any(b <= a for (_, a), (_, b) in zip(sal, sal[1:])):
        bad.append("El salario de los empleados no crece con el nivel (%s)" % ", ".join(str(s) for _, s in sal))
    for role, by_act in emp.get("support_salary_per_day", {}).items():
        if isinstance(by_act, dict):
            total += 1
            values = [by_act[k] for k in ("II", "III", "IV") if k in by_act]
            if any(not _num(v) or v <= 0 for v in values) or any(b <= a for a, b in zip(values, values[1:])):
                bad.append("El salario de apoyo (%s) debe ser positivo y crecer con el acto" % role)
    mult = _by_int_key(emp.get("contract_salary_mult"))
    if mult:
        total += 1
        values = [v for _, v in mult]
        if any(not _num(v) or v <= 0 for v in values) or any(b >= a for a, b in zip(values, values[1:])):
            bad.append("El contrato corto debe pagar más: los multiplicadores deben bajar al alargar el contrato (%s)" % values)
    phi = _by_int_key(emp.get("dismissal_phi"))
    if phi:
        total += 1
        values = [v for _, v in phi]
        if any(not _num(v) or not 0 < v <= 1 for v in values) or any(b <= a for a, b in zip(values, values[1:])):
            bad.append("La indemnización φ debe estar en (0, 1] y crecer con la duración del contrato (%s)" % values)
    add("C31", "Economía", "Los salarios son positivos, crecen con el nivel y el contrato corto paga más", total or 1, bad)

    # C32 ningún ⏳ del registro apunta a una tarea terminada o inexistente
    if task_status is not None:
        refs = [(t, w) for t in _strings(world) for w in _WAIT_REF.findall(t)]
        bad = []
        for text, tid in refs:
            if tid not in task_status:
                bad.append("world.json: ⏳ %s apunta a una tarea que no existe" % tid)
            elif task_status[tid] == "done":
                bad.append("world.json: ⏳ %s apunta a una tarea terminada: debe resolverse" % tid)
        add("C32", "Economía", "Los ⏳ del registro del mundo apuntan a tareas pendientes que existen", len(refs), sorted(set(bad)))


def _economy_checks(world, add, task_status=None):
    """Campos económicos del registro (F0-52): C20 a C32. Solo corre si el registro los tiene."""
    if not _has_economy(world):
        return
    _economy_mineral_checks(world, add)
    _economy_tool_checks(world, add)
    _economy_other_checks(world, add, task_status)
    _economy_zone_checks(world, add)


def check(world, story, decisions=None, hilos=None, task_status=None):
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
         for m in minerals if not lo <= len(m["zones"]) <= hi and m["id"] not in rules.get("mineral_zones_excepciones", [])])
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
    recipes = world.get("recipes", [])
    groups = [(r, g) for r in recipes for g in r.get("inputs", [])]
    bad = []
    if taller:
        for r in recipes:
            act = r.get("act")
            if act not in idx:
                bad.append("%s no tiene un acto válido (%s): cada receta declara en qué acto se desbloquea" % (r["name"], act or "sin acto"))
                continue
            if idx[act] < idx[taller["act"]]:
                bad.append("%s se desbloquea en el Acto %s y el taller abre en el Acto %s" % (r["name"], act, taller["act"]))
            for group in r.get("inputs", []):
                firsts = [available[i] for i in group if available.get(i)]
                if not firsts or min(idx[a] for a in firsts) > idx[act]:
                    got = min(firsts, key=lambda a: idx[a]) if firsts else "—"
                    bad.append("%s (Acto %s) necesita %s, que aparece en el Acto %s" %
                               (r["name"], act, " o ".join(names[i] for i in group), got))
    add("C8", "Mecánicas", "Cada receta se desbloquea con el taller o después y sus ingredientes existen en el acto de la receta",
        len(groups) + len(recipes), bad)

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
    _economy_checks(world, add, task_status)
    checks.sort(key=lambda c: int(c["id"][1:]))

    total = sum(c["total"] for c in checks)
    failed = sum(c["failed"] for c in checks)
    return {
        "pct": round(100 * (total - failed) / total) if total else None,
        "total": total,
        "failed": failed,
        "checks": checks,
    }
