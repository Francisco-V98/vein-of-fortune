// Tablero del equipo de Veta de Fortuna: /equipo abre un panel con el diagrama de traspasos de cada tarea
// (quién le pasa el trabajo a quién, qué entregó cada uno, qué hallazgos dejó y quién los resolvió),
// los especialistas que trabajan ahora y una bandeja con lo que te toca a ti: revisar, aprobar un PR o probar.
// Se actualiza solo. Solo lee archivos del repositorio y ejecuta `gh pr list`. Los botones de la bandeja
// envían un mensaje a la conversación como si lo escribieras tú, solo cuando los pulsas; no modifican archivos.

import { svgAhora, svgAvatar, svgFlujo, svgTraspasos } from './vis.js'

const PANE = 'vf-equipo'
const EQUIPO = 'studio/data/equipo.json'
const ROADMAP = 'studio/data/roadmap.json'
const DIR_DATOS = 'studio/data'
const DIR_TAREAS = 'studio/data/tasks'
const EN_MARCHA = ['sprint', 'doing', 'qa', 'review']
const SONDEO_MS = 3000
const PRS_MS = 45000

const GLIFO_ESTADO = { pendiente: '○', activa: '▶', hecha: '●', omitida: '–' }

// Estado del panel
let tab = 'flujo'
let equipo = null
let tareas = []
let hechas = 0
let agentes = []
let prs = []
let seleccion = ''
let acciones = {}
let firmaDatos = ''
let actualizado = ''
let error = ''

// ---------- lógica pura (se prueba sin sesión) ----------

// Etapas de una tarea. Si su archivo de actividad trae `pipeline`, manda; si no, se infiere del estado.
export function pipelineDe(estadoTarea, actividad, etapas) {
  const ids = etapas.map((e) => e.id)
  const explicito = actividad && actividad.pipeline && Array.isArray(actividad.pipeline.etapas) ? actividad.pipeline.etapas : null
  if (explicito) {
    return ids.map((id) => {
      const x = explicito.find((p) => p.etapa === id)
      return {
        etapa: id,
        estado: x ? x.estado : 'pendiente',
        nota: x ? x.nota || '' : '',
        at: x ? x.at || '' : '',
        entrega: x ? x.entrega || '' : '',
        por: x ? x.por || '' : '',
        hallazgos: x && Array.isArray(x.hallazgos) ? x.hallazgos : [],
        inferido: false,
      }
    })
  }
  const por = {
    backlog: { ideacion: 'pendiente', analisis: 'pendiente', produccion: 'pendiente', qa: 'pendiente', autor: 'pendiente', playtest: 'pendiente', cierre: 'pendiente' },
    sprint: { ideacion: 'omitida', analisis: 'omitida', produccion: 'pendiente', qa: 'pendiente', autor: 'pendiente', playtest: 'pendiente', cierre: 'pendiente' },
    doing: { ideacion: 'omitida', analisis: 'omitida', produccion: 'activa', qa: 'pendiente', autor: 'pendiente', playtest: 'pendiente', cierre: 'pendiente' },
    review: { ideacion: 'omitida', analisis: 'omitida', produccion: 'hecha', qa: 'hecha', autor: 'activa', playtest: 'pendiente', cierre: 'pendiente' },
    qa: { ideacion: 'omitida', analisis: 'omitida', produccion: 'hecha', qa: 'hecha', autor: 'hecha', playtest: 'activa', cierre: 'pendiente' },
    done: { ideacion: 'hecha', analisis: 'hecha', produccion: 'hecha', qa: 'hecha', autor: 'hecha', playtest: 'hecha', cierre: 'hecha' },
  }
  const mapa = por[estadoTarea] || por.backlog
  return ids.map((id) => ({ etapa: id, estado: mapa[id] || 'pendiente', nota: '', at: '', entrega: '', por: '', hallazgos: [], inferido: true }))
}

// La etapa en la que está la tarea: la activa, o si no la primera pendiente
export function etapaActual(pipeline) {
  const activa = pipeline.find((p) => p.estado === 'activa')
  if (activa) return activa.etapa
  const pendiente = pipeline.find((p) => p.estado === 'pendiente')
  return pendiente ? pendiente.etapa : 'cierre'
}

