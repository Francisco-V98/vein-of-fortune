// Tablero del equipo de Veta de Fortuna: /equipo abre un panel que muestra en qué etapa va cada
// tarea (ideación, análisis, producción, QA, revisión del autor y cierre), qué especialistas
// trabajan ahora y los botones con los que el autor aprueba o devuelve una tarea.
// Solo lee archivos del repositorio. Los botones del autor envían un mensaje como si lo escribiera
// el autor; no modifican ningún archivo por su cuenta.

const PANE = 'vf-equipo'
const EQUIPO = 'studio/data/equipo.json'
const ROADMAP = 'studio/data/roadmap.json'
const TAREAS = 'studio/data/tasks/'
const EN_MARCHA = ['sprint', 'doing', 'qa', 'review']

const GLIFO_ESTADO = { pendiente: '○', activa: '▶', hecha: '●', omitida: '–' }

// Estado del panel
let tab = 'flujo'
let equipo = null
let tareas = []
let hechas = 0
let agentes = []
let seleccion = ''
let cargando = false
let error = ''

// ---------- lógica pura (se prueba sin sesión) ----------

// Etapas de una tarea. Si su archivo de actividad trae `pipeline`, manda; si no, se infiere del estado.
export function pipelineDe(estadoTarea, actividad, etapas) {
  const ids = etapas.map((e) => e.id)
  const explicito = actividad && actividad.pipeline && Array.isArray(actividad.pipeline.etapas) ? actividad.pipeline.etapas : null
  if (explicito) {
    return ids.map((id) => {
      const x = explicito.find((p) => p.etapa === id)
      return { etapa: id, estado: x ? x.estado : 'pendiente', nota: x ? x.nota || '' : '', at: x ? x.at || '' : '', inferido: false }
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
  return ids.map((id) => ({ etapa: id, estado: mapa[id] || 'pendiente', nota: 'Inferido del estado de la tarea', at: '', inferido: true }))
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

// Dibujo del flujo para la app de escritorio: seis nodos unidos por flechas
export function svgFlujo(etapas, conteo, actual, ancho) {
  const w = Math.max(360, Math.min(ancho, 640))
  const h = 110
  const paso = w / etapas.length
  const partes = []
  partes.push('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + w + ' ' + h + '" width="' + w + '" height="' + h + '">')
  partes.push('<rect width="' + w + '" height="' + h + '" rx="10" fill="#17232C"/>')
  etapas.forEach((e, i) => {
    const cx = Math.round(paso * i + paso / 2)
    if (i < etapas.length - 1) {
      partes.push('<line x1="' + (cx + 22) + '" y1="44" x2="' + (cx + paso - 22) + '" y2="44" stroke="#5B7C8C" stroke-width="2"/>')
      partes.push('<polygon points="' + (cx + paso - 22) + ',39 ' + (cx + paso - 14) + ',44 ' + (cx + paso - 22) + ',49" fill="#5B7C8C"/>')
    }
    const n = conteo[e.id] || 0
    const activo = e.id === actual || n > 0
    partes.push('<circle cx="' + cx + '" cy="44" r="22" fill="' + (activo ? '#9A2640' : '#22333F') + '" stroke="' + (activo ? '#E3B25C' : '#36505F') + '" stroke-width="3"/>')
    partes.push('<text x="' + cx + '" y="51" text-anchor="middle" font-family="monospace" font-size="20" font-weight="bold" fill="#C9DCDF">' + e.glifo + '</text>')
    if (n > 0) {
      partes.push('<circle cx="' + (cx + 18) + '" cy="24" r="10" fill="#E3B25C"/>')
      partes.push('<text x="' + (cx + 18) + '" y="28" text-anchor="middle" font-family="monospace" font-size="12" font-weight="bold" fill="#17232C">' + n + '</text>')
    }
    partes.push('<text x="' + cx + '" y="88" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#8FB0BA">' + e.nombre.replace('Revisión del autor', 'Revisión').replace('Prueba del autor', 'Prueba') + '</text>')
  })
  partes.push('</svg>')
  return partes.join('')
}

// ---------- lectura de datos ----------

async function leerJson($, ruta) {
  try {
    return JSON.parse(await $.fs.read(ruta))
  } catch (e) {
    return null
  }
}

async function cargar($) {
  cargando = true
  error = ''
  $.ui.invalidate('ui.render')
  const eq = await leerJson($, EQUIPO)
  if (!eq) {
    error = 'No se pudo leer ' + EQUIPO
    cargando = false
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
          const actividad = await leerJson($, TAREAS + t.id + '.json')
          const pipeline = pipelineDe(t.status, actividad, equipo.etapas)
          const etapa = etapaActual(pipeline)
          lista.push({
            id: t.id,
            titulo: t.title,
            estado: t.status,
            pipeline,
            etapa,
            rol: rolDe(etapa, actividad, equipo.etapas),
            especialista: actividad && actividad.pipeline && actividad.pipeline.especialista ? actividad.pipeline.especialista : '',
            hito: hito.id,
          })
        }
      }
    }
  } else {
    error = 'No se pudo leer ' + ROADMAP
  }
  tareas = lista
  if (!seleccion || !tareas.find((t) => t.id === seleccion)) seleccion = tareas.length ? tareas[0].id : ''
  cargando = false
  $.ui.invalidate('ui.render')
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

function nombreRol(id) {
  if (!equipo) return id
  const r = equipo.roles.find((x) => x.id === id)
  return r ? r.nombre : id
}

function nombreEtapa(id) {
  if (!equipo) return id
  const e = equipo.etapas.find((x) => x.id === id)
  return e ? e.nombre : id
}

// ---------- el mod ----------

export function register(on) {
  on('session.start', async ($, e, next) => {
    $.clock.every(30000, () => cargar($))
    $.clock.every(4000, () => refrescarAgentes($))
    await $.command.register({
      name: 'equipo',
      description: 'Tablero del equipo: en qué etapa va cada tarea y quién trabaja ahora',
      immediate: true,
    })
    return next(e)
  })

  on('command.run', { command: 'equipo' }, async ($) => {
    await $.ui.open({ id: PANE, title: 'Equipo', focus: true, closeOnEscape: true })
    cargar($)
    refrescarAgentes($)
    return {}
  })

  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    if (e.requestId !== PANE) return next(e)
    const { Box, Text, Button, Input, Select, Svg } = $.ui.resolve(e)
    const redibujar = () => $.ui.invalidate('ui.render')

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
      children: [
        pestana('flujo', 'Flujo', '1'),
        pestana('equipo', 'Equipo', '2'),
        pestana('tarea', 'Tarea', '3'),
        Button({ key: 'actualizar', label: cargando ? 'Actualizando…' : 'Actualizar', hotkey: 'r', plain: true, onPress: () => cargar($) }),
      ],
    })

    const filas = []
    if (error) filas.push(Text({ color: 'yellow', children: [error] }))
    if (!equipo) {
      filas.push(Text({ dimColor: true, children: [cargando ? 'Cargando el equipo…' : 'Sin datos todavía.'] }))
    } else if (tab === 'flujo') {
      filas.push(...vistaFlujo({ Text, Svg }, e))
    } else if (tab === 'equipo') {
      filas.push(...vistaEquipo({ Text }))
    } else {
      filas.push(
        ...vistaTarea({ Text, Box, Button, Input, Select }, {
          elegir: (valor) => {
            seleccion = valor
            redibujar()
          },
          aprobar: (t) =>
            $.prompt.submit({
              text: t.etapa === 'autor'
                ? 'Apruebo la revisión de la tarea ' + t.id + ' (' + t.titulo + '). Pásala a la siguiente etapa del flujo.'
                : 'Aprobé la prueba de la tarea ' + t.id + ' (' + t.titulo + '). Ciérrala como hecha y sigue con lo que toca.',
              asUser: true,
            }),
          devolver: (t, comentario) =>
            $.prompt.submit({ text: 'Devuelvo la tarea ' + t.id + ' (' + t.titulo + ') a producción con este comentario: ' + comentario, asUser: true }),
        }),
      )
    }

    return Box({ flexDirection: 'column', children: [cabecera, Text({ children: [' '] }), ...filas] })
  })
}

