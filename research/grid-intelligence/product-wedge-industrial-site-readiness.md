# Product wedge — industrial land readiness and energy-site diligence

Status: commercial hypothesis; not yet validated with buyers.

## The specific problem

Energy-intensive projects often begin with a site that looks attractive on a map:
industrial designation, a large parcel, nearby power infrastructure and a
reasonable asking price. That view can hide development friction:

- a sector may have a partial plan but no completed reparcelation;
- urbanisation works may be unstarted or not accepted;
- road access or basic services may be absent;
- the zoning layer may be informative rather than legally decisive;
- an existing DIC declaration may apply only to a different use or under
  specific conditions;
- a mapped electrical installation says nothing about available connection
  capacity.

The opportunity is to make these hidden distinctions legible before a buyer
spends time and money on a site.

## Initial customer and job

Primary candidate customers:
- battery-storage and renewable project developers;
- data-centre and high-load industrial developers;
- industrial land acquisition teams;
- infrastructure and energy investment funds;
- specialist land brokers serving energy projects.

Job to be done: "Before I option, buy or commission detailed engineering on this
site, tell me what is already documented, what is incomplete, what is legally
uncertain, and what I must verify next."

## First deliverable: a site evidence dossier

For each parcel or development sector, return:

1. **Land identity:** parcel/sector identifiers, municipality, geometry, area.
2. **Planning context:** zoning and classification fields, source dates,
   approving authority, legal framework, and explicit warning where the source
   is informative.
3. **Development maturity:** partial-plan approval/publication, PAI award,
   reparcelation stage, urbanisation project and works status.
4. **Physical services:** road access, water, sewerage, stormwater, public
   lighting and recorded electrical installation.
5. **Environmental/physical context:** protected areas, flood, terrain, land
   cover and access constraints.
6. **Infrastructure context:** nearby mapped power assets, voltage where
   sourced, and distance; clearly marked as non-authoritative if derived from
   OSM.
7. **Grid-access evidence:** only from commercially cleared/licensed sources
   or documents supplied by the client with contractual processing rights.
   Otherwise mark as not assessed, not zero.
8. **Verification plan:** exact documents, authorities, operator studies and
   professional reviews still required.

## Why the ICV data matters

The SU-SUZ attribute dictionary contains fields that are unusually useful for
industrial land maturity: global land-use class (including industrial),
planning-sector area, buildable floor area, plan approval/publication dates,
approving authority, PAI award, reparcelation status, urbanisation project and
works dates, road access and basic services.

That makes it possible to distinguish:
- industrial land on paper;
- a planned sector with unresolved development steps;
- a sector with urbanisation in progress;
- a sector with documented accepted urbanisation works and services.

This is more informative than a simple zoning polygon, but the inventory is
explicitly informative and must be checked against binding planning documents.

## Why this is not a grid-capacity product yet

The most valuable node-level capacity information is subject to source-specific
reuse restrictions or remains uncleared. The product must not disguise this
gap. There are three valid ways to add grid evidence:
- obtain written commercial permission from the relevant operator;
- use a third-party source with a licence that covers the intended use;
- process client-provided access documents under a contract that defines
  rights, retention and derived outputs.

Until then, the product can provide land/planning readiness and infrastructure
context, while marking actual grid capacity as unassessed.

## Initial commercial test

Do not build a subscription platform first.

1. Assemble a reproducible Alicante sample using only CC BY sources.
2. Produce 5–10 evidence dossiers for real candidate industrial sectors/parcels.
3. Ask developers, land brokers and infrastructure investors to review the
   dossiers against their current manual diligence process.
4. Measure whether the report finds material issues earlier, reduces analyst
   time, or changes the order in which sites are investigated.
5. Ask whether the buyer would pay for the dossier and what evidence they would
   require before relying on it.

The sample must include weak and rejected sites, not only attractive examples.

## Commercial packaging hypothesis

- One-off paid screening dossier per site / portfolio.
- Portfolio triage for funds or developers comparing many sites.
- Later: recurring monitoring when planning status, source snapshots or
  infrastructure context changes.

The initial service is an analyst-assisted evidence product. Automate only the
repeatable joins, source snapshots and report generation after the workflow
proves useful.

## Success and failure conditions

Proceed if buyers value the development-maturity evidence and can identify
material cost/time savings. Stop or narrow the product if:
- buyers already receive the same information from their planning consultants;
- the ICV records are too stale or incomplete for reliable triage;
- legal status cannot be established efficiently;
- restricted grid data is essential to every buying decision and cannot be
  licensed or supplied by clients;
- the report does not change a real acquisition or development decision.

## Non-claims

This product does not:
- certify planning legality;
- guarantee buildability or land-use approval;
- estimate grid headroom from electrical-installation flags;
- replace environmental impact assessment;
- replace the network operator's access/connection study;
- provide legal, engineering or investment advice without qualified review.
