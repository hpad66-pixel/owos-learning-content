# Book I. The connected story of I&I Intelligence

## 1. Start with the rain, not the software

Imagine a rainstorm moving across one sanitary-sewer basin. Rain lands on roofs, streets, yards,
canals, and soil. Most of that water should remain outside the sanitary sewer. Some of it does not.
Water may enter rapidly through a direct connection, slowly through a cracked pipe surrounded by
wet soil, or persistently through a defect exposed to groundwater. The sewer does not label these
gallons when they arrive. A flow meter only records the combined flow passing the meter.

That is the first reason I&I analysis exists. The utility does not begin with a clean measurement
called infiltration or inflow. It begins with combined observations and must separate the story
carefully. Ordinary wastewater is still being generated. Groundwater may already be entering the
system. Rainfall adds a time-varying response. Upstream stations, control settings, pump
availability, and storage affect what the receiving station experiences.

The application therefore cannot begin with a red dashboard tile. It must begin with a declared
question and boundary. Which basin is being studied? Which event? Which meters? Which rainfall
record? Which station receives the flow? Which pump configuration is available? What decision is
the analysis expected to support?

Once those questions are answered, the system can build a chain that a person can inspect:

```text
physical event
  -> observation
  -> accepted input
  -> calculation
  -> interpreted result
  -> operating consequence
  -> reviewed decision
  -> authorized response
  -> measured outcome
```

This is the larger equation. The mathematics is essential, but the formula is one link in a much
longer chain. A correct formula applied to the wrong basin, wrong clock, wrong pump curve, or wrong
decision purpose still produces an unusable result.

## 2. The boundary gives every number its meaning

A number becomes meaningful only after its boundary is known. A rainfall depth of 3.20 inches
describes the event forcing, but it does not tell us how many gallons fell until the contributing
area is declared. A flow of 1.250 million gallons per day describes a rate at a meter, but it does
not tell us whether every customer, industrial discharge, transfer, or upstream station inside the
study boundary is represented.

The worked example declares a synthetic 640-acre basin connected to a sample pump station. This
boundary lets the calculation convert 3.20 inches of rain into 55.612 million gallons falling over
the basin. That rainfall volume is not sewer flow. It is the physical opportunity for rainfall to
produce a sewer response. The distinction matters because the later capture fraction compares
rainfall-derived sewer volume with rainfall volume over the same area.

The boundary also protects normalized comparisons. The inch-diameter-mile denominator combines the
length and nominal diameter of included sewer segments. It is useful only when the numerator and
denominator describe the same system. Dividing a station flow by an inventory that excludes private
laterals, abandoned segments, or part of the service area may create a precise-looking comparison
that does not represent the intended system.

For the agentic application, boundary is not a note at the bottom of a report. It is a required
object attached to every request, input snapshot, formula run, result, dashboard value, and
decision. If a boundary cannot be resolved, the system returns a data gap instead of continuing.

## 3. Data becomes evidence only after it is qualified

The story now moves from the physical system to its records. Flow may come from a permanent meter,
a temporary basin meter, or a SCADA historian. Rainfall may come from a utility gauge, an approved
public source, radar, or an uploaded event file. Pipe dimensions may come from GIS, as-built
drawings, or a field-verified inventory. Pump performance may come from a manufacturer curve,
certified test, or field performance test.

These records do not arrive ready for calculation. Their clocks may use different time zones.
Units may differ. Flow records may contain gaps, duplicates, fouling, low-depth error, surcharge, or
backwater effects. Rain gauges may miss periods or poorly represent spatial rainfall. A pump curve
may belong to the wrong impeller, speed, or revision. A wet-well volume may be based on geometric
dimensions that do not match the current control levels.

Data wrangling is the controlled work that turns those records into candidate inputs. The system
resolves identity, time, unit, boundary, quality, and provenance. It preserves the original record,
records every transformation, and decides whether the result is acceptable for the requested
method. The accepted input snapshot is then frozen. A later correction creates a new version
rather than silently changing an old calculation.

