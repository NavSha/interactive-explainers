---
type: map
domain: evaluation
last_updated: 2026-04-17
parts_live: 2
parts_planned: 4
---

# Evaluation & Testing

Why you can't unit-test creativity, how AI teams measure "good," and the
ship/hold decisions that separate good AI shops from great ones.

## Articles

### Written

- [What Makes AI "Good"?](../../evaluation/what-makes-ai-good.html) — The
  eval problem, taxonomy of failures, evaluation methods, the eval spectrum.
- [Evals in Practice](../../evaluation/evals-in-practice.html) — Building
  test sets, non-determinism, regression testing, ship-or-hold decisions.

### Planned

- **LLM-as-judge — done right** — Pros, failure modes (positional bias,
  verbosity bias), when to use Sonnet vs. Opus as judge. *Gap:* mentioned
  briefly in `what-makes-ai-good §III` but deserves its own treatment;
  most production evals now lean on it.
- **Human eval workflows** — Annotation pipelines, rubrics, inter-rater
  reliability, active learning. *Gap:* `evals-in-practice` assumes you know
  how to get humans to label; the operational playbook is missing.
- **Evals in production** — Logging, sampling, online vs. offline evals,
  drift detection. *Gap:* current coverage is all pre-deploy; the
  continuous-eval side isn't touched.
- **Evaluating agents (multi-turn)** — Why agent evals are fundamentally
  harder. *Gap:* cross-cuts with `agents/`, but bespoke enough to live here.

### Considered, dropped

(none yet)

## Themes

- **Non-determinism as a first-class problem** — `evals-in-practice §III`;
  also relevant to `ai-ux` (users see different answers).
- **Ship/hold decision framework** — `evals-in-practice §IV`.
- **The eval spectrum** — exact-match → human judgment, `what-makes-ai-good §IV`.

## Entities

- **LLM-as-judge** — pattern introduced in `what-makes-ai-good §III`.
- **Golden dataset** — the test set you protect at all costs.
- **Regression harness** — pattern for catching quality drops pre-ship.

## Cross-topic bridges

- **evaluation ↔ agents** — Agent eval is a category of its own; worth a bridge.
- **evaluation ↔ grounding** — RAG systems need retrieval-quality and
  generation-faithfulness metrics.
- **evaluation ↔ ai-ux** — Non-determinism is an eval problem *and* a UX problem.
- **evaluation ↔ cost-latency** — Quality is the third leg of the triangle.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
