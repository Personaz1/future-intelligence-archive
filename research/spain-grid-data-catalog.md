# Spain electricity grid — data source catalog
Last checked: 2026-11-25

This is a source inventory, not a claim that all layers are complete, open-licensed for resale, or technically sufficient for connection decisions. Record retrieval date, publisher, original URL, file checksum, publication date, geography, units, and reuse terms for every ingestion.

## 1. Official transmission network geometry — REE

REE ArcGIS REST service:
- Service: https://georedservices.ree.es/arcgis_ags1/rest/services/WEBREE/Instalaciones_RdT_WEBREE/MapServer
- Layer 3: `Subestaciones` (point geometry).
- Layer 11: `Circuitos` (polyline geometry).
- Both expose ArcGIS REST query endpoints; supported output formats include JSON and GeoJSON.
- Circuit layer exposes `ID`, `CODIGO_BDI`, `CODIGO_MRID`, `CODIGO_EIC`, `TENSION`, `ESTADO`, `PAIS`, owner/operator fields and circuit endpoint/position fields.
- It also exposes monthly transport-rating fields `CAP_ENE` ... `CAP_DIC` in **MVA**, plus matching `ELEM_LIM_*` limiting-element fields. Seasonal fields `CAP_PRI`, `CAP_VER`, `CAP_OTO`, `CAP_INV` also exist.
- These are circuit transport ratings, not spare connection capacity. They must not be re-labelled as MW or summed into a hosting-capacity estimate.
- Substation layer contains identifiers/names and owner/operator attributes. Check its metadata before relying on individual fields.
- Layer metadata: https://georedservices.ree.es/arcgis_ags1/rest/services/WEBREE/Instalaciones_RdT_WEBREE/MapServer/layers

A second REE detail service is also discoverable:
- https://georedservices.ree.es/arcgis_ags2/rest/services/Zonas_de_detalle_WEBREE_MIL1/MapServer
- Layer 1: substation points.
- Layer 36: circuit polylines.
- Its circuit metadata identifies source spatial reference EPSG:25830 and voltage classes.

Important: these are transmission assets, not a complete model of all distribution feeders. Do not infer that an absent line is physically absent.

## 2. Access capacity — regulator and network operators

### CNMC national aggregation
- Portal: https://www.cnmc.es/sectores-que-regulamos/energia/supervision-del-mercado-electrico/informe-acceso-y-conexion-redes
- Maps: generation and demand.
- Aggregates monthly submissions from transmission and distribution network operators under Circular informativa 6/2025.
- Filters include network operator, province, voltage, free substation positions, regulatory reservation flags and available capacity.
- CNMC explicitly says published values are informative, node values influence each other and must not be directly summed. Applications go to the relevant network operator.

### REE
- Demand access capacity: https://www.ree.es/es/clientes/consumidor/acceso-conexion/conoce-la-capacidad-de-acceso
- Generation access capacity: https://www.ree.es/es/clientes/titular-de-almacenamiento/acceso-conexion/conoce-la-capacidad-de-acceso
- The pages expose monthly CSV/XLSX and occupied-by-position files. On 2026-11-25, the latest publication displayed was 2026-11-03.
- Direct CSV snapshots:
  - Demand: https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/2026_11_03_GRT_demanda.csv
  - Generation: https://www.ree.es/sites/default/files/12_CLIENTES/Documentos/2026_11_03_GRT_generacion.csv
- REE's demand methodology evaluates active power simultaneously at a node or zone, using short-circuit power, static and dynamic criteria; it explicitly says national sums are not meaningful because nodes share zones of influence.
- **Reuse warning:** ESIOS/API legal terms explicitly prohibit commercial use of ESIOS data. The specific terms for REE's GIS layers and access-capacity CSV files remain unverified; do not automatically apply or ignore the ESIOS terms.
- Generation access is technology-specific (MGES/MPE) and the granted access is not a guarantee of generation/evacuation in real-time operation.
- Capture each publication's issue date, scenario, node identifier, voltage, technology/direction, units and methodology.

