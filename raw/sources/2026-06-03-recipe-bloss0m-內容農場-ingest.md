# 歸檔：recipe.bloss0m.com 內容農場與 wiki Ingest 脈絡

**歸檔日**：2026-06-03  
**來源類型**：站點實勘（https://recipe.bloss0m.com/）、本機 `Recipe` repo（`README.md`、`astro.config.mjs`、`src/lib/seo.ts`）、擁有者對話（2026-06 轉職／時間配置／內容農場策略）

---

## 站點摘要

- 品牌：**今天煮什麼**；網域 **https://recipe.bloss0m.com/**，隸屬 bloss0m 生態之子站。
- 定位：台灣一人份、租屋族、懶人料理；首頁強調「先食材後菜名」、冰箱剩料工具（本地 recipe + taxonomy 排序）。
- 內容結構：情境入口（一人料理、10 分鐘、高蛋白等）、牛肉／義大利麵專區、食譜／食材／情境 taxonomy、冰箱工具頁。
- 技術：Astro static、Cloudflare Pages；build 約 119 頁（2026-06 本機驗證）。
- 變現路線：SEO 累積索引 → **Google AdSense**（`PUBLIC_ADSENSE_CLIENT`、`AdSlot`、政策頁）；之後可小預算 **Google Ads** 測高意圖 landing（對話中規劃，尚未執行）。

## SEO／部署發現（可驗證）

- 生產環境 `robots.txt` 曾指向 `https://example.com/sitemap-index.xml`，因 build 未設 `PUBLIC_SITE_URL`；README 要求 `PUBLIC_SITE_URL=https://recipe.bloss0m.com`。
- `src/lib/seo.ts` 的 `absoluteUrl` fallback 為 `example.com`；`SeoHead.astro` 另有 `Astro.site` fallback，兩者不一致。
- 線上 `/sitemap-index.xml` 曾回 500；本機帶正確 env 的 static build 可產出正確 sitemap。

## 與個人架構的關係（擁有者陳述）

- **內容農場**與 [[concepts/貼圖商務自動化]] 同屬雙軌中的 **變現／產品軌**（非知識合成軌）。
- 平日約 4h 投入：ml-intern skill（AI CUP）與本內容農場並行；假日時間少。
- **Open**：食譜站與 LINE 貼圖是否共用 bloss0m 品牌流量、導流策略未定。

## 轉職脈絡（對話，非站點本體）

- 擁有者：國泰金控 AI 架構師；公開站 bloss0m.com 主打 Agentic AI；目標職類含 AI agent 相關。
- 內容農場對 Agent 轉職的敘事建議：以 **agentic 內容管線 + 可量測 SEO 指標** 呈現，而非僅「寫了很多食譜」。