// Quién hace una etapa: el especialista de la tarea en Producción, o el rol fijo de la etapa
export function rolDe(etapa, actividad, etapas) {
  const def = etapas.find((e) => e.id === etapa)
  if (!def) return ''
  if (def.rol === 'especialista') {
    return actividad && actividad.pipeline && actividad.pipeline.especialista ? actividad.pipeline.especialista : 'disenador'
  }
  return def.rol
}

// Cuántas tareas hay en cada etapa
export function contarPorEtapa(lista) {
  const conteo = {}
  for (const t of lista) conteo[t.etapa] = (conteo[t.etapa] || 0) + 1
  return conteo
}

// Rol al que pertenece un subagente según su tipo
export function rolDeAgente(tipo, roles) {
  const r = roles.find((x) => x.agente && x.agente === tipo)
  return r ? r.id : ''
}

// El PR abierto cuya rama lleva el ID de la tarea, si hay
export function prDeTarea(id, lista) {
  return lista.find((p) => typeof p.headRefName === 'string' && (p.headRefName.includes('/' + id + '-') || p.headRefName.endsWith('/' + id))) || null
}

// Lo que le toca al autor: tareas en su etapa y PR abiertos que ninguna tarea cubre
export function accionesDelAutor(lista, listaPrs) {
  const items = []
  const cubiertos = new Set()
  for (const t of lista) {
    if (t.etapa !== 'autor' && t.etapa !== 'playtest') continue
    const pr = prDeTarea(t.id, listaPrs)
    if (pr) cubiertos.add(pr.number)
    items.push({ clave: t.id + ':' + t.etapa, id: t.id, titulo: t.titulo, tipo: t.etapa === 'autor' ? 'revisar' : 'probar', pr })
  }
  for (const pr of listaPrs) {
    if (cubiertos.has(pr.number)) continue
    items.push({ clave: 'pr-' + pr.number, id: 'PR #' + pr.number, titulo: pr.title, tipo: 'pr', pr })
  }
  return items
}

// El mensaje que se envía cuando el autor termina su parte
export function mensajeAutor(accion, decision) {
  const que = accion.tipo === 'pr' ? 'el ' + accion.id : 'la tarea ' + accion.id + ' (' + accion.titulo + ')'
  if (decision === 'aprobado') {
    if (accion.tipo === 'pr') return 'Terminé mi parte en ' + que + ': lo revisé y lo apruebo. Puedes fusionarlo.'
    if (accion.tipo === 'probar') return 'Terminé mi parte en ' + que + ': la probé y todo está bien. Ciérrala y sigue con el flujo.'
    return 'Terminé mi parte en ' + que + ': revisé el entregable y está aprobado. Pásala a la siguiente etapa del flujo.'
  }
  return (
    'Terminé mi parte en ' + que + ': dejé ajustes en el chat, en mis comentarios de arriba. Revísalos, decide qué especialista los resuelve y devuelve el trabajo a la etapa que corresponda; ' +
    'cuando esté listo vuelvo a revisar.'
  )
}

// Firma de los archivos que importan: cambia cuando alguien edita el roadmap, el equipo o una tarea
export function firmaDe(archivosDatos, archivosTareas) {
  const interesa = archivosDatos.filter((a) => a.name === 'roadmap.json' || a.name === 'equipo.json')
  return interesa
    .concat(archivosTareas)
    .map((a) => a.name + ':' + a.size)
    .sort()
    .join('|')
}

// ---------- lectura de datos ----------

async function leerJson($, ruta) {
  try {
    return JSON.parse(await $.fs.read(ruta))
  } catch (e) {
    return null
  }
}

function elegirSeleccion() {
  if (seleccion && tareas.find((t) => t.id === seleccion)) return
  const trabajando = tareas.find((t) => t.etapa !== 'autor' && t.etapa !== 'playtest' && t.etapa !== 'cierre')
  seleccion = trabajando ? trabajando.id : tareas.length ? tareas[0].id : ''
}

