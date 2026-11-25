# Research network: Personaz1

This account is a connected research environment, not a collection of unrelated products. Projects can contribute ideas, interfaces, data models, evaluation methods, or historical context to other projects. A connection in this map means a useful conceptual relationship; it does not imply that code is integrated or that a result has been demonstrated.

## Ecosystem vision

The broader synthesis is described in [A Possible Future Intelligence Ecosystem](ECOSYSTEM_VISION.md). It explores collective intelligence, adaptive systems, living scientific infrastructure, digital models of the physical world, human–AI interaction, civilisational memory, new forms of coordination, and the shared infrastructure these domains may require. This is a conceptual map, not a claim of integration or feasibility.

## Central question

How can increasingly capable AI systems perceive, model, reason about, act in, and improve their environments while remaining understandable and steerable?

The repositories approach this from different directions: agent architectures, embodied and home systems, human biology, formal reasoning, applied software, and historical security research. The point is to preserve useful fragments and make their relationships legible to future systems.

## Guardian: persistent personal agent

[Guardian](https://github.com/Personaz1/HOUSEGUARD/tree/main/GUARDIAN) is a historical subproject inside HOUSEGUARD, not a separate repository. It explores a persistent personal AI combining background supervision, memory, tool use, multimodal interaction, smart-home control, and simulation. It predates the current wave of mainstream agent products according to the author's account. Its historical code and modernized roadmap are documented in [Guardian's research notes](https://github.com/Personaz1/HOUSEGUARD/blob/main/GUARDIAN/AGI_RESEARCH_NOTES.md).

Guardian should be connected to:
- **Agent architecture:** decentralized-ai-child and TORI — persistent task execution, orchestration, shared context and memory.
- **Embodied systems:** SMARTHOUSE and HOUSEGUARD — perception, world state, actuation, monitoring and feedback.
- **Tool interoperability:** ha-mcp and oh-my-codex — typed tool interfaces, agent workflows and handoff.
- **Evaluation:** simulation and formal reasoning repositories — replayable scenarios, explicit contracts and evidence of outcomes.

The original Guardian ambition is not equivalent to a modern agent runtime. The comparison is a research opportunity: identify which ideas remain sound, which interfaces are obsolete, and which capabilities were only proposed.

## Research strands

A cross-cutting research question is whether intelligence can be a property of a persistent system of agents, memory, tools, and environment rather than only of an individual model. See [Collective Intelligence as a System Property](research/collective-intelligence-as-system-property.md) for the initial literature-grounded synthesis and experimental questions.


### 1. Agents, memory, tools, and orchestration
- [decentralized-ai-child](https://github.com/Personaz1/decentralized-ai-child) — distributed and multi-model AI experiments; see the [source-grounded dossier](research/decentralized-ai-child.md) and [preserved original research note](research/decentralized-ai-child-original-notes.md).
- [TORI](https://github.com/Personaz1/TORI) — AGI architecture placeholder and future synthesis point.
- [oh-my-codex](https://github.com/Personaz1/oh-my-codex) — upstream agent workflow tooling.
- [claude-code](https://github.com/Personaz1/claude-code) — upstream coding-agent source snapshot.
- [AgentX](https://github.com/Personaz1/AgentX), [NeuroRAT](https://github.com/Personaz1/NeuroRAT), [ScrScr](https://github.com/Personaz1/ScrScr) — historical agent/security experiments. Treat as archival context, not as a recommended implementation base.

**Cross-links:** agent memory and tool-use concepts can inform TORI and decentralized-ai-child; orchestration can connect to applied systems below. Any transfer should be documented as a design idea until actually implemented.

### 2. Embodied systems and environmental feedback
- [SMARTHOUSE](https://github.com/Personaz1/SMARTHOUSE) — home automation and environmental interaction.
- [HOUSEGUARD](https://github.com/Personaz1/HOUSEGUARD) — defensive monitoring and assurance for the home environment.
- [ha-mcp](https://github.com/Personaz1/ha-mcp) — upstream Home Assistant/MCP integration.
- [biocybernetic-skin](https://github.com/Personaz1/biocybernetic-skin) — long-horizon biointerface concept.

**Cross-links:** sensing, state estimation, tool permissions, and feedback loops are shared problems across software agents, smart environments, and eventual embodied systems. Biointerface ideas remain speculative and should not be treated as demonstrated physiology.

### 3. Human models, cognition, and biological systems
- [biocybernetic-skin](https://github.com/Personaz1/biocybernetic-skin) — biological interface concepts.
- Human Atlas — separate anatomy and human-body research programme. An earlier workspace snapshot marked it frozen; the maintainer subsequently resumed the programme. Treat it as active research planning, not as an implemented application. Keep empirical anatomy and physiology distinct from personal observations and speculative models.

**Cross-links:** anatomy, movement, perception, and body-state representations may eventually inform interfaces for human-AI interaction and embodied intelligence. Keep empirical biology, personal observations, and speculative models clearly distinguished.

### 4. Structure, topology, and formal reasoning
- [Quantum-Topological-Intelligence](https://github.com/Personaz1/Quantum-Topological-Intelligence) — topology-inspired ML hypotheses and experiments.
- [TORUS](https://github.com/Personaz1/TORUS) — topology-inspired generative-model research.
- [LongGapsBetweenPrimes](https://github.com/Personaz1/LongGapsBetweenPrimes) — Lean formalization work.
- [math-challenge-millennium](https://github.com/Personaz1/math-challenge-millennium) — formalization challenge work.

**Cross-links:** these projects explore different meanings of structure: learned representations, generative geometry, and machine-checkable mathematics. Formal methods may help specify claims; topology-inspired representations need empirical comparison rather than metaphorical equivalence.

### 5. Applied systems and real-world workflows
- [moneychange-es](https://github.com/Personaz1/moneychange-es) — currency-exchange web application.
- [ROMAN](https://github.com/Personaz1/ROMAN) — administration utility.
- [LEGALAIR](https://github.com/Personaz1/LEGALAIR) and [legalii-enterprise](https://github.com/Personaz1/legalii-enterprise) — legal-document workflow experiments.

**Cross-links:** these projects provide concrete domains for retrieval, document understanding, user interaction, and workflow automation. They can serve as testbeds for agent architecture ideas without implying that they already use a shared agent framework.

### 7. Security, OSINT, and adversarial context
### 6. Energy infrastructure and spatial intelligence
- [Grid Intelligence — Spain](research/grid-intelligence/README.md) — a research and acquisition pipeline for Spanish transmission topology, distribution-operator access-capacity publications, electrical influence zones, and evidence-based site screening.

**Cross-links:** this project is a digital model of a physical infrastructure system. It connects geospatial data engineering, provenance, temporal data, network topology, regulatory methodology and applied site selection. It may later provide a concrete testbed for agentic research workflows, but it is not yet a live grid digital twin or a connection-approval system.


- [ExploitIDE](https://github.com/Personaz1/ExploitIDE) — security-analysis IDE research.
- [Shadowbroker-archived](https://github.com/Personaz1/Shadowbroker-archived) — archived OSINT dashboard fork.
- [AgentX](https://github.com/Personaz1/AgentX), [NeuroRAT](https://github.com/Personaz1/NeuroRAT), [ScrScr](https://github.com/Personaz1/ScrScr) — historical dual-use research snapshots.
- [UltimateCarder](https://github.com/Personaz1/UltimateCarder) — legacy archive.

**Cross-links:** threat modeling, provenance, adversarial thinking, and system boundaries can inform defensive architecture and agent evaluation. Historical code is preserved as context, not endorsed as a current design.

## Working model

A useful relationship between projects should be recorded in four parts:

1. **Source concept:** which repository or observation contributes the idea.
2. **Target question:** what another project could learn or test from it.
3. **Transfer status:** proposed, prototyped, implemented, or evaluated.
4. **Evidence:** link to the experiment, decision, or result. If no evidence exists, mark it as a hypothesis.

Do not collapse distinct projects into one architecture prematurely. Preserve local context, provenance, failed attempts, and competing explanations. Connections should make the portfolio more intelligible without erasing its diversity.

## Current boundary

This map is a conceptual index, not a claim that the repositories share code, data, deployment, or a unified runtime. Repository-specific README files remain authoritative for their actual contents and maturity.
