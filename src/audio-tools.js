import {createModel} from 'vosk-browser';
let context,source,recognizer,model,processor,filters,gain,modelPromise;
let enabled=false,callback=()=>{},activeKey='';
function graph(audio){if(context)return;context=new AudioContext({sampleRate:16000});source=context.createMediaElementSource(audio);filters=[100,350,1000,3500,10000].map(f=>{const filter=context.createBiquadFilter();filter.type='peaking';filter.frequency.value=f;filter.Q.value=1;return filter;});gain=context.createGain();let tail=source;for(const f of filters){tail.connect(f);tail=f;}tail.connect(gain);gain.connect(context.destination);}
export async function effects(audio,values,voiceGain){graph(audio);await context.resume();values.forEach((db,i)=>filters[i].gain.value=db);gain.gain.value=voiceGain;}
export async function transcribe(audio,key,onResult,onStatus){
  graph(audio);await context.resume();enabled=true;callback=onResult;
  if(!model){onStatus('Loading bundled English model… First use can take a minute.');modelPromise||=createModel(new URL('../assets/english-model.tar.gz',location.href).href,-1);try{model=await modelPromise;}catch(e){modelPromise=null;enabled=false;throw e;}}
  if(!enabled)return;
  if(recognizer&&activeKey!==key){recognizer.remove();recognizer=null;}
  if(!recognizer){activeKey=key;model.on('error',m=>onStatus('Recognition error: '+m.error));recognizer=new model.KaldiRecognizer(context.sampleRate);recognizer.setWords(true);recognizer.on('result',m=>{if(enabled&&m.result?.text)callback(m.result.text);});}
  if(!processor){processor=context.createScriptProcessor(4096,1,1);source.connect(processor);processor.connect(context.destination);processor.onaudioprocess=e=>{if(enabled&&recognizer&&!audio.paused&&!audio.seeking)recognizer.acceptWaveform(e.inputBuffer);};}
  onStatus('Offline English transcription · finalized passages appear while you listen.');
}
export function stopTranscription(){enabled=false;if(recognizer){recognizer.remove();recognizer=null;}activeKey='';}
export function finishTranscription(){if(enabled&&recognizer)recognizer.retrieveFinalResult();}
export function transcriptionActive(){return enabled;}
export async function scanRecognizer(onResult){
  if(!model){modelPromise||=createModel(new URL('../assets/english-model.tar.gz',location.href).href,-1);try{model=await modelPromise;}catch(e){modelPromise=null;throw e;}}
  const r=new model.KaldiRecognizer(16000);r.setWords(true);let pending=null;
  const finish=()=>{pending?.resolve();pending=null;};r.on('result',message=>{onResult(message.result);finish();});r.on('partialresult',finish);r.on('error',message=>{pending?.reject(Error(message.error||'Speech recognition failed.'));pending=null;});
  function wait(send){return new Promise((resolve,reject)=>{const timeout=setTimeout(()=>{if(pending){pending=null;reject(Error('Speech recognition timed out.'));}},120000);pending={resolve:()=>{clearTimeout(timeout);resolve();},reject:e=>{clearTimeout(timeout);reject(e);}};send();});}
  return {accept:bytes=>{const copy=new Uint8Array(bytes);return wait(()=>r.acceptWaveformFloat(new Float32Array(copy.buffer),16000));},finish:()=>wait(()=>r.retrieveFinalResult()),remove:()=>{pending?.reject(Error('Chapter scan cancelled.'));pending=null;r.remove();}};
}
