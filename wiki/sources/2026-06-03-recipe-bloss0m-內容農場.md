---
type: Source
title: "recipe.bloss0m.com 內容農場實勘"
description: "**今天煮什麼**（https://recipe.bloss0m.com/）為 bloss0m 子域食譜 SEO 站：一人份、食材優先、情境與專區叢集、冰箱剩料工具。"
tags: ["內容農場", "seo", "recipe"]
timestamp: 2026-06-03T00:00:00Z
status: active
source_count: 1
---
# recipe.bloss0m.com 內容農場實勘

歸檔：`raw/sources/2026-06-03-recipe-bloss0m-內容農場.md`（canonical；同文見 `-ingest` 檔）

## Summary

- **今天煮什麼**（https://recipe.bloss0m.com/）為 bloss0m 子域食譜 SEO 站：一人份、食材優先、情境與專區叢集、冰箱剩料工具。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)
- 技術為 Astro static + Cloudflare Pages；變現路線為 SEO → **AdSense**，Ad 買量為後段選項。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)
- 生產環境曾出現 **canonical／sitemap 指向 example.com** 的部署設定問題，需 `PUBLIC_SITE_URL` 與 redeploy。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)
- 與 [貼圖商務自動化](/concepts/貼圖商務自動化.md) 並列為個人 **變現軌**；與貼圖／主站品牌流量分工尚待決策。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)

## Key Concepts

- [內容農場變現軌](/concepts/內容農場變現軌.md) — 食譜 SEO 站與貼圖商務同属變現脈絡
- [貼圖商務自動化](/concepts/貼圖商務自動化.md) — 雙軌中的貼圖產品線

## Entities

- [recipe-bloss0m-com](/entities/recipe-bloss0m-com.md) — 子域站點與 AdSense 就緒狀態
- [line-貼圖平台](/entities/line-貼圖平台.md) — 同軌另一終點；品牌流量是否共用（未知）

## Notable Claims

- 首頁主訴：「先看你手邊有什麼」、工具頁已接本地 recipe 與 taxonomy 排序。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)
- 本機 build 約 **119 頁**；含 Recipe／FAQ 等 structured data 與分片 sitemap。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)
- `robots.txt` 透過 `src/pages/robots.txt.ts` 生成；未設 env 時 Sitemap 會變成 `example.com`。（確定）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)

## Limitations / Gaps

- 未收錄 Cloudflare 實際 env 截圖或 GSC 索引數據。（未知）
- Google AdSense 是否已送審、核准狀態未記錄。（未知）
- 批次內容生產 agent 是否已接入產線：僅為轉職敘事建議，非現況斷言。（推測）[2026-06-03-recipe-bloss0m-內容農場](/sources/2026-06-03-recipe-bloss0m-內容農場.md)

## Relationships

- related_to: [內容農場變現軌](/concepts/內容農場變現軌.md)
- related_to: [recipe-bloss0m-com](/entities/recipe-bloss0m-com.md)
- related_to: [雙軌個人架構](/concepts/雙軌個人架構.md)

# Citations

[1] `raw/sources/2026-06-03-recipe-bloss0m-內容農場.md`（immutable archive）
