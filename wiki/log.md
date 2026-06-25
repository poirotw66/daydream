# Wiki Log

Chronological, append-only operational log.

## [2026-05-06] bootstrap | Initialize empty LLM Wiki repository

- 建立 `raw/sources`、`raw/assets` 與 `wiki/*` 分層（sources、concepts、entities、queries、faq、lint、graph）。
- 初始化 `wiki/index.md`（空目錄）、`wiki/log.md`。
- 放置 **AGENTS.md** 於 repo 根目錄；頁面版型於 `docs/templates/page-template.md`。

## [2026-05-08] docs | Restore docs/ in this repository

- 本倉 **`docs/`** 已就緒；`docs/templates/page-template.md` 與版型約定對齊；Agent 操作複製提示以本倉 **docs/OPERATIONS.md** 為準。

## [2026-05-11] docs | Align README / index / log with standalone repo

- 敘述改為本 repo **llm-wiki-example** 即主工作區，移除「example 子資料夾」「上一層主倉」等易誤導路徑；**docs/OPERATIONS.md** 統一為本倉權威操作提示；同步修正 **wiki/README.md** 標題與 AGENTS.md 說明。

## [2026-05-11] hygiene | .gitignore and graphify scope

- **.gitignore**：改為 `**/.DS_Store`；新增 `graphify-out/`（本倉不納入 graphify 產物，本機產生者不提交）。
- **README.md**：新增「Graphify 與 `graphify-out/`」小節，對照 Cursor 規則中可能引用之不存在路徑。

## [2026-05-11] docs | Source template split and OPERATIONS coverage

- **docs/templates**：`page-template.md` 改為索引；新增 **page-template-source.md**（對齊 **AGENTS.md** Source Page Schema 區塊名稱）、**page-template-concept.md**（非 source 頁）；**AGENTS.md** 目錄契約與 Source 版型句同步更新。
- **docs/OPERATIONS.md**：補 **FAQ**、**Graph**、**Wiki log append (pass / no-op)** 英文複製提示；Lint／總述對齊「每次執行須 append `wiki/log.md`」規則。

## [2026-05-15] ingest | 260515.md → 個人雙軌構思

- 歸檔：`raw/sources/2026-05-15-個人雙軌構思.md`（來源 `260515.md`）。
- 新增 source：[[sources/2026-05-15-個人雙軌構思]]。
- 概念：[[concepts/雙軌個人架構]]、[[concepts/研究與知識合成]]、[[concepts/解說式輸出]]、[[concepts/貼圖商務自動化]]。
- 實體：[[entities/notebooklm]]、[[entities/line-貼圖平台]]。
- 更新 `wiki/index.md` Overview／目錄條目。

## [2026-05-15] ingest | 0515.md + 桌球 Baseline PDF

- 歸檔：`raw/sources/2026-05-15-ai-cup-參賽筆記.md`（`0515.md`）、`raw/sources/2026-ai-cup-桌球戰術-baseline-method.pdf` + `2026-ai-cup-桌球戰術-baseline-文稿.md`。
- Sources：[[sources/2026-05-15-ai-cup-參賽筆記]]、[[sources/2026-ai-cup-桌球戰術-baseline]]。
- Concepts：[[concepts/ai-cup-2026-參賽]]、[[concepts/桌球戰術時序預測]]、[[concepts/桌球-baseline-lstm-多任務]]、[[concepts/esg-永續承諾驗證任務]]。
- Entities：[[entities/ai-cup-2026]]、[[entities/veripromise-esg4k]]、[[entities/ml-intern-參賽方法]]。
- 更新 `wiki/index.md`。

## [2026-06-03] ingest | recipe.bloss0m.com 內容農場與變現軌

- 歸檔：`raw/sources/2026-06-03-recipe-bloss0m-內容農場-ingest.md`（站點實勘、Recipe repo、對話脈絡）。
- Source：[[sources/2026-06-03-recipe-bloss0m-內容農場]]。
- Concept：[[concepts/內容農場變現軌]]。
- Entity：[[entities/recipe-bloss0m-com]]。
- 更新：[[entities/line-貼圖平台]]（品牌流量 Open Question）、[[concepts/貼圖商務自動化]]、[[concepts/雙軌個人架構]]。
- 更新 `wiki/index.md` Overview／Concepts／Entities／Sources。

## [2026-06-03] ingest | 年底轉職、ml-intern、平日 4h

- 歸檔：`raw/sources/2026-06-03-年底轉職與時間配置-ingest.md`（對話脈絡）。
- Source：[[sources/2026-06-03-年底轉職與時間配置]]。
- Concept：[[concepts/年底轉職-agent-準備]]。
- Entities：[[entities/bloss0m-com]]、[[entities/國泰金控-ai-架構師]]。
- 更新：[[entities/ml-intern-參賽方法]]（skill 實作、時間配額）、[[concepts/ai-cup-2026-參賽]]、[[entities/recipe-bloss0m-com]]。
- 更新 `wiki/index.md` Overview／Concepts／Entities／Sources。

## [2026-06-03] projects | #001 Agentic RAG Eval Kit 定稿

- 新增：[[projects/ideas/2026-06-03-001-agentic-rag-eval-kit]]（7 天 MVP、評分、候選池狀態）。
- 更新：[[concepts/年底轉職-agent-準備]]、[[entities/ml-intern-參賽方法]]；`wiki/index.md` 新增 **## Projects**。
