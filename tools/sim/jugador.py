"""Jugador simulado: estado, decisiones y el paso de un día.

Una `Partida` simula a un jugador que reparte los 3 bloques de cada día entre expediciones, tienda y descanso,
vende por el canal que más le conviene (tienda, spot, pedidos, mercado negro, canal legal de la Aetherita),
contrata empleados y (en la campaña) compra mejoras, paga la deuda y gasta en estilo de vida.
Todas las cifras del juego vienen de `mundo.cargar()`; los supuestos de modelado, de supuestos.json.
"""
import math

from .mercado import Azar, MercadoRef

def C_MEDIA(xs):
    return sum(xs) / len(xs)


EPS = 1e-9  # tolerancia numérica, no una cifra del juego
ING = ("v_spot", "v_tienda", "v_pedidos", "v_negro", "v_legal", "v_especial")
OPE = ("desgaste", "viaje", "guardar", "renta", "filtro")


def srnd(x, az):
    """Redondeo aleatorio: la parte decimal es la probabilidad de subir una unidad."""
    f = math.floor(x)
    return f + (1 if az.u() < x - f else 0)


class Partida:
    def __init__(self, P, S, semilla, perfil, cfg):
        self.P, self.S, self.cfg, self.perfil = P, S, cfg, perfil
        sub = S["semillas"]["sub"]
        self.az = Azar(semilla)
        self.az_m = Azar(semilla + sub["mercado"])
        self.az_e = Azar(semilla + sub["empleados"])
        self.az_d = Azar(semilla + sub["decisiones"])
        self.az_p = Azar(semilla + sub["pedidos"])
        self.mk = MercadoRef(P, self.az_m, cfg["ruido"], acto=cfg["acto"], sueltos=cfg.get("sueltos", True),
                             tope_diario=cfg.get("tope_diario", True), comprador_cap=cfg.get("buyer_cap", True))
        self.mk.caida_max = S["mercado"]["caida_max_pct"]
        self.mk.markup_tienda = cfg.get("markup_tienda", P["mk"]["tienda"]["media"])
        self.acto = cfg["acto"]
        self.motor = cfg.get("motor_minas")  # None = el modelo sin entradas (las 50 reglas vigentes)
        self.integridad = 100.0  # % de integridad de la herramienta (solo con el motor de minas)
        self.dia = cfg.get("dia0", P["t"]["inicio_dia"])
        self.cash = float(cfg.get("cash", 0.0))
        self.stock = {m: 0.0 for m in P["min"]}
        self.rich = {z: float(P["Z"][z]["riqueza0"]) for z in P["zonas"]}
        self.region = P["viaje"]["lugares"][0]
        self.niveles = dict(cfg["niveles"])
        self.tienda = cfg.get("tienda", 0)
        self.almacen = cfg.get("almacen", 0)
        self.casa = cfg.get("casa", 0)
        self.f = {}
        self.vig = 0.0
        self.cierre_negro = 0
        self.cierre_tienda = 0
        self.sobornos = 0
        self.dia_soborno = 0
        self.ultimo_soborno = 0
        self.guardias = cfg.get("guardias", 0)
        self.dependiente = cfg.get("dependiente", False)
        self.emps = [self._nuevo_emp(n) for n in cfg.get("empleados", [])]
        self.prod_ema = {m: 0.0 for m in P["min"]}
        self.uso_zona = {z: 0.0 for z in P["zonas"]}
        self.ordenes = []
        self.pedidos_extra = 0.0
        self.ultimo_pedido = {}
        self.cont = {"exp": 0, "exp_zona": {z: 0 for z in P["zonas"]}, "tienda_bloques": 0, "redadas": 0, "noches_negras": 0,
                     "menas": 0, "descartes": 0, "aeth_vendidas": 0, "pedidos_hechos": 0, "pedidos_perdidos": 0,
                     "dias_tope": 0, "emp_exp": 0, "emp_baja": 0, "bruto": 0.0, "rich_sum": 0.0, "rich_n": 0,
                     "especiales": 0, "especiales_viales": 0, "slip": 0.0}
        self.neg_extra = 0.0
        self.vig_aeth = 0.0
        self.e_dia = {"ing": 0.0}
        self.dia_inicio = self.dia
        self.energia_fn = cfg["energia"]
        self.zonas_ok = cfg.get("zonas")
        self.wmem = None
        self.ev_cache = {}
        self.cuota_dia = 0.0
        self._tipo_de_juego = {}
        for t in P["herr"]["tipos"]:
            self._tipo_de_juego[P["herr"]["tipo"][t]["minijuego"]] = t

    # ------------------------------------------------------------------ contabilidad
    def mover(self, cat, monto):
        self.cash += monto
        self.f[cat] = self.f.get(cat, 0.0) + monto

    def ingreso_neto(self, f=None):
        f = self.f if f is None else f
        return sum(f.get(c, 0.0) for c in ING) + sum(f.get(c, 0.0) for c in OPE)

    def valor_stock(self, sin_aeth=False):
        mk = self.mk
        return sum(u * mk.justo(m) for m, u in self.stock.items() if u > 0 and not (sin_aeth and m == "aetherita"))

    def patrimonio(self):
        if self.cfg.get("patrimonio_fijo") is not None:
            return self.cfg["patrimonio_fijo"]
        return self.cash + self.valor_stock()

    def w(self):
        return self.mk.peso_jugador(self.patrimonio())

    # ------------------------------------------------------------------ herramientas
    def nivel_min(self, m, tier_max=None):
        """Nivel de la mejor herramienta que puede extraer el mineral m (0 si no puede)."""
        P = self.P
        d = P["M"][m]
        if tier_max is not None and d["tier"] > tier_max:
            return 0
        if m == "aetherita" and self.cfg.get("aeth_modo") == "ninguno":
            return 0
        mejor = 0
        if P["exp"]["aeth_minijuego"] in d["minijuegos"]:
            tipos = P["exp"]["aeth_tipos"]
        else:
            tipos = [self._tipo_de_juego[j] for j in d["minijuegos"] if j in self._tipo_de_juego]
        for t in tipos:
            mejor = max(mejor, self.niveles.get(t, 0))
        if mejor < d["tier"]:
            return 0
        if P["exp"]["aeth_minijuego"] in d["minijuegos"] and mejor < P["exp"]["aeth_nivel"]:
            return 0
        return mejor

    def tipo_usado(self, m):
        P = self.P
        d = P["M"][m]
        if P["exp"]["aeth_minijuego"] in d["minijuegos"]:
            tipos = P["exp"]["aeth_tipos"]
        else:
            tipos = [self._tipo_de_juego[j] for j in d["minijuegos"] if j in self._tipo_de_juego]
        return max(tipos, key=lambda t: self.niveles.get(t, 0))

    def nivel_max(self):
        return max(self.niveles.values())

    def nivel_detector(self):
        """Nivel del detector del acto (el detector se mejora aparte de la herramienta, documento 28 §5.5)."""
        return self.P["herr"]["detector_acto"].get(self.acto, 1)

    def carga(self, profunda):
        c = self.P["herr"]["niveles"][self.nivel_max() - 1]["carga"]
        return c * (self.P["exp"]["carga_prof"] if profunda else 1)

    def energia(self):
        e = self.energia_fn(self)
        if self.motor:
            e += self.motor.delta_energia()
        if self.casa > 0:
            e += self.P["energia"]["casa"][self.casa - 1]
        return e

    # ------------------------------------------------------------------ valor de una expedición (decisión)
    def valor_unidad(self, m, w, q=1.0):
        mk = self.mk
        if m == "aetherita":
            return self.valor_aeth(q)
        return mk.precio_venta(m, q, w, "spot")

    def aeth_cupo(self):
        """Viales que aún se pueden colocar (canal legal) dentro del horizonte de la política."""
        P, S = self.P, self.S
        if self.cfg.get("aeth_modo") == "negro3":
            return float(S["prototipo"]["aeth_noche"])
        if self.cfg.get("aeth_modo") == "ninguno":
            return 0.0
        if P["actos"].index(self.acto) < P["actos"].index(P["exp"]["aeth_legal"]["desde"]):
            return 0.0
        return max(0.0, P["exp"]["aeth_legal"]["tope"] * S["politica"]["aeth_cobertura_dias"] - self.stock["aetherita"])

    def valor_aeth(self, q):
        P = self.P
        cur = self.mk.cur["aetherita"]
        if self.cfg.get("aeth_modo") == "negro3":
            return cur * (1.0 + P["M"]["aetherita"]["prima_negra"] / 100.0) * self.S["prototipo"]["aeth_descuento"]
        lc = P["exp"]["aeth_legal"]
        imp = (1.0 - P["mk"]["impuesto"] / 100.0) if lc["impuesto"] else 1.0
        return cur * lc["precio"] * imp

    def plan_zona(self, z, w, rich, efic=1.0, tier_max=None, E=None, foco=None):
        """Plan de la expedición a z: conjunto S de minerales que se extraen, menas esperadas y valor neto.

        Devuelve dict o None si no se puede extraer nada."""
        P, S, cfg = self.P, self.S, self.cfg
        Z = P["Z"][z]
        prof = Z["profunda"]
        E = self.energia() if E is None else E
        Eeff = E * (P["exp"]["energia_prof"] if prof else 1.0)
        c = cfg["descarte"]
        mk = self.mk
        proto = cfg.get("proto", False)
        niv = P["herr"]["niveles"]
        lvl_any = max(self.nivel_max(), 1)
        filas = []
        resto = []
        for m, pc in Z["mezcla"].items():
            p = pc / 100.0
            d = P["M"][m]
            lvl = self.nivel_min(m, tier_max)
            if lvl > 0:
                e = d["energia"] * niv[lvl - 1]["energia"]
                u1 = d["rend"] * niv[lvl - 1]["rend"] * rich * efic * self.calidad_media()
                v = u1 * self.valor_unidad(m, w)
                if m == "aetherita":
                    if self.aeth_cupo() <= 0:
                        resto.append((m, p, e))
                        continue
                filas.append([m, p, e, v, u1, lvl, self.desgaste_mena(m, lvl)])
            else:
                resto.append((m, p, d["energia"] * niv[lvl_any - 1]["energia"]))
        if not filas:
            return None
        if cfg["mina_todo"]:
            elegidas = filas
        else:
            filas.sort(key=lambda r: -(r[3] / r[2]))
            mejor, mejor_r = None, -1.0
            fuera_base = sum(r[1] * r[2] for r in resto)
            for k in range(1, len(filas) + 1):
                s_in = filas[:k]
                s_out = filas[k:]
                num = sum(r[1] * r[3] for r in s_in)
                den = sum(r[1] * r[2] for r in s_in) + c * (fuera_base + sum(r[1] * r[2] for r in s_out))
                if den <= 0:
                    continue
                r_k = num / den
                if r_k > mejor_r:
                    mejor_r, mejor = r_k, k
            elegidas = filas[:mejor]
            if foco and foco not in [r[0] for r in elegidas]:
                extra = [r for r in filas if r[0] == foco]
                elegidas = elegidas + extra
        elegidas_ids = [r[0] for r in elegidas]
        fuera = [r for r in filas if r[0] not in elegidas_ids]
        if cfg["mina_todo"]:
            # el prototipo renormaliza sobre lo extraíble y no cobra el descarte
            tot = sum(r[1] for r in elegidas)
            e_med = sum(r[1] * r[2] for r in elegidas) / tot
            menas = Eeff / e_med
            probs = {r[0]: r[1] / tot for r in elegidas}
        else:
            den = sum(r[1] * r[2] for r in elegidas) + c * (sum(r[1] * r[2] for r in fuera) + sum(r[1] * r[2] for r in resto))
            draws = Eeff / den
            probs = {r[0]: r[1] * draws for r in elegidas}
            menas = sum(probs.values())
            probs = {m: x / menas for m, x in probs.items()}
        tope_menas = P["exp"]["tope_menas"] * Z["bloques"]
        if menas > tope_menas:
            menas = float(tope_menas)
        unidades = {}
        for r in elegidas:
            unidades[r[0]] = menas * probs[r[0]] * r[4]
        tot_u = sum(unidades.values())
        car = self.carga(prof)
        if tot_u > car:
            k = car / tot_u
            unidades = {m: u * k for m, u in unidades.items()}
            menas *= k
        val = 0.0
        for m, u in unidades.items():
            if m == "aetherita":
                val += min(u, self.aeth_cupo()) * self.valor_unidad(m, w)
            else:
                val += u * mk.precio_venta(m, u, w, "spot")
        # desgaste esperado: cada mena gasta la herramienta con la que se extrae
        if proto:
            lvl = self.nivel_max()
            costo_pt = P["herr"]["rep_dinero"][lvl - 1] + P["M"][P["herr"]["rep_pieza"][lvl - 1]]["precio"] / P["herr"]["rep_pts_pieza"]
            desgaste = menas * S["prototipo"]["pts_mena"] * costo_pt
        else:
            desgaste = 0.0
            for r in elegidas:
                desgaste += menas * probs[r[0]] * r[6]
        filtro = 0.0
        if "aetherita" in unidades and not proto:
            filtro = P["exp"]["aeth_filtro"]
        return {"z": z, "S": elegidas_ids, "menas": menas, "unidades": unidades, "valor": val, "desgaste": desgaste,
                "filtro": filtro, "ev": val - desgaste - filtro, "prof": prof, "probs": probs, "E": Eeff, "efic": efic,
                "tier_max": tier_max}

    def desgaste_mena(self, m, lvl):
        """Costo esperado de reparar el desgaste de extraer una mena de m con una herramienta de nivel lvl."""
        P = self.P
        d = P["M"][m]
        pts = self.desgaste_medio() * (1.0 + P["herr"]["dureza"] * (d["tier"] - 1))
        t = self.tipo_usado(m)
        money = P["herr"]["rep_dinero"][lvl - 1] * P["herr"]["tipo"][t]["mult"]
        parte = P["M"][P["herr"]["rep_pieza"][lvl - 1]]["precio"] / P["herr"]["rep_pts_pieza"]
        return pts * (money + parte)

    def calidad_media(self):
        if self.cfg.get("proto"):
            return self.S["prototipo"]["calidad"]
        pr = self.perfil["probs"]
        mr = self.P["exp"]["mult_res"]
        return sum(p / 100.0 * mr[r] for p, r in zip(pr, self.P["resultados"]))

    def desgaste_medio(self):
        pr = self.perfil["probs"]
        dg = self.P["herr"]["desgaste"]
        return sum(p / 100.0 * dg[r] for p, r in zip(pr, self.P["resultados"]))

    # ------------------------------------------------------------------ ejecutar una expedición
    def ejecutar(self, plan, efic=1.0, tier_max=None, emp=None, forzar=None):
        """Realiza la expedición con menas discretas. Devuelve unidades extraídas (dict)."""
        P, S, cfg = self.P, self.S, self.cfg
        az = self.az_e if emp is not None else self.az
        z = plan["z"]
        Z = P["Z"][z]
        rich = self.rich[z] / 100.0
        mot = self.motor
        if mot:  # interruptor v2 (F0-93): entrada, cierres, batería, clima y estación
            if emp is None:
                mot.entrar(z, self.nivel_detector())
            rich *= mot.factor(z, emp is not None)
        niv = P["herr"]["niveles"]
        mr = P["exp"]["mult_res"]
        resultados = P["resultados"]
        probs_res = self.perfil["probs"]
        unidades = {}
        if cfg.get("proto"):
            for m, u in plan["unidades"].items():
                lo_u, hi_u = S["prototipo"]["ruido_unidades"]
                unidades[m] = u * (lo_u + (hi_u - lo_u) * az.u())
            wear = plan["desgaste"]
            self.mover("desgaste", -wear)
            self.cont["menas"] += plan["menas"]
        else:
            E = plan["E"]
            c = cfg["descarte"]
            sel = set(plan["S"])
            mezcla = [(m, pc / 100.0) for m, pc in Z["mezcla"].items()]
            lvl_any = max(self.nivel_max(), 1)
            carga = self.carga(Z["profunda"])
            tope_menas = P["exp"]["tope_menas"] * Z["bloques"]
            menas = 0
            total_u = 0
            desgaste_total = 0.0
            guardar = 0
            escaneos = 0
            tope_escaneos = S["politica"]["max_escaneos_por_bloque"] * Z["bloques"]
            if mot:  # las menas visibles acotan lo que se puede mirar (todas) y lo que se puede picar (la mitad)
                vis = mot.visibles(z, az) * Z["bloques"]
                tope_escaneos = max(1, int(vis))
                tope_menas = max(1, math.ceil(vis * mot.P["picables"]))
            while E > 0:
                escaneos += 1
                if escaneos > tope_escaneos:
                    break
                k = az.u()
                acum = 0.0
                m = mezcla[-1][0]
                for mm, p in mezcla:
                    acum += p
                    if k <= acum:
                        m = mm
                        break
                d = P["M"][m]
                quiere = m in sel
                tam = 1.0
                if mot and emp is None:  # el detector gasta una carga por mena; sin carga se pica a ciegas
                    tam = mot.tamano(az.u())  # cantidad real de la mena (el rango que muestra el detector)
                    if mot.escanear():
                        if quiere and tam < mot.saltar_si_menor():
                            quiere = False  # el rango de cantidad enseña que es pequeña: se salta sin gastar energía
                    elif not quiere and self.nivel_min(m, tier_max) > 0:
                        quiere = True
                if quiere:
                    lvl = self.nivel_min(m, tier_max)
                    e = d["energia"] * niv[lvl - 1]["energia"]
                    if e > E:
                        break
                    E -= e
                    k2 = az.u() * 100.0
                    acum = 0.0
                    res = resultados[-1]
                    for pr, r in zip(probs_res, resultados):
                        acum += pr
                        if k2 <= acum:
                            res = r
                            break
                    if forzar:
                        res = forzar
                    mellada = 1.0
                    if mot and emp is None:  # herramienta mellada (< 20 % de integridad): baja el margen del minijuego
                        mellada = mot.mellada(self.integridad)
                    u = srnd(d["rend"] * niv[lvl - 1]["rend"] * mr[res] * rich * efic * mellada * tam, az)
                    if total_u + u > carga:
                        u = int(carga - total_u)
                    unidades[m] = unidades.get(m, 0) + u
                    total_u += u
                    menas += 1
                    pts = P["herr"]["desgaste"][res] * (1.0 + P["herr"]["dureza"] * (d["tier"] - 1))
                    if mot and emp is None:
                        self.integridad -= pts * mot.mult_desgaste() / niv[lvl - 1]["dur"] * 100.0
                    t = self.tipo_usado(m)
                    money = P["herr"]["rep_dinero"][lvl - 1] * P["herr"]["tipo"][t]["mult"]
                    parte = P["M"][P["herr"]["rep_pieza"][lvl - 1]]["precio"] / P["herr"]["rep_pts_pieza"]
                    desgaste_total += pts * (money + parte)
                    if m == "aetherita":
                        guardar = 1
                    if total_u >= carga or menas >= tope_menas:
                        break
                elif mot and emp is None:
                    self.cont["descartes"] += 1  # con carga se descarta gratis: el costo es la carga
                else:
                    ec = d["energia"] * niv[lvl_any - 1]["energia"] * c
                    if ec > E:
                        break
                    E -= ec
                    self.cont["descartes"] += 1
            self.cont["menas"] += menas
            if mot:
                desgaste_total *= mot.mult_desgaste()
            self.mover("desgaste", -desgaste_total)
            if guardar:
                self.mover("filtro", -P["exp"]["aeth_filtro"])
        for m, u in unidades.items():
            self.stock[m] += u
            if emp is None:
                self.cont["bruto"] += u * self.mk.justo(m)
            self.prod_ema[m] += u
        if emp is None:
            self.cont["rich_sum"] += self.rich[z]
            self.cont["rich_n"] += 1
        self.rich[z] = max(P["exp"]["rico_min"], self.rich[z] + P["exp"]["rico_exp"] * efic)
        return unidades

    # ------------------------------------------------------------------ viaje
    def costo_viaje(self, a, b):
        if a == b:
            return 0.0
        for x, y, c in self.P["viaje"]["rutas"]:
            if (x, y) == (a, b) or (x, y) == (b, a):
                return float(c)
        return float(self.P["viaje"]["misma_boca"])

    # ------------------------------------------------------------------ ventas
    def tienda_unidades(self):
        return self.P["tienda"][self.tienda]["unidades"]

    def tienda_abierta(self):
        return self.cfg.get("tienda_activa", True) and self.cierre_tienda <= 0

    def valor_tienda_extra(self):
        """Ganancia de vender en la tienda frente al spot (decisión de usar un bloque)."""
        mk = self.mk
        w = self.w()
        rem = self.tienda_unidades()
        total = 0.0
        for m in sorted(self.stock, key=lambda x: -self.P["M"][x]["precio"]):
            if m == "aetherita":
                continue
            u = min(self.reservable(m), rem)
            if u <= 0:
                continue
            total += u * (mk.precio_venta(m, u, w, "tienda") - mk.precio_venta(m, u, w, "spot"))
            rem -= u
        return total

    def reservable(self, m):
        res = 0.0
        for o in self.ordenes:
            if o["mineral"] == m:
                res = max(res, o["qty"])
        return max(0.0, self.stock[m] - res)

    def vender_tienda(self):
        mk = self.mk
        w = self.w()
        rem = self.tienda_unidades()
        for m in sorted(self.stock, key=lambda x: -self.P["M"][x]["precio"]):
            if m == "aetherita":
                continue
            u = min(self.reservable(m), rem)
            if u <= 0:
                continue
            ing = u * mk.precio_venta(m, u, w, "tienda")
            self.mover("v_tienda", ing)
            self.stock[m] -= u
            rem -= u
        self.cont["tienda_bloques"] += 1

    def vender_spot(self, conservar):
        """Vende al spot lo que no se conserva. Si hay tope por comprador, lo que sobra se queda (si cabe en el almacén)."""
        mk = self.mk
        w = self.w()
        P, cfg = self.P, self.cfg
        for m in list(self.stock):
            u = self.stock[m]
            if u <= EPS or m == "aetherita":
                continue
            q = u - conservar.get(m, 0.0)
            if q <= EPS:
                continue
            if cfg.get("buyer_cap", True):
                libre = mk._cap_restante(m)
                if q > libre:
                    cabe = max(0.0, self.capacidad_almacen() - sum(v for k, v in self.stock.items() if k != m) - conservar.get(m, 0.0) - (u - q))
                    sobra = q - libre
                    q = q - min(sobra, max(0.0, cabe))
            p_sin = mk.precio_venta(m, q, 0.0, "spot") if q > 0 else 0.0
            ing = mk.vender(m, q, w, "spot")
            self.cont["slip"] += max(0.0, q * p_sin - ing)
            self.mover("v_spot", ing)
            self.stock[m] -= q

    def capacidad_almacen(self):
        if not self.cfg.get("almacen_activo", True):
            return float("inf")
        return self.P["mk"]["almacen"][self.almacen]["capacity"]

    def vender_aeth(self):
        P, cfg = self.P, self.cfg
        modo = cfg.get("aeth_modo", "legal")
        u = self.stock["aetherita"]
        if u <= 0 or modo == "ninguno":
            return
        if modo == "negro3":
            q = min(u, self.S["prototipo"]["aeth_noche"])
            ing = q * self.valor_aeth(1.0)
            self.mover("v_negro", ing)
            self.stock["aetherita"] -= q
            return
        if P["actos"].index(self.acto) < P["actos"].index(P["exp"]["aeth_legal"]["desde"]):
            return
        q = min(u, P["exp"]["aeth_legal"]["tope"])
        self.mover("v_legal", q * self.valor_aeth(1.0))
        self.stock["aetherita"] -= q
        self.cont["aeth_vendidas"] += q

    # ------------------------------------------------------------------ pedidos
    def generar_pedidos(self):
        P, cfg = self.P, self.cfg
        if not cfg.get("pedidos", False):
            return
        if P["actos"].index(self.acto) < P["actos"].index(P["pedidos"]["desde"]):
            return
        tipos = P["pedidos"]["tipos"]
        for oid in P["pedidos"]["orden"]:
            o = tipos[oid]
            if o["cadencia"] is None or oid == "negro":
                continue
            if P["actos"].index(self.acto) < P["actos"].index(o["desde"]):
                continue
            if self.dia % o["cadencia"] != 0:
                continue
            # mineral: elegido en proporción a la producción reciente (valor)
            pesos = [(m, self.prod_ema[m] * self.mk.justo(m)) for m in P["min"] if self.prod_ema[m] > 0 and m != "aetherita"]
            tot = sum(p for _, p in pesos)
            if tot <= 0:
                continue
            k = self.az_p.u() * tot
            acum = 0.0
            m = pesos[-1][0]
            for mm, p in pesos:
                acum += p
                if k <= acum:
                    m = mm
                    break
            dias_prod = o["cantidad"][0] + (o["cantidad"][1] - o["cantidad"][0]) * self.az_p.u()
            prod_dia = self.prod_ema[m] / max(self.S["politica"]["ventana_prod"], 1)
            qty = max(1, int(round(dias_prod * prod_dia)))
            plazo = int(round(o["plazo"][0] + (o["plazo"][1] - o["plazo"][0]) * self.az_p.u()))
            # acepta si puede cumplirlo con lo que tiene más lo que producirá
            if self.stock[m] + prod_dia * (plazo - 1) < qty:
                continue
            justo = self.mk.justo(m)
            precio = justo * (1.0 + o["prima"] / 100.0)
            self.ordenes.append({"tipo": oid, "mineral": m, "qty": qty, "vence": self.dia + plazo, "precio": precio,
                                 "valor": qty * precio, "extra_ref": justo})

    def cumplir_pedidos(self):
        P = self.P
        w = self.w()
        quedan = []
        for o in self.ordenes:
            m = o["mineral"]
            if self.stock[m] >= o["qty"]:
                ing = o["qty"] * o["precio"] * (1.0 - P["mk"]["impuesto"] / 100.0)
                ref = self.mk.precio_venta(m, o["qty"], w, "spot") * o["qty"]
                self.mover("v_pedidos", ing)
                self.pedidos_extra += ing - ref
                self.stock[m] -= o["qty"]
                self.cont["pedidos_hechos"] += 1
            elif self.dia >= o["vence"]:
                pen = P["pedidos"]["tipos"][o["tipo"]]["penal"]
                if isinstance(pen, dict):
                    idx = P["actos"].index(self.acto)
                    pen = pen[[a for a in P["actos"][: idx + 1] if a in pen][-1]]
                self.mover("penal_pedidos", -o["valor"] * pen / 100.0)
                self.cont["pedidos_perdidos"] += 1
            else:
                quedan.append(o)
        self.ordenes = quedan

    # ------------------------------------------------------------------ mercado negro
    def nivel_vig(self):
        for n in self.P["vig"]["niveles"]:
            if n["min"] <= self.vig <= n["max"]:
                return n["id"]
        return self.P["vig"]["niveles"][-1]["id"]

    def noche_negra(self, conservar):
        """Una operación negra con el stock sobrante. Devuelve True si se hizo."""
        P, cfg = self.P, self.cfg
        pol = cfg.get("negro")
        if not pol or self.cierre_negro > 0:
            return False
        if P["actos"].index(self.acto) < P["actos"].index("II"):
            return False
        V = P["vig"]
        if pol["umbral"] < 100 and self.vig >= pol["umbral"]:
            if pol.get("soborno") and self.vig >= pol["umbral"] + pol["margen_soborno"]:
                costo = (V["soborno"]["base"] + V["soborno"]["pct"] / 100.0 * self.patrimonio()) * V["soborno"]["crece"] ** self.sobornos
                self.mover("soborno", -costo)
                self.sobornos += 1
                self.ultimo_soborno = self.dia
                self.vig = max(0.0, self.vig + V["soborno"]["baja"])
            return False
        cap = V["tope_noche"][self.acto]
        mk = self.mk
        # el lote se llena con stock propio (y, si la política lo dice, comprando al spot)
        cand = sorted(P["min"], key=lambda m: -P["M"][m]["prima_negra"])
        lote = {}
        valor = 0.0
        for m in cand:
            if m == "aetherita":
                continue
            u = self.stock[m] - conservar.get(m, 0.0)
            if u <= EPS:
                continue
            pr = mk.justo(m)
            q = min(u, (cap - valor) / pr)
            if q <= 0:
                break
            lote[m] = q
            valor += q * pr
        if pol.get("comprar") and valor < cap:
            # arbitraje: comprar al spot el mineral y la cantidad que más ganan al revender en negro
            w = self.w()
            mejor = None
            for m in P["min"]:
                if m == "aetherita":
                    continue
                for f in self.S["politica"]["e1_grilla"]:
                    q = (cap - valor) * f / mk.justo(m)
                    ganancia = q * mk.precio_venta(m, q, w, "negro") - q * mk.precio_compra(m, q, w, "spot")
                    if mejor is None or ganancia > mejor[0]:
                        mejor = (ganancia, m, q)
            if mejor and mejor[0] > 0:
                _, m, q = mejor
                costo = mk.comprar(m, q, w, "spot")
                self.mover("compras", -costo)
                self.stock[m] += q
                lote[m] = lote.get(m, 0.0) + q
                valor += q * mk.justo(m)
        if not lote or valor <= 0:
            return False
        w = self.w()
        ing_neg = 0.0
        ref = 0.0
        for m, q in lote.items():
            ing_neg += q * mk.precio_venta(m, q, w, "negro")
            ref += q * mk.precio_venta(m, q, w, "spot")
            self.stock[m] -= q
        dv = (V["op_base"] + V["op_span"] * valor / cap)
        dv = min(max(dv, V["op_min"]), V["op_max"])
        if cfg.get("faroleros"):
            dv *= V["faroleros"]
        self.vig = min(100.0, self.vig + dv)
        self.cont["noches_negras"] += 1
        # inspecciones y multas
        nivel = self.nivel_vig()
        f = P["dif"]["castigo"][P["dif"]["orden"].index(cfg.get("dificultad", "intermedio"))]
        multa = 0.0
        decomiso = 0.0
        if nivel == "observado" and self.az_d.u() * 100.0 < V["multas"]["observado"]["inspection_pct"]:
            multa = max(V["multas"]["observado"]["fine_min"], V["multas"]["observado"]["fine_pct_wealth"] / 100.0 * self.patrimonio()) * f
        elif nivel == "vigilado" and self.az_d.u() * 100.0 < V["multas"]["vigilado"]["inspection_pct"]:
            multa = max(V["multas"]["vigilado"]["fine_min"], V["multas"]["vigilado"]["fine_pct_wealth"] / 100.0 * self.patrimonio()) * f
            decomiso = ing_neg * V["multas"]["vigilado"]["seizure_pct"] / 100.0
        if nivel == "bajo-investigacion":
            multa = max(V["redada"]["minimo"], V["redada"]["pct"] / 100.0 * self.patrimonio()) * f
            decomiso = ing_neg
            self.cierre_negro = V["redada"]["negro"]
            self.cierre_tienda = V["redada"]["tienda"]
            self.vig = float(V["redada"]["despues"])
            self.cont["redadas"] += 1
        self.mover("v_negro", ing_neg - decomiso)
        self.neg_extra += ing_neg - decomiso - ref
        if multa:
            self.mover("multas", -multa)
        return True

    def pedido_especial_aeth(self):
        P, cfg = self.P, self.cfg
        sp = P["vig"]["especial"]
        if not cfg.get("especiales", False) or cfg.get("aeth_modo") == "negro3":
            return
        cada = sp["cada_casilda"] if cfg.get("casilda") else sp["cada"]
        prima = sp["prima"] + (C_MEDIA(sp["bono_casilda"]) if cfg.get("casilda") else 0.0)
        if P["actos"].index(self.acto) < P["actos"].index(sp["desde"]) or self.dia % cada != 0:
            return
        if self.cierre_negro > 0 or self.stock["aetherita"] < 1:
            return
        q = min(self.stock["aetherita"], sp["viales"][0] + int(self.az_d.u() * (sp["viales"][1] - sp["viales"][0] + 1)))
        self.mover("v_especial", q * self.mk.cur["aetherita"] * (1.0 + prima / 100.0))
        self.cont["especiales"] += 1
        self.cont["especiales_viales"] += q
        self.vig_aeth += sp["vigilancia"]
        self.stock["aetherita"] -= q
        self.vig = min(100.0, self.vig + sp["vigilancia"])

    # ------------------------------------------------------------------ empleados
    def _nuevo_emp(self, n):
        lv = self.P["emp"]["niveles"][n - 1]
        return {"nivel": n, "dias": 0, "baja": 0, "lealtad": "media", "contrato": self.P["t"]["contratos"][-1]}

    def sueldo(self, e):
        P = self.P
        base = P["emp"]["niveles"][e["nivel"] - 1]["sueldo"]
        if not P["emp"]["asignacion"]["sueldo_sigue"]:
            base = P["emp"]["niveles"][0]["sueldo"]
        return base * P["emp"]["contrato"][str(e["contrato"])]

    def sueldo_apoyo(self, rol):
        P = self.P
        dep = P["emp"]["apoyo"]["dependiente"][self.acto if self.acto in P["emp"]["apoyo"]["dependiente"] else "II"]
        if rol == "dependiente":
            return dep
        if rol == "guardia":
            return dep * P["emp"]["guardia_pct"] / 100.0
        return dep

    def turno_empleados(self):
        P, S, cfg = self.P, self.S, self.cfg
        w = self.w()
        f = P["dif"]["castigo"][P["dif"]["orden"].index(self.cfg.get("dificultad", "intermedio"))]
        for e in self.emps:
            lv = P["emp"]["niveles"][e["nivel"] - 1]
            self.mover("salarios", -self.sueldo(e))
            e["dias"] += 1
            if e["dias"] % P["emp"]["sube_cada"] == 0 and e["nivel"] < len(P["emp"]["niveles"]) and self.cfg.get("ascenso", False):
                e["nivel"] += 1
            if e["baja"] > 0:
                e["baja"] -= 1
                self.cont["emp_baja"] += 1
                continue
            mejor = None
            ocupadas = sorted(self.uso_zona, key=lambda zz: -self.uso_zona[zz])[: S["politica"]["emp_evitar"]]
            for z in P["zonas"]:
                if not self.zona_disponible(z) or (z in ocupadas and self.uso_zona[z] > 0):
                    continue
                pl = self.plan_zona(z, w, self.rich[z] / 100.0, lv["efic"] / 100.0, lv["tier"])
                if pl and (mejor is None or pl["ev"] > mejor["ev"]):
                    mejor = pl
            if not mejor:
                continue
            z = mejor["z"]
            rz = P["emp"]["riesgo"][z]
            prob_herida = rz["injury_pct"] * f * (0.5 if self.guardias and P["emp"]["guardia_mitad"] else 1.0)
            if cfg.get("sin_riesgo"):
                prob_herida = 0.0
            self.cont["emp_exp"] += 1
            if prob_herida and self.az_e.u() * 100.0 < prob_herida:
                e["baja"] = rz["sick_days"]
                if self.az_e.u() * 100.0 < rz["lose_load_pct"]:
                    continue
            u = self.ejecutar(mejor, lv["efic"] / 100.0, lv["tier"], emp=e)
            robo = P["emp"]["robo"][e["lealtad"]]
            if not cfg.get("sin_riesgo") and self.az_e.u() * 100.0 < robo / P["t"]["semana"]:
                val = sum(q * self.mk.justo(m) for m, q in u.items())
                for m in u:
                    self.stock[m] -= u[m] * P["emp"]["robo_valor"] / 100.0
                self.cont["robo_valor"] = self.cont.get("robo_valor", 0.0) + val * P["emp"]["robo_valor"] / 100.0
        if self.dependiente:
            self.mover("salarios", -self.sueldo_apoyo("dependiente"))
        if self.guardias:
            self.mover("salarios", -self.guardias * self.sueldo_apoyo("guardia"))

    # ------------------------------------------------------------------ el día
    def zona_acceso(self, z):
        P = self.P
        Z = P["Z"][z]
        if self.zonas_ok is not None and z not in self.zonas_ok:
            return False
        return P["actos"].index(Z["acto"]) <= P["actos"].index(self.acto)

    def zona_disponible(self, z):
        P = self.P
        Z = P["Z"][z]
        if not self.zona_acceso(z):
            return False
        if Z["dias_abierta"]:
            wd = (self.dia - P["t"]["semana_empieza"]) % P["t"]["semana"] + 1
            if wd not in Z["dias_abierta"]:
                return False
        return True

    def opciones(self, b, w):
        P = self.P
        ops = []
        for z in P["zonas"]:
            if self.cfg.get("fija") and z != self.cfg["fija"]:
                continue
            if not self.zona_disponible(z):
                continue
            Z = P["Z"][z]
            if Z["profunda"] and b != 1:
                continue
            pl = self.plan_zona(z, w, self.rich[z] / 100.0)
            if not pl or pl["ev"] <= 0:
                continue
            tr = self.costo_viaje(self.region, Z["lugar"])
            ops.append(((pl["ev"] - tr) / Z["bloques"], z, pl, tr, Z["bloques"]))
        return ops

    def jugar_dia(self):
        P, S, cfg = self.P, self.S, self.cfg
        mk = self.mk
        mk.fijar_acto(self.acto)
        mk.nuevo_dia(self.dia)
        self.aplicar_guion()
        if self.motor:
            self.motor.actos = self.motor.actos or P["actos"]
            self.motor.nuevo_dia(self.dia, self.acto, P["zonas"])
            if self.integridad < self.motor.reparar_bajo:  # el jugador repara al empezar el día (el costo ya se cobra por punto)
                self.integridad = 100.0
        for m in self.prod_ema:
            self.prod_ema[m] *= 1.0 - 1.0 / max(S["politica"]["ventana_prod"], 1)
        self.generar_pedidos()
        self.f_dia0 = dict(self.f)
        b = 0
        usadas_tienda = 0
        while b < P["t"]["bloques_dia"]:
            mk.paso()
            w = self.w()
            if self.dependiente and b < 2 and self.tienda_abierta() and self.valor_tienda_extra() > 0:
                self.vender_tienda()
            if cfg.get("ausente"):
                b += 1
                continue
            ops = self.opciones(b, w)
            mejor = max(ops, key=lambda o: o[0]) if ops else None
            tienda_val = 0.0
            if cfg.get("tienda_activa", True) and not self.dependiente and b < 2 and self.tienda_abierta():
                tienda_val = self.valor_tienda_extra()
            eleccion = None
            if tienda_val > (mejor[0] if mejor else 0.0):
                eleccion = "tienda"
            elif mejor:
                eleccion = mejor
            eps = self.perfil["eps"]
            if eps > 0 and self.az_d.u() < eps:
                alternativas = list(ops)
                if eleccion == "tienda" or tienda_val > 0:
                    alternativas.append("tienda")
                alternativas.append(None)
                eleccion = alternativas[int(self.az_d.u() * len(alternativas))]
            if eleccion == "tienda":
                self.vender_tienda()
                b += 1
                continue
            if not eleccion:
                b += 1
                continue
            _, z, pl, tr, nb = eleccion
            self.region = P["Z"][z]["lugar"]
            if tr:
                self.mover("viaje", -tr)
            self.ejecutar(pl)
            self.cont["exp"] += 1
            self.cont["exp_zona"][z] += 1
            self.uso_zona[z] += 1.0
            for _ in range(nb - 1):
                mk.paso()
            b += nb
            self.cumplir_pedidos()
        self.fin_de_dia()

    def aplicar_guion(self):
        """Deriva guionizada del Acto I (precios que suben por las noticias del guion)."""
        self.mk.guion = {m: 0.0 for m in self.P["min"]}
        if not self.cfg.get("guion", False):
            return
        for d in self.P["a1"]["deriva"]:
            if self.dia < d["desde"]:
                continue
            if d["tipo"] == "escalon":
                self.mk.guion[d["mineral"]] = float(d["pct"])
            else:
                dias = min(self.dia, d["hasta"]) - d["desde"]
                self.mk.guion[d["mineral"]] = float(d["pct_dia"] * dias)

    def fin_de_dia(self):
        P, S, cfg = self.P, self.S, self.cfg
        mk = self.mk
        w = self.w()
        self.cumplir_pedidos()
        self.pedido_especial_aeth()
        self.vender_aeth()
        self.noche_negra(self.reservas_pedidos())
        if cfg.get("proto"):
            conservar = self.conservar_proto()
        else:
            conservar = self.conservar_normal()
        self.vender_spot(conservar)
        self.cobrar_guardar()
        self.turno_empleados()
        # vigilancia y cierres
        if self.cierre_negro > 0:
            self.cierre_negro -= 1
        if self.cierre_tienda > 0:
            self.cierre_tienda -= 1
        self.vig = max(0.0, self.vig - P["vig"]["decae"] - P["vig"]["guardia_extra"] * self.guardias)
        if self.dia - self.ultimo_soborno >= P["vig"]["soborno"]["enfria"] and self.sobornos > 0:
            self.sobornos -= P["vig"]["soborno"]["enfria_n"]
            self.ultimo_soborno = self.dia
        for m in mk.ids:
            pass
        if cfg.get("fin_dia_hook"):
            cfg["fin_dia_hook"](self)
        self.dia += 1

    def cobrar_guardar(self):
        """Costo de guardar el stock (y renta del almacén) y regeneración diaria de las zonas."""
        P, cfg = self.P, self.cfg
        gastos = 0.0
        for m, u in self.stock.items():
            if u > EPS:
                gastos += max(P["mk"]["guardar_min"], u * P["M"][m]["precio"] * P["M"][m]["guardar"] / 100.0)
        self.mover("guardar", -gastos)
        if cfg.get("almacen_activo", True) and self.almacen > 0:
            self.mover("renta", -P["mk"]["almacen"][self.almacen]["rent_per_day"])
        for z in self.rich:
            self.rich[z] = min(P["exp"]["rico_max"], self.rich[z] + P["exp"]["rico_dia"] + (self.motor.extra_riqueza_dia() if self.motor else 0))
            self.uso_zona[z] *= self.S["politica"]["uso_zona_decae"]

    def reservas_pedidos(self):
        cons = {m: 0.0 for m in self.stock}
        for o in self.ordenes:
            cons[o["mineral"]] = max(cons[o["mineral"]], min(self.stock[o["mineral"]], o["qty"]))
        return cons

    def conservar_proto(self):
        S = self.S
        if not self.cfg.get("tienda_activa", True):
            return {}
        cap = self.tienda_unidades()
        tot = sum(v for m, v in self.stock.items() if m != "aetherita")
        if tot > cap:
            f = (tot - cap) / tot
            return {m: self.stock[m] * (1 - f) for m in self.stock}
        return {m: self.stock[m] for m in self.stock}

    def conservar_normal(self):
        """Conserva para la tienda de mañana (hasta su capacidad) y para los pedidos abiertos."""
        P = self.P
        cons = {m: 0.0 for m in self.stock}
        for o in self.ordenes:
            cons[o["mineral"]] = max(cons[o["mineral"]], min(self.stock[o["mineral"]], o["qty"]))
        if self.cfg.get("tienda_activa", True) and self.tienda_abierta_manana():
            cap = min(self.tienda_unidades(), self.capacidad_almacen())
            resto = cap
            for m in sorted(self.stock, key=lambda x: -P["M"][x]["precio"]):
                if m == "aetherita":
                    continue
                libre = self.stock[m] - cons[m]
                k = min(libre, resto)
                if k > 0:
                    cons[m] += k
                    resto -= k
        return cons

    def tienda_abierta_manana(self):
        return self.cierre_tienda <= 1
