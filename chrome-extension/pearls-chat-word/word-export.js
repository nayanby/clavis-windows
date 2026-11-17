/* Build an OOXML Word document from the local, sanitized Clinical Notes template. */
(() => {
  const W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main';
  const R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships';
  const REL = 'http://schemas.openxmlformats.org/package/2006/relationships';
  const esc = text => String(text ?? '').replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\ufffe\uffff]/g, '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const textOf = runs => (runs || []).map(run => run.text).join('');
  function xml(text) {
    const doc = new DOMParser().parseFromString(text, 'application/xml');
    if (doc.querySelector('parsererror')) throw Error('The Word template contains invalid XML.');
    return doc;
  }
  const declaration = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>';
  const headingStyles = ['Heading1', 'Heading2', 'Heading3', 'Heading4', 'boldside2', 'Boldside3'];
  class Writer {
    constructor(zip, profile, onProgress) {
      this.zip = zip; this.profile = profile; this.relationships = []; this.abstracts = []; this.numbers = [];
      this.sequence = 100; this.imageIndex = 0; this.drawingIndex = 0; this.warnings = [];
      this.onProgress = onProgress;
    }
    relationship(type, target, external = false) {
      const id = 'rIdPearls' + (this.relationships.length + 1);
      this.relationships.push(`<Relationship Id="${id}" Type="${R}/${type}" Target="${esc(target)}"${external ? ' TargetMode="External"' : ''}/>`);
      return id;
    }
    runs(runs, { heading = false, table = false, header = false } = {}) {
      return (runs || []).map(run => {
        const properties = [];
        if (run.bold && !heading) properties.push('<w:rStyle w:val="SubtleEmphasis"/>');
        if (run.bold) properties.push('<w:b/>');
        if (header && !run.bold) properties.push('<w:b/>');
        if (header) properties.push('<w:color w:val="5C3A52"/>');
        if (run.italic) properties.push('<w:i/>');
        if (run.underline || run.href) properties.push('<w:u w:val="single"/>');
        if (run.strike) properties.push('<w:strike/>');
        if (run.code) properties.push('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>');
        if (run.highlight) properties.push('<w:shd w:val="clear" w:fill="FFF1BD"/>');
        if (run.sub) properties.push('<w:vertAlign w:val="subscript"/>');
        else if (run.sup) properties.push('<w:vertAlign w:val="superscript"/>');
        if (table) properties.push(`<w:sz w:val="${this.profile.bodyHalfPoints - 2}"/><w:szCs w:val="${this.profile.bodyHalfPoints - 2}"/>`);
        const pieces = String(run.text || '').split(/(\n|\t)/).map(piece => piece === '\n' ? '<w:br/>' : piece === '\t' ? '<w:tab/>' : `<w:t xml:space="preserve">${esc(piece)}</w:t>`).join('');
        const value = `<w:r>${properties.length ? '<w:rPr>' + properties.join('') + '</w:rPr>' : ''}${pieces}</w:r>`;
        if (run.href && /^(https?:|mailto:)/i.test(run.href)) return `<w:hyperlink r:id="${this.relationship('hyperlink', run.href, true)}">${value}</w:hyperlink>`;
        return value;
      }).join('');
    }
    paragraph(runs, options = {}) {
      const style = options.style || 'Normal';
      const props = [`<w:pStyle w:val="${style}"/>`];
      if (options.keepNext) props.push('<w:keepNext/>');
      // Headings receive NO numPr, including numId=0. Their styles have no list ancestry.
      if (options.number) props.push(`<w:numPr><w:ilvl w:val="${options.depth || 0}"/><w:numId w:val="${options.number}"/></w:numPr>`);
      if (options.table) props.push('<w:spacing w:before="0" w:after="30" w:line="250" w:lineRule="auto"/>');
      if (options.indent) props.push(`<w:ind w:left="${options.indent}"/>`);
      return `<w:p><w:pPr>${props.join('')}</w:pPr>${this.runs(runs, { heading: options.heading, table: options.table, header: options.header })}</w:p>`;
    }
    headingPlan(blocks) {
      const headings = blocks.filter(block => block.type === 'heading');
      const romanToken=heading=>/^\s*([IVXLCDM]+)[.)]\s+/i.exec(textOf(heading.runs))?.[1].toUpperCase();
      const romanDepth=Math.min(...headings.filter(heading=>!heading.inferred&&(romanToken(heading)?.length>1||/^[IVX]$/.test(romanToken(heading)||''))).map(heading=>heading.level));
      const plans = new Map();
      for (const heading of headings) {
        const text=textOf(heading.runs);
        let level=Math.max(2,Math.min(6,heading.level||2));
        if(heading.inferred)level=6;
        else if(romanToken(heading)&&heading.level===romanDepth)level=2;
        else if(/^\s*[A-Za-z][.)]\s+/.test(text))level=3;
        else if(/^\s*\d+[.)]\s+/.test(text))level=4;
        // The document title is the sole H1. Preserve every source prefix exactly.
        plans.set(heading,{style:headingStyles[level-1]});
      }
      return plans;
    }
    numbering(list, depth, start = list.start || 1) {
      const id = ++this.sequence;
      const format = list.ordered ? ({ '1': 'decimal', a: 'lowerLetter', A: 'upperLetter', i: 'lowerRoman', I: 'upperRoman' }[list.format] || 'decimal') : 'bullet';
      let levels = '';
      for (let i = 0; i < 9; i++) {
        const marker = list.ordered ? '%' + (i + 1) + '.' : ['•', '○', '▪'][Math.min(i, 2)];
        const left = 260 + i * 260;
        levels += `<w:lvl w:ilvl="${i}"><w:start w:val="${Math.max(1, Number(start) || 1)}"/><w:numFmt w:val="${format}"/><w:lvlText w:val="${esc(marker)}"/><w:lvlJc w:val="left"/><w:pPr><w:tabs><w:tab w:val="num" w:pos="${left}"/></w:tabs><w:ind w:left="${left}" w:hanging="220"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/></w:rPr></w:lvl>`;
      }
      this.abstracts.push(`<w:abstractNum w:abstractNumId="${id}"><w:multiLevelType w:val="multilevel"/>${levels}</w:abstractNum>`);
      this.numbers.push(`<w:num w:numId="${id}"><w:abstractNumId w:val="${id}"/><w:lvlOverride w:ilvl="${depth}"><w:startOverride w:val="${Math.max(1, Number(start) || 1)}"/></w:lvlOverride></w:num>`);
      return id;
    }
    blocks(blocks, options = {}) {
      const plans = options.table ? new Map() : this.headingPlan(blocks || []);
      return (blocks || []).map(block => {
        if (block.type === 'heading') {
          // Labels within cells are table text, never clinical outline headings.
          if(options.table)return this.paragraph(block.runs.map(run=>({...run,bold:true})),{...options,style:'Normal'});
          const plan = plans.get(block);
          return this.paragraph(plan.runs || block.runs, { style: plan.style, heading: true, keepNext: true, table: options.table });
        }
        if (block.type === 'paragraph') return this.paragraph(block.runs, options);
        if (block.type === 'code') return String(block.text).split('\n').map(line => this.paragraph([{ text: line || ' ', code: true }], { ...options, style: 'ChatCode' })).join('');
        if (block.type === 'quote') return this.blocks(block.blocks, { ...options, indent: 300 });
        if (block.type === 'rule') return this.paragraph([{ text: ' ' }], options);
        if (block.type === 'image') return this.image(block, options);
        if (block.type === 'table') return this.table(block, options);
        if (block.type === 'list') {
          const depth = Math.min(options.depth || 0, 8);
          let number = this.numbering(block, depth);
          let output = '';
          for (const item of block.items) {
            if (item.value !== null && Number.isFinite(item.value)) number = this.numbering(block, depth, item.value);
            let used = false;
            for (const child of item.blocks) {
              if (!used && child.type === 'paragraph') {
                output += this.paragraph(child.runs, { ...options, style: 'level' + (Math.min(depth, 2) + 1), number, depth }); used = true;
              } else {
                if (!used) { output += this.paragraph([], { ...options, number, depth }); used = true; }
                output += this.blocks([child], { ...options, depth: child.type === 'list' ? depth + 1 : depth, indent: child.type === 'paragraph' ? 260 + depth * 260 : options.indent });
              }
            }
            if (!used) output += this.paragraph([], { ...options, number, depth });
          }
          return output;
        }
        return '';
      }).join('');
    }
    table(table, options) {
      const matrix = [], starts = [];
      for (let rowIndex = 0; rowIndex < table.rows.length; rowIndex++) {
        matrix[rowIndex] ||= []; starts[rowIndex] ||= [];
        let column = 0;
        for (const cell of table.rows[rowIndex].cells) {
          while (matrix[rowIndex][column]) column++;
          const span = Math.max(1, Math.min(30, cell.colspan || 1));
          const rows = Math.max(1, Math.min(table.rows.length - rowIndex, cell.rowspan || 1));
          starts[rowIndex].push({ column, cell, span, rows, continuation: false });
          for (let r = rowIndex; r < rowIndex + rows; r++) {
            matrix[r] ||= []; starts[r] ||= [];
            for (let c = column; c < column + span; c++) matrix[r][c] = true;
            if (r > rowIndex) starts[r].push({ column, cell, span, rows, continuation: true });
          }
          column += span;
        }
      }
      const count = Math.max(1, ...matrix.map(row => row.length));
      const width = Math.floor(this.profile.contentWidthTwips / count);
      const grid = '<w:tblGrid>' + Array.from({ length: count }, () => `<w:gridCol w:w="${width}"/>`).join('') + '</w:tblGrid>';
      const borders = ['top', 'left', 'bottom', 'right', 'insideH', 'insideV'].map(side => `<w:${side} w:val="single" w:sz="4" w:color="D9D9D9"/>`).join('');
      let rows = '';
      for (let i = 0; i < starts.length; i++) {
        let cells = '', cursor = 0;
        const entries = starts[i].sort((a, b) => a.column - b.column);
        for (const entry of entries) {
          while (cursor < entry.column) { cells += '<w:tc><w:p/></w:tc>'; cursor++; }
          const header = entry.cell.header;
          const merge = entry.rows > 1 ? `<w:vMerge${entry.continuation ? '' : ' w:val="restart"'}/>` : '';
          const shade = header ? 'E7E1E4' : i % 2 ? 'F8F6F8' : 'FFFFFF';
          const content = entry.continuation ? '<w:p/>' : this.blocks(entry.cell.blocks, { ...options, table: true, header });
          cells += `<w:tc><w:tcPr><w:tcW w:w="${width * entry.span}" w:type="dxa"/>${entry.span > 1 ? '<w:gridSpan w:val="' + entry.span + '"/>' : ''}${merge}<w:shd w:fill="${shade}"/><w:tcMar><w:top w:w="65" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="65" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar><w:vAlign w:val="center"/></w:tcPr>${content || '<w:p/>'}${/<\/w:tbl>$/.test(content) ? '<w:p/>' : ''}</w:tc>`;
          cursor += entry.span;
        }
        while (cursor < count) { cells += '<w:tc><w:p/></w:tc>'; cursor++; }
        const header = table.rows[i]?.cells.length && table.rows[i].cells.every(cell => cell.header);
        rows += `<w:tr><w:trPr><w:cantSplit/>${header ? '<w:tblHeader/>' : ''}</w:trPr>${cells}</w:tr>`;
      }
      return `<w:tbl><w:tblPr><w:tblW w:w="${width * count}" w:type="dxa"/><w:tblBorders>${borders}</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>${grid}${rows}</w:tbl>${options.table?'<w:p/>':''}`;
    }
    image(image, options) {
      const match = /^data:image\/png;base64,([\s\S]+)$/.exec(image.data || image.src || '');
      if (!match) {
        this.warnings.push('An image is represented by its caption and source link.');
        return this.paragraph([{ text: image.alt || 'Image', italic: true }, ...(/^https?:/i.test(image.src || '') ? [{ text: ' — Source image', href: image.src }] : [])], options);
      }
      const name = 'image' + (++this.imageIndex) + '.png';
      this.zip.file('word/media/' + name, match[1], { base64: true });
      const id = this.relationship('image', 'media/' + name);
      const maxWidth = this.profile.contentWidthTwips * 635;
      // User's export size: 4 cm high (360,000 EMU per cm).
      const cy = 1440000;
      const cx = Math.round(Math.min(maxWidth, cy * Math.max(1, image.width || 640) / Math.max(1, image.height || 480)));
      const drawingId = ++this.drawingIndex;
      return `<w:p><w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="${cx}" cy="${cy}"/><wp:docPr id="${drawingId}" name="${name}" descr="${esc(image.alt)}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="${drawingId}" name="${name}"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="${id}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>`;
    }
    async finish(body, title) {
      const doc = xml(await this.zip.file('word/document.xml').async('string'));
      const section = new XMLSerializer().serializeToString(doc.getElementsByTagNameNS(W, 'sectPr')[0]);
      const document = `${declaration}<w:document xmlns:w="${W}" xmlns:r="${R}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><w:body>${body}${section}</w:body></w:document>`;
      const parsed = xml(document);
      // Keep OOXML property order valid even when several inline formats combine.
      const rOrder = 'rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow emboss imprint noProof snapToGrid vanish webHidden color spacing w kern position sz szCs highlight u effect bdr shd fitText vertAlign rtl cs em lang eastAsianLayout specVanish oMath rPrChange'.split(' ');
      for (const props of parsed.getElementsByTagNameNS(W, 'rPr')) {
        [...props.children].sort((a,b) => rOrder.indexOf(a.localName) - rOrder.indexOf(b.localName)).forEach(node => props.appendChild(node));
      }
      const normalized = new XMLSerializer().serializeToString(parsed);
      xml(normalized);
      this.zip.file('word/document.xml', normalized);
      this.zip.file('word/numbering.xml', `${declaration}<w:numbering xmlns:w="${W}">${this.abstracts.join('')}${this.numbers.join('')}</w:numbering>`);
      const relationships = xml(await this.zip.file('word/_rels/document.xml.rels').async('string'));
      const root = relationships.documentElement;
      for (const relationship of this.relationships) root.appendChild(relationships.importNode(xml(`<Relationships xmlns="${REL}">${relationship}</Relationships>`).documentElement.firstElementChild, true));
      this.zip.file('word/_rels/document.xml.rels', new XMLSerializer().serializeToString(relationships));
      const now = new Date().toISOString();
      this.zip.file('docProps/core.xml', `${declaration}<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>${esc(title)}</dc:title><dc:creator></dc:creator><cp:lastModifiedBy></cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">${now}</dcterms:created></cp:coreProperties>`);
      const bytes = await this.zip.generateAsync({ type: 'uint8array', compression: 'DEFLATE' },meta=>this.onProgress?.(meta.percent));
      return { bytes, warnings: [...new Set(this.warnings)] };
    }
  }
  function alphabet(index) { let value = index + 1, text = ''; while (value) { value--; text = String.fromCharCode(65 + value % 26) + text; value = Math.floor(value / 26); } return text; }
  async function create(chat, { title = chat.title || 'Conversation', includePrompts = true, single = false, templateBytes, profile, onProgress } = {}) {
    if (!globalThis.JSZip) throw Error('The local Word packaging library could not load.');
    const zip = await JSZip.loadAsync(templateBytes);
    const writer = new Writer(zip, profile, onProgress);
    let body = writer.paragraph([{ text: title }], { style: 'Heading1', heading: true, keepNext: true });
    const messages = chat.messages.filter(message => includePrompts || message.role === 'assistant');
    if (!messages.length) throw Error('No responses are available to export.');
    if (chat.url && /^https?:/.test(chat.url)) body += writer.paragraph([{ text: 'Source conversation', href: chat.url }], { style: 'ChatMetadata' });
    let assistantIndex = 0, userIndex = 0;
    for (const message of messages) {
      if (!single) body += writer.paragraph([{ text: message.role === 'assistant' ? 'Response ' + (++assistantIndex) : 'My message ' + (++userIndex) }], { style: 'ChatRole', keepNext: true });
      let blocks=message.blocks;
      if(single&&blocks[0]?.type==='heading'&&textOf(blocks[0].runs).trim().toLocaleLowerCase()===title.trim().toLocaleLowerCase())blocks=blocks.slice(1);
      body += writer.blocks(blocks);
    }
    return writer.finish(body, title);
  }
  globalThis.PearlsWord = { create, alphabet };
})();
