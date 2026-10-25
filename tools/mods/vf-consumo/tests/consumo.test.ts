import { expect, mock, test } from 'claude-code/testing'
import {
  acumularTurno, barra, cerrarRegistro, claveDia, frescos, leerLimites, masCaros, nuevoRegistro, podar,
  anotarAgente, construirExportacion, porRol, MAX_AGENTES_REG,
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
  cerrarRegistro(reg, { cinco: { pct: 31.5, resetsAt: LIMITES.cinco.resetsAt }, semana: { pct: 12.5, resetsAt: LIMITES.semana.resetsAt } })
  expect(puntos(reg.p5)).toBe(1.5)
  expect(puntos(reg.p7)).toBe(0)
  reg.p5 = [90, 4] // el contador bajó
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
  const por = tokensPorPunto([reg], LIMITES.cinco, 5 * 3600 * 1000, Date.parse('2026-10-13T19:00:00Z'))
  expect(por).toBe(Math.round(1000 / 30))
  expect(tokensPorPunto([reg], LIMITES.cinco, 5 * 3600 * 1000, Date.parse('2026-10-13T21:00:00Z'))).toBeNull()
  expect(tokensPorPunto([], LIMITES.cinco, 5 * 3600 * 1000)).toBeNull()
  expect(tokensPorPunto([reg], null, 5 * 3600 * 1000)).toBeNull()
})

test('si la ventana se reinicia mientras corre el prompt, sus puntos quedan sin dato', async () => {
  const reg = nuevoRegistro({ id: 'r', t: 1, texto: 'x', limites: LIMITES })
  cerrarRegistro(reg, { cinco: { pct: 2, resetsAt: LIMITES.cinco.resetsAt + 5 * 3600 * 1000 }, semana: LIMITES.semana })
  expect(puntos(reg.p5)).toBeNull()
  expect(puntos(reg.p7)).toBe(0)
})

test('un turno sin respuesta no inventa un modelo ni tokens', async () => {
  const reg = acumularTurno(nuevoRegistro({ id: 'ab', t: 1, texto: 'x', limites: LIMITES }), undefined, false, 800)
  expect(Object.keys(reg.mod).length).toBe(0)
  expect(reg.n).toBe(1)
  expect(reg.nu).toBe(0)
})

