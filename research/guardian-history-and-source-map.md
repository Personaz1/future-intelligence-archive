<!-- Curated copy for the public archive. Original source: https://github.com/Personaz1/HOUSEGUARD/blob/main/GUARDIAN/HISTORY_AND_SOURCE_MAP.md ; source blob SHA: b8dc6ab2e93dfa114dae4c1be7b6dbe382b83bee ; retrieved 2026-11-25. -->

# Guardian — historical source archaeology

**Research date:** 2026-11-25  
**Repository:** `Personaz1/HOUSEGUARD`  
**Scope:** public Git history and source files currently available in the repository. This is a source map, not a claim that every historical runtime behavior has been reproduced.

## 1. Provenance and chronology

The public Git history currently available for the Guardian subtree begins with the repository import on **2025-08-09**:

- `fc610fc4a8` — `Initial import (clean): Guardian + SmartHouse, .gitignore, integrated bridge` — 2025-08-09 13:00 UTC.
- `b88aa9341d` — `AGI PREP: Current state before major autonomy upgrade - ReAct cycle, streaming fixes, error handling` — 2025-08-16 14:06 UTC.
- `e32c93302b` — `ΔΣ::Guardian - Major architectural overhaul...` — 2025-08-16 19:24 UTC.
- `cf48a9e8ca` — `Architectural revolution: Sleeping Guardian with simple tools and triggers` — 2025-08-17 00:15 UTC.
- `517f34c023` — `Add wake-up trigger system with context switching and user command handling` — 2025-08-17 00:26 UTC.
- `677985f65c` — `Fix core.py merge conflicts - create clean version` — 2025-08-21 14:36 UTC.
- `bbb89da92b` — `Fix imports in autonomous __init__.py` — 2025-08-21 14:37 UTC.

The initial import is not necessarily the project's start date. The August 16 commit patch contains an earlier `guardian_sandbox/memory_graph.md` history with entries dated **2025-08-03**, **2025-08-05**, and **2025-08-09**. This is evidence that work and iteration predate the first public import, although those dates do not independently establish when the project was conceived.

The author's recollection is that Guardian began roughly two years before this 2026 review, in a period with far fewer ready-made agent tools. The public repository evidence presently confirms substantial work by early August 2025; it does not, by itself, prove the earlier start date. Preserve both facts without forcing them into a false exact chronology.

## 2. The original architecture was authored, not just configured

The source contains several manually designed layers:

### A. Model instruction and operating contract

`GUARDIAN/prompts/guardian_prompt.py` is the main located system prompt. It describes Guardian as a persistent subsystem, defines its workspace and memory model, names the tool interfaces, and specifies how it should coordinate chat, system analysis, and autonomous work.

Notable explicit instructions:
- direct response for ordinary tasks versus a structured reasoning procedure for complex tasks;
- a four-part complex-task sequence: analyze, plan, execute reasoning, respond;
- persistent workspace and long-term memory conventions;
- ReAct tool vocabulary: `plan_step`, `act_step`, `reflect`, and `SystemTools.react_cycle`;
- event-driven synchronization between chat, system analysis, and autonomous components.

This is a designed operating contract for a model-driven agent. It is not evidence that the model's private internal reasoning was directly observable or that every declared tool was functional.

### B. Hand-built ReAct orchestration

The August 16 source and commit notes identify a custom ReAct cycle in `ai_client/tools/system_tools.py`:

- `plan_step(goal)`
- `act_step(...)` / `act_step_autonomous(...)`
- `reflect(history)` / `reflect_autonomous(...)`
- `_is_goal_achieved(...)`
- `_needs_user_input(...)`
- `react_cycle(goal, max_steps, autonomous)`

The documented cycle is iterative: plan → act → reflect → evaluate whether the goal is achieved → continue or stop. It also records action history, handles consecutive errors, and has a user-input pause path.

Important technical qualification: the surviving implementation is a hand-authored orchestration procedure, but parts of its planner, action selection, and reflection are heuristic/rule-based (for example, keyword-based routing to system, file, home, network, or general actions). Do not describe this as a fully general reasoning engine. Its historical significance is that the control loop and tool-routing procedure were explicitly designed and implemented around the model rather than delegated to a modern agent framework.

The August 16 note `guardian_sandbox/notes/2025-08-16_autonomous_react_implementation.md` records the author's then-current intent and design choices. It should be treated as a dated development note, not as independent proof that every described behavior worked end to end.

