"""Online book metadata lookup, in the spirit of Calibre's downloader."""
import base64
import html
import logging
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from urllib.parse import urlparse

import requests

TIMEOUT = 15
HEADERS = {'User-Agent': 'Clavis/1.0 (book metadata lookup)'}
COVER_HOSTS = {'covers.openlibrary.org', 'openlibrary.org', 'archive.org'}
MAX_COVER = 8 * 1024 * 1024
RESULT_LIMIT = 6

_cache = {}
_lock = threading.Lock()


def _json(url, params):
    response = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def _plain(value, limit=2000):
    if isinstance(value, list):
        value = ' '.join(str(item) for item in value if item)
    text = re.sub(r'<[^>]+>', ' ', str(value or ''))
    text = html.unescape(re.sub(r'<br\s*/?>', ' ', text, flags=re.I))
    return re.sub(r'\s+', ' ', text).strip()[:limit]


def _slug(value):
    return re.sub(r'[^a-z0-9]+', ' ', str(value or '').lower()).strip()


def _query_text(value):
    # Hyphens negate terms in Open Library and punctuation breaks IA's query.
    text = re.sub(r'\(\s*\d{4}\s*\)', ' ', str(value or ''))
    text = re.sub(r'[^\w\s]+', ' ', text, flags=re.UNICODE)
    return re.sub(r'\s+', ' ', text).strip()


def _authors(value):
    if isinstance(value, str):
        value = re.split(r'\s*(?:;|\band\b)\s*', value)
    return [str(a).strip() for a in (value or []) if str(a).strip()][:6]


def _open_library(query, isbn=''):
    params = {'limit': 8, 'fields': 'key,title,author_name,publisher,first_publish_year,isbn,subject,cover_i'}
    if isbn:
        params['isbn'] = isbn
    else:
        params['q'] = query
    data = _json('https://openlibrary.org/search.json', params)
    results = []
    for doc in data.get('docs') or []:
        title = _plain(doc.get('title'), 300)
        if not title:
            continue
        isbns = [str(i) for i in (doc.get('isbn') or []) if i]
        isbn = next((i for i in isbns if len(i) == 13), isbns[0] if isbns else '')
        cover = f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-L.jpg" if doc.get('cover_i') else ''
        thumb = f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-M.jpg" if doc.get('cover_i') else ''
        results.append({
            'source': 'Open Library', 'title': title, 'authors': _authors(doc.get('author_name')),
            'publisher': _plain((doc.get('publisher') or [''])[0], 300),
            'published': str(doc.get('first_publish_year') or ''),
            'isbn': isbn, 'tags': [_plain(s, 60) for s in (doc.get('subject') or [])[:8]],
            'description': '', 'coverUrl': cover, 'thumbUrl': thumb,
        })
    return results


def _internet_archive(query, isbn=''):
    cleaned = query.strip()
    if not cleaned and not isbn:
        return []
    search = f'isbn:({isbn})' if isbn else f'{cleaned} AND mediatype:texts'
    data = _json('https://archive.org/advancedsearch.php', {
        'q': search,
        'fl[]': ['identifier', 'title', 'creator', 'year', 'publisher', 'isbn', 'description'],
        'rows': 8, 'page': 1, 'output': 'json',
    })
    results = []
    for doc in (data.get('response') or {}).get('docs') or []:
        title = _plain(doc.get('title'), 300)
        if not title or not doc.get('identifier'):
            continue
        isbns = doc.get('isbn') or []
        if isinstance(isbns, str):
            isbns = isbns.split()
        isbns = [str(i) for i in isbns if i]
        cover = f"https://archive.org/services/img/{doc['identifier']}"
        results.append({
            'source': 'Internet Archive', 'title': title, 'authors': _authors(doc.get('creator')),
            'publisher': _plain(doc.get('publisher'), 300),
            'published': str(doc.get('year') or ''),
            'isbn': next((i for i in isbns if len(i) == 13), isbns[0] if isbns else ''),
            'tags': [], 'description': _plain(doc.get('description'), 2000),
            'coverUrl': cover, 'thumbUrl': cover,
        })
    return results


def _crossref(query, isbn=''):
    params = {'rows': 10, 'select': 'title,author,publisher,issued,ISBN,type,abstract'}
    if isbn:
        params['filter'] = 'isbn:' + isbn
    else:
        params['query.bibliographic'] = query
    data = _json('https://api.crossref.org/works', params)
    results = []
    for item in (data.get('message') or {}).get('items') or []:
        if not re.search(r'book|monograph', str(item.get('type') or ''), re.I):
            continue
        titles = item.get('title') or []
        title = _plain(titles[0] if titles else '', 300)
        if not title:
            continue
        authors = []
        for person in item.get('author') or []:
            name = ' '.join(x for x in (person.get('given'), person.get('family')) if x)
            if name:
                authors.append(name)
        issued = (item.get('issued') or {}).get('date-parts') or [[]]
        year = str((issued[0] or [''])[0] or '')
        isbns = item.get('ISBN') or []
        results.append({
            'source': 'Crossref', 'title': title, 'authors': authors[:6],
            'publisher': _plain(item.get('publisher'), 300), 'published': year,
            'isbn': (isbns[0] if isbns else ''), 'tags': [],
            'description': _plain(item.get('abstract'), 2000),
            'coverUrl': '', 'thumbUrl': '',
        })
    return results


