"""Deterministically build the Lux homepage, complete library, and Pages artifact.

The research snapshot is preserved as Markdown. Generated HTML resolves wikilinks,
keeps tables and callouts readable, and adds dates, provenance and navigation.
No network access occurs during a build. Run: python tools/build_site.py
"""
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
import hashlib
import html
import json
import posixpath
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from urllib.parse import quote, urlsplit

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = '/Project-Lux/'
ORIGIN = 'https://dionnedeh.github.io'
LAUNCH = '2026-11-11'
E = html.escape
TYPE_LABELS = {'synthesis':'Synthesis','source':'Source note','concept':'Concept','entity':'Entity','moc':'Topic guide'}
TYPE_FILTERS = {'synthesis':'synthesis','source':'source','concept':'concept','entity':'entity','moc':'moc'}
SPECIAL = {'index':'index.html','log':'../updates.html','CLAUDE':'../method.html','README':'../method.html#publication'}
MD = MarkdownIt('commonmark', {'html':False}).enable(['table','strikethrough'])

def write(rel, text):
    path = ROOT/rel
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8',newline='\n')

def asset(rel):
    # Git normalises text assets to LF. Hash the same text on Windows and Linux.
    content = (ROOT/rel).read_text(encoding='utf-8').encode('utf-8')
    return rel+'?v='+hashlib.sha256(content).hexdigest()[:12]

def human(iso):
    d=date.fromisoformat(str(iso)[:10])
    return f'{d.day} {d.strftime("%B")} {d.year}'

def plain(text):
    return ' '.join(BeautifulSoup(MD.render(text),'html.parser').get_text(' ',strip=True).split())

def short(text, limit=165):
    text=' '.join(text.split())
    return text if len(text)<=limit else text[:limit].rsplit(' ',1)[0].rstrip(' ,;:')+'…'

def header(prefix='', library=False):
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap nav-wrap"><a class="brand" href="{prefix}index.html"><img src="{prefix}assets/mark.svg" width="34" height="34" alt=""><span>LUX <small>by Voelori</small></span></a><nav aria-label="Main navigation"><a href="{prefix}index.html#purpose">The purpose</a><a href="{prefix}index.html#explore">AI &amp; fusion</a><a href="{prefix}library/index.html"{' aria-current="page"' if library else ''}>Research library</a><a href="{prefix}method.html">Our approach</a></nav></div></header>'''

def footer(prefix=''):
    return f'''<footer class="site-footer"><div class="wrap footer-inner"><a class="brand" href="{prefix}index.html">LUX <small>by Voelori</small></a><p>AI, fusion, and the possibilities ahead.</p><nav aria-label="Footer"><a href="{prefix}method.html">Evidence &amp; method</a><a href="{prefix}updates.html">Updates</a><a href="https://github.com/DionNedeh/Project-Lux">GitHub ↗</a></nav><span class="draft-label">A Voelori research resource</span></div></footer>'''

def page(title, description, path, body, prefix='', scripts=(), noindex=False, full_title=None):
    canonical=ORIGIN+BASE+path
    # Pages read "<title> — Project Lux"; the homepage leads with the project name instead.
    full_title=full_title or f'{title} — Project Lux'
    script_html=''.join(f'<script src="{prefix}{asset(s)}" defer></script>' for s in scripts)
    robots='<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#f7f2e9"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'"><title>{E(full_title)}</title><meta name="description" content="{E(short(description))}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{E(full_title)}"><meta property="og:description" content="{E(short(description))}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{ORIGIN+BASE}assets/social-card.png"><meta name="twitter:card" content="summary_large_image">{robots}<link rel="icon" href="{prefix}assets/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}{asset('styles.css')}">{script_html}</head><body>{header(prefix,path=='library/index.html')}<main id="main">{body}</main>{footer(prefix)}</body></html>'''

