"""Entry point: resolve paths, start the local server, open the native window.

Run directly with ``python -m cnl_desktop``, or frozen as the packaged .exe.
``--server-only`` starts the HTTP server without a window, which is how the
endpoints get verified in a real browser before packaging.
"""

from __future__ import annotations

import argparse
import ctypes
import logging
import os
import shutil
import sys
import threading
import time
from pathlib import Path

from . import paths

log = logging.getLogger("cnl_desktop")

MUTEX_NAME = "ClinicalNotesDesktop.SingleInstance"
ERROR_ALREADY_EXISTS = 183

# The app's name, read by the window title, dialog captions, the argparse
# prog and the startup log line. MUTEX_NAME identifies the first window so a
# second launch can open beside it (its own server, its own WebView2 profile)
# rather than being turned away. Both still read and write the same data folder.
WINDOW_TITLE = "Cortex"
WINDOW_BG = "#f2f4f7"

# Logical pixels, which is what pywebview asks for; it multiplies each by the
# monitor DPI scale itself. The window opens at this size only if it fits.
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 940
# Small enough that Windows Snap to half the screen still works on a 1080p
# display at 150% scaling. 940x620 logical was 1410 physical wide, which is
# larger than half of 1920, so the window would not shrink or dock to the side.
WINDOW_MIN_SIZE = (560, 400)
# Physical pixels of desktop to leave visible around the window when it is too
# big for the work area. See window_geometry.
WINDOW_MARGIN = 48


def _acquire_single_instance() -> ctypes.c_void_p | None:
    """Return the mutex handle, or None if another instance already holds it.

    use_last_error is required: without it GetLastError() can report another
    thread's error, and this process is threaded.
    """
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateMutexW.restype = ctypes.c_void_p
    handle = kernel32.CreateMutexW(None, False, MUTEX_NAME)
    if ctypes.get_last_error() == ERROR_ALREADY_EXISTS:
        if handle:
            kernel32.CloseHandle(handle)
        return None
    # Keep a reference: the mutex is released when the handle is closed.
    return ctypes.c_void_p(handle) if handle else None


def _start_server(data_root: Path, port: int = 0):
    from .server import start_server

    server = start_server(data_root, port=port)
    thread = threading.Thread(target=server.serve_forever, name="cnl-http", daemon=True)
    thread.start()
    return server, thread


def run_server_only(server) -> int:
    """Block until interrupted. Used for browser-based verification."""
    url = f"http://127.0.0.1:{server.port}/"
    log.info("server-only mode: %s", url)

    # The banner is a courtesy to whoever is watching a console, not something to
    # fail on. The packaged app is built --windowed, which leaves sys.stdout as
    # None however it was launched, so the flag was unusable there: the server came
    # up, this line raised, and the process exited 1 with the port already bound.
    stream = sys.stdout
    if stream is not None:
        try:
            stream.write(f"{WINDOW_TITLE} server on {url}\nPress Ctrl+C to stop.\n")
            stream.flush()
        except (OSError, ValueError):
            pass

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
        server.server_close()
    return 0


class _RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


def _work_area() -> tuple[int, int, int, int]:
    """Primary monitor work area in physical pixels, as (left, top, width, height).

    The work area rather than the screen bounds, because the taskbar is the reason
    a window sized to the screen does not fit.
    """
    user32 = ctypes.windll.user32
    # Must precede the measurement. pywebview calls this too, but only when it
    # starts the window, which is after create_window - and an unaware process is
    # handed virtualised metrics by SystemParametersInfoW, so measuring first
    # would compute against a screen size the window is never actually placed on.
    # Setting the same awareness pywebview is about to set cannot conflict with it.
    try:
        user32.SetProcessDPIAware()
    except OSError:
        pass

    area = _RECT()
    SPI_GETWORKAREA = 0x0030
    if user32.SystemParametersInfoW(SPI_GETWORKAREA, 0, ctypes.byref(area), 0):
        return area.left, area.top, area.right - area.left, area.bottom - area.top
    return 0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def _dpi_scale() -> float:
    """The logical-to-physical factor pywebview multiplies window geometry by.

    It reads GetDpiForWindow/96 once the form has a handle; under the system-wide
    awareness both this and _work_area set, that is the system DPI.
    """
    user32 = ctypes.windll.user32
    try:
        dpi = user32.GetDpiForSystem()
        if dpi:
            return dpi / 96
    except AttributeError:
        pass  # Windows older than 10 1607
    dc = user32.GetDC(None)
    try:
        dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, 88)  # LOGPIXELSX
    finally:
        user32.ReleaseDC(None, dc)
    return dpi / 96 if dpi else 1.0


