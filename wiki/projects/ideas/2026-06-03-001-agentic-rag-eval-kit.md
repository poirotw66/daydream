---
title: "#001 Agentic RAG Eval Kit"
type: query
status: active
updated: "2026-06-03"
source_count: 1
tags: ["side-project", "idea-001", "eval", "agent"]
---

# #001 Agentic RAG Eval Kit

> 定稿日：2026-06-03｜狀態：**候選池**（每週至多 1 實作；可併入 [[entities/ml-intern-參賽方法]] 或獨立 PR）

## 一句話

在既有 **Agentic RAG** 上新增 **Eval Kit**：固定 golden set（預設 10 題，可縮 5 題）+ 自動評分（faithfulness、latency、tool-call 次數），輸出可重現 JSON 報告。

## 轉職訊號

面試可說：不只會架 LangGraph／MCP，而是用 **可重現 eval** 證明查詢重寫、自我校正等節點是否值得保留——對齊企業 agent 2026 的 **eval + observability** 主戰場。（推測）[[sources/2026-06-03-年底轉職與時間配置]]

## 7 天 MVP

| 日 | 交付 |
|----|------|
| Day 1–2 | 從**公開** PDF 建 mini corpus（可選：[[sources/2026-ai-cup-桌球戰術-baseline]] 文稿或自備公開文件） |
| Day 3–4 | 在 Agentic RAG 加 `/eval/run`（或 CLI 等價）→ JSON 報告（含上述指標） |
| Day 5 | README 對照表：改寫 on/off；除既有 **16.7x** 敘事外至少 **2 個** 新指標 |
| Day 6–7 | [[entities/bloss0m-com]] 短文：〈為什麼 agent 專案要先有 golden set〉 |

**縮 scope 規則**：若本週實作 ≤5h → golden set 改 **5 題** 仍算 MVP 達標。

## 與現有資產

- 程式／架構：延伸 bloss0m **Agentic RAG**（LangGraph、MCP、Cloud Run）。（確定）[[sources/2026-06-03-年底轉職與時間配置]]
- 文章：與「長時間 AI 工程的 Harness 設計」互掛。（推測）
- 可選合流：納入 [[entities/ml-intern-參賽方法]] 的 eval 子命令，而非獨立 repo。（未知）

## 時事錨點

- 企業 agent 落地瓶頸常落在 **評測、觀測、回歸**，而非再疊一層 demo。（推測）[[sources/2026-06-03-年底轉職與時間配置]]

## 評分（2026-06-03 定稿）

| 維度 | 分數 |
|------|------|
| 求職相關 | 5 |
| Agent 深度 | 5 |
| 7 天可交付 | 4 |
| 時事相關 | 4 |
| 與 bloss0m 差異化 | 4 |
| **總計** | **22 / 25** |

門檻 ≥16/25 → **進候選池**。（確定）[[sources/2026-06-03-年底轉職與時間配置]]

## 決策

- **候選池**：待與 ml-intern skill MVP 排程（skill 優先或合併）。（確定）
- **公開性**：僅公開文件 + synthetic QA；**不得**使用國泰內部資料 — **Yes**。（確定）

## Agent 維度

編排 · 工具 · **eval** · 維運（次要：記憶、安全）

## Relationships

- related_to: [[concepts/年底轉職-agent-準備]]
- related_to: [[entities/bloss0m-com]]
- related_to: [[entities/ml-intern-參賽方法]]
- grounded_in: [[sources/2026-06-03-年底轉職與時間配置]]
