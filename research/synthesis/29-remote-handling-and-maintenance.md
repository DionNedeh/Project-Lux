---
title: "Remote Handling and Maintenance"
type: synthesis
doc: 29
part: 3
aliases:
  - "Remote Handling and Maintenance"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/operations
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[23-standards-codes-liability]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[33-safety-environment-decommissioning]]"
---
# 29 — Remote Handling and Maintenance Technology

*Project Lux · Once a machine has run on tritium, no human ever goes inside it again*

---

## 1. The constraint, stated plainly

After a fusion machine has operated with deuterium-tritium fuel, its interior is:

- **Radioactive** from neutron activation of the structure
- **Contaminated** with tritium, which permeates into surfaces and adsorbs onto dust
- **Coated in activated dust** from erosion of plasma-facing components — beryllium, tungsten, carbon — which is chemically toxic as well as radiologically hazardous
- **Under vacuum**, in a geometry threaded through a superconducting magnet set

**[[jet|JET]] has not admitted a human being into its vacuum vessel in over thirty years.**

Every subsequent maintenance operation — replacing a [[divertor]] cassette, changing a blanket module, repairing a diagnostic, retrieving a dropped bolt — must be performed by machines, through ports, guided from a control room. This is not a peripheral capability. **It is the difference between a fusion plant that achieves 85% availability and one that achieves 45%**, and per [[10-economics-and-markets|Document 10]], that difference roughly doubles the cost of electricity.

---

## 2. JET: the only [[tokamak]] ever maintained fully remotely

JET is the sole existence proof that this can be done at scale, and its system is consequently the most valuable single body of experience in the field.

### The architecture

**Two articulated booms, each 12 metres long**, snake into the vacuum vessel through a port. They carry cameras, lighting, tools and end-effectors, and they must reach around a torus while supporting their own weight cantilevered from a single anchor point — a structural problem that gets harder with every metre of reach.

The primary end-effector is **MASCOT**: a **master-slave manipulator with haptic force feedback**. The operator moves a master arm in the control room; the slave arm inside the vessel reproduces the motion, and forces encountered by the slave are transmitted back to the operator's hands.

That feedback is the essential feature. **The operator feels every action** — the weight of a component being carried, the resistance of a bolt being tightened, the moment a fastener seats. Without it, remote assembly of precision components is effectively impossible; with it, a skilled operator can perform tasks approaching the dexterity of direct handling.

### The scale of a real campaign

The number that conveys what this actually means: JET's **ITER-Like Wall** installation — replacing the entire plasma-facing first wall of the vacuum vessel — required **18 months of work, two shifts a day**, performed entirely remotely.

That is the benchmark for a first-wall replacement on a machine of JET's size. A power plant with a larger vessel, higher activation, and a commercial availability requirement must do something comparable **on a routine schedule**.

### [[race-culham|RACE]]

**Remote Applications in Challenging Environments** — UKAEA's robotics and remote-handling centre at Culham Science Centre — is the institutional home of this capability. Recent upgrades to JET's Remote Handling Control Room have made the system, in UKAEA's description, one of the most advanced robotics and remote handling systems in the world.

Notably, those upgrades were made **specifically to support the JET Decommissioning and Repurposing programme** — the system built to maintain the machine is now being used to take it apart, which is itself the first full-scale demonstration of fusion decommissioning ([[33-safety-environment-decommissioning|Document 33]]).

---

## 3. [[iter|ITER]]'s approach

ITER's remote maintenance is a different architecture, because ITER's components are far heavier and its activation far higher.

**Transfer casks.** Rather than reaching into the vessel with a long boom, ITER docks a large shielded cask to a port. The cask forms a sealed, shielded volume; the port plug or component is withdrawn into it; the cask undocks and is transported on air-cushion vehicles to the **Hot Cell Facility**. The vessel is never opened to the building atmosphere.

**In-vessel systems:**
- **Blanket remote handling** — a rail-mounted vehicle deployed inside the torus to handle blanket modules weighing up to about 4.5 tonnes each, of which there are 440
- **Divertor remote handling** — cassette movers extracting the 54 divertor cassettes, each around 10 tonnes, through lower ports
- **In-vessel viewing** — deployable systems for inspection between campaigns

**The Hot Cell Facility** is where removed components are refurbished, repaired or prepared for disposal — a shielded industrial building sized to receive the largest in-vessel components, with its own remote handling systems, and one of the larger buildings on the ITER site.

---

## 4. The problems that are not solved

### 4.1 Cutting and welding irradiated material

To replace an in-vessel component you must cut it out and weld a new one in — remotely, in a confined space, on material that has been irradiated.

**Irradiated material does not weld like new material.** Helium generated by transmutation ([[09-engineering-challenges|Document 09]]) is trapped in the lattice, and on melting it comes out of solution and forms bubbles at grain boundaries — producing **helium-induced weld cracking**. Above roughly 1 appm helium, conventional fusion welding of irradiated steel becomes unreliable.

This is why DOE's roadmap carries the mid-term milestone **"qualify joining and cutting methods for irradiated materials to enable modular in-vessel replacement"**, and why no code covers it ([[23-standards-codes-liability|Document 23]]). Candidate approaches include solid-state joining (friction stir, diffusion bonding), laser welding with controlled heat input, and — most commonly in current designs — **avoiding the problem entirely** by designing joints outside the high-flux region.

