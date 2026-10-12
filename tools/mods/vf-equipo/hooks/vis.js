// Dibujos del tablero del equipo: SVG para la app de escritorio. Funciones puras, sin acceso al mods API.

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

// Colores para los avatares de los roles, siempre con iniciales para no depender solo del color
const AVATARES = ['#C23B55', '#B8893A', '#5B7C8C', '#8FB0BA', '#9A2640', '#E3B25C', '#36505F', '#B8893A', '#C23B55']

const FUENTE = 'system-ui, -apple-system, Segoe UI, sans-serif'

export function esc(texto) {
  return String(texto).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

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

// Iniciales de un nombre de rol: «Diseñador de sistemas» → DS
export function iniciales(nombre) {
  const palabras = String(nombre).replace(/\(.*\)/, '').split(/\s+/).filter((p) => p.length > 2)
  if (palabras.length === 0) return String(nombre).slice(0, 2).toUpperCase()
  if (palabras.length === 1) return palabras[0].slice(0, 2).toUpperCase()
  return (palabras[0][0] + palabras[1][0]).toUpperCase()
}

// El flujo: una estación por etapa, con el número de tareas y un aro punteado donde participa el autor
export function svgFlujo(etapas, conteo, humanas, ancho) {
  const W = Math.max(360, Math.min(ancho, 600))
  const H = 128
  const paso = W / etapas.length
  const partes = []
  partes.push('<rect x="0.5" y="0.5" width="' + (W - 1) + '" height="' + (H - 1) + '" rx="14" fill="' + C.tarjeta + '" stroke="' + C.borde + '"/>')
  etapas.forEach((e, i) => {
    const cx = Math.round(paso * i + paso / 2)
    const n = conteo[e.id] || 0
    if (i < etapas.length - 1) {
      partes.push('<line x1="' + (cx + 25) + '" y1="52" x2="' + (cx + paso - 25) + '" y2="52" stroke="' + C.tenue + '" stroke-width="2"/>')
      partes.push('<polygon points="' + (cx + paso - 25) + ',47 ' + (cx + paso - 17) + ',52 ' + (cx + paso - 25) + ',57" fill="' + C.tenue + '"/>')
    }
    if (humanas.includes(e.id)) partes.push('<circle cx="' + cx + '" cy="52" r="30" fill="none" stroke="' + C.laton + '" stroke-width="2" stroke-dasharray="3 5"/>')
    partes.push('<circle cx="' + cx + '" cy="52" r="23" fill="' + (n > 0 ? C.vino : C.fondo) + '" stroke="' + (n > 0 ? C.ambar : C.borde) + '" stroke-width="3"/>')
    partes.push(t(cx, 59, e.glifo, 20, n > 0 ? C.texto : C.suave, ' text-anchor="middle" font-weight="700"'))
    if (n > 0) {
      partes.push('<circle cx="' + (cx + 19) + '" cy="31" r="10" fill="' + C.ambar + '"/>')
      partes.push(t(cx + 19, 35, n, 12, C.fondo, ' text-anchor="middle" font-weight="700"'))
    }
    const nombre = e.nombre.replace('Revisión del autor', 'Revisión').replace('Prueba del autor', 'Prueba')
    partes.push(t(cx, 104, nombre, 11, n > 0 ? C.texto : C.tenue, ' text-anchor="middle" font-weight="' + (n > 0 ? 600 : 400) + '"'))
    partes.push(t(cx, 118, n === 1 ? '1 tarea' : n > 1 ? n + ' tareas' : '—', 10, n > 0 ? C.ambar : C.tenue, ' text-anchor="middle"'))
  })
  return envolver(W, H, partes)
}

// Quién trabaja ahora: un punto que parpadea por cada especialista activo
export function svgAhora(vivos, ancho) {
  const W = Math.max(300, Math.min(ancho, 600))
  const H = Math.max(40, 12 + vivos.length * 26)
  const partes = []
  partes.push('<rect x="0.5" y="0.5" width="' + (W - 1) + '" height="' + (H - 1) + '" rx="12" fill="' + C.tarjeta + '" stroke="' + C.borde + '"/>')
  if (vivos.length === 0) {
    partes.push('<circle cx="22" cy="20" r="5" fill="' + C.borde + '"/>')
    partes.push(t(38, 24, 'Nadie trabaja ahora en esta sesión', 12, C.tenue))
  }
  vivos.forEach((v, i) => {
    const y = 22 + i * 26
    partes.push('<circle cx="22" cy="' + y + '" r="5" fill="' + C.ambar + '"><animate attributeName="opacity" values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/></circle>')
    partes.push(t(38, y + 4, v.nombre, 13, C.texto, ' font-weight="700"'))
    if (v.detalle) partes.push(t(38 + Math.round(v.nombre.length * 7.2) + 10, y + 4, recortar(v.detalle, 38), 12, C.suave))
  })
  return envolver(W, H, partes)
}

// Avatar de un rol: círculo con sus iniciales; punto ámbar si está trabajando
export function svgAvatar(nombre, indice, activo, humano) {
  const color = AVATARES[indice % AVATARES.length]
  const partes = []
  partes.push('<circle cx="24" cy="24" r="20" fill="' + color + '" stroke="' + (humano ? C.ambar : C.fondo) + '" stroke-width="3"' + (humano ? ' stroke-dasharray="4 4"' : '') + '/>')
  partes.push(t(24, 30, iniciales(nombre), 15, C.fondo, ' text-anchor="middle" font-weight="800"'))
  if (activo) partes.push('<circle cx="40" cy="8" r="6" fill="' + C.ambar + '" stroke="' + C.fondo + '" stroke-width="2"/>')
  return envolver(48, 48, partes)
}

// Línea de tiempo de una tarea: una fila por etapa con su estado, quién la hace y la nota
export function svgLinea(filas, ancho) {
  const W = Math.max(320, Math.min(ancho, 600))
  const alto = 54
  const H = filas.length * alto + 8
  const partes = []
  filas.forEach((f, i) => {
    const y = 8 + i * alto
    const cy = y + 18
    if (i < filas.length - 1) {
      const hecha = f.estado === 'hecha' || f.estado === 'omitida'
      partes.push('<line x1="18" y1="' + (cy + 12) + '" x2="18" y2="' + (cy + alto - 12) + '" stroke="' + (hecha ? C.suave : C.borde) + '" stroke-width="2"' + (hecha ? '' : ' stroke-dasharray="3 4"') + '/>')
    }
    if (f.estado === 'hecha') {
      partes.push('<circle cx="18" cy="' + cy + '" r="11" fill="' + C.suave + '"/>')
      partes.push('<path d="M13 ' + cy + ' l4 4 l7 -8" fill="none" stroke="' + C.fondo + '" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    } else if (f.estado === 'activa') {
      partes.push('<circle cx="18" cy="' + cy + '" r="13" fill="' + C.vino + '" stroke="' + C.ambar + '" stroke-width="3"><animate attributeName="stroke-opacity" values="1;0.35;1" dur="1.6s" repeatCount="indefinite"/></circle>')
      partes.push('<circle cx="18" cy="' + cy + '" r="4" fill="' + C.ambar + '"/>')
    } else if (f.estado === 'omitida') {
      partes.push('<circle cx="18" cy="' + cy + '" r="9" fill="none" stroke="' + C.tenue + '" stroke-width="2" stroke-dasharray="2 3"/>')
      partes.push('<line x1="14" y1="' + cy + '" x2="22" y2="' + cy + '" stroke="' + C.tenue + '" stroke-width="2"/>')
    } else {
      partes.push('<circle cx="18" cy="' + cy + '" r="9" fill="none" stroke="' + C.borde + '" stroke-width="2.5"/>')
    }
    const apagada = f.estado === 'pendiente' || f.estado === 'omitida'
    partes.push(t(42, cy - 2, f.nombre, 14, apagada ? C.tenue : C.texto, ' font-weight="' + (f.estado === 'activa' ? 800 : 600) + '"'))
    const etiqueta = f.estado === 'omitida' ? 'omitida · ' + f.quien : f.quien
    partes.push(t(42, cy + 14, etiqueta, 11, f.estado === 'activa' ? C.ambar : C.tenue))
    if (f.nota) partes.push(t(42 + Math.round(etiqueta.length * 6) + 12, cy + 14, recortar(f.nota, 42), 11, C.suave))
  })
  return envolver(W, H, partes)
}
