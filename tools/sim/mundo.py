"""Mundo del simulador: lee TODAS las cifras del juego de studio/data/world.json.

Ninguna cifra del juego vive en el código del simulador. `compilar(lector)` recorre world.json con un
`Lector` que anota cada clave que lee; el resultado es un árbol `P` (parámetros) con acceso por atributo.
La huella es el sha256 de los valores de las claves leídas: si cambia una cifra que el simulador usa,
la huella cambia y los resultados guardados caducan. Solo biblioteca estándar.
"""
import copy
import hashlib
import json
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[2]
WORLD = RAIZ / "studio" / "data" / "world.json"
SUPUESTOS = RAIZ / "studio" / "data" / "sim" / "supuestos.json"


class D(dict):
    """Diccionario con acceso por atributo (solo lectura cómoda)."""

    __getattr__ = dict.__getitem__


class Lector:
    """Lee world.json por rutas con puntos y anota las claves leídas.

    Segmentos: nombre de clave, entero (índice) o `id` de un elemento de lista (minerals.carbon.energy).
    """

    def __init__(self, world):
        self.world = world
        self.leidas = {}

    def _resolver(self, ruta):
        nodo = self.world
        for seg in ruta.split("."):
            if isinstance(nodo, list):
                if seg.lstrip("-").isdigit():
                    nodo = nodo[int(seg)]
                else:
                    nodo = next(e for e in nodo if isinstance(e, dict) and (e.get("id") == seg))
            else:
                nodo = nodo[seg]
        return nodo

    def g(self, ruta, defecto=None, opcional=False):
        try:
            v = self._resolver(ruta)
        except (KeyError, StopIteration, IndexError):
            if not opcional:
                raise KeyError("world.json: falta la clave %s" % ruta)
            self.leidas[ruta] = None
            return defecto
        self.leidas[ruta] = copy.deepcopy(v)
        return copy.deepcopy(v)

    def ids(self, ruta):
        """Ids de una lista de objetos (se anota como una clave)."""
        lista = self._resolver(ruta)
        r = [e["id"] for e in lista]
        self.leidas[ruta + ".*.id"] = r
        return r

    def largo(self, ruta):
        n = len(self._resolver(ruta))
        self.leidas[ruta + ".#"] = n
        return n


def cargar_world(ruta=WORLD):
    return json.loads(pathlib.Path(ruta).read_text(encoding="utf-8"))


def cargar_supuestos(ruta=SUPUESTOS):
    return json.loads(pathlib.Path(ruta).read_text(encoding="utf-8"))


ACTOS = ("I", "II", "III", "IV")


def minas(L):
    """Entradas, cierres, batería del detector, clima y estaciones de las minas (F0-92: ya forman parte de la huella)."""
    g = L.g
    m, s = "economy.mine_entrances.", "economy.seasons_weather."
    return D(
        n=g(m + "entrances_per_mine"), reparto=g(m + "split"),
        rend_base=g(m + "base_yield_mult"), calidad=g(m + "quality_mult"), calidad_a1=g(m + "quality_mult_act1"),
        menas_visibles=g(m + "visible_ores"), picables=g(m + "pickable_ratio"),
        bateria=g(m + "detector.battery_by_level"), costo_escaneo=g(m + "detector.cost_per_scan"),
        cambios_dia=g(m + "switch.per_mine_per_day"),
        sev=g(m + "closures.by_severity"), min_abiertas=g(m + "closures.min_open"),
        orden_cierre=g(m + "closures.close_order"), presion=g(m + "closures.pressure_mult_by_closed"),
        sin_cierres_en=g(m + "closures.none_in_act"),
        mellada=g(m + "tool_dull"),
        sin_clima=g(s + "no_weather_days"), sin_estacion=g(s + "no_season_effect_days"), estaciones=g(s + "season_effects"), clima=g(s + "weather_effects"))


