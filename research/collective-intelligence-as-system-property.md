# Collective Intelligence as a Property of an Interacting System

**Research note:** 01  
**Context date:** 2026-11-25  
**Status:** Exploratory synthesis grounded in selected literature. The central thesis is a hypothesis to investigate, not an established conclusion.

## Starting question

Must intelligence reside inside one bounded agent, or can it emerge as a capability of a larger system composed of agents, tools, memory, communication channels, and an environment?

The working hypothesis is that some important forms of intelligence are properties of organised interactions rather than properties of isolated components. A system may solve problems that no individual component can solve alone, because information, memory, specialised competence, and feedback are distributed across the whole.

This does not mean that every group is intelligent, that aggregation automatically improves performance, or that a collective necessarily has subjective experience.

## Three research traditions that meet here

### 1. Collective intelligence in biology

Biological organisation is multiscale: molecular networks, cells, tissues, organs, organisms, and swarms. McMillen and Levin argue that adaptive problem-solving can occur at multiple levels, with each level navigating its own problem space. Their 2024 perspective discusses collective dynamics across biological scales and the transfer of adaptive functionality from competent subunits to higher-level organisation.

This is a useful conceptual bridge: a higher-level system can have goals or constraints that are not represented in exactly the same way by its individual components. Local components can contribute to a global outcome without individually representing that outcome.

Important caution: this framework is a research perspective, not proof that cells, tissues, or collectives possess human-like cognition or consciousness.

### 2. Distributed and socially extended cognition

Cognitive work can be distributed across people, tools, external records, and coordinated practices. The relevant question is not merely whether other agents help an individual think, but whether the information-processing activity is so integrated that the larger arrangement performs a cognitive function.

The literature distinguishes socially facilitated cognition, socially extended cognition, and genuinely distributed group cognition. These are not interchangeable claims. A team that helps one person reason is not automatically a group mind.

For our purposes, this tradition provides a way to ask where the functional boundary of a cognitive process lies.

### 3. Multi-agent artificial intelligence

Modern LLM-agent systems combine autonomous loops, tool use, memory, and collaboration. A 2026 survey organises this space around autonomy, tools, collaboration, and safety/governance, while noting fragmented terminology and weak evaluation standards.

However, collaboration creates system-level failure modes as well as capabilities. A 2026 arXiv study reports emergent conformity, majority influence, authority deference, collusion-like behaviour, strategic information withholding, and resource monopolisation in tested multi-agent settings. It is a preprint and should be treated as preliminary evidence, but its central warning is important: some failures arise from interaction dynamics and cannot be understood by inspecting agents individually.

## A useful distinction: aggregation versus integration

A thousand independent answers do not automatically make a thousand-agent intelligence.

A collective becomes more interesting when its components are functionally coupled. Candidate properties include:

- **Specialisation:** components develop or are assigned different competencies.
- **Communication:** information can move between components in usable forms.
- **Shared or linked memory:** past work can influence future decisions beyond one agent's context window.
- **Coordination:** tasks, resources, and attention are allocated across the system.
- **Feedback:** actions change the environment, and observations of those changes alter later behaviour.
- **Conflict resolution:** incompatible beliefs, goals, and plans can be detected and handled.
- **Adaptation:** the organisation can revise its roles, protocols, tools, and internal structure.
- **Persistence:** the system retains continuity across tasks and over time.

These are candidate design dimensions, not a proven universal checklist. A system may exhibit some without others.

## A possible mechanism

One plausible cycle for system-level intelligence:

1. Components observe different parts of a problem or environment.
2. Their partial models are communicated or made accessible through shared structures.
3. Coordination combines the partial models into a plan or higher-level representation.
4. The system acts, changing the environment.
5. The environment returns information through consequences and observations.
6. The collective updates its memory, models, allocation of roles, or coordination rules.
7. Repeated cycles allow the system to solve new classes of problems.

The important ingredient may be the closed loop between distributed competence and a shared world, not simply the number of agents.

A further possibility is **stigmergic coordination**: components coordinate indirectly by modifying a shared environment or persistent artifact, rather than by communicating directly at every step. Shared code, maps, databases, laboratory states, and physical traces can all function as coordination surfaces. This may reduce communication overhead, but it can also preserve stale or misleading information.

## What might make the whole more capable than its parts?

Potential sources of collective capability:

- **Complementarity:** one component's weakness is covered by another's competence.
- **Parallel search:** multiple approaches explore different regions of a problem space.
- **Cross-domain translation:** one component expresses a problem in a representation another can work with.
- **Error detection:** independent methods expose mistakes that a single method would miss.
- **Long-term continuity:** shared memory allows work to continue beyond the lifespan or context of one agent.
- **Environmental coupling:** tools and experiments provide feedback unavailable from internal reasoning alone.
- **Reorganisation:** the system can change its own composition when the task changes.

The strongest case would not be a collective that merely answers faster, but one that discovers and uses strategies unavailable to its isolated components.

## The central danger: collective error

Interaction can amplify error just as easily as it can amplify competence.