This is why the I&I capability must sit on top of SCADA and other systems rather than replace them.
SCADA remains the source for operating observations. GIS remains the source for spatial and asset
records. The calculation service consumes approved snapshots. PumpOS shows the result in operating
context. Droobi explains the lineage and drafts the next step. No layer is allowed to pretend it is
the source when it is not.

## 4. Establish the ordinary flow before explaining the storm

The wet-weather response cannot be isolated until expected dry-weather flow is established. Dry
weather does not mean zero unwanted water. It usually contains base wastewater flow from customers
and processes plus some amount of groundwater infiltration.

The worked example calculates an average dry-weather flow of 1.250 MGD. That value provides the
ordinary comparison condition. A separate dry-weather decomposition estimates 0.250 MGD of
groundwater infiltration by subtracting the supported base-wastewater estimate from measured
dry-weather flow.

This subtraction is simple mathematically and demanding evidentially. If the base-wastewater
estimate omits an industrial discharge, transferred flow, or seasonal customer pattern, the
remainder will be mislabeled as groundwater infiltration. The result therefore conveys an estimate
under a named method and boundary. It does not identify a cracked pipe or assign ownership.

The system also divides the groundwater-infiltration estimate by 412 inch-diameter-miles of
declared sewer inventory. The resulting 606.8 gallons per day per inch-diameter-mile is a screening
metric. It helps compare like-for-like inventories or prioritize review. It does not create a
universal pass or fail threshold. The agent must preserve that distinction whenever it explains
the number.

## 5. RTK explains the shape of rainfall response

RTK is not a device. It is a unit-hydrograph method used to represent rainfall-derived infiltration
and inflow. The name comes from three parameters: R, T, and K.

`R` is the fraction of rainfall volume assigned to a response component. It controls volume. If
the same storm falls on the same basin and R increases, more of the rainfall volume is represented
as sewer response.

`T` is the time from a rainfall increment to the component peak. It controls how quickly that
component reaches its maximum flow. A short T represents a rapid response. A longer T represents a
delayed response.

`K` is the recession duration divided by T. It controls how long the response takes to return
toward zero after the peak. A larger K creates a longer tail.

One triangular component cannot usually describe every pathway. The worked example uses short,
medium, and long components. The short component represents a rapid response. The intermediate
component spreads flow over a longer period. The long component represents delayed response and
recession. These are mathematical response components. They do not prove that a particular roof
leader, lateral, main, or manhole caused the flow.

The RTK method proceeds in three connected calculations.

First, `F-RTK-001` converts each component's R value, rainfall depth, and basin area into a component
volume. It also calculates the component base duration from T and K. This answers, "How much
rainfall-derived volume belongs to this response component, and how long does its triangular
response last?"

Second, `F-RTK-002` converts that component volume and duration into a triangular hydrograph. The
triangle rises to its peak at T and then recedes over K times T. This answers, "At each elapsed
time, what flow rate does this one component contribute?"

Third, `F-RTK-003` shifts and adds the component responses created by every rainfall increment.
This is superposition. It answers, "What complete rainfall-derived flow hydrograph results when the
whole storm is considered?"

The worked event produces 1.780 million gallons of integrated RDII and a modeled peak RDII flow of
2.704 MGD. The integrated volume conveys how much event-related water the model assigns above the
expected baseline. The peak conveys the largest modeled instantaneous burden. Volume matters for
storage, treatment, and annualization. Peak flow matters for pumps, force mains, wet wells, and
overflow risk. Neither number locates a defect.

The rainfall capture fraction is 3.20 percent because the 1.780 MG of RDII is compared with the
55.612 MG of rain falling over the declared basin. That fraction helps compare events and calibrate
the response model. It does not mean that 3.20 percent of every future storm will enter the sewer.
Rainfall distribution, antecedent moisture, groundwater, season, event definition, and data quality
all affect transfer.

RTK is therefore both important and easy to misuse. It gives the application a reproducible way to
turn rainfall into a timed response. It does not turn assumed parameters into field-confirmed
truth. A calibrated RTK result requires accepted flow and rainfall records, an approved event
window, parameter bounds, calibration criteria, and independent review.

