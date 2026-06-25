# LLM Wiki（llm-wiki-example）

Persistent, LLM-maintained knowledge base in markdown；`wiki/` 為 [OKF v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) Knowledge Bundle（規約見 repo 根目錄 **AGENTS.md**）。

## Folder Layout

```text
raw/
  sources/    # archived sources（新增歸檔；既有檔不就地修改）
  assets/     # images / attachments（選用）
wiki/
  sources/
  entities/
  concepts/
  queries/
  faq/
  lint/
  graph/
  index.md
  log.md
AGENTS.md     # repo 根目錄規約，以此為準
```

## Quick Start

1. 提供 **指定**來源檔或將稿件 **歸檔**為 `raw/sources/` 下之 **新檔** `*.md`。  
2. 依 **AGENTS.md** 執行 Ingest（wiki/sources、concepts、entities、index、log）。  
3. 確認 `wiki/index.md` 已列出條目，`wiki/log.md` 已 append。

## Naming Suggestions

- Source page: `wiki/sources/<source-slug>.md`
- Entity page: `wiki/entities/<entity-name>.md`
- Concept page: `wiki/concepts/<concept-name>.md`
- Query page: `wiki/queries/<query-slug>.md`
- FAQ page: `wiki/faq/<faq-slug>.md`

## Editing Discipline

- Do not change **existing** files under `raw/` in place; add new archives during Ingest.

## GitHub Pages（網頁閱讀）

- 站點由 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 從 `wiki/` 建置。
- 線上網址：**https://poirotw66.github.io/daydream/**
- 本機預覽：

```bash
pip install -r requirements-docs.txt
NO_MKDOCS_2_WARNING=1 mkdocs serve
# → http://127.0.0.1:8000/daydream/
```

- 建置棧：`mkdocs-ng` 1.7+（社群維護的 MkDocs 1.x fork）+ Material 9.7；**勿**升級至尚未穩定的 MkDocs 2.0。

- `push` 至 `main` 時，[`.github/workflows/deploy-wiki-pages.yml`](../.github/workflows/deploy-wiki-pages.yml) 自動部署。
- 首次請在 GitHub repo **Settings → Pages → Build and deployment → Source: GitHub Actions**。
- 若 CI 出現 `Failed to create deployment (status: 404)`，代表 Pages 尚未啟用或 Source 不是 **GitHub Actions**；完成上述設定後到 **Actions** 重跑 **Deploy wiki to GitHub Pages**。
- `Node 20 is being deprecated` 為 runner 提示，與此 404 無關；`deploy-pages@v4` 已跑在 Node 24。

### 站點 UX（僅 GitHub Pages）

- **首頁 Hero**：四張主軌卡片（雙軌／AI CUP／內容農場／轉職）。
- **OKF 標籤**：每頁顯示 `Concept`／`Entity`／`Source` 等類型與 `description` 摘要。
- **頂部 Tabs**：Concepts、Entities、Sources… 一鍵切換。
- **標籤雲**：frontmatter `tags` 可點選篩選。
- 樣式：`wiki/stylesheets/extra.css`；建置時注入見 `docs/mkdocs_hooks.py`（不修改 wiki 正文）。
