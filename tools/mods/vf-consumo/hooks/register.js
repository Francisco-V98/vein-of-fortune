// Mod de consumo: guarda cuántos tokens gasta cada prompt, cuánto sube cada ventana
// (cinco horas y semanal) y arma un historial para ver en qué se fue el consumo.
import {
  acumularTurno, anotarAgente, barra, construirExportacion, porRol, PRINCIPAL, SIN_ROL, cerrarRegistro, claveDia, coma, fechaCorta, frescos, hora, leerLimites, masCaros, nombreModelo,
  nuevoRegistro, podar, porModelo, porcentaje, puntos, restarUso, sumarADia, sumarTardio, tiempoHasta, tokens,
  tokensPorPunto, ultimosDias, usoRegistro, usoVacio, sumarUso,
  CINCO_HORAS, MAX_MUESTRAS, SIETE_DIAS,
} from './logica.js'

const PANE = 'vf-consumo'

// Estado del módulo (se pierde al recargar; lo que importa vive en $.store)
let registros = []
let dias = {}
let muestras = []
let agentes = {} // agentId → { rol, modelo, esfuerzo, t }, propio de este mod y acotado
const pendientes = [] // Agent en curso: de ahí sale el esfuerzo, que agent.spawn no trae
let limites = { cinco: null, semana: null }
const abiertos = new Map() // prompts en curso, por id de turno
let ultimoCerrado = null // el último prompt guardado: recibe lo que un subagente gaste tarde
let cola = Promise.resolve() // las escrituras al almacén van una detrás de otra
let temporizador = null
let tab = 'ahora'
let orden = 'recientes'
let abierto = null
let pagina = 0
let error = ''
let aviso = ''

async function cargarAlmacen($) {
  try {
    registros = (await $.store.get('registros')) || []
    dias = (await $.store.get('dias')) || {}
    muestras = (await $.store.get('muestras')) || []
    agentes = (await $.store.get('agentes')) || {}
  } catch (e) {
    fallo('No se pudo leer el historial: ', e)
  }
}

// Encola una escritura: dentro de esta sesión nunca se pisan dos escrituras seguidas.
// Con dos sesiones abiertas a la vez queda una ventana mínima entre leer y guardar.
function enCola(tarea) {
  cola = cola.then(tarea, tarea)
  return cola
}

function fallo(prefijo, e) {
  error = prefijo + (e && e.message ? e.message : String(e))
}

// Guarda un prompt cerrado: lee el almacén, lo suma y lo guarda de nuevo.
// Si el id ya estaba, lo reemplaza y no lo cuenta dos veces en el resumen por día.
function guardarRegistro($, reg) {
  return enCola(async () => {
    try {
      const lista = (await $.store.get('registros')) || []
      const nuevoDias = (await $.store.get('dias')) || {}
      const ya = lista.some((r) => r.id === reg.id)
      if (!ya) sumarADia(nuevoDias, reg)
      registros = podar([...lista.filter((r) => r.id !== reg.id), reg])
      dias = nuevoDias
      await $.store.set('registros', registros)
      await $.store.set('dias', dias)
      error = ''
    } catch (e) {
      fallo('No se pudo guardar el historial: ', e)
    }
  })
}

// Un subagente terminó después de que su prompt se cerró: su gasto se suma a ese prompt
function guardarTardio($, reg, delta) {
  return enCola(async () => {
    try {
      const lista = (await $.store.get('registros')) || []
      const nuevoDias = (await $.store.get('dias')) || {}
      sumarTardio(nuevoDias, reg.t, delta)
      registros = podar([...lista.filter((r) => r.id !== reg.id), reg])
      dias = nuevoDias
      await $.store.set('registros', registros)
      await $.store.set('dias', dias)
      error = ''
    } catch (e) {
      fallo('No se pudo guardar el historial: ', e)
    }
  })
}

