import { expect, mock, test } from 'claude-code/testing'
import { accionesDelAutor, contarPorEtapa, estadoDeRoles, etapaActual, firmaDe, hallazgosDe, infoDeRoles, lineasDe, mensajeAutor, ordinal, pipelineDe, prDeTarea, rolDe, rolDeAgente, seleccionDe, traspasosDe } from '../hooks/register.js'
import {
  OP_MODELO, OP_OTRO, OP_SOLO, OP_TAREA, aprobacionVigente, aprobar, anotarLanzamiento, claveTarea, contarPorModelo, familiaDe, interpretarRespuesta,
  mensajeCambio, nuevoLanzamiento, pideFable, preguntaFable, resolverEleccion, resolverRol,
} from '../hooks/politica.js'
import { envolverTexto, fijarFase, iniciales, svgFlujo, svgOficina, svgTraspasos } from '../hooks/vis.js'

const ETAPAS = [
  { id: 'ideacion', nombre: 'Ideación', rol: 'ideador', glifo: 'I' },
  { id: 'analisis', nombre: 'Análisis', rol: 'analista', glifo: 'A' },
  { id: 'produccion', nombre: 'Producción', rol: 'especialista', glifo: 'P' },
  { id: 'qa', nombre: 'QA', rol: 'qa', glifo: 'Q' },
  { id: 'autor', nombre: 'Revisión del autor', rol: 'autor', glifo: 'R' },
  { id: 'playtest', nombre: 'Prueba del autor', rol: 'autor', glifo: 'T' },
  { id: 'cierre', nombre: 'Cierre', rol: 'coordinador', glifo: 'C' },
]
const ROLES = [
  { id: 'narrador', nombre: 'Narrador', corto: 'Narrador', tipo: 'agente', agente: 'narrador', depto: 'narrativa', desde: 'F0', hace: 'Escribe', entrega: 'Texto' },
  { id: 'dev', nombre: 'Desarrollador de juego', corto: 'Dev', tipo: 'agente', agente: 'desarrollador-juego', depto: 'ingenieria', desde: 'F1', hace: 'Programa', entrega: 'Código' },
  { id: 'autor', nombre: 'Autor', corto: 'Autor', tipo: 'humano', agente: null, depto: 'direccion', desde: 'F0', hace: 'Revisa', entrega: 'Aprobación' },
]
const DEPTOS = [{ id: 'narrativa', nombre: 'Narrativa' }, { id: 'ingenieria', nombre: 'Ingeniería' }, { id: 'direccion', nombre: 'Dirección' }]
const EQUIPO = { etapas: ETAPAS, roles: ROLES, deptos: DEPTOS, reglas: ['Una regla'] }
const ROADMAP = {
  phases: [
    {
      id: 'F0',
      milestones: [
        {
          id: 'F0.1',
          tasks: [
            { id: 'F0-01', title: 'En revisión', status: 'review' },
            { id: 'F0-02', title: 'En curso', status: 'doing' },
            { id: 'F0-03', title: 'Pendiente', status: 'backlog' },
            { id: 'F0-04', title: 'Hecha', status: 'done' },
          ],
        },
      ],
    },
  ],
}
const PRS = [
  { number: 7, title: 'PR de la tarea en revisión', headRefName: 'studio/F0-01-algo', url: 'https://example.com/pull/7' },
  { number: 9, title: 'PR suelto', headRefName: 'feat/otra-cosa', url: 'https://example.com/pull/9' },
]
const PANE = {
  plugin: 'vf-equipo',
  component: 'Pane',
  requestId: 'vf-equipo',
  viewport: { columns: 100, rows: 30 },
  props: { title: 'Equipo', isFocused: true, bodyColumns: 60, placement: 'dock', scroll: { offset: 0, bodyRows: 30 }, view: {} },
} as const

test('sin pipeline explícito se infiere del estado de la tarea', async () => {
  expect(etapaActual(pipelineDe('doing', null, ETAPAS))).toBe('produccion')
  expect(etapaActual(pipelineDe('review', null, ETAPAS))).toBe('autor')
  expect(etapaActual(pipelineDe('qa', null, ETAPAS))).toBe('playtest')
  expect(pipelineDe('done', null, ETAPAS).every((p) => p.estado === 'hecha')).toBe(true)
})

test('un pipeline explícito manda y conserva entregas y hallazgos', async () => {
  const hallazgo = { de: 'analista', texto: 'Algo no cuadra', estado: 'resuelto', resuelto_por: 'narrador', como: 'Se corrigió' }
  const actividad = {
    pipeline: {
      especialista: 'narrador',
      etapas: [
        { etapa: 'ideacion', estado: 'hecha', at: '2026-10-12', nota: 'Tres opciones', entrega: 'Opciones' },
        { etapa: 'analisis', estado: 'activa', hallazgos: [hallazgo] },
      ],
    },
  }
  const p = pipelineDe('doing', actividad, ETAPAS)
  expect(etapaActual(p)).toBe('analisis')
  expect(p[0].entrega).toBe('Opciones')
  expect(p[1].hallazgos[0].como).toBe('Se corrigió')
  expect(p[2].estado).toBe('pendiente')
  expect(rolDe('produccion', actividad, ETAPAS)).toBe('narrador')
})

