# Interactive Explainers Wiki

Planning layer for the "AI for PMs" site. Tracks what's covered, what's planned,
what's missing, and what concepts cut across topics.

Last updated: 2026-05-16

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

## Themes

Cross-cutting concepts backed by dedicated pages in `themes/`.

- [RAG](themes/rag.md) — retrieval-augmented generation (grounding, context-windows, llm-fundamentals)
- [Hallucinations](themes/hallucinations.md) — confabulation by design (grounding, evaluation, ai-ux, llm-fundamentals)
- [HITL](themes/hitl.md) — human-in-the-loop (ai-ux, agents, grounding, llm-fundamentals)
- [Cost–Quality–Latency](themes/cost-quality-tradeoff.md) — the triangle (all topics)
- [Tool-Use Reliability](themes/tool-use-reliability.md) — compound failure in agent loops (agents, evaluation)
- [Next-Token Prediction](themes/next-token-prediction.md) — the site's core thesis (llm-fundamentals, grounding)

## Entities

Named things referenced across articles, backed by dedicated pages in `entities/`.

- [RAG Pipeline](entities/rag-pipeline.md) — pattern (grounding, context-windows)
- [MCP](entities/mcp.md) — Model Context Protocol (agents, grounding)
- [Claude](entities/claude.md) — Anthropic's model family (all topics)
- [Vector Database](entities/vector-db.md) — tool class (grounding, context-windows)
- [ReAct Pattern](entities/react-pattern.md) — Reasoning + Acting (agents, vibe-coding)
- [Claude Code](entities/claude-code.md) — agentic coding CLI (vibe-coding, agents)

## Health

- Latest lint: 2026-04-17 — see [`LINT.md`](LINT.md)
- Latest reflect: 2026-05-16 (first pass) — see [`REFLECT.md`](REFLECT.md)
- Run `python3 scripts/lint.py` to regenerate lint.
