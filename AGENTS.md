# 📘 Personal LLM Wiki Schema

You help the **repository owner** maintain this wiki. Treat the repo as a **personal, persistent, graph-aware, source-grounded** knowledge system—a second brain for learning, projects, and creative work—not a corporate or team handbook.

---

# 🎯 System Goal

Build a **self-evolving personal knowledge base** that:

* Minimizes hallucination when you revisit topics months later
* Maximizes traceability (what you read, concluded, and when)
* Maintains structured relationships (graph) across interests and projects
* Supports **future-you**: quick recall, reusable notes, FAQ for yourself, RAG / agents on your own corpus

Typical personal use (non-exhaustive): research synthesis, tool notes, project runbooks, creative pipelines (e.g. content or product workflows), and cross-linking ideas across domains.

---

# 🧠 Core Principles

* Source-grounded > Speculation
* Structure > Volume
* Links > Isolation
* Evolution > Perfection
* **Personal relevance > generic completeness** (capture what matters to the owner, not “everything an org might need”)

---

# 📦 OKF Alignment (v0.1)

`wiki/` is an [**Open Knowledge Format (OKF)** v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) **Knowledge Bundle**—a directory of markdown concepts with YAML frontmatter, cross-linked for humans and agents. Spec: [okf/SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

| OKF term | This repo |
|----------|-----------|
| Knowledge Bundle | `wiki/` |
| Concept | Any `wiki/**/*.md` except reserved `index.md`, `log.md` |
| Concept ID | Path under `wiki/` without `.md` (e.g. `concepts/雙軌個人架構`) |
| Citation | `# Citations` section + links to `raw/` or `/sources/*.md` |
| Bundle extensions | `raw/` (immutable provenance), `docs/` (templates, ops)—**not** part of the OKF bundle |

**Conformance (required):** every concept file has parseable YAML frontmatter with non-empty `type`. **Recommended OKF keys:** `title`, `description`, `tags`, `timestamp` (ISO 8601). **Personal extensions** (allowed by OKF §4.1): `status`, `source_count`, `resource` (canonical URI when applicable).

### `type` values (this bundle)

| `type` | Directory | Meaning |
|--------|-----------|---------|
| `Concept` | `concepts/` | Abstract ideas, frameworks, workflows |
| `Entity` | `entities/` | Tools, products, platforms, roles |
| `Source` | `sources/` | Ingested readings, exports, transcripts |
| `Query` | `queries/` | Reusable Q&A |
| `Playbook` | `faq/` | FAQ / how-I-do-X checklists |
| `Project Idea` | `projects/ideas/` | Side-project candidates |
| `Lint Report` | `lint/` | Wiki health diagnostics |

Use descriptive `type` strings OKF-style when none of the above fit (e.g. `Reference`); consumers MUST tolerate unknown types.

---

# 📁 Directory Contract

* `raw/`: immutable **existing** sources (❗ do not edit in place). **New** files may be **archived** into `raw/sources/` as step 2 of Ingest. **Outside** the OKF bundle; cited from concept `# Citations`.

* `wiki/`: OKF **Knowledge Bundle** + personal extensions (`lint/`, `graph/`, `projects/`)

* `wiki/index.md`: bundle-root catalog ([OKF §6](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#6-index-files)); **only** place that MAY declare `okf_version` in frontmatter

* `wiki/log.md`: optional bundle update log ([OKF §7](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#7-log-files-optional))

* `wiki/sources/`: parsed knowledge from **your** readings, clips, exports, transcripts

* `wiki/concepts/`: abstract ideas you care about (e.g. RAG, worldbuilding, pricing)

* `wiki/entities/`: concrete tools, products, stacks, or domains you use (e.g. NotebookLM, LINE Creators Market, a specific framework)

* `wiki/queries/`: reusable Q&A you asked once and want again

* `wiki/faq/`: FAQ **for yourself** (recurring confusion, checklists, “how I do X”)

* `wiki/lint/`: diagnostics on your wiki’s health

* `wiki/graph/`: relationship mappings (optional advanced)

* `docs/` (**supporting files**, not part of the wiki knowledge corpus):

  * `docs/templates/page-template.md` — index of templates; choose **page-template-source.md** for `wiki/sources/*` or **page-template-concept.md** for other wiki types. MUST still match **Required Frontmatter** below and, for `wiki/sources/*`, the **Source Page Schema** section headings exactly.

  * `docs/OPERATIONS.md` — canonical **copy-paste English prompts** and numbered procedural checklists for Ingest / Query / Lint / FAQ / Graph agents; maintain prompts here as the single source of truth.

---

# 🧱 Wiki Page Conventions

* Markdown only

* Must include YAML frontmatter on **every concept** (`wiki/**/*.md` except reserved files). `wiki/index.md`: no frontmatter **except** optional `okf_version` (OKF §11)

* Language: **Traditional Chinese**

* English only for technical terms (API, RAG, NotebookLM...)

* Writing style:

  * concise
  * structured
  * verifiable
  * first-person or neutral “筆記” tone is fine; avoid corporate boilerplate (“請全體同仁…”, RACI, approval flows) unless the owner explicitly ingests such material

* **檔案與路徑命名**（`wiki/**`、Ingest 新增之 `raw/sources/*.md` 等由本 wiki 決定之檔名）：

  * 使用**繁體中文**或**英文**（含技術詞、既有目錄沿用之 slug，例如 `concepts/api`）。
  * **勿**以**漢語拼音**拼寫中文語意作為檔名或路徑片段：對台灣讀者不直觀，也與本地慣用之書寫系統不一致；應改為繁體字面，或改用具辨識度之英文識別名。
  * 穩定、可記的 slug 優先（未來檢索與連結不會斷）。

---

# 📌 Required Frontmatter (OKF + extensions)

Every concept document:

```yaml
---
type: Concept          # REQUIRED (OKF §4.1) — see type table above
title: "<Display name>"
description: "<One-line summary>"   # recommended; feeds index entries
tags: []
timestamp: 2026-06-03T00:00:00Z   # ISO 8601; last meaningful change
resource: <optional URI>          # when concept binds to an external asset
status: active                    # extension: draft | active | needs-review
source_count: 0                   # extension: ingested source count
---
```

### `wiki/index.md` (bundle root)

```yaml
---
okf_version: "0.1"
---
```

* Body follows **Index Structure** below (OKF §6). No other frontmatter keys on `index.md`.
* Standalone overview pages (e.g. `wiki/overview.md`) are normal concepts with `type: Concept` or `Playbook`.

---

# 🔗 Linking Rules (MANDATORY)

OKF cross-links ([§5](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#5-cross-linking)):

* Use **bundle-relative** paths from `wiki/` root: `[顯示文字](/concepts/雙軌個人架構.md)`
* Relative paths (`./other.md`) are allowed for siblings
* Do **not** use `[[wiki-link]]` syntax in new or updated pages
* Every concept MUST link to ≥1 other concept
* Every new concept MUST appear in `wiki/index.md` (or a subdirectory `index.md` when introduced)
* Relationship kind is conveyed by **prose** around the link, not by link syntax

---

# 🧩 Knowledge Graph Rules

Every page should implicitly or explicitly define relationships:

### Allowed Relationships

* `concept → concept`
* `concept → entity`
* `entity → concept`
* `source → concept/entity`

Optional explicit section (personal convention, not OKF-required):

```md
## Relationships

- related_to: [API](/concepts/api.md)
- implemented_by: [Spring Boot](/entities/spring-boot.md)
```

👉 Consumers may build a graph from all markdown links (OKF §5.3)

---

# 📏 Page Granularity Rules

* One page = one concept / entity
* > 500 words → split
* Do NOT mix abstraction layers (keep “idea” and “how I run my sticker pipeline” on separate pages when possible)

---

# 📌 Citation Rules (CRITICAL)

OKF citations ([§8](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#8-citations)):

* Ground claims in **your** sources (`raw/sources/*`, ingested `/sources/*.md`, or external URLs)
* End each concept with `# Citations` when external or archived material is referenced
* Number citations; inline body may use `[1]` or markdown links

```md
# Citations

[1] [2026-05-15 個人雙軌構思](/sources/2026-05-15-個人雙軌構思.md)
[2] `raw/sources/2026-05-15-個人雙軌構思.md`（immutable archive）
```

* Ingested source concepts SHOULD link to `raw/` path in Citations for traceability

---

# ⚠️ Uncertainty Markers

* （確定）
* （推測）
* （未知）

Use these liberally for personal notes—opinions and half-baked ideas are welcome if labeled.

---

# 📚 Source Page Schema

Each `wiki/sources/*` must include:

```md
## Summary
- 3–5 bullets

## Key Concepts

## Entities

## Notable Claims

## Limitations / Gaps
```

Starter layouts: **`docs/templates/page-template-source.md`** (`wiki/sources/*`); **`docs/templates/page-template-concept.md`** (concept / entity / query / lint). See **`docs/templates/page-template.md`** for the index.

---

# 📑 Index Structure

Canonical catalog: **`wiki/index.md`** with optional `okf_version: "0.1"` frontmatter. OKF index body ([§6](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#6-index-files)):

```md
# Overview

* [AGENTS.md](../AGENTS.md) - bundle rules (OKF + personal extensions)
* …

# Concepts

* [雙軌個人架構](/concepts/雙軌個人架構.md) - one-line description from frontmatter `description`
```

* Use `# Section` headings (OKF style), not `##` under `# Index`, unless you keep a hybrid—**new entries** MUST use `* [title](path) - description` bullets.
* **`description`** in each concept’s frontmatter SHOULD match the index one-liner.
* Optional extra sections: `# Projects`, `# Areas` for multi-track personal scope.
* Subdirectories MAY add their own `index.md` for progressive disclosure.

---

# 🛠 Operation: Ingest

1. Read the **specified** source file (path or artifact provided for this ingest).
2. **Archive** it into `raw/sources/*.md` (new file only; stable name per **owner** convention; follow **檔案與路徑命名** in Wiki Page Conventions). **Do not** overwrite or in-place edit existing files under `raw/` unless explicitly approved.
3. Create/update `wiki/sources/` from that archived file under `raw/sources/`.
4. Extract:

   * concepts
   * entities
5. Update related pages (only those tied to the owner’s current interests—no obligation to “cover the whole domain”)
6. Link everything
7. Update index
8. Append log

---

# ❓ Operation: Query

Answer **for the owner** (study, build, write, decide)—not as an internal support desk.

1. Read index
2. Find relevant pages
3. Synthesize answer
4. Cite sources
5. Mark uncertainty
6. Persist under `wiki/queries/` if reusable for future-you
7. Update index + log when persisting

## Query Resolution Rule (MANDATORY)

1. Check `wiki/` summary pages first (`faq`, `concepts`, `entities`).
2. If summary information is sufficient and non-conflicting, answer directly.
3. If summary information is insufficient, ambiguous, or conflicting, verify with `raw/sources/*`.
4. Final answers MUST include traceable locations (at minimum file paths; include section/line anchors when needed).

---

# 📚 Operation: FAQ

## Purpose

Generate reusable knowledge from **your** existing wiki—patterns you keep re-asking, personal workflows, mental models.

---

## Steps

1. Read `wiki/index.md`
2. Scan:

   * sources
   * concepts
   * entities
   * queries
3. Detect:

   * repeated patterns
   * confusing topics
   * personal workflows
   * cross-page relationships
4. Generate FAQ (basic → advanced)
5. Persist new or updated FAQ pages under `wiki/faq/`
6. Update `wiki/index.md` (FAQ section: each entry = link + one-line description)
7. Append `wiki/log.md`

---

## FAQ Page Format

```yaml
---
type: Playbook
title: "<FAQ title>"
description: "<One-line scope>"
tags: ["faq"]
timestamp: 2026-06-03T00:00:00Z
status: active
source_count: 0
---
```

```md
# <FAQ Title>

## Scope

說明範圍（對「未來的我」）

## FAQ

### 1. 問題

**Short Answer：**  

**Detailed Answer：**  

**Related Pages：**
- [concepts/...](/concepts/....md)
- [sources/...](/sources/....md)
```

---

## FAQ Rules

* 8–15 questions
* Must include:

  * beginner questions (past-you would have wanted)
  * cross-page synthesis question
* No hallucinated questions—only gaps visible in the wiki

---

# 🧪 Operation: Lint

Detect issues that hurt **personal** trust in the wiki:

* contradictions
* stale info
* orphan pages
* missing pages
* duplicate concepts
* no-source pages
* outdated pages (>30 days) — tune threshold if the owner prefers slower-moving reference notes

Output → `wiki/lint/`

When you **add or materially change** persisted lint artifacts under `wiki/lint/`, update `wiki/index.md` if the catalog should surface them (e.g. link a lint summary page).

Append `wiki/log.md` for **every** Lint run (including when no new files were written — record pass / short summary).

---

# 🧠 Operation: Graph

Build knowledge relationships across **your** interests and projects:

1. Traverse all pages
2. Extract links
3. Infer relationships
4. Generate graph summary
5. When you add or materially change persisted graph artifacts, update `wiki/index.md` (e.g. link `wiki/graph/knowledge-map.md` or the chosen output)
6. Append `wiki/log.md` — do this for every Graph run, including when output is optional or unchanged (record pass / no-op)

Optional output:

```md
wiki/graph/knowledge-map.md
```

---

# 🪵 Logging Rules

Prefer OKF log format ([§7](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#7-log-files-optional)); legacy `[YYYY-MM-DD] operation | title` lines may coexist:

```md
## 2026-06-03
* **Update**: Ingest [AI CUP 參賽筆記](/sources/2026-05-15-ai-cup-參賽筆記.md); aligned bundle to OKF v0.1.
* **Creation**: Added [雙軌個人架構](/concepts/雙軌個人架構.md).
```

---

# 🚫 Hard Constraints

* **Do not modify** existing files under `raw/` (immutable). **New** archives into `raw/sources/` as step 2 of Ingest are allowed.
* NEVER hallucinate without marking
* ALWAYS cite
* ALWAYS link pages
* ALWAYS append `wiki/log.md` when completing any operation defined in this document (each run leaves a trace; use pass / no-op when that operation allows no file changes)
* Update `wiki/index.md` when the operation **creates, deletes, or materially changes** wiki pages or catalog-listed artifacts; when an operation’s steps are narrower (e.g. Graph: index only after graph artifacts change), **follow those steps**
* Do not invent org policies, stakeholders, or “official” processes unless they appear in sources

---

# 🧠 Behavior Principles

* Conservative > creative
* Explicit > implicit
* Linked > isolated
* Structured > verbose
* **Owner intent > template completeness** (ask or infer focus when unclear)

---

# ⚡ Example Commands

```md
- Ingest: specified path → archive to raw/sources/*.md → wiki (per Ingest steps)
- Ingest all files already under raw/sources/ (one pass each; update index + log)
- Generate FAQ from current wiki (8–15 questions, no fabricated Qs)
- Answer: <question> with citations and uncertainty markers (for me)
- Lint the wiki
- Build knowledge graph (e.g. wiki/graph/knowledge-map.md)
- Copy-paste agent prompts from docs/OPERATIONS.md
```
