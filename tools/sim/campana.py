"""Corridas del simulador: Acto I guionizado, etapas estacionarias y campaña completa con progresión."""
import math
import statistics

from . import mundo
from .jugador import Partida, srnd
from .mercado import Azar, MercadoRef


MIN_HORA = 60.0  # minutos que tiene una hora (conversión de unidades)


# ------------------------------------------------------------------ utilidades
def semilla(S, i, extra=0):
    return S["semillas"]["base"] + S["semillas"]["paso"] * i + extra


def semilla_flujo(S, nombre, i=0):
    """Semilla de un flujo propio (cada experimento usa el suyo para no mezclar sus números al azar)."""
    return semilla(S, i, S["semillas"]["flujos"][nombre])


def perfil_de(P, S, pid):
    d = S["perfiles"][pid]
    return {"id": pid, "probs": list(P["exp"]["probs"][d["probs"]]), "eps": d["eps"], "compras": d["compras"],
            "reserva": d["reserva"], "acto1_exp": d["acto1_exp"], "duracion": d["duracion"]}


def ic95(valores, S):
    n = len(valores)
    if n < 2:
        return [None, None]
    m = sum(valores) / n
    if not all(math.isfinite(v) for v in valores):
        # Un valor infinito (p. ej. rampa con inicio nulo) no tiene desviación: Python 3.11 lanza error con pstdev.
        return [m, m]
    sd = statistics.pstdev(valores) * (n / (n - 1)) ** 0.5
    h = S["estadistica"]["z95"] * sd / n ** 0.5
    return [m - h, m + h]


def ic_prop(k, n, S):
    """Intervalo de Wilson para una proporción."""
    if n == 0:
        return [None, None]
    z = S["estadistica"]["z95"]
    p = k / n
    den = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / den
    h = z * ((p * (1 - p) / n + (z / (2 * n)) ** 2) ** 0.5) / den
    return [max(0.0, centro - h), min(1.0, centro + h)]


def media(xs):
    return sum(xs) / len(xs) if xs else 0.0


def horas_de(P, dias):
    return dias * P["t"]["dia_min"] / MIN_HORA


def dias_de_horas(P, horas):
    return int(round(horas * MIN_HORA / P["t"]["dia_min"]))


def energia_etapa(P, ref):
    acto, idx = ref
    e = P["energia"]["por_acto"][acto]
    return float(e[idx] if isinstance(e, list) else e)


def nivel_etapa(P, ref):
    acto, idx = ref
    return P["herr"]["niveles_acto"][acto][idx]


def cfg_base(P, S, acto, niveles, energia, **kw):
    cfg = {"acto": acto, "niveles": niveles, "energia": (lambda p, e=energia: e), "ruido": S["ruido"], "descarte": P["exp"]["descarte_pct"] / 100.0,
           "mina_todo": False, "proto": False, "buyer_cap": True, "almacen_activo": True, "tienda_activa": True,
           "aeth_modo": "legal", "pedidos": False, "negro": None, "sueltos": True, "tienda": 0}
    cfg.update(kw)
    return cfg


def cfg_etapa(P, S, eid, proto=False, **kw):
    """Configuración de una etapa estacionaria (IIe, II, III, IV) como la del prototipo de F0-52."""
    e = S["prototipo"]["etapas"][eid]
    L = nivel_etapa(P, e["nivel"])
    niveles = {t: L for t in P["herr"]["tipos"]}
    cfg = cfg_base(P, S, e["acto"], niveles, energia_etapa(P, e["energia"]), tienda=e["tienda"], patrimonio_fijo=float(e["patrimonio"]))
    if proto:
        cfg.update({"proto": True, "mina_todo": True, "descarte": 0.0, "buyer_cap": False, "almacen_activo": False,
                    "aeth_modo": "negro3", "ruido": S["ruido_prototipo"], "sueltos": True, "tope_diario": True})
        if eid == "IIe":
            cfg["acto"] = "II"
    cfg.update(kw)
    return cfg


CONT_CLAVES = ("bruto", "rich_sum", "rich_n", "slip", "especiales", "especiales_viales", "emp_exp", "emp_baja", "redadas",
               "noches_negras", "aeth_vendidas", "tienda_bloques", "pedidos_hechos", "pedidos_perdidos", "exp", "menas", "descartes")


