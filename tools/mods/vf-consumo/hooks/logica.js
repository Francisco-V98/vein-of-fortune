// Lógica pura del mod de consumo: sin acceso al motor, para poder probarla.
// Un «uso» es [entrada, salida, caché leída, caché escrita], en tokens.

export const MAX_REGISTROS = 3000
export const MAX_MUESTRAS = 600
export const CINCO_HORAS = 5 * 3600 * 1000
export const UN_DIA = 24 * 3600 * 1000
export const SIETE_DIAS = 7 * UN_DIA
export const MAX_AGENTES = 500 // agentes recordados (agentId → rol, modelo, esfuerzo)
export const MAX_AGENTES_REG = 40 // agentes distintos con detalle por prompt; el resto va a «_otros»
export const OTROS = '_otros'
export const SIN_ROL = 'sin rol'
export const PRINCIPAL = 'hilo principal'

export const usoVacio = () => [0, 0, 0, 0]

// Convierte el uso que informa el motor (ModelUsage) en la lista de cuatro cifras
export function usoDe(u) {
  if (!u) return usoVacio()
  return [
    Number(u.input_tokens) || 0,
    Number(u.output_tokens) || 0,
    Number(u.cache_read_input_tokens) || 0,
    Number(u.cache_creation_input_tokens) || 0,
  ]
}

export function sumarUso(a, b) {
  return [a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]]
}

export function restarUso(a, b) {
  return [a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3]]
}

// Tokens nuevos: lo que no vino de la caché (entrada, salida y caché escrita)
export const frescos = (u) => u[0] + u[1] + u[3]
export const totalUso = (u) => u[0] + u[1] + u[2] + u[3]

export function nuevoRegistro({ id, t, texto, proyecto, origen, limites }) {
  const l = limites || {}
  return {
    id,
    t,
    txt: String(texto || '').replace(/\s+/g, ' ').trim().slice(0, 200) || '(continuación sin texto)',
    cwd: proyecto || '',
    org: origen || 'composer',
    mod: {},
    sub: usoVacio(),
    sub_ag: {},
    subN: 0,
    n: 0,
    ms: 0,
    nu: 0,
    p5: [l.cinco ? l.cinco.pct : null, null],
    p7: [l.semana ? l.semana.pct : null, null],
    w5: l.cinco ? l.cinco.resetsAt : null,
    w7: l.semana ? l.semana.resetsAt : null,
  }
}

// Suma el uso de un turno al registro: del hilo principal o de un subagente
export function acumularTurno(reg, usage, esSub, durMs, agentId) {
  const u = usoDe(usage)
  if (esSub) {
    reg.sub = sumarUso(reg.sub, u)
    reg.subN += 1
    if (agentId) {
      const ag = reg.sub_ag || (reg.sub_ag = {}) // registros viejos no lo tienen
      let clave = String(agentId)
      // Acotado: pasado el tope, los agentes nuevos se agrupan en «_otros» (no se pierde ningún token)
      if (!(clave in ag) && Object.keys(ag).filter((k) => k !== OTROS).length >= MAX_AGENTES_REG) clave = OTROS
      ag[clave] = sumarUso(ag[clave] || usoVacio(), u)
    }
  } else {
    reg.n += 1
    reg.ms += Number(durMs) || 0
  }
  // Un turno sin respuesta (interrumpido o con error) no trae modelo ni tokens
  if (usage) {
    const modelo = usage.model || 'desconocido'
    reg.mod[modelo] = sumarUso(reg.mod[modelo] || usoVacio(), u)
  }
  reg.nu = frescos(usoRegistro(reg))
  return reg
}

// Uso total del registro (todos los modelos: principal más subagentes)
export function usoRegistro(reg) {
  return Object.values(reg.mod || {}).reduce((acc, u) => sumarUso(acc, u), usoVacio())
}

// Cierra el registro con las ventanas de ahora. Si una ventana se reinició mientras corría
// el prompt, sus puntos no se pueden calcular y quedan sin dato.
export function cerrarRegistro(reg, limites) {
  const l = limites || {}
  const mismaVentana = (inicio, fin) => inicio === null || inicio === undefined || !fin || inicio === fin.resetsAt
  reg.p5[1] = l.cinco && mismaVentana(reg.w5, l.cinco) ? l.cinco.pct : null
  reg.p7[1] = l.semana && mismaVentana(reg.w7, l.semana) ? l.semana.pct : null
  reg.nu = frescos(usoRegistro(reg))
  return reg
}

// Puntos de la ventana que gastó el registro (puede ser 0 por la resolución de un punto)
export function puntos(par) {
  if (!par || par[0] === null || par[1] === null) return null
  const d = Math.round((par[1] - par[0]) * 10) / 10
  return d < 0 ? 0 : d
}

// De la lista de ventanas del motor, saca la de cinco horas y la semanal
export function leerLimites(lista) {
  const salida = { cinco: null, semana: null }
  for (const v of lista || []) {
    const dato = { pct: Number(v.percentUsed) || 0, resetsAt: v.resetsAt ? Date.parse(v.resetsAt) : null }
    if (v.kind === 'five_hour') salida.cinco = dato
    else if (v.kind === 'seven_day') salida.semana = dato
  }
  return salida
}

