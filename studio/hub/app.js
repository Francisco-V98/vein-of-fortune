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
    done: { label: 'Finalizada', glyph: '●' },
    dropped: { label: 'Desestimada', glyph: '✕' }
  };
  var STATUS_ORDER = ['backlog', 'sprint', 'doing', 'review', 'done', 'dropped'];
  var QUEUE_ORDER = { doing: 0, review: 1, sprint: 2, backlog: 3 };
  var AUTHOR = { autor: 'Autor', claude: 'Claude' };

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
    var m = href.match(/^(\d{2}-[\w-]+)\.md(?:#(.+))?$/);
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
  function statusPill(s) {
    return '<span class="pill s-' + s + '">' + STATUS[s].glyph + ' ' + STATUS[s].label + '</span>';
  }
  function targetPill(t) { return '<span class="pill ' + targetClass(t) + '">' + esc(t) + '</span>'; }
  function bar(pct, ok) { return '<div class="bar' + (ok ? ' ok' : '') + '" role="img" aria-label="' + pct + ' por ciento"><span style="width:' + pct + '%"></span></div>'; }
  function hoursRange(p) { return p.hours ? p.hours[0] + '–' + p.hours[1] + ' h estimadas' : 'sin estimación global'; }
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
    rm: { target: 'all', hideDone: false, open: null },
    board: { phase: 'current', target: 'all' },
    art: { cat: 'Todas' }
  };
  var lb = { list: [], idx: 0, opener: null };

  /* ---------- navegación lateral ---------- */
  function buildNav() {
    var cfg = H.config;
    var h = '<div class="brand"><div class="brand-mark" aria-hidden="true">' + esc(cfg.mark || 'VF') + '</div><div><div class="brand-title">' + esc(cfg.title) + '</div><div class="brand-sub">' + esc(cfg.subtitle) + '</div></div></div>';
    h += '<nav class="nav" aria-label="Secciones">';
    h += '<div class="nav-group">Panel</div>';
    h += link('', 'Inicio', '◆') + link('roadmap', 'Roadmap', '▤') + link('tablero', 'Tablero', '▦');
    H.groups.forEach(function (g) {
      var docs = H.docs.filter(function (d) { return d.group === g; });
      if (!docs.length) return;
      h += '<div class="nav-group">' + esc(g) + '</div>';
      docs.forEach(function (d) {
        var parts = d.title.split(' · ');
        h += '<a href="#/docs/' + d.id + '" data-key="docs/' + d.id + '"><span class="num">' + esc(d.id.slice(0, 2)) + '</span>' + esc(parts.length > 1 ? parts.slice(1).join(' · ') : d.title) + '</a>';
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

  /* ---------- vistas ---------- */
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

    h += '<h2 class="section-title">Fases <small>fase actual: ' + esc(cur.id + ' · ' + cur.name) + '</small></h2><div class="card">';
    phases.forEach(function (p) {
      var pr = progress(phaseTasks(p));
      h += '<div class="phase-row"><div class="phase-name"><a href="#/roadmap" data-phase="' + p.id + '" style="color:inherit;text-decoration:none">' + esc(p.id + ' · ' + p.name) + '</a><small>' + hoursRange(p) + ' · ' + esc(p.target) + '</small></div>' + bar(pr.pct, pr.pct === 100) + '<div class="pct">' + pr.pct + '%</div></div>';
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
      .sort(function (a, b) { return (QUEUE_ORDER[a.t.status] - QUEUE_ORDER[b.t.status]) || (a.idx - b.idx); })
      .slice(0, 6);
    h += '<h2 class="section-title">Siguiente en la cola</h2><div class="card">';
    if (!queue.length) h += '<div class="empty">No quedan tareas pendientes.</div>';
    queue.forEach(function (q) {
      h += '<div class="phase-row" style="grid-template-columns:70px 1fr auto"><span class="tid">' + esc(q.t.id) + '</span><span>' + taskLink(q.t) + '</span>' + statusPill(q.t.status) + '</div>';
    });
    h += '</div>';

    h += '<h2 class="section-title">Estado del diseño <small>✅ acordado · 🟡 propuesta · ❓ abierto</small></h2><div class="table-wrap"><table><thead><tr><th>Documento</th><th class="num-cell">✅</th><th class="num-cell">🟡</th><th class="num-cell">❓</th></tr></thead><tbody>';
    H.docs.forEach(function (d) {
      h += '<tr><td><a href="#/docs/' + d.id + '">' + esc(d.title) + '</a></td><td class="num-cell">' + d.counts.ok + '</td><td class="num-cell">' + d.counts.prop + '</td><td class="num-cell">' + d.counts.open + '</td></tr>';
    });
    h += '</tbody></table></div>';
    return h;
  }

  function viewRoadmap() {
    var s = state.rm;
    var cur = currentPhase();
    if (!s.open) { s.open = {}; s.open[cur.id] = true; }
    var h = '<p class="eyebrow">Plan</p><h1 class="page-title">Roadmap</h1><p class="page-lead">Fases, hitos y tareas con su objetivo (MVP, Release 1 o Evolutivo) y su estado. Las horas son horas del autor, no tiempo de cálculo de la IA. Actualizado el ' + esc(H.roadmap.meta.updated) + '.</p>';
    h += '<div class="filters"><div class="filter-group"><span class="filter-label">Objetivo</span>';
    ['all'].concat(targets).forEach(function (t) {
      h += '<button class="chip" type="button" data-action="rm-target" data-value="' + esc(t) + '" aria-pressed="' + (s.target === t) + '">' + (t === 'all' ? 'Todos' : esc(t)) + '</button>';
    });
    h += '</div><div class="filter-group"><button class="chip" type="button" data-action="rm-hide" aria-pressed="' + s.hideDone + '">Ocultar finalizadas</button></div></div>';

    var shown = 0;
    phases.forEach(function (p) {
      var all = phaseTasks(p);
      var list = all.filter(function (t) { return s.target === 'all' || t.target === s.target; });
      if (!list.length) return;
      shown++;
      var pr = progress(all);
      h += '<details class="phase" data-phase="' + p.id + '"' + (s.open[p.id] ? ' open' : '') + '><summary><div><div class="phase-head"><span class="phase-id">' + esc(p.id) + '</span><span class="phase-title">' + esc(p.name) + '</span>' + targetPill(p.target) + '</div><div class="stat-sub">' + hoursRange(p) + ' · ' + pr.nd + ' de ' + pr.n + ' tareas</div></div>' + bar(pr.pct, pr.pct === 100) + '<div class="pct">' + pr.pct + '%</div></summary><div class="phase-body">';
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
    return '<details class="task"><summary>' + chk + '<span class="tid">' + esc(t.id) + '</span><span class="ttitle ' + t.status + '">' + esc(t.title) + badges(t) + '</span><span class="est">' + num(t.est) + ' h</span>' + statusPill(t.status) + '</summary>' + body + '</details>';
  }

  function viewBoard() {
    var b = state.board;
    var cur = currentPhase();
    var phaseId = b.phase === 'current' ? cur.id : b.phase;
    var list = TASKS.filter(function (t) {
      return (phaseId === 'all' || t.phase.id === phaseId) && (b.target === 'all' || t.target === b.target);
    });
    var h = '<p class="eyebrow">Plan</p><h1 class="page-title">Tablero</h1><p class="page-lead">Tareas por estado. Los estados se guardan en el código del proyecto y los cambia Claude al trabajar: si una tarea pasó a «En proceso», es porque se editó su archivo de datos. Toca una tarjeta para ver su historial, evidencias y comentarios.</p>';
    h += '<div class="filters"><div class="filter-group"><label class="filter-label" for="bPhase">Fase</label><select id="bPhase" data-action="board-phase"><option value="current"' + (b.phase === 'current' ? ' selected' : '') + '>Fase actual (' + esc(cur.id) + ')</option><option value="all"' + (b.phase === 'all' ? ' selected' : '') + '>Todas</option>' +
      phases.map(function (p) { return '<option value="' + p.id + '"' + (b.phase === p.id ? ' selected' : '') + '>' + esc(p.id + ' · ' + p.name) + '</option>'; }).join('') + '</select></div>' +
      '<div class="filter-group"><label class="filter-label" for="bTarget">Objetivo</label><select id="bTarget" data-action="board-target"><option value="all">Todos</option>' +
      targets.map(function (t) { return '<option value="' + esc(t) + '"' + (b.target === t ? ' selected' : '') + '>' + esc(t) + '</option>'; }).join('') + '</select></div></div>';
    h += '<div class="board">';
    STATUS_ORDER.forEach(function (st) {
      var cards = list.filter(function (t) { return t.status === st; });
      h += '<section class="col" aria-label="' + STATUS[st].label + '"><div class="col-head"><span class="s-' + st + '">' + STATUS[st].glyph + ' ' + STATUS[st].label + '</span><small>' + cards.length + '</small></div><div class="col-body">';
      if (!cards.length) h += '<div class="empty">Sin tareas</div>';
      cards.forEach(function (t) {
        h += '<a class="kcard" href="#/tarea/' + esc(t.id) + '"><div>' + esc(t.title) + '</div><div class="meta"><span>' + esc(t.id) + '</span><span>' + num(t.est) + ' h</span><span class="' + targetClass(t.target) + '">' + esc(t.target) + '</span>' + badges(t) + '</div></a>';
      });
      h += '</div></section>';
    });
    return h + '</div>';
  }

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
    h += '<div class="doc-meta"><span class="chip">' + esc(t.id) + '</span>' + statusPill(t.status) + targetPill(t.target) + '<span class="chip">' + num(t.est) + ' h estimadas</span></div>';
    h += '<div class="task-layout"><div>';
    h += '<div class="card"><dl class="task-dl"><dt>Descripción</dt><dd>' + (t.desc ? esc(t.desc) : '—') + '</dd><dt>Listo cuando</dt><dd>' + (t.done_when ? esc(t.done_when) : '—') + '</dd></dl></div>';
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
        h += '<li><span class="tid">' + esc(x.at) + '</span><div>' + statusPill(x.to) + '</div><div class="tl-from">desde ' + esc(STATUS[x.from].label) + (x.by ? ' · ' + esc(AUTHOR[x.by] || x.by) : '') + '</div><p>' + esc(x.note) + '</p></li>';
      });
      h += '</ol>';
    }
    h += '</aside></div>';
    return h;
  }

  function viewDoc(id) {
    var d = H.docs.filter(function (x) { return x.id === id; })[0];
    if (!d) return '<div class="notice">No existe el documento «' + esc(id) + '».</div>';
    var r = mdToHtml(d.md);
    var h = '<div class="doc-layout"><article class="prose">';
    h += '<div class="doc-meta"><span class="chip">' + esc(d.group) + '</span><span class="chip" title="Acordado">✅ ' + d.counts.ok + '</span><span class="chip" title="Propuesta">🟡 ' + d.counts.prop + '</span><span class="chip" title="Abierto">❓ ' + d.counts.open + '</span><a class="chip" href="../docs/' + esc(d.id) + '.md" target="_blank" rel="noopener">Abrir archivo .md</a></div>';
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
        h += '<div class="result"><a class="r-title" href="#/tarea/' + esc(e.task.id) + '">' + esc(e.task.id) + ' · ' + highlight(e.task.title, tokens) + '</a><span class="r-where">Tarea · ' + esc(e.task.phase.id) + ' · ' + STATUS[e.task.status].label + '</span>' + (e.task.desc ? '<p>' + highlight(e.task.desc, tokens) + '</p>' : '') + '</div>';
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
  function render() {
    var r = parseHash();
    var key = r.segs[0] || '';
    var html, title = H.config.title;
    var anchor = null;
    var activeKey = key;
    switch (key) {
      case '': html = viewHome(); title += ' · Inicio'; break;
      case 'roadmap': html = viewRoadmap(); title += ' · Roadmap'; break;
      case 'tablero': html = viewBoard(); title += ' · Tablero'; break;
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
    main.innerHTML = html;
    document.title = title;
    setActive(activeKey);
    closeMenu();
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
    if (act === 'rm-target') { state.rm.target = val; render(); }
    else if (act === 'rm-hide') { state.rm.hideDone = !state.rm.hideDone; render(); }
    else if (act === 'art-cat') { state.art.cat = val; render(); }
    else if (act === 'open-img') { openLightbox(+el.getAttribute('data-index'), el); }
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
    if (act === 'board-phase') { state.board.phase = el.value; render(); }
    else if (act === 'board-target') { state.board.target = el.value; render(); }
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
  window.addEventListener('hashchange', render);

  /* ---------- inicio ---------- */
  $('#gen').textContent = 'Actualizado ' + H.generated;
  document.title = H.config.title + ' · ' + H.config.subtitle;
  buildNav();
  render();
})();
