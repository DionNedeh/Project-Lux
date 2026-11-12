# Project Lux

**AI, fusion, and the possibilities ahead.** A Voelori research resource.

[Visit Project Lux](https://dionnedeh.github.io/Project-Lux/) · [Research library](https://dionnedeh.github.io/Project-Lux/library/index.html) · [Evidence and method](https://dionnedeh.github.io/Project-Lux/method.html)

Lux explores how AI might contribute to more effective energy systems, beginning with fusion. Its public site includes an introduction to learning, forecasting and experimental control, eight featured citation briefs, and a complete publication snapshot of 282 interconnected research notes:

| Collection | Notes |
|---|---:|
| Synthesis | 46 |
| Source notes | 48 |
| Concepts | 75 |
| Entities | 106 |
| Topic guides | 7 |

Research records are individually dated. Publication is not a new scientific validation of the corpus. Source-access limitations, unresolved conflicts, simulations, preprints, and company projections retain their original context. Lux does not claim an operating plant or measured energy savings.

## Repository structure

- `templates/home.html` — the approved homepage layout, before generation.
- `styles.css`, `site.js`, `library.js`, `assets/` — presentation and browser-local interactions.
- `research/` — Markdown publication snapshot, with original frontmatter and content.
- `library/` — generated full notes, reference briefs, and catalogue.
- `tools/library-manifest.json` — provenance, source hashes, revision dates, and publication dates.
- `tools/featured-references.json` — the eight bounded homepage briefs and their citations.
- `tools/build_site.py` — deterministic static generator and publication artifact builder.
- `tools/check_site.py` — all-page local link, anchor, outline, metadata and provenance checks.
- `tests/` — Markdown conversion regressions and real-browser interaction, accessibility, responsive and publication checks.
- `.github/workflows/pages.yml` — build and test every pull request; publish passing `main` builds to GitHub Pages.
- `_site/` — ignored deployment artifact containing only public website files and research notes.

The working Obsidian vault is separate from this publication checkout. Raw third-party PDFs, captured article text, internal research logs, and personal workspace files are not included. Source notes link to publishers and open archives. No redistribution licence is asserted over third-party papers.

## Build and check

Use Python 3.12 and Node 24, matching CI:

```sh
python -m pip install -r tools/requirements.txt
npm ci --ignore-scripts --no-audit --no-fund
python tools/build_site.py
python -m unittest discover -s tests/unit -v
npx playwright install chromium
npm test
```

On a system with an installed browser, `LUX_BROWSER_EXECUTABLE` can specify its executable for tests. CI installs Playwright's pinned Chromium revision instead.

The build renders all 282 notes and the eight citation briefs, builds the complete text-search index, stamps local CSS/JS assets by content hash, emits canonical metadata, a sitemap and custom 404, and checks the entire site. It fails on unresolved links, broken anchors, duplicate IDs, missing metadata, source digest drift or heading jumps.

To preview the exact Pages layout:

```sh
node tools/serve.cjs
```

Open `http://127.0.0.1:8768/Project-Lux/`. The preview serves only `_site/`, including real 404 behaviour. Stop it with Ctrl+C.

To check an already deployed site, set `LUX_TEST_URL` to its trailing-slash URL before running `npm test`. This skips the local server. Automated accessibility checks support, but do not replace, manual assistive-technology review.

## Update the research

Update and validate the source wiki first. Then import an explicit publication snapshot:

```sh
python tools/import_wiki.py /path/to/Project-Lux-vault
python tools/build_site.py
```

The importer includes only `concepts`, `entities`, `moc`, `sources`, and `synthesis`. It never modifies the source vault or imports raw captures, internal activity logs, or workspace settings. Unknown/stale publication files need an explicit review; imports do not silently delete them.

`source_sha256` records the original file bytes at import. `text_sha256` is line-ending-normalised so reproducibility checks work on both Windows and Linux. The public Markdown retains all source text and frontmatter; Git may normalise line endings.

Review the generated diff and dates, add a public update when evidence changes, and commit both source and generated files. CI rebuilds and refuses deployment if the committed output is stale. Preserve contradictory evidence and source limitations; do not remove evidence to satisfy formatting or length checks.

## Publication

GitHub Pages uses the **GitHub Actions** source. The deployment job depends on the complete check job, uses only `pages: write` and `id-token: write`, and publishes the checked `_site/` artifact. Pull requests run checks without deployment permissions. See [publication verification](docs/publication-verification.md) for the checks performed for the initial release and remaining limits.

The static site has no accounts, backend, analytics, cookies, or third-party runtime requests. Full-text search is performed locally in the browser. The visible research remains readable with JavaScript disabled.

## Corrections

Please report errors through this repository's issue tracker with a page URL, exact claim, and supporting primary source where possible. No response deadline is promised. Project Lux is maintained by Voelori.
