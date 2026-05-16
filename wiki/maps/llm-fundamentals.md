---
type: map
domain: llm-fundamentals
last_updated: 2026-04-17
parts_live: 2
parts_planned: 4
---

# LLM Fundamentals

What LLMs are, how they predict, and the ML vocabulary PMs need before
everything else. The foundation course for the rest of the site.

## Articles

### Written

- [The ML Concepts Behind LLMs](../../llm-fundamentals/ml-concepts.html) — The
  vocabulary PMs need: supervised vs. unsupervised, overfitting, train/test
  split, fine-tuning vs. prompting, embeddings & similarity.
- [How LLMs Actually Work](../../llm-fundamentals/how-llms-work.html) — From
  training to inference, next-token prediction, parameters, the capability
  landscape, and limitations.

### Planned

- **Tokenization, up close** — Subwords, BPE, why `"strawberry"` confuses
  models, why tokenization explains a shocking number of weird behaviors.
  *Gap:* tokens are introduced in `cost-latency/tokens` as a pricing unit;
  the *linguistic* side of tokenization never gets explained, yet it drives
  model failures readers will hit.
- **Transformers, for PMs** — Attention, self-attention, why this
  architecture beat RNNs. *Gap:* readers keep asking "what actually makes
  LLMs different from chatbots from 2015?" and the answer lives one level below
  next-token prediction.
- **Pre-training vs. post-training vs. RLHF** — How models get their
  "personality" and alignment. *Gap:* system prompts, safety behavior, and
  model persona decisions only make sense once you understand the
  training pipeline.
- **Open vs. closed models** — Llama, Mistral, DeepSeek, GPT-4, Claude —
  licensing, hosting, cost implications. *Gap:* PMs increasingly face the
  "should we self-host?" question; the site currently assumes API-hosted models.

### Considered, dropped

(none yet)

## Themes

- **Next-token prediction as the whole story** — the site's core claim; appears
  throughout `how-llms-work` and referenced implicitly elsewhere.
- **Model capability vs. size** — scale laws, diminishing returns.
- **Embeddings as the universal representation** — connects `ml-concepts §VI`
  to `grounding/grounding-your-data §III`.

## Entities

- **Foundation model families** — GPT, Claude, Llama, Gemini.
- **Embeddings** — numerical representations of meaning.
- **Parameters** — the "size" unit (7B, 70B, 400B+).

## Cross-topic bridges

- **llm-fundamentals ↔ cost-latency** — Tokens introduced here; priced there.
- **llm-fundamentals ↔ grounding** — Embeddings covered here; used for retrieval there.
- **llm-fundamentals ↔ context-windows** — The window is a constraint of the
  architecture explained here.
- **llm-fundamentals ↔ evaluation** — "Limitations that matter" previews the
  eval problem.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
