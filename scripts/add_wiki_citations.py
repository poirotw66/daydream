#!/usr/bin/env python3
"""Add # Citations sections and refresh stale timestamps."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
SKIP = {"index.md", "log.md", "README.md"}
REFRESH_TS = "2026-06-25T12:00:00Z"
STALE_PREFIXES = ("2026-05-15",)

SOURCE_TO_RAW: dict[str, list[str]] = {
    "/sources/2026-05-15-個人雙軌構思.md": ["raw/sources/2026-05-15-個人雙軌構思.md"],
    "/sources/2026-05-15-ai-cup-參賽筆記.md": ["raw/sources/2026-05-15-ai-cup-參賽筆記.md"],
    "/sources/2026-ai-cup-桌球戰術-baseline.md": [
        "raw/sources/2026-ai-cup-桌球戰術-baseline-method.pdf",
        "raw/sources/2026-ai-cup-桌球戰術-baseline-文稿.md",
    ],
    "/sources/2026-06-03-recipe-bloss0m-內容農場.md": ["raw/sources/2026-06-03-recipe-bloss0m-內容農場.md"],
    "/sources/2026-06-03-年底轉職與時間配置.md": ["raw/sources/2026-06-03-年底轉職與時間配置.md"],
}


def parse_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        return "", text, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text, text
    return text[: end + 5], text[4:end], text[end + 5 :]


def collect_source_links(body: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    patterns = [
        r"\[([^\]]*)\]\((/sources/[^)]+\.md)\)",
        r"grounded_in:\s*\[([^\]]*)\]\((/sources/[^)]+\.md)\)",
    ]
    for pattern in patterns:
        for label, link in re.findall(pattern, body):
            if link not in seen:
                seen.add(link)
                label = label.strip() or link.split("/")[-1].removesuffix(".md")
                found.append((label, link))
    return found


def build_citations(links: list[tuple[str, str]], is_source: bool, self_link: str | None) -> str:
    lines = ["\n# Citations\n"]
    n = 0
    if is_source and self_link:
        for raw_path in SOURCE_TO_RAW.get(self_link, []):
            n += 1
            lines.append(f"[{n}] `{raw_path}`（immutable archive）")
    for _label, link in links:
        if is_source and link == self_link:
            continue
        n += 1
        raw_note = ""
        raw_paths = SOURCE_TO_RAW.get(link, [])
        if raw_paths:
            raw_note = " — " + ", ".join(f"`{p}`" for p in raw_paths)
        display = _label if not _label.startswith("/") else link.split("/")[-1].removesuffix(".md")
        lines.append(f"[{n}] [{display}]({link}){raw_note}")
    if n == 0:
        lines.append("\n（尚無外部引用）")
    return "\n".join(lines) + "\n"


def refresh_timestamp(fm: str) -> str:
    if not re.search(rf"^timestamp:\s*{STALE_PREFIXES[0]}", fm, re.M):
        return fm
    return re.sub(r"^timestamp:.*$", f"timestamp: {REFRESH_TS}", fm, count=1, flags=re.M)


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    head, fm, body = parse_frontmatter(text)
    if not head:
        return False

    rel = "/" + str(path.relative_to(WIKI)).replace("\\", "/")
    is_source = "/sources/" in rel
    self_link = rel if is_source else None

    if "# Citations" in body:
        body_changed = False
    else:
        links = collect_source_links(body)
        body = body.rstrip() + build_citations(links, is_source, self_link)
        body_changed = True

    new_fm = refresh_timestamp(fm)
    ts_changed = new_fm != fm
    if not body_changed and not ts_changed:
        return False

    path.write_text(f"---\n{new_fm}\n---{body}", encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(WIKI.rglob("*.md")):
        if path.name in SKIP or "lint" in path.parts:
            continue
        if process(path):
            changed += 1
            print(path.relative_to(WIKI))
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
