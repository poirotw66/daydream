---
type: Lint Report
title: "Wiki 健康檢查 2026-06-25"
description: "OKF v0.1 合規、連結、引用、歸檔與 frontmatter 品質掃描"
tags: ["lint"]
timestamp: 2026-06-25T00:00:00Z
status: active
source_count: 0
---

# Wiki 健康檢查 2026-06-25

掃描範圍：`wiki/` 24 個概念檔 + `index.md`；對照 `raw/sources/` 與 [AGENTS.md](../../AGENTS.md)（OKF v0.1）。

## 摘要

| 嚴重度 | 數量 | 說明 |
|--------|------|------|
| **error** | 0（已修 12） | `description` 遷移損壞已於本次 lint 重填 |
| **warn** | 0（已修） | 全庫已補 `# Citations`（24 概念檔 + FAQ／Query） |
| **info** | 0（已處理） | Queries／FAQ 已各 1 頁；11 檔 timestamp 已刷新 |
| **pass** | — | 無斷鏈、無 index 孤兒、無重複 title、OKF `type` 齊全 |

## Errors（應修）

### 1. ~~損壞的 `description`~~（**已於 2026-06-25 修復**）

遷移腳本剝除連結導致 12 檔 `description` 空白；已自 Summary 重填。

## Warnings

### 3. ~~缺少 `# Citations`~~（**已於 2026-06-25 修復**）

`scripts/add_wiki_citations.py` 已為 24 概念檔補齊；另新增 FAQ／Query 各含 Citations。

### 4. ~~`raw/` 與 wiki source 檔名不一致~~（**已於 2026-06-25 修復**）

| wiki source | raw 歸檔 |
|-------------|----------|
| `sources/2026-06-03-recipe-bloss0m-內容農場.md` | `raw/sources/2026-06-03-recipe-bloss0m-內容農場.md`（保留 `-ingest` 原檔） |
| `sources/2026-06-03-年底轉職與時間配置.md` | `raw/sources/2026-06-03-年底轉職與時間配置.md` |
| `sources/2026-05-15-ai-cup-參賽筆記.md` | `raw/sources/2026-05-15-ai-cup-參賽筆記.md`（新補） |

## Info（可排程）

### 5. ~~逾 30 天 `timestamp`~~（**已刷新 11 檔至 2026-06-25**）

### 6. ~~空區塊~~（**已補**）

- [平日時間與三線並行](/queries/平日時間與三線並行.md)
- [daydream Wiki 入門與工作流](/faq/daydream-入門與工作流.md)（12 題）

### 7. `log.md` 歷史條目

仍含 `[[wiki-link]]`；歷史紀錄可保留，新條目用 OKF log 格式（已於 2026-06-03 條目示範）。

## Pass

- **OKF 必填 `type`：** 24/24 概念檔合規
- **index 覆蓋：** 24/24 已列入 `/index.md`
- **斷鏈：** 0（bundle-relative `/…/*.md` 均存在）
- **重複 title：** 0
- **矛盾：** 未發現跨頁衝突（雙軌／三線並行／內容農場與貼圖並行敘事一致）

## 建議修復優先序

1. ~~**P0** — 重填損壞 `description`~~ ✅
2. ~~**P1** — raw 歸檔對齊~~ ✅
3. ~~**P2** — `# Citations`~~ ✅
4. ~~**P3** — FAQ／Query／timestamp~~ ✅

## Relationships

- related_to: [index](/index.md)
- related_to: [AGENTS.md](../../AGENTS.md)

# Citations

[1] [OKF SPEC v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
