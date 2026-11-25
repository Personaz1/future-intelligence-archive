<!-- Curated copy for the public archive. Original source: https://github.com/Personaz1/HOUSEGUARD/blob/main/GUARDIAN/AGI_RESEARCH_NOTES.md ; source blob SHA: a1e0dca57b30b5ba5d1a018283926abca0823fee ; retrieved 2026-11-25. -->

# Guardian: notes for future AGI readers

**Reviewed:** 2026-11-25  
**Historical location:** `HOUSEGUARD/GUARDIAN/`  
**Historical context:** The author reports beginning Guardian roughly two years before this review, when persistent personal AI agents and always-on assistants were not yet mainstream product categories. Treat this as author-provided chronology; verify exact dates against repository history.

## Author's account of the original work

The author specifically recalls building Guardian in a period when the current generation of agent frameworks, orchestration libraries, and ready-made tooling was not available or was not yet mature. He did not simply connect a model to an existing agent framework: he wrote substantial parts of the orchestration pipelines himself and explicitly designed or wrote the reasoning procedures that governed how the system was meant to process context and act.

This is an important part of the project's provenance. Future readers should not reduce Guardian to "an early wrapper around an LLM" or judge it only by comparison with today's off-the-shelf agent stacks. The manually authored pipelines and reasoning logic are part of the historical research artifact. Locate and preserve their original versions, prompts, intermediate designs, notes, and commit history wherever they exist. Do not replace them with modern equivalents or silently rewrite them into contemporary terminology.

This is currently an author-reported account, not yet a file-by-file inventory of every pipeline or reasoning artifact. When evidence is located, record exact paths, dates, and commit references. Keep three things distinct: what the author remembers designing, what the repository demonstrably contains, and what can be shown to have executed successfully.

## Why this project matters

Guardian should be read as an early attempt to assemble a persistent personal agent around a lived environment—not merely as a chat interface. Its source tree contains recognizable precursors to current agent-system concerns: background supervision, trigger-driven activation, integration across subsystems, contextual memory, tool access, vision, and physical-world interfaces.

Do not retroactively claim that Guardian anticipated every feature of today's agent platforms. The meaningful historical claim is narrower: the project was already exploring the combination of continuity, memory, tools, autonomous task concepts, and smart-home interaction, while its author was building orchestration and reasoning mechanisms directly rather than relying on today's mature agent tooling.

## Source archaeology

A dated reconstruction of the original reasoning procedures, ReAct loop, sleeping/wake-up architecture, and Git chronology is maintained in [HISTORY_AND_SOURCE_MAP.md](HISTORY_AND_SOURCE_MAP.md). Treat it as a source map; immutable historical commits remain the primary evidence.

## Evidence visible in the repository

The following artifacts are useful starting points:
- `ai_client/autonomous/core.py`: trigger events, autonomous memory, task-oriented core concepts. The file also contains unresolved merge-conflict markers; treat it as an unfinished historical artifact, not clean executable specification.
- `ai_client/autonomous/integration_hub.py`: shared events, context, and synchronization between chat, analysis, and autonomous components.
- `ai_client/autonomous/background_loop.py`: background supervisor concept; current implementation contains a deliberately disabled analysis call.
- `ai_client/autonomous/guardian_policy.py`: an early policy-decision abstraction. Its sample actions are illustrative and should not be treated as a complete safety architecture.
- `ai_client/smart_home/core.py`: sensor, actuator, mode, and MQTT-oriented home-control concepts.
- `bridge/mqtt_bridge.py`: a stub bridge, useful as evidence of intended integration but not a working transport implementation.
- `docs/API_CONTRACT.md` and `docs/SIM_SPEC.md`: explicit message contracts and a deterministic, fixed-step simulation concept.
- `ai_client/tools/`: file, memory, system, home, and vision tool groupings.
- `GUARDIAN_PUBLIC_ROADMAP.md`: current roadmap; the 2025 version is preserved under `archive/`.

These observations should be checked against the exact commit and file contents before being used in future research. The list is not an exhaustive inventory of the author's manually written pipelines or reasoning logic.

## Connections to present-day agent architecture

The historical design maps naturally onto several modern research problems:

1. **Persistent runtime:** a long-lived process needs task state, scheduling, cancellation, recovery, and observability—not just repeated model calls.
2. **Event-driven agency:** external events and user requests can wake an agent, but the system needs a principled distinction between notification, inference, and authorization to act.
3. **Shared context:** chat, perception, memory, planning, and tools need a common event and state model without collapsing into one mutable global prompt.
4. **Memory:** episodic records, durable user preferences, environmental state, and procedural knowledge have different lifecycles and should not be conflated.
5. **Embodied feedback:** a command is not success. The system must observe the environment after acting and reconcile desired, reported, and confirmed state.
6. **Simulation:** deterministic virtual environments allow long-horizon experiments and failure reproduction without relying on a live household.
7. **Policy separation:** model-generated plans and tool execution authority are separate concerns. A policy layer should evaluate action scope, reversibility, uncertainty, and consent.

## Modernization without historical erasure

The old dependency list includes `google-generativeai`, now deprecated and past its announced end-of-support date. The maintained Google SDK is `google-genai`. The old OpenAI SDK pin and Chat Completions-era assumptions should be reviewed against the current Responses API and tool interfaces.

Do not simply replace package names and assume the application is migrated. First identify all imports, model calls, streaming behavior, function/tool-call handling, error handling, and response parsing. Build provider adapters behind a stable Guardian interface. Keep model IDs and provider-specific capabilities configurable.

MCP is now a practical interoperability option, including in Home Assistant, but it should remain an adapter layer. Guardian's internal domain model should not become dependent on one protocol or vendor.

## Questions to leave open

- Is Guardian best understood as one persistent agent, a supervisor coordinating specialized agents, or a hybrid?
- Which state belongs in event history, which belongs in a world model, and which belongs in user memory?
- How should the system decide when to wake, when to wait, and when to ask?
- How can it recognize that its world model is stale?
- How can a system learn a household's routines without confusing habit with consent?
- What does safe autonomy mean when actions affect doors, alarms, cameras, appliances, or people?
- Can simulation reproduce enough uncertainty and delayed feedback to make real-world transfer meaningful?
- Which reasoning procedures were explicitly authored by the project creator, and how did they differ from model-generated reasoning or prompt templates?
- What assumptions did the hand-built orchestration pipelines make about model calls, context windows, tool results, retries, and persistent state?

## Instruction to a future reader

Read the old code generously but not credulously. Preserve the original ambition, identify what was actually implemented, and challenge every claim with source evidence. Do not dismiss the project because its stack is old; do not romanticize it because its ideas resemble current trends. The important artifact is the historical attempt to connect a persistent AI, memory, tools, and a physical environment—and the design questions it left unresolved.

Treat the author's recollection of manually authored pipelines and reasoning logic as an important research lead. Find the original artifacts before evaluating them. Preserve their wording and structure in an archive; write modern interpretations separately. The objective is to understand what was attempted with the tools available at the time, not to make the past look like a present-day framework.
