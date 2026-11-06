"""Rewrite the app HTML in memory so it runs fully offline.

The source HTML is never modified on disk; assets/app.html stays a verbatim copy
so it can be swapped for a newer export later. Every substitution asserts it
matched the expected number of times, because a silent miss would quietly restore
a CDN dependency and the app would appear to work until the network went away.

JSZip is not cosmetic here: it is the .docx parser (the app calls
JSZip.loadAsync on every document), so a failed rewrite means no notes render.
"""

from __future__ import annotations

import re

from .save_js import APP_SCOPE_ANCHORS, SAVE_JS
from .study_navigation import STUDY_BRIDGE_JS, STUDY_NAV_JS
from .pearls import PEARLS_CSS, PEARLS_JS
from .study_editor import STUDY_EDITOR_JS
from .quiz_generation import QUIZ_GENERATION_JS, QUIZ_EXPLANATION_SCHEMA_JS, QUIZ_REQUIREMENTS

SAVE_JS = SAVE_JS.replace("cnlInstallHome();\ncnlInstallTopbarHoverReveal();",
                          STUDY_NAV_JS + PEARLS_JS + "\ncnlInstallHome();\ncnlInstallPearls();\ncnlInstallTopbarHoverReveal();", 1)
from .view_modes import VIEW_MODES_CSS
from . import paths

# Both vendored stylesheets are verbatim Google Fonts CSS, so each still points at
# fonts.gstatic.com. The directory differs per family (averiaseriflibre/v19,
# inter/v20) and changes whenever Google re-cuts a font, so match the shape of the
# URL rather than one fixed prefix.
_GSTATIC_DIR = re.compile(r"https://fonts\.gstatic\.com/s/[a-z0-9]+/v\d+/")

# The page ships a single Google Fonts link, but the desktop build offers two
# families, so that one link expands into one local stylesheet each.
VENDOR_FONT_LINKS = (
    '<link href="/vendor/averia-serif-libre.css" rel="stylesheet">'
    '<link href="/vendor/inter.css" rel="stylesheet">'
)

_JSZIP_TAG = re.compile(
    r'<script[^>]+src="https://cdn\.jsdelivr\.net/npm/jszip[^"]*"[^>]*>\s*</script>',
    re.I,
)
_FONTS_LINK = re.compile(
    r'<link[^>]+href="https://fonts\.googleapis\.com/css2[^"]*"[^>]*>',
    re.I,
)
_PRECONNECT = re.compile(r'<link[^>]+rel="preconnect"[^>]*>\s*', re.I)
_ICON_LINK = re.compile(
    r'<link[^>]+rel="icon"[^>]+href="clinical_notes_library_icon\.ico"[^>]*>', re.I
)
_TOUCH_ICON = re.compile(r'<link[^>]+rel="apple-touch-icon"[^>]*>\s*', re.I)
_MANIFEST = re.compile(r'<link[^>]+rel="manifest"[^>]*>\s*', re.I)
_HEAD_CLOSE = re.compile(r'</head>', re.I)

