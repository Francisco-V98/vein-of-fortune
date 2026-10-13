// Lógica pura del mod de consumo: sin acceso al motor, para poder probarla.
// Un «uso» es [entrada, salida, caché leída, caché escrita], en tokens.

export const MAX_REGISTROS = 3000
export const MAX_MUESTRAS = 600
export const CINCO_HORAS = 5 * 3600 * 1000
export const SIETE_DIAS = 7 * 24 * 3600 * 1000

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
    subN: 0,
    n: 0,
    ms: 0,
    p5: [l.cinco ? l.cinco.pct : null, null],
    p7: [l.semana ? l.semana.pct : null, null],
  }
}

// Suma el uso de un turno al registro: del hilo principal o de un subagente
export function acumularTurno(reg, usage, esSub, durMs) {
  const u = usoDe(usage)
  if (esSub) {
    reg.sub = sumarUso(reg.sub, u)
    reg.subN += 1
  } else {
    reg.n += 1
    reg.ms += Number(durMs) || 0
  }
  const modelo = (usage && usage.model) || 'desconocido'
  reg.mod[modelo] = sumarUso(reg.mod[modelo] || usoVacio(), u)
  return reg
}

// Uso total del registro (todos los modelos: principal más subagentes)
export function usoRegistro(reg) {
  return Object.values(reg.mod || {}).reduce((acc, u) => sumarUso(acc, u), usoVacio())
}

export function cerrarRegistro(reg, limites) {
  const l = limites || {}
  reg.p5[1] = l.cinco ? l.cinco.pct : reg.p5[1]
  reg.p7[1] = l.semana ? l.semana.pct : reg.p7[1]
  return reg
}

// Puntos de la ventana que gastó el registro (puede ser 0 por la resolución de un punto)
export function puntos(par) {
  if (!par || par[0] === null || par[1] === null) return null
  const d = Math.round((par[1] - par[0]) * 10) / 10
  return d < 0 ? 0 : d // si la ventana se reinició en medio, no se resta
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

export function podar(lista, max = MAX_REGISTROS) {
  return lista.length > max ? lista.slice(lista.length - max) : lista
}

export function podarMuestras(lista, max = MAX_MUESTRAS) {
  return lista.length > max ? lista.slice(lista.length - max) : lista
}

// Tokens gastados desde un instante (para relacionarlos con el % de la ventana)
export function usoDesde(registros, desdeMs) {
  return registros.filter((r) => r.t >= desdeMs).reduce((acc, r) => sumarUso(acc, usoRegistro(r)), usoVacio())
}

// Estima cuántos tokens nuevos valen un punto de la ventana, con lo gastado y el % usado
export function tokensPorPunto(registros, ventana, duracion) {
  if (!ventana || !ventana.resetsAt || !(ventana.pct > 0)) return null
  const desde = ventana.resetsAt - duracion
  const nuevos = frescos(usoDesde(registros, desde))
  if (nuevos <= 0) return null
  return Math.round(nuevos / ventana.pct)
}

export function ultimosDias(dias, cuantos, ahoraMs) {
  const filas = []
  for (let i = cuantos - 1; i >= 0; i--) {
    const k = claveDia(ahoraMs - i * 24 * 3600 * 1000)
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
    .map((r) => ({ reg: r, nuevos: frescos(usoRegistro(r)) }))
    .sort((a, b) => b.nuevos - a.nuevos)
    .slice(0, cuantos)
}

// ---- Formato ----

export function tokens(n) {
  const v = Math.round(n)
  if (v >= 1e6) return (v / 1e6).toFixed(1).replace('.', ',') + ' M'
  if (v >= 1e4) return Math.round(v / 1e3) + ' k'
  if (v >= 1e3) return (v / 1e3).toFixed(1).replace('.', ',') + ' k'
  return String(v)
}

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