### 4.2 Dexterity versus payload

There is a fundamental tension. High-payload systems (moving a 10-tonne divertor cassette) are stiff, heavy and slow. High-dexterity systems (MASCOT-class manipulation) are light and compliant. A real maintenance campaign needs both, often in the same confined space, and the transitions between them are where schedule is lost.

### 4.3 Recovery from the unexpected

Planned maintenance can be rehearsed on mock-ups. **The failures that destroy availability are the unplanned ones**: a tool that breaks inside the vessel, a fastener that shears, a component that will not release. In a machine no human can enter, every such event must be resolved by improvising with the tools already inside, or by developing a new tool and qualifying it before deployment.

JET's remote handling system was explicitly designed to be **flexible and adaptable** for exactly this reason, and that flexibility is the hardest property to specify in advance.

### 4.4 Nobody has done it at power-plant scale or cadence

JET proved feasibility on a research machine with a research schedule. A commercial plant must replace divertor cassettes roughly annually and blanket modules every few years, **on a schedule the finance depends on**, with higher activation, larger components, and a tritium inventory in the building.

**There is no operating experience for this.** DOE's roadmap accordingly asks, in the mid-term, to *"demonstrate remote handling and sensing prototypes for activated blankets/PFCs in corrosive, hazardous environments"* and to *"validate mock-up maintenance workflows and collect reliability data for predictive maintenance models."* The word *mock-up* is doing significant work in that sentence.

---

## 5. Design responses

The most interesting development is that leading designs increasingly treat remote maintenance as an **architectural driver** rather than a downstream problem.

| Approach | Concept | Rationale |
|---|---|---|
| **Demountable magnets** | **[[arc|ARC]]** (CFS) | Joints in the toroidal field coils allow the entire vacuum vessel to be lifted out and replaced as a unit, rather than repaired in situ. The most-irradiated component becomes a **consumable** |
| **Liquid first wall** | **[[general-fusion|General Fusion]]** | The wall is flowing liquid lead-lithium. It cannot be neutron-damaged and does not need replacing |
| **Vertical maintenance** | **[[eu-demo|EU DEMO]]** | Large blanket segments withdrawn vertically through upper ports as single units, rather than many small modules through equatorial ports |
| **Linear geometry** | **Realta**, **Zap**, mirrors and Z-pinches | A cylinder can be opened at the end and segments slid out. Vastly easier than working inside a torus threaded through 3D coils |
| **Modular / small unit size** | **Avalanche** (0.1 MWe), **Helion** | If a unit is small enough, replace the whole machine rather than maintaining it |

That last row is a genuine strategic divergence. **Fission learned that big plants amortise fixed costs; fusion may learn that small ones amortise maintenance.** A 100 kWe unit that is swapped out entirely and refurbished in a factory has no remote handling problem at the site at all.

**Stellarators sit at the difficult end of this spectrum.** Servicing a torus threaded through a set of non-planar 3D coils is materially harder than servicing an axisymmetric tokamak, and it is the strongest practical argument against the concept — set against its equally strong arguments of no disruptions and inherent steady state.

---

## 6. The wider robotics connection

Fusion remote handling is not an isolated discipline. It shares problems with — and increasingly borrows from — nuclear decommissioning (Sellafield, Fukushima), space robotics, subsea intervention, and surgical robotics. RACE's remit is deliberately broader than fusion for this reason.

The technologies converging on it:
- **Force-feedback teleoperation** with improved transparency and latency compensation
- **Digital twins** for offline rehearsal and collision checking before deployment — connecting directly to the simulation infrastructure in [[19-simulation-codes-nuclear-data|Document 19]]
- **Machine vision** for pose estimation in cluttered, poorly lit, radiation-degraded camera environments
- **Shared autonomy** — the robot handles the routine trajectory, the human handles the contact-rich moment
- **Radiation-hardened electronics**, or the discipline of keeping all electronics outside and running everything hydraulically or through long cable runs

---

## 7. Assessment

**JET's remote handling programme is one of fusion's most underrated assets.** It is the only operational experience anywhere of maintaining a tritium-contaminated tokamak, it produced a working answer, and the decommissioning programme running to 2040 will extend it into the end-of-life phase that every future plant must eventually reach.

**Remote maintenance is a stronger determinant of fusion economics than most plasma physics.** A plant that cannot replace a divertor in eight weeks cannot achieve the availability its business case assumes, and no amount of confinement improvement compensates for that.

**The most important design decisions in fusion may turn out to be maintenance decisions.** ARC's demountable magnets, General Fusion's liquid wall, and the linear concepts' open geometry are not incidental features — they are bets that the binding constraint on a fusion plant is not making the plasma but **getting back inside afterwards**.

---

**Continue to:** [[30-power-plant-designs-compared|30 — Power Plant Designs Compared]] · [[33-safety-environment-decommissioning|33 — Safety, Environment and Decommissioning]] · [[24-grid-integration-and-operations|24 — Grid Integration and Operations]]