# Desktop-only UI policy. The app HTML ships verbatim, so controls that only
# make sense in a browser (folder pickers, upload, export-to-directory buttons)
# are hidden here instead of being edited out of the source.
DESKTOP_UI_CSS = """
<style id="cnl-desktop-ui">
/* Everything the user reads sits in a centred 1000px column rather than
   stretching to the window. The app's own "TRUE NARROW" block sets
   max-width:100% !important on .app-shell, .screen-area and .screen, which is
   what let the home and subject screens run edge to edge and quietly defeated
   the 1180px measure the app asks for two rules earlier. transform_html injects
   this stylesheet at the very end of the document head, so it is the last word
   in the cascade and an equal-specificity !important beats it. That 1180px is
   now inert for the same reason: it is wider than the column that contains it.

   Only the content region is capped. The header stays full-bleed because its
   reader toolbar is position:fixed to the viewport and would not follow a
   narrowed ancestor, and because a sticky bar that stops short of the window
   edge reads as broken. The poster backdrop and every modal are siblings of
   <main>, so they are outside this element and keep covering the window.

   The same column contains the reader and canvas surfaces. What narrows is
   the home and subject screens,
   and with them the balance between their display type and the column it
   sits in: a 30px title reads larger over 960px of content than it did
   over 1344px.

   So the composition is scaled by the same ratio the column was, 1000/1400 =
   5/7, in the COLUMN SCALE block at the foot of this sheet and in the home and
   Rapid Revision rules below. Two classes of size, and only two:

   - layout geometry, scaled in full: the column padding, the grid minimums that
     decide how many cards fit a row, and every gap, padding, margin, radius and
     min-height that was set against them. Scaling the grid minimums is what
     keeps the column count - five subject cards and four chapter cards across -
     instead of leaving three and four much wider ones in a narrower room.
   - display type above 20px, scaled in full, so the hierarchy keeps its
     proportions: 32 -> 23, 30 -> 21, 26 -> 19, 24 -> 17.

   Type at 20px or below is deliberately left alone. It was sized for
   legibility and for the steps between it, not against the column, and 5/7 of
   it lands in the low teens where a card title and its own body copy come out
   the same size. The 20px boundary is what keeps that from happening: the
   Rapid Revision breadcrumb stays 20px and the poster names under it stay 16px,
   and the subject card's 19px name still sits above the app's 17px chapter
   name. Nothing is enlarged, so the smallest sizes in the sheet are unchanged. */
:root{--cnl-ui-width:1000px;--cnl-ui-content-width:960px}
.screen-area{
  width:100%!important;
  max-width:var(--cnl-ui-width)!important;
  min-width:0;
  margin-left:auto!important;
  margin-right:auto!important;
}

/* Browser-only controls: the desktop app owns data\\files, so folder pickers,
   upload and directory exports have nothing to act on. */
#refreshServerLibraryBtn,#masterFolderBtn,#selectSaveDirectoryBtn,
#saveFormattedFolderBtn,#saveStandaloneBtn,#createFolderHomeBtn,
#uploadDocumentHomeBtn,#homeDocumentInput,#masterFolderInput{display:none!important}
.master-folder-help:not(#formattedSaveStatus){display:none!important}
.chapter-meta{display:none!important}
.subject-card>div:last-child{display:flex;flex-direction:column;align-items:center;text-align:center}
.subject-name{font-size:19px!important;line-height:1.25!important}

/* "Save in My Notes" saves an AI-generated note into data\\files\\My Notes. The
   app's own version of this needs the File System Access API, which WebView2 does
   not expose, so save_js.py replaces the window hook it calls with a POST to the
   local server. The button stays visible and keeps the app's own show/hide
   logic, which reveals it only while a generated note is open. */

/* Only the two folders the app may write to are managed, so only their cards get
   rename/delete. Every other subject and chapter is read-only and shows no
   controls at all. save_js.py adds .cnl-managed after matching the card's name
   against the subjects the server will accept, ignoring case because the library
   scanner reports a folder with the spelling it happens to have on disk.
   opacity keeps the 30px buttons from reflowing the card, pointer-events stops
   invisible buttons being clicked, focus-within keeps them reachable by
   keyboard. */
.subject-card-actions,.chapter-actions{display:none!important}
.subject-card.cnl-managed .subject-card-actions,
.chapter-card.cnl-managed .chapter-actions{
  display:flex!important;
  opacity:0!important;pointer-events:none!important;
  transition:opacity .13s ease!important;
}
.subject-card.cnl-managed:hover .subject-card-actions,
.subject-card.cnl-managed:focus-within .subject-card-actions,
.chapter-card.cnl-managed:hover .chapter-actions,
.chapter-card.cnl-managed:focus-within .chapter-actions{
  opacity:1!important;pointer-events:auto!important;
}

/* Reader toolbar. Mark as read is gone: opening a note is what Previously Read
   records. The remaining 28px buttons sit in a 36px bar, top:4px centres them. */
.reader-header-actions{
  top:4px!important;right:8px!important;height:28px!important;
  max-width:calc(100vw - 130px)!important;
  align-items:center!important;padding-bottom:0!important;
}
#cnlTopReadControl,
body.view-reader #cnlTopReadControl{display:none!important}
body.view-reader #cnlSlidesTopBtn{display:flex!important}
body:not(.view-reader) #cnlSlidesTopBtn{display:none!important}

/* Snapshot / Slides / Flashcards / Quiz / Pen: square marks, hover name. */
.reader-header-actions .study-top-btn.study-top-icon,
.app-header .study-top-btn.study-top-icon,
.cnl-pen-open.cnl-tool-icon,
.cnl-nb-new.cnl-tool-icon{
  width:28px!important;min-width:28px!important;padding:0!important;
  display:inline-flex!important;align-items:center;justify-content:center;
}
.study-top-icon svg,
.cnl-tool-icon svg{display:block;width:15px;height:15px}

/* Folder over document name, two smaller lines instead of "folder / name". */
body.view-reader #breadcrumb.cnl-reader-title,
body.view-reader #breadcrumb{
  display:flex!important;
  flex-direction:column!important;
  align-items:flex-start!important;
  justify-content:center!important;
  gap:0!important;
  margin-top:0!important;
  white-space:normal!important;
  overflow:hidden!important;
  text-overflow:clip!important;
  font:inherit!important;
  line-height:1.15!important;
  max-width:min(420px,calc(46vw - 110px - var(--cnl-wordmark-w,0px)))!important;
}
body.view-reader #breadcrumb .cnl-reader-title-folder{
  display:block;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font:500 11px/1.15 "Averia Serif Libre",serif!important;
  color:#6b7288!important;
}
body.view-reader #breadcrumb .cnl-reader-title-file{
  display:block;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font:700 13px/1.15 "Averia Serif Libre",serif!important;
  color:var(--cnl-ink,#292664)!important;
}

/* The app's own download button saves a formatted DOCX directly. save_js.py
   hides it and puts #cnlMoreBtn beside it, whose menu offers a snapshot of the
   section on screen, Word and PDF; the Word option clicks this hidden button so
   the app's own DOCX builder - the highest-fidelity path available - still does
   the work. A hidden element still dispatches click(), which is what that
   delegation depends on.

   Stated twice, and the second selector is the one that does the work. The app
   has its own body.view-reader #saveCurrentFormattedBtn{display:flex!important}
   (app.html:2800-2802). Two !important declarations are settled by specificity
   and not by order, so the bare id at (1,0,0) loses to it at (1,1,1) and the
   button stays on screen in the reader - the only view it appears in, and the
   only view this rule was ever about. Matching the app's selector ties the
   specificity, and because this stylesheet is injected immediately before
   </head>, after the app's own, source order then decides it in our favour. */
#saveCurrentFormattedBtn,
body.view-reader #saveCurrentFormattedBtn{display:none!important}

/* The reader's "Gemini" button (API keys and provider settings) is gone at the
   user's request. Hidden rather than removed from the DOM: the app looks it up
   again on every refresh of the AI panel, and hiding keeps that code running
   harmlessly. Keys and providers stay reachable from the home screen's own AI
   settings panel.

   The AI note's save button was hidden here beside it. It is back on the bar at
   the user's request, relabelled "Save in My Notes", so it is no longer listed.
   A bare id is enough for Gemini: the app's only body.view-reader
   display:flex!important rule is #saveCurrentFormattedBtn's, which is why the
   block above has to state its selector twice and this one does not. */
#aiToolsBtn{display:none!important}

.cnl-save-menu{
  position:fixed;z-index:80;min-width:212px;padding:5px;
  background:#fff;border:1px solid var(--cnl-line,#dde1ef);border-radius:10px;
  box-shadow:0 12px 30px rgba(41,38,100,.20);
  display:flex;flex-direction:column;gap:2px;
}
.cnl-save-menu[hidden]{display:none}
.cnl-save-menu button{
  appearance:none;cursor:pointer;text-align:left;
  border:0;background:transparent;border-radius:7px;
  padding:8px 10px;color:var(--cnl-ink,#292664);
  font:600 12.5px/1.25 system-ui,-apple-system,"Segoe UI",sans-serif;
}
.cnl-save-menu button:hover:not(:disabled){background:rgba(181,204,241,.30)}
.cnl-save-menu button:disabled{opacity:.5;cursor:default}

/* The snapshot row is icon-only while the Word and PDF rows beside it keep their
   labels, so it centres its mark rather than starting it at the left edge where a
   label would begin. The row's own padding is untouched: 8px top and bottom around
   a 15px icon comes to 31px against the 31.6px the 12.5px/1.25 text rows make, so
   the menu's height does not move when the label is dropped. */
.cnl-save-menu button.cnl-icon-item{display:flex;align-items:center;justify-content:center}
.cnl-save-menu button.cnl-icon-item svg{display:block;width:15px;height:15px}

/* The reading-settings picker reuses .cnl-save-menu and only adds group headings, a
   tick column and the three step rows. The tick character comes from save_js.py: this
   Python string is not raw, so a CSS unicode escape written here would be eaten by
   Python.

   It still scrolls, but nothing needs it to any more: a face of two rows and three
   scales of one row each is eight rows, against the thirty-one the four full ladders
   used to make. The cap stays because the menu hangs off a button near the top of the
   screen with nowhere to grow upwards into, and a short window is the case it was
   written for. */
.cnl-view-menu{max-height:calc(100vh - 76px);overflow-y:auto;overscroll-behavior:contain}
.cnl-view-menu-label{
  padding:7px 10px 3px;color:var(--cnl-muted,#7a7897);
  font:700 10px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif;
  letter-spacing:.08em;text-transform:uppercase;
}
.cnl-view-menu-label:not(:first-child){margin-top:4px;border-top:1px solid var(--cnl-line,#dde1ef);padding-top:8px}
.cnl-view-tick{display:inline-block;width:15px;visibility:hidden}
.cnl-view-menu button[aria-checked="true"] .cnl-view-tick{visibility:visible}
.cnl-view-menu button[aria-checked="true"]{color:var(--cnl-ink,#292664)}

/* A scale row: decrease, the rung it is on, increase. What sits between the two is a
   signed count of rungs from the default rather than the percentage underneath, so it
   is short and its width changes as it counts; the span takes the row's remaining
   width and centres its text, which is what holds the two buttons at fixed ends
   whatever the middle reads. They keep the menu's own chrome with a hairline around
   them, because unlike a pick they are not full-width rows and need an edge to read
   as pressable. The extra class is what outranks `.cnl-save-menu button` - no
   !important, and the disabled state that greys a button at the end of a ladder is
   the menu's own. */
.cnl-view-menu .cnl-view-step{display:flex;align-items:center;gap:6px;padding:1px 6px 5px}
.cnl-view-menu .cnl-view-step-value{
  flex:1 1 auto;min-width:54px;text-align:center;
  font:700 12.5px/1.25 system-ui,-apple-system,"Segoe UI",sans-serif;
  font-variant-numeric:tabular-nums;color:var(--cnl-ink,#292664);
}
.cnl-view-menu .cnl-view-step button{
  flex:0 0 auto;width:32px;padding:6px 0;text-align:center;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:7px;
  font:700 14px/1 system-ui,-apple-system,"Segoe UI",sans-serif;
}

#cnlSaveToast{
  position:fixed;left:50%;bottom:26px;z-index:90;transform:translateX(-50%);
  max-width:min(620px,92vw);padding:9px 15px;border-radius:10px;
  background:var(--cnl-ink,#292664);color:#fff;
  font:600 12.5px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;
  box-shadow:0 10px 28px rgba(41,38,100,.28);
  opacity:0;pointer-events:none;transition:opacity .18s ease;white-space:pre-line;
}
#cnlSaveToast.cnl-on{opacity:1}

/* Reader layout grips, added by save_js.py after a note renders. They are pure
   affordance for two in-app overrides - table column widths and image position -
   which the server stores per note, so the .docx is never written.

   The column handle sits wholly inside its cell. The reading view paints the table
   with overflow:hidden and a border-radius, which would clip anything hanging off
   the last column's right edge. Its visible line is white with a dark ring because
   row one is #6F3D5D and the body rows are white, and a single-colour line
   disappears against one of the two. */
.reader-main .paper td{position:relative}
.cnl-col-grip{
  position:absolute;top:0;right:0;width:9px;height:100%;z-index:4;
  cursor:col-resize;touch-action:none;
}
.cnl-col-grip::after{
  content:'';position:absolute;top:0;right:3px;width:2px;height:100%;
  background:transparent;box-shadow:none;transition:background .12s ease;
}
.cnl-col-grip:hover::after,.cnl-col-grip.cnl-active::after{
  background:#fff;box-shadow:0 0 0 1px rgba(41,38,100,.6)
}
body.cnl-drag-col{cursor:col-resize!important}
body.cnl-drag-col .cnl-col-grip::after{background:#fff;box-shadow:0 0 0 1px rgba(41,38,100,.6)}
body.cnl-drag-col,body.cnl-drag-img{user-select:none!important}

/* The wrap is already display:inline-block; position:relative gives the handle
   something to sit against. The app's own .paper .doc-image-wrap rule sets
   overflow:hidden, so the handle has to stay inside the image's box. */
.doc-image-wrap{position:relative}
.cnl-img-grip{
  position:absolute;top:1px;left:1px;width:15px;height:15px;z-index:5;
  cursor:grab;touch-action:none;opacity:0;transition:opacity .12s ease;
  border-radius:4px;background:rgba(111,61,93,.88);color:#fff;
  font:700 10px/15px system-ui,-apple-system,"Segoe UI",sans-serif;text-align:center;
}
.doc-image-wrap:hover .cnl-img-grip,.doc-image-wrap.cnl-dragging .cnl-img-grip{opacity:1}
.doc-image-wrap.cnl-dragging{opacity:.45}
body.cnl-drag-img{cursor:grabbing!important}

/* A drop target is marked with an outline, never a border: .doc-block margins are
   all zero, so a border would push the note's text down while it is being dragged
   and the target would move out from under the pointer. */
.doc-block.cnl-drop-target,table.cnl-drop-target{outline:2px solid #6f3d5d;outline-offset:2px}
.doc-block.cnl-drop-end,table.cnl-drop-end{box-shadow:0 4px 0 -1px #6f3d5d}

/* Page colour for the reading surfaces. Two tokens, and they stay two even though
   the values now sit one step apart: --cnl-sheet feeds .paper and nothing else,
   --cnl-page feeds the study surfaces. Merging them into one near-white would make
   the note sheet and the flashcard/quiz/dialog surfaces permanently move together,
   which is what the split was introduced to stop. Each value still has one source.

   The lavender accent surfaces (.ai-flash-back, .ai-quiz-explain) keep their tint
   - they are callouts sitting ON the page, not the page. The quiz hover, right and
   wrong states are all !important too, but at (0,3,0) and (0,2,0) against the
   (0,1,0) below, and specificity beats source order between two !important rules,
   so they keep winning.

   Screen only. cnlNoteTarget() in save_js.py forces background:#fff on html, body
   and .paper for every PDF and PNG export, so a printed note stays white whatever
   the sheet looks like on screen. */
:root{--cnl-page:#FCFCFC;--cnl-sheet:#FBFBFB}
.paper{background:var(--cnl-sheet)!important}
.ai-modal,.ai-flash-front,.ai-quiz-opt{background:var(--cnl-page)!important}

/* The outline slides in from the right. It is a pure fixed overlay - the app's own
   comment at .reader-sidebar says it "no longer consumes layout width" - so the
   note's page needs no matching margin and stays centred.

   Both states are declared here, not just the closed one. The app already asks for
   translateX(0) when open and 0 is the same on either edge, so borrowing its open
   rules would work on paper - but the closed rule below is also the value the panel
   starts its 200ms slide from, and borrowing would leave the open position decided
   by rules scattered over four places in app.html at three different specificities.
   One block, both positions, next to the edge they belong to.

   opacity and pointer-events travel with the transform because the app sets all
   three together: a panel that slides in but stays transparent is still hidden.

   The toggle is not in the top-left cluster with Back and Home: save_js.py moves it
   into the reader's own action strip, at the extreme right of the bar. */
.reader-sidebar{
  left:auto!important;right:0!important;
  border-right:0!important;border-left:1px solid var(--cnl-line,#dde1ef)!important;
  box-shadow:-10px 0 28px rgba(41,38,100,.06)!important;
}
body.reader-sidebar-hidden .reader-sidebar{
  transform:translateX(100%)!important;
  opacity:0!important;pointer-events:none!important;
}
/* Same specificity as the closed rule and later in source order, so this is what the
   panel settles into the moment reader-sidebar-hidden is dropped - which is how the
   app opens the outline on desktop. reader-sidebar-open is the narrow-window path,
   where the app keeps both classes on the body and lets this one decide. */
body.reader-sidebar-open .reader-sidebar,
body:not(.reader-sidebar-hidden) .reader-sidebar{
  transform:translateX(0)!important;
  opacity:1!important;pointer-events:auto!important;
  z-index:120000!important;
}

/* Outline rows for H2. The vendor gives every generation the same 8px of vertical
   padding, which reads as a flat list of equals; an H1 and the H2s under it should
   not share a rhythm. Halving H2's padding and tightening its line height leaves H1
   with the air that says "new part of the note" and groups the H2s under it into a
   run. Only H2 moves - H3 and H4 are already a smaller face, and H2 is what was
   asked for.

   The toggle has to shrink with it. .reader-tree-row is align-items:center, so the
   row is as tall as the taller of the heading button and the expand button beside
   it, and at the vendor's 28px the toggle is taller than an H2 row with 4px of
   padding - tightening the text alone would change nothing on any row that has
   children. 22px is under the new row height and still a comfortable mouse target.

   Nested H2s sit inside .reader-tree-children, which is display:block, so none of
   .reader-toc's 2px gap reaches them: this padding is the whole of their spacing. */
.reader-tree-node.level-2 > .reader-tree-row .reader-heading{
  padding-top:4px!important;padding-bottom:4px!important;line-height:1.2!important;
}
.reader-tree-node.level-2 > .reader-tree-row .reader-tree-toggle{
  flex:0 0 22px!important;width:22px!important;height:22px!important;
  font-size:15px!important;
}

/* Back and Home alone on the left, the outline toggle on the right, "Aa" in the
   middle of the bar.

   The left cluster is two buttons wide now instead of four, so the room the header
   reserves for it drops to match: 6px of inset plus 2x30px plus the 4px gap is 70px,
   and 76px is the figure the app already uses for the same pair in the subject view.

   The cluster's geometry is restated because the app's own .top-left-nav .icon-btn
   (app.html:3334-3345) loses to .app-header .icon-btn (app.html:4286-4296) on
   source order at the same (0,2,0) specificity - which is why Back renders 28px
   tall beside a 30px Home, whose id also appears at app.html:2599-2606. Saying it
   again later in the document puts the pair on one geometry without editing the
   app's rule for Home. padding is zeroed for the same reason: .app-header .icon-btn
   hands every header button 5px 7px, which inside a 30px border-box leaves a 14px
   content box for a 15px glyph. */
body.view-reader .app-header{padding-left:112px!important}
.top-left-nav .icon-btn{
  width:30px!important;height:30px!important;flex:0 0 30px!important;
  border-radius:8px!important;font-size:15px!important;padding:0!important;
}

/* "Aa" centred in the bar. .app-header is position:sticky, so it is a containing
   block, and an absolutely positioned child is out of flow - the header's grid
   columns carry on as though the button were not there. left:50% resolves against
   the padding box, so this is the true centre of the bar and not of the space
   between its two paddings. The z-index sits between the two toolbar clusters'
   100000 and 100200, where nothing else is.

   top is a length rather than 50%: the bar's 36px border box carries a 1px bottom
   border, so its padding box is 35px and centring in that puts a 30px button half a
   pixel above the .top-left-nav pair, which the app pins at top:3px. 3px is also
   what centres 30px in 36px, so this lands on the same row as Back and Home. */
#cnlTypeBtn{display:none}
body.view-reader #cnlTypeBtn,
body.view-reader .reader-header-actions #cnlTypeBtn,
body.cnl-canvas-mode.view-reader #cnlTypeBtn{
  position:static!important;
  top:auto!important;
  right:auto!important;
  left:auto!important;
  transform:none!important;
  z-index:auto!important;
  display:inline-flex!important;
  align-items:center!important;
  justify-content:center!important;
  opacity:1!important;
  visibility:visible!important;
  pointer-events:auto!important;
  order:-1;
  flex:0 0 28px!important;
  width:28px!important;
  min-width:28px!important;
  height:28px!important;
  border-radius:7px!important;
  font:700 12px/1 system-ui,-apple-system,"Segoe UI",sans-serif!important;
  letter-spacing:0!important;
  padding:0!important;
}

/* Four groups make this the tallest menu in the app, about 595px, and the window
   resizes down to 620px - where a menu hung 39px below the bar would run off the
   bottom. It scrolls instead. The 52px of slack is the button's own 33px bottom
   edge, the 6px gap and a little air; the children are pinned because a flex column
   with a capped height shrinks its items rather than overflowing them.
   z-index 80 sat the menu behind the 36px header, which hid Font and the
   spacing rows. */
#cnlTypeMenu{
  z-index:150000!important;
  max-height:calc(100vh - 52px);
  overflow-y:auto;
}
#cnlTypeMenu > *{flex:0 0 auto}

/* The outline toggle and the More button beside it join a strip whose children are
   all 28px and which clips at that height - .reader-header-actions is
   overflow-y:hidden (app.html:3104-3112). The app's id rule would carry the toggle
   in at 30px and lose 1px off the top and bottom to the clip, and .top-left-nav
   .icon-btn no longer reaches it now that it has left that cluster, so both take
   the strip's own 28px, 7px geometry instead. One rule for the pair because two
   unlike buttons sitting side by side at the far right read as a mistake. */
.reader-header-actions #cnlMoreBtn{
  width:28px!important;min-width:28px!important;height:28px!important;
  flex:0 0 28px!important;border-radius:7px!important;font-size:14px!important;
  padding:0!important;
}
#toc .reader-flashcard-count{display:none!important}
#aiSavedPosterBtn{display:none!important}
/* Corner pills sit on the page, not in the auto-hiding header. Undo/Redo
   bottom-left, Outline top-right. */
html body > #cnlInkEditPills,
html body > #cnlOutlinePill,
html body > #cnlPdfPagePills,
body.view-reader #cnlInkEditPills,
body.view-reader #cnlOutlinePill,
body.cnl-canvas-mode.view-reader #cnlInkEditPills,
body.cnl-canvas-mode.view-reader #cnlOutlinePill,
body.cnl-pdf-open #cnlOutlinePill,
body.cnl-pdf-open #cnlPdfPagePills{
  display:none;
  position:fixed!important;
  z-index:130000!important;
  align-items:center!important;
  gap:8px!important;
  pointer-events:none!important;
  opacity:1!important;
  visibility:visible!important;
  transform:none!important;
}
html body > #cnlInkEditPills,
body.view-reader #cnlInkEditPills,
body.view-reader > #cnlInkEditPills,
body.cnl-canvas-mode.view-reader #cnlInkEditPills{
  left:16px!important;
  right:auto!important;
  bottom:16px!important;
  top:auto!important;
  justify-content:flex-start!important;
}
html body > #cnlOutlinePill,
body.view-reader #cnlOutlinePill,
body.view-reader > #cnlOutlinePill,
body.cnl-canvas-mode.view-reader #cnlOutlinePill,
body.cnl-pdf-open #cnlOutlinePill{
  right:16px!important;
  left:auto!important;
  top:52px!important;
  bottom:auto!important;
  justify-content:flex-end!important;
}
html body > #cnlPdfPagePills,
body.cnl-pdf-open #cnlPdfPagePills{
  right:16px!important;
  left:auto!important;
  bottom:16px!important;
  top:auto!important;
  justify-content:flex-end!important;
}
body.view-reader #cnlInkEditPills,
body.view-reader > #cnlInkEditPills,
body.cnl-canvas-mode.view-reader #cnlInkEditPills,
body.view-reader #cnlOutlinePill,
body.view-reader > #cnlOutlinePill,
body.cnl-canvas-mode.view-reader #cnlOutlinePill,
body.cnl-pdf-open #cnlOutlinePill,
body.cnl-pdf-open #cnlPdfPagePills{
  display:flex!important;
}
body:not(.view-reader):not(.cnl-pdf-open) #cnlInkEditPills,
body:not(.view-reader):not(.cnl-pdf-open) #cnlOutlinePill,
body:not(.view-reader):not(.cnl-pdf-open) #cnlOutlineBtn,
body:not(.view-reader) #cnlTypeBtn,
#cnlPdfPagePills[hidden]{display:none!important}
body.cnl-pdf-open #cnlPdfOutlineBtn{display:none!important}
#cnlInkEditPills button,
#cnlOutlinePill button,
#cnlPdfPagePills button,
#cnlOutlineBtn{
  appearance:none;
  pointer-events:auto!important;
  width:32px;
  min-width:32px;
  height:32px;
  padding:0;
  margin:0;
  border-radius:999px;
  border:1px solid var(--ui-line,#d9dee7);
  background:#fff!important;
  color:var(--cnl-ink,#292664)!important;
  cursor:pointer;
  opacity:1!important;
  font-size:0;
  line-height:0;
  box-shadow:0 1px 4px rgba(41,38,100,.08);
  display:inline-flex;
  align-items:center;
  justify-content:center;
}
#cnlInkEditPills button svg,
#cnlOutlinePill button svg,
#cnlPdfPagePills button svg,
#cnlOutlineBtn svg{
  display:block;
  width:16px;
  height:16px;
}
#cnlInkEditPills button:hover,
#cnlOutlinePill button:hover,
#cnlPdfPagePills button:hover,
#cnlOutlineBtn:hover{background:#f6f7f9!important}
#cnlInkEditPills button:disabled{opacity:.35!important;cursor:default;box-shadow:none}
/* Home was pinned to the far right and sat on top of Outline. In the reader it
   stays in the left cluster with Back. */
body.view-reader #headerHomeBtn{
  position:static!important;
  top:auto!important;
  right:auto!important;
  z-index:auto!important;
}
body.view-reader .app-header{padding-right:8px!important}

/* The app's own name, in the corner the fixed navigation cluster leaves free.
   .top-left-nav is position:fixed at left:6px and the header reserves 18px, 76px
   or 112px of left padding per view to clear it, so this is the first thing in
   flow and reads as the top-left of the bar in all three.

   Its width is a token because the breadcrumb clearance below has to subtract
   it: 20px Averia bold sets "Cortex" at about 72px, plus 8px of padding and 1px
   of divider here and the row's own 8px gap. Rename the app and this is the
   number to re-measure. */
.app-header{--cnl-wordmark-w:0px}
.cnl-app-title{display:none!important}
/* The row centres its items, and a 3px top margin on one of them shifts its text
   down half that against the wordmark beside it. */
.breadcrumb-row .breadcrumb{margin-top:0}

/* The breadcrumb starts 70px further left than it did and "Aa" now sits in the band
   it runs through, so it stops short of the button instead of passing under it.
   50vw - 110px is the distance from the 76px inset to the button's left edge with
   clearance to spare, less the wordmark that now shares the row; wider than about
   1340px the app's own 560px cap binds first and nothing changes. */
.breadcrumb{max-width:min(560px,calc(50vw - 110px - var(--cnl-wordmark-w,0px)))!important}

/* Below about 1000px there is no room for all three groups. The right strip is a
   fixed ~464px wide and right-anchored 6px from the edge, so the bar's centre falls
   inside it: at a 910px viewport the two meet at 440px. A centred button there
   paints over the outline toggle and takes its clicks, because the z-index that
   keeps it clear of the breadcrumb puts it above the strip too. Past the crossover
   it therefore goes back to sitting beside Home, where it was before this change,
   and the header reserves the app's own three-button inset again.

   1000px rather than the 970px where they actually touch, so the swap happens with
   a visible gap still between them. left is a length and the transform is dropped:
   at this width Home ends at 70px, so 76px leaves the same 6px gap the wide layout
   has, and neither property carries !important above, so this equal-specificity
   later rule wins on source order.

   The breadcrumb guard goes with it, still less the wordmark that shares its row.
   With nothing centred to stop short of, the app's own cap is what the layout had
   all along. */
@media(max-width:1000px){
  body.view-reader .app-header{padding-left:112px!important}
  .breadcrumb{max-width:min(calc(48vw - var(--cnl-wordmark-w,0px)),560px)!important}
}

/* Poster text size and spacing, as two unitless ratios on the page element.

   The app sizes the poster with absolute pt and px in about twenty places and its
   sheet cannot be edited, so each of those values is restated here as itself times
   a token. At the default of 1 every calc() collapses back to the original number
   and the poster is exactly the design; the tokens only start to matter once a
   setting moves.

   They are written INLINE on #aiPosterPage by cnlApplyPosterType(), not declared
   here with a value, for two reasons: an inline custom property survives
   page.outerHTML, which is how cnlPosterTarget() carries the poster into the PDF
   and PNG export, and it lets the poster's settings menu repaint live without
   touching a sheet.
   The fallbacks below are what a poster rendered without that pass gets.

   Text is a ratio rather than a size so the poster keeps its own hierarchy - the
   title stays larger than the body at every setting - instead of flattening to one
   uniform point size. The page's own 30px/68px padding is deliberately NOT scaled:
   it is the sheet's margin, and growing it would shrink the area the content has to
   fit into, which is the opposite of what turning the text up is for. */
.ai-poster-page .ai-poster-eyebrow{font-size:calc(9px * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-title{font-size:calc(16.5pt * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-subtitle{font-size:calc(9.75pt * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-section-head{font-size:calc(11.25pt * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-table-title{font-size:calc(9.5pt * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-footer{font-size:calc(9.5px * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-tldr p,
.ai-poster-page .ai-poster-section p,
.ai-poster-page .ai-poster-subsection{font-size:calc(8.5pt * var(--cnl-poster-text,1))!important}
/* The lists and the table are no longer 8.5pt, so neither can stay in the selector
   list above. The lists are the poster's body text - a section is bullets almost end
   to end - and at 8.5pt on a 20cm sheet they were the smallest reading size on the
   page; both levels share one number because a nested list is the same voice as its
   parent, indented. The table sits half a point under them, which is enough to keep a
   wide grid of short cells from competing with the bullets beside it. Its title stays
   9.5pt, so the caption now matches the lists rather than the grid it names. */
.ai-poster-page .ai-poster-section ul,
.ai-poster-page .ai-poster-section ul ul,
.ai-poster-page .ai-poster-numbered{font-size:calc(9.5pt * var(--cnl-poster-text,1))!important}
.ai-poster-page .ai-poster-table{font-size:calc(9pt * var(--cnl-poster-text,1))!important}
/* The catch-all. Anything in the poster that inherits rather than being sized by a
   rule of its own follows the page, so this one line covers what the list misses. */
.ai-poster-page{font-size:calc(var(--body-size) * var(--cnl-poster-text,1))!important}

/* Line spacing: the same treatment for the third token. Every line-height the
   poster sheet declares is restated as itself times the token, so at the default
   of 1 each collapses back to the designed number.

   The ratios stay unitless, which is what lets one rule cover a whole subtree: an
   unitless line-height is inherited as a ratio, so a run inside a paragraph or a
   cell inside a table follows the size that element ends up at rather than a px
   height frozen here. The first list is every poster element that declares a
   line-height of its own and keeps the designed 1.15; the second is the three list
   selectors and the table, which are 1.25. The page's own var(--body-lh) covers
   whatever declares nothing - the eyebrow and the footer. */
#aiPosterBackdrop .ai-poster-page{line-height:calc(var(--body-lh) * var(--cnl-poster-line,1))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-title,
#aiPosterBackdrop .ai-poster-page .ai-poster-subtitle,
#aiPosterBackdrop .ai-poster-page .ai-poster-tldr p,
#aiPosterBackdrop .ai-poster-page .ai-poster-section-head,
#aiPosterBackdrop .ai-poster-page .ai-poster-section p,
#aiPosterBackdrop .ai-poster-page .ai-poster-subsection,
#aiPosterBackdrop .ai-poster-page .ai-poster-table-title{line-height:calc(1.15 * var(--cnl-poster-line,1))!important}
/* The bullets match the reading view's leading rather than the poster's. 1.15 was
   set against 8.5pt, where the lines were short enough that a tighter box still read
   as separate items; at 9.5pt the same ratio packs a wrapped bullet into a block, and
   the gap between two items stops being the largest space in the list.

   The table joins this group for the first time, and it is a correction as well as a
   change. app.html:1644 sets `.ai-poster-table{line-height:1}`, and this sheet never
   restated it - so the one leading in the poster that was NOT the page's 1.3 was also
   the only one the spacing control could not move. Every cell wrapped to lines exactly
   one font-size tall and stayed there at every setting. 1.25 is a real step up from
   that, and it now scales with the token like the rest of the sheet. */
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul,
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul ul,
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered{line-height:var(--body-lh) !important}

/* Spacing: the poster's paragraph-spacing control, scoped the way the reading view
   scopes its own.

   --cnl-para-scale in view_modes.py moves nothing but the vertical air between two
   blocks: _apply_para_scale rewrites padding-top and padding-bottom on .doc-block
   rules and deliberately leaves the list indent's padding-left alone. This token now
   does the same job here, on the poster's equivalent of a paragraph - the gap between
   two point blocks, two groups, two list items, a subsection and what follows it, a
   table and what precedes it, and the blocks stacked inside a section body.

   That scoping is the fix. This token used to multiply every gap, margin and padding
   the poster sets, all thirty of them, so turning Spacing down shrank the cells of
   every table, pulled every bullet closer to its marker and narrowed every column as
   well as tightening the paragraphs. None of that is what paragraph spacing means in
   the reading view, and none of it is what turning one knob labelled Spacing reads as
   promising.

   Everything structural is therefore pinned at its designed number, and stated anyway
   rather than deleted, because app.html:3009-3070 restates the poster's layout under
   #aiPosterBackdrop at !important and a bare .ai-poster-page prefix loses to it. That
   block also forces gap:8px on .ai-poster-sections, -row, -full-row and -column,
   overriding the 12pt and 0.65em they declare at app.html:1444-1452 - so 8px is the
   number actually on screen. Pinned covers box padding, table cell padding, list
   indents, the gaps that separate section cards, and the header and footer chrome.

   The em-based gaps stay scaled even though they already follow the text token:
   leaving them out would make this control silently skip most of the air inside a
   section, and scaling both is what keeps the two controls independent rather than
   having one drag the other along.

   At 100% the token is 1, so a poster at 100% is still the design down to the pixel.
   Below it only the inter-block air closes up; above it only that air opens. */

/* ---- pinned: structure, boxes, indents and chrome ---- */
#aiPosterBackdrop .ai-poster-page .ai-poster-eyebrow{margin:0 0 2px!important}
#aiPosterBackdrop .ai-poster-page .kd-title{gap:10px!important;margin:0 0 14px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-subtitle{margin:0 0 0.20em!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-sections{gap:8px!important;margin-bottom:12pt!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-row,
#aiPosterBackdrop .ai-poster-page .ai-poster-full-row,
#aiPosterBackdrop .ai-poster-page .ai-poster-column{gap:8px!important}
/* The flow's gutter is horizontal air, so the spacing token has no claim on it and it
   is pinned like every other gap in this block. Nothing else here addresses columns:
   .ai-poster-section-grid, which app.html's own 760px fallback and this sheet both
   used to style, is never built - appendBalancedBlocks (app.html:11926) has no call
   site and every section flows through .ai-poster-flow instead - so the rule that
   pinned that grid's gap and the 760px block that overrode it are both gone. */
#aiPosterBackdrop .ai-poster-page .ai-poster-flow{column-gap:6px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-tldr{gap:7px!important;padding:6pt 10.5pt!important;margin:0 0 12pt!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-section-head{gap:6px!important;padding:6pt 10.5pt!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul{padding-left:18px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered{padding-left:20px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered li{padding-left:2px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table-title{margin:0 0 4.5pt!important}
/* The poster's own table variant is gone: a poster table now wears the reading view's
   table box, so one grid, one radius, one padding and one banding exist in the whole
   app. The numbers are view_modes.py's - RELAXED_SPEC's TABLES block for the box and
   TABLE_FIXES_CSS for the three values that win there (9pt, 1.25 and 6px of padding on
   all four sides, not the spec's 6px 7px). They are literals here rather than
   var(--note-*) for the same reason they are literals in view_modes.py: that sheet
   states its own palette, and #ADADAD has no token anywhere.

   Pinned, like every other cell padding and border here. This is the inside of a box
   and the box itself, not the air between two blocks, so the spacing control has no
   claim on any of it - only the wrap's margin scales, in the section below. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table{
  min-width:0!important;
  box-sizing:border-box!important;
  border:1px solid #ADADAD!important;
  border-radius:8px!important;
  border-collapse:separate!important;
  border-spacing:0!important;
  overflow:hidden!important;
  background:#FFFFFF!important;
  color:#000000!important;
  margin:0 auto!important;
}
#aiPosterBackdrop .ai-poster-page .ai-poster-table th,
#aiPosterBackdrop .ai-poster-page .ai-poster-table td{
  width:auto!important;
  min-width:0!important;
  max-width:none!important;
  box-sizing:border-box!important;
  padding:6px!important;
  border:0!important;
  border-right:1px solid #ADADAD!important;
  border-bottom:1px solid #ADADAD!important;
  white-space:normal!important;
  overflow-wrap:anywhere!important;
  word-break:normal!important;
}
/* The inside grid stops at the outer edge, or the 8px radius draws a double line. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table th:last-child,
#aiPosterBackdrop .ai-poster-page .ai-poster-table td:last-child{border-right:0!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody tr:last-of-type > td{border-bottom:0!important}
/* Corners follow the table's radius, 1px in. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table thead tr:first-child > th:first-child{border-top-left-radius:7px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table thead tr:first-child > th:last-child{border-top-right-radius:7px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody tr:last-of-type > td:first-child{border-bottom-left-radius:7px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody tr:last-of-type > td:last-child{border-bottom-right-radius:7px!important}
/* Header and banding. Row-position selectors are safe on the poster in a way they are
   not in the reading view: buildPosterSection appends a real <thead> and <tbody> and
   no <colgroup> (app.html:12019-12041), so a <tr> really is its parent's first child
   and nth-child counts rows, not a column group. The reading view needs
   _ROW_SELECTOR_FIXES for exactly the opposite reason.

   A poster whose AI supplied no headers has no <thead> at all, so the banding below
   starts at the first row and nothing is shaded plum. That is correct - there is no
   header row to shade - and it is why the header rules key off thead rather than
   tr:first-child.

   The banding is one row out of phase with the reading view's, on purpose, and it is
   worth stating because a side-by-side comparison reads as a bug. The reader's first
   body row is lavender: renderTable builds no <tbody>, so app.html's
   `tbody tr:nth-child(...)` banding never matches and the `tr:nth-child(2n)` fallback
   written for the colgroup offset paints row one white - which the header rule then
   covers in plum, leaving lavender as the first row anyone sees. The poster has a
   real <thead>, so its first body row really is the first body row, and white there is
   what app.html:506's own comment says the striping was always meant to be. Same two
   colours, same alternation, opposite phase. Do not "match" them by shifting this
   block: that would make the poster open on a shaded row under a plum header. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table thead th{
  background:#6F3D5D!important;
  color:#FFFFFF!important;
  font-weight:700!important;
}
#aiPosterBackdrop .ai-poster-page .ai-poster-table thead th *{color:#FFFFFF!important;background:transparent!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody tr:nth-child(odd) td{background:#FFFFFF!important;color:#000000!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody tr:nth-child(even) td{background:#E7E6F0!important;color:#000000!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-table tbody td *{color:#000000!important;background:transparent!important}
/* Bold markdown inside a cell keeps the poster's 800 weight and loses the blue. The
   reading view forces every descendant of a body cell to black, so #28467C was the
   last thing on a poster table that still belonged to the removed variant. (1,2,1)
   beats app.html:3078's (1,1,1), both !important, and this sheet is injected last. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table strong{color:#000000!important;font-weight:800!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-footer{margin-top:6px!important;padding-top:6px!important;gap:6px!important}

/* ---- scaled: the vertical air between two blocks ---- */
#aiPosterBackdrop .ai-poster-page .ai-poster-group + .ai-poster-group{margin-top:calc(0.42em * var(--cnl-poster-space,1))!important}
/* 6pt above and below the whole table block - caption included, since the wrap holds
   both. Air between two blocks, so it scales; the box it surrounds does not. */
#aiPosterBackdrop .ai-poster-page .ai-poster-table-wrap{margin:calc(6pt * var(--cnl-poster-space,1)) 0!important}
/* The box's own padding is pinned; only the flex gap between the blocks stacked in it
   moves, because .ai-poster-section-body is a column flex (app.html:1496-1502). */
#aiPosterBackdrop .ai-poster-page .ai-poster-section-body{padding:4.5pt 9pt 9pt!important;gap:calc(0.35em * var(--cnl-poster-space,1))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-point-block + .ai-poster-point-block{margin-top:calc(0.20em * var(--cnl-poster-space,1))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-subsection{margin:0 0 calc(0.18em * var(--cnl-poster-space,1))!important}
/* Indent pinned, gap above the nested list scaled. 12px, not the Level-1 18px: the
   circle marker's box is 1.38em wide and hangs in the padding, so 12px puts the child
   bullet on the parent text's column rather than a further indent past it. */
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul ul{margin-top:calc(0.20em * var(--cnl-poster-space,1))!important;padding-left:12px!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul ul li + li{margin-top:calc(0.20em * var(--cnl-poster-space,1))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered li + li{margin-top:calc(0.20em * var(--cnl-poster-space,1))!important}
/* The after side of both levels, and of the numbered list with them.

   It is a bottom margin on every li and not a second term on `li + li`. These lists
   sit in the multi-column flow, which is block layout, so adjacent vertical margins
   collapse and a pair never adds: where the two rules above give an item 0.20em of top
   margin, that 0.20em is the gap and this 0.15em is swallowed by it. After the last
   item there is no larger neighbour to swallow it, and that is the side which had
   nothing at all - the section body's flex gap started where the text ended.

   A Level-1 bullet is the case where nothing is swallowed. The only rule that ever gave
   one a top margin was app.html's own long chain through .ai-poster-section-col, and
   that element is never built - appendBalancedBlocks has no call site - so the prefixed
   copy of it matched nothing either and is gone. Between two Level-1 bullets the gap is
   therefore this 0.15em, 1.8px at the baked 103/90, where two nested bullets get the
   0.20em above them, 2.3px.

   A sublist does not pay it twice. The ul has no bottom padding or border, so its last
   item's margin collapses out through it and then through the parent li, and one
   0.15em arrives below the sublist rather than two. */
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul li{margin-bottom:calc(0.15em * var(--cnl-poster-space,1))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered li{margin-bottom:calc(0.15em * var(--cnl-poster-space,1))!important}

/* Paragraph spacing, before as well as after.

   Every rule above gives a paragraph-level block air on one side only: a subsection
   clears what follows it, a point block clears what precedes it, and a plain
   paragraph in a section body has no margin at all and leans on its container's flex
   gap. Turning the spacing up therefore moved a block away from one neighbour and
   left the other side exactly where it was.

   Each rule here puts the setting's own growth - (token - 1), in the same unit as the
   side that already had it - on the side that had none. At the default of 1 the
   growth is 0, so a poster at 100% is still the design down to the pixel and the
   extra air only appears above it.

   max() against 0 keeps it an increase-only feature: below 1x the added side stays
   shut rather than going negative and pulling a paragraph into its neighbour.

   The two `+` selectors keep their single side on purpose. Point blocks and groups
   live in the multi-column flow, which is block layout, so adjacent vertical margins
   collapse there: a bottom margin between two of them would be swallowed by the next
   block's larger top margin, and would only ever show after the last one - which is
   precisely the side that was missing. */
#aiPosterBackdrop .ai-poster-page .ai-poster-section p{
  margin-top:max(0px,calc(0.18em * (var(--cnl-poster-space,1) - 1)))!important;
  margin-bottom:max(0px,calc(0.18em * (var(--cnl-poster-space,1) - 1)))!important;
}
#aiPosterBackdrop .ai-poster-page .ai-poster-subsection{margin-top:max(0px,calc(0.18em * (var(--cnl-poster-space,1) - 1)))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-point-block{margin-bottom:max(0px,calc(0.20em * (var(--cnl-poster-space,1) - 1)))!important}
#aiPosterBackdrop .ai-poster-page .ai-poster-group{margin-bottom:max(0px,calc(0.42em * (var(--cnl-poster-space,1) - 1)))!important}

/* The poster toolbar is a fixed 36px that cannot grow to wrap what is in it, and
   what is in it varies: the review group is three more items and only appears once
   a poster has been opened from the home screen. So the row scrolls sideways rather
   than clipping, with the scrollbar suppressed because a 36px bar has no room to
   give one up. */
.ai-poster-toolbar-inner{overflow-x:auto;scrollbar-width:none}
.ai-poster-toolbar-inner::-webkit-scrollbar{display:none}
/* The pen menu hangs below this row. overflow-x:auto would clip it, and a
   visible y with a hidden x is computed as auto/auto, so the snapshot bar is
   allowed to overflow rather than hide the menu. */
#aiPosterBackdrop .ai-poster-toolbar{overflow:visible;position:relative;z-index:6}
#aiPosterBackdrop .ai-poster-toolbar-inner{overflow:visible}

/* Snapshot type follows the same face as the notes. Averia is pinned on
   .ai-poster-page in the app sheet; these beat it so Inter is actually reachable. */
#aiPosterBackdrop .ai-poster-page{font-family:"Averia Serif Libre",serif!important}
#cnlPosterTypeMenu{max-height:calc(100vh - 52px);overflow-y:auto;z-index:5}

/* The image export lost its label, so it no longer gets a width from 9px of padding
   around 11px of text and has to state its own box. 23px is the height that padding
   does produce on every sibling here, and box-sizing is border-box app-wide
   (app.html:58), so the 1px borders fall inside it and the button lines up with
   "Save as PDF" beside it instead of standing 3px proud of the row.

   It needs a disabled state of its own now: its export reports through the toast
   rather than by relabelling the button, and .ai-poster-tool-btn styles :disabled
   not at all, so without this the only sign an export is running would be that
   nothing happens. */
#cnlPosterPngBtn{
  width:26px;min-width:26px;height:23px;padding:0;
  display:inline-flex;align-items:center;justify-content:center;
}
#cnlPosterPngBtn:disabled{opacity:.5;cursor:default}
#cnlPosterPngBtn svg{display:block;width:14px;height:14px}

/* ---- Home tab: Deep Dive / Rapid Revision --------------------------------
   #homeScreen carries data-cnl-home and each of its three states shows one set
   of children; the app's own heading, subject grid, activity panels and action
   rows are the Deep Dive set, hidden rather than moved.

   The two option buttons do double duty. On the landing they are the choice;
   once a mode is picked they shrink into a switcher above the content so there
   is always a way across, because setAppView hides both #headerBackBtn and
   #headerHomeBtn on this tab.

   No bottom margin: on the landing the only visible follower is the closing
   credit, which brings its own 44px of top padding, and #homeScreen is a flex
   container so the two would add rather than collapse. The non-landing states
   set their own 13px below. */
#cnlHomeLanding{margin:0}
.cnl-home-landing-title{display:none}
.cnl-home-modes{display:flex;flex-direction:column;gap:14px}
.cnl-home-mode{
  display:flex;flex-direction:row;align-items:center;gap:16px;
  min-height:0;padding:18px;text-align:left;cursor:pointer;
  border:0;border-radius:16px;background:#fff;
  box-shadow:none;font-family:inherit;color:var(--cnl-ink,#292664);
}
.cnl-home-mode:hover{filter:brightness(.98)}
.cnl-home-mode.cnl-active{outline:2px solid var(--cnl-ink,#292664)}
.cnl-home-mode-icon{
  flex:0 0 46px;width:46px;height:46px;border-radius:12px;
  display:flex;align-items:center;justify-content:center;
  background:rgba(255,255,255,.72);font-size:20px;
}
.cnl-home-mode-text{flex:1 1 auto;min-width:0;display:flex;flex-direction:column;gap:4px}
.cnl-home-mode-name{font:700 17px/1.1 "Averia Serif Libre",serif;letter-spacing:.04em}
.cnl-home-mode-sub{font-size:13px;line-height:1.4;color:#667395}
.cnl-home-mode-go{flex:0 0 auto;opacity:.45;font-size:18px}
#cnlHomeDeepDive{background:linear-gradient(90deg,#EAF3FC,#CFE1F5)}
#cnlHomeRapidRevision{background:linear-gradient(90deg,#F0E8EB,#E1D0DC)}
#cnlHomePdfs{background:linear-gradient(90deg,#E8F2EA,#CFE4D4)}
#cnlHomeNotebooks{background:linear-gradient(90deg,#F6EFE4,#E8D9C4)}

/* Today's reading and reviewing, counted in headings because that is the
   granularity the activity log records. */
.cnl-home-stats{display:flex;flex-wrap:wrap;gap:13px;margin-top:16px}
.cnl-home-stat{
  display:flex;flex-direction:column;gap:2px;min-width:94px;padding:10px 13px;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:10px;background:#fff;
}
.cnl-home-stat b{
  color:var(--cnl-ink,#292664);font:700 19px/1.1 "Averia Serif Libre",serif;
  font-variant-numeric:tabular-nums;
}
.cnl-home-stat span{font-size:12.5px;color:#5c627a}

/* The closing credit: a plum "NERD BEHIND THIS" caption over a navy signature,
   supplied as artwork and vendored at /vendor/nerd-behind-this.svg. It is the
   last child of #homeScreen, and the per-state hiding lists name specific
   furniture and never touch it, so it shows in all four home states. Kept out
   of the reader on purpose: a signature under a clinical note is the wrong
   company, and the reader is the surface that gets exported to PDF and PNG.

   #homeScreen is a flex column whose min-height is the viewport less the 72px
   sticky .app-header - the same subtraction .screen-area already makes - so the
   credit can sit at the bottom of the page rather than merely at the end of the
   content. margin-top:auto takes whatever free space is above it.

   The 44px of air is padding rather than margin because the top margin is now
   auto, and an auto margin resolves to zero once the content is tall enough to
   leave no free space - so the gap has to live on a property that always
   applies. Padding does not collapse either, which is why #cnlHomeLanding's
   19px bottom margin was dropped: as flex items the two would add to 63px.
   Measured in all four home states, the gap from the content above to the
   artwork is 44px, and the artwork's bottom edge lands exactly on the content
   box's.

   Halved to 160px on request. The caption is 27 of the artwork's 822 units
   tall, so its capitals come out about 4.5px here against the 9px they had at
   the 320px this size was originally chosen for - which was chosen as the first
   width at which a letter-spaced line this short reads as words rather than
   texture. */
.cnl-credit{
  display:block;width:160px;max-width:70%;height:auto;
  margin:auto auto 0;padding-top:44px;
}
body.view-home #homeScreen{
  min-height:calc(100vh - 72px);
  display:flex;flex-direction:column;
}
/* #homeScreen{display:flex} used to apply even while a note was open, so the
   landing kept a full viewport of height and the reader appeared under it. */
body:not(.view-home) #homeScreen{display:none!important}
body:not(.view-subject) #subjectScreen{display:none!important}
body:not(.view-reader) #readerScreen{display:none!important}
body.view-reader #readerScreen{display:grid!important}

/* Three coverage cards under the mode buttons: H1 and H2 have / total for
   flashcards, quizzes and snapshots. Create more still walks leftover H1s. */
.cnl-home-quick{
  display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:14px 0 0
}
.cnl-h1-stat{
  display:flex;flex-direction:column;align-items:center;gap:0;
  padding:14px 8px;border:0;border-radius:16px;text-align:center;
  color:var(--cnl-ink,#292664);
}
.cnl-h1-stat-flash{background:linear-gradient(90deg,#EAF3FC,#CFE1F5)}
.cnl-h1-stat-quiz{background:linear-gradient(90deg,#F2F3FA,#E2E5F2)}
.cnl-h1-stat-snapshot{background:linear-gradient(90deg,#F0E8EB,#E1D0DC)}
.cnl-h1-stat-icon{
  width:36px;height:36px;border-radius:10px;margin:0 auto;
  display:flex;align-items:center;justify-content:center;
  background:rgba(255,255,255,.72);
}
.cnl-h1-stat-icon svg{display:block;width:18px;height:18px}
.cnl-h1-stat-flash .cnl-h1-stat-icon{color:#294C7B}
.cnl-h1-stat-quiz .cnl-h1-stat-icon{color:var(--cnl-ink,#292664)}
.cnl-h1-stat-snapshot .cnl-h1-stat-icon{color:#5B3A52}
.cnl-h1-stat-label{
  margin-top:8px;font:700 12px/1.2 "Averia Serif Libre",serif;
  letter-spacing:.06em;text-transform:uppercase;
}
.cnl-h1-stat-count{
  margin-top:2px;font:700 16px/1.1 "Averia Serif Libre",serif;
  font-variant-numeric:tabular-nums;
}
.cnl-h1-stat-count-h2{
  margin-top:1px;font:700 13px/1.1 "Averia Serif Libre",serif;
  font-variant-numeric:tabular-nums;opacity:.72;
}
.cnl-h1-stat-create{
  margin-top:10px;width:100%;min-height:36px;padding:4px 8px;
  border:0;border-radius:10px;background:rgba(255,255,255,.72);
  color:var(--cnl-ink,#292664);font:600 12px/1.2 "Averia Serif Libre",serif;
  cursor:pointer;
}
.cnl-h1-stat-create:disabled{opacity:.45;cursor:default}
#cnlHomeLanding .cnl-home-activity{margin-top:17px}
.cnl-h1-job-backdrop{z-index:1300}
.cnl-wait-backdrop{z-index:150000}
.cnl-wait-modal{text-align:center;min-width:min(92vw,280px)}
.cnl-wait-copy{margin:12px 0 0;color:var(--poster-secondary);font-size:13px;line-height:1.4}
.cnl-wait-spin{
  width:28px;height:28px;margin:16px auto 0;border-radius:50%;
  border:3px solid rgba(41,38,100,.12);border-top-color:var(--cnl-ink,#292664);
  animation:cnl-wait-spin .7s linear infinite
}
@keyframes cnl-wait-spin{to{transform:rotate(360deg)}}
.cnl-h1-job-bar{display:block;width:100%;height:8px;margin:10px 0 8px}
.cnl-h1-job-count{margin:0 0 4px;font-size:13px}
.cnl-h1-job-file{margin:0;color:var(--poster-secondary);font-size:12px;line-height:1.35}
.folder-modal.cnl-storage-modal{width:min(92vw,460px)}
.cnl-storage-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid var(--ui-line)}
.cnl-storage-row:last-of-type{border-bottom:0}
.cnl-storage-row b{display:block;font-size:13px}
.cnl-storage-row p{margin:4px 0 0;color:var(--poster-secondary);font-size:11.5px;line-height:1.35}

/* Once a mode is chosen the landing (and its compact switcher row) goes away.
   Back in the header returns to the landing. The attribute has to be present:
   before cnlSetHomeMode runs there is no state to be in. */
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) #cnlHomeLanding{display:none!important}
body.view-home[data-cnl-home]:not([data-cnl-home="landing"]) #headerBackBtn,
body.view-home[data-cnl-home]:not([data-cnl-home="landing"]) #headerHomeBtn{
  display:inline-flex!important;
}
body.view-home[data-cnl-home]:not([data-cnl-home="landing"]) .app-header{
  padding-left:120px!important;
}

/* Pull-to-refresh from Master: on the home top bar, hidden in the reader and
   while a PDF/notebook bar already has its own ↻. */
#cnlLibraryRefresh{display:inline-flex!important}
body.view-reader #cnlLibraryRefresh,
body.view-home[data-cnl-home="pdf"] #cnlLibraryRefresh,
body.view-home[data-cnl-home="notebook"] #cnlLibraryRefresh{display:none!important}
#cnlLibraryRefresh.cnl-busy,
#cnlPdfRefresh.cnl-busy,
#cnlNbRefresh.cnl-busy,
#cnlRapidRefresh.cnl-busy{
  animation:cnlRefreshSpin .75s linear infinite;
}
@keyframes cnlRefreshSpin{to{transform:rotate(360deg)}}

#cnlPdfHeaderBar,
#cnlNbHeaderBar{display:none!important}
/* PDF and notebook tools live in the app header, not on a second bar under it. */
body.view-home[data-cnl-home="pdf"] .app-header,
body.view-home[data-cnl-home="notebook"] .app-header{
  height:40px!important;min-height:40px!important;
  display:flex!important;grid-template-columns:none!important;
  align-items:center!important;gap:8px!important;
  padding-top:0!important;padding-bottom:0!important;padding-right:8px!important;
}
body.view-home[data-cnl-home="pdf"] .app-header-left,
body.view-home[data-cnl-home="notebook"] .app-header-left{flex:0 0 auto}
body.view-home[data-cnl-home="pdf"] #breadcrumb,
body.view-home[data-cnl-home="pdf"] .cnl-app-title,
body.view-home[data-cnl-home="pdf"] .reader-header-actions,
body.view-home[data-cnl-home="notebook"] #breadcrumb,
body.view-home[data-cnl-home="notebook"] .cnl-app-title,
body.view-home[data-cnl-home="notebook"] .reader-header-actions{display:none!important}
body.view-home[data-cnl-home="pdf"] #cnlPdfHeaderBar,
body.view-home[data-cnl-home="notebook"] #cnlNbHeaderBar{
  display:flex!important;flex:1 1 auto;min-width:0;align-items:center;gap:6px;
  margin:0!important;padding:0!important;border:0!important;
  overflow-x:auto;scrollbar-width:none;
}
body.view-home[data-cnl-home="pdf"] #cnlPdfHeaderBar::-webkit-scrollbar,
body.view-home[data-cnl-home="notebook"] #cnlNbHeaderBar::-webkit-scrollbar{display:none}
body.view-home[data-cnl-home="pdf"] #cnlPdfBack,
body.view-home[data-cnl-home="notebook"] #cnlNbBack{display:none!important}
body.view-home[data-cnl-home="pdf"] #cnlPdfPath,
body.view-home[data-cnl-home="notebook"] #cnlNbPath{
  flex:1 1 auto;min-width:0;font:700 14px/1.2 "Averia Serif Libre",serif!important;
}
body.view-home[data-cnl-home="pdf"] #cnlPdfHeaderBar .icon-btn,
body.view-home[data-cnl-home="pdf"] #cnlPdfHeaderBar .cnl-nb-new,
body.view-home[data-cnl-home="notebook"] #cnlNbHeaderBar .icon-btn,
body.view-home[data-cnl-home="notebook"] #cnlNbHeaderBar .cnl-nb-new{
  height:28px!important;min-height:28px!important;flex:0 0 auto;
}
body.view-home[data-cnl-home="pdf"] .cnl-pdf-split{height:calc(100vh - 56px)!important;min-height:0}
body.view-home[data-cnl-home="notebook"] #homeScreen{
  padding:0!important;max-width:none!important;margin:0!important;
  min-height:calc(100vh - 40px)!important;
}
body.view-home[data-cnl-home="notebook"] #cnlNotebookShelf,
body.view-home[data-cnl-home="notebook"] #cnlNbBody{
  margin:0!important;padding:0!important;flex:1 1 auto;min-height:0;
}
body.view-home[data-cnl-home="notebook"] .cnl-nb-stage{
  height:calc(100vh - 40px)!important;min-height:0;
  padding:4px 0 8px!important;border-radius:0;
}
body.view-home[data-cnl-home="notebook"] .cnl-nb-sheet{
  margin:0 auto 8px!important;width:min(180mm,100%)!important;background:#F7F2E8!important;
}
#cnlNbTools{display:flex;align-items:center;gap:6px;flex:0 0 auto}
#cnlNbTools[hidden],
#cnlNbNew[hidden]{display:none!important}
body.view-home[data-cnl-home="notebook"] #cnlNbCount{
  min-width:0;font:600 12px/1 "Inter",system-ui,sans-serif;color:#5c627a;
  font-variant-numeric:tabular-nums;white-space:nowrap;
}
#homeScreen[data-cnl-home="landing"] #cnlHomeBack{display:none!important}
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-landing-title,
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-quick,
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-activity,
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-stats,
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-mode-sub{display:none!important}
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-modes{
  display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:6px;max-width:760px;
}
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-mode{
  min-height:0;padding:6px 10px;border-radius:7px;box-shadow:none;align-items:center;
  background:#fff;border:1px solid var(--cnl-line,#dde1ef);
}
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-mode-icon,
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-mode-go{display:none}
#homeScreen[data-cnl-home]:not([data-cnl-home="landing"]) .cnl-home-mode-name{
  font-size:12px;letter-spacing:.08em;
}

/* Each state shows exactly one body of content. Child selectors only, because
   Rapid Revision's own subject and chapter cards are .subject-card and
   .chapter-card living inside #cnlRapidBody and must not be caught here.

   One hide rule per panel naming the state that owns it, rather than a list per
   state: everything is shown by default and only ever hidden, so there is no rule
   here that has to put a display back. That matters for #subjectGrid, which the app
   lays out as a grid - a matching show rule would have to guess "grid" and would
   flatten it to a block the moment the guess was wrong.

   The activity panels are not in this list: save_js.py reparents them into
   #cnlHomeLanding, so they stop being children of #homeScreen and the child
   selectors that used to hide them per state would silently match nothing. The
   .cnl-home-activity rule above does that job now. */
/* ---- Slides ----------------------------------------------------------------

   A teaching deck, drawn in the snapshot's own language: a major heading in a
   coloured head band, the body on that section's wash, navy `Label:` openers,
   filled and hollow bullet markers and round-edged tables with a plum header.

   The card holds 16:9 whatever the window is, and every size on it is a share of
   the card's own width rather than of the viewport - that is what `container-type:
   size` and the cqw unit below are for - so the whole slide scales as one piece
   and a deck looks the same on any monitor. --fit is what the fitter steps down
   when a crowded card would otherwise be cut. */

.cnl-slide-backdrop{
  position:fixed; inset:0; z-index:130000;
  display:flex; flex-direction:column;
  background:#F5F4FA;
}
.cnl-slide-backdrop[hidden]{display:none}
/* !important because the app sets the reader's own overflow and would otherwise
   leave the note scrolling under a full-screen deck: the wheel would turn the page
   behind the card instead of doing nothing, and closing the deck would land the
   reader somewhere the user never went. */
body.cnl-slides-open{overflow:hidden !important}

.cnl-slide-bar{
  display:flex; align-items:center; gap:8px;
  padding:8px 14px;
  background:#FFFFFF;
  border-bottom:1px solid #E7E1E4;
  flex:none;
}
.cnl-slide-spacer{flex:1}
.cnl-slide-status{font-size:12px; color:#667395}
.cnl-slide-status.ok{color:#28467C; font-weight:600}
.cnl-slide-status.err{color:#8A2E3B; font-weight:600}

/* The stage is the query container the card is sized against. It has to be the
   stage and not the card: an element cannot query itself, so a card asking for a
   share of its own width would silently get a share of the window instead. */
.cnl-slide-stage{
  flex:1; min-height:0;
  display:flex; align-items:center; justify-content:center;
  padding:1.2vmin;
  container-type:size;
  --slide-scale:1;
}
.cnl-slide-empty{
  max-width:32em; text-align:center;
  font-size:15px; line-height:1.5; color:#667395;
}

.cnl-slide-nav{
  display:flex; align-items:center; justify-content:center; gap:14px;
  padding:6px 0 12px; flex:none;
}
.cnl-slide-count{font-size:12px; color:#667395; min-width:5em; text-align:center}

/* 16:9 whichever way the window is shaped: as wide as the stage allows, or as
   tall, whichever runs out first. The type is a share of the card's own width and
   is written in px by the player, which measures the card once it is laid out. */
.cnl-slide{
  width:min(100cqw, calc(100cqh * 16 / 9));
  height:min(100cqh, calc(100cqw * 9 / 16));
  background:#EDF2F9;
  border-radius:0.85em;
  box-shadow:0 1px 6px rgba(40,70,124,0.14);
  display:flex; flex-direction:column;
  position:relative; overflow:hidden;
}
.cnl-slide.even{background:#F2EEF0}
.cnl-slide.title-card{background:#FFFFFF; justify-content:center; padding:0 6%}

/* The head band is the snapshot's section head, carried by every card the
   heading runs across. */
.cnl-slide-head{
  display:flex; align-items:baseline; gap:0.7em;
  padding:0.75em 1.1em;
  background:#28467C; color:#FFFFFF;
  font-weight:700; font-size:1.2em; line-height:1.25;
}
.cnl-slide.even .cnl-slide-head{background:#6F3D5D}
.cnl-slide-head .cont{
  margin-left:auto; flex:none;
  font-weight:400; font-size:0.6em; opacity:0.85;
}

.cnl-slide-body{
  flex:1; min-height:0; overflow:hidden;
  padding:0.85em 1.25em 1.5em;
  line-height:1.32;
}
.cnl-slide-body.two-column{
  display:grid; grid-template-columns:1fr 1fr; gap:0 1.5em;
  align-content:start;
}
.cnl-slide-body.two-column .full{grid-column:1 / -1}

.cnl-slide-deck-title{
  margin:0; color:#28467C;
  font-weight:700; font-size:2.2em; line-height:1.12;
}
.cnl-slide-kicker{
  font-weight:700; font-size:0.62em;
  letter-spacing:.14em; text-transform:uppercase;
  color:#6F3D5D; margin-bottom:0.9em;
}
.cnl-slide-deck-sub{
  margin-top:0.7em; font-size:1em; line-height:1.35;
  color:#667395; max-width:80%;
}

/* An internal heading inside a card: the snapshot's group head. */
.cnl-slide-group-h{
  margin:0.55em 0 0.25em;
  font-weight:700; font-size:1.02em;
  color:#28467C; line-height:1.3;
}
.cnl-slide-group-h:first-child{margin-top:0}

.cnl-slide ul.cnl-slide-list,
.cnl-slide ol.cnl-slide-list{margin:0; padding:0 0 0 1.35em; list-style:none}
.cnl-slide ol.cnl-slide-list{list-style:decimal; padding-left:1.5em}
.cnl-slide li.cnl-slide-li,
.cnl-slide li.cnl-slide-num{margin:0 0 0.3em; padding:0; position:relative}
.cnl-slide li.cnl-slide-num::marker{font-weight:700; color:#28467C}

/* L1 a filled disc, L2 a hollow ring at the same marker size. */
.cnl-slide li.cnl-slide-li:not(.sub)::before{
  content:""; position:absolute; left:-1.05em; top:0.55em;
  width:0.35em; height:0.35em; border-radius:50%; background:currentColor;
}
.cnl-slide li.cnl-slide-li.sub::before{
  content:""; position:absolute; left:-1.05em; top:0.55em;
  width:0.4em; height:0.4em; border-radius:50%;
  border:1.2px solid currentColor; background:transparent;
}
.cnl-slide li.cnl-slide-li > ul.cnl-slide-list{
  list-style:none; margin:0.25em 0 0.45em; padding-left:0.95em; font-size:0.88em;
}

/* `Label:` = navy, **emphasis** = plum, exactly as on a snapshot. */
.cnl-slide .cnl-slide-label{color:#28467C; font-weight:700}
.cnl-slide-body strong,.cnl-slide-body b{color:#6F3D5D; font-weight:700}

.cnl-slide-table-title{
  text-align:center; font-weight:700; font-size:0.95em; margin:0.6em 0 0.25em;
}
.cnl-slide table.cnl-slide-table{
  width:100%; border-collapse:separate; border-spacing:0;
  border:0.5pt solid #AEAAAA; border-radius:0.7em; overflow:hidden;
  margin:0.35em 0 0.3em;
  font-size:0.82em; line-height:1.2;
  table-layout:fixed; color:#000; background:#FFFFFF;
}
.cnl-slide table.cnl-slide-table th,
.cnl-slide table.cnl-slide-table td{
  padding:0.45em 0.6em;
  border-right:0.5pt solid #AEAAAA;
  border-bottom:0.5pt solid #AEAAAA;
  vertical-align:top; word-wrap:break-word; overflow-wrap:anywhere;
}
.cnl-slide table.cnl-slide-table th:last-child,
.cnl-slide table.cnl-slide-table td:last-child{border-right:0}
.cnl-slide table.cnl-slide-table tr:last-child th,
.cnl-slide table.cnl-slide-table tr:last-child td{border-bottom:0}
.cnl-slide table.cnl-slide-table th{
  background:#6F3D5D; color:#FFFFFF; font-weight:700; vertical-align:middle;
}
.cnl-slide table.cnl-slide-table th strong,
.cnl-slide table.cnl-slide-table th b{color:#FFFFFF}
.cnl-slide table.cnl-slide-table td{background:#FFFFFF; color:#000}
.cnl-slide table.cnl-slide-table td strong,
.cnl-slide table.cnl-slide-table td b{color:#000}
.cnl-slide table.cnl-slide-table tr.stripe td{background:#E7E1E4}

.cnl-slide-flow{
  display:flex; align-items:stretch; justify-content:center; flex-wrap:wrap;
  gap:0.3em; margin:0.4em 0 0.3em;
}
.cnl-slide-flow-title{
  width:100%; text-align:center; font-weight:700; font-size:0.95em;
  color:#28467C; margin-bottom:0.15em;
}
.cnl-slide-step{
  flex:1 1 6.5em; min-width:5em; max-width:11em;
  background:#FFFFFF; border:0.5pt solid #AEAAAA; border-radius:0.6em;
  padding:0.42em 0.5em; text-align:center;
  font-size:0.82em; line-height:1.2; font-weight:700;
  display:flex; align-items:center; justify-content:center;
}
.cnl-slide-arrow{
  align-self:center; color:#6F3D5D; font-weight:700; font-size:1.05em; line-height:1;
}

/* A set-apart box inside the body: its heading over its own lines, lifted off the
   section wash the way a snapshot lifts a table. */
.cnl-slide-box{
  background:#FFFFFF; border:0.5pt solid #AEAAAA; border-radius:0.6em;
  padding:0.5em 0.7em; margin:0.5em 0 0.35em;
}
.cnl-slide-box-h{
  font-weight:700; font-size:0.95em; line-height:1.25;
  color:#28467C; margin-bottom:0.25em;
}
.cnl-slide-box-text{font-size:0.92em; line-height:1.3}
.cnl-slide-box ul.cnl-slide-list{font-size:0.92em}

.cnl-slide-key{
  margin:0.6em 1.25em 0;
  border-left:0.25em solid #6F3D5D; border-radius:0 0.5em 0.5em 0;
  background:#FFFFFF; padding:0.5em 0.7em;
  font-size:0.92em; line-height:1.3;
}
.cnl-slide-foot{
  position:absolute; right:1.2em; bottom:0.7em;
  color:#667395; font-weight:700; font-size:0.62em; line-height:1;
}

/* ---- The snapshot, on the master's own measurements -------------------------

   The palette already matched - both draw from the same colours.xml - so what was
   left apart was the geometry, and the desktop's was drawn a size down throughout:
   sharper corners, a smaller head, and a table two points under the phone's. These
   put the numbers back, in pt where the sheet is already in pt so the whole thing
   still scales off one root size.

   The title is the larger change. The phone gives a snapshot a navy plate across
   the top, which is what makes it read as a snapshot rather than as a short note;
   the desktop had it as plain dark text. */

#aiPosterBackdrop .ai-poster-title{
  display:block;
  margin:0 auto 12pt;
  max-width:100%;
  text-align:center;
  background:var(--poster-primary);
  color:var(--poster-white) !important;
  font-weight:700;
  font-size:15pt;
  line-height:1.25;
  padding:6.75pt 13.5pt;
  border-radius:9pt;
  white-space:normal;
}

/* Same 710px sheet as the notes reader (#paper in the Relaxed spec). The app
   pins min-width at 20cm, which is why a snapshot sat wider than the note it
   was made from; 0 min-width drops that pin. Side padding matches #paper. */
#aiPosterBackdrop .ai-poster-page{
  width:min(calc(100% - 60px),710px) !important;
  max-width:710px !important;
  min-width:0 !important;
  padding-left:30px !important;
  padding-right:30px !important;
}

/* One column. Newspaper flow is a leftover of the desktop poster; the master
   draws a snapshot as a single run of sections, the way a note is a single run
   of sections. !important because app.html sets column-count:2 on .ai-poster-flow
   and this sheet earlier pins only the gutter. */
#aiPosterBackdrop .ai-poster-flow,
#aiPosterBackdrop .ai-poster-page .ai-poster-flow,
#aiPosterBackdrop .ai-poster-flow.one-col{
  column-count:1 !important;
  -webkit-column-count:1 !important;
  column-gap:0 !important;
}

#aiPosterBackdrop .ai-poster-sections{ gap:10.5pt !important }
#aiPosterBackdrop .ai-poster-section{ border-radius:9pt }
#aiPosterBackdrop .ai-poster-section-head{
  padding:6.75pt 10.5pt !important;
  font-size:12pt !important;
  line-height:1.25 !important;
}
#aiPosterBackdrop .ai-poster-section-body{ padding:4.5pt 9pt 10.5pt !important }

/* Body type is the notes' own: 10pt / 1.55, written onto the page as
   --body-size / --body-lh by cnlApplyPosterType from the reader's Aa. The
   earlier calc(8.5pt * poster-token) rules are what made a snapshot read a
   size down from the note it summarises. */
#aiPosterBackdrop .ai-poster-page,
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul,
#aiPosterBackdrop .ai-poster-page .ai-poster-section ul ul,
#aiPosterBackdrop .ai-poster-page .ai-poster-numbered,
#aiPosterBackdrop .ai-poster-page .ai-poster-section p{
  font-size:var(--body-size) !important;
  line-height:var(--body-lh) !important;
}
#aiPosterBackdrop .ai-poster-page .ai-poster-subsection{
  font-size:11pt !important;
  line-height:var(--body-lh) !important;
  margin:10px 0 4px !important;
}

/* The master's list: L1 a filled disc, L2 a hollow ring. Gaps match the notes
   reader's L1 0.30em / L2 0.22em, moved by the same --cnl-para-scale. Native
   markers are turned off so the discs sit where Averia's first-line midline is. */
#aiPosterBackdrop .ai-poster-section ul{
  list-style:none !important;
  padding:0 0 0 1.35em !important;
  margin:0 !important;
}
#aiPosterBackdrop .ai-poster-section ul li{
  position:relative;
  margin:0 !important;
  padding:0 0 calc(0.30em * var(--cnl-para-scale,1)) !important;
}
#aiPosterBackdrop .ai-poster-section ul li::marker{content:none !important}
#aiPosterBackdrop .ai-poster-section ul li::before{
  content:"";
  position:absolute;
  left:-1.05em;
  top:0.55em;
  width:0.35em;
  height:0.35em;
  border-radius:50%;
  background:currentColor;
  box-sizing:border-box;
}
#aiPosterBackdrop .ai-poster-section ul ul{
  list-style:none !important;
  padding-left:0.65em !important;
  margin:0 !important;
  font-size:inherit !important;
}
#aiPosterBackdrop .ai-poster-section ul ul li{
  padding-bottom:calc(0.22em * var(--cnl-para-scale,1)) !important;
}
#aiPosterBackdrop .ai-poster-section ul ul li::before{
  width:0.4em;
  height:0.4em;
  border:1.2px solid currentColor;
  background:transparent;
}
#aiPosterBackdrop .ai-poster-section ul li:has(+ li) > ul > li:last-child{
  padding-bottom:calc(0.30em * var(--cnl-para-scale,1)) !important;
}
#aiPosterBackdrop .ai-poster-page .ai-poster-point-block + .ai-poster-point-block{
  margin-top:0 !important;
}

/* The phone's table: one point under the note's 105% rung, hairlined in grey on
   every inside edge, and rounded enough to sit inside a section without its
   corners fighting the box's. */
#aiPosterBackdrop .ai-poster-table{
  font-size:var(--table-size,10.025pt) !important;
  line-height:1.2 !important;
  border:0.5pt solid #AEAAAA;
  border-radius:7.5pt;
  color:#000;
}
#aiPosterBackdrop .ai-poster-table th,
#aiPosterBackdrop .ai-poster-table td{
  padding:6pt 7.5pt;
  border-right:0.5pt solid #AEAAAA;
  border-bottom:0.5pt solid #AEAAAA;
  overflow-wrap:anywhere;
}
#aiPosterBackdrop .ai-poster-table th:last-child,
#aiPosterBackdrop .ai-poster-table td:last-child{ border-right:0 }
#aiPosterBackdrop .ai-poster-table tr:last-child th,
#aiPosterBackdrop .ai-poster-table tr:last-child td{ border-bottom:0 }
#aiPosterBackdrop .ai-poster-table th{ vertical-align:middle }

/* A4 pages for the master's snapshot PDF. Padding lives on the page, not on
   @page, because Edge's --print-to-pdf with a zero margin is the only way to
   get the same 0.5cm / 1cm box the phone prints. The on-screen 710px / 30px
   pin has to be named with the same #aiPosterBackdrop prefix or it wins here
   and the A4 sheet starts 30px in from the left. */
#aiPosterBackdrop .ai-poster-page.paged{
  padding:0 !important;
  background:transparent !important;
  box-shadow:none !important;
  width:100% !important;
  max-width:none !important;
  min-width:0 !important;
  margin:0 auto !important;
}
.cnl-print-page{
  width:210mm;
  height:297mm;
  max-width:100%;
  margin:0 auto;
  padding:0.5cm 1cm 1cm;
  box-sizing:border-box;
  overflow:hidden;
  background:#fff;
}

/* Master's credit: hidden on the viewer, shown on the exported PDF under the
   title. Charcoal 10pt, Cortex in bold, Play mark sitting on the second line. */
.ai-poster-credit{
  display:none;
  text-align:center;
  color:#667395;
  font-size:10pt;
  line-height:1.35;
  margin:4px 0 12px;
  font-weight:400;
}
.ai-poster-credit .brand{color:#667395;font-weight:700}
.ai-poster-credit img.play-icon{
  height:1.15em;width:1.15em;vertical-align:-0.15em;margin-left:0.3em;
}
.cnl-print-page .ai-poster-credit{display:block !important}
@media print{
  @page{size:A4;margin:0}
  html,body{background:#fff;width:100%;margin:0;padding:0}
  .ai-poster-credit{display:block !important}
  .cnl-print-page{
    page-break-after:always;
    break-after:page;
  }
  .cnl-print-page:last-child{
    page-break-after:auto;
    break-after:auto;
  }
}

/* ---- The note, drawn the way the master draws it ---------------------------

   The desktop and the phone render notes from the same page, so most of this
   already matches. What the phone adds on top is one stylesheet, and these are
   the parts of it that are about how a note looks rather than about being on
   Android: the paper staying white and the contents panel staying put are this
   app's business, so those rules are left out.

   Three things change. Word's space-before and space-after go, leaving the line
   box to do the spacing, with the gaps that actually read put back by hand
   between bullet levels. The two heading bars go up two points, because the page
   writes both at 12pt and a note's H2 and H3 sit above that. And the bullet
   markers are sized in em rather than px, so they scale with the type. */

/* Same as Master: the whole note stays on screen. The page still marks every
   other H1 section .cnl-section-hidden when a heading is opened; that hide is
   what left H1/H2 bars missing from the viewer. */
body.view-reader .doc-root > .cnl-section-hidden,
body.view-reader .doc-root .cnl-section-hidden,
body.view-reader .cnl-section-hidden{
  display:revert !important;
}
body.view-reader #paper .doc-p.h1,
body.cnl-reading-view #paper .doc-p.h1{
  background:#5C3A52 !important;
  background-color:#5C3A52 !important;
  color:#FFFFFF !important;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}
body.view-reader #paper .doc-p.h2,
body.cnl-reading-view #paper .doc-p.h2{
  background:#E7E6F0 !important;
  background-color:#E7E6F0 !important;
  color:#1F3864 !important;
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}

/* Body air off: only the line box spaces ordinary blocks. Headings and bold
   side headings keep the page's own --before/--after. */
:root{ --body-gap:0px }
.doc-root .doc-block:not(.h1):not(.h2):not(.h3):not(.h4):not(.boldside1):not(.boldside2):not(.boldside3){
  --before:0px; --after:0px;
  padding-top:0 !important; padding-bottom:0 !important;
}
/* A small gap after a Level-1 bullet, unless a Level-2 follows it. */
.doc-root .doc-block:has(> .doc-list[data-list-level="0"]):not(:has(+ .doc-block:has(> .doc-list[data-list-level="1"]))),
.doc-root .doc-block:has(> .doc-p.doc-list[data-list-level="0"]):not(:has(+ .doc-block:has(> .doc-p.doc-list[data-list-level="1"]))){
  padding-bottom:0.025em !important;
}
/* Level-2 back out to a Level-1, or on to a numbered list. */
.doc-root .doc-block:has(> .doc-list[data-list-level="1"]):has(+ .doc-block:has(> .doc-list[data-list-level="0"])),
.doc-root .doc-block:has(> .doc-p.doc-list[data-list-level="1"]):has(+ .doc-block:has(> .doc-p.doc-list[data-list-level="0"])),
.doc-root .doc-block:has(> .doc-list[data-list-level="1"]):has(+ .doc-block:has(> .doc-list .list-marker.is-number)),
.doc-root .doc-block:has(> .doc-p.doc-list[data-list-level="1"]):has(+ .doc-block:has(> .doc-p.doc-list .list-marker.is-number)){
  padding-bottom:0.5em !important;
}

/* The two heading bars, two points up. Inside a table a heading keeps the
   cell's type, or one bar would blow the column open. */
.doc-root .doc-p.h2, .doc-root .doc-p.h3{ font-size:14pt !important }
.doc-root .doc-p.h2 *, .doc-root .doc-p.h3 *{ font-size:inherit !important }
.doc-root td .doc-p.h2, .doc-root td .doc-p.h3,
.doc-root th .doc-p.h2, .doc-root th .doc-p.h3{ font-size:9.5pt !important }

/* L1 filled disc, L2 hollow ring, both in em so they follow the type. Nudged
   onto Averia's first-line midline, which the geometric centre reads above. */
.doc-root .doc-list .list-marker.is-bullet{
  align-items:flex-start !important; padding-top:0.5em !important;
}
.doc-root .doc-list[data-list-level="0"] .list-marker.is-bullet::before{
  width:0.35em !important; height:0.35em !important; flex:0 0 0.35em !important;
  box-sizing:border-box !important; border-radius:50% !important;
  background:currentColor !important; border:none !important;
}
.doc-root .doc-list[data-list-level="1"] .list-marker.is-bullet::before{
  width:0.4em !important; height:0.4em !important; flex:0 0 0.4em !important;
  box-sizing:border-box !important; border-radius:50% !important;
  border:1.2px solid currentColor !important; background:transparent !important;
}

/* A first-level bold side heading and everything under it, drawn as one of a
   snapshot's sections: the heading in its own colour over a wash, the content
   inset inside the box, and the tone stepping navy / plum down the note so two
   sections never touch in the same colour. save_js.py puts the wrapper in. */
.doc-root .cnl-bs-section{
  margin:0.5em 0 0.7em !important;
  border-radius:10px; overflow:hidden; background:#EDF2F9 !important;
}
.doc-root .cnl-bs-section[data-tone="1"]{ background:#F2EEF0 !important }
.doc-root .cnl-bs-section > .doc-block.boldside1{
  --before:0px; --after:0px;
  padding-left:12px !important; padding-right:12px !important;
  background:transparent !important;
}
.doc-root .cnl-bs-section > .doc-block.boldside1 > .doc-p.boldside1,
.doc-root .cnl-bs-section > .doc-block.boldside1 > .doc-p.boldside1 *{
  color:#28467C !important;
  background:transparent !important; background-color:transparent !important;
}
.doc-root .cnl-bs-section[data-tone="1"] > .doc-block.boldside1 > .doc-p.boldside1,
.doc-root .cnl-bs-section[data-tone="1"] > .doc-block.boldside1 > .doc-p.boldside1 *{
  color:#6F3D5D !important;
}
.doc-root .cnl-bs-section > .doc-block.boldside1 > .doc-p.boldside1{
  border-bottom:2px solid #28467C !important;
}
.doc-root .cnl-bs-section[data-tone="1"] > .doc-block.boldside1 > .doc-p.boldside1{
  border-bottom-color:#6F3D5D !important;
}
.doc-root .cnl-bs-section > .doc-block:not(.boldside1){
  padding-left:12px !important; padding-right:12px !important;
}

/* Plum is Word's Emphasis, which the user's own notes use too, so the bold
   belongs only to the notes the AI wrote. */
#paper.cnl-ai-note [data-word-character-style="Emphasis"],
#paper.cnl-ai-note [data-word-character-style="emphasis"]{ font-weight:700 !important }

/* Put the hidden attribute back in charge of the reader's toolbar.

   The app shows its reader-only buttons with `display:flex !important`, which a
   toolbar of permanent buttons never noticed. Several of them are not permanent:
   Save in My Notes and the saved-snapshot button ship with `hidden` set and are
   meant to appear only once there is something to save or to show. An attribute
   cannot beat !important, so both sat there on every note and the Save button
   answered with "Open an AI-generated note first" when pressed.

   Specificity, not another !important, is what settles it: this is one class more
   specific than the rule it has to beat, so the button obeys its own hidden flag
   again and nothing else about the toolbar changes. */
body.view-reader .reader-only[hidden]{display:none !important}
body.view-reader #cnlNoteZoom{display:flex!important}
body:not(.view-reader) #cnlNoteZoom{display:none!important}

/* Page zoom grows the sheet. Clip would hide the extra width; pan instead. */
body.cnl-page-zoomed .reader-main,
body.cnl-page-zoomed .reader-main .stage,
body.cnl-snapshot-zoomed #aiPosterBackdrop .ai-poster-scroll{
  overflow-x:auto!important;
}

#homeScreen[data-cnl-home]:not([data-cnl-home="deep"]) > .screen-heading,
#homeScreen[data-cnl-home]:not([data-cnl-home="deep"]) > #subjectGrid,
#homeScreen[data-cnl-home]:not([data-cnl-home="deep"]) > #cnlDeepNewNoteHost,
#homeScreen[data-cnl-home]:not([data-cnl-home="deep"]) > .home-actions,
#homeScreen[data-cnl-home]:not([data-cnl-home="rapid"]) > #cnlRapidRevision,
#homeScreen[data-cnl-home]:not([data-cnl-home="pdf"]) > #cnlPdfShelf,
#homeScreen[data-cnl-home]:not([data-cnl-home="notebook"]) > #cnlNotebookShelf,
#homeScreen[data-cnl-home]:not([data-cnl-home="performance"]) > #cnlPerformance{
  display:none!important;
}

.cnl-deep-new-note{margin:0 0 14px}
.cnl-new-note-btn{min-height:40px}
.cnl-new-note-modal .cnl-new-note-actions{
  display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;
}
.cnl-new-note-paste{
  display:block;width:100%;min-height:160px;margin:10px 0 0;padding:10px;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:8px;resize:vertical;
  font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;
}
.cnl-new-note-paste[hidden]{display:none}

/* Deep Dive keeps the action strip for #formattedSaveStatus alone, the one line
   of the app's browser furniture that still says something true: how many notes
   the library scan found. Every button in the two rows above it has moved to the
   landing or been hidden as browser-only, so the rows go and the divider's air
   comes down to meet the text. */
.home-actions{margin-top:16px!important;padding-top:10px!important}
.home-actions .master-folder-row{display:none!important}

/* ---- Rapid Revision: the saved-poster browser ---------------------------- */
.cnl-rapid-bar{
  position:relative;z-index:6;
  display:flex;align-items:center;gap:7px;margin:0 0 13px;padding-bottom:10px;
  border-bottom:1px solid var(--cnl-line,#dde1ef);
}
.cnl-rapid-path{
  flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  color:var(--cnl-ink,#292664);font:700 20px/1.2 "Averia Serif Libre",serif;
}
.cnl-rapid-list{display:flex;flex-direction:column;gap:13px}
/* The row is the positioned ancestor and the button inside it is what opens the
   poster, because a poster can also be renamed and deleted from here and a button
   cannot contain one. 84px on the right clears the two 30px actions and their 12px
   inset, so a long poster name does not run underneath them when they appear. */
.cnl-rapid-row{position:relative}
.cnl-rapid-item{
  display:flex;flex-direction:column;align-items:flex-start;gap:6px;width:100%;
  padding:17px 84px 17px 17px;text-align:left;cursor:pointer;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:9px;background:#fff;
  font-family:inherit;color:var(--cnl-ink,#292664);
  transition:border-color .16s ease,box-shadow .16s ease;
}
.cnl-rapid-item:hover{border-color:var(--cnl-coral,#e9a8a3);box-shadow:0 10px 24px rgba(85,43,47,.12)}
.cnl-rapid-item-name{font:700 16px/1.3 "Averia Serif Libre",serif}
.cnl-rapid-item-meta{font-size:12px;color:#5c627a}
/* Revealed rather than permanent, for the reason the app's own card actions are:
   the list should read as a list. opacity keeps the buttons from reflowing the row
   and pointer-events stops an invisible one being clicked; focus-within keeps them
   reachable from the keyboard. */
.cnl-rapid-actions{
  position:absolute;top:50%;right:12px;transform:translateY(-50%);
  display:flex;gap:6px;
  opacity:0;pointer-events:none;transition:opacity .13s ease;
}
.cnl-rapid-row:hover .cnl-rapid-actions,
.cnl-rapid-row:focus-within .cnl-rapid-actions{opacity:1;pointer-events:auto}

/* ---- PDFs: the shelf and the reader ----------------------------------------
   The shelf borrows Rapid Revision's bar and rows outright, so a list of books
   reads the same as a list of snapshots. Only the reader below is new.

   The reader scrolls in its own box rather than in the page. The column has to be
   the scroll container for the page observer to have something to measure against,
   and a viewer whose toolbar scrolls away with the pages would put the zoom out of
   reach exactly when it is wanted. */
.cnl-pdf-group{
  margin:6px 0 -4px;font:700 12px/1.4 "Inter",system-ui,sans-serif;
  letter-spacing:.09em;text-transform:uppercase;color:#7b819c;
}
.cnl-pdf-zoom{display:flex;align-items:center;gap:4px;flex:0 0 auto}
#cnlPdfZoom[hidden]{display:none!important}
#cnlPdfZoom:not([hidden]){display:flex!important}
.cnl-pdf-zoom-level{
  min-width:44px;text-align:center;font:600 12px/1 "Inter",system-ui,sans-serif;
  color:#5c627a;font-variant-numeric:tabular-nums;
}
/* Fixed against the viewport rather than sized by content: the column is a scroller
   and a scroller with no height of its own grows to fit every page instead. */
.cnl-pdf-split{display:flex;gap:14px;height:calc(100vh - 250px);min-height:340px;overflow-x:hidden}
.cnl-pdf-outline{
  position:fixed!important;top:40px;right:0;bottom:0;width:min(300px,86vw);
  z-index:120000;margin:0;padding:12px 8px 24px;overflow:auto;
  background:var(--poster-page,#fff);
  border:0;border-left:1px solid var(--cnl-line,#dde1ef)!important;
  box-shadow:-10px 0 28px rgba(41,38,100,.06);
  transform:translateX(100%);opacity:0;pointer-events:none;
  transition:transform .2s ease,opacity .16s ease;
}
.cnl-pdf-outline[hidden]{display:block!important}
body.cnl-pdf-outline-open .cnl-pdf-outline,
.cnl-pdf-outline:not([hidden]){
  transform:translateX(0);opacity:1;pointer-events:auto;
}
.cnl-pdf-outline-list{display:flex;flex-direction:column;gap:1px}
.cnl-pdf-outline-item{
  padding:7px 10px;text-align:left;border:0;border-radius:6px;background:none;
  cursor:pointer;font:500 13px/1.35 "Inter",system-ui,sans-serif;
  color:var(--cnl-ink,#292664);
}
.cnl-pdf-outline-item:hover{background:rgba(233,168,163,.16)}
.cnl-pdf-column{
  flex:1 1 auto;min-width:0;overflow-x:hidden;overflow-y:auto;overscroll-behavior-x:none;
  display:flex;flex-direction:column;align-items:center;padding:2px 2px 30px;background:#f3f4f8;
  border-radius:9px;
}
.cnl-pdf-stack{
  flex:0 0 auto;max-width:none;display:flex;flex-direction:column;align-items:stretch;gap:14px;
}
/* padding-top carries the page's aspect, so the slot stands at its full height
   before its image exists and the scrollbar does not move as pages arrive.
   Width is set in px on the stack; zoom is CSS zoom, same as notes. */
.cnl-pdf-page{
  position:relative;flex:0 0 auto;width:100%;max-width:none;height:0;background:#fff;
  box-shadow:0 2px 10px rgba(41,38,100,.13);
}
.cnl-pdf-image{
  position:absolute;inset:0;width:100%;height:100%;display:block;
  opacity:0;transition:opacity .18s ease;
}
.cnl-pdf-page.cnl-on .cnl-pdf-image{opacity:1}
/* The number shows through an undrawn page and is covered by a drawn one, which is
   what makes an unrendered slot read as "page 40, coming" and not as a blank. */
.cnl-pdf-number{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  font:600 13px/1 "Inter",system-ui,sans-serif;color:#9aa0b8;
}
.cnl-pdf-failed{background:#fdf1f0}

/* ---- Notebooks: blank paper filed beside the PDFs --------------------------
   The shelf rows are the PDF shelf's, so the two lists read as one. What is new is
   the sheet: one page at a time, A4, and the host the ink controller draws on. */
.cnl-nb-head{display:flex;align-items:center;justify-content:space-between;gap:10px}
.cnl-pdf-subgroup{padding-left:2px;opacity:.85}
.cnl-nb-empty{padding:2px 2px 6px}
.cnl-nb-new{
  padding:5px 11px;border:1px solid var(--cnl-line,#dde1ef);border-radius:7px;
  background:#fff;cursor:pointer;color:var(--cnl-ink,#292664);
  font:600 12px/1 "Inter",system-ui,sans-serif;letter-spacing:.02em;
  text-transform:none;
}
.cnl-nb-new:hover{border-color:var(--cnl-coral,#e9a8a3)}
.cnl-nb-bar{
  position:relative;z-index:6;
  display:flex;align-items:center;gap:9px;margin:0 0 13px;
}
.cnl-nb-count{
  font:600 13px/1 "Inter",system-ui,sans-serif;color:#5c627a;
  font-variant-numeric:tabular-nums;min-width:112px;
}
.cnl-nb-stage{
  display:flex;justify-content:center;overflow:auto;padding:0 0 26px;
  height:calc(100vh - 290px);min-height:320px;background:#f3f4f8;border-radius:9px;
}
/* The ink controller measures its canvases off this box, so it has to be the
   positioned ancestor and it has to have a height before they are sized. The
   aspect-ratio is set inline by the view; the width here is what gives it one. */
.cnl-nb-sheet{
  position:relative;width:min(180mm,100%);height:auto;margin:14px 0;background:#F7F2E8;
  box-shadow:0 2px 12px rgba(41,38,100,.15);flex:0 0 auto;align-self:flex-start;
  overflow:hidden;
}
/* Ruled paper matches Master: 8 mm pitch, 12 mm from the top, 10 mm from the
   edges, cream sheet, blue-grey rules. */
.cnl-nb-ruled{background-color:#F7F2E8;background-image:none}
.cnl-nb-ruled::before{
  content:"";position:absolute;top:12mm;right:10mm;bottom:10mm;left:10mm;
  pointer-events:none;z-index:0;
  background-image:repeating-linear-gradient(
    to bottom,#B7C6DA 0,#B7C6DA 1px,transparent 1px,transparent 8mm);
}

/* ---- Performance: the quiz and flashcard report ----------------------------
   The bar is Rapid Revision's, so the title sits where a title sits and the way out
   of the tab is the switcher above it rather than a second back arrow.

   Two halves, and they are not the same shape. Quizzes are dated events, so that half
   gets a trend. Flashcards keep only each card's present state and the last time it
   was reviewed, so that half gets totals and a split - no series, because the days
   behind it were never written down. */
.cnl-perf-bar{
  display:flex;align-items:center;gap:9px;margin:0 0 13px;padding-bottom:10px;
  border-bottom:1px solid var(--cnl-line,#dde1ef);
}
.cnl-perf-path{
  color:var(--cnl-ink,#292664);font:700 20px/1.2 "Averia Serif Libre",serif;
}
.cnl-perf-stamp{
  flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-size:12.5px;color:#5c627a;text-align:right;
}
.cnl-perf-body{display:flex;flex-direction:column;gap:19px}
.cnl-perf-section{display:flex;flex-direction:column;gap:11px}
.cnl-perf-heading{
  margin:0;color:var(--cnl-ink,#292664);
  font:700 17px/1.2 "Averia Serif Libre",serif;letter-spacing:.05em;
}
.cnl-perf-note{margin:0;max-width:74ch;font-size:12.5px;line-height:1.5;color:#5c627a}
.cnl-perf-subhead{
  margin:6px 0 0;font-size:10.5px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:#5c627a;
}

/* The landing's .cnl-home-stat supplies the box, so these tiles and the two on the
   landing are one kind of thing. The hint needs two classes to win: the landing's
   own ".cnl-home-stat span" rule sets 12.5px on every span in the tile, and one class
   would lose to it on specificity rather than on order. */
.cnl-perf-tiles{display:flex;flex-wrap:wrap;gap:9px}
.cnl-perf-tile{flex:1 1 148px;min-width:0}
.cnl-perf-tile .cnl-perf-hint{font-size:11.5px;line-height:1.4;color:#7b8199}

/* Accuracy by day. A percentage of the track rather than a height scaled against the
   best day, so the bars mean the same thing in every column and the series needs no
   maximum told to it. grid-auto-flow keeps one column per day without wrapping: the
   server caps the series at a fortnight, which fits the narrowest window this ships in. */
.cnl-perf-series{
  display:grid;grid-auto-flow:column;grid-auto-columns:minmax(18px,1fr);
  gap:5px;align-items:end;
}
.cnl-perf-day{display:flex;flex-direction:column;align-items:center;gap:5px;min-width:0;width:100%}
.cnl-perf-bar{
  position:relative;width:100%;height:62px;overflow:hidden;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:6px;background:#f2f4fb;
}
.cnl-perf-bar::after{
  content:'';position:absolute;left:0;right:0;bottom:0;height:var(--cnl-fill,0%);
  background:var(--cnl-ink,#292664);
}
.cnl-perf-day-label{
  max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-size:10px;color:#7b8199;font-variant-numeric:tabular-nums;
}

/* Recent quizzes. A grid rather than a table so the note name can be ellipsised: a
   table cell will not truncate without a max-width hack that guesses at the layout,
   while minmax(0,1fr) gives the name exactly what is left and no more. */
.cnl-perf-list{
  display:flex;flex-direction:column;overflow:hidden;background:#fff;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:10px;
}
.cnl-perf-row{
  display:grid;grid-template-columns:74px minmax(0,1fr) 56px 44px;
  align-items:center;gap:9px;padding:8px 11px;
  border-top:1px solid var(--cnl-line,#dde1ef);
}
.cnl-perf-row:first-child{border-top:0}
.cnl-perf-when{font-size:12px;color:#7b8199;white-space:nowrap}
.cnl-perf-what{
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-size:13px;color:var(--cnl-ink,#292664);
}
.cnl-perf-score{
  font:700 13px/1 "Averia Serif Libre",serif;color:var(--cnl-ink,#292664);
  font-variant-numeric:tabular-nums;text-align:right;
}
.cnl-perf-pct{
  font-size:12px;color:#5c627a;text-align:right;font-variant-numeric:tabular-nums;
}

/* Where the cards are: one hue darkening as a card progresses, so the ramp reads as
   the order it happens in rather than as three unrelated categories. */
.cnl-perf-split{display:flex;flex-direction:column;gap:7px}
.cnl-perf-split-bar{
  display:flex;height:14px;overflow:hidden;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:7px;background:#f2f4fb;
}
.cnl-perf-slice{display:block;height:100%}
.cnl-perf-legend{display:flex;flex-wrap:wrap;gap:13px}
.cnl-perf-chip{display:flex;align-items:center;gap:5px;font-size:12px;color:#5c627a}
.cnl-perf-dot{display:block;width:9px;height:9px;border-radius:3px}
.cnl-perf-new{background:#b9d0ef}
.cnl-perf-learning{background:var(--cnl-sky,#7aa7e0)}
.cnl-perf-mature{background:var(--cnl-ink,#292664)}

/* The deck table. Numbers are right-aligned and tabular so two decks can be compared
   down a column; the deck name is allowed to wrap, for the reason the list above is a
   grid - truncating it would need the same guess. */
.cnl-perf-table{width:100%;border-collapse:collapse;background:#fff;font-size:12.5px}
.cnl-perf-table th,
.cnl-perf-table td{
  padding:7px 9px;text-align:left;
  border-bottom:1px solid var(--cnl-line,#dde1ef);
}
.cnl-perf-table thead th{
  font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  color:#5c627a;border-bottom-color:var(--cnl-slate,#b9bfd3);
}
.cnl-perf-table tbody tr:last-child th,
.cnl-perf-table tbody tr:last-child td{border-bottom:0}
.cnl-perf-table tbody th{font-weight:500;line-height:1.35;color:var(--cnl-ink,#292664)}
.cnl-perf-num{
  text-align:right;white-space:nowrap;color:#3d4358;font-variant-numeric:tabular-nums;
}

/* ---- COLUMN SCALE ----------------------------------------------------------
   The app-authored sizes the 1000px column scales. They come from three
   separate blocks of app.html and each needs !important to beat the last of
   them, so they are gathered here rather than edited in place. The rule and its
   reasoning are at the .screen-area cap at the top of this sheet: geometry and
   display type above 20px take the ratio, everything else stays.

   Scoped to min-width:901px because that is where the app's own narrow-screen
   tuning stops - it drops this padding to 28px 16px 54px at 900px, to 30px on
   top at 700px and to 10px either side at 560px, and collapses both grids to a
   single column. An unscoped !important here would beat all three and leave a
   phone-width window with desktop margins.

   The chapter card's right padding is the one exception to the ratio. It is not
   air: .chapter-actions is absolutely positioned at top:12px right:12px holding
   a 30px button, and 12+30+12 is exactly the 54px the card reserves. Taking
   5/7 of it would put the hover-only rename and delete controls on top of the
   chapter title.

   The card padding and the grid gaps are a second exception, in the other
   direction. The user asked for the pills under Deep Dive and Rapid Revision to
   carry the same padding the landing pills have, so rather than each surface
   taking 5/7 of whatever it happened to be, all of them take the landing pill's
   own scaled values: 17px of padding and a 13px gap. */
@media(min-width:901px){
  .home-screen,.subject-screen{padding:34px 20px 51px!important}
  .screen-heading{margin-bottom:17px!important;padding-bottom:10px!important}
  .screen-heading h1{font-size:23px!important}

  .subject-grid{
    grid-template-columns:repeat(auto-fill,minmax(164px,1fr))!important;
    gap:13px!important;
  }
  .subject-card{min-height:104px!important;padding:17px!important;border-radius:11px!important}
  .subject-icon{width:27px!important;height:27px!important;border-radius:7px!important}
  .subject-name{margin-top:14px!important}
  .subject-count{margin-top:4px!important}

  .chapter-grid{
    grid-template-columns:repeat(auto-fill,minmax(214px,1fr))!important;
    gap:13px!important;
  }
  .chapter-card{padding:17px 54px 17px 17px!important;border-radius:10px!important}
  .chapter-name{margin-top:6px!important}

  .master-folder-button{min-width:150px!important;min-height:33px!important}
  .master-folder-help{max-width:443px!important}
}

/* ---- THE TWO COLOUR FAMILIES -----------------------------------------------
   Deep Dive is blue and Rapid Revision is red, so a card says which half of the
   library it belongs to before its label has been read. The chooser on the
   landing is washed the same way and the colour then carries into everything
   that mode opens. HOME stays white: it is the way out of both, and tinting it
   would make three families where the user asked for two.

   Both washes are the app's own palette colours thinned against white rather
   than new hexes, so they follow --cnl-mist and --cnl-coral if those are ever
   retuned. 20% is the resting wash and 34% the hover or the marked pill, which
   is the step the app already takes between a card and its highlight.

   The Rapid Revision selectors have to name #cnlRapidBody. Its folder levels
   reuse the app's own .subject-card and .chapter-card - the same classes Deep
   Dive shows - so an unscoped rule would paint both halves one colour. And each
   family restates its hover background because the app's .chapter-card:hover
   paints var(--cnl-paper), a lilac-grey that would take a red card grey under
   the cursor. */
#cnlHomeDeepDive,
#homeScreen[data-cnl-home="deep"] #subjectGrid .subject-card,
#subjectScreen .chapter-card{
  background:color-mix(in srgb,var(--cnl-mist,#b5ccf1) 20%,#fff)!important;
}
#cnlHomeDeepDive:hover,
#cnlHomeDeepDive.cnl-active,
#homeScreen[data-cnl-home="deep"] #subjectGrid .subject-card:hover,
#subjectScreen .chapter-card:hover{
  background:color-mix(in srgb,var(--cnl-mist,#b5ccf1) 34%,#fff)!important;
}

#cnlHomeRapidRevision,
#cnlRapidBody .subject-card,
#cnlRapidBody .chapter-card,
#cnlRapidBody .cnl-rapid-item{
  background:color-mix(in srgb,var(--cnl-coral,#e9a8a3) 20%,#fff)!important;
}
#cnlHomeRapidRevision:hover,
#cnlHomeRapidRevision.cnl-active,
#cnlRapidBody .subject-card:hover,
#cnlRapidBody .chapter-card:hover,
#cnlRapidBody .cnl-rapid-item:hover{
  background:color-mix(in srgb,var(--cnl-coral,#e9a8a3) 34%,#fff)!important;
  border-color:var(--cnl-coral,#e9a8a3)!important;
}

/* ---------- ink: handwriting over a note ----------

   Two canvases rather than one, because a wash highlighter belongs behind the
   glyphs and a pen belongs over them. Painting both on one canvas would put the
   wash on top, where it greys the very words it is meant to mark. The stacking is
   the whole reason for the pair: wash at 0, the note's own text at 1, pen at 2.

   .paper becomes the positioning parent. It already contains the note and already
   scrolls with it, so a canvas laid over it stays glued to the text through a
   window resize and through the browser's own zoom without anything having to
   recompute a transform.

   Neither canvas ever takes a pointer. Drawing is listened for on .paper itself,
   so a finger or a wheel still scrolls the note while a tool is selected, and only
   a pen or a held mouse button draws. */
.paper{position:relative}
.paper .doc-root{position:relative;z-index:1}
.cnl-ink-layer{
  position:absolute;top:0;left:0;
  pointer-events:none;
  touch-action:none;
}
.cnl-ink-wash{z-index:0}
.cnl-ink-pen{z-index:2}

/* The note stops selecting under a live tool. Without this a drag with the mouse
   held down paints a stroke and sweeps a text selection under it at the same
   time, and the selection's blue wins the repaint. */
body.cnl-inking .paper .doc-root{user-select:none!important;-webkit-user-select:none!important}

/* The palette. Anchored to the reader's right edge, clear of the sidebar toggle,
   and only ever present in the reader. */
#cnlInkBar{
  position:fixed;right:14px;top:50%;transform:translateY(-50%);
  z-index:120001;
  display:none;flex-direction:column;gap:6px;
  padding:7px 6px;
  background:#FFFFFF;
  border:1px solid #E3E3E6;border-radius:13px;
  box-shadow:0 6px 22px rgba(0,0,0,.13);
}
body.view-reader #cnlInkBar{display:flex}

/* z-index 120001 puts the bar over the snapshot sheet's 120000, so a note can be
   annotated with the sheet open. The sheet is its own surface and keeps its own
   ink, which is why the bar stays reachable rather than being hidden behind it. */
#cnlInkBar .cnl-ink-btn{
  width:30px;height:30px;padding:0;
  display:flex;align-items:center;justify-content:center;
  background:#FFFFFF;
  border:1px solid #E3E3E6;border-radius:9px;
  cursor:pointer;
  transition:border-color .12s,background .12s;
}
#cnlInkBar .cnl-ink-btn:hover{border-color:#B9B9C0}
#cnlInkBar .cnl-ink-btn[aria-pressed="true"]{
  border-color:#555879;box-shadow:inset 0 0 0 1px #555879;
}
#cnlInkBar .cnl-ink-btn[disabled]{opacity:.34;cursor:default}
#cnlInkBar .cnl-ink-btn[disabled]:hover{border-color:#E3E3E6}

/* A tool's swatch is the colour it draws in, so the row reads as the marks it
   makes rather than as a list of names. A wash is a filled tile because that is
   how it lands on the page; an underliner is a bar for the same reason. */
#cnlInkBar .cnl-ink-swatch{display:block;border-radius:3px}
#cnlInkBar .cnl-ink-nib{width:13px;height:13px;border-radius:50%}
#cnlInkBar .cnl-ink-wash-chip{width:17px;height:13px;border:1px solid rgba(0,0,0,.14)}
#cnlInkBar .cnl-ink-rule{width:17px;height:4px;border-radius:2px}
#cnlInkBar .cnl-ink-sep{height:1px;margin:2px 3px;background:#E9E9EC}
#cnlInkBar .cnl-ink-btn svg{display:block;width:15px;height:15px}

/* ---- Canvas only ------------------------------------------------------------
   Notes, PDFs and notebooks can drop the library chrome so the page fills the
   window. The remaining bar is Pen, page options (Aa or zoom), outline, and Exit. */
body:not(.cnl-canvas-mode) .cnl-canvas-exit{display:none!important}
body.cnl-canvas-mode .cnl-canvas-enter{display:none!important}
body.cnl-canvas-mode .cnl-canvas-exit{display:inline-flex!important}

body.cnl-canvas-mode .cnl-app-title,
body.cnl-canvas-mode #breadcrumb,
body.cnl-canvas-mode .top-left-nav,
body.cnl-canvas-mode #cnlTopReadControl,
body.cnl-canvas-mode #aiPosterTopBtn,
body.cnl-canvas-mode #cnlSlidesTopBtn,
body.cnl-canvas-mode #aiFlashcardsTopBtn,
body.cnl-canvas-mode #aiQuizTopBtn,
body.cnl-canvas-mode #aiToolsBtn,
body.cnl-canvas-mode #aiSavedPosterBtn,
body.cnl-canvas-mode #saveGeneratedAiDocxBtn,
body.cnl-canvas-mode #cnlMoreBtn,
body.cnl-canvas-mode #cnlHomeLanding,
body.cnl-canvas-mode .cnl-credit,
body.cnl-canvas-mode #cnlPdfBack,
body.cnl-canvas-mode #cnlPdfPath,
body.cnl-canvas-mode #cnlPdfImport,
body.cnl-canvas-mode #cnlPdfRefresh{
  display:none!important;
}

body.cnl-canvas-mode .screen-area{
  max-width:var(--cnl-ui-width)!important;margin:0 auto!important;
}

/* Window mode: keep the original 710px sheet when the window is wider.
   The spec used min(100% - 60px, 710px) plus stage side padding, so a
   narrower window still showed a gutter. Side padding is zeroed and the
   sheet is min(100%, 710px): full width below 710px, original size above. */
body.view-reader:not(.cnl-canvas-mode) .reader-main .stage,
body.view-reader:not(.cnl-canvas-mode) .stage{
  max-width:none!important;
  padding-left:0!important;
  padding-right:0!important;
}
body.view-reader:not(.cnl-canvas-mode).cnl-reading-view #paper,
body.view-reader:not(.cnl-canvas-mode).cnl-reading-view #paper.paper,
body.view-reader:not(.cnl-canvas-mode) .reader-main .paper{
  width:min(100%,710px)!important;
  max-width:710px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}

/* Notes: slim header, page fills the shared content column. */
body.cnl-canvas-mode.view-reader .app-header{
  position:sticky;top:0;z-index:100200;
  display:flex!important;align-items:center;justify-content:flex-end;gap:8px;
  padding:6px 12px!important;padding-left:12px!important;
  background:rgba(242,244,247,.96);
}
body.cnl-canvas-mode.view-reader .app-header-left,
body.cnl-canvas-mode.view-reader .app-brand-wrap,
body.cnl-canvas-mode.view-reader .breadcrumb-row{
  display:contents;
}
body.cnl-canvas-mode.view-reader .reader-header-actions{
  position:static!important;height:auto!important;right:auto!important;top:auto!important;
  display:flex!important;align-items:center;gap:8px;
}
body.cnl-canvas-mode.view-reader #cnlTypeBtn{
  position:static!important;right:auto!important;top:auto!important;
  left:auto!important;transform:none!important;display:inline-flex!important;
  z-index:auto!important;
}
body.cnl-canvas-mode.view-reader .reader-screen{
  min-height:calc(100vh - 48px)!important;
}
body.cnl-canvas-mode.view-reader .reader-sidebar{
  top:48px!important;height:calc(100vh - 48px)!important;
}
body.cnl-canvas-mode.view-reader .stage{
  max-width:none!important;padding:10px 16px 40px!important;
}
body.cnl-canvas-mode.cnl-reading-view #paper{
  width:100%!important;
  max-width:none!important;
}

/* PDFs and notebooks: tools stay in the app header. Other home surfaces drop that chrome. */
body.cnl-canvas-mode:not(.view-reader):not([data-cnl-home="pdf"]):not([data-cnl-home="notebook"]) .app-header{display:none!important}
body.cnl-canvas-mode[data-cnl-home="pdf"] .app-header,
body.cnl-canvas-mode[data-cnl-home="notebook"] .app-header{
  display:flex!important;height:40px!important;min-height:40px!important;
  padding:0 8px!important;
}
body.cnl-canvas-mode[data-cnl-home="pdf"] .top-left-nav,
body.cnl-canvas-mode[data-cnl-home="pdf"] #breadcrumb,
body.cnl-canvas-mode[data-cnl-home="notebook"] #breadcrumb{display:none!important}
body.cnl-canvas-mode #homeScreen{
  min-height:100vh!important;padding:0!important;margin:0!important;
}
body.cnl-canvas-mode #cnlPdfShelf{margin:0;padding:0}
body.cnl-canvas-mode #cnlPdfShelf .cnl-rapid-bar{
  margin:0;padding:6px 12px;border-bottom:1px solid var(--cnl-line,#dde1ef);
  background:rgba(242,244,247,.96);
}
body.cnl-canvas-mode .cnl-pdf-split{
  height:calc(100vh - 48px)!important;min-height:0;gap:0;
}
body.cnl-canvas-mode .cnl-pdf-column{border-radius:0;padding-bottom:16px}
#cnlPdfCanvasEnter[hidden]{display:none!important}

/* Notebooks: page tools stay in the app header. */
body.cnl-canvas-mode #cnlNotebookShelf{margin:0;padding:0}
body.cnl-canvas-mode[data-cnl-home="notebook"] #cnlNbPath,
body.cnl-canvas-mode[data-cnl-home="notebook"] #cnlNbNew,
body.cnl-canvas-mode[data-cnl-home="notebook"] #cnlNbBack{display:none!important}
body.cnl-canvas-mode .cnl-nb-stage{
  height:calc(100vh - 48px)!important;min-height:0;border-radius:0;padding-bottom:16px;
}
body.cnl-canvas-mode .cnl-nb-sheet{
  width:100%!important;
}

/* ---- Master chrome: drawer, tabs, study pages ---------------------------- */
#cnlMenuBtn{
  display:none;
  align-items:center;justify-content:center;
  width:30px!important;height:30px!important;flex:0 0 30px!important;
  padding:0!important;margin:0;
  border:1px solid var(--card-border,#dde1ef)!important;
  background:#fff!important;border-radius:8px!important;cursor:pointer;
  color:var(--cnl-ink,#292664)!important;font-size:15px!important;line-height:1;
  box-shadow:none;
}
#cnlMenuBtn svg{display:block;width:15px;height:15px}
body.view-home #cnlMenuBtn{display:inline-flex}
body.view-home .app-header{padding-left:48px!important}
body.view-home[data-cnl-home="landing"] #breadcrumb{display:none!important}
#cnlMenuBtn:hover{background:#f4f5f8!important}
#cnlDrawerBackdrop{
  display:none;position:fixed;inset:0;z-index:140000;background:rgba(20,22,40,.35);
}
#cnlDrawerBackdrop.show{display:block}
#cnlDrawer{
  position:absolute;top:0;left:0;bottom:0;width:min(86vw,320px);
  background:#fff;box-shadow:8px 0 28px rgba(20,22,40,.18);
  display:flex;flex-direction:column;padding:18px 0 12px;
}
.cnl-drawer-head{
  display:flex;align-items:center;gap:10px;padding:8px 16px 14px;
  border-bottom:1px solid var(--cnl-line,#dde1ef);
}
.cnl-drawer-head b{
  font:700 20px/1.2 "Averia Serif Libre",serif;color:var(--cnl-ink,#292664);
}
.cnl-drawer-row{
  appearance:none;display:flex;align-items:center;gap:12px;width:100%;
  padding:13px 20px;border:0;background:transparent;text-align:left;cursor:pointer;
  color:var(--cnl-ink,#292664);font:600 15px/1.2 "Averia Serif Libre",serif;
}
.cnl-drawer-row:hover{background:#F5F4FA}
.cnl-drawer-row span{opacity:.7;width:22px;text-align:center}
#cnlTabBar{
  display:none;position:fixed;left:0;right:0;bottom:0;z-index:40;
  height:58px;background:#fff;
  border-top:1px solid var(--cnl-line,#dde1ef);
}
body.view-home[data-cnl-home="landing"][data-cnl-tab="home"] #cnlTabBar,
body.view-home[data-cnl-tab="flash"] #cnlTabBar,
body.view-home[data-cnl-tab="quiz"] #cnlTabBar,
body.view-home[data-cnl-tab="create"] #cnlTabBar{display:flex}
.cnl-tab{
  flex:1;border:0;background:transparent;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;
  color:#667395;font:600 11px/1.1 system-ui,-apple-system,"Segoe UI",sans-serif;
}
.cnl-tab .cnl-tab-icon{font-size:18px;line-height:1}
.cnl-tab.cnl-active{color:var(--cnl-ink,#292664)}
/* The tab pages are fixed overlays, so they sit outside .screen-area and inherit
   neither its 1000px column nor its centring. Their background still has to cover
   the window edge to edge, so the column is made with padding rather than width:
   480px either side of the centre puts the content in the same 960px band the home
   screen's grids occupy, and the 18px floor is what the gutters were before. */
.cnl-tab-page{
  display:none;position:fixed;z-index:40;left:0;right:0;
  top:72px;bottom:58px;overflow:auto;
  padding:16px max(18px,calc((100% - var(--cnl-ui-content-width))/2)) 24px;background:#F5F4FA;
}
body[data-cnl-tab="create"] #cnlCreatePage{display:none}
body[data-cnl-tab="flash"] #cnlFlashPage,
body[data-cnl-tab="quiz"] #cnlQuizPage{display:block}
body[data-cnl-tab="create"] #homeScreen,
body[data-cnl-tab="flash"] #homeScreen,
body[data-cnl-tab="quiz"] #homeScreen{display:none!important}
body[data-cnl-tab="create"] #createAiNoteBackdrop.show,
body[data-cnl-tab="create"] #createAiNoteBackdrop{
  display:flex!important;position:fixed;z-index:45;
  top:72px;left:0;right:0;bottom:58px;align-items:flex-start;
  background:#F5F4FA;padding:16px 18px;
}
body[data-cnl-tab="create"] #createAiNoteBackdrop .folder-modal{
  width:min(100%,640px);margin:0 auto;box-shadow:none;
}
.cnl-tab-page h2{
  margin:0 0 8px;font:700 22px/1.2 "Averia Serif Libre",serif;color:var(--cnl-ink,#292664);
}
.cnl-tab-page .cnl-tab-blurb{
  margin:0 0 16px;padding:10px 12px;border-radius:10px;background:#E8EFF8;
  color:#28467C;font-size:13px;line-height:1.4;
}
/* The heading rows, their empty state and the box a deck or quiz opens inside
   are the study pages' own furniture; the navigation that builds them, and the
   bar, fields and buttons around them, are styled by study_navigation.py. */
.cnl-study-row{
  display:flex;align-items:center;justify-content:space-between;gap:12px;
  width:100%;padding:14px 16px;margin:0 0 10px;text-align:left;cursor:pointer;
  border:1px solid var(--cnl-line,#dde1ef);border-radius:14px;background:#fff;
  font:inherit;color:var(--cnl-ink,#292664);
}
.cnl-study-row b{display:block;font:700 15px/1.25 "Averia Serif Libre",serif}
.cnl-study-row small{display:block;margin-top:3px;color:#667395;font-size:12.5px}
.cnl-study-empty{color:#667395;padding:24px 8px;text-align:center}
.cnl-study-mount{
  margin-top:12px;background:#fff;border:1px solid var(--cnl-line,#dde1ef);
  border-radius:16px;padding:8px 12px 16px;min-height:120px;
}
/* The mount outlives whatever it holds - a closed deck leaves the div behind -
   so an empty one would show as an empty white card under the list. */
.cnl-study-mount:empty{display:none}
.cnl-study-editor{
  box-sizing:border-box;width:min(720px,calc(100vw - 32px));
  max-height:calc(100vh - 48px);overflow:auto;padding:24px;
  border:1px solid #d9deeb;border-radius:16px;background:#fff;color:#292664;
  font:14px/1.5 system-ui,sans-serif;
}
.cnl-study-editor::backdrop{background:rgba(20,22,40,.45)}
.cnl-study-editor h2{margin:0 0 18px;font-size:22px}
.cnl-study-editor label{display:grid;gap:6px;margin-bottom:14px;font-weight:600}
.cnl-study-editor textarea,.cnl-study-editor select{
  box-sizing:border-box;width:100%;min-width:0;padding:10px;border:1px solid #b9c7db;
  border-radius:8px;background:#fff;color:#23354f;font:400 14px/1.5 system-ui,sans-serif;
}
.cnl-study-editor textarea{resize:vertical}
.cnl-study-editor fieldset{min-width:0;border:1px solid #d9deeb;border-radius:8px}
.cnl-study-editor [role="alert"]{color:#a12635}
.cnl-study-editor-actions{display:flex;justify-content:flex-end;gap:8px}
.cnl-study-edit{margin:8px 0}
body.view-reader #cnlTabBar,
body.view-reader .cnl-tab-page,
body.view-reader #createAiNoteBackdrop{display:none!important}
/* The page's ☰ still toggles the contents list. Hide it and use the same
   menu button as Home; Outline on the right is what opens the contents. */
body.view-reader #readerSidebarToggle{display:none!important}
body.view-reader #cnlMenuBtn{display:inline-flex!important}
body.view-reader #cnlDrawerBackdrop{display:none}
body.view-reader #cnlDrawerBackdrop.show{display:block!important}
body.cnl-canvas-mode #cnlTabBar,
body.cnl-canvas-mode #cnlMenuBtn,
body.cnl-canvas-mode #cnlDrawerBackdrop,
body.cnl-canvas-mode .cnl-tab-page{display:none!important}
#aiHomeSettingsBackdrop,
#cnlFsrsBackdrop,
#cnlStorageBackdrop,
.cnl-h1-job-backdrop{z-index:150000}
</style>
"""


