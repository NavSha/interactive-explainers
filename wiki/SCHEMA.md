# Wiki Schema — Interactive Explainers

A planning layer for the "AI for Builders" site. Adapted from Karpathy's "LLM Wiki"
pattern (compilation over retrieval), but **flipped**: articles are the
deliverable, this wiki is the brain that reasons about what to write next.

## Purpose

- Track what's covered across the 8 topic series.
- Surface what's missing (planned articles, orphan concepts, thin topics).
- Maintain a shared vocabulary of themes and entities across the site.
- Run periodic health checks (LINT) and audits (REFLECT) to grow the site.

## Layout

```
wiki/
├── SCHEMA.md         # this file
├── INDEX.md          # topic registry + map links
├── LINT.md           # coverage health (auto/semi-auto)
├── REFLECT.md        # periodic "what to write next" audit
├── maps/             # one file per topic (8 topics)
├── themes/           # cross-cutting concepts (RAG, HITL, tool use, ...)
└── entities/         # named things (Claude, MCP, ReAct, ...)
```

## Topic map — `maps/<slug>.md`

```yaml
---
type: map
domain: <slug>              # matches INDEX.md registry
last_updated: YYYY-MM-DD
parts_live: N
parts_planned: N
---
```

**Sections (all required, may be empty):**

- **Articles**
  - `Written` — existing HTMLs with one-liner summaries
  - `Planned` — subtopics on the backlog, each with a `Gap:` rationale
  - `Considered, dropped` — ideas rejected, with reason
- **Themes** — concepts cutting across 2+ articles in this topic
- **Entities** — named tools/models/protocols/patterns appearing in the series
- **Cross-topic bridges** — connections to other topics
- **Sources** — external reading that informed the series

## Theme page — `themes/<slug>.md`

Create when a concept appears in 2+ articles with real substance.

```yaml
---
type: theme
domains: [<slug>, ...]
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

Sections: *Summary* (≤ 3 sentences) · *Articles mentioning it* · *Builder takeaway*.

## Entity page — `entities/<slug>.md`

For named things the site references (models, tools, protocols, patterns, orgs).

```yaml
---
type: entity
kind: model | tool | protocol | pattern | org
domains: [<slug>, ...]
---
```

Sections: *What it is* · *Articles mentioning it* · *Canonical link*.

## LINT checks

- **Orphan concepts** — terms mentioned 3+ times across articles with no theme/entity page backing.
- **Stale articles** — `last_updated` > 180 days and concept drift since.
- **Topic imbalance** — `parts_live` vs. `parts_planned` skew.
- **Broken cross-refs** — internal links between articles that 404.
- **Missing bridges** — articles in different topics referencing overlapping concepts.

## REFLECT pass

Periodic (quarterly or on-demand). Produces:

- Ranked backlog of `Planned` articles (gap severity × reader interest).
- Stance audit — does the site take positions? Still current?
- Topic balance check — which topic is thinnest and why.
- One unexpected bridge proposal.

## Conventions

- **Topic slugs match directory names**: `agents/` ↔ `agents`.
- **Links from wiki use relative paths**: `../../agents/tools.html`.
- **Dates in YYYY-MM-DD**, always absolute.
- **Planned articles must include `Gap:`** — why this omission matters.
- **Dropped entries must include `Why:`** — future-you will forget.
- **Immutable written articles in the wiki** — if content changes, bump `last_updated` in the map entry.

## What this wiki is NOT

- Not a CMS — articles still live as HTML in topic dirs.
- Not published — `wiki/` is planning context, not part of the site.
- Not a replacement for `CLAUDE.md` — CLAUDE.md tells Claude *how* to work here; the wiki tells Claude *what* is covered and missing.
