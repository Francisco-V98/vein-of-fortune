// Panel de estado de Veta de Fortuna: /estado abre un panel con el avance del roadmap,
// la limpieza y la coherencia del diseño, las tareas en curso y los PR abiertos.
// Solo lee archivos del repositorio y ejecuta `python3 studio/hub/build.py` y `git`/`gh` de lectura.

const PANE = 'vf-estado'
const ROADMAP = 'studio/data/roadmap.json'
const ESTADOS = ['backlog', 'sprint', 'doing', 'review', 'qa', 'done']
const ETIQUETA = {
  backlog: 'Pendiente',
  sprint: 'En sprint',
  doing: 'En curso',
  review: 'En revisión',
  qa: 'En QA',
  done: 'Hecha',
}
const GLIFO = { backlog: '·', sprint: '◇', doing: '▶', review: '◉', qa: '✔', done: '■' }
const ANCHO_BARRA = 24

// Estado del panel
let tab = 'resumen'
let datos = null
let medidas = null
let ramas = null
let cargando = false
let error = ''

// Barra de progreso de texto: ██████░░░░
function barra(parte, total, ancho) {
  const w = ancho || ANCHO_BARRA
  const p = total > 0 ? parte / total : 0
  const llenos = Math.round(p * w)
  return '█'.repeat(llenos) + '░'.repeat(w - llenos)
}

function porcentaje(parte, total) {
  return total > 0 ? Math.round((parte / total) * 100) : 0
}

// Convierte el roadmap en cifras por estado, fase e hito
export function resumir(roadmap) {
  const total = { n: 0, hechas: 0, est: 0, estHechas: 0, porEstado: {} }
  for (const e of ESTADOS) total.porEstado[e] = 0
  const fases = []
  const enCurso = []
  for (const fase of roadmap.phases || []) {
    const f = { id: fase.id, nombre: fase.name, n: 0, hechas: 0, hitos: [] }
    for (const hito of fase.milestones || []) {
      const h = { id: hito.id, nombre: hito.name, n: 0, hechas: 0 }
      for (const t of hito.tasks || []) {
        const estado = ESTADOS.includes(t.status) ? t.status : 'backlog'
        const est = Number(t.est) || 0
        total.n += 1
        total.est += est
        total.porEstado[estado] += 1
        h.n += 1
        f.n += 1
        if (estado === 'done') {
          total.hechas += 1
          total.estHechas += est
          h.hechas += 1
          f.hechas += 1
        }
        if (estado === 'doing' || estado === 'review' || estado === 'qa' || estado === 'sprint') {
          enCurso.push({ id: t.id, titulo: t.title, estado, hito: hito.id, prio: t.prio })
        }
      }
      f.hitos.push(h)
    }
    fases.push(f)
  }
  const orden = { doing: 0, qa: 1, review: 2, sprint: 3 }
  enCurso.sort((a, b) => orden[a.estado] - orden[b.estado] || String(a.id).localeCompare(String(b.id)))
  return { total, fases, enCurso }
}

// Lee de la salida de build.py los dos porcentajes del diseño
export function leerMedidas(salida) {
  const limpieza = /Limpieza del diseño:\s*(\d+)\s*%/.exec(salida)
  const coherencia = /Coherencia:\s*(\d+)\s*%\s*·\s*(\d+)\s+de\s+(\d+)/.exec(salida)
  return {
    limpieza: limpieza ? Number(limpieza[1]) : null,
    coherencia: coherencia ? Number(coherencia[1]) : null,
    hallazgos: coherencia ? Number(coherencia[2]) : null,
    comprobaciones: coherencia ? Number(coherencia[3]) : null,
  }
}

// Carga el roadmap (rápido). Con `completo` también calcula medidas, rama y PR (más lento)
async function cargar($, completo) {
  cargando = true
  error = ''
  $.ui.invalidate('ui.render')
  try {
    const texto = await $.fs.read(ROADMAP)
    datos = resumir(JSON.parse(texto))
  } catch (e) {
    error = 'No se pudo leer ' + ROADMAP + ': ' + (e && e.message ? e.message : String(e))
  }
  if (completo) {
    try {
      const build = await $.process.run(['python3', 'studio/hub/build.py'], { timeoutMs: 60000 })
      medidas = leerMedidas(build.stdout + '\n' + build.stderr)
    } catch (e) {
      medidas = null
    }
    try {
      const rama = await $.process.run(['git', 'branch', '--show-current'])
      let prs = []
      try {
        const lista = await $.process.run(['gh', 'pr', 'list', '--json', 'number,title,headRefName', '--limit', '20'])
        prs = lista.exitCode === 0 ? JSON.parse(lista.stdout) : []
      } catch (e) {
        prs = []
      }
      ramas = { actual: rama.stdout.trim(), prs }
    } catch (e) {
      ramas = null
    }
  }
  cargando = false
  $.ui.invalidate('ui.render')
}

