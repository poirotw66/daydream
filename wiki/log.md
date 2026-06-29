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

## 2026-06-03
* **Update**: Aligned `wiki/` to [OKF v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)—`AGENTS.md` OKF section, frontmatter (`type`/`description`/`timestamp`), bundle-relative links, [index](/index.md) with `okf_version: "0.1"`.
* **Update**: Migrated 24 concept files; refreshed `docs/templates/*` and `docs/OPERATIONS.md` ingest prompt.

## 2026-06-25
* **Lint**: [Wiki 健康檢查 2026-06-25](/lint/2026-06-25-wiki-health.md) — 0 斷鏈；23 頁缺 `# Citations`；補齊 12 個損壞 `description`；標記 raw 歸檔 slug 不一致與 AI CUP 筆記缺 raw。

## 2026-06-25
* **Update**: P1 — 新增 `raw/sources/2026-05-15-ai-cup-參賽筆記.md`；canonical 複本 `2026-06-03-recipe-bloss0m-內容農場.md`、`2026-06-03-年底轉職與時間配置.md`。
* **Update**: P2 — 24 概念檔補 `# Citations`；11 檔 `timestamp` 刷新至 2026-06-25。
* **Creation**: [平日時間與三線並行](/queries/平日時間與三線並行.md)、[daydream 入門與工作流 FAQ](/faq/daydream-入門與工作流.md)。
* **Update**: [Lint 報告](/lint/2026-06-25-wiki-health.md) 結案 P1–P3。

## 2026-06-25
* **Update**: GitHub Pages — `mkdocs.yml`、Material 主題、`.github/workflows/deploy-wiki-pages.yml`；`wiki/README.md` → [wiki-guide.md](/wiki-guide.md)。
* **Update**: [index](/index.md) 新增線上站連結；目標 URL https://poirotw66.github.io/daydream/
* **Update**: MkDocs UX — Hero 卡片、OKF 類型標籤、Tabs、tags 插件、`extra.css`／`extra.js`。

## [2026-06-25] docs | MkDocs 棧升級與站點修復

* **Update**: `requirements-docs.txt` → `mkdocs-ng` 1.7+ + Material 9.7（維持 MkDocs 1.x，避開未穩定之 2.0）。
* **Update**: CI 設 `NO_MKDOCS_2_WARNING=1`；`docs/mkdocs_hooks.py` 站內連結改相對路徑、`.github/` 改 GitHub blob URL。
* **Update**: 自訂 logo `wiki/assets/daydream-logo.png`（192px，~72KB）；[wiki-guide](/wiki-guide.md) 補本機預覽說明。
* **Update**: [index](/index.md) 精簡首頁 — Hero 主軌卡片 + 入門連結 + 分區摘要；完整條目改由頂部導覽承載。

## [2026-06-25] ingest | 主線重定義：Agent 職涯

* **Archive**: `raw/sources/2026-06-25-主線重定義-agent職涯.md`
* **Creation**: [主線重定義 Agent 職涯](/sources/2026-06-25-主線重定義-agent職涯.md)、[現職場內 Agent 案子](/concepts/現職場內-agent-案子.md)
* **Update**: [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md) — 鎖定 Agent 開發／應用；場內案子 + bloss0m；廢止 ml-intern 時間主軸
* **Update**: [AI CUP 2026 參賽](/concepts/ai-cup-2026-參賽.md)、[ML-Intern 參賽方法](/entities/ml-intern-參賽方法.md) → 已結案／`needs-review`
* **Update**: FAQ、首頁 Hero
* **Update**: 根目錄 [README.md](../README.md) — daydream 入門、現行主軸、連結與 MkDocs 預覽

## [2026-06-25] ingest | 學習與 side 主軸第二調整

* **Archive**: `raw/sources/2026-06-25-學習與-side-主軸調整.md`
* **Creation**: [學習與 side 主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)；concepts — [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)、[金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md)、[每日資訊收集-agent](/concepts/每日資訊收集-agent.md)、[每日技術前沿-blog](/concepts/每日技術前沿-blog.md)、[李宏毅課程論文深讀](/concepts/李宏毅課程論文深讀.md)
* **Creation**: entities — [kaggle](/entities/kaggle.md)、[autoresearch](/entities/autoresearch.md)、[李宏毅-課程](/entities/李宏毅-課程.md)、[cursor-superpowers](/entities/cursor-superpowers.md)
* **Update**: [內容農場變現軌](/concepts/內容農場變現軌.md)、[recipe-bloss0m-com](/entities/recipe-bloss0m-com.md) → 暫時收尾；[ml-intern-參賽方法](/entities/ml-intern-參賽方法.md) 重啟；[年底轉職-agent-準備](/concepts/年底轉職-agent-準備.md)、Hero、README、query、FAQ

