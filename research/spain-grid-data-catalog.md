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
- Generation access capacity: https://www.ree.es/es/clientes/generador/acceso-conexion/conoce-la-capacidad-de-acceso
- Capture each publication's issue date, scenario, node identifier, voltage, technology/direction, units and methodology.

### i-DE / Iberdrola distribution
- Demand map and methodology: https://www.i-de.es/conexion-red-electrica/suministro-electrico/mapa-capacidad-consumo
- The published capacity is indicative; individual applications receive specific study.
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
- Storage access rules have changed; capture the exact applicable resolution and effective date per dataset.

### Other DSOs
Investigate separately:
- e-redes: https://www.e-redes.es/
- UFD: https://www.ufd.es/
Do not assume common schemas, geographic coverage or commercial reuse rights.

## 3. System operation and market data

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
- i-DE methodology explicitly warns about interdependent nodes, non-additivity and the need for a specific connection study.
- e-distribución November 2026 pages expose separate official CSV/XLSX files for demand and generation, including the direct CSV download URLs recorded above.

This catalog should be expanded only after each new source has been opened and its schema, cadence and terms inspected.
