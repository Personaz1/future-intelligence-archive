# REE acquisition status

Last reviewed: 2026-11-25

This file separates what has been verified from what has merely been designed.
A public service endpoint or a layer metadata page is not proof that a complete
national dataset has been downloaded, validated, or licensed for redistribution.

## Source validation

| Source | What is established | Current status | Not yet established |
|---|---|---|---|
| REE ArcGIS MapServer | Official public service exposes transmission substations (layer 3) and circuits (layer 11); service supports JSON/GeoJSON queries | Service and layer metadata inspected | Full national extraction, record counts, completeness, refresh cadence |
| REE circuits, layer 11 | Polyline geometry; IDs/MRiD/EIC, voltage, owners/operators, country, status, endpoint positions, monthly/seasonal transport ratings (MVA), limiting-element fields | Metadata inspected | Meaning and data quality of every field; whether all records are in-service or planned |
| REE transmission access capacity | Separate monthly demand and generation CSV/XLSX; November 2026 publication dated 3 Nov; demand includes scenario/node/zone criteria and occupied/access margin information | Official pages and direct CSV URLs verified | CSV files not downloaded; headers, row counts, exact normalization and reuse terms unverified |
| REE transport-network overview | REE describes a network with over 46,000 km of circuits, 700+ substations and 6,000+ positions | Publisher overview inspected | Exact alignment with the ArcGIS layer's scope and record counts |
| CNMC access-capacity maps | Monthly operator submissions; published capacity is indicative and node values must not be summed as if independent | Official publication and caveats reviewed | Raw source files, historical snapshots, schema stability and reuse terms |
| i-DE / e-distribución | Operator-facing public generation and demand capacity information exists, including downloadable data on e-distribución pages | Official pages reviewed | Downloaded source files, column mapping, complete version history and redistribution rights |

## Extractor status

The script `experiments/ree_transmission_geojson.py` now queries two geographic
envelopes: mainland/Balearics (including Ceuta and Melilla) and Canary Islands.
It paginates, retries transient HTTP failures, deduplicates features, and writes
a manifest with per-region received counts.

**Important:** the revised extractor has been committed but has not yet been
run against the live service in this environment. No GeoJSON dataset or feature
count is claimed here. The offline tests check helper behavior, not the remote
service, pagination completeness, or geographic coverage.

## Next validation gates

1. Run the extractor from a network-enabled environment.
2. Compare downloaded counts with ArcGIS `returnCountOnly` results per layer
   and region; investigate any mismatch.
3. Check for null/duplicate identifiers, invalid geometries, unexpected
   countries, and assets outside the intended geographic envelopes.
4. Reconcile the circuit layer's `PAIS`, `ESTADO`, `TENSION`, monthly
   `CAP_*` and `ELEM_LIM_*` fields against the source metadata.
5. Inspect the substation layer schema before assuming it shares circuit fields.
6. Record source timestamps, checksums, coordinate system, parser version and
   source terms for every snapshot.
7. Do not derive connection hosting capacity from line transport ratings.
   They are different engineering quantities.

## Interpretation boundary

The REE layer describes transmission infrastructure. It does not provide a
complete distribution network and does not, by itself, answer whether a
specific solar, battery, industrial or data-centre project can connect.

## New capacity and rating workflows

- `experiments/fetch_ree_access_capacity.py` preserves the official November 2026 REE transmission demand and generation CSVs separately, with SHA-256 manifests.
- `experiments/fetch_edistribucion_capacity.py` preserves the official November
  2026 e-distribución demand and generation CSVs separately, computes SHA-256
  checksums and inspects the CSV header/delimiter without rewriting source bytes.
- `experiments/analyze_ree_circuit_ratings.py` produces descriptive monthly
  MVA distributions grouped by voltage, status and country, including missing
  values, zero values and limiting-element counts. It intentionally does not
  sum circuit ratings.
- Offline tests have been added for both utilities. They have not been executed
  against the live operator files or a downloaded REE dataset in this environment.

## e-distribución November 2026 source links

Demand:
https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/nodos/demanda/202611/2026_11_04_R1299_demanda.csv

Generation:
https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/nodos/generacion/202611/2026_11_04_R1299_generaci%C3%B3n.csv

The official demand and generation pages state that the published values are
indicative, are refreshed monthly, may be committed by applications received
before publication, and can be affected by constraints in other networks.
Demand and generation remain separate data products. Storage access rules
must be represented with their applicable regulatory effective dates.

## REE November 2026 access-capacity sources

