# Open-Source Repository Landscape for the I&I Intelligence System

## PumpOS system curves, pump-station hydraulics, RDII, RTK, sewer modeling, optimization, telemetry, and agent infrastructure

**Research cutoff:** July 28, 2026  
**Companion document:** `ii-intelligence-system-bible-v2.md`  
**Purpose:** identify reusable open-source GitHub repositories and state precisely where each one can, and cannot, fit in the governed PumpOS and I&I calculation architecture.

---

## 1. Executive conclusion

There is no single open-source repository that implements the complete I&I Intelligence System described in the Bible. The calculation chain crosses several engineering and software domains:

1. rainfall and flow observations;
2. dry-weather baseline and observed RDII separation;
3. RTK hydrograph generation and calibration;
4. gravity-sewer hydraulic routing;
5. pump and force-main system curves;
6. pump operating-point, storage, cycling, energy, and resilience calculations;
7. calibration, uncertainty, and scenario management;
8. GIS and asset topology;
9. SCADA and time-series ingestion;
10. calculation lineage, approvals, dashboards, and agent explanation.

The recommended architecture is therefore a governed composition, not an attempt to find one repository and make it the product:

- **Use the official EPA SWMM solver as the primary open-source sewer and RDII simulation engine.**
- **Implement the Bible's formula registry as PumpOS-owned deterministic calculation services.** These services must own formula identifiers, units, input contracts, assumptions, precision, fail-closed rules, versioning, and tests.
- **Use `fluids`, SciPy, EPANET, WNTR, and pandapipes as reference implementations or cross-check engines for force-main losses, system curves, and pump operating points.** They do not replace the controlled PumpOS formula service.
- **Use PySWMM and one selected SWMM model I/O library as adapters around SWMM.**
- **Use water-control and optimization repositories only inside a scenario or recommendation boundary.** No optimization output should directly operate a station without an approved control policy and a separate operational safety layer.
- **Keep the agent outside the numerical kernel.** It may assemble an approved run, explain results, identify missing evidence, and route approvals. It must not silently invent pump curves, RTK parameters, roughness, minor-loss coefficients, operating lineups, event windows, or capacity criteria.

“Open source” is not the same as “engineering authority.” Repository code must be pinned, tested, validated against independent examples, reviewed for license compatibility, and wrapped by APAS-owned contracts before it becomes part of a production calculation.

---

## 2. How to read the repository ratings

### 2.1 Adoption classes

| Class | Meaning |
|---|---|
| **A - core candidate** | Strong candidate for a controlled production dependency or reference engine. It still requires version pinning, verification, and APAS acceptance tests. |
| **B - adapter or specialist** | Useful for model I/O, automation, calibration, visualization, or a bounded specialist function. It is not the calculation authority by itself. |
| **C - research accelerator** | Useful for prototypes, benchmarks, comparative research, or algorithm development. It should not enter production calculations without an engineering and software validation program. |
| **D - infrastructure** | Supports data, GIS, telemetry, workflow, provenance, or agents. It does not establish hydraulic correctness. |
| **Archive/reference** | Useful to understand prior art or reproduce a study, but not a preferred new production dependency. |

### 2.2 Engineering fit labels

| Label | Meaning |
|---|---|
| **Direct** | Implements or directly supports a formula family or model required by the Bible. |
| **Cross-check** | Can independently reproduce part of a result and expose disagreements. |
| **Workflow** | Moves, validates, stores, or displays data without being the hydraulic solver. |
| **Research only** | Demonstrates an approach but has maturity, activity, licensing, dependency, or scope limitations. |

### 2.3 License caution

The license entries below are a research snapshot, not legal advice. APAS must re-read the exact license, notices, bundled dependencies, and release-specific terms before adoption. This is especially important for GPL code, source-available code, repositories that include multiple licenses, and projects that require a commercial optimizer.

---

## 3. Highest-priority repository shortlist