def correr_etapa(P, S, cfg, perfil, sem, dias, calentamiento=0, hook=None):
    """Corre `dias` días con la configuración dada; mide después del calentamiento.

    Devuelve dict ligero con el ingreso neto por día, el reparto de expediciones por zona, el flujo medio y contadores."""
    p = Partida(P, S, sem, perfil, cfg)
    f0 = {}
    c0 = {k: 0 for k in CONT_CLAVES}
    z0 = {z: 0 for z in P["zonas"]}
    ex0 = {"pe": 0.0, "ne": 0.0, "va": 0.0}
    sem_fosa = {}
    for d in range(dias):
        if d == calentamiento:
            f0 = dict(p.f)
            c0 = {k: p.cont[k] for k in CONT_CLAVES}
            z0 = dict(p.cont["exp_zona"])
            ex0 = {"pe": p.pedidos_extra, "ne": p.neg_extra, "va": p.vig_aeth}
        dia_antes = p.dia
        fosa_antes = p.cont["exp_zona"].get("fosa", 0)
        p.jugar_dia()
        if d >= calentamiento and p.cont["exp_zona"].get("fosa", 0) > fosa_antes:
            semana = (dia_antes - 1) // P["t"]["semana"]
            sem_fosa[semana] = sem_fosa.get(semana, 0) + p.cont["exp_zona"]["fosa"] - fosa_antes
        if hook:
            hook(p, d)
    n = dias - calentamiento
    dif = {k: p.f.get(k, 0.0) - f0.get(k, 0.0) for k in p.f}
    flujo = {k: v / n for k, v in dif.items()}
    zonas = {z: p.cont["exp_zona"][z] - z0[z] for z in P["zonas"]}
    cont = {k: p.cont[k] - c0[k] for k in CONT_CLAVES}
    return {"neto_dia": p.ingreso_neto(dif) / n, "flujo": flujo, "zonas": zonas, "cont": cont, "dias": n,
            "pedidos_extra": (p.pedidos_extra - ex0["pe"]) / n, "negro_extra": (p.neg_extra - ex0["ne"]) / n,
            "vig_aeth": (p.vig_aeth - ex0["va"]) / n, "max_fosa_semana": max(sem_fosa.values()) if sem_fosa else 0,
            "vig_final": p.vig, "patrimonio": p.patrimonio(), "stock_aeth": p.stock["aetherita"], "partida": p if cfg.get("guardar_partida") else None}


# ------------------------------------------------------------------ Acto I
def acto1(P, S, perfil, sem, n_exp=None, mejora=False, urgente=False, dificultad="intermedio", descarte=None, motor=None):
    """El Acto I guionizado (7 días). Devuelve caja antes de la cuota, margen y si paga a tiempo."""
    a1 = P["a1"]
    n_exp = perfil["acto1_exp"] if n_exp is None else n_exp
    clave = [k for k, v in P["exp"]["probs"].items() if list(v) == list(perfil["probs"])][0]
    cfg = cfg_base(P, S, "I", {t: 0 for t in P["herr"]["tipos"]}, float(P["energia"]["por_acto"]["I"][0]),
                   cash=float(P["deuda"]["caja0"]), tienda=0, sueltos=False, guion=True, buyer_cap=True,
                   markup_tienda=P["mk"]["tienda"]["destreza"][clave], dificultad=dificultad,
                   descarte=(P["exp"]["descarte_pct"] / 100.0 if descarte is None else descarte))
    if motor is not None:  # interruptor v2 (F0-92): las entradas, la batería y la caminata también rigen en el Acto I
        cfg["motor_minas"] = motor
        motor.actos = motor.actos or P["actos"]
    cfg["niveles"]["pico"] = 1
    p = Partida(P, S, sem, dict(perfil, eps=0.0), cfg)
    mk = p.mk
    hecho = 0
    seq = list(zip(a1["dias_exp"], a1["minerales"]))
    extra = [(a1["extra_dia"], a1["extra_min"][i % len(a1["extra_min"])]) for i in range(max(0, n_exp - len(seq)))]
    seq = (seq + extra)[:n_exp]
    por_dia = {}
    for d, m in seq:
        por_dia.setdefault(d, []).append(m)
    mejora_hecha = False
    pedido_ok = False
    urg_ok = False
    gestion = float(P["deuda"]["gestion"])
    for d in range(1, P["deuda"]["dia1"] + 1):
        p.dia = d
        mk.fijar_acto("I")
        mk.nuevo_dia(d)
        p.aplicar_guion()
        if motor is not None:
            motor.nuevo_dia(d, "I", P["zonas"])
        for _ in range(P["t"]["bloques_dia"]):
            mk.paso()
        w = p.w()
        if d == a1["gestion_dia"]:
            p.stock[a1["saco"]["mineral"]] += a1["saco"]["units"]
            p.vender_tienda()
            p.mover("gestion", -gestion)
        if d == a1["pedido_std"]["offered_day"]:
            o = P["pedidos"]["tipos"]["estandar"]
            m = o["mineral"]
            p.ordenes.append({"tipo": "estandar", "mineral": m, "qty": o["unidades"], "vence": a1["pedido_std"]["delivery_day"] + o["plazo"][1],
                              "precio": mk.justo(m) * (1.0 + o["prima"] / 100.0), "valor": 0.0})
        if d in a1["dias_tienda"] and d != a1["gestion_dia"] and d != P["deuda"]["dia1"]:
            p.vender_tienda()
        if d == a1["pedido_std"]["delivery_day"]:
            p.cumplir_pedidos()
            pedido_ok = not p.ordenes
        if d == a1["mejora_dia"] and mejora:
            tipo = a1["mejora_herr"]
            k = a1["mejora_nivel"]
            costo = P["herr"]["costo"][tipo][str(k)]
            req = P["herr"]["minerales"][tipo][str(k)]
            mm, qq = req["mineral"], req["qty"]
            if p.stock[mm] >= qq and p.cash >= costo:
                p.stock[mm] -= qq
                p.mover("compras", -costo)
                p.niveles[tipo] = k
                mejora_hecha = True
            elif p.cash >= costo + qq * mk.cur[mm] * P["herr"]["mercado"]:
                p.mover("compras", -(costo + qq * mk.cur[mm] * P["herr"]["mercado"]))
                p.niveles[tipo] = k
                mejora_hecha = True
        for m in por_dia.get(d, []):
            nivel1 = (hecho == 0)
            pl = p.plan_zona("galerias-hollin", w, p.rich["galerias-hollin"] / 100.0, foco=m)
            p.ejecutar(pl, forzar=(a1["resultado1"] if nivel1 else None))
            hecho += 1
            p.cont["exp"] += 1
        if d == P["deuda"]["dia1"]:
            if urgente:
                o = P["pedidos"]["tipos"]["urgente"]
                m = o["mineral"]
                if p.stock[m] >= o["unidades"]:
                    ing = o["unidades"] * mk.justo(m) * (1.0 + o["prima"] / 100.0) * (1.0 - P["mk"]["impuesto"] / 100.0)
                    p.mover("v_pedidos", ing)
                    p.stock[m] -= o["unidades"]
                    urg_ok = True
            p.vender_tienda()
            p.vender_spot({})
        p.cobrar_guardar()
    caja = p.cash
    Q = float(P["deuda"]["cuota1"])
    neto = caja - P["deuda"]["caja0"] + gestion
    horas = horas_de(P, P["deuda"]["dia1"])
    return {"caja": caja, "cuota": Q, "paga": caja >= Q, "margen": caja - Q, "neto_hora": neto / horas, "mejora": mejora_hecha,
            "exp": hecho, "pedido": pedido_ok, "urgente": urg_ok, "nivel_pico": p.niveles["pico"]}


