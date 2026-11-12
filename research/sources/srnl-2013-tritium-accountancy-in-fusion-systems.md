---
title: "Tritium Accountancy in Fusion Systems"
type: source
source_type: paper
file: "raw/papers/SRNL-2013-tritium-accountancy-in-fusion-systems.pdf"
authors: "Klein, Clark, Harvel, Farmer, Moore, Tovo & Poore (7 authors, Savannah River National Laboratory)"
publisher: "SRNL-STI-2013-00384; published as Fusion Science and Technology 67:2, 420–423, DOI 10.13182/FST14-T44"
source_date: 2013
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/security
status: stable
confidence: high
related:
  - "[[tritium-accountancy]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[11-policy-regulation-safety]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[37-military-dual-use-security]]"
created: 2026-10-19
updated: 2026-10-19
---
**The framework paper.** A five-page Savannah River National Laboratory conference paper setting out
how nuclear material accountancy is actually constructed, and why a continuously operating fusion
fuel cycle breaks it. Until this ingest the vault asserted that accountancy is *"genuinely hard
because tritium permeates through hot metal"* ([[11-policy-regulation-safety]] §5) without holding
anything that explained the mechanism.

## The accountancy structure

| Term | Meaning |
|---|---|
| **MBA** — Material Balance Area | The boundary of the accountancy structure; everything entering or leaving is measured and accounted |
| **MSA** — Material Sub-Account | Subdivisions of an MBA, used to localise and minimise inventory differences between process operations |
| **KMP** — Key Measurement Point | Where material crossing an MSA boundary is measured |
| **PI / PIT** — Physical Inventory / Inventory Taking | The periodic measurement of how much tritium is where |

A **single MBA structure** is stated to be adequate and more cost-effective when only tracking
tritium transfers, decay and breeding — multiple structures being needed for custodianship of
special nuclear material, which tritium is not.

## The equations, and where fusion breaks them

**Inventory difference**, the quantity accountancy exists to compute:

```
ID = SI + R − S − EI                               (Eq. 1)
```

`SI` starting inventory · `R` receipts · `S` shipments · `EI` ending physical inventory. Its
statistical uncertainty, the **Limit of Error on Inventory Difference (LEID)**, sums the variances:

```
σ²_ID = σ²_SI + σ²_R + σ²_S + σ²_EI                (Eq. 2)
```

> [!warning] Equation 1 assumes the plant can stop, and a power plant cannot
> The paper's central objection: Eq. 1 *"is implicit"* in requiring that tritium flow **stop long
> enough for physical inventory measurements** to be taken. *"Continuous running of the fusion device
> does not allow the tritium process to be stopped to perform tritium PI measurements."*
>
> Worse, the uncertainty on a continuously measured flow **grows with time**:
> ```
> σ(continuous flow measurements) ∝ √t             (Eq. 3)
> ```
> So for a continuously operating fuel cycle the receipt and shipment uncertainties *"will eventually
> grow with time to the point where the uncertainty in these terms will dominate"* the inventory
> terms — and the inventory difference stops meaning anything.
>
> **The stated remedy is to enlarge the MSA boundary** until flows can be physically measured with
> low enough uncertainty. That is an admission: accountancy resolution is traded away to keep the
> arithmetic valid.

## The fusion-modified balance

Fusion adds a source (breeding), a sink (burn-up) and a holdup (retention) that classical
accountancy has no terms for. The paper proposes a **net** quantity:

```
NET = ID + BU = SI + (IN + BR) − (LOSS + OUT) − EI (Eq. 5)
```

`BU` burn-up · `BR` breeding · `LOSS` process losses · `OUT` flows out.

> [!warning] Retention is not measured — it is whatever is left over
> The paper states the assumption plainly: *"all tritium that is not measured or accounted for in the
> other terms of the equation resides in the FC [fusion chamber]."*
>
> So in-vessel retained tritium — the inventory that permeates into walls, dust and coolant — enters
> the books as a **residual**, not a measurement. Every error elsewhere in the balance lands on it.
> This is the precise mechanism behind the vault's existing claim that fusion accountancy is harder
> than for solid fissile material.

Decay is handled in the receipt and shipment terms by escalating each transfer to the start of the
inventory period, then decaying the total to match the ending inventory.

## Access limitations

**Inspected in full.** The five-page report was captured to `raw/` from `sti.srs.gov` and extracted;
all equations and quotations above were read from that extract. Prepared under DOE contract
DE-AC09-08SR22470.

**The report, not the journal version.** This is **SRNL-STI-2013-00384**, the laboratory report. It
was published as Klein *et al.*, *Fusion Science and Technology* **67**:2, 420–423, DOI
10.13182/FST14-T44 — identified from the reference list of
[[sindelar-2023-tritium-accountancy-control-challenges-fusion|Sindelar *et al.* 2023]], which cites
it as reference 7. **The published version was not inspected or compared against this capture.**

## What this source does not establish

- **It is dated 2013.** Thirteen years old at ingest, and it predates every private fusion pilot
  plant design in this vault. Its framework is structural rather than technological, so it ages
  better than a figure would — but nothing here reflects current practice or current instruments.
- **No measurement accuracies.** The paper refers to PI measurement techniques and their
  uncertainties but tabulates none; for those see
  [[sindelar-2023-tritium-accountancy-control-challenges-fusion]].
- **No regulatory position.** It notes that tritium is not a special nuclear material and that
  NMC&A requirements therefore come from national rather than IAEA authority, but does not set out
  what any regime requires.
- **Nothing measured in a fusion plant.** No D-T power plant has operated a fuel cycle, so the
  continuous-flow problem described here has never been encountered in practice — it is derived from
  the structure of the equations, not from an operating record.
