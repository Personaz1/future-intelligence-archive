# Competitive benchmark — Rare Context

Reviewed: 2026-11-25

## What is already built

Rare Context describes itself as a sourced database of scarce assets and their
owners: powered land, power plants, data centres, substations, grid capacity,
mines and water rights.

Its Spanish distribution-capacity source page reports:
- 16,548 facts held from Spanish distribution operators;
- 18,955 source records in its public substations JSONL snapshot;
- 2,381 substations represented in the linked substations pages;
- monthly refresh;
- source coverage for e-distribución (including EASA and Ceuta), i-DE,
  Viesgo, E-REDES and BEGASA;
- UFD not collected at the time of its page, citing access failures.

Crucially, it does **not** publish the values of restricted Spanish operator
capacity facts. It publishes that a fact exists, its label and its source, and
offers further research on request. It states that each fact retains the
licence of its source.

The public site-screening API currently documents site coverage for the
Netherlands, United Kingdom and Germany. Its filters include land size,
distance to substations, voltage, grid headroom in Great Britain, zoning,
environmental designations, permits and water stress. Spain is not listed as a
site-screening country in the API documentation inspected here.

## Strategic implications

1. **The general concept is not novel.** A sourced asset/owner/land/grid
   intelligence layer already exists. A generic "map of substations plus
   capacity" would be a weak differentiator.
2. **The Spanish data-rights problem is real.** Rare Context's treatment of
   Spanish operator capacity as restricted/listed-only is consistent with the
   operator legal notices reviewed separately.
3. **There may be a geographic wedge.** The inspected Rare Context site API
   documents site screening in NL, GB and DE, not Spain. A Spain-first workflow
   could fill a regional coverage and workflow gap, subject to data rights.
4. **A stronger wedge is explainable project due diligence.** Combine parcel
   constraints, planning status, grid topology, connection-point identity,
   affected transmission nodes, regulatory queue states, water and cooling,
   fibre and project-specific load profiles. Show exactly which evidence is
   open, restricted, missing or inferred.
5. **Do not clone their restricted-data approach blindly.** Listing a fact
   without its value may be lawful under their interpretation and product
   design, but this archive has not independently established that this
   approach is legally safe for every source. Obtain Spanish legal advice.

## Differentiation hypotheses to test

- Spanish local-authority and regional planning integration is more complete
  than generic international site maps.
- Industrial and data-centre load screening is treated as seriously as
  generation siting.
- The tool exposes electrical influence zones and the actual reason a node is
  constrained, rather than relying on nearest-substation distance.
- It tracks changes between monthly source snapshots and identifies when a
  site's evidence changed materially.
- It returns a project-specific diligence dossier, not merely a map pin or
  numeric score.

These are hypotheses, not demonstrated advantages. Compare the actual
Rare Context product and any other vendors before committing to a commercial
position.

## Go / no-go test

Proceed only if at least one of the following is true:
- a defensible Spanish data source can be commercially reused;
- operators grant a written licence for the relevant capacity data;
- the product can create material value from independently licensed sources
  and client-supplied documents without republishing restricted values;
- a paying buyer confirms a need for a Spain-specific workflow that existing
  products do not satisfy.

Otherwise, keep this as a research archive rather than turning it into a
software business.

## Sources

- Spanish distributor capacity source: https://rarecontext.com/sources/es-distribuidoras-capacidad-acceso
- Rare Context API and country coverage: https://rarecontext.com/api/sites
- Rare Context data licence: https://rarecontext.com/data-licence