### C. Sleeping Guardian and wake-up architecture

The August 17 commit sequence is especially important:

1. `cf48a9e8ca` reduced the previous autonomous core and introduced the **Sleeping Guardian** concept: simple observation tools, triggers, and long sleep intervals instead of constant expensive model activity.
2. `517f34c023` then expanded it into a hybrid architecture combining sleeping, missions, ReAct, and planning.

The August 17 version of `ai_client/autonomous/core.py` contains explicit types and procedures:
- `TriggerEvent`, `ObservationResult`, `Mission`, `MissionPlan`;
- `_hybrid_guardian_loop`;
- observation sources for camera, sensors, logs, and system state;
- mission scheduling and parallel execution;
- mission planning and step execution;
- wake-up triggers for user commands, emergencies, schedules, and mission requests;
- context switching into analysis, assistance, security, and maintenance modes;
- returning to sleep after work.

The same file is available in the historical commit `517f34c023f1538b80472d783f5bf46ec5ad4849`. Prefer that immutable revision when studying the August 17 implementation. The current `main` version of `core.py` contains unresolved merge-conflict markers and must not be mistaken for a clean representation of that historical design.

### D. Shared context and memory

`ai_client/autonomous/integration_hub.py` connects chat events, system analysis, and autonomous tasks. It maintains shared events/context and routes new activity into system analysis and the autonomous core.

`AutonomousMemory` in the historical core stores experiences, patterns, and strategies. Other memory modules include conversation history and user profiles. These are distinct attempts at continuity, not one unified or fully specified memory architecture.

### E. Tool interface and environment

The source tree includes explicit tool groupings for files, system operations, vision, memory, and smart-home control. The smart-home side also has sensor/actuator abstractions and MQTT integration plans.

The separate documents `docs/API_CONTRACT.md` and `docs/SIM_SPEC.md` define message topics, observations, actuator commands, fixed simulation steps, seeded randomness, and an episode lifecycle. This is a notable attempt to make agent/environment interaction reproducible and model-agnostic at the contract level.

## 3. What the chronology suggests

The commit sequence shows design iteration rather than one static architecture:

- A ReAct-oriented task loop and tool handling were already being prepared by August 16.
- The autonomous core was then deliberately simplified into a sleeping, trigger-driven architecture on August 17.
- Within roughly twelve minutes, the design expanded again to combine sleep, explicit missions, wake-up triggers, context switching, ReAct, and planning.
- The August 21 cleanup resolved a merge conflict in the autonomous core, but a later/current file again contains conflict markers. The historical commit is therefore essential evidence.

This sequence should be preserved as a series of design decisions, including reversals and unfinished transitions. Do not flatten it into a single polished architecture diagram.

## 4. Evidence quality and open questions

Use these labels when extending the archive:

- **Repository evidence:** a source file, dated note, commit, or diff exists.
- **Author recollection:** a historical detail supplied by the creator but not yet corroborated by the repository.
- **Design intent:** a prompt, TODO, comment, or architecture document specifies intended behavior.
- **Implementation evidence:** code exists for a procedure; this alone does not prove it ran correctly.
- **Runtime evidence:** logs, recordings, deployment artifacts, or reproducible traces demonstrate execution.
- **Unverified:** insufficient evidence.

Open research tasks:
1. Recover the full pre-import history if it exists in another repository, local backup, exported archive, or earlier branch.
2. Trace every revision of `guardian_prompt.py`, including its system-prompt evolution.
3. Compare the August 16 ReAct implementation with the August 17 sleeping/hybrid core and the August 21 conflict-resolution commit.
4. Recover the complete August 16 development note and related memory-graph entries from the historical commit, preserving their original wording.
5. Map which model calls actually performed planning/reflection versus which decisions were hard-coded heuristics.
6. Find logs or saved conversation traces that demonstrate the system's real runtime behavior.
7. Establish the provenance of other prompt-like files before treating them as Guardian originals. In particular, do not assume every file named like a prompt in the repository root belongs to Guardian's original prompt lineage.

## 5. Preservation rule

Do not rewrite historical code, prompts, or development notes to make them resemble current agent frameworks. Keep immutable historical revisions and dated source copies. Put modern explanations, compatibility layers, and redesigns beside them.

The objective is to reconstruct what was designed, what was implemented, what was actually run, and what the creator was trying to achieve with the tools available at the time. Preserve uncertainty rather than filling gaps with plausible stories.
