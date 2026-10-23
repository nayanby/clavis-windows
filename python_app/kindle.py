"""Kindle device detection, MOBI/AZW3 metadata parsing, import and export."""
import hashlib
import json
import logging
import os
import re
import struct
import time
from pathlib import Path

KINDLE_EXTS = {'.mobi', '.azw', '.azw3', '.kfx'}
EXTH_TYPES = {
    100: 'author', 101: 'publisher', 103: 'description', 104: 'isbn',
    105: 'subject', 106: 'publishDate', 107: 'review', 108: 'contributor',
    109: 'rights', 112: 'source', 113: 'asin', 121: 'kf8Boundary',
    122: 'fixedLayout', 201: 'coverOffset', 202: 'thumbOffset',
    203: 'hasFakeCover', 503: 'title', 524: 'language',
}


def parse_pdb(data):
    if len(data) < 78:
        raise ValueError('File is too small to be a valid book.')
    name = data[:32].replace(b'\x00', b'').decode('latin-1', errors='replace').strip()
    nrec = struct.unpack_from('>H', data, 76)[0]
    if nrec < 1 or 78 + nrec * 8 > len(data):
        raise ValueError('This file has an invalid record structure.')
    offsets = [struct.unpack_from('>I', data, 78 + i * 8)[0] for i in range(nrec)]
    offsets.append(len(data))
    return name, [data[offsets[i]:offsets[i + 1]] for i in range(nrec)]


def parse_exth(data, offset, length):
    meta = {}
    if offset + 12 > len(data):
        return meta
    if data[offset:offset + 4] != b'EXTH':
        return meta
    count = struct.unpack_from('>I', data, offset + 8)[0]
    pos = offset + 12
    for _ in range(min(count, 200)):
        if pos + 8 > offset + length:
            break
        rtype, rlen = struct.unpack_from('>II', data, pos)
        if rlen < 8 or pos + rlen > offset + length:
            break
        value = data[pos + 8:pos + rlen]
        if rtype in EXTH_TYPES:
            key = EXTH_TYPES[rtype]
            text = value.decode('utf-8', errors='replace').strip()
            if text:
                if key not in meta:
                    meta[key] = text
                elif isinstance(meta[key], list):
                    meta[key].append(text)
                else:
                    meta[key] = [meta[key], text]
        pos += rlen
    return meta


def parse_mobi_header(record):
    if len(record) < 16 + 232 or record[16:20] != b'MOBI':
        return {}, {}
    ml = struct.unpack_from('>I', record, 20)[0]
    if ml < 232 or 16 + ml > len(record):
        return {}, {}
    kind = struct.unpack_from('>I', record, 24)[0]
    enc_val = struct.unpack_from('>I', record, 28)[0]
    title_off = struct.unpack_from('>I', record, 84)[0]
    title_len = struct.unpack_from('>I', record, 88)[0]
    locale = struct.unpack_from('>I', record, 92)[0]
    first_image = struct.unpack_from('>I', record, 108)[0]
    exth_flag = struct.unpack_from('>I', record, 128)[0]
    meta = {'encoding': enc_val, 'kind': kind, 'locale': locale,
            'headerLength': ml, 'firstImage': first_image}
    if 0 < title_off < len(record) and title_len:
        end = min(title_off + title_len, len(record))
        raw = record[title_off:end].split(b'\x00')[0]
        try:
            t = raw.decode('utf-8').strip()
        except UnicodeDecodeError:
            t = raw.decode('latin-1', errors='replace').strip()
        if t:
            meta['title'] = t
    exth = {}
    eo = 16 + ml
    if exth_flag & 0x40 and eo + 12 <= len(record) and record[eo:eo + 4] == b'EXTH':
        el = struct.unpack_from('>I', record, eo + 4)[0]
        if el > 0 and eo + el <= len(record):
            exth = parse_exth(record, eo, el)
    return meta, exth


def parse_kf8_header(records, boundary):
    if boundary is None or boundary < 0 or boundary >= len(records):
        return {}
    meta, exth = parse_mobi_header(records[boundary])
    out = dict(exth)
    if meta.get('title'):
        out['title'] = meta['title']
    return out


def find_boundary(records, mobi_meta, exth=None):
    raw = (exth or {}).get('kf8Boundary')
    try:
        index = int(raw)
    except (TypeError, ValueError):
        index = -1
    if 0 < index < len(records):
        return index
    return None


def extract_cover(records, mobi_meta, exth):
    first_image = mobi_meta.get('firstImage')
    base = first_image if isinstance(first_image, int) and 0 <= first_image < len(records) else 0
    for key in ('coverOffset', 'thumbOffset'):
        try:
            offset = int(exth.get(key, -1))
        except (ValueError, TypeError):
            continue
        index = base + offset
        if not 0 <= index < len(records):
            continue
        data = records[index]
        if data[:3] == b'\xff\xd8\xff':
            return data, 'image/jpeg'
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            return data, 'image/png'
    return None, None


