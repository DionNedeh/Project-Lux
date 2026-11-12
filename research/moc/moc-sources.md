---
title: "MOC — Sources"
type: moc
tags:
  - fusion/moc
  - fusion/source
status: stable
confidence: high
created: 2026-08-26
updated: 2026-11-02
---
Every ingested source in `raw/`. **48 pages**: 35 papers/reports, 13 article or metadata captures.

## The five carrying most weight

- **[[fia-global-fusion-industry-report-2026]]** — all company-level data here
- **[[doe-fusion-science-technology-roadmap-2026]]** — the US strategy, with quantified milestones
- **[[wurzel-hsu-2025-lawson-criterion-progress-update]]** — the canonical performance dataset
- **[[too-cheap-to-meter-stochastic-fusion-costs-2026]]** — the economics counterweight
- **[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]** — the canonical fuel-cycle analysis, and this vault's authority on whether a plant can fuel itself

## Design studies

[[arc-compact-high-field-demonstration-power-plant]] · [[manta-negative-triangularity-pilot-plant]] · [[eurofusion-research-roadmap-2018]] · [[overview-of-the-helios-design]] · [[maturation-of-critical-technologies-demo-balance-of-plant]] · [[tokamak-cooling-systems-and-power-conversion-system-options]] · [[willis-2026-st-e1-pre-concept-design-overview]] · [[yang-2026-st-e1-tritium-tmap8-surrogate-models]]

## Physics and engineering results

[[prototyping-test-canis-hts-planar-coil-array]] · [[mast-u-superx-divertor-exhaust-control]] · [[runaway-electron-generation-iter-mitigated-disruptions-2026]] · [[sparc-first-campaign-cgyro-predictions]] · [[sparc-toroidal-field-model-coil-program]] · [[baby-tritium-self-sufficiency-experiment]] · [[quasi-single-stage-stellarator-optimization-2026]] · [[novel-approach-proton-boron-11-fusion-2026]] · [[toward-icf-energy-based-on-heavy-ion-beam]]

## Tritium accountancy and safeguards

[[srnl-2013-tritium-accountancy-in-fusion-systems]] · [[sindelar-2023-tritium-accountancy-control-challenges-fusion]] · [[thalia-hera-ukaea-tritium-accountancy-2026]] · [[marsteller-2025-t2apir-first-results]] · [[flynn-larsen-2022-kalman-filters-tritium-accountancy]]

Added 2026-10-19. The measurement discipline behind [[tritium-accountancy]] — framework, instrument
accuracies, the only live instrument programme, and the underpinning spectroscopy.

Flynn and Larsen added 2026-11-02: the only source on **continuous** operation, and the only one
stating its own failure mode.

## Safety, environment, people, demand

[[iter-safety-licensing-lessons-for-demo]] · [[fusion-commercialization-social-environmental-challenges]] · [[accelerating-the-fusion-workforce-2025]] · [[nuclear-fusion-for-ai-data-centers-2026]]

## Round 4 — AI, regulation and public acceptability

[[fusionmae-crossref-metadata-2026]] · [[tokamak-agnostic-elm-crossref-metadata-2026]] · [[tcv-predict-first-rampdown-2025]] · [[hl3-data-driven-rl-control-2025]] · [[china-fusion-device-radiation-safety-2025]] · [[uk-fusion-strategy-2026]] · [[public-acceptability-scoping-review-2026]] · [[fusion-fission-twin-conjoint-public-support-2026]]

## Fuel cycle and tritium self-sufficiency

[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]] · [[meschini-2023-tritium-fuel-cycle-arc-step]] · [[meschini-2025-trapping-tritium-self-sufficiency]] · [[yang-2026-st-e1-tritium-tmap8-surrogate-models]] · [[st-e1-tritium-systems-crossref-metadata-2026]]

Added 2026-11-02. Three code lineages on one question — Abdou's residence-time method, its MIT
extension to [[arc]]- and [[step]]-class plants, and Tokamak Energy's PyFuel. Only the 2025 paper
models [[tritium-retention|trapping]].


## Materials and supply chain

[[ukaea-2026-vanadium-strategy]] · [[gonzalez-de-vicente-2022-fusion-waste]]

Added 2026-11-02. [[vanadium-alloys|V-4Cr-4Ti]] has a documented manufacturing ceiling
(**1200 kg**) and no commercial line — [[22-critical-materials-supply-chains]] §5.

## Held at abstract or metadata level only

[[fusionmae-crossref-metadata-2026]] · [[tokamak-agnostic-elm-crossref-metadata-2026]] · [[public-acceptability-scoping-review-2026]]

**Two Crossref records and one institutional scoping-review record**, each carrying a capture-limit
warning on its source page.

> [!note] Read in full but not captured, 2026-11-02
> [[st-e1-neutronics-crossref-metadata-2026|086003]] and
> [[st-e1-tritium-systems-crossref-metadata-2026|086004]] left this category when IOP's block
> lifted, but **their `file:` fields still point at Crossref JSON** — plain requests remain
> bot-blocked, so neither is held. Basenames keep the `crossref-metadata` form that wikilinks
> depend on.

## Also in raw/

*Counts current at 2026-11-02.*

- `raw/papers/` — **35** PDFs
- `raw/extracts/` — **18** text extractions
- `raw/articles/` — **13** captured official pages, primary article pages or DOI metadata records
- `raw/research-logs/` — **14** session research logs with source attribution

## Live query

``` dataview
TABLE authors AS Authors, publisher AS Publisher, source_date AS Date
FROM "wiki/sources"
SORT source_date DESC
```

---

## Other maps

[[moc-start-here|Start Here]] · [[moc-physics|Physics]] · [[moc-machines|Machines]] · [[moc-engineering|Engineering]] · [[moc-companies|Companies]] · [[moc-economics-policy|Economics & Policy]]
