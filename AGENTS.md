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

# 📁 Directory Contract

* `raw/`: immutable **existing** sources (❗ do not edit in place). **New** files may be **archived** into `raw/sources/` as step 2 of Ingest.

* `wiki/`: LLM-managed **personal** knowledge base

* `wiki/index.md`: your canonical catalog (start here)

* `wiki/log.md`: append-only personal changelog of wiki operations

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

* Must include YAML frontmatter on wiki pages **except** `wiki/index.md` (catalog — see **Required Frontmatter** below)

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

# 📌 Required Frontmatter

```yaml
---
title: "<Page title>"
type: "<overview|entity|concept|source|query|lint>"
status: "<draft|active|needs-review>"
updated: "YYYY-MM-DD"
source_count: 0
tags: []
---
```

### `wiki/index.md` (catalog)

* **YAML frontmatter is optional** for this file. The required shape is the **Index Structure** heading layout (`# Index`, `## Overview`, …); do not fail compliance for missing frontmatter here.
* The `type: "overview"` value in the schema is for **standalone** overview pages if you add them (e.g. a personal dashboard `wiki/overview.md` for one focus area); it is **not** required for `wiki/index.md`.
* If you choose to add frontmatter to `wiki/index.md`, use the same keys as **Required Frontmatter** (e.g. `type: overview`, `title` describing the catalog).

---

# 🔗 Linking Rules (MANDATORY)

* Every page MUST link to ≥1 page
* Every new page MUST be referenced from `wiki/index.md` (or from a page that is already in the catalog chain)
* Prefer bidirectional links so “idea ↔ project ↔ source” stays navigable for future-you

---

# 🧩 Knowledge Graph Rules

Every page should implicitly or explicitly define relationships:

### Allowed Relationships

* `concept → concept`
* `concept → entity`
* `entity → concept`
* `source → concept/entity`

### Optional explicit section:

```md
## Relationships

- related_to: [[concepts/api]]
- implemented_by: [[entities/spring-boot]]
- used_in: [[sources/ch1]]
```

👉 This enables graph-based reasoning later (personal RAG / agents)

---

# 📏 Page Granularity Rules

* One page = one concept / entity
* > 500 words → split
* Do NOT mix abstraction layers (keep “idea” and “how I run my sticker pipeline” on separate pages when possible)

---

# 📌 Citation Rules (CRITICAL)

* All claims must cite **your** sources (articles, papers, exports, past-you notes)

Format:

```md
[[sources/ch1]]
```

Multiple:

```md
[[sources/ch1]], [[sources/ch3]]
```

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

The canonical catalog is **`wiki/index.md`** (single file). Do **not** assume a separate `wiki/overview.md` unless the owner adds one for a focus area; by default, **all index sections below—including Overview—live in `wiki/index.md`**, in this order:

```md
# Index

## Overview
## Concepts
## Entities
## Sources
## Queries
## FAQ
```

* **`## Overview`**: Short orientation only—**personal scope** (what this repo is for, current focus areas, how future-you should use it), pointers to repo-root **`AGENTS.md`** and **`wiki/README.md`** when present. Use a few bullets; do not duplicate the full taxonomy—**Concepts** onward hold the linked catalog.
* **`## Concepts` … `## FAQ`**: Each entry = **link + one-line description** (per section).

Optional: the owner may add extra index sections (e.g. `## Projects`, `## Areas`) when a second track (research vs. product, job vs. side project) needs a visible split—keep entries link + one-line description.

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
title: "<FAQ title>"
type: "query"
status: "active"
updated: "YYYY-MM-DD"
source_count: 0
tags: ["faq"]
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
- [[concepts/...]]
- [[sources/...]]
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

Append only:

```md
## [YYYY-MM-DD] <operation> | <title>
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
