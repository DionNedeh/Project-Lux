---
title: "Direct Internal Recycling (DIR)"
type: concept
domain: engineering
symbol: "DIR"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
sources:
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[doe-fusion-science-technology-roadmap-2026]]"
related:
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-breeding-ratio]]"
  - "[[eu-demo]]"
  - "[[availability]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[09-engineering-challenges]]"
created: 2026-10-19
updated: 2026-11-02
---
Routing most of the plasma exhaust **straight back to the fuelling system**, bypassing the isotope
separation system altogether. An [[eu-demo|EU-DEMO]] concept, and the cheapest available reduction in
a plant's [[tritium-start-up-inventory|tritium inventory]].

## The logic

Few per cent of fuelled tritium burns ([[tritium-burn-fraction]]). The rest returns to the
exhaust essentially as it went in — a hydrogen-isotope mixture whose composition is close to what the
fuelling system wants anyway.

Full isotope separation by cryogenic distillation is slow, and the
**isotope separation system dominates the inner cycle's processing time**. Every hour spent in a
distillation column is tritium sitting in holdup: capital locked up at $30,000–35,000/gram, decaying
at 5.5% per year, and appearing in the plant's safety case as potential release.

DIR's claim is that most of that exhaust never needed separating.

## The quantified effect

From [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]], which credits the
EU-DEMO concept explicitly: at `η_f · f_b` = 1%, recycling **80% of exhaust directly** lowers the
required [[tritium-breeding-ratio|TBR]] from **1.120 to 1.075**.

That is a 0.045 reduction in required TBR bought with plumbing rather than neutronics — and it moves
the requirement from the middle of Abdou's *possible* band toward his *high-confidence* band
(≤1.05). Against a working margin of only 10%, that is a significant purchase.

The mechanism is simple: shorter processing means less tritium in holdup, so a smaller start-up and
reserve inventory, so less surplus the blanket must breed.

## Status

**A concept with roadmap backing, not a demonstrated system.** DIR is a
[[doe-fusion-science-technology-roadmap-2026|DOE roadmap]] milestone, and the frontier in tritium
processing is **inventory reduction rather than throughput**
([[28-vacuum-wall-conditioning-tritium-plant|Document 28 §6]]).

Two cautions belong on the record:

- **No integrated fuel cycle has ever run**, with or without DIR. The 80%/1.075 figure is model
  output from a system-level dynamics code.
- **Two further designs make DIR a requirement, not an option.**
  [[st-e1-tritium-systems-crossref-metadata-2026|ST-E1]] specifies a DIR fraction of **0.7**, with
  protium at **1 at% in / 0.8 at% out**, and [[meschini-2023-tritium-fuel-cycle-arc-step|Meschini
  *et al.* 2023]] name DIR as one of three conditions for self-sufficiency in [[arc|ARC]]- and
  [[step|STEP]]-class plants.
- **The sensitivity is not uniform.** Helios's own study found DIR fraction among the parameters
  that **barely move** system dynamics, against availability, doubling time and burn fraction which
  dominate ([[overview-of-the-helios-design]]). Not flatly contradictory — different designs at
  different operating points — but the vault records both, and DIR's benefit should not be assumed
  design-independent.
