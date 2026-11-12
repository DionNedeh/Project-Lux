"""Offline release checks: every page, link, anchor, heading and source record."""
from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
BASE='/Project-Lux/'

def main():
    errors=[];links=0
    pages=sorted(ROOT.glob('*.html'))+sorted((ROOT/'library').glob('*.html'))
    parsed={p.resolve():BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser') for p in pages}
    ids={p:{n['id'] for n in soup.select('[id]')} for p,soup in parsed.items()}
    for path,soup in parsed.items():
        rel=path.relative_to(ROOT).as_posix()
        duplicates=[s for s,n in Counter(n['id'] for n in soup.select('[id]')).items() if n>1]
        if duplicates:errors.append(f'{rel}: duplicate IDs {duplicates}')
        headings=[int(n.name[1]) for n in soup.find_all(re.compile('^h[1-6]$'))]
        if headings.count(1)!=1:errors.append(f'{rel}: expected one h1')
        if any(b>a+1 for a,b in zip(headings,headings[1:])):errors.append(f'{rel}: skipped heading level')
        if not soup.find('html',lang=True) or not soup.find('main',id='main'):errors.append(f'{rel}: missing language or main landmark')
        for name in ['description','viewport']:
            if not soup.find('meta',attrs={'name':name}):errors.append(f'{rel}: missing {name}')
        for img in soup.find_all('img'):
            if not img.has_attr('alt'):errors.append(f'{rel}: image without alt')
        for node in soup.select('[href],[src]'):
            href=node.get('href',node.get('src',''));u=urlsplit(href)
            if u.scheme or u.netloc:
                if u.scheme not in ['https','http','mailto','data']:errors.append(f'{rel}: unsupported link scheme {href}')
                continue
            links+=1
            part=unquote(u.path)
            if part.startswith(BASE):target=ROOT/part[len(BASE):]
            elif part.startswith('/'):
                errors.append(f'{rel}: invalid root path {href}');continue
            elif part:target=path.parent/part
            else:target=path
            target=target.resolve()
            if not target.is_relative_to(ROOT):errors.append(f'{rel}: link leaves the publication root: {href}');continue
            if not target.is_file():errors.append(f'{rel}: missing local target {href}')
            elif u.fragment and target.suffix=='.html' and unquote(u.fragment) not in ids.get(target,set()):errors.append(f'{rel}: missing fragment {href}')
        body=str(soup.find('main'))
        if '[[' in body or re.search(r'\[!\w+\]',body):errors.append(f'{rel}: unresolved wiki markup')
        if re.search(r'(?:C:[\\/]|file:///|gh[pousr]_[A-Za-z0-9]{20})',body):errors.append(f'{rel}: private path or credential pattern')
        for node in soup.find_all(True):
            if any(str(key).lower().startswith('on') for key in node.attrs):errors.append(f'{rel}: inline event handler')
    manifest=json.loads((ROOT/'tools/library-manifest.json').read_text(encoding='utf-8'))
    for rel,record in manifest.items():
        path=ROOT/'research'/rel
        text=path.read_text(encoding='utf-8-sig').replace('\r\n','\n')
        if hashlib.sha256(text.encode()).hexdigest()!=record['text_sha256']:errors.append(f'{rel}: provenance digest mismatch')
        if not (ROOT/'library'/f'{path.stem}.html').is_file():errors.append(f'{rel}: no rendered note')
    expected=len(manifest)+8+1+4
    if len(pages)!=expected:errors.append(f'Expected {expected} HTML pages; found {len(pages)}')
    sitemap=ET.parse(ROOT/'sitemap.xml')
    locations=[n.text for n in sitemap.findall('.//{*}loc')]
    if len(locations)!=len(pages)-1:errors.append('Sitemap does not cover every indexable page')
    if not (ROOT/'assets/social-card.png').is_file():errors.append('Social preview image missing')
    report={'html_pages':len(pages),'local_links_and_assets':links,'source_notes':len(manifest),'errors':errors}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return bool(errors)

if __name__=='__main__':sys.exit(main())