function guardarAgente($, agentId, datos) {
  return enCola(async () => {
    try {
      agentes = anotarAgente((await $.store.get('agentes')) || agentes, agentId, datos)
      await $.store.set('agentes', agentes)
    } catch (e) {
      // sin el mapa el gasto sale como «sin rol»: no se avisa
    }
  })
}

function guardarMuestra($, ahora) {
  if (!limites.cinco && !limites.semana) return Promise.resolve()
  return enCola(async () => {
    try {
      const lista = (await $.store.get('muestras')) || []
      lista.push([ahora, limites.cinco ? limites.cinco.pct : null, limites.semana ? limites.semana.pct : null])
      muestras = podar(lista, MAX_MUESTRAS)
      await $.store.set('muestras', muestras)
    } catch (e) {
      // las muestras son un extra: si falla, no se avisa
    }
  })
}

async function leerLimitesAhora($) {
  try {
    const u = await $.session.usage()
    limites = leerLimites(u.rateLimits)
  } catch (e) {
    // sin suscripción no hay ventanas: el panel lo dice
  }
}

// Una ventana cuya hora de reinicio ya pasó está vencida: su porcentaje es una lectura vieja
const vencida = (v, ahora) => Boolean(v && v.resetsAt && v.resetsAt < ahora)

function textoEstado(ahora) {
  const c = limites.cinco && !vencida(limites.cinco, ahora) ? porcentaje(limites.cinco.pct) : '—'
  const s = limites.semana && !vencida(limites.semana, ahora) ? porcentaje(limites.semana.pct) : '—'
  return '5 h ' + c + ' · semana ' + s
}

function carpeta(ruta) {
  const partes = String(ruta || '').split('/').filter(Boolean)
  return partes.length ? partes[partes.length - 1] : ''
}

// Un subagente cuenta dentro del prompt que lo lanzó. Si ese prompt ya se cerró, su gasto se
// suma al último guardado, para no inventar un prompt que nadie escribió.
async function registrarSubagente($, e, ahora) {
  const enCurso = [...abiertos.values()].pop()
  if (enCurso) {
    acumularTurno(enCurso, e.usage, true, e.durationMs, e.agentId)
    return
  }
  if (!ultimoCerrado) return
  const antes = { uso: usoRegistro(ultimoCerrado), sub: ultimoCerrado.sub, mod: { ...ultimoCerrado.mod } }
  acumularTurno(ultimoCerrado, e.usage, true, e.durationMs, e.agentId)
  const mod = {}
  for (const [m, u] of Object.entries(ultimoCerrado.mod)) mod[m] = restarUso(u, antes.mod[m] || usoVacio())
  const delta = { uso: restarUso(usoRegistro(ultimoCerrado), antes.uso), sub: restarUso(ultimoCerrado.sub, antes.sub), mod }
  await guardarTardio($, ultimoCerrado, delta)
}