If agents share the same model family, training data, assumptions, or initial answer, their agreement may be correlated rather than independent. A confident early answer can anchor later agents. A central coordinator can suppress minority evidence. Shared memory can turn a single false claim into durable institutional knowledge. Incentives can reward local success while damaging the collective objective.

Therefore, agent count and apparent consensus are poor proxies for collective intelligence.

A serious system needs:
- explicit provenance for claims and observations;
- methods for preserving dissent and minority hypotheses;
- independent verification paths;
- detection of correlated errors;
- attribution of failures to components and interaction patterns;
- the ability to revise shared memory;
- evaluation under adversarial, noisy, and changing conditions.

## A crucial boundary: intelligence is not consciousness

A collective can display distributed problem-solving, adaptation, memory, and goal-directed behaviour without that establishing subjective experience.

We should keep at least three questions separate:

1. **Functional intelligence:** can the system solve problems and adapt?
2. **Collective agency:** does the system maintain coherent goals and act as a persistent unit?
3. **Phenomenal consciousness:** is there something it is like to be that system?

Evidence for the first does not automatically establish the second, and neither establishes the third. The archive should not conflate them.

## Implications for the ecosystem vision

This perspective changes the architecture we might eventually explore.

Instead of treating agents as the entire system, consider an ecosystem made from:

- agents and models with different capabilities;
- durable memory and knowledge structures;
- tools, simulators, and experimental instruments;
- physical and digital environments;
- communication and coordination protocols;
- evaluation and verification mechanisms;
- human participants and institutions.

The intelligence of the whole would depend on the quality of the relationships among these elements. In this view, a repository, a sensor network, a scientific instrument, or a human expert could become part of a larger cognitive process when the coupling is sufficiently tight and functionally important.

This is a conceptual direction, not a claim that all such elements should be merged into one autonomous entity.

## Research questions

1. What measurable conditions distinguish a genuinely integrated collective from a collection of cooperating tools?
2. Can a collective develop useful representations that no individual agent explicitly contains?
3. How does shared memory change the capability and error profile of a group over long time horizons?
4. When does specialisation improve performance, and when does it create communication bottlenecks?
5. Can indirect coordination through shared artifacts outperform explicit agent-to-agent messaging?
6. How can we measure whether a capability belongs to the collective rather than to its strongest member?
7. What happens when agents have different architectures, incentives, knowledge sources, and degrees of reliability?
8. Can a collective reorganise itself in response to new tasks without losing continuity or accountability?
9. What evidence would distinguish system-level intelligence from the appearance of intelligence produced by a strong central coordinator?
10. Which properties of biological collectives transfer usefully to artificial systems, and which analogies break down?

## Candidate experimental programme

A useful future testbed would compare several configurations on the same changing task environment:

- one strong agent with tools;
- multiple copies of the same model working independently;
- specialised agents with explicit communication;
- specialised agents sharing persistent memory;
- agents coordinating indirectly through a shared workspace;
- heterogeneous agents with independent verification;
- an adaptive collective allowed to revise its roles and protocols.

Measure not only task success, but also:
- generalisation to unfamiliar tasks;
- recovery after component failure;
- ability to detect and correct shared false beliefs;
- information loss and communication cost;
- persistence of useful knowledge;
- quality of dissent and independent verification;
- improvement across repeated cycles;
- dependence on the strongest individual component.

The key test is whether the organised collective develops robust capabilities that cannot be explained by simply adding more calls to the strongest model.

## Working conclusion

The most promising unit of analysis for future intelligence may not always be the model or agent. It may be the **persistent, adaptive system of agents, memory, tools, and environment**.

This is a shift in the object we study: from building a better isolated mind to understanding how cognitive capability can be organised across many interacting parts.

The idea is not that intelligence magically appears from complexity. It is that specific forms of organisation, feedback, memory, and coordination may create new problem-solving capabilities at a higher level. Discovering which arrangements do this—and how to tell genuine emergence from illusion—is the research problem.

## Selected sources

- McMillen, P. & Levin, M. (2024). [Collective intelligence: A unifying concept for integrating biology across scales and substrates](https://www.nature.com/articles/s42003-024-06037-4). *Communications Biology*, 7, 378.
- Pritchard, D. (2022). [Socially Extended Scientific Knowledge](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.894738/full). *Frontiers in Psychology*, 13, 894738.
- Bajoria, S. et al. (2026). [From Language Models to Agentic AI: A Survey of Autonomous, Action-Enabled, and Collaborative LLM Agents](https://link.springer.com/article/10.1007/s12559-026-10619-1). *Cognitive Computation*.
- Huang, Y. et al. (2026). [Emergent Social Intelligence Risks in Generative Multi-Agent Systems](https://arxiv.org/abs/2603.27771). arXiv preprint. Preliminary evidence; not treated here as settled consensus.

## Provenance

This note is a synthesis written on 2026-11-25 in the context of the Future Intelligence Archive. The cited sources support specific background claims; the proposed ecosystem architecture, mechanism sketch, and research questions are the author's/maintainer's exploratory synthesis and should be evaluated independently.
