---
type: Query
title: "金融業 Agent 有哪些應用場景？"
description: "場景地圖、金融 Agent 設計約束、可公開 side 候選與正職／side 分工"
tags: ["query", "agent", "金融"]
timestamp: 2026-06-25T20:00:00Z
status: active
source_count: 3
---

# 金融業 Agent 有哪些應用場景？

## 問題

[金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md) 應鎖定哪些場景？哪些適合 **side 公開實作**，哪些留給 [現職場內-agent-案子](/concepts/現職場內-agent-案子.md)？

## 答案（2026-06-25 探索）

### 1. 場景地圖（五類）

| 類別 | 典型任務 | Agent 型態 | Side 可公開？ |
|------|----------|------------|---------------|
| **知識／合規** | 法規／內規問答、公開說明書摘要、合規檢核清單 | RAG + citation + 拒答 | **高** — 金管會／央行／SEC 等公開文本 |
| **風控／反詐** | 交易異常調查、AML 案件整理、規則＋模型解釋 | Tool-using copilot、**human-in-the-loop** | **中** — [IEEE-CIS](https://www.kaggle.com/competitions/ieee-fraud-detection) 等公開資料；不做真實攔截 |
| **營運／流程** | 對帳差異歸因、工單分類、客訴路由 | 工作流 Agent + 表單工具 | **低** — 易碰內部流程；side 僅能抽象 demo |
| **投研／資訊** | 財報／法說摘要、產業新聞 synthesis | 多步檢索 + 引用 | **中** — 公開 10-K／新聞；須免責與非投顧聲明 |
| **Agent 基建** | Golden set eval、回歸、tool trace 觀測 | Harness／eval kit | **高** — 與 [#001 Eval Kit](/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md) 合流 |

（推測）場景分類綜合 wiki 既有發想與公開金融 Agent 實務；**未** ingest 單一外部白皮書。

### 2. 金融 Agent 共通設計約束

不論場景，企業／監管語境下反覆出現的 pattern（推測，對齊 [國泰金控-ai-架構師](/entities/國泰金控-ai-架構師.md) 與 [2026-06-03-年底轉職與時間配置](/sources/2026-06-03-年底轉職與時間配置.md)）：

| 約束 | 實作含義 |
|------|----------|
| **Human-in-the-loop** | 高風險動作（拒付、下單、核准）僅建議，不自主執行 |
| **Provenance** | 每則回答附來源片段／tool log，可稽核 |
| **Refusal & escalation** | 不確定、缺資料、涉個資 → 拒答或轉人工 |
| **Tool boundary** | 區分 read-only（查法規）vs write（需二次確認） |
| **Eval regression** | 法規改版、prompt 改動 → golden set 回歸（#001 敘事） |
| **PII / 內規** | Side **不得**用真實客戶資料；合成或公開集 only |

### 3. 正職 vs Side 分工

| | 場內案子 | Side（公開） |
|---|----------|--------------|
| **資料** | 企業真實（受 NDA） | 公開法規、Kaggle、合成 QA |
| **深度** | 上線、合規簽核、規模 | 7 天 MVP、可點驗 repo |
| **敘事** | 面試抽象化方法論 | [bloss0m-com](/entities/bloss0m-com.md) 文章 + GitHub |
| **重疊** | eval／編排 pattern 可「同構不同資料」對外展示 | （推測）[2026-06-25-主線重定義-agent職涯](/sources/2026-06-25-主線重定義-agent職涯.md) |

### 4. Side 候選（已評分，≥16 進池）

沿用 2026-06-03 五維（各 1–5）；「與 bloss0m 差異化」改讀為 **金融場景加分**。（推測）

| ID | 一句話 | 公開資料 | 總分 | 連結 |
|----|--------|----------|------|------|
| **#002** | 台灣**公開法規** Agentic RAG：引用段落 + eval | 金管會等公開網頁／PDF | **21/25** | [詳情](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) |
| **#003** | **詐欺調查 Copilot**：IEEE-CIS 特徵解釋 + 調查備忘錄草稿 | Kaggle IEEE-CIS | **20/25** | [詳情](/projects/ideas/2026-06-25-003-詐欺調查-copilot.md) |
| **#001** | 通用 Eval Kit；可換 **金融 golden set** | 公開 PDF／10-K 摘錄 | **22/25**（既有） | [詳情](/projects/ideas/2026-06-03-001-agentic-rag-eval-kit.md) |

**建議首實作順序**（推測）：

1. **#002** — 最直接呼應「金融 + RAG + 合規敘事」，與轉職、場內案子語言一致。
2. **#001 金融版 golden** — 在 #002 corpus 上掛 `/eval/run`，一週內可併交付。
3. **#003** — 與 [kaggle-經典賽與學習路徑](/queries/kaggle-經典賽與學習路徑.md) P3 並行，偏 tabular＋tool 敘事。

### 5. 不建議優先的 side 方向

- **自主交易／投顧建議 Agent** — 監管與免責複雜；面試風險高。（推測）
- **宣稱取代風控模型** — 與 IEEE-CIS 類 ML 賽事錯位；Agent 應做 **調查輔助**。（推測）
- **需內部 API 的營運 Agent** — 無法公開驗證。（確定）side 公開性規則

### 6. 與其他主線的橋接

- **Blog**：寫 Agent 設計約束、eval 方法、#002／#003 實驗筆記（科技前沿，不必每篇都金融）。
- **Kaggle**：IEEE-CIS 餵 #003 特徵直覺；Titanic 仍先練 harness 紀律。
- **場內**：抽象化「法規 RAG + audit log + 回歸 eval」故事，不寫內部專名。（推測）

## 不確定

- ~~#002 首選 corpus~~ → **已鎖定** [洗錢防制法體系](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md)（確定）[2026-06-25-002-corpus-規劃](/sources/2026-06-25-002-corpus-規劃.md)
- 發想評分是否正式把第五維改為「金融場景相關」。（未知）
- 場內案子是否與 #002 同構場景。（未知）

## Relationships

- related_to: [金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md)
- related_to: [現職場內-agent-案子](/concepts/現職場內-agent-案子.md)
- related_to: [kaggle-經典賽與學習路徑](/queries/kaggle-經典賽與學習路徑.md)

# Citations

[1] [2026-06-25-金融業-agent-應用探索](/sources/2026-06-25-金融業-agent-應用探索.md) — `raw/sources/2026-06-25-金融業-agent-應用探索.md`
[2] [2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md)
[3] [2026-06-03-年底轉職與時間配置](/sources/2026-06-03-年底轉職與時間配置.md)
