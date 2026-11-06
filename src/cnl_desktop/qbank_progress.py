"""Qbank attempts and bookmarks are user data, independent of question files."""
import copy
from pathlib import Path
import threading
import time
from . import study_packs

_LOCK=threading.RLock()


def _path(data_root: Path):
    return data_root/'performance'/'qbank-progress.json'


def read(data_root: Path):
    with _LOCK:
        target=_path(data_root)
        if not target.exists():return {'version':1,'banks':{}}
        payload=study_packs._read_json(target)
        if not isinstance(payload,dict) or not isinstance(payload.get('banks'),dict):
            raise ValueError('Could not read Qbank progress. The existing file has been kept.')
        return payload


def update(data_root: Path, payload: dict):
    bank=payload.get('bank');op=payload.get('op')
    if not isinstance(bank,str) or not bank or len(bank)>2000:
        raise ValueError('Invalid Qbank identity.')
    with _LOCK:
        state=read(data_root)
        entry=copy.deepcopy(state['banks'].get(bank,{'bookmarks':[],'attempt':None}))
        if op=='bookmark':
            key=payload.get('question');marked=payload.get('marked')
            if not isinstance(key,str) or not key or len(key)>1000 or type(marked) is not bool:
                raise ValueError('Invalid bookmark.')
            marks=set(entry.get('bookmarks',[]))
            if marked:marks.add(key)
            else:marks.discard(key)
            entry['bookmarks']=sorted(marks)
        elif op=='retry':
            entry['attempt']=None
        elif op=='attempt':
            attempt=payload.get('attempt')
            if not isinstance(attempt,dict):raise ValueError('Missing attempt.')
            answers=attempt.get('answers');index=attempt.get('index');status=attempt.get('status')
            if (not isinstance(answers,list) or not 1<=len(answers)<=10000
                or any(a is not None and (type(a) is not int or not -1<=a<=31) for a in answers)
                or type(index) is not int or not 0<=index<len(answers)
                or status not in {'paused','submitted'}):raise ValueError('Invalid attempt data.')
            signature=attempt.get('signature');identity=attempt.get('id')
            if not isinstance(signature,str) or len(signature)>200 or not isinstance(identity,str) or not 1<=len(identity)<=100:
                raise ValueError('Invalid attempt identity.')
            old=entry.get('attempt') or {}
            if old.get('status')=='submitted' and old.get('id')==identity:
                return {'entry':entry,'newSubmission':False}
            score=attempt.get('score',0);total=attempt.get('total',0)
            if type(score) is not int or type(total) is not int or not 0<=score<=total<=len(answers):
                raise ValueError('Invalid result.')
            if status=='submitted' and any(a is None for a in answers):
                raise ValueError('Answer or review every question before submitting.')
            entry['attempt']={key:attempt[key] for key in ('id','signature','answers','index','status')}
            entry['attempt'].update(score=score,total=total,updatedAt=int(time.time()*1000))
            if status=='submitted':entry['attempt']['submittedAt']=entry['attempt']['updatedAt']
        else:raise ValueError('Unknown Qbank progress action.')
        state['banks'][bank]=entry
        study_packs._write_json(_path(data_root),state)
        return {'entry':entry,'newSubmission':op=='attempt' and entry['attempt']['status']=='submitted'}
