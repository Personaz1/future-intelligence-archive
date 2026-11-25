# Archive index

**Snapshot date:** 2026-11-25  
**Maintainer:** Personaz1  
**Purpose:** navigation and provenance for a connected body of independent engineering and research work.

This index is deliberately conservative. A repository's existence or README description is not proof that its proposed capabilities work. Status labels below describe the current documented state, not an independent certification.

## How to interpret status

- **Prototype / implementation present** — source or application structure exists; operational completeness still requires review.
- **Research / hypothesis** — a question, model, or experimental direction exists; claims require discriminating tests.
- **Placeholder / concept** — insufficient implementation or specification to evaluate as a working system.
- **Archive** — preserved historical or dual-use material; not presented as a current product.
- **Fork / upstream** — derived work; upstream authorship and license remain material.

## Agent systems and orchestration

| Project | Repository / evidence | Documented status | Review notes |
|---|---|---|---|
| Guardian | [HOUSEGUARD/GUARDIAN](https://github.com/Personaz1/HOUSEGUARD/tree/main/GUARDIAN) · [archived research notes](research/guardian.md) · [historical source map](research/guardian-history-and-source-map.md) · [original source map](https://github.com/Personaz1/HOUSEGUARD/blob/main/GUARDIAN/HISTORY_AND_SOURCE_MAP.md) | Historical agent prototype and architecture record | Nested in HOUSEGUARD, not a separate repository. Inspect immutable historical commits and distinguish implemented orchestration from planned capabilities. |
| decentralized-ai-child | Private repository (not publicly inspectable) | Experimental multi-model / distributed architecture; currently private | Not publicly inspectable while private. Do not infer self-evolution, consensus, self-replication, or autonomous improvement from feature labels. |
| TORI | [Repository](https://github.com/Personaz1/TORI) · [archived research notes](research/tori.md) · [original notes](https://github.com/Personaz1/TORI/blob/main/AGI_RESEARCH_NOTES.md) | Placeholder / future synthesis point | No unified AGI implementation is claimed. |
| oh-my-codex | [Repository](https://github.com/Personaz1/oh-my-codex) | Fork / upstream tooling | Attribute upstream work to Yeachan-Heo; distinguish local modifications from inherited code. |
| claude-code | [Repository](https://github.com/Personaz1/claude-code) | Fork / source snapshot | Upstream identified as ultraworkers/claw-code in workspace notes; verify current provenance and redistribution rights before promoting. |

## Embodied systems and environmental feedback

| Project | Repository / evidence | Documented status | Review notes |
|---|---|---|---|
| SMARTHOUSE | [Repository](https://github.com/Personaz1/SMARTHOUSE) · [archived research notes](research/smarthouse.md) | Local-first home-automation skeleton / prototype | MQTT, API, configuration, and monitoring concepts; not represented as a finished autonomous home. |
| HOUSEGUARD | [Repository](https://github.com/Personaz1/HOUSEGUARD) | Defensive smart-home security and assurance project | Contains the Guardian historical subproject. Review actual controls, threat model, and tests before making security claims. |
| ha-mcp | [Repository](https://github.com/Personaz1/ha-mcp) | Fork / integration source | Preserve upstream attribution to homeassistant-ai/ha-mcp. |
| Biocybernetic Skin | [Repository](https://github.com/Personaz1/biocybernetic-skin) | Long-horizon biointerface concept study | Conceptual research; no demonstrated clinical or physiological efficacy is claimed. |

## Applied software and workflows

| Project | Repository / evidence | Documented status | Review notes |
|---|---|---|---|
| MoneyChange | [Repository](https://github.com/Personaz1/moneychange-es) | Multilingual currency-exchange web application with Strapi backend | Code and deployment configuration exist; do not infer live rates, production deployment, or regulatory compliance without current evidence. |
| ROMAN | [Repository](https://github.com/Personaz1/ROMAN) | Small Gemini / Streamlit administration utility | Assess current source and reproducibility before claiming operational readiness. |
| LEGALAIR | [Repository](https://github.com/Personaz1/LEGALAIR) | Legal-document processing and review prototype | No legal accuracy guarantee. |
| LEGALII Enterprise | [Repository](https://github.com/Personaz1/legalii-enterprise) | Local-first legal-document workflow prototype | Review the relevant branch and current implementation; no legal accuracy guarantee. |

## Representation, topology, and formal reasoning

| Project | Repository / evidence | Documented status | Review notes |
|---|---|---|---|
| Quantum-Topological-Intelligence (QTI) | [Repository](https://github.com/Personaz1/Quantum-Topological-Intelligence) · [archived research notes](research/quantum-topological-intelligence.md) | Topology-inspired ML hypotheses and experiments | Not quantum computing, consciousness research, or a demonstrated replacement for neural networks. Require baselines and reproducible comparisons. |
| TORUS | [Repository](https://github.com/Personaz1/TORUS) · [archived research notes](research/torus.md) | Topology-inspired generative-model research | Hypotheses require empirical comparison; avoid performance claims without results. |
| LongGapsBetweenPrimes | [Repository](https://github.com/Personaz1/LongGapsBetweenPrimes) | Lean formalization work; forked source | Verify upstream attribution and theorem status in Lean source. |
| Math Challenge Millennium | [Repository](https://github.com/Personaz1/math-challenge-millennium) | Forked Lean comparator / formalization workspaces | Do not imply a Millennium Prize problem has been solved unless a machine-checked proof and independent review support it. |

## Security, OSINT, and historical archives

These repositories are preserved as historical research context. Their presence is not an endorsement, deployment recommendation, or claim of current maintenance.

| Project | Repository | Documented status / boundary |
|---|---|---|
| ExploitIDE | [Repository](https://github.com/Personaz1/ExploitIDE) | Security-analysis IDE research; inspect current scope and safety boundaries. |
| AgentX | [Repository](https://github.com/Personaz1/AgentX) | Archived C2 / remote-agent research snapshot; not a deployable product. |
| NeuroRAT | [Repository](https://github.com/Personaz1/NeuroRAT) | Archived legacy dual-use research snapshot. |
| ScrScr | [Repository](https://github.com/Personaz1/ScrScr) | Archived SSH-authentication interception proof-of-concept. |
| Shadowbroker-archived | [Repository](https://github.com/Personaz1/Shadowbroker-archived) | Archived OSINT dashboard fork; preserve upstream attribution. |
| UltimateCarder | [Repository](https://github.com/Personaz1/UltimateCarder) | Legacy archive; not a current product. |

## Separate / frozen research

- **Human Atlas** — a separate research programme. Its dossier is frozen; do not treat it as active development unless the maintainer explicitly resumes it. The detailed working dossier remains in the private workspace and is intentionally not linked from this public archive.

## Review priorities

1. Start with the Guardian history map and inspect the cited commits, not only current files.
2. For each software project, identify executable entry points, dependencies, tests, configuration, and reproducible run instructions.
3. For research projects, identify hypotheses, baselines, datasets, evaluation protocol, and negative results.
4. Verify fork lineage and licenses before attributing code.
5. Record the exact repository, branch, commit SHA, file path, and date for every material conclusion.

## Known limitations of this index

- This is a curated navigation document, not a repository-wide code audit.
- Status descriptions are based on available project documentation and prior inspection; individual source trees and CI pipelines still need deeper review.
- Some linked repositories or branches may be private, archived, renamed, or unavailable to a public reader.
- Conceptual links do not establish shared code, shared runtime, or demonstrated causal relationships.