### i-DE / Iberdrola distribution
- Demand map and methodology: https://www.i-de.es/conexion-red-electrica/suministro-electrico/mapa-capacidad-consumo
- Generation map: https://www.i-de.es/conexion-red-electrica/produccion-energia/mapa-capacidad-acceso
- The current November 2026 publication was indexed as PDFs dated 2026-11-04 for both demand and generation (generation file 4.6 MB; demand file 3.7 MB). The public map page also advertises downloadable data formats.
- The May 2026 generation PDF exposes a useful schema: distributor code, province, municipality, UTM X/Y, substation, voltage, available MW, regulatory commitment flag, occupied MW, pending admitted capacity by PV/wind/other, occupied/free positions, affected transmission node, short-circuit-limited flag, 0* flag, comments, connection-point name and connection-point ID. Treat this as a schema discovery, not proof that every month's schema is unchanged.
- The connection-point identifier and affected transmission node are valuable candidate join keys, but require reconciliation against REE/DSO GIS IDs. Coordinate CRS must be confirmed before spatial joins.
- The published capacity is indicative; individual applications receive specific study.
- **Reuse warning:** i-DE's legal notice prohibits commercial use of site information and requires authorization for commercial reproduction, transformation, distribution or public communication. The November files are public downloads, not an established commercial licence.
- i-DE says node capacities are interdependent and cannot be summed across nodes or voltage levels at a substation.
- Its demand methodology accounts for facilities scheduled for commissioning in the current year and included in the approved investment plan, but excludes future reinforcements.
- A node with a zero published value may have a special "Nudo 0" interpretation; preserve the flag rather than flattening it into a simple numeric zero.

### e-distribución
- Generation: https://www.edistribucion.com/es/red-electrica/nodos-capacidad-red/capacidad-generacion.html
- Demand: https://www.edistribucion.com/es/red-electrica/nodos-capacidad-red/capacidad-demanda.html
- November 2026 generation and demand pages both advertise downloadable CSV/XLSX publications, with monthly updates. Official November CSVs are linked from the pages:
  - Demand: https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/nodos/demanda/202611/2026_11_04_R1299_demanda.csv
  - Generation: https://www.edistribucion.com/content/dam/edistribucion/conexion-a-la-red/descargables/nodos/generacion/202611/2026_11_04_R1299_generaci%C3%B3n.csv
- The demand publication also includes EASA and Ceuta distributor files. The generation page includes corresponding e-distribución, EASA and Ceuta publications.
- Both pages say the map is informative, values are indicative, nodes are interdependent and capacity is not cumulative/simultaneous. The published capacity does not include possible constraints in other distributors or the transmission network.
- **Reuse warning:** e-distribución's legal notice restricts content to private use and expressly prohibits commercial use, copying, distribution or modification without rights-holder authorization. Public CSV download is not a commercial licence.
- Storage access rules have changed; capture the exact applicable resolution and effective date per dataset.

### Other DSOs

#### UFD (Naturgy)
- Official capacity publication located: https://www.ufd.es/wp-content/uploads/2025/08/Publicacion-capacidades-25-Julio.pdf
- A December 2024 UFD publication explains that coordinates use ETRS89 / UTM zone 29 in Lugo, Ourense, A Coruña and Pontevedra, and zone 30 in other provinces. Preserve this per-record/province CRS rule; do not treat all coordinates as one UTM zone.
- UFD data distinguishes available, occupied and under-study capacity, and can include position/park-level detail, short-circuit limitation and physical feasibility for new connection positions.
- The latest UFD capacity publication located in this review is dated 25 July 2025. A newer November 2026 file was not found; current cadence and latest official version require confirmation.

#### Viesgo Distribución
- Public network map: https://www.viesgodistribucion.com/mapa-interactivo-de-la-red
- The map describes outages and scheduled works; no public node-level access-capacity dataset was verified in this review.

#### Excluded from Spain scope: E-REDES
- https://www.e-redes.pt/ is Portugal's distribution network operator, not a Spanish DSO. Do not include it in Spanish coverage totals.

Do not assume common schemas, geographic coverage or commercial reuse rights.

## 3. System operation and market data

