// Mod de consumo: guarda cuántos tokens gasta cada prompt, cuánto sube cada ventana
// (cinco horas y semanal) y arma un historial para ver en qué se fue el consumo.
import {
  acumularTurno, barra, cerrarRegistro, claveDia, fechaCorta, frescos, hora, leerLimites, masCaros, nombreModelo,
  nuevoRegistro, podar, podarMuestras, porModelo, porcentaje, puntos, sumarADia, tiempoHasta, tokens,
  tokensPorPunto, ultimosDias, usoRegistro, usoVacio, sumarUso,
  CINCO_HORAS, SIETE_DIAS,
} from './logica.js'

const PANE = 'vf-consumo'

// Estado del módulo (se pierde al recargar; lo que importa vive en $.store)
let registros = []
let dias = {}
let muestras = []
let limites = { cinco: null, semana: null }
let actual = null
let tab = 'ahora'
let orden = 'recientes'
let abierto = null
let pagina = 0
let error = ''

async function cargarAlmacen($) {
  try {
    registros = (await $.store.get('registros')) || []
    dias = (await $.store.get('dias')) || {}
    muestras = (await $.store.get('muestras')) || []
  } catch (e) {
    error = 'No se pudo leer el historial: ' + (e && e.message ? e.message : String(e))
  }
}

// Lee, suma y guarda de nuevo: así dos sesiones abiertas a la vez no se pisan
async function guardarRegistro($, reg) {
  try {
    const lista = ((await $.store.get('registros')) || []).filter((r) => r.id !== reg.id)
    lista.push(reg)
    const nuevoDias = (await $.store.get('dias')) || {}
    sumarADia(nuevoDias, reg)
    registros = podar(lista)
    dias = nuevoDias
    await $.store.set('registros', registros)
    await $.store.set('dias', dias)
  } catch (e) {
    error = 'No se pudo guardar el historial: ' + (e && e.message ? e.message : String(e))
  }
}

async function guardarMuestra($, ahora) {
  if (!limites.cinco && !limites.semana) return
  try {
    const lista = (await $.store.get('muestras')) || []
    lista.push([ahora, limites.cinco ? limites.cinco.pct : null, limites.semana ? limites.semana.pct : null])
    muestras = podarMuestras(lista)
    await $.store.set('muestras', muestras)
  } catch (e) {
    // las muestras son un extra: si falla, no se avisa
  }
}

async function leerLimitesAhora($) {
  try {
    const u = await $.session.usage()
    limites = leerLimites(u.rateLimits)
  } catch (e) {
    // sin suscripción no hay ventanas: el panel lo dice
  }
}

function textoEstado() {
  const c = limites.cinco ? porcentaje(limites.cinco.pct) : '—'
  const s = limites.semana ? porcentaje(limites.semana.pct) : '—'
  return '5 h ' + c + ' · semana ' + s
}

function carpeta(ruta) {
  const partes = String(ruta || '').split('/').filter(Boolean)
  return partes.length ? partes[partes.length - 1] : ''
}

