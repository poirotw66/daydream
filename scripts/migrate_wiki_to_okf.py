#!/usr/bin/env python3
"""One-off migration: wiki links and frontmatter toward OKF v0.1."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

TYPE_MAP = {
    "concept": "Concept",
    "entity": "Entity",
    "source": "Source",
    "query": "Query",
    "lint": "Lint Report",
}

SKIP = {"index.md", "log.md", "README.md"}


def wiki_links_to_okf(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        display = match.group(2).strip() if match.group(2) else target.split("/")[-1]
        if target == "index":
            return f"[{display}](/index.md)"
        path = target if target.startswith("/") else f"/{target}"
        if not path.endswith(".md"):
            path = f"{path}.md"
        return f"[{display}]({path})"

    return re.sub(r"\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]", repl, text)


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content
    block = content[4:end]
    body = content[end + 5 :]
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def extract_description(body: str, title: str) -> str:
    for heading in ("## Summary", "# Summary"):
        idx = body.find(heading)
        if idx == -1:
            continue
        rest = body[idx + len(heading) :].lstrip("\n")
        line = rest.split("\n", 1)[0].strip()
        if line.startswith("- "):
            line = line[2:].strip()
        line = re.sub(r"（(?:確定|推測|未知)）", "", line)
        line = re.sub(r"\[\[[^\]]+\]\]", "", line)
        line = re.sub(r"\[[^\]]+\]\([^)]+\)", "", line)
        line = line.strip()
        if line:
            return line[:240]
    return title


def to_timestamp(updated: str) -> str:
    if "T" in updated:
        return updated
    return f"{updated}T00:00:00Z"


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    if not meta:
        return False

    raw_type = meta.get("type", "Concept")
    okf_type = TYPE_MAP.get(raw_type.lower(), raw_type)
    if path.parts[-3:-1] == ("projects", "ideas") and raw_type.lower() == "query":
        okf_type = "Project Idea"

    title = meta.get("title", path.stem)
    updated = meta.get("updated", meta.get("timestamp", "2026-06-03")[:10])
    timestamp = to_timestamp(updated)
    description = meta.get("description") or extract_description(body, title)
    description = description.replace('"', "'")

    tags = meta.get("tags", "[]")
    status = meta.get("status", "active")
    source_count = meta.get("source_count", "0")

    body = wiki_links_to_okf(body)

    new_fm = f"""---
type: {okf_type}
title: "{title}"
description: "{description}"
tags: {tags}
timestamp: {timestamp}
status: {status}
source_count: {source_count}
---
"""
    path.write_text(new_fm + body, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(WIKI.rglob("*.md")):
        if path.name in SKIP:
            continue
        if migrate_file(path):
            changed += 1
    print(f"Migrated {changed} concept files under {WIKI}")


if __name__ == "__main__":
    main()
