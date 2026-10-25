/* Hub del estudio: sitio local sin dependencias externas.
   Los datos vienen de data.js (generado por build.py).
   El estado de las tareas NO se cambia desde aquí: vive en los archivos de datos. */
(function () {
  'use strict';

  var H = window.HUB;
  var main = document.getElementById('main');
  if (!H) {
    main.innerHTML = '<div class="notice"><strong>No se encontró data.js.</strong> Ejecuta <code>python3 studio/hub/build.py</code> y recarga la página.</div>';
    return;
  }

  /* ---------- utilidades ---------- */
  var STATUS = {
    backlog: { label: 'Backlog', glyph: '○' },
    sprint: { label: 'Sprint', glyph: '◔' },
    doing: { label: 'En proceso', glyph: '◐' },
    review: { label: 'Revisión', glyph: '◕' },
    qa: { label: 'QA', glyph: '◈' },
    done: { label: 'Finalizada', glyph: '●' },
    dropped: { label: 'Desestimada', glyph: '✕' }
  };
  var STATUS_ORDER = ['backlog', 'sprint', 'doing', 'review', 'qa', 'done', 'dropped'];
  var QUEUE_ORDER = { doing: 0, qa: 1, review: 2, sprint: 3, backlog: 4 };
  var AUTHOR = { autor: 'Autor', claude: 'Claude' };
  var PRIOS = ['P0', 'P1', 'P2', 'P3'];
  var PRANK = { P0: 0, P1: 1, P2: 2, P3: 3 };
  var PRIO_LABEL = (H.roadmap.meta && H.roadmap.meta.priorities) || {
    P0: 'Indispensable', P1: 'Importante', P2: 'Deseable', P3: 'Opcional'
  };
  var SCOPES = [
    { key: 'all', label: 'Todo', max: 3, hint: 'P0 a P3' },
    { key: 'P2', label: 'P0–P2', max: 2, hint: 'sin lo opcional' },
    { key: 'P1', label: 'P0–P1', max: 1, hint: 'indispensable e importante' },
    { key: 'P0', label: 'Solo P0', max: 0, hint: 'solo lo indispensable' }
  ];
  var PRIO_COLOR = { P0: '#c23b55', P1: '#e3b25c', P2: '#8fb0ba', P3: '#5b7c8c' };

  function $$(sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function foldChar(ch) {
    if (ch.length !== 1) return ch;
    var f = ch.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
    return f.length === 1 ? f : ch;
  }
  function fold(s) { return Array.from(String(s)).map(foldChar).join(''); }
  function slug(s) {
    return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase()
      .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'seccion';
  }
  function num(n) { return Number.isInteger(n) ? String(n) : n.toFixed(1); }
  function targetClass(t) { return 't-' + String(t).split(' ')[0]; }
  function safeUrl(u) { return /^https?:\/\//.test(u) ? u : '#'; }
  function $(sel, el) { return (el || document).querySelector(sel); }
  function $all(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }

  /* ---------- markdown (subconjunto usado en los documentos) ---------- */
  function mdLink(text, href) {
    var adr = href.match(/^(?:adr\/)?(\d{4}-[\w-]+)\.md(?:#(.+))?$/);
    if (adr) return '<a href="#/docs/adr-' + adr[1] + (adr[2] ? '?h=' + adr[2] : '') + '">' + text + '</a>';
    var m = href.replace(/^\.\.\//, '').match(/^(\d{2}-[\w-]+)\.md(?:#(.+))?$/);
    if (m) return '<a href="#/docs/' + m[1] + (m[2] ? '?h=' + m[2] : '') + '">' + text + '</a>';
    if (/^https?:\/\//.test(href)) return '<a href="' + href + '" target="_blank" rel="noopener noreferrer">' + text + '</a>';
    if (href.charAt(0) === '#') return '<a href="' + href + '">' + text + '</a>';
    return '<a href="../' + href + '" target="_blank" rel="noopener">' + text + '</a>';
  }
  function inline(raw) {
    var s = esc(raw);
    var codes = [];
    s = s.replace(/`([^`]+)`/g, function (m, c) { codes.push(c); return '\u0000' + (codes.length - 1) + '\u0000'; });
    s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, function (m, alt, src) {
      return '<img src="' + (/^https?:/.test(src) ? src : '../' + src) + '" alt="' + alt + '">';
    });
    s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (m, t, h) { return mdLink(t, h); });
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/(^|[^*\w])\*(?!\s)([^*]+?)\*(?![*\w])/g, '$1<em>$2</em>');
    s = s.replace(/~~(.+?)~~/g, '<del>$1</del>');
    s = s.replace(/\u0000(\d+)\u0000/g, function (m, i) { return '<code>' + codes[+i] + '</code>'; });
    return s;
  }
  function stripMd(s) {
    return s.replace(/`([^`]+)`/g, '$1').replace(/!\[[^\]]*\]\([^)]*\)/g, '')
      .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/\*\*|__|~~/g, '').replace(/^[>\s#*-]+\s*/, '')
      .replace(/\|/g, ' ').replace(/\s+/g, ' ').trim();
  }
  function splitRow(line) {
    var t = line.trim();
    if (t.charAt(0) === '|') t = t.slice(1);
    if (t.charAt(t.length - 1) === '|') t = t.slice(0, -1);
    return t.split('|').map(function (c) { return c.trim(); });
  }
  function renderList(items) {
    var out = '';
    var stack = [];
    items.forEach(function (it) {
      while (stack.length && it.indent < stack[stack.length - 1].indent) out += '</li></' + stack.pop().tag + '>';
      var top = stack[stack.length - 1];
      if (!top || it.indent > top.indent) {
        var tag = it.ordered ? 'ol' : 'ul';
        stack.push({ indent: it.indent, tag: tag });
        out += '<' + tag + '><li>' + inline(it.text);
      } else {
        out += '</li><li>' + inline(it.text);
      }
    });
    while (stack.length) out += '</li></' + stack.pop().tag + '>';
    return out;
  }
  function markers(html) {
    return html.replace(/✅/g, '<span class="mk" title="Acordado">✅</span>')
      .replace(/🟡/g, '<span class="mk" title="Propuesta pendiente de confirmar">🟡</span>')
      .replace(/❓/g, '<span class="mk" title="Abierto">❓</span>');
  }
  function mdToHtml(md) {
    var lines = md.replace(/\r\n/g, '\n').split('\n');
    var html = [];
    var toc = [];
    var seen = {};
    var i = 0;
    var isBlockStart = function (l) {
      return /^(#{1,6})\s/.test(l) || /^```/.test(l) || /^>/.test(l) || /^\s*([-*]|\d+\.)\s+/.test(l) || /^\s*(-{3,}|\*{3,})\s*$/.test(l);
    };
    while (i < lines.length) {
      var line = lines[i];
      var m;
      if (/^```/.test(line)) {
        var code = [];
        i++;
        while (i < lines.length && !/^```/.test(lines[i])) { code.push(lines[i]); i++; }
        i++;
        html.push('<pre><code>' + esc(code.join('\n')) + '</code></pre>');
        continue;
      }
      if (/^\s*$/.test(line)) { i++; continue; }
      if ((m = line.match(/^(#{1,6})\s+(.*)$/))) {
        var level = m[1].length;
        var plain = stripMd(m[2]);
        var id = slug(plain);
        if (seen[id]) { seen[id]++; id += '-' + seen[id]; } else { seen[id] = 1; }
        if (level === 2 || level === 3) toc.push({ level: level, text: plain, id: id });
        html.push('<h' + level + ' id="' + id + '">' + inline(m[2]) + '</h' + level + '>');
        i++;
        continue;
      }
      if (/^\s*(-{3,}|\*{3,})\s*$/.test(line)) { html.push('<hr>'); i++; continue; }
      if (/^>/.test(line)) {
        var q = [];
        while (i < lines.length && /^>/.test(lines[i])) { q.push(lines[i].replace(/^>\s?/, '')); i++; }
        html.push('<blockquote><p>' + inline(q.join(' ')) + '</p></blockquote>');
        continue;
      }
      if (line.indexOf('|') !== -1 && i + 1 < lines.length && /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(lines[i + 1])) {
        var head = splitRow(line);
        i += 2;
        var rows = [];
        while (i < lines.length && lines[i].indexOf('|') !== -1 && !/^\s*$/.test(lines[i])) { rows.push(splitRow(lines[i])); i++; }
        var t = '<div class="table-wrap"><table><thead><tr>' + head.map(function (c) { return '<th>' + inline(c) + '</th>'; }).join('') + '</tr></thead><tbody>';
        rows.forEach(function (r) { t += '<tr>' + r.map(function (c) { return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>'; });
        html.push(t + '</tbody></table></div>');
        continue;
      }
      if (/^\s*([-*]|\d+\.)\s+/.test(line)) {
        var items = [];
        while (i < lines.length && /^\s*([-*]|\d+\.)\s+/.test(lines[i])) {
          var lm = lines[i].match(/^(\s*)([-*]|\d+\.)\s+(.*)$/);
          items.push({ indent: lm[1].length, ordered: /\d/.test(lm[2]), text: lm[3] });
          i++;
        }
        html.push(renderList(items));
        continue;
      }
      var para = [line];
      i++;
      while (i < lines.length && !/^\s*$/.test(lines[i]) && !isBlockStart(lines[i]) && !(lines[i].indexOf('|') !== -1 && i + 1 < lines.length && /^\s*\|?\s*:?-{2,}/.test(lines[i + 1]))) { para.push(lines[i]); i++; }
      html.push('<p>' + inline(para.join(' ')) + '</p>');
    }
    return { html: markers(html.join('\n')), toc: toc };
  }

  /* ---------- datos derivados ---------- */
  var phases = H.roadmap.phases;
  var targets = H.roadmap.meta.targets;

  function allTasks() {
    var out = [];
    phases.forEach(function (p) {
      p.milestones.forEach(function (m) {
        m.tasks.forEach(function (t) {
          var c = {};
          Object.keys(t).forEach(function (k) { c[k] = t[k]; });
          c.phase = p;
          c.ms = m;
          c.target = t.target || p.target;
          c.prio = t.prio || 'P1';
          c.history = t.history || [];
          c.comments = t.comments || [];
          c.evidence = t.evidence || [];
          out.push(c);
        });
      });
    });
    return out;
  }
  var TASKS = allTasks();
  function taskById(id) { return TASKS.filter(function (t) { return t.id === id; })[0]; }

  function progress(list) {
    var act = list.filter(function (t) { return t.status !== 'dropped'; });
    var total = 0, done = 0, nd = 0;
    act.forEach(function (t) { total += t.est; if (t.status === 'done') { done += t.est; nd++; } });
    return { n: act.length, nd: nd, total: total, done: done, pct: total ? Math.round(100 * done / total) : 0 };
  }
  function phaseTasks(p) { return TASKS.filter(function (t) { return t.phase.id === p.id; }); }
  function currentPhase() {
    for (var i = 0; i < phases.length; i++) {
      if (progress(phaseTasks(phases[i])).pct < 100) return phases[i];
    }
    return phases[phases.length - 1];
  }
  function inScope(t) { return PRANK[t.prio] <= SCOPES.filter(function (s) { return s.key === state.scope; })[0].max; }

  function statusPill(s) {
    return '<span class="pill s-' + s + '">' + STATUS[s].glyph + ' ' + STATUS[s].label + '</span>';
  }
  function targetPill(t) { return '<span class="pill ' + targetClass(t) + '">' + esc(t) + '</span>'; }
  function prioPill(p) { return '<span class="pill p-' + p + '" title="' + esc(PRIO_LABEL[p] || p) + '">' + p + '</span>'; }
  function bar(pct, ok) { return '<div class="bar' + (ok ? ' ok' : '') + '" role="img" aria-label="' + pct + ' por ciento"><span style="width:' + pct + '%"></span></div>'; }
  function hoursLabel(p) {
    var base = progress(phaseTasks(p)).total;
    return 'base ' + num(base) + ' h' + (p.hours ? ' · rango ' + p.hours[0] + '–' + p.hours[1] + ' h' : '') + (p.confidence ? ' · estimación ' + p.confidence : '');
  }
  function taskLink(t, text) { return '<a href="#/tarea/' + esc(t.id) + '">' + (text || esc(t.title)) + '</a>'; }
  function move(h) { return STATUS[h.from].label + ' → ' + STATUS[h.to].label; }

  function recentActivity(limit) {
    var items = [];
    TASKS.forEach(function (t) {
      t.history.forEach(function (h, i) { items.push({ t: t, h: h, i: i }); });
    });
    items.sort(function (a, b) { return a.h.at < b.h.at ? 1 : a.h.at > b.h.at ? -1 : (b.i - a.i); });
    return items.slice(0, limit);
  }

  /* ---------- estado de las vistas ---------- */
  var state = {
    scope: 'all',
    rm: { target: 'all', hideDone: false, open: null },
    board: { phase: 'all', target: 'all', limit: {} },
    tl: { px: 1.1, target: 'launch', rate: 0, sel: null },
    art: { cat: 'Todas' },
    qa: { area: 'Todas', type: 'Todos' },
    dc: { act: 'all', level: 'all', who: 'all' },
    hl: { act: 'all', tipo: 'all', estado: 'all', who: 'all' },
    sim: { grupo: 'all', estado: 'all', open: {} },
    sb: { v: {} },
    s1: { mode: 'feliz', reme: 'all', diff: 'all', open: {}, v: {}, gal: false, galf: 'todas' }
  };
  var lb = { list: [], idx: 0, opener: null };

  function scopeChips() {
    return '<div class="filter-group"><span class="filter-label">Alcance</span>' + SCOPES.map(function (s) {
      return '<button class="chip" type="button" data-action="scope" data-value="' + s.key + '" aria-pressed="' + (state.scope === s.key) + '" title="' + esc(s.hint) + '">' + esc(s.label) + '</button>';
    }).join('') + '</div>';
  }
  function prioLegend() {
    return '<div class="prio-legend">' + PRIOS.map(function (p) { return '<span>' + prioPill(p) + ' ' + esc(PRIO_LABEL[p]) + '</span>'; }).join('') + '</div>';
  }

  /* ---------- navegación lateral ---------- */
  function buildNav() {
    var cfg = H.config;
    var h = '<div class="brand"><div class="brand-mark" aria-hidden="true">' + esc(cfg.mark || 'VF') + '</div><div><div class="brand-title">' + esc(cfg.title) + '</div><div class="brand-sub">' + esc(cfg.subtitle) + '</div></div></div>';
    h += '<nav class="nav" aria-label="Secciones">';
    h += '<div class="nav-group">Panel</div>';
    h += link('', 'Inicio', '◆') + link('juego', 'El juego', '★') + link('personajes', 'Personajes y NPC', '☺') + link('storyboard', 'Storyboard del Acto I', '▣') + link('semana1', 'Semana 1 · camino feliz', '①') + link('mapa', 'Mapa de historia', '⌖') + link('decisiones', 'Árbol de decisiones', '⑂') + link('hilos', 'Hilos narrativos', '⧉') + link('limpieza', 'Limpieza del diseño', '◌') + link('coherencia', 'Coherencia del diseño', '⌘') + link('simulador', 'Simulador de economía', '⚖') + link('roadmap', 'Roadmap', '▤') + link('linea', 'Línea de tiempo', '⟷') + link('tablero', 'Tablero', '▦') + link('qa', 'QA', '✔');
    H.groups.forEach(function (g) {
      var docs = H.docs.filter(function (d) { return d.group === g; });
      if (!docs.length) return;
      h += '<div class="nav-group">' + esc(g) + '</div>';
      docs.forEach(function (d) {
        var parts = d.title.split(' · ');
        var label = d.id.indexOf('adr-') === 0 ? 'A' + parseInt(d.id.slice(4, 8), 10) : d.id.slice(0, 2);
        h += '<a href="#/docs/' + d.id + '" data-key="docs/' + d.id + '"><span class="num">' + esc(label) + '</span>' + esc(parts.length > 1 ? parts.slice(1).join(' · ') : d.title) + '</a>';
      });
    });
    h += '<div class="nav-group">Recursos</div>';
    h += link('arte', 'Arte y assets', '▣') + link('sonido', 'Sonido', '♪') + link('paleta', 'Paleta', '◧');
    h += '</nav>';
    $('#sidebar').innerHTML = h;
    function link(key, label, glyph) {
      return '<a href="#/' + key + '" data-key="' + key + '"><span class="num" aria-hidden="true">' + glyph + '</span>' + label + '</a>';
    }
  }
  function setActive(key) {
    $all('.nav a').forEach(function (a) {
      if (a.getAttribute('data-key') === key) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
  }

  /* ---------- inicio ---------- */
  function scopeTable() {
    var live = TASKS.filter(function (t) { return t.status !== 'dropped'; });
    var launch = live.filter(function (t) { return t.target !== 'Evolutivo'; });
    var after = live.filter(function (t) { return t.target === 'Evolutivo'; });
    var totalLaunch = launch.reduce(function (a, t) { return a + t.est; }, 0);
    var h = '<div class="table-wrap"><table><thead><tr><th>Prioridad</th><th class="num-cell">Tareas</th><th class="num-cell">Horas</th><th class="num-cell">Hechas</th><th class="num-cell">Acumulado</th><th class="num-cell">% del lanzamiento</th></tr></thead><tbody>';
    var cum = 0;
    PRIOS.forEach(function (p) {
      var l = launch.filter(function (t) { return t.prio === p; });
      var hrs = l.reduce(function (a, t) { return a + t.est; }, 0);
      var dn = l.filter(function (t) { return t.status === 'done'; }).reduce(function (a, t) { return a + t.est; }, 0);
      cum += hrs;
      h += '<tr><td>' + prioPill(p) + ' ' + esc(PRIO_LABEL[p]) + '</td><td class="num-cell">' + l.length + '</td><td class="num-cell">' + num(hrs) + ' h</td><td class="num-cell">' + num(dn) + ' h</td><td class="num-cell">' + num(cum) + ' h</td><td class="num-cell">' + (totalLaunch ? Math.round(100 * cum / totalLaunch) : 0) + '%</td></tr>';
    });
    var ah = after.reduce(function (a, t) { return a + t.est; }, 0);
    h += '<tr><td><span class="pill t-Evolutivo">Evolutivo</span> después del lanzamiento</td><td class="num-cell">' + after.length + '</td><td class="num-cell">' + num(ah) + ' h</td><td class="num-cell">—</td><td class="num-cell">—</td><td class="num-cell">—</td></tr>';
    return h + '</tbody></table></div>';
  }

  function viewHome() {
    var cfg = H.config;
    var cur = currentPhase();
    var hero = H.assets.images.filter(function (i) { return /mina-horizontal/.test(i.file); })[0];
    var h = '<section class="hero">' + (hero ? '<img src="../' + esc(hero.file) + '" alt="">' : '') +
      '<div class="hero-body"><p class="eyebrow">' + esc(cfg.subtitle) + ' · ' + esc(cfg.titleEn || '') + '</p><h1>' + esc(cfg.title) + '</h1><p>' + esc(cfg.tagline) + '. Todo el diseño, el arte, el plan y el avance del proyecto en un solo lugar.</p><div class="chips">' +
      cfg.chips.map(function (c) { return '<span class="chip brass">' + esc(c) + '</span>'; }).join('') + '</div></div></section>';

    h += '<div class="grid grid-3">';
    targets.forEach(function (t) {
      var p = progress(TASKS.filter(function (x) { return x.target === t; }));
      h += '<div class="card"><div class="stat-label">' + esc(t) + '</div><div class="stat-value">' + p.pct + '%</div>' + bar(p.pct, true) +
        '<div class="stat-sub" style="margin-top:8px">' + p.nd + ' de ' + p.n + ' tareas · ' + num(p.done) + ' de ' + num(p.total) + ' h</div></div>';
    });
    h += '</div>';

    h += '<h2 class="section-title">Alcance y prioridades <small>horas base hasta el lanzamiento</small></h2>' + scopeTable() +
      '<p class="stat-sub">Las horas son estimaciones base del autor. El rango real de cada fase está en el roadmap. <a href="#/linea">Ver la línea de tiempo en horas →</a></p>';

    h += '<h2 class="section-title">Fases <small>fase actual: ' + esc(cur.id + ' · ' + cur.name) + '</small></h2><div class="card">';
    phases.forEach(function (p) {
      var pr = progress(phaseTasks(p));
      h += '<div class="phase-row"><div class="phase-name"><a href="#/roadmap" data-phase="' + p.id + '" style="color:inherit;text-decoration:none">' + esc(p.id + ' · ' + p.name) + '</a><small>' + hoursLabel(p) + ' · ' + esc(p.target) + '</small></div>' + bar(pr.pct, pr.pct === 100) + '<div class="pct">' + pr.pct + '%</div></div>';
    });
    h += '</div>';

    var act = recentActivity(8);
    h += '<h2 class="section-title">Actividad reciente <small>últimos movimientos de tareas</small></h2><div class="card">';
    if (!act.length) h += '<div class="empty">Todavía no hay movimientos registrados.</div>';
    act.forEach(function (a) {
      h += '<div class="act-row"><span class="tid">' + esc(a.h.at) + '</span><span>' + taskLink(a.t, esc(a.t.id) + ' · ' + esc(a.t.title)) + '<small class="act-note">' + esc(move(a.h)) + ' — ' + esc(a.h.note) + '</small></span></div>';
    });
    h += '</div>';

    var queue = TASKS.filter(function (t) { return t.status !== 'done' && t.status !== 'dropped'; })
      .map(function (t, idx) { return { t: t, idx: idx }; })
      .sort(function (a, b) { return (QUEUE_ORDER[a.t.status] - QUEUE_ORDER[b.t.status]) || (PRANK[a.t.prio] - PRANK[b.t.prio]) || (a.idx - b.idx); })
      .slice(0, 6);
    h += '<h2 class="section-title">Siguiente en la cola</h2><div class="card">';
    if (!queue.length) h += '<div class="empty">No quedan tareas pendientes.</div>';
    queue.forEach(function (q) {
      h += '<div class="phase-row" style="grid-template-columns:70px 1fr auto auto"><span class="tid">' + esc(q.t.id) + '</span><span>' + taskLink(q.t) + '</span>' + prioPill(q.t.prio) + statusPill(q.t.status) + '</div>';
    });
    h += '</div>';

    h += '<h2 class="section-title">Limpieza del diseño <small>✅ acordado ÷ (✅ + 🟡 + ❓) · meta ' + H.cleanliness.target + ' %</small></h2>' + cleanTable(H.docs.slice().sort(function (a, b) { return cleanSort(a) - cleanSort(b); }).slice(0, 8)) + '<p class="clean-more"><a href="#/limpieza">Ver todos los documentos y los puntos abiertos →</a> · Coherencia con el registro del mundo: <strong>' + H.coherence.pct + ' %</strong> <a href="#/coherencia">Ver hallazgos →</a></p>' + simHome();
    return h;
  }

  function simHome() {
    var S = H.sim;
    if (!S || !S.disponible) return '<p class="clean-more">Equilibrio de la economía: <strong>sin resultados todavía</strong> <a href="#/simulador">Ver el simulador →</a></p>';
    return '<p class="clean-more">Equilibrio de la economía: <strong>' + S.conteo.pasa + ' de ' + S.conteo.total + ' reglas pasan</strong>' + (S.caducado ? ' · <span class="sim-flag">resultado caducado</span>' : '') + ' <a href="#/simulador">Ver el simulador →</a></p>';
  }

  /* ---------- limpieza del diseño ---------- */
  function cleanSort(d) { return d.clean.pct === null ? 101 : d.clean.pct; }
  function cleanLevel(p) { return p === null ? 'na' : p >= H.cleanliness.target ? 'good' : p >= 60 ? 'mid' : 'low'; }
  function cleanChip(d) {
    var p = d.clean.pct;
    return '<span class="chip clean-chip ' + cleanLevel(p) + '" title="✅ ÷ (✅ + 🟡 + ❓). Meta ' + H.cleanliness.target + ' %">Limpieza ' + (p === null ? 'n/a' : p + ' %') + '</span>';
  }
  function cleanBar(p) {
    return '<span class="cln-bar ' + cleanLevel(p) + '" role="img" aria-label="Limpieza ' + (p === null ? 'no aplica' : p + ' por ciento') + '"><i style="width:' + (p || 0) + '%"></i><b style="left:' + H.cleanliness.target + '%"></b></span>';
  }
  function cleanTable(docs) {
    var h = '<div class="table-wrap"><table><thead><tr><th>Documento</th><th>Limpieza</th><th class="num-cell">✅</th><th class="num-cell">🟡</th><th class="num-cell">❓</th><th class="num-cell">⏳</th></tr></thead><tbody>';
    docs.forEach(function (d) {
      var p = d.clean.pct;
      h += '<tr><td><a href="#/docs/' + d.id + '">' + esc(d.title) + '</a></td><td class="cln-cell">' + cleanBar(p) + '<span class="cln-pct">' + (p === null ? 'n/a' : p + ' %') + '</span></td><td class="num-cell">' + d.counts.ok + '</td><td class="num-cell">' + d.counts.prop + '</td><td class="num-cell">' + d.counts.open + '</td><td class="num-cell">' + d.clean.wait + '</td></tr>';
    });
    return h + '</tbody></table></div>';
  }
  function viewClean() {
    var c = H.cleanliness;
    var docs = H.docs.slice().sort(function (a, b) { return cleanSort(a) - cleanSort(b); });
    var pending = docs.filter(function (d) { return d.clean.pct !== null && d.clean.pct < c.target; }).length;
    var h = '<p class="eyebrow">Calidad</p><h1 class="page-title">Limpieza del diseño</h1><p class="page-lead">Todo debe quedar <strong>✅ acordado</strong>, sin ambigüedades. Lo que depende de algo posterior se marca <strong>⏳ con la tarea de la que depende</strong> y no resta. Cada documento se mide como ✅ ÷ (✅ + 🟡 + ❓): la meta es acercarse al 100 % y, como referencia mínima, ' + c.target + ' %. Además se comprueba que todo conecte: enlaces entre documentos y tareas citadas.</p>';
    h += '<div class="cln-summary"><div class="ring" style="--p:' + (c.pct || 0) + '"><b>' + (c.pct === null ? '—' : c.pct + '%') + '</b><span>del diseño</span></div><div class="st-grid">' +
      '<div class="st-card"><small>✅ Acordado</small><b>' + c.ok + '</b><span>puntos cerrados</span></div>' +
      '<div class="st-card"><small>🟡 + ❓ Por cerrar</small><b>' + (c.prop + c.open) + '</b><span>' + c.prop + ' propuestas · ' + c.open + ' abiertos</span></div>' +
      '<div class="st-card"><small>⏳ Diferido</small><b>' + c.wait + '</b><span>depende de una tarea posterior</span></div>' +
      '<div class="st-card"><small>Conexiones rotas</small><b>' + c.problems + '</b><span>' + (c.problems ? 'hay que corregirlas' : 'todo conecta') + '</span></div></div></div>';
    h += '<h2 class="section-title">Por documento <small>' + pending + ' por debajo de la meta</small></h2>' + cleanTable(docs);
    h += '<h2 class="section-title">Puntos por cerrar</h2><p class="page-lead">Cada punto 🟡 u ❓ es algo por confirmar con el autor o por decidir. Se atienden en pasadas de cierre por documento.</p>';
    docs.forEach(function (d) {
      if (!d.clean.items.length && !d.clean.problems.length) return;
      h += '<details class="cln-doc"><summary><span class="cln-name">' + esc(d.title) + '</span>' + cleanChip(d) + '<small>' + d.clean.items.length + ' punto(s)' + (d.clean.problems.length ? ' · ' + d.clean.problems.length + ' conexión(es) rota(s)' : '') + '</small></summary>';
      if (d.clean.problems.length) h += '<ul class="cln-problems">' + d.clean.problems.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
      h += '<ul class="cln-items">' + d.clean.items.map(function (it) {
        return '<li><span class="cln-k">' + it.kinds.map(function (k) { return k === 'prop' ? '🟡' : k === 'open' ? '❓' : '⏳'; }).join('') + '</span><span><small>' + esc(it.heading) + ' · línea ' + it.line + '</small><br>' + esc(it.text) + '</span></li>';
      }).join('') + '</ul></details>';
    });
    return h;
  }

  /* ---------- coherencia del diseño ---------- */
  function actOf(list, i) { return list[i] || ''; }
  function viewCoherence() {
    var co = H.coherence, w = H.world, st = H.story;
    var acts = w.acts;
    var h = '<p class="eyebrow">Calidad</p><h1 class="page-title">Coherencia del diseño</h1><p class="page-lead">El <a href="../data/world.json" target="_blank" rel="noopener">registro del mundo</a> es la fuente de verdad de minerales, zonas, minijuegos, recetas y personajes. Aquí se comprueba que las reglas, el mapa de historia y los números base no se contradigan ni queden sin definir. Un hallazgo es algo por decidir o por corregir: al principio hay muchos y se resuelven a medida que se cierran las tareas.</p>';
    h += '<div class="cln-summary"><div class="ring" style="--p:' + (co.pct || 0) + '"><b>' + (co.pct === null ? '—' : co.pct + '%') + '</b><span>coherente</span></div><div class="st-grid">' +
      '<div class="st-card"><small>Comprobaciones</small><b>' + co.total + '</b><span>entre ' + co.checks.length + ' reglas</span></div>' +
      '<div class="st-card"><small>Hallazgos</small><b>' + co.failed + '</b><span>por decidir o corregir</span></div>' +
      '<div class="st-card"><small>Minerales</small><b>' + w.minerals.length + '</b><span>' + w.zones.length + ' zonas · ' + w.recipes.length + ' recetas</span></div>' +
      '<div class="st-card"><small>Personajes</small><b>' + w.characters.length + '</b><span>' + w.factions.length + ' facciones</span></div></div></div>';
    h += '<h2 class="section-title">Minerales y zonas</h2><p class="page-lead">● zona principal · ○ zona secundaria. Las columnas muestran el acto en que se abre cada zona; la última compara cuándo aparece el mineral según las zonas con cuándo lo pone el mapa de historia.</p>';
    h += '<div class="table-wrap"><table class="cph-matrix"><thead><tr><th>Mineral</th>' + w.zones.map(function (z) { return '<th class="cph-z"><span>' + esc(z.name) + '</span><small>Acto ' + esc(z.act) + '</small></th>'; }).join('') + '<th>Minijuegos</th><th>Según zonas</th><th>Mapa de historia</th></tr></thead><tbody>';
    var stMin = (st.lanes.filter(function (l) { return l.id === 'minerales'; })[0] || { cells: [] }).cells;
    w.minerals.forEach(function (m) {
      var first = w.zones.filter(function (z) { return m.zones[z.id]; }).map(function (z) { return z.act; }).sort(function (a, b) { return acts.indexOf(a) - acts.indexOf(b); })[0];
      var inStory = ''; stMin.forEach(function (cell, i) { if (cell.indexOf(m.name) >= 0) inStory = acts[i]; });
      h += '<tr><td><b>' + esc(m.name) + '</b></td>' + w.zones.map(function (z) {
        var r = m.zones[z.id];
        return '<td class="cph-c">' + (r === 'principal' ? '●' : r === 'secundario' ? '○' : '') + '</td>';
      }).join('') + '<td>' + esc(m.minigames.map(function (g) { var x = w.minigames.filter(function (y) { return y.id === g; })[0]; return x ? x.name : g; }).join(', ')) + '</td><td class="cph-c">' + esc(first || '—') + '</td><td class="cph-c' + (inStory !== first ? ' cph-bad' : '') + '">' + esc(inStory || '—') + '</td></tr>';
    });
    h += '</tbody></table></div>';
    h += '<h2 class="section-title">Comprobaciones</h2>';
    co.checks.forEach(function (c) {
      var ok = c.failed === 0;
      h += '<details class="cln-doc"' + (ok ? '' : ' open') + '><summary><span class="cph-st ' + (ok ? 'ok' : 'bad') + '">' + (ok ? '✓' : c.failed) + '</span><span class="cln-name">' + esc(c.title) + '</span><small>' + esc(c.area) + ' · ' + (c.total - c.failed) + ' de ' + c.total + ' en orden</small></summary>';
      if (c.findings.length) h += '<ul class="cln-items cph-find">' + c.findings.map(function (f) { return '<li><span class="cln-k">•</span><span>' + esc(f) + '</span></li>'; }).join('') + '</ul>';
      h += '</details>';
    });
    return h;
  }

  /* ---------- simulador de economía y progresión ---------- */
  var SIM_LABEL = { pasa: 'Pasa', falla: 'Falla', incierto: 'Incierto' };
  var SIM_COLOR = { lento: '#8fb0ba', medio: '#e3b25c', rapido: '#4fb6a5', optimizador: '#c23b55' };
  var SIM_EXTRA = ['#b8a6d9', '#7fb069', '#d98e5f', '#6fa8dc'];
  /* Los pisos de estatus llegan de los datos como {comerciante: 15000, ...} o como [{valor, etiqueta}]; se normalizan a lista ordenada. */
  function simRefs(raw) {
    var list = Array.isArray(raw) ? raw : Object.keys(raw || {}).map(function (k) { return { valor: raw[k], etiqueta: k.charAt(0).toUpperCase() + k.slice(1) }; });
    return list.filter(function (r) { return r && typeof r.valor === 'number' && isFinite(r.valor) && r.valor > 0; })
      .map(function (r) { return { valor: r.valor, etiqueta: r.etiqueta == null ? '' : String(r.etiqueta) }; })
      .sort(function (a, b) { return a.valor - b.valor; });
  }
  var SIM_CH = { w: 760, h: 300, l: 66, r: 16, t: 18, b: 34 };

  function simNum(v) {
    if (typeof v !== 'number' || !isFinite(v)) return v == null ? '—' : String(v);
    var a = Math.abs(v);
    var s = String(Number.isInteger(v) || a >= 1000 ? Math.round(v) : +v.toFixed(a >= 100 ? 0 : a >= 10 ? 1 : a >= 1 ? 2 : 3));
    var p = s.split('.');
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return p.join(',');
  }
  function simUnit(r) { return r.unidad ? ' ' + r.unidad : ''; }
  function simRange(v) {
    if (v && typeof v === 'object' && !Array.isArray(v)) return (v.min != null ? '≥ ' + simNum(v.min) : '') + (v.min != null && v.max != null ? ' y ' : '') + (v.max != null ? '≤ ' + simNum(v.max) : '');
    if (Array.isArray(v)) return simNum(v[0]) + ' – ' + simNum(v[1]);
    return simNum(v);
  }
  function simIc(ic) { return ic ? '[' + simNum(ic[0]) + ' – ' + simNum(ic[1]) + ']' : ''; }
  function simPill(estado) { return '<span class="sim-st ' + esc(estado) + '">' + esc(SIM_LABEL[estado] || estado) + '</span>'; }
  function simDocs(docs) {
    return (docs || []).map(function (d) {
      var m = /^\s*(\d{2})/.exec(d);
      var doc = m && H.docs.filter(function (x) { return x.id.indexOf(m[1] + '-') === 0; })[0];
      return doc ? '<a href="#/docs/' + esc(doc.id) + '" title="' + esc(doc.title) + '">' + esc(d) + '</a>' : esc(d);
    }).join(' · ');
  }
  function simProfiles(res) {
    return res.perfiles.map(function (p, i) {
      var id = typeof p === 'string' ? p : p.id;
      return { id: id, name: typeof p === 'string' ? p : (p.nombre || p.id), color: SIM_COLOR[id] || SIM_EXTRA[i % SIM_EXTRA.length] };
    });
  }
  function simLegend(profiles) {
    return '<div class="sim-legend">' + profiles.map(function (p) { return '<span><i style="background:' + p.color + '"></i>' + esc(p.name) + '</span>'; }).join('') + '</div>';
  }
  function simFailing(r) {
    return Object.keys(r.por_perfil || {}).filter(function (k) { return r.por_perfil[k].estado && r.por_perfil[k].estado !== 'pasa'; });
  }

  /* Ejes: log (potencias de 10) y lineal con marcas "bonitas" */
  function simLogAxis(lo, hi, y0, y1) {
    var a = Math.floor(Math.log10(Math.max(lo, 1))), b = Math.max(Math.ceil(Math.log10(hi)), a + 1);
    var ticks = [];
    for (var e = a; e <= b; e++) ticks.push(Math.pow(10, e));
    return { ticks: ticks, y: function (v) { return y0 - (Math.log10(Math.max(v, ticks[0])) - a) / (b - a) * (y0 - y1); }, min: ticks[0] };
  }
  function simLinAxis(lo, hi, y0, y1) {
    var span = hi - lo || 1, raw = span / 5, mag = Math.pow(10, Math.floor(Math.log10(raw)));
    var step = [1, 2, 5, 10].map(function (k) { return k * mag; }).filter(function (s) { return s >= raw; })[0];
    var a = Math.floor(lo / step) * step, b = Math.ceil(hi / step) * step, ticks = [];
    for (var v = a; v <= b + step / 2; v += step) ticks.push(v);
    return { ticks: ticks, y: function (v) { return y0 - (v - a) / (b - a) * (y0 - y1); } };
  }
  function simGrid(ax, c) {
    return ax.ticks.map(function (t) {
      var y = ax.y(t).toFixed(1);
      return '<line x1="' + c.l + '" y1="' + y + '" x2="' + (c.w - c.r) + '" y2="' + y + '" stroke="#2a3d4a" stroke-width="1"/><text x="' + (c.l - 6) + '" y="' + (+y + 4) + '" text-anchor="end" fill="#8fb0ba" font-size="11">' + simNum(t) + '</text>';
    }).join('');
  }
  function simSvg(label, body) {
    return '<svg class="sim-chart" viewBox="0 0 ' + SIM_CH.w + ' ' + SIM_CH.h + '" role="img" aria-label="' + esc(label) + '">' + body + '</svg>';
  }
  function simFigure(title, lead, svg, profiles, rows) {
    return '<figure class="sim-fig"><h3 class="sl-sub">' + esc(title) + '</h3><p class="page-lead">' + lead + '</p>' + simLegend(profiles) + svg +
      '<details class="sim-data"><summary>Ver las cifras</summary><div class="table-wrap"><table><thead><tr>' + rows.head.map(function (x) { return '<th>' + esc(x) + '</th>'; }).join('') + '</tr></thead><tbody>' +
      rows.body.map(function (r) { return '<tr>' + r.map(function (x, i) { return '<td' + (i ? ' class="num-cell"' : '') + '>' + esc(x) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div></details></figure>';
  }

  /* Gráfico 1: ingreso neto por hora y acto (log), objetivo del medio y banda */
  function simChartIncome(S, profiles) {
    var c = SIM_CH, s = S.ingreso_hora_por_acto, band = s.banda == null ? 0.2 : s.banda;
    var vals = [], P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    s.actos.forEach(function (a) { vals.push(s.objetivo[a] * (1 - band), s.objetivo[a] * (1 + band)); P.forEach(function (p) { vals.push(s.perfiles[p.id][a]); }); });
    var ax = simLogAxis(Math.min.apply(null, vals) * 0.8, Math.max.apply(null, vals) * 1.2, c.h - c.b, c.t);
    var gw = (c.w - c.l - c.r) / s.actos.length, bw = gw * 0.78 / Math.max(P.length, 1);
    var g = simGrid(ax, c), base = ax.y(ax.min);
    s.actos.forEach(function (a, i) {
      var x0 = c.l + i * gw, o = s.objetivo[a];
      g += '<rect x="' + x0.toFixed(1) + '" y="' + ax.y(o * (1 + band)).toFixed(1) + '" width="' + gw.toFixed(1) + '" height="' + (ax.y(o * (1 - band)) - ax.y(o * (1 + band))).toFixed(1) + '" fill="#e3b25c" opacity="0.13"/>';
      P.forEach(function (p, k) {
        var v = s.perfiles[p.id][a], x = x0 + gw * 0.11 + k * bw, y = ax.y(v);
        g += '<rect x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + (bw - 2).toFixed(1) + '" height="' + Math.max(base - y, 0).toFixed(1) + '" fill="' + p.color + '"><title>' + esc(p.name) + ' · acto ' + esc(a) + ': ' + simNum(v) + ' por hora</title></rect>';
      });
      g += '<line x1="' + x0.toFixed(1) + '" y1="' + ax.y(o).toFixed(1) + '" x2="' + (x0 + gw).toFixed(1) + '" y2="' + ax.y(o).toFixed(1) + '" stroke="#e3b25c" stroke-width="1.6" stroke-dasharray="6 4"><title>Objetivo del acto ' + esc(a) + ': ' + simNum(o) + '</title></line>';
      g += '<text x="' + (x0 + gw / 2).toFixed(1) + '" y="' + (c.h - 12) + '" text-anchor="middle" fill="#c9dcdf" font-size="12">Acto ' + esc(a) + '</text>';
    });
    return simSvg('Ingreso neto por hora en cada acto y perfil, escala logarítmica, con el objetivo del acto y su banda de más o menos ' + Math.round(band * 100) + ' por ciento', g);
  }

  /* Gráfico 2: patrimonio por perfil en el tiempo (log) con los pisos de estatus */
  function simChartWealth(S, profiles) {
    var c = SIM_CH, s = S.patrimonio_por_dia, refs = simRefs(s.referencias);
    var P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    var vals = refs.map(function (r) { return r.valor; });
    P.forEach(function (p) { s.perfiles[p.id].forEach(function (v) { vals.push(v); }); });
    var pos = vals.filter(function (v) { return v > 0; });
    var ax = simLogAxis(Math.min.apply(null, pos), Math.max.apply(null, pos) * 1.1, c.h - c.b, c.t);
    var d0 = s.dias[0], d1 = s.dias[s.dias.length - 1];
    var x = function (d) { return c.l + (d - d0) / (d1 - d0 || 1) * (c.w - c.l - c.r); };
    var g = simGrid(ax, c);
    refs.forEach(function (r) {
      var y = ax.y(r.valor).toFixed(1);
      g += '<line x1="' + c.l + '" y1="' + y + '" x2="' + (c.w - c.r) + '" y2="' + y + '" stroke="#e3b25c" stroke-width="1.2" stroke-dasharray="5 4"/><text x="' + (c.l + 6) + '" y="' + (y - 4) + '" fill="#e3b25c" font-size="11">' + esc(r.etiqueta) + ' ' + simNum(r.valor) + '</text>';
    });
    (s.actos || []).forEach(function (a) {
      var xx = x(a.dia).toFixed(1);
      g += '<line x1="' + xx + '" y1="' + c.t + '" x2="' + xx + '" y2="' + (c.h - c.b) + '" stroke="#5b7c8c" stroke-dasharray="2 4"/><text x="' + (+xx + 4) + '" y="' + (c.h - c.b - 6) + '" fill="#8fb0ba" font-size="11">Acto ' + esc(a.acto) + '</text>';
    });
    P.forEach(function (p) {
      g += '<polyline fill="none" stroke="' + p.color + '" stroke-width="2.2" stroke-linejoin="round" points="' + s.perfiles[p.id].map(function (v, i) { return x(s.dias[i]).toFixed(1) + ',' + ax.y(v).toFixed(1); }).join(' ') + '"><title>' + esc(p.name) + '</title></polyline>';
    });
    g += '<text x="' + c.l + '" y="' + (c.h - 12) + '" fill="#5b7c8c" font-size="11">día ' + simNum(d0) + '</text><text x="' + (c.w - c.r) + '" y="' + (c.h - 12) + '" text-anchor="end" fill="#5b7c8c" font-size="11">día ' + simNum(d1) + ' →</text>';
    return simSvg('Patrimonio de cada perfil a lo largo de los días, escala logarítmica, con los pisos de estatus' + (refs.length ? ' de ' + refs.map(function (r) { return simNum(r.valor); }).join(', ') : ''), g);
  }

  /* Gráfico 3: caja antes de la cuota del día 7 (p10 / p50 / p90) frente a la cuota */
  function simChartCash(S, profiles) {
    var c = SIM_CH, s = S.acto1_caja_antes_de_cuota, P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    var vals = [0, s.cuota * 1.15];
    P.forEach(function (p) { vals.push(s.perfiles[p.id].p10, s.perfiles[p.id].p90); });
    var ax = simLinAxis(Math.min.apply(null, vals), Math.max.apply(null, vals), c.h - c.b, c.t);
    var gw = (c.w - c.l - c.r) / P.length, g = simGrid(ax, c);
    P.forEach(function (p, i) {
      var q = s.perfiles[p.id], cx = c.l + gw * (i + 0.5);
      g += '<line x1="' + cx.toFixed(1) + '" y1="' + ax.y(q.p10).toFixed(1) + '" x2="' + cx.toFixed(1) + '" y2="' + ax.y(q.p90).toFixed(1) + '" stroke="' + p.color + '" stroke-width="14" stroke-linecap="round" opacity="0.35"><title>' + esc(p.name) + ': p10 ' + simNum(q.p10) + ' · p50 ' + simNum(q.p50) + ' · p90 ' + simNum(q.p90) + '</title></line>' +
        '<line x1="' + (cx - 14).toFixed(1) + '" y1="' + ax.y(q.p50).toFixed(1) + '" x2="' + (cx + 14).toFixed(1) + '" y2="' + ax.y(q.p50).toFixed(1) + '" stroke="' + p.color + '" stroke-width="3"/>';
      [['p90', q.p90], ['p50', q.p50], ['p10', q.p10]].forEach(function (e) {
        g += '<text x="' + (cx + 22).toFixed(1) + '" y="' + (ax.y(e[1]) + 4).toFixed(1) + '" fill="#c9dcdf" font-size="11">' + e[0] + ' ' + simNum(e[1]) + '</text>';
      });
      g += '<text x="' + cx.toFixed(1) + '" y="' + (c.h - 12) + '" text-anchor="middle" fill="#c9dcdf" font-size="12">' + esc(p.name) + '</text>';
    });
    var yc = ax.y(s.cuota).toFixed(1);
    g += '<line x1="' + c.l + '" y1="' + yc + '" x2="' + (c.w - c.r) + '" y2="' + yc + '" stroke="#c23b55" stroke-width="1.8" stroke-dasharray="6 4"/><text x="' + (c.w - c.r) + '" y="' + (yc - 5) + '" text-anchor="end" fill="#ef8da0" font-size="12">Cuota del día 7: ' + simNum(s.cuota) + '</text>';
    return simSvg('Caja antes de pagar la cuota del día 7 por perfil: percentiles 10, 50 y 90 frente a la cuota de ' + s.cuota, g);
  }

  function simRuleRows(res, profiles) {
    var q = state.sim, h = '';
    res.reglas.filter(function (r) { return (q.grupo === 'all' || r.grupo === q.grupo) && (q.estado === 'all' || r.estado === q.estado); }).forEach(function (r) {
      var open = !!q.open[r.id], fail = simFailing(r), cols = 7;
      h += '<tr class="sim-row ' + esc(r.estado) + '"><td><button class="sim-toggle" type="button" data-action="sim-row" data-value="' + esc(r.id) + '" aria-expanded="' + open + '" aria-label="Cifras por perfil de ' + esc(r.id) + '">' + (open ? '▾' : '▸') + '</button> <b>' + esc(r.id) + '</b></td>' +
        '<td>' + esc(r.titulo) + '<small class="sim-metric">' + esc(r.metrica) + '</small></td><td>' + simPill(r.estado) + '</td>' +
        '<td class="num-cell">' + simNum(r.valor) + simUnit(r) + (r.ic95 ? '<small class="sim-ic">IC 95 % ' + simIc(r.ic95) + (r.n != null ? ' · n = ' + simNum(r.n) : '') + '</small>' : (r.n != null ? '<small class="sim-ic">n = ' + simNum(r.n) + '</small>' : '')) + '</td>' +
        '<td class="num-cell">' + esc(simRange(r.umbral)) + '<small class="sim-ic">' + (r.origen === 'doc' ? 'del documento' : 'propuesto') + '</small></td>' +
        '<td>' + (fail.length ? esc(fail.map(function (k) { return (profiles.filter(function (p) { return p.id === k; })[0] || { name: k }).name; }).join(', ')) : '—') + '</td><td>' + simDocs(r.docs) + '</td></tr>';
      if (open) {
        var pp = r.por_perfil || {}, keys = profiles.filter(function (p) { return pp[p.id]; });
        h += '<tr class="sim-detail"><td colspan="' + cols + '">' + (keys.length ? '<table class="sim-sub"><thead><tr><th>Perfil</th><th>Valor</th><th>IC 95 %</th><th>n</th><th>Estado</th></tr></thead><tbody>' + keys.map(function (p) {
          var c = pp[p.id];
          return '<tr><td>' + esc(p.name) + '</td><td class="num-cell">' + simNum(c.valor) + simUnit(r) + '</td><td class="num-cell">' + (c.ic95 ? simIc(c.ic95) : '—') + '</td><td class="num-cell">' + (c.n != null ? simNum(c.n) : '—') + '</td><td>' + simPill(c.estado || r.estado) + '</td></tr>';
        }).join('') + '</tbody></table>' : '<small>Esta regla no se mide por perfil.</small>') + '</td></tr>';
      }
    });
    return h || '<tr><td colspan="7"><div class="empty">Ninguna regla con estos filtros.</div></td></tr>';
  }

  function simTrace(S, res) {
    var tr = (S.reglas && S.reglas.trazabilidad) || [];
    if (!tr.length) return '<div class="empty">reglas.json todavía no trae la trazabilidad requisito → regla.</div>';
    var byId = {}; res.reglas.forEach(function (r) { byId[r.id] = r; });
    return '<div class="table-wrap"><table><thead><tr><th>Requisito</th><th>Fuente</th><th>Reglas que lo comprueban</th></tr></thead><tbody>' + tr.map(function (t) {
      return '<tr><td>' + esc(t.requisito) + '</td><td>' + simDocs([t.fuente]) + '</td><td>' + (t.reglas.length ? t.reglas.map(function (id) {
        var r = byId[id];
        return '<span class="sim-st ' + (r ? esc(r.estado) : 'falla') + '" title="' + esc(r ? r.titulo + ' · ' + SIM_LABEL[r.estado] : 'regla inexistente') + '">' + esc(id) + '</span>';
      }).join(' ') : '<span class="sim-st falla">sin regla</span>') + '</td></tr>';
    }).join('') + '</tbody></table></div>';
  }

  function viewSimulator() {
    var S = H.sim, h = '<p class="eyebrow">Calidad</p><h1 class="page-title">Simulador de economía y progresión</h1>';
    if (!S || !S.disponible) {
      return h + '<div class="notice">' + esc(S ? S.motivo : 'El hub no trae datos del simulador.') + '. Genera los resultados con <code>python3 tools/sim/run.py --completo</code> y después <code>python3 studio/hub/build.py</code>.</div>';
    }
    var res = S.resultados, c = S.conteo, profiles = simProfiles(res), q = state.sim;
    var grupos = res.reglas.reduce(function (a, r) { if (a.indexOf(r.grupo) < 0) a.push(r.grupo); return a; }, []);
    var pct = c.total ? Math.round(100 * c.pasa / c.total) : 0;
    h += '<p class="page-lead">Comprueba con cifras que el equilibrio de <a href="#/docs/28-numeros-base-de-la-economia">los números base</a> se sostiene: cuatro perfiles de jugador recorren la campaña con las cifras de <a href="../data/world.json" target="_blank" rel="noopener">world.json</a>. Cada regla dice si <strong>pasa</strong>, <strong>falla</strong> o es <strong>incierta</strong> (el intervalo de confianza toca el umbral). Al cierre no puede haber reglas en falla ni inciertas.</p>';
    if (S.caducado) h += '<div class="sim-stale" role="alert"><strong>Resultado caducado.</strong> Las cifras de world.json cambiaron desde que se generó este resultado: lo que ves ya no vale. Reejecuta <code>python3 tools/sim/run.py --completo</code>.</div>';
    else if (!S.huella_verificada) h += '<div class="notice sim-unverified">La huella frente a world.json todavía no se puede verificar (falta tools/sim/mundo.py): solo se valida la forma del resultado.</div>';
    h += '<div class="cln-summary"><div class="ring" style="--p:' + pct + '"><b>' + c.pasa + '/' + c.total + '</b><span>reglas pasan</span></div><div class="st-grid">' +
      '<div class="st-card sim-ok"><small>Pasan</small><b>' + c.pasa + '</b><span>de ' + c.total + ' reglas</span></div>' +
      '<div class="st-card sim-bad"><small>Fallan</small><b>' + c.falla + '</b><span>' + (c.falla ? 'proponer un cambio de cifra' : 'ninguna') + '</span></div>' +
      '<div class="st-card sim-mid"><small>Inciertas</small><b>' + c.incierto + '</b><span>' + (c.incierto ? 'faltan corridas' : 'ninguna') + '</span></div>' +
      '<div class="st-card"><small>Generado</small><b class="sim-date">' + esc(res.generado) + '</b><span>' + profiles.length + ' perfiles · ' + (Array.isArray(res.semillas) ? res.semillas.length + ' semillas' : 'semillas fijas') + '</span></div></div></div>';

    h += '<h2 class="section-title">Reglas <small>valor medido frente al umbral · clic en ▸ para ver las cifras por perfil</small></h2>';
    h += '<div class="filters"><div class="filter-group"><span class="filter-label">Grupo</span>' + filterChips('sim-grupo', q.grupo, [['all', 'Todos']].concat(grupos.map(function (g) { return [g, g]; }))) + '</div>' +
      '<div class="filter-group"><span class="filter-label">Estado</span>' + filterChips('sim-estado', q.estado, [['all', 'Todos'], ['pasa', 'Pasa'], ['falla', 'Falla'], ['incierto', 'Incierto']]) + '</div></div>';
    h += '<div class="table-wrap"><table class="sim-table"><thead><tr><th>Regla</th><th>Qué se mide</th><th>Estado</th><th class="num-cell">Valor</th><th class="num-cell">Umbral</th><th>Perfil que falla</th><th>Documento</th></tr></thead><tbody>' + simRuleRows(res, profiles) + '</tbody></table></div>';

    h += '<h2 class="section-title">Gráficos</h2>';
    h += simFigure('Ingreso neto por hora en cada acto', 'Escala logarítmica. La línea ámbar es el objetivo del acto (la media del perfil medio) y la franja, su banda de ±' + Math.round((res.series.ingreso_hora_por_acto.banda == null ? 0.2 : res.series.ingreso_hora_por_acto.banda) * 100) + ' %.', simChartIncome(res.series, profiles), profiles, simIncomeRows(res.series, profiles));
    h += simFigure('Patrimonio de cada perfil en el tiempo', 'Escala logarítmica. Las líneas ámbar son los pisos de estatus (Comerciante, Empresario, Magnate); las verticales separan los actos.', simChartWealth(res.series, profiles), profiles, simWealthRows(res.series, profiles));
    h += simFigure('Caja antes de la cuota del día 7', 'Barra de p10 a p90 y marca en la mediana, por perfil. Por encima de la línea roja la cuota se paga a tiempo; por debajo, el jugador pide prórroga.', simChartCash(res.series, profiles), profiles, simCashRows(res.series, profiles));

    h += '<h2 class="section-title">Trazabilidad <small>requisito del diseño → regla que lo comprueba</small></h2>' + simTrace(S, res);
    return h;
  }
  function simIncomeRows(S, profiles) {
    var s = S.ingreso_hora_por_acto, P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    return { head: ['Acto', 'Objetivo'].concat(P.map(function (p) { return p.name; })), body: s.actos.map(function (a) { return [a, simNum(s.objetivo[a])].concat(P.map(function (p) { return simNum(s.perfiles[p.id][a]); })); }) };
  }
  function simWealthRows(S, profiles) {
    var s = S.patrimonio_por_dia, P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    var step = Math.max(1, Math.ceil(s.dias.length / 12)), idx = [];
    for (var i = 0; i < s.dias.length; i += step) idx.push(i);
    if (idx[idx.length - 1] !== s.dias.length - 1) idx.push(s.dias.length - 1);
    return { head: ['Día'].concat(P.map(function (p) { return p.name; })), body: idx.map(function (i) { return [simNum(s.dias[i])].concat(P.map(function (p) { return simNum(s.perfiles[p.id][i]); })); }) };
  }
  function simCashRows(S, profiles) {
    var s = S.acto1_caja_antes_de_cuota, P = profiles.filter(function (p) { return s.perfiles[p.id]; });
    return { head: ['Perfil', 'p10', 'p50', 'p90', 'Cuota'], body: P.map(function (p) { var q = s.perfiles[p.id]; return [p.name, simNum(q.p10), simNum(q.p50), simNum(q.p90), simNum(s.cuota)]; }) };
  }

  /* ---------- roadmap ---------- */
  function viewRoadmap() {
    var s = state.rm;
    var cur = currentPhase();
    if (!s.open) { s.open = {}; s.open[cur.id] = true; }
    var h = '<p class="eyebrow">Plan</p><h1 class="page-title">Roadmap</h1><p class="page-lead">Fases, hitos y tareas con su objetivo (MVP, Release 1 o Evolutivo), prioridad y estado. Las horas son horas del autor, no tiempo de cálculo de la IA. Actualizado el ' + esc(H.roadmap.meta.updated) + '. <a href="#/linea">Ver en línea de tiempo →</a></p>';
    h += '<div class="filters">' + scopeChips() + '<div class="filter-group"><span class="filter-label">Objetivo</span>';
    ['all'].concat(targets).forEach(function (t) {
      h += '<button class="chip" type="button" data-action="rm-target" data-value="' + esc(t) + '" aria-pressed="' + (s.target === t) + '">' + (t === 'all' ? 'Todos' : esc(t)) + '</button>';
    });
    h += '</div><div class="filter-group"><button class="chip" type="button" data-action="rm-hide" aria-pressed="' + s.hideDone + '">Ocultar finalizadas</button></div></div>' + prioLegend();

    var shown = 0;
    phases.forEach(function (p) {
      var all = phaseTasks(p);
      var list = all.filter(function (t) { return (s.target === 'all' || t.target === s.target) && inScope(t); });
      if (!list.length) return;
      shown++;
      var pr = progress(all);
      var sc = progress(list);
      h += '<details class="phase" data-phase="' + p.id + '"' + (s.open[p.id] ? ' open' : '') + '><summary><div><div class="phase-head"><span class="phase-id">' + esc(p.id) + '</span><span class="phase-title">' + esc(p.name) + '</span>' + targetPill(p.target) + '</div><div class="stat-sub">' + hoursLabel(p) + ' · ' + pr.nd + ' de ' + pr.n + ' tareas' + (state.scope !== 'all' ? ' · en este alcance: ' + sc.n + ' tareas, ' + num(sc.total) + ' h' : '') + '</div></div>' + bar(pr.pct, pr.pct === 100) + '<div class="pct">' + pr.pct + '%</div></summary><div class="phase-body">';
      h += '<p class="phase-goal">' + esc(p.goal) + '</p>';
      if (p.gate) h += '<div class="gate"><strong>◆ </strong>' + esc(p.gate) + '</div>';
      p.milestones.forEach(function (m) {
        var tasks = list.filter(function (t) { return t.ms.id === m.id; });
        if (s.hideDone) tasks = tasks.filter(function (t) { return t.status !== 'done'; });
        if (!tasks.length) return;
        var mp = progress(all.filter(function (t) { return t.ms.id === m.id; }));
        h += '<div class="ms"><div class="ms-head"><span>' + esc(m.id + ' · ' + m.name) + '</span><small>' + mp.nd + '/' + mp.n + ' · ' + num(mp.done) + '/' + num(mp.total) + ' h</small></div>';
        tasks.forEach(function (t) { h += taskRow(t); });
        h += '</div>';
      });
      h += '</div></details>';
    });
    if (!shown) h += '<div class="empty">No hay tareas para este filtro.</div>';
    return h;
  }
  function badges(t) {
    var parts = [];
    if (t.comments.length) parts.push('💬 ' + t.comments.length);
    if (t.evidence.length) parts.push('📎 ' + t.evidence.length);
    return parts.length ? '<span class="badges">' + parts.join(' · ') + '</span>' : '';
  }
  function taskRow(t) {
    var chk = '<span class="check ' + t.status + '" aria-hidden="true">' + (t.status === 'done' ? '✓' : '') + '</span>';
    var body = '<div class="task-body"><dl>' + (t.desc ? '<dt>Descripción</dt><dd>' + esc(t.desc) + '</dd>' : '') + (t.done_when ? '<dt>Listo cuando</dt><dd>' + esc(t.done_when) + '</dd>' : '') + '</dl><p><a href="#/tarea/' + esc(t.id) + '">Ver detalle, historial y evidencias →</a></p></div>';
    return '<details class="task"><summary>' + chk + '<span class="tid">' + esc(t.id) + '</span><span class="ttitle ' + t.status + '">' + esc(t.title) + badges(t) + '</span>' + prioPill(t.prio) + '<span class="est">' + num(t.est) + ' h</span>' + statusPill(t.status) + '</summary>' + body + '</details>';
  }

  /* ---------- línea de tiempo en horas ---------- */
  function viewTimeline() {
    var tl = state.tl;
    var list = TASKS.filter(function (t) {
      if (t.status === 'dropped' || !inScope(t)) return false;
      if (tl.target === 'launch') return t.target !== 'Evolutivo';
      return tl.target === 'all' || t.target === tl.target;
    });
    var LABEL = 190;
    var px = tl.px;
    var pos = 0, doneH = 0;
    var lanes = [], lmap = {};
    list.forEach(function (t) {
      var lane = lmap[t.phase.id];
      if (!lane) { lane = lmap[t.phase.id] = { p: t.phase, ms: [], mmap: {}, start: pos, end: pos, total: 0, done: 0 }; lanes.push(lane); }
      var m = lane.mmap[t.ms.id];
      if (!m) { m = lane.mmap[t.ms.id] = { m: t.ms, start: pos, end: pos, total: 0, done: 0, prio: { P0: 0, P1: 0, P2: 0, P3: 0 }, tasks: [] }; lane.ms.push(m); }
      m.tasks.push(t);
      m.total += t.est;
      m.prio[t.prio] += t.est;
      if (t.status === 'done') { m.done += t.est; lane.done += t.est; doneH += t.est; }
      pos += t.est;
      m.end = pos;
      lane.end = pos;
      lane.total += t.est;
    });
    var total = pos;
    var width = Math.round(LABEL + total * px + 70);

    var h = '<p class="eyebrow">Plan</p><h1 class="page-title">Línea de tiempo en horas</h1><p class="page-lead">Las tareas colocadas en el orden del plan, una detrás de otra, con el ancho proporcional a sus horas. No hay fechas: solo horas de trabajo del autor. Cambia el alcance para ver cuánto se acorta el camino si se recorta.</p>';
    h += '<div class="filters">' + scopeChips() + '<div class="filter-group"><label class="filter-label" for="tlTarget">Mostrar</label><select id="tlTarget" data-action="tl-target">' +
      [['launch', 'Hasta el lanzamiento'], ['all', 'Todo'], ['MVP', 'MVP'], ['Release 1', 'Release 1'], ['Evolutivo', 'Evolutivo']].map(function (o) { return '<option value="' + o[0] + '"' + (tl.target === o[0] ? ' selected' : '') + '>' + o[1] + '</option>'; }).join('') + '</select></div>' +
      '<div class="filter-group"><label class="filter-label" for="tlZoom">Zoom</label><input id="tlZoom" type="range" min="0.3" max="2.5" step="0.1" value="' + px + '" data-action="tl-zoom"></div>' +
      '<div class="filter-group"><label class="filter-label" for="tlRate">Equivalencia</label><select id="tlRate" data-action="tl-rate">' +
      [[0, 'Solo horas'], [5, '5 h por semana'], [10, '10 h por semana'], [20, '20 h por semana'], [30, '30 h por semana']].map(function (o) { return '<option value="' + o[0] + '"' + (tl.rate === o[0] ? ' selected' : '') + '>' + o[1] + '</option>'; }).join('') + '</select></div></div>' + prioLegend();

    var remaining = total - doneH;
    h += '<div class="grid grid-3" style="margin:14px 0 18px"><div class="card"><div class="stat-label">Total en este alcance</div><div class="stat-value">' + num(total) + ' h</div><div class="stat-sub">' + list.length + ' tareas</div></div>' +
      '<div class="card"><div class="stat-label">Hechas</div><div class="stat-value">' + num(doneH) + ' h</div><div class="stat-sub">' + (total ? Math.round(100 * doneH / total) : 0) + ' % del camino</div></div>' +
      '<div class="card"><div class="stat-label">Por recorrer</div><div class="stat-value">' + num(remaining) + ' h</div><div class="stat-sub">' + (tl.rate ? '≈ ' + Math.ceil(remaining / tl.rate) + ' semanas a ' + tl.rate + ' h por semana' : 'sin equivalencia en calendario') + '</div></div></div>';

    if (!total) return h + '<div class="empty">No hay tareas para este filtro.</div>';

    var step = [10, 25, 50, 100, 200, 500].filter(function (s) { return s * px >= 64; })[0] || 500;
    var ticks = '';
    for (var x = 0; x <= total; x += step) {
      ticks += '<span class="tl-tick" style="left:' + Math.round(LABEL + x * px) + 'px">' + x + ' h</span>';
    }
    var inner = '<div class="tl-inner" style="width:' + width + 'px"><div class="tl-ruler">' + ticks + '</div>';
    lanes.forEach(function (lane) {
      inner += '<div class="tl-lane"><div class="tl-lane-label"><strong>' + esc(lane.p.id + ' · ' + lane.p.name) + '</strong><small>' + num(lane.total) + ' h · ' + esc(lane.p.target) + '</small></div>';
      lane.ms.forEach(function (m) {
        var w = Math.max(4, Math.round((m.end - m.start) * px));
        var left = Math.round(LABEL + m.start * px);
        var pctDone = m.total ? Math.round(100 * m.done / m.total) : 0;
        var stripe = PRIOS.map(function (p) { return m.prio[p] ? '<i style="width:' + (100 * m.prio[p] / m.total) + '%;background:' + PRIO_COLOR[p] + '"></i>' : ''; }).join('');
        var tip = m.m.id + ' · ' + m.m.name + ' — ' + num(m.total) + ' h (' + num(m.done) + ' h hechas)';
        inner += '<button type="button" class="tl-block' + (tl.sel === m.m.id ? ' sel' : '') + '" data-action="tl-select" data-value="' + esc(m.m.id) + '" style="left:' + left + 'px;width:' + w + 'px;--p:' + pctDone + '%" title="' + esc(tip) + '" aria-label="' + esc(tip) + '"><span class="tl-name">' + (w > 60 ? esc(m.m.name) : '') + '</span><span class="tl-h">' + (w > 40 ? num(m.total) + ' h' : '') + '</span><span class="tl-prio">' + stripe + '</span></button>';
      });
      if (lane.p.gate) inner += '<span class="tl-gate" style="left:' + Math.round(LABEL + lane.end * px - 8) + 'px" title="' + esc(lane.p.gate) + '">◆</span>';
      inner += '</div>';
    });
    inner += '<div class="tl-today" style="left:' + Math.round(LABEL + doneH * px) + 'px"><span>Avance: ' + num(doneH) + ' h</span></div></div>';
    h += '<div class="tl-wrap" tabindex="0" aria-label="Línea de tiempo en horas">' + inner + '</div>';
    h += '<p class="stat-sub">Cada bloque es un hito: el relleno claro muestra lo hecho y la franja de abajo, la mezcla de prioridades. Toca un bloque para ver sus tareas. ◆ marca una puerta de decisión.</p>';

    var sel = null;
    lanes.forEach(function (l) { l.ms.forEach(function (m) { if (m.m.id === tl.sel) sel = m; }); });
    if (sel) {
      h += '<h2 class="section-title">' + esc(sel.m.id + ' · ' + sel.m.name) + ' <small>' + num(sel.total) + ' h · del hito ' + num(sel.start) + ' h al ' + num(sel.end) + ' h</small></h2><div class="card">';
      sel.tasks.forEach(function (t) {
        h += '<div class="phase-row" style="grid-template-columns:62px 1fr auto auto auto"><span class="tid">' + esc(t.id) + '</span><span>' + taskLink(t) + '</span>' + prioPill(t.prio) + '<span class="est">' + num(t.est) + ' h</span>' + statusPill(t.status) + '</div>';
      });
      h += '</div>';
    }

    h += '<h2 class="section-title">Horas acumuladas al final de cada fase</h2><div class="table-wrap"><table><thead><tr><th>Fase</th><th class="num-cell">Horas de la fase</th><th class="num-cell">Acumuladas</th><th>Puerta de decisión</th></tr></thead><tbody>';
    lanes.forEach(function (l) {
      h += '<tr><td>' + esc(l.p.id + ' · ' + l.p.name) + '</td><td class="num-cell">' + num(l.total) + ' h</td><td class="num-cell">' + num(l.end) + ' h' + (tl.rate ? ' · semana ' + Math.ceil(l.end / tl.rate) : '') + '</td><td>' + (l.p.gate ? esc(l.p.gate) : '—') + '</td></tr>';
    });
    return h + '</tbody></table></div>';
  }

  /* ---------- tablero ---------- */
  function viewBoard() {
    var b = state.board;
    var cur = currentPhase();
    var phaseId = b.phase === 'current' ? cur.id : b.phase;
    var list = TASKS.filter(function (t) {
      return (phaseId === 'all' || t.phase.id === phaseId) && (b.target === 'all' || t.target === b.target) && inScope(t);
    });
    var h = '<p class="eyebrow">Plan</p><h1 class="page-title">Tablero</h1><p class="page-lead">Tareas por estado. Los estados se guardan en el código del proyecto y los cambia Claude al trabajar: si una tarea pasó a «En proceso», es porque se editó su archivo de datos. Toca una tarjeta para ver su historial, evidencias y comentarios.</p>';
    h += '<div class="filters">' + scopeChips() + '<div class="filter-group"><label class="filter-label" for="bPhase">Fase</label><select id="bPhase" data-action="board-phase"><option value="all"' + (b.phase === 'all' ? ' selected' : '') + '>Todas</option><option value="current"' + (b.phase === 'current' ? ' selected' : '') + '>Fase actual (' + esc(cur.id) + ')</option>' +
      phases.map(function (p) { return '<option value="' + p.id + '"' + (b.phase === p.id ? ' selected' : '') + '>' + esc(p.id + ' · ' + p.name) + '</option>'; }).join('') + '</select></div>' +
      '<div class="filter-group"><label class="filter-label" for="bTarget">Objetivo</label><select id="bTarget" data-action="board-target"><option value="all">Todos</option>' +
      targets.map(function (t) { return '<option value="' + esc(t) + '"' + (b.target === t ? ' selected' : '') + '>' + esc(t) + '</option>'; }).join('') + '</select></div></div>' + prioLegend();
    h += '<div class="board">';
    STATUS_ORDER.forEach(function (st) {
      var cards = list.filter(function (t) { return t.status === st; });
      var lim = b.limit[st] || 12;
      h += '<section class="col" aria-label="' + STATUS[st].label + '"><div class="col-head"><span class="s-' + st + '">' + STATUS[st].glyph + ' ' + STATUS[st].label + '</span><small>' + cards.length + '</small></div><div class="col-body">';
      if (!cards.length) h += '<div class="empty">Sin tareas</div>';
      cards.slice(0, lim).forEach(function (t) {
        h += '<a class="kcard" href="#/tarea/' + esc(t.id) + '"><div>' + esc(t.title) + '</div><div class="meta"><span>' + esc(t.id) + '</span>' + prioPill(t.prio) + '<span>' + num(t.est) + ' h</span><span class="' + targetClass(t.target) + '">' + esc(t.target) + '</span>' + badges(t) + '</div></a>';
      });
      if (cards.length > lim) h += '<button type="button" class="chip more" data-action="board-more" data-value="' + st + '">Mostrar ' + Math.min(25, cards.length - lim) + ' más (' + (cards.length - lim) + ' ocultas)</button>';
      h += '</div></section>';
    });
    return h + '</div>';
  }



  /* ---------- presentación del juego ---------- */
  var deck = { idx: 0, io: null, n: 0, ids: [], secOf: [], first: {} };

  function pres() { return H.presentation || { sections: [], slides: [] }; }
  function secById(id) { return pres().sections.filter(function (x) { return x.id === id; })[0]; }
  function docLabel(id) {
    var d = H.docs.filter(function (x) { return x.id === id; })[0];
    return d ? d.title : id;
  }
  function arNum(ar) { var p = String(ar).split('/'); return parseFloat(p[0]) / parseFloat(p[1] || 1); }
  function clamp01(x) { return Math.max(0, Math.min(1, x)); }
  /* Recorta una celda de una hoja de arte: col y row cuentan desde 0; fx y fy son el punto de interés dentro de la celda. */
  function cropStyle(c, arn) {
    var cw = 1 / c.cols, ch = 1 / c.rows, zoom = c.zoom || 1;
    var vw = cw / zoom;
    var vh = vw * (c.w / c.h) / arn;
    if (vh > 1) { vh = 1; vw = vh * arn * (c.h / c.w); }
    var cx = (c.col + (c.fx == null ? 0.5 : c.fx)) * cw;
    var cy = (c.row + (c.fy == null ? 0.5 : c.fy)) * ch;
    var px = vw >= 1 ? 50 : clamp01((cx - vw / 2) / (1 - vw)) * 100;
    var py = vh >= 1 ? 50 : clamp01((cy - vh / 2) / (1 - vh)) * 100;
    return 'background-image:url(../' + c.file + ');background-size:' + (100 / vw).toFixed(2) + '% auto;background-position:' + px.toFixed(2) + '% ' + py.toFixed(2) + '%;';
  }
  function cropBox(sheet, ar, label) {
    return '<div class="cropbox" role="img" aria-label="' + esc(label || '') + '" style="aspect-ratio:' + ar + ';' + cropStyle(sheet, arNum(ar)) + '"></div>';
  }
  function sourceChips(s) {
    if (!s.source || !s.source.length) return '';
    return '<span class="sl-src">Fuente: ' + s.source.map(function (id) { return '<a href="#/docs/' + esc(id) + '">' + esc(docLabel(id)) + '</a>'; }).join(' · ') + '</span>';
  }
  function kicker(s) {
    var sec = secById(s.section);
    return '<p class="sl-kicker">' + (sec ? '<span class="sl-sec"><b>' + esc(sec.n) + '</b> ' + esc(sec.title) + '</span>' : '') + (s.kicker ? '<span>' + esc(s.kicker) + '</span>' : '') + '</p>';
  }
  function head(s) {
    return kicker(s) + (s.title ? '<h2 class="sl-title">' + inline(s.title) + '</h2>' : '') + (s.lead ? '<p class="sl-lead">' + inline(s.lead) + '</p>' : '');
  }
  function glyph(g, cls) { return g ? '<span class="gl ' + (cls || '') + '" aria-hidden="true">' + esc(g) + '</span>' : ''; }
  function chips(list) { return list && list.length ? '<div class="sl-chips">' + list.map(function (c) { return '<span class="sl-chip">' + esc(c) + '</span>'; }).join('') + '</div>' : ''; }
  function note(s) { return s.foot ? '<p class="sl-note">' + inline(s.foot) + '</p>' : ''; }
  function tiles(list, col) {
    return list && list.length ? '<div class="sl-tiles' + (col ? ' col' : '') + '">' + list.map(function (t) { return '<div class="sl-tile">' + glyph(t.glyph) + '<div><small>' + esc(t.label) + '</small><strong>' + inline(t.value) + '</strong></div></div>'; }).join('') + '</div>' : '';
  }
  function bigStats(list) {
    return list && list.length ? '<div class="sl-stats">' + list.map(function (st) { return '<div><b>' + esc(st.n) + '</b><span>' + esc(st.l) + '</span></div>'; }).join('') + '</div>' : '';
  }
  function figLink(file, caption, cls) {
    return '<figure class="sl-fig ' + (cls || '') + '"><a href="../' + esc(file) + '" target="_blank" rel="noopener"><img loading="lazy" src="../' + esc(file) + '" alt="' + esc(caption || '') + '"></a>' + (caption ? '<figcaption>' + esc(caption) + '</figcaption>' : '') + '</figure>';
  }

  function lCover(s) {
    return '<img class="bg-img" src="../' + esc(s.image) + '" alt=""><div class="bg-over bg-over-l"></div><div class="cover-body"><p class="sl-kicker"><span>' + esc(s.kicker) + '</span></p><h1 class="cover-title">' + esc(s.title) + '</h1><p class="cover-en">' + esc(s.titleEn) + '</p><p class="cover-tag">' + esc(s.tagline) + '</p>' + chips(s.chips) + '<p class="sl-hint">Flechas, Inicio y Fin para moverte · F: pantalla completa</p></div>';
  }
  function lAgenda(s) {
    var slides = pres().slides;
    return head(s) + '<div class="ag-grid">' + pres().sections.map(function (sec) {
      var count = slides.filter(function (x) { return x.section === sec.id; }).length;
      return '<button type="button" class="ag-item" data-action="deck-go" data-index="' + deck.first[sec.id] + '" style="--acc:' + esc(sec.accent) + '"><span class="ag-n">' + esc(sec.n) + '</span><h3>' + esc(sec.title) + '</h3><p>' + esc(sec.blurb) + '</p><small>' + count + ' láminas</small></button>';
    }).join('') + '</div>';
  }
  function lSection(s) {
    var sec = secById(s.section);
    return '<img class="bg-img" src="../' + esc(sec.image) + '" alt=""><div class="bg-over bg-over-c"></div><div class="sec-body"><span class="sec-n">' + esc(sec.n) + '</span><h2 class="sec-title">' + esc(sec.title) + '</h2><p class="sec-blurb">' + esc(sec.blurb) + '</p></div>';
  }
  function lStatement(s) {
    return kicker(s) + '<blockquote class="st-quote">' + inline(s.statement) + '</blockquote>' + (s.author ? '<p class="st-author">' + inline(s.author) + '</p>' : '') + tiles(s.tiles);
  }
  function lSpecs(s) {
    return head(s) + '<div class="sp-grid">' + s.items.map(function (it) {
      return '<div class="sp-item">' + glyph(it.glyph) + '<div><small>' + esc(it.label) + '</small><strong>' + inline(it.value) + '</strong></div></div>';
    }).join('') + '</div>';
  }
  function rangeVisual(rows) {
    return '<div class="rg">' + rows.map(function (r) {
      return '<div class="rg-row"><span>' + esc(r.label) + '</span><div class="rg-bar"><i style="left:' + r.min + '%;width:' + Math.max(2, r.max - r.min) + '%"></i></div><b>' + r.min + '–' + r.max + '%</b></div>';
    }).join('') + '</div>';
  }
  function lCards(s) {
    return head(s) + bigStats(s.stats) + '<div class="sl-cards' + (s.big ? ' big' : '') + '" style="--cols:' + (s.cols || 3) + '">' + s.cards.map(function (c, k) {
      return '<article class="sl-card">' + (s.numbered ? glyph(String(k + 1), 'num') : glyph(c.glyph)) + (c.tag ? '<span class="sl-tag">' + esc(c.tag) + '</span>' : '') + '<h3>' + inline(c.title) + '</h3>' + (c.text ? '<p>' + inline(c.text) + '</p>' : '') + (c.ranges ? rangeVisual(c.ranges) : '') + chips(c.chips) + '</article>';
    }).join('') + '</div>' + note(s);
  }
  function lDay(s) {
    return head(s) + '<div class="day-track">' + s.blocks.map(function (b, i) {
      return '<div class="day-block b' + i + '">' + glyph(b.glyph) + '<h3>' + esc(b.name) + '</h3><p>' + esc(b.text) + '</p></div>';
    }).join('<span class="day-arrow" aria-hidden="true">›</span>') + '</div><p class="day-cost">' + inline(s.cost) + '</p><div class="day-free"><strong>' + esc(s.free.title) + '</strong>' + s.free.items.map(function (it) { return '<span class="sl-chip">' + esc(it) + '</span>'; }).join('') + '</div>' + note(s);
  }
  function lCycle(s) {
    var box = function (b, cls) { return '<div class="cy-box ' + cls + '"><h3>' + esc(b.title) + '</h3><ul>' + b.points.map(function (p) { return '<li>' + esc(p) + '</li>'; }).join('') + '</ul></div>'; };
    return head(s) + '<div class="cy">' + box(s.left, 'cy-l') + '<div class="cy-mid"><div class="cy-arrow cy-to-r"><span>' + esc(s.toRight) + '</span></div><div class="cy-arrow cy-to-l"><span>' + esc(s.toLeft) + '</span></div></div>' + box(s.right, 'cy-r') + '</div>';
  }
  function lShowcase(s) {
    return head(s) + '<div class="sc">' + figLink(s.image, s.caption) + '<ul class="sc-list">' + s.items.map(function (it) { return '<li><b>' + esc(it.name) + '</b><span>' + esc(it.tension) + '</span></li>'; }).join('') + '</ul></div>' + note(s);
  }
  function marketChart() {
    return '<svg class="mkt-chart" viewBox="0 0 440 250" role="img" aria-label="Ejemplo: tras una noticia, el valor justo cambia y el precio lo alcanza con retraso">' +
      '<g stroke="#2a3d4a" stroke-width="1"><line x1="30" y1="24" x2="30" y2="214"/><line x1="30" y1="214" x2="430" y2="214"/></g>' +
      '<line x1="210" y1="30" x2="210" y2="214" stroke="#8fb0ba" stroke-dasharray="3 4"/>' +
      '<path d="M30 124 H210 V82 H430" fill="none" stroke="#e3b25c" stroke-width="2" stroke-dasharray="6 5"/>' +
      '<polyline fill="none" stroke="#c23b55" stroke-width="2.6" stroke-linejoin="round" points="30,130 50,120 70,128 90,116 110,124 130,130 150,118 170,126 190,122 210,124 230,116 250,106 270,96 290,88 310,82 330,78 350,86 370,80 390,84 410,78 430,82"/>' +
      '<text x="216" y="44" fill="#8fb0ba" font-size="12">Noticia: huelga en el Hollín</text>' +
      '<text x="34" y="236" fill="#5b7c8c" font-size="11">tiempo →</text>' +
      '<line x1="40" y1="16" x2="64" y2="16" stroke="#e3b25c" stroke-width="2" stroke-dasharray="6 5"/><text x="70" y="20" fill="#c9dcdf" font-size="12">Valor justo</text>' +
      '<line x1="170" y1="16" x2="194" y2="16" stroke="#c23b55" stroke-width="2.6"/><text x="200" y="20" fill="#c9dcdf" font-size="12">Precio (llega con retraso)</text></svg>';
  }
  function lMarket(s) {
    return head(s) + '<div class="mkt"><div class="mkt-left">' + marketChart() + '</div><div class="mkt-right">' + s.points.map(function (p) {
      return '<div class="sl-tile">' + glyph(p.glyph) + '<div><strong>' + esc(p.title) + '</strong><small>' + inline(p.text) + '</small></div></div>';
    }).join('') + '</div></div>' + note(s);
  }
  function lLadder(s) {
    return head(s) + '<div class="ld">' + s.steps.map(function (st, i) {
      return '<div class="ld-step" style="--lv:' + (i + 1) + '"><span class="sl-tag">' + esc(st.tag) + '</span><h3>' + esc(st.title) + '</h3><p>' + esc(st.text) + '</p></div>';
    }).join('') + '</div>' + note(s);
  }
  function lMeter(s) {
    return head(s) + bigStats(s.facts) + '<div class="mt"><div class="mt-bar">' + s.zones.map(function (z) { return '<i style="flex:' + z.w + ';background:' + esc(z.color) + '"></i>'; }).join('') + '</div><div class="mt-zones">' + s.zones.map(function (z) {
      return '<div style="flex:' + z.w + '"><b style="color:' + esc(z.color) + '">' + esc(z.name) + '</b><small>' + esc(z.range) + '</small><p>' + esc(z.text) + '</p></div>';
    }).join('') + '</div></div><div class="mt-low"><strong>' + esc(s.lowerTitle) + '</strong>' + chips(s.lower) + '</div>';
  }
  function lFlow(s) {
    return head(s) + '<ol class="fl' + (s.colored ? ' colored' : '') + '">' + s.steps.map(function (st) {
      return '<li' + (s.colored ? ' class="s-' + esc(st.title) + '"' : '') + '>' + glyph(st.glyph) + '<h3>' + esc(st.title) + '</h3><p>' + esc(st.text) + '</p></li>';
    }).join('') + '</ol>' + chips(s.chips) + (s.warn ? '<p class="fl-warn">' + inline(s.warn) + '</p>' : '');
  }
  function lScale(s) {
    var heat = ['#4fb6a5', '#e3b25c', '#ef8da0', '#c23b55'];
    return head(s) + '<div class="sc-bar">' + heat.map(function (c) { return '<i style="background:' + c + '"></i>'; }).join('') + '</div><div class="sc-levels">' + s.levels.map(function (l, i) {
      return '<div class="sc-level" style="--c:' + heat[i] + '"><h3>' + esc(l.name) + '</h3><p>' + esc(l.text) + '</p></div>';
    }).join('') + '</div><div class="sl-cards" style="--cols:3">' + s.facts.map(function (f) {
      return '<article class="sl-card">' + glyph(f.glyph) + '<h3>' + esc(f.title) + '</h3><p>' + esc(f.text) + '</p></article>';
    }).join('') + '</div>';
  }
  function lMap(s) {
    return head(s) + '<div class="mp"><div class="mp-img"><img loading="lazy" src="../' + esc(s.image) + '" alt="Mapa de Valdoria">' + s.spots.map(function (sp) {
      return '<span class="mp-pin" style="left:' + (sp.x * 100) + '%;top:' + (sp.y * 100) + '%" title="' + esc(sp.name) + '">' + sp.n + '</span>';
    }).join('') + '</div><ol class="mp-legend">' + s.spots.map(function (sp) {
      return '<li><span class="mp-n">' + sp.n + '</span><div><b>' + esc(sp.name) + '</b><small>' + esc(sp.text) + '</small></div></li>';
    }).join('') + '</ol></div>';
  }
  function lCrops(s) {
    var ar = s.ar || '1/1';
    return head(s) + '<div class="cr' + (s.compact ? ' compact' : '') + '" style="--cols:' + s.cols + '">' + s.items.map(function (it) {
      return '<figure class="cr-item' + (it.hot ? ' hot' : '') + '">' + cropBox(it.sheet, ar, it.title) + '<figcaption><b>' + esc(it.title) + '</b>' + (it.tag ? '<span class="sl-tag">' + esc(it.tag) + '</span>' : '') + (it.text ? '<small>' + esc(it.text) + '</small>' : '') + '</figcaption></figure>';
    }).join('') + '</div>' + note(s);
  }
  function lFeature(s) {
    var m = s.media;
    var media = '<figure class="ft-media' + (m.glow ? ' glow' : '') + '">' + cropBox(m.sheet, m.ar || '1/1', m.caption) + (m.caption ? '<figcaption>' + esc(m.caption) + '</figcaption>' : '') + '</figure>';
    var body = kicker(s) + '<h2 class="sl-title">' + inline(s.title) + '</h2><p class="sl-lead">' + inline(s.text) + '</p>' + tiles(s.tiles, true) +
      (s.outcomes ? '<div class="ft-out">' + s.outcomes.map(function (o, i) { return '<div class="ft-o"><span class="gl num">' + (i + 1) + '</span><div><strong>' + esc(o.title) + '</strong><small>' + esc(o.text) + '</small></div></div>'; }).join('') + '</div>' : '') + note(s);
    return '<div class="ft"><div>' + media + '</div><div>' + body + '</div></div>';
  }
  function lActs(s) {
    return head(s) + '<ol class="ac">' + s.acts.map(function (a) {
      return '<li>' + cropBox(a.sheet, '16/10', a.title) + '<span class="ac-n">' + esc(a.n) + '</span><span class="sl-tag">' + esc(a.tag) + '</span><h3>' + esc(a.title) + '</h3><p>' + esc(a.text) + '</p></li>';
    }).join('') + '</ol>' + note(s);
  }
  function lPalette(s) {
    var p = H.palette;
    return head(s) + '<div class="pl-grid">' + p.colors.map(function (c) {
      return '<div class="pl-sw"><i style="background:' + esc(c.hex) + '"></i><b>' + esc(c.name) + '</b><small>' + esc(c.hex) + '</small></div>';
    }).join('') + '</div><div class="pl-bar">' + p.proportion.map(function (x) { return '<i style="width:' + x.pct + '%;background:' + esc(x.color) + '"></i>'; }).join('') + '</div><div class="pl-leg">' + p.proportion.map(function (x) {
      return '<span><i style="background:' + esc(x.color) + '"></i>' + esc(x.label) + ' ' + x.pct + '%</span>';
    }).join('') + '</div><ul class="pl-rules">' + s.rules.map(function (r) { return '<li>' + esc(r) + '</li>'; }).join('') + '</ul>';
  }
  function lMosaic(s) {
    return head(s) + '<div class="mo">' + s.images.map(function (im, i) { return figLink(im.file, im.caption, 'mo-' + i); }).join('') + '</div>' + chips(s.chips) + note(s);
  }
  function lBrand(s) {
    return head(s) + '<div class="br"><div>' + chips(s.chips) + '<div class="br-bubbles">' + s.voice.map(function (v) {
      return '<div class="bubble"><span class="sl-tag">' + esc(v.lang) + '</span><p>' + inline(v.text) + '</p></div>';
    }).join('') + '</div></div><div class="br-tags">' + s.taglines.map(function (t) { return '<p class="br-es">' + esc(t.es) + '</p><p class="br-en">' + esc(t.en) + '</p>'; }).join('') + '<p class="br-sym">Símbolo de marca: ' + esc(s.symbol) + '</p></div></div>';
  }
  function lArch(s) {
    return head(s) + '<div class="ar"><div class="ar-app">' + esc(s.app) + '</div><div class="ar-mods">' + s.modules.map(function (m) { return '<span>' + esc(m) + '</span>'; }).join('') + '</div><div class="ar-detail"><div class="ar-layers">' + s.layers.map(function (l, i) {
      return '<div class="ar-layer l' + i + '"><b>' + esc(l.name) + '</b><small>' + esc(l.text) + '</small></div>';
    }).join('') + '</div><div class="ar-badges">' + chips(s.badges) + '<p class="ar-cap">Cada módulo tiene estas capas. Las dependencias apuntan hacia el dominio.</p></div></div></div>';
  }
  var PHASE_COLORS = ['#8fb0ba', '#86c5e8', '#4fb6a5', '#e3b25c', '#c23b55', '#b8893a', '#5b7c8c'];
  function lPlan(s) {
    var live = TASKS.filter(function (t) { return t.status !== 'dropped'; });
    var total = live.reduce(function (a, t) { return a + t.est; }, 0);
    var cum = 0, segs = '', gates = '', rows = '';
    phases.forEach(function (p, i) {
      var l = live.filter(function (t) { return t.phase.id === p.id; });
      var hrs = l.reduce(function (a, t) { return a + t.est; }, 0);
      var dn = l.filter(function (t) { return t.status === 'done'; }).reduce(function (a, t) { return a + t.est; }, 0);
      cum += hrs;
      segs += '<div class="pb-seg' + (p.target === 'Evolutivo' ? ' later' : '') + '" style="flex:' + hrs + ';--c:' + PHASE_COLORS[i % PHASE_COLORS.length] + '" title="' + esc(p.name) + '"><i style="width:' + (hrs ? 100 * dn / hrs : 0) + '%"></i><b>' + esc(p.id) + '</b><small>' + num(hrs) + ' h</small></div>';
      if (p.gate) gates += '<span class="pb-gate" style="left:' + (100 * cum / total) + '%" title="' + esc(p.gate) + '">◆<em>hora ' + num(cum) + '</em></span>';
      rows += '<tr><td><b>' + esc(p.id) + '</b> ' + esc(p.name) + '</td><td>' + esc(p.target) + '</td><td class="num-cell">' + num(hrs) + ' h</td><td class="num-cell">' + num(cum) + ' h</td></tr>';
    });
    var launch = live.filter(function (t) { return t.target !== 'Evolutivo'; });
    var lh = launch.reduce(function (a, t) { return a + t.est; }, 0);
    var cp = 0;
    var pri = PRIOS.map(function (p) {
      var h = launch.filter(function (t) { return t.prio === p; }).reduce(function (a, t) { return a + t.est; }, 0);
      cp += h;
      return '<div class="pr-seg" style="flex:' + h + ';background:' + PRIO_COLOR[p] + '"><b>' + p + '</b><small>' + num(h) + ' h · acum. ' + num(cp) + '</small></div>';
    }).join('');
    return head(s) + '<div class="pb-wrap"><div class="pb">' + segs + '</div>' + gates + '</div><p class="sl-note">Barra proporcional a las horas de cada fase; el relleno claro es lo hecho. ◆ marca las puertas de decisión: <b>¿es divertido?</b> y <b>¿seguimos hacia la versión 1?</b></p>' +
      '<h3 class="sl-sub">Hasta el lanzamiento: ' + num(lh) + ' h por prioridad</h3><div class="pr">' + pri + '</div><details class="pl-det"><summary>Ver tabla de fases</summary><div class="table-wrap"><table><thead><tr><th>Fase</th><th>Objetivo</th><th class="num-cell">Horas</th><th class="num-cell">Acumuladas</th></tr></thead><tbody>' + rows + '</tbody></table></div></details>';
  }
  function lStatus(s) {
    var adr = H.docs.filter(function (d) { return d.id.indexOf('adr-') === 0; }).length;
    var live = TASKS.filter(function (t) { return t.status !== 'dropped'; });
    var done = live.filter(function (t) { return t.status === 'done'; });
    var tot = live.reduce(function (a, t) { return a + t.est; }, 0);
    var dh = done.reduce(function (a, t) { return a + t.est; }, 0);
    var pct = Math.round(100 * dh / tot);
    var by = function (st) { return live.filter(function (t) { return t.status === st; }).length; };
    var card = function (label, value, sub) { return '<div class="st-card"><small>' + esc(label) + '</small><b>' + value + '</b><span>' + sub + '</span></div>'; };
    var queue = TASKS.filter(function (t) { return t.status !== 'done' && t.status !== 'dropped'; })
      .map(function (t, idx) { return { t: t, idx: idx }; })
      .sort(function (a, b) { return (QUEUE_ORDER[a.t.status] - QUEUE_ORDER[b.t.status]) || (PRANK[a.t.prio] - PRANK[b.t.prio]) || (a.idx - b.idx); }).slice(0, 5);
    return head(s) + '<div class="stt"><div class="ring" style="--p:' + pct + '"><b>' + pct + '%</b><span>del plan</span></div><div class="st-grid">' +
      card('Tareas', live.length, done.length + ' finalizadas · ' + by('review') + ' en revisión') +
      card('Documentos', H.docs.length - adr, adr + ' decisiones (ADR)') +
      card('Casos de QA', (H.qa && H.qa.cases ? H.qa.cases.length : 0), 'sin ejecutar aún') +
      card('Arte de referencia', H.assets.images.length, 'imágenes con IA') + '</div></div>' +
      '<h3 class="sl-sub">Lo siguiente</h3><ul class="sl-next">' + queue.map(function (q) { return '<li><span class="tid">' + esc(q.t.id) + '</span> ' + esc(q.t.title) + ' ' + statusPill(q.t.status) + '</li>'; }).join('') + '</ul>';
  }
  function lChecklist(s) {
    return head(s) + '<div class="cl">' + s.items.map(function (it) {
      return '<div class="cl-item"><span class="cl-box" aria-hidden="true"></span><div><strong>' + esc(it.title) + '</strong><small>' + esc(it.text) + '</small></div></div>';
    }).join('') + '</div>';
  }
  function lClosing(s) {
    return '<img class="bg-img" src="../' + esc(s.image) + '" alt=""><div class="bg-over bg-over-c"></div><div class="sec-body"><p class="sl-kicker"><span>' + esc(s.kicker) + '</span></p><h2 class="cover-title">' + esc(s.title) + '</h2>' + s.taglines.map(function (t, i) { return '<p class="' + (i ? 'cover-en' : 'cover-tag') + '">' + esc(t) + '</p>'; }).join('') + '</div>';
  }
  var LAYOUTS = { cover: lCover, section: lSection, closing: lClosing };
  var BODY = { agenda: lAgenda, statement: lStatement, specs: lSpecs, cards: lCards, day: lDay, cycle: lCycle, showcase: lShowcase, market: lMarket, ladder: lLadder, meter: lMeter, flow: lFlow, scale: lScale, map: lMap, crops: lCrops, feature: lFeature, acts: lActs, palette: lPalette, mosaic: lMosaic, brand: lBrand, arch: lArch, plan: lPlan, status: lStatus, checklist: lChecklist };

  function slideHtml(s, i, n) {
    var sec = secById(s.section);
    var style = sec ? ' style="--acc:' + esc(sec.accent) + '"' : '';
    var h = '<section class="slide lay-' + esc(s.layout) + '" id="slide-' + esc(s.id) + '" data-idx="' + i + '"' + style + ' aria-label="' + esc(s.title || (sec && sec.title) || s.id) + '">';
    if (LAYOUTS[s.layout]) h += LAYOUTS[s.layout](s);
    else h += '<div class="slide-body">' + (BODY[s.layout] ? BODY[s.layout](s) : '') + '</div>';
    h += '<div class="sl-foot">' + sourceChips(s) + '<span class="sl-num">' + (sec ? esc(sec.n) + ' · ' + esc(sec.title) + ' · ' : '') + (i + 1) + ' / ' + n + '</span></div></section>';
    return h;
  }
  function viewGame() {
    var p = pres();
    var slides = p.slides;
    if (!slides.length) return '<div class="notice">No hay láminas. Revisa <code>studio/data/presentation.json</code>.</div>';
    deck.n = slides.length;
    deck.ids = slides.map(function (s) { return s.id; });
    deck.secOf = slides.map(function (s) { return s.section || ''; });
    deck.first = {};
    slides.forEach(function (s, i) { if (s.section && deck.first[s.section] == null) deck.first[s.section] = i; });
    var pills = p.sections.map(function (sec) {
      return '<button type="button" class="deck-pill" data-sec="' + esc(sec.id) + '" data-action="deck-go" data-index="' + deck.first[sec.id] + '" style="--acc:' + esc(sec.accent) + '" title="' + esc(sec.title) + '"><i></i><b>' + esc(sec.n) + '</b><span>' + esc(sec.title) + '</span></button>';
    }).join('');
    return '<div class="deck-wrap" id="deckWrap"><div class="deck-bar"><div class="deck-title"><strong>El juego</strong><span id="deckCount">1 / ' + slides.length + '</span></div><div class="deck-pills">' + pills + '</div><div class="deck-actions">' +
      '<button class="chip" type="button" data-action="deck-prev" aria-label="Lámina anterior">‹</button><button class="chip" type="button" data-action="deck-next" aria-label="Lámina siguiente">›</button>' +
      '<button class="chip" type="button" data-action="deck-full" title="Tecla F">Pantalla completa</button><button class="chip" type="button" data-action="deck-print" title="Imprimir o guardar como PDF">PDF</button></div><div class="deck-prog"><i id="deckProg"></i></div></div>' +
      '<div class="deck" id="deck" tabindex="0" aria-label="Presentación del juego">' + slides.map(function (s, i) { return slideHtml(s, i, slides.length); }).join('') + '</div></div>';
  }
  function setDeckIdx(i) {
    deck.idx = i;
    var c = $('#deckCount');
    if (c) c.textContent = (i + 1) + ' / ' + deck.n;
    var pr = $('#deckProg');
    if (pr) pr.style.width = (100 * (i + 1) / deck.n) + '%';
    $all('.deck-pill').forEach(function (b) { if (b.getAttribute('data-sec') === deck.secOf[i]) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
  }
  function gotoSlide(i) {
    if (i < 0 || i >= deck.n) return;
    var el = document.getElementById('slide-' + deck.ids[i]);
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (el) el.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'start' });
    setDeckIdx(i);
  }
  function initDeck() {
    var d = $('#deck');
    if (!d || !('IntersectionObserver' in window)) { setDeckIdx(0); return; }
    deck.io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) setDeckIdx(+en.target.getAttribute('data-idx')); });
    }, { root: d, threshold: 0.55 });
    $all('.slide', d).forEach(function (el) { deck.io.observe(el); });
    setDeckIdx(0);
  }
  function teardownDeck() {
    if (deck.io) { deck.io.disconnect(); deck.io = null; }
    if (document.fullscreenElement && document.exitFullscreen) { try { document.exitFullscreen(); } catch (e) { /* sin acción */ } }
  }
  function toggleFullscreen() {
    var w = $('#deckWrap');
    if (!w) return;
    try {
      if (document.fullscreenElement) document.exitFullscreen();
      else if (w.requestFullscreen) w.requestFullscreen();
    } catch (e) { toast('Tu navegador no permite pantalla completa aquí'); }
  }
  document.addEventListener('keydown', function (e) {
    if (parseHash().segs[0] !== 'juego' || !$('#lightbox').hidden) return;
    var tag = (e.target && e.target.tagName) || '';
    if (/INPUT|SELECT|TEXTAREA/.test(tag) || e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ') { e.preventDefault(); gotoSlide(deck.idx + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); gotoSlide(deck.idx - 1); }
    else if (k === 'Home') { e.preventDefault(); gotoSlide(0); }
    else if (k === 'End') { e.preventDefault(); gotoSlide(deck.n - 1); }
    else if (k === 'f' || k === 'F') { e.preventDefault(); toggleFullscreen(); }
  });

  /* ---------- mapa de historia ---------- */
  /* Filas «Bifurcaciones» y «Consecuencias»: salen de decisions.json, no de story.json. */
  function decisionRows(st) {
    var D = H.decisions;
    if (!D || !D.nodes.length) return '';
    function cells(fn) {
      return st.acts.map(function (a) { return '<div class="st-cell" style="--c:' + esc(a.color) + '">' + fn(D.nodes.filter(function (n) { return n.acto === a.n; })) + '</div>'; }).join('');
    }
    var forks = cells(function (nodes) {
      var big = nodes.filter(function (n) { return n.nivel !== 'pequena'; });
      return big.length ? '<ul>' + big.map(function (n) { return '<li><a href="#/decisiones">' + esc(n.titulo) + '</a> <small>' + esc(LEVEL[n.nivel].label.toLowerCase()) + '</small></li>'; }).join('') + '</ul>' : '<p class="stat-sub">—</p>';
    });
    var smalls = cells(function (nodes) {
      var n = nodes.filter(function (x) { return x.nivel === 'pequena'; }).length;
      return '<p><a href="#/decisiones">' + n + ' decisiones pequeñas</a></p>';
    });
    return '<div class="st-row"><div class="st-lab"><span class="gl" aria-hidden="true">⑂</span>Bifurcaciones</div>' + forks + '</div>' +
      '<div class="st-row"><div class="st-lab"><span class="gl" aria-hidden="true">↳</span>Consecuencias</div>' + smalls + '</div>';
  }
  function viewStory() {
    var st = H.story || { acts: [], lanes: [], after: '' };
    var byId = {};
    TASKS.forEach(function (t) { byId[t.id] = t; });
    var h = '<p class="eyebrow">Diseño del juego</p><h1 class="page-title">Mapa de historia</h1><p class="page-lead">Los cuatro actos en columnas y, en filas, lo que pasa y se desbloquea en cada uno. Los actos se activan por umbrales y se pueden recorrer con más o menos desvíos, así que la duración es orientativa. Documento: ' + '<a href="#/docs/17-mapa-de-historia">17 · Mapa de historia</a>.</p>';
    h += '<div class="story" style="--n:' + st.acts.length + '">';
    h += '<div class="st-row st-head"><div class="st-lab"></div>' + st.acts.map(function (a) {
      return '<div class="st-act" style="--c:' + esc(a.color) + '"><span class="st-n">Acto ' + esc(a.n) + '</span><h2>' + esc(a.title) + '</h2><small>' + esc(a.place) + '</small><span class="st-time">⏱ ' + esc(a.time) + '</span></div>';
    }).join('') + '</div>';
    h += '<div class="st-row st-close"><div class="st-lab"><span class="gl" aria-hidden="true">⚑</span>Se cierra cuando</div>' + st.acts.map(function (a) {
      return '<div class="st-cell" style="--c:' + esc(a.color) + '"><p>' + esc(a.closes) + '</p></div>';
    }).join('') + '</div>';
    st.lanes.forEach(function (l) {
      h += '<div class="st-row"><div class="st-lab"><span class="gl" aria-hidden="true">' + esc(l.glyph || '•') + '</span>' + esc(l.label) + '</div>' + st.acts.map(function (a, i) {
        var cell = l.cells[i] || [];
        return '<div class="st-cell" style="--c:' + esc(a.color) + '"><ul>' + cell.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></div>';
      }).join('') + '</div>';
    });
    h += decisionRows(st);
    h += '<div class="st-row"><div class="st-lab"><span class="gl" aria-hidden="true">▤</span>Tareas del plan</div>' + st.acts.map(function (a) {
      return '<div class="st-cell" style="--c:' + esc(a.color) + '"><ul class="st-tasks">' + (a.tasks || []).map(function (id) {
        var t = byId[id];
        return t ? '<li>' + statusPill(t.status) + ' <a href="#/tarea/' + esc(t.id) + '"><span class="tid">' + esc(t.id) + '</span> ' + esc(t.title) + '</a></li>' : '';
      }).join('') + '</ul></div>';
    }).join('') + '</div>';
    h += '</div>';
    if (st.after) h += '<p class="st-after">' + esc(st.after) + '</p>';
    return h;
  }

  /* ---------- árbol de decisiones ---------- */
  var LEVEL = {
    grande: { label: 'Grande', glyph: '◆' },
    mediana: { label: 'Mediana', glyph: '◈' },
    pequena: { label: 'Pequeña', glyph: '◇' }
  };
  var LEVEL_ORDER = ['grande', 'mediana', 'pequena'];
  function decisionMark(estado) {
    return estado === 'ok' ? '<span class="mk" title="Acordado por el autor">✅</span>' : '<span class="mk" title="Propuesta del narrador pendiente de confirmar">🟡</span>';
  }
  function flagChip(id, flags) {
    var f = flags[id];
    return '<span class="chip dc-flag ' + (f && f.tipo === 'medidor' ? 'brass' : '') + '" title="' + esc(f ? f.descripcion : id) + '">' + esc(id) + '</span>';
  }
  function flagChips(ids, flags) { return ids.map(function (id) { return flagChip(id, flags); }).join(' '); }
  function nodeFlags(n) {
    var set = [];
    n.opciones.forEach(function (o) { o.fija.forEach(function (f) { if (set.indexOf(f) < 0) set.push(f); }); });
    return set;
  }
  function nodeWhos(n, flags) {
    var out = [];
    nodeFlags(n).concat(n.lee).forEach(function (id) {
      ((flags[id] || {}).personajes || []).forEach(function (w) { if (out.indexOf(w) < 0) out.push(w); });
    });
    return out;
  }
  function decisionOption(o, flags, showFix) {
    var rows = [['Mundo', o.mundo], ['Mercado', o.mercado], ['Personajes', o.personajes]].filter(function (r) { return r[1] && r[1] !== '—'; });
    return '<li class="dc-opt"><b>' + esc(o.texto) + '</b><dl>' + rows.map(function (r) { return '<dt>' + r[0] + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') + '</dl>' +
      (showFix && o.fija.length ? '<div class="dc-fx">→ fija ' + flagChips(o.fija, flags) + '</div>' : '') + '</li>';
  }
  function decisionCard(n, flags) {
    var lv = LEVEL[n.nivel];
    var fija = nodeFlags(n);
    var differ = n.opciones.some(function (o) { return o.fija.join() !== n.opciones[0].fija.join(); });  // si todas fijan lo mismo, basta el resumen de abajo
    var h = '<article class="dc-card dc-' + n.nivel + '" id="' + esc(n.id) + '"><header><span class="dc-level" title="Decisión ' + lv.label.toLowerCase() + '"><span aria-hidden="true">' + lv.glyph + '</span> ' + lv.label + '</span>' + decisionMark(n.estado) + '</header>';
    h += '<h3>' + esc(n.titulo) + '</h3><p class="dc-trigger"><small>Dispara</small> ' + esc(n.dispara) + '</p>';
    h += '<ul class="dc-opts">' + n.opciones.map(function (o) { return decisionOption(o, flags, differ); }).join('') + '</ul>';
    if (n.lee.length || fija.length) {
      h += '<div class="dc-flow">' + (n.lee.length ? '<span><small>Lee</small> ' + flagChips(n.lee, flags) + '</span>' : '') + (n.lee.length && fija.length ? ' <span class="dc-arrow" aria-hidden="true">→</span> ' : '') + (fija.length ? '<span><small>Fija</small> ' + flagChips(fija, flags) + '</span>' : '') + '</div>';
    }
    return h + '</article>';
  }
  function decisionBottleneck(c, titles, visible) {
    return '<div class="dc-neck"><b>⇣ ' + esc(c.titulo) + '</b><small>Reúne ' + c.recibe.map(function (id) { return '<span' + (visible[id] ? '' : ' class="dc-off"') + '>' + esc(titles[id] || id) + '</span>'; }).join(' · ') + '</small></div>';
  }
  function decisionColumn(a, D, flags, visible) {
    var titles = {};
    D.nodes.forEach(function (n) { titles[n.id] = n.titulo; });
    var nodes = D.nodes.filter(function (n) { return n.acto === a.n; });
    var shown = nodes.filter(function (n) { return visible[n.id]; });
    var necks = D.cuellos.filter(function (c) { return c.acto === a.n; });
    var h = '<section class="dc-col" style="--c:' + esc(a.color) + '"><div class="dc-col-head"><span class="st-n">Acto ' + esc(a.n) + '</span><h2>' + esc(a.title) + '</h2><small>' + shown.length + ' de ' + nodes.length + ' decisiones</small></div>';
    var after = {};
    necks.forEach(function (c) {
      var pos = -1;
      shown.forEach(function (n, i) { if (c.recibe.indexOf(n.id) >= 0) pos = i; });
      if (pos >= 0) (after[pos] = after[pos] || []).push(c);
    });
    shown.forEach(function (n, i) {
      h += decisionCard(n, flags);
      (after[i] || []).forEach(function (c) { h += decisionBottleneck(c, titles, visible); });
    });
    if (!shown.length) h += '<div class="empty">Ninguna decisión con este filtro.</div>';
    return h + '</section>';
  }
  function decisionSummary(D, acts) {
    var cupos = D.meta.cupos || {};
    var count = function (lv) { return D.nodes.filter(function (n) { return n.nivel === lv; }).length; };
    var ok = D.nodes.filter(function (n) { return n.estado === 'ok'; }).length;
    var h = '<div class="st-grid dc-summary">' + LEVEL_ORDER.map(function (lv) {
      return '<div class="st-card"><small>' + LEVEL[lv].label + 's</small><b>' + count(lv) + ' / ' + (cupos[lv] || '?') + '</b><span>' + acts.map(function (a) { return a.n + ': ' + D.nodes.filter(function (n) { return n.nivel === lv && n.acto === a.n; }).length; }).join(' · ') + '</span></div>';
    }).join('') + '<div class="st-card"><small>Estado</small><b>' + ok + ' / ' + D.nodes.length + '</b><span>✅ acordadas · 🟡 ' + (D.nodes.length - ok) + ' propuestas</span></div></div>';
    h += '<h2 class="section-title">Las ocho cintas</h2><div class="dc-tapes">' + acts.map(function (a) {
      var t = D.cintas.filter(function (x) { return x.acto === a.n; });
      return '<div class="dc-tape" style="--c:' + esc(a.color) + '"><span class="st-n">Acto ' + esc(a.n) + '</span><b>' + (t.length ? t.map(function (x) { return x.n; }).join(', ') : '—') + '</b><small>' + t.length + ' cinta(s)</small></div>';
    }).join('') + '</div><p class="stat-sub">Se recogen a lo largo de la historia y solo se oyen en el Acto IV.</p>';
    return h;
  }
  function filterChips(action, cur, items) {
    return items.map(function (it) { return '<button class="chip" type="button" data-action="' + action + '" data-value="' + esc(it[0]) + '" aria-pressed="' + (cur === it[0]) + '">' + esc(it[1]) + '</button>'; }).join('');
  }
  function decisionFilters(D, acts, who) {
    var q = state.dc;
    return '<div class="filters"><div class="filter-group"><span class="filter-label">Acto</span>' + filterChips('dc-act', q.act, [['all', 'Todos']].concat(acts.map(function (a) { return [a.n, a.n]; }))) + '</div>' +
      '<div class="filter-group"><span class="filter-label">Nivel</span>' + filterChips('dc-level', q.level, [['all', 'Todos']].concat(LEVEL_ORDER.map(function (lv) { return [lv, LEVEL[lv].label]; }))) + '</div>' +
      '<div class="filter-group"><label class="filter-label" for="dcWho">Personaje</label><select id="dcWho" data-action="dc-who"><option value="all">Todos</option>' + who.map(function (w) { return '<option value="' + esc(w) + '"' + (q.who === w ? ' selected' : '') + '>' + esc(w) + '</option>'; }).join('') + '</select></div></div>';
  }
  function decisionFlagTable(D, flags) {
    var title = {};
    D.nodes.forEach(function (n) { title[n.id] = n.titulo; });
    var link = function (id) { return '<a href="#/decisiones?h=' + esc(id) + '" title="' + esc(title[id]) + '">' + esc(title[id]) + '</a>'; };
    var h = '<h2 class="section-title">Banderas y quién las usa</h2><p class="page-lead">Cada bandera se fija en una decisión y se lee en otras, siempre de un acto igual o posterior. La flecha va de quien la fija a quien la lee.</p><div class="table-wrap"><table><thead><tr><th>Bandera</th><th>Qué guarda</th><th>Personajes</th><th>Fija → Lee</th></tr></thead><tbody>';
    D.flags.forEach(function (f) {
      var sets = D.nodes.filter(function (n) { return nodeFlags(n).indexOf(f.id) >= 0; });
      var reads = D.nodes.filter(function (n) { return n.lee.indexOf(f.id) >= 0; });
      h += '<tr><td>' + flagChip(f.id, flags) + '</td><td>' + esc(f.descripcion) + '</td><td>' + esc(f.personajes.join(', ')) + '</td><td>' + sets.map(function (n) { return link(n.id); }).join(', ') + ' → ' + (reads.length ? reads.map(function (n) { return link(n.id); }).join(', ') : '—') + '</td></tr>';
    });
    return h + '</tbody></table></div>';
  }
  function decisionProofs(D) {
    return '<h2 class="section-title">Pruebas de Reme en el Acto IV</h2><div class="table-wrap"><table><thead><tr><th>Variante</th><th>Prueba</th></tr></thead><tbody>' + D.pruebas_iv.map(function (p) {
      return '<tr><td><b>' + esc(p.variante) + '</b></td><td>' + esc(p.prueba) + '</td></tr>';
    }).join('') + '</tbody></table></div>';
  }
  function viewDecisions() {
    var D = H.decisions;
    var acts = (H.story && H.story.acts) || [];
    var h = '<p class="eyebrow">Diseño del juego</p><h1 class="page-title">Árbol de decisiones</h1><p class="page-lead">Las decisiones de los cuatro actos: quién las dispara, qué opciones hay y qué cambian en el mundo, el mercado y los personajes. Los cuellos reúnen las ramas de un acto en una misma escena. Documento: <a href="#/docs/23-arbol-de-decisiones">23 · Árbol de decisiones</a>. Contiene spoilers.</p>';
    if (!D || !D.nodes.length) return h + '<div class="empty">Sin datos: falta studio/data/decisions.json.</div>';
    var flags = {};
    D.flags.forEach(function (f) { flags[f.id] = f; });
    var who = [];
    D.nodes.forEach(function (n) { nodeWhos(n, flags).forEach(function (w) { if (who.indexOf(w) < 0) who.push(w); }); });
    who.sort(function (a, b) { return a.localeCompare(b, 'es'); });
    var q = state.dc;
    var visible = {};
    D.nodes.forEach(function (n) {
      visible[n.id] = (q.act === 'all' || n.acto === q.act) && (q.level === 'all' || n.nivel === q.level) && (q.who === 'all' || nodeWhos(n, flags).indexOf(q.who) >= 0);
    });
    h += decisionSummary(D, acts) + '<h2 class="section-title">Decisiones por acto</h2>' + decisionFilters(D, acts, who);
    h += '<div class="dc-board" style="--n:' + acts.length + '">' + acts.map(function (a) { return decisionColumn(a, D, flags, visible); }).join('') + '</div>';
    return h + decisionFlagTable(D, flags) + decisionProofs(D);
  }

  /* ---------- hilos narrativos ---------- */
  var THREAD_TYPES = { pista: 'Pista', promesa: 'Promesa', secreto: 'Secreto', conflicto: 'Conflicto' };
  var THREAD_STATES = { resuelto: 'Resuelto', abierto: 'Abierto', aplazado: 'Aplazado' };
  var THREAD_ACTS = ['I', 'II', 'III', 'IV', 'despues'];
  var THREAD_NODE = /\bn-[a-z0-9]+(?:-[a-z0-9]+)*/g;
  function threadActLabel(a) { return a === 'despues' ? 'Después' : 'Acto ' + a; }
  /* Acto donde se dibuja el hilo: el de su primera siembra. */
  function threadHome(t) {
    var ranks = (t.siembra || []).map(function (e) { return THREAD_ACTS.indexOf(e.acto); }).filter(function (i) { return i >= 0; });
    return ranks.length ? THREAD_ACTS[Math.min.apply(null, ranks)] : null;
  }
  function threadColumns() {
    var cols = ((H.story && H.story.acts) || []).map(function (a) { return { n: a.n, title: a.title, color: a.color }; });
    return cols.concat([{ n: 'despues', title: 'Sandbox y segunda parte', color: '#5b7c8c' }]);
  }
  /* Una referencia libre («doc 19 §3 · nodo n-ii-x · cinta 3») en chips; los ids de nodo enlazan al árbol de decisiones. */
  function threadRefChips(ref) {
    return String(ref || '').split('·').map(function (x) { return x.trim(); }).filter(Boolean).map(function (x) {
      var node = x.match(THREAD_NODE);
      return node ? '<a class="chip hl-ref" href="#/decisiones?h=' + esc(node[0]) + '">' + esc(x) + '</a>' : '<span class="chip hl-ref">' + esc(x) + '</span>';
    }).join(' ');
  }
  function threadEntries(label, entries) {
    if (!entries.length) return '';
    return '<div class="hl-entries"><small>' + label + '</small><ul>' + entries.map(function (e) {
      return '<li>' + decisionMark(e.estado) + ' <b>' + esc(e.acto === 'despues' ? 'Después' : e.acto) + '</b> ' + esc(e.donde) + (e.ref ? '<div class="hl-refs">' + threadRefChips(e.ref) + '</div>' : '') + '</li>';
    }).join('') + '</ul></div>';
  }
  function threadCard(t) {
    var sow = t.siembra || [], solve = t.resuelve || [];
    var allOk = sow.concat(solve).every(function (e) { return e.estado === 'ok'; });
    var arrow = solve.length ? '<span class="hl-arrow" title="Se resuelve en"><span aria-hidden="true">→</span> ' + solve.map(function (e) { return esc(e.acto === 'despues' ? 'Después' : e.acto); }).join(', ') + '</span>' : '<span class="hl-arrow hl-open">sin resolver</span>';
    var h = '<article class="dc-card hl-card hl-' + esc(t.estado) + '" id="' + esc(t.id) + '"><header><span class="dc-level">' + esc(THREAD_TYPES[t.tipo] || t.tipo) + '</span>' + decisionMark(allOk ? 'ok' : 'prop') + '</header>';
    h += '<h3>' + esc(t.titulo) + '</h3><p class="hl-state"><span class="chip hl-st-' + esc(t.estado) + '">' + esc(THREAD_STATES[t.estado] || t.estado) + '</span> ' + arrow + '</p>';
    if (t.personajes && t.personajes.length) h += '<p class="hl-who"><small>Personajes</small> ' + t.personajes.map(esc).join(', ') + '</p>';
    h += threadEntries('Se siembra', sow) + threadEntries('Se resuelve', solve);
    if (t.cambia) h += '<p class="hl-change"><small>Cambia</small> ' + esc(t.cambia) + '</p>';
    if (t.motivo) h += '<p class="hl-reason"><small>Motivo</small> ' + esc(t.motivo) + '</p>';
    return h + '</article>';
  }
  function threadColumn(col, list, total) {
    var h = '<section class="dc-col" style="--c:' + esc(col.color) + '"><div class="dc-col-head"><span class="st-n">' + esc(threadActLabel(col.n)) + '</span><h2>' + esc(col.title) + '</h2><small>' + list.length + ' de ' + total + ' hilos</small></div>';
    h += list.map(threadCard).join('');
    if (!list.length) h += '<div class="empty">Ningún hilo con este filtro.</div>';
    return h + '</section>';
  }
  function threadFilters(who) {
    var q = state.hl;
    var all = [['all', 'Todos']];
    return '<div class="filters"><div class="filter-group"><span class="filter-label">Acto</span>' + filterChips('hl-act', q.act, all.concat(THREAD_ACTS.map(function (a) { return [a, a === 'despues' ? 'Después' : a]; }))) + '</div>' +
      '<div class="filter-group"><span class="filter-label">Tipo</span>' + filterChips('hl-tipo', q.tipo, all.concat(Object.keys(THREAD_TYPES).map(function (k) { return [k, THREAD_TYPES[k]]; }))) + '</div>' +
      '<div class="filter-group"><span class="filter-label">Estado</span>' + filterChips('hl-estado', q.estado, all.concat(Object.keys(THREAD_STATES).map(function (k) { return [k, THREAD_STATES[k]]; }))) + '</div>' +
      '<div class="filter-group"><label class="filter-label" for="hlWho">Personaje</label><select id="hlWho" data-action="hl-who"><option value="all">Todos</option>' + who.map(function (w) { return '<option value="' + esc(w) + '"' + (q.who === w ? ' selected' : '') + '>' + esc(w) + '</option>'; }).join('') + '</select></div></div>';
  }
  function threadSummary(R) {
    var by = function (map, k) { return (map && map[k]) || 0; };
    var h = '<div class="st-grid dc-summary">' +
      '<div class="st-card"><small>Hilos</small><b>' + R.total + '</b><span>' + Object.keys(THREAD_TYPES).map(function (k) { return THREAD_TYPES[k].toLowerCase() + 's ' + by(R.por_tipo, k); }).join(' · ') + '</span></div>' +
      '<div class="st-card"><small>Estado</small><b>' + by(R.por_estado, 'resuelto') + ' / ' + R.total + '</b><span>resueltos · ' + by(R.por_estado, 'abierto') + ' abiertos · ' + by(R.por_estado, 'aplazado') + ' aplazados</span></div>' +
      '<div class="st-card"><small>Sembrados sin resolver</small><b>' + R.sin_resolver.length + '</b><span>sin resolución y sin motivo</span></div>' +
      '<div class="st-card"><small>Resueltos sin sembrar</small><b>' + R.sin_sembrar.length + '</b><span>o resueltos antes de sembrarse</span></div>' +
      '<div class="st-card"><small>Personajes que faltan</small><b>' + R.faltan.length + '</b><span>en el mapa de historia entre siembra y resolución</span></div></div>';
    var review = R.sin_resolver.concat(R.sin_sembrar, R.faltan.map(function (f) { return f.texto; }));
    h += '<h2 class="section-title">Para revisar</h2>';
    if (!review.length) return h + '<p class="stat-sub">Nada pendiente: todo hilo sembrado se resuelve o dice por qué sigue abierto.</p>';
    return h + '<ul class="hl-review">' + review.map(function (msg) {
      var id = msg.split(' ')[0].replace(/:$/, '');
      return '<li><a href="#/hilos?h=' + esc(id) + '">' + esc(id) + '</a> ' + esc(msg.slice(msg.indexOf(' ') + 1)) + '</li>';
    }).join('') + '</ul>';
  }
  function viewThreads() {
    var T = H.hilos;
    var h = '<p class="eyebrow">Diseño del juego</p><h1 class="page-title">Hilos narrativos</h1><p class="page-lead">Cada pista, promesa o secreto con dónde se siembra, dónde se resuelve y qué cambia. El hilo se dibuja en el acto donde se siembra y la marca → dice dónde se resuelve. Los avisos de abajo salen de las comprobaciones del build. Contiene spoilers.</p>';
    if (!T || !T.hilos.length) return h + '<div class="empty">Sin hilos cargados.</div>';
    var who = [];
    T.hilos.forEach(function (t) { (t.personajes || []).forEach(function (w) { if (who.indexOf(w) < 0) who.push(w); }); });
    who.sort(function (a, b) { return a.localeCompare(b, 'es'); });
    var q = state.hl;
    var cols = threadColumns();
    h += threadSummary(T.resumen) + '<h2 class="section-title">Hilos por acto</h2>' + threadFilters(who);
    h += '<div class="dc-board" style="--n:' + cols.length + '">' + cols.map(function (col) {
      var mine = T.hilos.filter(function (t) { return threadHome(t) === col.n; });
      var shown = mine.filter(function (t) {
        return (q.act === 'all' || col.n === q.act) && (q.tipo === 'all' || t.tipo === q.tipo) && (q.estado === 'all' || t.estado === q.estado) && (q.who === 'all' || (t.personajes || []).indexOf(q.who) >= 0);
      });
      return threadColumn(col, shown, mine.length);
    }).join('') + '</div>';
    return h;
  }

  /* ---------- QA ---------- */
  var RESULT_LABEL = { 'not-run': 'Sin ejecutar', pass: 'Aprobado', fail: 'Fallido', blocked: 'Bloqueado', skipped: 'Omitido' };
  var SEVERITY_LABEL = { S1: 'Crítico', S2: 'Grave', S3: 'Moderado', S4: 'Menor' };
  function resultPill(st) { return '<span class="pill r-' + st + '">' + esc(RESULT_LABEL[st] || st) + '</span>'; }

  function viewQA() {
    var qa = H.qa || { areas: [], types: [], cases: [], bugs: [] };
    var cases = qa.cases;
    var q = state.qa;
    var count = function (f) { return cases.filter(f).length; };
    var ran = count(function (c) { return c.result.status !== 'not-run'; });
    var openBugs = qa.bugs.filter(function (b) { return ['cerrado', 'no-se-corrige', 'verificado'].indexOf(b.status) < 0; });
    var inQa = TASKS.filter(function (t) { return t.status === 'qa'; });
    var inReview = TASKS.filter(function (t) { return t.status === 'review'; });

    var h = '<p class="eyebrow">Calidad</p><h1 class="page-title">QA</h1><p class="page-lead">El QA es una etapa del flujo, entre la revisión y el cierre. Aquí se ven los casos de prueba, sus resultados y los errores. Procedimiento completo en <a href="#/docs/16-calidad-y-qa">Calidad y QA</a>.</p>';
    h += '<div class="flow">' + ['backlog', 'sprint', 'doing', 'review', 'qa', 'done'].map(function (s) {
      var n = TASKS.filter(function (t) { return t.status === s; }).length;
      return '<span class="flow-step s-' + s + (s === 'qa' ? ' flow-qa' : '') + '"><b>' + STATUS[s].label + '</b><small>' + n + '</small></span>';
    }).join('<span class="flow-arrow">→</span>') + '</div>';

    h += '<div class="grid grid-3" style="margin:16px 0 8px">' +
      '<div class="card"><div class="stat-label">Casos de prueba</div><div class="stat-value">' + cases.length + '</div><div class="stat-sub">' + count(function (c) { return c.auto; }) + ' automáticos · ' + count(function (c) { return !c.auto; }) + ' manuales</div></div>' +
      '<div class="card"><div class="stat-label">Ejecutados</div><div class="stat-value">' + ran + ' / ' + cases.length + '</div><div class="stat-sub">' + count(function (c) { return c.result.status === 'pass'; }) + ' aprobados · ' + count(function (c) { return c.result.status === 'fail'; }) + ' fallidos · ' + count(function (c) { return c.result.status === 'blocked'; }) + ' bloqueados</div></div>' +
      '<div class="card"><div class="stat-label">Errores abiertos</div><div class="stat-value">' + openBugs.length + '</div><div class="stat-sub">' + ['S1', 'S2', 'S3', 'S4'].map(function (s) { return s + ': ' + openBugs.filter(function (b) { return b.severity === s; }).length; }).join(' · ') + '</div></div></div>';
    if (!ran) h += '<p class="stat-sub">Todavía no se ha ejecutado ningún caso: el prototipo aún no existe. Los casos se derivan del diseño y se ejecutan desde la Fase 2.</p>';

    h += '<h2 class="section-title">Tareas en revisión y en QA <small>' + inReview.length + ' en revisión · ' + inQa.length + ' en QA</small></h2><div class="card">';
    var pending = inQa.concat(inReview);
    if (!pending.length) h += '<div class="empty">Ninguna tarea espera revisión ni QA.</div>';
    pending.slice(0, 12).forEach(function (t) {
      h += '<div class="phase-row" style="grid-template-columns:62px 1fr auto auto"><span class="tid">' + esc(t.id) + '</span><span>' + taskLink(t) + '</span>' + prioPill(t.prio) + statusPill(t.status) + '</div>';
    });
    if (pending.length > 12) h += '<div class="empty">Y ' + (pending.length - 12) + ' más en el <a href="#/tablero">tablero</a>.</div>';
    h += '</div>';

    h += '<h2 class="section-title">Cobertura por área</h2><div class="table-wrap"><table><thead><tr><th>Área</th><th class="num-cell">Casos</th><th class="num-cell">Automáticos</th><th class="num-cell">Ejecutados</th><th class="num-cell">Aprobados</th><th class="num-cell">Fallidos</th></tr></thead><tbody>';
    qa.areas.forEach(function (a) {
      var l = cases.filter(function (c) { return c.area === a; });
      if (!l.length) return;
      h += '<tr><td>' + esc(a) + '</td><td class="num-cell">' + l.length + '</td><td class="num-cell">' + l.filter(function (c) { return c.auto; }).length + '</td><td class="num-cell">' + l.filter(function (c) { return c.result.status !== 'not-run'; }).length + '</td><td class="num-cell">' + l.filter(function (c) { return c.result.status === 'pass'; }).length + '</td><td class="num-cell">' + l.filter(function (c) { return c.result.status === 'fail'; }).length + '</td></tr>';
    });
    h += '</tbody></table></div>';

    var areas = ['Todas'].concat(qa.areas.filter(function (a) { return cases.some(function (c) { return c.area === a; }); }));
    var types = ['Todos'].concat(qa.types);
    var list = cases.filter(function (c) { return (q.area === 'Todas' || c.area === q.area) && (q.type === 'Todos' || c.type === q.type); });
    h += '<h2 class="section-title">Casos de prueba <small>' + list.length + ' de ' + cases.length + '</small></h2>';
    h += '<div class="filters"><div class="filter-group"><span class="filter-label">Área</span>' + areas.map(function (a) { return '<button class="chip" type="button" data-action="qa-area" data-value="' + esc(a) + '" aria-pressed="' + (q.area === a) + '">' + esc(a) + '</button>'; }).join('') + '</div>' +
      '<div class="filter-group"><span class="filter-label">Tipo</span>' + types.map(function (a) { return '<button class="chip" type="button" data-action="qa-type" data-value="' + esc(a) + '" aria-pressed="' + (q.type === a) + '">' + esc(a) + '</button>'; }).join('') + '</div></div>';
    h += '<div class="table-wrap"><table><thead><tr><th>ID</th><th>Caso</th><th>Tipo</th><th>Nivel</th><th>Prio</th><th>Tareas</th><th>Resultado</th></tr></thead><tbody>';
    list.forEach(function (c) {
      var links = c.tasks.map(function (id) { var t = taskById(id); return t ? '<a href="#/tarea/' + esc(id) + '">' + esc(id) + '</a>' : esc(id); }).join(', ');
      h += '<tr><td class="tid">' + esc(c.id) + '</td><td><details class="case"><summary>' + esc(c.title) + '</summary><ol>' + c.steps.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol><p><strong>Esperado:</strong> ' + esc(c.expected) + '</p></details></td><td>' + esc(c.type) + '</td><td>' + esc(c.level) + (c.auto ? ' · auto' : ' · manual') + '</td><td>' + prioPill(c.prio) + '</td><td>' + links + '</td><td>' + resultPill(c.result.status) + '</td></tr>';
    });
    h += '</tbody></table></div>';

    h += '<h2 class="section-title">Errores <small>' + qa.bugs.length + ' registrados</small></h2>';
    if (!qa.bugs.length) h += '<div class="notice">No hay errores registrados. Cuando aparezca uno se guarda como <code>data/qa/bugs/BUG-NNNN.json</code> con su severidad: S1 crítico, S2 grave, S3 moderado, S4 menor.</div>';
    else {
      h += '<div class="table-wrap"><table><thead><tr><th>ID</th><th>Error</th><th>Severidad</th><th>Estado</th><th>Tarea</th></tr></thead><tbody>';
      qa.bugs.forEach(function (b) {
        h += '<tr><td class="tid">' + esc(b.id) + '</td><td>' + esc(b.title) + '</td><td><span class="pill sev-' + esc(b.severity) + '">' + esc(b.severity) + ' · ' + esc(SEVERITY_LABEL[b.severity] || '') + '</span></td><td>' + esc(b.status) + '</td><td>' + (b.task ? '<a href="#/tarea/' + esc(b.task) + '">' + esc(b.task) + '</a>' : '—') + '</td></tr>';
      });
      h += '</tbody></table></div>';
    }
    h += '<h2 class="section-title">Criterios de salida de una versión</h2><div class="card"><ul class="prose" style="margin:0"><li>0 errores S1 y S2 abiertos.</li><li>Casos de prioridad P0 aprobados (automáticos y manuales).</li><li>Matriz de dispositivos recorrida y lista de seguridad completa.</li><li>Presupuestos de rendimiento cumplidos.</li><li>Informe de QA de la versión redactado.</li></ul></div>';
    return h;
  }

  /* ---------- tarea ---------- */
  function evidenceItem(e) {
    var cap = '<div class="ev-cap"><strong>' + esc(e.title || e.type) + '</strong>' + (e.note ? '<span>' + esc(e.note) + '</span>' : '') + '<small>' + esc(e.at || '') + ' · ' + esc(e.type) + '</small></div>';
    if (e.type === 'image') {
      return '<figure class="ev">' + (e.exists === false ? '<div class="empty">Falta el archivo ' + esc(e.path) + '</div>' : '<a href="../' + esc(e.path) + '" target="_blank" rel="noopener"><img loading="lazy" src="../' + esc(e.path) + '" alt="' + esc(e.title || '') + '"></a>') + cap + '</figure>';
    }
    if (e.type === 'link') return '<div class="ev ev-text"><a href="' + esc(safeUrl(e.url)) + '" target="_blank" rel="noopener noreferrer">' + esc(e.url) + '</a>' + cap + '</div>';
    if (e.type === 'file') return '<div class="ev ev-text"><a href="../' + esc(e.path) + '" target="_blank" rel="noopener">' + esc(e.path) + '</a>' + cap + '</div>';
    if (e.type === 'doc') return '<div class="ev ev-text"><a href="#/docs/' + esc(e.doc) + '">Documento ' + esc(e.doc) + '</a>' + cap + '</div>';
    return '<div class="ev ev-text">' + (e.text ? '<p>' + esc(e.text) + '</p>' : '') + cap + '</div>';
  }
  function viewTask(id) {
    var t = taskById(id);
    if (!t) return '<div class="notice">No existe la tarea «' + esc(id) + '». <a href="#/roadmap">Volver al roadmap</a>.</div>';
    var h = '<p class="eyebrow"><a href="#/roadmap" data-phase="' + esc(t.phase.id) + '">' + esc(t.phase.id + ' · ' + t.phase.name) + '</a> › ' + esc(t.ms.id + ' · ' + t.ms.name) + '</p>';
    h += '<h1 class="page-title">' + esc(t.title) + '</h1>';
    h += '<div class="doc-meta"><span class="chip">' + esc(t.id) + '</span>' + statusPill(t.status) + prioPill(t.prio) + targetPill(t.target) + '<span class="chip">' + num(t.est) + ' h estimadas</span></div>';
    h += '<div class="task-layout"><div>';
    h += '<div class="card"><dl class="task-dl"><dt>Prioridad</dt><dd>' + esc(t.prio + ' · ' + (PRIO_LABEL[t.prio] || '')) + '</dd><dt>Descripción</dt><dd>' + (t.desc ? esc(t.desc) : 'Se detalla antes de entrar a la fase.') + '</dd><dt>Listo cuando</dt><dd>' + (t.done_when ? esc(t.done_when) : 'Se define antes de entrar a la fase.') + '</dd></dl></div>';
    h += '<h2 class="section-title">Evidencias <small>' + t.evidence.length + '</small></h2>';
    h += t.evidence.length ? '<div class="ev-grid">' + t.evidence.map(evidenceItem).join('') + '</div>' : '<div class="empty">Sin evidencias todavía.</div>';
    h += '<h2 class="section-title">Comentarios <small>' + t.comments.length + '</small></h2>';
    if (!t.comments.length) h += '<div class="empty">Sin comentarios.</div>';
    t.comments.forEach(function (c) {
      h += '<div class="comment by-' + esc(c.by) + '"><div class="comment-head"><strong>' + esc(AUTHOR[c.by] || c.by) + '</strong><span class="tid">' + esc(c.at) + '</span></div><p>' + esc(c.text) + '</p></div>';
    });
    h += '<p class="stat-sub" style="margin-top:14px">Para comentar o mover esta tarea, díselo a Claude: los cambios se guardan editando los archivos de datos, no desde esta página.</p>';
    h += '</div><aside><h2 class="section-title" style="margin-top:0">Historial <small>' + t.history.length + '</small></h2>';
    if (!t.history.length) h += '<div class="empty">Sin movimientos: sigue en Backlog.</div>';
    else {
      h += '<ol class="timeline">';
      t.history.forEach(function (x) {
        h += '<li><span class="tid">' + esc(x.at) + '</span><div>' + statusPill(x.to) + '</div><div class="tl-from">desde ' + esc(STATUS[x.from].label) + (x.by ? ' · ' + esc(AUTHOR[x.by] || x.by) : '') + '</div><p>' + esc(x.note) + '</p>' + (x.ref ? '<p class="tl-ref"><code>' + esc(x.ref) + '</code></p>' : '') + '</li>';
      });
      h += '</ol>';
    }
    h += '</aside></div>';
    return h;
  }

  /* ---------- documentos, arte, sonido, paleta ---------- */
  function viewDoc(id) {
    var d = H.docs.filter(function (x) { return x.id === id; })[0];
    if (!d) return '<div class="notice">No existe el documento «' + esc(id) + '».</div>';
    var r = mdToHtml(d.md);
    var h = '<div class="doc-layout"><article class="prose">';
    h += '<div class="doc-meta"><span class="chip">' + esc(d.group) + '</span>' + cleanChip(d) + '<span class="chip" title="Acordado">✅ ' + d.counts.ok + '</span><span class="chip" title="Propuesta">🟡 ' + d.counts.prop + '</span><span class="chip" title="Abierto">❓ ' + d.counts.open + '</span><a class="chip" href="../docs/' + (d.id.indexOf('adr-') === 0 ? 'adr/' + esc(d.id.slice(4)) : esc(d.id)) + '.md" target="_blank" rel="noopener">Abrir archivo .md</a></div>';
    h += r.html + '</article>';
    h += '<nav class="toc" aria-label="En este documento"><div class="toc-title">En este documento</div>' +
      r.toc.map(function (t) { return '<a class="l' + t.level + '" href="#/docs/' + d.id + '?h=' + t.id + '">' + esc(t.text) + '</a>'; }).join('') + '</nav></div>';
    return h;
  }

  /* ---------- galería de personajes y NPC ---------- */
  function viewGallery() {
    var G = H.gallery;
    var byFile = {};
    H.assets.images.forEach(function (i) { byFile[i.file] = i; });
    var list = [];
    function shot(file, label, cls) {
      var a = byFile[file];
      if (!a) return '';
      list.push(a);
      return '<button class="gx-shot ' + (cls || '') + '" type="button" data-action="open-img" data-index="' + (list.length - 1) + '"><img loading="lazy" src="../' + esc(file) + '" alt="' + esc(a.title) + '"><span>' + esc(label) + '</span></button>';
    }
    var TIPO = { modelo: 'Modelo', poses: 'Poses', expresiones: 'Expresiones' };
    var nSheets = G.people.reduce(function (n, p) { return n + p.sheets.length; }, 0) + G.sections.reduce(function (n, s) { return n + s.sheets.length; }, 0);
    var h = '<p class="eyebrow">Recursos</p><h1 class="page-title">Personajes y NPC</h1><p class="page-lead">Todas las hojas de personajes y NPC en un solo sitio: ' + G.people.length + ' personajes con hoja de modelo, de poses y de expresiones, y ' + G.sections.reduce(function (n, s) { return n + s.sheets.length; }, 0) + ' hojas de NPC, enemigos y criaturas (' + nSheets + ' en total). Toca una imagen para verla grande y pasa a la siguiente con las flechas. Estilo: <a href="#/docs/12-direccion-de-arte">12 · Dirección de arte</a>.</p>';
    h += '<nav class="gx-index" aria-label="Secciones de la galería"><a class="chip" href="#/personajes?h=gx-personajes">Personajes</a>' + G.sections.map(function (s) { return '<a class="chip" href="#/personajes?h=gx-' + esc(s.id) + '">' + esc(s.title) + '</a>'; }).join('') + '</nav>';
    h += '<h2 class="section-title" id="gx-personajes">Personajes <small>' + G.people.length + '</small></h2><div class="gx-people">';
    G.people.forEach(function (p) {
      h += '<article class="gx-card"><header class="gx-head"><h3>' + esc(p.name) + '</h3><div class="gx-tags">' + (p.faction ? '<span class="chip">' + esc(p.faction) + '</span>' : '') + '<span class="chip">Acto ' + esc(p.act) + '</span></div></header><div class="gx-sheets">' + p.sheets.map(function (sh) { return shot(sh.file, TIPO[sh.tipo]); }).join('') + '</div></article>';
    });
    h += '</div>';
    G.sections.forEach(function (sec) {
      h += '<h2 class="section-title" id="gx-' + esc(sec.id) + '">' + esc(sec.title) + ' <small>' + sec.sheets.length + ' hojas</small></h2><p class="gx-lead">' + esc(sec.lead) + '</p><div class="gx-npcs">';
      sec.sheets.forEach(function (sh) {
        var label = sh.npcs.map(function (n) { return n.name; }).join(' · ');
        var facs = [];
        sh.npcs.forEach(function (n) { if (n.faction && facs.indexOf(n.faction) < 0) facs.push(n.faction); });
        h += '<article class="gx-card">' + shot(sh.file, label, 'gx-wide') + '<div class="gx-tags">' + facs.map(function (f) { return '<span class="chip">' + esc(f) + '</span>'; }).join('') + '</div></article>';
      });
      h += '</div>';
    });
    lb.list = list;
    return h;
  }

  /* ---------- storyboard del Acto I (F0-24) ---------- */
  function viewStoryboard() {
    var S = H.storyboard;
    var h = '<p class="eyebrow">Diseño del juego</p><h1 class="page-title">Storyboard del Acto I</h1>';
    if (!S) return h + '<div class="notice">Falta <code>studio/data/storyboard.json</code>.</div>';
    var byFile = {};
    H.assets.images.forEach(function (i) { byFile[i.file] = i; });
    var list = [];
    function shot(file, label) {
      var a = byFile[file];
      if (!a) return '<div class="notice">Falta la imagen ' + esc(file) + '</div>';
      list.push(a);
      return '<button class="sb-shot" type="button" data-action="open-img" data-index="' + (list.length - 1) + '" aria-label="Ampliar: ' + esc(label || a.title) + '"><img loading="lazy" src="../' + esc(file) + '" alt="' + esc(a.title) + '"><span class="sb-stamp">ARTE PROVISIONAL</span></button>';
    }
    function wireframe(p) {
      var w = p.wireframe, b = w.barra;
      var bar = '<div class="wf-bar"><span>Día ' + esc(b.dia) + '</span><span>' + esc(b.estacion) + '</span><span>clima</span><span>' + esc(b.bloque) + '</span><span>' + (b.esquirlas != null ? esc(b.esquirlas) + ' esq.' : '— esq.') + '</span><span class="wf-btn">Esperar</span><span class="wf-btn">Libreta</span></div>';
      var figs = p.personajes.map(function (n) { return '<i class="wf-fig" title="' + esc(n) + '"><b>' + esc(n.charAt(0)) + '</b></i>'; }).join('');
      var stage = '<div class="wf-stage ' + esc(p.vista) + '"><em>' + (p.vista === 'interior' ? 'Interior · corte lateral' : 'Exterior · vista aérea') + '</em><div class="wf-figs">' + figs + '</div></div>';
      var lines = p.dialogo.slice(0, 2).map(function (d) { return '<p><b>' + esc(d.quien) + ':</b> ' + esc(d.texto) + '</p>'; }).join('');
      var box = '<div class="wf-box">' + lines + '</div>';
      var btns = '<div class="wf-btns">' + w.botones.map(function (t) { return '<span class="wf-btn">' + esc(t) + '</span>'; }).join('') + '</div>';
      return '<div class="wf" role="img" aria-label="Esquema de la pantalla del juego: barra superior, escena, caja de diálogo y botones">' + bar + stage + box + btns + '</div>';
    }
    function panel(p) {
      var h = '<article class="sb-panel"><div class="sb-media">' + shot(p.imagen, p.titulo) + '</div><div class="sb-info">';
      h += '<div class="gx-tags"><span class="chip">Día ' + esc(p.dia) + ' · ' + esc(p.bloque) + '</span><span class="chip">' + (p.vista === 'interior' ? 'Interior lateral' : 'Exterior aéreo') + '</span></div>';
      h += '<p class="sb-desc">' + esc(p.descripcion) + '</p>';
      h += '<dl class="sb-facts"><dt>Lugar</dt><dd>' + esc(p.lugar) + '</dd><dt>Personajes</dt><dd>' + p.personajes.map(esc).join(', ') + '</dd><dt>Props</dt><dd>' + p.props.map(esc).join(' · ') + '</dd></dl>';
      h += p.dialogo.map(function (d) { return '<blockquote class="sb-line"><b>' + esc(d.quien) + '</b> «' + esc(d.texto) + '»</blockquote>'; }).join('');
      if (p.defecto) h += '<div class="notice">' + esc(p.defecto) + '</div>';
      return h + '</div><div class="sb-wf">' + wireframe(p) + '</div></article>';
    }
    h += '<p class="page-lead">' + esc(S.nota) + ' Fuente: <a href="#/docs/27-guion-del-acto-i">27 · Guion del Acto I</a> y <a href="#/docs/30-flujo-de-pantallas">30 · Flujo de pantallas</a>. Los esquemas de pantalla son estructura, no diseño final de interfaz. Para el paso a paso de los siete días, mira <a href="#/semana1">Semana 1 · camino feliz</a>.</p>';
    h += '<nav class="gx-index" aria-label="Escenas del storyboard"><a class="chip" href="#/storyboard?h=sb-mapa">Mapa</a>' + S.escenas.map(function (e) { return '<a class="chip" href="#/storyboard?h=sb-' + esc(e.id) + '">' + esc(e.id) + ' · ' + esc(e.titulo) + '</a>'; }).join('') + '<a class="chip" href="#/storyboard?h=sb-props">Props</a></nav>';
    var M = S.mapa;
    h += '<h2 class="section-title" id="sb-mapa">Mapa de Valdoria con niebla <small>pestaña de la libreta · seis regiones</small></h2><p class="gx-lead">' + esc(M.nota) + '</p>';
    h += '<div class="sb-map">' + shot(M.imagen, 'Mapa de Valdoria con niebla') + '<div class="table-wrap"><table><thead><tr><th>Región</th><th>Posición</th><th>Estado</th><th>Qué se ve</th></tr></thead><tbody>' +
      M.regiones.map(function (r) { return '<tr><td>' + esc(r.nombre) + '</td><td>' + esc(r.posicion) + '</td><td><span class="pill ' + (r.estado === 'abierta' ? 'st-aprobada' : 'st-superada') + '">' + esc(r.estado) + '</span></td><td>' + esc(r.se_ve) + '</td></tr>'; }).join('') +
      '</tbody></table>' + M.reglas.map(function (x) { return '<p class="gx-lead">' + esc(x) + '</p>'; }).join('') + '</div></div>';
    S.escenas.forEach(function (e) {
      var ps = S.paneles.filter(function (p) { return p.escena === e.id; });
      h += '<h2 class="section-title" id="sb-' + esc(e.id) + '"><code>' + esc(e.id) + '</code> ' + esc(e.titulo) + (e.variantes ? ' <small>3 variantes</small>' : '') + '</h2>';
      if (e.variantes) {
        var cur = state.sb.v[e.id] || 'A';
        h += '<div class="filters" role="tablist" aria-label="Variante de ' + esc(e.id) + '"><div class="filter-group">' + S.variantes.map(function (v) {
          return '<button class="chip" type="button" role="tab" data-action="sb-var" data-scene="' + esc(e.id) + '" data-value="' + esc(v.id) + '" aria-pressed="' + (cur === v.id) + '" aria-selected="' + (cur === v.id) + '">Variante ' + esc(v.id) + ' · ' + esc(v.nombre) + '</button>';
        }).join('') + '</div></div>';
        ps = ps.filter(function (p) { return p.variante === cur; });
      }
      ps.forEach(function (p) { h += panel(p); });
      if (e.id === 'd7.2') {
        var T = S.tabla_d72;
        h += '<h3 class="sb-sub">' + esc(T.titulo) + '</h3><p class="gx-lead">' + esc(T.fuente) + ' La imagen es la misma en las cuatro dificultades: cambia la cuenta, no el decorado.</p><div class="table-wrap"><table><thead><tr><th>Salida</th>' + T.dificultades.map(function (d) { return '<th>' + esc(d) + '</th>'; }).join('') + '</tr></thead><tbody>' +
          T.filas.map(function (f) { return '<tr><td>' + esc(f.salida) + '<br><small>f-pago-reme = ' + esc(f.flag) + '</small></td>' + f.celdas.map(function (c) { return '<td>' + esc(c) + '</td>'; }).join('') + '</tr>'; }).join('') +
          '</tbody></table></div><p class="gx-lead">' + esc(T.nota) + '</p>';
      }
    });
    h += '<h2 class="section-title" id="sb-props">Hoja de props <small>referencia provisional para F3-16</small></h2><div class="sb-map">' + shot(M.hoja_props, 'Hoja de props') + '</div>';
    lb.list = list;
    return h;
  }

  /* ---------- semana 1 · camino feliz (F0-24) ---------- */
  var S1_KEY = 'vf-semana1-obligatorios';
  var S1_REME = ['Consorcio', 'Ministerio', 'Faroleros'];
  var S1_DIFF = ['Novato', 'Intermedio', 'Difícil', 'Hardcore'];
  function s1Load() {
    try { return JSON.parse(localStorage.getItem(S1_KEY) || '{}') || {}; } catch (err) { return {}; }
  }
  function s1Save(map) {
    try { localStorage.setItem(S1_KEY, JSON.stringify(map)); } catch (err) { /* sin almacenamiento: el estado vive solo en la página */ }
  }
  function s1Days(v) {
    if (typeof v === 'number') return [v];
    var t = String(v), m = t.match(/(\d+)\s*a\s*(\d+)/), out = [], i;
    if (m) { for (i = +m[1]; i <= +m[2]; i++) out.push(i); return out; }
    if (/todos|todas/i.test(t)) return [1, 2, 3, 4, 5, 6, 7];
    m = t.match(/\d+/);
    return m ? [+m[0]] : [];
  }
  function s1Ul(items) { return '<ul class="s1-list">' + items.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>'; }
  function s1Sec(title, items, cls) {
    if (!items || !items.length) return '';
    return '<div class="s1-sec ' + (cls || '') + '"><h5>' + esc(title) + '</h5>' + s1Ul(items) + '</div>';
  }
  function s1Row(label, text) { return text ? '<div class="s1-sec"><h5>' + esc(label) + '</h5><p>' + esc(text) + '</p></div>' : ''; }

  function viewSemana1() {
    var W = H.semana1, st = state.s1;
    var h = '<p class="eyebrow">Diseño del juego</p><h1 class="page-title">Semana 1 · camino feliz</h1>';
    if (!W) return h + '<div class="notice">Falta <code>studio/data/semana1.json</code>.</div>';
    var happy = st.mode === 'feliz', checks = s1Load();
    var sbScenes = {};
    (H.storyboard ? H.storyboard.escenas : []).forEach(function (e) { sbScenes[e.id] = true; });
    var reme = W.variantes_globales[0], diff = W.variantes_globales[2];
    var IM = W.imagenes || {}, CAB = W.imagenes_cabecera || {}, byFile = {}, list = [], listIdx = {}, info = {};
    var REME_VAR = { Consorcio: 'A', Ministerio: 'B', Faroleros: 'C' };
    H.assets.images.forEach(function (i) { byFile[i.file] = i; });
    W.dias.forEach(function (d) { d.bloques.forEach(function (b) { b.escenas.forEach(function (sc) { info[sc] = { dia: d.dia, bloque: b.bloque, lugar: b.lugar }; }); }); });
    var allScenes = Object.keys(info);
    function varOf(sc) {
      var im = IM[sc];
      if (!im || !im.variantes) return null;
      return st.v[sc] || (!happy && REME_VAR[st.reme]) || 'A';
    }
    function fileOf(sc) {
      var im = IM[sc], v = varOf(sc);
      return !im ? null : (v ? im.variantes[v] : im.archivo);
    }
    function isDone(sc) { return !!(IM[sc] && IM[sc].estado === 'hecha' && fileOf(sc)); }
    function lbIndex(file) {
      if (!(file in listIdx)) { listIdx[file] = list.length; list.push(byFile[file]); }
      return listIdx[file];
    }
    function thumb(file, label, cls) {
      var a = byFile[file];
      if (!a) return '<div class="s1-pend ' + (cls || '') + '">Falta la imagen ' + esc(file) + '</div>';
      return '<button class="sb-shot s1-shot ' + (cls || '') + '" type="button" data-action="open-img" data-index="' + lbIndex(file) + '" aria-label="Ampliar: ' + esc(label) + '"><img loading="lazy" src="../' + esc(file) + '" alt="' + esc(a.title) + '"><span class="sb-stamp">ARTE PROVISIONAL</span></button>';
    }
    function sceneThumb(sc, cls) {
      if (!isDone(sc)) return '<div class="s1-pend ' + (cls || '') + '" title="' + esc(IM[sc] ? IM[sc].nota : '') + '">Imagen pendiente · ' + esc(sc) + '</div>';
      return thumb(fileOf(sc), 'escena ' + sc, cls);
    }
    function vtabs(sc) {
      var im = IM[sc];
      if (!im || !im.variantes) return '';
      var cur = varOf(sc);
      return '<div class="s1-vtabs s1-noprint" role="group" aria-label="Variante de ' + esc(sc) + '">' + Object.keys(im.variantes).map(function (k) {
        return '<button class="chip" type="button" data-action="s1-var" data-scene="' + esc(sc) + '" data-value="' + k + '" aria-pressed="' + (cur === k) + '">' + k + '</button>';
      }).join('') + '</div>';
    }
    function sceneCard(sc, withNote) {
      var im = IM[sc];
      return '<figure class="s1-scene" id="' + (withNote ? 's1-gsc-' : 's1-sc-') + esc(sc) + '"><div class="s1-scene-img">' + sceneThumb(sc) + '</div><figcaption><b>' + esc(sc) + '</b>' + (info[sc] ? ' <small>Día ' + info[sc].dia + ' · ' + esc(info[sc].bloque) + '</small>' : '') + vtabs(sc) + (withNote && im ? '<span class="s1-note">' + esc(im.nota) + '</span>' : '') + '</figcaption></figure>';
    }
    function filmstrip(scs) {
      return '<div class="s1-film" aria-label="Imágenes del día en orden">' + scs.map(function (sc) {
        if (!isDone(sc)) return '<span class="s1-frame is-pend" title="Imagen pendiente · ' + esc(sc) + '"><i>pendiente</i><b>' + esc(sc) + '</b></span>';
        return '<button class="s1-frame" type="button" data-action="open-img" data-index="' + lbIndex(fileOf(sc)) + '" aria-label="Ampliar: escena ' + esc(sc) + '" title="' + esc(sc) + '"><img loading="lazy" src="../' + esc(fileOf(sc)) + '" alt=""><b>' + esc(sc) + '</b></button>';
      }).join('') + '</div>';
    }
    function dayScenes(d) { var o = []; d.bloques.forEach(function (b) { o = o.concat(b.escenas); }); return o; }
    var nDone = allScenes.filter(isDone).length;
    function weekStrip() {
      var x = '<section class="s1-week" id="s1-semana-img"><h2 class="section-title">Tira de la semana <small>' + nDone + ' de ' + allScenes.length + ' escenas con imagen · arte provisional</small></h2><div class="s1-week-head">';
      if (CAB.mapa) x += '<div class="s1-cab"><span>Mapa de Valdoria</span>' + thumb(CAB.mapa, 'Mapa de Valdoria con niebla', 's1-cab-img') + '</div>';
      if (CAB.props) x += '<div class="s1-cab"><span>Hoja de props</span>' + thumb(CAB.props, 'Hoja de props', 's1-cab-img') + '</div>';
      x += '</div><div class="s1-week-grid">' + W.dias.map(function (d) {
        return '<div class="s1-week-day"><a href="#/semana1?h=s1-d' + d.dia + '"><b>Día ' + d.dia + '</b> <small>' + esc(d.nombre) + '</small></a>' + filmstrip(dayScenes(d)) + '</div>';
      }).join('') + '</div></section>';
      return x;
    }
    function gallery() {
      var f = st.galf, shown = 0;
      var x = '<section class="s1-gal" id="s1-galeria"><h2 class="section-title">Galería de la semana <small>' + nDone + ' de ' + allScenes.length + ' escenas con imagen</small></h2><div class="filters s1-noprint" role="group" aria-label="Filtro de la galería"><div class="filter-group"><span class="filter-label">Mostrar</span>' +
        [['todas', 'Todas'], ['hechas', 'Solo hechas'], ['pendientes', 'Solo pendientes']].map(function (a) { return '<button class="chip" type="button" data-action="s1-galf" data-value="' + a[0] + '" aria-pressed="' + (f === a[0]) + '">' + a[1] + '</button>'; }).join('') + '</div></div>';
      W.dias.forEach(function (d) {
        var scs = dayScenes(d).filter(function (sc) { return f === 'todas' || (f === 'hechas') === isDone(sc); });
        if (!scs.length) return;
        shown += scs.length;
        x += '<h3 class="sb-sub"><a href="#/semana1?h=s1-d' + d.dia + '">Día ' + d.dia + ' · ' + esc(d.nombre) + '</a></h3><div class="s1-gal-grid">' + scs.map(function (sc) { return sceneCard(sc, true); }).join('') + '</div>';
      });
      if (!shown) x += '<div class="notice">Ninguna escena coincide con el filtro.</div>';
      return x + '</section>';
    }
    function changes(day, block) {
      var out = [];
      if (happy) return out;
      [[reme, st.reme, 'Variante de Reme'], [diff, st.diff, 'Dificultad']].forEach(function (a) {
        if (!a[0]) return;
        a[0].que_cambia.forEach(function (c) {
          if (s1Days(c.dia).indexOf(day) < 0) return;
          var sc = (String(c.escena).match(/d\d+\.\d+/) || [''])[0];
          var inBlock = block ? block.escenas.indexOf(sc) >= 0 : !sc || !W.dias[day - 1].bloques.some(function (b) { return b.escenas.indexOf(sc) >= 0; });
          if (inBlock) out.push({ who: a[2], sel: a[1], c: c });
        });
      });
      return out;
    }
    function callouts(list) {
      return list.map(function (x) {
        var c = x.c, po = c.por_opcion, body = '<span class="s1-ctx">' + esc(c.cambio) + '</span>';
        if (po && x.sel !== 'all') body += '<div><mark>' + esc(x.sel) + '</mark> ' + esc(po[x.sel] || '') + '</div>';
        else if (po) body += '<ul class="s1-list">' + Object.keys(po).map(function (k) { return '<li><b>' + esc(k) + ':</b> ' + esc(po[k]) + '</li>'; }).join('') + '</ul>';
        return '<div class="s1-var"><b>' + esc(x.who) + (x.sel !== 'all' ? ': ' + esc(x.sel) : '') + (c.escena ? ' · ' + esc(c.escena) : '') + '</b> ' + body + '</div>';
      }).join('');
    }
    function obsFor(day, name) {
      return W.obligatorios_de_la_semana.filter(function (o) { return o.dia === day && o.bloque === name; });
    }
    function statePair(label, o) {
      return '<div class="s1-state"><h5>' + esc(label) + '</h5><dl>' + [['esquirlas', 'Esquirlas'], ['inventario', 'Inventario'], ['herramienta', 'Herramienta'], ['deuda', 'Deuda']].map(function (k) { return '<dt>' + k[1] + '</dt><dd>' + esc(o[k[0]]) + '</dd>'; }).join('') + '</dl></div>';
    }
    function tutorialBox(tut) {
      if (!tut) return '';
      var body = tut.length ? '<ul class="s1-tutlist">' + tut.map(function (t) {
        return '<li><b>' + esc(t.que) + '</b><dl class="s1-ver"><dt>Cómo se enseña</dt><dd>' + esc(t.como) + '</dd><dt class="s1-gate-k">Compuerta</dt><dd>' + esc(t.compuerta) + '</dd><dt>Si falla o abandonas</dt><dd>' + esc(t.si_falla) + '</dd></dl></li>';
      }).join('') + '</ul>' : '<p>Sin proceso de primera vez en este bloque.</p>';
      return '<div class="s1-sec s1-tut"><h5>Tutorial y compuerta</h5>' + body + '</div>';
    }
    function block(d, b) {
      var key = 'd' + d.dia + '-' + b.bloque;
      var obs = obsFor(d.dia, b.bloque), ch = changes(d.dia, b), hl = ch.some(function (x) { return x.sel !== 'all'; });
      var open = st.open[key] || hl;
      var x = '<details class="s1-block' + (b.obligatorio ? ' is-ob' : '') + (hl ? ' s1-hl' : '') + '" data-key="' + esc(key) + '"' + (open ? ' open' : '') + '><summary><span class="s1-when">' + esc(b.bloque) + '</span><span class="s1-where">' + esc(b.lugar) + '</span><span class="s1-badges">' +
        (b.obligatorio ? '<span class="pill s1-must">OBLIGATORIO</span>' : '<span class="pill s1-opt">opcional</span>') + obs.map(function (o) { return '<a class="chip brass" href="#/semana1?h=s1-' + esc(o.id) + '">' + esc(o.id) + '</a>'; }).join('') + (ch.length ? '<span class="pill s1-chg">' + (hl ? 'cambia' : 'variantes') + '</span>' : '') + '</span></summary><div class="s1-body">';
      if (b.escenas.length) x += '<div class="s1-shots">' + b.escenas.map(function (sc) { return sceneCard(sc, false); }).join('') + '</div>';
      x += '<div class="gx-tags">' + (b.escenas.length ? b.escenas.map(function (sc) {
        return sbScenes[sc] ? '<a class="chip" href="#/storyboard?h=sb-' + esc(sc) + '" title="Ver el panel del storyboard">' + esc(sc) + ' ▣</a>' : '<span class="chip">' + esc(sc) + '</span>';
      }).join('') : '<span class="chip">sin escenas guionizadas</span>') + '</div>';
      x += '<p class="s1-why"><b>' + (b.obligatorio ? 'Obligatorio porque' : 'Por qué') + ':</b> ' + esc(b.por_que_obligatorio) + '</p>';
      x += callouts(ch);
      x += s1Row('Se dispara cuando', b.dispara);
      x += s1Sec('Pasos', b.pasos, 's1-steps') + s1Sec('Cómo se hace', b.como) + s1Sec('Qué se espera', b.se_espera);
      x += tutorialBox(b.tutorial);
      if (!happy) x += s1Sec('Opcional', b.opcional) + s1Row('Si no lo haces', b.si_no_lo_haces);
      x += s1Row('Ayuda en pantalla', b.ayuda_en_pantalla) + s1Row('Prensa y rumores', b.prensa);
      if (b.hilos.length) x += '<div class="s1-sec"><h5>Hilos</h5><div class="gx-tags">' + b.hilos.map(function (hid) { return '<a class="chip" href="#/hilos?h=' + esc(hid) + '">' + esc(hid) + '</a>'; }).join('') + '</div></div>';
      return x + '</div></details>';
    }
    function decision(d) {
      var x = '';
      if (d.decision) {
        var D = d.decision;
        x += '<div class="s1-dec" id="s1-dec-' + d.dia + '"><h4>Decisión del día <small>' + esc(D.tipo) + (D.id ? ' · <a href="#/semana1?h=s1-r-' + esc(D.id) + '">' + esc(D.id) + '</a>' : '') + '</small></h4><p><b>' + esc(D.pregunta) + '</b></p><div class="table-wrap"><table><thead><tr><th>Opción</th><th>Efecto</th><th>Bandera</th><th>Fuente</th></tr></thead><tbody>' +
          D.opciones.map(function (o) { return '<tr><td>' + esc(o.texto) + '</td><td>' + esc(o.efecto) + '</td><td><code>' + esc(o.bandera) + '</code></td><td><small>' + esc(o.fuente) + '</small></td></tr>'; }).join('') + '</tbody></table></div></div>';
      }
      var otras = W.decisiones_y_ramas.filter(function (r) { return r.dia === d.dia && !(d.decision && d.decision.id === r.id); });
      if (otras.length) x += '<p class="s1-others"><b>Otras decisiones del día:</b> ' + otras.map(function (r) { return '<a class="chip" href="#/semana1?h=s1-r-' + esc(r.id) + '">' + esc(r.id) + '</a>'; }).join(' ') + '</p>';
      return x;
    }
    function dayCard(d) {
      var ch = changes(d.dia, null);
      var x = '<section class="s1-day" id="s1-d' + d.dia + '"><h2 class="section-title">Día ' + d.dia + ' · ' + esc(d.nombre) + ' <small>' + esc(d.fecha) + '</small></h2>';
      x += filmstrip(dayScenes(d));
      x += '<p class="s1-goal"><b>Objetivo.</b> ' + esc(d.objetivo_del_dia) + '</p><p class="s1-new"><b>Mecánica nueva.</b> ' + esc(d.mecanica_nueva) + '</p>' + callouts(ch);
      x += '<div class="s1-states">' + statePair('Al empezar', d.estado_al_empezar) + statePair('Al terminar', d.estado_al_terminar) + '</div>';
      x += '<div class="s1-blocks">' + d.bloques.map(function (b) { return block(d, b); }).join('') + '</div>' + decision(d);
      x += s1Sec('Al cerrar el día debe ser cierto', d.checkpoints, 's1-check');
      return x + '</section>';
    }
    function chips(group, key, list, label, all) {
      return '<div class="filter-group"><span class="filter-label">' + label + '</span>' + [['all', all]].concat(list.map(function (n) { return [n, n]; })).map(function (a) {
        return '<button class="chip" type="button" data-action="' + key + '" data-value="' + esc(a[0]) + '" aria-pressed="' + (group === a[0]) + '"' + (happy && key !== 's1-mode' ? ' disabled title="Pasa a «Con variantes» para usar este filtro"' : '') + '>' + esc(a[1]) + '</button>';
      }).join('') + '</div>';
    }

    h += '<p class="page-lead">' + esc(W.nota) + ' Fuente: <a href="#/docs/27-guion-del-acto-i">27 · Guion del Acto I</a>. Mira también el <a href="#/storyboard">storyboard del Acto I</a>.</p>';
    h += '<div class="filters s1-noprint" role="group" aria-label="Filtros de la semana 1">' +
      '<div class="filter-group"><span class="filter-label">Modo</span><button class="chip" type="button" data-action="s1-mode" data-value="feliz" aria-pressed="' + happy + '">Solo camino feliz</button><button class="chip" type="button" data-action="s1-mode" data-value="variantes" aria-pressed="' + !happy + '">Con variantes</button></div>' +
      chips(st.reme, 's1-reme', S1_REME, 'Variante de Reme', 'Ninguna') + chips(st.diff, 's1-diff', S1_DIFF, 'Dificultad', 'Ninguna') +
      '<div class="filter-group"><button class="chip" type="button" data-action="s1-open" data-value="1">Desplegar todo</button><button class="chip" type="button" data-action="s1-open" data-value="0">Plegar todo</button><button class="chip" type="button" data-action="deck-print">Imprimir</button></div></div>';
    h += '<div class="filters s1-noprint" role="group" aria-label="Vista de la semana"><div class="filter-group"><span class="filter-label">Vista</span><button class="chip" type="button" data-action="s1-gal" data-value="0" aria-pressed="' + !st.gal + '">Detalle por día</button><button class="chip" type="button" data-action="s1-gal" data-value="1" aria-pressed="' + st.gal + '">Galería de imágenes</button><span class="s1-count-img">' + nDone + ' de ' + allScenes.length + ' escenas con imagen</span></div></div>';
    h += weekStrip();
    if (st.gal) { lb.list = list; return '<div class="s1">' + h + gallery() + '</div>'; }
    h += '<nav class="s1-line" aria-label="Línea de tiempo de la semana">' + W.dias.map(function (d) {
      var short = d.mecanica_nueva.split(/[:.]/)[0];
      return '<a class="s1-chip" href="#/semana1?h=s1-d' + d.dia + '" title="' + esc(d.mecanica_nueva) + '"><b>Día ' + d.dia + '</b><span>' + esc(d.nombre) + '</span><small>' + esc(short) + '</small>' + (d.decision ? '<i class="s1-mark" title="Decisión del día: ' + esc(d.decision.id || d.decision.tipo) + '">⑂ decisión</i>' : '') + '</a>';
    }).join('') + '<a class="s1-chip s1-gate" href="#/semana1?h=s1-puerta"><b>Puerta</b><span>del Acto I</span><small>Quiroga sella en d7.3</small></a></nav>';
    h += '<div class="s1-door" id="s1-puerta"><h3>Puerta del Acto I</h3>' + s1Ul(W.puerta_del_acto.condiciones) + '<p><b>Resultado.</b> ' + esc(W.puerta_del_acto.resultado) + '</p></div>';
    if (W.reglas_decididas && W.reglas_decididas.length) h += '<div class="s1-door" id="s1-reglas"><h3>Reglas decididas por el autor</h3>' + s1Ul(W.reglas_decididas) + '</div>';
    h += '<details class="s1-sum"><summary>Resumen del camino feliz</summary>' + s1Ul(W.camino_feliz_resumen) + '</details>';
    W.dias.forEach(function (d) { h += dayCard(d); });

    var done = W.obligatorios_de_la_semana.filter(function (o) { return checks[o.id]; }).length;
    h += '<section class="s1-obs" id="s1-obligatorios"><h2 class="section-title">Obligatorios de la semana <small id="s1-count">' + done + ' de ' + W.obligatorios_de_la_semana.length + ' cumplidos</small></h2><p class="gx-lead">Marca cada uno al comprobarlo en la partida. Se guarda en este navegador.</p>' +
      '<div class="s1-noprint"><button class="chip" type="button" data-action="s1-reset">Reiniciar</button></div><ul class="s1-checks">' +
      W.obligatorios_de_la_semana.map(function (o) {
        return '<li id="s1-' + esc(o.id) + '"' + (checks[o.id] ? ' class="is-done"' : '') + '><label><input type="checkbox" data-action="s1-check" data-id="' + esc(o.id) + '"' + (checks[o.id] ? ' checked' : '') + '><span><b>' + esc(o.id) + '</b> · <a href="#/semana1?h=s1-d' + o.dia + '">Día ' + o.dia + ' · ' + esc(o.bloque) + '</a> · ' + esc(o.que) + '</span></label>' +
          '<dl class="s1-ver"><dt>Por qué</dt><dd>' + esc(o.por_que) + '</dd><dt>Verificación</dt><dd>' + esc(o.verificacion) + '</dd><dt>Falla si</dt><dd>' + esc(o.falla_si) + '</dd></dl></li>';
      }).join('') + '</ul></section>';

    h += '<section id="s1-ramas"><h2 class="section-title">Decisiones y ramas</h2><p class="gx-lead">Qué pasa al instante con cada opción y dónde se nota después.</p>';
    W.decisiones_y_ramas.forEach(function (r) {
      var dd = W.dias.filter(function (d) { return d.decision && d.decision.id === r.id; })[0];
      h += '<h3 class="sb-sub" id="s1-r-' + esc(r.id) + '"><code>' + esc(r.id) + '</code> <small>día ' + esc(r.dia) + (dd ? ' · ' + esc(dd.decision.pregunta) : '') + '</small></h3><div class="table-wrap"><table><thead><tr><th>Opción</th><th>Al instante</th><th>Después</th><th>Bandera</th></tr></thead><tbody>' +
        r.opciones.map(function (o) {
          return '<tr><td><b>' + esc(o.id) + '</b></td><td>' + esc(o.consecuencia_inmediata) + '</td><td>' + (o.consecuencias_posteriores.length ? '<ul class="s1-list">' + o.consecuencias_posteriores.map(function (c) { return '<li><b>' + (typeof c.dia === 'number' ? 'Día ' + c.dia : esc(c.dia)) + ' · ' + esc(c.escena) + '</b> ' + esc(c.que) + '</li>'; }).join('') + '</ul>' : '—') + '</td><td><code>' + esc(o.bandera) + '</code></td></tr>';
        }).join('') + '</tbody></table></div>';
    });
    h += '</section>';

    if (!happy) {
      h += '<section id="s1-variantes"><h2 class="section-title">Variantes globales</h2>' + W.variantes_globales.map(function (v) {
        return '<details class="s1-sum"><summary>' + esc(v.eje) + '</summary><div class="table-wrap"><table><thead><tr><th>Día</th><th>Escena</th><th>Qué cambia</th></tr></thead><tbody>' +
          v.que_cambia.map(function (c) { return '<tr><td>' + esc(c.dia) + '</td><td>' + esc(c.escena) + '</td><td>' + esc(c.cambio) + (c.por_opcion ? '<ul class="s1-list">' + Object.keys(c.por_opcion).map(function (k) { return '<li><b>' + esc(k) + ':</b> ' + esc(c.por_opcion[k]) + '</li>'; }).join('') + '</ul>' : '') + '</td></tr>'; }).join('') + '</tbody></table></div></details>';
      }).join('') + '</section>';
      h += '<section id="s1-errores"><h2 class="section-title">Errores comunes y recuperación</h2><div class="table-wrap"><table><thead><tr><th>Situación</th><th>Qué pasa</th><th>Cómo se recupera</th></tr></thead><tbody>' +
        W.errores_comunes_y_recuperacion.map(function (e) { return '<tr><td>' + esc(e.situacion) + '</td><td>' + esc(e.que_pasa) + '</td><td>' + esc(e.como_se_recupera) + '</td></tr>'; }).join('') + '</tbody></table></div></section>';
    }
    if (W.dudas && W.dudas.length) h += '<details class="s1-sum"><summary>Dudas abiertas para el autor (' + W.dudas.length + ')</summary>' + s1Ul(W.dudas) + '</details>';
    lb.list = list;
    return '<div class="s1">' + h + '</div>';
  }

  function viewArt() {
    var imgs = H.assets.images;
    var cats = ['Todas'];
    imgs.forEach(function (i) { if (cats.indexOf(i.category) < 0) cats.push(i.category); });
    var list = imgs.filter(function (i) { return state.art.cat === 'Todas' || i.category === state.art.cat; });
    lb.list = list;
    var h = '<p class="eyebrow">Recursos</p><h1 class="page-title">Arte y assets</h1><p class="page-lead">' + esc(H.assets.source_note) + '</p>';
    h += '<div class="filters"><div class="filter-group"><span class="filter-label">Categoría</span>' + cats.map(function (c) {
      return '<button class="chip" type="button" data-action="art-cat" data-value="' + esc(c) + '" aria-pressed="' + (state.art.cat === c) + '">' + esc(c) + '</button>';
    }).join('') + '</div></div>';
    h += '<div class="gallery">';
    list.forEach(function (i, n) {
      h += '<button class="thumb" type="button" data-action="open-img" data-index="' + n + '"><img loading="lazy" src="../' + esc(i.file) + '" alt="' + esc(i.title) + '"><div class="thumb-info"><div class="thumb-title">' + esc(i.title) + '</div><div class="thumb-meta"><span class="pill st-' + esc(i.status) + '">' + esc(i.status) + '</span><span class="chip">' + esc(i.category) + '</span><span class="chip">ronda ' + i.round + '</span></div></div></button>';
    });
    h += '</div>';
    h += '<h2 class="section-title">Registro de assets <small>base del registro de licencias</small></h2><div class="table-wrap"><table><thead><tr><th>Archivo</th><th>Origen</th><th>Licencia / uso comercial</th><th class="num-cell">KB</th></tr></thead><tbody>';
    imgs.forEach(function (i) {
      h += '<tr><td>' + esc(i.file.replace('assets-ref/', '')) + (i.exists ? '' : ' <span class="pill s-review">falta</span>') + '</td><td>IA (gpt_image_2_5)</td><td>Por revisar</td><td class="num-cell">' + (i.kb || '—') + '</td></tr>';
    });
    return h + '</tbody></table></div>';
  }

  function viewSound() {
    var a = H.assets;
    var h = '<p class="eyebrow">Recursos</p><h1 class="page-title">Sonido</h1><p class="page-lead">Referencia sonora: Balatro. Voces de personajes como blips cortos. Antes de usar cualquier sonido hay que registrar su licencia.</p>';
    h += '<h2 class="section-title">Archivos de audio <small>' + a.audio.length + '</small></h2>';
    if (!a.audio.length) h += '<div class="notice">Todavía no hay audio. Los archivos .mp3, .wav u .ogg que se coloquen en <code>studio/assets-ref/audio/</code> aparecerán aquí después de ejecutar <code>python3 studio/hub/build.py</code>.</div>';
    else h += '<div class="grid grid-2">' + a.audio.map(function (f) { return '<div class="card"><div style="font-weight:600;margin-bottom:8px">' + esc(f.name) + '</div><audio controls preload="none" src="../' + esc(f.file) + '" style="width:100%"></audio></div>'; }).join('') + '</div>';
    h += '<h2 class="section-title">Plan de sonidos <small>' + a.sounds_planned.length + ' previstos</small></h2><div class="table-wrap"><table><thead><tr><th>Sonido</th><th>Grupo</th><th>Estado</th></tr></thead><tbody>';
    a.sounds_planned.forEach(function (s) { h += '<tr><td>' + esc(s.name) + '</td><td>' + esc(s.group) + '</td><td><span class="pill s-backlog">' + esc(s.status) + '</span></td></tr>'; });
    return h + '</tbody></table></div>';
  }

  function viewPalette() {
    var p = H.palette;
    var h = '<p class="eyebrow">Recursos</p><h1 class="page-title">Paleta</h1><p class="page-lead">Colores fríos, vinotinto como acento principal y latón como detalle. Toca un color para copiar su código.</p>';
    h += '<div class="proportion" role="img" aria-label="Proporción de uso de colores: ' + p.proportion.map(function (x) { return esc(x.label) + ' ' + x.pct + ' por ciento'; }).join(', ') + '">' + p.proportion.map(function (x) { return '<span style="width:' + x.pct + '%;background:' + x.color + '"></span>'; }).join('') + '</div>';
    h += '<ul class="legend">' + p.proportion.map(function (x) { return '<li><i style="background:' + x.color + '"></i>' + esc(x.label) + ' <b>' + x.pct + '%</b></li>'; }).join('') + '</ul>';
    h += '<h2 class="section-title">Colores</h2><div class="swatches">' + p.colors.map(function (c) {
      return '<button class="swatch" type="button" data-action="copy-hex" data-hex="' + esc(c.hex) + '" aria-label="Copiar ' + esc(c.name) + ' ' + esc(c.hex) + '"><div class="swatch-chip" style="background:' + esc(c.hex) + '"></div><div class="swatch-info"><div class="swatch-name">' + esc(c.name) + '</div><div class="swatch-hex">' + esc(c.hex) + ' · ' + esc(c.role) + '</div><div class="swatch-use">' + esc(c.use) + '</div></div></button>';
    }).join('') + '</div>';
    h += '<h2 class="section-title">Reglas de uso</h2><div class="card"><ul class="prose" style="margin:0">' + p.rules.map(function (r) { return '<li>' + esc(r) + '</li>'; }).join('') + '</ul></div>';
    return h;
  }

  /* ---------- búsqueda ---------- */
  var searchIndex = null;
  function buildIndex() {
    searchIndex = [];
    H.docs.forEach(function (d) {
      var cur = { id: '', text: d.title };
      d.md.split('\n').forEach(function (line) {
        if (/^\s*\|?\s*:?-{2,}/.test(line) && line.indexOf('|') !== -1) return;
        var hm = line.match(/^(#{1,6})\s+(.*)$/);
        if (hm) cur = { id: slug(stripMd(hm[2])), text: stripMd(hm[2]) };
        var text = stripMd(line);
        if (text.length < 3) return;
        searchIndex.push({ kind: 'doc', doc: d, head: cur, text: text, f: fold(text) });
      });
    });
    TASKS.forEach(function (t) {
      var text = t.id + ' ' + t.title + (t.desc ? ' — ' + t.desc : '');
      searchIndex.push({ kind: 'task', task: t, text: text, f: fold(text) });
      t.comments.forEach(function (c) { searchIndex.push({ kind: 'activity', task: t, label: 'Comentario · ' + (AUTHOR[c.by] || c.by), text: c.text, f: fold(c.text) }); });
      t.history.forEach(function (x) { searchIndex.push({ kind: 'activity', task: t, label: 'Historial · ' + move(x), text: x.note, f: fold(x.note) }); });
      t.evidence.forEach(function (e) {
        var tx = (e.title || '') + ' ' + (e.note || '') + ' ' + (e.text || '');
        if (tx.trim()) searchIndex.push({ kind: 'activity', task: t, label: 'Evidencia', text: tx.trim(), f: fold(tx) });
      });
    });
  }
  function highlight(text, tokens) {
    var f = fold(text);
    var marks = [];
    tokens.forEach(function (tk) {
      var from = 0, at;
      while ((at = f.indexOf(tk, from)) !== -1) { marks.push([at, at + tk.length]); from = at + tk.length; }
    });
    marks.sort(function (a, b) { return a[0] - b[0]; });
    var out = '', pos = 0;
    marks.forEach(function (m) {
      if (m[0] < pos) return;
      out += esc(text.slice(pos, m[0])) + '<mark>' + esc(text.slice(m[0], m[1])) + '</mark>';
      pos = m[1];
    });
    return out + esc(text.slice(pos));
  }
  function viewSearch(q) {
    if (!searchIndex) buildIndex();
    var tokens = fold(q).split(/\s+/).filter(Boolean);
    var h = '<p class="eyebrow">Búsqueda</p><h1 class="page-title">Resultados para «' + esc(q) + '»</h1>';
    if (!tokens.length) return h + '<div class="empty">Escribe algo para buscar.</div>';
    var hits = searchIndex.filter(function (e) { return tokens.every(function (t) { return e.f.indexOf(t) !== -1; }); });
    h += '<p class="page-lead">' + hits.length + ' coincidencia' + (hits.length === 1 ? '' : 's') + (hits.length > 60 ? ' (se muestran las primeras 60)' : '') + '.</p>';
    hits.slice(0, 60).forEach(function (e) {
      if (e.kind === 'doc') {
        h += '<div class="result"><a class="r-title" href="#/docs/' + e.doc.id + (e.head.id ? '?h=' + e.head.id : '') + '">' + esc(e.doc.title) + '</a><span class="r-where">' + esc(e.head.text) + '</span><p>' + highlight(e.text, tokens) + '</p></div>';
      } else if (e.kind === 'task') {
        h += '<div class="result"><a class="r-title" href="#/tarea/' + esc(e.task.id) + '">' + esc(e.task.id) + ' · ' + highlight(e.task.title, tokens) + '</a><span class="r-where">Tarea · ' + esc(e.task.phase.id) + ' · ' + e.task.prio + ' · ' + STATUS[e.task.status].label + '</span>' + (e.task.desc ? '<p>' + highlight(e.task.desc, tokens) + '</p>' : '') + '</div>';
      } else {
        h += '<div class="result"><a class="r-title" href="#/tarea/' + esc(e.task.id) + '">' + esc(e.task.id) + ' · ' + esc(e.task.title) + '</a><span class="r-where">' + esc(e.label) + '</span><p>' + highlight(e.text, tokens) + '</p></div>';
      }
    });
    if (!hits.length) h += '<div class="empty">Sin resultados.</div>';
    return h;
  }

  /* ---------- ruteo ---------- */
  function parseHash() {
    var raw = location.hash.replace(/^#\/?/, '');
    var parts = raw.split('?');
    var query = {};
    (parts[1] || '').split('&').forEach(function (kv) {
      if (!kv) return;
      var p = kv.split('=');
      query[decodeURIComponent(p[0])] = decodeURIComponent((p[1] || '').replace(/\+/g, ' '));
    });
    return { segs: parts[0].split('/').filter(Boolean).map(decodeURIComponent), query: query };
  }
  function render(keepScroll) {
    var r = parseHash();
    var key = r.segs[0] || '';
    var html, title = H.config.title;
    var anchor = null;
    var activeKey = key;
    var y = window.scrollY;
    var tlScroll = $('.tl-wrap') ? $('.tl-wrap').scrollLeft : 0;
    var dcScroll = $('.dc-board') ? $('.dc-board').scrollLeft : 0;
    switch (key) {
      case '': html = viewHome(); title += ' · Inicio'; break;
      case 'roadmap': html = viewRoadmap(); title += ' · Roadmap'; break;
      case 'linea': html = viewTimeline(); title += ' · Línea de tiempo'; break;
      case 'tablero': html = viewBoard(); title += ' · Tablero'; break;
      case 'qa': html = viewQA(); title += ' · QA'; break;
      case 'juego': html = viewGame(); title += ' · El juego'; break;
      case 'mapa': html = viewStory(); title += ' · Mapa de historia'; break;
      case 'decisiones': html = viewDecisions(); title += ' · Árbol de decisiones'; anchor = r.query.h || null; break;
      case 'hilos': html = viewThreads(); title += ' · Hilos narrativos'; anchor = r.query.h || null; break;
      case 'limpieza': html = viewClean(); title += ' · Limpieza del diseño'; break;
      case 'coherencia': html = viewCoherence(); title += ' · Coherencia del diseño'; break;
      case 'simulador': html = viewSimulator(); title += ' · Simulador de economía'; break;
      case 'tarea': html = viewTask(r.segs[1] || ''); title += ' · ' + (r.segs[1] || 'Tarea'); activeKey = 'tablero'; break;
      case 'personajes': html = viewGallery(); title += ' · Personajes y NPC'; anchor = r.query.h || null; break;
      case 'storyboard': html = viewStoryboard(); title += ' · Storyboard del Acto I'; anchor = r.query.h || null; break;
      case 'semana1': html = viewSemana1(); title += ' · Semana 1'; anchor = r.query.h || null; break;
      case 'arte': html = viewArt(); title += ' · Arte'; break;
      case 'sonido': html = viewSound(); title += ' · Sonido'; break;
      case 'paleta': html = viewPalette(); title += ' · Paleta'; break;
      case 'buscar': html = viewSearch(r.query.q || ''); title += ' · Buscar'; activeKey = '__ninguno__'; break;
      case 'docs':
        html = viewDoc(r.segs[1] || '');
        anchor = r.query.h || null;
        activeKey = 'docs/' + (r.segs[1] || '');
        var d = H.docs.filter(function (x) { return x.id === r.segs[1]; })[0];
        if (d) title += ' · ' + d.title;
        break;
      default: html = '<div class="notice">Página no encontrada. <a href="#/">Volver al inicio</a>.</div>';
    }
    teardownDeck();
    main.className = key === 'juego' ? 'is-deck' : '';
    main.innerHTML = html;
    document.title = title;
    setActive(activeKey);
    closeMenu();
    if (keepScroll) {
      window.scrollTo(0, y);
      if ($('.tl-wrap')) $('.tl-wrap').scrollLeft = tlScroll;
      if ($('.dc-board')) $('.dc-board').scrollLeft = dcScroll;
      return;
    }
    if (key === 'juego') initDeck();
    var target = anchor && document.getElementById(anchor);
    if (target) target.scrollIntoView(); else window.scrollTo(0, 0);
  }

  /* ---------- interacciones ---------- */
  function openLightbox(idx, opener) {
    lb.idx = idx;
    lb.opener = opener || null;
    showLightbox();
    $('#lightbox').hidden = false;
    $('#lbClose').focus();
  }
  function showLightbox() {
    var i = lb.list[lb.idx];
    if (!i) return;
    $('#lbImg').src = '../' + i.file;
    $('#lbImg').alt = i.title;
    $('#lbCap').innerHTML = '<strong>' + esc(i.title) + '</strong><br>' + esc(i.note || '') + '<br><span class="est">' + esc(i.category) + ' · ronda ' + i.round + ' · ' + esc(i.status) + ' · ' + (lb.idx + 1) + '/' + lb.list.length + '</span>';
  }
  function closeLightbox() {
    $('#lightbox').hidden = true;
    if (lb.opener && document.body.contains(lb.opener)) lb.opener.focus();
  }
  function stepLightbox(d) {
    if (!lb.list.length) return;
    lb.idx = (lb.idx + d + lb.list.length) % lb.list.length;
    showLightbox();
  }
  function toast(msg) {
    var t = document.createElement('div');
    t.textContent = msg;
    t.setAttribute('role', 'status');
    t.style.cssText = 'position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:#17232c;border:1px solid #b8893a;color:#e3b25c;padding:8px 16px;border-radius:4px;z-index:300;font-family:ui-monospace,monospace;font-size:13px';
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 1600);
  }
  function openMenu() { $('#sidebar').classList.add('open'); $('#menuBtn').setAttribute('aria-expanded', 'true'); }
  function closeMenu() { $('#sidebar').classList.remove('open'); $('#menuBtn').setAttribute('aria-expanded', 'false'); }

  document.addEventListener('click', function (e) {
    var pl = e.target.closest('a[data-phase]');
    if (pl) { state.rm.open = {}; state.rm.open[pl.getAttribute('data-phase')] = true; }
    var el = e.target.closest('[data-action]');
    if (!el) return;
    var act = el.getAttribute('data-action');
    var val = el.getAttribute('data-value');
    if (act === 'scope') { state.scope = val; render(true); }
    else if (act === 'rm-target') { state.rm.target = val; render(true); }
    else if (act === 'rm-hide') { state.rm.hideDone = !state.rm.hideDone; render(true); }
    else if (act === 'art-cat') { state.art.cat = val; render(); }
    else if (act === 'qa-area') { state.qa.area = val; render(true); }
    else if (act === 'deck-go') { gotoSlide(+el.getAttribute('data-index')); }
    else if (act === 'deck-next') { gotoSlide(deck.idx + 1); }
    else if (act === 'deck-prev') { gotoSlide(deck.idx - 1); }
    else if (act === 'deck-full') { toggleFullscreen(); }
    else if (act === 'deck-print') { window.print(); }
    else if (act === 'dc-act') { state.dc.act = val; render(true); }
    else if (act === 'dc-level') { state.dc.level = val; render(true); }
    else if (act === 'hl-act') { state.hl.act = val; render(true); }
    else if (act === 'hl-tipo') { state.hl.tipo = val; render(true); }
    else if (act === 'hl-estado') { state.hl.estado = val; render(true); }
    else if (act === 'sb-var') { state.sb.v[el.getAttribute('data-scene')] = val; render(true); }
    else if (act === 's1-var') { state.s1.v[el.getAttribute('data-scene')] = val; render(true); }
    else if (act === 's1-gal') { state.s1.gal = val === '1'; render(true); }
    else if (act === 's1-galf') { state.s1.galf = val; render(true); }
    else if (act === 's1-mode') { state.s1.mode = val; render(true); }
    else if (act === 's1-reme') { state.s1.reme = val; render(true); }
    else if (act === 's1-diff') { state.s1.diff = val; render(true); }
    else if (act === 's1-open') {
      $$('.s1-block').forEach(function (d) { d.open = val === '1'; if (val === '1') state.s1.open[d.getAttribute('data-key')] = true; else delete state.s1.open[d.getAttribute('data-key')]; });
    }
    else if (act === 's1-reset') { s1Save({}); render(true); }
    else if (act === 'qa-type') { state.qa.type = val; render(true); }
    else if (act === 'sim-grupo') { state.sim.grupo = val; render(true); }
    else if (act === 'sim-estado') { state.sim.estado = val; render(true); }
    else if (act === 'sim-row') { if (state.sim.open[val]) delete state.sim.open[val]; else state.sim.open[val] = true; render(true); }
    else if (act === 'open-img') { openLightbox(+el.getAttribute('data-index'), el); }
    else if (act === 'tl-select') { state.tl.sel = state.tl.sel === val ? null : val; render(true); }
    else if (act === 'board-more') { state.board.limit[val] = (state.board.limit[val] || 12) + 25; render(true); }
    else if (act === 'copy-hex') {
      var hex = el.getAttribute('data-hex');
      try {
        navigator.clipboard.writeText(hex).then(function () { toast('Copiado ' + hex); }, function () { toast(hex); });
      } catch (err) { toast(hex); }
    }
  });
  document.addEventListener('change', function (e) {
    var el = e.target.closest('[data-action]');
    if (!el) return;
    var act = el.getAttribute('data-action');
    if (act === 'board-phase') { state.board.phase = el.value; state.board.limit = {}; render(true); }
    else if (act === 'board-target') { state.board.target = el.value; state.board.limit = {}; render(true); }
    else if (act === 's1-check') {
      var map = s1Load(), id = el.getAttribute('data-id');
      if (el.checked) map[id] = true; else delete map[id];
      s1Save(map);
      var li = el.closest('li');
      if (li) li.classList.toggle('is-done', el.checked);
      var total = $$('.s1-checks input').length, n = $$('.s1-checks input:checked').length;
      if ($('#s1-count')) $('#s1-count').textContent = n + ' de ' + total + ' cumplidos';
    }
    else if (act === 'dc-who') { state.dc.who = el.value; render(true); }
    else if (act === 'hl-who') { state.hl.who = el.value; render(true); }
    else if (act === 'tl-target') { state.tl.target = el.value; state.tl.sel = null; render(true); }
    else if (act === 'tl-zoom') { state.tl.px = parseFloat(el.value); render(true); }
    else if (act === 'tl-rate') { state.tl.rate = parseInt(el.value, 10); render(true); }
  });
  main.addEventListener('toggle', function (e) {
    var d = e.target;
    if (d.classList && d.classList.contains('s1-block')) {
      var k = d.getAttribute('data-key');
      if (d.open) state.s1.open[k] = true; else delete state.s1.open[k];
    }
    if (d.classList && d.classList.contains('phase') && state.rm.open) {
      var id = d.getAttribute('data-phase');
      if (d.open) state.rm.open[id] = true; else delete state.rm.open[id];
    }
  }, true);

  var s1Opened = [];
  window.addEventListener('beforeprint', function () {
    s1Opened = $$('.s1-block:not([open])');
    s1Opened.forEach(function (d) { d.open = true; });
  });
  window.addEventListener('afterprint', function () { s1Opened.forEach(function (d) { d.open = false; }); s1Opened = []; });

  $('#lbClose').addEventListener('click', closeLightbox);
  $('#lbPrev').addEventListener('click', function () { stepLightbox(-1); });
  $('#lbNext').addEventListener('click', function () { stepLightbox(1); });
  $('#lightbox').addEventListener('click', function (e) { if (e.target.id === 'lightbox') closeLightbox(); });
  document.addEventListener('keydown', function (e) {
    if ($('#lightbox').hidden) { if (e.key === 'Escape') closeMenu(); return; }
    if (e.key === 'Escape') closeLightbox();
    else if (e.key === 'ArrowLeft') stepLightbox(-1);
    else if (e.key === 'ArrowRight') stepLightbox(1);
  });
  $('#menuBtn').addEventListener('click', function () {
    if ($('#sidebar').classList.contains('open')) closeMenu(); else openMenu();
  });
  var searchTimer = null;
  $('#searchForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var q = $('#q').value.trim();
    if (q) location.hash = '#/buscar?q=' + encodeURIComponent(q);
  });
  $('#q').addEventListener('input', function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      var q = $('#q').value.trim();
      if (q.length >= 2) location.hash = '#/buscar?q=' + encodeURIComponent(q);
    }, 350);
  });
  window.addEventListener('hashchange', function () { render(false); });

  /* ---------- arranque ---------- */
  $('#gen').textContent = 'Actualizado ' + H.generated;
  document.title = H.config.title + ' · ' + H.config.subtitle;
  buildNav();
  render(false);
})();
