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
<div class="dd-hero dd-hero--hub" markdown>

# 點子集散中心

<p class="dd-hero__subtitle">Side 發想、實驗與輸出的起點 — 先看清「現在在追什麼點子」，再進各頁細節。</p>

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
