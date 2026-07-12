---
type: map
domain: agents
last_updated: 2026-04-17
parts_live: 3
parts_planned: 3
---

# Agents & Tool Use

What separates an AI agent from a chatbot — the core loop, the toolbox, and
when *not* to reach for them.

## Articles

### Written

- [The Agent Loop](../../agents/agent-loop.html) — Think, act, observe, repeat.
  The fundamental cycle that turns a language model into something that can act.
  6 sections: The Gap → One-Shot LLM → The Loop → An Agent in Action →
  When to Use What → What's Next.
- [Tools & Function Calling](../../agents/tools.html) — How agents touch the
  real world via APIs, databases, code execution. Covers tool schemas, the
  request/response protocol, designing good tools, and the toolbox-scaling problem.
- [Planning, Failure & Tradeoffs](../../agents/planning.html) — When to use
  agents vs. not. Failure modes, cost equation, guardrails, decision framework.

### Planned

- **Multi-agent orchestration** — Supervisor/worker, debate, committees, swarms.
  *Gap:* current series treats agents as singular actors. Real production
  systems (Claude orchestration, Devin, agentic coding tools) are multi-agent.
- **Memory patterns for agents** — Scratchpads, vector recall, episodic memory,
  reflection loops. *Gap:* crosses with `context-windows`, but agent-specific
  memory patterns (compaction, summarization during loops) deserve their own page.
- **Your first agent — a build-along** — Hands-on tutorial: Claude + tool use
  API → working research agent in < 50 lines. *Gap:* current series is
  conceptual only. Builders who've read it ask "how do I actually try this?"

### Considered, dropped

- *Agent benchmarks deep dive (SWE-bench, GAIA, etc.)* — Why: too volatile,
  benchmarks will shift. Better covered as a theme page that links out.

## Themes

Concepts cutting across articles in this topic:

- **The ReAct pattern** — appears in `agent-loop` and implicitly in `tools`.
  Foundational to the entire series.
- **Tool-use reliability** — appears in `tools` and `planning`. Tools work
  individually but compound failure across loops.
- **Cost-reliability tradeoff** — `planning` covers it, but touches every article.
- **Human oversight as the practical answer** — `planning` introduces it;
  deeply connected to `ai-ux/human-in-the-loop`.

## Entities

Named things referenced in the series:

- **Model Context Protocol (MCP)** — mentioned in `tools`. Anthropic's tool
  protocol standard.
- **Function calling / tool use API** — Claude and OpenAI both expose this.
- **ReAct (Reasoning + Acting) pattern** — the archetypal loop.
- **Toolbox scaling** — design pattern, not a product; covered in `tools §V`.

## Cross-topic bridges

- **agents ↔ context-windows** — Agent memory is context management at scale.
  Each loop step adds to the window. See `context-windows/designing-for-memory`.
- **agents ↔ cost-latency** — Agent loops multiply token spend. `planning §III`
  (The Cost Equation) is the formal bridge.
- **agents ↔ ai-ux** — HITL is the practical answer to agent unreliability.
  `planning §IV` (Guardrails) → `ai-ux/human-in-the-loop`.
- **agents ↔ evaluation** — Evaluating agentic systems is fundamentally harder
  than evaluating single-turn LLMs. Worth a bridge theme.
- **agents ↔ grounding** — Agents with tool use effectively do live grounding;
  contrast with retrieval-based grounding in `grounding/`.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