export function register(on) {
  on('session.start', async ($, e, next) => {
    await cargarAlmacen($)
    await leerLimitesAhora($)
    $.ui.status(textoEstado(await $.clock.now()))
    // La cuenta atrás de las ventanas se refresca sola cada minuto
    if (temporizador) temporizador.cancel()
    temporizador = $.clock.every(60000, () => $.ui.invalidate('ui.render'))
    await $.command.register({
      name: 'consumo',
      description: 'Panel de consumo de tokens: ventana de cinco horas, semana, prompts e historial',
      immediate: true,
    })
    return next(e)
  })

  on('command.run', { command: 'consumo' }, async ($, e) => {
    if (String((e && e.args) || '').trim().toLowerCase() === 'exportar') await exportar($)
    await $.ui.open({ id: PANE, title: 'Consumo', focus: true, closeOnEscape: true })
    return {}
  })

  // Solo observa los Agent que se lanzan (no los modifica): respaldo para el esfuerzo si agent.spawn no lo trae
  on('tool.call', { tool: 'Agent' }, async ($, e, next) => {
    pendientes.push({ id: e.tool_use_id, tipo: e.subagent_type || '', descripcion: e.description || '', esfuerzo: e.effort || '' })
    if (pendientes.length > 50) pendientes.shift()
    return next(e)
  })

  // Apunta rol, modelo y esfuerzo de cada subagente: lo necesita la vista «Roles»
  on('agent.spawn', async ($, e, next) => {
    const r = await next(e)
    if (!r || r.deny || !r.agentId || e.resume) return r
    try {
      const i = pendientes.findIndex((p) => (e.tool_use_id && p.id === e.tool_use_id) || (p.tipo === e.subagentType && p.descripcion === e.description))
      const p = i >= 0 ? pendientes.splice(i, 1)[0] : null
      const rol = String(e.subagentType || '').split(':').pop()
      await guardarAgente($, r.agentId, { rol, modelo: nombreModelo(r.model || e.model), esfuerzo: e.effort || (p && p.esfuerzo) || '', t: await $.clock.now() })
    } catch (err) {
      // un fallo aquí no debe frenar el lanzamiento
    }
    return r
  })

  // Cada turno del hilo principal es un «prompt»: aquí se abre su registro
  on('turn.start', async ($, e, next) => {
    try {
      const ahora = await $.clock.now()
      const cwd = await $.session.cwd()
      await leerLimitesAhora($)
      abiertos.set(e.turnId, nuevoRegistro({ id: e.turnId, t: ahora, texto: e.text, proyecto: carpeta(cwd), limites }))
    } catch (err) {
      abiertos.delete(e.turnId)
    }
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    try {
      const ahora = await $.clock.now()
      if (e.agentId) {
        await registrarSubagente($, e, ahora)
      } else {
        const reg = abiertos.get(e.turnId) || nuevoRegistro({ id: e.turnId, t: ahora - (e.durationMs || 0), texto: '', proyecto: '', limites })
        acumularTurno(reg, e.usage, false, e.durationMs)
        await leerLimitesAhora($)
        cerrarRegistro(reg, limites)
        abiertos.delete(e.turnId)
        ultimoCerrado = reg
        await guardarRegistro($, reg)
        await guardarMuestra($, ahora)
      }
      $.ui.status(textoEstado(ahora))
      $.ui.invalidate('ui.render')
    } catch (err) {
      fallo('Error al registrar el turno: ', err)
    }
    return next(e)
  })

  // El motor avisa cuando una ventana sube un punto entero
  on('session.measure', async ($, e, next) => {
    try {
      if (e.changed && e.changed.includes('rateLimits')) {
        limites = leerLimites(e.rateLimits)
        const ahora = await $.clock.now()
        $.ui.status(textoEstado(ahora))
        await guardarMuestra($, ahora)
        $.ui.invalidate('ui.render')
      }
    } catch (err) {
      // el aviso es un extra: nada que hacer si falla
    }
    return next(e)
  })

  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    if (e.requestId !== PANE) return next(e)
    const { Box, Text, Button } = $.ui.resolve(e)
    const ahora = await $.clock.now()
    const filas = e.viewport && e.viewport.rows ? e.viewport.rows : 24
    const redibujar = () => $.ui.invalidate('ui.render')
    const ctx = { Text, Box, Button, redibujar, ahora, filas }

    const pestana = (nombre, etiqueta, tecla) =>
      Button({
        key: 'tab-' + nombre,
        label: etiqueta,
        hotkey: tecla,
        plain: true,
        dimColor: tab !== nombre,
        onPress: () => {
          tab = nombre
          pagina = 0
          abierto = null
          aviso = ''
          redibujar()
        },
      })

    const cabecera = Box({
      flexDirection: 'row',
      columnGap: 3,
      children: [pestana('ahora', 'Ahora', '1'), pestana('prompts', 'Prompts', '2'), pestana('dias', 'Días', '3'), pestana('roles', 'Roles', '4')],
    })

    const cuerpo = []
    if (error) cuerpo.push(Text({ color: 'yellow', children: [error] }))
    if (aviso) cuerpo.push(Text({ color: 'green', wrap: 'truncate', children: [aviso] }))
    if (tab === 'ahora') cuerpo.push(...vistaAhora(ctx))
    else if (tab === 'prompts') cuerpo.push(...vistaPrompts(ctx))
    else if (tab === 'roles') cuerpo.push(...vistaRoles(ctx))
    else cuerpo.push(...vistaDias(ctx))

    return Box({ flexDirection: 'column', children: [cabecera, Text({ children: [' '] }), ...cuerpo] })
  })
}

