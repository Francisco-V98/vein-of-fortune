import { expect, mock, test } from 'claude-code/testing'
import {
  acumularTurno, barra, cerrarRegistro, claveDia, frescos, leerLimites, masCaros, nuevoRegistro, podar,
  porModelo, puntos, sumarADia, tiempoHasta, tokens, tokensPorPunto, ultimosDias, usoRegistro,
} from '../hooks/logica.js'

const LIMITES = leerLimites([
  { kind: 'five_hour', percentUsed: 30, resetsAt: '2026-10-13T20:00:00Z' },
  { kind: 'seven_day', percentUsed: 12.5, resetsAt: '2026-10-18T00:00:00Z' },
])

const USO_A = { input_tokens: 100, output_tokens: 400, cache_read_input_tokens: 9000, cache_creation_input_tokens: 500, model: 'claude-sonnet-5-5' }
const USO_B = { input_tokens: 50, output_tokens: 100, cache_read_input_tokens: 3000, cache_creation_input_tokens: 0, model: 'claude-opus-5-5' }

const PANE = {
  plugin: 'vf-consumo',
  component: 'Pane',
  requestId: 'vf-consumo',
  viewport: { columns: 100, rows: 30 },
  props: { title: 'Consumo', isFocused: true, bodyColumns: 60, placement: 'dock', scroll: { offset: 0, bodyRows: 30 }, view: {} },
} as const

test('leerLimites separa la ventana de cinco horas y la semanal', async () => {
  expect(LIMITES.cinco.pct).toBe(30)
  expect(LIMITES.semana.pct).toBe(12.5)
  expect(LIMITES.cinco.resetsAt).toBe(Date.parse('2026-10-13T20:00:00Z'))
  expect(leerLimites([]).cinco).toBeNull()
})

test('un registro suma el hilo principal y los subagentes por separado', async () => {
  const reg = nuevoRegistro({ id: 't1', t: 1000, texto: '  hola\n  mundo  ', proyecto: 'juego', limites: LIMITES })
  acumularTurno(reg, USO_A, false, 4000)
  acumularTurno(reg, USO_B, true, 2000)
  expect(reg.txt).toBe('hola mundo')
  expect(reg.n).toBe(1)
  expect(reg.ms).toBe(4000)
  expect(reg.subN).toBe(1)
  expect(reg.sub).toEqual([50, 100, 3000, 0])
  expect(usoRegistro(reg)).toEqual([150, 500, 12000, 500])
  expect(frescos(usoRegistro(reg))).toBe(1150)
  expect(Object.keys(reg.mod).length).toBe(2)
})

test('los puntos de la ventana que gastó un prompt nunca son negativos', async () => {
  const reg = nuevoRegistro({ id: 't2', t: 1, texto: 'x', limites: LIMITES })
  cerrarRegistro(reg, { cinco: { pct: 31.5 }, semana: { pct: 12.5 } })
  expect(puntos(reg.p5)).toBe(1.5)
  expect(puntos(reg.p7)).toBe(0)
  reg.p5 = [90, 4] // la ventana se reinició entre medias
  expect(puntos(reg.p5)).toBe(0)
  expect(puntos([null, 5])).toBeNull()
})

test('el resumen por día y por modelo suma lo que se guarda', async () => {
  const ahora = Date.parse('2026-10-13T15:00:00')
  const dias = {}
  const r1 = acumularTurno(nuevoRegistro({ id: 'a', t: ahora, texto: 'uno', limites: LIMITES }), USO_A, false, 1)
  const r2 = acumularTurno(nuevoRegistro({ id: 'b', t: ahora - 86400000, texto: 'dos', limites: LIMITES }), USO_B, false, 1)
  sumarADia(dias, r1)
  sumarADia(dias, r2)
  const filas = ultimosDias(dias, 2, ahora)
  expect(filas.length).toBe(2)
  expect(filas[1].dia).toBe(claveDia(ahora))
  expect(filas[1].n).toBe(1)
  expect(filas[0].n).toBe(1)
  const modelos = porModelo(filas)
  expect(modelos[0].modelo).toBe('claude-sonnet-5-5')
  const caros = masCaros([r1, r2], 0, 1)
  expect(caros[0].reg.id).toBe('a')
})

