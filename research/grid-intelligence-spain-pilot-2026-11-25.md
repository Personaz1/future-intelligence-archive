# Grid Intelligence: Spain pilot research brief
Date: 2026-11-25
Status: hypothesis / desk-research stage; no product claims validated.

## Working thesis

Build a decision-support layer for electricity infrastructure: combine grid topology, published access capacity, demand/generation/storage data, constraints, land/site context, and time-series market data to screen locations and projects before expensive engineering due diligence.

The product is **not** another map of spare capacity. Published capacity is informational, nodal values are interdependent, and only the relevant network operator's project-specific study determines whether access is granted.

## Initial geography

Pilot: Alicante province, Valencian Community, Spain.

Reasons:
- A bounded geography makes source reconciliation and field validation tractable.
- Official i-DE demand-capacity material for Alicante exposes municipality, UTM coordinates, substation, voltage level, firm available capacity, occupied/unassessed demand capacity, positions, node and connection-point identifiers.
- REE's November 2026 transmission-generation capacity publication includes ELCHE 220 and ELDA 220 nodes.

## Initial data inventory

### Network access / capacity
- CNMC monthly access-and-connection maps for demand and generation, across transmission and distribution. CNMC explicitly warns values are informational and cannot be summed directly because nodes influence one another.
- REE transmission-node access-capacity tables for demand, generation and storage, including CSV/XLSX/PDF publications and explanatory methodology.
- DSO maps and tables: i-DE, e-distribución, e-redes, UFD. Coverage and reuse terms must be checked operator by operator.

### System operation / market
- REE REData REST API: demand, generation mix, exchanges, market indicators and historical time series.
- ESIOS: market indicators and electricity-system transparency.
- ENTSO-E Transparency Platform: European generation, load, transmission, balancing and cross-border data; API requires registration/token.

### Geographic / contextual layers to investigate
- Official substation and transmission-line geometry; voltage classes; distribution network where legally reusable.
- Cadastre/land parcels, zoning and protected areas.
- Flood, wildfire, environmental and planning constraints.
- Renewable resource, industrial demand, logistics, water availability and access.
- Grid reinforcement and planned infrastructure, with dates and confidence labels.

## Product wedge to test

**Preliminary site and project feasibility screening** for:
- battery energy storage systems (BESS),
- large electricity consumers (data centres, industrial facilities, EV charging),
- solar/wind generation.

For a selected site and target power, produce:
1. nearest relevant substations/nodes and voltage levels;
2. published access-capacity signals by direction and technology;
3. known shared-zone, position, short-circuit, static/dynamic or other constraints where published;
4. nearby generation, demand and storage context;
5. time-stamped evidence and provenance for every data point;
6. missing-data list and uncertainty classification;
7. a clear warning that screening is not a connection offer or engineering approval.

## Competitive landscape — first pass, not exhaustive

- CNMC / REE and DSOs already publish official capacity maps and tables.
- Noda markets AI-assisted site/network/permitting intelligence.
- GridCapacity API aggregates operator capacity publications into a normalized API.
- Ampervia publishes Spain capacity analysis and site-screening-oriented datasets.
- Wood Mackenzie, Modo Energy and specialist engineering consultancies address adjacent grid, storage and market analytics.

Therefore, a generic capacity map, normalized table or generic energy dashboard is not a defensible wedge. Differentiation must come from project-specific interpretation, source reconciliation, historical change tracking, local site constraints, uncertainty/provenance, and workflow integration.

## First experiments

### Experiment 1 — data audit for Alicante
- Download latest CNMC demand/generation layers.
- Download latest REE demand/generation/storage tables and zone dictionaries.
- Obtain latest i-DE Alicante distribution tables for both demand and generation.
- Normalize identifiers, coordinates, units, voltage levels, timestamps and definitions.
- Identify coverage gaps, duplicate nodes, inconsistent values and update cadence.
- Produce a source-to-field lineage matrix.

### Experiment 2 — one real site screening
Choose one publicly documented industrial/energy site in Alicante (not a private address). Evaluate a hypothetical 5 MW, 20 MW and 50 MW demand or BESS project. Show what can and cannot be inferred from public sources. Do not represent any estimate as confirmed connection capacity.

