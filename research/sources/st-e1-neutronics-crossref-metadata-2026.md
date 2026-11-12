---
title: "Nuclear Technology Considerations and Neutronics for the ST-E1 Fusion Power Plant"
type: source
source_type: paper
file: "raw/articles/st-e1-neutronics-crossref-metadata-2026.json"
authors: "Chandrasekhar, Lister Wilson, Michelle Levine, Irukuvarghula, Bharatbhai Godhani, David Naish et al. (8 authors, Tokamak Energy Ltd)"
publisher: "Nuclear Fusion 66 086003, DOI 10.1088/1741-4326/ae63e2, CC BY 4.0"
source_date: 2026-07-10
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/engineering
  - fusion/computation
status: stable
confidence: high
related:
  - "[[st-e1]]"
  - "[[tokamak-energy]]"
  - "[[tritium-breeding-ratio]]"
  - "[[declared-tbr-values]]"
  - "[[vanadium-alloys]]"
  - "[[rafm-steel]]"
  - "[[tungsten-pfc]]"
  - "[[nuclear-data-fendl]]"
  - "[[rebco]]"
  - "[[displacements-per-atom]]"
  - "[[spherical-tokamak]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[43-fusion-waste-classification-and-disposal]]"
created: 2026-10-19
updated: 2026-11-02
---
The [[st-e1|ST-E1]] Focus Collection's neutronics and shielding paper.

> [!note] Full text reached 2026-11-02. The page basename is historical
> Captured on 19 October 2026 as a Crossref metadata record only, because IOP served a CAPTCHA.
> **The publisher block has since lifted and the full text was read on 2 November 2026** —
> sections 1 to 3.6, via the harness's own fetch. The basename still says
> `crossref-metadata` and the `file:` field still points at the JSON, because **no local
> capture of the full text was possible**: plain HTTP requests are still bot-blocked. See
> *Access limitations*.

> [!warning] CORRECTION 2026-11-02 — the 30-year magnet life does not survive the full text
> This page previously recorded, from the abstract, that the design *"demonstrates feasibility of
> limiting neutron flux to the magnet systems to support a full power life of 30 years."* **The
> full text shows the baseline does not achieve it.** Peak HTS fast flux is **9.5 × 10⁹ cm⁻² s⁻¹**
> against a stated **< 4 × 10⁹** limit — **2.4× over** — for **13 full-power years**, not 30. A
> **2400 MW** variant, tungsten boride at aspect ratio 2.31 with a 100 mm plasma–wall gap, reaches
> ~**5.6 × 10⁹** and roughly **25 fpy**. The abstract described an *intent*; the paper reports a
> shortfall against it.

## Breeding, now with numbers

| Code | TBR | of which Li-7 |
|---|---|---|
| MCNP | **1.169** | 0.327 |
| G4Tokamak | **1.194** | 0.322 |

No TBR target is stated, and **lithium enrichment is not mentioned** — the breeder is covered in
[[st-e1-tritium-systems-crossref-metadata-2026|086004]]. Inboard breeding is **ruled out for lack
of space**; the outboard vertical shield reflects neutrons back to recover TBR. Both values sit
**above** 086004's 1.146 baseline — [[declared-tbr-values]].

## What the full text settles

Detail sits on the pages that should carry it; this is the index of it.

- **Nuclear data**, previously open: **ENDF/B-VIII.0** transport, **FISPACT-II / TENDL-2019**
  activation — [[nuclear-data-fendl]].
- **The MCNP benchmark has a metric:** mean flux ratio **0.90** — [[19-simulation-codes-nuclear-data]].
- **Radiation damage:** ≈ **50 dpa/fpy** in centre-column tungsten carbide —
  [[displacements-per-atom]].
- **Cryogenic margin:** 18.5 kW against 20 kW — [[18-superconductors-and-magnets]].
- **Materials:** **V-4Cr-4Ti** shield box ([[vanadium-alloys]]), **F82H** [[rafm-steel|RAFM]]
  overhead shield, 316L(N)-IG vessel, K-doped [[tungsten-pfc|tungsten]] armour.

## What it still does not establish

- **No neutron wall loading in MW m⁻²**, so the overview's figures remain uncross-checked; **no
  cumulative fluence**, only the fast-flux limit.
- **Nothing measured.** Pre-concept simulation of an unbuilt plant, by its designers.
- **Activation remains a named problem**: non-reduced-activation steels and plasma-facing
  components activate most in the machine.

## Access limitations

**Read 2 November 2026** via the harness's fetch of the IOP landing page — sections 1–3.6 of a
120,716-character page; closing sections, licence statement and affiliations were not in the
retrieved text. **CC BY 4.0** per Crossref.

**No local capture was possible.** A plain request returned a page carrying a Radware marker
rather than the article; a substituted user-agent was **not pursued**, being bot-check
circumvention. The raw capture remains the Crossref JSON of 19 October 2026; `raw/` is
append-only.
