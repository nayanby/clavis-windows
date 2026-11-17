(() => {
  const $ = id => document.getElementById(id);
  const tabId = Number(new URL(location.href).searchParams.get('tab'));
  let chat = null, busy = false;
  const status = (text, error = false) => { $('status').textContent = text; $('status').classList.toggle('error', error); };
  function setBusy(value) {
    busy = value;
    $('all').disabled = value || !chat;
    $('single').disabled = value || !chat?.messages.some(message => message.role === 'assistant');
    $('refresh').disabled = value;
    $('response').disabled = value || !chat?.messages.some(message => message.role === 'assistant');
  }
  async function invoke(action, selectedId = null) {
    const results = await chrome.scripting.executeScript({ target: { tabId }, func: async (action, selectedId) => {
      try {
        const reader = globalThis.PearlsCapture;
        if (action === 'scan') return { value: reader.snapshot() };
        if (action === 'all') return { value: await reader.resolveImages(await reader.conversation()) };
        const data = reader.snapshot();
        const responses = data.messages.filter(message => message.role === 'assistant');
        const response = responses[selectedId];
        if (!response) throw Error('That response is no longer visible. Refresh responses and select it again.');
        data.messages = [response];
        return { value: await reader.resolveImages(data) };
      } catch (error) { return { error: error.message || String(error) }; }
    }, args: [action, selectedId] });
    const result = results[0]?.result;
    if (!result) throw Error('Could not read the chat tab. Reopen the extension from your conversation.');
    if (result.error) throw Error(result.error);
    return result.value;
  }
  async function scan() {
    if (busy) return;
    setBusy(true); status('Reading responses from your chat…');
    try {
      if (!Number.isInteger(tabId) || tabId <= 0) throw Error('Open a chat and click the extension icon there.');
      await chrome.scripting.executeScript({ target: { tabId }, files: ['capture.js'] });
      chat = await invoke('scan');
      $('source').textContent = ({ chatgpt: 'ChatGPT', claude: 'Claude', gemini: 'Gemini' }[chat.provider] || 'Chat') + ' · ' + chat.title;
      if (!$('title').value.trim()) $('title').value = chat.title || 'Conversation';
      const responses = chat.messages.filter(message => message.role === 'assistant');
      $('response').replaceChildren(...responses.map((message, index) => {
        const option = document.createElement('option'); option.value = String(index);
        option.textContent = 'Response ' + (index + 1) + ' — ' + (message.preview || 'Response').slice(0, 90); return option;
      }));
      $('response').value = String(Math.max(0, responses.length - 1)); preview();
      status(responses.length + ' assistant response' + (responses.length === 1 ? '' : 's') + ' currently loaded. Entire-chat export will traverse the chat history.');
    } catch (error) { chat = null; status(error.message, true); }
    finally { setBusy(false); }
  }
  function preview() {
    const response = chat?.messages.filter(message => message.role === 'assistant')[Number($('response').value)];
    $('preview').textContent = response?.preview || 'No assistant responses found.';
  }
  const safeName = text => String(text).replace(/[<>:"/\\|?*\u0000-\u001f]/g, ' ').replace(/[. ]+$/g, '').trim().slice(0, 130) || 'Conversation';
  async function download(mode) {
    if (busy) return;
    const index = Number($('response').value);
    const previous = mode === 'single' ? chat.messages.filter(message => message.role === 'assistant')[index] : null;
    setBusy(true); $('warnings').hidden = true;
    status(mode === 'all' ? 'Collecting chat history. Keep this tab open; the chat will scroll temporarily…' : 'Preparing the selected response…');
    try {
      const data = await invoke(mode, index);
      // Refuse a response that shifted when the page loaded additional messages.
      if (previous && (previous.id ? data.messages[0].id !== previous.id : data.messages[0].preview !== previous.preview)) throw Error('The response order changed. Refresh responses, then select the response again.');
      const [template, profile] = await Promise.all([
        fetch(chrome.runtime.getURL('template/base.docx')).then(response => { if (!response.ok) throw Error('Word template could not load.'); return response.arrayBuffer(); }),
        fetch(chrome.runtime.getURL('template/profile.json')).then(response => { if (!response.ok) throw Error('Template settings could not load.'); return response.json(); })
      ]);
      const title = $('title').value.trim() || data.title || 'Conversation';
      const generated = await PearlsWord.create(data, { title, includePrompts: mode === 'single' || $('prompts').checked, single: mode === 'single', templateBytes: template, profile });
      const url = URL.createObjectURL(new Blob([generated.bytes], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' }));
      const filename = safeName(title) + (mode === 'single' ? ' - Response ' + (index + 1) : '') + '.docx';
      const downloadId = await chrome.downloads.download({ url, filename, saveAs: true });
      const listener = delta => {
        if (delta.id !== downloadId || !delta.state) return;
        if (delta.state.current === 'complete' || delta.state.current === 'interrupted') {
          URL.revokeObjectURL(url); chrome.downloads.onChanged.removeListener(listener);
          status(delta.state.current === 'complete' ? 'Saved ' + filename : 'The download was cancelled or interrupted.', delta.state.current !== 'complete');
        }
      };
      chrome.downloads.onChanged.addListener(listener);
      setTimeout(() => { URL.revokeObjectURL(url); chrome.downloads.onChanged.removeListener(listener); }, 300000);
      const warnings = [...new Set([...(data.warnings || []), ...generated.warnings])];
      if (warnings.length) { $('warnings').textContent = warnings.join('\n\n'); $('warnings').hidden = false; }
      status('Word document prepared. Choose where to save it.');
    } catch (error) { status(error.message || String(error), true); }
    finally { setBusy(false); }
  }
  $('refresh').addEventListener('click', scan);
  $('response').addEventListener('change', preview);
  $('all').addEventListener('click', () => download('all'));
  $('single').addEventListener('click', () => download('single'));
  scan().then(() => {
    if (!chat) return;
    const params = new URL(location.href).searchParams;
    const mode = params.get('mode');
    if (mode === 'all') { download('all'); return; }
    if (mode !== 'single') return;
    const responses = chat.messages.filter(message => message.role === 'assistant');
    const id = params.get('responseId');
    const index = id ? responses.findIndex(message => message.id === id) : Number(params.get('index'));
    const selected = responses[index];
    let hash = 2166136261;
    for (const char of selected?.preview || '') { hash ^= char.codePointAt(0); hash = Math.imul(hash, 16777619); }
    if (!selected || (params.get('fingerprint') && params.get('fingerprint') !== (hash >>> 0).toString(16))) {
      status('The chat changed after you clicked. Refresh responses and choose the response to download.', true); return;
    }
    $('response').value = String(index); preview(); download('single');
  });
})();
