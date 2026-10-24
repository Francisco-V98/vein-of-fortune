"""Motor de las minas de cinco entradas (F0-93, parte 1): sorteo, cierres, batería del detector, clima y estaciones.

Solo se activa con el interruptor `cfg["motor_minas"]` (un `MotorMinas`); sin él, `Partida` se comporta como antes.
Las claves de economy.mine_entrances y economy.seasons_weather se leen con un `Lector` propio, fuera de `mundo.compilar`,
por eso la huella de las cifras no cambia hasta que F0-92 las recalibre y las integre. Solo biblioteca estándar.
"""
import random

from . import mundo

MIN_HORA = 60.0  # minutos por hora (conversión de unidades)


def cargar(world=None):
    """Lee las claves de entradas, cierres, batería y clima de world.json (sin tocar la huella)."""
    L = mundo.Lector(world if world is not None else mundo.cargar_world())
    g = L.g
    m, s = "economy.mine_entrances.", "economy.seasons_weather."
    return mundo.D(
        n=g(m + "entrances_per_mine"), reparto=g(m + "split"),
        calidad=g(m + "quality_mult"), calidad_a1=g(m + "quality_mult_act1"),
        menas_visibles=g(m + "visible_ores"),
        bateria=g(m + "detector.battery_by_level"), costo_escaneo=g(m + "detector.cost_per_scan"),
        cambios_dia=g(m + "switch.per_mine_per_day"),
        sev=g(m + "closures.by_severity"), min_abiertas=g(m + "closures.min_open"),
        orden_cierre=g(m + "closures.close_order"), presion=g(m + "closures.pressure_mult_by_closed"),
        sin_cierres_en=g(m + "closures.none_in_act"),
        sin_clima=g(s + "no_weather_days"), estaciones=g(s + "season_effects"), clima=g(s + "weather_effects"))


def sortear_entradas(semilla, dia, mina, P):
    """Calidades de las entradas de una mina en un día: lista con el reparto 2/2/1, mezclada con la semilla del día."""
    r = random.Random("%s|%s|%s" % (semilla, dia, mina))
    cal = [c for c, k in P["reparto"].items() for _ in range(k)]
    r.shuffle(cal)
    return cal


def mult_calidad(cal, acto, P):
    return (P["calidad_a1"] if acto == P["sin_cierres_en"] else P["calidad"])[cal]


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


class MotorMinas:
    """Interruptor v2: factor de rendimiento por mina y día que `Partida.ejecutar` aplica a la riqueza de la zona.

    `severidad` es la del problema social o político del día (0 si no hay): se suma la lluvia fuerte de la zona.
    `minutos_caminar` es el parámetro de J5: minutos por trayecto de una entrada a otra.
    """

    def __init__(self, semilla, P=None, severidad=None, clima=None, minutos_caminar=0.0):
        self.P = P or cargar()
        self.semilla, self.severidad, self.clima = semilla, severidad or (lambda dia, zona: 0), clima
        self.minutos_caminar = minutos_caminar
        self.minas = {}
        self.dia = None

    def nuevo_dia(self, dia, acto, zonas, estacion=None, anio=0):
        P = self.P
        self.dia, self.acto, self.minas = dia, acto, {}
        for z in zonas:
            tipo = self.clima.del_dia(dia, z, estacion, anio) if self.clima else next(iter(P["clima"]))
            ent = sortear_entradas(self.semilla, dia, z, P)
            cerr = cerrar(ent, self.severidad(dia, z) + cierres_por_clima(tipo, P), acto, P)
            self.minas[z] = Mina(ent, cerr, P)

    def factor(self, zona, empleado):
        m = self.minas[zona]
        return m.mult_empleados(self.acto) if empleado else m.mult_jugador(self.acto)

    def horas_caminando(self, cambios):
        return cambios * self.minutos_caminar / MIN_HORA