def window_geometry(
    width: int, height: int, min_size: tuple[int, int], cascade: int = 0
) -> dict:
    """Size and position that open the window centred and entirely on screen.

    Everything is decided in physical pixels, because that is the space the work
    area is measured in and the space WinForms ultimately receives, then divided
    back down: create_window wants logical values and multiplies them by the scale
    again. Doing the arithmetic the other way round is what let a window that fits
    the screen logically arrive 42 physical pixels too tall for it.

    An explicit x and y also switches pywebview off WinForms' CenterScreen, which
    centres on whichever monitor currently holds the mouse cursor rather than the
    primary one.
    """
    left, top, avail_w, avail_h = _work_area()
    scale = _dpi_scale()
    if avail_w <= 0 or avail_h <= 0 or scale <= 0:
        log.warning("unusable screen metrics (%dx%d at %.2f); using defaults", avail_w, avail_h, scale)
        return dict(width=width, height=height, min_size=min_size)

    # Leave desktop visible around the window. Clamping to the work area itself is
    # what opened it edge to edge: at 1.5x a 940-logical-pixel height is 1410
    # physical, so on a 1368px-tall area it came out at exactly 1368 with nothing
    # above or below it. The reservation is dropped on an axis where it would leave
    # less room than that axis's own minimum, because a Size smaller than
    # MinimumSize is what makes WinForms grow the form back past the clamp.
    room_w = avail_w - 2 * WINDOW_MARGIN
    room_h = avail_h - 2 * WINDOW_MARGIN
    if room_w < int(min_size[0] * scale):
        room_w = avail_w
    if room_h < int(min_size[1] * scale):
        room_h = avail_h

    # The minimum is clamped to the size as well as to the screen: a MinimumSize
    # larger than Size makes WinForms grow the form back past the clamp. It is
    # also capped at half the work area so Aero Snap to the side of the screen
    # is never refused.
    phys_w = min(int(width * scale), room_w)
    phys_h = min(int(height * scale), room_h)
    phys_min = (
        min(int(min_size[0] * scale), room_w, phys_w, max(1, avail_w // 2)),
        min(int(min_size[1] * scale), room_h, phys_h, max(1, avail_h // 2)),
    )
    # Centred in the work area, not in the reserved room, so the two margins are
    # equal rather than the window sitting 48px in from one edge only.
    phys_x = left + (avail_w - phys_w) // 2
    phys_y = top + (avail_h - phys_h) // 2
    # A second window is shifted so it does not land exactly on the first.
    if cascade:
        step = int(40 * scale) * int(cascade)
        phys_x = min(max(left, phys_x + step), left + max(0, avail_w - phys_w))
        phys_y = min(max(top, phys_y + step), top + max(0, avail_h - phys_h))

    log.info(
        "window: %dx%d physical at %d,%d in a %dx%d work area at %.2fx scale",
        phys_w, phys_h, phys_x, phys_y, avail_w, avail_h, scale,
    )
    return dict(
        width=phys_w / scale,
        height=phys_h / scale,
        x=phys_x / scale,
        y=phys_y / scale,
        min_size=(phys_min[0] / scale, phys_min[1] / scale),
    )


def run_window(server, data_root: Path, profile: Path, cascade: int = 0) -> int:
    import webview

    from .webview_patch import apply_patches

    # Must precede create_window: pywebview binds its WebView2 delegates in
    # EdgeChrome.__init__, so a later patch would not be seen.
    apply_patches(paths.exports_dir(data_root))

    url = f"http://127.0.0.1:{server.port}/"
    icon = paths.resource_root() / "app.ico"
    geometry = window_geometry(
        WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_SIZE, cascade=cascade
    )

    from .qbank_converter import QbankConverter
    converter = QbankConverter()
    converter._window = webview.create_window(
        WINDOW_TITLE,
        url,
        js_api=converter,
        **geometry,
        background_color=WINDOW_BG,
        # Page zoom is the app's: it scales the note or PDF, not the chrome.
        text_select=True,
        # Do not let pywebview inject its two-finger touchstart blocker.
        # WebView2 native pinch and the page gesture handlers stay available.
        zoomable=True,
        resizable=True,
    )

    kwargs = dict(
        gui="edgechromium",
        debug=False,
        # private_mode=True wipes localStorage on exit, losing AI keys,
        # flashcard state and quiz settings.
        private_mode=False,
        storage_path=str(profile),
    )
    if icon.is_file():
        kwargs["icon"] = str(icon)

    webview.start(**kwargs)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog=WINDOW_TITLE)
    parser.add_argument(
        "--server-only",
        action="store_true",
        help="run the HTTP server without opening a window",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="override the data folder (defaults to <app folder>/data)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=0,
        help="serve on this port instead of one the OS assigns (0 = ephemeral)",
    )
    args = parser.parse_args(argv)

    data_root = Path(args.data_dir).resolve() if args.data_dir else paths.data_dir()
    paths.ensure_data_tree(data_root)
    log_path = paths.setup_logging(data_root)

    log.info("=" * 60)
    log.info("%s starting (frozen=%s)", WINDOW_TITLE, paths.is_frozen())
    log.info("app root : %s", paths.app_root())
    log.info("data dir : %s", data_root)
    log.info("assets   : %s", paths.resource_root())
    log.info("log file : %s", log_path)

    mutex = None
    extra_profile = None
    profile = paths.profile_dir()
    cascade = 0
    if not args.server_only:
        mutex = _acquire_single_instance()
        if mutex is None:
            extra_profile = paths.extra_profile_dir(os.getpid())
            profile = extra_profile
            cascade = 1 + (os.getpid() % 6)
            log.info("extra window pid=%d profile=%s", os.getpid(), profile)
        else:
            # A previous hard kill can leave WebView2 children holding the profile
            # lock; without this the window opens blank (init fails 0x800700AA).
            from .orphans import reap_orphan_webview2

            reap_orphan_webview2(profile)
            log.info("primary window profile=%s", profile)

    server = None
    port_marker = paths.port_file(data_root)
    try:
        try:
            server, _ = _start_server(data_root, args.port)
        except Exception:
            log.exception("could not start the local server")
            ctypes.WinDLL("user32", use_last_error=True).MessageBoxW(
                None,
                f"{WINDOW_TITLE} could not start its local server.\n\n"
                f"See the log for details:\n{log_path}",
                WINDOW_TITLE,
                0x10,
            )
            return 1

        log.info("server listening on http://127.0.0.1:%d/", server.port)
        try:
            port_marker.write_text(str(server.port), encoding="utf-8")
        except OSError:
            log.warning("could not write %s", port_marker)

        try:
            if args.server_only:
                return run_server_only(server)
            return run_window(server, data_root, profile, cascade=cascade)
        except Exception:
            log.exception("fatal error")
            return 1
        finally:
            if server is not None:
                server.shutdown()
                server.server_close()
                log.info("server stopped")
            try:
                if port_marker.read_text(encoding="utf-8").strip() == str(server.port):
                    port_marker.unlink()
            except OSError:
                pass
    finally:
        if extra_profile is not None:
            shutil.rmtree(extra_profile, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
