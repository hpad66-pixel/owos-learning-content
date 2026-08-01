# Part VII. Fully populated dashboard mockups

This section shows the actual dashboard compositions that were missing from the earlier candidate. Every numbered value is populated from sample calculation run `RUN-MD-EX-01`. The screenshots and interactive prototype are development mockups, not evidence that these screens are implemented in PumpOS.

## How to read every mockup

Each visible `M-##` identifier is the stable dashboard metric identifier. Selecting that value in the prototype opens its displayed value, exact result path, source class, formula chain, importance, and decision boundary. The screens use rounded display values, while calculation dependencies consume stored full-precision results.

The standalone prototype is stored at [`dashboard-mockups/index.html`](dashboard-mockups/index.html).

## DASH-01. Fleet Command Center

**Decision question:** Which basin, station, or decision needs attention first?

![Fleet Command Center populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/01-fleet-command-center.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-07` / #7 RDII event volume | **1.780 MG** | `hydrograph_summary.integrated_RDII_volume_gal` | DS-01, DS-02, DS-03 | F-RDII-001 -> F-RDII-002 -> F-FLOW-001 -> F-RTK-001 -> F-RTK-002 -> F-RTK-003 |
| `M-10` / #10 Peak total station inflow | **3.929 MGD / 2,728.3 gpm** | `hydrograph_summary.peak_total_flow_gpm` | DS-01, DS-02, DS-03 | F-DWF-001 -> F-RTK-003 -> F-CONV-001 |
| `M-14` / #14 Peak firm-capacity utilization | **66.06%** | `pump_station_analysis.capacity.peak_utilization_fraction` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-21` / #21 Time to exhaust usable storage during full outage | **16.49 min** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.time_to_exhaust_available_storage_min` | DS-01, DS-07 | F-PUMP-003 |
| `M-29` / #29 Annual net direct benefit | **-$97,174/yr** | `rehabilitation_and_economics.annual_net_direct_benefit_USD` | DS-09 | F-COST-001 |
| `M-32` / #32 Net present value | **-$9,945,711** | `rehabilitation_and_economics.NPV_USD` | DS-09 | F-PV-001 -> F-ECON-003 |

### Decisions supported

- `DEC-02` Open basin investigation: consumes M-06, M-07, M-08, M-09; requires I_and_I_analyst, collection_system_engineer; produces `draft_investigation`.
- `DEC-03` Review station normal and contingency condition: consumes M-10, M-11, M-12, M-13, M-14, M-15, M-16, M-17, M-18, M-19, M-20, M-21; requires pump_station_engineer, operations_supervisor; produces `approved_contingency_action_or_request_for_more_evidence`.
- `DEC-06` Screen rehabilitation economics: consumes M-27, M-28, M-29, M-30, M-31, M-32, M-33, M-34; requires engineer, finance, capital_planning; produces `scenario_review_not_project_authorization`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-02. Basin and I&I Workspace

**Decision question:** What did the event produce, and how was that conclusion calculated?

![Basin and I&I Workspace populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/02-basin-and-ii-workspace.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-01` / #1 Event rainfall depth | **3.20 in** | `hydrograph_summary.rainfall_depth_in` | DS-02 | Direct accepted input |
| `M-02` / #2 Rainfall volume over basin | **55.612 MG** | `hydrograph_summary.rainfall_volume_gal` | DS-02, DS-03 | F-UNIT-001 |
| `M-03` / #3 Average dry-weather flow | **1.250 MGD** | `hydrograph_summary.average_dry_weather_flow_MGD` | DS-01 | F-DWF-001 |
| `M-04` / #4 Groundwater infiltration | **0.250 MGD** | `inventory_and_dry_weather.GWI_gpd` | DS-01, DS-04 | F-GWI-001 -> F-CONV-001 |
| `M-05` / #5 Inch-diameter-mile inventory | **412 in-mi** | `inventory_and_dry_weather.inch_diameter_mile` | DS-03 | F-IDM-001 |
| `M-06` / #6 Normalized dry-weather GWI | **606.8 gpd/in-mi** | `inventory_and_dry_weather.GWI_gpd_per_inch_diameter_mile` | DS-01, DS-03, DS-04 | F-GWI-001 -> F-IDM-001 -> F-NORM-001 |
| `M-07` / #7 RDII event volume | **1.780 MG** | `hydrograph_summary.integrated_RDII_volume_gal` | DS-01, DS-02, DS-03 | F-RDII-001 -> F-RDII-002 -> F-FLOW-001 -> F-RTK-001 -> F-RTK-002 -> F-RTK-003 |
| `M-08` / #8 Rainfall capture fraction | **3.20%** | `hydrograph_summary.capture_fraction_total_R` | DS-01, DS-02, DS-03 | F-UNIT-001 -> F-RDII-002 -> F-RDII-003 |
| `M-09` / #9 Peak RDII flow | **2.704 MGD** | `hydrograph_summary.peak_RDII_MGD` | DS-01, DS-02, DS-03 | F-RTK-001 -> F-RTK-002 -> F-RTK-003 -> F-CONV-001 |
| `M-10` / #10 Peak total station inflow | **3.929 MGD / 2,728.3 gpm** | `hydrograph_summary.peak_total_flow_gpm` | DS-01, DS-02, DS-03 | F-DWF-001 -> F-RTK-003 -> F-CONV-001 |

### Decisions supported

- `DEC-01` Accept or reject event for analysis: consumes M-01, M-03; requires I_and_I_analyst; produces `accepted_event_or_data_gap`.
- `DEC-02` Open basin investigation: consumes M-06, M-07, M-08, M-09; requires I_and_I_analyst, collection_system_engineer; produces `draft_investigation`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-03. Station Hydraulics and Resiliency

**Decision question:** Can the station convey the event under normal and contingency conditions?

![Station Hydraulics and Resiliency populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/03-station-hydraulics-resiliency.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-10` / #10 Peak total station inflow | **3.929 MGD / 2,728.3 gpm** | `hydrograph_summary.peak_total_flow_gpm` | DS-01, DS-02, DS-03 | F-DWF-001 -> F-RTK-003 -> F-CONV-001 |
| `M-11` / #11 One-pump operating capacity at maximum static head | **2,994.3 gpm** | `pump_station_analysis.operating_points.1_pump_maximum_static_head.total_flow_gpm` | DS-05, DS-06 | F-HYD-001 -> F-HYD-002 -> F-HYD-003 -> F-HYD-004 -> F-HYD-005 -> F-PUMP-001 |
| `M-12` / #12 Conservative two-pump firm capacity | **4,129.8 gpm** | `pump_station_analysis.capacity.conservative_firm_capacity_gpm` | DS-05, DS-06 | F-HYD-001 -> F-HYD-002 -> F-HYD-003 -> F-HYD-004 -> F-HYD-005 -> F-PUMP-001 |
| `M-13` / #13 Peak firm-capacity margin | **1,401.5 gpm / 33.94%** | `pump_station_analysis.capacity.peak_margin_gpm` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-14` / #14 Peak firm-capacity utilization | **66.06%** | `pump_station_analysis.capacity.peak_utilization_fraction` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-15` / #15 One-pump normal required storage | **0 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-NORMAL.required_storage_gal` | DS-01, DS-05, DS-06, DS-07 | F-MASS-001 -> F-FLOW-001 -> F-PUMP-007 |
| `M-16` / #16 Derated one-pump available capacity | **2,245.7 gpm** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.available_capacity_gpm` | DS-05, DS-06 | F-PUMP-001 |
| `M-17` / #17 Derated one-pump required storage | **75,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.required_storage_gal` | DS-01, DS-05, DS-06, DS-07 | F-MASS-001 -> F-FLOW-001 -> F-PUMP-007 |
| `M-18` / #18 Derated one-pump storage shortfall | **30,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.storage_shortfall_gal` | DS-01, DS-05, DS-06, DS-07 | F-PUMP-007 |
| `M-19` / #19 Complete-outage required storage for 30 minutes | **81,848 gal** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.required_storage_gal` | DS-01, DS-07 | F-PUMP-004 |
| `M-20` / #20 Complete-outage storage shortfall | **36,848 gal** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.storage_shortfall_gal` | DS-01, DS-07 | F-PUMP-004 |
| `M-21` / #21 Time to exhaust usable storage during full outage | **16.49 min** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.time_to_exhaust_available_storage_min` | DS-01, DS-07 | F-PUMP-003 |

### Decisions supported

- `DEC-03` Review station normal and contingency condition: consumes M-10, M-11, M-12, M-13, M-14, M-15, M-16, M-17, M-18, M-19, M-20, M-21; requires pump_station_engineer, operations_supervisor; produces `approved_contingency_action_or_request_for_more_evidence`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-04. Operations, Cycling, and Energy

**Decision question:** What operating burden did the flow create?

![Operations, Cycling, and Energy populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/04-operations-cycling-energy.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-22` / #22 Illustrative cycles per hour | **2.475 cycles/hr** | `pump_station_analysis.cycling.cycles_per_hour` | DS-01, DS-05, DS-07 | F-PUMP-005 |
| `M-23` / #23 Event pumping energy | **1,589.9 kWh** | `pump_station_analysis.energy.event_staged_control_energy_kWh` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-24` / #24 Event energy cost | **$190.79** | `pump_station_analysis.energy.event_staged_control_energy_cost_USD` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-25` / #25 Aggregate pump hours per average dry-weather day | **6.892 hr/day** | `pump_station_analysis.operating_time.aggregate_pump_hours_per_ADWF_day` | DS-01, DS-05 | F-PUMP-006 |
| `M-26` / #26 Illustrative Miami-Dade NAPOT | **3.446 hr/day** | `pump_station_analysis.operating_time.illustrative_Miami_Dade_NAPOT_hours_per_day` | DS-01, DS-05, DS-10 | F-PUMP-006 -> F-MDC-NAPOT-001 |

### Decisions supported

- `DEC-04` Review cycling and energy: consumes M-22, M-23, M-24; requires asset_manager, pump_station_engineer; produces `maintenance_or_efficiency_investigation`.
- `DEC-05` Review jurisdiction-specific operating time: consumes M-25, M-26; requires operations, compliance_reviewer; produces `reviewed_rule_pack_finding`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-05. Program and Economics Workspace

**Decision question:** Does the stated rehabilitation scenario justify further development?

![Program and Economics Workspace populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/05-program-economics.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-27` / #27 Annual modeled I&I reduction | **35.116 MG/yr** | `rehabilitation_and_economics.annual_total_I_and_I_reduction_MG` | DS-01, DS-02, DS-03, DS-09 | F-ECON-002 -> F-VERIFY-001 |
| `M-28` / #28 Annual gross marginal-cost benefit | **$22,826/yr** | `rehabilitation_and_economics.annual_gross_marginal_cost_benefit_USD` | DS-09 | F-COST-001 |
| `M-29` / #29 Annual net direct benefit | **-$97,174/yr** | `rehabilitation_and_economics.annual_net_direct_benefit_USD` | DS-09 | F-COST-001 |
| `M-30` / #30 Present value of gross benefits | **$339,586** | `rehabilitation_and_economics.PV_gross_benefits_USD` | DS-09 | F-PV-001 |
| `M-31` / #31 Present value of total costs | **$10,285,297** | `rehabilitation_and_economics.PV_total_costs_USD` | DS-09 | F-PV-001 |
| `M-32` / #32 Net present value | **-$9,945,711** | `rehabilitation_and_economics.NPV_USD` | DS-09 | F-PV-001 -> F-ECON-003 |
| `M-33` / #33 Benefit-cost ratio | **0.033** | `rehabilitation_and_economics.benefit_cost_ratio` | DS-09 | F-BCR-001 |
| `M-34` / #34 Simple payback | **Not calculable because annual net benefit is nonpositive** | `rehabilitation_and_economics.simple_payback_years` | DS-09 | F-ECON-004 |

### Decisions supported

- `DEC-06` Screen rehabilitation economics: consumes M-27, M-28, M-29, M-30, M-31, M-32, M-33, M-34; requires engineer, finance, capital_planning; produces `scenario_review_not_project_authorization`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-06. Asset and Manual Compliance

**Decision question:** Which approved requirement applies to the asset, and what evidence is due?

![Asset and Manual Compliance populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/06-asset-manual-compliance.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-22` / #22 Illustrative cycles per hour | **2.475 cycles/hr** | `pump_station_analysis.cycling.cycles_per_hour` | DS-01, DS-05, DS-07 | F-PUMP-005 |
| `M-23` / #23 Event pumping energy | **1,589.9 kWh** | `pump_station_analysis.energy.event_staged_control_energy_kWh` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-25` / #25 Aggregate pump hours per average dry-weather day | **6.892 hr/day** | `pump_station_analysis.operating_time.aggregate_pump_hours_per_ADWF_day` | DS-01, DS-05 | F-PUMP-006 |

### Decisions supported

- `DEC-04` Review cycling and energy: consumes M-22, M-23, M-24; requires asset_manager, pump_station_engineer; produces `maintenance_or_efficiency_investigation`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-07. Data Gap Center

**Decision question:** What missing contract prevents a result from becoming production-authoritative?

![Data Gap Center populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/07-data-gap-center.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-10` / #10 Peak total station inflow | **3.929 MGD / 2,728.3 gpm** | `hydrograph_summary.peak_total_flow_gpm` | DS-01, DS-02, DS-03 | F-DWF-001 -> F-RTK-003 -> F-CONV-001 |
| `M-11` / #11 One-pump operating capacity at maximum static head | **2,994.3 gpm** | `pump_station_analysis.operating_points.1_pump_maximum_static_head.total_flow_gpm` | DS-05, DS-06 | F-HYD-001 -> F-HYD-002 -> F-HYD-003 -> F-HYD-004 -> F-HYD-005 -> F-PUMP-001 |
| `M-18` / #18 Derated one-pump storage shortfall | **30,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.storage_shortfall_gal` | DS-01, DS-05, DS-06, DS-07 | F-PUMP-007 |
| `M-23` / #23 Event pumping energy | **1,589.9 kWh** | `pump_station_analysis.energy.event_staged_control_energy_kWh` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-27` / #27 Annual modeled I&I reduction | **35.116 MG/yr** | `rehabilitation_and_economics.annual_total_I_and_I_reduction_MG` | DS-01, DS-02, DS-03, DS-09 | F-ECON-002 -> F-VERIFY-001 |
| `M-29` / #29 Annual net direct benefit | **-$97,174/yr** | `rehabilitation_and_economics.annual_net_direct_benefit_USD` | DS-09 | F-COST-001 |

### Decisions supported

- `DEC-02` Open basin investigation: consumes M-06, M-07, M-08, M-09; requires I_and_I_analyst, collection_system_engineer; produces `draft_investigation`.
- `DEC-03` Review station normal and contingency condition: consumes M-10, M-11, M-12, M-13, M-14, M-15, M-16, M-17, M-18, M-19, M-20, M-21; requires pump_station_engineer, operations_supervisor; produces `approved_contingency_action_or_request_for_more_evidence`.
- `DEC-04` Review cycling and energy: consumes M-22, M-23, M-24; requires asset_manager, pump_station_engineer; produces `maintenance_or_efficiency_investigation`.
- `DEC-06` Screen rehabilitation economics: consumes M-27, M-28, M-29, M-30, M-31, M-32, M-33, M-34; requires engineer, finance, capital_planning; produces `scenario_review_not_project_authorization`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-08. Action and Approval Center

**Decision question:** What decision is proposed, who must approve it, and what evidence supports it?

![Action and Approval Center populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/08-action-approval-center.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-08` / #8 Rainfall capture fraction | **3.20%** | `hydrograph_summary.capture_fraction_total_R` | DS-01, DS-02, DS-03 | F-UNIT-001 -> F-RDII-002 -> F-RDII-003 |
| `M-14` / #14 Peak firm-capacity utilization | **66.06%** | `pump_station_analysis.capacity.peak_utilization_fraction` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-18` / #18 Derated one-pump storage shortfall | **30,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.storage_shortfall_gal` | DS-01, DS-05, DS-06, DS-07 | F-PUMP-007 |
| `M-20` / #20 Complete-outage storage shortfall | **36,848 gal** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.storage_shortfall_gal` | DS-01, DS-07 | F-PUMP-004 |
| `M-21` / #21 Time to exhaust usable storage during full outage | **16.49 min** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.time_to_exhaust_available_storage_min` | DS-01, DS-07 | F-PUMP-003 |
| `M-32` / #32 Net present value | **-$9,945,711** | `rehabilitation_and_economics.NPV_USD` | DS-09 | F-PV-001 -> F-ECON-003 |

### Decisions supported

- `DEC-02` Open basin investigation: consumes M-06, M-07, M-08, M-09; requires I_and_I_analyst, collection_system_engineer; produces `draft_investigation`.
- `DEC-03` Review station normal and contingency condition: consumes M-10, M-11, M-12, M-13, M-14, M-15, M-16, M-17, M-18, M-19, M-20, M-21; requires pump_station_engineer, operations_supervisor; produces `approved_contingency_action_or_request_for_more_evidence`.
- `DEC-06` Screen rehabilitation economics: consumes M-27, M-28, M-29, M-30, M-31, M-32, M-33, M-34; requires engineer, finance, capital_planning; produces `scenario_review_not_project_authorization`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## DASH-09. Calculation Lineage Explorer

**Decision question:** Can every displayed number be traced to its accepted source and calculation?

![Calculation Lineage Explorer populated with the MD-EX-01 worked values](dashboard-mockups/screenshots/09-calculation-lineage-explorer.png)

### Values displayed and their wiring

| Dashboard number | Worked value | Result path | Source class | Formula chain |
| --- | --- | --- | --- | --- |
| `M-01` / #1 Event rainfall depth | **3.20 in** | `hydrograph_summary.rainfall_depth_in` | DS-02 | Direct accepted input |
| `M-02` / #2 Rainfall volume over basin | **55.612 MG** | `hydrograph_summary.rainfall_volume_gal` | DS-02, DS-03 | F-UNIT-001 |
| `M-03` / #3 Average dry-weather flow | **1.250 MGD** | `hydrograph_summary.average_dry_weather_flow_MGD` | DS-01 | F-DWF-001 |
| `M-04` / #4 Groundwater infiltration | **0.250 MGD** | `inventory_and_dry_weather.GWI_gpd` | DS-01, DS-04 | F-GWI-001 -> F-CONV-001 |
| `M-05` / #5 Inch-diameter-mile inventory | **412 in-mi** | `inventory_and_dry_weather.inch_diameter_mile` | DS-03 | F-IDM-001 |
| `M-06` / #6 Normalized dry-weather GWI | **606.8 gpd/in-mi** | `inventory_and_dry_weather.GWI_gpd_per_inch_diameter_mile` | DS-01, DS-03, DS-04 | F-GWI-001 -> F-IDM-001 -> F-NORM-001 |
| `M-07` / #7 RDII event volume | **1.780 MG** | `hydrograph_summary.integrated_RDII_volume_gal` | DS-01, DS-02, DS-03 | F-RDII-001 -> F-RDII-002 -> F-FLOW-001 -> F-RTK-001 -> F-RTK-002 -> F-RTK-003 |
| `M-08` / #8 Rainfall capture fraction | **3.20%** | `hydrograph_summary.capture_fraction_total_R` | DS-01, DS-02, DS-03 | F-UNIT-001 -> F-RDII-002 -> F-RDII-003 |
| `M-09` / #9 Peak RDII flow | **2.704 MGD** | `hydrograph_summary.peak_RDII_MGD` | DS-01, DS-02, DS-03 | F-RTK-001 -> F-RTK-002 -> F-RTK-003 -> F-CONV-001 |
| `M-10` / #10 Peak total station inflow | **3.929 MGD / 2,728.3 gpm** | `hydrograph_summary.peak_total_flow_gpm` | DS-01, DS-02, DS-03 | F-DWF-001 -> F-RTK-003 -> F-CONV-001 |
| `M-11` / #11 One-pump operating capacity at maximum static head | **2,994.3 gpm** | `pump_station_analysis.operating_points.1_pump_maximum_static_head.total_flow_gpm` | DS-05, DS-06 | F-HYD-001 -> F-HYD-002 -> F-HYD-003 -> F-HYD-004 -> F-HYD-005 -> F-PUMP-001 |
| `M-12` / #12 Conservative two-pump firm capacity | **4,129.8 gpm** | `pump_station_analysis.capacity.conservative_firm_capacity_gpm` | DS-05, DS-06 | F-HYD-001 -> F-HYD-002 -> F-HYD-003 -> F-HYD-004 -> F-HYD-005 -> F-PUMP-001 |
| `M-13` / #13 Peak firm-capacity margin | **1,401.5 gpm / 33.94%** | `pump_station_analysis.capacity.peak_margin_gpm` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-14` / #14 Peak firm-capacity utilization | **66.06%** | `pump_station_analysis.capacity.peak_utilization_fraction` | DS-01, DS-02, DS-03, DS-05, DS-06 | F-PUMP-002 |
| `M-15` / #15 One-pump normal required storage | **0 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-NORMAL.required_storage_gal` | DS-01, DS-05, DS-06, DS-07 | F-MASS-001 -> F-FLOW-001 -> F-PUMP-007 |
| `M-16` / #16 Derated one-pump available capacity | **2,245.7 gpm** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.available_capacity_gpm` | DS-05, DS-06 | F-PUMP-001 |
| `M-17` / #17 Derated one-pump required storage | **75,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.required_storage_gal` | DS-01, DS-05, DS-06, DS-07 | F-MASS-001 -> F-FLOW-001 -> F-PUMP-007 |
| `M-18` / #18 Derated one-pump storage shortfall | **30,312 gal** | `pump_station_analysis.storage.contingency_results.ONE-PUMP-DERATED-75.storage_shortfall_gal` | DS-01, DS-05, DS-06, DS-07 | F-PUMP-007 |
| `M-19` / #19 Complete-outage required storage for 30 minutes | **81,848 gal** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.required_storage_gal` | DS-01, DS-07 | F-PUMP-004 |
| `M-20` / #20 Complete-outage storage shortfall | **36,848 gal** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.storage_shortfall_gal` | DS-01, DS-07 | F-PUMP-004 |
| `M-21` / #21 Time to exhaust usable storage during full outage | **16.49 min** | `pump_station_analysis.storage.contingency_results.COMPLETE-OUTAGE-30-MIN.time_to_exhaust_available_storage_min` | DS-01, DS-07 | F-PUMP-003 |
| `M-22` / #22 Illustrative cycles per hour | **2.475 cycles/hr** | `pump_station_analysis.cycling.cycles_per_hour` | DS-01, DS-05, DS-07 | F-PUMP-005 |
| `M-23` / #23 Event pumping energy | **1,589.9 kWh** | `pump_station_analysis.energy.event_staged_control_energy_kWh` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-24` / #24 Event energy cost | **$190.79** | `pump_station_analysis.energy.event_staged_control_energy_cost_USD` | DS-05, DS-06, DS-08 | F-ENERGY-001 -> F-ENERGY-002 |
| `M-25` / #25 Aggregate pump hours per average dry-weather day | **6.892 hr/day** | `pump_station_analysis.operating_time.aggregate_pump_hours_per_ADWF_day` | DS-01, DS-05 | F-PUMP-006 |
| `M-26` / #26 Illustrative Miami-Dade NAPOT | **3.446 hr/day** | `pump_station_analysis.operating_time.illustrative_Miami_Dade_NAPOT_hours_per_day` | DS-01, DS-05, DS-10 | F-PUMP-006 -> F-MDC-NAPOT-001 |
| `M-27` / #27 Annual modeled I&I reduction | **35.116 MG/yr** | `rehabilitation_and_economics.annual_total_I_and_I_reduction_MG` | DS-01, DS-02, DS-03, DS-09 | F-ECON-002 -> F-VERIFY-001 |
| `M-28` / #28 Annual gross marginal-cost benefit | **$22,826/yr** | `rehabilitation_and_economics.annual_gross_marginal_cost_benefit_USD` | DS-09 | F-COST-001 |
| `M-29` / #29 Annual net direct benefit | **-$97,174/yr** | `rehabilitation_and_economics.annual_net_direct_benefit_USD` | DS-09 | F-COST-001 |
| `M-30` / #30 Present value of gross benefits | **$339,586** | `rehabilitation_and_economics.PV_gross_benefits_USD` | DS-09 | F-PV-001 |
| `M-31` / #31 Present value of total costs | **$10,285,297** | `rehabilitation_and_economics.PV_total_costs_USD` | DS-09 | F-PV-001 |
| `M-32` / #32 Net present value | **-$9,945,711** | `rehabilitation_and_economics.NPV_USD` | DS-09 | F-PV-001 -> F-ECON-003 |
| `M-33` / #33 Benefit-cost ratio | **0.033** | `rehabilitation_and_economics.benefit_cost_ratio` | DS-09 | F-BCR-001 |
| `M-34` / #34 Simple payback | **Not calculable because annual net benefit is nonpositive** | `rehabilitation_and_economics.simple_payback_years` | DS-09 | F-ECON-004 |

### Decisions supported

- `DEC-01` Accept or reject event for analysis: consumes M-01, M-03; requires I_and_I_analyst; produces `accepted_event_or_data_gap`.
- `DEC-02` Open basin investigation: consumes M-06, M-07, M-08, M-09; requires I_and_I_analyst, collection_system_engineer; produces `draft_investigation`.
- `DEC-03` Review station normal and contingency condition: consumes M-10, M-11, M-12, M-13, M-14, M-15, M-16, M-17, M-18, M-19, M-20, M-21; requires pump_station_engineer, operations_supervisor; produces `approved_contingency_action_or_request_for_more_evidence`.
- `DEC-04` Review cycling and energy: consumes M-22, M-23, M-24; requires asset_manager, pump_station_engineer; produces `maintenance_or_efficiency_investigation`.
- `DEC-05` Review jurisdiction-specific operating time: consumes M-25, M-26; requires operations, compliance_reviewer; produces `reviewed_rule_pack_finding`.
- `DEC-06` Screen rehabilitation economics: consumes M-27, M-28, M-29, M-30, M-31, M-32, M-33, M-34; requires engineer, finance, capital_planning; produces `scenario_review_not_project_authorization`.

### What this screen does not establish

This mockup demonstrates information architecture and traceability using illustrative sample data. It does not approve the event, certify station capacity, establish regulatory compliance, authorize a project, or prove that the screen exists in the current PumpOS production build.

## Dashboard coverage statement

The nine mockups collectively display all 34 numbered metrics. The lineage explorer displays the entire set in one auditable table. The other eight screens organize the same values around the operational questions that a fleet manager, I&I analyst, station engineer, asset manager, compliance reviewer, finance reviewer, and approving authority must answer.