def has_drm(mobi_meta, records):
    if not records:
        return False
    rec0 = records[0]
    if len(rec0) < 16 + 232 or mobi_meta.get('headerLength', 0) < 172:
        return False
    drm_offset, drm_count = struct.unpack_from('>II', rec0, 164)
    return drm_offset not in (0, 0xFFFFFFFF) or drm_count not in (0, 0xFFFFFFFF)


def parse_book(filepath):
    filepath = Path(filepath)
    data = filepath.read_bytes()
    pdb_name, records = parse_pdb(data)
    if not records:
        raise ValueError('This file contains no readable records.')
    mobi_meta, exth = parse_mobi_header(records[0])
    boundary = find_boundary(records, mobi_meta, exth)
    if boundary is not None:
        kf8 = parse_kf8_header(records, boundary)
        for k, v in kf8.items():
            if k not in exth or k == 'title':
                exth[k] = v
    title = exth.get('title') or mobi_meta.get('title') or pdb_name or filepath.stem
    author = exth.get('author', '')
    if isinstance(author, list):
        author = ', '.join(author)
    publisher = exth.get('publisher', '')
    description = exth.get('description', '')
    isbn = exth.get('isbn', '')
    subject = exth.get('subject', '')
    if isinstance(subject, list):
        subject = ', '.join(subject)
    asin = exth.get('asin', '')
    language = exth.get('language', '')
    cover_data, cover_mime = extract_cover(records, mobi_meta, exth)
    drm = has_drm(mobi_meta, records)
    ext = filepath.suffix.lower()
    if ext == '.azw3' or boundary is not None or mobi_meta.get('kind') == 8:
        fmt = 'AZW3'
    elif ext == '.azw':
        fmt = 'AZW'
    elif ext == '.kfx':
        fmt = 'KFX'
    else:
        fmt = 'MOBI'
    return {
        'title': title,
        'author': author,
        'publisher': publisher,
        'description': description,
        'isbn': isbn,
        'subject': subject,
        'asin': asin,
        'language': language,
        'coverData': cover_data,
        'coverMime': cover_mime,
        'drm': drm,
        'format': fmt,
    }


def detect_device():
    import string
    for letter in string.ascii_uppercase:
        drive = Path(f'{letter}:\\')
        if drive.is_dir():
            docs = drive / 'documents'
            system = drive / 'system'
            if docs.is_dir() and system.is_dir():
                return str(drive)
    return None


SIDECAR_DIRS = {'.sdr'}
SIDECAR_NAMES = {'metadata.kfx'}


def is_sidecar(root, path):
    parts = [p.lower() for p in path.relative_to(root).parts[:-1]]
    if any(p in SIDECAR_DIRS for p in parts):
        return True
    name = path.name
    if name.lower() in SIDECAR_NAMES:
        return True
    return name.startswith('CR!')


def fallback_title(path):
    stem = path.stem
    stem = re.sub(r'[_\s]+sample$', '', stem, flags=re.I)
    stem = re.sub(r'\s+-\s+unknown$', '', stem, flags=re.I)
    stem = re.sub(r'[_\s]+[A-Z0-9]{10}$', '', stem)
    title = re.sub(r'\s+', ' ', stem.replace('_', ' ')).strip()
    return title or path.stem


def scan_device(device_path):
    if not device_path:
        return []
    root = Path(device_path)
    books = []
    seen_ids = set()
    for ext in KINDLE_EXTS:
        for f in sorted(root.rglob(f'*{ext}')):
            if not f.is_file():
                continue
            if f.stat().st_size < 1024 or is_sidecar(root, f):
                continue
            book_id = hashlib.sha256(str(f.resolve()).lower().encode()).hexdigest()[:24]
            if book_id in seen_ids:
                continue
            seen_ids.add(book_id)
            meta = None
            if f.suffix.lower() != '.kfx':
                try:
                    meta = parse_book(f)
                except Exception:
                    logging.exception('Kindle scan %s', f)
            if meta is not None:
                books.append({
                    'id': book_id,
                    'title': meta['title'],
                    'author': meta['author'],
                    'publisher': meta['publisher'],
                    'description': meta['description'],
                    'isbn': meta['isbn'],
                    'subject': meta['subject'],
                    'asin': meta['asin'],
                    'language': meta['language'],
                    'format': meta['format'],
                    'drm': meta['drm'],
                    'path': str(f),
                    'size': f.stat().st_size,
                    'hasCover': meta['coverData'] is not None,
                })
            else:
                books.append({
                    'id': book_id,
                    'title': fallback_title(f),
                    'author': '',
                    'format': f.suffix.lstrip('.').upper(),
                    'drm': False,
                    'path': str(f),
                    'size': f.stat().st_size,
                    'hasCover': False,
                })
    return books


def book_cover(filepath):
    meta = parse_book(filepath)
    if meta['coverData'] and meta['coverMime']:
        return meta['coverData'], meta['coverMime']
    return None, None