## 6. The basin hydrograph becomes the station's inflow

The station does not receive an abstract RDII percentage. It receives flow over time. The expected
dry-weather hydrograph and the modeled rainfall-derived hydrograph are combined on the same clock.
In the sample event, peak total inflow reaches 3.929 MGD, or 2,728.3 gallons per minute.

This is the handoff from basin analysis to pump-station analysis. The peak total flow is an output
of the rainfall and dry-weather chain and an input to the station chain. That dependency must be
explicit in the application. The dashboard may round the display, but the station calculation
must consume the stored full-precision result.

The station side begins by building the system head curve. Flow through the force main creates
velocity. Velocity and pipe geometry determine Reynolds number. Reynolds number, roughness, and
diameter determine the friction factor. Friction factor, length, diameter, and velocity determine
major head loss. Fittings and valves create minor head loss. Static head and all relevant losses
combine into the head the pumps must overcome at each trial flow.

The pump curve describes the head a pump can produce at each flow under the represented speed,
impeller, and condition. The operating point is where pump head equals system head. For parallel
pumps, each identical pump is evaluated at its share of total flow under the stated assumption.

In the worked station, one pump at maximum static head produces an operating capacity of 2,994.3
gpm. The conservative two-pump firm capacity is 4,129.8 gpm. Comparing the 2,728.3 gpm peak inflow
with firm capacity produces a margin of 1,401.5 gpm, or 33.94 percent, and a utilization of 66.06
percent.

Those results convey a named capacity comparison for this event and configuration. They do not
certify the station. A different static head, pump condition, control state, force-main
configuration, or event can change the operating point.

## 7. Capacity alone does not answer resilience

A station can have acceptable normal firm capacity and still face a contingency problem. The
reason is storage. When inflow exceeds available pumping capacity, the difference accumulates in
the wet well or connected system. The question becomes how much usable storage exists, how quickly
it is consumed, and whether response arrives before the limiting level is reached.

The normal one-pump sample requires no storage because the one-pump operating capacity exceeds the
event inflow at the screened condition. The story changes when that pump is hypothetically derated
to 75 percent capacity. Available capacity falls to 2,245.7 gpm. The event requires 75,312 gallons
of storage against 45,000 gallons available, producing a 30,312-gallon shortfall.

The complete-outage screen is more severe. With no pumping for 30 minutes at the stated inflow, the
required storage is 81,848 gallons. The shortfall is 36,848 gallons. At that constant inflow, the
45,000 gallons of usable storage is exhausted in 16.49 minutes.

Each result answers a different question. Required storage says how much volume the scenario needs.
Shortfall says how much the requirement exceeds the declared usable storage. Time to exhaustion
says how long the operator or automated control strategy has before the modeled storage boundary
is reached. These values support contingency planning. They do not predict an overflow time under
all real hydraulic conditions unless the dynamic model and field conditions support that claim.

## 8. Operating burden becomes energy, maintenance, and cost

Flow also creates an operating burden before any overflow occurs. Pump cycling affects starts,
equipment wear, and control performance. The sample constant-speed cycling screen produces 2.475
cycles per hour under its simplified assumptions. That value should be compared with an applicable
reviewed manual or control requirement. The formula does not create the allowable limit.

Flow and total dynamic head determine hydraulic power. Pump and motor efficiencies determine the
electrical input power required to deliver that hydraulic work. Integrating power over the event
produces 1,589.9 kilowatt-hours. Applying the stated energy price produces an event energy cost of
$190.79.

The meaning is operational, not merely financial. The energy result connects an I&I hydrograph to
equipment duty. It can help explain why wet-weather energy rises, compare operating strategies, or
screen the avoidable burden of unwanted flow. It remains modeled until compared with accepted
power-meter or motor-control-center evidence.

