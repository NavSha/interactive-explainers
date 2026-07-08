#!/usr/bin/env python3
"""Inject favicon links + OG/Twitter/description meta tags into every site HTML
page. Idempotent: skips tags a page already has. Descriptions come from the
page's .lead paragraph (fallback: first prose <p>)."""
import os
import re
import html as htmllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://navsha.github.io/interactive-explainers/"
EXCLUDE_DIRS = {".git", ".claude", "wiki", "node_modules", ".impeccable", "assets", "scripts"}

pages = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for f in filenames:
        if f.endswith(".html"):
            pages.append(os.path.join(dirpath, f))

TAG_RE = re.compile(r"<(?:p|div)[^>]*class=\"[^\"]*lead[^\"]*\"[^>]*>(.*?)</(?:p|div)>", re.S)
P_RE = re.compile(r"<article[^>]*>.*?<p[^>]*>(.*?)</p>", re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

def clean(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = htmllib.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 160:
        text = text[:157].rsplit(" ", 1)[0] + "…"
    return text

changed = 0
for path in sorted(pages):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    depth = rel.count("/")
    prefix = "../" * depth
    url = BASE_URL + ("" if rel == "index.html" else rel)

    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    m = TITLE_RE.search(content)
    title = htmllib.unescape(m.group(1).strip()) if m else "AI for Builders"
    m = TAG_RE.search(content) or P_RE.search(content)
    desc = clean(m.group(1)) if m else "Interactive guides to how AI actually works — tokens, agents, evals, context, and the craft of shipping with it."

    def esc(s):
        return htmllib.escape(s, quote=True)

    lines = []
    if 'name="description"' not in content:
        lines.append(f'  <meta name="description" content="{esc(desc)}">')
    if 'property="og:' not in content:
        lines += [
            f'  <meta property="og:type" content="article">' if rel != "index.html" else '  <meta property="og:type" content="website">',
            f'  <meta property="og:title" content="{esc(title)}">',
            f'  <meta property="og:description" content="{esc(desc)}">',
            f'  <meta property="og:url" content="{esc(url)}">',
            f'  <meta property="og:image" content="{BASE_URL}assets/og-image.png">',
            f'  <meta property="og:site_name" content="AI for Builders">',
        ]
    if 'name="twitter:' not in content:
        lines += [
            '  <meta name="twitter:card" content="summary_large_image">',
            f'  <meta name="twitter:title" content="{esc(title)}">',
            f'  <meta name="twitter:description" content="{esc(desc)}">',
            f'  <meta name="twitter:image" content="{BASE_URL}assets/og-image.png">',
        ]
    if 'rel="icon"' not in content:
        lines += [
            f'  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32.png">',
            f'  <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">',
        ]
    if not lines:
        continue

    block = "\n".join(lines) + "\n"
    # insert right after <title>…</title>
    new_content, n = re.subn(r"(</title>\n)", r"\1" + block, content, count=1)
    if n != 1:
        print(f"SKIP (no title anchor): {rel}")
        continue
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    changed += 1
    print(f"OK {rel}  [{desc[:60]}…]" if len(desc) > 60 else f"OK {rel}  [{desc}]")

print(f"\n{changed} page(s) updated")