class TransformError(RuntimeError):
    """The HTML no longer matches the anchors this rewrite depends on."""


def _sub(pattern: re.Pattern, replacement: str, html: str, expected: int, what: str) -> str:
    # A lambda keeps the replacement verbatim. re.subn otherwise parses backslash
    # escapes in it, and DESKTOP_UI_CSS mentions Windows paths in its comments:
    # "\A" raises PatternError and "\f" silently turns into a formfeed.
    result, count = pattern.subn(lambda _match: replacement, html)
    if count != expected:
        raise TransformError(
            f"{what}: expected {expected} match(es), found {count}. "
            f"The app HTML has changed and this rewrite needs updating."
        )
    return result


# The app's whole script is one outer IIFE, and saving an AI-generated note needs
# the DOCX blob the app is holding in pendingDocuments, which lives inside it and
# is never exposed on window. A <script> before </body> would be outside that
# scope, so the save features are spliced in just before the outer IIFE closes.
# The anchor is that IIFE's last statement: if a future export moves it, the build
# fails loudly instead of shipping save buttons that cannot find the note they are
# supposed to write.
_SAVE_ANCHOR = (
    "  $('#aiCreateQuizBtn')?.addEventListener('click',async()=>{\n"
    "    aiSelectTool('quiz');\n"
    "    await aiGenerate('quiz');\n"
    "  });\n"
    "\n"
    "})();\n"
    "\n"
    "})();\n"
)

