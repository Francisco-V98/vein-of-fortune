"""Mercado de referencia del simulador (sustituible por el real de F2-04/F2-08).

Interfaz que debe cumplir cualquier mercado que lo reemplace (la usan jugador.py, campana.py y reglas.py):
    fijar_acto(acto)                      -> actualiza profundidad y compradores NPC
    nuevo_dia(dia)                        -> abre el día (eventos, tope diario, contadores)
    paso()                                -> actualiza los precios (3 veces al día)
    precio(m)                             -> precio de pantalla (valor justo con ruido), sin spread
    justo(m)                              -> valor justo (base, estación y eventos), sin ruido
    peso_jugador(patrimonio)              -> w(P)
    precio_venta(m, q, w, canal)          -> precio medio por unidad al vender q (sin registrar)
    vender(m, q, w, canal)                -> ingreso neto y registra el impacto
    precio_compra(m, q, w, canal)         -> precio medio por unidad al comprar q (sin registrar)
    comprar(m, q, w, canal)               -> costo y registra el impacto
Canales de venta: spot, bolsa, tienda, negro. Canales de compra: spot, bolsa, marketplace.
"""
import math
import random

TINY = 1e-12  # evita log(0)


class Azar:
    """Generador con normal propia (Box-Muller) y t de Student, para que el resultado no dependa de la plataforma."""

    def __init__(self, semilla):
        self.r = random.Random(semilla)
        self._guardada = None

    def u(self):
        return self.r.random()

    def normal(self):
        if self._guardada is not None:
            z, self._guardada = self._guardada, None
            return z
        u1 = max(self.r.random(), TINY)
        u2 = self.r.random()
        rad = math.sqrt(-2.0 * math.log(u1))
        ang = 2.0 * math.pi * u2
        self._guardada = rad * math.sin(ang)
        return rad * math.cos(ang)

    def t_unitaria(self, gl):
        """t de Student con gl grados de libertad (gl par), reescalada a varianza 1."""
        chi = 0.0
        for _ in range(int(gl) // 2):
            chi += -2.0 * math.log(max(self.r.random(), TINY))
        t = self.normal() / math.sqrt(chi / gl)
        return t / math.sqrt(gl / (gl - 2.0))


class MercadoRef:
    def __init__(self, P, azar, ruido, acto="II", sueltos=True, tope_diario=True, comprador_cap=True):
        """ruido: dict {modelo: gauss|t, gl, escala, agrup_pers, agrup_int}"""
        self.P = P
        self.az = azar
        self.ruido = ruido
        self.ids = list(P["min"])
        self.acto = acto
        self.sueltos = sueltos
        self.tope_diario = tope_diario
        self.comprador_cap = comprador_cap
        M = P["M"]
        self.M = M
        self.x = {m: 0.0 for m in self.ids}
        self.presion = {m: 0.0 for m in self.ids}
        self.eventos = {m: 0.0 for m in self.ids}
        self.apertura = {m: float(M[m]["precio"]) for m in self.ids}
        self.cur = {m: float(M[m]["precio"]) for m in self.ids}
        self.vendido = {m: 0.0 for m in self.ids}
        self.rg = 0.0
        self.dia = 0
        self.guion = {m: 0.0 for m in self.ids}
        self.estacion_cache = {}
        self.tope_alcanzado = {m: 0 for m in self.ids}
        self.sigma_mult = 1.0
        self.caida_max = float("inf")
        self.markup_tienda = P["mk"]["tienda"]["media"]
        t = P["t"]
        self._inicio = t["estaciones"].index(t["inicio_estacion"]) * t["estacion"] + t["inicio_dia_estacion"] - 1
        self._anio = t["anio"]
        self._est = t["estacion"]
        self.pesos_evento = P["mk"]["sueltos"]["pesos"]
        self._ev_claves = list(self.pesos_evento.keys())
        self._ev_pesos = [self.pesos_evento[k] for k in self._ev_claves]
        self._ev_total = float(sum(self._ev_pesos))

    # ---------- calendario y estación
    def estacion(self, m, dia):
        """Puntos de mercado de la estación, interpolados entre las mitades de cada estación."""
        d = (dia - 1 + self._inicio) % self._anio
        s, pos = divmod(d, self._est)
        tab = self.M[m]["estacion"]
        orden = self.P["t"]["estaciones"]
        cur = tab[orden[s]]
        t = (pos + 0.5) / self._est
        if t < 0.5:
            otro = tab[orden[(s - 1) % len(orden)]]
            k = 0.5 - t
        else:
            otro = tab[orden[(s + 1) % len(orden)]]
            k = t - 0.5
        return cur + (otro - cur) * k

    # ---------- interfaz
    def fijar_acto(self, acto):
        self.acto = acto

    def nuevo_dia(self, dia):
        self.dia = dia
        P = self.P
        for m in self.ids:
            self.apertura[m] = self.cur[m]
            self.vendido[m] = 0.0
            self.eventos[m] *= 1.0 - P["mk"]["decae"]
            if self.sueltos and self.az.u() * 100.0 < P["mk"]["sueltos"]["prob"]:
                k = self.az.u() * self._ev_total
                acum = 0.0
                pts = P["mk"]["eventos"][self._ev_claves[-1]]
                for nombre, peso in zip(self._ev_claves, self._ev_pesos):
                    acum += peso
                    if k <= acum:
                        pts = P["mk"]["eventos"][nombre]
                        break
                self.eventos[m] += pts if self.az.u() < 0.5 else -pts
        # régimen de volatilidad del día (agrupación de eventos)
        r = self.ruido
        if r.get("agrup_int", 0) > 0:
            self.rg = r["agrup_pers"] * self.rg + r["agrup_int"] * self.az.normal()
        else:
            self.rg = 0.0

    def paso(self):
        P = self.P
        phi = P["mk"]["persistencia"]
        r = self.ruido
        regimen = math.exp(self.rg) if r.get("agrup_int", 0) > 0 else 1.0
        escala = r.get("escala", 1.0) * regimen * self.sigma_mult
        for m in self.ids:
            d = self.M[m]
            if r["modelo"] == "t":
                z = self.az.t_unitaria(r["gl"])
            else:
                z = self.az.normal()
            self.x[m] = phi * self.x[m] + d["sigma"] * escala * z
            p = self.justo(m) * (1.0 + self.x[m] / 100.0)
            if self.tope_diario:
                lo = self.apertura[m] * (1.0 - d["tope"] / 100.0)
                hi = self.apertura[m] * (1.0 + d["tope"] / 100.0)
                if p <= lo:
                    p = lo
                    self.tope_alcanzado[m] += 1
                elif p >= hi:
                    p = hi
                    self.tope_alcanzado[m] += 1
            self.cur[m] = p
            self.presion[m] *= 1.0 - P["mk"]["recup"]

    def justo(self, m):
        d = self.M[m]
        return d["precio"] * (1.0 + (self.estacion(m, self.dia) + self.eventos[m] + self.guion[m]) / 100.0)

    def precio(self, m):
        return self.cur[m]

    def peso_jugador(self, patrimonio):
        k = self.P["mk"]
        w = k["w_min"] + k["w_span"] * patrimonio / (patrimonio + k["w_mitad"])
        return min(w, k["w_max"])

    def _prof(self):
        return self.P["mk"]["prof"][self.acto]

    def _cap_restante(self, m):
        if not self.comprador_cap:
            return float("inf")
        cap = self.M[m]["comprador"] * self.P["mk"]["compradores"][self.acto]
        return max(0.0, cap - self.vendido[m])

    def _slip(self, m, q, w):
        """Caída media (en %) al vender q unidades y caída final."""
        k = w * q / (self.M[m]["liq"] * self._prof())
        return self.presion[m] + 0.5 * k, k

    def _spread(self, m, canal):
        s = self.M[m]["spread"] / 200.0
        if canal == "bolsa":
            s *= self.P["mk"]["bolsa"]["spread"]
        return s

    def _impuesto(self, canal):
        k = self.P["mk"]
        if canal == "negro":
            return k["impuesto_negro"] / 100.0
        if canal == "bolsa":
            return k["bolsa"]["impuesto"] / 100.0
        return k["impuesto"] / 100.0

    def precio_venta(self, m, q, w, canal="spot"):
        k = self.P["mk"]
        cur = self.cur[m]
        if canal == "tienda":
            return cur * self.markup_tienda * (1.0 - self._impuesto("tienda"))
        if canal == "negro":
            return cur * (1.0 + self.M[m]["prima_negra"] / 100.0) * (1.0 - self._impuesto("negro"))
        if q <= 0:
            return cur
        libre = self._cap_restante(m)
        q_in = min(q, libre)
        q_ex = q - q_in
        base = cur * (1.0 - self._spread(m, canal)) * (1.0 - self._impuesto(canal))
        s_in, k_in = self._slip(m, q_in, w)
        total = q_in * base * (1.0 - min(s_in, self.caida_max) / 100.0)
        if q_ex > 0:
            mult = k["exceso"]
            presion = self.presion[m] + k_in
            k_ex = w * q_ex / (self.M[m]["liq"] * self._prof())
            s_ex = presion + 0.5 * k_ex * mult
            total += q_ex * base * (1.0 - min(s_ex, self.caida_max) / 100.0)
        return total / q

    def vender(self, m, q, w, canal="spot"):
        if q <= 0:
            return 0.0
        p = self.precio_venta(m, q, w, canal)
        if canal in ("spot", "bolsa"):
            self.presion[m] += w * q / (self.M[m]["liq"] * self._prof())
            self.vendido[m] += q
        return p * q

    def precio_compra(self, m, q, w, canal="spot"):
        k = self.P["mk"]
        cur = self.cur[m]
        if canal == "marketplace":
            return cur * k["mercado_recargo"]
        kk = w * q / (self.M[m]["liq"] * self._prof())
        s = self.presion[m] - 0.5 * kk
        return cur * (1.0 + self._spread(m, canal)) * (1.0 - min(max(s, -self.caida_max), self.caida_max) / 100.0)

    def comprar(self, m, q, w, canal="spot"):
        if q <= 0:
            return 0.0
        p = self.precio_compra(m, q, w, canal)
        if canal in ("spot", "bolsa"):
            self.presion[m] -= w * q / (self.M[m]["liq"] * self._prof())
        return p * q
