// Arnés mínimo para renderizar el hub sin navegador (lo usan las pruebas de tools/ci).
// Uso: node hub_harness.js <hub.json> <hash> [accion=valor ...]
// Carga studio/hub/app.js con un DOM de mentira, aplica los clics pedidos (data-action) y escribe
// en la salida estándar el HTML de <main> como JSON.
'use strict';
const fs = require('fs');
const path = require('path');
const [, , hubPath, hash, ...clicks] = process.argv;

function element() {
  return {
    innerHTML: '', textContent: '', hidden: false, className: '', value: '', style: {},
    classList: { add() {}, remove() {}, contains() { return false; } },
    setAttribute() {}, getAttribute() { return null; }, addEventListener() {}, focus() {}, appendChild() {},
    querySelector() { return null; }, querySelectorAll() { return []; }, closest() { return null; }, remove() {}
  };
}
const byId = {};
const get = (id) => byId[id] || (byId[id] = element());
const handlers = {};
global.window = {
  HUB: JSON.parse(fs.readFileSync(hubPath, 'utf8')), scrollY: 0, scrollTo() {},
  addEventListener() {}, print() {}
};
global.location = { hash: hash || '' };
global.document = {
  body: element(), createElement: element,
  getElementById: get,
  querySelector: (sel) => (sel[0] === '#' ? get(sel.slice(1)) : null),
  querySelectorAll: () => [],
  addEventListener: (type, fn) => { (handlers[type] = handlers[type] || []).push(fn); }
};
const file = path.join(__dirname, '..', '..', '..', 'studio', 'hub', 'app.js');
(0, eval)(fs.readFileSync(file, 'utf8'));

for (const c of clicks) {
  const i = c.indexOf('=');
  const attrs = { 'data-action': c.slice(0, i), 'data-value': c.slice(i + 1) };
  const target = { closest: (sel) => (sel === '[data-action]' ? { getAttribute: (n) => attrs[n] } : null) };
  (handlers.click || []).forEach((fn) => fn({ target }));
}
process.stdout.write(JSON.stringify({ html: get('main').innerHTML, sidebar: get('sidebar').innerHTML }));