export function claveDia(ms) {
  const d = new Date(ms)
  const dos = (n) => String(n).padStart(2, '0')
  return d.getFullYear() + '-' + dos(d.getMonth() + 1) + '-' + dos(d.getDate())
}

// Suma el registro al resumen por día (que dura para siempre; los registros se podan)
export function sumarADia(dias, reg) {
  const k = claveDia(reg.t)
  const dia = dias[k] || { n: 0, uso: usoVacio(), sub: usoVacio(), mod: {} }
  dia.n += 1
  dia.uso = sumarUso(dia.uso, usoRegistro(reg))
  dia.sub = sumarUso(dia.sub, reg.sub)
  for (const [m, u] of Object.entries(reg.mod)) dia.mod[m] = sumarUso(dia.mod[m] || usoVacio(), u)
  dias[k] = dia
  return dias
}

// Suma al resumen por día lo que un subagente gastó después de que el prompt ya se había cerrado,
// sin contar un prompt más
export function sumarTardio(dias, t, delta) {
  const k = claveDia(t)
  const dia = dias[k] || { n: 0, uso: usoVacio(), sub: usoVacio(), mod: {} }
  dia.uso = sumarUso(dia.uso, delta.uso)
  dia.sub = sumarUso(dia.sub, delta.sub)
  for (const [m, u] of Object.entries(delta.mod)) dia.mod[m] = sumarUso(dia.mod[m] || usoVacio(), u)
  dias[k] = dia
  return dias
}

// Se queda con los últimos `max` elementos (registros y muestras usan la misma poda)
export function podar(lista, max = MAX_REGISTROS) {
  return lista.length > max ? lista.slice(lista.length - max) : lista
}

// Tokens gastados desde un instante (para relacionarlos con el % de la ventana)
export function usoDesde(registros, desdeMs) {
  return registros.filter((r) => r.t >= desdeMs).reduce((acc, r) => sumarUso(acc, usoRegistro(r)), usoVacio())
}

// Estima cuántos tokens nuevos valen un punto de la ventana, con lo gastado y el % usado
export function tokensPorPunto(registros, ventana, duracion, ahora) {
  if (!ventana || !ventana.resetsAt || !(ventana.pct > 0)) return null
  if (ahora !== undefined && ventana.resetsAt < ahora) return null
  const desde = ventana.resetsAt - duracion
  const nuevos = frescos(usoDesde(registros, desde))
  if (nuevos <= 0) return null
  return Math.round(nuevos / ventana.pct)
}

export function ultimosDias(dias, cuantos, ahoraMs) {
  const filas = []
  for (let i = cuantos - 1; i >= 0; i--) {
    const f = new Date(ahoraMs)
    f.setDate(f.getDate() - i) // por calendario: un cambio de horario no repite ni salta un día
    const k = claveDia(f.getTime())
    const d = dias[k]
    filas.push({ dia: k, n: d ? d.n : 0, uso: d ? d.uso : usoVacio(), sub: d ? d.sub : usoVacio(), mod: d ? d.mod : {} })
  }
  return filas
}

export function porModelo(filas) {
  const acc = {}
  for (const f of filas) for (const [m, u] of Object.entries(f.mod)) acc[m] = sumarUso(acc[m] || usoVacio(), u)
  return Object.entries(acc)
    .map(([modelo, uso]) => ({ modelo, uso }))
    .sort((a, b) => totalUso(b.uso) - totalUso(a.uso))
}

export function masCaros(registros, desdeMs, cuantos) {
  return registros
    .filter((r) => r.t >= desdeMs)
    .map((r) => ({ reg: r, nuevos: r.nu === undefined ? frescos(usoRegistro(r)) : r.nu }))
    .sort((a, b) => b.nuevos - a.nuevos)
    .slice(0, cuantos)
}

// ---- Formato ----

export function tokens(n) {
  const v = Math.round(n)
  if (v >= 999500) return (v / 1e6).toFixed(1).replace('.', ',') + ' M'
  if (v >= 1e4) return Math.round(v / 1e3) + ' k'
  if (v >= 1e3) return (v / 1e3).toFixed(1).replace('.', ',') + ' k'
  return String(v)
}

// 1,5 en lugar de 1.5, para el español
export const coma = (n) => String(n).replace('.', ',')

export function barra(pct, ancho = 20) {
  const lleno = Math.max(0, Math.min(ancho, Math.round((pct / 100) * ancho)))
  return '█'.repeat(lleno) + '░'.repeat(ancho - lleno)
}

export function porcentaje(pct) {
  return (Math.round(pct * 10) / 10).toString().replace('.', ',') + ' %'
}

