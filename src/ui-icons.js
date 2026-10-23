// Crisp, font-independent controls drawn on a shared 24px optical grid.
const svg=body=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">${body}</svg>`;
export const uiIcons={
  play:svg('<path d="M8 5.5a.8.8 0 0 1 1.2-.7l10 6.5a.8.8 0 0 1 0 1.4l-10 6.5a.8.8 0 0 1-1.2-.7Z" fill="currentColor" stroke="none"/>'),
  pause:svg('<rect x="6" y="4.5" width="4" height="15" rx="1.1" fill="currentColor" stroke="none"/><rect x="14" y="4.5" width="4" height="15" rx="1.1" fill="currentColor" stroke="none"/>'),
  previous:svg('<path d="M5 5v14"/><path d="m18 5-10 7 10 7Z" fill="currentColor" stroke="none"/>'),
  next:svg('<path d="M19 5v14"/><path d="m6 5 10 7-10 7Z" fill="currentColor" stroke="none"/>'),
  back:svg('<path d="M4.5 9A8 8 0 1 1 4 15M4.5 4.5V9H9"/>'),
  forward:svg('<path d="M19.5 9A8 8 0 1 0 20 15m-.5-10.5V9H15"/>'),
  Home:svg('<path d="m3 10 9-7 9 7M5 9v11h5v-6h4v6h5V9"/>'),
  EPUB:svg('<path d="M12 5c-3-2-6-2-9-1v15c3-1 6-1 9 1 3-2 6-2 9-1V4c-3-1-6-1-9 1Zm0 0v15"/>'),
  PDF:svg('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Zm0 0v6h6M8 13h8M8 17h6"/>'),
  Audio:svg('<path d="M4 13v-2a8 8 0 0 1 16 0v2M6 12H4a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1Zm12 0h2a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-5a1 1 0 0 1 1-1Z"/>'),
  News:svg('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h4v4H7Zm8 0h2m-2 4h2M7 16h10"/>'),
  Podcasts:svg('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M6 10v1a6 6 0 0 0 12 0v-1m-6 7v4m-4 0h8"/>'),
  Journals:svg('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Zm0 0v6h6M8 13h8M8 17h8M8 9h2"/>'),
  Journalling:svg('<path d="M12 5H5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-7M15 4l5 5M9 15l1-5 8-8a1.4 1.4 0 0 1 2 0l2 2a1.4 1.4 0 0 1 0 2l-8 8Z"/>'),
  Downloads:svg('<path d="M12 3v12m-5-5 5 5 5-5M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>'),
  Kindle:svg('<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 10h8M8 14h5"/><circle cx="12" cy="19" r="1" fill="currentColor" stroke="none"/>'),
  Files:svg('<path d="M3 7V5a2 2 0 0 1 2-2h5l2 3h7a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Zm0 2h18"/>'),
  Settings:svg('<path d="m9 3-.6 2.3-2 .9L4.2 5.5 2 9.2l1.7 1.6v2.4L2 14.8l2.2 3.7 2.2-.7 2 .9L9 21h6l.6-2.3 2-.9 2.2.7 2.2-3.7-1.7-1.6v-2.4L22 9.2l-2.2-3.7-2.2.7-2-.9L15 3Z"/><circle cx="12" cy="12" r="3"/>')
};
export const transportIcon=(key,seconds)=>`<span class="transport-icon ${key==='back'||key==='forward'?'seek-icon':''}">${uiIcons[key]}${key==='back'||key==='forward'?`<span class="seek-seconds">${Number(seconds)||30}</span>`:''}</span>`;
