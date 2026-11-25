# Grid Intelligence — Spain

Research and prototype work on Spanish electricity infrastructure, grid topology, access capacity, power flows, generation, demand and storage.

## Current status — 2026-11-25

We have verified that useful official sources exist at three distinct layers:

1. **Physical transmission topology:** REE ArcGIS REST layers for substations (point features) and circuits (line features), including voltage attributes.
2. **Access capacity:** CNMC national monthly maps plus operator-level CSV/XLSX publications. These describe indicative access capacity, not guaranteed connection rights.
3. **System operation:** REE REData REST API for time-series demand, generation and other system indicators.

This is enough to begin assembling a source-grounded national data model. It is not yet a complete Spanish grid digital twin: distribution topology, source reuse terms, data completeness and node identity reconciliation remain open.

## Repository map

- [Spain grid data source catalog](../spain-grid-data-catalog.md) — official portals, service endpoints, caveats and ingestion rules.
- [Canonical data model](../grid-intelligence-data-model.md) — nodes, circuits, capacity observations, evidence and semantic distinctions.
- [Spain pilot research brief](../grid-intelligence-spain-pilot-2026-11-25.md) — commercial thesis, Alicante pilot and go/no-go criteria.
- [REE transmission GeoJSON extractor](../../experiments/ree_transmission_geojson.py) — initial utility to fetch transmission substations and circuits for mainland Spain + Balearic bounding box.

## Build sequence

### Phase 1 — establish the base map
- Extract REE transmission substations and circuits.
- Validate geometry, coordinate reference system, voltage and identifiers.
- Create reproducible raw-data snapshots and manifests.

### Phase 2 — attach access capacity
- Ingest REE transmission capacity tables for demand and generation/storage.
- Ingest CNMC monthly maps and operator datasets.
- Keep each publication as a dated observation; never overwrite history.
- Reconcile source node IDs to physical GIS nodes only where evidence supports the match.

### Phase 3 — add system context
- Ingest REData regional time series for demand, generation mix and exchanges.
- Add market and congestion indicators where licensing/access permits.
- Add planning and environmental layers.

### Phase 4 — test commercial value
- Run a real, public-site feasibility screen.
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

Run the REE GIS extractor, inspect its output and create the first validated inventory of Spanish transmission substations and circuits. Then obtain and normalize the current CNMC/DSO capacity files. The first useful deliverable is a dated, queryable dataset with provenance — not a polished frontend.