def load_docs():
    manifest=json.loads((ROOT/'tools/library-manifest.json').read_text(encoding='utf-8'))
    docs={}
    for path in sorted((ROOT/'research').rglob('*.md')):
        rel=path.relative_to(ROOT/'research').as_posix()
        raw=path.read_text(encoding='utf-8-sig').replace('\r\n','\n')
        if not raw.startswith('---\n'):
            raise ValueError(f'{rel}: missing frontmatter')
        front, body=raw[4:].split('\n---',1)
        meta=yaml.safe_load(front)
        for field in ['title','type','created','updated','status','confidence']:
            if field not in meta:raise ValueError(f'{rel}: missing {field}')
        entry=manifest[rel]
        if hashlib.sha256(raw.encode()).hexdigest()!=entry['text_sha256']:
            raise ValueError(f'{rel}: source changed; update the publication manifest through import_wiki.py')
        if path.stem in docs:raise ValueError(f'Duplicate basename {path.stem}')
        docs[path.stem]={'slug':path.stem,'rel':rel,'meta':meta,'body':body.strip(),'manifest':entry,'path':f'library/{path.stem}.html'}
    return docs

def wiki_links(text, docs, outbound=None):
    """Convert links outside code spans/fences, including escaped table aliases."""
    def link(match):
        inner=match.group(1).replace('\\|','|')
        target, _, label=inner.partition('|')
        target=target.strip()
        if target in docs:
            href=target+'.html'
            label=label or str(docs[target]['meta']['title'])
            if outbound is not None:outbound.add(target)
        elif target in SPECIAL:
            href=SPECIAL[target]
            label=label or {'index':'Research library','log':'Project updates','CLAUDE':'Evidence & method','README':'About the research library'}[target]
        else:raise ValueError(f'Unresolved wikilink: {target}')
        label=label.replace('[','\\[').replace(']','\\]')
        return f'[{label}]({href})'
    # A wikilink is one token even when its display text contains inline code or
    # a wrapped source line. Fenced code and standalone inline code stay literal.
    pattern=re.compile(r'```[\s\S]*?```|\[\[([^\]]+)\]\]|`[^`\n]*`')
    return pattern.sub(lambda match:link(match) if match.group(1) is not None else match.group(0),text)

def slugify(text):
    value=re.sub(r'[^\w\- ]','',text.lower().strip()).replace(' ','-')
    return value or 'section'

def render_doc(doc, docs):
    outbound=set()
    body=wiki_links(doc['body'],docs,outbound)
    tokens=MD.parse(body)
    # The document title is shown once in the page header, retaining the numbered
    # document identifier in the eyebrow. No substantive paragraphs are removed.
    if len(tokens)>2 and tokens[0].type=='heading_open' and tokens[0].tag=='h1':tokens=tokens[3:]
    counts=Counter(); headings=[]; previous=1
    for i, token in enumerate(tokens):
        if token.type=='heading_open':
            level=max(2,int(token.tag[1]))
            level=min(level,previous+1)
            token.tag=f'h{level}';tokens[i+2].tag=token.tag;previous=level
            text=''.join(' ' if c.type in ('softbreak','hardbreak') else c.content for c in tokens[i+1].children or [] if c.type in ('text','code_inline','softbreak','hardbreak'))
            base=slugify(text);n=counts[base];counts[base]+=1;ident=base+(f'-{n}' if n else '')
            token.attrSet('id',ident)
            if level==2:headings.append((ident,text))
    rendered=MD.renderer.render(tokens,MD.options,{})
    soup=BeautifulSoup(rendered,'html.parser')
    for i, table in enumerate(soup.find_all('table'),1):
        wrapper=soup.new_tag('div',attrs={'class':'table-wrap','role':'region','tabindex':'0','aria-label':f'Table {i} — scroll horizontally if needed'})
        table.wrap(wrapper)
        for th in table.select('thead th'):th['scope']='col'
    for quote_tag in soup.find_all('blockquote'):
        first=quote_tag.find('p')
        if first and first.contents and isinstance(first.contents[0],str):
            marker=re.match(r'^\[!(\w+)\]\s*',str(first.contents[0]))
            if marker:
                quote_tag.name='aside';quote_tag['class']=['callout',f'callout-{marker.group(1).lower()}']
                first.contents[0].replace_with(str(first.contents[0])[marker.end():])
                label=soup.new_tag('p',attrs={'class':'callout-label'})
                label.string=marker.group(1).capitalize();quote_tag.insert(0,label)
    for heading in soup.find_all(re.compile('^h[2-6]$')):
        a=soup.new_tag('a',href='#'+heading['id'],attrs={'class':'heading-link','aria-hidden':'true','tabindex':'-1','title':'Link to this section'})
        a.string='#';heading.append(a)
    text=soup.get_text(' ',strip=True)
    doc.update(html=str(soup),outbound=outbound,headings=headings,text=text,summary=short(next((p.get_text(' ',strip=True) for p in soup.find_all('p') if len(p.get_text())>65 and not p.find_parent('aside')),text)))

