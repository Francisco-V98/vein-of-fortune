import { expect, mock, test } from 'claude-code/testing'
import { contarPorEtapa, etapaActual, pipelineDe, rolDe, rolDeAgente } from '../hooks/register.js'
import { iniciales, svgFlujo, svgLinea } from '../hooks/vis.js'

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
  { id: 'narrador', nombre: 'Narrador', tipo: 'agente', agente: 'narrador', hace: 'Escribe', entrega: 'Texto' },
  { id: 'autor', nombre: 'Autor', tipo: 'humano', agente: null, hace: 'Revisa', entrega: 'Aprobación' },
]
const EQUIPO = { etapas: ETAPAS, roles: ROLES, reglas: ['Una regla'] }
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
  const hecha = pipelineDe('done', null, ETAPAS)
  expect(hecha.every((p) => p.estado === 'hecha')).toBe(true)
})

test('un pipeline explícito manda sobre el estado', async () => {
  const actividad = {
    pipeline: {
      especialista: 'narrador',
      etapas: [
        { etapa: 'ideacion', estado: 'hecha', at: '2026-10-12', nota: 'Tres opciones' },
        { etapa: 'analisis', estado: 'activa' },
      ],
    },
  }
  const p = pipelineDe('doing', actividad, ETAPAS)
  expect(etapaActual(p)).toBe('analisis')
  expect(p[0].nota).toBe('Tres opciones')
  expect(p[2].estado).toBe('pendiente')
  expect(rolDe('produccion', actividad, ETAPAS)).toBe('narrador')
  expect(rolDe('qa', actividad, ETAPAS)).toBe('qa')
})

test('cuenta tareas por etapa y relaciona agentes con roles', async () => {
  expect(contarPorEtapa([{ etapa: 'qa' }, { etapa: 'qa' }, { etapa: 'autor' }])).toEqual({ qa: 2, autor: 1 })
  expect(rolDeAgente('narrador', ROLES)).toBe('narrador')
  expect(rolDeAgente('otro', ROLES)).toBe('')
})

test('el dibujo del flujo es un SVG con un nodo por etapa', async () => {
  const svg = svgFlujo(ETAPAS, { produccion: 2 }, ['autor', 'playtest'], 600)
  expect(svg.startsWith('<svg')).toBe(true)
  expect(svg.split('<circle').length - 1).toBe(10)
  expect(svg).toContain('>Revisión<')
})

test('las iniciales y la línea de tiempo se dibujan', async () => {
  expect(iniciales('Diseñador de sistemas')).toBe('DS')
  expect(iniciales('Francisco (autor)')).toBe('FR')
  const linea = svgLinea([{ nombre: 'Ideación', quien: 'Ideador', estado: 'hecha', nota: 'Tres opciones' }, { nombre: 'Análisis', quien: 'Analista', estado: 'activa', nota: '' }], 500)
  expect(linea).toContain('Ideación')
  expect(linea).toContain('<animate')
})

test('/equipo dibuja el flujo, la tarea en revisión y los botones del autor', async ($, on) => {
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('agent.list', () => ({ value: [{ id: 'a1', type: 'narrador', status: 'running', description: 'Escribe F0-41' }] }))
  on('fs.read', ($, e) => {
    if (e.path.endsWith('equipo.json')) return { value: JSON.stringify(EQUIPO) }
    if (e.path.endsWith('roadmap.json')) return { value: JSON.stringify(ROADMAP) }
    return { deny: 'no existe' }
  })
  on('prompt.submit', ($, e) => ({ text: e.text }))
  on('session.start', () => ({ cwd: '/work' }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: '/work' })
  await $.command.run({ command: 'equipo', args: '' })
  await new Promise((r) => setTimeout(r, 150))

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  expect(await ui.find({ type: 'Svg' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /F0-02/ })).toBeDefined()
  await ui.press({ key: 'tab-tarea' })
  expect(await ui.find({ key: 'aprobar' })).toBeDefined()
  expect(await ui.find({ key: 'devolver' })).toBeDefined()
  await ui.unmount()

  const terminal = await $.ui.mount({ ...PANE, surface: 'terminal' })
  // El estado del panel se conserva entre dibujos: volver a la pestaña del flujo
  await terminal.press({ key: 'tab-flujo' })
  expect(await terminal.find({ type: 'Text', text: /I 0  →  A 0  →  P 1/ })).toBeDefined()
  await terminal.unmount()
})
