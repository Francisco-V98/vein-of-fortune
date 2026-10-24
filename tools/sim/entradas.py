"""Motor de las minas de cinco entradas (F0-93, parte 1): sorteo, cierres, batería del detector, clima y estaciones.

Solo se activa con el interruptor `cfg["motor_minas"]` (un `MotorMinas`); sin él, `Partida` se comporta como antes.
Las claves de economy.mine_entrances y economy.seasons_weather las lee `mundo.compilar` (P["minas"]) desde F0-92, así que
entran en la huella de las cifras. Solo biblioteca estándar.
"""
import random

from . import mundo

MIN_HORA = 60.0  # minutos por hora (conversión de unidades)


def cargar(world=None):
    """Claves de entradas, cierres, batería y clima de world.json (ya forman parte de la huella desde F0-92)."""
    return mundo.cargar(world)[0]["minas"]


def sortear_entradas(semilla, dia, mina, P):
    """Calidades de las entradas de una mina en un día: lista con el reparto 2/2/1, mezclada con la semilla del día."""
    r = random.Random("%s|%s|%s" % (semilla, dia, mina))
    cal = [c for c, k in P["reparto"].items() for _ in range(k)]
    r.shuffle(cal)
    return cal


def mult_calidad(cal, acto, P):
    if acto == P["sin_cierres_en"]:  # el abanico estrecho del Acto I protege la cuota
        return P["calidad_a1"][cal] * P["rend_base"]
    return P["calidad"][cal] * P["rend_base"]


def cerrar(entradas, severidad, acto, P):
    """Índices de entradas cerradas: sin cierres en el Acto I, al menos `min_abiertas` abiertas, abundante → media → escasa."""
    if acto == P["sin_cierres_en"]:
        return []
    n = min(severidad, len(entradas) - P["min_abiertas"])
    cerradas = []
    for cal in P["orden_cierre"]:
        for i, c in enumerate(entradas):
            if c == cal and len(cerradas) < n:
                cerradas.append(i)
    return cerradas


def mult_presion(n_cerradas, P):
    pr = P["presion"]
    return pr[min(n_cerradas, len(pr) - 1)]


def carga_maxima(nivel, nieve, P, clima_efecto=None):
    """Batería del detector por nivel (1 a 4); la nieve resta cargas."""
    b = P["bateria"][min(max(nivel, 1), len(P["bateria"])) - 1]
    if nieve:
        b += (clima_efecto or P["clima"]["nieve"])["detector_charge_delta"]
    return max(b, 0)


class Bateria:
    """Batería del detector: una carga por clic y recarga completa por noche."""

    def __init__(self, maxima, costo):
        self.maxima, self.costo, self.cargas = maxima, costo, maxima

    def escanear(self):
        """True si había carga (la gasta); False si hay que picar a ciegas."""
        if self.cargas < self.costo:
            return False
        self.cargas -= self.costo
        return True

    def recargar(self):
        self.cargas = self.maxima


class Mina:
    """Estado de una mina en un día: entradas sorteadas, cerradas, entrada actual y cambio (1 vez al día)."""

    def __init__(self, entradas, cerradas, P):
        self.P, self.entradas, self.cerradas = P, entradas, list(cerradas)
        self.cambios = 0
        self.actual = next(i for i in range(len(entradas)) if i not in self.cerradas)

    def abiertas(self):
        return [i for i in range(len(self.entradas)) if i not in self.cerradas]

    def cambiar(self, a):
        """Cambia de entrada: una vez por mina y día; solo a una abierta distinta de la actual."""
        if a == self.actual or a in self.cerradas or self.cambios >= self.P["cambios_dia"]:
            return False
        self.actual = a
        self.cambios += 1
        return True

    def mult_jugador(self, acto):
        return mult_calidad(self.entradas[self.actual], acto, self.P) * mult_presion(len(self.cerradas), self.P)

    def mult_empleados(self, acto):
        """Los empleados rinden la media de las entradas abiertas (con la misma presión)."""
        ab = self.abiertas()
        media = sum(mult_calidad(self.entradas[i], acto, self.P) for i in ab) / len(ab)
        return media * mult_presion(len(self.cerradas), self.P)


