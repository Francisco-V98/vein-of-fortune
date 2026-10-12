import { expect, mock, test } from 'claude-code/testing'
import { accionesDelAutor, contarPorEtapa, estadoDeRoles, etapaActual, firmaDe, hallazgosDe, mensajeAutor, pipelineDe, prDeTarea, rolDe, rolDeAgente, rutaDe } from '../hooks/register.js'
import { envolverTexto, iniciales, svgFlujo, svgOficina, svgTraspasos } from '../hooks/vis.js'

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

test('el estado de cada rol, la ruta y los hallazgos salen de las tareas', async () => {
  const pipeline = [
    { etapa: 'ideacion', estado: 'omitida', rolEfectivo: 'ideador', hallazgos: [] },
    { etapa: 'produccion', estado: 'activa', rolEfectivo: 'narrador', hallazgos: [{ de: 'narrador', estado: 'abierto' }] },
    { etapa: 'qa', estado: 'pendiente', rolEfectivo: 'autor', hallazgos: [{ de: 'autor', estado: 'resuelto', resuelto_por: 'narrador' }] },
    { etapa: 'autor', estado: 'pendiente', rolEfectivo: 'autor', hallazgos: [] },
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
  expect(rutaDe(tarea).map((r) => r.rol)).toEqual(['narrador', 'autor'])
  expect(hallazgosDe(tarea).length).toBe(2)
})

test('el plano de la oficina coloca a todos, anima a quien trabaja y dibuja el recorrido', async () => {
  const estado = { narrador: 'trabajando', dev: 'reserva', autor: 'libre' }
  const o = svgOficina({
    ancho: 580,
    deptos: DEPTOS,
    roles: ROLES,
    estado,
    tarea: { narrador: 'F0-41' },
    ruta: [{ rol: 'narrador', estado: 'hecha' }, { rol: 'autor', estado: 'activa' }],
    hallazgos: [{ de: 'narrador', a: '', estado: 'abierto' }],
    pendientesAutor: 2,
    pie: 'Fase F0',
  })
  expect(Object.keys(o.centros).sort()).toEqual(['autor', 'dev', 'narrador'])
  expect(o.svg).toContain('F0-41')
  expect(o.svg).toContain('<animateMotion')
  expect(o.svg).toContain('Dev · F1')
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