export function tiempoHasta(ms, ahora) {
  if (ms === null || ms === undefined) return '—'
  const s = Math.max(0, Math.round((ms - ahora) / 1000))
  const d = Math.floor(s / 86400)
  const h = Math.floor((s % 86400) / 3600)
  const m = Math.floor((s % 3600) / 60)
  if (d > 0) return d + ' d ' + h + ' h'
  if (h > 0) return h + ' h ' + m + ' min'
  return m + ' min'
}

export function hora(ms) {
  const d = new Date(ms)
  const dos = (n) => String(n).padStart(2, '0')
  return dos(d.getHours()) + ':' + dos(d.getMinutes())
}

export function fechaCorta(clave) {
  const [, mes, dia] = clave.split('-')
  return dia + '/' + mes
}

export function nombreModelo(id) {
  const m = String(id || '').replace(/^claude-/, '')
  return m.replace(/-\d{8}$/, '')
}


// ---- Roles: quién gastó (hilo principal y subagentes por rol, modelo y esfuerzo) ----

// El mapa agentId → { rol, modelo, esfuerzo, t } con uno más, sin pasar del tope (se van los que entraron primero)
export function anotarAgente(mapa, agentId, datos, max = MAX_AGENTES) {
  const nuevo = { ...(mapa || {}) }
  delete nuevo[agentId] // si se repite, se renueva y pasa a ser el más reciente
  nuevo[agentId] = {
    rol: String(datos.rol || ''),
    modelo: String(datos.modelo || ''),
    esfuerzo: String(datos.esfuerzo || ''),
    t: Number(datos.t) || 0,
  }
  // Se expulsa por orden de inserción (el primero que entró), no por `t`
  const claves = Object.keys(nuevo)
  if (claves.length <= max) return nuevo
  for (const k of claves.slice(0, claves.length - max)) delete nuevo[k]
  return nuevo
}

// Filas por rol, modelo y esfuerzo con los tokens de los registros desde `desdeMs`.
// Hilo principal = uso del registro menos subagentes. Lo que un registro no atribuye a un agente
// conocido (sin sub_ag, agente sin rol o con el spawn ya podado) cae en «sin rol»,
// así que las filas siempre suman el uso total de los registros.
export function porRol(registros, mapa, desdeMs = 0) {
  const acc = new Map()
  const sumar = (rol, modelo, esfuerzo, uso, id) => {
    const k = [rol, modelo, esfuerzo].join('|')
    const f = acc.get(k) || { rol, modelo, esfuerzo, uso: usoVacio(), ids: new Set(), agentes: 0 }
    f.uso = sumarUso(f.uso, uso)
    if (id) f.ids.add(id) // ids únicos: un mismo agente en varios prompts cuenta una vez
    f.agentes = f.ids.size
    acc.set(k, f)
  }
  const m = mapa || {}
  for (const r of registros) {
    if (r.t < desdeMs) continue
    const sub = r.sub || usoVacio()
    sumar(PRINCIPAL, '', '', restarUso(usoRegistro(r), sub), null)
    let atribuido = usoVacio()
    for (const [id, uso] of Object.entries(r.sub_ag || {})) {
      const a = id === OTROS ? null : m[id]
      if (a && a.rol) sumar(a.rol, a.modelo, a.esfuerzo, uso, id)
      else sumar(SIN_ROL, a ? a.modelo : '', a ? a.esfuerzo : '', uso, id === OTROS ? null : id)
      atribuido = sumarUso(atribuido, uso)
    }
    const resto = restarUso(sub, atribuido)
    if (resto.some((x) => x !== 0)) sumar(SIN_ROL, '', '', resto, null)
  }
  return [...acc.values()].map(({ ids, ...f }) => f).filter((f) => totalUso(f.uso) !== 0).sort((a, b) => frescos(b.uso) - frescos(a.uso))
}

// Qué se escribe en el archivo de `/consumo exportar`. Solo cifras, fechas y roles:
// nunca el texto del prompt, la carpeta del proyecto ni los ids de turno o de agente.
export function construirExportacion(registros, mapa, ahoraMs) {
  const m = mapa || {}
  const cifras = (u) => ({ entrada: u[0], salida: u[1], cache_leida: u[2], cache_escrita: u[3], nuevos: frescos(u) })
  const lista = registros.map((r) => ({
    fecha: new Date(r.t).toISOString(),
    modelos: Object.fromEntries(Object.entries(r.mod || {}).map(([k, u]) => [k, cifras(u)])),
    total: cifras(usoRegistro(r)),
    subagentes: cifras(r.sub || usoVacio()),
    por_rol: porRol([r], m).map((f) => ({ rol: f.rol, modelo: f.modelo || null, esfuerzo: f.esfuerzo || null, ...cifras(f.uso) })),
    puntos_5h: puntos(r.p5),
    puntos_semana: puntos(r.p7),
  }))
  return {
    version: 1,
    generado: new Date(ahoraMs).toISOString(),
    prompts: lista.length,
    por_rol: porRol(registros, m).map((f) => ({ rol: f.rol, modelo: f.modelo || null, esfuerzo: f.esfuerzo || null, ...cifras(f.uso) })),
    registros: lista,
  }
}
