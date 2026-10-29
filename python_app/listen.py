"""Local ebook narration: text preparation, offline voice and cached speech."""
import array
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import tarfile
import threading
import time
import unicodedata
import uuid
import wave
from pathlib import Path

VOICE = 'kitten-micro-en-v0_8'
VOICE_URL = f'https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/{VOICE}.tar.bz2'
VOICE_SHA = '85faaea7511ca9d1d2f251fed0a4553bdf0d1ee046102fa60ddd8046c751f76f'
SPEAKERS = [{'id': 1, 'label': 'Original voice'}, {'id': 0, 'label': 'Hugo · male'}]
# Speaker ids are the model's own: sid 0 is the original 1:06 voice, sid 4 is Hugo.
SPEAKER_IDS = {1: 0, 0: 4}

TEXT_LIMIT = 8 * 1024 * 1024
MAX_SPAN = 2000
AUDIO_LIMIT = 512 * 1024 * 1024
DOWNLOAD_LIMIT = 120 * 1024 * 1024
ARCHIVE_LIMIT = 400 * 1024 * 1024

_CLOSERS = '"\u2019\u201d\')]'
_ABBREVIATIONS = re.compile(r'(?i:mr|mrs|ms|dr|prof|sr|jr|st|vs|etc)')
_TITLES = (('Mrs', 'Missus'), ('Mr', 'Mister'), ('Dr', 'Doctor'), ('Prof', 'Professor'), ('Ms', 'Miz'))
_WORD = re.compile(r"[^\W_]+(?:['\u2019\-][^\W_]+)*")
_DOC_ID = re.compile(r'^[a-f0-9]{64}$')
_NUMBER_WORDS_SMALL = ('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen '
                       'fifteen sixteen seventeen eighteen nineteen').split()
_NUMBER_WORDS_TENS = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')


def clean(value):
    text = str(value or '').replace('\u00ad', '')
    text = re.sub(r'(?<=[^\W\d_])-\r?\n(?=[^\W\d_])', '', text)
    text = re.sub(r'[\t\v\f ]+', ' ', text)
    text = re.sub(r' *\r?\n *', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    return text.strip()


def roman(value):
    if not re.fullmatch(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})', value):
        return None
    total = previous = 0
    for letter in reversed(value):
        current = (1, 5, 10, 50, 100, 500, 1000)['IVXLCDM'.index(letter)]
        total += -current if current < previous else current
        previous = current
    return total


