# scripts/

Maintenance scripts for the wiki planning layer.

## `lint.py`

Scans all article HTMLs + `wiki/maps/*.md` and writes `wiki/LINT.md`.

```bash
python3 scripts/lint.py              # write wiki/LINT.md
python3 scripts/lint.py --dry-run    # print to stdout, don't write
```

No third-party deps. Python 3.9+.

### What it checks

- **A. Topic balance** — reads `parts_live` / `parts_planned` from each map's
  frontmatter.
- **B. Orphan concepts** — watchlist terms appearing in 2+ articles with no
  matching `themes/<slug>.md` or `entities/<slug>.md`.
- **C. Broken cross-references** — `<a href>` between articles that 404.
- **D. Stale articles** — > 180 days since the last git commit touched the file.
- **E. Cross-topic overlap** — watchlist terms appearing in 2+ topics
  (bridge candidates).

### Extending the watchlist

Edit the `WATCHLIST` list in `lint.py`. Each entry is
`(canonical_term, [aliases], category)`. Add terms as the site grows.

A concept with a theme/entity page at `wiki/themes/<slug>.md` or
`wiki/entities/<slug>.md` stops appearing as an orphan — the page's filename
stem is the slug (`slugify` is `lowercase, non-alnum → -`).