async function cargar($) {
  error = ''
  const eq = await leerJson($, EQUIPO)
  if (!eq) {
    error = 'No se pudo leer ' + EQUIPO
    $.ui.invalidate('ui.render')
    return
  }
  equipo = eq
  const roadmap = await leerJson($, ROADMAP)
  const lista = []
  hechas = 0
  if (roadmap) {
    for (const fase of roadmap.phases || []) {
      for (const hito of fase.milestones || []) {
        for (const t of hito.tasks || []) {
          if (t.status === 'done') hechas += 1
          if (!EN_MARCHA.includes(t.status)) continue
          const actividad = await leerJson($, DIR_TAREAS + '/' + t.id + '.json')
          const pipeline = pipelineDe(t.status, actividad, equipo.etapas)
          const etapa = etapaActual(pipeline)
          const especialista = actividad && actividad.pipeline && actividad.pipeline.especialista ? actividad.pipeline.especialista : ''
          lista.push({ id: t.id, titulo: t.title, estado: t.status, pipeline, etapa, rol: rolDe(etapa, actividad, equipo.etapas), especialista, hito: hito.id })
        }
      }
    }
  } else {
    error = 'No se pudo leer ' + ROADMAP
  }
  tareas = lista
  elegirSeleccion()
  const ahora = new Date()
  actualizado = String(ahora.getHours()).padStart(2, '0') + ':' + String(ahora.getMinutes()).padStart(2, '0') + ':' + String(ahora.getSeconds()).padStart(2, '0')
  $.ui.invalidate('ui.render')
}

// Mira si cambió algo en los datos y, solo entonces, los vuelve a cargar
async function sondear($) {
  try {
    const datos = await $.fs.list(DIR_DATOS)
    const tareasDir = await $.fs.list(DIR_TAREAS)
    const firma = firmaDe(datos, tareasDir)
    if (firma !== firmaDatos) {
      firmaDatos = firma
      await cargar($)
    }
  } catch (e) {
    error = 'No se pudo vigilar los datos'
  }
}

async function refrescarAgentes($) {
  try {
    const lista = await $.agent.list()
    const firma = JSON.stringify(lista.map((a) => [a.id, a.type, a.status]))
    if (firma !== JSON.stringify(agentes.map((a) => [a.id, a.type, a.status]))) {
      agentes = lista
      $.ui.invalidate('ui.render')
    }
  } catch (e) {
    agentes = []
  }
}

async function cargarPrs($) {
  try {
    const r = await $.process.run(['gh', 'pr', 'list', '--json', 'number,title,headRefName,url', '--limit', '30'], { timeoutMs: 20000 })
    const lista = r.exitCode === 0 ? JSON.parse(r.stdout) : []
    if (JSON.stringify(lista) !== JSON.stringify(prs)) {
      prs = lista
      $.ui.invalidate('ui.render')
    }
  } catch (e) {
    prs = []
  }
}

// Guarda lo que el autor decidió en cada acción, para que sobreviva a un reinicio
async function guardarAccion($, clave, valor) {
  acciones = { ...acciones, [clave]: valor }
  $.ui.invalidate('ui.render')
  try {
    await $.store.set('acciones', acciones)
  } catch (e) {
    error = 'No se pudo guardar tu decisión'
  }
}

function nombreRol(id) {
  if (!equipo) return id
  const r = equipo.roles.find((x) => x.id === id)
  return r ? r.nombre : id
}

function indiceRol(id) {
  if (!equipo) return 0
  const i = equipo.roles.findIndex((x) => x.id === id)
  return i < 0 ? 0 : i
}

function nombreEtapa(id) {
  if (!equipo) return id
  const e = equipo.etapas.find((x) => x.id === id)
  return e ? e.nombre : id
}

// ---------- el mod ----------