### Experiment 3 — time-series value
Track monthly changes in published node capacity and compare with REE demand, generation mix, prices, curtailment/congestion signals and announced projects. Test whether the combined view reveals actionable changes not obvious in any single source.

## Go / no-go criteria

Continue only if the pilot demonstrates at least one of:
- materially faster or cheaper preliminary screening than current manual research;
- a useful signal unavailable in any single official source;
- measurable historical or predictive value;
- a buyer who confirms willingness to pay for the report/workflow.

Stop or reposition if the product is merely repackaging public maps, if data rights prevent commercial reuse, or if the output cannot be distinguished from a disclaimer-heavy generic report.

## Core technical distinctions

Never conflate:
- installed generation capacity (MW),
- instantaneous generation/load (MW),
- energy produced/consumed over time (MWh),
- thermal transfer capability / hosting capacity,
- access capacity available for a new request,
- granted access capacity,
- commissioned/operational capacity,
- connection bay/position availability.

Capacity is directional and technology-/scenario-dependent. Demand, generation and storage are not interchangeable. Nodal values may share constraints and must not be summed as independent quantities.

## Primary sources

- CNMC access and connection information: https://www.cnmc.es/sectores-que-regulamos/energia/supervision-del-mercado-electrico/informe-acceso-y-conexion-redes
- REE demand access capacity: https://www.ree.es/es/clientes/consumidor/acceso-conexion/conoce-la-capacidad-de-acceso
- REE generation access capacity: https://www.ree.es/es/clientes/generador/acceso-conexion/conoce-la-capacidad-de-acceso
- REE REData API: https://www.ree.es/es/datos/apidatos
- ENTSO-E data portal: https://www.entsoe.eu/data/
- i-DE Alicante demand capacity publication (example, 2026-04-01): https://www.i-de.es/documents/d/guest/2026_04_01_r1-001_demanda

## Open questions

1. What are the current commercial reuse terms for each DSO dataset?
2. Can we obtain reliable geospatial network topology, not just node points?
3. Which exact buyer has the most expensive early-stage site-selection mistake?
4. Can we quantify the accuracy and usefulness of a preliminary screen against real engineering studies?
5. Is the defensible asset a dataset, a scoring model, a workflow, or a combination?


## Additional verified GIS sources (checked 2026-11-25)

REE exposes public ArcGIS REST feature layers for transmission assets:
- Transmission substations: layer 3, point geometry.
- Transmission circuits: layer 11, polyline geometry.
- Service directory: https://georedservices.ree.es/arcgis_ags1/rest/services/WEBREE/Instalaciones_RdT_WEBREE/MapServer/layers
- Circuit attributes include voltage classes (30, 66, 110, 132, 150, 220, 400 kV); supported query formats include JSON and GeoJSON.
- These are transmission assets, not a complete distribution network.

A second REE detail service exposes substation layer 1 and circuit layer 36:
https://georedservices.ree.es/arcgis_ags2/rest/services/Zonas_de_detalle_WEBREE_MIL1/MapServer/layers

e-distribución publishes monthly downloadable capacity files:
- Generation: https://www.edistribucion.com/es/red-electrica/nodos-capacidad-red/capacidad-generacion.html
- Demand: https://www.edistribucion.com/es/red-electrica/nodos-capacidad-red/capacidad-demanda.html
Its November 2026 generation page advertises CSV/XLSX files and warns that capacities are not cumulative/simultaneous; one connection can affect nearby nodes.

## Repository implementation started

- `research/spain-grid-data-catalog.md`: verified official source inventory and ingestion caveats.
- `research/grid-intelligence-data-model.md`: canonical schema with provenance and capacity semantics.
- `research/grid-intelligence/README.md`: workstream index and build sequence.
- `experiments/ree_transmission_geojson.py`: first extractor for REE transmission substations/circuits. Current bounding box covers mainland Spain and Balearic area; it excludes the Canary Islands. It has not yet been executed or validated against a live download.

This is a first implementation scaffold, not yet a populated national dataset.
