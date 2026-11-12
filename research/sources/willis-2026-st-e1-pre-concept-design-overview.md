---
title: "Tokamak Energy's Pre-concept Design for a Fusion Power Plant: An Overview of ST-E1"
type: source
source_type: paper
file: "raw/papers/Willis-2026-ST-E1-pre-concept-design-overview.pdf"
authors: "Willis, McNamara, Maartensson, Astbury, Yildirim et al. (85 authors, Tokamak Energy with PPPL, ORNL, INL, Columbia)"
publisher: "Nuclear Fusion 66 086001 (IAEA / IOP Publishing), CC BY 4.0, 11 pp"
source_date: 2026-07-10
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/designs
  - fusion/engineering
status: stable
confidence: high
related:
  - "[[st-e1]]"
  - "[[tokamak-energy]]"
  - "[[tritium-breeding-ratio]]"
  - "[[lithium-6]]"
  - "[[availability]]"
  - "[[q-gain-definitions]]"
  - "[[rafm-steel]]"
  - "[[tungsten-pfc]]"
  - "[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[09-engineering-challenges]]"
created: 2026-10-19
updated: 2026-10-19
---
The **authoritative design document** for [[st-e1|ST-E1]], [[tokamak-energy|Tokamak Energy]]'s
pre-concept fusion power plant, and the overview heading an **11-paper Focus Collection**. Received
19 December 2025, revised 12 February 2026, accepted 20 March 2026, published 10 July 2026. 85
authors, predominantly Tokamak Energy with contributions from PPPL, ORNL, INL and Columbia.

This capture closes the gap recorded at the previous ingest, where ST-E1's parameters reached the
vault only at second hand through a fuel-cycle preprint.

## The design is a financing argument

The stated problem is not physical but commercial: pilot plants are needed to de-risk fusion, yet
their limited lifetime energy output and high upfront capital cost make them hard to fund. ST-E1's
answer is **phased operation with a designed upgrade path**, separating **permanent** assets from
**replaceable** ones so that operating data can be bought without writing off the capital-intensive
parts.

| Permanent (full plant life) | Replaceable |
|---|---|
| Low-aspect-ratio magnet cage — TF, PF and CS coils | Breeding blanket system |
| Vacuum vessel, neutron shielding, cryostat | In-vessel structural items |
| Civil structures and plant | Divertor and other plasma-facing components |
| | High-performance neutron shielding |
| | Elements of H&CD and diagnostics |
| | In-vessel auxiliary control and field-correction coils |

Replaceable segments are engineered for **5 full-power years**, with tungsten armour tiles
potentially needing more frequent replacement in the high-damage mid-plane region.

## The reference design point

Table 1 of the paper. **Where a parameter is identical between phases the commercial column is
empty** — reproduced here with that convention preserved.

| Parameter | Pilot phase | Commercial |
|---|---|---|
| R₀ (m) | 5.0 | — |
| Aspect ratio A | 2.3 | — |
| B₀ (T) | 5.25 | — |
| I_p (MA) | 15 | — |
| Solenoid flux swing (Vs) | 30 | — |
| δ / κ | 0.5 / 2.4 | — |
| P_fus,nom (MW) | **1500** | **2000–2500** |
| P_sep/R (MW m⁻¹) | 25 | 30–40 |
| P_aux,nom (MW) | 75 | 25–50 |
| Q (–) | **20** | **50–70** |
| P_elec,net (MWe) | **300–500** | **800–1000** |
| TF lifetime (FPY) | > 30 | — |
| Neutron wall loading (MW m⁻²) | < 1.6 | 2.1–2.6 |
| TBR (–) | **> 1.14** | — |
| Maintenance scheme | Radial | — |

Mission-level targets alongside the RDP: **normalised CapEx $12,000–14,000/kW** of net electric
(defined in the paper as overnight capital cost per unit net electric power) and **plant availability
> 80%**.

Later studies identified a family of equivalent-performance devices at **A = 1.9–2.3** with
**B₀ = 3.25–5.25 T**, so the design point is a choice within a band rather than a unique solution.

> [!warning] The paper writes `Q` bare
> Table 1 gives "Q (–)" with no subscript, and the prose says only *"fusion gain"*. The vault does
> not accept an unqualified Q ([[q-gain-definitions]]). **Arithmetic on the paper's own rows
> identifies it:** 1500 MW / 75 MW = 20 exactly for the pilot phase, and 2000–2500 / 25–50 spans
> the quoted 50–70 for the commercial phase. It is therefore **`Q_sci`** — fusion power over
> auxiliary heating power — *as derived by this vault*, not as labelled by the source. Recorded as a
> derivation, not a quotation.

## The finding with the widest consequences: unenriched lithium

**ST-E1's breeder is pure, unenriched lithium**, with vanadium-alloy structure and helium cooling in
the initial configuration. The paper's stated rationale is to achieve a high **volumetric** TBR
*"without reliance on Li-6 enrichment"* or extensive use of toxic multipliers such as
[[beryllium|beryllium]], while keeping radioactive waste acceptable.

This matters because the vault has recorded ⁶Li enrichment to **30–90%** as a requirement of breeding
blankets and as a sovereignty chokepoint concentrated in Russia and China
([[lithium-6]], [[22-critical-materials-supply-chains]]). **ST-E1 is a design route that sidesteps
that chokepoint entirely** — plausibly because a low-aspect-ratio spherical tokamak affords thick,
high-coverage blanket volume. It does not invalidate the enrichment finding for other designs; it
establishes that enrichment is a property of particular blanket architectures rather than of D-T
fusion.