export function register(on) {
  on('session.start', async ($, e, next) => {
    try {
      const guardadas = await $.store.get('acciones')
      if (guardadas && typeof guardadas === 'object') acciones = guardadas
    } catch (err) {
      acciones = {}
    }
    // Se actualiza solo: mira los datos y los especialistas cada pocos segundos, y los PR cada rato
    $.clock.every(SONDEO_MS, () => sondear($))
    $.clock.every(SONDEO_MS, () => refrescarAgentes($))
    $.clock.every(PRS_MS, () => cargarPrs($))
    await $.command.register({
      name: 'equipo',
      description: 'Tablero del equipo: traspasos, hallazgos y lo que te toca a ti',
      immediate: true,
    })
    return next(e)
  })

  // Al terminar cada turno el trabajo suele haber cambiado: se actualiza sin esperar al sondeo
  on('turn.complete', async ($, e, next) => {
    sondear($)
    refrescarAgentes($)
    return next(e)
  })

  on('command.run', { command: 'equipo' }, async ($) => {
    await $.ui.open({ id: PANE, title: 'Equipo', focus: true, closeOnEscape: true })
    sondear($)
    refrescarAgentes($)
    cargarPrs($)
    return {}
  })

  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    if (e.requestId !== PANE) return next(e)
    const { Box, Text, Button, Svg, Link } = $.ui.resolve(e)
    const redibujar = () => $.ui.invalidate('ui.render')
    const escritorio = e.surface === 'desktop'
    const ancho = Math.max(320, Math.min(600, Math.round((e.props && e.props.bodyColumns ? e.props.bodyColumns : 60) * 9)))
    const ctx = { Box, Text, Button, Svg, Link, escritorio, ancho }

    const pestana = (nombre, etiqueta, tecla) =>
      Button({
        key: 'tab-' + nombre,
        label: etiqueta,
        hotkey: tecla,
        plain: true,
        dimColor: tab !== nombre,
        onPress: () => {
          tab = nombre
          redibujar()
        },
      })

    const cabecera = Box({
      flexDirection: 'row',
      columnGap: 3,
      children: [pestana('flujo', 'Flujo', '1'), pestana('equipo', 'Equipo', '2'), Text({ dimColor: true, children: [actualizado ? 'se actualiza solo · ' + actualizado : 'cargando…'] })],
    })

    const filas = []
    if (error) filas.push(Text({ color: 'yellow', children: [error] }))
    if (!equipo) {
      filas.push(Text({ dimColor: true, children: ['Cargando el equipo…'] }))
    } else if (tab === 'flujo') {
      filas.push(
        ...vistaFlujo(ctx, {
          elegir: (id) => {
            seleccion = id
            redibujar()
          },
          decidir: (clave, valor) => guardarAccion($, clave, valor),
          enviar: async (accion, decision) => {
            await guardarAccion($, accion.clave, { decision, enviado: true })
            await $.prompt.submit({ text: mensajeAutor(accion, decision), asUser: true })
          },
        }),
      )
    } else {
      filas.push(...vistaEquipo(ctx))
    }

    return Box({ flexDirection: 'column', children: [cabecera, Text({ children: [' '] }), ...filas] })
  })
}

// ---------- vistas ----------

function titulo(Text, texto) {
  return Text({ bold: true, color: 'cyan', children: [texto] })
}

function etapasHumanas() {
  return equipo.etapas.filter((e) => equipo.roles.some((r) => r.id === e.rol && r.tipo === 'humano')).map((e) => e.id)
}

