/* Exercise the shipped reader method and desktop override together. */
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'assets/app.html'), 'utf8');
const method = html.match(/  getListInfo\(p, merged\)\{[\s\S]*?\n  \}/)[0];
const viewer = fs.readFileSync(path.join(root, 'assets/vendor/consumer-viewer.js'), 'utf8');
const override = viewer.slice(0, viewer.indexOf('/* Align bullets'));
const context = vm.createContext({});
vm.runInContext('class DocxPrototype {' + method + '}\n' + override + `
  globalThis.reader = new DocxPrototype();
  reader.numberingMap = new Map([['7','10']]);
  reader.abstractMap = new Map([['10',{levels:new Map([[0,{numFmt:'bullet'}],[1,{numFmt:'decimal'}]])}]]);
  reader.resolveStyle = id => ({p: id === 'List' ? {numId:'7',ilvl:0} : {numId:'0'}});
`, context);
const reader = context.reader;
for (const location of ['body', 'table']) {
  assert.equal(reader.getListInfo(null, {props:{numId:'0'},styleId:'List'}), null, location+' explicit cancellation');
  assert.equal(reader.getListInfo(null, {props:{},styleId:'Normal'}), null, location+' inherited cancellation');
  assert.equal(reader.getListInfo(null, {props:{}}), null, location+' plain paragraph');
  assert.equal(reader.getListInfo(null, {props:{},styleId:'List'}).lvl.numFmt, 'bullet', location+' genuine bullet');
  assert.equal(reader.getListInfo(null, {props:{numId:'7',ilvl:1}}).lvl.numFmt, 'decimal', location+' genuine numbered list');
}
console.log('PASS: normal text, cancelled lists, genuine bullets and numbered lists');
