#!/usr/bin/env python3
"""Pre-launch inline-script checker: extracts every inline <script> block from
site HTML files and syntax-checks it with `node --check`. A parse error in an
inline block silently kills every widget defined in it."""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = {".git", ".claude", "wiki", "node_modules", ".impeccable"}

html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for f in filenames:
        if f.endswith(".html"):
            html_files.append(os.path.join(dirpath, f))

SCRIPT_RE = re.compile(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", re.S | re.I)

failures = []
for hf in sorted(html_files):
    rel = os.path.relpath(hf, ROOT)
    with open(hf, encoding="utf-8") as fh:
        content = fh.read()
    for i, m in enumerate(SCRIPT_RE.finditer(content)):
        body = m.group(1)
        if not body.strip():
            continue
        line_offset = content[: m.start(1)].count("\n") + 1
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(body)
            tmp = tf.name
        try:
            r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            if r.returncode != 0:
                err = r.stderr.strip().splitlines()
                msg = next((l for l in err if "Error" in l), err[0] if err else "?")
                bad_line = "?"
                mline = re.search(r"\.js:(\d+)", r.stderr)
                if mline:
                    bad_line = str(int(mline.group(1)) + line_offset - 1)
                failures.append((rel, f"block {i+1}", f"HTML line ~{bad_line}", msg))
        finally:
            os.unlink(tmp)

if failures:
    for rel, blk, line, msg in failures:
        print(f"SYNTAX FAIL  {rel}  {blk}  {line}  {msg}")
    print(f"\n{len(failures)} failing script block(s) across {len(html_files)} files")
    sys.exit(1)
print(f"OK: all inline script blocks parse ({len(html_files)} HTML files checked)")