export function register(on) {
  on('session.start', async ($, e, next) => {
    await cargarAlmacen($)
    await leerLimitesAhora($)
    $.ui.status(textoEstado())
    // La cuenta atrás de las ventanas se refresca sola cada minuto
    $.clock.every(60000, () => $.ui.invalidate('ui.render'))
    await $.command.register({
      name: 'consumo',
      description: 'Panel de consumo de tokens: ventana de cinco horas, semana, prompts e historial',
      immediate: true,
    })
    return next(e)
  })

  on('command.run', { command: 'consumo' }, async ($) => {
    await $.ui.open({ id: PANE, title: 'Consumo', focus: true, closeOnEscape: true })
    return {}
  })

  // Cada turno del hilo principal es un «prompt»: aquí se abre su registro
  on('turn.start', async ($, e, next) => {
    try {
      const ahora = await $.clock.now()
      const cwd = await $.session.cwd()
      await leerLimitesAhora($)
      actual = nuevoRegistro({ id: e.turnId, t: ahora, texto: e.text, proyecto: carpeta(cwd), limites })
    } catch (err) {
      actual = null
    }
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    try {
      const ahora = await $.clock.now()
      const esSub = Boolean(e.agentId)
      if (esSub) {
        // Subagente: cuenta dentro del prompt que lo lanzó; si ya cerró, va suelto
        const reg = actual || nuevoRegistro({ id: e.turnId, t: ahora, texto: '(trabajo en segundo plano)', proyecto: '', limites })
        acumularTurno(reg, e.usage, true, e.durationMs)
        if (!actual) {
          await guardarRegistro($, cerrarRegistro(reg, limites))
        }
      } else {
        const reg = actual || nuevoRegistro({ id: e.turnId, t: ahora - (e.durationMs || 0), texto: '', proyecto: '', limites })
        acumularTurno(reg, e.usage, false, e.durationMs)
        await leerLimitesAhora($)
        cerrarRegistro(reg, limites)
        actual = null
        await guardarRegistro($, reg)
        await guardarMuestra($, ahora)
      }
      $.ui.status(textoEstado())
      $.ui.invalidate('ui.render')
    } catch (err) {
      error = 'Error al registrar el turno: ' + (err && err.message ? err.message : String(err))
    }
    return next(e)
  })

  // El motor avisa cuando una ventana sube un punto entero
  on('session.measure', async ($, e, next) => {
    try {
      if (e.changed && e.changed.includes('rateLimits')) {
        limites = leerLimites(e.rateLimits)
        $.ui.status(textoEstado())
        await guardarMuestra($, await $.clock.now())
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
          redibujar()
        },
      })

    const cabecera = Box({
      flexDirection: 'row',
      columnGap: 3,
      children: [pestana('ahora', 'Ahora', '1'), pestana('prompts', 'Prompts', '2'), pestana('dias', 'Días', '3')],
    })

    const cuerpo = []
    if (error) cuerpo.push(Text({ color: 'yellow', children: [error] }))
    if (tab === 'ahora') cuerpo.push(...vistaAhora(ctx))
    else if (tab === 'prompts') cuerpo.push(...vistaPrompts(ctx))
    else cuerpo.push(...vistaDias(ctx))

    return Box({ flexDirection: 'column', children: [cabecera, Text({ children: [' '] }), ...cuerpo] })
  })
}

const titulo = (Text, texto) => Text({ bold: true, color: 'cyan', children: [texto] })
const linea = (Text, texto, dim) => Text({ dimColor: Boolean(dim), wrap: 'truncate', children: [texto] })
const vacio = (Text) => Text({ children: [' '] })

function filaVentana(Text, nombre, ventana, ahora) {
  if (!ventana) return linea(Text, nombre + ': sin lectura todavía (aparece tras el primer mensaje)', true)
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
  const por5 = tokensPorPunto(registros, limites.cinco, CINCO_HORAS)
  const por7 = tokensPorPunto(registros, limites.semana, SIETE_DIAS)
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
  const delta = p === null ? '' : ' · +' + String(p).replace('.', ',') + ' pts'
  return linea(Text, hora(r.t) + ' · ' + tokens(frescos(usoRegistro(r))) + delta + ' · ' + r.txt)
}

function vistaPrompts({ Text, Box, Button, redibujar, filas }) {
  const salida = []
  const base = registros.slice()
  const lista = orden === 'recientes' ? base.reverse() : base.sort((a, b) => frescos(usoRegistro(b)) - frescos(usoRegistro(a)))
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
    linea(Text, '   Proyecto: ' + (r.cwd || '—') + ' · ' + r.n + ' turnos · ' + Math.round(r.ms / 1000) + ' s'),
    linea(Text, '   Entrada ' + tokens(u[0]) + ' · Salida ' + tokens(u[1]) + ' · Caché leída ' + tokens(u[2]) + ' · Caché escrita ' + tokens(u[3])),
    linea(Text, '   Principal ' + tokens(frescos(sumarUso(u, r.sub.map((x) => -x)))) + ' nuevos · Subagentes ' + tokens(frescos(r.sub)) + ' nuevos (' + r.subN + ' turnos)'),
    linea(Text, '   Ventanas: 5 h ' + (p5 === null ? '—' : '+' + String(p5).replace('.', ',') + ' pts') + ' · semana ' + (p7 === null ? '—' : '+' + String(p7).replace('.', ',') + ' pts')),
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
  const caros = masCaros(registros, ahora - SIETE_DIAS, 5)
  if (!caros.length) salida.push(linea(Text, 'Sin datos todavía.', true))
  for (const c of caros) salida.push(linea(Text, fechaCorta(claveDia(c.reg.t)) + ' ' + hora(c.reg.t) + ' · ' + tokens(c.nuevos) + ' · ' + c.reg.txt))
  return salida
}