**Vanadium alloys are chosen over [[rafm-steel|RAFM steel]]** for a wider allowable temperature
window and favourable neutron absorption, enabling higher temperatures and improved thermodynamic
efficiency. This explains the V-4Cr-4Ti pipework modelled in
[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]. Shielding is **tungsten carbide** in modular
units, plus boron carbide, RAFM and stainless steels.

## Other figures worth carrying

- **Commercial phase is steady-state**, requiring fully non-inductive current sustainment with high
  self-driven bootstrap fraction. Pilot phase retains a solenoid (30 Vs flux swing).
- **Pedestal and density:** κ = 1.3–1.6, Greenwald density fraction at the pedestal top
  f_GW = 0.8–1.0, q_min ≳ 2.2 to avoid sawteeth and low-order neoclassical tearing modes, core
  radiated fraction 45–69%.
- **An upgrade path is deliberately preserved for the blanket:** greater use of liquid lithium as a
  self- or dual-cooled option in the commercial configuration *could* reduce recirculating power by
  **up to 200 MW** and raise thermal cycle efficiency. Stated as an upgrade option, not a design.
- **Grid behaviour:** a 5-minute current ramp to full fusion power while capping peak grid draw at
  500 MW needs only **1–2 MWh** of on-site storage — notably modest against the
  [[thermal-storage-pulsed-operation|thermal storage]] burden carried by pulsed designs, because
  ST-E1 is not pulsed.

## Internal inconsistency preserved

**The paper gives two TBR figures.** Table 1's RDP states **TBR > 1.14**; §3.2 states the *"target of
the TBR is ~1.1, leaving a sufficient margin to cover decay and processing losses"*. These are not
the same requirement, and the paper does not reconcile them. Both are recorded; see
[[tritium-breeding-ratio]] and *Known conflicts* in [[index]].

## Access limitations

**Inspected in full.** The 11-page article was captured to `raw/` and extracted to `raw/extracts/`;
every figure above was read from that extract. **CC BY 4.0**, confirmed both in the article text and
by OpenAlex (`oa_status: gold`, licence `cc-by`).

> [!note] The route to this capture, and why it is recorded
> **The publisher's own PDF link is CAPTCHA-gated.** IOP's PDF URL returned a *Radware Bot Manager
> Captcha* HTML page rather than the article. That download was discarded without being finalised
> into `raw/` — a 14 KB HTML file named `.pdf` is not evidence. **No attempt was made to work around
> the CAPTCHA.**
>
> OpenAlex lists **only** that CAPTCHA-gated IOP URL as a PDF location for this CC BY 4.0 article;
> the DOAJ record carries a landing page and no full text. The copy captured here came from **OSTI
> (osti.gov/servlets/purl/3378206, OSTI ID 3378206)**, a legitimate DOE repository route reached
> because DOE-funded co-authors deposited it under contracts AC02-09CH11466 and SC0024889.
>
> **The captured file is the version of record**, not an accepted manuscript: it carries IOP's
> "PAPER · OPEN ACCESS" banner, the typeset `Nucl. Fusion 66 (2026) 086001 (11pp)` header, the DOI
> and an IOP download stamp. **OSTI's own metadata flags it `journal_type: AM` (accepted
> manuscript), which the file itself contradicts.** The file is trusted over the metadata, and the
> disagreement is recorded rather than resolved silently.
>
> This is the second CC BY 4.0 fusion paper in this vault whose publisher route is CAPTCHA-blocked,
> after Tang *et al.* on [[helios|Helios]] balance of plant. The pattern is worth noting: open
> licence does not imply open access in practice.

**Not inspected:** the **10 companion papers** of the Focus Collection, all in *Nuclear Fusion*
volume 66 — 086002 Wilson *et al.* (PyTok whole-plant code), 086003 Chandrasekhar *et al.*
(neutronics), **086004 Yildirim *et al.* (tritium production and processing)**, 086005 Mohamed
*et al.* (thermal management and net power), 086006 Willis *et al.* (maintenance and site layout),
086007 Maartensson *et al.* (physics and magnet design), 086008 McNamara *et al.* (flat-top scenario),
086009 Zhang *et al.* (time-dependent scenarios), 086010 Lopez *et al.* (heating and current drive),
086011 Robinson *et al.* (power and particle exhaust). Recorded in *Known gaps*.

**Updated 2026-10-19.** The two companions carrying this paper's breeding evidence were sought
immediately afterwards. Both are now held as **Crossref metadata with complete abstracts only** —
[[st-e1-neutronics-crossref-metadata-2026|086003]] and
[[st-e1-tritium-systems-crossref-metadata-2026|086004]] — because their full texts are unreachable
by every route tried. **Neither abstract states a TBR**, so this paper's unenriched-lithium breeding
claim remains asserted and unevidenced in this vault. 086003's abstract does not mention lithium at
all.

## What this source does not establish

- **Nothing is built, and nothing is measured.** This is a **pre-concept** design. Every figure is a
  target, a requirement or a systems-code output. ST-E1 has no hardware; Tokamak Energy's hardware
  evidence remains [[st40|ST40]] and the Demo4 magnet.
- **The TBR is not demonstrated and the unenriched-lithium claim is not validated here.** The
  volumetric-TBR argument is asserted in this overview and referred to the companion neutronics and
  tritium papers (086003, 086004), **neither of which is held**. No breeding blanket has operated in
  any device.
- **The availability target is a target.** >80% sits far above anything fusion has demonstrated, and
  the paper itself identifies availability as a dominant economic determinant whose maintenance cost
  and schedule drivers are still being identified.
- **CapEx is an estimate against an unbuilt plant.** $12–14k/kW is a design goal; the paper notes
  that even if ST-E1 misses its normalised CapEx or availability targets it would still provide
  significant value — which is an explicit acknowledgement that it may miss them.
