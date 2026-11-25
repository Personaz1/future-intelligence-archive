# Research Project 01 — Independent Evidence and Collective Intelligence

**Started:** 2026-11-25  
**Status:** Research proposal; no discovery claimed  
**Research area:** Network science, collective decision-making, distributed cognition, multi-agent AI

## Research question

Under what conditions does interaction improve the accuracy and adaptability of a collective, and under what conditions does it destroy useful diversity by producing premature convergence?

## Motivation

The archive's ecosystem vision treats intelligence as potentially distributed across agents, memory, tools, and environment. This project narrows that broad idea to a measurable question: when does communication make a group better at solving a problem?

The project is deliberately computational. It should be possible to conduct an initial study using mathematical models, simulations, public datasets, and reproducible code, without a wet lab or specialised hardware.

## Candidate central hypothesis

**H1 — Delayed convergence hypothesis:** In environments where participants possess partially independent, noisy evidence, preserving private initial estimates before exposing participants to one another's conclusions can improve collective accuracy and robustness compared with immediate social influence.

This is a candidate hypothesis, not a novelty claim. Related ideas exist in research on wisdom of crowds, social influence, information cascades, correlated errors, deliberation, and ensemble learning. The first task is to establish what is already known and identify a genuinely unresolved boundary condition.

## Secondary hypotheses

- **H2 — Error correlation:** Increasing the correlation of participants' errors reduces the marginal value of adding more participants.
- **H3 — Structured diversity:** Networks that preserve semi-independent clusters while allowing selective cross-cluster exchange may outperform both fully isolated groups and fully connected groups on some classes of tasks.
- **H4 — Evidence-first communication:** Sharing evidence, uncertainty, and provenance may be more robust than sharing only conclusions or confidence scores.
- **H5 — Adaptive topology:** Changing communication structure in response to disagreement or detected error correlation may outperform a fixed topology in non-stationary environments.

All hypotheses are falsifiable. Null and negative results are valid outcomes.

## Scope and exclusions

Initial scope:
- binary and multi-class decision tasks with known ground truth;
- agents with controllable competence, bias, and error correlation;
- communication networks with controllable topology;
- explicit models of private estimates, social influence, evidence sharing, and shared memory;
- changing environments and component failures.

Excluded from the initial phase:
- claims about consciousness or subjective experience;
- biological or clinical interventions;
- claims that a simulated agent is equivalent to an LLM or human;
- claims of novelty before a structured literature review;
- treating agreement, agent count, or response volume as measures of intelligence.

## Experimental design

Compare at least these conditions under matched task instances and compute budgets:

1. Independent estimates followed by majority aggregation.
2. Immediate communication before estimates are finalised.
3. Delayed communication after private estimates are recorded.
4. Evidence-sharing rather than conclusion-sharing.
5. Modular networks with controlled bridges between clusters.
6. Fully connected and sparse network baselines.
7. Adaptive communication rules that change based on disagreement or reliability signals.

Vary:
- number of participants;
- individual competence;
- shared and subgroup-correlated errors;
- network topology;
- communication timing and frequency;
- confidence calibration;
- environmental drift;
- missing or unreliable participants.

## Primary measurements

- collective accuracy and regret;
- performance relative to the best individual and to an independent-vote baseline;
- calibration and uncertainty quality;
- robustness to correlated errors and misleading majorities;
- recovery after participant failure;
- information diversity retained over time;
- communication cost;
- performance on changed or unfamiliar task distributions.

A collective should not be called more intelligent merely because it generates more discussion or reaches consensus faster.

## Methodological safeguards

- Fix hypotheses and primary metrics before large parameter sweeps.
- Separate exploratory runs from confirmatory runs.
- Use multiple random seeds and report uncertainty intervals.
- Include simple baselines and ablation tests.
- Preserve code, configurations, seeds, raw outputs, and analysis.
- Search prior literature before describing any result as novel.
- Have a separate critical pass attempt to falsify the leading interpretation.
- Distinguish a new observation in our simulation from a new scientific discovery.

## First milestones

1. Map prior work on wisdom of crowds, social influence, information cascades, correlated errors, and network topology.
2. Formalise a minimal generative model with controllable independent and shared error sources.
3. Implement reproducible simulation baselines.
4. Run exploratory experiments to identify possible effects.
5. Design confirmatory experiments for any surviving effect.
6. Compare the result with existing literature and public datasets.
7. Publish code and a concise technical report only if the result survives scrutiny.

## Capability boundary

This project can be advanced with literature research, mathematical reasoning, code generation, simulation, analysis, and repository-based provenance. The current setup does not provide independent access to a physical laboratory, a panel of genuinely independent frontier models, or automatic peer review. Role-based critique within one model is not equivalent to independent replication.

The strongest possible initial outcome is a reproducible computational result or a well-defined new benchmark. A claim about real human or biological collectives would require external data and independent validation.

## Initial position

The working question is not whether groups are always smarter than individuals. It is whether we can identify the organisational conditions under which interaction creates reliable capability — and the conditions under which it destroys it.

The project begins with a hypothesis, not a conclusion.
