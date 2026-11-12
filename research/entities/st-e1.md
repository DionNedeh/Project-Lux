---
title: "ST-E1"
type: entity
entity_type: machine
country: "United Kingdom"
status_detail: planned
major_radius_m_approx: 5
net_electric_mwe_approx: 400
tags:
  - fusion/entity
  - fusion/machines
  - fusion/designs
status: stable
confidence: high
sources:
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
related:
  - "[[tokamak-energy]]"
  - "[[st40]]"
  - "[[step]]"
  - "[[spherical-tokamak]]"
  - "[[declared-tbr-values]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-accountancy]]"
  - "[[tritium-doubling-time]]"
  - "[[tritium-retention]]"
  - "[[lithium-6]]"
  - "[[availability]]"
  - "[[q-gain-definitions]]"
  - "[[rafm-steel]]"
  - "[[vanadium-alloys]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-10-19
updated: 2026-11-02
---
[[tokamak-energy|Tokamak Energy]]'s **pre-concept** [[spherical-tokamak|low-aspect-ratio]] power
plant, successor to [[st40|ST40]], and a [[us-doe|DOE]] milestone-programme design. An 11-paper
Focus Collection headed by [[willis-2026-st-e1-pre-concept-design-overview|Willis *et al.* 2026]].

**Its organising idea is financial.** **Phased operation** — pilot, upgrade, commercial — with
**permanent assets** (magnet cage, vessel, cryostat, civil works) built to commercial spec from the
outset and **in-vessel systems replaceable** every 5 full-power years. The first design in
[[30-power-plant-designs-compared|Document 30]] organised commercially rather than physically.

## Reference design point

| Parameter | Pilot | Commercial |
|---|---|---|
| R₀ · A · B₀ | 5.0 m · 2.3 · 5.25 T | — |
| I_p | 15 MA | — |
| P_fus,nom | **1500 MW** | **2000–2500 MW** |
| P_aux,nom | 75 MW | 25–50 MW |
| `Q_sci` *(derived)* | **20** | **50–70** |
| P_elec,net | **300–500 MWe** | **800–1000 MWe** |
| Neutron wall loading | < 1.6 MW m⁻² | 2.1–2.6 |
| TBR · TF life · maintenance | > 1.14 · > 30 FPY · radial | — |

Mission targets: CapEx **$12–14k/kW**, **[[availability]] > 80%**.

> [!warning] The source writes `Q` unqualified
> Table 1 gives "Q (–)" with no subscript; 1500/75 = 20 makes it **`Q_sci`** — **this vault's
> derivation, not the source's label** ([[q-gain-definitions]]).

## What distinguishes it

- **Breeds on pure, unenriched lithium** — liquid, helium-cooled, integral extraction loop. The
  only such route here ([[lithium-6]]), and **now evidenced**: 086004 selects natural lithium.
- **[[vanadium-alloys|V-4Cr-4Ti]], not [[rafm-steel|RAFM steel]]**, for the centre-column shield
  box — though F82H and 316L(N)-IG appear elsewhere.
- **Shielding, not breeding, drives the design**, modelled in the in-house Geant4 code
  **G4Tokamak** ([[19-simulation-codes-nuclear-data]]).
- **Not pulsed**: a 5-minute ramp capping grid draw at 500 MW needs **1–2 MWh** storage.

> [!warning] CORRECTION 2026-11-02 — the "> 30 FPY" above is an intent, not a result
> [[st-e1-neutronics-crossref-metadata-2026|086003]] gives peak HTS fast flux **9.5 × 10⁹** against
> its own **< 4 × 10⁹** limit — **2.4× over**, for an estimated **13 fpy**. A 2400 MW variant at
> A = 2.31 recovers ~25 fpy. See [[18-superconductors-and-magnets]].

## Fuel cycle

**1.58 kg** start-up inventory, **152-day** [[tritium-doubling-time|doubling time]], 1.39 kg
holdup, 2.6–2.9% [[tritium-burn-fraction|burn fraction]], [[direct-internal-recycling|DIR]] 0.7, no
trapping physics ([[tritium-retention]]). Full table:
[[28-vacuum-wall-conditioning-tritium-plant|Document 28 §6]].

## Recorded disagreements

**TBR** — **RESOLVED**: three figures, one sensitivity table ([[declared-tbr-values]]). A new
tension replaces it: 086003 gives 1.169–1.194, above 086004's 1.146 baseline.
**Availability** — **37.5% / > 80% / 100%** across three sources ([[availability]]).
**Net electric** — resolves as **phasing**, with a residual gap to the 2023 figure.

## Evidence limits

Nothing is built or measured. **Eight of ten companion papers remain uncaptured**, and **nobody can
account for tritium in a liquid-lithium breeder** ([[tritium-accountancy]]).

---

**Changed 2026-10-19.** Upgraded from draft; net electric corrected to **phased**.
**Changed 2026-11-02.** 086003 and 086004 read in full: magnet life corrected to **13 fpy
estimated**, TBR conflict resolved, lithium claim evidenced, fuel-cycle figures added.
