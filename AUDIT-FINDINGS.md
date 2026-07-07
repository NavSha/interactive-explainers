# Phase 2 editorial findings — FIX queue

From 7 parallel per-series reviews (2026-07-08). Apply top to bottom, check off,
commit in per-file or per-series chunks. JUDGMENT items are logged at the bottom
of AUDIT.md (Deferred) — do NOT act on them.

Pricing reference for fixes (current, July 2026): Claude Haiku 4.5 $1/$5 per MTok,
Claude Sonnet 4.x $3/$15, Claude Opus $5/$25. Where a widget needs non-Anthropic
prices, prefer genericizing ("small/mid/frontier tier") over guessing.

## llm-fundamentals/how-llms-work.html
- [ ] :1241 "factor of 68 billion" math error → "factor of 25 billion" (per-query basis)
- [ ] :1247 "inference cost approaches training cost" wrong at $1.1M/yr vs $75M → reword to lifetime line-item framing
- [ ] :517 stale lineup "GPT-4o, Claude Sonnet, Gemini Pro" → current gen names
- [ ] :1037–1117 Model Landscape widget = 2024 roster/prices → reframe as tier archetypes or refresh
- [ ] :509, :1292 "beat GPT-4" (retired) → "a frontier model"
- [ ] :1046 GPT-4o $5/$15 here vs $2.50/$10 in tokenization.html → align or drop hard prices

## llm-fundamentals/tokenization.html
- [ ] :383 inverted ratio "1 word ≈ 0.75 tokens" → "1 token ≈ 0.75 words"
- [ ] :892,:919–920 leftover LLM self-correction "Wait — that's option D" + runtime patch → set answer 'd' + clean explanation directly, delete patch block
- [ ] :903 quiz Q4 "$3.00 per request" units error ($0.003) + "they're equal" undercuts answer → fix units, adjust example so B is cheaper
- [ ] :908 quiz Q5 "100,000 chars = 20,000 tokens" → 25,000 (4 chars/token)
- [ ] :392,:449 "GPT-4" stale → current name or "GPT"
- [ ] :795–801 cost widget 2024 roster/prices → refresh (Haiku 4.5 $1/$5) or genericize
- [ ] :590 Spanish preset "marron"/"esta cambiando" → "marrón"/"está cambiando"

## agents/
- [x] agent-loop.html:990 quiz "support bot with GPT-4" → genericize "a frontier LLM"
- [x] tools.html:282 "50 tools adds" → "50 tools add"
- [x] tools.html:281 "40%+ of an 8k context window" stale framing → token-count framing
- [x] tools.html:724–726 latency bar: else-if and else both #D97706, green state unreachable → final else #059669
- [x] planning.html:528–530 calculator pricing stale (Haiku $0.25/$1.25, Opus $15/$75) → Haiku 4.5 $1/$5, Opus $5/$25
- [x] planning.html:356 "SWE-bench 60% to near 100% in a single year" overstated → soften to verified range
- [x] orchestration.html:540 "In Part 3, we showed" broken cross-ref → state stat directly
- [x] orchestration.html:436–438 callout--analogy labeled "Architecture Insight" → callout--insight + "Key Insight"
- [x] orchestration.html:470 "Both protocols donated late 2025" → A2A mid-2025, MCP late 2025

## cost-latency/
- [ ] tokens.html:188 "in 2026" pricing table stale → update tiers (Haiku 4.5 $1/$5; Opus $5/$25) AND recompute ripple: "60x" (:221), "1/60th" (:300,:579,:731,:734), JS pricing (:602,:643)
- [ ] tokens.html:225 "GPT-4o-mini/GPT-4o/o1" stale → genericize tiers
- [ ] tokens.html:235 "bandaids" → "band-aids" (also latency.html:231)
- [ ] latency.html:231 "GPT-4-class models" → "frontier-class models"
- [ ] caching-batching.html:93 "$500/day into $75" vs body math ($191) → "$190"
- [ ] caching-batching.html:275 "55% reduction on the input side" → total 55%, input ~78%
- [ ] caching-batching.html:145 "$6/million" conflicts with $3/M elsewhere → $3/M, cached "$0.30–$0.75/million"

## context-windows/
- [ ] the-context-window.html:924–931 widget roster stale + "Claude (extended) 680,000" never real → update roster, fix 680K
- [ ] the-context-window.html:721–725,:1156–1158 dropdown stale models/prices (GPT-4 $30/M) → update; keep 8K option as "Legacy 8K model"
- [ ] the-context-window.html:702 "6,200 tokens… 77%" vs own math/quiz (6,000 / 73%) → 6,000 / 73%
- [ ] designing-for-memory.html:338–341 widget dropdown stale roster → current names
- [ ] designing-for-memory.html:1056 "server-side caching doesn't exist in standard APIs" outdated (OpenAI Responses API) → soften per review

## evaluation/
- [x] what-makes-ai-good.html:1053–1058 quiz Q2 cast mismatch (stakeholder/engineer vs user/teammate) → align options + explanation
- [x] evals-in-practice.html:355–368 "take from this series" reads as finale but is Part 2 of 4 → reword + point to Part 3
- [x] evals-in-practice.html:222 "AgentCompany" → "TheAgentCompany"
- [x] evals-in-practice.html:841 "Donde está mi pedido?" → "¿Dónde está mi pedido?"
- [x] harness-engineering.html:305–308 callout--analogy labeled "Architecture Insight" → callout--insight + "Key Insight"
- [x] llm-as-judge.html:214 "GPT-4 judging Claude" → current/generic

## grounding/
- [x] grounding-your-data.html:534 "embed-v3" → "embed-v4"
- [x] when-rag-isnt-enough.html:453 "Upgrading from GPT-4" → "last year's model"
- [x] when-rag-isnt-enough.html:411 "70% of the way" vs Part 1 "80%" → align to 80%
- [x] when-rag-isnt-enough.html:639 summary labeled "Takeaway" vs series "Summary" → "Summary"
- [x] hallucinations-safety.html:1184,:1190 citation widget misattributes HackAPrompt paper (Schulhoff et al., not Perez/Ribeiro) → fix source card per review
- [x] graph-rag.html:357 "Three hops" but traversal is two (widget verdict agrees) → "Two hops"

## ai-ux/
- [x] human-in-the-loop.html:761 "(~20% vs. >40%)" reversed vs sentence order → "(>40% vs. ~20%)"
- [x] streaming-ux.html:256–270 article-nav before capstone quiz (Parts 1–2 do quiz first) → move quiz above nav
- [x] trust-recovery.html:345–359 same nav/quiz order issue → move quiz above nav
- [x] trust-recovery.html:141 "positive impact from the technology" overstates survey → scope to job impact (match Part 1)

## vibe-coding/
- [x] the-tools.html:204 TOC anchor #why-pms-should-care vs id why-this-changes-how-you-build → fix href
- [x] the-reality-check.html:477 TOC anchor #working-with-engineers vs id collaborating-on-production-code → fix href
- [x] the-reality-check.html:1275 quiz "Options B and D" → "Options A and B"
- [x] the-reality-check.html:1278,:1286 quiz person mix (you/they) → consistent second person
- [x] the-reality-check.html:732 + debugging.html:630 "SWE-bench 60% to near 100%" overstated → soften (same as planning.html:356)

## evaluation/harness-engineering.html + ai-ux (structural, decide once)
Quiz-after-nav also flagged for harness-engineering.html:317–333 — same fix as
streaming-ux/trust-recovery: move quiz above article-nav.
