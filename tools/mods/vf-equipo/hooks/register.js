// Tablero del equipo de Veta de Fortuna: /equipo abre un panel que muestra en qué etapa va cada
// tarea (ideación, análisis, producción, QA, revisión del autor y cierre), qué especialistas
// trabajan ahora y los botones con los que el autor aprueba o devuelve una tarea.
// Solo lee archivos del repositorio. Los botones del autor envían un mensaje como si lo escribiera
// el autor; no modifican ningún archivo por su cuenta.

import { svgAhora, svgAvatar, svgFlujo, svgLinea } from './vis.js'

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
    const escritorio = e.surface === 'desktop'
    const ancho = Math.max(320, Math.min(600, Math.round((e.props && e.props.bodyColumns ? e.props.bodyColumns : 60) * 9)))

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
      filas.push(...vistaFlujo({ Text, Box, Svg, escritorio, ancho }))
    } else if (tab === 'equipo') {
      filas.push(...vistaEquipo({ Text, Box, Svg, escritorio }))
    } else {
      filas.push(
        ...vistaTarea({ Text, Box, Button, Input, Select, Svg, escritorio, ancho }, {
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

function etapasHumanas() {
  return equipo.etapas.filter((e) => equipo.roles.some((r) => r.id === e.rol && r.tipo === 'humano')).map((e) => e.id)
}

function titulo(Text, texto) {
  return Text({ bold: true, color: 'cyan', children: [texto] })
}

function vistaFlujo({ Text, Box, Svg, escritorio, ancho }) {
  const filas = []
  const conteo = contarPorEtapa(tareas)
  const vivos = agentes
    .filter((a) => a.status === 'running' || a.status === 'waiting')
    .map((a) => {
      const rol = rolDeAgente(a.type, equipo.roles)
      return { nombre: rol ? nombreRol(rol) : a.type, detalle: a.description || '' }
    })

  if (escritorio) {
    filas.push(Svg({ alt: 'Flujo de las tareas por etapa', width: Math.min(ancho, 600), height: 128, source: svgFlujo(equipo.etapas, conteo, etapasHumanas(), ancho) }))
  } else {
    filas.push(Text({ bold: true, children: [equipo.etapas.map((s) => s.glifo + ' ' + (conteo[s.id] || 0)).join('  →  ')] }))
  }
  filas.push(Text({ dimColor: true, children: ['Hechas ' + hechas + ' · en marcha ' + tareas.length + (escritorio ? ' · el aro punteado marca dónde participas tú' : '')] }))
  filas.push(Text({ children: [' '] }))

  filas.push(titulo(Text, 'Ahora trabajando'))
  if (escritorio) {
    filas.push(Svg({ alt: 'Especialistas activos', width: Math.min(ancho, 600), height: Math.max(40, 12 + vivos.length * 26), source: svgAhora(vivos, ancho) }))
  } else if (vivos.length === 0) {
    filas.push(Text({ dimColor: true, children: ['Nadie trabaja ahora en esta sesión.'] }))
  } else {
    for (const v of vivos) filas.push(Text({ children: ['● ' + v.nombre + (v.detalle ? ' · ' + v.detalle : '')] }))
  }
  filas.push(Text({ children: [' '] }))

  filas.push(titulo(Text, 'Tareas por etapa'))
  const vacias = []
  for (const etapa of equipo.etapas) {
    const aqui = tareas.filter((t) => t.etapa === etapa.id)
    if (aqui.length === 0) {
      vacias.push(etapa.nombre)
      continue
    }
    filas.push(
      Box({
        flexDirection: 'column',
        borderStyle: 'round',
        paddingX: 1,
        marginBottom: 1,
        children: [
          Text({ bold: true, color: 'yellow', children: [etapa.glifo + '  ' + etapa.nombre + '  ·  ' + aqui.length]}),
          ...aqui.flatMap((t) => [
            Box({ flexDirection: 'row', columnGap: 2, children: [Text({ bold: true, children: [t.id] }), Text({ dimColor: true, children: [nombreRol(t.rol)] })] }),
            Text({ wrap: 'wrap', children: [t.titulo] }),
          ]),
        ],
      }),
    )
  }
  if (vacias.length) filas.push(Text({ dimColor: true, wrap: 'wrap', children: ['Sin tareas en: ' + vacias.join(', ')] }))
  filas.push(Text({ children: [' '] }))
  filas.push(titulo(Text, 'Reglas del flujo'))
  for (const r of equipo.reglas) filas.push(Text({ dimColor: true, wrap: 'wrap', children: ['· ' + r] }))
  return filas
}

function vistaEquipo({ Text, Box, Svg, escritorio }) {
  const filas = []
  equipo.roles.forEach((rol, i) => {
    const suyas = tareas.filter((t) => t.rol === rol.id)
    const vivo = Boolean(rol.agente) && agentes.some((a) => a.type === rol.agente && (a.status === 'running' || a.status === 'waiting'))
    const cuerpo = [
      Box({
        flexDirection: 'row',
        columnGap: 1,
        children: [Text({ bold: true, children: [rol.nombre] }), Text({ dimColor: true, children: ['· ' + rol.tipo] })],
      }),
      Text({ wrap: 'wrap', children: [rol.hace] }),
      Text({ dimColor: true, wrap: 'wrap', children: ['Entrega: ' + rol.entrega] }),
    ]
    if (suyas.length) cuerpo.push(Text({ color: 'yellow', children: ['Ahora: ' + suyas.map((t) => t.id).join(', ')] }))
    const avatar = escritorio
      ? Svg({ alt: rol.nombre, width: 48, height: 48, source: svgAvatar(rol.nombre, i, vivo || suyas.length > 0, rol.tipo === 'humano') })
      : Text({ bold: true, children: [(vivo ? '●' : '○') + ' '] })
    filas.push(
      Box({
        flexDirection: 'row',
        columnGap: 2,
        borderStyle: 'round',
        paddingX: 1,
        marginBottom: 1,
        children: [avatar, Box({ flexDirection: 'column', flexShrink: 1, children: cuerpo })],
      }),
    )
  })
  return filas
}

function vistaTarea({ Text, Box, Button, Input, Select, Svg, escritorio, ancho }, acciones) {
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
  const conEspecialista = t.especialista ? { pipeline: { especialista: t.especialista } } : null
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, wrap: 'wrap', children: [t.id + ' · ' + t.titulo] }))
  filas.push(Text({ dimColor: true, children: ['Estado ' + t.estado + ' · hito ' + t.hito] }))
  filas.push(Text({ children: [' '] }))
  const lineas = t.pipeline.map((p) => ({
    nombre: nombreEtapa(p.etapa),
    quien: nombreRol(rolDe(p.etapa, conEspecialista, equipo.etapas)),
    estado: p.estado,
    nota: p.inferido ? '' : p.nota,
  }))
  if (escritorio) {
    filas.push(Svg({ alt: 'Flujo de la tarea', width: Math.min(ancho, 600), height: lineas.length * 54 + 8, source: svgLinea(lineas, ancho) }))
  } else {
    for (const l of lineas) {
      filas.push(Text({ bold: l.estado === 'activa', dimColor: l.estado === 'omitida' || l.estado === 'pendiente', children: [GLIFO_ESTADO[l.estado] + ' ' + l.nombre + ' · ' + l.quien + (l.nota ? ' — ' + l.nota : '')] }))
    }
  }
  if (t.etapa === 'autor' || t.etapa === 'playtest') {
    filas.push(Text({ children: [' '] }))
    filas.push(
      Box({
        flexDirection: 'column',
        borderStyle: 'round',
        paddingX: 1,
        children: [
          Text({ bold: true, color: 'yellow', children: [t.etapa === 'autor' ? 'Te toca revisar esta tarea' : 'Te toca jugar y probar esta tarea'] }),
          Button({ key: 'aprobar', label: t.etapa === 'autor' ? 'Aprobar revisión' : 'Aprobar prueba', hotkey: 'a', onPress: () => acciones.aprobar(t) }),
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
        ],
      }),
    )
  }
  return filas
}