Demand CSV:
https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/2026_11_03_GRT_demanda.csv

Generation CSV:
https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/2026_11_03_GRT_generacion.csv

The REE demand page describes capacity as active power assessed simultaneously
at a node or zone, with short-circuit, static and dynamic criteria. It explicitly
warns that nodal values cannot be summed nationally because zones of influence
interrelate the results. The generation page distinguishes MGES/MPE technology
types and warns that access rights do not guarantee real-time generation or
evacuation. Both pages say individual studies prevail.

## Additional DSO coverage findings

- **i-DE:** November 2026 demand and generation publications are indexed as
  separate PDFs dated 4 November. The May 2026 generation PDF was inspected
  structurally: it exposes connection-point IDs, affected transmission node,
  available/occupied/under-study capacity, regulatory commitment, short-circuit
  limitation, position counts and a `0*` flag. The November PDF files have
  not yet been downloaded and compared column-by-column.
- **UFD:** an official capacity publication dated 25 July 2025 was located.
  UFD's published coordinate system is province-dependent: ETRS89 / UTM zone
  29 for Galicia provinces and zone 30 elsewhere. Its data distinguishes
  available, occupied and under-study capacity, and includes connection
  position/physical-feasibility semantics. No newer November 2026 publication
  was located in this review.
- **Viesgo Distribución:** a public map for outages and scheduled network works
  was verified; no public node-level access-capacity dataset was verified.
- **E-REDES:** this is a Portuguese DSO, not a Spanish operator; excluded from
  the Spain coverage model.

These findings make a single generic DSO parser unsafe. Use operator-specific
adapters that emit the same canonical entities while preserving each source's
flags, units, CRS and publication semantics.


## Commercially reusable pilot infrastructure layer

An OSM Overpass acquisition utility has been added:
`experiments/fetch_osm_power_infrastructure.py`. It retrieves power-tagged
nodes/ways/relations for a WGS84 bounding box, stores the raw response and
records a checksum, tag counts and ODbL 1.0 attribution in its manifest.

The default envelope is a pilot-scale Alicante area, not national coverage.
The utility has not yet been run against Overpass. OSM is volunteered mapping:
it can provide candidate infrastructure geometry, but cannot establish
authoritative asset status, electrical connectivity or available capacity.
Any distributed derivative database must comply with ODbL share-alike terms.


## Valencian planning and land-cover acquisition

Five regional datasets have now been verified at their publisher pages and added
to the licensed pilot stack:

- ICV **PATFOR strategic forest land**: CC BY; GeoPackage layer delineating strategic forest land by province and recording the factor used under PATFOR criteria. Catalogue update frequency is not confirmed. WFS feature type `Planeamiento.TFEFactores`.
- ICV **Declaraciones de Interés Comunitario (DIC)**: CC BY; records non-urban parcels with a recorded community-interest declaration under Valencian planning law. Publisher says the layer is informational and derived from administrative case files; a DIC does not automatically authorize a new energy project. WFS feature type `DeclaracionInteresComunitario`.
- ICV **Planeamiento.Zonificacion**: CC BY; urban planning zoning/classification compiled from approved planning documents at scales 1:500–1:25,000. Catalogue frequency is bianual. Publisher explicitly says the layer is informative and directs users to underlying planning instruments and the competent authority for legally valid status. WFS feature type `Planeamiento.Zonificacion`.
- ICV **SU-SUZ**: CC BY; urban land under execution units and developable
  sectors, with planning/execution status. Publisher catalogue says bianual
  update frequency and explicitly labels the information informative. WFS
  feature type `InventarioSuSuz`; GeoPackage WFS request URL is recorded in
  `research/spain-grid-data-catalog.md`.
- ICV **COSCV 2025**: CC BY; regional land-cover mapping based on ICV 1:5,000
  topographic cartography, SIGPAC2025 in agricultural areas and PATFOR data
  dated 2025 in forest areas. The portal labels this edition historical data.
  Complete GeoPackage ZIP URL is recorded in the source catalog.

Acquisition utility: `experiments/fetch_gva_land_layers.py` (now supports `patfor_tfe`, `dic`, `zoning`, `su_suz` and `coscv_2025`).
Offline metadata/hash tests: `tests/test_fetch_gva_land_layers.py`.

**Status:** publisher pages, CC BY metadata and download endpoints verified.
The files have not yet been downloaded or schema-validated in this environment.
SU-SUZ is not a legally binding planning determination; COSCV land cover is
not zoning. Both are regional Valencian layers, not national Spain coverage.
