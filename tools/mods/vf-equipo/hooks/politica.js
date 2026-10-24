// Política de modelos y esfuerzo por agente del mod de equipo.
// Lógica pura, sin acceso al motor, para poder probarla (mismo patrón que vf-consumo/hooks/logica.js).
// La tabla vive en studio/data/equipo.json: cada rol con agente trae `modelo` y `esfuerzo`, y el bloque
// `politica_modelos` dice qué valores son válidos y si Fable 5.1 exige autorización.

export const MODELOS = ['haiku', 'sonnet', 'opus', 'fable']
export const ESFUERZOS = ['low', 'medium', 'high', 'xhigh', 'max']
// Cuánto dura un «Aprobar para esta tarea»
export const TTL_APROBACION_MS = 8 * 3600 * 1000
export const MAX_LANZAMIENTOS = 500
export const MAX_APROBACIONES = 50
export const DENEGADO_FABLE = 'Fable no autorizado'

// Etiquetas del diálogo. El diálogo del motor admite de 2 a 4 opciones, así que se pregunta en dos pasos:
// primero aprobar o cambiar de modelo, y si se cambia, cuál.
export const OP_TAREA = 'Aprobar para esta tarea'
export const OP_SOLO = 'Aprobar solo este'
export const OP_OTRO = 'Usar otro modelo'
export const OP_MODELO = { opus: 'Usar Opus', sonnet: 'Usar Sonnet', haiku: 'Usar Haiku' }

const ID_TAREA = /\bF\d+-\d+\b/g

function listaValida(equipo, campo, porDefecto) {
  const p = equipo && equipo.politica_modelos
  return p && Array.isArray(p[campo]) && p[campo].length ? p[campo] : porDefecto
}

// El rol de un subagente según su tipo (campo `agente` de los roles). Acepta el tipo con prefijo de plugin («plugin:analista»).
export function resolverRol(subagentType, equipo) {
  if (!subagentType || !equipo || !Array.isArray(equipo.roles)) return null
  const tipo = String(subagentType)
  const base = tipo.includes(':') ? tipo.split(':').pop() : tipo
  return equipo.roles.find((r) => r.agente && (r.agente === tipo || r.agente === base)) || null
}

// Qué modelo y esfuerzo lleva un encargo: lo que el coordinador fijó se respeta; lo que falta se rellena con la tabla del rol.
// Devuelve { rol, model, effort, motivo }. `motivo` es «defecto» (todo sale de la tabla) o «ajuste» (el coordinador cambió algo).
// Sin equipo o sin rol conocido no se inventa nada: model y effort quedan como venían.
export function resolverEleccion(entrada, equipo) {
  const e = entrada || {}
  const rol = resolverRol(e.subagent_type, equipo)
  const modelos = listaValida(equipo, 'modelos', MODELOS)
  const esfuerzos = listaValida(equipo, 'esfuerzos', ESFUERZOS)
  const deTabla = {
    model: rol && modelos.includes(rol.modelo) ? rol.modelo : undefined,
    effort: rol && esfuerzos.includes(rol.esfuerzo) ? rol.esfuerzo : undefined,
  }
  const model = e.model || deTabla.model
  const effort = e.effort || deTabla.effort
  const ajusta = (e.model && e.model !== deTabla.model) || (e.effort && e.effort !== deTabla.effort)
  return { rol: rol ? rol.id : '', model, effort, motivo: ajusta ? 'ajuste' : 'defecto' }
}

// ¿Hay que pedir permiso al autor? Sin equipo legible se pide igual (más vale preguntar de más que dejar pasar Fable).
export function pideFable(eleccion, equipo) {
  if (!eleccion || !/fable/i.test(String(eleccion.model || ''))) return false
  const p = equipo && equipo.politica_modelos
  return !(p && p.fable_requiere_autorizacion === false)
}

// La tarea a la que pertenece un encargo: el ID (F0-87…) más repetido en la descripción y el prompt;
// si no hay, el de la rama git. Cadena vacía si no hay ninguno.
export function claveTarea(texto, rama) {
  const cuenta = new Map()
  for (const id of String(texto || '').match(ID_TAREA) || []) cuenta.set(id, (cuenta.get(id) || 0) + 1)
  let mejor = ''
  let max = 0
  for (const [id, n] of cuenta) {
    if (n > max) {
      mejor = id
      max = n
    }
  }
  if (mejor) return mejor
  const deRama = String(rama || '').match(ID_TAREA)
  return deRama ? deRama[0] : ''
}

// ---------- aprobaciones por tarea ----------

// ¿Hay una aprobación sin caducar para la tarea?
export function aprobacionVigente(aprobaciones, clave, ahora) {
  if (!clave || !aprobaciones || typeof aprobaciones !== 'object') return false
  const hasta = aprobaciones[clave]
  return typeof hasta === 'number' && hasta > ahora
}

// El mapa de aprobaciones con la tarea añadida, sin las caducadas y con tope
export function aprobar(aprobaciones, clave, ahora, ttl = TTL_APROBACION_MS) {
  const siguiente = {}
  for (const [k, hasta] of Object.entries(aprobaciones || {})) if (typeof hasta === 'number' && hasta > ahora) siguiente[k] = hasta
  siguiente[clave] = ahora + ttl
  const claves = Object.keys(siguiente).sort((a, b) => siguiente[b] - siguiente[a]).slice(0, MAX_APROBACIONES)
  return Object.fromEntries(claves.map((k) => [k, siguiente[k]]))
}

