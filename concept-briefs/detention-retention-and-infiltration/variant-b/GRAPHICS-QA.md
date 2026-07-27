---
title: Graphics accuracy QA/QC
brief: owos:concept-brief:003
reviewed: 2026-07-27
method: each graphic checked against white-paper.md 0.7 and research/added-terminology-source-dossier.md
status: six defects found and corrected, two of them material
---

# Graphics accuracy QA/QC

The test applied to every graphic: **does it remain true with its caption removed, and does it
contradict anything in the white paper or the source dossier?**

Six defects. Two would have taught something false.

## Material

### 1. Hydrograph violated reservoir routing

**Found.** The outflow curve peaked at t=0.50 with a value of 0.46 while the inflow curve at that
same moment was 0.081. Outflow exceeded inflow at the outflow peak.

**Why it is wrong.** Storage rises while inflow exceeds outflow and falls once it does not. Peak
outflow therefore occurs *exactly* where the two curves cross on the inflow recession. A curve set
that peaks outflow far above the concurrent inflow describes a basin manufacturing water. Any
practitioner would catch it, and it would undermine the brief's credibility on the one measurement it
exists to correct.

**Corrected.** Outflow peak moved to t=0.40 with value 0.476, which is the inflow value at that
instant to three decimals. Volume held nearly constant. The result is a 45 percent peak reduction
carrying a 1 percent volume reduction, which is a stronger version of the original teaching point.

**Turned into instruction.** The crossing is now marked on the graphic and explained in the readout:
up to that moment more was arriving than leaving and the basin was still filling. That crossing is
not a drawing choice, it is what storage does.

### 2. Permanent pool graphic contradicted its own caption

**Found.** The caption reads "the capacity is the empty space above the water." The graphic filled
that space with translucent blue.

**Why it is wrong.** The brief exists partly to repair the belief that a full-looking pond has no
capacity. Filling the storm storage band draws the misconception.

**Corrected.** Storm storage is now an empty band with a dashed amber boundary. The water is the
permanent pool only.

## Correctness and clarity

### 3. Route diagram showed a red outlet between storms

**Found.** The interactive drove the outlet indicator from `outlet` (is flow leaving) rather than
from whether the outlet was obstructed. Between storms nothing flows, so the indicator rendered red,
which reads as blocked.

**Corrected.** `blocked` is now a separate state flag. Red appears only in the obstructed state.

### 4. Detention graphic showed a dry basin full of water with no time state

**Found.** The basin was drawn holding water with no indication of when. This is the exact defect
that disqualified the retired Variant A route comparison, which drew a dry detention basin identical
to a wet pond.

**Corrected.** The graphic now states that it shows the basin during the storm and that this basin is
dry between them.

### 5. Infiltration plant route did not close

**Found.** Plant uptake was drawn as an arrow into the soil with no return. Water taken up by
vegetation leaves the system upward as evapotranspiration, which is a genuine exit and one the white
paper defines.

**Corrected.** A dashed return path to air was added.

### 6. Overflow arrow did not start at the overflow

**Found.** The exit arrow began beside the riser rather than at the notch it leaves through, implying
the overflow discharges through the outlet structure.

**Corrected.** The path now begins at the notch and passes the riser.

## Checked and correct, no change

- **Retention.** Two panels for the two meanings, one infiltrating with no surface outlet, one a
  permanent pool with an outlet. Matches the white paper's treatment of the ambiguity.
- **Tailwater.** Low creek surface below the outlet gives free discharge; high creek surface above
  the outlet submerges it. The mechanism and both geometries are right.
- **Outlet and overflow elevations.** Ordinary release low, overflow higher.
- **Route interactive, all four states.** Water levels, active exits, creek levels, and the backflow
  indication are each consistent with the white paper.
- **No graphic carries units, axis values, or a quantity that could be read as a design figure.**
  Every one is labelled qualitative.

## Standing rule for every future brief

A graphic ships only when all four hold:

1. It stays true with the caption removed.
2. It contradicts nothing in the white paper or the source dossier.
3. Any physical relationship it draws is consistent with the governing mechanism, not merely
   plausible in shape.
4. It shows no quantity that could be mistaken for a design value, and says what it does not prove.
