# Grid Intelligence — canonical data model
Status: initial schema, 2026-11-25

## Design principle

Keep source observations immutable and preserve provenance. Build normalized entities as derived views. Do not overwrite source facts with estimates or inferred joins.

## Core entities

### NetworkOperator
- operator_id
- legal_name
- role: transmission | distribution
- country
- service_area_geometry_ref
- source_url

### GridNode
- node_id (internal stable identifier)
- source_operator_id
- source_node_id
- canonical_name
- aliases[]
- voltage_kv
- node_type: substation_busbar | connection_node | other
- geometry (point)
- geometry_crs
- municipality / province / autonomous_community
- valid_from / valid_to
- identity_match_confidence

A substation can contain multiple nodes/busbars at different voltage levels. Never collapse them into one capacity number.

### GridCircuit
- circuit_id
- source_operator_id
- source_circuit_id
- name
- voltage_kv
- geometry (LineString/MultiLineString)
- endpoints (node IDs, nullable unless verified)
- circuit_type: overhead | underground | submarine | unknown
- source_record_ref

### CapacityObservation
Use this entity for connection/access-capacity observations, not physical circuit ratings.
- observation_id
- node_id
- operator_id
- direction: demand | generation | storage | hybrid | unknown
- technology (nullable)
- capacity_type: available | occupied | requested | granted | commissioned | operational | other
- value
- unit: MW | kW (normalize to MW only in a derived field)
- source_publication_date
- retrieved_at
- methodology_version
- scenario
- source_record_ref
- caveat_codes[]

### CircuitTransportRatingObservation
Use this entity for a physical circuit's published transport/thermal rating. It is not a connection-capacity observation.
- observation_id
- circuit_id
- source_operator_id
- rating_period: month | season
- period_key: 2026-11 | summer | winter | etc.
- value
- unit: MVA
- limiting_element_code (nullable)
- circuit_status_at_source
- source_publication_date / source_edit_timestamp (nullable)
- retrieved_at
- source_record_ref
- methodology_version / source_layer_version
- caveat_codes[]

### SourceSnapshot
Immutable record of a retrieved source publication or API snapshot.
- snapshot_id
- publisher / operator_id
- source_url
- dataset_key
- publication_date / publication_period
- retrieved_at_utc
- media_type
- byte_size
- sha256
- original_filename
- source_crs (nullable)
- parser_name / parser_version (nullable)
- reuse_terms_status: unknown | reviewed | permitted | restricted
- notes

### ConnectionPositionObservation
- node_id
- voltage_kv
- free_positions
- occupied_positions
- source_publication_date
- source_record_ref

### SystemMetric
- geography_id
- metric: demand | generation | price | curtailment | exchange | other
- value
- unit: MW | MWh | EUR_per_MWh | other
- interval_start / interval_end
- source and source_record_ref

### Site
- site_id
- geometry
- intended_use
- requested_power_mw
- direction: demand | generation | storage
- project_stage
- constraints[]

### Evidence
Every displayed claim must point to one or more Evidence records:
- evidence_id
- source_url
- source_publisher
- source_timestamp
- retrieval_timestamp
- exact source field/value
- transformation steps
- parser/version/checksum
- limitations

## Required semantic distinctions

- MW = active power; MWh = energy over time; MVA = apparent power. Never silently equate them.
- Installed capacity is not instantaneous output.
- Access capacity (MW/kW) and circuit transport rating (MVA) are separate entity types and must never be joined as if they were interchangeable.
- Granted access is not necessarily commissioned or operational.
- Demand access and generation access are different directions and methodologies.
- Storage may be modelled as demand, generation, or hybrid depending on regulation and operating mode; preserve source treatment.
- Zero, missing, not assessed, reserved and not applicable are distinct states.
- A substation's multiple busbars/voltage levels are distinct nodes.
- Adjacent nodes may share constraints; published MW values are not additive by default.

## Derived products (not source facts)

- nearest substations/circuits to a site;
- capacity signal by direction/technology and publication date;
- capacity trend by node across monthly snapshots;
- network-context features (nearby nodes, voltage levels, circuit corridors);
- screening score with explainable components and confidence;
- data completeness and source disagreement flags.

Every derived result must carry its inputs, calculation version, date and uncertainty. Never label a screening score as a probability of receiving a permit unless calibrated against observed outcomes.


## Source-specific implementation note (REE + e-distribución, 2026-11)

REE circuit layer 11 exposes monthly fields `CAP_ENE` ... `CAP_DIC`
(MVA) and matching `ELEM_LIM_*` fields. These map to
`CircuitTransportRatingObservation`, not `CapacityObservation`.

e-distribución publishes separate monthly demand and generation access-capacity
files. They map to `CapacityObservation` with direction fixed by the source
publication. Preserve each original file as a `SourceSnapshot`; only map
columns after inspecting the downloaded header and accompanying methodology.

Do not assume the REE circuit layer's `FECHA_RECARGA` is the same as the
publication date or the retrieval timestamp. Store it as a source edit/update
timestamp until the publisher's semantics are confirmed.


## DSO publication fields discovered in i-DE generation data

A May 2026 i-DE generation publication exposes fields beyond a single MW value:
available capacity, occupied capacity, admitted-but-unresolved applications split
by PV/wind/other, occupied/free positions, affected transmission node,
short-circuit-limited flag, regulatory-commitment flag, `0*` flag, connection
point name and connection point identifier. The November 2026 generation and
demand publications are indexed as separate PDFs dated 4 November.

Model these flags and identifiers explicitly. In particular:
- `0*` is a methodological state that can indicate potential capacity subject
  to reinforcements; it is not the same as ordinary zero.
- regulatory commitment means applications are pending due to a competitive
  allocation process at the predominantly affected transmission node; it is
  not simply "occupied MW".
- occupied capacity, pending admitted applications and available capacity
  remain separate observations.
- preserve the source UTM coordinates and defer spatial joins until the exact
  coordinate reference system is verified.