| Priority | Repository | Adopt it for | Do not treat it as |
|---:|---|---|---|
| 1 | [USEPA/Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model) | Controlled SWMM sewer, wastewater, stormwater, dynamic-wave, runoff, and RDII simulations | A complete PumpOS/I&I application or a substitute for field calibration |
| 2 | [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm) | Python stepping, result extraction, controlled inflows, automation, and simulation orchestration | An independent hydraulic solver |
| 3 | [pyswmm/swmmio](https://github.com/pyswmm/swmmio) and [MarkusPic/swmm_api](https://github.com/MarkusPic/swmm_api) | A bake-off for INP/RPT/OUT manipulation, model diffing, GIS export, and batch preparation | Two permanent overlapping dependencies unless each has a distinct governed responsibility |
| 4 | [CalebBell/fluids](https://github.com/CalebBell/fluids) | Friction factors, fittings, loss coefficients, flow-meter and pump-related engineering primitives; reference tests for `F-HYD-001` through `F-HYD-005` | The APAS system-curve contract or pump-station digital twin |
| 5 | [OpenWaterAnalytics/EPANET](https://github.com/OpenWaterAnalytics/EPANET) | Pressurized force-main and pump-curve cross-checking; extended-period network scenarios | A gravity sanitary-sewer or RDII engine |
| 6 | [USEPA/WNTR](https://github.com/USEPA/WNTR) | Python EPANET-compatible network construction, pump/pipe scenarios, leaks, pressure-dependent analysis, resilience, and result comparison | The official I&I residual, RTK, or wet-well storage method |
| 7 | [e2nIEE/pandapipes](https://github.com/e2nIEE/pandapipes) | A second independent pipe-network and pump cross-check, especially during validation | A drop-in sewer model or a currently validated authority for wastewater pump stations |
| 8 | [ImperialCollegeLondon/SWMManywhere](https://github.com/ImperialCollegeLondon/SWMManywhere) | Synthetic or incomplete-network model generation, research scenarios, and GIS-derived starting points | An as-built system of record |
| 9 | [kLabUM/pystorms](https://github.com/kLabUM/pystorms) | Testing and benchmarking control strategies against curated SWMM scenarios | Authority to control a live pump station |
| 10 | [rtc-tools/rtc-tools](https://github.com/rtc-tools/rtc-tools) | Offline optimization and model-predictive-control research for pumps, storage, and networks | A permitted control action or a replacement for station safeguards |
| 11 | [geopandas/geopandas](https://github.com/geopandas/geopandas), [postgis/postgis](https://github.com/postgis/postgis), and [networkx/networkx](https://github.com/networkx/networkx) | Basin, sewer, station, force-main, and dependency topology | Hydraulic truth without elevations, diameters, roughness, connectivity QA, and field validation |
| 12 | [unionai-oss/pandera](https://github.com/unionai-oss/pandera), [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations), and [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) | Data contracts, quality checks, and calculation provenance | Engineering acceptance or professional judgment |

---

## 4. Repository inventory by engineering function

## 4.1 Sewer hydraulics, rainfall-runoff, RDII, and RTK

### 4.1.1 `USEPA/Stormwater-Management-Model`

- **Repository:** [USEPA/Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model)
- **Class:** A - core candidate
- **Language/license:** C; public-domain release statement in the repository
- **What it provides:** the official U.S. EPA SWMM solver for single-event and continuous simulation of runoff, stormwater, wastewater, and combined collection systems.
- **Bible connection:** `F-RTK-001` through `F-RTK-003`, `F-MASS-001`, `F-MANNING-001`, dynamic sewer routing, node depth, conduit flow, surcharge, flooding, storage, and pump/link behavior.
- **Recommended use:** run a pinned solver build as a separately versioned calculation engine. Record solver version, source commit, build hash, model hash, options, time step, continuity errors, warnings, and output hash in every run manifest.
- **Critical boundary:** SWMM can execute an RDII model, but it does not prove that selected R, T, and K values are calibrated or that rainfall and flow observations are valid.

### 4.1.2 `pyswmm/Stormwater-Management-Model`

- **Repository:** [pyswmm/Stormwater-Management-Model](https://github.com/pyswmm/Stormwater-Management-Model)
- **Class:** A/B - community solver candidate
- **Language/license:** C/C++; repository describes a combination of MIT and public-domain terms
- **What it provides:** Open Water Analytics/PySWMM community development of the SWMM solver, regression tests, builds, and APIs used by the PySWMM ecosystem.
- **Bible connection:** the same sewer and RDII formula families as the EPA solver.
- **Recommended use:** evaluate as the application-facing SWMM build where its packaging or API support is advantageous, while retaining regression comparison against the official EPA release.
- **Critical boundary:** do not mix solver builds within one validation series without recording the engine and demonstrating result equivalence or explaining differences.

### 4.1.3 `pyswmm/pyswmm`

- **Repository:** [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm)
- **Class:** A - adapter
- **Language/license:** Python; BSD-2-Clause
- **What it provides:** Python wrappers that step through SWMM simulations, inspect nodes and links, introduce controlled inflows, extract binary output, and implement external control logic.
- **Bible connection:** orchestration around `F-RTK-003`, dynamic station inflow, storage routing, event replay, scenario comparison, and dashboard time series.
- **Recommended use:** build a thin APAS adapter around a pinned PySWMM version. The adapter should translate APAS contracts into SWMM input, execute the model, capture logs, and translate output into immutable result contracts.
- **Critical boundary:** PySWMM wraps SWMM. It does not create a second independent hydraulic answer.

### 4.1.4 `pyswmm/swmmio`

- **Repository:** [pyswmm/swmmio](https://github.com/pyswmm/swmmio)
- **Class:** B - model I/O
- **Language/license:** Python; MIT
- **What it provides:** DataFrame and GeoDataFrame access to SWMM input and report sections, programmatic editing, analysis, and visualization.
- **Bible connection:** `DS-03` basin and sewer inventory, model preparation, model-difference reports, topology QA, and dashboard mapping.
- **Recommended use:** candidate for model ingestion, normalization, controlled model edits, and readable diff generation.
- **Critical boundary:** editing a valid text file is not the same as creating a calibrated model. Every generated or changed model still needs hydraulic and engineering review.

### 4.1.5 `MarkusPic/swmm_api`

- **Repository:** [MarkusPic/swmm_api](https://github.com/MarkusPic/swmm_api)
- **Class:** B - model I/O and automation
- **Language/license:** Python; MIT
- **What it provides:** reading, manipulating, writing, running, and extracting SWMM INP, RPT, and OUT data, plus GIS-oriented functions.
- **Bible connection:** model ingestion, controlled batch runs, result extraction, input provenance, and spatial export.
- **Recommended use:** conduct a structured bake-off against `swmmio`. Test full round trips, unsupported sections, preservation of comments and units, large-model performance, binary-output compatibility, and failure behavior.
- **Critical boundary:** the GitHub repository identifies itself as a snapshot with the full source maintained elsewhere. APAS must decide whether an external GitLab source and release process are acceptable.

### 4.1.6 `mgeranmehr/swmmx_dev`

- **Repository:** [mgeranmehr/swmmx_dev](https://github.com/mgeranmehr/swmmx_dev)
- **Class:** C - emerging unified toolkit
- **Language/license:** Python; MIT
- **What it provides:** a newer toolkit for building, editing, running, importing, visualizing, and exporting SWMM models.
- **Bible connection:** potential consolidation of model-builder and runner functions.
- **Recommended use:** evaluate in a sandbox and contribute tests or issues if useful.
- **Critical boundary:** its own repository warns that it is under active testing and development. It is not a preferred first production dependency for material calculations until APAS completes a validation program.

### 4.1.7 `ImperialCollegeLondon/SWMManywhere`

- **Repository:** [ImperialCollegeLondon/SWMManywhere](https://github.com/ImperialCollegeLondon/SWMManywhere)
- **Class:** B/C - network synthesis
- **Language/license:** Python; BSD-3-Clause
- **What it provides:** synthesis of urban drainage models from public street, elevation, and building data, generation of SWMM inputs, and comparison with known models.
- **Bible connection:** `DS-03` provisional basin/network inventory, missing-model research, scenario generation, and spatial sensitivity studies.
- **Recommended use:** generate a provisional research model when as-built information is missing, with every synthetic attribute explicitly labeled and prevented from silently entering an approved engineering model.
- **Critical boundary:** a synthesized network is not an as-built network, a record drawing, a survey, or a field-verified sewer inventory.

### 4.1.8 `AaltoUrbanWater/GisToSWMM5`

- **Repository:** [AaltoUrbanWater/GisToSWMM5](https://github.com/AaltoUrbanWater/GisToSWMM5)
- **Class:** B/C - GIS model preparation
- **What it provides:** automated subcatchment generation for SWMM from GIS data.
- **Bible connection:** basin delineation and model preprocessing.
- **Recommended use:** research and model-preparation comparison, particularly where the utility already has high-quality GIS layers.
- **Critical boundary:** applicability, maintenance activity, units, coordinate systems, and generated assumptions require review before use.

### 4.1.9 `kLabUM/pystorms`

- **Repository:** [kLabUM/pystorms](https://github.com/kLabUM/pystorms)
- **Class:** C - control benchmark
- **Language/license:** Python/Jupyter; GPL-3.0
- **What it provides:** curated SWMM control scenarios and a simulation sandbox for comparing stormwater control algorithms.
- **Bible connection:** scenario testing for pump, gate, valve, storage, and wet-weather control recommendations.
- **Recommended use:** offline controller benchmarking and regression scenarios.
- **Critical boundary:** GPL obligations require legal review, and benchmark success does not authorize live control.

### 4.1.10 `UVAdMIST/swmm_mpc`

- **Repository:** [UVAdMIST/swmm_mpc](https://github.com/UVAdMIST/swmm_mpc)
- **Class:** Archive/reference
- **What it provides:** a Python model-predictive-control package for EPA SWMM models.
- **Bible connection:** prior art for predictive control and storage/flow objectives.
- **Recommended use:** inspect algorithms and reproduce research where helpful.
- **Critical boundary:** the repository has been inactive for years; do not make it a new production foundation.

### 4.1.11 `kLabUM/BaeOpt`

- **Repository:** [kLabUM/BaeOpt](https://github.com/kLabUM/BaeOpt)
- **Class:** C - calibration and control research
- **What it provides:** Bayesian approaches for calibration and control of stormwater networks.
- **Bible connection:** RTK/SWMM parameter search, uncertainty exploration, and controller research.
- **Recommended use:** research comparison for parameter-search strategies.
- **Critical boundary:** a notebook or research implementation does not define APAS calibration acceptance criteria, parameter bounds, identifiability, validation events, or uncertainty reporting.

### 4.1.12 `hzambran/hydroPSO`

- **Repository:** [hzambran/hydroPSO](https://github.com/hzambran/hydroPSO)
- **Class:** B/C - model-independent calibration
- **Language:** R
- **What it provides:** particle-swarm optimization, parallel model execution, sensitivity, and calibration for external environmental models.
- **Bible connection:** possible SWMM or RTK parameter search around an approved objective function.
- **Recommended use:** comparative calibration research where an R execution boundary is acceptable.
- **Critical boundary:** optimization finds parameters that improve the selected objective. It does not establish uniqueness, physical plausibility, or predictive validity.

### 4.1.13 `conradwasko/hydroEvents`

- **Repository:** [conradwasko/hydroEvents](https://github.com/conradwasko/hydroEvents)
- **Class:** B/C - event extraction
- **Language:** R
- **What it provides:** precipitation and flow event extraction and hydrograph-oriented event functions.
- **Bible connection:** candidate concepts for event segmentation before `F-RDII-001` through `F-RDII-003`.
- **Recommended use:** compare its event-separation behavior with the APAS event contract.
- **Critical boundary:** the I&I application still needs a U.S.-utility-specific event definition, antecedent-dry-period rule, clock handling, missing-data rule, and approval state.

---

## 4.2 Force mains, pump curves, system curves, and operating points

### 4.2.1 `CalebBell/fluids`

- **Repository:** [CalebBell/fluids](https://github.com/CalebBell/fluids)
- **Class:** A - engineering primitive library
- **Language/license:** Python; MIT
- **What it provides:** friction factors, Reynolds-number-dependent methods, piping and fitting losses, valves, pumps, tanks, flow meters, open-channel functions, and fluid-property utilities.
- **Bible connection:** `F-HYD-001` circular-pipe area/velocity/Reynolds number, `F-HYD-002` friction factor, `F-HYD-003` Darcy-Weisbach major loss, `F-HYD-004` minor loss, and reference calculations for `F-HYD-005` system head.
- **Recommended use:** wrap only explicitly accepted functions. Pin the method selected for every correlation; store its citation/method identifier; convert into APAS units at the boundary; and compare outputs with hand calculations and a second engine.
- **Critical boundary:** a library containing many valid correlations cannot select the correct correlation or coefficient for the actual force main without an approved method and verified asset data.

### 4.2.2 `OpenWaterAnalytics/EPANET`

- **Repository:** [OpenWaterAnalytics/EPANET](https://github.com/OpenWaterAnalytics/EPANET)
- **Class:** A - pressurized-network solver and cross-check
- **Language/license:** C; MIT
- **What it provides:** actively maintained EPANET hydraulic and water-quality solver and programmer toolkit.
- **Bible connection:** pump curves, controls, parallel pumps, pressurized-pipe losses, tanks, extended-period operation, and cross-checks for `F-HYD-005`, `F-PUMP-001`, `F-PUMP-002`, and `F-ENERGY-001`.
- **Recommended use:** create a small force-main model from the same approved PumpOS inputs and compare its operating point, total head, flow, and energy with the PumpOS formula service.
- **Critical boundary:** EPANET is primarily a pressurized water-distribution engine. Its demand and network assumptions are not the same as gravity sewer, RDII, wet-well routing, solids, gas, or wastewater pump-station behavior.

### 4.2.3 `USEPA/EPANET2.2`

- **Repository:** [USEPA/EPANET2.2](https://github.com/USEPA/EPANET2.2)
- **Class:** Archive/reference
- **Language/license:** C/Delphi materials; MIT
- **What it provides:** the official EPA 2.2.0 release source and documentation archive.
- **Bible connection:** authoritative release comparison and documentation baseline.
- **Recommended use:** retain as a reference and regression target where official 2.2 behavior matters.
- **Critical boundary:** the repository describes itself as an archive. New development should normally evaluate the active OWA EPANET line while preserving the official EPA reference.

### 4.2.4 `USEPA/WNTR`

- **Repository:** [USEPA/WNTR](https://github.com/USEPA/WNTR)
- **Class:** A/B - Python simulation and resilience
- **Language:** Python
- **What it provides:** EPANET-compatible network construction, simulation, pressure-dependent demand, leaks, disruptive events, response/repair strategies, resilience metrics, and visualization.
- **Bible connection:** force-main and pump scenarios, sensor-placement research, pump-lineup perturbations, resilience analysis, and a Python-accessible comparison engine.
- **Recommended use:** create test networks and evaluate whether the PumpOS operating-point and energy results remain consistent under defined scenarios.
- **Critical boundary:** drinking-water resilience constructs must not be relabeled as wastewater station requirements without an approved mapping.

### 4.2.5 `KIOS-Research/EPyT`

- **Repository:** [KIOS-Research/EPyT](https://github.com/KIOS-Research/EPyT)
- **Class:** B - Python EPANET toolkit
- **What it provides:** Python access to EPANET functions and model analysis.
- **Bible connection:** programmatic pump-curve and pressurized-network runs.
- **Recommended use:** compare ergonomics, coverage, packaging, version support, and numerical equivalence with WNTR before choosing a Python EPANET adapter.
- **Critical boundary:** avoid carrying multiple EPANET Python wrappers unless each has a distinct, tested responsibility.

### 4.2.6 `WaterFutures/EPyT-Flow`

- **Repository:** [WaterFutures/EPyT-Flow](https://github.com/WaterFutures/EPyT-Flow)
- **Class:** B/C - scenario and sensor research
- **Language/license:** Python; MIT
- **What it provides:** high- and low-level EPANET access, hydraulic and water-quality scenario data, sensors, leaks, faults, uncertainty, control environments, and a REST interface.
- **Bible connection:** SCADA-like scenario generation, sensor faults, uncertainty, event diagnosis, and controller testing for pressurized networks.
- **Recommended use:** research synthetic pump/force-main telemetry and fault-detection workflows.
- **Critical boundary:** its water-distribution scenarios are not automatically representative of wastewater force mains, wet wells, ragging, solids, or station controls.

### 4.2.7 `OpenWaterAnalytics/EPANET-Matlab-Toolkit`

- **Repository:** [OpenWaterAnalytics/EPANET-Matlab-Toolkit](https://github.com/OpenWaterAnalytics/EPANET-Matlab-Toolkit)
- **Class:** B - MATLAB adapter
- **What it provides:** MATLAB access to EPANET simulation libraries.
- **Bible connection:** independent prototype and comparison environment for engineering teams with existing MATLAB models.
- **Recommended use:** validation bridge when legacy pump or network analyses are in MATLAB.
- **Critical boundary:** it should not create a second production formula registry.

### 4.2.8 `epanet-js/epanet-js-toolkit`

- **Repository:** [epanet-js/epanet-js-toolkit](https://github.com/epanet-js/epanet-js-toolkit)
- **Class:** B - browser/Node adapter
- **Language/license:** TypeScript/WebAssembly; toolkit identified as MIT
- **What it provides:** OWA EPANET compiled for JavaScript/WebAssembly with a TypeScript API for browser or Node execution.
- **Bible connection:** interactive pump/force-main model previews and browser-side hydraulic demonstrations.
- **Recommended use:** consider for an engineering sandbox or client-side visualization after server-side calculation authority is established.
- **Critical boundary:** distinguish the MIT toolkit from any separate source-available or commercial application layers. Do not make the browser result the sole authoritative calculation without a controlled build and parity tests.

### 4.2.9 `e2nIEE/pandapipes`

- **Repository:** [e2nIEE/pandapipes](https://github.com/e2nIEE/pandapipes)
- **Class:** B/C - independent pipe-network cross-check
- **Language/license:** Python; BSD-3-Clause
- **What it provides:** pipe-flow calculations for gas, heat, and water networks, including pumps, valves, controls, and pressure profiles.
- **Bible connection:** independent comparison of pipe losses, pump elements, network pressure, and operating scenarios.
- **Recommended use:** verification test harness and sensitivity research.
- **Critical boundary:** demonstrate the fluid model, pump model, friction formulation, units, boundary conditions, and wastewater applicability before relying on a result.

### 4.2.10 `lanl-ansi/WaterModels.jl`

- **Repository:** [lanl-ansi/WaterModels.jl](https://github.com/lanl-ansi/WaterModels.jl)
- **Class:** C - network optimization research
- **Language:** Julia/JuMP
- **What it provides:** steady-state water-network flow, optimal operation, and design formulations, including nonlinear, convex-relaxation, and piecewise-linear forms.
- **Bible connection:** pump scheduling, energy-cost optimization, design alternatives, and comparison of hydraulic optimization formulations.
- **Recommended use:** offline research after PumpOS has a stable scenario contract.
- **Critical boundary:** optimization formulations and relaxations may intentionally approximate the hydraulic equations. The selected formulation and solution gap must be visible.

### 4.2.11 `rtc-tools/rtc-tools`

- **Repository:** [rtc-tools/rtc-tools](https://github.com/rtc-tools/rtc-tools)
- **Class:** B/C - dynamic optimization framework
- **Language:** Python
- **What it provides:** simulation and optimization of dynamic systems, including reservoirs, pumps, and networks; supports goal programming and uncertainty.
- **Bible connection:** pump/storage scheduling, response-horizon optimization, energy objectives, and scenario recommendations.
- **Recommended use:** offline recommendation service behind a policy and approval boundary.
- **Critical boundary:** the optimization objective, constraints, forecast uncertainty, fallback state, and infeasibility behavior must be governed. The optimizer must never bypass PLC/RTU interlocks.

### 4.2.12 `meghnathomas/MILPNet`

- **Repository:** [meghnathomas/MILPNet](https://github.com/meghnathomas/MILPNet)
- **Class:** C - pump-scheduling research
- **What it provides:** mixed-integer linear approximations for water-network hydraulics and devices, with example pump scheduling.
- **Bible connection:** research for discrete lineup and schedule decisions.
- **Recommended use:** study the formulation and construct APAS-owned examples.
- **Critical boundary:** its documented implementation depends on Gurobi, which is not an open-source solver. The repository may be open source while the complete execution stack is not.

---

## 4.3 Numerical calculation, calibration, uncertainty, and tests

| Repository | Class | Use in the I&I system | Key boundary |
|---|---|---|---|
| [numpy/numpy](https://github.com/numpy/numpy) | A/D | Arrays, vectorized hydrographs, numerical data contracts | Not an engineering method |
| [scipy/scipy](https://github.com/scipy/scipy) | A/D | Root finding for pump/system-curve intersection, integration, interpolation, optimization, statistics | The selected algorithm, tolerances, bounds, and failure behavior must be registered |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | A/D | Time-series alignment, resampling, joins, event tables | Defaults can silently change clocks, null handling, and aggregation meaning |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) | B | Regression, time-series diagnostics, model statistics | Statistical association does not identify physical defects |
| [lmfit/lmfit-py](https://github.com/lmfit/lmfit-py) | B/C | Bounded nonlinear parameter fitting for pump curves or RTK experiments | Fit quality does not establish extrapolation validity or physical plausibility |
| [SALib/SALib](https://github.com/SALib/SALib) | B/C | Global sensitivity analysis for roughness, K values, RTK, rainfall, and curve uncertainty | Sensitivity results depend on declared distributions and ranges |
| [pydata/xarray](https://github.com/pydata/xarray) | D | Labeled multidimensional event/scenario ensembles | Does not validate coordinates or engineering meaning |
| [uncertainties/uncertainties](https://github.com/uncertainties/uncertainties) | B/C | Exploratory first-order uncertainty propagation | Must be checked against `F-UNC-001`, covariance assumptions, and nonlinear limitations |

### Required numerical rules for PumpOS

For `F-PUMP-001`, PumpOS should not merely call a generic root solver. The service must:

1. validate that the pump curve and system curve share compatible flow and head units;
2. identify the permitted interpolation domain;
3. reject unauthorized extrapolation;
4. find and report every intersection in the permitted domain;
5. apply an approved selection rule if more than one intersection exists;
6. record convergence tolerance and residual head mismatch;
7. verify that the result falls in an approved pump operating region;
8. propagate the operating point to capacity, storage, cycling, and energy formulas without premature rounding;
9. expose a trace showing the exact curve points, interpolation method, system inputs, and solver version.

SciPy can execute part of this procedure. It cannot define the procedure.

---

## 4.4 GIS, basin boundaries, sewer topology, and graph relationships

| Repository | Class | Recommended use | Bible connection |
|---|---|---|---|
| [geopandas/geopandas](https://github.com/geopandas/geopandas) | D | Read, transform, join, and analyze basin, parcel, sewer, station, rain-gauge, and inspection layers | `DS-02`, `DS-03`, basin/gauge association, dashboard maps |
| [shapely/shapely](https://github.com/shapely/shapely) | D | Geometry operations and spatial validation | Basin and asset geometry QA |
| [postgis/postgis](https://github.com/postgis/postgis) | D | Governed spatial system of record and server-side spatial queries | Basin, network, station, and evidence relationships |
| [qgis/QGIS](https://github.com/qgis/QGIS) | D | Desktop engineering review, model inspection, map production, and correction workflows | Human GIS review and provisional-to-approved asset workflow |
| [OSGeo/gdal](https://github.com/OSGeo/gdal) | D | Raster/vector conversion and coordinate-system handling | DEM, rainfall grids, imagery, and GIS ingestion |
| [networkx/networkx](https://github.com/networkx/networkx) | D | Directed sewer topology, upstream-trace, service-area dependency, and lineage graphs | basin-to-station and formula/source dependency paths |
| [KIOS-Research/ImportEpanetInpFiles](https://github.com/KIOS-Research/ImportEpanetInpFiles) | C | QGIS import/export experiments for EPANET INP data | Force-main/network visualization |

The graph used for physical network connectivity and the graph used for calculation provenance are related but not identical. PumpOS must preserve that distinction:

- the **physical graph** connects basins, pipes, manholes, stations, pumps, force mains, and discharge points;
- the **evidence graph** connects source records, normalized inputs, formulas, results, dashboard metrics, decisions, approvals, and versions.

NetworkX can calculate paths in either graph. It does not define which relationship types are permissible or which source is authoritative.

---

## 4.5 SCADA, RTU/PLC, telemetry, and time-series infrastructure

| Repository | Class | Potential role | Critical boundary |
|---|---|---|---|
| [eclipse-mosquitto/mosquitto](https://github.com/eclipse-mosquitto/mosquitto) | D | MQTT broker for bounded telemetry or event transport | MQTT alone does not provide industrial tag semantics, store-and-forward assurance, or control authorization |
| [eclipse-sparkplug/sparkplug](https://github.com/eclipse-sparkplug/sparkplug) | D | Sparkplug payload and state conventions over MQTT for industrial telemetry | Adoption must align with the utility's existing SCADA/OT architecture |
| [FreeOpcUa/opcua-asyncio](https://github.com/FreeOpcUa/opcua-asyncio) | D | Python OPC UA client/server integration | Read-only integration should be separated from any write/control path |
| [OPCFoundation/UA-.NETStandard](https://github.com/OPCFoundation/UA-.NETStandard) | D | OPC UA integration in .NET environments | Certificate, identity, endpoint, and OT security governance are mandatory |
| [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | D | IoT telemetry, device management, rule chains, and dashboards | Not a replacement for utility SCADA, historian, or approved alarm management |
| [influxdata/influxdb](https://github.com/influxdata/influxdb) | D | High-frequency time-series storage and query | Review current edition, license, clustering, retention, and operational model |
| [timescale/timescaledb](https://github.com/timescale/timescaledb) | D | PostgreSQL-based time-series storage and continuous aggregation | Review current license boundaries and feature editions |
| [apache/iotdb](https://github.com/apache/iotdb) | D | Industrial time-series database | Adds another operational platform that must be justified against existing utility systems |
| [grafana/grafana](https://github.com/grafana/grafana) | D | Engineering observability and early dashboard prototypes | The production PumpOS dashboard must still enforce metric lineage, approval state, and role-based interpretation |

### Recommended OT boundary

The I&I Intelligence System should initially consume approved, read-only replicated telemetry rather than connect the agent directly to a live control channel. A safe high-level pattern is:

```text
PLC / RTU / SCADA
        |
        | approved read-only replication
        v
Historian or operational data gateway
        |
        | quality flags + original timestamp + ingest timestamp
        v
PumpOS normalized time-series service
        |
        +--> deterministic calculations
        +--> SWMM/EPANET scenario services
        +--> dashboards and lineage
        +--> agent explanation

No agent-to-PLC write path in the initial architecture.
```

---

## 4.6 Data quality, workflow, reproducibility, and lineage

| Repository | Class | Potential role | Critical boundary |
|---|---|---|---|
| [unionai-oss/pandera](https://github.com/unionai-oss/pandera) | D | DataFrame schemas for units, ranges, nullable fields, clocks, and accepted data states | A valid schema does not mean a sensor is calibrated |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | D | Batch data-quality suites and evidence reports | Expectations must be engineering-owned and versioned |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | D | API and calculation-contract validation | Type correctness is not hydraulic correctness |
| [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) | D | Standardized job/dataset lineage events | Formula-, metric-, and approval-level lineage still needs the APAS domain model |
| [MarquezProject/marquez](https://github.com/MarquezProject/marquez) | D | OpenLineage metadata collection and exploration | Evaluate scale, access control, and domain-extension needs |
| [dagster-io/dagster](https://github.com/dagster-io/dagster) | D | Asset-oriented pipelines, partitions, sensors, and run metadata | Scheduler success does not approve an engineering result |
| [apache/airflow](https://github.com/apache/airflow) | D | Scheduled and dependency-based batch workflows | Less naturally domain-oriented than a calculation-specific service; compare before selecting |
| [temporalio/temporal](https://github.com/temporalio/temporal) | D | Durable long-running workflows and human approval waits | Workflow durability does not define approval authority |
| [neo4j/neo4j](https://github.com/neo4j/neo4j) | D | Property-graph storage and traversal | Review Community Edition license and deployment boundaries |
| [apache/age](https://github.com/apache/age) | D | Graph relationships within PostgreSQL | Validate maturity, operational support, and query needs before preferring it over relational tables |

The calculation record must remain reproducible even if the workflow or graph platform changes. At minimum, every material result should preserve:

- source record identifiers and hashes;
- original and normalized values;
- units and conversion identifiers;
- quality flags and acceptance state;
- basin, station, pump, force-main, and event boundaries;
- formula and method identifiers;
- formula-registry version;
- solver/library versions and source commits;
- parameter-set version and approval;
- result values at full retained precision;
- warnings, exclusions, residuals, and fail-closed outcomes;
- dashboard metric identifiers;
- decision and approval records.

---

## 4.7 Agent frameworks

| Repository | Class | Potential role | Prohibited role |
|---|---|---|---|
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | D | Stateful agent workflow, tool routing, review checkpoints, and resumable analysis | Numerical authority or direct station control |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | D | Typed agent inputs, outputs, tools, and result validation | Proof that a hydraulic result is correct |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | D | Standardized tool exposure to the agent | Authorization to use every exposed tool |

The agent layer should receive tools such as:

- `get_approved_event(event_id)`;
- `get_station_configuration(station_id, effective_time)`;
- `run_formula(formula_id, approved_input_set_id)`;
- `run_swmm(model_version_id, event_id, scenario_id)`;
- `compare_operating_point(run_a, run_b)`;
- `trace_metric(metric_id, run_id)`;
- `open_data_gap(case_id)`;
- `prepare_recommendation(case_id)`;
- `route_for_approval(recommendation_id)`.

It should not receive an unrestricted “execute arbitrary formula,” “write arbitrary SCADA tag,” or “change approved coefficient” tool.

---

## 5. Direct mapping from the Bible's formula families to repositories

| Bible formula family | Primary APAS implementation | Open-source engine/reference | Intended use |
|---|---|---|---|
| `F-UNIT-001`, `F-CONV-001` | PumpOS formula service | NumPy/Pint if selected | Unit-safe deterministic calculation and tests |
| `F-FLOW-001`, `F-DWF-001`, `F-RDII-001` to `003`, `F-GWI-001` | PumpOS I&I service | pandas, NumPy, SciPy | Clock alignment, integration, baseline, residual, event volume, capture |
| `F-RTK-001` to `003` | PumpOS RTK service with approved parameter registry | EPA SWMM; PySWMM | Independent event hydrograph execution and model comparison |
| `F-MASS-001`, `F-MANNING-001` | PumpOS calculation where simple; SWMM for dynamic network routing | EPA SWMM | Sewer hydraulics and storage continuity |
| `F-HYD-001` to `005` | PumpOS system-curve service | `fluids`; EPANET; WNTR; pandapipes | Primitive calculations plus at least two cross-check paths |
| `F-PUMP-001`, `002` | PumpOS operating-point and capacity service | SciPy root finding; EPANET/WNTR | Curve intersection, lineup scenarios, comparison |
| `F-PUMP-003`, `004`, `007` | PumpOS wet-well/storage service | SWMM storage routing; PySWMM | Static screening plus dynamic event routing |
| `F-PUMP-005`, `006`, `F-MDC-NAPOT-001` | PumpOS operations service | pandas/NumPy | Cycling, runtime, and jurisdiction-controlled operational calculations |
| `F-ENERGY-001`, `002` | PumpOS energy service | `fluids`; EPANET energy output where applicable | Power, energy, cost, and operating-point dependency |
| `F-COST-001`, `F-PV-001`, `F-BCR-001`, `F-ECON-002` to `004` | PumpOS economics service | NumPy/SciPy | Controlled economic scenario calculations |
| `F-UNC-001` | PumpOS uncertainty service | SALib; `uncertainties`; SciPy | Propagation, sensitivity, and scenario envelopes |
| `F-VERIFY-001` | PumpOS verification service | pandas/statsmodels | Before/after weather-normalized evaluation |

---

## 6. Recommended PumpOS repository architecture

```text
APAS-owned repositories
|
+-- ii-contracts
|   +-- source schemas
|   +-- formula registry
|   +-- unit registry
|   +-- result schemas
|   +-- metric and decision lineage
|
+-- ii-calculation-kernel
|   +-- baseline and RDII
|   +-- RTK
|   +-- system curve
|   +-- pump operating point
|   +-- storage and overflow
|   +-- cycling and energy
|   +-- economics and uncertainty
|
+-- ii-model-adapters
|   +-- SWMM adapter
|   +-- EPANET/WNTR comparison adapter
|   +-- GIS adapter
|   +-- SCADA/historian read adapter
|
+-- ii-validation
|   +-- hand-calculation fixtures
|   +-- EPA/OWA regression models
|   +-- cross-engine comparisons
|   +-- numerical tolerance reports
|   +-- golden dashboard values
|
+-- ii-workflows
|   +-- event acceptance
|   +-- model/calibration approval
|   +-- scenario execution
|   +-- recommendation approval
|   +-- post-project verification
|
+-- ii-agent
    +-- bounded tools
    +-- explanation and trace
    +-- data-gap detection
    +-- recommendation drafting
    +-- no numerical kernel
    +-- no direct control writes
```

The open-source repositories should be dependencies behind these APAS boundaries. They should not become the boundaries.

---

## 7. Proof-of-concept dependency stack

### 7.1 Calculation and modeling

- Python 3.12 or an APAS-approved long-term runtime
- NumPy, pandas, SciPy
- `fluids`
- official EPA SWMM solver
- PySWMM
- one selected SWMM I/O package after the `swmmio` versus `swmm_api` bake-off
- WNTR with a pinned EPANET engine for cross-checking
- optional pandapipes validation environment

### 7.2 Data and spatial

- PostgreSQL and PostGIS
- one deliberate time-series strategy: native PostgreSQL partitioning, TimescaleDB, InfluxDB, or an existing utility historian
- GeoPandas, Shapely, GDAL, and NetworkX
- Pandera or Pydantic at calculation boundaries

### 7.3 Workflow, provenance, and dashboards

- OpenLineage-compatible events or an APAS equivalent
- a durable workflow engine selected after a Dagster/Temporal comparison
- Grafana for early engineering observability if useful
- PumpOS-native production dashboards for governed metric display

### 7.4 Agent

- a typed, stateful agent framework selected after a small LangGraph/PydanticAI proof of concept
- tool calls only to approved PumpOS services
- immutable run and trace identifiers returned with every answer

---

## 8. Repositories that should not be confused with production authority

The following types of repository may be useful but require an explicit warning label:

- student or single-notebook pump-curve examples;
- repositories with no declared license;
- repositories that fit a polynomial to a pump curve without domain and monotonicity controls;
- optimization demos that require proprietary solvers;
- abandoned SWMM wrappers tied to an old solver;
- browser demonstrations without pinned engine parity tests;
- generic AI agents that generate calculations in text;
- research controller code without operational interlocks;
- synthetic sewer-network generators used as if they were as-built records;
- dashboards that recompute values independently of the formula registry.

No repository should be embedded merely because it has a familiar formula or a plausible graph. For the I&I Intelligence System, admissibility requires provenance, unit control, repeatability, tests, failure rules, and engineering review.

---

## 9. Required repository evaluation scorecard

Before APAS adopts any candidate, score it against the following:

| Area | Questions |
|---|---|
| Scope | Does the repository solve the exact physical or workflow problem, or only an adjacent one? |
| Method | Which equations, correlations, solvers, interpolation rules, and defaults are implemented? |
| Units | Are U.S. customary and SI units explicit and tested? Can mixed-unit input fail closed? |
| Verification | Are there tests against published examples, EPA examples, analytical solutions, or another engine? |
| Numerical behavior | What are the tolerances, time steps, convergence rules, extrapolation behavior, and discontinuities? |
| Data contract | Can every input and output be mapped to `DS-01` through `DS-11` and a formula/result schema? |
| Provenance | Can the exact source version, build, model, parameters, and run settings be recorded? |
| Activity | Is the project maintained, and are releases, security issues, and compatibility changes visible? |
| License | Can APAS embed, modify, distribute, host, and commercially operate it under the intended architecture? |
| Security | What native-code, file-parsing, network, plugin, and supply-chain risks are introduced? |
| Performance | Can it process the expected station count, event count, time resolution, and scenario volume? |
| Failure behavior | Does it expose invalid input, nonconvergence, continuity error, missing data, or an empty result? |
| Explainability | Can the result be traced to physical inputs and a registered method rather than only a model score? |
| Replaceability | Is it behind an APAS adapter so it can be upgraded or replaced without changing the domain contract? |

---

## 10. Recommended next implementation sequence

1. **Freeze the formula and data contracts first.** Convert the Bible's 39 formulas and 11 source classes into executable schemas and acceptance tests.
2. **Build a PumpOS-owned system-curve kernel.** Implement `F-HYD-001` through `F-HYD-005` and `F-PUMP-001` with explicit units, curve domains, interpolation rules, root-selection rules, and fail-closed states.
3. **Create independent cross-check fixtures.** Reproduce the Bible's sample station in `fluids`, EPANET/WNTR, and pandapipes where applicable. Differences must be explained, not averaged.
4. **Pin and wrap EPA SWMM.** Create a run manifest and a small set of EPA and APAS golden models, including an RDII/RTK event and a wet-well routing case.
5. **Select one SWMM model I/O package.** Run the `swmmio` and `swmm_api` bake-off before creating broad dependencies.
6. **Build source adapters in read-only mode.** Start with exported SCADA/historian, rainfall, pump-curve, GIS, wet-well, and force-main records.
7. **Make dashboard numbers come only from result contracts.** No dashboard-specific calculation logic.
8. **Add lineage and approval workflows.** Every dashboard metric should trace through a result to a formula, parameter set, source record, and approval state.
9. **Add the agent last.** Give it tools to retrieve, run, compare, trace, explain, and route approval; never give it authority to invent or silently modify engineering inputs.
10. **Run a basin-and-station pilot.** Use one real basin and one station, preserve the paper's numbered dashboard values as golden fixtures, and compare modeled outputs with accepted field evidence.

---

## 11. Bottom-line selection

If APAS starts with only six external technical dependencies, they should be:

1. [USEPA/Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model);
2. [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm);
3. one of [pyswmm/swmmio](https://github.com/pyswmm/swmmio) or [MarkusPic/swmm_api](https://github.com/MarkusPic/swmm_api), selected by tests;
4. [CalebBell/fluids](https://github.com/CalebBell/fluids);
5. [OpenWaterAnalytics/EPANET](https://github.com/OpenWaterAnalytics/EPANET) through [USEPA/WNTR](https://github.com/USEPA/WNTR) for cross-checks;
6. the standard NumPy/pandas/SciPy numerical stack.

Everything else should be added only when a defined capability, validation plan, and ownership boundary require it.

