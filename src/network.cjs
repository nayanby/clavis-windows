const dns=require('node:dns/promises');
const net=require('node:net');
function privateAddress(ip) {
  if(net.isIPv4(ip)) {const p=ip.split('.').map(Number);return p[0]===0||p[0]===10||p[0]===127||p[0]>=224||(p[0]===169&&p[1]===254)||(p[0]===172&&p[1]>=16&&p[1]<=31)||(p[0]===192&&p[1]===168)||(p[0]===100&&p[1]>=64&&p[1]<=127);}
  return ip==='::'||ip==='::1'||/^(fc|fd|fe[89ab])/i.test(ip)||/^::ffff:/i.test(ip);
}
async function publicURL(value) {
  const u=new URL(value);
  if(u.protocol!=='https:'||u.username||u.password)throw Error('Enter a public HTTPS address.');
  const host=u.hostname.replace(/^\[|\]$/g,'');
  const addresses=net.isIP(host)?[{address:host}]:await dns.lookup(host,{all:true});
  if(!addresses.length||addresses.some(a=>privateAddress(a.address)))throw Error('Local network addresses are not supported.');
  return u;
}
async function request(value, limit=12*1024*1024) {
  let u=await publicURL(value);
  for(let redirects=0;redirects<6;redirects++) {
    const r=await fetch(u,{redirect:'manual',cache:'no-store',signal:AbortSignal.timeout(25000),headers:{'User-Agent':'Clavis-Windows/0.1 RSS Reader','Accept':'application/rss+xml, application/atom+xml, text/html, */*','Cache-Control':'no-cache','Pragma':'no-cache'}});
    if([301,302,303,307,308].includes(r.status)){await r.body?.cancel();u=await publicURL(new URL(r.headers.get('location'),u));continue;}
    if(!r.ok){await r.body?.cancel();throw Error(`The server returned HTTP ${r.status}.`);}
    let size=0;const chunks=[];
    for await(const chunk of r.body){size+=chunk.length;if(size>limit)throw Error('The response is too large.');chunks.push(chunk);}
    return {text:Buffer.concat(chunks).toString('utf8'),url:u.href};
  }
  throw Error('Too many redirects.');
}
module.exports={privateAddress,publicURL,request};