const titulo = (Text, texto) => Text({ bold: true, color: 'cyan', children: [texto] })
const linea = (Text, texto, dim) => Text({ dimColor: Boolean(dim), wrap: 'truncate', children: [texto] })
const vacio = (Text) => Text({ children: [' '] })

function filaVentana(Text, nombre, ventana, ahora) {
  if (!ventana) return linea(Text, nombre + ': sin lectura todavía (aparece tras el primer mensaje)', true)
  if (vencida(ventana, ahora)) return linea(Text, nombre + ': ventana reiniciada · la lectura se actualiza con el próximo mensaje', true)
  return linea(Text, nombre + ' ' + barra(ventana.pct, 18) + ' ' + porcentaje(ventana.pct) + ' · se reinicia en ' + tiempoHasta(ventana.resetsAt, ahora))
}

function vistaAhora({ Text, ahora }) {
  const filas = []
  filas.push(titulo(Text, 'Ventanas de uso'))
  filas.push(filaVentana(Text, 'Cinco horas', limites.cinco, ahora))
  filas.push(filaVentana(Text, 'Semana     ', limites.semana, ahora))
  if (!limites.cinco && !limites.semana) {
    filas.push(linea(Text, 'Las ventanas solo existen con una suscripción de Claude.', true))
  }
  filas.push(vacio(Text))

  const hoy = ultimosDias(dias, 1, ahora)[0]
  filas.push(titulo(Text, 'Hoy'))
  filas.push(linea(Text, hoy.n + ' prompts · ' + tokens(frescos(hoy.uso)) + ' tokens nuevos · ' + tokens(hoy.uso[2]) + ' leídos de caché'))
  filas.push(linea(Text, 'Subagentes: ' + tokens(frescos(hoy.sub)) + ' tokens nuevos de esos'))
  filas.push(vacio(Text))

  filas.push(titulo(Text, 'Cuánto vale un punto'))
  const por5 = tokensPorPunto(registros, limites.cinco, CINCO_HORAS, ahora)
  const por7 = tokensPorPunto(registros, limites.semana, SIETE_DIAS, ahora)
  filas.push(linea(Text, 'Cinco horas: ' + (por5 ? '≈ ' + tokens(por5) + ' tokens nuevos por 1 %' : 'aún sin datos')))
  filas.push(linea(Text, 'Semana: ' + (por7 ? '≈ ' + tokens(por7) + ' tokens nuevos por 1 %' : 'aún sin datos')))
  filas.push(linea(Text, 'Estimación con lo que este mod vio gastar en cada ventana.', true))
  filas.push(vacio(Text))

  filas.push(titulo(Text, 'Últimos prompts'))
  const ultimos = registros.slice(-5).reverse()
  if (!ultimos.length) filas.push(linea(Text, 'Todavía no hay prompts registrados.', true))
  for (const r of ultimos) filas.push(filaPrompt(Text, r))
  return filas
}

function filaPrompt(Text, r) {
  const p = puntos(r.p5)
  const delta = p === null ? '' : ' · +' + coma(p) + ' pts'
  return linea(Text, hora(r.t) + ' · ' + tokens(frescos(usoRegistro(r))) + delta + ' · ' + r.txt)
}

