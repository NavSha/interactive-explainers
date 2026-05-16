---
type: entity
kind: pattern
domains: [grounding, context-windows]
---

## What it is

The end-to-end system that retrieves relevant documents and injects them into an LLM's context window at inference time. Components: document ingestion → chunking → embedding → vector storage → query embedding → retrieval → reranking → prompt assembly. The pipeline is the implementation of RAG as a concept.

## Articles mentioning it

- [Grounding Models in Your Data](../../grounding/index.html)
- [When RAG Isn't Enough](../../grounding/when-rag-isnt-enough.html)
- [Designing for Memory](../../context-windows/designing-for-memory.html)

## Canonical link

<https://research.ibm.com/blog/retrieval-augmented-generation-RAG>
