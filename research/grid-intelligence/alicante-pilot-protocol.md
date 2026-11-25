# Alicante pilot — validation protocol

Status: protocol defined; no parcels have yet been scored.

## Question

Can a transparent, reproducible first-pass site-screening workflow identify
candidate locations for energy-intensive projects using commercially reusable
public data, without pretending to know unpublished grid headroom?

The pilot is not a land-investment recommendation and does not replace
municipal planning review, environmental assessment or a network connection
study.

## Pilot geography

Start with Elche and the surrounding Alicante industrial/urban corridor, then
expand to the province after the first data-quality review. The regional ICV
datasets cover the Comunitat Valenciana and are therefore suitable for this
pilot, but they do not establish nationwide coverage.

## Candidate cohorts

Build a stratified sample, not a hand-picked set of attractive sites:

1. Existing industrial land / industrial estates.
2. Urban or developable sectors from the ICV SU-SUZ inventory.
3. Rural parcels with sufficient contiguous area, subject to zoning and
   environmental exclusions.
4. Existing generation or major infrastructure surroundings as a separate
   context cohort, not an automatic suitability advantage.

Each cohort must contain both positive and negative examples. Do not select
only sites that appear promising.

## Data layers and their roles

| Layer | Role | What it cannot prove |
|---|---|---|
| Cadastre parcel geometry | Stable parcel-level spatial reference and area | Ownership, title, easements or buildability |
| ICV Planeamiento.Zonificacion | Regional planning classification / zoning context | Legally definitive status; publisher says consult binding planning documents |
| ICV SU-SUZ | Urban/developable sector and execution-status context | That a specific parcel is immediately buildable |
| ICV COSCV 2025 | Current-ish land-cover evidence, based on 2025 source inputs | Legal zoning or permitted use |
| Protected areas | Environmental screening | Full permit feasibility |
| Flood risk | Exposure / engineering-review flag | Detailed parcel-scale hydraulic safety |
| Terrain / slope | Civil works and constructability context | Geotechnical suitability |
| OSM power assets | Candidate infrastructure geometry | Authoritative network topology, connection route or capacity |
| CNMC regional energy statistics | Regional generation / market context | Local grid headroom |

## Coordinate and geometry rules

- Keep each source in its native CRS and record it in the source manifest.
- Use EPSG:25830 only for layers whose metadata confirms ETRS89 / UTM zone 30N.
- Reproject geometries explicitly for analysis; never relabel coordinates.
- Validate polygon validity, geometry type, extent and unexpected empty layers.
- Record area in square metres after projection to a suitable metric CRS.
- Keep original geometry and derived geometry separately.
- Do not infer parcel adjacency from rounded centroid coordinates.

## Screening workflow

1. Load only datasets whose commercial reuse status is recorded.
2. Validate archive signatures, GeoPackage integrity, CRS, feature count and
   source dates.
3. Join parcels to planning and environmental polygons using exact spatial
   predicates; preserve all intersecting features and overlap area.
4. Calculate parcel area, contiguous usable area, slope distribution and
   distances to mapped infrastructure.
5. Apply hard exclusions only where the source semantics justify them.
6. Label informational or uncertain evidence as review flags, not hard blockers.
7. Generate separate profiles for BESS, solar, data centres and industrial
   demand; do not use one generic score.
8. Export a report with every source feature, transformation, assumption and
   unresolved issue.

## Evaluation

Measure:
- fraction of parcels with complete and valid geometry;
- fraction with a deterministic planning classification join;
- percentage of source features with valid CRS and licence metadata;
- spatial join disagreement against manual QGIS review;
- false exclusion rate from environmental/planning flags;
- reproducibility of scores from the same immutable snapshots;
- amount of missing or stale evidence per municipality.

A manual reviewer should inspect a random sample from every candidate cohort,
including rejected sites. Record disagreements and update the method version.

## Critical limits

- A high land score does not imply grid connection feasibility.
- OSM proximity is not proof of electrical connectivity.
- Public transmission geometry does not disclose every distribution constraint.
- A planning layer marked informative must be confirmed against the binding
  municipal instrument.
- No score may compensate for a legally prohibited use.
- No commercial report may contain restricted operator capacity values until
  rights are cleared.

## Exit criteria

Proceed to a buyer-facing prototype only when:
- the acquisition scripts have been run and their downloads validated;
- each layer's licence and attribution are recorded;
- CRS and feature schemas are inspected, not guessed;
- a manually reviewed sample shows acceptable spatial-join accuracy;
- a Spanish planning professional confirms how the informative zoning layer
  should be escalated to binding documents;
- the report clearly separates land suitability from grid-access uncertainty.
