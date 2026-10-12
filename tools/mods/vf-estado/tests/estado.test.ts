import { expect, mock, test } from 'claude-code/testing'
import { leerMedidas, resumir } from '../hooks/register.js'

const ROADMAP = {
  phases: [
    {
      id: 'F0',
      name: 'Diseño',
      milestones: [
        {
          id: 'F0.1',
          name: 'Hito uno',
          tasks: [
            { id: 'F0-01', title: 'Primera', est: 4, status: 'done', prio: 'P0' },
            { id: 'F0-02', title: 'Segunda', est: 2, status: 'doing', prio: 'P1' },
            { id: 'F0-03', title: 'Tercera', est: 6, status: 'backlog', prio: 'P2' },
          ],
        },
      ],
    },
  ],
}

const PANE = {
  plugin: 'vf-estado',
  component: 'Pane',
  requestId: 'vf-estado',
  viewport: { columns: 100, rows: 30 },
  props: { title: 'Estado', isFocused: true, bodyColumns: 60, placement: 'dock', scroll: { offset: 0, bodyRows: 30 }, view: {} },
} as const

test('resumir cuenta tareas, horas y las que están en movimiento', async () => {
  const r = resumir(ROADMAP)
  expect(r.total.n).toBe(3)
  expect(r.total.hechas).toBe(1)
  expect(r.total.est).toBe(12)
  expect(r.total.estHechas).toBe(4)
  expect(r.total.porEstado.doing).toBe(1)
  expect(r.enCurso.length).toBe(1)
  expect(r.enCurso[0].id).toBe('F0-02')
})

test('leerMedidas saca la limpieza y la coherencia de la salida de build.py', async () => {
  const salida = [
    'OK: 27 documentos, 507 tareas',
    'Limpieza del diseño: 48 % (meta 90 %) · ✅ 211 · 🟡 166 · ❓ 63 · ⏳ 3 · conexiones rotas: 0',
    'Coherencia: 68 % · 29 de 92 comprobaciones con hallazgos',
  ].join('\n')
  const m = leerMedidas(salida)
  expect(m.limpieza).toBe(48)
  expect(m.coherencia).toBe(68)
  expect(m.hallazgos).toBe(29)
  expect(m.comprobaciones).toBe(92)
})

test('/estado abre el panel y dibuja el avance', async ($, on) => {
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('fs.read', () => ({ value: JSON.stringify(ROADMAP) }))
  on('process.run', ($, e) => ({
    value: {
      exitCode: 0,
      stdout: e.argv[0] === 'python3' ? 'Limpieza del diseño: 50 % (meta 90 %)\nCoherencia: 70 % · 3 de 10 comprobaciones' : '[]',
      stderr: '',
    },
  }))
  on('session.start', () => ({ cwd: '/work' }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: '/work' })
  await $.command.run({ command: 'estado', args: '' })
  await new Promise((r) => setTimeout(r, 100))

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  expect(await ui.find({ type: 'Text', text: 'Avance del proyecto' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /33 %/ })).toBeDefined()
  await ui.press({ key: 'tab-curso' })
  expect(await ui.find({ type: 'Text', text: /F0-02/ })).toBeDefined()
  await ui.unmount()
})
