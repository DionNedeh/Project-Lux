---
title: "Physics and Technology Considerations for the Deuterium–Tritium Fuel Cycle and Conditions for Tritium Fuel Self Sufficiency"
type: source
source_type: paper
file: "raw/papers/Abdou-2021-DT-fuel-cycle-tritium-self-sufficiency.pdf"
authors: "Abdou, Riva, Ying, Day, Loarte, Baylor, Humrickhouse, Fuerst & Cho (9 authors)"
publisher: "Nuclear Fusion 61 013001 (IAEA / IOP Publishing), 51 pp"
source_date: 2020-11-23
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[tritium-breeding-ratio]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[lithium-6]]"
  - "[[pellet-injection]]"
  - "[[eu-demo]]"
  - "[[iter]]"
  - "[[09-engineering-challenges]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[14-open-problems-and-risks]]"
created: 2026-10-19
updated: 2026-10-19
---
The **canonical quantitative treatment** of whether a D-T fusion plant can fuel itself. A 51-page
*Nuclear Fusion* review from nine authors across UCLA, KIT, the [[iter|ITER Organization]],
[[ornl|ORNL]], INL and NFRI Korea, built on a time-dependent fuel-cycle dynamics model covering all
components of the cycle.

Until this ingest the vault asserted the **1.05–1.15** design band on the authority of the
[[doe-fusion-science-technology-roadmap-2026|DOE roadmap]] alone. This is the primary source that
band comes from, with its reasoning attached.

> [!warning] The paper's primary conclusion is negative
> The authors state plainly that the physics and technology state-of-the-art **will not enable**
> DEMO and future power plants to satisfy the fuel-cycle requirements they set out. This is a
> review that concludes a gap, not a solution.

## The central reframing: TBR is not the binding constraint

The vault has treated tritium as a **breeding** problem. This paper's case is that breeding is
downstream of two plasma parameters and one chemical-plant parameter.

What binds is the **product of fuelling efficiency and burn fraction**, `η_f · f_b`, together with
the inner-cycle **processing time** `t_p`:

| Condition | Required TBR | Start-up inventory (3 GW) |
|---|---|---|
| ITER's estimated `f_b` = 0.36%, 100% availability | **1.82** | **>200 kg** — the paper calls this unacceptable |
| `η_f · f_b` = 1% | 1.08 | — |
| `η_f · f_b` = 2%, `t_p` = 4 h | — | **11 kg** |
| `η_f · f_b` = 5%, `t_p` = 1 h | 1.02 | **<5 kg** |

**Stated requirement: `η_f · f_b` > 2% and `t_p` of 1–4 h** for self-sufficiency with reasonable
confidence. Start-up inventory scales **linearly with fusion power** — a 100 MW facility needs
about **1 kg**.

See [[tritium-burn-fraction]] and [[tritium-start-up-inventory]].