// ---------- diálogo de Fable ----------

// La pregunta del primer paso. Sin tarea identificada no se ofrece aprobarla entera.
export function preguntaFable(eleccion, descripcion, clave) {
  const que = (eleccion.rol || 'este agente') + (descripcion ? ' («' + String(descripcion).slice(0, 60) + '»)' : '')
  return {
    pregunta: 'Fable 5.1 gasta mucho más: ¿lo usamos en ' + que + (clave ? ' de la tarea ' + clave : '') + '?',
    header: 'Fable 5.1',
    opciones: clave ? [OP_TAREA, OP_SOLO, OP_OTRO] : [OP_SOLO, OP_OTRO],
  }
}

// El segundo paso: a qué modelo cambiar
export function preguntaOtroModelo(descripcion) {
  return {
    pregunta: '¿Con qué modelo lo lanzamos' + (descripcion ? ' («' + String(descripcion).slice(0, 60) + '»)' : '') + '?',
    header: 'Modelo',
    opciones: [OP_MODELO.opus, OP_MODELO.sonnet, OP_MODELO.haiku],
  }
}

// Lo que significa una respuesta: una etiqueta exacta, o el texto libre de «Other», que solo vale si nombra un modelo
// (opus, sonnet o haiku); cualquier otra cosa se toma como rechazo.
// Devuelve { accion: 'tarea' | 'solo' | 'otro' | 'modelo' | 'rechazar', model? }.
export function interpretarRespuesta(respuesta) {
  const texto = String(respuesta || '').trim()
  if (texto === OP_TAREA) return { accion: 'tarea' }
  if (texto === OP_SOLO) return { accion: 'solo' }
  if (texto === OP_OTRO) return { accion: 'otro' }
  for (const [m, etiqueta] of Object.entries(OP_MODELO)) if (texto === etiqueta) return { accion: 'modelo', model: m }
  const palabras = texto.toLowerCase().match(/[a-záéíóúñ]+/g) || []
  const nombrados = Object.keys(OP_MODELO).filter((m) => palabras.includes(m))
  if (nombrados.length === 1 && !palabras.includes('fable')) return { accion: 'modelo', model: nombrados[0] }
  return { accion: 'rechazar' }
}

// ---------- lanzamientos ----------

// La familia de un modelo a partir de su alias o su id completo
export function familiaDe(modelo) {
  const m = String(modelo || '').toLowerCase()
  return MODELOS.find((f) => m.includes(f)) || ''
}

export function nuevoLanzamiento({ rol, modelo, esfuerzo, motivo, tarea, autorizado, t }) {
  return { rol: rol || '', modelo: modelo || '', esfuerzo: esfuerzo || '', motivo: motivo === 'ajuste' ? 'ajuste' : 'defecto', tarea: tarea || '', autorizado: Boolean(autorizado), t: t || 0 }
}

// El mapa agentId → lanzamiento con uno más, sin pasar del tope (se van los más antiguos)
export function anotarLanzamiento(mapa, agentId, registro, max = MAX_LANZAMIENTOS) {
  const siguiente = { ...(mapa || {}), [agentId]: registro }
  const ids = Object.keys(siguiente)
  if (ids.length <= max) return siguiente
  ids.sort((a, b) => (siguiente[b].t || 0) - (siguiente[a].t || 0))
  return Object.fromEntries(ids.slice(0, max).map((id) => [id, siguiente[id]]))
}

// Cuántos lanzamientos hubo por modelo desde un instante (el inicio de la sesión)
export function contarPorModelo(mapa, desde = 0) {
  const cuenta = {}
  for (const l of Object.values(mapa || {})) {
    if ((l.t || 0) < desde) continue
    const clave = familiaDe(l.modelo) || 'heredado'
    cuenta[clave] = (cuenta[clave] || 0) + 1
  }
  return cuenta
}

// Los últimos lanzamientos, el más reciente primero
export function ultimosLanzamientos(mapa, n = 5) {
  return Object.entries(mapa || {})
    .map(([id, l]) => ({ id, ...l }))
    .sort((a, b) => (b.t || 0) - (a.t || 0))
    .slice(0, n)
}

// El mensaje al coordinador para cambiar el modelo o el esfuerzo de un rol en equipo.json (los mods no editan archivos)
export function mensajeCambio(rol, que) {
  const campo = que === 'esfuerzo' ? 'esfuerzo' : 'modelo'
  const validos = campo === 'modelo' ? MODELOS : ESFUERZOS
  const ahora = (campo === 'modelo' ? rol.modelo : rol.esfuerzo) || 'sin definir'
  return (
    'Quiero cambiar el ' + campo + ' del rol «' + rol.nombre + '» (agente ' + rol.agente + '), que ahora es ' + ahora + '. ' +
    'Pregúntame a cuál (' + validos.join(', ') + ') y edita el campo «' + campo + '» de ese rol en studio/data/equipo.json; ' +
    'después sincroniza el agente y deja constancia en la tarea.' + (campo === 'modelo' ? ' Recuerda que Fable 5.1 sigue necesitando mi autorización en cada lanzamiento.' : '')
  )
}