def topic_names(doc):
    ignored={'source','entity','synthesis','concept','moc','reference','overview','current'}
    return sorted({str(t).split('/')[-1] for t in doc['meta'].get('tags',[]) if str(t).split('/')[-1] not in ignored})

def featured_refs(docs):
    refs=json.loads((ROOT/'tools/featured-references.json').read_text(encoding='utf-8'))
    for ref in refs:
        ref['slug']=Path(ref['note']).stem
        if ref['slug'] not in docs:raise ValueError(f'Featured reference missing: {ref["id"]}')
        ref['access']=ref['access'].replace('For this draft','For the initial page release').replace('for this draft','for the initial page release').replace('This draft','The initial page release').replace('this draft','the initial page release').replace('draft briefs','featured briefs').replace('Draft','Release')
        ref['limits']=ref['limits'].replace('for this draft','for the initial page release')
    return refs

def citation_map(refs):
    return {r['slug']:r['cites'] for r in refs}

def date_meta(doc, backlinks=''):
    m=doc['meta'];entry=doc['manifest']
    rows=[('Document type',TYPE_LABELS[m['type']]),('Research note updated',f'<time datetime="{m["updated"]}">{human(m["updated"])}</time>'),('First written',human(m['created'])),('Added to this site',human(entry['added'])),('Library assessment',f'{E(str(m["confidence"]).capitalize())} confidence · {E(str(m["status"]))}')]
    if m.get('source_date'):rows.append(('Source date',E(str(m['source_date']))))
    if backlinks:rows.append(('Cited on the homepage',backlinks))
    return '<dl class="doc-meta">'+''.join(f'<div><dt>{label}</dt><dd>{value}</dd></div>' for label,value in rows)+'</dl>'

