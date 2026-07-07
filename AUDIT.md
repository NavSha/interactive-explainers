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
- [ ] Smoke-test the primary widget on each article page: does it respond to input?
- [ ] Nav consistency sweep: "Part X of Y" counts match actual series sizes
      (LLM Fundamentals 3, Agents 4, Cost & Latency 3, Evaluation 4,
      Context Windows 3, Grounding 4, AI UX 4, Vibe Coding 4); prev/next links
      correct; series names consistent between landing page and article headers.
- [ ] Landing page Latest strip is current and links resolve.
- [ ] Open PR for Phase 1.

## Phase 2 — Editorial + interaction quality (branch: `audit/editorial`)

- [ ] Per-article editorial review, all 29 articles (parallel sub-agents OK, one
      per article, shared rubric): factual accuracy (model names, prices, context
      sizes — flag stale claims), tone consistency (humor 2.5–3/5, confident
      conversational), epigraph present and correct format (4-bar verse), callout
      types used correctly (--insight/--analogy/--pm-tip/--summary), repeated
      analogies across articles. Fix clear errors; log judgment calls to
      Deferred instead of rewriting.
- [ ] Widget UX pass on every interactive widget: obvious affordance, works with
      touch (no hover-only interactions), keyboard-operable, honors
      prefers-reduced-motion. Fix mechanical gaps; log design-level issues.
- [ ] Open PR for Phase 2.

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
