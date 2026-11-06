"""Native, user-selected HTML conversion destinations; HTML parsing stays inert in UI."""
import json
import os
from pathlib import Path
import secrets
import threading
import time


class QbankConverter:
    def __init__(self):
        self._window = None
        self._files = {}
        self._lock = threading.Lock()

    def choose_qbank_html(self):
        import webview
        if not self._lock.acquire(blocking=False):
            return {'error': 'A conversion is already open.'}
        try:
            selected = self._window.create_file_dialog(webview.FileDialog.OPEN,
                allow_multiple=True, file_types=('HTML files (*.html;*.htm)',))
            self._files.clear()
            files = []
            for name in dict.fromkeys(selected or []):
                path = Path(name).resolve()
                row = {'name': path.name}
                try:
                    if path.suffix.lower() not in {'.html', '.htm'}:
                        raise ValueError('Choose an HTML file.')
                    if path.stat().st_size > 10 * 1024 * 1024:
                        raise ValueError('HTML file exceeds 10 MB.')
                    raw = path.read_bytes()
                    # Honour declared HTML encodings without executing any source scripts.
                    from lxml.html import document_fromstring, tostring
                    from lxml.etree import HTMLParser
                    try:
                        source_text = raw.decode('utf-8-sig')
                    except UnicodeDecodeError:
                        source_text = tostring(document_fromstring(raw, parser=HTMLParser(no_network=True)), encoding='unicode')
                    token = secrets.token_urlsafe(24)
                    self._files[token] = path
                    row.update(token=token, html=source_text)
                except (ValueError, OSError, LookupError) as error:
                    row['error'] = str(error)
                files.append(row)
            return {'files': files}
        finally:
            self._lock.release()

    def save_qbank_json(self, token, questions):
        with self._lock:
            source = self._files.pop(str(token), None)
            if source is None:
                return {'error': 'Choose the HTML file again.'}
            try:
                if not isinstance(questions, list) or not questions or len(questions) > 10000:
                    raise ValueError('No valid questions were extracted.')
                for question in questions:
                    if (not isinstance(question, dict) or not isinstance(question.get('question'), str)
                        or not isinstance(question.get('options'), list) or len(question['options']) < 2):
                        raise ValueError('Invalid question data.')
                folder = source.parent / source.stem
                # Reject folder symlinks/junctions which redirect output away from the selected file.
                if folder.resolve() != folder.absolute():
                    raise ValueError('Output folder redirects to another location.')
                folder.mkdir(exist_ok=True)
                destination = folder / (source.stem + '.json')
                if destination.is_symlink() or destination.resolve().parent != folder.resolve():
                    raise ValueError('Invalid JSON destination.')
                payload = {'version': 1, 'folder': 'HTML Imports', 'document': source.stem,
                    'headingText': source.stem, 'headingIndex': 0,
                    'madeAt': int(time.time()*1000), 'sourceFile': source.name, 'questions': questions}
                content = json.dumps(payload, ensure_ascii=False, indent=2).encode('utf-8')
                if len(content) > 50 * 1024 * 1024:
                    raise ValueError('Converted JSON exceeds 50 MB.')
                backup = None
                if destination.exists():
                    previous = destination.read_bytes()
                    backup = folder / '_backups' / (source.stem + '.' + str(time.time_ns()) + '.json.bak')
                    backup.parent.mkdir(exist_ok=True)
                    backup.write_bytes(previous)
                    if backup.read_bytes() != previous:
                        raise OSError('Could not verify the previous JSON backup.')
                temporary = destination.with_name('.' + destination.name + '.' + secrets.token_hex(8) + '.tmp')
                try:
                    temporary.write_bytes(content)
                    try:
                        os.replace(temporary, destination)
                    except PermissionError:
                        if backup is None:
                            raise
                        try:
                            destination.write_bytes(content)
                        except OSError:
                            destination.write_bytes(previous)
                            raise
                finally:
                    temporary.unlink(missing_ok=True)
                if destination.read_bytes() != content:
                    raise OSError('Could not verify the saved JSON.')
                return {'path': str(destination), 'count': len(questions),
                    'review': sum(bool(q.get('answerReviewRequired')) for q in questions),
                    'backup': str(backup) if backup else None}
            except (ValueError, OSError, TypeError) as error:
                return {'error': str(error)}
