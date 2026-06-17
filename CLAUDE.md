# CLAUDE.md — Interactive Explainers

## What This Is
"AI for PMs" — a static site of interactive guides explaining AI concepts. No frameworks, no build step. Plain HTML/CSS/JS.

## Tech Stack
- HTML pages with inline `<script>` and `<style>` blocks for per-page interactivity
- Shared styles: `styles/shared.css` (Newsreader serif + Inter sans + JetBrains Mono)
- No bundler, no npm — just files served directly

## How to Preview
```bash
open index.html
# or use any local server:
python3 -m http.server 8000
```

## Deployment
- GitHub Pages from `master` branch: https://navsha.github.io/interactive-explainers/
- Push to master = auto-deploy (takes ~1 min)

## Critical: CSS Cache Busting
All site HTML files (33 as of June 2026) link to `shared.css?v=N`. **When editing shared.css, bump the `?v=N` in every HTML file** or changes won't appear on the live site. Current version: v=10.

## Structure
```
index.html                          # Landing page (topic grid)
agents/                             # Agents & Tool Use (3 parts)
  index.html, agent-loop.html, tools.html, planning.html
cost-latency/                       # Cost & Latency Tradeoffs (2 parts)
  index.html, tokens.html, latency.html
evaluation/                         # Evaluation & Testing (2 parts)
  index.html, what-makes-ai-good.html, evals-in-practice.html
context-windows/                    # Context Windows & Memory (2 parts)
  index.html, the-context-window.html, designing-for-memory.html
styles/shared.css                   # Shared design system
```

## Conventions
- Each article page has an epigraph (original 4-bar verse) between the TOC and the article prose
- Color accents per topic: Agents (blue→purple), Cost (orange→red), Eval (teal→cyan), Context (purple→pink)
- Interactive widgets use the `.widget` class system and sit between `<article class="prose">` sections


## Design Context

- **PRODUCT.md** (project root): strategic design context — register (`brand`), audience (builders shipping AI products), brand personality, anti-references, and the 5 design principles. Read before any design work.
- **DESIGN.md** (project root): the visual system — tokens, typography hierarchy ("The Three Voices Rule"), color doctrine, component specs, do's and don'ts. North Star: **"The Builder's Field Guide."**
- Accessibility floor: WCAG AA — body text ≥4.5:1, reduced-motion alternatives for all widget animations, keyboard-operable widgets.

## gstack

Use the `/browse` skill from gstack for all web browsing. Never use `mcp__claude-in-chrome__*` tools.

### Available skills

`/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/design-consultation`, `/review`, `/ship`, `/browse`, `/qa`, `/qa-only`, `/design-review`, `/setup-browser-cookies`, `/retro`, `/investigate`, `/document-release`, `/codex`, `/careful`, `/freeze`, `/guard`, `/unfreeze`, `/gstack-upgrade`
