---
title: "Multiscale Assessment of Tritium Behavior in Preliminary Fusion Pilot Plant Design Using Surrogate Models in TMAP8"
type: source
source_type: paper
file: "raw/papers/Yang-2026-ST-E1-tritium-TMAP8-surrogate-models.pdf"
authors: "Yang, Simon, Yildirim, Trueba, Robinson & Shimada (6 authors)"
publisher: "arXiv:2604.19647v1 (preprint; submitted to Nuclear Fusion, not peer-reviewed), 10 pp"
source_date: 2026-04-21
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/engineering
  - fusion/computation
status: stable
confidence: medium
related:
  - "[[st-e1]]"
  - "[[tokamak-energy]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[availability]]"
  - "[[tungsten-pfc]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-10-19
updated: 2026-10-19
---
A multiscale tritium-transport study of **[[st-e1|ST-E1]]**, [[tokamak-energy|Tokamak Energy]]'s
preliminary fusion pilot plant, coupling component-level 1D models of plasma-facing components to a
17-subsystem fuel-cycle model inside **TMAP8**, with Gaussian-process surrogates standing in for the
expensive component simulations. Authors are from INL and Tokamak Energy; the plant design sits
under the [[us-doe|DOE]] milestone programme.

> [!warning] This is an unreviewed preprint, and its confidence is set accordingly
> arXiv v1, submitted to *Nuclear Fusion*, **not peer-reviewed**. It also contains internal
> numerical inconsistencies visible in the paper itself (recorded below). It is ingested because it
> is the only ST-E1 fuel-cycle modelling in reach, and a labelled weak source is worth more than a
> silent gap — but nothing in this vault should rest on it alone.

## What it is, and is not, about

**It computes no TBR and no self-sufficiency result.** The breeding ratio is an *input*. What the
paper produces is tritium **retention and recovery** behaviour in components, and the effect of
feeding surrogate-derived residence times into a system-level cycle model.

