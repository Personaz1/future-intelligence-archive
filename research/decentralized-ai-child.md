# Decentralized AI System — research dossier

**Source repository:** [Personaz1/decentralized-ai-child](https://github.com/Personaz1/decentralized-ai-child)  
**Source branch:** `main`  
**Source snapshot:** `880cf8bea749d9f95f006ad1a3cac03d8a763391`  
**Snapshot date:** 2026-11-25  
**Archive role:** preservation and technical reconstruction, not a claim of operational readiness.

## 1. What the project is trying to explore

The repository is an experimental attempt to coordinate multiple AI models and computational nodes as a larger system. Its scope is broader than simple model routing. The source tree contains attempts at:

- model selection, loading, updating, and management;
- node identity, state, resource monitoring, and workload allocation;
- inter-node messages and knowledge exchange;
- consensus and conflict-prevention mechanisms;
- code analysis, automated testing, validation, backup, and security checks;
- self-reflection, evolutionary selection, and code modification;
- ethical decision records and network self-organization;
- a web interface and metrics visualization.

The central research question is whether a collection of heterogeneous models and nodes can become more capable through coordination, shared state, verification, and adaptation — and under what conditions this is actually better than one strong model.

The project should be read as an early architecture experiment. Module names and documentation describe intended capabilities, not proof that those capabilities work end to end.

## 2. Architecture visible in the source tree

### Coordination and orchestration

- `src/core/decentralized_ai.py` defines `DecentralizedAISystem`. It wires reflection, evolution, testing, validation, code analysis, LLM integration, and security components. It starts recurring asynchronous background loops and contains a request path that selects an available node.
- `src/main.py` is an intended application entry point. It loads YAML configuration and initializes the system.
- `src/core/node.py` defines a basic node state and a small PyTorch feed-forward network. Its communication and learning methods are placeholders rather than a completed distributed learning implementation.

### Communication and shared knowledge

- `src/communication/protocol.py` defines a typed message model and an in-process asyncio queue with subscriber callbacks. The message-processing loop still contains a placeholder.
- `src/core/knowledge_exchange.py` and model-management modules indicate an intended exchange/update layer. Their actual semantics and failure behavior need deeper review.
- `src/core/consensus.py` models proposed changes as hash-linked blocks and counts validator identifiers. This is a simple local validation ledger, not a demonstrated distributed consensus protocol: the visible implementation does not establish independent validator identity, network agreement, Byzantine fault tolerance, persistence, or protection against a single process controlling the validator list.
- `src/core/evolutionary_consensus.py` collects proposals, updates node reputation, combines proposal parameters, and selects a new rule. Its improvement evaluator currently returns `True` unconditionally (marked TODO), so the code does not demonstrate that a new rule is better.

### Adaptation and self-modification

- `src/core/self_evolution.py` contains a population / fitness / selection / mutation workflow.
- `src/core/self_reflection.py`, `src/core/auto_testing.py`, and `src/core/code_analysis_system.py` represent a proposed feedback loop from code inspection to suggested changes and testing.
- `src/core/decentralized_ai.py` includes an `_apply_improvement` path that attempts backup, security validation, validation, file writes, module reload, and change-history recording.
- These mechanisms are important as architectural intent. They must not be described as safe autonomous self-improvement without demonstrating the complete loop, isolation, reproducible evaluation, rollback, and resistance to prompt- or data-induced harmful changes.
- `src/core/self_replication.py` exists as a separate module. Its presence does not establish safe or reliable self-replication. Treat it as an experimental research artifact requiring isolated review.

### Model integration and resource management

The repository includes `GemmaNode`, `LLMSystem`, `ModelManager`, `ModelUpdater`, `AutoScaler`, and `PerformanceMonitor`. The configuration references Gemma 3 4B and Wav2Vec2, with CUDA-oriented settings. This indicates an intended heterogeneous local-model stack, but configuration alone does not prove that the models load, communicate, or complete a distributed task.

### Governance and safety concepts

The tree contains `ethical_system.py`, `security_system.py`, `vulnerability_detection.py`, `validation_system.py`, `backup_system.py`, and `conflict_prevention.py`. These are attempts to make adaptation and coordination inspectable and constrained. Their existence should be preserved as a design choice, not promoted as a guarantee of safety or ethical correctness.

## 3. Important source-level observations

These are direct observations from the snapshot, not assumptions about what the author intended:

1. **Consensus is not yet a distributed protocol.** The basic `Consensus` class appends validator IDs to a block and marks it validated after a count threshold. The code shown does not authenticate validators or exchange consensus state across independent nodes.
2. **Evolutionary consensus lacks a real fitness test.** `_evaluate_improvement()` is a TODO that returns `True`. The proposal-combination logic therefore cannot substantiate an improvement claim.
3. **Node learning is a placeholder.** `Node.learn()` contains `pass`; `Node.communicate()` returns a skeletal message object.
4. **The communication worker is incomplete.** `CommunicationProtocol.process_messages()` dequeues and prints messages; application-level routing and delivery semantics are not implemented there.
5. **Startup wiring is inconsistent in the snapshot.** `src/main.py` constructs `DecentralizedAISystem` with `system_root`, `logger`, and `config`, while the visible constructor in `src/core/decentralized_ai.py` accepts only an optional `config_path`. The constructor also loads its configuration with `json.load`, whereas the provided example configuration is YAML. These are concrete integration issues to resolve before claiming a reproducible launch.
6. **The web server has unresolved integration details.** The visible `src/web/server.py` refers to `Request` without importing it and assumes system methods and node attributes whose compatibility with the visible core implementation must be checked. `run_web.py` uses a `web.server:app` import path while the inspected source file is under `src/web/server.py`.
7. **Documentation contains aspirational deployment guidance.** The deployment guide mentions service names, scripts, ports, and monitoring endpoints. Those instructions are not evidence that the corresponding deployment assets or services exist in the current tree.
8. **Tests are present, but test files are not test results.** The repository includes tests for node behavior, LLM behavior, security checks, and broader system behavior. Their presence is useful evidence of intended contracts; it does not establish that the suite passes in the current environment.

## 4. Research questions worth carrying forward

### Multi-model coordination
- What should be the true unit of coordination: model instance, agent, process, physical node, task, or shared memory?
- When should a task be routed to one model, several independent models, or a staged pipeline?
- How can the system estimate whether model diversity adds information rather than correlated repetition?
- What is the cost of coordination in latency, tokens, bandwidth, memory, and operational complexity?

### Consensus versus verification
- Agreement is not correctness. How should the architecture distinguish consensus, independent verification, evidence aggregation, and calibrated uncertainty?
- Can validators be made meaningfully independent in model family, context, data, execution environment, and incentives?
- How should a system handle minority reports, unresolved disagreement, and adversarial nodes?
- What evidence should be required before a proposed model, code, or policy change is accepted?

### Identity, state, and fault tolerance
- What identity is stable across restarts, model updates, and node migration?
- Which state is local, replicated, shared, derived, or authoritative?
- How are stale state, partitions, duplicate messages, partial failure, replay, and conflicting writes handled?
- What is the recovery model when a node disappears during a long-running task?

### Learning and adaptation
- How can a system distinguish genuine improvement from metric gaming, overfitting, or regression on unmeasured tasks?
- Which changes should be proposed, simulated, sandboxed, independently tested, and approved?
- Can a system learn from task outcomes without silently rewriting its own evaluation criteria?
- How should negative results and failed generations be preserved?

### Long-running agency
- What becomes possible when agents retain task state and exchange observations over hours or days?
- How should goals, subgoals, commitments, memory, and provenance be represented?
- How can a future system reconstruct why a decision was made and which evidence changed it?

## 5. Connections to the wider research network

- **Guardian:** compare persistent task loops, memory, tool use, and orchestration. Guardian is a separate historical agent experiment; no shared runtime is implied.
- **TORI:** a possible future synthesis and comparison point for general-intelligence architectures. It is not an implemented integration.
- **TORUS and QTI:** potential sources of alternative representations or memory hypotheses. These links are research questions, not demonstrated transfers.
- **SMARTHOUSE / HOUSEGUARD:** practical environments for studying state synchronization, tool permissions, feedback, and long-running tasks.
- **Lean formalization projects:** possible sources of sharply specified reasoning and verification tasks.

## 6. Evidence and maturity labels

| Item | What the source supports | What it does not establish |
|---|---|---|
| Model and node modules | A modular architecture was attempted | Reliable distributed inference |
| Message protocol | Message schema, queue, subscriptions | Robust network transport or delivery guarantees |
| Consensus classes | Basic validator-count and proposal logic | Byzantine consensus or correctness |
| Evolution modules | Population, proposal, mutation, and selection structures | Measured autonomous improvement |
| Reflection / testing / validation modules | Intended feedback workflow and component boundaries | Safe self-modification in production |
| Ethical and security modules | Explicit attempts at policy and safety checks | Ethical correctness or comprehensive security |
| Tests | Test cases and expected behavior | Passing CI or verified coverage |
| Deployment docs | Intended operational shape | Successful deployment |

## 7. Preservation note

Keep the original source and its commit history intact. Do not rewrite the old implementation to make it resemble a current agent framework. Add modern interpretations, comparisons, test results, and replacement designs as separate dated documents. If a future system revisits this work, it should be able to distinguish:

- what was actually coded;
- what the documentation claimed;
- what the code author was trying to explore;
- what remained a placeholder;
- what failed or was never evaluated;
- what later research independently confirms or rejects.

The original short research note is preserved separately in [decentralized-ai-child-original-notes.md](decentralized-ai-child-original-notes.md).
