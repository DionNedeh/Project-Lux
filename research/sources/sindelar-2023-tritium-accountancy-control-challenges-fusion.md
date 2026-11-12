---
title: "Assessment of Challenges for Tritium Accountancy and Control in Fusion Energy Systems"
type: source
source_type: paper
file: "raw/papers/Sindelar-2023-tritium-accountancy-control-challenges-fusion.pdf"
authors: "Sindelar, Babineau, Gibbs, Klein & Moore (SRNL, ORNL and Savannah River Site)"
publisher: "INMM & ESARDA Joint Annual Meeting, 22–26 May 2023, 9 pp"
source_date: 2023-05-22
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/security
  - fusion/policy
status: stable
confidence: high
related:
  - "[[tritium-accountancy]]"
  - "[[srnl-2013-tritium-accountancy-in-fusion-systems]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-start-up-inventory]]"
  - "[[iter]]"
  - "[[us-nrc]]"
  - "[[us-doe]]"
  - "[[11-policy-regulation-safety]]"
  - "[[37-military-dual-use-security]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-10-19
updated: 2026-10-19
---
The current assessment, presented to the **INMM & ESARDA joint annual meeting** — the safeguards
profession's own forum — and recapping the tritium panel of the **Fusion Energy and Nonproliferation
Workshop** held at [[pppl|PPPL]]. Funded jointly by **DOE NNSA's Office of Defense Nuclear
Nonproliferation** and the **DOE Office of Fusion Energy Science**, which is itself informative about
who is asking the question.

## The regulatory position, precisely

This is the paper that lets the vault state tritium's status exactly rather than by implication:

- **Until 2011** tritium was regarded as a **special nuclear material (SNM)** by the US DOE.
- **At present** it is categorised as **"other nuclear material"** for Nuclear Material Control and
  Accountability purposes, per **DOE-STD-1194-2019**, driven by **DOE Order 474.2A** (7 February
  2023).
- **Neither the [[us-nrc|US NRC]] nor the IAEA consider tritium an SNM.**
- Prospective fusion systems — fission/fusion hybrids excepted — would not require special
  fissionable materials, and so *"would not be subject to safeguards per the IAEA"*.
- Consequently **neither the IAEA nor the NRC prescribe material control and accountability
  requirements for tritium at all.**

> [!warning] The breeding margin *is* the diversion quantity
> The sharpest finding, and one that reframes a number this vault has only treated as an engineering
> requirement. Sustainability requires breeding **10–20% above what is burned** — and the paper
> states that *"this additional 10–20% of bred tritium could become a source for diversion of tritium
> for use other than the specific fusion device at which it is bred."*
>
> The tritium panel puts it more starkly: the excess, bred minus burned minus losses, *"is where any
> diverted tritium would have to come from, otherwise, the fusion process will not be sustainable."*
>
> So [[tritium-breeding-ratio|TBR > 1.1]] is simultaneously the condition for fusion existing as an
> energy source **and** the quantity a safeguards regime would have to watch. The margin cannot be
> designed away without destroying the fuel cycle.

## Measurement accuracies

Table 1, *"Techniques for Tritium Accountancy"*. **The figures are compiled from Nishi *et al.*,
*Fusion Engineering and Design* **81** (2006) 745–751** — see the dating caveat below.

| Method | Practical accuracy (uncertainty) |
|---|---|
| **"Static" PVTC** (pressure, volume, temperature, concentration) | **1–5%** integrated |
| — pressure | 0.2–0.9% |
| — volume | < 0.5% |
| — temperature | 0.1 °C |
| **"Dynamic" PVTC** — accountancy with mass flowing | **a few %** integrated |
| **Calorimetric method** | **~1%** integrated |
| *Concentration:* **laser Raman spectrometer** | **< 0.5%** — the best listed |
| *Concentration:* mass spectrometer | 0.5–5% |
| *Concentration:* gas chromatograph | few to 5% |
| *Concentration:* Bremsstrahlung X-ray | a few % |
| *Concentration:* ionisation chamber | few to 10% |
| Releases to environment | **~10%** |

> [!warning] The two measurements fusion most needs do not exist
> The table's own note: *"Measurement methods including indirect methods using neutron flux for
> tritium consumption by the fusion reaction and for tritium production in the blanket **would need to
> be developed**."*
>
> That is the whole of the fusion-specific problem in one sentence. **Burn-up and breeding — the two
> terms the fusion-modified balance adds ([[srnl-2013-tritium-accountancy-in-fusion-systems]] Eq. 5)
> — have no measurement method.** Everything in the table above measures tritium in a pipe or a bed,
> not tritium being made in a blanket or consumed in a plasma.

## The tritium panel's findings

- **[[iter|ITER]]'s total in-process tritium inventory is expected to be approximately 1 kg.**
  Note this is *in-process* inventory, a different quantity from the
  [[tritium-start-up-inventory|start-up inventory]] of 11 kg that Abdou computes for a 3 GW plant.
- Commercial D-T plants are put at **several hundred grams up to 1 kg** in-process each, with
  *"hundreds to thousands"* of plants globally at scale.
- **Steady state is not reached until permeation and hold-up losses have occurred**, and is
  plant-specific — so early-life accountancy is measuring a system that is still filling its own
  walls.
- Accountancy error **spreads through successive input, burn, output and breed steps**.
- The international staff scale for monitoring *"would be substantial"*.
- Static-system inventory methods named: **installed metal hydride beds, installed molecular sieve
  beds, sealed confinement vessels**; loss detection by **inventory-difference control limits** and
  **statistical sampling plans**.

## Access limitations

**Inspected in full.** The nine-page paper was captured to `raw/` from the INMM resource server and
extracted; everything above was read from that extract. Publicly posted by INMM; the paper carries a
US Government public-access licence under the DOE Public Access Plan.

> [!note] The accuracy figures are twenty years old
> Table 1 is reproduced from a **2006** paper (Nishi *et al.*) inside a **2023** assessment. The
> vault records them as the best compiled figures it holds, **not as current instrument
> performance** — two decades of spectroscopy and mass spectrometry sit between that table and now.
> **Nishi *et al.* 2006 is not held in `raw/`**, so these accuracies reach the vault at second hand.

**Not inspected**, and all cited by this paper as the primary record behind its findings:

- The **Fusion Energy and Nonproliferation Workshop Summary Report**, Revision 1, 7 April 2023
  (PPPL-hosted) — the source of the tritium panel findings quoted above.
- **Nishi *et al.*** (2006) — the origin of every accuracy figure.
- **Flynn & Larsen**, *Investigating the Application of Kalman Filters for Real-time Accountancy in
  Fusion Fuel Cycles*, *Fusion Engineering and Design* **176** (2022) 113037 — directly addressing
  the continuous-flow problem, and the obvious next capture on this subject.
- DOE-STD-1194-2019, DOE O 474.2A and DOE-STD-1129-2015, the governing US standards.

## What this source does not establish

- **No measurement of anything.** This is an assessment of challenges and a recap of a workshop
  panel. It reports no experiment and no plant data.
- **It does not propose a regime.** It *"discusses the practicality of establishing a regulatory
  framework for safeguards controls"* — it does not conclude that one should exist or specify one.
- **The accuracies are not fusion-demonstrated.** They are generic tritium-handling instrument
  figures; none was obtained on an operating fusion fuel cycle, because none exists.
- **US-centric.** The regulatory analysis is DOE and NRC; it establishes that the IAEA does not
  cover tritium, but says nothing about what other national regimes require.