test('cuenta tareas por etapa y relaciona agentes con roles', async () => {
  expect(contarPorEtapa([{ etapa: 'qa' }, { etapa: 'qa' }, { etapa: 'autor' }])).toEqual({ qa: 2, autor: 1 })
  expect(rolDeAgente('narrador', ROLES)).toBe('narrador')
  expect(rolDeAgente('otro', ROLES)).toBe('')
})

test('la bandeja del autor reúne sus tareas y los PR sin tarea', async () => {
  const tareas = [
    { id: 'F0-01', titulo: 'En revisión', etapa: 'autor' },
    { id: 'F0-02', titulo: 'En curso', etapa: 'produccion' },
    { id: 'F0-05', titulo: 'A probar', etapa: 'playtest' },
  ]
  expect(prDeTarea('F0-01', PRS)?.number).toBe(7)
  expect(prDeTarea('F0-02', PRS)).toBeNull()
  const items = accionesDelAutor(tareas, PRS)
  expect(items.map((i) => i.clave)).toEqual(['F0-01:autor', 'F0-05:playtest', 'pr-9'])
  expect(items[0].tipo).toBe('revisar')
  expect(items[1].tipo).toBe('probar')
  expect(items[2].tipo).toBe('pr')
})

test('el mensaje cambia según la decisión y el tipo de acción', async () => {
  const revisar = { tipo: 'revisar', id: 'F0-01', titulo: 'Algo' }
  expect(mensajeAutor(revisar, 'aprobado')).toContain('está aprobado')
  expect(mensajeAutor(revisar, 'ajustes')).toContain('dejé ajustes en el chat')
  expect(mensajeAutor({ tipo: 'pr', id: 'PR #9', titulo: 'x' }, 'aprobado')).toContain('Puedes fusionarlo')
  expect(mensajeAutor({ tipo: 'probar', id: 'F0-05', titulo: 'x' }, 'aprobado')).toContain('la probé')
})

test('la firma cambia solo cuando cambia un archivo que importa', async () => {
  const datos = [{ name: 'roadmap.json', size: 10 }, { name: 'equipo.json', size: 5 }, { name: 'palette.json', size: 1 }]
  const tareas = [{ name: 'F0-01.json', size: 100 }]
  const base = firmaDe(datos, tareas)
  expect(firmaDe([{ name: 'roadmap.json', size: 10 }, { name: 'equipo.json', size: 5 }, { name: 'palette.json', size: 99 }], tareas)).toBe(base)
  expect(firmaDe(datos, [{ name: 'F0-01.json', size: 120 }])).not.toBe(base)
})

test('el texto se parte en líneas y el diagrama muestra hallazgos y traspasos', async () => {
  expect(envolverTexto('uno dos tres cuatro', 9)).toEqual(['uno dos', 'tres', 'cuatro'])
  expect(iniciales('Diseñador de sistemas')).toBe('DS')
  const filas = [
    { nombre: 'Análisis', quien: 'Analista', indice: 1, estado: 'hecha', nota: '', entrega: 'Informe', hallazgos: [{ de: 'Analista', texto: 'Choca con el mapa', estado: 'resuelto', resuelto_por: 'Narrador', como: 'Se actualizó' }] },
    { nombre: 'Producción', quien: 'Narrador', indice: 3, estado: 'activa', nota: 'En ello', entrega: '', hallazgos: [{ de: 'Narrador', texto: 'Falta un dato', estado: 'abierto' }] },
  ]
  const d = svgTraspasos(filas, 520)
  expect(d.svg).toContain('pasa a Narrador')
  expect(d.svg).toContain('Lo resolvió Narrador')
  expect(d.svg).toContain('⚑')
  expect(d.svg).toContain('AHORA')
  expect(d.alto).toBeGreaterThan(200)
  expect(svgFlujo(ETAPAS, { produccion: 2 }, ['autor', 'playtest'], 600).split('<circle').length - 1).toBe(10)
})

test('el estado de cada rol y los hallazgos salen de las tareas', async () => {
  const pipeline = [
    { etapa: 'ideacion', estado: 'omitida', rolEfectivo: 'ideador', hallazgos: [] },
    { etapa: 'produccion', estado: 'activa', rolEfectivo: 'narrador', hallazgos: [{ de: 'narrador', estado: 'abierto', texto: 'Falta un dato' }] },
    { etapa: 'qa', estado: 'pendiente', rolEfectivo: 'autor', hallazgos: [{ de: 'autor', estado: 'resuelto', resuelto_por: 'narrador', texto: 'Cambiar el tono', como: 'Se reescribió' }] },
  ]
  const tarea = { id: 'F0-41', pipeline }
  const { estado, tarea: quien } = estadoDeRoles([tarea], [], ROLES, 'F0', ['F0', 'F1'], 0)
  expect(estado.narrador).toBe('trabajando')
  expect(quien.narrador).toBe('F0-41')
  expect(estado.dev).toBe('reserva')
  expect(estado.autor).toBe('libre')
  expect(estadoDeRoles([], [], ROLES, 'F1', ['F0', 'F1'], 2).estado.dev).toBe('libre')
  expect(estadoDeRoles([], [], ROLES, 'F0', ['F0', 'F1'], 2).estado.autor).toBe('trabajando')
  expect(estadoDeRoles([], [{ type: 'narrador', status: 'running' }], ROLES, 'F0', ['F0', 'F1'], 0).estado.narrador).toBe('trabajando')
  const h = hallazgosDe(tarea, (id: string) => id.toUpperCase())
  expect(h.length).toBe(2)
  expect(h[1].titulo.join(' ')).toContain('Lo resolvió NARRADOR: Se reescribió')
})

