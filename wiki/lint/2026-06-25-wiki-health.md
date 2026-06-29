---
type: Lint Report
title: "Wiki 健康檢查 2026-06-25（重跑）"
description: "OKF 合規、斷鏈、孤兒頁、status、index 計數與敘事一致性"
tags: ["lint"]
timestamp: 2026-06-25T24:30:00Z
status: active
source_count: 0
---

# Wiki 健康檢查 2026-06-25（重跑）

掃描範圍：`wiki/` 共 **48** 個 `.md`（含 `index.md`、`log.md`、`wiki-guide.md`）；對照 `mkdocs.yml` nav 與 [AGENTS.md](../../AGENTS.md)。

## 摘要

| 嚴重度 | 數量 | 說明 |
|--------|------|------|
| **error** | 2 | 斷鏈指向已刪除 `faq/` 頁（歷史 log、舊 lint 條目） |
| **warn** | 1 | `index.md` Sources 計數與實際不符（7 → 應為 11）— **本次已修** |
| **info** | 6 | `draft`／`needs-review` 頁、`source_count` 與 Citations 條數不一致、無 `wiki/graph/`、Open Question 過時 |
| **pass** | — | 無孤兒頁、無重複 title、概念頁皆有 `# Citations`、#001 已自 nav 移除 |

## Errors（應修）

### 1. 斷鏈：`/faq/daydream-入門與工作流.md`

FAQ 專區已於 2026-06-25 移除；下列檔案仍含連結：

| 檔案 | 建議 |
|------|------|
| [log.md](/log.md) L78 | 歷史條目改純文字或註「已刪」；**不影響 build**（MkDocs 不發佈 log 內死鏈檢查） |
| 本檔舊版條目 | 已由本次重跑覆寫 |

**使用者路徑斷鏈：** **0**（`concepts`／`entities`／`sources`／`queries`／`projects` 互鏈均存在）

## Warnings

### 2. ~~`index.md` 分區計數過時~~（**已於本次 lint 修復**）

| 區塊 | 舊 | 實際 |
|------|-----|------|
| Sources | 7 | **11** |

Concepts 16、Entities 12、Projects 2、Queries 3 — 正確。

## Info（可排程）

### 3. `status` 非 active

| 頁面 | status | 建議 |
|------|--------|------|
| [每日資訊收集-agent](/concepts/每日資訊收集-agent.md) | `draft` | 補來源清單後升 `active` |
| [內容農場變現軌](/concepts/內容農場變現軌.md) | `needs-review` | 標 `archived` 或保留暫停說明 |
| [recipe-bloss0m-com](/entities/recipe-bloss0m-com.md) | `needs-review` | 同上 |
| [ai-cup-2026-參賽](/concepts/ai-cup-2026-參賽.md) | `needs-review` | 已結案；可改 `archived` |

### 4. `source_count` 與 `# Citations` 條數不一致（9 檔）

OKF `source_count` 慣例為**歸檔來源數**；部分頁將外部 URL 亦列入 Citations，導致條數 > `source_count`。**非斷鏈**；可漸進對齊或維持現狀。

範例：[#002](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) 宣告 3、Citations 7（含 MOJ／金管會外部連結）。

### 5. Open Question 已過時

| 頁面 | 項目 | 狀態 |
|------|------|------|
| [金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md) | #002 corpus 選型 | 已鎖定 — **本次已自 Open Questions 移除** |
| [金融業-agent-應用探索](/queries/金融業-agent-應用探索.md) | 同上 | 已標 ~~已鎖定~~ |

### 6. 無 `wiki/graph/`

[AGENTS.md](../../AGENTS.md) Graph 操作可選；目前 **0** 檔。非錯誤。

### 7. 歷史 `log.md` 條目

含已刪 [#001](/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md)、FAQ 連結 — **append-only 保留**；新讀者應以最新條目為準。

## Pass

- **OKF `type`：** 概念／實體／來源／query／project 頁皆有 frontmatter `type`
- **Catalog：** `mkdocs.yml` nav 覆蓋所有知識頁；**無孤兒**
- **主線敘事：** 內容農場暫停、#001 結案、候選池 #002／#003 — **跨頁一致**（確定）
- **timestamp：** 無逾 30 天未更新之概念頁（閾值 2026-05-26）
- **#001 專案頁：** 已刪除；無殘留 nav 條目

## 建議修復優先序

1. ~~**P0** — 修正 `index.md` Sources 計數~~ ✅
2. ~~**P1** — 移除過時 Open Question（#002 corpus）~~ ✅
3. **P2** — `draft`／`needs-review` 頁決定 `archived` 或補內容
4. **P3** — 可選：統一 `source_count` 或 Graph 初版

## Relationships

- related_to: [index](/index.md)
- related_to: [AGENTS.md](../../AGENTS.md)

# Citations

[1] [AGENTS.md](../../AGENTS.md) — Operation: Lint
[2] [log.md](/log.md) — 2026-06-25 retire #001、移除 FAQ