def _isbn_variants(value):
    digits = re.sub(r'[^0-9Xx]', '', str(value or '')).upper()
    variants = set()
    if len(digits) == 10:
        variants.add(digits)
        core = '978' + digits[:9]
        total = sum(int(core[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
        variants.add(core + str((10 - total % 10) % 10))
    elif len(digits) == 13 and digits.isdigit():
        variants.add(digits)
        if digits.startswith('978'):
            core = digits[3:12]
            total = sum(int(core[i]) * (10 - i) for i in range(9))
            variants.add(core + 'X' if total % 11 == 10 else core + str((11 - total % 11) % 11))
    return variants


def _key(candidate):
    isbn = re.sub(r'[^0-9Xx]', '', str(candidate.get('isbn') or ''))
    if isbn:
        return 'isbn:' + isbn
    authors = candidate.get('authors') or ['']
    return 'title:' + _slug(candidate.get('title')) + '|' + _slug(authors[0] if authors else '')


def _score(candidate, query, isbn=''):
    if isbn:
        found = re.sub(r'[^0-9Xx]', '', str(candidate.get('isbn') or ''))
        score = 1.0 if found == isbn else 0.0
    else:
        title = _slug(candidate.get('title'))
        wanted = _slug(query)
        score = SequenceMatcher(None, title, wanted).ratio()
        if title and title == wanted:
            score += 0.6
        elif wanted and (title.startswith(wanted) or wanted.startswith(title)):
            score += 0.25
        if candidate.get('isbn'):
            score += 0.05
        authors = candidate.get('authors') or []
        last = _slug(authors[0]).split()[-1:] if authors else []
        if last and last[0] in _slug(query).split():
            score += 0.35
    if candidate.get('coverUrl'):
        score += 0.1
    return score


def _download(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in COVER_HOSTS:
        raise ValueError('That cover address is not supported.')
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT, stream=True)
    response.raise_for_status()
    mime = (response.headers.get('content-type') or '').split(';')[0].strip().lower()
    if not mime.startswith('image/'):
        raise ValueError('That address is not an image.')
    data = b''
    for chunk in response.iter_content(65536):
        data += chunk
        if len(data) > MAX_COVER:
            raise ValueError('The cover image is too large.')
    return data, _sniff(data, mime)


def _sniff(data, fallback='image/jpeg'):
    if data[:3] == b'\xff\xd8\xff':
        return 'image/jpeg'
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return 'image/png'
    if data[:4] == b'GIF8':
        return 'image/gif'
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'image/webp'
    return fallback


def _thumb(url):
    if not url:
        return None
    try:
        data, mime = _download(url)
        return 'data:' + mime + ';base64,' + base64.b64encode(data).decode()
    except Exception:
        return None


def search(query='', isbn=''):
    query = (query or '').strip()
    isbn = re.sub(r'[^0-9Xx]', '', isbn or '')
    if not isbn and re.fullmatch(r'(?:97[89][-\s]?)?[0-9][0-9\-\s]{7,15}[0-9Xx]', query):
        candidates = _isbn_variants(query)
        if candidates:
            isbn = next(iter(candidates))
    if not isbn:
        query = _query_text(query)
    key = (query.lower(), isbn.lower())
    with _lock:
        cached = _cache.get(key)
    if cached is not None:
        return cached
    if not query and not isbn:
        raise ValueError('Enter a title, author or ISBN to search for.')
    results, failures = [], 0
    with ThreadPoolExecutor(max_workers=3) as pool:
        jobs = [pool.submit(_open_library, query, isbn), pool.submit(_internet_archive, query, isbn),
                pool.submit(_crossref, query, isbn)]
        for job in jobs:
            try:
                results.extend(job.result())
            except Exception:
                failures += 1
                logging.warning('Metadata source failed', exc_info=True)
    if not results and failures == len(jobs):
        raise ValueError('The metadata services could not be reached. Check your internet connection and try again.')
    if isbn:
        wanted = _isbn_variants(isbn)
        results = [c for c in results if _isbn_variants(c.get('isbn')) & wanted]
    merged = {}
    for candidate in results:
        candidate['author'] = ', '.join(candidate.get('authors') or [])
        candidate['subject'] = ', '.join(candidate.get('tags') or [])
        key_ = _key(candidate)
        if key_ not in merged:
            merged[key_] = candidate
            continue
        kept = merged[key_]
        for field in ('publisher', 'published', 'isbn', 'description', 'coverUrl', 'thumbUrl'):
            if not kept.get(field) and candidate.get(field):
                kept[field] = candidate[field]
    ranked = sorted(merged.values(), key=lambda c: _score(c, query, isbn), reverse=True)[:RESULT_LIMIT]
    with ThreadPoolExecutor(max_workers=4) as pool:
        thumbs = list(pool.map(lambda c: _thumb(c.get('thumbUrl') or c.get('coverUrl')), ranked))
    for candidate, thumb in zip(ranked, thumbs):
        candidate['coverThumb'] = thumb
    with _lock:
        if len(_cache) > 30:
            _cache.clear()
        _cache[key] = ranked
    return ranked


def cover(url):
    return _download(url)
