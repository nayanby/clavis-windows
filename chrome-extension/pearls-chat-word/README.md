# Pearls Chat to Word

Chrome extension for ChatGPT, Claude and Gemini. Download the active chat or one assistant response as a genuine editable `.docx` using your Clinical Notes Templatex styles. Runs locally; no API key, native app or server is required.

## Install

1. Extract the ZIP to a permanent folder. Keep the folder after installation.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode**.
4. Choose **Load unpacked** and select the folder containing `manifest.json`.
5. Pin **Pearls Chat to Word** from Chrome's Extensions menu.

The extension requests `activeTab`, `scripting`, `downloads` and access to the four supported chat origins. This lets it display its download toolbars automatically. It does not request cookies, history, all-site access or API credentials. No chat content is uploaded to a service.

## Use

Open your conversation on **chatgpt.com**, **chat.openai.com**, **claude.ai** or **gemini.google.com**. Reload an already-open chat after installing the extension. Wait for the response to finish.

A **Download entire chat** toolbar appears at the top of the chat. A **Download response** toolbar appears below each assistant response. Clicking either starts that export in a separate tab, then opens Chrome's save dialog. The exporter tab shows progress and any image or history limitations. Keep it open until the download starts.

Clicking the extension icon displays a compact white floating toolbar at the upper right of the chat, with exactly two Word icons: **Download response** and **Download entire chat**. Hover over an icon to see its label. The response icon uses the assistant response most visible in the current viewport, or the latest response if none is visible. Click the extension icon again to dock the toolbar back at the top of the chat. Opening the toolbar does not navigate away from the conversation. The control under each response is also a compact Word icon aligned to the right.

A progress panel appears immediately below the toolbar you clicked. It shows chat collection, template formatting, actual Word-file packaging progress, the save step and download completion or cancellation. Export buttons are disabled during that job to prevent overlapping exports. The chat stays in front while a background export tab generates the document.

The temporary export tab opens in the background only after you choose a download, then closes after the file is saved. Progress stays below the on-page toolbar.

- **Entire chat:** export the active conversation, optionally including your messages. Keep the exporter tab open while it traverses the chat.
- **One response:** select a response from the dropdown, check its preview and choose **Download this response**. Use **Refresh responses** after the chat changes.
- Edit the document title before downloading. Chrome asks where to save the Word file.

If earlier responses are not in the one-response dropdown, scroll to them in the chat first, or use Entire chat to collect the history. The extension never sends a prompt, changes a message or selects a different response branch.

## Word formatting

- Your retained template supplies page geometry, Averia Serif Libre typography, plum/navy headings and emphasis styles. Install Averia Serif Libre on the computer that opens the Word document to match the template exactly.
- Headings are real named Word paragraph styles, with **no list inheritance or numId=0 markers**. A BS3 heading is never exported as a bullet.
- Only the document title uses H1. Roman-numbered sections use H2; lettered subsections use H3; numeric sub-subsections use H4. The exporter preserves heading prefixes exactly and never adds, removes or renumbers them. For a single response, its opening title becomes the document title without a duplicate chat-title heading.
- Short standalone bold-only labels are recognized as headings. Medical statements, body paragraphs and actual list items retain their source structure.
- Bullets and numbering are native editable Word lists, including nesting, list starts and separate restarts. Abstract numbering definitions are written before concrete list instances.
- Tables are editable Word tables with repeating header rows, light borders, merged cells and text exactly one point smaller than the body. Bold row labels remain table text, without heading shading or forced uppercase.
- Inline bold, italics, links, highlights, subscript, superscript, code and quotations are retained. The extension formats content; it does not rewrite or fact-check it.

## Content limits

The export includes the active conversation branch and history exposed by the chat page. It cannot recover deleted turns, inaccessible history or alternative branches. Expand collapsed material before exporting. Separate canvases, Claude artifacts and attached source documents are not automatically opened or exported. If traversal cannot maintain a continuous message sequence, export stops instead of silently producing a partial chat.

Readable images, including pictures inside preview buttons, are downloaded and embedded as PNG at 4 cm height. Width follows the image proportions up to the page width. The extension can retrieve images from the providers' image CDNs when page CORS prevents access. Browser restrictions can still prevent downloading some remote or protected images; those keep a labelled source link and trigger a visible warning. Source URLs in an exported document can contain private chat identifiers; share the document accordingly.

Equations retain their LaTeX/text representation rather than becoming native Word equation objects. Interactive charts, videos and proprietary site widgets are outside the supported text/table/image export.

Chat sites change their HTML over time. If no responses are detected, leave the conversation open, refresh the extension and retry. This version has automated tests against representative DOM fixtures for all three sites; live signed-in site layouts still need user verification.

## Development

All runtime assets are bundled. `build_template.py` regenerates the sanitized reference template and icons; it requires Python, lxml and Pillow. `tests/test-browser.cjs` runs browser fixture tests with Playwright. `tests/verify_docx.py` checks generated OOXML packages, heading styles, numbering and table fonts. QA files are not part of the extension ZIP.

Chrome API references: [activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab), [scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting), [downloads](https://developer.chrome.com/docs/extensions/reference/api/downloads). Third-party license notices are in `THIRD_PARTY_NOTICES.txt`.