// ---------- vistas ----------

function vistaFlujo({ Text, Svg }, e) {
  const filas = []
  const conteo = contarPorEtapa(tareas)
  const ancho = Math.round((e.props && e.props.bodyColumns ? e.props.bodyColumns : 60) * 8)
  if (e.surface === 'desktop') {
    filas.push(Svg({ alt: 'Flujo de las tareas por etapa', width: Math.max(360, Math.min(ancho, 640)), height: 110, source: svgFlujo(equipo.etapas, conteo, '', ancho) }))
  } else {
    filas.push(Text({ bold: true, children: [equipo.etapas.map((s) => s.glifo + ' ' + (conteo[s.id] || 0)).join('  →  ')] }))
  }
  filas.push(Text({ dimColor: true, children: ['Hechas: ' + hechas + ' · en marcha: ' + tareas.length] }))
  filas.push(Text({ children: [' '] }))

  const vivos = agentes.filter((a) => a.status === 'running' || a.status === 'waiting')
  filas.push(Text({ bold: true, children: ['Ahora trabajando'] }))
  if (vivos.length === 0) filas.push(Text({ dimColor: true, children: ['Ningún especialista activo en esta sesión.'] }))
  for (const a of vivos) {
    const rol = rolDeAgente(a.type, equipo.roles)
    filas.push(Text({ children: ['● ' + (rol ? nombreRol(rol) : a.type) + (a.description ? ' · ' + a.description : '')] }))
  }
  filas.push(Text({ children: [' '] }))

  for (const etapa of equipo.etapas) {
    const aqui = tareas.filter((t) => t.etapa === etapa.id)
    filas.push(Text({ bold: true, color: aqui.length ? 'yellow' : undefined, dimColor: aqui.length === 0, children: [etapa.glifo + ' ' + etapa.nombre + ' (' + aqui.length + ')'] }))
    for (const t of aqui) {
      filas.push(Text({ children: ['  ' + t.id + ' · ' + nombreRol(t.rol)] }))
      filas.push(Text({ dimColor: true, children: ['    ' + t.titulo] }))
    }
  }
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, children: ['Reglas del flujo'] }))
  for (const r of equipo.reglas) filas.push(Text({ dimColor: true, children: ['· ' + r] }))
  return filas
}