function vistaFlujo(ctx, acc) {
  const { Text, Box, Button, Svg, escritorio, ancho } = ctx
  const filas = []
  const conteo = contarPorEtapa(tareas)

  // 1. Lo que te toca a ti
  filas.push(titulo(Text, 'Te toca a ti'))
  const items = accionesDelAutor(tareas, prs)
  if (items.length === 0) filas.push(Text({ dimColor: true, children: ['Nada pendiente de ti. ✓'] }))
  for (const item of items) filas.push(tarjetaAccion(ctx, item, acciones[item.clave], acc))
  filas.push(Text({ children: [' '] }))

  // 2. El flujo en una mirada
  if (escritorio) {
    filas.push(Svg({ alt: 'Flujo de las tareas por etapa', width: Math.min(ancho, 600), height: 128, source: svgFlujo(equipo.etapas, conteo, etapasHumanas(), ancho) }))
  } else {
    filas.push(Text({ bold: true, children: [equipo.etapas.map((s) => s.glifo + ' ' + (conteo[s.id] || 0)).join('  →  ')] }))
  }
  filas.push(Text({ dimColor: true, children: ['Hechas ' + hechas + ' · en marcha ' + tareas.length + (escritorio ? ' · el aro punteado marca dónde participas tú' : '')] }))
  filas.push(Text({ children: [' '] }))

  // 3. Quién trabaja ahora
  const vivos = agentes
    .filter((a) => a.status === 'running' || a.status === 'waiting')
    .map((a) => {
      const rol = rolDeAgente(a.type, equipo.roles)
      return { nombre: rol ? nombreRol(rol) : a.type, detalle: a.description || '' }
    })
  filas.push(titulo(Text, 'Ahora trabajando'))
  if (escritorio) {
    filas.push(Svg({ alt: 'Especialistas activos', width: Math.min(ancho, 600), height: Math.max(40, 12 + vivos.length * 26), source: svgAhora(vivos, ancho) }))
  } else if (vivos.length === 0) {
    filas.push(Text({ dimColor: true, children: ['Nadie trabaja ahora en esta sesión.'] }))
  } else {
    for (const v of vivos) filas.push(Text({ children: ['● ' + v.nombre + (v.detalle ? ' · ' + v.detalle : '')] }))
  }
  filas.push(Text({ children: [' '] }))

  // 4. Diagrama de traspasos de la tarea elegida
  filas.push(titulo(Text, 'Traspasos de la tarea'))
  if (tareas.length === 0) {
    filas.push(Text({ dimColor: true, children: ['No hay tareas en marcha.'] }))
    return filas
  }
  filas.push(
    Box({
      flexDirection: 'row',
      flexWrap: 'wrap',
      columnGap: 2,
      children: tareas.map((t) => {
        const def = equipo.etapas.find((e) => e.id === t.etapa)
        return Button({
          key: 'sel-' + t.id,
          label: t.id + ' ' + (def ? def.glifo : ''),
          plain: true,
          dimColor: t.id !== seleccion,
          onPress: () => acc.elegir(t.id),
        })
      }),
    }),
  )
  const t = tareas.find((x) => x.id === seleccion) || tareas[0]
  const conEspecialista = t.especialista ? { pipeline: { especialista: t.especialista } } : null
  filas.push(Text({ bold: true, wrap: 'wrap', children: [t.id + ' · ' + t.titulo] }))
  const pr = prDeTarea(t.id, prs)
  filas.push(Text({ dimColor: true, children: ['Estado ' + t.estado + ' · hito ' + t.hito + ' · ahora: ' + nombreEtapa(t.etapa) + ' (' + nombreRol(t.rol) + ')' + (pr ? ' · PR #' + pr.number : '')] }))
  filas.push(Text({ children: [' '] }))
  const lineas = t.pipeline.map((p, i) => {
    const rolId = p.por || rolDe(p.etapa, conEspecialista, equipo.etapas)
    const sig = t.pipeline[i + 1]
    return {
      nombre: nombreEtapa(p.etapa),
      quien: nombreRol(rolId),
      indice: indiceRol(rolId),
      estado: p.estado,
      nota: p.inferido ? '' : p.nota,
      entrega: p.entrega,
      hallazgos: (p.hallazgos || []).map((h) => ({ ...h, de: nombreRol(h.de), resuelto_por: nombreRol(h.resuelto_por) })),
      siguiente: sig ? nombreEtapa(sig.etapa) : '',
    }
  })
  if (escritorio) {
    const d = svgTraspasos(lineas, ancho)
    filas.push(Svg({ alt: 'Diagrama de traspasos de la tarea', width: d.ancho, height: d.alto, source: d.svg }))
  } else {
    for (const l of lineas) {
      filas.push(Text({ bold: l.estado === 'activa', dimColor: l.estado === 'omitida' || l.estado === 'pendiente', wrap: 'wrap', children: [GLIFO_ESTADO[l.estado] + ' ' + l.nombre + ' · ' + l.quien + (l.nota ? ' — ' + l.nota : '')] }))
      if (l.entrega) filas.push(Text({ dimColor: true, wrap: 'wrap', children: ['    Entrega: ' + l.entrega] }))
      for (const h of l.hallazgos) {
        filas.push(Text({ color: h.estado === 'resuelto' ? undefined : 'yellow', wrap: 'wrap', children: ['    ' + (h.estado === 'resuelto' ? '✓' : '⚑') + ' ' + h.de + ': ' + h.texto]}))
        if (h.estado === 'resuelto' && h.como) filas.push(Text({ dimColor: true, wrap: 'wrap', children: ['      Lo resolvió ' + h.resuelto_por + ': ' + h.como] }))
      }
    }
  }
  return filas
}

