export function readingWidth(value) {
  const width = Number(value);
  return Number.isFinite(width) && width > 0 ? Math.max(8, Math.min(20, width)) : 20;
}

export function readingTheme(settings, dark = false) {
  return {
    body: {color: dark ? '#dddff3' : '#292664', background: dark ? '#252632' : '#ffffff',
      'font-family': 'Averia, Georgia, serif', 'font-size': `${settings.fontSize || 19}px`,
      'line-height': `${settings.lineHeight || 1.7}`, padding: `${settings.margin ?? 32}px !important`},
    p: {'line-height': `${settings.lineHeight || 1.7} !important`}
  };
}

export function readingFontCSS(base) {
  return [['regular',400,'normal'],['bold',700,'normal'],['italic',400,'italic'],['bold_italic',700,'italic']]
    .map(([file,weight,style]) => `@font-face{font-family:Averia;src:url("${new URL('averia_serif_libre_'+file+'.ttf',base).href}");font-weight:${weight};font-style:${style};font-display:swap}`).join('\n');
}

export function themeCSS(theme) {
  return Object.entries(theme).map(([selector, rules]) =>
    `${selector}{${Object.entries(rules).map(([key, value]) => `${key}:${value}`).join(';')}}`).join('\n');
}

// Match narration offsets to the original DOM without flattening its markup.
// Preparation removes soft hyphens, joins wrapped words and normalizes whitespace.
export function markSentences(root, text, chapter) {
  const document = root.ownerDocument;
  const walker = document.createTreeWalker(root, 4);
  const nodes = [];
  while (walker.nextNode()) {
    if (!walker.currentNode.parentElement.closest('script,style,noscript,svg')) nodes.push(walker.currentNode);
  }
  const significant = char => !/[\s\u00ad]/u.test(char);
  const source = [];
  for (const node of nodes) {
    for (let offset = 0; offset < node.data.length;) {
      const char = String.fromCodePoint(node.data.codePointAt(offset));
      if (significant(char) && !(char === '-' && /^-\r?\n/.test(node.data.slice(offset))))
        source.push({node, offset, end: offset + char.length, char});
      offset += char.length;
    }
  }
  const canonical = Array.from(text);
  const expected = canonical.slice(chapter.start, chapter.end).filter(significant).join('');
  if (source.map(item => item.char).join('') !== expected) return [];
  let cursor = 0, sentence = 0;
  const pieces = new Map();
  for (let offset = chapter.start; offset < chapter.end; offset++) {
    if (!significant(canonical[offset])) continue;
    const item = source[cursor++];
    while (sentence < chapter.sentences.length && offset >= chapter.sentences[sentence][1]) sentence++;
    if (sentence >= chapter.sentences.length || offset < chapter.sentences[sentence][0]) continue;
    const list = pieces.get(item.node) || [];
    const last = list.at(-1);
    if (last?.sentence === sentence) last.end = item.end;
    else list.push({start: item.offset, end: item.end, sentence});
    pieces.set(item.node, list);
  }
  const groups = chapter.sentences.map(() => []);
  for (const [node, parts] of pieces) {
    const fragment = document.createDocumentFragment();
    let offset = 0;
    for (const part of parts) {
      fragment.append(document.createTextNode(node.data.slice(offset, part.start)));
      const span = document.createElement('span');
      span.className = 'listen-sentence';
      span.textContent = node.data.slice(part.start, part.end);
      groups[part.sentence].push(span);
      fragment.append(span);
      offset = part.end;
    }
    fragment.append(document.createTextNode(node.data.slice(offset)));
    node.replaceWith(fragment);
  }
  return groups;
}
