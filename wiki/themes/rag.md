---
type: theme
domains: [grounding, context-windows, llm-fundamentals]
first_seen: 2026-05-16
last_updated: 2026-05-16
---

## Summary

RAG augments LLM responses with retrieved external knowledge at inference time, avoiding the cost and staleness of fine-tuning. It's the dominant pattern for grounding models in proprietary or frequently-changing data. Architecturally it's context engineering — stuffing the window with relevant chunks so the model can cite rather than confabulate.

## Articles mentioning it

- [Grounding Models in Your Data](../../grounding/index.html)
- [When RAG Isn't Enough](../../grounding/when-rag-isnt-enough.html)
- [Hallucinations, Safety & Trust](../../grounding/hallucinations-safety-trust.html)
- [The Context Window](../../context-windows/the-context-window.html)
- [Designing for Memory](../../context-windows/designing-for-memory.html)
- [How LLMs Work](../../llm-fundamentals/how-llms-work.html)
- [ML Concepts](../../llm-fundamentals/ml-concepts.html)

47 mentions across 7 articles.

## Builder takeaway

RAG is not a magic box — chunk quality, retrieval relevance, and faithfulness each need their own eval axis. Treat RAG as a system with tunable knobs, not a single toggle.