class Clima:
    """Clima por zona y día con la semilla; respeta los días sin clima y los topes de nieve y lluvia fuerte."""

    def __init__(self, semilla, probs, P, tope_lluvia):
        self.semilla, self.probs, self.P, self.tope_lluvia = semilla, probs, P, tope_lluvia
        self.nieve = {}   # (año, zona) -> días de nieve
        self.lluvia = {}  # (año, estación, zona) -> días de lluvia fuerte

    def del_dia(self, dia, zona, estacion, anio=0):
        """Devuelve 'despejado', 'lluvia', 'nieve' o 'niebla'. `probs` es {tipo: probabilidad}; el resto, despejado."""
        lo, hi = self.P["sin_clima"]
        base = next(iter(self.P["clima"]))
        if lo <= dia <= hi or not self.probs:
            return base
        r = random.Random("%s|%s|%s|clima" % (self.semilla, dia, zona)).random()
        acum = 0.0
        for tipo, p in self.probs.items():
            acum += p
            if r < acum:
                break
        else:
            return base
        if tipo == "nieve":
            if estacion != "invierno" or self.nieve.get((anio, zona), 0) >= self.P["clima"]["nieve"]["max_days_per_winter_per_zone"]:
                return base
            self.nieve[(anio, zona)] = self.nieve.get((anio, zona), 0) + 1
        elif tipo == "lluvia":
            k = (anio, estacion, zona)
            if self.lluvia.get(k, 0) >= self.tope_lluvia:
                return base
            self.lluvia[k] = self.lluvia.get(k, 0) + 1
        return tipo


def cierres_por_clima(tipo, P):
    """Entradas que cierra el clima (la lluvia fuerte cierra una)."""
    return P["clima"][tipo].get("heavy_rain_closes_entrances", 0)


def efectos_estacion(estacion, P):
    """Efectos de la estación: dict con las claves que existan (energy_delta, mine_wealth_recovery_per_day, tool_wear_pct, ...)."""
    return dict(P["estaciones"].get(estacion, {}))


def menas_visibles(acto, estacion, tipo_clima, P, azar=None):
    """Menas que el detector muestra: base del acto (un rango se sortea) con otoño y niebla restando."""
    v = P["menas_visibles"][acto]
    if isinstance(v, list):
        v = (azar or random.Random()).randint(v[0], v[-1])
    v += efectos_estacion(estacion, P).get("visible_ores_delta", 0)
    v += P["clima"].get(tipo_clima, {}).get("visible_ores_delta", 0)
    return max(v, 0)


