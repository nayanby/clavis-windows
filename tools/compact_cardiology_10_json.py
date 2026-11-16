"""Apply authored compact notes to the local chapter; never install implicitly."""
import compact_cardiology_12_transferred as editor
from qbank_json_chapters import ROOT
from cardiology_10_compact_diagnosis import edits
from cardiology_10_compact_treatment import edits as treatment
from cardiology_10_compact_completion import edits as completion
assert not set(treatment)&set(completion)
treatment.update(completion)
assert not set(edits)&set(treatment)
edits.update(treatment)
editor.BANK=ROOT/'Cardiology/10. Infective Endocarditis.json'
editor.EDITS={'cardiology-rebuild-'+k:v for k,v in edits.items()}
def rebalance_uninstalled(q):
 # The transferred A answer made the draft A18/B16/C16/D16. Reorder one
 # unpublished question only; preserve the correct medical answer verbatim.
 if q['id']=='cardiology-rebuild-10-001' and q['correctIndex']==0:
  q['options'][0],q['options'][1]=q['options'][1],q['options'][0]
  q['correctIndex']=1
  for option in q['explanationTeaching']['otherOptions']:
   if option['optionIndex'] in (0,1):option['optionIndex']=1-option['optionIndex']
editor.EDIT_HOOK=rebalance_uninstalled
if __name__=='__main__':
 import json
 assert json.loads(editor.BANK.read_text(encoding='utf-8'))['status']!='installed_verified'
 editor.main()
