# Grid Intelligence — preliminary site screening specification

Status: research specification, not an engineering model or connection decision.

## Objective

Given a parcel or approximate site polygon and a project profile, produce a
traceable first-pass assessment of whether the location deserves paid technical
due diligence for a grid connection.

Initial project profiles:
- utility-scale solar / wind;
- standalone or hybrid battery storage;
- data centre / large industrial demand;
- high-power EV charging or industrial electrification.

The product must not claim to predict permit approval from public map values.

## Output states

Use explicit states rather than a single opaque "viability score":

- `candidate_for_engineering_review`: no public-data blocker found; enough
  evidence exists to justify a formal network study.
- `reinforcement_dependent`: public evidence suggests a path may exist only
  with network reinforcement or a future position.
- `regulatory_queue_risk`: affected node is subject to a competitive allocation
  process or a regulatory commitment flag.
- `likely_blocked_in_published_scenario`: source indicates zero capacity,
  no physical position, or a hard land/environmental exclusion.
- `insufficient_evidence`: missing, stale, contradictory or unjoinable data.

These are screening states, not legal or engineering conclusions.

## Evidence layers

### 1. Site and land
- parcel geometry and cadastral identity;
- zoning / permitted land use;
- protected areas and environmental constraints;
- flood, wildfire and other physical risk;
- road access, slope and constructability;
- project-specific land area and setback requirements.

### 2. Distribution access
- operator and service territory;
- node / busbar / connection-point identifier;
- voltage;
- direction and technology;
- available, occupied, under-study and granted quantities;
- free/occupied positions;
- `0*` and regulatory-commitment flags;
- physical connection-position feasibility;
- affected transmission node;
- source publication date and methodology.

### 3. Transmission context
- nearest and electrically relevant REE nodes;
- voltage and circuit topology;
- electrical-influence-zone membership;
- access capacity by criterion and technology;
- affected transmission node / zone;
- occupied positions and request/permit pipeline where published;
- monthly circuit transport ratings (MVA) and limiting elements as context only.

Geometric proximity is not proof of electrical connectivity. A nearby high-voltage
line may not be a feasible connection route.

### 4. System and market context
- regional demand and generation mix;
- congestion / redispatch / curtailment indicators where reliable;
- renewable resource and load profile;
- nearby storage, generation and major demand projects;
- commissioning schedule and approved network reinforcements.

## Decision logic

1. Validate the site geometry and intended project profile.
2. Identify the responsible distribution operator; do not infer it from nearest
   substation alone.
3. Retrieve node-level capacity for the correct direction and technology.
4. Preserve source states: zero, zero-star, missing, not assessed, regulatory
   commitment and under study are different.
5. Resolve the affected transmission node and applicable electrical-influence
   zone where the source exposes them.
6. Evaluate the relevant transmission-side capacity and published queue context.
7. Check position feasibility, voltage-specific application thresholds and
   reinforcement dependencies.
8. Apply land/environmental hard constraints.
9. Return an evidence bundle, blockers, unresolved joins and next formal study
   required.

## Scoring policy

Do not add MW values from adjacent nodes, different voltage levels, or
interdependent zones. Do not treat circuit MVA ratings as available MW.
Do not turn missing data into a negative score or zero.

If a ranking is needed, use a transparent multi-criteria profile:
- connection evidence quality;
- published capacity state;
- physical-position feasibility;
- reinforcement dependency;
- transmission-side dependency;
- land/environmental constraints;
- data freshness and confidence.

Hard blockers must not be compensated by a high score elsewhere. Keep the
individual dimensions visible and version the ranking method.

## Minimum evidence bundle

Every screened site should include:
- input geometry and project assumptions;
- responsible operator and source node identifiers;
- original source values, units and publication dates;
- source URLs and snapshot checksums;
- exact transformations and spatial joins;
- unresolved identity matches;
- limitations and required formal studies;
- screening method version.

## First validation experiment

Use a small, manually reviewable sample in the i-DE service area in Alicante
province:
- choose several real industrial/solar/storage candidate parcels;
- compare the automated operator/node mapping with published operator maps;
- manually verify affected transmission nodes and voltage;
- test whether the method correctly distinguishes zero, zero-star,
  regulatory commitment, physical infeasibility and stale/missing records.

Only after this validation should the product produce ranked commercial
shortlists.