def number_words(value):
    n = int(value)
    if n < 20:
        return _NUMBER_WORDS_SMALL[n]
    if n < 100:
        return _NUMBER_WORDS_TENS[n // 10] + ('' if n % 10 == 0 else ' ' + _NUMBER_WORDS_SMALL[n % 10])
    if n < 1000:
        return _NUMBER_WORDS_SMALL[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + number_words(n % 100))
    return _NUMBER_WORDS_SMALL[n // 1000] + ' thousand' + ('' if n % 1000 == 0 else ' ' + number_words(n % 1000))


def spoken(value):
    text = unicodedata.normalize('NFKC', clean(value)).replace('\u00a0', ' ')
    for title, replacement in _TITLES:
        text = re.sub(r'\b' + title + r'\.(?=\s)', replacement, text, flags=re.I)

    def announce(match):
        label, number = match.group(1), match.group(2)
        count = int(number) if number.isdigit() else roman(number)
        if count is None or not 0 <= count < 4000:
            return match.group(0)
        return label.capitalize() + ' ' + number_words(count)

    return re.sub(r'\b(chapter|book|part)\s+([IVXLCDM]+|\d+)\b(?!\.\d)', announce, text, flags=re.I)


def _abbreviation(text, point):
    if text[point] != '.':
        return False
    if 0 < point < len(text) - 1 and text[point - 1].isdigit() and text[point + 1].isdigit():
        return True
    start = point
    while start > 0 and text[start - 1].isalpha():
        start -= 1
    word = text[start:point]
    return bool(_ABBREVIATIONS.fullmatch(word)) or len(word) == 1


def _sentence_stop(text, point, limit):
    """Return the index just past a sentence ending at or after `point`, or -1."""
    char = text[point]
    if char == '\n' and point + 1 < limit and text[point + 1] == '\n':
        return point + 2
    if char not in '.!?':
        return -1
    after = point + 1
    while after < limit and text[after] in _CLOSERS:
        after += 1
    if after < len(text) and not text[after].isspace():
        return -1
    if _abbreviation(text, point):
        return -1
    return after


def chunk_end(text, start, span=600):
    limit = min(len(text), start + span)
    if limit == len(text):
        return limit
    best = -1
    for index in range(start + 1, limit):
        stop = _sentence_stop(text, index, len(text))
        if stop > 0:
            best = stop
    if best > start + min(80, span // 3):
        return best
    extended = min(len(text), limit + 300)
    for index in range(limit, extended):
        stop = _sentence_stop(text, index, extended)
        if stop > 0:
            return stop
    space = text.rfind(' ', start, limit)
    if space > start:
        return space + 1
    return limit


def sentence_ranges(text, start, end):
    ranges = []
    index = start
    while index < end:
        while index < end and text[index].isspace():
            index += 1
        if index >= end:
            break
        stop = end
        for point in range(index + 1, end):
            found = _sentence_stop(text, point, end)
            if found > 0:
                stop = min(found, end)
                break
        trimmed = stop
        while trimmed > index and text[trimmed - 1].isspace():
            trimmed -= 1
        if trimmed > index:
            ranges.append([index, trimmed])
        index = max(stop, index + 1)
    return ranges


def passages(text, sentences, limit=MAX_SPAN):
    result = []
    index = 0
    while index < len(sentences):
        target = 160 if not result else 600
        start, end = sentences[index]
        if end - start > limit:
            point = start
            while end - point > limit:
                cut = point + limit
                space = text.rfind(' ', point + limit // 2, cut)
                if space > point:
                    cut = space + 1
                result.append([point, cut])
                point = cut
                while point < end and text[point].isspace():
                    point += 1
            result.append([point, end])
            index += 1
            continue
        last = index
        probe = index + 1
        while probe < len(sentences) and sentences[probe][1] - start <= target:
            last = probe
            probe += 1
        result.append([start, sentences[last][1]])
        index = last + 1
    return result


def word_start(text, position):
    point = max(0, min(len(text), position))
    while point > 0 and not text[point - 1].isspace():
        point -= 1
    return point


def skip_words(text, position, count):
    at = max(0, min(len(text), position))
    if not count:
        return word_start(text, at)
    while at < len(text) and text[at].isspace():
        at += 1
    anchor_at = word_start(text, at)
    starts = [match.start() for match in _WORD.finditer(text)]
    anchor = next((start for start in starts if start >= anchor_at), len(text))
    if count > 0:
        ahead = [start for start in starts if start >= anchor]
        return ahead[count] if len(ahead) > count else len(text)
    behind = [start for start in starts if start < anchor]
    return behind[count] if len(behind) >= -count else 0


class Narration:
    def __init__(self, folder, media):
        self.folder = Path(folder)
        self.docs = self.folder / 'docs'
        self.audio = self.folder / 'audio'
        self.voice_root = self.folder / 'voice' / VOICE
        self.docs.mkdir(parents=True, exist_ok=True)
        self.audio.mkdir(parents=True, exist_ok=True)
        self._media = media
        self._lock = threading.RLock()
        self._engine_lock = threading.Lock()
        self._speak_lock = threading.Lock()
        self._engine = None
        self._rate = 24000
        self._voice = {'downloading': False, 'progress': 0, 'error': ''}
        self._docs = {}
        self.progress_file = self.folder / 'progress.json'
        try:
            self._progress = json.loads(self.progress_file.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            self._progress = {}

    # ---- session documents ----

    def installed(self):
        return all((self.voice_root / name).exists() for name in ('model.onnx', 'voices.bin', 'tokens.txt')) \
            and (self.voice_root / 'espeak-ng-data' / 'phondata').is_file()

    def voice(self):
        with self._lock:
            state = dict(self._voice)
        return {'installed': self.installed(), 'downloading': state['downloading'],
                'progress': state['progress'], 'error': state['error'], 'speakers': SPEAKERS}

    def prepare(self, spec):
        if not isinstance(spec, dict):
            raise ValueError('There is no text to read yet.')
        book = str(spec.get('bookId') or '')[:120]
        key = str(spec.get('key') or '').strip()
        if not key or len(key) > 600:
            raise ValueError('The reading could not be identified.')
        title = re.sub(r'\s+', ' ', str(spec.get('title') or '')).strip()[:300] or 'Reading'
        items = spec.get('chapters')
        if not isinstance(items, list) or not items:
            raise ValueError('There is no text to read yet.')
        if len(items) > 4000:
            raise ValueError('This book has too many sections to read at once.')
        text = ''
        chapters = []
        truncated = False
        for index, item in enumerate(items):
            value = item.get('text') if isinstance(item, dict) else ''
            cleaned = clean(value)
            if not cleaned:
                continue
            if len(cleaned) > TEXT_LIMIT:
                cleaned = cleaned[:TEXT_LIMIT]
                truncated = True
            if text:
                text += '\n\n'
            if len(text) + len(cleaned) > TEXT_LIMIT:
                truncated = True
                break
            start = len(text)
            text += cleaned
            label = re.sub(r'\s+', ' ', str((item.get('label') if isinstance(item, dict) else '') or '')).strip()[:120]
            chapters.append({'label': label or f'Section {index + 1}', 'start': start})
        if not text.strip() or not chapters:
            raise ValueError('No selectable text was found. Scanned PDFs need OCR before listening.')
        for index, chapter in enumerate(chapters):
            chapter['end'] = chapters[index + 1]['start'] - 2 if index + 1 < len(chapters) else len(text)
            chapter['end'] = max(chapter['start'], chapter['end'])
            chapter['sentences'] = sentence_ranges(text, chapter['start'], chapter['end'])
            chapter['passages'] = passages(text, chapter['sentences'])
        identity = hashlib.sha256(key.encode('utf-8')).hexdigest()
        document = {'id': identity, 'key': key, 'book': book, 'title': title, 'text': text,
                    'chapters': chapters, 'truncated': truncated}
        self._write(document)
        saved = self._progress.get(identity) or {}
        position = max(0, min(len(text), int(saved.get('position') or 0)))
        return self._public(document, position)

    def load(self, identity):
        identity = str(identity or '')
        if not _DOC_ID.fullmatch(identity):
            raise ValueError('That reading is no longer available.')
        if identity in self._docs:
            return self._docs[identity]
        path = self.docs / f'{identity}.json'
        try:
            document = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            raise ValueError('That reading is no longer available. Open the book again.')
        if not isinstance(document.get('chapters'), list) or not isinstance(document.get('text'), str):
            raise ValueError('That reading is no longer available. Open the book again.')
        self._docs[identity] = document
        return document

    def resume(self):
        latest = max(self._progress.items(), key=lambda item: item[1].get('time') or 0, default=None)
        if not latest:
            return None
        try:
            document = self.load(latest[0])
        except ValueError:
            return None
        position = max(0, min(len(document['text']), int(latest[1].get('position') or 0)))
        return self._public(document, position)

    def save_position(self, identity, position):
        document = self.load(identity)
        if not document.get('book'):
            return True
        position = max(0, min(len(document['text']), int(position or 0)))
        with self._lock:
            self._progress[document['id']] = {'position': position, 'time': int(time.time() * 1000)}
            self._progress = dict(sorted(self._progress.items(), key=lambda item: item[1].get('time') or 0)[-40:])
            tmp = self.progress_file.with_suffix('.json.tmp')
            tmp.write_text(json.dumps(self._progress, ensure_ascii=False), encoding='utf-8')
            os.replace(tmp, self.progress_file)
        return True

    def position(self, identity, position, words=0):
        document = self.load(identity)
        point = max(0, min(len(document['text']), int(position or 0)))
        return {'position': skip_words(document['text'], point, int(words or 0))}

    def _public(self, document, position):
        return {'id': document['id'], 'title': document['title'], 'bookId': document.get('book') or '',
                'text': document['text'], 'chapters': document['chapters'],
                'truncated': document.get('truncated', False), 'position': position,
                'voice': self.voice()}

    def _write(self, document):
        path = self.docs / f"{document['id']}.json"
        tmp = path.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(document, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        os.replace(tmp, path)
        self._docs[document['id']] = document

    # ---- speech ----

    def speak(self, identity, start, end, rate=1.0, speaker=1):
        document = self.load(identity)
        text = document['text']
        start = max(0, min(len(text), int(start or 0)))
        end = max(start, min(len(text), int(end or 0)))
        if end <= start:
            raise ValueError('There is nothing to read at this point.')
        end = min(end, start + MAX_SPAN)
        rate = max(.5, min(2.5, float(rate or 1)))
        speaker = 1 if int(speaker or 0) == 1 else 0
        chunk = text[start:end]
        name = hashlib.sha1(f'{VOICE}|{SPEAKER_IDS[speaker]}|{rate:.2f}|{chunk}'.encode('utf-8')).hexdigest()[:40]
        path = self.audio / f'{name}.wav'
        if not path.is_file():
            engine, sample_rate = self._load_engine()
            with self._speak_lock:
                if not path.is_file():
                    samples = engine.generate(self._spoken_text(chunk), sid=SPEAKER_IDS[speaker], speed=rate).samples
                    if not samples or not any(abs(value) > .002 for value in samples):
                        raise ValueError('The offline voice returned no audio. Try Play again.')
                    self._write_wav(path, samples, sample_rate)
                    self._prune()
        seconds = max(.05, (path.stat().st_size - 44) / 2 / self._rate)
        return {'start': start, 'end': end, 'url': self._media(str(path)), 'rate': rate,
                'speaker': speaker, 'seconds': round(seconds, 3)}

    @staticmethod
    def _spoken_text(chunk):
        paragraphs = [spoken(part) for part in re.split(r'\n[ \t]*\n+', chunk) if part.strip()]
        return '\n\n'.join(paragraphs) or spoken(chunk)

    def _write_wav(self, path, samples, rate):
        frames = array.array('h', (int(round(max(-1.0, min(1.0, float(value))) * 32767)) for value in samples))
        if sys.byteorder == 'big':
            frames.byteswap()
        tmp = path.with_suffix('.wav.tmp')
        with wave.open(str(tmp), 'wb') as handle:
            handle.setnchannels(1)
            handle.setsampwidth(2)
            handle.setframerate(rate)
            handle.writeframes(frames.tobytes())
        os.replace(tmp, path)
        self._rate = rate

    def _load_engine(self):
        with self._engine_lock:
            if self._engine is not None:
                return self._engine, self._rate
            if not self.installed():
                raise ValueError('Download the offline voice before listening.')
            try:
                import sherpa_onnx
            except ImportError:
                logging.exception('sherpa-onnx is missing')
                raise ValueError('The offline voice is not available in this build. Reinstall Clavis.')
            root = self.voice_root
            config = sherpa_onnx.OfflineTtsConfig(
                model=sherpa_onnx.OfflineTtsModelConfig(
                    kitten=sherpa_onnx.OfflineTtsKittenModelConfig(
                        model=str(root / 'model.onnx'), voices=str(root / 'voices.bin'),
                        tokens=str(root / 'tokens.txt'), data_dir=str(root / 'espeak-ng-data')),
                    num_threads=2),
                max_num_sentences=1, silence_scale=1.5)
            engine = sherpa_onnx.OfflineTts(config)
            self._rate = int(engine.sample_rate) or 24000
            self._engine = engine
            return self._engine, self._rate

    def _prune(self):
        files = []
        total = 0
        for file in self.audio.glob('*.wav'):
            try:
                stat = file.stat()
            except OSError:
                continue
            files.append((stat.st_mtime, stat.st_size, file))
            total += stat.st_size
        if total <= AUDIO_LIMIT:
            return
        for _, size, file in sorted(files):
            try:
                file.unlink()
            except OSError:
                continue
            total -= size
            if total <= AUDIO_LIMIT * .75:
                break

    # ---- offline voice download ----

    def close(self):
        with self._engine_lock:
            self._engine = None

    def download(self):
        if self.installed():
            return self.voice()
        with self._lock:
            if self._voice['downloading']:
                return self.voice()
            self._voice.update(downloading=True, progress=0, error='')
        threading.Thread(target=self._download, daemon=True).start()
        return self.voice()

    def _download(self):
        import requests
        work = self.folder / 'voice'
        work.mkdir(parents=True, exist_ok=True)
        archive = work / f'{VOICE}.download'
        stage = work / f'stage-{uuid.uuid4().hex}'
        try:
            total = 0
            digest = hashlib.sha256()
            with requests.get(VOICE_URL, stream=True, timeout=(20, 90),
                              headers={'User-Agent': 'Clavis/1.0 offline voice'}) as response:
                response.raise_for_status()
                length = int(response.headers.get('content-length') or 0)
                with open(archive, 'wb') as handle:
                    for block in response.iter_content(262144):
                        if not block:
                            continue
                        total += len(block)
                        if total > DOWNLOAD_LIMIT:
                            raise ValueError('The voice download was larger than expected.')
                        digest.update(block)
                        handle.write(block)
                        percent = int(total * 100 / length) if length else 0
                        with self._lock:
                            self._voice['progress'] = min(99, percent)
            if digest.hexdigest() != VOICE_SHA:
                raise ValueError('The voice download did not match the published checksum.')
            stage.mkdir(parents=True, exist_ok=True)
            with tarfile.open(archive, 'r:bz2') as tar:
                members = tar.getmembers()
                if len(members) > 4000 or sum(m.size for m in members) > ARCHIVE_LIMIT:
                    raise ValueError('The voice archive was larger than expected.')
                for member in members:
                    name = member.name.replace('\\', '/')
                    if name != VOICE and not name.startswith(VOICE + '/'):
                        raise ValueError('The voice archive had an unexpected layout.')
                    if not (member.isfile() or member.isdir()):
                        raise ValueError('The voice archive had an unexpected layout.')
                tar.extractall(stage, filter='data')
            target = self.voice_root
            source = stage / VOICE
            if not (source / 'model.onnx').is_file():
                raise ValueError('The voice archive did not contain the model.')
            if target.exists() and not self.installed():
                shutil.rmtree(target, ignore_errors=True)
            if not target.exists():
                os.replace(source, target)
            with self._lock:
                self._voice.update(downloading=False, progress=100, error='')
        except Exception as error:
            logging.exception('Voice download')
            with self._lock:
                self._voice.update(downloading=False, progress=0, error=str(error) or 'The voice download failed.')
        finally:
            try:
                archive.unlink()
            except OSError:
                pass
            shutil.rmtree(stage, ignore_errors=True)
