---
type: theme
domains: [grounding, evaluation, ai-ux, llm-fundamentals]
first_seen: 2026-05-16
last_updated: 2026-05-16
---

## Summary

LLMs generate plausible-sounding but factually wrong output because they optimize for next-token probability, not truth. This isn't a bug — it's the default behavior of a prediction engine. The site's position: hallucinations are confabulation by design, and the product response is grounding + guardrails, not waiting for models to "get smarter."

## Articles mentioning it

- [Hallucinations, Safety & Trust](../../grounding/hallucinations-safety-trust.html)
- [Grounding Models in Your Data](../../grounding/index.html)
- [When RAG Isn't Enough](../../grounding/when-rag-isnt-enough.html)
- [What Makes AI "Good"?](../../evaluation/what-makes-ai-good.html)
- [Evals in Practice](../../evaluation/evals-in-practice.html)
- [Designing for Uncertainty](../../ai-ux/designing-for-uncertainty.html)
- [How LLMs Work](../../llm-fundamentals/how-llms-work.html)

27 mentions across 6 articles.

## PM takeaway

Don't promise "no hallucinations" — design for graceful failure. Citation UX, confidence signals, and human review loops are the product answer.