The paper also notes ST-E1 is **not intended to supply tritium to further plants**, which removes
the doubling-time pressure that drives much of
[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou's]] analysis.

## The declared inputs

From Table 6, attributed to Tokamak Energy — **all of these are inputs, none are findings**:

| Parameter | Value |
|---|---|
| Tritium breeding ratio | **1.113** |
| Tritium burn efficiency (TBE) | **0.02** |
| Availability factor | **0.375** |
| Tritium burn rate | **2.7938 × 10⁻⁶ kg/s** |
| Tritium decay rate | 1.78 × 10⁻⁹ s⁻¹ |
| Non-radioactive losses `ε_i` | per-component, **1.62 × 10⁻⁸ to 3.33 × 10⁻⁷**; zero for all others |

The input TBR of 1.113 sits inside Abdou's **possible** band (1.05–1.15), not the high-confidence
band.

> [!warning] TBE is tabulated but never defined
> The paper gives **TBE = 0.02** in Table 6 and defines the term nowhere in its text. Whether this
> denotes Abdou's *product* `η_f · f_b` or the burn fraction `f_b` alone **cannot be determined from
> this source**. The difference decides whether ST-E1's assumption sits exactly on Abdou's 2% floor
> or at roughly a quarter of it. The vault records the ambiguity rather than the favourable reading.
> This is the [[q-gain-definitions|unqualified-symbol error class]] in a new place.

*Vault derivation, not a paper figure:* the stated burn rate over a year at the stated availability
gives roughly **33 kg of tritium per year** (88 kg/yr at continuous duty × 0.375). Recorded as
arithmetic on the paper's inputs, for scale against the 30–40 kg world inventory on
[[tritium-breeding-ratio]].

## Components and materials

| Component | Armour | Pipe |
|---|---|---|
| Divertor | 3 or 8 mm W | 1 mm V44 or 1 mm W |
| Centre-column first wall | 5 mm W | 5 mm V44 |
| Blanket first wall | 5 mm W | 2.5 or 5 mm V44 |
| Vacuum vessel | none | 50 mm stainless steel |

**V44 is V-4Cr-4Ti**, a vanadium alloy — notable because the vault's structural-materials coverage
is [[rafm-steel|RAFM steel]] and [[tungsten-pfc|tungsten]]. Only the divertor and the two first-wall
components use surrogate-derived residence times; the remaining 14 subsystems use baseline values.

## Results

- **Component inventories saturate** after roughly 10,000 s, reaching quasi-steady state before the
  modelled 50 pulses complete (50 pulses × 600 s injection + 1,000 s dwell, 80,000 s total).
- **Thinner armour lowers retention but raises coolant-side losses** — a design trade the paper
  surfaces without resolving.
- **Bake-out works, on these assumptions.** Heating the 8 mm W armour / 1 mm W pipe divertor case to
  873 K releases **over 95% of retained tritium in about 33 h** (30 h ramp, 170 h hold), with
  chamber pressure reaching a minimum of 1.93 × 10⁻³ Pa.
- **Surrogate accuracy is strongly asymmetric.** Steady-state flux is predicted well — best RMSPE
  **1.60%** for the W-pipe case, **9.92%** for V44. Residence times are predicted poorly:
  **8.35% / 13.68%** (W pipe) and **23.90% / 31.26%** (V44) for `τ₀` and `τ₁`. Residence time is
  precisely the quantity fed into the system model.

## Internal inconsistencies preserved

Three, all visible within the paper:

1. **Cost reduction.** §3.1 claims an *"order-of-magnitude"* lower computational cost; the
   discussion states a factor of **2.7 × 10⁻⁶**. These differ by five orders of magnitude and the
   paper does not reconcile them. No wall-clock timings are given.
2. **Residence-time uncertainty.** The discussion cites **33.58% and 50.57%**; the results section
   gives **23.90% and 31.26%** for the same quantities.
3. **Bake-out temperatures.** Table 1 lists 873 K for the V44-pipe divertor and 673 K for the
   W-pipe divertor; the body text gives the reverse. **The authors flag this one themselves.**

Additionally, **up to 20% of training simulations were discarded** for numerical instability or for
fits exceeding the 80,000 s window — a selection effect on the surrogate training set that the paper
notes but does not quantify the consequences of.

## Access limitations

**Inspected in full**, with a caveat about route. The arXiv v1 PDF was captured to `raw/` and
extracted to `raw/extracts/`; all figures above were read from that extract. A first attempt to read
the PDF over the web returned compressed binary and recovered nothing — the local extraction is the
path that worked, and the earlier failure is recorded here so it is not mistaken for absence.

**No version of record exists yet.** The paper is submitted to *Nuclear Fusion* and unpublished as
of 2026-10-19. If it is accepted, the published version must be compared against this capture.

**Not inspected:** Tokamak Energy's own ST-E1 design documentation, cited as Ref. [25] and the source
of every input in Table 6. The vault therefore holds ST-E1's fuel-cycle parameters only at second
hand.

> [!warning] Updated 2026-10-19 — the authoritative design paper is now held, and it does not match
> [[willis-2026-st-e1-pre-concept-design-overview|Willis *et al.* 2026]] was captured after this
> page was written. Two of this preprint's inputs disagree with it:
>
> | Quantity | This preprint | Willis *et al.* |
> |---|---|---|
> | TBR | 1.113 | **> 1.14** (RDP table); **~1.1** (prose) |
> | Availability factor | 0.375 | **> 80%** (mission target) |
>
> Neither disagreement is explained by any source. The availability gap matters because 37.5% and
> 80% fall either side of Abdou's 50% self-sufficiency threshold, so the two papers imply different
> conclusions about the same plant. A plausible reconciliation is that this preprint models an early
> or pilot-phase operating point — **but no source states that, and the vault does not assume it.**
> Recorded under *Known conflicts* in [[index]].

## What this source does not establish

- **Nothing about whether ST-E1 achieves tritium self-sufficiency.** TBR is an input; the paper
  frames low-inventory self-sufficient operation as future work.
- **Nothing measured.** No ST-E1 hardware exists. This is simulation of a preliminary design, using
  literature material properties with **no uncertainty quantification**.
- **Retention is deliberately overestimated.** The authors state peak tritium fluxes are conservative
  and likely too high because **re-emission is excluded**, coolant-side tritium concentration and
  surface partial pressure are both fixed at zero, and geometry is **1D only**.
- **Trapping physics is simplified.** A **single intrinsic trap** per material is modelled where real
  materials have several; irradiation damage, dynamic trapping, isotopic competition and mixed D–T
  surface effects are all excluded. Irradiation damage is the omission that matters most for a
  neutron-loaded first wall.