def build_documents(docs, refs):
    cited=citation_map(refs)
    incoming=defaultdict(set)
    for slug,doc in docs.items():
        for target in doc['outbound']:incoming[target].add(slug)
        for val in doc['meta'].get('related',[])+doc['meta'].get('sources',[]):
            for target in re.findall(r'\[\[([^]|]+)',str(val)):
                if target in docs:incoming[target].add(slug)
    for slug,doc in docs.items():
        m=doc['meta'];title=str(m['title'])
        label=TYPE_LABELS[m['type']]
        if 'doc' in m:label+=f' · Document {int(m["doc"]):02d}'
        cite=' · '.join(f'<a href="../index.html#{anchor}">{E(name)}</a>' for anchor,name in cited.get(slug,[]))
        toc='<details class="doc-toc" open><summary>On this page</summary><ol>'+''.join(f'<li><a href="#{ident}">{E(text)}</a></li>' for ident,text in doc['headings'])+'</ol></details>' if len(doc['headings'])>=2 else ''
        tags=''.join(f'<a href="index.html?topic={quote(t)}">{E(t.replace("-"," "))}</a>' for t in topic_names(doc))
        provenance=f'<a href="../research/{doc["rel"]}" download>Download this research note (.md)</a>'
        source_meta=''
        if m.get('authors') or m.get('publisher'):
            source_meta='<p>'+E(str(m.get('authors','')))+' · '+E(str(m.get('publisher','')))+'</p>'
        if m.get('file'):
            source_meta+='<p class="provenance">The source note records a local capture. Captured third-party files are not redistributed here. Publisher and DOI links appear in the note or bibliography.</p>'
        related=set()
        for val in m.get('related',[])+m.get('sources',[]):
            for target in re.findall(r'\[\[([^]|]+)',str(val)):
                if target in docs and target!=slug:related.add(target)
        related_html='<section class="related-reading"><h2>Continue exploring</h2><ul>'+''.join(f'<li><a href="{s}.html">{E(str(docs[s]["meta"]["title"]))}</a> <small>{TYPE_LABELS[docs[s]["meta"]["type"]]}</small></li>' for s in sorted(related))+'</ul></section>' if related else ''
        incoming_html='<details class="backlinks"><summary>Linked from '+str(len(incoming[slug]))+' library notes</summary><ul>'+''.join(f'<li><a href="{s}.html">{E(str(docs[s]["meta"]["title"]))}</a></li>' for s in sorted(incoming[slug]))+'</ul></details>'
        eyebrow=f'<p class="eyebrow">{E(label)}</p>'
        body=f'''<section class="doc-head"><div class="wrap reading"><p class="breadcrumbs"><a href="../index.html">Project Lux</a> / <a href="index.html">Research library</a> / {E(TYPE_LABELS[m['type']])}</p>{eyebrow}<h1 id="doc-title">{E(title)}</h1>{date_meta(doc,cite)}<p class="snapshot-note">A dated research record. Statements about schedules, policy, or company progress reflect the note’s date. <a href="../method.html#reading-the-evidence">How to read the evidence</a></p><div class="topic-links" role="navigation" aria-label="Topics">{tags}</div>{toc}</div></section><article class="wrap reading doc-body" aria-labelledby="doc-title"><div class="prose">{doc['html']}</div><section class="source-box provenance-box"><h2>About this research note</h2>{source_meta}<p>{provenance}</p><p class="provenance">Published from <code>research/{E(doc['rel'])}</code>. Source text is preserved; this page adds navigation, accessible tables, and resolved links. Library confidence is an editorial assessment, not independent certification. <a href="../method.html#publication">Publication method</a>.</p></section>{related_html}{incoming_html}<nav class="doc-nav" aria-label="Continue reading"><a href="index.html">← Research library</a><a href="#doc-title">Back to the top ↑</a></nav></article>'''
        write(doc['path'],page(title,doc['summary'],doc['path'],body,'../'))

def featured_row(r):
    return f'<a class="library-row" href="library/{r["id"]}.html" data-category="{r["category"]}" data-keywords="{E(r["keywords"])}"><span class="ref">{r["id"]}</span><div><h3>{E(r["title"])}</h3><p>{E(r["subtitle"])}</p></div><div class="row-meta"><span class="badge">{E(r["label"])}</span><small>Research / {r["date"]}</small></div><span class="row-arrow" aria-hidden="true">↗</span></a>'

