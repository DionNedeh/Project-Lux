---
title: "MOC — Companies"
type: moc
tags:
  - fusion/moc
  - fusion/companies
status: stable
confidence: high
created: 2026-08-26
updated: 2026-08-29
---
All 37 company pages. Long-form analysis in [[07-private-fusion-industry]]; funding data from [[fia-global-fusion-industry-report-2026]].

**Sector totals:** $14.24 bn cumulative · $4.48 bn in the year to July 2026 · 56 companies · avg $2.7 bn further needed each.

## The billion-dollar tier — all US

| Company | Declared | Approach |
|---|---|---|
| [[commonwealth-fusion-systems]] | **~$4 bn** | High-field tokamak |
| [[helion-energy]] | $1.5 bn | Pulsed FRC, D-³He |
| [[tae-technologies]] | $1.5 bn | Beam-driven FRC → p-¹¹B |
| [[shine-technologies]] | $1.1 bn | Neutrons → isotopes → energy |
| [[pacific-fusion]] | $1.0 bn | Pulser-driven ICF |

## $100m – $1bn

[[proxima-fusion]] · [[enn]] · [[focused-energy]] · [[general-fusion]] · [[inertia-enterprises]] · [[marvel-fusion]] · [[yan-fusion]] · [[zap-energy]] · [[tokamak-energy]] · [[type-one-energy]] · [[xcimer-energy]] · [[first-light-fusion]] · [[startorus]] · [[kyoto-fusioneering]] · [[thea-energy]] · [[energy-singularity]] · [[avalanche-energy]]

## Smaller and specialist

[[renaissance-fusion]] · [[helical-fusion]] · [[ex-fusion]] · [[blue-laser-fusion]] · [[novatron]] · [[nt-tao]] · [[gauss-fusion]] · [[openstar-technologies]] · [[realta-fusion]] · [[astral-systems]] · [[longview-fusion]] · [[hb11-energy]] · [[maritime-fusion]] · [[stellarex]] · [[neofusion]]

## Not developers — suppliers and counterparties

[[kyoto-fusioneering]] (plant technology) · [[black-moon-energy]] (helium-3) · [[google]] · [[microsoft]] (offtake)

## Live query

``` dataview
TABLE country AS Country, funding_usd AS Funding, approach AS Approach
FROM "wiki/entities"
WHERE entity_type = "company"
SORT funding_usd DESC
```

---

## Other maps

[[moc-start-here|Start Here]] · [[moc-physics|Physics]] · [[moc-machines|Machines]] · [[moc-engineering|Engineering]] · [[moc-economics-policy|Economics & Policy]] · [[moc-sources|Sources]]
