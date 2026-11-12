---
title: "Recirculating Power"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/economics
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
related:
  - "[[q-gain-definitions]]"
  - "[[direct-energy-conversion]]"
  - "[[gyrotron]]"
  - "[[balance-of-plant]]"
  - "[[helios]]"
  - "[[stellarator]]"
  - "[[10-economics-and-markets]]"
  - "[[24-grid-integration-and-operations]]"
created: 2026-08-26
updated: 2026-09-12
---
The electricity a fusion plant consumes to run itself, subtracted from gross output. **The reason Q_sci and Q_eng diverge so sharply.**

## The load list

- **Cryoplant** for the magnets. Removing heat at 4.5 K costs **250–1,000 W of room-temperature power per watt removed**
- **Plasma heating and current drive** — tens to >100 MW at 30–50% wall-plug efficiency. Usually the dominant term
- **Coolant pumping** — severe for helium, and for liquid metals against MHD drag
- **Tritium plant, vacuum systems, controls**

For a tokamak, plausible recirculating fractions are **20–40% of gross output**.

## The consequence

**Q_eng > 1 typically requires Q_sci in the 10–30+ range.** This is why scientific breakeven at Q_sci = 1, while a genuine milestone, is a long way from a generator — and why [[q-gain-definitions]] insists on saying which Q.

It is also a direct argument for HTS at 20 K rather than LTS at 4.5 K, which cuts the Carnot penalty by roughly 4–5×, and for [[direct-energy-conversion]], which removes the thermal cycle altogether.

## The stellarator claim, quantified

The [[stellarator|stellarator]] case has always rested partly on low recirculating power: no driven
plasma current, no current-drive load, inherently steady-state. [[helios|Helios]] puts numbers to it
([[overview-of-the-helios-design]]) — **69.8 MW** of **459.9 MWe** generated, roughly **15%**, against
the **20–40%** above. The dominant tokamak term is simply absent: once ignited it needs under 1 MW of
heating, against tens to >100 MW of current drive.

Its Sankey diagram itemises the self-consumption, which is rarer in published designs than it should
be:

| Load | Value |
|---|---|
| Generated electric | 459.9 MW |
| Recirculating pumps | 21.8 MW |
| Gross cycle electric | 438.1 MW |
| Maintenance and operations | 20.0 MW |
| Tritium plant | 15.0 MW |
| Cryoplant | 10.5 MW |
| ECRH | 2.5 MW |
| **Net plant electric** | **390.1 MW** |

The four auxiliary loads total exactly the 48 MW the text quotes, so ECRH sits inside that figure
rather than beside it. Note what the itemisation shows: **no single dominant term**. In a tokamak,
current drive alone would exceed this entire list.

> [!warning] A design projection
> Helios is preconceptual; every figure above is modelled. The values come from the Sankey image, not
> the text layer of the paper.
