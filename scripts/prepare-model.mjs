import fs from 'node:fs/promises';
import path from 'node:path';
import JSZip from 'jszip';
import * as tar from 'tar';
const source=process.argv[2];
if(!source)throw Error('Usage: node scripts/prepare-model.mjs <Clavis english-model.zip>');
const output=path.resolve('assets/english-model.tar.gz');
const staging=path.resolve('test-output/model-staging');
await fs.mkdir(staging,{recursive:true});
const zip=await JSZip.loadAsync(await fs.readFile(source));
for(const item of Object.values(zip.files)){
  if(item.dir)continue;
  const parts=item.name.split('/').filter(Boolean);if(parts.length>1&&parts[0].startsWith('vosk'))parts.shift();
  const dest=path.resolve(staging,'model',...parts);if(!dest.startsWith(staging+path.sep))throw Error('Invalid model path');
  await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,await item.async('nodebuffer'));
}
await tar.c({gzip:true,file:output,cwd:staging},['model']);
console.log('Prepared bundled offline model:',output,(await fs.stat(output)).size);