test('las pasadas repetidas por la misma línea se numeran y se cuentan', async () => {
  const actividad = {
    pipeline: {
      traspasos: [
        { de: 'narrador', a: 'qa', que: 'v1', at: '2026-10-12' },
        { de: 'qa', a: 'autor', que: 'ok', at: '2026-10-12' },
        { de: 'autor', a: 'narrador', que: 'ajustes', at: '2026-10-13', tipo: 'devolucion' },
        { de: 'narrador', a: 'qa', que: 'v2', at: '2026-10-13' },
      ],
    },
  }
  const pipeline = [
    { etapa: 'produccion', estado: 'hecha', rolEfectivo: 'narrador', hallazgos: [] },
    { etapa: 'qa', estado: 'activa', rolEfectivo: 'qa', hallazgos: [] },
    { etapa: 'autor', estado: 'pendiente', rolEfectivo: 'autor', hallazgos: [] },
    { etapa: 'cierre', estado: 'pendiente', rolEfectivo: 'coordinador', hallazgos: [] },
  ]
  const log = traspasosDe(actividad, pipeline)
  expect(log.length).toBe(4)
  expect(log[2].tipo).toBe('devolucion')
  const lineas = lineasDe(log, pipeline, 'qa', (id: string) => id)
  const nq = lineas.find((l) => l.de === 'narrador' && l.a === 'qa')
  expect(nq.pasadas.length).toBe(2)
  expect(nq.estado).toBe('activa')
  expect(nq.titulo[1]).toContain('1.ª pasada · 12 oct: v1')
  expect(nq.titulo[2]).toContain('2.ª pasada · 13 oct: v2')
  expect(lineas.find((l) => l.de === 'autor' && l.a === 'narrador').titulo[1]).toContain('devolución')
  // lo que falta por recorrer sale punteado y sin pasadas
  const pendiente = lineas.find((l) => l.de === 'autor' && l.a === 'coordinador')
  expect(pendiente.estado).toBe('pendiente')
  expect(pendiente.pasadas.length).toBe(0)
  expect(ordinal(3)).toBe('3.ª')
  const info = infoDeRoles(ROLES, [], 'F0-41', lineas, [], 'F0', ['F0', 'F1'], (id: string) => id)
  expect(info.autor.join(' ')).toContain('recibió 1 y entregó 1')
  expect(info.dev.join(' ')).toContain('En reserva')
})

test('las animaciones arrancan en la fase del reloj para no reiniciarse al redibujar', async () => {
  const a = fijarFase('<svg><animate attributeName="r" dur="2s" repeatCount="indefinite"/><animateMotion dur="4s" begin="1s" repeatCount="indefinite" path="M0,0"/></svg>', 5000)
  expect(a).toContain('<animate attributeName="r" dur="2s" repeatCount="indefinite" begin="-1.00s"/>')
  expect(a).toContain('begin="-0.00s"')
  // el mismo instante da siempre el mismo dibujo; otro instante cambia la fase
  expect(fijarFase('<svg><animate dur="2s"/></svg>', 5000)).toBe(fijarFase('<svg><animate dur="2s"/></svg>', 5000))
  expect(fijarFase('<svg><animate dur="2s"/></svg>', 5500)).not.toBe(fijarFase('<svg><animate dur="2s"/></svg>', 5000))
})

test('lo que se toca con un clic implica a sus roles y lleva su texto', async () => {
  const info = { narrador: ['Narrador · agente', 'Escribe'] }
  const lineas = [{ clave: 'narrador>autor', de: 'narrador', a: 'autor', titulo: ['Narrador → Autor', '1.ª pasada: v1'], pasadas: [{}] }]
  const hallazgos = [{ clave: 'h0', de: 'autor', a: 'narrador', titulo: ['Hallazgo resuelto · Autor', 'Cambiar el tono'] }]
  expect(seleccionDe(null, info, lineas, hallazgos)).toBeNull()
  expect(seleccionDe({ tipo: 'rol', id: 'narrador' }, info, lineas, hallazgos)?.roles).toEqual(['narrador'])
  expect(seleccionDe({ tipo: 'linea', id: 'narrador>autor' }, info, lineas, hallazgos)?.roles).toEqual(['narrador', 'autor'])
  expect(seleccionDe({ tipo: 'hallazgo', id: 'h0' }, info, lineas, hallazgos)?.titulo[1]).toBe('Cambiar el tono')
  expect(seleccionDe({ tipo: 'linea', id: 'no-existe' }, info, lineas, hallazgos)).toBeNull()
})