def lote_acto1(P, S, perfil, n, motor_fn=None, **kw):
    """`motor_fn(semilla)` crea el motor de minas de cada corrida (None = el modelo sin entradas)."""
    out = []
    for i in range(n):
        sem = semilla_flujo(S, "acto1", i)
        out.append(acto1(P, S, perfil, sem, motor=motor_fn(sem) if motor_fn else None, **kw))
    return out


def resumen_acto1(res, S):
    n = len(res)
    k = sum(1 for r in res if r["paga"])
    cajas = sorted(r["caja"] for r in res)
    q_lo, q_med, q_hi = S["estadistica"]["percentiles"]
    Q = res[0]["cuota"]
    m = media([r["margen"] for r in res])
    return {"n": n, "paga": k / n, "paga_ic": ic_prop(k, n, S), "margen": m, "margen_pct": m / Q * 100.0,
            "margen_pct_ic": [x / Q * 100.0 if x is not None else None for x in ic95([r["margen"] for r in res], S)],
            "neto_hora": media([r["neto_hora"] for r in res]), "caja_p10": cajas[int(q_lo * n)], "caja_p50": cajas[int(q_med * n)],
            "caja_p90": cajas[min(n - 1, int(q_hi * n))], "cuota": Q}


def S_colchon(S):
    """Colchón de caja (múltiplo del precio, menos 1) que exige un gasto sin retorno."""
    return S["campana"]["estilo_colchon"] - 1.0


