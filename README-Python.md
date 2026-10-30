# Clavis Windows — Python edition 0.2.5

Run **Clavis.exe**. This is a Python application using pywebview and the installed Microsoft Edge WebView2 runtime. It contains no Electron host. The interface uses HTML/CSS/JavaScript, with native Python services for files, RSS, playback metadata, notes and BitTorrent downloads. A system WebView2 runtime is required.

Everything persistent stays in **Data** next to Clavis.exe: library.json, Books, annotations, transcripts, logs, backups and SessionPython (WebView2 browser storage). Imported originals are copied into Data/Books under readable book titles. Downloads use that same Books folder. Keep the entire app folder together when moving it. Existing Electron library data is compatible.

The app starts windowed at 70% of the screen working area, with 80% interface scaling. Sidebar and chapter/transcript lists scroll independently. Native file dialogs import EPUB/PDF/audio files or audiobook folders. Embedded audio chapters are read through Mutagen and FFmpeg. Offline English speech recognition can find approximate spoken headings for review. RSS includes subscription URLs only, with no bundled article snapshots. Opening a feed category or source fetches live content, bypasses caching and sorts all returned entries before keeping the newest 300 in memory for the current session. Fetched article content is not persisted in library.json.

Torrent downloads use libtorrent; they resume on request after reopening. Remove stops the job and keeps its files. Delete book sends unshared managed book files to the Recycle Bin after confirmation. Remove from library keeps files.

EPUB and PDF books can be read aloud with the built-in Kitten neural voice. Three narrators are available: Original, Hugo and a deeper male voice. Listen starts at the current chapter or page, with play/pause, back/forward 30 words, previous/next chapter, speed, a sleep timer, live sentence highlighting, optional text following and a saved listening position. Speech is synthesized on the computer into a local cache; the 44 MB voice is downloaded once on first use and checked against a published SHA-256 before installation. PDF listening skips pages without selectable text, and scanned PDFs report that OCR is needed.

Hover over the Clavis taskbar icon to show native preview buttons for seeking backward, play/pause, and seeking forward. They work while minimized, follow the skip interval in Settings, and are disabled until audio is loaded.

The shared pastel visual theme uses six transparent illustrations for library/imports, downloads, RSS, settings, search and bookmarks/journals, with matching matte surfaces in both themes. All original Clavis icons remain unchanged. The illustration prompts and preservation hashes are included in assets/pastel.

To build from source: install the dependencies in python_app/requirements.txt, run npm ci and npm run build, then python -m PyInstaller --noconfirm --distpath release/python-0.2.5 --workpath release/python-build Clavis-Python.spec. Node is only a frontend build dependency; it is not used by the executable.

Third-party notices are in licenses. FFmpeg retains its upstream license. The bundled speech model is supplied for offline recognition; narration uses sherpa-onnx and the KittenTTS v0.8 model (both Apache-2.0), loaded locally. The UI sanitizes article content before display.