test('cuántos tokens vale un punto sale de lo gastado en la ventana', async () => {
  const reg = acumularTurno(nuevoRegistro({ id: 'c', t: Date.parse('2026-10-13T18:00:00Z'), texto: 'x', limites: LIMITES }), USO_A, false, 1)
  const por = tokensPorPunto([reg], LIMITES.cinco, 5 * 3600 * 1000)
  expect(por).toBe(Math.round(1000 / 30))
  expect(tokensPorPunto([], LIMITES.cinco, 5 * 3600 * 1000)).toBeNull()
  expect(tokensPorPunto([reg], null, 5 * 3600 * 1000)).toBeNull()
})

test('el formato de cifras, barras y tiempos', async () => {
  expect(tokens(950)).toBe('950')
  expect(tokens(1500)).toBe('1,5 k')
  expect(tokens(25000)).toBe('25 k')
  expect(tokens(2500000)).toBe('2,5 M')
  expect(barra(50, 10)).toBe('█████░░░░░')
  expect(tiempoHasta(Date.parse('2026-10-13T20:00:00Z'), Date.parse('2026-10-13T17:30:00Z'))).toBe('2 h 30 min')
  expect(tiempoHasta(null, 0)).toBe('—')
  expect(podar([1, 2, 3, 4], 2)).toEqual([3, 4])
})

test('/consumo abre el panel y dibuja las ventanas y el historial', async ($, on) => {
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('session.start', () => ({ cwd: '/work/juego' }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.command.run({ command: 'consumo', args: '' })
  await new Promise((r) => setTimeout(r, 50))

  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect(await ui.find({ type: 'Text', text: 'Ventanas de uso' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'Todavía no hay prompts registrados.' })).toBeDefined()
  await ui.press({ key: 'tab-dias' })
  expect(await ui.find({ type: 'Text', text: /Últimos 14 días/ })).toBeDefined()
  await ui.press({ key: 'tab-prompts' })
  expect(await ui.find({ type: 'Text', text: /prompts guardados/ })).toBeDefined()
  await ui.unmount()
})

test('un turno completo se guarda con sus tokens, sus subagentes y los puntos de la ventana', async ($, on) => {
  const almacen: Record<string, unknown> = {}
  let pct = 30
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('session.start', () => ({ cwd: '/work/juego' }))
  on('store.get', (_$, e) => ({ value: almacen[e.key] }))
  on('store.set', (_$, e) => {
    almacen[e.key] = e.value
    return { value: undefined }
  })
  on('session.cwd', () => ({ value: '/work/juego' }))
  on('turn.start', (_$, e) => ({ turnId: e.turnId }))
  on('turn.complete', (_$, e) => ({ text: e.answer }))
  on('ui.status', () => ({ value: undefined }))
  on('session.usage', () => ({
    value: {
      startedAt: 0,
      context: {},
      rateLimits: [
        { kind: 'five_hour', percentUsed: pct, resetsAt: '2026-10-13T20:00:00Z' },
        { kind: 'seven_day', percentUsed: 10, resetsAt: '2026-10-18T00:00:00Z' },
      ],
    },
  }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.turn.start({ text: 'Revisa el documento 25', turnId: 'turno-1' })
  await $.turn.complete({ answer: 'Listo', durationMs: 5000, isAborted: false, turnId: 'sub-1', agentId: 'agente-1', reason: 'answer', usage: USO_B })
  pct = 31.5
  await $.turn.complete({ answer: 'Listo', durationMs: 9000, isAborted: false, turnId: 'turno-1', reason: 'answer', usage: USO_A })

  const guardados = almacen.registros as any[]
  expect(guardados.length).toBe(1)
  expect(guardados[0].txt).toBe('Revisa el documento 25')
  expect(guardados[0].cwd).toBe('juego')
  expect(guardados[0].subN).toBe(1)
  expect(guardados[0].p5).toEqual([30, 31.5])
  expect(Object.keys(almacen.dias as object).length).toBe(1)
  expect((almacen.muestras as any[]).length).toBe(1)
})