def import_books(services, device_books, selected_ids):
    selected = [b for b in device_books if b['id'] in selected_ids]
    added = []
    for sb in selected:
        if any(x['id'] == sb['id'] for x in services.store['books']):
            continue
        src = Path(sb['path'])
        folder = services.folder(sb['title'])
        dest = folder / src.name
        import shutil
        shutil.copy2(str(src), str(dest))
        kind = 'Kindle'
        b = {
            'id': sb['id'],
            'title': sb['title'],
            'author': sb.get('author', ''),
            'publisher': sb.get('publisher', ''),
            'description': sb.get('description', ''),
            'isbn': sb.get('isbn', ''),
            'subject': sb.get('subject', ''),
            'asin': sb.get('asin', ''),
            'language': sb.get('language', ''),
            'kind': kind,
            'path': str(dest),
            'source': str(folder),
            'position': 0,
            'progress': 0,
            'bookmarks': [],
            'lastActive': 0,
            'kindleFormat': sb.get('format', 'MOBI'),
        }
        if sb.get('drm'):
            b['kindleDrm'] = True
        meta = {}
        if dest.suffix.lower() != '.kfx':
            try:
                meta = parse_book(str(dest))
            except Exception:
                logging.exception('Kindle import %s', dest)
        if meta.get('coverData') and meta.get('coverMime'):
            ext = 'jpg' if meta['coverMime'] == 'image/jpeg' else 'png'
            cover_path = folder / f'cover.{ext}'
            cover_path.write_bytes(meta['coverData'])
            b['cover'] = str(cover_path)
        services.store['books'].append(b)
        added.append(b)
    services.save()
    return services.state()


def find_calibre():
    import os
    import shutil as _sh
    exe = _sh.which('ebook-convert')
    if exe:
        return exe
    for base in (os.environ.get('ProgramFiles'), os.environ.get('ProgramFiles(x86)'), os.environ.get('LOCALAPPDATA')):
        if not base:
            continue
        for sub in ('Calibre2', 'Calibre 2', os.path.join('Programs', 'Calibre2')):
            candidate = Path(base) / sub / 'ebook-convert.exe'
            if candidate.is_file():
                return str(candidate)
    return None


def convert_book_file(src_path, dest_path, calibre_exe):
    import subprocess
    result = subprocess.run(
        [calibre_exe, str(src_path), str(dest_path), '--prefer-metadata-cover'],
        capture_output=True, text=True, timeout=300,
        creationflags=0x08000000,
    )
    if result.returncode != 0:
        raise ValueError(result.stderr.strip() or 'Conversion failed.')
    if not Path(dest_path).is_file():
        raise ValueError('Conversion produced no output file.')


def convert_book(services, book):
    src = Path(book.get('path') or '')
    if book.get('kind') != 'Kindle' and src.suffix.lower() not in KINDLE_EXTS:
        return services.view(book)
    if not src.is_file():
        raise ValueError('The book file is missing from its folder.')
    if src.suffix.lower() == '.kfx':
        raise ValueError('KFX books are copy-protected by Amazon and cannot be read here.')
    dest = src.with_suffix('.epub')
    if not dest.is_file():
        calibre = find_calibre()
        if not calibre:
            raise ValueError('Calibre is needed to convert Kindle formats to EPUB.')
        convert_book_file(src, dest, calibre)
    book['kindleFormat'] = book.get('kindleFormat') or src.suffix.lstrip('.').upper()
    book['path'] = str(dest)
    book['kind'] = 'EPUB'
    services.save()
    return services.view(book)


def export_to_device(services, book_ids, device_path):
    if not device_path:
        raise ValueError('No Kindle device detected.')
    dest_dir = Path(device_path) / 'documents'
    if not dest_dir.is_dir():
        raise ValueError('Kindle documents folder not found.')
    import shutil
    calibre = find_calibre()
    copied = []
    skipped = []
    errors = []
    for bid in book_ids:
        b = next((x for x in services.store['books'] if x['id'] == bid), None)
        if not b:
            continue
        src = b.get('path')
        if not src or not Path(src).is_file():
            skipped.append({'title': b['title'], 'reason': 'File not found'})
            continue
        src = Path(src)
        suffix = src.suffix.lower()
        dest_name = src.stem + ('.azw3' if suffix == '.epub' else suffix)
        dest = dest_dir / dest_name
        try:
            if suffix in KINDLE_EXTS:
                shutil.copy2(str(src), str(dest))
            elif suffix == '.epub':
                if not calibre:
                    skipped.append({'title': b['title'], 'reason': 'Calibre not found — install calibre to convert EPUB'})
                    continue
                convert_book_file(src, dest, calibre)
            else:
                skipped.append({'title': b['title'], 'reason': f'{suffix} not supported for Kindle'})
                continue
            copied.append(b['title'])
        except Exception as e:
            errors.append({'title': b['title'], 'reason': str(e)})
    return {'copied': copied, 'skipped': skipped, 'errors': errors}


def delete_device_book(device_books, book_id):
    b = next((x for x in device_books if x['id'] == book_id), None)
    if not b:
        raise ValueError('Book not found on Kindle device.')
    p = Path(b['path'])
    if p.is_file():
        from send2trash import send2trash
        send2trash(str(p))
    return True
