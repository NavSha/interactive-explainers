# Launch Audit — target: 2026-07-11 (a few days out)

Pre-launch audit of the full site (33 HTML files, 29 articles across 8 series).
Worked top to bottom by an autonomous loop: pick the next unchecked item, complete
it, fix what's found, check it off, commit. One branch per phase; open a PR when
a phase completes. Merging is manual (master auto-deploys to GitHub Pages).

**Rules for the loop:**
- Fix-only discipline: fix what the audit finds; do NOT rewrite or "improve"
  articles beyond the finding. No new features, no redesigns.
- Commit after every completed item (small, revertable units).
- If shared.css changes, bump `?v=N` in ALL site HTML files (currently v=10);
  exclude `.claude/` and `wiki/` from bulk edits.
- Record findings that are out of scope under "Deferred / post-launch" at the
  bottom instead of acting on them.
- Never merge to master; stop at the PR.

## Phase 1 — Mechanical (branch: `audit/mechanical`)

- [x] Crawl all internal links across the site (landing page, series indexes,
      article prev/next, in-prose cross-links). Fix any 404s / wrong paths.
      → `scripts/check_links.py`: all internal refs resolve, 41 HTML files.
- [x] Verify every referenced asset exists (scripts, images, fonts, data files).
      → covered by the same crawler (href+src) + url() sweep: no file url() refs.
