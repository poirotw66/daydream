"""MkDocs hooks: OKF frontmatter strip + link rewrites for GitHub Pages."""

from __future__ import annotations

import html
import os
import re
from pathlib import PurePosixPath

REPO = "https://github.com/poirotw66/daydream/blob/main"

_BUNDLE_PREFIXES = ("concepts", "entities", "sources", "queries", "projects", "lint")

_INTERNAL_LINK = re.compile(
    r"\]\((?P<path>/?(?:"
    + "|".join(_BUNDLE_PREFIXES)
    + r")/[^)\s#]+\.md)(?P<anchor>#[^)]*)?\)"
)

_TYPE_CLASS = {
    "Concept": "concept",
    "Entity": "entity",
    "Source": "source",
    "Query": "query",
    "Playbook": "playbook",
    "Project Idea": "project-idea",
    "Lint Report": "lint-report",
}


def _strip_frontmatter(markdown: str) -> str:
    if not markdown.startswith("---\n"):
        return markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return markdown
    return markdown[end + 5 :]


def _relative_wiki_link(target: str, page_uri: str) -> str:
    """OKF bundle path → MkDocs-relative path from the current page."""
    normalized = target.lstrip("/")
    page_dir = str(PurePosixPath(page_uri).parent)
    if page_dir == ".":
        return normalized
    rel = os.path.relpath(normalized, page_dir)
    return rel.replace("\\", "/")


def _rewrite_links(markdown: str, page_uri: str) -> str:
    def repl(match: re.Match[str]) -> str:
        rel = _relative_wiki_link(match.group("path"), page_uri)
        anchor = match.group("anchor") or ""
        return f"]({rel}{anchor})"

    markdown = _INTERNAL_LINK.sub(repl, markdown)

    for name in ("index.md", "wiki-guide.md"):
        markdown = re.sub(
            rf"\]\(/?{re.escape(name)}\)",
            lambda _m, n=name: f"]({_relative_wiki_link(n, page_uri)})",
            markdown,
        )

    markdown = markdown.replace("](../AGENTS.md)", f"]({REPO}/AGENTS.md)")
    markdown = markdown.replace("](../../AGENTS.md)", f"]({REPO}/AGENTS.md)")
    markdown = markdown.replace("](../docs/OPERATIONS.md)", f"]({REPO}/docs/OPERATIONS.md)")
    markdown = markdown.replace("](../../docs/OPERATIONS.md)", f"]({REPO}/docs/OPERATIONS.md)")
    markdown = re.sub(
        r"\]\(\.\./(?:\.\./)?(\.github/[^)]+)\)",
        lambda m: f"]({REPO}/{m.group(1)})",
        markdown,
    )

    return markdown


def _type_slug(okf_type: str) -> str:
    return _TYPE_CLASS.get(okf_type, okf_type.lower().replace(" ", "-"))


def _page_header(meta: dict) -> str:
    okf_type = meta.get("type")
    if not okf_type:
        return ""

    slug = _type_slug(str(okf_type))
    parts = [f'<span class="okf-type okf-type--{slug}">{html.escape(str(okf_type))}</span>']

    status = meta.get("status")
    if status:
        parts.append(f'<span class="okf-status">{html.escape(str(status))}</span>')

    header = f'<div class="dd-page-meta">{"".join(parts)}</div>\n\n'

    description = meta.get("description")
    if description:
        header += f'<p class="okf-description">{html.escape(str(description))}</p>\n\n'

    return header


def _index_hero() -> str:
    return """
<div class="dd-hero" markdown>

# daydream Wiki

<p class="dd-hero__subtitle">Agent 職涯 — 場內案子、Kaggle 實驗、金融 Agent 發想、每日技術 blog。</p>

<div class="grid cards" markdown>

- :material-briefcase-account:{ .lg .middle } **年底轉職**

    ---

    AI agent 開發／應用

    [:octicons-arrow-right-24: 進入](/concepts/年底轉職-agent-準備.md)

- :material-domain:{ .lg .middle } **場內案子**

    ---

    國泰 · 企業級 Agent

    [:octicons-arrow-right-24: 進入](/concepts/現職場內-agent-案子.md)

- :material-chart-timeline-variant:{ .lg .middle } **Kaggle 實驗**

    ---

    ml-intern × autoresearch

    [:octicons-arrow-right-24: 進入](/concepts/ml-intern-autoresearch-路線.md)

- :material-newspaper-variant-outline:{ .lg .middle } **每日輸出**

    ---

    技術前沿 blog · 資訊 agent

    [:octicons-arrow-right-24: 進入](/concepts/每日技術前沿-blog.md)

</div>

</div>

"""


def on_page_markdown(markdown: str, page, config, files) -> str:
    meta = dict(getattr(page, "meta", {}) or {})
    page_uri = page.file.src_uri

    markdown = _strip_frontmatter(markdown)

    if page_uri == "index.md":
        markdown = _index_hero() + markdown

    header = _page_header(meta)
    if header and page_uri != "index.md":
        markdown = header + markdown

    return _rewrite_links(markdown, page_uri)
