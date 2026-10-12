// Dibujos del panel de estado: SVG para la app de escritorio. Funciones puras, sin acceso al mods API.

export const C = {
  fondo: '#17232C',
  tarjeta: '#22333F',
  borde: '#36505F',
  texto: '#C9DCDF',
  suave: '#8FB0BA',
  tenue: '#5B7C8C',
  vino: '#9A2640',
  vinoClaro: '#C23B55',
  laton: '#B8893A',
  ambar: '#E3B25C',
}

// Un color por estado, siempre acompañado de su nombre para no depender solo del color
export const COLOR_ESTADO = {
  backlog: '#36505F',
  sprint: '#5B7C8C',
  doing: '#E3B25C',
  review: '#C23B55',
  qa: '#B8893A',
  done: '#8FB0BA',
}

const FUENTE = 'system-ui, -apple-system, Segoe UI, sans-serif'

export function esc(texto) {
  return String(texto).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

// Recorta un texto a un número aproximado de caracteres
export function recortar(texto, max) {
  const t = String(texto)
  return t.length > max ? t.slice(0, Math.max(1, max - 1)) + '…' : t
}

function t(x, y, texto, tam, color, extra) {
  return '<text x="' + x + '" y="' + y + '" font-family="' + FUENTE + '" font-size="' + tam + '" fill="' + color + '"' + (extra || '') + '>' + esc(texto) + '</text>'
}

function envolver(ancho, alto, partes) {
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + ancho + ' ' + alto + '" width="' + ancho + '" height="' + alto + '">' + partes.join('') + '</svg>'
}

function pildora(x, y, texto, relleno, colorTexto) {
  const w = Math.round(texto.length * 6.4 + 18)
  return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="22" rx="11" fill="' + relleno + '"/>' + t(x + 9, y + 15, texto, 11, colorTexto, ' font-weight="600"') + '|' + w
}

// Tarjeta de avance: anillo con el porcentaje y las cifras clave
export function svgResumen(r, ancho) {
  const W = ancho
  const H = 156
  const p = r.n > 0 ? r.hechas / r.n : 0
  const radio = 46
  const largo = 2 * Math.PI * radio
  const partes = []
  partes.push('<rect x="0.5" y="0.5" width="' + (W - 1) + '" height="' + (H - 1) + '" rx="14" fill="' + C.tarjeta + '" stroke="' + C.borde + '"/>')
  partes.push('<circle cx="76" cy="78" r="' + radio + '" fill="none" stroke="' + C.fondo + '" stroke-width="14"/>')
  partes.push(
    '<circle cx="76" cy="78" r="' + radio + '" fill="none" stroke="' + C.ambar + '" stroke-width="14" stroke-linecap="round" stroke-dasharray="' +
      (p * largo).toFixed(1) + ' ' + largo.toFixed(1) + '" transform="rotate(-90 76 78)"/>',
  )
  partes.push(t(76, 84, Math.round(p * 100) + ' %', 22, C.texto, ' text-anchor="middle" font-weight="700"'))
  partes.push(t(150, 40, 'Avance del proyecto', 16, C.texto, ' font-weight="700"'))
  partes.push(t(150, 62, r.hechas + ' de ' + r.n + ' tareas hechas', 13, C.suave))
  const horas = r.est > 0 ? Math.round((r.estHechas / r.est) * 100) : 0
  partes.push(t(150, 82, horas + ' % por horas estimadas · ' + Math.round(r.estHechas) + ' de ' + Math.round(r.est) + ' h', 12, C.tenue))
  let x = 150
  const fichas = [
    ['En revisión ' + r.porEstado.review, C.vinoClaro, C.texto],
    ['En curso ' + (r.porEstado.doing + r.porEstado.sprint), C.ambar, C.fondo],
    ['En QA ' + r.porEstado.qa, C.laton, C.fondo],
  ]
  for (const [texto, relleno, color] of fichas) {
    const hecho = pildora(x, 104, texto, relleno, color).split('|')
    partes.push(hecho[0])
    x += Number(hecho[1]) + 8
  }
  return envolver(W, H, partes)
}

// Barra apilada con todos los estados y su leyenda
export function svgEstados(porEstado, orden, etiquetas, ancho) {
  const W = ancho
  const total = orden.reduce((a, e) => a + porEstado[e], 0) || 1
  const partes = []
  let x = 0
  const barraW = W
  partes.push('<clipPath id="e"><rect x="0" y="0" width="' + barraW + '" height="16" rx="8"/></clipPath><g clip-path="url(#e)">')
  for (const e of orden) {
    const w = (porEstado[e] / total) * barraW
    if (w <= 0) continue
    partes.push('<rect x="' + x.toFixed(1) + '" y="0" width="' + Math.max(w, 3).toFixed(1) + '" height="16" fill="' + COLOR_ESTADO[e] + '"/>')
    x += w
  }
  partes.push('</g>')
  const col = Math.floor(W / 3)
  orden.forEach((e, i) => {
    const cx = (i % 3) * col
    const cy = 34 + Math.floor(i / 3) * 22
    partes.push('<rect x="' + cx + '" y="' + (cy - 9) + '" width="10" height="10" rx="3" fill="' + COLOR_ESTADO[e] + '"/>')
    partes.push(t(cx + 16, cy, etiquetas[e] + ' ' + porEstado[e], 12, C.suave))
  })
  return envolver(W, 78, partes)
}

// Medidores de calidad con la marca de la meta
export function svgMedidas(m, ancho) {
  const W = ancho
  const filas = [
    ['Limpieza del diseño', m && m.limpieza !== null ? m.limpieza : null, C.ambar, 90],
    ['Coherencia', m && m.coherencia !== null ? m.coherencia : null, C.suave, null],
  ]
  const partes = []
  const x0 = 0
  const pistaW = W - 0
  filas.forEach(([nombre, valor, color, meta], i) => {
    const y = i * 52
    partes.push(t(x0, y + 14, nombre, 13, C.texto, ' font-weight="600"'))
    partes.push(t(W, y + 14, valor === null ? 'sin datos' : valor + ' %', 13, valor === null ? C.tenue : C.texto, ' text-anchor="end" font-weight="700"'))
    partes.push('<rect x="0" y="' + (y + 24) + '" width="' + pistaW + '" height="12" rx="6" fill="' + C.fondo + '"/>')
    if (valor !== null) partes.push('<rect x="0" y="' + (y + 24) + '" width="' + Math.max(12, (valor / 100) * pistaW).toFixed(1) + '" height="12" rx="6" fill="' + color + '"/>')
    if (meta) {
      const mx = (meta / 100) * pistaW
      partes.push('<rect x="' + (mx - 1) + '" y="' + (y + 20) + '" width="2" height="20" fill="' + C.vinoClaro + '"/>')
      partes.push(t(mx, y + 52, 'meta ' + meta + ' %', 10, C.vinoClaro, ' text-anchor="middle"'))
    } else if (m && m.hallazgos !== null && m.hallazgos !== undefined) {
      partes.push(t(W, y + 52, m.hallazgos + ' hallazgos de ' + m.comprobaciones + ' comprobaciones', 10, C.tenue, ' text-anchor="end"'))
    }
  })
  return envolver(W, 106, partes)
}

// Filas de barras: sirve para fases e hitos. Cada fila: { codigo, nombre, hechas, n }
export function svgFilas(filas, ancho, opciones) {
  const W = ancho
  const alto = (opciones && opciones.alto) || 30
  const colCodigo = (opciones && opciones.colCodigo) || 44
  const colCifra = 78
  const barraX = colCodigo + 150
  const barraW = Math.max(60, W - barraX - colCifra)
  const partes = []
  filas.forEach((f, i) => {
    const y = i * alto
    const p = f.n > 0 ? f.hechas / f.n : 0
    const completa = f.n > 0 && f.hechas === f.n
    partes.push(t(0, y + 17, f.codigo, 12, completa ? C.ambar : C.texto, ' font-weight="700"'))
    partes.push(t(colCodigo, y + 17, recortar(f.nombre, 24), 12, f.hechas === 0 ? C.tenue : C.suave))
    partes.push('<rect x="' + barraX + '" y="' + (y + 8) + '" width="' + barraW + '" height="10" rx="5" fill="' + C.fondo + '"/>')
    if (p > 0) partes.push('<rect x="' + barraX + '" y="' + (y + 8) + '" width="' + Math.max(10, p * barraW).toFixed(1) + '" height="10" rx="5" fill="' + (completa ? C.ambar : C.suave) + '"/>')
    partes.push(t(W, y + 17, f.hechas + '/' + f.n + (completa ? ' ✓' : ''), 12, completa ? C.ambar : C.texto, ' text-anchor="end"'))
  })
  return envolver(W, Math.max(alto, filas.length * alto), partes)
}