test('el formato de cifras, barras y tiempos', async () => {
  expect(tokens(999999)).toBe('1,0 M')
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

test('un subagente que termina tarde se suma al último prompt sin contar uno más', async ($, on) => {
  const almacen: Record<string, unknown> = {}
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
  on('session.usage', () => ({ value: { startedAt: 0, context: {}, rateLimits: [] } }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.turn.start({ text: 'Lanza un agente', turnId: 'turno-9' })
  await $.turn.complete({ answer: 'Hecho', durationMs: 1000, isAborted: false, turnId: 'turno-9', reason: 'answer', usage: USO_A })
  await $.turn.complete({ answer: 'Informe', durationMs: 500, isAborted: false, turnId: 'sub-9', agentId: 'tarde', reason: 'answer', usage: USO_B })

  const guardados = almacen.registros as any[]
  expect(guardados.length).toBe(1)
  expect(guardados[0].subN).toBe(1)
  const dia = Object.values(almacen.dias as Record<string, any>)[0]
  expect(dia.n).toBe(1)
  expect(dia.sub).toEqual([50, 100, 3000, 0])
  expect(dia.uso).toEqual([150, 500, 12000, 500])
})

test('session.measure actualiza la línea de estado y guarda una muestra', async ($, on) => {
  const almacen: Record<string, unknown> = {}
  const estados: string[] = []
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('session.start', () => ({ cwd: '/work/juego' }))
  on('store.get', (_$, e) => ({ value: almacen[e.key] }))
  on('store.set', (_$, e) => {
    almacen[e.key] = e.value
    return { value: undefined }
  })
  on('ui.status', (_$, e) => {
    estados.push(String(e.text))
    return { value: undefined }
  })
  on('session.usage', () => ({ value: { startedAt: 0, context: {}, rateLimits: [] } }))
  on('session.measure', (_$, e) => ({ changed: e.changed }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.session.measure({
    context: {},
    changed: ['rateLimits'],
    rateLimits: [{ kind: 'five_hour', percentUsed: 42, resetsAt: '2099-01-01T00:00:00Z' }],
  })

  expect((almacen.muestras as any[]).length).toBe(1)
  expect((almacen.muestras as any[])[0][1]).toBe(42)
  expect(estados[estados.length - 1]).toContain('42')
})

function almacenado($: any, on: any, limites: any[] = []) {
  const almacen: Record<string, unknown> = {}
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('session.start', () => ({ cwd: '/work/juego' }))
  on('store.get', (_$: any, e: any) => ({ value: almacen[e.key] }))
  on('store.set', (_$: any, e: any) => {
    almacen[e.key] = e.value
    return { value: undefined }
  })
  on('session.cwd', () => ({ value: '/work/juego' }))
  on('turn.start', (_$: any, e: any) => ({ turnId: e.turnId }))
  on('turn.complete', (_$: any, e: any) => ({ text: e.answer }))
  on('ui.status', () => ({ value: undefined }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('session.usage', () => ({ value: { startedAt: 0, context: {}, rateLimits: limites } }))
  return almacen
}

test('dos prompts solapados se cierran cada uno con lo suyo, aunque terminen al revés', async ($, on) => {
  const almacen = almacenado($, on)
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.turn.start({ text: 'Primero', turnId: 'p1' })
  await $.turn.start({ text: 'Segundo', turnId: 'p2' })
  await $.turn.complete({ answer: 'b', durationMs: 10, isAborted: false, turnId: 'p2', reason: 'answer', usage: USO_B })
  await $.turn.complete({ answer: 'a', durationMs: 20, isAborted: false, turnId: 'p1', reason: 'answer', usage: USO_A })

  const guardados = almacen.registros as any[]
  const por = Object.fromEntries(guardados.map((r) => [r.id, r]))
  expect(guardados.length).toBe(2)
  expect(por.p1.txt).toBe('Primero')
  expect(por.p1.nu).toBe(1000)
  expect(por.p2.txt).toBe('Segundo')
  expect(por.p2.nu).toBe(150)
})

test('un turno que se guarda dos veces con el mismo id no se cuenta dos veces por día', async ($, on) => {
  const almacen = almacenado($, on)
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.turn.complete({ answer: 'a', durationMs: 10, isAborted: false, turnId: 'igual', reason: 'answer', usage: USO_A })
  await $.turn.complete({ answer: 'a', durationMs: 10, isAborted: false, turnId: 'igual', reason: 'answer', usage: USO_A })

  expect((almacen.registros as any[]).length).toBe(1)
  expect(Object.values(almacen.dias as Record<string, any>)[0].n).toBe(1)
})

test('el panel dice que la ventana se reinició si su hora de reinicio ya pasó', async ($, on) => {
  almacenado($, on, [{ kind: 'five_hour', percentUsed: 80, resetsAt: '1960-01-01T00:00:00Z' }])
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.command.run({ command: 'consumo', args: '' })
  await new Promise((r) => setTimeout(r, 50))

  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  expect(await ui.find({ type: 'Text', text: /ventana reiniciada/ })).toBeDefined()
  await ui.unmount()
})

test('los últimos días son consecutivos y terminan hoy', async () => {
  const ahora = Date.parse('2026-10-13T12:00:00')
  const filas = ultimosDias({}, 4, ahora)
  expect(filas.map((f) => f.dia)).toEqual(['2026-10-10', '2026-10-11', '2026-10-12', '2026-10-13'])
})

// ---- Roles y exportación ----

const MAPA = { 'ag-a': { rol: 'analista', modelo: 'opus', esfuerzo: 'high', t: 1 }, 'ag-b': { rol: 'qa', modelo: 'haiku', esfuerzo: '', t: 2 } }
const sumaFrescos = (filas: any[]) => filas.reduce((a, f) => a + frescos(f.uso), 0)

function regConSubs() {
  const reg = nuevoRegistro({ id: 'r1', t: 5000, texto: 'secreto: mi contraseña', proyecto: 'carpeta-privada', limites: LIMITES })
  acumularTurno(reg, USO_A, false, 1000)
  acumularTurno(reg, USO_B, true, 500, 'ag-a')
  acumularTurno(reg, USO_B, true, 500, 'ag-b')
  acumularTurno(reg, USO_B, true, 500, 'ag-b')
  return reg
}

test('el gasto de los subagentes se atribuye por agentId y suma el total', async () => {
  const reg = regConSubs()
  expect(reg.sub_ag['ag-b']).toEqual([100, 200, 6000, 0])
  const filas = porRol([reg], MAPA)
  expect(filas.find((f) => f.rol === 'analista').esfuerzo).toBe('high')
  expect(filas.find((f) => f.rol === 'qa').agentes).toBe(1)
  expect(filas.find((f) => f.rol === 'hilo principal').uso).toEqual([100, 400, 9000, 500])
  expect(sumaFrescos(filas)).toBe(frescos(usoRegistro(reg)))
})

test('un agente sin rol, sin spawn o ya podado sale como «sin rol» sin perder tokens', async () => {
  const reg = regConSubs()
  const filas = porRol([reg], { 'ag-a': { rol: '', modelo: 'opus', esfuerzo: '', t: 1 } })
  const sin = filas.filter((f) => f.rol === 'sin rol')
  expect(sin.reduce((a, f) => a + frescos(f.uso), 0)).toBe(frescos(reg.sub))
  expect(sumaFrescos(filas)).toBe(frescos(usoRegistro(reg)))
  expect(porRol([reg], undefined).every((f) => f.rol === 'hilo principal' || f.rol === 'sin rol')).toBe(true)
})

test('más de 500 lanzamientos podan los más antiguos', async () => {
  let mapa: Record<string, any> = {}
  for (let i = 0; i < 520; i++) mapa = anotarAgente(mapa, 'ag-' + i, { rol: 'qa', t: 0 }) // t igual: manda el orden
  expect(Object.keys(mapa).length).toBe(500)
  expect(mapa['ag-0']).toBeUndefined()
  expect(mapa['ag-519']).toBeDefined()
  mapa = anotarAgente(mapa, 'ag-519', { rol: 'otro', t: 9999 })
  expect(Object.keys(mapa).length).toBe(500)
  expect(mapa['ag-519'].rol).toBe('otro')
})

test('un registro acota sus agentes y agrupa el resto en _otros sin perder tokens', async () => {
  const reg = nuevoRegistro({ id: 'r2', t: 1, texto: '', limites: LIMITES })
  for (let i = 0; i < MAX_AGENTES_REG + 10; i++) acumularTurno(reg, USO_B, true, 0, 'ag-' + i)
  expect(Object.keys(reg.sub_ag).length).toBe(MAX_AGENTES_REG + 1)
  expect(reg.sub_ag._otros).toEqual([500, 1000, 30000, 0])
  expect(sumaFrescos(porRol([reg], {}))).toBe(frescos(usoRegistro(reg)))
})

test('los registros viejos sin sub_ag cuentan sus subagentes como «sin rol»', async () => {
  const viejo = { id: 'v', t: 10, txt: 'x', cwd: '', mod: { 'claude-opus-5-5': [200, 300, 0, 0] }, sub: [50, 100, 0, 0], subN: 1, n: 1, ms: 0, nu: 500, p5: [null, null], p7: [null, null] }
  const filas = porRol([viejo], MAPA)
  expect(filas.find((f) => f.rol === 'sin rol').uso).toEqual([50, 100, 0, 0])
  expect(filas.find((f) => f.rol === 'hilo principal').uso).toEqual([150, 200, 0, 0])
  acumularTurno(viejo as any, USO_B, true, 0, 'ag-a') // y aceptan agentes nuevos
  expect(viejo.sub_ag['ag-a']).toEqual([50, 100, 3000, 0])
})

test('la exportación lleva cifras y fechas pero no el texto, la carpeta ni los ids', async () => {
  const reg = regConSubs()
  const json = JSON.stringify(construirExportacion([reg], MAPA, 9000))
  expect(json).not.toContain('secreto')
  expect(json).not.toContain('contraseña')
  expect(json).not.toContain('carpeta-privada')
  expect(json).not.toContain('ag-a')
  expect(json).not.toContain('r1')
  const e = JSON.parse(json)
  expect(e.prompts).toBe(1)
  expect(e.registros[0].fecha).toBe(new Date(5000).toISOString())
  expect(e.registros[0].modelos['claude-sonnet-5-5'].nuevos).toBe(1000)
  expect(e.por_rol.find((f: any) => f.rol === 'analista').esfuerzo).toBe('high')
})

test('turnos completos con agentId llenan sub_ag, agent.spawn guarda el rol y /consumo exportar escribe el JSON', async ($, on) => {
  const almacen: Record<string, unknown> = {}
  const escritos: Record<string, string> = {}
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('store.get', (_$, e) => ({ value: almacen[e.key] }))
  on('store.set', (_$, e) => {
    almacen[e.key] = e.value
    return { value: undefined }
  })
  on('fs.write', (_$: any, e: any) => {
    escritos[e.path] = e.text
    return { value: undefined }
  })
  on('session.start', () => ({ cwd: '/work/juego' }))
  on('session.cwd', () => ({ value: '/work/juego' }))
  on('turn.start', (_$, e) => ({ turnId: e.turnId }))
  on('turn.complete', (_$, e) => ({ text: e.answer }))
  on('ui.status', () => ({ value: undefined }))
  on('session.usage', () => ({ value: { startedAt: 0, context: {}, rateLimits: [] } }))
  on('agent.spawn', () => ({ model: 'claude-opus-5-5', agentId: 'ag-1' }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.agent.spawn({ prompt: 'x', description: 'Revisa', subagentType: 'analista', model: 'opus' })
  expect((almacen.agentes as any)['ag-1'].rol).toBe('analista')
  await $.turn.start({ text: 'Prompt privado', turnId: 't-1' })
  await $.turn.complete({ answer: 'ok', durationMs: 10, isAborted: false, turnId: 'sub-1', agentId: 'ag-1', reason: 'answer', usage: USO_B })
  await $.turn.complete({ answer: 'ok', durationMs: 10, isAborted: false, turnId: 't-1', reason: 'answer', usage: USO_A })
  expect((almacen.registros as any[])[0].sub_ag['ag-1']).toEqual([50, 100, 3000, 0])
  // llega tarde: se suma al último prompt cerrado
  await $.turn.complete({ answer: 'ok', durationMs: 10, isAborted: false, turnId: 'sub-2', agentId: 'ag-1', reason: 'answer', usage: USO_B })
  expect((almacen.registros as any[])[0].sub_ag['ag-1']).toEqual([100, 200, 6000, 0])

  await $.command.run({ command: 'consumo', args: 'exportar' })
  const ruta = Object.keys(escritos)[0]
  expect(ruta).toMatch(/consumo-\d{4}-\d{2}-\d{2}\.json$/)
  expect(escritos[ruta]).not.toContain('Prompt privado')
  expect(JSON.parse(escritos[ruta]).por_rol.some((f: any) => f.rol === 'analista')).toBe(true)

  const ui = await $.ui.mount({ ...PANE, surface: 'terminal' })
  await ui.press({ key: 'tab-roles' })
  expect(await ui.find({ type: 'Text', text: /por rol/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /analista/ })).toBeDefined()
  await ui.unmount()
})

test('anotarAgente con tope pequeño expulsa por orden de inserción aunque t sea 0 o NaN', async () => {
  let mapa: Record<string, any> = {}
  mapa = anotarAgente(mapa, 'a', { rol: 'x', t: 50 }, 2)
  mapa = anotarAgente(mapa, 'b', { rol: 'x', t: NaN }, 2)
  mapa = anotarAgente(mapa, 'c', { rol: 'x', t: 0 }, 2)
  expect(Object.keys(mapa)).toEqual(['b', 'c'])
  mapa = anotarAgente(mapa, 'b', { rol: 'y', t: 0 }, 2) // renovar lo manda al final
  mapa = anotarAgente(mapa, 'd', { rol: 'x', t: 0 }, 2)
  expect(Object.keys(mapa)).toEqual(['b', 'd'])
})

test('el desborde a _otros convive con un registro viejo y cuenta ids únicos', async () => {
  const viejo: any = { id: 'v', t: 10, txt: 'x', cwd: '', mod: { m: [100, 100, 0, 0] }, sub: [40, 40, 0, 0], subN: 1, n: 1, ms: 0, nu: 0, p5: [null, null], p7: [null, null] }
  for (let i = 0; i < MAX_AGENTES_REG + 3; i++) acumularTurno(viejo, { ...USO_B, model: 'm' }, true, 0, 'ag-' + i)
  expect(viejo.sub_ag._otros).toBeDefined()
  const otro = nuevoRegistro({ id: 'o', t: 11, texto: '', limites: LIMITES })
  acumularTurno(otro, USO_B, true, 0, 'ag-0')
  const filas = porRol([viejo, otro], { 'ag-0': { rol: 'qa', modelo: 'haiku', esfuerzo: '', t: 1 } })
  expect(filas.find((f) => f.rol === 'qa').agentes).toBe(1)
  expect(sumaFrescos(filas)).toBe(frescos(usoRegistro(viejo)) + frescos(usoRegistro(otro)))
})

test('tool.call con effort y luego agent.spawn: el esfuerzo del spawn manda y el de tool.call es respaldo', async ($, on) => {
  const almacen: Record<string, unknown> = {}
  on('command.register', () => ({ value: undefined }))
  mock.clock(on)
  on('store.get', (_$, e) => ({ value: almacen[e.key] }))
  on('store.set', (_$, e) => {
    almacen[e.key] = e.value
    return { value: undefined }
  })
  on('session.start', () => ({ cwd: '/work/juego' }))
  on('session.usage', () => ({ value: { startedAt: 0, context: {}, rateLimits: [] } }))
  on('ui.status', () => ({ value: undefined }))
  let n = 0
  on('agent.spawn', () => ({ model: 'claude-opus-5-5', agentId: 'ag-' + ++n }))
  on('tool.call', () => ({ result: { agentId: 'x', content: [] } }))
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work/juego' })
  await $.tool.call({ tool: 'Agent', description: 'Uno', prompt: 'x', subagent_type: 'analista', effort: 'low', tool_use_id: 'tu-1' })
  await $.agent.spawn({ prompt: 'x', description: 'Uno', subagentType: 'analista', effort: 'high', tool_use_id: 'tu-1' } as any)
  await $.tool.call({ tool: 'Agent', description: 'Dos', prompt: 'x', subagent_type: 'qa', effort: 'medium', tool_use_id: 'tu-2' })
  await $.agent.spawn({ prompt: 'x', description: 'Dos', subagentType: 'qa', tool_use_id: 'tu-2' } as any)
  const ag = almacen.agentes as Record<string, any>
  expect(ag['ag-1'].esfuerzo).toBe('high')
  expect(ag['ag-2'].esfuerzo).toBe('medium')
})

test('el JSON exportado no contiene cwd ni ids de turno o agente', async () => {
  const reg = regConSubs()
  const json = JSON.stringify(construirExportacion([reg], MAPA, 9000))
  expect(json).not.toContain('carpeta-privada')
  for (const clave of ['"cwd"', '"id"', '"txt"', 'agentId', 'turnId', 'ag-b']) expect(json).not.toContain(clave)
})
