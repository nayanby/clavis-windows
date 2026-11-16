"""Install the tested adapter into the packaged app without changing its base renderer."""
import hashlib,json,time,zipfile
from pathlib import Path
from qbank_json_chapters import REPO, DATA

def install():
 root=(DATA.parent/'_internal/assets/vendor').resolve()
 target=root/'qbank-explanations.js'
 adapter=(REPO/'assets/vendor/qbank-concise.js').read_bytes()
 marker=b'\n/* CNL CONCISE QBANK ADAPTER */\n'
 assert target.resolve().parent==root and not target.is_symlink() and not root.is_junction()
 before=target.read_bytes();base=before.split(marker)[0]
 result=base+marker+adapter
 dest=root/'qbank-concise.js'
 backup=DATA/'qbank-reset-backups'/f'concise-renderer-{time.time_ns()}.zip'
 backup.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(backup,'x',zipfile.ZIP_DEFLATED) as z:
  z.writestr(target.name,before)
  if dest.exists():z.writestr(dest.name,dest.read_bytes())
 with zipfile.ZipFile(backup) as z:assert z.read(target.name)==before
 assert target.read_bytes()==before
 target.write_bytes(result);dest.write_bytes(adapter)
 assert target.read_bytes()==result and dest.read_bytes()==adapter
 report=dict(status='installed_verified',backup=str(backup),adapterSha256=hashlib.sha256(adapter).hexdigest(),baseRendererPreserved=target.read_bytes().split(marker)[0]==base,runtimeRenderer=str(target))
 (REPO/'Qbank Rebuild/Cardiology/audit/concise-renderer-install.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
 print(json.dumps(report,indent=2))

if __name__=='__main__':install()
