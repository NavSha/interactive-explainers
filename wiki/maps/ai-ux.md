---
type: map
domain: ai-ux
last_updated: 2026-04-17
parts_live: 2
parts_planned: 4
---

# AI UX & HITL

Designing for uncertainty, and deciding when a human belongs in the loop.

## Articles

### Written

- [Designing for Uncertainty](../../ai-ux/designing-for-uncertainty.html) —
  The UX problem with AI, confidence signals, progressive disclosure, loading
  states that don't lie, error states for AI.
- [When to Keep Humans in the Loop](../../ai-ux/human-in-the-loop.html) —
  Automation threshold, review queues, escalation patterns, feedback loops,
  the 80/20 rule, measuring success.

### Planned

- **Streaming UX patterns** — Partial answers, tool-call visibility,
  interruptibility. The chat-first mental model breaks once agents are
  involved. *Gap:* streaming is treated as a latency tactic in `cost-latency`
  but the UX grammar for it doesn't exist on the site.
- **AI onboarding patterns** — Empty states, example prompts, prompt
  discovery, scaffolded first-run. *Gap:* major product problem; first
  interaction with an AI feature is the make-or-break moment.
- **Trust recovery after failure** — Patterns for users who've been
  burned by AI: undo, explanation, escalation, graceful degradation.
  *Gap:* error states covered in `designing-for-uncertainty §V` but
  *repeat failure* and *user skepticism* are different problems.
- **Agent UX — beyond the prompt box** — Ambient agents, proactive
  suggestions, observation mode. *Gap:* the "death of the prompt box" is
  happening; site hasn't touched it.

### Considered, dropped

(none yet)

## Themes

- **Confidence signals** — `designing-for-uncertainty §II`. Cross-cuts
  with `grounding` (source citation).
- **The automation threshold** — `human-in-the-loop §I`. The core question
  every AI product eventually answers.
- **Feedback loops as product infrastructure** — `human-in-the-loop §IV`.
- **Uncertainty as first-class UX** — the series' central claim.

## Entities

- **Review queue** — pattern; `human-in-the-loop §II`.
- **Escalation pattern** — `human-in-the-loop §III`.
- **Confidence display** — bar, percentage, hedged language.

## Cross-topic bridges

- **ai-ux ↔ agents** — HITL is the practical answer to agent unreliability.
  `human-in-the-loop` ↔ `agents/planning §IV`.
- **ai-ux ↔ grounding** — Source citation UX belongs in both.
- **ai-ux ↔ evaluation** — Human-in-the-loop is both a product pattern
  *and* an eval mechanism.
- **ai-ux ↔ cost-latency** — Streaming lives in both.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
