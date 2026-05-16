---
type: map
domain: vibe-coding
last_updated: 2026-04-17
parts_live: 3
parts_planned: 3
---

# Vibe Coding

What it is, how to do it well, and where it breaks. The PM-to-builder
bridge topic.

## Articles

### Written

- [The Tools](../../vibe-coding/the-tools.html) — What vibe coding is, why
  PMs should care, Replit, Claude Code, the landscape.
- [The Craft](../../vibe-coding/the-craft.html) — Prompting mindset, anatomy
  of a good prompt, iteration loop, working with context, patterns and
  anti-patterns.
- [The Reality Check](../../vibe-coding/the-reality-check.html) — What vibe
  coding can't do, the quality question, when to hand off, working with
  engineers, the maintenance trap, the road ahead.

### Planned

- **Debugging with an agent** — The "read the error, paste it back, iterate"
  loop as a learnable skill. *Gap:* `the-craft` covers prompting for
  *creation*; debugging is a distinct mode with its own patterns.
- **Project structure for LLM-assisted codebases** — CLAUDE.md conventions,
  directory layouts, how to make a repo readable to an agent. *Gap:*
  readers with growing side projects hit this wall; not covered.
- **Review & commit discipline** — Git-level hygiene when every line
  might be AI-written: diff review, branch strategy, test gating.
  *Gap:* `the-reality-check §IV` (Working with Engineers) touches it;
  the *personal* discipline side is missing.

### Considered, dropped

- *Tool-specific deep dives beyond Replit/Claude Code* — Why: landscape
  moves too fast. Better as a living landscape page than static articles.

## Themes

- **PM-as-builder** — central to the series.
- **Knowing when to hand off** — `the-reality-check §III`.
- **The maintenance trap** — `the-reality-check §V`. Load-bearing warning
  for anyone treating vibe-coded projects as production.
- **Context matters more than prompts** — `the-craft §IV`. Unifies the series.

## Entities

- **Replit** — `the-tools §III`.
- **Claude Code** — `the-tools §IV`.
- **Cursor, Lovable** — mentioned in `the-tools §V`.
- **CLAUDE.md** — convention referenced implicitly; worth its own entity page.

## Cross-topic bridges

- **vibe-coding ↔ agents** — Claude Code is an agent. The patterns
  transfer.
- **vibe-coding ↔ context-windows** — `the-craft §IV` (Working with Context)
  is literally context engineering.
- **vibe-coding ↔ evaluation** — "How do you know the code works?" is an
  eval question.
- **vibe-coding ↔ ai-ux** — The PM experience of *using* these tools is
  itself a case study in AI UX.

## Sources

External reading that informed this series (to be populated).

## Health

- Last reviewed: 2026-04-17 (map created)
- Content drift since last review: n/a