def build_briefs(docs,refs):
    for r in refs:
        doc=docs[r['slug']]
        cite=' · '.join(f'<a href="../index.html#{anchor}">{E(name)}</a>' for anchor,name in r['cites'])
        direct=f'<p><a href="{E(r["url"])}">Open the primary source ↗</a></p>' if r['url'] else ''
        content=f'''<section class="doc-head"><div class="wrap reading"><p class="breadcrumbs"><a href="../index.html">Project Lux</a> / <a href="index.html">Research library</a> / {r['id']}</p><span class="badge">{E(r['label'])}</span><h1 id="doc-title">{E(r['title'])}</h1><p class="doc-deck">{E(r['subtitle'])}</p>{date_meta(doc,cite)}</div></section><article class="wrap reading doc-body" aria-labelledby="doc-title"><section id="finding"><h2>What this reference supports</h2><p>{E(r['claim'])}</p></section><section id="limits"><h2>Where the evidence stops</h2><p>{E(r['limits'])}</p></section><section id="source" class="source-box"><h2>Source &amp; provenance</h2><p>{E(r['source'])}</p>{direct}<p><a href="{r['slug']}.html">Read the full research note →</a></p><p><a href="../research/{doc['rel']}" download>Download the original note (.md)</a></p></section><section id="verification"><h2>How this brief was checked</h2><p>{E(r['access'])}</p><p class="provenance">This brief is a reading aid for a dated research record. Its publication date does not imply a fresh scientific validation. <a href="../method.html">Read the evidence and publication method</a>.</p></section><nav class="doc-nav" aria-label="Continue reading"><a href="index.html">← Complete research library</a><a href="../index.html#library">Return to the featured research ↗</a></nav></article>'''
        write(f'library/{r["id"]}.html',page(r['title'],r['subtitle'],f'library/{r["id"]}.html',content,'../'))

def catalogue_row(doc):
    m=doc['meta'];topics=topic_names(doc)
    return f'''<a class="catalogue-row" href="{doc['slug']}.html" data-slug="{doc['slug']}" data-type="{m['type']}" data-topics="{' '.join(topics)}" data-updated="{m['updated']}"><div><span class="catalogue-kind">{TYPE_LABELS[m['type']]}</span><h3>{E(str(m['title']))}</h3><p>{E(doc['summary'])}</p></div><div class="catalogue-meta"><span>{human(m['updated'])}</span><span aria-hidden="true">↗</span></div></a>'''