function vistaPrompts({ Text, Box, Button, redibujar, filas }) {
  const salida = []
  const base = registros.slice()
  const lista = orden === 'recientes' ? base.reverse() : base.sort((a, b) => (b.nu === undefined ? frescos(usoRegistro(b)) : b.nu) - (a.nu === undefined ? frescos(usoRegistro(a)) : a.nu))
  const tamano = Math.max(5, Math.floor((filas - 8) / 2))
  const paginas = Math.max(1, Math.ceil(lista.length / tamano))
  if (pagina >= paginas) pagina = paginas - 1

  salida.push(
    Box({
      flexDirection: 'row',
      columnGap: 3,
      children: [
        Button({ key: 'orden', label: orden === 'recientes' ? 'Orden: recientes' : 'Orden: más caros', plain: true, onPress: () => { orden = orden === 'recientes' ? 'caros' : 'recientes'; pagina = 0; redibujar() } }),
        Button({ key: 'ant', label: '‹ Anterior', plain: true, dimColor: pagina === 0, onPress: () => { if (pagina > 0) pagina -= 1; redibujar() } }),
        Button({ key: 'sig', label: 'Siguiente ›', plain: true, dimColor: pagina >= paginas - 1, onPress: () => { if (pagina < paginas - 1) pagina += 1; redibujar() } }),
      ],
    }),
  )
  salida.push(linea(Text, 'Página ' + (pagina + 1) + ' de ' + paginas + ' · ' + lista.length + ' prompts guardados', true))
  salida.push(vacio(Text))
  if (!lista.length) salida.push(linea(Text, 'Todavía no hay prompts registrados.', true))
  for (const r of lista.slice(pagina * tamano, (pagina + 1) * tamano)) {
    const dia = fechaCorta(claveDia(r.t))
    salida.push(
      Button({
        key: 'p-' + r.id,
        plain: true,
        onPress: () => { abierto = abierto === r.id ? null : r.id; redibujar() },
        children: [Text({ wrap: 'truncate', children: [(abierto === r.id ? '▾ ' : '▸ ') + dia + ' ' + hora(r.t) + ' · ' + tokens(frescos(usoRegistro(r))) + ' · ' + r.txt] })],
      }),
    )
    if (abierto === r.id) salida.push(...detallePrompt(Text, r))
  }
  return salida
}

function detallePrompt(Text, r) {
  const u = usoRegistro(r)
  const p5 = puntos(r.p5)
  const p7 = puntos(r.p7)
  const filas = [
    linea(Text, '   Proyecto: ' + (r.cwd || '—') + ' · ' + r.n + (r.n === 1 ? ' turno' : ' turnos') + ' · ' + Math.round(r.ms / 1000) + ' s'),
    linea(Text, '   Entrada ' + tokens(u[0]) + ' · Salida ' + tokens(u[1]) + ' · Caché leída ' + tokens(u[2]) + ' · Caché escrita ' + tokens(u[3])),
    linea(Text, '   Principal ' + tokens(frescos(restarUso(u, r.sub))) + ' nuevos · Subagentes ' + tokens(frescos(r.sub)) + ' nuevos (' + r.subN + (r.subN === 1 ? ' turno)' : ' turnos)')),
    linea(Text, '   Ventanas: 5 h ' + (p5 === null ? '—' : '+' + coma(p5) + ' pts') + ' · semana ' + (p7 === null ? '—' : '+' + coma(p7) + ' pts') + ' (incluye el gasto de otras sesiones)'),
  ]
  for (const [m, uso] of Object.entries(r.mod)) filas.push(linea(Text, '   ' + nombreModelo(m) + ': ' + tokens(frescos(uso)) + ' nuevos, ' + tokens(uso[2]) + ' de caché', true))
  filas.push(linea(Text, '   ' + r.txt, true))
  return filas
}