> [!note] Independently corroborated, 2026-10-19
> [[st-e1-tritium-systems-crossref-metadata-2026|ST-E1's fuel-cycle paper]] reports **extraction
> sensitivity and fuelling efficiency as the dominant drivers of inventory performance, rather than
> marginal improvements in breeding ratio** — this paper's central reframing, reached six years later
> by a company design team using inventory modelling of a liquid-lithium blanket, with no shared
> authorship. Read from an abstract only, and carrying no figures, so it corroborates the *ordering*
> of the parameters and not their values.

## The achievability bands

The paper's own confidence framing, which the vault now adopts with attribution:

- **Unlikely** if required TBR > **1.15**
- **Possible** if **1.05 < TBR ≤ 1.15**
- **Attained with high confidence** if TBR ≤ **1.05**

Against this, the **maximum achievable** TBR for the most detailed blanket system designs available
is estimated at **1.15**, with high confidence only at **1.05**. The achievable range is given as
**1.05–1.15** — so the requirement and the capability occupy the same interval, and the working
margin is **10%**.

> [!warning] A measured reason to distrust calculated TBR
> A series of integral blanket-neutronics experiments found calculation **overestimated** the
> tritium production rate by an **average factor of 1.14**, against a 5% measurement uncertainty.
> The authors call the overestimation *"alarming"* and a safety factor of **>1.1 to 1.2** on
> calculated TBR was recommended. This is a sharper, sourced statement of the warning already on
> [[tritium-breeding-ratio]].

## Availability is a tritium parameter

The finding the authors themselves flag as significant, and the one with the widest consequences
for this vault's coverage of near-term devices:

| Availability factor | Self-sufficiency |
|---|---|
| AF < 10% | **Impossible** for any `η_f · f_b` |
| AF > 30%, `1% ≤ η_f · f_b ≤ 2%` | Possible |
| AF > 50%, `η_f · f_b` > 2% | Achievable with reasonable confidence |

This bears directly on the near-term facilities the vault treats as the path to a blanket
demonstration — FNSF, VNS and CTF are all predicted **below 30%**. See [[availability]].

**Reserve inventory.** A reserve time of **24 h** leads to unacceptable reserve and start-up
inventories. The conclusion is that reserves must cover only **a few hours**, which converts the
problem into one of reliability and fast maintainability rather than storage.

## Direct internal recycling

The paper credits the **[[eu-demo|EU-DEMO]] direct internal recycling concept** — routing plasma
exhaust straight to fuelling without passing the isotope separation system — with reducing overall
processing time and inventories, and with a positive effect on required TBR. At `η_f · f_b` = 1%,
recycling **80%** of exhaust directly lowers required TBR from **1.120 to 1.075**. See
[[direct-internal-recycling]].

## R&D gaps the paper names

- Cutting processing time, including **batch to continuous** tritium technology
- Raising `η_f · f_b` toward 5%; high-field-side [[pellet-injection|pellet injection]] is the
  favoured route, but sustained high-speed injection has been demonstrated only at **1 Hz,
  short-pulse** capability
- Separate D and T transport in core and pedestal, and the inward DT pinch
- A **fusion nuclear science facility** sized to accumulate surplus tritium for DEMO start-up

## Access limitations

**Inspected in full.** The 51-page published version was captured to `raw/` from IOP and extracted
to `raw/extracts/`; all figures recorded above were read from that extract, not from a secondary
summary. Bibliographic record verified against the article's own first page: *Nucl. Fusion* **61**
(2021) 013001, DOI `10.1088/1741-4326/abbf35`, © 2020 IAEA Vienna.

**Licence not confirmed.** IOP labels the article a *"Free article"* and serves the PDF without
paywall, but states no open-access licence, and the PDF carries a per-article price line. Recorded
here as **free to read at the publisher**, not as CC-licensed.

> [!note] Two bibliographic traps in this record
> **One paper, not two.** Web search results in this session reported "Abdou 2021" and
> "Nucl. Fusion 61 013001" as *different* papers — a 2021 review and a separate 2020 time-dependent
> model. The article's own first page settles it: they are the **same paper**, published online
> 23 November 2020 in the January 2021 issue. The `source_date` above is the online date.
>
> **A 1986 predecessor exists.** Abdou *et al.*, *Deuterium–Tritium Fuel Self-Sufficiency in Fusion
> Reactors* (1986), reached a compatible conclusion about restricted parameter space. It is **not
> held in `raw/`** and nothing on this page derives from it.

## What this source does not establish

- **No measured plant fuel cycle.** Every figure is model output or a design requirement. No D-T
  plant has ever closed its fuel cycle; this paper does not change that.
- **The loss assumption is weak by the authors' own account.** Environmental tritium losses are set
  to **10⁻⁴** — and the paper says *arbitrarily*. Five components, including the blanket and
  plasma-facing components, are assigned **zero** direct environmental loss on the grounds that they
  sit inside the vacuum vessel. Published critiques of this paper attack the loss assumption; a
  figure of **0.1%** circulates in that commentary and is **not** the paper's value, which is
  ten times smaller. The vault records the paper's own figure and does not endorse the critique.
- **Burning-plasma predictions are self-declared unreliable.** The authors state that the maximum
  achievable burn fraction in ITER *"remain[s] uncertain"*, that ITER fuelling estimates
  *"cannot be fully validated"* for lack of burning-plasma experiments, and that pellet fuelling
  efficiency at shallow penetration is *"highly uncertain"* and possibly optimistic.
- **Schedules in it are stale.** The authors note that ITER and FNSF start-date results were
  calculated years earlier and the schedules have since slipped. Anything date-dependent here is
  read as of **2020**, not 2026.
