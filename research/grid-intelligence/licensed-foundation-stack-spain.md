# Commercially reusable foundation data — Spain

Reviewed: 2026-11-25

Purpose: identify data layers that can support a commercial site-intelligence
product without assuming that restricted operator capacity publications can
be republished.

This is a source shortlist, not a blanket legal opinion. Verify the licence on
the exact distribution and keep the required attribution and version metadata.

## Foundation layers

| Layer | Source | Licence / reuse status | Use in product | Main caveat |
|---|---|---|---|---|
| National geographic base | IGN / CNIG Download Centre | CC BY 4.0-compatible licence under Order FOM/2807/2015 | Base maps, topography, DEM, LiDAR, orthophotos | Follow exact CNIG attribution formula; product/service-specific terms may vary |
| Cadastral parcels | Spanish Cadastre INSPIRE WFS, catalogued in datos.gob.es | CC BY 4.0 on the published dataset record | Parcel geometry, parcel identity, building/land spatial context | Do not infer legal ownership or encumbrances; inspect exact service conditions and data fields |
| Protected areas | MITECO Natura 2000 dataset | CC BY | Hard environmental screening and distance overlays | National distribution last updated 2025-01-30 in the catalogue; check regional updates and legal designation status |
| Valencian protected-area management | Generalitat Valenciana open data | CC BY | Local pilot environmental zoning in Alicante / Comunitat Valenciana | Regional dataset; confirm authoritative legal boundaries and current amendments |
| Flood-risk zones | Official INSPIRE WMS datasets in datos.gob.es | CC BY 4.0 on catalog records | Flood exposure and exclusion / engineering-review flags | WMS is a visualization service; obtain vector source where possible and verify map scale/return period |
| Regional generation statistics | CNMC Data portal | CC BY-SA 4.0 | Installed capacity, energy sold, technology mix, number of installations | Share-alike obligations; regional/temporal statistics, not nodal grid capacity |
| Retail electricity market | CNMC Data portal | CC BY-SA 4.0 | Operator and CCAA market context, supply counts, consumption | Market statistics are not a proxy for local spare grid capacity |
| Power plants | JRC Open Power Plants Database (JRC-PPDB-OPEN) | CC BY 4.0 | Existing generation asset inventory and regional context | 2019 snapshot; explicitly incomplete; not a live register |
| Sector energy system context | JRC-IDEES-2023 | CC BY 4.0 | Historical sectoral energy balances and drivers through 2023, including industry and power generation | Modelled/disaggregated statistics, not site-specific metered demand |
| Power infrastructure volunteered map | OpenStreetMap | ODbL 1.0 | Candidate substations, power lines, transformers and route geometry | Coverage and positional accuracy vary; derivative distributed databases may need ODbL share-alike |

## Direct source references

- CNIG / IGN downloads and terms: https://centrodedescargas.cnig.es/CentroDescargas/index.jsp
- IGN data policy: https://www.ign.es/web/politica-datos
- Cadastre INSPIRE parcel WFS catalogue entry:
  https://datos.gob.es/es/catalogo/e0dat0002-spanish-general-directorate-for-cadastre-cadastral-parcel-inspire-download-service-wfs1
- Cadastre WFS GetCapabilities:
  https://ovc.catastro.meh.es/INSPIRE/wfsCP.aspx?service=wfs&version=2.0.0&request=getcapabilities
- MITECO Natura 2000 dataset:
  https://datos.gob.es/es/catalogo/e05068001-espacios-protegidos-de-la-red-natura-2000
- Valencian Natura 2000 management dataset:
  https://datos.gob.es/es/catalogo/a10002983-norma-de-gestion-de-los-espacios-protegidos-de-la-red-natura-2000
- ICV SU-SUZ inventory (CC BY):
  https://dadesobertes.gva.es/es/dataset/inventario-de-suelo-urbano-y-urbanizable-su-suz-en-la-comunitat-valenciana
- ICV COSCV 2025 land cover (CC BY):
  https://dadesobertes.gva.es/dataset/cartografia-de-ocupacion-del-suelo-de-la-comunitat-valenciana-coscv-ano-de-edicion-2025
- Flood-risk WMS catalogue entry:
  https://datos.gob.es/es/catalogo/e0dat0002-servicio-wms-web-map-service-areas-de-riesgo-potencial-significativo-de-inundacion-arpsi
- CNMC Data reuse terms:
  https://data.cnmc.es/condiciones-de-uso
- JRC Open Power Plants Database:
  https://data.jrc.ec.europa.eu/dataset/9810feeb-f062-49cd-8e76-8d8cfd488a05
- JRC-IDEES-2023: https://joint-research-centre.ec.europa.eu/what-we-do/scientific-tools-and-databases/potencia-policy-oriented-tool-energy-and-climate-change-impact-assessment/jrc-idees_en
- OpenStreetMap copyright / ODbL:
  https://www.openstreetmap.org/copyright

## What this stack can support

A legally more tractable first version can answer:
- What parcels and buildings exist around a candidate location?
- What are the terrain, slope, elevation, flood and protected-area constraints?
- What existing generation assets are nearby?
- What is the regional generation mix and demand context?
- Where does OSM indicate substations, transformers and power corridors?
- Which facts are official, which are volunteered, and which are missing?

It cannot answer from these sources alone:
- guaranteed available connection capacity;
- exact current thermal loading or dynamic stability margin;
- the operator's queue, reserved capacity or internal engineering constraints;
- whether a specific project will receive access and connection permits.

## Recommended separation

Keep source layers physically and logically separate:
1. CC BY 4.0 layers with attribution and update dates.
2. CC BY-SA 4.0 layers in a separately tracked share-alike dataset.
3. ODbL infrastructure layers in a separate share-alike database.
4. Restricted operator capacity facts excluded from commercial outputs until
   written permission is obtained.

This separation makes it easier to demonstrate provenance and prevents an
uncleared source from silently contaminating a commercially distributed
database.

## First implementation experiment

Build a small Alicante pilot using only:
- CNIG/IGN base geography and terrain;
- Cadastre parcel geometry;
- MITECO / Generalitat Valenciana protected-area layers;
- official flood-risk layers;
- CNMC Data regional energy context;
- OSM power infrastructure as a non-authoritative candidate layer.

Then compare the resulting map against the restricted operator capacity
sources only in a private research notebook, without publishing their values.
This tests how much useful screening value can be created from commercially
cleared inputs alone.