test('sin registro de traspasos se derivan de las etapas hechas', async () => {
  const pipeline = [
    { etapa: 'produccion', estado: 'hecha', rolEfectivo: 'narrador', entrega: 'Texto', at: '2026-10-12', hallazgos: [] },
    { etapa: 'qa', estado: 'activa', rolEfectivo: 'qa', hallazgos: [] },
  ]
  const log = traspasosDe({}, pipeline)
  expect(log).toEqual([{ n: 1, de: 'narrador', a: 'qa', que: 'Texto', at: '2026-10-12', tipo: 'entrega' }])
})

test('el plano de la oficina coloca a todos, anima a quien trabaja, marca a Fran y trae globos de información', async () => {
  const estado = { narrador: 'trabajando', dev: 'reserva', autor: 'libre' }
  const lineas = [
    { de: 'narrador', a: 'autor', estado: 'activa', pasadas: [{ n: 1 }, { n: 2 }], titulo: ['Narrador → Autor · 2 pasadas', '1.ª pasada: v1', '2.ª pasada: v2'] },
  ]
  const o = svgOficina({
    ancho: 580,
    deptos: DEPTOS,
    roles: ROLES,
    estado,
    tarea: { narrador: 'F0-41' },
    lineas,
    hallazgos: [{ de: 'narrador', a: '', estado: 'abierto', titulo: ['Hallazgo abierto', 'Falta un dato'] }],
    info: { narrador: ['Narrador · agente', 'Escribe'] },
    pendientesAutor: 2,
    pie: 'Fase F0',
  })
  expect(Object.keys(o.centros).sort()).toEqual(['autor', 'dev', 'narrador'])
  expect(o.svg).toContain('F0-41')
  expect(o.svg).toContain('<animateMotion')
  expect(o.svg).toContain('Dev · F1')
  expect(o.svg).toContain('TÚ')
  expect(o.svg).toContain('★ Autor')
  expect(o.svg).toContain('<title>Narrador · agente')
  expect(o.svg).toContain('2.ª pasada: v2')
  expect(o.svg).toContain('×2')
  expect(o.svg).toContain('Falta un dato')
  expect(o.alto).toBeGreaterThan(100)
})

