"""Apply explicit concise edits, retaining question IDs and key positions."""
import compact_cardiology_12_transferred as editor
from qbank_json_chapters import ROOT
from cardiology_15_compact_antiplatelets import edits
from cardiology_15_compact_coronary_valves import edits as coronary
from cardiology_15_compact_hf import edits as hf
from cardiology_15_compact_rhythm import edits as rhythm
from cardiology_15_compact_other import edits as other
for group in (coronary,hf,rhythm,other):
 assert not set(edits)&set(group)
 edits.update(group)
assert len(edits)==93,len(edits)
editor.BANK=ROOT/'Cardiology/15. Cardiovascular Pharmacology Antithrombotic Therapy and Landmark Trials.json'
editor.EDITS={'cardiology-rebuild-'+k:v for k,v in edits.items()}
if __name__=='__main__':editor.main()