# ------------------------------------------------------------------ deuda
class Deuda:
    """La deuda de la herencia: cuota semanal, abono anónimo, recargos por atraso y mora."""

    def __init__(self, P, dificultad="intermedio"):
        self.P = P
        d = P["deuda"]
        self.K = float(d["K"])
        self.saldo = float(d["K"])
        self.pagado_cap = 0.0
        self.extra_cap = 0.0
        self.atrasadas = []  # cuotas vencidas sin pagar: {"monto", "semanas"}
        self.semanas_atraso = 0
        self.mora = False
        self.dif = P["dif"]["orden"].index(dificultad)
        self.dificultad = dificultad
        self.recargo_total = 0.0
        self.cuotas_pagadas = 0
        self.dia_abono_ciclo = d["abono"]["dia"]
        self.credito_sem_restantes = 0
        self.intereses = 0.0
        self.gestion_fiada = 0.0

    def tasa_semanal(self):
        d = self.P["deuda"]
        t = d["int_sem"] / 100.0
        if self.mora:
            t += d["mora"]["pp"] / 100.0 / (d["int_mes"] / d["int_sem"])
        return t

    def cuota(self, dia):
        d = self.P["deuda"]
        interes = self.saldo * self.tasa_semanal()
        credito = 0.0
        if self.credito_sem_restantes > 0:
            credito = min(float(d["abono"]["credito"]), interes)
        amort = min(self.saldo, float(d["amort"]))
        return amort + interes - credito, amort, interes, credito

    def vence_hoy(self, dia):
        d = self.P["deuda"]
        return dia >= d["dia1"] and (dia - d["dia1"]) % self.P["t"]["semana"] == 0

    def avanzar_dia(self, dia):
        """Actualiza el ciclo del abono anónimo (llega el día 14 y cada 28 días)."""
        d = self.P["deuda"]["abono"]
        if dia >= d["dia"] and (dia - d["dia"]) % d["periodo"] == 0:
            self.credito_sem_restantes = d["semanas"]

    def pagar(self, p, dia):
        """Paga la cuota que vence hoy (si hay caja). Devuelve True si pagó."""
        P = self.P
        if not self.vence_hoy(dia):
            return None
        d = P["deuda"]
        monto, amort, interes, credito = self.cuota(dia)
        extra = sum(a["monto"] for a in self.atrasadas)
        total = monto + extra
        if p.cash >= total:
            p.mover("cuotas", -total)
            self.saldo -= amort
            self.pagado_cap += amort
            self.intereses += interes - credito
            self.cuotas_pagadas += 1
            if self.credito_sem_restantes > 0:
                self.credito_sem_restantes -= 1
            self.atrasadas = []
            self.semanas_atraso = 0
            self.mora = False
            ab = d["abono"]
            if dia >= ab["dia"] and (dia - ab["dia"]) % ab["periodo"] == 0:
                self.credito_sem_restantes = ab["semanas"]
            return True
        # atraso: recargo por semana sobre la cuota atrasada, con tope
        rec = d["recargo"][self.dificultad] / 100.0
        tope = d["recargo_tope"]
        for a in self.atrasadas:
            if a["semanas"] < tope:
                a["monto"] += a["base"] * rec
                self.recargo_total += a["base"] * rec
            a["semanas"] += 1
        self.atrasadas.append({"monto": monto, "base": monto, "semanas": 0})
        self.semanas_atraso += 1
        if self.semanas_atraso >= d["mora"]["semanas"]:
            self.mora = True
        return False

    def extra(self, p, monto):
        monto = min(monto, self.saldo, max(0.0, p.cash))
        if monto <= 0:
            return 0.0
        p.mover("extra_deuda", -monto)
        self.saldo -= monto
        self.pagado_cap += monto
        self.extra_cap += monto
        return monto

    @property
    def fraccion(self):
        return self.pagado_cap / self.K


# ------------------------------------------------------------------ campaña
def duraciones(P, S, pid):
    """Días de cada acto (II, III, IV) según el perfil: lento = máximo de horas, rápido = mínimo, medio = media."""
    modo = S["perfiles"][pid]["duracion"]
    out = {}
    for a in ("II", "III", "IV"):
        lo, hi = P["ritmo"]["actos"][a]["horas"]
        h = {"max": hi, "min": lo, "media": (lo + hi) / 2.0}[modo]
        out[a] = dias_de_horas(P, h)
    return out


