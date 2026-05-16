---
type: map
domain: grounding
last_updated: 2026-04-17
parts_live: 3
parts_planned: 3
---

# Grounding & Guardrails

How to make a model say true things about your data, and how to catch it
when it doesn't.

## Articles

### Written

- [Grounding Models in Your Data](../../grounding/grounding-your-data.html) —
  The RAG pipeline from first principles: embeddings, vector search,
  building your first RAG system.
- [When RAG Isn't Enough](../../grounding/when-rag-isnt-enough.html) —
  Chunking strategies, hybrid search, reranking, query rewriting.
- [Hallucinations, Safety & Trust](../../grounding/hallucinations-safety.html) —
  Confabulation by design, detection, content filtering, red-teaming,
  trust architectures, the product tradeoff.

### Planned

- **Graph RAG & structured retrieval** — When vector similarity stops being
  the right tool and entity relationships matter (Microsoft's GraphRAG,
  LightRAG, knowledge graphs). *Gap:* the RAG coverage is purely vector-based;
  the site hasn't touched structured retrieval at all.
- **Evaluating RAG systems** — Retrieval quality metrics (recall@k, MRR),
  faithfulness, answer relevance. *Gap:* `when-rag-isnt-enough` teaches
  optimizations but not how to *measure* whether they worked.
- **Citation UX & source-trust patterns** — How to surface retrieved sources
  so users can verify. Inline cites, hover previews, provenance badges.
  *Gap:* `hallucinations-safety §V` (Trust Architectures) gestures at UX but
  the UX patterns themselves belong in a dedicated page (and bridge to `ai-ux`).

### Considered, dropped

(none yet)

## Themes

- **Confabulation by design** — `hallucinations-safety §I`. The core claim
  that hallucinations aren't bugs, they're the default behavior.
- **RAG is context engineering** — bridge to `context-windows`.
- **Trust architectures** — the hierarchy of interventions from prompt-level
  to system-level.
- **The product tradeoff** — safety vs. usefulness, `hallucinations-safety §VI`.

## Entities

- **RAG (Retrieval-Augmented Generation)** — foundational pattern.
- **Vector database / vector search** — `grounding-your-data §IV`.
- **Reranker** — `when-rag-isnt-enough §IV`.
- **Hybrid search (BM25 + vector)** — `when-rag-isnt-enough §III`.
- **Red-teaming** — evaluation practice; `hallucinations-safety §IV`.

## Cross-topic bridges

- **grounding ↔ context-windows** — RAG as context engineering.
- **grounding ↔ agents** — Agents with tool use do live grounding;
  worth contrasting.
- **grounding ↔ evaluation** — RAG needs its own eval axes (retrieval,
  faithfulness).
- **grounding ↔ ai-ux** — Source citation is a trust UX problem as much
  as a retrieval problem.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
