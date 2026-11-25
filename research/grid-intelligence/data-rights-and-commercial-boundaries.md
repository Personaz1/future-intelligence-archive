# Data rights and commercial boundaries

Reviewed: 2026-11-25

This is a research triage, not a legal opinion. Public accessibility, regulatory
publication duties and permission for commercial reuse are separate questions.

## Findings

| Source | Primary legal evidence reviewed | Current classification | Commercial implication |
|---|---|---|---|
| e-distribución access-capacity CSV/XLSX | Official legal notice says private viewing/reproduction only for exclusive personal use; no copying, distribution, modification, public communication or commercial use without rights-holder authorization | **Restricted without permission** | Do not redistribute, sell, publish, or build a paid service on this content until written authorization or a clearly applicable legal basis is confirmed |
| i-DE capacity map / documents | Official legal notice prohibits commercial use of site information; reproduction, transformation, distribution and public communication of content for commercial purposes require authorization | **Restricted without permission** | Same: obtain written authorization or use a legally cleared alternative |
| REE ESIOS / API data | ESIOS legal notice explicitly prohibits commercial use of its data/content; requires source and update-date attribution for permitted reuse | **Restricted for commercial use under ESIOS terms** | Do not treat REE operational time-series/API data as a free commercial feed |
| REE ArcGIS transmission GIS | Layer/service metadata inspected; a specific commercial reuse licence for the GIS feature data has not been established in this review | **Unknown / not cleared** | Keep commercial reuse on hold until the service-specific terms and rights are confirmed |
| REE access-capacity CSV/XLSX | Direct download links and methodology pages verified; a specific reuse licence for these files has not been conclusively established here | **Unknown / not cleared** | Do not assume the ESIOS terms automatically govern these files, but do not assume they are commercially reusable either |
| UFD capacity publications | Public PDFs found; source-specific commercial reuse terms not yet verified | **Unknown / not cleared** | Permission and current publication status need checking |
| Viesgo map | Public operational map found; terms for reuse of map data not reviewed | **Unknown / not cleared** | Do not scrape or republish without rights review |
| CNMC Data portal datasets | Official portal terms state CC BY-SA 4.0 and explicitly allow commercial and non-commercial reuse, subject to attribution, date, integrity and share-alike conditions | **Reusable under CC BY-SA 4.0 where the dataset is actually published in CNMC Data** | Viable open-data source class; verify each dataset's page and metadata |
| CNMC capacity maps on cnmc.es | Official capacity-map publication reviewed; no matching node-level capacity dataset was found in CNMC Data during this review | **Not cleared by CNMC Data licence** | Do not extend CNMC Data portal terms to separate maps or operator-origin data without confirmation |

## Critical distinction

CNMC's open-data portal (data.cnmc.es) has CC BY-SA 4.0 terms that permit
commercial reuse of datasets actually published in that portal. The national
capacity maps are published on the separate CNMC corporate site and aggregate
data supplied by network operators. The portal licence must not be assumed to
cover those maps or the underlying operator files.

Likewise, a statutory duty to publish access-capacity information does not by
itself establish an open licence for commercial republication.

## Product consequences

1. **No raw-data resale or public mirror** of operator datasets until rights are
   cleared.
2. **Permission-first path:** request written commercial reuse / derived-service
   permission from each operator and clarify whether storage, transformations,
   derived metrics, caching and customer reports are covered.
3. **Open-data path:** build the general geospatial, temporal and system-context
   layers from sources whose licences expressly allow commercial reuse. CNMC
   Data datasets can be used under CC BY-SA 4.0 when their individual records
   are actually published there and the attribution/share-alike obligations
   are followed.
4. **Client-supplied evidence path:** a customer may supply its own project
   documents and access correspondence. The rights to process and retain that
   material must be defined in the customer contract; do not assume this cures
   restrictions on separately sourced operator data.
5. **Research path:** retain source links, schemas, legal notices and local
   validation notes, but do not publish restricted source rows, derived
   extracts or screenshots as a substitute for permission.
6. **Legal review gate:** before a paid pilot, obtain Spanish IP / public-sector
   data-reuse advice on whether the proposed transformations and analytical
   outputs fall within each source's restrictions.

## Immediate actions

- Pause any commercial positioning that promises redistribution of operator
  capacity data.
- Draft a concise permission request to REE, e-distribución, i-DE and UFD once
  the intended product scope is stable.
- Identify datasets in CNMC Data, IGN, Cadastre, environmental agencies and
  other public sources with explicit commercial reuse terms.
- Record licence status per source snapshot in every manifest; default to
  unknown and commercial_use_not_cleared until evidence supports another
  status.

## Sources

- e-distribución legal notice: https://www.edistribucion.com/es/aviso-legal.html
- i-DE legal notice: https://www.i-de.es/es/informacion-legal
- REE ESIOS legal notice: https://www.esios.ree.es/es/aviso-legal-y-politica-de-privacidad
- CNMC Data reuse terms: https://data.cnmc.es/condiciones-de-uso
- CNMC capacity-map page: https://www.cnmc.es/sectores-que-regulamos/energia/supervision-del-mercado-electrico/informe-acceso-y-conexion-redes
