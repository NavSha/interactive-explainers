# Interactive Explainers Wiki

Planning layer for the "AI for PMs" site. Tracks what's covered, what's planned,
what's missing, and what concepts cut across topics.

Last updated: 2026-04-17

Conventions in [`SCHEMA.md`](SCHEMA.md).

## Topic registry

Canonical slugs (match directory names in repo root).

- `llm-fundamentals` — what LLMs are, how they predict, training vs. inference
- `agents` — agent loops, tools, planning, failure modes
- `cost-latency` — tokens, pricing, latency tradeoffs
- `evaluation` — what "good" means, running evals in practice
- `context-windows` — the window, memory, long-context design
- `grounding` — hallucinations, RAG, safety rails
- `ai-ux` — designing for uncertainty, human-in-the-loop
- `vibe-coding` — the tools, the craft, the reality check

## Maps

- [LLM Fundamentals](maps/llm-fundamentals.md) — 2 live · 4 planned
- [Agents & Tool Use](maps/agents.md) — 3 live · 3 planned
- [Cost & Latency](maps/cost-latency.md) — 2 live · 3 planned
- [Evaluation & Testing](maps/evaluation.md) — 2 live · 4 planned
- [Context Windows & Memory](maps/context-windows.md) — 2 live · 3 planned
- [Grounding & Guardrails](maps/grounding.md) — 3 live · 3 planned
- [AI UX & HITL](maps/ai-ux.md) — 2 live · 4 planned
- [Vibe Coding](maps/vibe-coding.md) — 3 live · 3 planned

**Totals:** 19 live · 27 planned

**Totals:** 19 article pages · 8 topic indexes · 3 infographics · 1 root index = 31 HTML files.

## Health

- Latest lint: 2026-04-17 (first pass) — see [`LINT.md`](LINT.md)
- Latest reflect: pending first pass — see [`REFLECT.md`](REFLECT.md)
- Run `python3 scripts/lint.py` to regenerate.
