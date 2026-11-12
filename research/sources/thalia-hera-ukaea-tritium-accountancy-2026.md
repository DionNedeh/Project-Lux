---
title: "Development of Analytical Techniques for Tritium Accountancy Around the Fusion Fuel Cycle (HERA and THALIA)"
type: source
source_type: notes
file: "raw/articles/thalia-hera-ukaea-tritium-accountancy-2026.html"
authors: "Mont, C. (UKAEA Tritium Fuel Cycle division)"
publisher: "LIBRTI Conference on Breeder Blanket Technology, Culham Campus, 3–5 February 2026 — programme entry"
source_date: 2026-02-03
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/programs
status: stable
confidence: medium
related:
  - "[[tritium-accountancy]]"
  - "[[librti]]"
  - "[[ukaea]]"
  - "[[lithium-lead-eutectic]]"
  - "[[st-e1]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[srnl-2013-tritium-accountancy-in-fusion-systems]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-10-19
updated: 2026-10-19
---
**The only live instrument-development programme on tritium accountancy that this vault holds.**
A conference programme entry from the **[[ukaea|UKAEA]] Tritium Fuel Cycle division**, working with
**[[librti|LIBRTI]]**, describing two named projects. It answers the question the American sources
leave open — who is actually building the missing measurements.

## Two projects, two halves of the problem

**HERA — real-time analysis of gas streams.** Tests a **mass spectrometer** and a **Raman
spectrometer**, aiming to quantify **H₂, D₂ and T₂ from the limit of detection up to 100% gas
streams**. A **palladium catalyst** enables semi-quantification of the mixed isotopologues **HD, HT
and DT**. The glovebox **generates its own calibration standards**, using calibrated vessels and
PVTc calculations.

> [!note] This is the continuous-flow problem being attacked directly
> [[srnl-2013-tritium-accountancy-in-fusion-systems|Klein *et al.*]] showed that a continuously
> operating fuel cycle cannot be stopped for physical inventory, and that flow-measurement
> uncertainty grows as √t. **HERA's "real-time" framing targets exactly that**, and its instrument
> choice is the best pair in the accountancy table — Raman at < 0.5% and mass spectrometry at
> 0.5–5% ([[sindelar-2023-tritium-accountancy-control-challenges-fusion]]). Its self-calibration by
> PVTc is that table's "static PVTC" method used as the reference for the dynamic one.

**THALIA — tritium trapped in liquid breeder materials.** Develops and validates a method for
accountancy of tritium held in **liquid lithium, LiPb and FLiBe**, with the **first phase on FLiBe**.
Two sub-projects:

- **ERATO** — sample preparation for analysing tritiated lithium-based salts by **liquid
  scintillation counting (LSC)**
- **CLIO** — hydrogen analysis by **ICP-MS**, a technique the entry notes *"is widely used but has
  not been developed for small atoms such as hydrogen and its isotopologues"*

**Both techniques are at low technology readiness level**, principally because getting the tritiated
lithium matrix into a state suitable for analysis is difficult. Stated challenges: working with
lithium-based materials, **unknown tritium speciation**, very low concentrations, and sample storage.

> [!warning] Breeder-inventory accountancy is at low TRL, and that has a named consequence
> [[sindelar-2023-tritium-accountancy-control-challenges-fusion|Sindelar *et al.*]] note that no
> method exists for measuring tritium production in a blanket, and this is the programme trying to
> build one — starting from a **low TRL** with **tritium speciation in the breeder unknown**.
>
> It lands directly on a design already in this vault: **[[st-e1|ST-E1]] breeds in *liquid
> lithium***, which is THALIA's third target material rather than its first. So the plant whose
> breeding claim this vault could not evidence also sits in the material class whose accountancy
> methods do not yet exist.

## Access limitations

**Programme entry only — a conference description, not an abstract, and not a paper.** The page was
captured to `raw/articles/` and the project names verified present in the captured HTML. There is no
publication behind it in this vault.

**No quantitative figures of any kind.** No detection limits, no tritium concentrations, no
accuracies, no timelines and no funding figure appear on the page. Everything above is a statement of
intent and approach.

Single-speaker programme entry: **Clemence Mont, UKAEA**, a 30-minute talk in Session 3-11. The
institutional authority is UKAEA's, not a peer-reviewed result's — hence `confidence: medium`.

## What this source does not establish

- **No results.** Nothing has been measured, validated or published. "Low technology readiness
  level" is the entry's own characterisation.
- **No evidence that either technique will work.** ICP-MS for hydrogen isotopes is explicitly
  undeveloped, and LSC sample preparation for tritiated lithium salts is the stated obstacle rather
  than a solved step.
- **Nothing about liquid lithium or LiPb specifically**, which are named as targets beyond the FLiBe
  first phase. The breeder most relevant to [[st-e1]] is the least advanced here.
- **No link to a regulatory requirement.** The programme is developing capability; nothing states
  what standard it would satisfy, and per
  [[sindelar-2023-tritium-accountancy-control-challenges-fusion]] no IAEA or NRC requirement for
  tritium exists to satisfy.
