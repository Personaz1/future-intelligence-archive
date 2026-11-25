# ICV SU-SUZ field mapping and interpretation

Source: ICV attribute dictionary for the SU-SUZ inventory:
https://icvficherosweb.icv.gva.es/04/geonetwork/definicion_datos/0702_inventario_su_suz_mdatos.pdf

Publisher dataset page:
https://dadesobertes.gva.es/es/dataset/inventario-de-suelo-urbano-y-urbanizable-su-suz-en-la-comunitat-valenciana

Licence: Creative Commons Attribution (CC BY), as shown on the publisher page.
Publisher caveat: the inventory is informative; consult the relevant planning
instrument and competent authority for legally valid status.

## Field dictionary

| Source field | Spanish alias / meaning | Normalized field | Interpretation |
|---|---|---|---|
| municipio | Municipio | municipality | Municipality name |
| cpm | Código INE | municipality_ine_code | Province/municipality INE code |
| pp | PP | partial_plan_name | Partial plan name |
| ue | UE | execution_unit | Execution unit |
| uso | Uso global del suelo | global_land_use | industrial, residential, tertiary, facilities |
| sup | Área (m²) | planning_area_m2 | Sector area according to planning document |
| edif_total | Edificabilidad (m²) | permitted_buildable_floor_area_m2 | Total buildable floor area / floor-space allowance |
| f_aprob | Aprobación PP | partial_plan_approval_date | Partial-plan approval date |
| f_public | Publicación PP | partial_plan_publication_date | Publication date in the provincial bulletin |
| org_res | Órgano | approving_authority | Municipality or Generalitat |
| legisl | Legislación | planning_legal_framework | LRAU / LUV / LOTUP |
| ord_porm | PP aprobado | partial_plan_approved | Yes / no |
| gestion | Gestión | development_management | Direct / indirect / owners |
| pai | PAI Adjudicado | PAI_awarded | Awarded / not awarded |
| Pr_repc | Reparcelación | reparcelation_status | Not started / processing / awarded |
| f_reparc | Registro | reparcelation_registry_date | Date reparcelation project was registered |
| p_urbaniz | Urbanización | urbanisation_project_exists | Whether an urbanisation project exists |
| f_incio | Inicio obras | urbanisation_works_start_date | Start date of urbanisation works |
| f_recep | Recepción obras | urbanisation_works_acceptance_date | Date works were accepted |
| f1acceso_r | Rodado | road_access | Road access yes/no |
| f2aceras | Aceras | sidewalks | Sidewalks yes/no |
| f3alumbrad | Alumbrado | public_lighting | Public lighting yes/no |
| f4agua_pot | Agua Potable | potable_water | Potable water yes/no |
| f5electric | Electricidad | electrical_installation | Electrical installation yes/no |
| f6alcantar | Alcantarillado | sewerage | Sewerage yes/no |
| f7pluviale | Pluviales | stormwater_collection | Stormwater collection yes/no |
| f8colector | Colector | collector_connection | Collector yes/no |

## Normalization rules

- Preserve the raw source value in every normalized record.
- Normalize Spanish accented yes/no values (Sí, No) without discarding the
  original spelling.
- Keep not_recorded distinct from no.
- Keep PAI award and reparcelation states distinct.
- Keep planning approval, reparcelation, urbanisation project and works
  acceptance as separate milestones.
- An empty acceptance date does not prove that works have not been completed;
  it means the source does not record an acceptance date.
- An electrical installation is a site-service indicator only. It is not
  available MW, voltage, transformer headroom, a granted access right or proof
  of an electrically feasible connection.

## Implemented tools

- CSV acquisition: experiments/fetch_gva_land_layers.py --sources su_suz_csv
- Normalization:
  experiments/normalize_suz_development_readiness.py input.csv output.jsonl
- Tests:
  tests/test_fetch_gva_land_layers.py,
  tests/test_normalize_suz_development_readiness.py

The acquisition and normalization code is committed. A live download and schema
validation have not yet been performed in this environment.
