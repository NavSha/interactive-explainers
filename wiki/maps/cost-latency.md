---
type: map
domain: cost-latency
last_updated: 2026-04-17
parts_live: 2
parts_planned: 3
---

# Cost & Latency

Tokens, pricing, model tiers, streaming, and the cost-latency-quality triangle
every AI PM ends up haggling with.

## Articles

### Written

- [Tokens, Models & the Cost Curve](../../cost-latency/tokens.html) — What
  tokens are, how pricing works, model tiers, cost at scale. The "cost per
  user action" reframe.
- [Latency, Streaming & Optimization](../../cost-latency/latency.html) — Why
  LLMs feel slow, how streaming changes perceived speed, the optimization
  playbook, the triangle.

### Planned

- **Prompt caching & batching** — Both Anthropic and OpenAI expose prompt
  caching; batching can cut bulk-job costs 50%+. *Gap:* the optimization
  playbook in `latency §III` mentions caching only in passing. This is the
  single biggest lever most PMs miss.
- **Self-hosting tradeoffs** — When running your own model on vLLM or
  similar makes financial sense. *Gap:* site assumes hosted APIs; many
  enterprise PMs need the self-host calculus.
- **Cost forecasting for launch docs** — How to put a defensible $/month
  number in a PRD before shipping. *Gap:* `tokens §IV` teaches unit economics
  but not forecasting methodology.

### Considered, dropped

- *Full model benchmarking matrix* — Why: too volatile, moves monthly.
  Better as a link-out from a theme page than an article.

## Themes

- **Unit economics of AI features** — appears in `tokens §IV`, `latency §IV`,
  and implicitly in `agents/planning`.
- **The cost-latency-quality triangle** — central to `latency §IV`; the
  closest thing to a site-wide framework.
- **Streaming as a perception hack** — `latency §II`. Crosses into `ai-ux`.

## Entities

- **Context/output pricing asymmetry** — most providers charge differently.
- **Model tiers** — frontier vs. mid vs. small (Haiku/Sonnet/Opus, Nano/Mini/etc.)
- **Streaming (SSE)** — the transport pattern.

## Cross-topic bridges

- **cost-latency ↔ llm-fundamentals** — tokens defined there, priced here.
- **cost-latency ↔ agents** — agent loops multiply token spend. See
  `agents/planning §III` (The Cost Equation).
- **cost-latency ↔ ai-ux** — streaming is a latency tactic and a UX tactic.
- **cost-latency ↔ evaluation** — quality is the third leg of the triangle.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
