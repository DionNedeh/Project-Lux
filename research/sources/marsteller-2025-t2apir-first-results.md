---
title: "First Results of the Tritium Absorption InfraRed Spectroscopy (T2ApIR) Experiment"
type: source
source_type: paper
file: "raw/papers/Marsteller-2025-T2ApIR-first-results.pdf"
authors: "Marsteller, Batzler, B. Bornschein, L. Bornschein, Eckard, Hanß, Kohpeiß, Kurz, Lietzow, Sturm, Vrkic, Welte & Größle (13 authors, IAP-TLK, Karlsruhe Institute of Technology)"
publisher: "arXiv:2512.19757v1 (preprint; no journal reference), CC BY 4.0, 24 pp"
source_date: 2025-12-19
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/data
status: stable
confidence: medium
related:
  - "[[tritium-accountancy]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[pellet-injection]]"
  - "[[tritium-start-up-inventory]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[19-simulation-codes-nuclear-data]]"
created: 2026-10-19
updated: 2026-10-19
---
An instrument paper from the **Tritium Laboratory Karlsruhe (IAP-TLK)** at KIT — one of very few
facilities licensed to handle gram-scale tritium — describing a cryogenic spectroscopy cell in
**scientific commissioning**.

> [!note] This is an enabling-data source, not an accountancy source
> T2ApIR does not measure plant inventories and makes no accountancy claim. It belongs in this
> cluster because the measurement it serves sits underneath accountancy: **laser Raman spectrometry
> is the most accurate tritium concentration method in the accountancy table** at **< 0.5%**
> ([[sindelar-2023-tritium-accountancy-control-challenges-fusion]]), and spectroscopic concentration
> measurement is only as good as the reference data behind it. The vault records the connection as
> that, and not as a claim the authors make.

## The stated gap

*"The literature on experimentally verified material properties of tritium is sparse"* — and the
paper names four places that scarcity bites: **pellet production** for magnetic confinement
([[pellet-injection]]), **target fuelling** for inertial confinement, **cryogenic distillation**
(the isotope-separation workhorse of [[28-vacuum-wall-conditioning-tritium-plant|the tritium
plant]]), and neutrino and rare-event physics.

That is a notable finding in itself: the properties of the fuel are less well characterised than the
machines built to burn it.

## What the instrument does

- Investigates **all six hydrogen isotopologues** (H₂, HD, D₂, HT, DT, T₂) and their mixtures in
  **gaseous, liquid and solid** phases, plus **the dynamics of phase changes**
- Mixtures with noble gases — **xenon and neon** — can also be studied
- A cryogenic measurement cell reaching **below 10 K**, with optical access for **infrared
  absorption spectroscopy**, **Raman spectroscopy** and a **polariscope**, alongside temperature and
  pressure measurement
- Ortho-para states are among the declared subjects

## Access limitations

**Inspected in full.** The 24-page preprint was captured to `raw/` from arXiv and extracted; the
quotations and figures above were read from that extract. **CC BY 4.0.**

> [!note] A page-count discrepancy, checked and resolved
> `file` reported the downloaded PDF as 4 pages against the arXiv listing's 24. Counting page breaks
> in the extract confirms **24 pages**, complete through a reference list ending on page 24 — the
> utility had misread the PDF's structure. Recorded because an apparently truncated capture is worth
> settling rather than assuming either way.

**Preprint, not peer-reviewed.** arXiv v1, with **no journal reference**; `confidence: medium`
reflects that and the commissioning status, not doubt about TLK.

## What this source does not establish

- **No results that this vault can use yet.** The experiment is in **scientific commissioning** —
  "first results" here means the apparatus works, not that material-property data has been
  published. The vault takes no tritium property value from it.
- **No accountancy performance figure.** No detection limit, sensitivity or concentration accuracy
  appears, so it cannot be compared against the < 0.5% Raman figure it ultimately supports.
- **Nothing about a fusion plant.** This is a laboratory cell handling laboratory quantities, not an
  in-line instrument on a fuel cycle.
