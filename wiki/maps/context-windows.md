---
type: map
domain: context-windows
last_updated: 2026-04-17
parts_live: 2
parts_planned: 3
---

# Context Windows & Memory

What the window is, why bigger isn't strictly better, and how real products
fake memory that doesn't exist.

## Articles

### Written

- [The Context Window](../../context-windows/the-context-window.html) — What
  it is, how big is big, "lost in the middle," what happens when you hit the
  limit.
- [Designing for Memory](../../context-windows/designing-for-memory.html) —
  The stateless illusion, conversation history strategies, summarization,
  external memory, the memory stack.

### Planned

- **Long-context, practically** — 1M-token windows are here. What changes?
  When is it a cheat code, when is it a trap (needle-in-haystack, cost,
  lost-in-the-middle at scale)? *Gap:* `the-context-window §II` gives the
  scale but stops before the implications.
- **Context engineering** — The term has become load-bearing; it's the
  discipline of choosing *what* goes into the window, *in what order*, and
  *at what density*. *Gap:* touched implicitly, never named.
- **Compaction and summarization mid-conversation** — Hierarchical summaries,
  rolling windows, selective retention. *Gap:* `designing-for-memory §III`
  introduces summarization but not the "when to trigger it" problem in
  agent loops or long chats.

### Considered, dropped

(none yet)

## Themes

- **Lost in the middle** — `the-context-window §III`. Also relevant to
  `grounding` (chunk ordering).
- **The memory stack** — layered memory architecture; `designing-for-memory §V`.
- **Windows vs. memory vs. recall** — three different things readers conflate.

## Entities

- **Vector memory store** — class of tool; see `grounding/grounding-your-data §IV`.
- **Summarization buffers** — pattern introduced in `designing-for-memory §III`.
- **Sliding-window conversation history** — pattern.

## Cross-topic bridges

- **context-windows ↔ agents** — Agent memory = context management at scale.
- **context-windows ↔ grounding** — RAG *is* context engineering, just
  automated. Worth calling out.
- **context-windows ↔ cost-latency** — Bigger windows = bigger bills.
- **context-windows ↔ llm-fundamentals** — The window is an architectural
  constraint, not a product choice.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
