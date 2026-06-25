---
type: Playbook
title: "daydream Wiki 入門與工作流"
description: "個人 wiki 怎麼用、雙軌／三線、Ingest 與 OKF 常見問題"
tags: ["faq"]
timestamp: 2026-06-25T12:00:00Z
status: active
source_count: 0
---

# daydream Wiki 入門與工作流

## Scope

給「未來的我」：快速回想本 repo 結構、時間分配、side project 規則與 Ingest 習慣。依現有 wiki 收斂，不臆造未寫入的 SOP。

## FAQ

### 1. daydream 這個 repo 是什麼？

**Short Answer：** 個人第二大腦；`wiki/` 是 [OKF v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) Knowledge Bundle，`raw/` 放不可改的來源歸檔。

**Detailed Answer：** 規約在 [AGENTS.md](../AGENTS.md)；目錄從 [index](/index.md) 進入。概念用 markdown + YAML frontmatter，連結用 `/concepts/foo.md` 形式。

**Related Pages：**
- [index](/index.md)
- [雙軌個人架構](/concepts/雙軌個人架構.md)

### 2. 「雙軌」與 2026-06 的「三線」差在哪？

**Short Answer：** 雙軌是知識 vs 變現產品；三線是 2026-06 後在變現軌內再拆求職主砲、變現、知識的**時間**配置。

**Detailed Answer：** [雙軌個人架構](/concepts/雙軌個人架構.md) 定義知識處理與貼圖／內容農場產品脈絡。[年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md) 將 ml-intern+bloss0m、recipe 農場、知識合成列為三線並行。

**Related Pages：**
- [內容農場變現軌](/concepts/內容農場變現軌.md)
- [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md)

### 3. 平日 4 小時建議怎麼切？

**Short Answer：** 常態週約 2h ml-intern、1.5h recipe 農場、30min 收斂（發想／bloss0m 短文／PR）。

**Detailed Answer：** 見 [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md) 時間表；賽季週可提高 ml-intern+競賽至約 14h。（確定）[2026-06-03 年底轉職與時間配置](/sources/2026-06-03-年底轉職與時間配置.md)

**Related Pages：**
- [ML-Intern 參賽方法](/entities/ml-intern-參賽方法.md)

### 4. ML-Intern 方法是什麼？

**Short Answer：** AI CUP 2026 的參賽取向；2026-06 起落地為可重現 **skill／harness**（baseline、指標、一鍵重跑）。

**Detailed Answer：** 名稱來自 [2026-05-15 AI CUP 參賽筆記](/sources/2026-05-15-ai-cup-參賽筆記.md)；具體 subcommand 與 SOP 仍標（未知）。可與 [#001 Eval Kit](/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md) 合流。

**Related Pages：**
- [AI CUP 2026 參賽](/concepts/ai-cup-2026-參賽.md)

### 5. recipe.bloss0m.com 與貼圖商務的關係？

**Short Answer：** 同屬變現軌、產品形態不同（SEO 站 vs LINE 貼圖）；品牌流量是否共用尚未定。

**Detailed Answer：** [內容農場變現軌](/concepts/內容農場變現軌.md) 對照表；[recipe.bloss0m.com](/entities/recipe-bloss0m-com.md) 與 [LINE 貼圖平台](/entities/line-貼圖平台.md) 為兩個終點。

**Related Pages：**
- [貼圖商務自動化](/concepts/貼圖商務自動化.md)

### 6. AI CUP 2026 我參哪兩場？

**Short Answer：** 桌球戰術時序預測 + ESG 永續承諾驗證（VeriPromiseESG4K）。

**Detailed Answer：** [AI CUP 2026 參賽](/concepts/ai-cup-2026-參賽.md)；桌球 Baseline 見 [官方 LSTM 簡報](/sources/2026-ai-cup-桌球戰術-baseline.md)；ESG 四子任務見 [ESG 永續承諾驗證任務](/concepts/esg-永續承諾驗證任務.md)。

**Related Pages：**
- [桌球 Baseline LSTM 多任務](/concepts/桌球-baseline-lstm-多任務.md)

### 7. Ingest 新資料時要做什麼？

**Short Answer：** 讀來源 → 歸檔 `raw/sources/` → 寫 `wiki/sources/` → 抽概念／實體 → 連結 → 更新 index → append log。

**Detailed Answer：** 步驟見 [AGENTS.md](../AGENTS.md) Operation: Ingest；Agent 提示見 [docs/OPERATIONS.md](../docs/OPERATIONS.md)。

**Related Pages：**
- [研究與知識合成](/concepts/研究與知識合成.md)

### 8. 為什麼 `raw/` 不能改？

**Short Answer：** 可追溯：幾個月後要知道「當初讀到／寫下的是什麼原文」。

**Detailed Answer：** 僅允許**新增**歸檔檔；wiki 概念可演進，但 `raw/sources/*` 為 immutable。引用寫在概念頁 `# Citations` 的 `` `raw/...` `` 路徑。

**Related Pages：**
- [2026-05-15 個人雙軌構思](/sources/2026-05-15-個人雙軌構思.md)

### 9. side project 發想怎麼進候選池？

**Short Answer：** 每天 ~15min 記一則；五維各 1–5 分，≥16/25 且公開性 Yes 才進池；每週最多實作 1 個。

**Detailed Answer：** 規則在 [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md)；#001 範例：[Agentic RAG Eval Kit](/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md)（22/25）。

**Related Pages：**
- [bloss0m.com](/entities/bloss0m-com.md)

### 10. bloss0m.com 在轉職敘事裡扮演什麼角色？

**Short Answer：** 公開驗證 Agent／RAG／上線能力的作品集與文章站；不得放國泰內部資料。

**Detailed Answer：** [bloss0m.com](/entities/bloss0m-com.md) 與 [國泰金控 AI 架構師](/entities/國泰金控-ai-架構師.md) 分工：現職提供面試背景，對外作品一律公開來源。

**Related Pages：**
- [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md)

### 11. OKF 的 `# Citations` 和 `## Evidence` 怎麼共存？

**Short Answer：** Evidence 可留作筆記脈絡；Citations 是 OKF 建議的文末編號引用區。

**Detailed Answer：** 新頁應有 `# Citations`；舊頁可漸進合併。見 [Lint 報告](/lint/2026-06-25-wiki-health.md) P2 修復說明。

**Related Pages：**
- [AGENTS.md](../AGENTS.md)

### 12. 知識合成軌時間不夠時怎麼辦？

**Short Answer：** 2026-06 規劃明確讓位給求職主砲與變現軌；可縮但不刪架構。

**Detailed Answer：** [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md) 三線第 3 點；工具仍記在 [NotebookLM](/entities/notebooklm.md)。

**Related Pages：**
- [研究與知識合成](/concepts/研究與知識合成.md)

## Relationships

- related_to: [index](/index.md)

# Citations

[1] [Wiki 健康檢查 2026-06-25](/lint/2026-06-25-wiki-health.md)