## [2026-06-25] query | Kaggle 路徑 survey + autoresearch 對齊

* **Archive**: `raw/sources/2026-06-25-kaggle路徑與輸出分工.md`
* **Creation**: [Kaggle 路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md)、[kaggle-經典賽與學習路徑](/queries/kaggle-經典賽與學習路徑.md)
* **Update**: [autoresearch](/entities/autoresearch.md) → [karpathy/autoresearch](https://github.com/karpathy/autoresearch)；blog／side 並存分工

## [2026-06-25] refactor | 移除 FAQ 專區

* **Delete**: `wiki/faq/daydream-入門與工作流.md`；本 wiki 可重用問答改以 `queries/` 為準
* **Update**: [index](/index.md)、[mkdocs.yml](../mkdocs.yml)、[README.md](../README.md)、[wiki-guide](/wiki-guide.md)、[mkdocs_hooks.py](../docs/mkdocs_hooks.py)

## [2026-06-25] query | 金融業 Agent 應用探索

* **Archive**: `raw/sources/2026-06-25-金融業-agent-應用探索.md`
* **Creation**: [金融業 Agent 應用探索](/sources/2026-06-25-金融業-agent-應用探索.md)、[query](/queries/金融業-agent-應用探索.md)
* **Creation**: projects — [#002 公開法規 RAG](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md)、[#003 詐欺 Copilot](/projects/ideas/2026-06-25-003-詐欺調查-copilot.md)
* **Update**: [金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md)、index、mkdocs nav

## [2026-06-25] plan | #002 Corpus 詳規

* **Archive**: `raw/sources/2026-06-25-002-corpus-規劃.md`
* **Creation**: [#002 corpus 規劃 source](/sources/2026-06-25-002-corpus-規劃.md)
* **Update**: [#002 公開法規 RAG](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) — 鎖定洗錢防制法體系、manifest、golden 10 題、Day 1～7

## [2026-06-25] update | #002 核心問題與交付清單

* **Update**: [#002](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) — 補「核心問題」「成功標準」「repo／wiki／blog 交付清單」

## [2026-06-25] ingest | #002 時事微調（國泰投信／ETtoday）

* **Archive**: `raw/sources/2026-06-25-國泰投信利害關係人-ettoday.md`
* **Creation**: [國泰投信利害關係人 ETtoday](/sources/2026-06-25-國泰投信利害關係人-ettoday.md)
* **Update**: [#002](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) — 雙軌 corpus（投信利害關係人主 + AML 輔）、法遵指引、golden 12 題、拒答媒體金額

## [2026-06-25] retire | #001 Agentic RAG Eval Kit 結案移除

* **Delete**: `wiki/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md`（擁有者已於 bloss0m 完成，不再進候選池）
* **Update**: [#002](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md)、[金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md)、[金融業-agent-應用探索](/queries/金融業-agent-應用探索.md)、[年底轉職-agent-準備](/concepts/年底轉職-agent-準備.md)、[bloss0m-com](/entities/bloss0m-com.md)、index、mkdocs nav

## [2026-06-25] lint | Wiki 健康檢查重跑

* **Update**: [Wiki 健康檢查 2026-06-25（重跑）](/lint/2026-06-25-wiki-health.md) — 2 error（歷史 faq 斷鏈）、index Sources 11、pass 主線一致
* **Fix**: [index](/index.md) 計數；[金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md) 移除已解決 Open Question

## [2026-06-25] ux | 首頁改為點子集散中心

* **Update**: [index](/index.md) — Side 點子卡、四主軸、決策捷徑；移除目錄式分區計數
* **Update**: [mkdocs_hooks.py](../docs/mkdocs_hooks.py) Hero、[extra.css](../wiki/stylesheets/extra.css) hub 樣式、[mkdocs.yml](../mkdocs.yml) nav「Side 點子」置頂

## [2026-06-25] schema | AGENTS.md / OPERATIONS 對齊現況

* **Update**: [AGENTS.md](../AGENTS.md) — `faq/` 廢止、`index.md` 點子集散、完整目錄改由 `mkdocs.yml` nav
* **Update**: [OPERATIONS.md](../docs/OPERATIONS.md) — FAQ deprecated、Query Persist prompt、nav 與 index hub 分工
