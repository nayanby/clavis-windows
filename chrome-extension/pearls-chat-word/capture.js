/* Read rendered chat content only. Never execute, click or submit chat content. */
(() => {
  const VERSION='1.0.6';
  if (globalThis.PearlsCapture?.version===VERSION) return;
  const SKIP = 'button,script,style,noscript,textarea,input,select,nav,[role="button"],[data-pearls-ignore],[data-markdown-copy="exclude"],.sr-only,[aria-hidden="true"]';
  const clean = value => String(value || '').replace(/\u00a0/g, ' ');
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  function site() {
    const host = location.hostname;
    if (host === 'chatgpt.com' || host === 'chat.openai.com') return 'chatgpt';
    if (host === 'claude.ai') return 'claude';
    if (host === 'gemini.google.com') return 'gemini';
    throw Error('Open a ChatGPT, Claude or Gemini conversation and click the extension icon there.');
  }
  function hidden(element) {
    return element.matches(SKIP) || element.hidden || element.closest('[hidden],[aria-hidden="true"]');
  }
  function inlines(node, format = {}) {
    if (node.nodeType === Node.TEXT_NODE) return [{ text: clean(node.nodeValue), ...format }];
    if (node.nodeType !== Node.ELEMENT_NODE || hidden(node)) return [];
    const tag = node.tagName.toLowerCase();
    if (tag === 'br') return [{ text: '\n', ...format }];
    if (tag === 'img') return [{ text: node.alt || '[Image]', ...format }];
    // KaTeX duplicates its visible and accessible representations. Preserve LaTeX once.
    if (node.matches('.katex,.MathJax,mjx-container,math')) {
      const latex = node.querySelector('annotation[encoding="application/x-tex"]')?.textContent;
      return [{ text: latex || node.getAttribute('aria-label') || node.textContent, ...format, math: true }];
    }
    const next = { ...format };
    if (tag === 'strong' || tag === 'b') next.bold = true;
    if (tag === 'em' || tag === 'i') next.italic = true;
    if (tag === 'u') next.underline = true;
    if (tag === 'del' || tag === 's') next.strike = true;
    if (tag === 'code') next.code = true;
    if (tag === 'mark') next.highlight = true;
    if (tag === 'sub') next.sub = true;
    if (tag === 'sup') next.sup = true;
    if (tag === 'a') {
      try { const href = new URL(node.getAttribute('href'), location.href); if (/^(https?:|mailto:)$/.test(href.protocol)) next.href = href.href; } catch {}
    }
    return [...node.childNodes].flatMap(child => inlines(child, next));
  }
  const textOf = runs => runs.map(run => run.text).join('');
  function blocks(parent) {
    const output = [];
    let pending = [];
    function flush() {
      if (textOf(pending).trim()) output.push({ type: 'paragraph', runs: pending });
      pending = [];
    }
    for (const node of parent.childNodes) {
      if (node.nodeType === Node.TEXT_NODE) { if (node.textContent.trim()) pending.push(...inlines(node)); continue; }
      if (node.nodeType !== Node.ELEMENT_NODE) continue;
      // Generated pictures are often wrapped in a preview button/link.
      if (node.matches('button,[role="button"]') && !node.closest('[data-pearls-ignore],[hidden],[aria-hidden="true"]')) {
        flush();
        for (const img of node.querySelectorAll('img')) if (!hidden(img)) output.push(image(img));
        continue;
      }
      if (hidden(node)) continue;
      const tag = node.tagName.toLowerCase();
      if (/^h[1-6]$/.test(tag)) { flush(); output.push({ type: 'heading', level: Number(tag[1]), runs: inlines(node) }); }
      else if (tag === 'p') {
        flush();
        if (node.querySelector('img') && !node.textContent.trim()) {
          for (const img of node.querySelectorAll('img')) output.push(image(img));
          continue;
        }
        const runs = inlines(node);
        const words = runs.filter(run => run.text.trim());
        const text = textOf(runs).trim();
        const heading = words.length && words.every(run => run.bold) && text.length < 100 && text.split(/\s+/).length <= 12 && !/[.!?;:]$/.test(text);
        if (text) output.push({ type: heading ? 'heading' : 'paragraph', ...(heading ? { level: 6, inferred: true } : {}), runs });
        // Inline image positions are preserved as image paragraphs after the caption text.
        for (const img of node.querySelectorAll('img')) output.push(image(img));
      }
      else if (tag === 'ul' || tag === 'ol') {
        flush();
        output.push({ type: 'list', ordered: tag === 'ol', start: Number(node.getAttribute('start')) || 1,
          format: node.getAttribute('type') || '1', items: [...node.children].filter(child => child.tagName === 'LI').map(li => ({ value: li.hasAttribute('value') ? Number(li.getAttribute('value')) : null, blocks: blocks(li) })) });
      }
      else if (tag === 'table') {
        flush();
        output.push({ type: 'table', rows: [...node.rows].map(row => ({ cells: [...row.cells].map(cell => ({ header: cell.tagName === 'TH', colspan: cell.colSpan || 1, rowspan: cell.rowSpan || 1, blocks: blocks(cell) })) })) });
      }
      else if (tag === 'pre') { flush(); output.push({ type: 'code', text: clean((node.querySelector('code') || node).textContent) }); }
      else if (tag === 'blockquote') { flush(); output.push({ type: 'quote', blocks: blocks(node) }); }
      else if (tag === 'img') { flush(); output.push(image(node)); }
      else if (tag === 'svg') {
        flush();
        const bytes = new TextEncoder().encode(new XMLSerializer().serializeToString(node));
        const base64 = btoa(Array.from(bytes, byte => String.fromCharCode(byte)).join(''));
        output.push({ type: 'image', src: 'data:image/svg+xml;base64,' + base64,
          alt: node.getAttribute('aria-label') || node.querySelector('title')?.textContent || 'Diagram',
          width: node.viewBox?.baseVal.width || node.width?.baseVal.value || 640,
          height: node.viewBox?.baseVal.height || node.height?.baseVal.value || 480 });
      }
      else if (tag === 'hr') { flush(); output.push({ type: 'rule' }); }
      else if (/^(div|section|article|main|figure|figcaption|details|summary|dl|dt|dd|li)$/.test(tag)) { flush(); output.push(...blocks(node)); }
      else if (node.querySelector('img')) { flush(); output.push(...blocks(node)); }
      else pending.push(...inlines(node));
    }
    flush(); return output;
  }
  function image(img) {
    return { type: 'image', src: img.currentSrc || img.src, alt: img.alt || 'Image', width: img.naturalWidth || img.width || 640, height: img.naturalHeight || img.height || 480 };
  }
  function contentImages(items) {
    return items.filter(item => {
      if (item.type === 'image' && /(?:\/s2\/favicons|\/favicon(?:V2)?(?:[?.\/]|$))/i.test(item.src || '')) return false;
      if(item.blocks)item.blocks=contentImages(item.blocks);
      for(const entry of item.items||[])entry.blocks=contentImages(entry.blocks);
      for(const row of item.rows||[])for(const cell of row.cells)cell.blocks=contentImages(cell.blocks);
      return true;
    });
  }
  function entries(provider) {
    let candidates = [];
    if (provider === 'chatgpt') {
      // ChatGPT's newer Work UI uses search units and response-body attributes
      // instead of data-message-author-role. Support both DOM generations.
      const selector='[data-message-author-role="user"],[data-message-author-role="assistant"],[data-chatgpt-search-unit-key],[data-response-body],[data-markdown-text-style="assistant-message"],[data-turn="user"],[data-turn="assistant"]';
      candidates = [...document.querySelectorAll(selector)].map(node => {
        const key=node.getAttribute('data-chatgpt-search-unit-key')||'';
        const role=node.getAttribute('data-message-author-role') || node.getAttribute('data-turn') || /:(user|assistant)$/.exec(key)?.[1] || (node.matches('[data-response-body],[data-markdown-text-style="assistant-message"]')?'assistant':null);
        const root=node.querySelector('[data-response-body],[data-markdown-text-style="assistant-message"],.markdown,.prose,[class*="whitespace-pre-wrap"]')||node;
        return {node,role,root,id:node.getAttribute('data-message-id')||root.getAttribute('data-response-body')||node.getAttribute('data-response-body')||node.getAttribute('data-chatgpt-search-message-ids')?.trim().split(/\s+/)[0]||node.closest('[data-message-id]')?.getAttribute('data-message-id')||key||node.closest('article[data-testid]')?.getAttribute('data-testid')};
      }).filter(entry=>entry.role==='user'||entry.role==='assistant');
    } else if (provider === 'claude') {
      candidates = [...document.querySelectorAll('[data-testid="user-message"],[data-testid="assistant-message"],.font-claude-response')].map(node => ({
        node, root: node.querySelector('.standard-markdown,.markdown,.prose') || node,
        role: node.matches('[data-testid="user-message"]') ? 'user' : 'assistant',
        id: node.closest('[data-message-id]')?.getAttribute('data-message-id') || node.getAttribute('data-message-id')
      }));
    } else if (provider === 'gemini') {
      candidates = [...document.querySelectorAll('user-query,model-response')].map(node => ({
        node, root: node.querySelector('.model-response-text,.query-text,.markdown') || node,
        role: node.tagName.toLowerCase() === 'user-query' ? 'user' : 'assistant',
        id: node.getAttribute('data-message-id') || node.getAttribute('id')
      }));
    }
    // Retain only outermost message candidates; nested adapter matches are duplicates.
    return candidates.filter(item => !candidates.some(other => other !== item && other.node.contains(item.node))).filter(item => !item.node.closest('[hidden],[aria-hidden="true"]'));
  }
  function isStreaming(provider) {
    const selectors = {
      chatgpt: '[data-testid="stop-button"],button[aria-label="Stop generating"]',
      claude: '[data-is-streaming="true"],button[aria-label="Stop response"],button[aria-label="Stop generating"]',
      gemini: 'button[aria-label="Stop response"],button[aria-label="Stop generating"],.stop-button:not([hidden])'
    };
    return [...document.querySelectorAll(selectors[provider])].some(node => node.getClientRects().length && !node.closest('[hidden],[aria-hidden="true"]'));
  }
  function snapshot(provider = site()) {
    if (isStreaming(provider)) throw Error('The response is still being generated. Wait for it to finish, then refresh.');
    const messages = entries(provider).map((entry, index) => ({
      id: entry.id || null, role: entry.role, blocks: contentImages(blocks(entry.root)),
      preview: entry.root.innerText?.trim().slice(0, 240) || entry.root.textContent.trim().slice(0, 240), index
    })).filter(message => message.blocks.length);
    if (!messages.length) throw Error('No chat messages were found. Open a conversation and let it finish loading. The site may also have changed its page layout.');
    const warnings = entries(provider).some(entry => entry.root.querySelector('canvas,video,iframe')) ? ['This response contains an interactive canvas, video or embedded frame. Its interactive content is not included in the Word file.'] : [];
    return { provider, title: document.title.replace(/\s*[-–|]\s*(ChatGPT|Claude|Gemini).*$/i, '').trim(), url: location.href, messages, warnings };
  }
  function scroller(provider) {
    const first = entries(provider)[0]?.node;
    for (let node = first?.parentElement; node; node = node.parentElement) {
      const style = getComputedStyle(node);
      if (/(auto|scroll)/.test(style.overflowY) && node.scrollHeight > node.clientHeight + 80) return node;
    }
    return document.scrollingElement;
  }
  const messageKey = message => message.id ? message.role + ':' + message.id : message.role + ':' + JSON.stringify(message.blocks);
  // Sequence overlap, rather than a Set of text, preserves repeated identical turns.
  function merge(left, right) {
    if (!left.length) return right.slice();
    if (!right.length) return left;
    const a = left.map(messageKey), b = right.map(messageKey);
    const contained = a.findIndex((_, index) => b.every((key, j) => a[index + j] === key));
    if (contained >= 0) return left;
    let overlap = Math.min(a.length, b.length);
    while (overlap > 0 && !a.slice(-overlap).every((key, j) => key === b[j])) overlap--;
    if (!overlap) {
      // Without an overlapping turn we cannot prove chronology for a virtualized page.
      throw Error('The page replaced its messages while scrolling. Export stopped to avoid an incomplete chat. Zoom out or expand the conversation history, then retry.');
    }
    return left.concat(right.slice(overlap));
  }
  async function conversation(onProgress = () => {}) {
    const provider = site(), container = scroller(provider), originalTop = container.scrollTop;
    let collected = [], topReached = false, bottomReached = false;
    try {
      // Let the site's own history loading run; no hidden endpoints or credentials.
      for (let i = 0; i < 100; i++) {
        container.scrollTop = 0;
        await sleep(350);
        const before = JSON.stringify(snapshot(provider).messages.map(messageKey));
        await sleep(400);
        const after = JSON.stringify(snapshot(provider).messages.map(messageKey));
        if (container.scrollTop <= 2 && before === after && i >= 2) { topReached = true; break; }
      }
      if (!topReached) throw Error('The start of the chat could not be reached. Expand earlier messages in the chat and retry.');
      let result;
      for (let i = 0; i < 250; i++) {
        result = snapshot(provider);
        collected = merge(collected, result.messages);
        onProgress({messages:collected.length});
        if (JSON.stringify(collected).length > 18000000) throw Error('This chat is too large for one export. Export individual responses instead.');
        const atBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - 5;
        if (atBottom) {
          await sleep(600);
          const final = snapshot(provider);
          collected = merge(collected, final.messages);
          if (container.scrollTop + container.clientHeight >= container.scrollHeight - 5) { bottomReached = true; break; }
        }
        container.scrollTop += Math.max(200, container.clientHeight * 0.6);
        await sleep(220);
      }
      if (!bottomReached) throw Error('The full chat could not be traversed. Export stopped instead of saving a partial conversation.');
      result.messages = collected;
      result.warnings.push('Exports the active conversation branch and history the site exposes in its page. Collapsed content, separate artifacts/canvases and alternative response branches are not included.');
      return result;
    } finally { container.scrollTop = originalTop; }
  }
  async function resolveImages(result) {
    const cache = new Map();
    async function walk(items) {
      for (const item of items || []) {
        if (item.type === 'image') {
          try {
            if (!cache.has(item.src)) cache.set(item.src, (async () => {
              const url = new URL(item.src, location.href);
              if (!/^(https?:|data:|blob:)$/.test(url.protocol)) throw Error('Unsupported image URL');
              let blob;
              try {
                const response = await fetch(url.href, { credentials: 'same-origin', signal: AbortSignal.timeout(15000) });
                if (!response.ok) throw Error('Image unavailable');
                blob = await response.blob();
              } catch(error) {
                // Extension fetch can read provider image CDNs that deny page CORS.
                if (url.protocol !== 'https:' || !globalThis.chrome?.runtime?.sendMessage) throw error;
                const resolved = await chrome.runtime.sendMessage({type:'PEARLS_FETCH_IMAGE',url:url.href});
                if (!resolved?.data) throw Error(resolved?.error || 'Image unavailable');
                blob = await (await fetch(resolved.data)).blob();
              }
              if (!/^image\/(png|jpeg|gif|webp|svg\+xml)/i.test(blob.type) || blob.size > 8000000) throw Error('Image format or size unsupported');
              const bitmap = await createImageBitmap(blob);
              const scale = Math.min(1, 1800 / Math.max(bitmap.width, bitmap.height));
              const canvas = document.createElement('canvas'); canvas.width = Math.max(1, Math.round(bitmap.width * scale)); canvas.height = Math.max(1, Math.round(bitmap.height * scale));
              canvas.getContext('2d').drawImage(bitmap, 0, 0, canvas.width, canvas.height); bitmap.close();
              return canvas.toDataURL('image/png');
            })());
            item.data = await cache.get(item.src);
          } catch { result.warnings.push('An image could not be embedded: ' + item.alt + '. Its caption and source link are retained.'); }
        }
        if (item.blocks) await walk(item.blocks);
        for (const entry of item.items || []) await walk(entry.blocks);
        for (const row of item.rows || []) for (const cell of row.cells) await walk(cell.blocks);
      }
    }
    for (const message of result.messages) await walk(message.blocks);
    result.warnings = [...new Set(result.warnings)];
    return result;
  }
  globalThis.PearlsCapture = { version:VERSION, snapshot, conversation, resolveImages, merge, blocks,
    responseTargets: () => entries(site()).filter(entry => entry.role === 'assistant'),
    isGenerating: () => isStreaming(site())
  };
})();
