---
title: "2026 AI CUP 桌球戰術 Baseline"
type: source
status: active
updated: "2026-05-15"
source_count: 1
tags: ["ai-cup", "桌球", "baseline"]
---

# 2026 AI CUP 桌球戰術 Baseline

歸檔：`raw/sources/2026-ai-cup-桌球戰術-baseline-method.pdf`；文字摘錄 `raw/sources/2026-ai-cup-桌球戰術-baseline-文稿.md`

## Summary

- 官方 Baseline 針對**三項預測**：下一拍球種 `actionId`、下一拍落點 `pointId`、該回合發球者是否得分。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- 資料以 rally／拍次為時序單位；`pointId` 會因對手**左右手持拍**而改變落點編碼語意。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- 前處理：自 `train.csv` 取特徵，對齊最長序列並以 0 **padding**。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- 模型：**LSTM** 多頭輸出 action、落點、回合勝負；Loss 為 CE（action／落點）與 BCEwithLogits（勝負）。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- 繳交以最後一次上傳為準。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]

## Key Concepts

- [[concepts/桌球戰術時序預測]] — 任務定義與欄位語意
- [[concepts/桌球-baseline-lstm-多任務]] — 前處理、架構與 loss

## Entities

- [[entities/ai-cup-2026]] — 桌球戰術預測競賽脈絡
- `train.csv` — 訓練資料（欄位見本頁與概念頁）

## Notable Claims

- 回合內交替擊球形成序列，最終預測 `serverGetPoint`（發球者是否得分）。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- 前兩板 `positionId` 分別表示發球方與接發球方站位。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]

## Limitations / Gaps

- PDF 未載明特徵完整清單、驗證指標與 leaderboard 規則細節。（未知）
- 下載／上傳步驟多為簡報截圖，未內嵌 URL。（未知）

## Relationships

- related_to: [[sources/2026-05-15-ai-cup-參賽筆記]]
- related_to: [[concepts/桌球-baseline-lstm-多任務]]