class Campana:
    """Una partida completa (Actos II a IV y un tramo posterior) con progresión: compras, deuda y estilo de vida."""

    def __init__(self, P, S, pid, sem, rapido=False, dias_extra=0, via_deuda=True, dificultad="intermedio", mejora_a1=None,
                 descarte=None, sobreescribe=None, variante=None):
        self.P, self.S, self.pid = P, S, pid
        self.perfil = perfil_de(P, S, pid)
        self.sem = sem
        self.dur = duraciones(P, S, pid)
        self.dias_extra = dias_extra
        self.via = via_deuda
        pol = S["perfiles"][pid]
        mejora = pol.get("acto1_mejora", False) if mejora_a1 is None else mejora_a1
        self.a1 = acto1(P, S, self.perfil, sem, mejora=mejora, urgente=mejora, dificultad=dificultad, descarte=descarte)
        self.deuda = Deuda(P, dificultad)
        self.inicio = {}
        t = P["deuda"]["dia1"]
        dia = t + 1
        for a in ("II", "III", "IV"):
            self.inicio[a] = dia
            dia += self.dur[a]
        self.fin = dia - 1
        self.total_dias = self.fin + dias_extra
        niv = {t_: 0 for t_ in P["herr"]["tipos"]}
        niv["pico"] = self.a1["nivel_pico"]
        cfg = cfg_base(P, S, "II", niv, 0.0, cash=0.0, tienda=0, sueltos=True, pedidos=True, negro=None, dificultad=dificultad,
                       descarte=(P["exp"]["descarte_pct"] / 100.0 if descarte is None else descarte),
                       dia0=self.inicio["II"], fin_dia_hook=self._hook, especiales=True)
        if sobreescribe:
            cfg.update(sobreescribe)
        cfg["energia"] = self._energia
        self.cfg = cfg
        cash = self.a1["caja"]
        if self.a1["paga"]:
            cash -= self.a1["cuota"]
            self.deuda.saldo -= P["deuda"]["amort"]
            self.deuda.pagado_cap += P["deuda"]["amort"]
            self.deuda.cuotas_pagadas = 1
            self.cuota7_pagada = True
        else:
            self.cuota7_pagada = False
            self.deuda.atrasadas.append({"monto": self.a1["cuota"] + 0.0, "base": self.a1["cuota"] + 0.0, "semanas": 1})
            self.deuda.recargo_total += self.a1["cuota"] * P["deuda"]["recargo"][dificultad] / 100.0
            self.deuda.atrasadas[0]["monto"] += self.a1["cuota"] * P["deuda"]["recargo"][dificultad] / 100.0
            self.deuda.semanas_atraso = 1
        cfg["cash"] = cash
        self.p = Partida(P, S, sem + 1, self.perfil, cfg)
        self.p.dia = self.inicio["II"]
        self.p.cash = cash
        self.p.f = {}
        self.dias_acto = {}
        self.serie_pat = {}
        self.por_acto = {a: {"neto": 0.0, "dias": 0, "f": {}} for a in ("II", "III", "IV", "post")}
        self.compras_log = []
        self.estatus_dia = {}
        self.nivel_pico = {}
        self.extra_hasta = {"II": 0.0, "III": 0.0}
        self.cap_fin = {}
        self.vida = []
        self._ev_memo = {}
        self.licencia_nivel = None
        self.prensa_hasta = -1
        self.licencia_hasta = -1
        self.mes_cobrado = -1
        self.p_ref_f = {}
        self.dia_ult_compra_herr = None
        self.primera_vez_nivel = {}
        self.consumo_estilo = 0.0
        self.pico_ing_acto = {}
        self.peso_hist = []
        self.pat_serie = []
        self.acto_actual = "II"
        self.cash_inicial = cash
        self.pago14 = None
        self.variante = variante
        self.asegura_acto()

    # ---------------------------------------------------------------- tiempo
    def acto_de(self, dia):
        for a in ("II", "III", "IV"):
            if dia < self.inicio[a] + self.dur[a]:
                return a
        return "IV"

    def asegura_acto(self):
        p = self.p
        a = self.acto_de(p.dia)
        p.acto = a
        self.acto_actual = a

    def _energia(self, p):
        P = self.P
        a = self.acto_de(p.dia)
        orden = P["actos"]
        previo = orden[orden.index(a) - 1]
        e_prev = P["energia"]["por_acto"][previo]
        e_prev = e_prev[1] if isinstance(e_prev, list) else e_prev
        e_fin = P["energia"]["por_acto"][a]
        e_fin = e_fin[1] if isinstance(e_fin, list) else e_fin
        if p.dia >= self.inicio["IV"] + self.dur["IV"]:
            return float(e_fin)
        t = (p.dia - self.inicio[a]) / float(self.dur[a])
        rampa = self.P["energia"]["rampa"]
        t = 1.0 if rampa <= 0 else t / rampa
        return e_prev + (e_fin - e_prev) * min(1.0, max(0.0, t))

    # ---------------------------------------------------------------- bucle
    def correr(self):
        p = self.p
        P = self.P
        self.neto_dia = []
        self.fa = {a: {} for a in ("II", "III", "IV", "post")}
        self.cont_a = {a: {"bruto": 0.0, "pedidos": 0.0, "slip": 0.0, "exp": 0, "rich_sum": 0.0, "rich_n": 0, "negro": 0.0}
                       for a in ("II", "III", "IV", "post")}
        self.pat_fin = {}
        self.dias_caja_neg = 0
        self.caja_min = p.cash
        self.dia_cap = {}
        self.pat_a = {a: [] for a in ("II", "III", "IV")}
        while p.dia <= self.total_dias:
            dia = p.dia
            self.asegura_acto()
            a = p.acto
            clave = a if dia <= self.fin else "post"
            f0 = dict(p.f)
            c0 = {"bruto": p.cont["bruto"], "pedidos": p.pedidos_extra, "slip": p.cont["slip"], "exp": p.cont["exp"],
                  "rich_sum": p.cont["rich_sum"], "rich_n": p.cont["rich_n"], "negro": p.neg_extra}
            p.jugar_dia()
            bucket = self.por_acto[clave]
            bucket["dias"] += 1
            difs = {k: p.f.get(k, 0.0) - f0.get(k, 0.0) for k in p.f}
            neto = p.ingreso_neto(difs)
            bucket["neto"] += neto
            self.neto_dia.append(neto)
            fa = self.fa[clave]
            for k, v in difs.items():
                fa[k] = fa.get(k, 0.0) + v
            ca = self.cont_a[clave]
            ca["bruto"] += p.cont["bruto"] - c0["bruto"]
            ca["pedidos"] += p.pedidos_extra - c0["pedidos"]
            ca["slip"] += p.cont["slip"] - c0["slip"]
            ca["exp"] += p.cont["exp"] - c0["exp"]
            ca["rich_sum"] += p.cont["rich_sum"] - c0["rich_sum"]
            ca["rich_n"] += p.cont["rich_n"] - c0["rich_n"]
            ca["negro"] += p.neg_extra - c0["negro"]
            if p.cash < 0:
                self.dias_caja_neg += 1
            self.caja_min = min(self.caja_min, p.cash)
            if dia % self.S["campana"]["paso_serie"] == 0 or dia == self.inicio["II"]:
                self.pat_serie.append((dia, p.patrimonio()))
            if a in self.pat_a and dia <= self.fin:
                self.pat_a[a].append(p.patrimonio())
            for clave_cap, meta in (("a5", P["deuda"]["via"]["a5_monto"]), ("circulo", P["deuda"]["via"]["circulo_monto"])):
                if clave_cap not in self.dia_cap and self.deuda.pagado_cap >= meta:
                    self.dia_cap[clave_cap] = dia
            fin_acto = {"II": self.inicio["III"] - 1, "III": self.inicio["IV"] - 1, "IV": self.fin}
            if dia == fin_acto.get(a):
                self.nivel_pico[a] = p.nivel_max()
                self.dias_acto[a] = dia
                self.pat_fin[a] = p.patrimonio()
                self.cap_fin[a] = self.deuda.pagado_cap
        return self

    def resumen(self):
        P = self.P
        p = self.p
        out = {"pid": self.pid, "dur": self.dur, "inicio": self.inicio, "fin": self.fin,
               "a1": dict(self.a1), "pat_fin": self.pat_fin,
               "nivel_pico": self.nivel_pico, "estatus_dia": self.estatus_dia, "cap_fin": self.cap_fin,
               "extra": self.extra_hasta, "dia_cap": self.dia_cap, "cuota7_pagada": self.cuota7_pagada,
               "pat_serie": self.pat_serie, "primera_vez": {str(k): v for k, v in self.primera_vez_nivel.items()},
               "compras": self.compras_log, "caja_min": self.caja_min, "dias_caja_neg": self.dias_caja_neg,
               "semana2": sum(self.neto_dia[:P["t"]["semana"]]), "neto_dia": self.neto_dia,
               "pago14": self.pago14, "saldo": self.deuda.saldo, "vida": list(self.vida),
               "cash_final": p.cash, "flujo_total": dict(p.f), "cash_inicial": self.cash_inicial,
               "exp_zona": dict(p.cont["exp_zona"]), "vig_aeth": p.vig_aeth, "especiales": p.cont["especiales"],
               "aeth_legal": p.cont["aeth_vendidas"], "dias_total": self.total_dias}
        porcentaje = {}
        for a, b in self.por_acto.items():
            if b["dias"]:
                porcentaje[a] = {"dias": b["dias"], "neto": b["neto"], "f": self.fa[a], "c": self.cont_a[a],
                                 "neto_hora": b["neto"] / horas_de(P, b["dias"])}
        out["acto"] = porcentaje
        return out

    # ---------------------------------------------------------------- compras (fin de día)
    def _hook(self, p):
        P, S = self.P, self.S
        dia = p.dia  # ya incrementado al final de jugar_dia? (se llama antes del incremento)
        self.asegura_acto()
        self.cobros_periodicos(p, dia)
        self.pagar_deuda(p, dia)
        self.comprar(p, dia)
        pat = p.patrimonio()
        for nombre, piso in P["ritmo"]["estatus"].items():
            if nombre not in self.estatus_dia and pat >= piso:
                self.estatus_dia[nombre] = dia

    def cobros_periodicos(self, p, dia):
        P = self.P
        mes = (dia - 1) // P["t"]["mes"]
        if mes != self.mes_cobrado:
            self.mes_cobrado = mes
            if self.acto_actual != "I":
                nivel = "minero"
                for nombre in ("comerciante", "empresario", "magnate"):
                    if nombre in self.estatus_dia:
                        nivel = nombre
                p.mover("licencias", -P["mk"]["licencias"][nivel])
                prensa = S_prensa = self.S["perfiles"][self.pid].get("prensa", [])
                for papel in prensa:
                    p.mover("prensa", -P["info"]["prensa"]["papeles"][papel]["subscription"])
            # impuesto predial y mantenimiento del auto
            if p.casa > 0:
                p.mover("estilo_fijo", -P["vida"]["casas"][p.casa - 1]["precio"] * P["vida"]["predial"] / 100.0)
            if "auto" in self.vida:
                p.mover("estilo_fijo", -P["vida"]["auto"] * P["vida"]["auto_mant"] / 100.0)

    def pagar_deuda(self, p, dia):
        P, S = self.P, self.S
        D = self.deuda
        if self.variante and dia == P["deuda"]["dia1"] + P["t"]["semana"]:
            v = self.variante
            if v == "cuota_extra":
                p.mover("luz", -float(P["deuda"]["cuota_luz"]))
            elif v == "adelanto":
                frac = P["deuda"]["adelanto"]["a_tiempo"] if self.cuota7_pagada else P["deuda"]["adelanto"]["prorroga"]
                monto = min(frac * P["deuda"]["cuota1"], D.saldo)
                p.mover("extra_deuda", -monto)
                D.saldo -= monto
                D.pagado_cap += monto
        res = D.pagar(p, dia)
        if dia == P["deuda"]["dia1"] + P["t"]["semana"]:
            self.pago14 = bool(res)
        if res is None or not self.via:
            return
        # pagos extra para llegar al umbral de la vía a tiempo
        a = self.acto_actual
        if a == "IV":
            return
        meta = P["deuda"]["via"]["a5_monto"] if a == "II" else P["deuda"]["via"]["circulo_monto"]
        fin_acto = self.inicio[a] + self.dur[a] - 1
        semanas_rest = max(1, (fin_acto - dia) // P["t"]["semana"] + 1)
        falta = meta - D.pagado_cap
        if falta <= 0:
            return
        extra = falta / semanas_rest
        ing_dia = max(1.0, self.por_acto[a]["neto"] / max(1, self.por_acto[a]["dias"]))
        reserva = S["campana"]["reserva_via_dias"] * ing_dia
        if p.cash - extra >= reserva:
            pag = D.extra(p, extra)
            if a in self.extra_hasta:
                self.extra_hasta[a] += pag

    def _valor_niveles(self, p, niveles):
        """Valor diario esperado (3 bloques) con la mejor zona, para comparar mejoras."""
        P = self.P
        clave = (tuple(sorted(niveles.items())), p.acto, round(p.energia() / 2))
        if clave in self._ev_memo:
            return self._ev_memo[clave]
        guardado = p.niveles
        p.niveles = niveles
        w = p.w()
        evs = []
        for z in P["zonas"]:
            if not p.zona_acceso(z):
                continue
            pl = p.plan_zona(z, w, 1.0)
            if pl:
                evs.append(pl["ev"] / P["Z"][z]["bloques"])
        p.niveles = guardado
        evs.sort(reverse=True)
        top = evs[: self.S["campana"]["zonas_rotacion"]]
        v = (sum(top) / len(top) if top else 0.0) * P["t"]["bloques_dia"]
        self._ev_memo[clave] = v
        return v

    def costo_paso(self, p, tipo, k):
        P = self.P
        if k == 1:
            return float(P["herr"]["tipo"][tipo]["primero"]), None, 0
        money = float(P["herr"]["costo"][tipo][str(k)])
        req = P["herr"]["minerales"][tipo][str(k)]
        return money, req["mineral"], req["qty"]

    def reserva_cuota(self, p, dia):
        """Caja que se guarda para la próxima cuota si vence pronto."""
        D = self.deuda
        P = self.P
        sem = P["t"]["semana"]
        falta = (P["deuda"]["dia1"] - dia) % sem
        if falta > self.S["campana"]["dias_reserva_cuota"]:
            return sum(a["monto"] for a in D.atrasadas)
        return D.cuota(dia)[0] + sum(a["monto"] for a in D.atrasadas)

    def puede(self, p, dia, monto, reserva, sin_reserva_cuota=False):
        extra = 0.0 if sin_reserva_cuota else self.reserva_cuota(p, dia)
        return p.cash - monto * (1 + reserva) >= extra

    def comprar(self, p, dia):
        P, S = self.P, self.S
        pol = S["perfiles"][self.pid]
        ceil_ = max(P["herr"]["niveles_acto"][p.acto])
        optimo = pol["compras"] == "optimizador"
        techo = len(P["herr"]["niveles"]) if optimo else ceil_
        reserva = pol["reserva"]
        caja_libre = p.cash
        # ---- herramientas (cada pocos días, con memoria)
        if dia % S["campana"]["revisar_cada"] == 0 or optimo:
            self.mejorar_herramientas(p, dia, techo, reserva, optimo)
        # ---- detector
        self.comprar_detector(p, dia, reserva)
        # ---- tienda y almacén
        objetivo_tienda = S["campana"]["tienda_por_acto"].get(p.acto, 0)
        if optimo:
            objetivo_tienda = min(len(P["tienda"]) - 1, objetivo_tienda + 1)
        if p.tienda < objetivo_tienda:
            c = P["tienda"][p.tienda + 1]["costo"]
            if self.puede(p, dia, c, reserva):
                p.mover("tienda_mejora", -c)
                p.tienda += 1
                self.compras_log.append((dia, "tienda", p.tienda, c))
        cap_necesaria = P["tienda"][p.tienda]["unidades"] * S["campana"]["almacen_colchon"]
        if p.almacen < len(P["mk"]["almacen"]) - 1 and P["mk"]["almacen"][p.almacen]["capacity"] < cap_necesaria:
            c = P["mk"]["almacen"][p.almacen + 1]["cost"]
            if self.puede(p, dia, c, reserva):
                p.mover("almacen", -c)
                p.almacen += 1
                self.compras_log.append((dia, "almacen", p.almacen, c))
        # ---- información
        info = pol.get("info", {})
        if info.get(p.acto) and ("info", p.acto) not in self.primera_vez_nivel:
            costo = P["info"][info[p.acto]]
            if self.puede(p, dia, costo, S_colchon(self.S)):
                p.mover("info", -costo)
                self.primera_vez_nivel[("info", p.acto)] = dia
        # ---- estilo de vida
        self.comprar_estilo(p, dia)

    def comprar_detector(self, p, dia, reserva):
        P = self.P
        nivel = P["herr"]["detector_acto"].get(p.acto)
        if nivel is None:
            return
        actual = getattr(p, "detector", 1)
        if actual >= nivel:
            return
        lv = P["herr"]["detector"][actual]  # siguiente nivel
        m = P["herr"]["detector_mineral"]
        qty = lv["minerals"]
        costo = lv["cost"] + (0 if p.stock[m] >= qty else qty * p.mk.cur[m] * P["herr"]["mercado"])
        if self.puede(p, dia, costo, S_colchon(self.S) if self.perfil["compras"] != "optimizador" else float("inf")):
            if p.stock[m] >= qty:
                p.stock[m] -= qty
                p.mover("detector", -lv["cost"])
            else:
                p.mover("detector", -costo)
            p.detector = actual + 1
            self.compras_log.append((dia, "detector", p.detector, costo))

    def mejorar_herramientas(self, p, dia, techo, reserva, optimo):
        P, S = self.P, self.S
        mejor = None
        base = self._valor_niveles(p, dict(p.niveles))
        for t in P["herr"]["tipos"]:
            l0 = p.niveles[t]
            costo_acum = 0.0
            for k in range(l0 + 1, techo + 1):
                money, mm, qty = self.costo_paso(p, t, k)
                mat = qty * P["M"][mm]["precio"] * P["herr"]["mercado"] if mm else 0.0
                costo_acum += money + mat
                if k > l0 + 1 and not S["campana"]["paquetes"]:
                    break
                nuevos = dict(p.niveles)
                nuevos[t] = k
                # herramienta de apoyo: sube todas las que ya tenían el mismo nivel? no; solo ese tipo
                delta = self._valor_niveles(p, nuevos) - base
                if delta <= 0:
                    continue
                dias_pago = costo_acum / delta
                limite = S["campana"]["pago_max_dias_optimo"] if optimo else S["campana"]["pago_max_dias"]
                if dias_pago > limite:
                    continue
                score = delta / costo_acum
                if mejor is None or score > mejor[0]:
                    mejor = (score, t, l0 + 1)
        if not mejor:
            return
        _, t, k = mejor
        money, mm, qty = self.costo_paso(p, t, k)
        usa_stock = mm is not None and p.stock[mm] >= qty
        mat = 0.0 if (mm is None or usa_stock) else qty * p.mk.cur[mm] * P["herr"]["mercado"]
        if self.puede(p, dia, money + mat, reserva):
            if usa_stock:
                p.stock[mm] -= qty
            p.mover("compras", -(money + mat))
            p.niveles[t] = k
            self.compras_log.append((dia, "herr:%s" % t, k, money + mat + (qty * p.mk.cur[mm] if usa_stock else 0.0)))
            if k not in self.primera_vez_nivel:
                self.primera_vez_nivel[k] = dia
            self._ev_memo.clear()

    def comprar_estilo(self, p, dia):
        P, S = self.P, self.S
        pat = p.patrimonio()
        colchon = S["campana"]["estilo_colchon"]
        lista = []
        ropa = P["vida"]["ropa"]
        lista.append(("ropa-minero", ropa["minero_con_licencia"], 0))
        lista.append(("casa-1", P["vida"]["casas"][0]["precio"], 0))
        lista.append(("ropa-comerciante", ropa["comerciante"], P["ritmo"]["estatus"]["comerciante"]))
        lista.append(("casa-2", P["vida"]["casas"][1]["precio"], P["ritmo"]["estatus"]["comerciante"]))
        lista.append(("ropa-empresario", ropa["empresario"], P["ritmo"]["estatus"]["empresario"]))
        lista.append(("casa-3", P["vida"]["casas"][2]["precio"], P["ritmo"]["estatus"]["empresario"]))
        lista.append(("auto", P["vida"]["auto"], P["ritmo"]["estatus"]["empresario"]))
        lista.append(("ropa-magnate", ropa["magnate"], P["ritmo"]["estatus"]["magnate"]))
        lista.append(("casa-4", P["vida"]["casas"][-1]["precio"], P["ritmo"]["estatus"]["magnate"]))
        for nombre, precio, piso in lista:
            if nombre in self.vida:
                continue
            if pat < piso:
                break
            if self.puede(p, dia, precio, colchon - 1.0):
                p.mover("estilo", -precio)
                self.vida.append(nombre)
                if nombre.startswith("casa-"):
                    p.casa = int(nombre.split("-")[1])
                self.compras_log.append((dia, nombre, 1, precio))
            break