def calendario(dia, cal):
    """(estación, día en la estación, año) del día de juego: el día 1 cae en un día dado de una estación."""
    n = cal["dias_por_estacion"]
    k = dia - 1 + cal["dia_en_estacion_del_dia_1"] - 1
    orden = cal["orden"]
    i0 = orden.index(cal["estacion_del_dia_1"])
    est = orden[(i0 + k // n) % len(orden)]
    return est, k % n + 1, k // (n * len(orden))


def severidad_sembrada(semilla, dia, zona, acto, ev, P, actos):
    """Severidad (0 a 3) del problema social o político del día, sembrada por la semilla; ninguno antes del acto `desde`."""
    if actos.index(acto) < actos.index(ev["eventos_desde_acto"]):
        return 0
    r = random.Random("%s|%s|%s|evento" % (semilla, dia, zona)).random()
    acum = 0.0
    for nombre in sorted(P["sev"], key=lambda k: -P["sev"][k]):  # de la más grave a la más leve
        acum += ev["eventos_por_dia"][nombre]
        if r < acum:
            return P["sev"][nombre]
    return 0


def mult_mellada(integridad_pct, P):
    """Rendimiento de una herramienta mellada (por debajo del umbral de integridad): el margen del minijuego baja."""
    d = P["mellada"]
    return 1.0 + d["minigame_margin_pct"] / 100.0 if integridad_pct < d["integrity_below_pct"] else 1.0


class MotorMinas:
    """Interruptor v2: entradas, cierres, batería, clima y estaciones de las minas que `Partida` aplica al jugar.

    `sup` son los supuestos (minas_v2 de supuestos.json): con ellos hay calendario, eventos sembrados y clima por zona.
    Sin `sup`, `severidad` (callable dia, zona -> 0..3) y `clima` se pasan a mano. `minutos_caminar` es el parámetro de J5.
    """

    def __init__(self, semilla, P=None, sup=None, severidad=None, clima=None, minutos_caminar=0.0, cargas_extra=0,
                 cambiar_entrada=True, actos=None, nieve_siempre=False):
        self.P = P or cargar()
        self.sup, self.semilla, self.actos = sup, semilla, actos
        self.minutos_caminar, self.cargas_extra, self.cambiar_entrada = minutos_caminar, cargas_extra, cambiar_entrada
        self.nieve_siempre = nieve_siempre
        self.severidad = severidad
        if severidad is None:
            if sup:
                self.severidad = lambda dia, zona: severidad_sembrada(semilla, dia, zona, self.acto, sup, self.P, self.actos)
            else:
                self.severidad = lambda dia, zona: 0
        if clima is None and sup:
            clima = Clima(semilla, sup["clima_probs"], self.P, self.P["clima"]["lluvia"]["max_per_season_per_zone"])
        self.clima = clima
        self.minas, self.tipos, self.bateria = {}, {}, None
        self.dia, self.acto, self.estacion = None, None, None
        self.cont = {"expediciones": 0, "cambios": 0, "escaneos": 0, "ciegas": 0, "dias_normal": 0, "dias_nieve": 0,
                     "cortas_normal": 0, "cortas_nieve": 0}
        self._visitadas, self._nieve, self._corta = set(), set(), False

    # --- día
    def _cerrar_dia(self):
        if self.bateria is not None:
            nieve = "nieve" if self._nieve else "normal"
            self.cont["dias_" + nieve] += 1
            self.cont["cortas_" + nieve] += 1 if self._corta else 0

    def nuevo_dia(self, dia, acto, zonas, estacion=None, anio=0):
        P = self.P
        self._cerrar_dia()
        self.dia, self.acto = dia, acto
        if estacion is None and self.sup:
            estacion, _, anio = calendario(dia, self.sup["calendario"])
        self.estacion = estacion
        self.minas, self.tipos, self.bateria = {}, {}, None
        self._visitadas, self._nieve, self._corta = set(), set(), False
        base = next(iter(P["clima"]))
        for z in zonas:
            tipo = "nieve" if self.nieve_siempre else (self.clima.del_dia(dia, z, estacion, anio) if self.clima else base)
            self.tipos[z] = tipo
            ent = sortear_entradas(self.semilla, dia, z, P)
            cerr = cerrar(ent, self.severidad(dia, z) + cierres_por_clima(tipo, P), acto, P)
            self.minas[z] = Mina(ent, cerr, P)

    # --- efectos del día
    def efectos(self):
        lo, hi = self.P["sin_estacion"]  # el Acto I (días 1 a 7) queda libre de efectos de estación
        if self.dia is not None and lo <= self.dia <= hi:
            return {}
        return efectos_estacion(self.estacion, self.P)

    def delta_energia(self):
        return self.efectos().get("energy_delta", 0)

    def extra_riqueza_dia(self):
        e = self.efectos()
        return e.get("mine_wealth_recovery_per_day", 0) - e.get("mine_wealth_recovery_base", 0)

    def mult_desgaste(self):
        return 1.0 + self.efectos().get("tool_wear_pct", 0) / 100.0

    def visibles(self, zona, azar):
        """Menas visibles de una visita: base del acto (un rango se sortea) con la estación y el clima de la zona."""
        v = self.P["menas_visibles"][self.acto]
        if isinstance(v, list):
            v = v[0] + int(azar.u() * (v[-1] - v[0] + 1))
        v += self.efectos().get("visible_ores_delta", 0) + self.P["clima"].get(self.tipos.get(zona), {}).get("visible_ores_delta", 0)
        return max(v, 1)

    def tamano(self, u):
        """Cantidad relativa de una mena (el detector muestra su rango): valores y probabilidades de minas_v2.tamano_mena."""
        if not self.sup:
            return 1.0
        t, acum = self.sup["tamano_mena"], 0.0
        for v, p in zip(t["valores"], t["probs"]):
            acum += p
            if u < acum:
                return v
        return t["valores"][-1]

    def saltar_si_menor(self):
        """Tamaño por debajo del cual el jugador salta una mena escaneada."""
        return self.sup["tamano_mena"]["saltar_si_menor"] if self.sup else 0.0

    def mellada(self, integridad):
        return mult_mellada(integridad, self.P)

    @property
    def reparar_bajo(self):
        """Integridad (%) por debajo de la cual el jugador repara al empezar el día."""
        return self.sup["reparar_bajo_pct"] if self.sup else 0.0

    def ratio_visibles(self, zona):
        """Menas visibles frente a las del acto sin estación ni clima (otoño y niebla restan)."""
        v = self.P["menas_visibles"][self.acto]
        base = sum(v) / len(v) if isinstance(v, list) else v
        delta = self.efectos().get("visible_ores_delta", 0) + self.P["clima"].get(self.tipos.get(zona), {}).get("visible_ores_delta", 0)
        return max(base + delta, 0) / base

    def factor(self, zona, empleado):
        m = self.minas[zona]
        return m.mult_empleados(self.acto) if empleado else m.mult_jugador(self.acto)

    # --- batería y entrada del jugador
    def bateria_dia(self, nivel):
        if self.bateria is None:
            self.bateria = Bateria(carga_maxima(nivel, False, self.P) + self.cargas_extra, self.P["costo_escaneo"])
        return self.bateria

    def entrar(self, zona, nivel):
        """El jugador entra a la mina: nieve resta una carga (una vez al día); en la primera visita escanea
        la entrada y, si es de la calidad a evitar, cambia (una vez al día) a otra abierta elegida a ciegas."""
        b = self.bateria_dia(nivel)
        self.cont["expediciones"] += 1
        if self.tipos.get(zona) == "nieve" and not self._nieve:  # la nieve gasta una carga una vez al día, en la primera zona nevada
            self._nieve.add(zona)
            b.cargas = max(b.cargas + self.P["clima"]["nieve"]["detector_charge_delta"], 0)
        if zona in self._visitadas:
            return
        self._visitadas.add(zona)
        m = self.minas[zona]
        pol = self.sup["politica_entrada"] if self.sup else None
        if not (self.cambiar_entrada and pol and pol["escanea_al_entrar"]):
            return
        if b.escanear():
            self.cont["escaneos"] += 1
            if m.entradas[m.actual] == pol["cambiar_si"]:
                otras = [i for i in m.abiertas() if i != m.actual]
                if otras and m.cambiar(random.Random("%s|%s|%s|cambio" % (self.semilla, self.dia, zona)).choice(otras)):
                    self.cont["cambios"] += 1
        else:
            self._corta = True

    def escanear(self):
        """Un clic del detector sobre una mena: True si había carga; si no, se pica a ciegas."""
        if self.bateria.escanear():
            self.cont["escaneos"] += 1
            return True
        self._corta = True
        self.cont["ciegas"] += 1
        return False

    def horas_caminando(self, cambios):
        return cambios * self.minutos_caminar / MIN_HORA

    def horas_caminadas(self):
        """Horas de caminata por entrar a la mina y por cambiar de entrada."""
        return self.horas_caminando(self.cont["expediciones"] + self.cont["cambios"])