### CNMC Data portal — commercially reusable context datasets
- Portal: https://data.cnmc.es/
- Reuse terms: CC BY-SA 4.0 for datasets actually published in CNMC Data. Commercial and non-commercial reuse is allowed with attribution, preservation of update dates/metadata, no distortion, and share-alike compliance.
- Electricity generation monthly statistics: https://data.cnmc.es/energia/energia-electrica/renovables-cogeneracion-y-residuos/evolucion-mensual-de-energia-electrica — technology, energy sold (GWh), installed capacity (MW), number of installations.
- Electricity generation annual statistics: https://data.cnmc.es/energia/energia-electrica/renovables-cogeneracion-y-residuos/evolucion-anual-de-energia-electrica — annual regional/technology context.
- Retail electricity market: https://data.cnmc.es/energia/energia-electrica/energia-y-suministros — quarterly operator/CCAA, customer counts and energy consumption.
- These are useful for regional market/system context, but they do not replace node-level grid topology or access-capacity data.
- Do not extend the portal's CC BY-SA licence to capacity maps published elsewhere on cnmc.es or to source data owned by distribution operators.


### REE REData API
- Documentation: https://www.ree.es/es/datos/apidatos
- REST GET interface: `/{lang}/datos/{category}/{widget}`
- Supports date range, time aggregation (hour/day/month/year), and geographic filters including autonomous communities.
- JSON:API-like response includes widget and indicator metadata, magnitudes, values and timestamps.
- Suitable for historical demand, generation mix, exchanges and system indicators. It is not a substitute for local network topology or node-specific hosting capacity.

### ESIOS
- https://www.esios.ree.es/
- Investigate market prices, balancing and operational indicators. Verify API access, terms and data granularity before ingestion.

### ENTSO-E Transparency Platform
- https://www.entsoe.eu/data/
- Cross-border and European system data. API registration/token and dataset-specific terms may apply.

## 4. Geographic and planning context (to be researched)
- Cadastre / parcel boundaries and land-use constraints.
- Protected areas, environmental constraints and planning zoning.
- Flood and wildfire risk.
- Renewable resource, industrial demand, logistics, water availability.
- National transmission planning and project commissioning timelines.
- Local distribution network topology where the DSO publishes reusable geometry.

## 5. Data-quality rules

For every observation store:
- publisher and original source URL;
- dataset/layer and source record identifier;
- source publication date and retrieval timestamp (UTC);
- valid-from / valid-to where known;
- original value, original unit and normalized value/unit;
- geographic reference system and coordinate precision;
- methodology/scenario/version;
- licence/reuse terms and attribution;
- parser version and checksum;
- confidence and known caveats.

Never convert missing data to zero. Never combine demand and generation capacity. Never add node capacities without an explicit network model that accounts for shared constraints. Separate available, occupied/committed, requested/pending, granted, commissioned and operational quantities.

## 6. Verified source notes

- CNMC announcement dated 2026-04-15 confirms national generation/demand maps and monthly updates.
- REE ArcGIS metadata confirms transmission substation point and circuit polyline layers; circuit records expose monthly/seasonal MVA transport ratings, limiting elements, status, country and stable identifiers.
- i-DE methodology explicitly warns about interdependent nodes, non-additivity and the need for a specific connection study. Its generation publication exposes connection-point identifiers, affected transmission nodes, occupied/free positions, regulatory-commitment and 0* flags.
- UFD has an official capacity publication dated 25 July 2025 with different semantics and a province-dependent UTM zone; the latest publication found is older than the November 2026 datasets of REE, i-DE and e-distribución.
- E-REDES is a Portuguese operator and is excluded from Spain's DSO coverage.
- e-distribución November 2026 pages expose separate official CSV/XLSX files for demand and generation, including the direct CSV download URLs recorded above.
- REE's access-capacity pages expose separate monthly transmission CSV/XLSX files for demand and generation. The 3 November 2026 CSV URLs are recorded above; REE explicitly warns that nodal capacities cannot be summed nationally.

This catalog should be expanded only after each new source has been opened and its schema, cadence and terms inspected.