- [x] Verify `shared.css?v=10` (correct version, no stale N) on every site HTML file.
      → 38/38 pages that link shared.css are at v=10; infographics/* are
      intentionally self-contained (no shared.css link).
- [x] Load every page headless and collect JS console errors; fix any that break
      a widget or page behavior.
      → gstack browse sweep over all 41 pages (local http.server): zero console
      errors/warnings on every page.
- [x] Smoke-test the primary widget on each article page: does it respond to input?
      → Headless click-smoke on all 29 articles. FOUND + FIXED launch blocker:
      unescaped apostrophe in quiz `question: 'You're …'` strings caused a
      SyntaxError that silently killed ALL widgets on 3 pages —
      ai-ux/designing-for-uncertainty.html, cost-latency/tokens.html,
      llm-fundamentals/ml-concepts.html. New `scripts/check_scripts.py` now
      node-checks every inline script block (41 files pass). All widgets
      verified responsive post-fix.
- [x] Nav consistency sweep: "Part X of Y" counts match actual series sizes
      (LLM Fundamentals 3, Agents 4, Cost & Latency 3, Evaluation 4,
      Context Windows 3, Grounding 4, AI UX 4, Vibe Coding 4); prev/next links
      correct; series names consistent between landing page and article headers.
      → All 8 series: part counts match, all 21 next-part chains link correctly,
      breadcrumbs uniform within every series.
- [x] Landing page Latest strip is current and links resolve.
      → Current (top 3 = May 18 batch, nothing newer on master); links verified
      by crawler.
- [x] Open PR for Phase 1.

## Phase 2 — Editorial + interaction quality (branch: `audit/editorial`)

- [x] Per-article editorial review, all 29 articles (parallel sub-agents OK, one
      per article, shared rubric): factual accuracy (model names, prices, context
      sizes — flag stale claims), tone consistency (humor 2.5–3/5, confident
      conversational), epigraph present and correct format (4-bar verse), callout
      types used correctly (--insight/--analogy/--pm-tip/--summary), repeated
      analogies across articles. Fix clear errors; log judgment calls to
      Deferred instead of rewriting.
      → DONE (7 parallel review agents + fix batches, 2026-07-08): all 35 FIX
      findings in AUDIT-FINDINGS.md applied and committed (0 unchecked).
      Epigraphs + callouts structurally clean across all 29; dominant issues
      were stale 2024 model rosters/prices and internal math errors. Judgment
      calls logged under Deferred below.
- [x] Widget UX pass on every interactive widget: obvious affordance, works with
      touch (no hover-only interactions), keyboard-operable, honors
      prefers-reduced-motion. Fix mechanical gaps; log design-level issues.
      → Touch: all 3 hover handlers site-wide are progressive enhancement over
      click targets (heatmap has click twin) — no hover-only blockers.
      Keyboard: all widgets drive via real <button> elements (verified in P1
      smoke); heatmap-cell tooltips logged to Deferred as design-level.
      Reduced motion: FIXED — all 29 decorative hero canvas loops now guard
      requestAnimationFrame behind prefers-reduced-motion (render one static
      frame, no loop); finite user-triggered animations left as-is. shared.css
      already covered CSS animations.
- [x] Open PR for Phase 2.

## Phase 3 — Launch surface (branch: `audit/launch-surface`)

- [ ] OG + Twitter card meta tags on every page (title, description, og:image);
      verify one page of each series renders correctly in a card validator.
- [ ] Favicon (all standard sizes + touch icon), linked from every page.
- [ ] Custom 404 page (GitHub Pages: `404.html` at root, on-brand).
- [ ] `sitemap.xml` + per-page `<meta name="description">`.
- [ ] Mobile sweep: screenshot every page at 375px width; fix layout breaks and
      widget touch failures.
- [ ] Performance spot-check: flag any page loading heavy assets (>500KB) or
      noticeably slow on throttled connection.
- [ ] Landing-page funnel walk: landing → learning path → first article → next
      article. Confirm the path holds end to end.
- [ ] Open PR for Phase 3.

## Final gate (manual — Navneet)

- [ ] Review + merge the three PRs.
- [ ] Post-merge live-site smoke test (GitHub Pages, ~1 min deploy lag).
- [ ] Content freeze: no changes in the last 24h before launch except audit fixes.

## Deferred / post-launch

(Loop appends out-of-scope findings here — one line each, with file:line.)

- Masthead micro-widget (from June critique follow-ups)
- Breadcrumb series names are shortened vs landing-page titles (e.g. "Cost &
  Latency" vs "Cost & Latency Tradeoffs", "Vibe Coding" vs "The Builder's Guide
  to Vibe Coding"). Uniform within each series; looks intentional. Decide
  post-launch whether to align.

- Heatmap cells (the-context-window needle-in-haystack widget) expose per-cell
  tooltips only via click/hover on non-focusable divs — keyboard users can't
  reach them. Design-level: consider tabindex + focus handler post-launch.

### Phase 2 editorial JUDGMENT log (not fixed — style/verification calls)
- callout--summary label split: "Takeaway" (how-llms-work, tokenization) vs
  "Summary" (ml-concepts, most others). Pick one label series-wide.
- Name-drop density: Garry Tan attributed 3x in harness-engineering (incl.
  "Memory is markdown / Brain is a git repo" quote that doesn't read like him);
  Karpathy "hasn't typed code since Dec 2025 / late 2025" appears in
  orchestration + vibe-coding (hedged in one, flat fact in another). Verify or
  soften attributions; anchor Andrew Chen's "18 months" prediction to a date.
- "Surgeon applying bandaids" analogy verbatim in tokens.html AND latency.html;
  Anthropic "~50% agentic tool calls are software engineering" stat in all 3
  cost-latency parts; a16z "$1B revenue" stat in latency + caching-batching.
  Dedupe when next editing these.
- Klarna cited as autonomy success in human-in-the-loop.html:551 — Klarna
  publicly walked back AI-only support in 2025; acknowledging it would
  strengthen the HITL thesis.
- tools.html:68 "very articulate quadriplegic" — ableist punchline, brand risk.
- Unverifiable vendor stats in orchestration.html:790 (Cars24 250 AI coworkers,
  Klarna $50 refunds) — verify or hedge "reportedly".
- needle-in-haystack heatmap (the-context-window.html:648) presents simulated
  data as measurements — add "illustrative data" to widget instruction.
- context-engineering.html compression example undercuts its own "structured
  beats prose" claim (:227); 4K/8K framing reads dated (:157,:213).
- the-reality-check.html:962 Spot-the-Bug sample has unintended 6th bug
  (quantity/qty, productId/id mismatch) that widget calls "fine".
- designing-for-uncertainty.html:470 epigraph line 4 breaks rhyme scheme ("fam").
- streaming-ux.html:178 "serif or proportional font" category confusion →
  "proportional font (serif or sans)".
- grounding-your-data.html:367 epigraph "confidently hack" strained rhyme.
- the-craft.html:587 orphan telephone-game analogy interrupts flow.
- trust-recovery widget can show 20:1 vs prose "5 to 15" (cap at 15 or leave).
- evals-in-practice.html:222 stacks 4 stat citations in one paragraph (dense);
  "SWE-bench 60%→near-perfect" claim needs source verification (also appears in
  planning, reality-check, debugging — being softened under FIX queue).
