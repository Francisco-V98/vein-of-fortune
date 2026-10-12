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

// Parte un texto en líneas de un ancho aproximado en caracteres
export function envolverTexto(texto, max) {
  const palabras = String(texto).split(/\s+/).filter(Boolean)
  const lineas = []
  let actual = ''
  for (const p of palabras) {
    if ((actual + ' ' + p).trim().length > max && actual) {
      lineas.push(actual)
      actual = p
    } else {
      actual = (actual + ' ' + p).trim()
    }
  }
  if (actual) lineas.push(actual)
  return lineas
}

// Diagrama de traspasos de una tarea: una estación por etapa, con quién la hace, lo que entrega,
// los hallazgos que dejó y cómo los resolvió quien correspondía, y las flechas de «pasa a».
// Cada fila: { nombre, quien, indice, estado, nota, entrega, siguiente, hallazgos: [{ de, texto, estado, resuelto_por, como }] }
export function svgTraspasos(filas, ancho) {
  const W = Math.max(340, Math.min(ancho, 600))
  const xTexto = 60
  const maxChars = Math.max(30, Math.floor((W - xTexto - 14) / 6.2))
  const partes = []
  let y = 6
  const huecos = []
  filas.forEach((f, i) => {
    const lineasNota = f.nota ? envolverTexto(f.nota, maxChars) : []
    const lineasEntrega = f.entrega ? envolverTexto('Entrega: ' + f.entrega, maxChars) : []
    const bloquesHallazgo = (f.hallazgos || []).map((h) => {
      const abierto = h.estado !== 'resuelto'
      const titulo = envolverTexto((abierto ? 'Hallazgo' : 'Hallazgo resuelto') + ' · ' + h.de + ': ' + h.texto, maxChars - 4)
      const como = !abierto && h.como ? envolverTexto('Lo resolvió ' + (h.resuelto_por || '') + ': ' + h.como, maxChars - 4) : []
      return { abierto, titulo, como }
    })
    const altoHallazgos = bloquesHallazgo.reduce((a, b) => a + 12 + (b.titulo.length + b.como.length) * 14 + 6, 0)
    const alto = 46 + lineasNota.length * 14 + lineasEntrega.length * 14 + altoHallazgos
    const activa = f.estado === 'activa'
    const apagada = f.estado === 'pendiente' || f.estado === 'omitida'
    const cy = y + 22
    if (activa) {
      partes.push('<rect x="2" y="' + (y - 4) + '" width="' + (W - 4) + '" height="' + (alto + 4) + '" rx="12" fill="' + C.vino + '" fill-opacity="0.22" stroke="' + C.ambar + '" stroke-opacity="0.6"/>')
    }
    // avatar
    const color = AVATARES[(f.indice || 0) % AVATARES.length]
    partes.push('<circle cx="30" cy="' + cy + '" r="17" fill="' + (apagada ? C.fondo : color) + '" stroke="' + (activa ? C.ambar : f.estado === 'hecha' ? C.suave : C.borde) + '" stroke-width="3"' + (f.estado === 'omitida' ? ' stroke-dasharray="3 4"' : '') + '>' + (activa ? '<animate attributeName="stroke-opacity" values="1;0.3;1" dur="1.6s" repeatCount="indefinite"/>' : '') + '</circle>')
    partes.push(t(30, cy + 5, iniciales(f.quien), 13, apagada ? C.tenue : C.fondo, ' text-anchor="middle" font-weight="800"'))
    if (f.estado === 'hecha') {
      partes.push('<circle cx="43" cy="' + (cy - 13) + '" r="7" fill="' + C.suave + '" stroke="' + C.fondo + '" stroke-width="2"/>')
      partes.push('<path d="M40 ' + (cy - 13) + ' l2.4 2.6 l4.2 -5" fill="none" stroke="' + C.fondo + '" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')
    }
    // texto de la estación
    let ty = y + 18
    partes.push(t(xTexto, ty, f.nombre, 14, apagada ? C.tenue : C.texto, ' font-weight="' + (activa ? 800 : 700) + '"'))
    const etiqueta = (f.estado === 'activa' ? 'AHORA · ' : f.estado === 'omitida' ? 'omitida · ' : '') + f.quien
    partes.push(t(xTexto, ty + 15, etiqueta, 11, activa ? C.ambar : C.tenue, activa ? ' font-weight="700"' : ''))
    ty += 32
    for (const l of lineasNota) {
      partes.push(t(xTexto, ty, l, 12, C.suave))
      ty += 14
    }
    for (const l of lineasEntrega) {
      partes.push(t(xTexto, ty, l, 12, C.ambar, ' font-style="italic"'))
      ty += 14
    }
    for (const b of bloquesHallazgo) {
      const h = 6 + (b.titulo.length + b.como.length) * 14 + 6
      partes.push('<rect x="' + (xTexto - 2) + '" y="' + (ty - 2) + '" width="' + (W - xTexto - 8) + '" height="' + h + '" rx="8" fill="' + C.fondo + '" stroke="' + (b.abierto ? C.vinoClaro : C.borde) + '"/>')
      partes.push('<rect x="' + (xTexto - 2) + '" y="' + (ty - 2) + '" width="4" height="' + h + '" rx="2" fill="' + (b.abierto ? C.vinoClaro : C.suave) + '"/>')
      let by = ty + 12
      b.titulo.forEach((l, j) => {
        partes.push(t(xTexto + 10, by, (j === 0 ? (b.abierto ? '⚑ ' : '✓ ') : '') + l, 11, b.abierto ? C.texto : C.suave))
        by += 14
      })
      b.como.forEach((l) => {
        partes.push(t(xTexto + 10, by, l, 11, C.ambar))
        by += 14
      })
      ty += h + 6
    }
    // flecha hacia la siguiente estación
    const finY = y + alto
    if (i < filas.length - 1) {
      const sig = filas[i + 1]
      const hecha = f.estado === 'hecha' || f.estado === 'omitida'
      partes.push('<line x1="30" y1="' + (cy + 20) + '" x2="30" y2="' + (finY + 14) + '" stroke="' + (hecha ? C.suave : C.borde) + '" stroke-width="2"' + (hecha ? '' : ' stroke-dasharray="3 4"') + '/>')
      partes.push('<polygon points="25,' + (finY + 12) + ' 35,' + (finY + 12) + ' 30,' + (finY + 20) + '" fill="' + (hecha ? C.suave : C.borde) + '"/>')
      huecos.push(t(xTexto, finY + 14, 'pasa a ' + sig.quien, 10, sig.estado === 'activa' ? C.ambar : C.tenue))
    }
    y += alto + 24
  })
  return { svg: envolver(W, y, partes.concat(huecos)), alto: y, ancho: W }
}

