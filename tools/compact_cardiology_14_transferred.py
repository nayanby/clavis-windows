"""Apply explicit concise edits to all retained Chapter 14 questions with hash audit."""
import compact_cardiology_12_transferred as editor
from cardiology_14_compact_conduction import edits as conduction
from cardiology_14_compact_rhythms import edits as rhythms
editor.BANK=editor.BANK.with_name('14. Advanced ECG Interpretation and Electrophysiology.json')
editor.EDITS={'cardiology-rebuild-'+k:v for k,v in {**conduction,**rhythms}.items()}
assert len(editor.EDITS)==45
if __name__=='__main__':editor.main()
