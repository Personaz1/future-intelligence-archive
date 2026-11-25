# SU-SUZ data contract and QA gates

## Purpose

The ICV SU-SUZ inventory is planning/development evidence for Valencian Community urbanizable sectors. In this pilot it supports screening of industrial land in Alicante. It is not a parcel-level legal opinion, construction permit, grid-connection decision, or power-capacity dataset.

## Source and licensing

Use the official ICV SU-SUZ inventory publication and its linked CSV/GeoPackage exports as the source of record. The portal labels the information as informative and publishes a CC BY license; preserve attribution and the exact source URL with every acquired snapshot. Record acquisition time, original filename, byte size, and SHA-256 for each raw file. Do not infer a legal update cadence from the portal's “Bianual” label; preserve the publisher wording until clarified.

## Semantic contract

- `municipio` and `cpm`: municipality identity fields; retain original values and leading zeros.
- `uso`: planning land-use classification; do not infer industrial suitability from a text label without a documented class mapping.
- `sup`: planning-sector area, not necessarily a parcel's available area.
- `edif_total`: permitted buildable floor area as recorded in the source; not a site-specific entitlement determination.
- Planning milestones (`ord_porm`, `gestion`, `pai`, `Pr_repc`, `p_urbaniz`, `f_incio`, `f_recep`) are separate states. Do not collapse them into a single “ready” score without explicit, validated rules.
- Service indicators (`f1acceso_r` through `f8colector`) describe recorded urban services. In particular, `f5electric` means electrical installation/service presence, not spare capacity, connection rights, voltage, MW/MVA, or connection cost.
- Missing, blank, unrecognized, negative, and not-applicable values must remain distinguishable. Normalization must not turn missing into “no”.
- Grid capacity remains `not_assessed` in this dataset.

## Required QA before publishing a snapshot

1. Save the unmodified source file and a provenance manifest before transformation.
2. Verify the CSV header includes at least `municipio`, `uso`, `sup`, and `f5electric`; record any schema drift rather than silently dropping columns.
3. Report row count, distinct municipality count, missingness for key fields, duplicate feature identifiers if present, and invalid numeric values in area/buildability fields.
4. Confirm delimiter, encoding, and coordinate reference system for spatial exports; do not assume the CRS from file extension.
5. Compare a small sample of normalized records against the source export and the ICV field dictionary.
6. Keep raw source values alongside normalized values so every derived state is auditable.
7. Do not publish a buildability ranking or “grid-ready” label from these fields alone.

## Output interpretation

The current normalizer produces evidence states, not a composite score. Summary counts are descriptive of the source inventory and must include the snapshot date and denominator. They do not establish that land is legally buildable, available for purchase, or electrically connectable.

## Next data gate

The next defensible step is to acquire the official CSV and spatial export in a network-enabled environment, archive them with provenance, run the pipeline, inspect real field values, and then update this contract with observed schema/quality findings. Until that happens, no dataset row counts or geographic findings should be represented as measured results.