test('/equipo dibuja el diagrama y la bandeja, y los botones llevan al autor hasta enviar su parte', async ($, on) => {
  mock.clock(on)
  on('command.register', () => ({ value: undefined }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('agent.list', () => ({ value: [{ id: 'a1', type: 'narrador', status: 'running', description: 'Escribe F0-41' }] }))
  on('fs.list', ($, e) => ({ value: e.path.endsWith('tasks') ? [{ name: 'F0-01.json', kind: 'file', size: 10, isLink: false }] : [{ name: 'roadmap.json', kind: 'file', size: 99, isLink: false }] }))
  on('fs.read', ($, e) => {
    if (e.path.endsWith('equipo.json')) return { value: JSON.stringify(EQUIPO) }
    if (e.path.endsWith('roadmap.json')) return { value: JSON.stringify(ROADMAP) }
    return { deny: 'no existe' }
  })
  on('process.run', () => ({ value: { exitCode: 0, stdout: JSON.stringify(PRS), stderr: '' } }))
  const guardado = new Map<string, unknown>()
  on('store.get', ($, e) => ({ value: guardado.get(e.key) }))
  on('store.set', ($, e) => {
    guardado.set(e.key, e.value)
    return { value: undefined }
  })
  const enviados: string[] = []
  on('prompt.submit', ($, e) => {
    enviados.push(e.text)
    return { text: e.text }
  })
  on('session.start', () => ({ cwd: '/work' }))
  on('turn.complete', () => ({ text: '' }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: '/work' })
  await $.command.run({ command: 'equipo', args: '' })
  await new Promise((r) => setTimeout(r, 200))

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  // El plano de la oficina se dibuja como SVG
  expect(await ui.find({ type: 'Svg' })).toBeDefined()
  // La bandeja muestra la tarea en revisión con su PR y los PR sueltos
  expect(await ui.find({ type: 'Text', text: 'En revisión' })).toBeDefined()
  expect(await ui.find({ type: 'Link' })).toBeDefined()
  expect(await ui.find({ key: 'ok-F0-01:autor' })).toBeDefined()
  expect(await ui.find({ key: 'ok-pr-9' })).toBeDefined()

  // Ruta de ajustes: Salieron ajustes → Terminé mi parte
  await ui.press({ key: 'aj-F0-01:autor' })
  expect(await ui.find({ type: 'Text', text: /Cuéntame los ajustes en el chat/ })).toBeDefined()
  await ui.press({ key: 'fin-F0-01:autor' })
  expect(enviados.length).toBe(1)
  expect(enviados[0]).toContain('dejé ajustes en el chat')
  expect((guardado.get('acciones') as any)['F0-01:autor'].enviado).toBe(true)

  // Ruta de aprobación en el PR suelto
  await ui.press({ key: 'ok-pr-9' })
  await ui.press({ key: 'fin-pr-9' })
  expect(enviados[1]).toContain('Puedes fusionarlo')

  // Tocar a un empleado resalta su escritorio y abre una tarjeta que se cierra con la ✕
  await ui.press({ key: 'p-narrador' })
  expect(await ui.find({ type: 'Text', text: /Narrador · agente/ })).toBeDefined()
  expect((await ui.find({ type: 'Svg' })).props.source).toContain('stroke-dasharray="6 5"')
  await ui.press({ key: 'cerrar-detalle' })
  expect(await ui.find({ type: 'Text', text: /Narrador · agente/ })).toBeUndefined()
  // Tocar otra vez el mismo botón también la cierra
  await ui.press({ key: 'p-autor' })
  expect(await ui.find({ key: 'cerrar-detalle' })).toBeDefined()
  await ui.press({ key: 'p-autor' })
  expect(await ui.find({ key: 'cerrar-detalle' })).toBeUndefined()

  // En la pestaña de traspasos se ve el detalle de la tarea
  await ui.press({ key: 'tab-traspasos' })
  expect(await ui.find({ type: 'Svg' })).toBeDefined()
  await ui.unmount()

  // En la terminal se dibuja con texto
  const terminal = await $.ui.mount({ ...PANE, surface: 'terminal' })
  await terminal.press({ key: 'tab-oficina' })
  expect(await terminal.find({ type: 'Text', text: /I 0  →  A 0  →  P 1/ })).toBeDefined()
  await terminal.unmount()
})


// ---------- política de modelos ----------

const ROLES_POL = [
  { id: 'analista', nombre: 'Analista', agente: 'analista', modelo: 'sonnet', esfuerzo: 'medium' },
  { id: 'arquitecto', nombre: 'Arquitecto', agente: 'arquitecto', modelo: 'opus', esfuerzo: 'high' },
  { id: 'ideador', nombre: 'Ideador', agente: 'ideador', modelo: 'fable', esfuerzo: 'high' },
  { id: 'autor', nombre: 'Autor', agente: null },
]
const EQUIPO_POL = { roles: ROLES_POL, politica_modelos: { modelos: ['haiku', 'sonnet', 'opus', 'fable'], esfuerzos: ['low', 'medium', 'high', 'xhigh', 'max'], fable_requiere_autorizacion: true } }

test('un rol se resuelve por el campo agente, también con prefijo de plugin; uno desconocido no devuelve nada', async () => {
  expect(resolverRol('analista', EQUIPO_POL)?.id).toBe('analista')
  expect(resolverRol('vf:arquitecto', EQUIPO_POL)?.id).toBe('arquitecto')
  expect(resolverRol('general-purpose', EQUIPO_POL)).toBeNull()
  expect(resolverRol(undefined, EQUIPO_POL)).toBeNull()
  expect(resolverRol('analista', null)).toBeNull()
})

test('la elección rellena modelo y esfuerzo desde la tabla y respeta lo que fijó el coordinador', async () => {
  expect(resolverEleccion({ subagent_type: 'analista' }, EQUIPO_POL)).toEqual({ rol: 'analista', model: 'sonnet', effort: 'medium', motivo: 'defecto' })
  // explícito distinto de la tabla: ajuste
  expect(resolverEleccion({ subagent_type: 'analista', model: 'opus' }, EQUIPO_POL)).toEqual({ rol: 'analista', model: 'opus', effort: 'medium', motivo: 'ajuste' })
  expect(resolverEleccion({ subagent_type: 'analista', effort: 'max' }, EQUIPO_POL)).toEqual({ rol: 'analista', model: 'sonnet', effort: 'max', motivo: 'ajuste' })
  // explícito igual al de la tabla: sigue siendo el defecto
  expect(resolverEleccion({ subagent_type: 'analista', model: 'sonnet', effort: 'medium' }, EQUIPO_POL).motivo).toBe('defecto')
  // rol desconocido: no se inventa nada
  expect(resolverEleccion({ subagent_type: 'Explore' }, EQUIPO_POL)).toEqual({ rol: '', model: undefined, effort: undefined, motivo: 'defecto' })
  expect(resolverEleccion({ subagent_type: 'Explore', model: 'haiku' }, EQUIPO_POL)).toEqual({ rol: '', model: 'haiku', effort: undefined, motivo: 'ajuste' })
  // valores de la tabla fuera de la lista válida se ignoran; sin equipo no se toca nada
  const rota = { roles: [{ id: 'x', agente: 'x', modelo: 'gpt', esfuerzo: 'ultra' }] }
  expect(resolverEleccion({ subagent_type: 'x' }, rota)).toEqual({ rol: 'x', model: undefined, effort: undefined, motivo: 'defecto' })
  expect(resolverEleccion({ subagent_type: 'analista' }, null)).toEqual({ rol: '', model: undefined, effort: undefined, motivo: 'defecto' })
})

test('solo Fable pide autorización, y sin equipo legible también', async () => {
  expect(pideFable({ model: 'fable' }, EQUIPO_POL)).toBe(true)
  expect(pideFable({ model: 'Fable' }, null)).toBe(true)
  expect(pideFable({ model: 'opus' }, EQUIPO_POL)).toBe(false)
  expect(pideFable({ model: undefined }, EQUIPO_POL)).toBe(false)
  expect(pideFable({ model: 'fable' }, { politica_modelos: { fable_requiere_autorizacion: false } })).toBe(false)
})

test('la clave de tarea sale del texto (el ID más repetido) y, si no, de la rama', async () => {
  expect(claveTarea('Revisa F0-87 y deja nota', 'studio/F0-12-otra')).toBe('F0-87')
  expect(claveTarea('Sigue F0-86 (cerrada). Trabajo de F0-87. Entrega F0-87', '')).toBe('F0-87')
  expect(claveTarea('sin id', 'studio/F0-87-politica-de-modelos')).toBe('F0-87')
  expect(claveTarea('sin id', 'main')).toBe('')
  expect(claveTarea('Tarea F12-3', '')).toBe('F12-3')
  expect(claveTarea(undefined, undefined)).toBe('')
})

test('una aprobación por tarea caduca y el mapa se poda', async () => {
  const a = aprobar({ viejo: 100 }, 'F0-87', 1000, 500)
  expect(a).toEqual({ 'F0-87': 1500 })
  expect(aprobacionVigente(a, 'F0-87', 1499)).toBe(true)
  expect(aprobacionVigente(a, 'F0-87', 1500)).toBe(false)
  expect(aprobacionVigente(a, 'F0-88', 1000)).toBe(false)
  expect(aprobacionVigente(a, '', 1000)).toBe(false)
  expect(aprobacionVigente(undefined, 'F0-87', 0)).toBe(false)
})

test('las respuestas del diálogo: etiquetas exactas, texto libre solo si nombra un modelo, y lo demás es rechazo', async () => {
  expect(interpretarRespuesta(OP_TAREA).accion).toBe('tarea')
  expect(interpretarRespuesta(OP_SOLO).accion).toBe('solo')
  expect(interpretarRespuesta(OP_OTRO).accion).toBe('otro')
  expect(interpretarRespuesta(OP_MODELO.haiku)).toEqual({ accion: 'modelo', model: 'haiku' })
  expect(interpretarRespuesta('mejor opus')).toEqual({ accion: 'modelo', model: 'opus' })
  expect(interpretarRespuesta('opus o sonnet').accion).toBe('rechazar')
  expect(interpretarRespuesta('fable sí, o haiku').accion).toBe('rechazar')
  expect(interpretarRespuesta('no gracias').accion).toBe('rechazar')
  expect(interpretarRespuesta('').accion).toBe('rechazar')
  // sin tarea identificada no se ofrece aprobar la tarea
  expect(preguntaFable({ rol: 'ideador' }, 'Ideas', '').opciones).toEqual([OP_SOLO, OP_OTRO])
  expect(preguntaFable({ rol: 'ideador' }, 'Ideas', 'F0-87').opciones.length).toBe(3)
})

test('los lanzamientos se anotan con tope, se cuentan por modelo y el mensaje de cambio nombra el campo', async () => {
  let mapa: Record<string, any> = {}
  for (let i = 0; i < 6; i++) mapa = anotarLanzamiento(mapa, 'a' + i, nuevoLanzamiento({ rol: 'analista', modelo: i % 2 ? 'claude-opus-4' : 'sonnet', t: i }), 4)
  expect(Object.keys(mapa).sort()).toEqual(['a2', 'a3', 'a4', 'a5'])
  expect(familiaDe('claude-opus-4')).toBe('opus')
  expect(contarPorModelo(mapa, 0)).toEqual({ sonnet: 2, opus: 2 })
  expect(contarPorModelo(mapa, 4)).toEqual({ sonnet: 1, opus: 1 })
  expect(nuevoLanzamiento({ motivo: 'raro' }).motivo).toBe('defecto')
  expect(mensajeCambio(ROLES_POL[0], 'modelo')).toContain('«modelo»')
  expect(mensajeCambio(ROLES_POL[0], 'esfuerzo')).toContain('«esfuerzo»')
})

// Prepara el hook sobre Agent con un equipo, un diálogo guionizado y un motor que acepta el lanzamiento
function prepararHook($: any, on: any, opciones: { equipo?: unknown; respuestas?: Array<string | Error>; rama?: string; almacen?: Record<string, unknown> }) {
  const reloj = mock.clock(on, { now: 1_000_000 })
  const almacen = new Map<string, unknown>(Object.entries(opciones.almacen || {}))
  on('store.get', (_$: any, e: any) => ({ value: almacen.get(e.key) }))
  on('store.set', (_$: any, e: any) => {
    almacen.set(e.key, e.value)
    return { value: undefined }
  })
  on('command.register', () => ({ value: undefined }))
  on('session.start', () => ({ cwd: '/work' }))
  on('fs.read', (_$: any, e: any) => (e.path.endsWith('equipo.json') && opciones.equipo !== undefined ? { value: JSON.stringify(opciones.equipo) } : { deny: 'no existe' }))
  on('process.run', () => ({ value: { exitCode: 0, stdout: (opciones.rama ?? 'main') + '\n', stderr: '' } }))
  const preguntas: any[] = []
  const respuestas = [...(opciones.respuestas || [])]
  on('tool.call', { tool: 'AskUserQuestion' }, (_$: any, e: any) => {
    preguntas.push(e.questions[0])
    const r = respuestas.shift()
    if (r === undefined || r instanceof Error) return { deny: 'cancelado' }
    return { result: { questions: e.questions, answers: { [e.questions[0].question]: r } } }
  })
  const llegadas: any[] = []
  on('tool.call', { tool: 'Agent' }, (_$: any, e: any) => {
    llegadas.push(e)
    return { result: { agentId: 'ag-' + llegadas.length, content: [] } }
  })
  const spawns: any[] = []
  on('agent.spawn', (_$: any, e: any) => {
    spawns.push(e)
    return { model: 'claude-' + (e.model || 'heredado') + '-5', agentId: 'ag-' + spawns.length }
  })
  return { reloj, almacen, preguntas, llegadas, spawns }
}

test('el hook rellena modelo y esfuerzo desde la tabla y deja pasar sin preguntar', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  const r = await $.tool.call({ tool: 'Agent', description: 'Revisa F0-87', prompt: 'Haz algo', subagent_type: 'arquitecto' })
  expect(r.deny).toBeUndefined()
  expect(t.llegadas[0].model).toBe('opus')
  expect(t.llegadas[0].effort).toBe('high')
  expect(t.preguntas.length).toBe(0)
  // lo explícito del coordinador se respeta
  await $.tool.call({ tool: 'Agent', description: 'Otro', prompt: 'x', subagent_type: 'arquitecto', model: 'haiku', effort: 'low' })
  expect(t.llegadas[1].model).toBe('haiku')
  expect(t.llegadas[1].effort).toBe('low')
  // un agente que no está en la tabla pasa tal cual
  await $.tool.call({ tool: 'Agent', description: 'Busca', prompt: 'x', subagent_type: 'Explore' })
  expect(t.llegadas[2].model).toBeUndefined()
  expect(t.llegadas[2].effort).toBeUndefined()
})

test('con Fable el diálogo ofrece aprobar o cambiar y «Aprobar para esta tarea» no vuelve a preguntar', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: [OP_TAREA, OP_SOLO, OP_SOLO] })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  const lanzar = (desc: string) => $.tool.call({ tool: 'Agent', description: desc, prompt: 'Trabaja en F0-87', subagent_type: 'ideador' })

  let r = await lanzar('Ideas')
  expect(r.deny).toBeUndefined()
  expect(t.llegadas[0].model).toBe('fable')
  expect(t.preguntas.length).toBe(1)
  expect(t.preguntas[0].options.map((o: any) => o.label)).toEqual([OP_TAREA, OP_SOLO, OP_OTRO])
  // misma tarea: ya hay aprobación vigente
  r = await lanzar('Más ideas')
  expect(r.deny).toBeUndefined()
  expect(t.preguntas.length).toBe(1)
  expect(t.llegadas[1].model).toBe('fable')
  // otra tarea: pregunta de nuevo y «solo este» no deja aprobación
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'Trabaja en F0-88', subagent_type: 'ideador' })
  expect(t.preguntas.length).toBe(2)
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'Trabaja en F0-88', subagent_type: 'ideador' })
  expect(t.preguntas.length).toBe(3)
})

