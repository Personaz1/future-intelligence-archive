# Spanish grid data coverage matrix

Reviewed: 2026-11-25

This matrix tracks verified publication coverage, not physical network coverage.
A source can exist without being downloadable in the current environment, and
a published capacity map does not replace an engineering connection study.

| Publisher / operator | Network layer | Latest publication located | Public source form | Useful fields / semantics | Acquisition state |
|---|---|---|---|---|---|
| REE | Transmission GIS | Current ArcGIS service metadata | ArcGIS REST / GeoJSON | Substations, circuits, voltage, status, IDs, monthly circuit ratings (MVA), limiting elements | Layer metadata verified; full extraction not run |
| REE | Transmission access capacity — demand | 2026-11-03 | CSV, XLSX, PDF | Node/zone capacity, active-power demand, scenario criteria, occupied/access margin | Direct CSV URL verified; fetcher committed; bytes not downloaded |
| REE | Transmission access capacity — generation | 2026-11-03 | CSV, XLSX, PDF | Technology-specific MGES/MPE, available and occupied capacity | Direct CSV URL verified; fetcher committed; bytes not downloaded |
| e-distribución | Distribution access capacity — demand | 2026-11 | CSV, XLSX | Firm demand access capacity; monthly publication | Direct CSV URL verified; fetcher committed; bytes not downloaded |
| e-distribución | Distribution access capacity — generation | 2026-11 | CSV, XLSX | Generation access capacity; monthly publication | Direct CSV URL verified; fetcher committed; bytes not downloaded |
| EASA / Ceuta | Distribution access capacity | 2026-11 | CSV, XLSX | Separate operator publications on e-distribución pages | Links verified; no dedicated adapter yet |
| i-DE | Distribution access capacity — demand | 2026-11-04 | PDF / map downloads | Busbar-level demand capacity, 0* and regulatory-commitment semantics | Current publication indexed; May 2026 generation PDF inspected for schema |
| i-DE | Distribution access capacity — generation | 2026-11-04 | PDF / map downloads | Connection-point ID, available/occupied/under-study capacity, technology buckets, positions, affected RdT node, 0* and Scc flags | Current publication indexed; May 2026 generation PDF inspected for schema |
| UFD | Distribution access capacity — generation | 2025-07-25 latest located | PDF | Available/occupied/under-study MW, position detail, physical viability, Scc limitation; CRS varies by province | Historical/currentness gap; no 2026 publication located |
| Viesgo Distribución | Operational map | Current map page | Interactive web map | Outages and scheduled works | Capacity dataset not verified |
| E-REDES | Portugal DSO | Out of scope | — | Portuguese distribution network | Excluded from Spain |

## What the matrix says

1. A national access-capacity layer is feasible in principle, but not yet complete.
2. Transmission and distribution need separate ingestion pipelines.
3. Demand and generation must remain separate; storage mode is a regulatory
   attribute, not a universal third column.
4. DSO adapters must preserve operator-specific flags, identifiers, coordinate
   systems and semantics.
5. UFD's older located publication and Viesgo's lack of a verified public
   capacity dataset are explicit coverage gaps, not zero-capacity areas.
6. CNMC is the aggregation and discovery layer; operator files remain essential
   for provenance, schema details and historical snapshots.

## Next data gates

- Download and inspect REE and e-distribución CSVs in a network-enabled runtime.
- Inspect i-DE November 2026 PDFs and compare with May schema.
- Locate a current UFD publication or record the operator's publication gap.
- Determine whether Viesgo publishes the standardized CNMC capacity format.
- Reconcile connection-point IDs, substation codes and affected transmission
  node IDs only when a deterministic mapping is available.
- Review reuse/licensing terms before redistribution or commercial packaging.


## Reuse clearance overlay

- e-distribución: restricted without rights-holder authorization for commercial
  reuse under its published legal notice.
- i-DE: restricted without authorization for commercial reproduction,
  transformation, distribution or public communication.
- REE ESIOS/API: commercial use prohibited by ESIOS terms. REE GIS and access
  capacity files remain separately un-cleared until their specific terms are
  confirmed.
- UFD and Viesgo: rights not yet reviewed.
- CNMC Data portal: CC BY-SA 4.0 permits commercial reuse for datasets actually
  published in that portal; it does not automatically cover the CNMC capacity
  maps or operator-origin files.

See [data rights and commercial boundaries](data-rights-and-commercial-boundaries.md).
