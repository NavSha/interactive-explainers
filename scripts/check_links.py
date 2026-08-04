#!/usr/bin/env python3
"""Pre-launch link/asset checker: verifies every internal href/src/srcset in site
HTML files resolves to a real file, and that #fragment targets exist as element
ids in the destination page. External (http/mailto) links are skipped."""
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
SRCSET_RE = re.compile(r"""srcset\s*=\s*["']([^"']+)["']""", re.I)
ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)

_id_cache = {}


def ids_for(path):
    """Set of element ids declared in an HTML file (cached)."""
    if path not in _id_cache:
        try:
            with open(path, encoding="utf-8") as fh:
                _id_cache[path] = set(ID_RE.findall(fh.read()))
        except OSError:
            _id_cache[path] = set()
    return _id_cache[path]


errors = []
for hf in sorted(html_files):
    rel_hf = os.path.relpath(hf, ROOT)
    with open(hf, encoding="utf-8") as fh:
        content = fh.read()

    candidates = [(m.group(1).strip(), "link") for m in ATTR_RE.finditer(content)]
    for m in SRCSET_RE.finditer(content):
        for part in m.group(1).split(","):
            url = part.strip().split()[0] if part.strip() else ""
            if url:
                candidates.append((url, "srcset"))

    for url, kind in candidates:
        if not url or url.startswith(("http://", "https://", "mailto:", "data:", "javascript:", "//")):
            continue
        parsed = urlparse(url)
        path = unquote(parsed.path)
        fragment = unquote(parsed.fragment)

        if not path:
            # same-page fragment link (#foo) — check against this file's ids
            if fragment and fragment not in ids_for(hf):
                errors.append((rel_hf, url, "missing fragment target"))
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
            elif fragment and fragment not in ids_for(target_index):
                errors.append((rel_hf, url, "missing fragment target"))
            continue
        if not os.path.isfile(target):
            errors.append((rel_hf, url, "missing file"))
            continue
        if fragment and target.endswith(".html") and fragment not in ids_for(target):
            errors.append((rel_hf, url, "missing fragment target"))

if errors:
    for src, url, why in errors:
        print(f"BROKEN  {src}  ->  {url}  ({why})")
    print(f"\n{len(errors)} broken reference(s) in {len(html_files)} HTML files")
    sys.exit(1)
print(f"OK: all internal references and fragments resolve ({len(html_files)} HTML files checked)")
