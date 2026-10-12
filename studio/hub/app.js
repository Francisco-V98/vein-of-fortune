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
    qa: { area: 'Todas', type: 'Todos' }
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
    h += link('', 'Inicio', '◆') + link('juego', 'El juego', '★') + link('mapa', 'Mapa de historia', '⌖') + link('roadmap', 'Roadmap', '▤') + link('linea', 'Línea de tiempo', '⟷') + link('tablero', 'Tablero', '▦') + link('qa', 'QA', '✔');
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

    h += '<h2 class="section-title">Estado del diseño <small>✅ acordado · 🟡 propuesta · ❓ abierto</small></h2><div class="table-wrap"><table><thead><tr><th>Documento</th><th class="num-cell">✅</th><th class="num-cell">🟡</th><th class="num-cell">❓</th></tr></thead><tbody>';
    H.docs.forEach(function (d) {
      h += '<tr><td><a href="#/docs/' + d.id + '">' + esc(d.title) + '</a></td><td class="num-cell">' + d.counts.ok + '</td><td class="num-cell">' + d.counts.prop + '</td><td class="num-cell">' + d.counts.open + '</td></tr>';
    });
    h += '</tbody></table></div>';
    return h;
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
    return '<svg class="mk-chart" viewBox="0 0 440 250" role="img" aria-label="Ejemplo: tras una noticia, el valor justo cambia y el precio lo alcanza con retraso">' +
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
    return head(s) + '<div class="mk"><div class="mk-left">' + marketChart() + '</div><div class="mk-right">' + s.points.map(function (p) {
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
    h += '<div class="doc-meta"><span class="chip">' + esc(d.group) + '</span><span class="chip" title="Acordado">✅ ' + d.counts.ok + '</span><span class="chip" title="Propuesta">🟡 ' + d.counts.prop + '</span><span class="chip" title="Abierto">❓ ' + d.counts.open + '</span><a class="chip" href="../docs/' + (d.id.indexOf('adr-') === 0 ? 'adr/' + esc(d.id.slice(4)) : esc(d.id)) + '.md" target="_blank" rel="noopener">Abrir archivo .md</a></div>';
    h += r.html + '</article>';
    h += '<nav class="toc" aria-label="En este documento"><div class="toc-title">En este documento</div>' +
      r.toc.map(function (t) { return '<a class="l' + t.level + '" href="#/docs/' + d.id + '?h=' + t.id + '">' + esc(t.text) + '</a>'; }).join('') + '</nav></div>';
    return h;
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
    switch (key) {
      case '': html = viewHome(); title += ' · Inicio'; break;
      case 'roadmap': html = viewRoadmap(); title += ' · Roadmap'; break;
      case 'linea': html = viewTimeline(); title += ' · Línea de tiempo'; break;
      case 'tablero': html = viewBoard(); title += ' · Tablero'; break;
      case 'qa': html = viewQA(); title += ' · QA'; break;
      case 'juego': html = viewGame(); title += ' · El juego'; break;
      case 'mapa': html = viewStory(); title += ' · Mapa de historia'; break;
      case 'tarea': html = viewTask(r.segs[1] || ''); title += ' · ' + (r.segs[1] || 'Tarea'); activeKey = 'tablero'; break;
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
    else if (act === 'qa-type') { state.qa.type = val; render(true); }
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
    else if (act === 'tl-target') { state.tl.target = el.value; state.tl.sel = null; render(true); }
    else if (act === 'tl-zoom') { state.tl.px = parseFloat(el.value); render(true); }
    else if (act === 'tl-rate') { state.tl.rate = parseInt(el.value, 10); render(true); }
  });
  main.addEventListener('toggle', function (e) {
    var d = e.target;
    if (d.classList && d.classList.contains('phase') && state.rm.open) {
      var id = d.getAttribute('data-phase');
      if (d.open) state.rm.open[id] = true; else delete state.rm.open[id];
    }
  }, true);

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
