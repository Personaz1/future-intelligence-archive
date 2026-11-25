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
