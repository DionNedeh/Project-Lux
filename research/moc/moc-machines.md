---
title: "MOC — Machines"
type: moc
tags:
  - fusion/moc
  - fusion/machines
status: stable
confidence: high
created: 2026-08-26
updated: 2026-09-08
---
Every fusion device with a page in this wiki. See [[04-magnetic-confinement-devices]] and [[05-inertial-confinement-fusion]] for the long-form treatment, and [[26-appendix-quantitative-data]] for measured performance.

## Being built now — the ones that matter

- [[sparc]] — **the most important machine in fusion.** Q > 1 attempt, 2027
- [[iter]] — 500 MW burning plasma. Research operation 2034, D-T 2039
- [[arc]] — first grid-scale commercial plant, ~400 MWe, Virginia
- [[step]] — UK prototype power plant, West Burton
- [[best-tokamak]] · [[cfetr]] — China's burning-plasma and DEMO-equivalent line
- [[infinity-two]] — 350 MW stellarator at a TVA site
- [[eos]] — planned integrated planar-coil stellarator; preceded by the [[canis]] magnet-array prototype
- [[helios]] — planar-coil stellarator power plant, ~390 MWe; preconceptual design only
- [[st-e1]] — spherical tokamak power plant, phased 300–500 then 800–1000 MWe; pre-concept design only
- [[eu-demo]] · [[manta]] · [[dtt]]

## Operating

**Tokamaks:** [[east]] (1,066 s H-mode) · [[jt-60sa]] (largest superconducting) · [[kstar]] · [[diii-d]] (US flagship) · [[asdex-upgrade]] · [[tcv]] · [[west]] · [[hh70]] (first fully HTS) · [[t-15md]] · [[sst-1]] · [[aditya-u]] · [[ktm]] · [[tcabr]]
**Spherical:** [[mast-upgrade]] · [[st40]] · [[globus-m2]]
**Stellarator:** [[wendelstein-7-x]] — world triple-product record at long pulse
**Inertial / pulsed:** [[nif]] · [[omega-laser]] · [[z-machine]]
**Alternative:** [[wham]] (17 T) · [[polaris]] · [[lm26]]

**Magnet prototype:** [[canis]] — nine planar HTS shaping coils operated as a 3 × 3 array at 20 K; no plasma

## Retired, and why they still matter

- [[jet]] — the most important device ever built. 69 MJ; the only tokamak maintained remotely
- [[tftr]] — **still holds the triple-product record, set in 1995**
- [[alcator-c-mod]] — the high-field ancestor of SPARC
- [[lhd]] — concluded December 2025 after 200,000 shots
- [[mftf-b]] — completed 1986, dismantled 1987, never operated
- [[zeta]] — the 1958 retraction that taught the field to measure confinement time
- [[t-3]] — the machine that converted the world to tokamaks

## Live query

``` dataview
TABLE country AS Country, status_detail AS Status, first_plasma AS "First plasma"
FROM "wiki/entities"
WHERE entity_type = "machine"
SORT status_detail ASC, title ASC
```

---

## Other maps

[[moc-start-here|Start Here]] · [[moc-physics|Physics]] · [[moc-engineering|Engineering]] · [[moc-companies|Companies]] · [[moc-economics-policy|Economics & Policy]] · [[moc-sources|Sources]]
