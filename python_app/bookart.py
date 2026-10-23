"""Cover art extraction for library books."""
import posixpath
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
        '.gif': 'image/gif', '.webp': 'image/webp'}
IMAGE_EXTS = tuple(MIME)
MAX_COVER = 16 * 1024 * 1024


def _resolve(zip_names, base, href):
    href = unquote(href.split('#')[0].split('?')[0])
    if not href:
        return None
    for candidate in (posixpath.normpath(posixpath.join(base, href)), href.lstrip('/')):
        for name in zip_names:
            if name.lower() == candidate.lower():
                return name
    leaf = posixpath.basename(href).lower()
    for name in zip_names:
        if posixpath.basename(name).lower() == leaf:
            return name
    return None


def epub_cover(filepath):
    path = Path(filepath)
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            opf = next((n for n in names if n.lower().endswith('.opf')), None)
            if not opf:
                return None, None
            text = archive.read(opf).decode('utf-8', errors='replace')
            base = posixpath.dirname(opf)
            href = None
            meta = re.search(r'<meta[^>]+name\s*=\s*["\']cover["\'][^>]*>', text, re.I)
            if meta:
                content = re.search(r'content\s*=\s*["\']([^"\']+)', meta.group(0), re.I)
                if content:
                    item = re.search(r'<item[^>]+id\s*=\s*["\']' + re.escape(content.group(1)) + r'["\'][^>]*>', text, re.I)
                    if item:
                        found = re.search(r'href\s*=\s*["\']([^"\']+)', item.group(0), re.I)
                        if found:
                            href = found.group(1)
            if not href:
                item = re.search(r'<item[^>]+properties\s*=\s*["\'][^"\']*cover-image[^"\']*["\'][^>]*>', text, re.I)
                if item:
                    found = re.search(r'href\s*=\s*["\']([^"\']+)', item.group(0), re.I)
                    if found:
                        href = found.group(1)
            if not href:
                ref = re.search(r'<reference[^>]+type\s*=\s*["\']cover["\'][^>]*>', text, re.I)
                if ref:
                    found = re.search(r'href\s*=\s*["\']([^"\']+)', ref.group(0), re.I)
                    if found:
                        href = found.group(1)
            name = _resolve(names, base, href) if href else None
            if not name:
                images = [n for n in names if n.lower().endswith(IMAGE_EXTS)]
                named = [n for n in images if 'cover' in posixpath.basename(n).lower()]
                name = (named or images or [None])[0]
            if not name:
                return None, None
            data = archive.read(name)
    except (zipfile.BadZipFile, OSError, KeyError):
        return None, None
    if not data or len(data) > MAX_COVER:
        return None, None
    suffix = posixpath.splitext(name)[1].lower()
    return data, MIME.get(suffix)


def for_book(book):
    path = Path(book.get('path') or '')
    if not path.is_file():
        return None, None
    if path.suffix.lower() == '.epub':
        return epub_cover(path)
    return None, None