export function register(on) {
  on('session.start', async ($, e, next) => {
    // Refresco ligero del roadmap cada 30 segundos mientras la sesión esté abierta
    $.clock.every(30000, () => cargar($, false))
    await $.command.register({
      name: 'estado',
      description: 'Panel de progreso y estadísticas del proyecto',
      immediate: true,
    })
    return next(e)
  })

  on('command.run', { command: 'estado' }, async ($) => {
    await $.ui.open({ id: PANE, title: 'Estado', focus: true, closeOnEscape: true })
    cargar($, true)
    return {}
  })

  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    if (e.requestId !== PANE) return next(e)
    const { Box, Text, Button } = $.ui.resolve(e)
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
        pestana('resumen', 'Resumen', '1'),
        pestana('hitos', 'Hitos', '2'),
        pestana('curso', 'En curso', '3'),
        Button({
          key: 'actualizar',
          label: cargando ? 'Actualizando…' : 'Actualizar',
          hotkey: 'r',
          plain: true,
          onPress: () => cargar($, true),
        }),
      ],
    })

    const filas = []
    if (error) filas.push(Text({ color: 'yellow', children: [error] }))
    if (!datos) {
      filas.push(Text({ dimColor: true, children: [cargando ? 'Cargando el roadmap…' : 'Sin datos todavía.'] }))
    } else if (tab === 'resumen') {
      filas.push(...vistaResumen(Text, Box, datos, medidas, ramas))
    } else if (tab === 'hitos') {
      filas.push(...vistaHitos(Text, datos))
    } else {
      filas.push(...vistaCurso(Text, datos))
    }

    return Box({
      flexDirection: 'column',
      children: [cabecera, Text({ children: [' '] }), ...filas],
    })
  })
}

function vistaResumen(Text, Box, d, medidas, ramas) {
  const t = d.total
  const filas = []
  filas.push(Text({ bold: true, children: ['Avance del proyecto'] }))
  filas.push(Text({ children: [barra(t.hechas, t.n) + ' ' + porcentaje(t.hechas, t.n) + ' %  (' + t.hechas + ' de ' + t.n + ' tareas)'] }))
  filas.push(Text({ dimColor: true, children: ['Por horas estimadas: ' + porcentaje(t.estHechas, t.est) + ' %  (' + t.estHechas + ' de ' + t.est + ' h)'] }))
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, children: ['Por estado'] }))
  for (const e of ESTADOS) {
    filas.push(Text({ children: [GLIFO[e] + ' ' + ETIQUETA[e].padEnd(12) + String(t.porEstado[e]).padStart(4)] }))
  }
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, children: ['Calidad del diseño'] }))
  if (medidas && medidas.limpieza !== null) {
    filas.push(Text({ children: ['Limpieza    ' + barra(medidas.limpieza, 100, 16) + ' ' + medidas.limpieza + ' %  (meta 90 %)'] }))
  } else {
    filas.push(Text({ dimColor: true, children: ['Limpieza: pulsa Actualizar (r)'] }))
  }
  if (medidas && medidas.coherencia !== null) {
    filas.push(Text({ children: ['Coherencia  ' + barra(medidas.coherencia, 100, 16) + ' ' + medidas.coherencia + ' %  (' + medidas.hallazgos + ' hallazgos)'] }))
  }
  filas.push(Text({ children: [' '] }))
  filas.push(Text({ bold: true, children: ['Por fase'] }))
  for (const f of d.fases) {
    filas.push(Text({ children: [f.id.padEnd(3) + ' ' + barra(f.hechas, f.n, 16) + ' ' + String(porcentaje(f.hechas, f.n)).padStart(3) + ' %  ' + f.hechas + '/' + f.n + '  ' + f.nombre] }))
  }
  if (ramas) {
    filas.push(Text({ children: [' '] }))
    filas.push(Text({ bold: true, children: ['Git'] }))
    filas.push(Text({ children: ['Rama: ' + (ramas.actual || '—')] }))
    if (ramas.prs.length === 0) filas.push(Text({ dimColor: true, children: ['Sin PR abiertos'] }))
    for (const pr of ramas.prs) filas.push(Text({ children: ['PR ' + pr.number + '  ' + pr.title] }))
  }
  return filas
}

function vistaHitos(Text, d) {
  const filas = []
  for (const f of d.fases) {
    filas.push(Text({ bold: true, children: [f.id + ' · ' + f.nombre + '  ' + f.hechas + '/' + f.n] }))
    for (const h of f.hitos) {
      const marca = h.n > 0 && h.hechas === h.n ? '■' : h.hechas > 0 ? '▣' : '□'
      filas.push(Text({
        dimColor: h.hechas === 0,
        children: [marca + ' ' + h.id.padEnd(6) + barra(h.hechas, h.n, 12) + ' ' + String(h.hechas).padStart(2) + '/' + String(h.n).padEnd(2) + ' ' + h.nombre],
      }))
    }
    filas.push(Text({ children: [' '] }))
  }
  return filas
}

function vistaCurso(Text, d) {
  const filas = [Text({ bold: true, children: ['Tareas en movimiento (' + d.enCurso.length + ')'] })]
  if (d.enCurso.length === 0) filas.push(Text({ dimColor: true, children: ['Ninguna tarea en curso, en revisión ni en QA.'] }))
  for (const t of d.enCurso) {
    filas.push(Text({ children: [GLIFO[t.estado] + ' ' + t.id + '  ' + ETIQUETA[t.estado] + (t.prio ? ' · ' + t.prio : '')] }))
    filas.push(Text({ dimColor: true, children: ['    ' + t.titulo] }))
  }
  return filas
}
