# Grid Intelligence — Spain

Research and prototype work on Spanish electricity infrastructure, grid topology, access capacity, power flows, generation, demand and storage.

## Current status — 2026-11-25

We have verified that useful official sources exist at three distinct layers:

1. **Physical transmission topology:** REE ArcGIS REST layers for substations (point features) and circuits (line features), including voltage attributes.
2. **Access capacity:** CNMC national monthly maps plus operator-level CSV/XLSX publications. These describe indicative access capacity, not guaranteed connection rights.
3. **System operation:** REE REData REST API for time-series demand, generation and other system indicators.

This is enough to begin assembling a source-grounded national data model. It is not yet a complete Spanish grid digital twin: distribution topology, source reuse terms, data completeness and node identity reconciliation remain open. Commercial reuse is a separate gate: e-distribución and i-DE publish explicit restrictions on commercial use without authorization, while REE source rights need source-specific review. Do not treat public downloads as an open commercial dataset.

## Repository map

- [Spain grid data source catalog](../spain-grid-data-catalog.md) — official portals, service endpoints, caveats and ingestion rules.
- [Canonical data model](../grid-intelligence-data-model.md) — nodes, circuits, capacity observations, evidence and semantic distinctions.
- [Spain pilot research brief](../grid-intelligence-spain-pilot-2026-11-25.md) — commercial thesis, Alicante pilot and go/no-go criteria.
- [REE transmission GeoJSON extractor](../../experiments/ree_transmission_geojson.py) — paginated extractor covering mainland/Balearics/Ceuta/Melilla and the Canary Islands.
- [REE circuit-rating analyzer](../../experiments/analyze_ree_circuit_ratings.py) — monthly MVA distributions and limiting-element counts; deliberately does not sum ratings.
- [e-distribución capacity fetcher](../../experiments/fetch_edistribucion_capacity.py) — preserves monthly demand/generation CSV snapshots with SHA-256 manifests.
- [OSM power infrastructure fetcher](../../experiments/fetch_osm_power_infrastructure.py) — retrieves a pilot area's volunteered power infrastructure under ODbL 1.0.
- [ICV land-layer fetcher](../../experiments/fetch_gva_land_layers.py) — downloads CC BY PATFOR forest land, DIC records, planning zoning, SU-SUZ GeoPackage/CSV and 2025 land-cover data for the Valencian Community.
- [SU-SUZ readiness normalizer](../../experiments/normalize_suz_development_readiness.py) — converts the source CSV into explicit planning, reparcelation, urbanisation and service states without inferring grid capacity.
- [Alicante pilot protocol](alicante-pilot-protocol.md) — stratified sample, spatial QA, source semantics and go/no-go criteria.
- [Product wedge: industrial site readiness](product-wedge-industrial-site-readiness.md) — an evidence-dossier service for energy-intensive site acquisition.
- [REE access-capacity fetcher](../../experiments/fetch_ree_access_capacity.py) — preserves separate transmission demand/generation CSVs with SHA-256 manifests.
- [REE acquisition status](ree-acquisition-status.md) — verified source facts, unverified steps and validation gates.
- [Operator coverage matrix](operator-coverage-matrix.md) — current publication coverage and known gaps across Spanish DSOs.
- [Site screening specification](site-screening-spec.md) — evidence-based first-pass site assessment for generation, storage and large demand.
- [Data rights and commercial boundaries](data-rights-and-commercial-boundaries.md) — source-specific reuse restrictions and licensing gates.
- [Competitive benchmark: Rare Context](competitive-benchmark-rare-context.md) — existing market coverage, legal approach and differentiation hypotheses.
- [Licensed foundation stack — Spain](licensed-foundation-stack-spain.md) — commercially reusable geospatial, cadastral, environmental and energy-context sources.

## Build sequence

### Phase 1 — establish the base map
- Extract REE transmission substations and circuits.
- Validate geometry, coordinate reference system, voltage and identifiers.
- Profile the monthly circuit transport ratings (MVA) and limiting elements without treating them as connection capacity.
- Create reproducible raw-data snapshots and manifests.

### Phase 2 — attach access capacity
- Preserve and normalize separate demand and generation access-capacity publications.
- Start with e-distribución's official monthly CSVs, then add EASA and Ceuta and other DSO operators.
- Ingest CNMC monthly maps and REE/operator datasets.
- Keep each publication as a dated observation; never overwrite history.
- Reconcile source node IDs to physical GIS nodes only where evidence supports the match.

### Phase 3 — add system context
- Ingest REData regional time series for demand, generation mix and exchanges.
- Add market and congestion indicators where licensing/access permits.
- Add planning and environmental layers.

### Phase 4 — test commercial value
- Clear source rights for every customer-facing layer or exclude the layer.
- Run a real, public-site feasibility screen using commercially reusable inputs.
- Compare findings with existing commercial products and manual consultant workflows.
- Seek buyer feedback before building a full platform.

## Non-negotiable data semantics

- MW is power; MWh is energy; MVA is apparent power.
- Generation capacity and demand capacity are separate.
- Published access capacity is indicative and may be non-additive across related nodes.
- A network map is not a connection approval.
- Missing, zero, reserved, pending and not-assessed are distinct states.
- Every result must retain source, publication date, retrieval date, methodology and uncertainty.

## Immediate next task

Run the REE GIS extractor from a network-enabled environment, compare results with ArcGIS count queries, inspect its output and create the first validated inventory of Spanish transmission substations and circuits. Acquire the five ICV CC BY planning/land layers for the Valencian pilot, validate GeoPackage/ZIP integrity, inspect schemas and CRS, then build the first development-sector readiness table. In parallel, acquire the official November 2026 e-distribución demand and generation CSVs, inspect their real headers, and define operator-specific normalization only after schema inspection. The first useful deliverable is a dated, queryable dataset with provenance — not a polished frontend.
