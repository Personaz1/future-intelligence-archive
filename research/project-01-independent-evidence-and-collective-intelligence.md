# Research Project 01 — Independent Evidence and Collective Intelligence

**Started:** 2026-11-25  
**Status:** Literature audit completed; original broad hypothesis is not novel  
**Research area:** Network science, collective decision-making, distributed cognition, multi-agent AI

## Research question

Under what conditions does interaction improve the accuracy and adaptability of a collective, and under what conditions does it destroy useful diversity by producing premature convergence?

## Motivation

The archive's ecosystem vision treats intelligence as potentially distributed across agents, memory, tools, and environment. This project narrows that broad idea to a measurable question: when does communication make a group better at solving a problem?

The project is deliberately computational. Initial work can use mathematical models, simulations, public datasets, and reproducible code, without a wet lab or specialised hardware.

## Candidate central hypothesis

**H1 — Delayed convergence hypothesis:** In environments where participants possess partially independent, noisy evidence, preserving private initial estimates before exposing participants to one another's conclusions can improve collective accuracy and robustness compared with immediate social influence.

This is a candidate hypothesis, not a novelty claim. Related ideas are well established in research on wisdom of crowds, social influence, information cascades, correlated errors, deliberation, and ensemble learning.

## Secondary hypotheses

- **H2 — Error correlation:** Increasing the correlation of participants' errors reduces the marginal value of adding more participants.
- **H3 — Structured diversity:** Networks that preserve semi-independent clusters while allowing selective cross-cluster exchange may outperform both fully isolated groups and fully connected groups on some classes of tasks.
- **H4 — Evidence-first communication:** Sharing evidence, uncertainty, and provenance may be more robust than sharing only conclusions or confidence scores.
- **H5 — Adaptive topology:** Changing communication structure in response to disagreement or detected error correlation may outperform a fixed topology in non-stationary environments.

All hypotheses are falsifiable. Null and negative results are valid outcomes.

## Literature audit — 2026-11-25

The initial novelty assumption has been substantially weakened. A first-pass literature search found direct prior work covering almost every broad component of the proposal:

1. **Social influence and collective wisdom:** Human experiments show that even mild exposure to others' estimates can reduce diversity without improving accuracy, while other work finds that carefully structured social information can improve collective estimates. The relationship is conditional, not a simple independence-versus-discussion dichotomy.  
   - Lorenz et al. (2011), *How social influence can undermine the wisdom of crowd effect*: https://doi.org/10.1073/pnas.1008636108  
   - Jayles et al. (2017), *How social information can improve estimation accuracy in human groups*: https://doi.org/10.1073/pnas.1703695114  
   - Kameda, Toyokawa & Tindale (2022), *Information aggregation and collective intelligence beyond the wisdom of crowds*: https://doi.org/10.1038/s44159-022-00054-y

2. **LLM communication topology and propagation:** A 2025 EMNLP paper already studies how communication topology affects the propagation of correct and incorrect outputs, including causal interventions on individual agents.  
   - Shen et al. (2025), *Understanding the Information Propagation Effects of Communication Topologies in LLM-based Multi-Agent Systems*: https://aclanthology.org/2025.emnlp-main.623/

3. **Collective effects and group size:** A 2026 PNAS paper studies nonlinear group-size effects and collective bias in LLM populations using a controlled interaction model and mean-field analysis.  
   - Flint et al. (2026), *Group size effects and collective misalignment in LLM multi-agent systems*: https://doi.org/10.1073/pnas.2531697123

4. **Evidence ancestry and repeated reports:** A September 2026 preprint formalises the epistemic Sybil problem: multiple reports may descend from the same evidence, and report text alone cannot generally identify their evidential ancestry. It includes mathematical analysis and more than 20,000 controlled LLM-agent calls.  
   - Bara (2026), *Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence*: https://arxiv.org/abs/2609.01873

5. **Copies versus independent observations:** An October 2026 preprint directly measures how LLM aggregators count restated evidence and shows that relayed copies can trigger premature commitment.  
   - Gao et al. (2026), *Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence in Multi-Agent Systems*: https://arxiv.org/abs/2610.06192

6. **Evidence laundering:** An EMNLP 2026 paper studies false claims replicated across paraphrased web pages and tests a structural provenance gate. This directly overlaps with the proposal's evidence-provenance direction.  
   - Zhou et al. (2026), *Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence*: https://aclanthology.org/2026.emnlp-main.509/

