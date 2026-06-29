# Operations Prompts (Copy-Paste)

Canonical English prompts for Ingest / Query / Lint / Graph agents. **FAQ is deprecated** in this bundle—use **Query** (persist reusable Q&A under `wiki/queries/`). See `AGENTS.md`.

Logging: every run of an operation defined in `AGENTS.md` must append `wiki/log.md` (use **pass** or **no-op** when no files changed). Update `wiki/index.md` when the operation changes **hub content** (Side ideas, axes, decision shortcuts) or **`mkdocs.yml` nav** when concepts/entities are added or removed.

---

## Ingest Prompt

Use this repository as a source-grounded wiki system. The `wiki/` directory is an **OKF v0.1** Knowledge Bundle (see `AGENTS.md` → OKF Alignment).

Follow `AGENTS.md` strictly:
1. Read the specified source file.
2. Archive it into `raw/sources/*.md` (new file only; do not modify existing files under `raw/`).
3. Create or update `wiki/sources/*` as OKF concepts (`type: Source`) using the **Source Page Schema** headings. Scaffold: `docs/templates/page-template-source.md`.
4. Extract and update related concepts under `wiki/concepts/*`, `wiki/entities/*`, etc. Use OKF `type` values and bundle-relative links (`/concepts/foo.md`).
5. Add cross-links; end with `# Citations` where applicable.
6. Update **`mkdocs.yml` nav`** for new/changed concepts and entities. Update **`wiki/index.md`** only when Side ideas or hub axes change (this repo’s index is an **idea hub**, not a full OKF bullet catalog).
7. Append `wiki/log.md` (OKF log format preferred).
8. Mark uncertainty explicitly when needed and cite sources for all claims.

---

## Query Prompt

Answer the user question using a traceable, source-grounded workflow.

Follow this order:
1. Read `wiki/index.md` (idea hub), then check `wiki/queries/`, `wiki/concepts/`, `wiki/entities/`, and `wiki/projects/ideas/` as needed.
2. If summary information is sufficient and non-conflicting, answer directly.
3. If summary information is insufficient, ambiguous, or conflicting, verify with `raw/sources/*`.
4. Final answers must include traceable locations (at minimum file paths; include section/line anchors when needed).
5. Cite sources and mark uncertainty (`（確定）`, `（推測）`, `（未知）`) when applicable.
6. If the answer is reusable for future-you, persist under `wiki/queries/` (see **Query Persist Prompt** below), update `mkdocs.yml` nav if needed, and append `wiki/log.md`.

---

## Lint Prompt

Run a wiki quality lint pass and report findings with evidence.

Follow `AGENTS.md` Operation: Lint.

Check for:
- contradictions
- stale information
- orphan pages
- missing pages
- duplicate concepts
- pages without sources
- outdated pages

Output results to `wiki/lint/` and include actionable fixes with file-level references. When you add or materially change persisted lint artifacts under `wiki/lint/`, update `wiki/index.md` only if the hub should surface them (e.g. link a lint summary).

**Always** append `wiki/log.md` for this run (even if no new lint files were written): one line summary, e.g. `pass` or `no issues` or short findings.

---

## Query Persist Prompt

Turn a reusable answer into a persisted `wiki/queries/*` page (replaces the deprecated FAQ workflow).

Follow `AGENTS.md` Operation: Query (steps 6–7).

1. Read `wiki/index.md` and scan sources, concepts, entities, and existing queries.
2. Confirm the question is grounded in the wiki (do not invent topics with no basis in corpus).
3. Create or update a page under `wiki/queries/` with OKF frontmatter (`type: Query`, `title`, `description`, `tags`, `timestamp`, etc.). Scaffold: `docs/templates/page-template-concept.md`.
4. Structure: question scope, synthesized answer, citations (`# Citations`), links to related concepts/entities/sources.
5. Add the page to **`mkdocs.yml` nav** (Queries section). Add a **decision shortcut** link on `wiki/index.md` only if it is a primary recurring decision path.
6. Append `wiki/log.md`.

---

## FAQ Prompt (deprecated)

> **Do not use** for this bundle. `wiki/faq/` is not used; persist reusable Q&A with **Query Persist Prompt** above.

Legacy reference only (if owner explicitly requests restoring `wiki/faq/`):

1. Read `wiki/index.md`.
2. Scan sources, concepts, entities, and queries pages.
3. Detect repeated patterns, confusing topics, workflows, and cross-page relationships.
4. Produce 8–15 questions (beginner through advanced, including at least one cross-page synthesis question). Do not invent questions with no basis in the wiki.
5. ~~Persist under `wiki/faq/`~~ → use `wiki/queries/` instead.
6. Update `mkdocs.yml` nav and `wiki/index.md` decision shortcuts as appropriate.
7. Append `wiki/log.md`.

---

## Graph Prompt

Build or refresh knowledge relationships for this wiki.

Follow `AGENTS.md` Operation: Graph.

1. Traverse wiki pages (respect link and relationship rules in `AGENTS.md`).
2. Extract links and infer relationships where appropriate.
3. Generate or update a graph summary (optional artifact example: `wiki/graph/knowledge-map.md`).
4. If you add or materially change persisted graph artifacts, update `wiki/index.md` or `mkdocs.yml` nav to link them only when they should be discoverable from the hub or site nav.
5. **Always** append `wiki/log.md` for this run — including when output is optional or **unchanged** (record `pass`, `no-op`, or one-line summary per `AGENTS.md`).

---

## Wiki log append (pass / no-op)

Use after any `AGENTS.md` operation when file edits were unnecessary but a trace is still required (e.g. Lint/Graph pass with no new artifacts).

1. Append a new dated section to `wiki/log.md` using the format: `## [YYYY-MM-DD] <operation> | <title>`.
2. One or two bullets: state **pass**, **no-op**, or brief outcome; name the operation (lint / graph / query persist / ingest / etc.).
3. Do not rewrite or delete prior log sections.