test('una aprobación caducada de la tarea vuelve a preguntar', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: [OP_SOLO], almacen: { aprobaciones: { 'F0-87': 999_999, 'F0-90': 2_000_000 } } })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'F0-87', subagent_type: 'ideador' })
  expect(t.preguntas.length).toBe(1)
  // una aprobación vigente de otra tarea no pregunta
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'F0-90', subagent_type: 'ideador' })
  expect(t.preguntas.length).toBe(1)
})

test('sin ID de tarea en el texto se usa el de la rama git', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: [], rama: 'studio/F0-90-algo', almacen: { aprobaciones: { 'F0-90': 2_000_000 } } })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  const r = await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'sin id', subagent_type: 'ideador' })
  expect(r.deny).toBeUndefined()
  expect(t.preguntas.length).toBe(0)
})

test('con Fable se puede elegir otro modelo en el segundo paso o escribirlo en «Other»', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: [OP_OTRO, OP_MODELO.sonnet, 'mejor haiku'] })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'F0-87', subagent_type: 'ideador' })
  expect(t.llegadas[0].model).toBe('sonnet')
  expect(t.llegadas[0].effort).toBe('high')
  expect(t.preguntas[1].options.map((o: any) => o.label)).toEqual([OP_MODELO.opus, OP_MODELO.sonnet, OP_MODELO.haiku])
  await $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'F0-87', subagent_type: 'ideador' })
  expect(t.llegadas[1].model).toBe('haiku')
})