function vistaEquipo({ Text }) {
  const filas = []
  for (const rol of equipo.roles) {
    const suyas = tareas.filter((t) => t.rol === rol.id)
    const vivo = rol.agente && agentes.some((a) => a.type === rol.agente && (a.status === 'running' || a.status === 'waiting'))
    filas.push(Text({ bold: true, children: [(vivo ? '● ' : '○ ') + rol.nombre + '  [' + rol.tipo + ']'] }))
    filas.push(Text({ children: ['  ' + rol.hace] }))
    filas.push(Text({ dimColor: true, children: ['  Entrega: ' + rol.entrega] }))
    if (suyas.length) filas.push(Text({ color: 'yellow', children: ['  Ahora: ' + suyas.map((t) => t.id).join(', ')] }))
    filas.push(Text({ children: [' '] }))
  }
  return filas
}

function vistaTarea({ Text, Box, Button, Input, Select }, acciones) {
  const filas = []
  if (tareas.length === 0) return [Text({ dimColor: true, children: ['No hay tareas en marcha.'] })]
  filas.push(
    Select({
      key: 'tarea',
      label: 'Tarea',
      value: seleccion,
      options: tareas.map((t) => ({ value: t.id, label: t.id + ' · ' + t.titulo.slice(0, 40) })),
      onSelect: acciones.elegir,
    }),
  )
  const t = tareas.find((x) => x.id === seleccion) || tareas[0]
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, children: [t.id + ' · ' + t.titulo] }))
  filas.push(Text({ dimColor: true, children: ['Estado: ' + t.estado + ' · hito ' + t.hito] }))
  filas.push(Text({ children: [' '] }))
  for (const p of t.pipeline) {
    const quien = nombreRol(rolDe(p.etapa, t.especialista ? { pipeline: { especialista: t.especialista } } : null, equipo.etapas))
    filas.push(Text({ bold: p.estado === 'activa', dimColor: p.estado === 'omitida' || p.estado === 'pendiente', children: [GLIFO_ESTADO[p.estado] + ' ' + nombreEtapa(p.etapa).padEnd(20) + quien] }))
    if (p.nota && !p.inferido) filas.push(Text({ dimColor: true, children: ['    ' + p.nota + (p.at ? ' (' + p.at + ')' : '')] }))
  }
  if (t.etapa === 'autor' || t.etapa === 'playtest') {
    filas.push(Text({ children: [' '] }))
    filas.push(Text({ bold: true, color: 'yellow', children: [t.etapa === 'autor' ? 'Te toca revisar esta tarea' : 'Te toca jugar y probar esta tarea'] }))
    filas.push(Button({ key: 'aprobar', label: t.etapa === 'autor' ? 'Aprobar revisión' : 'Aprobar prueba', hotkey: 'a', onPress: () => acciones.aprobar(t) }))
    filas.push(
      Input({
        key: 'devolver',
        label: 'Devolver',
        placeholder: 'Escribe qué cambiar y pulsa Enter',
        value: '',
        submitLabel: 'devolver',
        onSubmit: (texto) => {
          if (texto.trim()) acciones.devolver(t, texto.trim())
        },
      }),
    )
  }
  return filas
}
