#!/usr/bin/env python3
"""Pre-launch link/asset checker: verifies every internal href/src in site HTML
files resolves to a real file. External (http/mailto/#) links are skipped."""
import os
import re
import sys
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = {".git", ".claude", "wiki", "node_modules", ".impeccable"}

html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for f in filenames:
        if f.endswith(".html"):
            html_files.append(os.path.join(dirpath, f))

ATTR_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)

errors = []
for hf in sorted(html_files):
    rel_hf = os.path.relpath(hf, ROOT)
    with open(hf, encoding="utf-8") as fh:
        content = fh.read()
    for m in ATTR_RE.finditer(content):
        url = m.group(1).strip()
        if not url or url.startswith(("http://", "https://", "mailto:", "#", "data:", "javascript:", "//")):
            continue
        path = unquote(urlparse(url).path)
        if not path:  # pure query/fragment link
            continue
        if path.startswith("/interactive-explainers/") or path == "/interactive-explainers":
            # site-absolute GitHub Pages path (used by 404.html) — maps to repo root
            sub = path[len("/interactive-explainers/"):]
            target = os.path.join(ROOT, sub) if sub else os.path.join(ROOT, "index.html")
        elif path.startswith("/"):
            target = os.path.join(ROOT, path.lstrip("/"))
        else:
            target = os.path.normpath(os.path.join(os.path.dirname(hf), path))
        if os.path.isdir(target):
            target_index = os.path.join(target, "index.html")
            if not os.path.isfile(target_index):
                errors.append((rel_hf, url, "directory without index.html"))
            continue
        if not os.path.isfile(target):
            errors.append((rel_hf, url, "missing file"))

if errors:
    for src, url, why in errors:
        print(f"BROKEN  {src}  ->  {url}  ({why})")
    print(f"\n{len(errors)} broken reference(s) in {len(html_files)} HTML files")
    sys.exit(1)
print(f"OK: all internal references resolve ({len(html_files)} HTML files checked)")
