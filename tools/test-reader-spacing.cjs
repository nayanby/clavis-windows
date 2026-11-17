const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('assets/vendor/consumer-viewer.js', 'utf8');
const patch = source.slice(0, source.indexOf('/* Word numId=0'));
let baseCalls = 0;
const context = {
  CNL_PREFS_DEFAULT: { lineScale: 23, paraScale: 1600, snapshotLineScale: 22, snapshotParaScale: 1600 },
  cnlPrefs: { paraScale: 2200 },
  cnlConsumerParagraphs: () => { baseCalls++; },
  getComputedStyle: () => ({ fontSize: '16px' }),
};
vm.createContext(context);
vm.runInContext(patch, context);
assert.equal(context.CNL_PREFS_DEFAULT.lineScale / 16, 1.375);
assert.equal(context.CNL_PREFS_DEFAULT.paraScale / 1600, 1.375);
assert.equal(context.CNL_PREFS_DEFAULT.snapshotParaScale, 1600);
function block(level, { bullet = true, numberedNext = true, table = false } = {}) {
  const styles = {};
  return {
    styles,
    closest: () => table,
    querySelector: () => ({ getAttribute: () => level, querySelector: () => bullet }),
    nextElementSibling: { matches: () => true, querySelector: () => numberedNext },
    style: { setProperty: (name, value) => { styles[name] = value; } },
  };
}
const cases = [block('0'), block('1'), block('2'), block('0', { bullet: false }),
  block('0', { numberedNext: false }), block('0', { table: true })];
context.cnlConsumerParagraphs({ querySelectorAll: () => cases });
assert.equal(baseCalls, 1);
assert.equal(cases[0].styles['padding-bottom'], '11px');
assert.equal(cases[1].styles['padding-bottom'], '11px');
cases.slice(2).forEach(item => assert.deepEqual(item.styles, {}));
context.cnlPrefs.paraScale = 1600;
context.cnlConsumerParagraphs({ querySelectorAll: () => [cases[0]] });
assert.equal(cases[0].styles['padding-bottom'], '8px');
console.log('Reader defaults and scaled bullet-to-number gaps passed; deeper lists and tables preserved.');
