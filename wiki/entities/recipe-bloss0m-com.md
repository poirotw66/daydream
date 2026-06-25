---
title: "recipe.bloss0m.com（今天煮什麼）"
type: entity
status: active
updated: "2026-06-03"
source_count: 1
tags: ["內容農場", "seo", "adsense"]
---

# recipe.bloss0m.com（今天煮什麼）

## Summary

**https://recipe.bloss0m.com/** 為個人 **內容農場**主戰場：台灣一人份食譜 SEO 站（品牌名 **今天煮什麼**），技術棧 Astro + Cloudflare Pages，變現路線為 **SEO 累積 → Google AdSense**（對話中規劃之 Google Ads 買量為後段）。（確定）[[sources/2026-06-03-recipe-bloss0m-內容農場]]

## Key Points

- **產品差異**：食材優先、情境叢集、**冰箱剩料工具**（本地 recipe + taxonomy 排序，非先上 LLM）。（確定）[[sources/2026-06-03-recipe-bloss0m-內容農場]]
- **SEO**：分片 sitemap、Recipe／FAQ 等 JSON-LD；部署須設 `PUBLIC_SITE_URL=https://recipe.bloss0m.com`，否則 canonical／robots 可能指向 `example.com`。（確定）[[sources/2026-06-03-recipe-bloss0m-內容農場]]
- **變現**：repo 已備 AdSlot、`ads.txt` 占位、`PUBLIC_ADSENSE_CLIENT`；送審前需真實 publisher id 與索引量。（確定）[[sources/2026-06-03-recipe-bloss0m-內容農場]]
- **生態**：bloss0m.com 子域；與 [[entities/line-貼圖平台]] 是否共用品牌導流尚未定。（未知）[[sources/2026-06-03-recipe-bloss0m-內容農場]]

## Evidence

- [[sources/2026-06-03-recipe-bloss0m-內容農場]]

## Open Questions

- AdSense 送審與核准時程？（未知）
- `seo.ts` 是否改為預設 `Astro.site`，避免 CI 漏 env？（推測）[[sources/2026-06-03-recipe-bloss0m-內容農場]]
- 內容批次是否接入 agent／skill 產線？（未知）

## Relationships

- related_to: [[concepts/內容農場變現軌]]
- related_to: [[concepts/貼圖商務自動化]]
- related_to: [[entities/line-貼圖平台]]
- related_to: [[entities/bloss0m-com]]
- related_to: [[concepts/年底轉職-agent-準備]]
- grounded_in: [[sources/2026-06-03-recipe-bloss0m-內容農場]]