test('cancelar, un texto que no nombra un modelo o un error del diálogo deniegan Fable', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: ['no sé', new Error('cancelado'), OP_OTRO, 'mmm'] })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  const lanzar = () => $.tool.call({ tool: 'Agent', description: 'Ideas', prompt: 'F0-87', subagent_type: 'ideador' })
  for (let i = 0; i < 3; i++) {
    const r = await lanzar()
    expect(r.deny).toBe('Fable no autorizado')
  }
  expect(t.llegadas.length).toBe(0)
})

test('sin equipo.json no bloquea, salvo que el encargo pida Fable', async ($, on) => {
  const t = prepararHook($, on, { respuestas: [] })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  const r = await $.tool.call({ tool: 'Agent', description: 'Algo', prompt: 'x', subagent_type: 'analista', model: 'sonnet' })
  expect(r.deny).toBeUndefined()
  expect(t.llegadas[0].model).toBe('sonnet')
  const f = await $.tool.call({ tool: 'Agent', description: 'Algo', prompt: 'x', subagent_type: 'analista', model: 'fable' })
  expect(f.deny).toBe('Fable no autorizado')
  expect(t.llegadas.length).toBe(1)
})

test('un lanzamiento desde un subagente también pasa por la política', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL, respuestas: [OP_SOLO] })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  await $.tool.call({ tool: 'Agent', agentId: 'sub-1', description: 'Ideas', prompt: 'F0-87', subagent_type: 'ideador' })
  expect(t.preguntas.length).toBe(1)
  expect(t.llegadas[0].model).toBe('fable')
})

