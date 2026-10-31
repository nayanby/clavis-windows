# Clavis for Windows

**Current release: Python 0.2.0.** See [README-Python.md](README-Python.md) for the current architecture, storage and build instructions. The delivered app now uses Python + pywebview + Edge WebView2, packaged with PyInstaller. Keep `Clavis.exe` and its `_internal` directory together. The Electron notes below describe the archived 0.1.x implementation.

A self-contained Windows desktop port based on the supplied Clavis Android project at `Audiobook/Reson`. Uses the original home artwork, Averia font and indigo palette. The Android project is unchanged.

## Run

Open `Clavis.exe` in the delivered application folder. Keep its supporting files and `resources` folder beside it. An optional `Clavis-Setup-0.1.4.exe` installer is also provided.

The interface opens at 80% scale in a normal window occupying 70% of the primary display’s work area.

## All data stays beside the app

Clavis creates a `Data` folder beside `Clavis.exe`:

| Location | Contents |
| --- | --- |
| `Data/Books/<actual book or folder name>` | Both imported EPUB/PDF/audio copies and downloaded books, in readable named folders |
| `Data/library.json` | Library, subscriptions, bookmarks, progress, settings and journal entries |
| `Data/ink` | PDF pen/highlighter/underline strokes |
| `Data/feed-cache` | Latest entries per news, article and podcast source, kept for offline reading |
| `Data/articles` | Extracted story text, reused for six hours |
| `Data/feed-activity.json` | Local count of how often each story is opened, used by Popular ordering |
| `Data/transcripts` | Cached offline audio transcription |
| `Data/Session` | Desktop browser cache, IndexedDB and speech-model cache |
| `Data/Logs`, `Data/CrashDumps` | App diagnostics |

Original imports are copied, not moved. Keep the whole app folder together when moving it to another location; library references inside `Data` are rebased on startup. Choose a writable folder. Running from a read-only directory is unsupported. Test runs use a separate profile under the source project's `test-output` folder.

Existing app-owned copies in the old `Library` and `Downloads` locations migrate to `Books` on startup, with progress, bookmarks and transfer paths retained. Disc subfolders and original filenames are retained. Names that Windows does not allow are sanitized; duplicate book names receive a readable `(2)` suffix. A magnet without a display name uses `New download` until completion, then receives its torrent name.

Removing a book from the library keeps its copied files. The separate file-removal action confirms moving the copied files to the Windows Recycle Bin. Original source files are untouched. Exporting a journal or drawing writes to a location selected explicitly in the Save dialog.

## Included

- Seven home categories: EPUB, PDF, Audio Books, News, Podcasts, Articles and Journalling.
- EPUB pagination, font size, spacing, margins, outline, search, bookmarks, saved position and text highlights.
- PDF page rendering, lazy loading, page jump, outline, text search, zoom, saved position, bookmarks, pen, highlighter, straight underline and undo. Ink is saved separately from the PDF.
- Offline read-aloud for EPUB and PDF from the current chapter or page: Kitten neural voice, play/pause, 30-word skips, chapter navigation, speed, sleep timer, live sentence highlight, follow option and saved listening position. Scanned PDFs are identified and skipped.
- Audio file and folder import, nested folders and disc grouping, natural chapter order, nearby and embedded cover images.
- Audio playback with byte-range streaming, chapter-relative seeking, cross-chapter skips, undo seek, speed, volume, bookmarks, sleep timer, media keys, equalizer and voice gain.
- Automatic MP3 ID3 CHAP and M4B/MP4 chapter discovery, including Nero `chpl` and supported QuickTime chapter tracks. Existing books are checked on first playback. Detect chapters rechecks metadata and offers a cancellable offline English spoken-heading scan when markers are missing; results are reviewed before being applied.
- Bundled offline Vosk English speech model and live-text panel. Finalized text is cached. Speech is processed locally; no microphone or API key is used.
- One hundred and fifty Clavis Plus starter sources (50 News, 50 Articles, 50 Podcasts) with namespace-aware RSS/Atom parsing, a Popular / My list / Browse desk in each category, 17 topic filters, latest-or-popular ordering, per-source and combined streams, open-count ranking held on this computer, article text cached for six hours, saved stories that stay readable when a publisher refuses the refresh, cover-first cards that page through the story with arrows or a drag, source credits, Listen narration for any article, publisher links and separate podcast playback.
- Typed journal entries and a handwriting page with pen/highlighter/underline, undo, text export and PNG export.
- Magnet downloads with progress, speed and peer counts, pause/resume, persisted jobs and automatic completed-book import. Restarted active jobs wait paused until resumed. Removing a job keeps its files.
- Compact Now Playing: artwork, seek bar, transport, speed, sleep timer, bookmarks, volume and chapter tools fit in the window. Long chapter lists and live text scroll inside their own panels.
- Native Clavis executable, installer and taskbar icons.
- Light, dark and Windows themes.

## Differences from Android

This is a first desktop port, not complete feature parity. Scheduled themes, motion-triggered sleep resume and playback rewind-after-pause are not ported. Offline live text follows playback instead of prefetching text ahead; recognition accuracy and throughput depend on audio and hardware. Spoken chapter scans can be slow, miss headings, or suggest spoken references as headings; review before applying. Handwriting uses one page per journal entry rather than Android's full notebook system. PDF text selection and embedded annotation export are not implemented. Journal PDF attachments open via their publisher link. Online podcast directory search is not included; use the bundled directory or an RSS address. A category refreshes when you open it, then at most every thirty minutes; opening another category while one is refreshing queues it instead of dropping it. Stories whose publisher only publishes a preview are labelled and open on the website. Publisher access restrictions remain in effect.

The Windows installer is unsigned. This build has not been submitted to the Microsoft Store.

## Develop and build

Node.js 24 or later:

```powershell
npm install
npm start
npm test
npm run test:desktop
npm run dist
```

`npm run dist` produces an NSIS installer and an unpacked runnable app in `release`. The speech model archive is excluded from this repository. Offline speech recognition requires a separately supplied model at `assets/english-model.tar.gz`; `scripts/prepare-model.mjs` can prepare it from the supplied Android source.

## Credits and licenses

Original Android project identifies Audivo as its source lineage. Clavis home artwork and fonts are reused from the user-supplied project. Averia font OFL and Vosk Apache notices are in `licenses`. Reader engines in this Windows port are EPUB.js (BSD-2-Clause) and PDF.js (Apache-2.0); audio metadata uses music-metadata (MIT), article extraction uses Mozilla Readability (Apache-2.0) and jsdom (MIT), HTML sanitization uses DOMPurify (Apache-2.0/MPL-2.0), and torrents use WebTorrent (MIT). Packaged Node dependencies retain their license files. Electron ships Chromium and bundled third-party notices. MuPDF and Android libtorrent native libraries are not included in this desktop app.

FFmpeg is bundled for offline audio decoding during spoken chapter scans. Its binary license, build information and source links are included in `resources/ffmpeg-LICENSE.txt` and `resources/ffmpeg-README.txt`; see https://github.com/eugeneware/ffmpeg-static and https://ffmpeg.org/ for upstream information.