# The app's AI module is a closure of its own, and the injected payload is spliced
# in after it closes, so none of the poster machinery is in scope there by name.
# Slides are generated and stored through that machinery, so the seven pieces it
# needs are handed out the same way the module already hands out aiProviderLabel -
# on window, from inside the closure, right where it exports the rest.
_AI_EXPORTS_ANCHOR = "  window.aiProviderLabel=aiProviderLabel;\n"

_AI_EXPORTS = (
    "  window.aiProviderLabel=aiProviderLabel;\n"
    "  // Slides are a deck made from a note by the same steps a snapshot is, and\n"
    "  // kept in the same file, so the desktop's own slide player reaches the\n"
    "  // scope descriptor, the study material, the provider call and the store\n"
    "  // through here rather than owning a second copy of any of it.\n"
    "  window.cnlReadingScopeDescriptor=cnlReadingScopeDescriptor;\n"
    "  window.aiPosterScopeDescriptor=aiPosterScopeDescriptor;\n"
    "  window.aiResolveStudyMaterial=aiResolveStudyMaterial;\n"
    "  window.aiCallSelectedProvider=aiCallSelectedProvider;\n"
    "  window.aiGetActiveKey=aiGetActiveKey;\n"
    "  window.aiSavePosterPayload=aiSavePosterPayload;\n"
    "  window.aiLoadSavedPosterForDescriptor=aiLoadSavedPosterForDescriptor;\n"
    "  window.aiSelectTool=aiSelectTool;\n"
    "  window.aiPopulateScopeSelect=aiPopulateScopeSelect;\n"
    "  window.aiLoadSavedFlashcardsForDescriptor=aiLoadSavedFlashcardsForDescriptor;\n"
    "  window.aiGetFlashcardLibrary=aiGetFlashcardLibrary;\n"
    "  window.aiRenderFlashcards=aiRenderFlashcards;\n"
    "  window.aiRenderQuiz=aiRenderQuiz;\n"
    "  window.aiSetInterfaceMode=aiSetInterfaceMode;\n"
    "  window.cnlBuildMainNoteDocx=cnlBuildMainNoteDocx;\n"
    "  window.cnlSafeDocxName=cnlSafeDocxName;\n"
    "  const CNL_AI_HEADING_RULES=[\n"
    "    '',\n"
    "    '# HEADING HIERARCHY OVERRIDE',\n"
    "    '',\n"
    "    'These rules replace section 2 above wherever the two disagree.',\n"
    "    '',\n"
    "    '- The note has exactly one H1, which the app writes from the title.',\n"
    "    '- Every Roman heading is an H2: {\"type\":\"heading\",\"level\":2,\"text\":\"I. CLINICAL FEATURES\"}.',\n"
    "    '  Never emit a heading block at level 1, 3 or 4.',\n"
    "    '- Every A/B/C heading is BoldSide1: {\"type\":\"boldside\",\"level\":1,\"text\":\"A. Clinical Presentation\"}.',\n"
    "    '  Never demote A/B/C to BoldSide2 or BoldSide3.',\n"
    "    '- A heading under a BoldSide1 is BoldSide2. A heading under a BoldSide2 is BoldSide3.',\n"
    "    '',\n"
    "    ''\n"
    "  ].join('\\n');\n"
    "  function cnlNoteLineKind(text){\n"
    "    const raw=String(text||'').replace(/\\*+/g,'').replace(/^#+\\s+/,'').trim();\n"
    "    if(!raw||raw.length>90) return null;\n"
    "    const body=raw.replace(/^[IVXLCDM]+[.)]\\s+/,'').replace(/^[A-Z][.)]\\s+/,'');\n"
    "    if(/[.!?].+/.test(body)) return null;\n"
    "    if(/^[IVXLCDM]+[.)]\\s+\\S/.test(raw)) return {type:'heading',level:2};\n"
    "    if(/^[A-Z][.)]\\s+\\S/.test(raw)) return {type:'boldside',level:1};\n"
    "    return null;\n"
    "  }\n"
    "  const cnlBuildMainNotePromptOrig=cnlBuildMainNotePrompt;\n"
    "  cnlBuildMainNotePrompt=function(topic){\n"
    "    return cnlBuildMainNotePromptOrig(topic)+CNL_AI_HEADING_RULES;\n"
    "  };\n"
    "  const cnlBuildMainNoteDocxOrig=cnlBuildMainNoteDocx;\n"
    "  cnlBuildMainNoteDocx=function(data,fileName){\n"
    "    if(data&&Array.isArray(data.blocks)){\n"
    "      data.blocks.forEach(function(block){\n"
    "        if(block&&block.type==='table') return;\n"
    "        const kind=cnlNoteLineKind(block&&block.text);\n"
    "        if(!kind) return;\n"
    "        block.type=kind.type;\n"
    "        block.level=kind.level;\n"
    "      });\n"
    "    }\n"
    "    return cnlBuildMainNoteDocxOrig(data,fileName);\n"
    "  };\n"
    "  window.cnlBuildMainNoteDocx=cnlBuildMainNoteDocx;\n"
    "  window.cnlRecordOpenedNote=function(record){\n"
    "    try{\n"
    "      record=record||cnlCurrentDocumentRecord();\n"
    "      if(!record) return;\n"
    "      const now=new Date().toISOString();\n"
    "      const name=record.displayName\n"
    "        || (typeof stripDocxExtension==='function' ? stripDocxExtension(record.fileName||'') : record.fileName)\n"
    "        || 'Document';\n"
    "      const descriptor={\n"
    "        scopeKey:'opened-note',\n"
    "        scopeValue:'document',\n"
    "        scopeLabel:name,\n"
    "        headingIndex:null\n"
    "      };\n"
    "      const entry=cnlNormalizeActivityEntry({\n"
    "        lastReadAt:now,\n"
    "        readAt:now,\n"
    "        readHistory:[{at:now,day:cnlLocalDayKey(now)}]\n"
    "      },descriptor);\n"
    "      cnlUpsertActivityIndex(record,descriptor,entry);\n"
    "      cnlRenderHomeActivity();\n"
    "    }catch(_){}\n"
    "  };\n"
    "  const cnlHomeActivityOrig=cnlRenderHomeActivity;\n"
    "  cnlRenderHomeActivity=function(){\n"
    "    cnlHomeActivityOrig();\n"
    "    try{cnlPaintOpenedNotes();}catch(_){}\n"
    "  };\n"
    "  function cnlPaintOpenedNotes(){\n"
    "    const el=document.getElementById('cnlRecentRead');\n"
    "    if(!el) return;\n"
    "    const byDoc=new Map();\n"
    "    for(const item of cnlActivityIndex()){\n"
    "      const at=item.lastReadAt||item.readAt;\n"
    "      if(!at) continue;\n"
    "      const key=item.docIdentity||item.storageKey||item.serverRelativePath||item.documentName||'';\n"
    "      if(!key) continue;\n"
    "      const prev=byDoc.get(key);\n"
    "      const ts=Date.parse(at)||0;\n"
    "      const prefer=item.scopeKey==='opened-note';\n"
    "      const prevPrefer=prev&&prev.scopeKey==='opened-note';\n"
    "      if(!prev || (prefer&&!prevPrefer) || ((prefer===!!prevPrefer) && ts>(Date.parse(prev.lastReadAt||prev.readAt)||0))){\n"
    "        byDoc.set(key,item);\n"
    "      }\n"
    "    }\n"
    "    const list=[...byDoc.values()].sort((a,b)=>{\n"
    "      return (Date.parse(b.lastReadAt||b.readAt)||0)-(Date.parse(a.lastReadAt||a.readAt)||0);\n"
    "    }).slice(0,5);\n"
    "    el.innerHTML='';\n"
    "    if(!list.length){\n"
    "      const empty=document.createElement('div');\n"
    "      empty.className='cnl-home-activity-empty';\n"
    "      empty.textContent='No notes opened yet.';\n"
    "      el.appendChild(empty);\n"
    "      return;\n"
    "    }\n"
    "    for(const item of list){\n"
    "      const btn=document.createElement('button');\n"
    "      btn.type='button';\n"
    "      btn.className='cnl-home-activity-item';\n"
    "      const topic=document.createElement('span');\n"
    "      topic.className='cnl-home-activity-topic';\n"
    "      topic.textContent=item.documentName||item.heading||'Note';\n"
    "      const meta=document.createElement('span');\n"
    "      meta.className='cnl-home-activity-meta';\n"
    "      const location=document.createElement('span');\n"
    "      location.textContent=item.folderName||'';\n"
    "      const time=document.createElement('span');\n"
    "      time.textContent=cnlRelativeActivityTime(item.lastReadAt||item.readAt);\n"
    "      meta.append(location,time);\n"
    "      btn.append(topic,meta);\n"
    "      btn.addEventListener('click',()=>cnlOpenActivityItem(item));\n"
    "      el.appendChild(btn);\n"
    "    }\n"
    "  }\n"
    "  window.cnlPosterInkDoc=function(){\n"
    "    const record=aiCurrentSourceRecord();\n"
    "    const path=record&&record.serverRelativePath?String(record.serverRelativePath):'';\n"
    "    if(!path) return null;\n"
    "    const key=String((aiCurrentPosterPayload&&aiCurrentPosterPayload.scope&&aiCurrentPosterPayload.scope.scopeKey)||'full');\n"
    "    return path+'::'+key;\n"
    "  };\n"
    "  function cnlQuizPackRef(){\n"
    "    const record=aiCurrentSourceRecord();\n"
    "    const descriptor=cnlReadingScopeDescriptor();\n"
    "    if(!record||!descriptor) return null;\n"
    "    const path=String(record.serverRelativePath||'');\n"
    "    const parts=path.split(/[\\\\/]/).filter(Boolean);\n"
    "    const file=parts.pop()||String(record.fileName||'');\n"
    "    const folder=parts.pop()||String(record.folderName||record.subject||'');\n"
    "    const heading=String(descriptor.scopeLabel||'').trim();\n"
    "    if(!heading) return null;\n"
    "    return {\n"
    "      folder:folder,\n"
    "      document:file.replace(/\\.docx$/i,''),\n"
    "      headingIndex:Number.isInteger(descriptor.headingIndex)?descriptor.headingIndex:0,\n"
    "      headingText:heading\n"
    "    };\n"
    "  }\n"
    "  async function cnlLoadSavedQuizPack(){\n"
    "    const ref=cnlQuizPackRef();\n"
    "    if(!ref) return null;\n"
    "    try{\n"
    "      const url='/api/saved-quiz?folder='+encodeURIComponent(ref.folder)\n"
    "        +'&document='+encodeURIComponent(ref.document)\n"
    "        +'&heading='+encodeURIComponent(ref.headingText);\n"
    "      const res=await fetch(url,{cache:'no-store'});\n"
    "      if(res.status===404) return null;\n"
    "      const data=await res.json().catch(()=>null);\n"
    "      if(!res.ok||!data||!Array.isArray(data.questions)||!data.questions.length) return null;\n"
    "      return data;\n"
    "    }catch{return null;}\n"
    "  }\n"
    "  function cnlSaveQuizPack(data){\n"
    "    if(data?.headingText || data?.studyLabel) return;\n"
    "    const ref=cnlQuizPackRef();\n"
    "    const questions=data&&Array.isArray(data.questions)?data.questions:[];\n"
    "    if(!ref||!questions.length) return;\n"
    "    fetch('/api/saved-quiz',{\n"
    "      method:'POST',\n"
    "      headers:{'Content-Type':'application/json'},\n"
    "      body:JSON.stringify({\n"
    "        folder:ref.folder,\n"
    "        document:ref.document,\n"
    "        headingIndex:ref.headingIndex,\n"
    "        headingText:ref.headingText,\n"
    "        questions:questions,\n"
    "        madeAt:Date.now()\n"
    "      })\n"
    "    }).catch(()=>{});\n"
    "  }\n"
    "  const cnlAiRenderQuiz=aiRenderQuiz;\n"
    "  const cnlAiGenerate=aiGenerate;\n"
    "  aiRenderQuiz=function(data){\n"
    "    cnlAiRenderQuiz(data);\n"
    "    cnlSaveQuizPack(data);\n"
    "  };\n"
    "  aiGenerate=async function(kind,opts){\n"
    "    if(kind==='quiz' && !window.cnlH1JobRunning){\n"
    "      const packed=await cnlLoadSavedQuizPack();\n"
    "      if(packed){aiRenderQuiz(packed);return;}\n"
    "    }\n"
    "    return cnlAiGenerate(kind,opts);\n"
    "  };\n"
    "  window.aiGenerate=aiGenerate;\n"
)

