---
title: "EU DEMO"
type: entity
entity_type: machine
country: "European Union"
status_detail: planned
operator: "[[eurofusion]]"
major_radius_m_approx: 9
net_electric_mwe_approx: 500
tags:
  - fusion/entity
  - fusion/machines
status: stable
confidence: high
sources:
  - "[[maturation-of-critical-technologies-demo-balance-of-plant]]"
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[gonzalez-de-vicente-2022-fusion-waste]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
related:
  - "[[iter]]"
  - "[[thermal-storage-pulsed-operation]]"
  - "[[tritium-breeding-ratio]]"
  - "[[direct-internal-recycling]]"
  - "[[tritium-start-up-inventory]]"
  - "[[balance-of-plant]]"
  - "[[primary-heat-transfer-system]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-08-26
updated: 2026-10-19
---
Europe's demonstration power plant — **the most conservative major design, deliberately**.

The European strategy has been to let [[iter]] retire the physics risk and then build a machine that **requires no new physics**. DEMO is consequently large (major radius around 9 m), operates in conventional ELMy [[h-mode]], uses a **pulsed** inductive scenario with [[thermal-storage-pulsed-operation|thermal storage]], and targets roughly **2 GW fusion for ~500 MWe net**.

It must do three things ITER does not: **breed its own tritium**, deliver **net electricity to the grid**, and achieve **utility-grade [[availability]]**.

EU-DEMO is also the origin of **[[direct-internal-recycling|direct internal recycling]]**, credited
with cutting processing time and inventory and with lowering required
[[tritium-breeding-ratio|TBR]] from 1.120 to 1.075 at `η_f · f_b` = 1%
([[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]) — the corpus's clearest case of a
**plumbing** decision buying breeding margin.

Two blanket concepts have been carried in parallel: **HCPB** (helium-cooled pebble bed, beryllium multiplier) and **[[lithium-lead-eutectic|WCLL]]** (water-cooled lithium-lead).

## The balance of plant it implies

Carrying two blankets means carrying two [[balance-of-plant|balance-of-plant]] designs, and the pre-concept phase settled a reference for each: **WCLL takes direct coupling with a small molten-salt store**, **HCPB takes indirect coupling** with a store large enough that the turbine never notices the dwell ([[maturation-of-critical-technologies-demo-balance-of-plant]]).

The plant-level consequence is scale. DEMO needs **8 separated primary coolant systems under WCLL and 14 under HCPB**, with 10 and 14 primary heat exchangers or steam generators respectively — against **one** primary circuit and four steam generators in a European Pressurized Reactor running at 4,300 MWth to DEMO's ~2,300 ([[primary-heat-transfer-system]]). Conservatism on the physics side has not bought simplicity on the plant side.

## The critique

Conservatism makes it large; large makes it expensive. The design has been re-baselined repeatedly and construction start has slipped with ITER's schedule. [[eurofusion]]'s roadmap targets DEMO construction in the 2030s and **fusion electricity on the European grid by 2050**.


**Waste inventory.** DEMO could generate **as much as 10,000 t of solid waste from in-vessel
components alone** — roughly four times the ILW, HLW and spent-fuel total of a European
sodium-cooled fast reactor — per [[gonzalez-de-vicente-2022-fusion-waste]]. The figure is a conceptual-design upper bound, not
a measured inventory. See [[43-fusion-waste-classification-and-disposal]].
