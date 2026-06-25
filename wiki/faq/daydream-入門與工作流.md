---
type: Playbook
title: "daydream Wiki 入門與工作流"
description: "個人 wiki 怎麼用、雙軌／三線、Ingest 與 OKF 常見問題"
tags: ["faq"]
timestamp: 2026-06-25T00:00:00Z
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

### 2. 「雙軌」與求職主線怎麼對齊？

**Short Answer：** 雙軌仍是知識 vs 變現產品；**2026-06-25** 起求職主軸改為**場內 Agent 案子**（正職）+ **bloss0m 公開作品**（side），AI CUP 已結案。

**Detailed Answer：** [雙軌個人架構](/concepts/雙軌個人架構.md) 定義知識與變現脈絡。[年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md) 與 [現職場內 Agent 案子](/concepts/現職場內-agent-案子.md) 收斂轉職方向為 Agent 開發／應用。

**Related Pages：**
- [內容農場變現軌](/concepts/內容農場變現軌.md)
- [主線重定義 2026-06-25](/sources/2026-06-25-主線重定義-agent職涯.md)

### 3. 平日 4 小時建議怎麼切？

**Short Answer：** **2026-06-25 起**：~1.5h Kaggle／ml-intern、~1.5h 金融 Agent side、~1h 每日 blog、~15min 金融 Agent 發想；場內案子用正職時間。

**Detailed Answer：** 見 [年底轉職 Agent 準備](/concepts/年底轉職-agent-準備.md)。內容農場已收尾；李宏毅深讀時段待排。

**Related Pages：**
- [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)
- [金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md)

### 4. ML-Intern / Autoresearch 還要做嗎？

**Short Answer：** **要**；與 [autoresearch](/entities/autoresearch.md) 並行，從 [Kaggle](/entities/kaggle.md) 經典賽重新啟動。

**Detailed Answer：** 見 [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)。AI CUP 已結案，eval 思路可延續到 #001 或 bloss0m。

**Related Pages：**
- [ML-Intern 參賽方法](/entities/ml-intern-參賽方法.md)

### 5. recipe.bloss0m.com 還維運嗎？

**Short Answer：** **暫時收尾**（2026-06-25）；不再佔 side 時間，頁面保留歷史。

**Detailed Answer：** [內容農場變現軌](/concepts/內容農場變現軌.md) 標 `needs-review`；[recipe.bloss0m.com](/entities/recipe-bloss0m-com.md) 站點狀態不變、主動投入暫停。

### 6. AI CUP 2026 現在什麼狀態？

**Short Answer：** 個人參賽階段**已告一段落**（2026-06-25）；桌球 + ESG 相關頁面保留作歷史參考。

**Detailed Answer：** [AI CUP 2026 參賽](/concepts/ai-cup-2026-參賽.md) 標為 `needs-review`；主線見 [主線重定義 2026-06-25](/sources/2026-06-25-主線重定義-agent職涯.md)。

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