// Tarjeta de una acción del autor, con el recorrido: empezar → aprobado o ajustes → terminé mi parte
function tarjetaAccion(ctx, item, estado, acc) {
  const { Text, Box, Button, Link } = ctx
  const decision = estado && estado.decision ? estado.decision : ''
  const enviado = Boolean(estado && estado.enviado)
  const etiqueta = item.tipo === 'pr' ? 'Revisar PR' : item.tipo === 'probar' ? 'Probar el juego' : 'Revisar entregable'
  const hijos = [
    Box({
      flexDirection: 'row',
      columnGap: 2,
      children: [Text({ bold: true, backgroundColor: 'yellow', color: 'black', children: [' ' + etiqueta + ' ']}), Text({ bold: true, children: [item.id] })],
    }),
    Text({ wrap: 'wrap', children: [item.titulo] }),
  ]
  if (item.pr && item.pr.url) hijos.push(Link({ href: item.pr.url, label: 'Abrir el PR #' + item.pr.number }))

  if (enviado) {
    hijos.push(Text({ dimColor: true, wrap: 'wrap', children: ['Enviado (' + (decision === 'aprobado' ? 'aprobado' : 'con ajustes') + '). Esperando al coordinador…'] }))
    hijos.push(Button({ key: 'deshacer-' + item.clave, label: 'Deshacer', plain: true, hotkey: 'z', onPress: () => acc.decidir(item.clave, {}) }))
  } else if (!decision) {
    hijos.push(Text({ dimColor: true, children: ['1) Haz tu revisión. 2) Dime cómo salió.'] }))
    hijos.push(
      Box({
        flexDirection: 'row',
        columnGap: 2,
        children: [
          Button({ key: 'ok-' + item.clave, label: 'Todo bien', hotkey: 'a', onPress: () => acc.decidir(item.clave, { decision: 'aprobado' }) }),
          Button({ key: 'aj-' + item.clave, label: 'Salieron ajustes', hotkey: 'j', onPress: () => acc.decidir(item.clave, { decision: 'ajustes' }) }),
        ],
      }),
    )
  } else {
    hijos.push(
      Text({
        color: decision === 'aprobado' ? undefined : 'yellow',
        wrap: 'wrap',
        children: [decision === 'aprobado' ? 'Marcado como aprobado. Cuando quieras, pulsa «Terminé mi parte» para que siga el flujo.' : 'Cuéntame los ajustes en el chat. Cuando termines de escribirlos, pulsa «Terminé mi parte».'],
      }),
    )
    hijos.push(
      Box({
        flexDirection: 'row',
        columnGap: 2,
        children: [
          Button({ key: 'fin-' + item.clave, label: 'Terminé mi parte', hotkey: 't', onPress: () => acc.enviar(item, decision) }),
          Button({ key: 'cambiar-' + item.clave, label: 'Cambiar', plain: true, onPress: () => acc.decidir(item.clave, {}) }),
        ],
      }),
    )
  }
  return Box({ flexDirection: 'column', borderStyle: 'round', paddingX: 1, marginBottom: 1, children: hijos })
}

function vistaEquipo(ctx) {
  const { Text, Box, Svg, escritorio } = ctx
  const filas = []
  equipo.roles.forEach((rol, i) => {
    const suyas = tareas.filter((t) => t.rol === rol.id)
    const vivo = Boolean(rol.agente) && agentes.some((a) => a.type === rol.agente && (a.status === 'running' || a.status === 'waiting'))
    const cuerpo = [
      Box({ flexDirection: 'row', columnGap: 1, children: [Text({ bold: true, children: [rol.nombre] }), Text({ dimColor: true, children: ['· ' + rol.tipo] })] }),
      Text({ wrap: 'wrap', children: [rol.hace] }),
      Text({ dimColor: true, wrap: 'wrap', children: ['Entrega: ' + rol.entrega] }),
    ]
    if (suyas.length) cuerpo.push(Text({ color: 'yellow', children: ['Ahora: ' + suyas.map((t) => t.id).join(', ')] }))
    const avatar = escritorio ? Svg({ alt: rol.nombre, width: 48, height: 48, source: svgAvatar(rol.nombre, i, vivo || suyas.length > 0, rol.tipo === 'humano') }) : Text({ bold: true, children: [(vivo ? '●' : '○') + ' '] })
    filas.push(Box({ flexDirection: 'row', columnGap: 2, borderStyle: 'round', paddingX: 1, marginBottom: 1, children: [avatar, Box({ flexDirection: 'column', flexShrink: 1, children: cuerpo })] }))
  })
  return filas
}
