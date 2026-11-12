"""Import a deliberate public snapshot, without changing the working wiki.

Usage: python tools/import_wiki.py PATH_TO_LUX_VAULT
Only the five content folders are included. Raw captures, workspace files,
internal logs, and operational instructions are never copied.
"""
from pathlib import Path
import hashlib
import json
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ('concepts', 'entities', 'moc', 'sources', 'synthesis')

def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    vault = Path(sys.argv[1]).resolve()
    manifest_path = ROOT / 'tools/library-manifest.json'
    prior = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    manifest = {}
    for folder in FOLDERS:
        paths = sorted((vault / 'wiki' / folder).glob('*.md'))
        if not paths:
            raise SystemExit(f'No content found for {folder}; refusing an incomplete import.')
        for path in paths:
            raw = path.read_bytes()
            text = raw.decode('utf-8-sig')
            parts = text.split('---', 2)
            meta = yaml.safe_load(parts[1])
            rel = f'{folder}/{path.name}'
            target = ROOT / 'research' / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            manifest[rel] = {
                'source_path': f'wiki/{rel}',
                'source_sha256': hashlib.sha256(raw).hexdigest(),
                # Normalised digest survives a Git checkout with different line endings.
                'text_sha256': hashlib.sha256(text.replace('\r\n','\n').encode()).hexdigest(),
                'source_updated': str(meta['updated']),
                'added': prior.get(rel, {}).get('added', '2026-11-11'),
            }
    existing = {p.relative_to(ROOT/'research').as_posix() for p in (ROOT/'research').rglob('*.md')}
    if existing - manifest.keys():
        raise SystemExit('Old research files need explicit review; nothing was deleted: '+str(existing-manifest.keys()))
    manifest_path.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
    print(f'Imported {len(manifest)} research notes. Raw captures and internal logs remain local.')

if __name__ == '__main__':
    main()