// ---------- la oficina: un estudio en planta, con empleados que trabajan y paquetes que viajan ----------

const COLOR_DEPTO = {
  direccion: '#B8893A',
  estrategia: '#8FB0BA',
  diseno: '#C23B55',
  narrativa: '#E3B25C',
  arte: '#9A2640',
  ingenieria: '#5B7C8C',
  calidad: '#36505F',
}
const PELO = ['#2b2b33', '#6b4a2f', '#c9a15a', '#8a3b2e', '#d8d8d8', '#3b3b55', '#7a5a3a']

// Un empleado sentado en su escritorio. estado: 'trabajando' | 'libre' | 'reserva'
function empleado(x, y, rol, indice, estado, tarea, pendientes) {
  const cx = x + 44
  const color = COLOR_DEPTO[rol.depto] || C.tenue
  const pelo = PELO[indice % PELO.length]
  const p = []
  const reserva = estado === 'reserva'
  p.push('<g opacity="' + (reserva ? 0.45 : 1) + '">')
  // escritorio y monitor
  p.push('<rect x="' + (x + 12) + '" y="' + (y + 50) + '" width="64" height="18" rx="4" fill="#27394a" stroke="' + C.borde + '"/>')
  p.push('<rect x="' + (x + 12) + '" y="' + (y + 50) + '" width="64" height="4" rx="2" fill="#36505F"/>')
  p.push('<rect x="' + (cx - 11) + '" y="' + (y + 36) + '" width="22" height="15" rx="2" fill="#0e161d" stroke="' + (estado === 'trabajando' ? C.ambar : C.borde) + '"/>')
  if (estado === 'trabajando') {
    p.push('<rect x="' + (cx - 8) + '" y="' + (y + 39) + '" width="16" height="9" rx="1" fill="' + C.texto + '"><animate attributeName="opacity" values="0.9;0.35;0.8;0.4;0.9" dur="1.1s" repeatCount="indefinite"/></rect>')
  } else if (!reserva) {
    p.push('<rect x="' + (cx - 8) + '" y="' + (y + 39) + '" width="16" height="9" rx="1" fill="' + C.borde + '"/>')
  }
  // persona
  const cuerpo = reserva ? 'none' : color
  const piel = reserva ? 'none' : '#E8B98F'
  const trazo = reserva ? ' stroke="' + C.tenue + '" stroke-dasharray="2 3"' : ''
  p.push('<g>')
  if (estado === 'trabajando') p.push('<animateTransform attributeName="transform" type="translate" values="0 0;0 -1.5;0 0" dur="0.6s" repeatCount="indefinite"/>')
  p.push('<rect x="' + (cx - 8) + '" y="' + (y + 28) + '" width="16" height="12" rx="3" fill="' + cuerpo + '"' + trazo + '/>')
  p.push('<rect x="' + (cx - 5) + '" y="' + (y + 16) + '" width="10" height="11" rx="3" fill="' + piel + '"' + trazo + '/>')
  if (!reserva) {
    p.push('<rect x="' + (cx - 6) + '" y="' + (y + 14) + '" width="12" height="5" rx="2" fill="' + pelo + '"/>')
    if (estado === 'trabajando') {
      p.push('<rect x="' + (cx - 3) + '" y="' + (y + 21) + '" width="2" height="2" fill="#17232C"/><rect x="' + (cx + 1) + '" y="' + (y + 21) + '" width="2" height="2" fill="#17232C"/>')
    } else {
      p.push('<rect x="' + (cx - 3) + '" y="' + (y + 22) + '" width="2" height="1" fill="#17232C"/><rect x="' + (cx + 1) + '" y="' + (y + 22) + '" width="2" height="1" fill="#17232C"/>')
    }
  }
  p.push('</g>')
  // brazos que teclean
  if (estado === 'trabajando') {
    p.push('<rect x="' + (cx - 12) + '" y="' + (y + 40) + '" width="5" height="4" fill="#E8B98F"><animate attributeName="y" values="' + (y + 40) + ';' + (y + 43) + ';' + (y + 40) + '" dur="0.35s" repeatCount="indefinite"/></rect>')
    p.push('<rect x="' + (cx + 7) + '" y="' + (y + 43) + '" width="5" height="4" fill="#E8B98F"><animate attributeName="y" values="' + (y + 43) + ';' + (y + 40) + ';' + (y + 43) + '" dur="0.35s" repeatCount="indefinite"/></rect>')
  }
  p.push('</g>')
  // z z z cuando está libre
  if (estado === 'libre') {
    p.push('<text x="' + (cx + 8) + '" y="' + (y + 14) + '" font-family="' + FUENTE + '" font-size="10" font-weight="700" fill="' + C.tenue + '">z<animate attributeName="opacity" values="0;1;0" dur="2.4s" repeatCount="indefinite"/><animateTransform attributeName="transform" type="translate" values="0 0;5 -8" dur="2.4s" repeatCount="indefinite"/></text>')
  }
  // globo con la tarea en la que trabaja
  if (estado === 'trabajando' && tarea) {
    const w = Math.round(tarea.length * 6.2 + 12)
    p.push('<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -2;0 0" dur="1.8s" repeatCount="indefinite"/>')
    p.push('<rect x="' + (cx - w / 2) + '" y="' + (y - 6) + '" width="' + w + '" height="16" rx="8" fill="' + C.ambar + '"/>')
    p.push('<polygon points="' + (cx - 4) + ',' + (y + 10) + ' ' + (cx + 4) + ',' + (y + 10) + ' ' + cx + ',' + (y + 15) + '" fill="' + C.ambar + '"/>')
    p.push(t(cx, y + 6, tarea, 10, C.fondo, ' text-anchor="middle" font-weight="800"'))
    p.push('</g>')
  }
  // bandeja con pendientes (solo el autor)
  if (rol.tipo === 'humano') {
    p.push('<rect x="' + (x + 58) + '" y="' + (y + 44) + '" width="16" height="7" rx="1" fill="#C9DCDF"/><rect x="' + (x + 60) + '" y="' + (y + 41) + '" width="12" height="4" fill="#8FB0BA"/>')
    if (pendientes > 0) {
      p.push('<circle cx="' + (x + 74) + '" cy="' + (y + 38) + '" r="8" fill="' + C.vinoClaro + '" stroke="' + C.fondo + '" stroke-width="2"><animate attributeName="r" values="8;10;8" dur="1.2s" repeatCount="indefinite"/></circle>')
      p.push(t(x + 74, y + 42, pendientes, 10, C.texto, ' text-anchor="middle" font-weight="800"'))
    }
  }
  // placa con el nombre
  p.push(t(cx, y + 80, reserva ? rol.corto + ' · ' + rol.desde : rol.corto, 10, estado === 'trabajando' ? C.ambar : reserva ? C.tenue : C.suave, ' text-anchor="middle" font-weight="' + (estado === 'trabajando' ? 700 : 500) + '"'))
  return p.join('')
}