Equivalent operating hours convert pumped volume into a time measure using representative pump
capacities. The sample gives 6.892 aggregate pump hours per average dry-weather day. A separate
Miami-Dade calculation produces an illustrative NAPOT value of 3.446 hours per day. NAPOT is
jurisdiction-specific. It belongs in a versioned Miami-Dade rule pack, not in the universal
mathematics layer.

## 9. Economics must preserve an unfavorable answer

The sample rehabilitation scenario assumes an annual modeled I&I reduction of 35.116 million
gallons. Applying the stated marginal conveyance and treatment cost produces a gross annual benefit
of $22,826. After the scenario's annual operations and maintenance cost, the net direct benefit is
negative $97,174 per year.

Discounting the stated cash flows produces $339,586 in present gross benefits and $10,285,297 in
present total costs. Net present value is negative $9,945,711. The benefit-cost ratio is 0.033.
Simple payback is not calculated because annual net benefit is not positive.

The unfavorable result is part of the design. An agentic application must not manipulate
assumptions until a project looks attractive. It must explain what was included, what was excluded,
and why the result has the sign it does. Avoided capacity, overflow risk, compliance exposure,
reliability, environmental effects, and public-health benefits are material considerations, but
they cannot be silently inserted without approved methods and evidence.

The economic screen therefore conveys one narrow scenario under stated assumptions. It can support
alternatives development. It does not authorize a project.

## 10. The dashboard is the visible end of the calculation chain

The dashboard is where different readers meet the same governed result. The basin analyst needs to
see rainfall, baseline, RDII volume, capture, and peak. The station engineer needs operating points,
capacity, storage, and contingency time. The asset manager needs cycling, energy, and applicable
manual requirements. Finance needs the annual and present-value assumptions. An executive needs to
see the consequence and the decision state without losing the ability to inspect evidence.

That is why every displayed value has a stable identifier from M-01 through M-34. The identifier is
not decoration. It is the handle that connects the displayed value to its full-precision result,
formula version, accepted input snapshot, sources, evidence class, decision use, and history.

When a reader selects M-21, the application should not merely repeat "16.49 minutes." It should
explain that the value is a constant-deficit storage screen, show the 45,000 gallons of usable
storage, the represented inflow and pumping availability, the governing formula, and the
assumptions. It should also say what the result does not establish.

## 11. The agent connects evidence, but does not become the calculator

Droobi's role begins after deterministic services have produced or refused a result. It can gather
the accepted calculation, applicable manual passages, topology relationships, open work orders,
and decision policy. It can explain the chain in plain language. It can identify that a pump curve,
meter calibration, or rule-pack review is missing. It can draft an investigation or work order.

Droobi cannot create a missing pump curve, choose an unregistered coefficient, rewrite an
unfavorable economic result, or turn a screening metric into a compliance finding. The
deterministic engine calculates. The application displays. The agent composes and explains. A named
person authorizes consequential action.

This separation is what makes the product agentic without making it reckless. The agent can pursue
a goal across approved tools and evidence, but its authority remains bounded. Every proposed action
retains the finding, evidence, assumptions, missing information, required approver, destination,
and completion evidence.

## 12. The loop closes only when the outcome is measured

The system is incomplete when a recommendation is approved. It must record what work was performed
and whether the expected result occurred. Post-rehabilitation flow and rainfall must be compared
with a defensible counterfactual that accounts for weather and operating differences. A raw
before-and-after comparison can confuse a smaller storm with a successful project.

Outcome verification therefore returns the story to its beginning. New observations enter through
the same governed pipeline. The application asks whether the measured response changed under
comparable conditions, whether uncertainty supports the conclusion, and whether the finding should
be retained, revised, or rejected.

The larger equation is now complete:

```text
rain and groundwater
  -> sewer response
  -> measured flow
  -> separated and modeled I&I
  -> station consequence
  -> operating and financial consequence
  -> reviewed action
  -> field work
  -> measured outcome
  -> better evidence for the next decision
```

This is the reason the architecture, formulas, dashboards, manuals, graph, agents, and human
approval model belong in one Bible. They are different parts of one evidence-to-action system.