_SAVE_SPLICE = (
    "  $('#aiCreateQuizBtn')?.addEventListener('click',async()=>{\n"
    "    aiSelectTool('quiz');\n"
    "    await aiGenerate('quiz');\n"
    "  });\n"
    "\n"
    + QUIZ_GENERATION_JS + "\n" + STUDY_BRIDGE_JS + "\n" + STUDY_EDITOR_JS + "\n"
    "})();\n"
    "\n" + SAVE_JS + "\n"
    "})();\n"
)


def _splice(old: str, new: str, html: str, expected: int, what: str) -> str:
    """Literal counterpart to _sub.

    The injected script is full of backslashes and braces, which re.sub would read
    as escapes and group references, so it has to go in verbatim.
    """
    count = html.count(old)
    if count != expected:
        raise TransformError(
            f"{what}: expected {expected} match(es), found {count}. "
            f"The app HTML has changed and this rewrite needs updating."
        )
    return html.replace(old, new)


def transform_html(html: str) -> str:
    """Point every external asset at the local /vendor copies, add the
    desktop-only UI policy, and splice in the desktop save features."""
    html = _sub(
        _JSZIP_TAG,
        '<script src="/vendor/jszip.min.js"></script>',
        html,
        1,
        "JSZip CDN script tag",
    )
    html = _sub(
        _FONTS_LINK,
        VENDOR_FONT_LINKS,
        html,
        1,
        "Google Fonts stylesheet link",
    )
    # Two preconnect hints (fonts.googleapis.com and fonts.gstatic.com).
    html = _sub(_PRECONNECT, "", html, 2, "font preconnect links")

    html = _sub(_ICON_LINK, '<link rel="icon" href="/app.ico" sizes="any">', html, 1, "favicon link")
    # Mobile-only references to files that were never shipped with the app.
    html = _sub(_TOUCH_ICON, "", html, 1, "apple-touch-icon link")
    html = _sub(_MANIFEST, "", html, 1, "webmanifest link")

    # Both blocks go in last so that, where the app's own CSS also uses !important,
    # source order decides in our favour. VIEW_MODES_CSS is after DESKTOP_UI_CSS
    # because the font overrides inside it must beat the Relaxed spec, which is
    # earlier in the same block.
    html = _sub(
        _HEAD_CLOSE,
        DESKTOP_UI_CSS + VIEW_MODES_CSS + '<style id="cnlPearlsStyles">' + PEARLS_CSS + '</style>'
        + '<style id="cnlConsumerViewer">'
        + (paths.resource_root() / "vendor" / "consumer-viewer.css").read_text(encoding="utf-8")
        + "</style><style id=\"cnlBodyFonts\">"
        + (paths.resource_root() / "vendor" / "body-fonts.css").read_text(encoding="utf-8")
        + "</style><style id=\"cnlConsumerType\">"
        + (paths.resource_root() / "vendor" / "consumer-type.css").read_text(encoding="utf-8")
        + "</style><style id=\"cnlConsumerUi\">"
        + (paths.resource_root() / "vendor" / "consumer-ui.css").read_text(encoding="utf-8")
        + "</style><style id=\"cnlQbankExplanations\">"
        + (paths.resource_root() / "vendor" / "qbank-explanations.css").read_text(encoding="utf-8")
        # Not "cnlReaderListen": an element id becomes a window property, and
        # that name is the script's own re-entry guard.
        + "</style><style id=\"cnlListenStyles\">"
        + (paths.resource_root() / "vendor" / "reader-listen.css").read_text(encoding="utf-8")
        + "</style></head>",
        html,
        1,
        "closing head tag",
    )

    # Checked against the app's own HTML, before the splice, so the injected
    # payload can never satisfy an assertion about itself.
    for anchor in APP_SCOPE_ANCHORS:
        found = html.count(anchor)
        if found != 1:
            raise TransformError(
                f"save_js reaches into the app's scope via {anchor!r}: expected 1 "
                f"occurrence, found {found}. A feature that depends on it would fail "
                f"silently in the browser, so the export needs re-reading."
            )

    # Route every notes outline/initial-heading jump through the settled-layout seek.
    for old_seek, new_seek, count in (
        ("requestAnimationFrame(()=>target.scrollIntoView({behavior:'smooth',block:'start'}));",
         "window.cnlSeekReaderHeading(target);", 1),
        ("requestAnimationFrame(()=>heads[firstH1]?.scrollIntoView({block:'start'}));",
         "window.cnlSeekReaderHeading(heads[firstH1]);", 1),
        ("requestAnimationFrame(()=>heads[targetIndex]?.scrollIntoView({block:'start'}));",
         "window.cnlSeekReaderHeading(heads[targetIndex]);", 2),
    ):
        html = _splice(old_seek, new_seek, html, count, "notes outline seek")

    # Before the payload goes in, so the names it reaches for are on window by the
    # time it runs.
    html = _splice(
        _AI_EXPORTS_ANCHOR,
        _AI_EXPORTS,
        html,
        1,
        "the AI module's window exports",
    )

    html = _splice(
        _SAVE_ANCHOR,
        _SAVE_SPLICE,
        html,
        1,
        "end of the app's main script scope",
    )

    html = _splice(
        "<body>\n",
        "<body>\n"
        '  <div id="cnlInkEditPills">'
        '<button type="button" id="cnlInkUndoBtn" title="Undo (Ctrl+Z)" aria-label="Undo"></button>'
        '<button type="button" id="cnlInkRedoBtn" title="Redo (Ctrl+Y)" aria-label="Redo"></button>'
        '</div>\n'
        '  <div id="cnlOutlinePill">'
        '<button id="cnlOutlineBtn" type="button" title="Show or hide the outline"'
        ' aria-label="Outline"></button>'
        '</div>\n'
        '  <button type="button" id="cnlListenPill" title="Read this note aloud"'
        ' aria-label="Read this note aloud">♪ Listen</button>\n'
        '  <div id="cnlListenDock" role="group" aria-label="Read this note aloud" hidden>\n'
        '    <div class="cnl-listen-head">'
        '<span id="cnlListenSection"></span><span id="cnlListenCount"></span>'
        '</div>\n'
        '    <div class="cnl-listen-row">\n'
        '      <button type="button" id="cnlListenBack" title="Back 30 words" aria-label="Back 30 words">−30</button>\n'
        '      <button type="button" id="cnlListenPlay" aria-label="Play narration">▶</button>\n'
        '      <button type="button" id="cnlListenFwd" title="Forward 30 words" aria-label="Forward 30 words">+30</button>\n'
        '      <select id="cnlListenRate" aria-label="Reading speed">'
        '<option value="0.8">0.8×</option><option value="1" selected>1×</option>'
        '<option value="1.2">1.2×</option><option value="1.5">1.5×</option>'
        '<option value="1.8">1.8×</option></select>\n'
        '      <select id="cnlListenVoice" aria-label="Voice"></select>\n'
        '      <button type="button" id="cnlListenClose" title="Stop listening" aria-label="Stop listening">✕</button>\n'
        '    </div>\n'
        '    <div id="cnlListenStatus" hidden></div>\n'
        '    <button type="button" id="cnlListenDownload" hidden>Download offline voice · 44 MB</button>\n'
        '    <div id="cnlListenBar"><span id="cnlListenBarFill"></span></div>\n'
        '    <audio id="cnlListenAudio" preload="auto" hidden></audio>\n'
        '  </div>\n',
        html,
        1,
        "Outline button as a direct child of body",
    )

    html = _splice(
        '<button id="aiPosterTopBtn" class="study-top-btn reader-only" type="button" title="Snapshot">Snapshot</button>',
        '<button id="aiPosterTopBtn" class="study-top-btn reader-only" type="button" title="Snapshot">Snapshot</button>\n'
        '        <button id="cnlSlidesTopBtn" class="study-top-btn reader-only" type="button"'
        ' title="Teaching slides for this heading" aria-label="Slides"></button>',
        html,
        1,
        "slides button beside Snapshot",
    )

    html = _splice(
        "  if(e.target.closest('#readerSidebarToggle')) return;\n\n  hideReaderSidebar();",
        "  if(e.target.closest('#readerSidebarToggle')) return;\n"
        "  if(e.target.closest('#cnlOutlineBtn,#cnlOutlinePill')) return;\n"
        "  return;\n",
        html,
        1,
        "outline button exemption from click-away",
    )

    html = _splice(
        "$('#readerSidebarToggle').addEventListener('click',()=>{\n"
        "  if(appView!=='reader'){\n"
        "    return;\n"
        "  }\n\n"
        "  if(innerWidth<=900){\n"
        "    document.body.classList.toggle('reader-sidebar-open');\n"
        "  }else{\n"
        "    document.body.classList.toggle('reader-sidebar-hidden');\n"
        "  }\n\n"
        "  updateReaderSidebarToggle();\n"
        "});",
        "$('#readerSidebarToggle').addEventListener('click',()=>{\n"
        "  if(appView!=='reader'){\n"
        "    return;\n"
        "  }\n"
        "  if(typeof window.cnlDrawerOpen==='function') window.cnlDrawerOpen(true);\n"
        "});",
        html,
        1,
        "hamburger opens the app menu, not the outline",
    )

    html = _splice(
        "    document.body.classList.toggle('reader-sidebar-hidden',innerWidth<=900);",
        "    document.body.classList.add('reader-sidebar-hidden');",
        html,
        1,
        "notes start with the outline closed",
    )

    html = _splice(
        "  function setHidden(next){\n"
        "    hidden=!!next;\n"
        "    header.classList.toggle('cnl-topbar-hidden',hidden);\n"
        "    document.body.classList.toggle('cnl-topbar-hidden',hidden);\n"
        "  }\n",
        "  function applyHidden(){\n"
        "    const vis=hidden&&!window.cnlTopbarPointerInTop;\n"
        "    header.classList.toggle('cnl-topbar-hidden',vis);\n"
        "    document.body.classList.toggle('cnl-topbar-hidden',vis);\n"
        "  }\n"
        "  function setHidden(next){\n"
        "    hidden=!!next;\n"
        "    applyHidden();\n"
        "  }\n"
        "  window.cnlApplyTopbarHidden=applyHidden;\n",
        html,
        1,
        "top-bar auto-hide respects pointer in the header region",
    )

    html = _splice("explanation:{type:'string'}", QUIZ_EXPLANATION_SCHEMA_JS,
                   html, 1, "detailed quiz teaching schema")
    html = _splice("required:['question','options','correctIndex','explanation']",
                   "required:['question','options','correctIndex','explanation','explanationTeaching']",
                   html, 1, "required detailed quiz explanation")
    html = _splice("- Include a 0-based correctIndex and a short explanation.", QUIZ_REQUIREMENTS,
                   html, 1, "detailed quiz generation instructions")

    html = _splice(
        "if(ex) ex.textContent=isGradable(q) ? (q.explanation||'') : [q.answerText,q.reviewNote,q.explanation].filter(Boolean).join('\\n\\n');",
        "if(ex) window.cnlRenderQbankExplanation(ex,q,isGradable(q));",
        html, 1, "structured Qbank explanation rendering",
    )
    html = _splice(
        "const gradedTotal=questions.filter(isGradable).length;",
        "let gradedTotal=questions.filter(isGradable).length;",
        html, 1, "editable quiz grading total",
    )
    html = _splice(
        "wrap.append(progress,source,qEl,opts,explain,nav);",
        "wrap.append(progress,source,qEl,opts,explain,nav);\n"
        "      cnlAddQuizEditor(nav,q,data,idx,()=>{\n"
        "        answered[idx]=null;\n"
        "        score=questions.reduce((sum,item,i)=>sum+(isGradable(item)&&answered[i]!=null&&answered[i]===item.correctIndex?1:0),0);\n"
        "        gradedTotal=questions.filter(isGradable).length;\n"
        "        if(window.cnlQuizReviewSession) window.cnlQuizReviewSession.questionsSolved=answered.filter(v=>v!=null).length;\n"
        "        renderQ();\n"
        "      });",
        html, 1, "manual quiz editor",
    )
    html = _splice(
        "wrap.append(meta,card,hint,noteBtn);",
        "wrap.append(meta,card,hint,noteBtn);\n"
        "      cnlAddFlashEditor(wrap,current,data,opts,render);",
        html, 1, "manual flashcard editor",
    )
    html = _splice(
        "}else if(session.scope){",
        "}else if(session.libraryEntry){\n"
        "      await aiPersistCurrentFlashcardSession();\n"
        "    }else if(session.scope){",
        html, 1, "deleting a card saves back to its library deck",
    )
    _assert_offline(html)
    before, after = html.rsplit("</body>", 1)
    html = (before + "<script>"
            + (paths.resource_root() / "vendor" / "consumer-viewer.js").read_text(encoding="utf-8")
            + "</script><script>"
            + (paths.resource_root() / "vendor" / "consumer-ui.js").read_text(encoding="utf-8")
            + "</script><script>"
            + (paths.resource_root() / "vendor" / "study-rich-text.js").read_text(encoding="utf-8")
            + "</script><script>"
            + (paths.resource_root() / "vendor" / "qbank-html-import.js").read_text(encoding="utf-8")
            + "</script><script>"
            + (paths.resource_root() / "vendor" / "qbank-explanations.js").read_text(encoding="utf-8")
            + "</script><script>"
            + (paths.resource_root() / "vendor" / "reader-listen.js").read_text(encoding="utf-8")
            + "</script></body>" + after)
    return html


def _assert_offline(html: str) -> None:
    """No page asset may still reach the network.

    The AI provider endpoints are deliberately excluded: those are runtime fetch
    calls made only when the user asks for AI features, not page assets, and they
    are the one thing that legitimately needs internet.
    """
    leftover = re.findall(
        r'(?:src|href)="(https?://[^"]+)"', html, flags=re.I
    )
    # Ignore the OOXML/purl XML namespace strings, which are never fetched.
    offenders = [
        url
        for url in leftover
        if "jsdelivr" in url or "googleapis.com/css" in url or "gstatic" in url
    ]
    if offenders:
        raise TransformError(f"HTML still references remote assets: {offenders}")


def transform_font_css(css: str) -> str:
    """Serve a vendored Google stylesheet with its font URLs pointing at /vendor.

    Applied to every vendored family stylesheet, so it must not assume one
    family's directory layout.
    """
    if not _GSTATIC_DIR.search(css):
        raise TransformError(
            "A vendored font stylesheet no longer references fonts.gstatic.com. "
            "The offline copy has drifted - re-download it or update _GSTATIC_DIR."
        )
    return _GSTATIC_DIR.sub("/vendor/fonts/", css)