test('agent.spawn guarda el rol, el modelo y el motivo de cada agente lanzado', async ($, on) => {
  const t = prepararHook($, on, { equipo: EQUIPO_POL })
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  await $.agent.spawn({ prompt: 'Trabaja en F0-87', description: 'Revisa', subagentType: 'analista', model: 'opus' })
  const guardado = t.almacen.get('lanzamientos') as Record<string, any>
  const l = guardado['ag-1']
  expect(l.rol).toBe('analista')
  expect(l.modelo).toBe('opus')
  expect(l.motivo).toBe('defecto')
  expect(l.tarea).toBe('F0-87')
  expect(l.autorizado).toBe(false)
  expect(l.t).toBe(1_000_000)
  expect(t.spawns.length).toBe(1)
})

test('la pestaña Equipo muestra modelo y esfuerzo, cuenta los lanzamientos y «Cambiar» pide el cambio al coordinador', async ($, on) => {
  mock.clock(on, { now: 5000 })
  mock.store(on)
  on('command.register', () => ({ value: undefined }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('agent.list', () => ({ value: [] }))
  on('fs.list', (_$: any, e: any) => ({ value: e.path.endsWith('tasks') ? [] : [{ name: 'equipo.json', kind: 'file', size: 99, isLink: false }] }))
  on('fs.read', (_$: any, e: any) => {
    if (e.path.endsWith('roadmap.json')) return { value: JSON.stringify(ROADMAP) }
    if (e.path.endsWith('equipo.json')) return { value: JSON.stringify({ ...EQUIPO, roles: ROLES_POL.map((r) => ({ ...r, corto: r.nombre, tipo: r.agente ? 'agente' : 'humano', depto: 'narrativa', desde: 'F0', hace: 'Hace', entrega: 'Algo' })) }) }
    return { deny: 'no existe' }
  })
  on('process.run', () => ({ value: { exitCode: 0, stdout: '[]', stderr: '' } }))
  const enviados: any[] = []
  on('prompt.submit', (_$: any, e: any) => {
    enviados.push(e)
    return { text: e.text }
  })
  on('session.start', () => ({ cwd: '/work' }))
  on('tool.call', { tool: 'Agent' }, () => ({ result: { agentId: 'z', content: [] } }))
  on('agent.spawn', (_$: any, e: any) => ({ model: 'claude-sonnet-5', agentId: 'z1' }))
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
  await $.agent.spawn({ prompt: 'F0-87', description: 'Revisa', subagentType: 'analista' })
  await $.command.run({ command: 'equipo', args: '' })
  await new Promise((r) => setTimeout(r, 100))
  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  await ui.press({ key: 'tab-equipo' })
  expect(await ui.find({ type: 'Text', text: /sonnet 1/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /Modelo sonnet · esfuerzo medium/ })).toBeDefined()
  expect(await ui.find({ key: 'modelo-autor' })).toBeUndefined()
  await ui.press({ key: 'esfuerzo-analista' })
  expect(enviados.length).toBe(1)
  expect(enviados[0].origin.asUser).toBe(true)
  expect(enviados[0].text).toContain('esfuerzo del rol «Analista»')
  await ui.unmount()
})
