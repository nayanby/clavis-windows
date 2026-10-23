"""Kindle device detection, MOBI/AZW3 metadata parsing, import and export."""
import hashlib
import json
import logging
import os
import struct
import time
from pathlib import Path

KINDLE_EXTS = {'.mobi', '.azw', '.azw3', '.kfx'}
EXTH_TYPES = {
    100: 'author', 102: 'publisher', 103: 'language', 104: 'asin',
    105: 'isbn', 109: 'subject', 110: 'publishDate', 113: 'asin',
    201: 'description', 202: 'contributor', 203: 'rights',
    204: 'subject', 205: 'review', 206: 'source', 207: 'asin',
    208: 'asin', 501: 'coverOffset', 502: 'thumbOffset', 503: 'hasFakeCover',
    504: 'sampleStart', 505: 'sampleEnd', 521: 'genre',
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
                if key in meta and isinstance(meta[key], str):
                    meta[key] = [meta[key], text]
                elif isinstance(meta[key], list):
                    meta[key].append(text)
                else:
                    meta[key] = text
        pos += rlen
    return meta


def parse_mobi_header(record):
    if len(record) < 16 + 232:
        return {}, {}
    palm = record[:16]
    compression, unused, text_len, text_records, enc = struct.unpack_from('>HHIII', palm)
    mobi = record[16:]
    ml = struct.unpack_from('>I', mobi, 20)[0]
    if ml < 232:
        return {}, {}
    kind = struct.unpack_from('>I', mobi, 24)[0]
    enc_val = struct.unpack_from('>I', mobi, 28)[0]
    exth_flag = mobi[31] if len(mobi) > 31 else 0
    title_off = struct.unpack_from('>I', mobi, 84)[0]
    title_len = struct.unpack_from('>I', mobi, 88)[0]
    locale = struct.unpack_from('>I', mobi, 92)[0] if len(mobi) > 95 else 0
    meta = {'encoding': enc_val, 'kind': kind, 'locale': locale}
    if title_off < len(record) and title_len:
        end = min(title_off + title_len, len(record))
        raw = record[title_off:end].split(b'\x00')[0]
        try:
            t = raw.decode('utf-8').strip()
        except UnicodeDecodeError:
            t = raw.decode('latin-1', errors='replace').strip()
        if t:
            meta['title'] = t
    exth = {}
    if exth_flag & 0x40 and ml >= 152:
        eo = 16 + ml
        el = struct.unpack_from('>I', mobi, 148)[0] if ml >= 152 else 0
        if eo + el <= len(record) and el > 0:
            exth = parse_exth(record, eo, el)
    return meta, exth


def parse_kf8_header(records, boundary):
    if boundary >= len(records):
        return {}
    rec = records[boundary]
    if len(rec) < 256:
        return {}
    if rec[:4] != b'KF8\x00' and rec[:8] != b'\x00\x00\x00\x00':
        pass
    ml = struct.unpack_from('>I', rec, 20)[0] if len(rec) > 20 else 0
    if ml < 232:
        return {}
    meta = {}
    title_off = struct.unpack_from('>I', rec, 84)[0] if ml > 87 else 0
    title_len = struct.unpack_from('>I', rec, 88)[0] if ml > 91 else 0
    if title_off < len(rec) and title_len:
        end = min(title_off + title_len, len(rec))
        raw = rec[title_off:end].split(b'\x00')[0]
        try:
            t = raw.decode('utf-8').strip()
        except UnicodeDecodeError:
            t = raw.decode('latin-1', errors='replace').strip()
        if t:
            meta['title'] = t
    if ml >= 152:
        el = struct.unpack_from('>I', rec, 148)[0]
        eo = 16 + ml
        if eo + el <= len(rec) and el > 0:
            exth = parse_exth(rec, eo, el)
            for k, v in exth.items():
                if k not in meta or k in ('author', 'subject'):
                    meta[k] = v
    return meta


def find_boundary(records, mobi_meta):
    if mobi_meta.get('kind') == 8:
        if len(records) > 1:
            rec0 = records[0]
            if len(rec0) >= 16 + 232:
                ml = struct.unpack_from('>I', rec0, 16 + 20)[0]
                if ml >= 108:
                    offset = struct.unpack_from('>I', rec0, 16 + 108)[0]
                    if offset < len(records):
                        return offset
    return None


def extract_cover(records, mobi_meta, exth):
    cover_off = None
    try:
        cover_off = int(exth.get('coverOffset', -1))
    except (ValueError, TypeError):
        cover_off = None
    if cover_off is not None and 0 <= cover_off < len(records):
        data = records[cover_off]
        if data[:3] == b'\xff\xd8\xff':
            return data, 'image/jpeg'
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            return data, 'image/png'
    thumb_off = None
    try:
        thumb_off = int(exth.get('thumbOffset', -1))
    except (ValueError, TypeError):
        thumb_off = None
    if thumb_off is not None and 0 <= thumb_off < len(records):
        data = records[thumb_off]
        if data[:3] == b'\xff\xd8\xff':
            return data, 'image/jpeg'
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            return data, 'image/png'
    return None, None


def has_drm(mobi_meta, records):
    if mobi_meta.get('kind') is not None and len(records) > 0:
        rec0 = records[0]
        if len(rec0) >= 16 + 232:
            ml = struct.unpack_from('>I', rec0, 16 + 20)[0]
            if ml >= 200:
                drm_off = struct.unpack_from('>I', rec0, 16 + 168)[0]
                if drm_off != 0xFFFFFFFF and drm_off > 0:
                    return True
    return False


def parse_book(filepath):
    filepath = Path(filepath)
    data = filepath.read_bytes()
    pdb_name, records = parse_pdb(data)
    if not records:
        raise ValueError('This file contains no readable records.')
    mobi_meta, exth = parse_mobi_header(records[0])
    boundary = find_boundary(records, mobi_meta)
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
        'format': 'AZW3' if boundary is not None else 'MOBI',
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
            if f.stat().st_size < 1024:
                continue
            book_id = hashlib.sha256(str(f.resolve()).lower().encode()).hexdigest()[:24]
            if book_id in seen_ids:
                continue
            seen_ids.add(book_id)
            try:
                meta = parse_book(f)
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
            except Exception:
                logging.exception('Kindle scan %s', f)
                books.append({
                    'id': book_id,
                    'title': f.stem.replace('_', ' '),
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
        meta = parse_book(str(dest))
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
    import shutil as _sh
    return _sh.which('ebook-convert')


def convert_to_azw3(src_path, dest_path, calibre_exe):
    import subprocess
    result = subprocess.run(
        [calibre_exe, str(src_path), str(dest_path),
         '--no-default-epub-cover', '--prefer-metadata-cover'],
        capture_output=True, text=True, timeout=300,
        creationflags=0x08000000,
    )
    if result.returncode != 0:
        raise ValueError(result.stderr.strip() or 'Conversion failed.')
    if not Path(dest_path).is_file():
        raise ValueError('Conversion produced no output file.')


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
                convert_to_azw3(src, dest, calibre)
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