function vistaDias({ Text, ahora }) {
  const salida = []
  const dias14 = ultimosDias(dias, 14, ahora)
  const maximo = Math.max(1, ...dias14.map((d) => frescos(d.uso)))
  salida.push(titulo(Text, 'Últimos 14 días (tokens nuevos)'))
  for (const d of dias14.slice().reverse()) {
    salida.push(linea(Text, fechaCorta(d.dia) + ' ' + barra((frescos(d.uso) / maximo) * 100, 14) + ' ' + tokens(frescos(d.uso)) + ' · ' + d.n + ' prompts', d.n === 0))
  }
  salida.push(vacio(Text))

  const semana = dias14.slice(-7)
  salida.push(titulo(Text, 'Últimos 7 días por modelo'))
  const modelos = porModelo(semana)
  if (!modelos.length) salida.push(linea(Text, 'Sin datos todavía.', true))
  for (const m of modelos) salida.push(linea(Text, nombreModelo(m.modelo) + ': ' + tokens(frescos(m.uso)) + ' nuevos · ' + tokens(m.uso[2]) + ' de caché'))
  const sub = semana.reduce((a, d) => sumarUso(a, d.sub), usoVacio())
  const todo = semana.reduce((a, d) => sumarUso(a, d.uso), usoVacio())
  salida.push(linea(Text, 'Subagentes: ' + tokens(frescos(sub)) + ' de ' + tokens(frescos(todo)) + ' nuevos', true))
  salida.push(vacio(Text))

  salida.push(titulo(Text, 'Lo más caro de la semana'))
  const caros = masCaros(registros, Date.parse(semana[0].dia + 'T00:00:00'), 5)
  if (!caros.length) salida.push(linea(Text, 'Sin datos todavía.', true))
  for (const c of caros) salida.push(linea(Text, fechaCorta(claveDia(c.reg.t)) + ' ' + hora(c.reg.t) + ' · ' + tokens(c.nuevos) + ' · ' + c.reg.txt))
  return salida
}

// Exporta cifras (sin el texto de los prompts) a un JSON local dentro del proyecto
const RUTA_EXPORTACION = '.claude/consumo'

async function exportar($) {
  try {
    const ahora = await $.clock.now()
    let base = ''
    try {
      base = String((await $.session.cwd()) || '').replace(/\/+$/, '')
    } catch (e) {
      // sin carpeta de sesión se usa la ruta relativa
    }
    const ruta = (base ? base + '/' : '') + RUTA_EXPORTACION + '/consumo-' + claveDia(ahora) + '.json'
    await $.fs.write(ruta, JSON.stringify(construirExportacion(registros, agentes, ahora), null, 2) + '\n')
    error = ''
    aviso = 'Exportado a ' + ruta + ' (' + registros.length + ' prompts, sin su texto)'
  } catch (e) {
    aviso = ''
    fallo('No se pudo exportar: ', e)
  }
}

const etiquetaFila = (f) => f.rol + (f.modelo ? ' · ' + f.modelo : '') + (f.esfuerzo ? ' · ' + f.esfuerzo : '')

function vistaRoles({ Text, ahora }) {
  const salida = []
  const desde = Date.parse(ultimosDias(dias, 7, ahora)[0].dia + 'T00:00:00')
  const filas = porRol(registros, agentes, desde)
  const total = filas.reduce((a, f) => a + frescos(f.uso), 0)
  salida.push(titulo(Text, 'Últimos 7 días por rol (tokens nuevos)'))
  salida.push(linea(Text, 'Hilo principal más subagentes por rol, modelo y esfuerzo; lo que no se puede atribuir sale como «sin rol».', true))
  if (!filas.length) salida.push(linea(Text, 'Sin datos todavía.', true))
  for (const f of filas) {
    const pct = total > 0 ? (frescos(f.uso) / total) * 100 : 0
    salida.push(linea(Text, barra(pct, 10) + ' ' + tokens(frescos(f.uso)) + ' · ' + porcentaje(pct) + ' · ' + etiquetaFila(f) + (f.agentes ? ' (' + f.agentes + (f.agentes === 1 ? ' agente)' : ' agentes)') : ''), f.rol === SIN_ROL))
  }
  if (filas.length) salida.push(linea(Text, 'Total ' + tokens(total) + ' nuevos · «' + PRINCIPAL + '» no lleva modelo ni esfuerzo.', true))
  salida.push(vacio(Text))
  salida.push(linea(Text, '/consumo exportar guarda estas cifras en ' + RUTA_EXPORTACION + ' (sin el texto de los prompts).', true))
  return salida
}
