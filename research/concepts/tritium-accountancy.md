---
title: "Tritium Accountancy"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/subsystems
  - fusion/security
status: stable
confidence: high
sources:
  - "[[srnl-2013-tritium-accountancy-in-fusion-systems]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[thalia-hera-ukaea-tritium-accountancy-2026]]"
  - "[[marsteller-2025-t2apir-first-results]]"
related:
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[librti]]"
  - "[[ukaea]]"
  - "[[iter]]"
  - "[[us-nrc]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[11-policy-regulation-safety]]"
  - "[[37-military-dual-use-security]]"
created: 2026-10-19
updated: 2026-11-02
---
Knowing where every gram of tritium is, to a defensible uncertainty, in a system that leaks by
design — the part of the fuel cycle whose instruments do not yet exist.

## The structure

A facility is divided into a **Material Balance Area** whose boundary is fully measured, subdivided
into **Material Sub-Accounts** with **Key Measurement Points**. Each period an inventory is taken
and the books closed by the **inventory difference**:

```
ID = SI + R − S − EI        σ²_ID = σ²_SI + σ²_R + σ²_S + σ²_EI
```

That uncertainty is the **Limit of Error on Inventory Difference**, which decides whether the
result means anything ([[srnl-2013-tritium-accountancy-in-fusion-systems]]).

## Why fusion breaks it

Three structural failures.

1. **The plant cannot stop.** Eq. 1 assumes flow halts long enough to measure, and uncertainty on a
   continuously measured flow **grows as √t**, so receipt and shipment terms eventually **dominate**
   the inventory terms. The stated remedy — enlarge the MSA — buys validity by surrendering
   resolution.
2. **[[tritium-retention|Retention]] is a residual, not a measurement.** The balance assumes *all
   tritium not accounted for elsewhere resides in the fusion chamber*, so **every error lands on
   the retained inventory.**
3. **The fusion-specific terms have no instrument.** Methods for consumption in the plasma and
   production in the blanket *"would need to be developed"*
   ([[sindelar-2023-tritium-accountancy-control-challenges-fusion]]).

## What can be measured, and by whom

Laser Raman is most accurate at **< 0.5%**, calorimetry ~1%, environmental releases ~10% —
**figures from 2006**. UKAEA's **HERA** and **THALIA** are building the missing instruments at
**low TRL**. Detail: [[28-vacuum-wall-conditioning-tritium-plant]] §7.

## A method for continuous operation

[[flynn-larsen-2022-kalman-filters-tritium-accountancy|Flynn and Larsen 2022]] apply a **Kalman
Filter** — the first such application — taking simulated sensor error from **64.37%** to
**≈ 0.001%** in three days, inside the **1% standard**.

> [!warning] It fails on exactly the error real sensors make
> Given accumulating bias the filter tracks the sensor's mean, not the true value — and the authors
> name vibration, ground loops and RF components as sources of precisely that. **Simulated sensors
> throughout.**

## No regime requires it

Tritium was a special nuclear material to the [[us-doe|DOE]] **until 2011**; **neither the
[[us-nrc|NRC]] nor the IAEA treats it as one**, so **neither prescribes any requirement** — yet the
**10–20% breeding surplus is the only divertible stock a plant makes**
([[37-military-dual-use-security]]).

## Status

**Never performed on a fusion power plant**, because none exists. [[iter|ITER]]'s in-process
inventory is expected at ~**1 kg** — not the same quantity as
[[tritium-start-up-inventory|start-up inventory]].