def build_catalogue(docs):
    counts=Counter(d['meta']['type'] for d in docs.values())
    types=[('all',f'All notes ({len(docs)})')]+[(t,f'{TYPE_LABELS[t]} ({counts[t]})') for t in ['synthesis','source','concept','entity','moc']]
    buttons=''.join(f'<button type="button" data-kind="{t}" aria-pressed="{str(t=="all").lower()}" class="{"active" if t=="all" else ""}">{label}</button>' for t,label in types)
    topics=sorted({t for d in docs.values() for t in topic_names(d)})
    opts=''.join(f'<option value="{t}">{E(t.replace("-"," ").capitalize())}</option>' for t in topics)
    ordered=sorted(docs.values(),key=lambda d:(str(d['meta']['title']).casefold(),d['slug']))
    body=f'''<section class="doc-head"><div class="wrap"><p class="eyebrow">The Project Lux research library</p><h1>Go deeper.<br><em>Keep the source in sight.</em></h1><p class="doc-deck catalogue-deck">{len(docs)} interconnected notes on fusion science, engineering, institutions, and AI. Follow a reading path or search the complete text.</p><div class="library-summary"><span><b>{counts['synthesis']}</b> syntheses</span><span><b>{counts['source']}</b> source notes</span><span><b>{counts['concept']}</b> concepts</span><span><b>{counts['entity']}</b> entities</span><span><b>{counts['moc']}</b> topic guides</span></div><p class="section-note">Research notes are individually dated. Site publication: {human(LAUNCH)}. <a href="../method.html">Evidence labels &amp; limitations</a></p></div></section><section class="wrap catalogue-section" aria-labelledby="browse-title"><div class="reading-paths"><a href="40-ai-for-fusion-transferable-control.html"><span>Start with AI</span><strong>From data to control ↗</strong></a><a href="01-fusion-physics-fundamentals.html"><span>Start with the science</span><strong>Fusion fundamentals ↗</strong></a><a href="09-engineering-challenges.html"><span>Start with the systems</span><strong>Beyond the plasma ↗</strong></a><a href="15-references.html"><span>Start with the sources</span><strong>References &amp; bibliography ↗</strong></a></div><h2 id="browse-title">Find your next question.</h2><div class="catalogue-controls" hidden><label class="catalogue-search" for="catalogue-search">Search titles, topics, and full text<input id="catalogue-search" type="search" placeholder="Try tritium, plasma control, or materials…" autocomplete="off"></label><div class="filters catalogue-filters" role="group" aria-label="Filter by document type">{buttons}</div><div class="catalogue-selects"><label>Topic<select id="topic-filter"><option value="all">All topics</option>{opts}</select></label><label>Order<select id="sort-order"><option value="title">Title A–Z</option><option value="updated">Most recently revised</option></select></label><button type="button" class="clear-filters">Reset filters</button></div></div><p class="catalogue-count" id="catalogue-count" role="status">{len(docs)} research notes</p><noscript><p>All notes are listed below. Your browser’s Find command can search titles; the topic guides provide another way to explore.</p></noscript><div class="catalogue-list">{''.join(catalogue_row(d) for d in ordered)}</div><div class="catalogue-empty" hidden><h3>No matching notes.</h3><p>Try a broader phrase, another topic, or reset the filters.</p><button type="button" class="clear-filters">Show the whole library</button></div><div class="library-bottom"><p>Looking for the short citations used on the homepage?</p><a href="../index.html#library">Browse the eight featured references ↗</a></div></section>'''
    data={slug: {'text':doc['text'],'title':str(doc['meta']['title'])} for slug,doc in docs.items()}
    write('assets/library-data.js','window.LUX_LIBRARY = '+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/')+';\n')
    write('library/index.html',page('Research library',f'{len(docs)} dated and interconnected fusion research notes. Search by topic, type, or full text.','library/index.html',body,'../',scripts=('assets/library-data.js','library.js')))

def build_home(docs,refs):
    raw=(ROOT/'templates/home.html').read_text(encoding='utf-8')
    # Preserve the original SVG as the accessible, static fallback for the moving grid.
    field=ET.fromstring((ROOT/'assets/field.svg').read_text(encoding='utf-8'))
    ns='{http://www.w3.org/2000/svg}'
    ET.register_namespace('',ns[1:-1])
    field.attrib.update({'class':'plasma-art','role':'img','aria-labelledby':'field-title','width':'600','height':'540'})
    title=ET.Element(ns+'title',{'id':'field-title'})
    title.text='An abstract toroidal field drawn in fine amber and copper lines, surrounding a luminous center.'
    field.insert(0,title)
    body=ET.Element(ns+'g',{'class':'field-body'})
    curves=field.findall(ns+'polyline')
    insert_at=list(field).index(curves[0])
    for curve in curves:
        field.remove(curve)
        body.append(curve)
    field.insert(insert_at,body)
    # Reference marks (dots, leaders, numbers) sit in their own layer above the moving grid canvas.
    marks=ET.Element(ns+'svg',{'class':'field-marks','viewBox':field.get('viewBox'),'aria-hidden':'true','focusable':'false'})
    children=list(field)
    for mark in children[children.index(body)+1:]:
        field.remove(mark)
        marks.append(mark)
    raw=raw.replace('<!-- MOVING_FIELD -->',ET.tostring(field,encoding='unicode')+ET.tostring(marks,encoding='unicode'))
    raw=re.sub(r'<!-- LIBRARY_ROWS_START -->.*?<!-- LIBRARY_ROWS_END -->','\n'.join(featured_row(r) for r in refs),raw,flags=re.S)
    raw=raw.replace('Design draft · 11 November 2026','A Voelori research resource').replace('CURATED DRAFT SELECTION','FEATURED RESEARCH')
    raw=raw.replace('The draft reflects those records, not a comprehensive November research update.','These summaries reflect those records; publication is not a new scientific validation.')
    raw=raw.replace('This is a selected reading shelf from the wider Lux wiki.',f'Explore all {len(docs)} notes in the complete research library.')
    raw=raw.replace('Open the library &amp; citation guide','Open the complete research library')
    raw=raw.replace('Every entry links to a dated library brief and the repository note behind it.','Every entry links to a dated library brief and the full research note behind it.')
    raw=raw.replace('From a signal<br>to a better experiment.','From a signal<br>to a better experiment.')
    soup=BeautifulSoup(raw,'html.parser')
    main=soup.find('main')
    # The approved visual direction is retained; shared site metadata/navigation is generated.
    body=''.join(str(child) for child in main.contents)
    body=body.replace('<p>Start with a guide, open a study, or inspect its limitations.',f'<p>Start with a guide, open a study, or inspect its limitations.')
    write('index.html',page('Intelligence for a brighter energy future','Project Lux explores how AI can help advance fusion energy. Explore the experiments, engineering, and evidence.','index.html',body,scripts=('site.js',),full_title='Project Lux — Intelligence for a brighter energy future'))

def info_page(title,deck,content,path):
    body=f'<section class="doc-head"><div class="wrap reading"><p class="eyebrow">Project Lux / A Voelori initiative</p><h1>{title}</h1><p class="doc-deck">{deck}</p></div></section><article class="wrap reading doc-body prose">{content}</article>'
    write(path,page(plain(title),plain(deck),path,body))

def build_information(docs):
    content=f'''<section id="purpose"><h2>Our purpose</h2><p>Project Lux explores how AI can contribute to more effective energy systems, beginning with fusion. We connect experimental results to the engineering questions around them. The public resource is a research library and a place to learn.</p><p>Lux does not claim an operating fusion plant, a validated plant controller, or measured energy savings. Its companion project <a href="https://dionnedeh.github.io/Project-Spira/">Spira</a> examines AI’s electricity and water demands. <a href="https://dionnedeh.github.io/Project-Valens/">Valens</a> is another Voelori resource, with its own subject and evidence library.</p></section><section id="reading-the-evidence"><h2>Read the result at its actual scale</h2><div class="guide-key"><div><h3>Experimental control</h3><p>A method tested on a physical research device for a specific task, duration, and operating envelope.</p></div><div><h3>Offline evaluation</h3><p>A representation, prediction, or forecast tested on data. This alone is not live machine control.</p></div><div><h3>Simulation or design</h3><p>A result depends on modeled assumptions and inputs. A proposed plant’s performance is not a measured operating result.</p></div><div><h3>Reported or announced</h3><p>A claim attributed to an organisation, survey, or announcement. Keep the claim’s source and date attached.</p></div></div><p>Peer review and demonstration type are different questions. A peer-reviewed simulation remains a simulation; a source note is not an independent replication.</p><p>Library confidence and status come from the original note’s editorial metadata. “High confidence” or “stable” does not certify that every statement is correct or current. Source limitations, conflicts, and dates take priority.</p></section><section id="citations"><h2>How the citations connect</h2><p>Homepage citations [L01]–[L08] open short briefs with bounded findings and links to the full library notes. Each note includes its revision date, original Markdown, related research, and incoming links. Study briefs also link to the primary paper.</p><p>The <a href="library/15-references.html">bibliography</a> collects the wider source trail. A failed retrieval is an access limitation, not evidence that a study or result does not exist. Metadata-only captures are labelled in the source notes, including <a href="library/L03.html">L03</a> and <a href="library/L04.html">L04</a>.</p></section><section id="publication"><h2>A dated library, made readable</h2><p>This release publishes {len(docs)} research notes from the existing Lux wiki. It adds navigation, resolved internal links, accessible table containers, and text search. The original Markdown accompanies each note; the public build does not replace research with screenshots or images of text.</p><p>Notes are written and maintained with AI assistance and human curation. They include synthesis and interpretation as well as reported findings. Publication is not a comprehensive new fact-check of the corpus. Research dates remain separate from the date the site was published.</p><p>Downloaded third-party papers, internal research logs, and personal workspace files are not distributed by this site. The source notes identify captures held locally and link to primary publishers or open archives where available. No new redistribution licence is asserted over third-party material.</p><p>The complete site is static. Search runs in your browser; there are no accounts, submitted search queries, tracking analytics, or contact forms. Visiting an external source follows that provider’s own practices.</p></section><section id="energy-boundaries"><h2>Keep the energy accounting clear</h2><p>Fusion output, plasma heating, total electrical input, and net electricity exported describe different system boundaries. Improving an experiment’s prediction or control metric does not itself prove a lower whole-system energy cost. Read <a href="library/L07.html">the energy-balance guide</a> and <a href="library/q-gain-definitions.html">the gain definitions note</a>.</p><p>Diagrams on the homepage are conceptual illustrations. They are not plasma simulations, facility measurements, or control interfaces.</p></section><section id="corrections"><h2>Corrections and continuing work</h2><p>Use the <a href="https://github.com/DionNedeh/Project-Lux/issues">Project Lux issue tracker</a> to report an error, with the page URL, exact claim, and a primary source where possible. Responses are not guaranteed on a particular schedule. Corrections should preserve the source trail and be recorded in <a href="updates.html">project updates</a>.</p></section>'''
    info_page('Curiosity, with a source.','How we present evidence, preserve context, and distinguish possibility from demonstration.',content,'method.html')
    update=f'''<section id="launch"><p class="eyebrow">{human(LAUNCH)}</p><h2>The first public library</h2><p>Project Lux’s first site release brings together {len(docs)} dated research notes, eight featured reference briefs, and an introduction to AI’s role in fusion research.</p><p>The site follows the shared Voelori style while using a distinct light-and-fusion visual identity. This is a publication of existing research records, not a claim that every source was independently revalidated at launch.</p><p><a href="library/index.html">Explore the library</a> · <a href="method.html">Read the publication method</a> · <a href="https://github.com/DionNedeh/Project-Lux/commits/main/">View the source history</a></p></section>'''
    info_page('A record of the work.','Publication milestones and changes to the Project Lux site.',update,'updates.html')
    missing=f'<section class="section wrap reading"><p class="eyebrow">404 / Page not found</p><h1>This page is not here.</h1><p>The address may have changed, or the link may be incomplete.</p><div class="actions"><a class="button" href="{BASE}index.html">Go to Project Lux</a><a href="{BASE}library/index.html">Search the research library →</a></div></section>'
    write('404.html',page('Page not found','Find your way back to Project Lux.','404.html',missing,BASE,noindex=True))

def build_sitemap(docs,refs):
    pages=[('index.html',LAUNCH),('method.html',LAUNCH),('updates.html',LAUNCH),('library/index.html',LAUNCH)]+[(d['path'],max(LAUNCH,str(d['meta']['updated']))) for d in docs.values()]+[(f'library/{r["id"]}.html',LAUNCH) for r in refs]
    write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{ORIGIN+BASE+path}</loc><lastmod>{stamp}</lastmod></url>\n' for path,stamp in pages)+'</urlset>\n')
    write('robots.txt',f'User-agent: *\nAllow: /\nSitemap: {ORIGIN+BASE}sitemap.xml\n')
    write('.nojekyll','')

def stage():
    target=(ROOT/'_site').resolve()
    if target.parent != ROOT.resolve():raise ValueError('Unexpected output directory')
    if target.exists():shutil.rmtree(target)
    target.mkdir()
    for folder in ['assets','library','research']:
        shutil.copytree(ROOT/folder,target/folder)
    for rel in ['index.html','method.html','updates.html','404.html','styles.css','site.js','library.js','sitemap.xml','robots.txt','.nojekyll']:
        shutil.copyfile(ROOT/rel,target/rel)

def main():
    docs=load_docs()
    for doc in docs.values():render_doc(doc,docs)
    refs=featured_refs(docs)
    build_documents(docs,refs)
    build_briefs(docs,refs)
    build_catalogue(docs)
    build_home(docs,refs)
    build_information(docs)
    build_sitemap(docs,refs)
    import check_site
    if check_site.main():return 1
    stage()
    print(f'Built {len(docs)} complete research pages, {len(refs)} citation briefs, catalogue, and site pages.')
    return 0

if __name__=='__main__':sys.exit(main())