7. **Shared agent memory:** A September 2026 preprint introduces a benchmark for correlated claim promotion into shared agent memory, including source-lineage tracking and consumer evaluation.  
   - Li et al. (2026), *A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory*: https://arxiv.org/abs/2609.30813

8. **Adaptive communication:** Recent work already learns or optimises who communicates with whom, when to communicate, and which communication topologies are useful.  
   - Leong et al. (2025), *AMAS: Adaptively Determining Communication Topology for LLM-based Multi-agent System*: https://aclanthology.org/2025.emnlp-industry.144/  
   - Li et al. (2026), *Learning Who Talks to Whom: Role-Aware Communication Topology Scheduling for Efficient LLM Multi-Agent Collaboration*: https://arxiv.org/abs/2610.25851

### Audit conclusion

The original broad proposal — delayed communication, diversity preservation, provenance-aware aggregation, and adaptive topology — is not a defensible novelty claim. These topics have direct prior art, including very recent papers. Re-running a simplified version would be useful as a replication exercise, but should not be presented as a new discovery.

This is a productive correction, not a failure. It prevents us from spending time rediscovering results already published.

## Revised candidate direction: provenance under incomplete observability

A possible remaining question is not simply whether provenance helps, but **what a collective system can reliably infer when provenance is incomplete, partially wrong, or unavailable**.

Potential experimental factors:
- true evidence ancestry is known to the evaluator but hidden or partially exposed to agents;
- metadata can be missing, noisy, or deliberately misleading;
- agents can transform evidence through summarisation, translation, quotation, and paraphrase;
- reports can share a common source while having independent extraction errors, or come from independent sources while sharing model-induced errors;
- the system must decide whether to aggregate, request more evidence, or abstain.

Candidate research question:

**Can a collective system estimate the effective number of independent evidence roots — and know when that estimate is not identifiable — under partial or unreliable provenance?**

This is only a candidate. It overlaps with the papers above and must be compared against their exact methods and limitations before any novelty claim. A useful contribution may be a carefully designed benchmark of provenance uncertainty and abstention, but that remains unproven.

## Experimental design if the revised direction survives review

Compare:
1. naive report-count aggregation;
2. text-similarity deduplication;
3. declared-source grouping;
4. evaluator-provided true ancestry (oracle upper bound);
5. uncertainty-aware aggregation that can abstain;
6. adversarially corrupted or missing provenance.

Vary:
- number of true evidence roots;
- number of reports per root;
- semantic transformation strength;
- extraction-error correlation;
- provenance completeness and corruption rate;
- proportion of adversarial reports;
- task difficulty and prior odds.

Primary measurements:
- posterior calibration;
- false-confidence and premature-commitment rate;
- accuracy and coverage;
- abstention quality;
- estimated effective evidence count versus true root count;
- robustness to provenance corruption;
- communication and compute cost.

A key distinction: report similarity is not evidence ancestry. Similar reports can arise from independent sources; dissimilar reports can descend from one source.

## Scope and exclusions

- No claims about consciousness or subjective experience.
- No claims that simulated agents are equivalent to humans.
- No novelty claim based on a literature skim.
- No use of consensus, agent count, or message volume as a proxy for intelligence.
- No claim of scientific discovery from simulation alone.

## Methodological safeguards

- Read the closest papers in full before finalising the question.
- Fix hypotheses and primary metrics before confirmatory runs.
- Separate exploratory and confirmatory experiments.
- Use multiple seeds, confidence intervals, and simple baselines.
- Preserve code, configurations, seeds, raw outputs, and analysis.
- Include ablations and a serious attempt to falsify the leading interpretation.
- Compare results against available public implementations and datasets.
- Distinguish reproduction, engineering improvement, benchmark contribution, and scientific discovery.

## Capability boundary

This project can be advanced with literature research, mathematical reasoning, code generation, simulation, analysis, and repository-based provenance. The current setup does not provide independent access to a physical laboratory, a panel of genuinely independent frontier models, or automatic peer review. Role-based critique within one model is not equivalent to independent replication.

A credible initial outcome could be a reproducible computational result, a benchmark, or a well-defined negative result. A claim about real human or biological collectives would require external data and independent validation.

## Current position

The question is not whether groups are always smarter than individuals. It is whether we can identify organisational conditions under which interaction creates reliable capability — and conditions under which it destroys it.

The broad initial hypothesis is established territory. The revised provenance-under-uncertainty direction is a lead to investigate, not a discovery.