def compilar(L):
    """Lee world.json a través del lector y devuelve el árbol de parámetros P."""
    g = L.g
    P = D()
    P["actos"] = list(g("acts"))
    # --- tiempo
    P["t"] = D(
        dia_min=g("economy.time.day_minutes"), bloque_min=g("economy.time.block_minutes"),
        bloques_dia=g("economy.time.blocks_per_day"), semana=g("economy.time.week_days"),
        mes=g("economy.time.month_days"), estacion=g("economy.time.season_days"),
        anio=g("economy.time.year_days"), estaciones=g("economy.time.seasons"),
        contratos=g("economy.time.contract_days"),
        inicio_dia=g("economy.calendar.start_day"), inicio_estacion=g("economy.calendar.start_season"),
        inicio_dia_estacion=g("economy.calendar.start_day_of_season"),
        dia_cuota=g("economy.calendar.quota_weekday"),
        semana_empieza=g("economy.calendar.week_starts_on_day"),
        fosa_dias=g("economy.calendar.fosa_open_weekdays"))
    # --- minerales
    P["min"] = L.ids("minerals")
    M = D()
    for mid in P["min"]:
        b = "minerals.%s." % mid
        M[mid] = D(
            id=mid, tier=g(b + "tier"), energia=g(b + "energy"), rend=g(b + "yield"), precio=g(b + "base_price"),
            sigma=g(b + "sigma"), tope=g(b + "daily_cap"), liq=g(b + "liquidity"), comprador=g(b + "buyer_cap"),
            guardar=g(b + "storage_pct"), spread=g(b + "spread"), prima_negra=g(b + "black_premium"),
            estacion=g(b + "season"), vol=g(b + "volatility_num"), minijuegos=g(b + "minigames"),
            sectores=g(b + "sectors"))
    P["M"] = M
    # --- zonas
    P["zonas"] = L.ids("zones")
    Z = D()
    for zid in P["zonas"]:
        b = "zones.%s." % zid
        Z[zid] = D(id=zid, acto=g(b + "act"), profunda=g(b + "deep"), bloques=g(b + "blocks"), mezcla=g(b + "zone_mix"),
                   riqueza0=g(b + "initial_wealth"), lugar=g(b + "place"),
                   dias_abierta=g(b + "open_weekdays", None, True))
    P["Z"] = Z
    # --- expediciones
    e = "economy.expedition."
    P["exp"] = D(
        bloques_normal=g(e + "normal_blocks"), bloques_prof=g(e + "deep_blocks"), max_normales=g(e + "max_normal_per_day"),
        mult_res=g(e + "result_multipliers"), probs=g(e + "result_probs"),
        energia_prof=g(e + "deep_energy_mult"), carga_prof=g(e + "deep_load_mult"),
        rico_min=g(e + "zone_wealth.min"), rico_max=g(e + "zone_wealth.max"),
        rico_exp=g(e + "zone_wealth.per_expedition"), rico_dia=g(e + "zone_wealth.per_day"),
        rico_salida=g(e + "zone_wealth.avg_at_exit_pct"),
        tope_menas=g(e + "ores_per_expedition.soft_cap_per_block"),
        descarte_pct=g(e + "ore_discard.energy_pct_of_ore"),
        aeth_nivel=g(e + "aetherita.tool_min_level"), aeth_minijuego=g(e + "aetherita.minigame"), aeth_tipos=g(e + "aetherita.tool_types"),
        aeth_filtro=g(e + "aetherita.filter_cost_per_expedition"),
        aeth_legal=D(desde=g(e + "aetherita.legal_channel.from_act"), tope=g(e + "aetherita.legal_channel.max_vials_per_day"),
                     precio=g(e + "aetherita.legal_channel.price_mult_of_fair"),
                     impuesto=g(e + "aetherita.legal_channel.sale_tax_applies"),
                     slippage=g(e + "aetherita.legal_channel.slippage")))
    P["resultados"] = list(P["exp"]["mult_res"].keys())
    # --- ritmo
    pc = "economy.pace."
    P["ritmo"] = D(
        hora=g(pc + "net_income_per_hour"), actos=D({a: D(horas=g(pc + "acts.%s.hours" % a), dias=g(pc + "acts.%s.days" % a),
                                                          patrimonio=g(pc + "acts.%s.wealth_end" % a)) for a in ACTOS}),
        patrimonio_rapido_I=g(pc + "acts.I.wealth_end_fast"), patrimonio_I=g(pc + "acts.I.wealth_end"),
        sumideros=g(pc + "sinks_per_act"), estatus=g(pc + "status_floors"), objetivo_es_media=g(pc + "target_is_act_mean"))
    # --- energía
    en = "economy.energy."
    P["energia"] = D(base=g(en + "base"), por_acto=g(en + "per_act"), casa=g(en + "house_bonus"),
                     mult_herr=g(en + "tool_energy_mult"), rampa=g(en + "ramp_fraction_of_act"), perdida=g(en + "load_loss_pct"),
                     perdida_dif=g(en + "load_loss_by_difficulty"), perdida_tope=g(en + "load_loss_cap_pct"))
    # --- herramientas
    tl = "economy.tools."
    tipos = L.ids("economy.tools.types")
    nivs = L.largo("economy.tools.levels")
    P["herr"] = D(
        tipos=tipos,
        tipo=D({t: D(minijuego=g(tl + "types.%s.minigame" % t), mult=g(tl + "types.%s.cost_mult" % t),
                     primero=g(tl + "types.%s.first_cost" % t)) for t in tipos}),
        niveles=[D(rend=g(tl + "levels.%d.yield_mult" % i), energia=g(tl + "levels.%d.energy_mult" % i),
                   dur=g(tl + "levels.%d.durability" % i), carga=g(tl + "levels.%d.load" % i),
                   escaner=g(tl + "levels.%d.scan_width_mult" % i)) for i in range(nivs)],
        niveles_acto=g(tl + "act_levels"),
        costo=g(tl + "upgrade_cost"), minerales=g(tl + "upgrade_minerals"), mercado=g(tl + "marketplace_markup"),
        rep_dinero=g(tl + "repair.money_per_point"), rep_pts_pieza=g(tl + "repair.points_per_part"),
        rep_pieza=g(tl + "repair.part_mineral"), desgaste=g(tl + "repair.wear_per_ore"),
        dureza=g(tl + "repair.hardness_per_tier"), rep_pct=g(tl + "repair.repair_pct_of_gross"),
        expl_desde=g(tl + "explosive.from_act"), expl_potencias=g(tl + "explosive.powers"),
        expl_bono=g(tl + "explosive.result_yield_bonus_pct"),
        detector=g(tl + "detector.levels"), detector_mineral=g(tl + "detector.upgrade_mineral"),
        detector_acto=g(tl + "detector.act_level"))
    # --- mercado
    mk = "economy.market."
    P["mk"] = D(
        eventos=g(mk + "event_base_points"), persistencia=g(mk + "noise_persistence_per_block"),
        decae=g(mk + "event_decay_per_day"), impuesto=g(mk + "sale_tax_pct"), impuesto_negro=g(mk + "black_market_tax_pct"),
        bolsa=D(acto=g(mk + "bolsa.act"), spread=g(mk + "bolsa.spread_mult"), impuesto=g(mk + "bolsa.sale_tax_pct")),
        prof=g(mk + "slippage.depth_by_act"), compradores=g(mk + "slippage.buyers_npc_by_act"),
        w_min=g(mk + "player_impact.w_min"), w_span=g(mk + "player_impact.w_span"),
        w_mitad=g(mk + "player_impact.w_half_wealth"), w_max=g(mk + "player_impact.w_max"),
        w_acto=g(mk + "player_impact.by_act"), recup=g(mk + "player_impact.recovery_per_block"),
        mercado_recargo=g(mk + "marketplace_markup"),
        tienda=D(lista=g(mk + "store.list_markup"), media=g(mk + "store.avg_client_markup"),
                 destreza=g(mk + "store.client_markup_by_skill"), propia=g(mk + "store.own_goods_only"),
                 slippage=g(mk + "store.slippage")),
        licencias=g(mk + "licenses"), guardar_min=g(mk + "storage_min_fee_per_lot_day"),
        almacen=g(mk + "warehouse"), sueltos=D(prob=g(mk + "loose_events.prob_pct_per_mineral_day"),
                                              pesos=g(mk + "loose_events.magnitude_weights")),
        exceso=g(mk + "buyer_cap_excess_slippage_mult"))
    # --- deuda
    d = "economy.debt."
    P["deuda"] = D(
        K=g(d + "principal"), caja0=g(d + "start_cash"), int_mes=g(d + "interest_monthly_pct"),
        int_sem=g(d + "interest_weekly_pct"), amort=g(d + "amortization_weekly"), dia1=g(d + "first_due_day"),
        cuota1=g(d + "first_payment"), cuota14=g(d + "payment_day_14"),
        abono=D(monto=g(d + "anonymous_payment.amount_per_month"), dia=g(d + "anonymous_payment.first_day"),
                periodo=g(d + "anonymous_payment.period_days"), credito=g(d + "anonymous_payment.credit_per_week"),
                semanas=g(d + "anonymous_payment.weeks")),
        pronto=D(desde=g(d + "early_payment.from_day"), pp=g(d + "early_payment.interest_pp")),
        gestion=g(d + "quiroga_management.fee"),
        recargo=g(d + "surcharge_pct_per_week"), recargo_tope=g(d + "surcharge_cap_weeks"),
        atraso=g(d + "late_installment"),
        mora=D(semanas=g(d + "mora.weeks_late"), pp=g(d + "mora.interest_pp"), cierra=g(d + "mora.closes_doors")),
        adelanto=D(a_tiempo=g(d + "advance_installment.on_time_fraction"),
                   prorroga=g(d + "advance_installment.after_extension_fraction")),
        cuota_luz=g(d + "extra_light_fee"), luz=D(monto=g(d + "light_debt.amount"), mes=g(d + "light_debt.growth_monthly_pct")),
        via=D(a5=g(d + "route.A5_pct"), a5_monto=g(d + "route.A5_amount"), circulo=g(d + "route.circle_pct"),
              circulo_monto=g(d + "route.circle_amount"), consorcio=g(d + "route.consortium_cap_pct"),
              consorcio_monto=g(d + "route.consortium_cap_amount")))
    # --- empleados
    em = "economy.employees."
    nl = L.largo("economy.employees.levels")
    P["emp"] = D(
        niveles=[D(nivel=g(em + "levels.%d.level" % i), efic=g(em + "levels.%d.efficiency_pct" % i),
                   tier=g(em + "levels.%d.max_tier" % i), sueldo=g(em + "levels.%d.salary_per_day" % i)) for i in range(nl)],
        nunca=g(em + "never_extract"), apoyo=g(em + "support_salary_per_day"),
        guardia_pct=g(em + "support_salary_per_day.guardia_pct_of_dependiente"),
        analista_pct=g(em + "support_salary_per_day.analista_pct_of_dependiente"),
        contrato=g(em + "contract_salary_mult"), despido=g(em + "dismissal_phi"),
        entreno_dias=g(em + "training.salary_days_multiplier"), entreno_baja=g(em + "training.sick_days"),
        sube_cada=g(em + "training.auto_level_every_days_worked"),
        canales=g(em + "hire_channels"), max_tienda=g(em + "max_staff_by_store_level"),
        max_mineros=g(em + "max_miners_by_store_level"), desgaste_zona=g(em + "zone_wear_per_expedition.formula"),
        riesgo=g(em + "risk.by_zone"), cuidado_max=g(em + "risk.care_reduction_max"),
        guardia_mitad=g(em + "risk.guard_halves"), robo=g(em + "risk.loyalty_theft_pct_per_week"),
        robo_valor=g(em + "risk.theft_pct_of_day_value"),
        asignacion=D(exp_dia=g(em + "miner_assignment.expeditions_per_day"),
                     sueldo_sigue=g(em + "miner_assignment.salary_follows_level")),
        candidatos=D(lealtad=g(em + "candidates.loyalty_pct"), nivel=g(em + "candidates.level_pct_by_act")),
        apoyo_efecto=D(dependiente_libera=g(em + "support_roles.dependiente_frees_shop_block"),
                       refinador=g(em + "support_roles.refinador_added_value"),
                       analista_costo=g(em + "support_roles.analista_only_cost")),
        papel_IV=g(em + "act_IV_role"))
    # --- tienda y mejoras
    P["tienda"] = [D(nivel=g("economy.store_upgrades.%d.level" % i), costo=g("economy.store_upgrades.%d.cost" % i),
                     plantilla=g("economy.store_upgrades.%d.staff" % i), mineros=g("economy.store_upgrades.%d.miners" % i),
                     unidades=g("economy.store_upgrades.%d.units_per_block" % i))
                   for i in range(L.largo("economy.store_upgrades"))]
    # --- información
    inf = "economy.information."
    P["info"] = D(prensa=D(papeles=g(inf + "layers.1.papers"), desde=g(inf + "layers.1.from_act"),
                           dias=g(inf + "layers.1.subscription_days"), rumor=g(inf + "layers.1.rumor")),
                  analisis=g(inf + "layers.2.cost"), tabulador=g(inf + "layers.3.cost"),
                  margen=g(inf + "layers.3.margin_points"))
    # --- viaje
    nr = L.largo("economy.travel.routes")
    P["viaje"] = D(rutas=[(g("economy.travel.routes.%d.a" % i), g("economy.travel.routes.%d.b" % i),
                           g("economy.travel.routes.%d.cost" % i)) for i in range(nr)],
                   misma_boca=g("economy.travel.same_mouth_cost"), lugares=g("economy.travel.places"))
    # --- pedidos
    ids = L.ids("economy.orders")
    ped = D()
    for oid in ids:
        o = "economy.orders.%s." % oid
        ped[oid] = D(id=oid, desde=g(o + "from_act"), prima=g(o + "premium_pct"), plazo=g(o + "deadline_days"),
                     penal=g(o + "penalty_pct"), cadencia=g(o + "cadence_days", None, True),
                     cantidad=g(o + "qty_days_of_production", None, True),
                     unidades=g(o + "first_units", None, True), mineral=g(o + "first_mineral", None, True),
                     vigilancia=g(o + "vigilance", None, True), deriva=g(o + "price_drift_pct", None, True),
                     impuesto=g(o + "tax_pct", None, True))
    P["pedidos"] = D(tipos=ped, orden=ids, propia=g("economy.orders_rules.own_goods_only"),
                     desde=g("economy.orders_rules.cadence_from_act"),
                     tope_pct=g("economy.orders_rules.income_share_cap_pct"))
    # --- vigilancia
    sv = "economy.surveillance."
    nvl = L.largo("economy.surveillance.levels")
    P["vig"] = D(
        niveles=[D(id=g(sv + "levels.%d.id" % i), min=g(sv + "levels.%d.min" % i), max=g(sv + "levels.%d.max" % i)) for i in range(nvl)],
        op_base=g(sv + "per_operation.base"), op_span=g(sv + "per_operation.span"),
        op_min=g(sv + "per_operation.min"), op_max=g(sv + "per_operation.max"),
        decae=g(sv + "natural_decay_per_day"), faroleros=g(sv + "faroleros_rate_mult"),
        tope_noche=g(sv + "night_volume_cap"),
        especial=D(desde=g(sv + "aetherita_special_orders.from_act"), cada=g(sv + "aetherita_special_orders.every_days"),
                   viales=g(sv + "aetherita_special_orders.vials"), prima=g(sv + "aetherita_special_orders.premium_pct"),
                   vigilancia=g(sv + "aetherita_special_orders.vigilance"), rutina=g(sv + "aetherita_special_orders.routine"),
                   cada_casilda=g(sv + "aetherita_special_orders.casilda_variant.every_days"),
                   bono_casilda=g(sv + "aetherita_special_orders.casilda_variant.premium_bonus_points")),
        soborno=D(base=g(sv + "bribe_quiroga.base"), pct=g(sv + "bribe_quiroga.pct_of_wealth"),
                  crece=g(sv + "bribe_quiroga.growth"), baja=g(sv + "bribe_quiroga.vigilance"),
                  enfria=g(sv + "bribe_quiroga.counter_drops_every_days"), enfria_n=g(sv + "bribe_quiroga.counter_drop")),
        guardia_extra=g(sv + "guard_extra_decay_per_day"), guardia_max=g(sv + "guard_max"),
        multas=g(sv + "fines"), redada=D(en=g(sv + "raid.at"), pct=g(sv + "raid.fine_pct_wealth"), minimo=g(sv + "raid.fine_min"),
                                         tienda=g(sv + "raid.store_closed_days"), negro=g(sv + "raid.black_market_closed_days"),
                                         despues=g(sv + "raid.vigilance_after")),
        neto_semanal=g(sv + "black_market_net_weekly_pct"))
    # --- estilo de vida
    lf = "economy.lifestyle."
    nh = L.largo("economy.lifestyle.houses")
    P["vida"] = D(casas=[D(precio=g(lf + "houses.%d.price" % i), energia=g(lf + "houses.%d.energy_bonus" % i)) for i in range(nh)],
                  predial=g(lf + "property_tax_pct_month"), ropa=g(lf + "clothes"),
                  auto=g(lf + "car.price"), auto_mant=g(lf + "car.upkeep_pct_month"))
    # --- dificultad
    P["dif"] = D(orden=g("economy.difficulty.order"), castigo=g("economy.difficulty.punishment_f"),
                 ayuda=g("economy.difficulty.help_g"), sigma=g("economy.difficulty.sigma_mult"))
    # --- guion del Acto I
    s = "economy.act1_script."
    P["a1"] = D(
        dias_exp=g(s + "expedition_days"), minerales=g(s + "expedition_minerals"),
        extra_dia=g(s + "extra_expedition_day"), extra_min=g(s + "extra_expedition_minerals"),
        resultado1=g(s + "first_expedition_result"), saco=g(s + "anselmo_sack"),
        gestion_dia=g(s + "management_day"), mejora_dia=g(s + "upgrade_day"), mejora_herr=g(s + "upgrade_tool"),
        mejora_nivel=g(s + "upgrade_level"), pedido_std=g(s + "standard_order"), pedido_urg=g(s + "urgent_order"),
        dias_tienda=g(s + "store_days"),
        deriva=[D(mineral=g("economy.scripted_drift_act1.%d.mineral" % i), desde=g("economy.scripted_drift_act1.%d.from_day" % i),
                  hasta=g("economy.scripted_drift_act1.%d.to_day" % i, None, True),
                  pct=g("economy.scripted_drift_act1.%d.pct" % i, None, True),
                  pct_dia=g("economy.scripted_drift_act1.%d.pct_per_day" % i, None, True),
                  tipo=g("economy.scripted_drift_act1.%d.kind" % i)) for i in range(L.largo("economy.scripted_drift_act1"))])
    P["minas"] = minas(L)
    return P


def cargar(world=None):
    """Devuelve (P, lector). `world` es un dict ya cargado (o None para leer studio/data/world.json)."""
    L = Lector(world if world is not None else cargar_world())
    return compilar(L), L


def claves(world):
    """Claves de world.json que lee el simulador, con su valor."""
    L = Lector(world)
    compilar(L)
    return L.leidas


def huella(world):
    """sha256 de los valores de las claves de world.json que usa el simulador (16 primeros caracteres)."""
    L = Lector(world)
    compilar(L)
    texto = json.dumps(sorted(L.leidas.items()), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]


def huella_texto(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:16]