// Plano de oficina completo. Devuelve { svg, alto, ancho, centros } donde centros[rol] = {x, y}
export function svgOficina(op) {
  const W = Math.max(360, Math.min(op.ancho, 600))
  const margen = 8
  const capacidad = 6
  const celda = Math.floor((W - margen * 3 - 16) / capacidad)
  const altoSala = 26 + 108 + 6
  const partes = []
  const centros = {}
  const salas = op.deptos.map((d) => ({ depto: d, roles: op.roles.filter((r) => r.depto === d.id) })).filter((s) => s.roles.length > 0)
  // empaqueta las salas por filas de hasta `capacidad` escritorios
  const filas = []
  let actual = []
  let usados = 0
  for (const sala of salas) {
    if (usados + sala.roles.length > capacidad && actual.length) {
      filas.push({ salas: actual, usados })
      actual = []
      usados = 0
    }
    actual.push(sala)
    usados += sala.roles.length
  }
  if (actual.length) filas.push({ salas: actual, usados })
  const alto = margen + filas.length * (altoSala + margen)
  partes.push('<defs><pattern id="suelo" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" fill="' + C.fondo + '"/><rect width="8" height="8" fill="#1b2a35"/><rect x="8" y="8" width="8" height="8" fill="#1b2a35"/></pattern></defs>')
  partes.push('<rect width="' + W + '" height="' + alto + '" rx="14" fill="url(#suelo)"/>')
  const capaSalas = []
  let ultimaLibre = null
  filas.forEach((fila, fi) => {
    const y = margen + fi * (altoSala + margen)
    // reparte el ancho sobrante entre las salas de la fila
    const ancho = W - margen * (fila.salas.length + 1)
    let x = margen
    fila.salas.forEach((sala) => {
      const w = Math.round((ancho * sala.roles.length) / (fila.usados + (fi === filas.length - 1 && fila.usados < capacidad ? capacidad - fila.usados : 0)))
      const activa = sala.roles.some((r) => op.estado[r.id] === 'trabajando')
      capaSalas.push('<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + altoSala + '" rx="12" fill="' + C.tarjeta + '" fill-opacity="0.85" stroke="' + (activa ? C.ambar : C.borde) + '"/>')
      capaSalas.push('<rect x="' + (x + 10) + '" y="' + (y + 9) + '" width="6" height="6" rx="1.5" fill="' + (COLOR_DEPTO[sala.depto.id] || C.tenue) + '"/>')
      capaSalas.push(t(x + 22, y + 16, sala.depto.nombre.toUpperCase(), 10, C.suave, ' font-weight="700" letter-spacing="0.8"'))
      const cw = w / sala.roles.length
      sala.roles.forEach((rol, k) => {
        const ex = x + k * cw + (cw - 88) / 2
        const ey = y + 46
        const cx = ex + 44
        centros[rol.id] = { x: cx, y: ey + 52 }
        const est = op.estado[rol.id] || 'libre'
        capaSalas.push('<g transform="translate(' + cx + ' ' + (ey + 80) + ') scale(1.2) translate(' + -cx + ' ' + -(ey + 80) + ')">' + empleado(ex, ey, rol, op.roles.indexOf(rol), est, op.tarea[rol.id] || '', rol.tipo === 'humano' ? op.pendientesAutor : 0) + '</g>')
      })
      x += w + margen
    })
    if (fi === filas.length - 1 && fila.usados < capacidad) ultimaLibre = { x, y, w: W - margen - x }
  })
  partes.push(capaSalas.join(''))

  // la ruta de la tarea elegida: paquetes que viajan entre escritorios
  const capaRuta = []
  const ruta = op.ruta || []
  for (let i = 0; i < ruta.length - 1; i++) {
    const a = centros[ruta[i].rol]
    const b = centros[ruta[i + 1].rol]
    if (!a || !b || ruta[i].rol === ruta[i + 1].rol) continue
    const hecho = ruta[i].estado === 'hecha' || ruta[i].estado === 'omitida'
    const hacia = ruta[i + 1].estado === 'activa'
    const medioY = Math.min(a.y, b.y) - 44 - (i % 2) * 16
    const d = 'M' + a.x + ',' + (a.y - 16) + ' C' + a.x + ',' + medioY + ' ' + b.x + ',' + medioY + ' ' + b.x + ',' + (b.y - 16)
    const color = hecho ? C.suave : hacia ? C.ambar : C.borde
    capaRuta.push('<path d="' + d + '" fill="none" stroke="' + color + '" stroke-width="' + (hecho || hacia ? 2.5 : 2) + '" stroke-linecap="round" stroke-opacity="' + (hecho || hacia ? 0.9 : 0.7) + '" stroke-dasharray="' + (hecho ? '' : '6 6') + '"' + (hacia ? '><animate attributeName="stroke-dashoffset" values="12;0" dur="0.7s" repeatCount="indefinite"/></path>' : '/>'))
    capaRuta.push('<circle cx="' + b.x + '" cy="' + (b.y - 16) + '" r="4" fill="' + color + '"/>')
    if (hecho || hacia) {
      capaRuta.push('<g><rect x="-6" y="-5" width="12" height="10" rx="2" fill="' + C.laton + '" stroke="' + C.ambar + '"/><rect x="-6" y="-1" width="12" height="2" fill="' + C.ambar + '"/><animateMotion dur="' + (hacia ? 1.8 : 3.6) + 's" begin="' + i * 0.4 + 's" repeatCount="indefinite" path="' + d + '"/></g>')
    }
  }
  // hallazgos: la bandera va de quien lo dejó a quien lo resolvió; los abiertos laten sobre quien lo dejó
  for (const h of op.hallazgos || []) {
    const a = centros[h.de]
    if (!a) continue
    if (h.estado === 'resuelto' && centros[h.a] && h.de !== h.a) {
      const b = centros[h.a]
      const medioY = Math.min(a.y, b.y) - 24
      const d = 'M' + a.x + ',' + (a.y - 24) + ' Q' + (a.x + b.x) / 2 + ',' + medioY + ' ' + b.x + ',' + (b.y - 24)
      capaRuta.push('<path d="' + d + '" fill="none" stroke="' + C.vinoClaro + '" stroke-opacity="0.55" stroke-width="1.5" stroke-dasharray="3 4"/>')
      capaRuta.push('<g><polygon points="0,-7 9,-3.5 0,0" fill="' + C.vinoClaro + '"/><rect x="-1" y="-7" width="1.8" height="12" fill="' + C.texto + '"/><animateMotion dur="4.5s" repeatCount="indefinite" path="' + d + '"/></g>')
    } else if (h.estado !== 'resuelto') {
      capaRuta.push('<g><circle cx="' + (a.x + 26) + '" cy="' + (a.y - 34) + '" r="8" fill="' + C.vinoClaro + '" stroke="' + C.fondo + '" stroke-width="2"><animate attributeName="r" values="8;10;8" dur="1s" repeatCount="indefinite"/></circle>' + t(a.x + 26, a.y - 30, '!', 11, C.texto, ' text-anchor="middle" font-weight="800"') + '</g>')
    }
  }
  partes.push(capaRuta.join(''))

  // leyenda en el hueco que queda en la última fila
  if (ultimaLibre && ultimaLibre.w > 120) {
    const { x: lx, y: ly, w } = ultimaLibre
    const items = [
      ['paquete', 'Un paquete: el trabajo pasa de uno a otro'],
      ['bandera', 'Una bandera: un hallazgo y quién lo resolvió'],
      ['alerta', 'Un hallazgo sin resolver'],
      ['reserva', 'Sin color: se une en su fase'],
    ]
    partes.push('<rect x="' + lx + '" y="' + ly + '" width="' + w + '" height="' + altoSala + '" rx="12" fill="' + C.tarjeta + '" fill-opacity="0.6" stroke="' + C.borde + '"/>')
    partes.push(t(lx + 12, ly + 17, 'CÓMO LEERLO', 10, C.suave, ' font-weight="700" letter-spacing="0.8"'))
    items.forEach(([k, texto], i) => {
      const iy = ly + 38 + i * 19
      if (k === 'paquete') partes.push('<rect x="' + (lx + 12) + '" y="' + (iy - 8) + '" width="12" height="10" rx="2" fill="' + C.laton + '" stroke="' + C.ambar + '"/>')
      if (k === 'bandera') partes.push('<polygon points="' + (lx + 14) + ',' + (iy - 9) + ' ' + (lx + 24) + ',' + (iy - 5) + ' ' + (lx + 14) + ',' + (iy - 1) + '" fill="' + C.vinoClaro + '"/><rect x="' + (lx + 13) + '" y="' + (iy - 9) + '" width="1.8" height="12" fill="' + C.texto + '"/>')
      if (k === 'alerta') partes.push('<circle cx="' + (lx + 18) + '" cy="' + (iy - 3) + '" r="6" fill="' + C.vinoClaro + '"/>')
      if (k === 'reserva') partes.push('<rect x="' + (lx + 12) + '" y="' + (iy - 9) + '" width="12" height="11" rx="3" fill="none" stroke="' + C.tenue + '" stroke-dasharray="2 3"/>')
      partes.push(t(lx + 32, iy, recortar(texto, Math.floor((w - 44) / 5.4)), 10, C.suave))
    })
    partes.push(t(lx + 12, ly + altoSala - 8, recortar(op.pie || '', Math.floor((w - 20) / 5.2)), 10, C.tenue))
  }
  return { svg: envolver(W, alto, partes), alto, ancho: W, centros }
}
