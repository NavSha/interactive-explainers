#!/usr/bin/env python3
"""
Lint pass for interactive-explainers wiki.

Scans article HTMLs + wiki maps, writes wiki/LINT.md with:
  A. Topic balance (parts_live vs. parts_planned)
  B. Orphan concepts — watchlist terms in 2+ articles with no theme/entity page
  C. Broken cross-references between articles
  D. Stale articles (> 180 days since last git commit)
  E. Cross-topic concept overlap (bridge candidates)

Usage:
  python3 scripts/lint.py
  python3 scripts/lint.py --dry-run   # print to stdout instead of writing

No third-party deps. Python 3.9+.
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
MAPS = WIKI / "maps"
THEMES = WIKI / "themes"
ENTITIES = WIKI / "entities"

TOPICS = [
    "llm-fundamentals",
    "agents",
    "cost-latency",
    "evaluation",
    "context-windows",
    "grounding",
    "ai-ux",
    "vibe-coding",
]

# Watchlist: (canonical_term, aliases, category).
# Add to this over time. A concept appearing in 2+ articles with no backing
# theme/entity page shows up in Section B as an orphan.
WATCHLIST: list[tuple[str, list[str], str]] = [
    # LLM fundamentals
    ("next-token prediction", ["next token", "next-token"], "llm"),
    ("tokenization", ["tokenize", "tokenizer"], "llm"),
    ("transformer", ["transformers"], "llm"),
    ("attention", ["self-attention"], "llm"),
    ("embedding", ["embeddings"], "llm"),
    ("fine-tuning", ["fine tuning", "finetune"], "llm"),
    ("RLHF", ["reinforcement learning from human feedback"], "llm"),
    ("inference", [], "llm"),
    # Agents
    ("ReAct", ["ReAct pattern"], "agents"),
    ("agent loop", ["agent-loop"], "agents"),
    ("tool use", ["function calling"], "agents"),
    ("MCP", ["Model Context Protocol"], "agents"),
    ("multi-agent", ["multi agent"], "agents"),
    # Cost / latency
    ("prompt caching", ["prompt cache"], "cost"),
    ("batching", [], "cost"),
    ("streaming", ["SSE"], "cost"),
    # Evaluation
    ("LLM-as-judge", ["llm as judge", "model as judge"], "eval"),
    ("golden dataset", ["golden set"], "eval"),
    ("regression testing", ["regression test"], "eval"),
    ("non-determinism", ["non deterministic", "nondeterminism"], "eval"),
    ("red-teaming", ["red team", "red-team"], "eval"),
    # Context windows
    ("context window", ["context-window"], "context"),
    ("lost in the middle", [], "context"),
    ("context engineering", [], "context"),
    ("summarization", ["summarize"], "context"),
    # Grounding
    ("RAG", ["retrieval-augmented generation", "retrieval augmented"], "grounding"),
    ("hybrid search", [], "grounding"),
    ("reranking", ["reranker"], "grounding"),
    ("vector search", ["vector db", "vector database"], "grounding"),
    ("hallucination", ["hallucinations", "confabulation"], "grounding"),
    ("chunking", [], "grounding"),
    ("Graph RAG", ["graph-rag"], "grounding"),
    # AI UX
    ("HITL", ["human-in-the-loop", "human in the loop"], "ux"),
    ("confidence signal", ["confidence signals"], "ux"),
    ("progressive disclosure", [], "ux"),
    ("review queue", ["review queues"], "ux"),
    ("escalation", ["escalate"], "ux"),
    # Vibe coding
    ("Claude Code", [], "vibe"),
    ("Cursor", [], "vibe"),
    ("Replit", [], "vibe"),
    ("Lovable", [], "vibe"),
    ("vibe coding", ["vibe-coding"], "vibe"),
    # Cross-cutting
    ("prompt injection", [], "cross"),
    ("tradeoff", ["trade-off", "tradeoffs"], "cross"),
]


class ArticleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self.hrefs: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.hrefs.append(v)

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip == 0:
            self._parts.append(data)

    def text(self) -> str:
        return " ".join(self._parts)


def load_articles():
    """Yield (topic, rel_path, text, hrefs) for each article HTML (skips index.html)."""
    for topic in TOPICS:
        topic_dir = ROOT / topic
        if not topic_dir.is_dir():
            continue
        for html in sorted(topic_dir.glob("*.html")):
            if html.name == "index.html":
                continue
            p = ArticleParser()
            p.feed(html.read_text(encoding="utf-8"))
            yield topic, html.relative_to(ROOT), p.text(), p.hrefs


def count_term(text: str, term: str, aliases: list[str]) -> int:
    t = text.lower()
    total = 0
    for variant in (term, *aliases):
        pat = r"\b" + re.escape(variant.lower()) + r"\b"
        total += len(re.findall(pat, t))
    return total


def parse_frontmatter(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end < 0:
        return {}
    out: dict[str, str] = {}
    for line in content[3:end].splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


def covered_slugs() -> set[str]:
    """Slugs of existing theme and entity pages (content pages, not READMEs)."""
    out: set[str] = set()
    for d in (THEMES, ENTITIES):
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            if p.name.lower() == "readme.md":
                continue
            out.add(p.stem.lower())
    return out


def git_last_modified(rel_path: Path) -> datetime | None:
    try:
        res = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(rel_path)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        s = res.stdout.strip()
        if not s:
            return None
        # %cI is strict ISO 8601 — but strip TZ for naive datetime compare
        return datetime.fromisoformat(s).replace(tzinfo=None)
    except Exception:
        return None


def slugify(term: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
    return s


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv

    articles = list(load_articles())
    covered = covered_slugs()

    # Concept mention counts.
    topic_mentions: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    article_mentions: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for topic, rel, text, _ in articles:
        for term, aliases, _cat in WATCHLIST:
            n = count_term(text, term, aliases)
            if n:
                topic_mentions[term][topic] += n
                article_mentions[term][str(rel)] += n

    # A. Topic balance.
    balance = []
    for slug in TOPICS:
        fm = parse_frontmatter(MAPS / f"{slug}.md")
        balance.append((slug, fm.get("parts_live", "?"), fm.get("parts_planned", "?")))

    # B. Orphan concepts: >=2 articles, >=3 mentions, no theme/entity page.
    orphans = []
    for term, aliases, category in WATCHLIST:
        if slugify(term) in covered:
            continue
        total = sum(topic_mentions[term].values())
        article_count = sum(1 for c in article_mentions[term].values() if c > 0)
        if article_count >= 2 and total >= 3:
            orphans.append((term, category, article_count, total, sorted(topic_mentions[term].keys())))
    orphans.sort(key=lambda x: (-x[2], -x[3]))

    # C. Broken internal cross-refs.
    broken = []
    for _topic, rel, _text, hrefs in articles:
        article_path = ROOT / rel
        for href in hrefs:
            if href.startswith(("http://", "https://", "mailto:", "#", "javascript:")):
                continue
            h = href.split("#", 1)[0].split("?", 1)[0]
            if not h:
                continue
            target = (article_path.parent / h).resolve()
            if not target.exists():
                broken.append((str(rel), href))

    # D. Stale articles.
    stale = []
    now = datetime.now()
    for _topic, rel, _text, _hrefs in articles:
        mtime = git_last_modified(rel)
        if mtime and (now - mtime).days > 180:
            stale.append((str(rel), mtime.date().isoformat(), (now - mtime).days))
    stale.sort(key=lambda x: -x[2])

    # E. Cross-topic overlap — bridge candidates.
    overlaps = []
    for term, _aliases, _cat in WATCHLIST:
        topics_hit = [t for t, c in topic_mentions[term].items() if c > 0]
        if len(topics_hit) >= 2:
            overlaps.append((term, sorted(topics_hit), sum(topic_mentions[term].values())))
    overlaps.sort(key=lambda x: (-len(x[1]), -x[2]))

    today = datetime.now().date().isoformat()
    out: list[str] = []
    out.append("---")
    out.append("type: lint")
    out.append(f"generated: {today}")
    out.append(f"corpus_size: {len(articles)} articles")
    out.append(f"domains: {len(TOPICS)}")
    out.append("---")
    out.append("")
    out.append(f"# Lint — {today}")
    out.append("")
    out.append("Generated by `scripts/lint.py`. Re-run after adding articles,")
    out.append("theme/entity pages, or watchlist concepts.")
    out.append("")

    out.append("## A. Topic balance")
    out.append("")
    out.append("| Domain | parts_live | parts_planned |")
    out.append("|---|---|---|")
    for slug, live, planned in balance:
        out.append(f"| `{slug}` | {live} | {planned} |")
    out.append("")

    out.append("## B. Orphan concepts")
    out.append("")
    out.append("Watchlist terms appearing in 2+ articles with no `themes/<slug>.md`")
    out.append("or `entities/<slug>.md` backing. Consider promoting to a theme/entity page.")
    out.append("")
    if orphans:
        out.append("| Concept | Category | Articles | Mentions | Topics |")
        out.append("|---|---|---|---|---|")
        for term, cat, ac, total, topics in orphans:
            out.append(f"| **{term}** | {cat} | {ac} | {total} | {', '.join(topics)} |")
    else:
        out.append("*(none)*")
    out.append("")

    out.append("## C. Broken cross-references")
    out.append("")
    if broken:
        for src, href in broken:
            out.append(f"- `{src}` → `{href}`")
    else:
        out.append("*(none — all internal links resolve)*")
    out.append("")

    out.append("## D. Stale articles (> 180 days since last git commit)")
    out.append("")
    if stale:
        for path, date, days in stale:
            out.append(f"- `{path}` — last touched {date} ({days}d ago)")
    else:
        out.append("*(none)*")
    out.append("")

    out.append("## E. Cross-topic concept overlap (bridge candidates)")
    out.append("")
    out.append("Watchlist terms appearing across 2+ topics. If a given concept")
    out.append("isn't named in the bridges section of either topic's map, add it.")
    out.append("")
    if overlaps:
        out.append("| Concept | Topics | Total mentions |")
        out.append("|---|---|---|")
        for term, topics, total in overlaps[:30]:
            out.append(f"| {term} | {', '.join(topics)} | {total} |")
    else:
        out.append("*(none)*")
    out.append("")

    rendered = "\n".join(out) + "\n"

    if dry_run:
        sys.stdout.write(rendered)
    else:
        (WIKI / "LINT.md").write_text(rendered, encoding="utf-8")
        print(f"Wrote {WIKI / 'LINT.md'}")
        print(f"  articles scanned: {len(articles)}")
        print(f"  orphan concepts: {len(orphans)}")
        print(f"  broken cross-refs: {len(broken)}")
        print(f"  stale articles: {len(stale)}")
        print(f"  bridge candidates: {len(overlaps)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
