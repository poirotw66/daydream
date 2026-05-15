---
title: "桌球 Baseline LSTM 多任務"
type: concept
status: active
updated: "2026-05-15"
source_count: 1
tags: ["baseline", "lstm", "桌球"]
---

# 桌球 Baseline LSTM 多任務

## Summary

AI CUP 桌球賽官方 Baseline：以**簡單 LSTM** 對 [[concepts/桌球戰術時序預測]] 的三項目標做多頭分類，並搭配 padding 前處理與差異化 loss。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]

## Key Points

- **前處理**：`train.csv` 選欄；序列長度對齊最長樣本，不足處尾部補 0。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- **輸出頭**：Action Logits、Landing Point Logits、Rally winner Logit。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]
- **Loss**：action／落點 → CrossEntropy；回合勝負 → BCEwithLogitsLoss。（確定）[[sources/2026-ai-cup-桌球戰術-baseline]]

## Evidence

- [[sources/2026-ai-cup-桌球戰術-baseline]]

## Open Questions

- 三 loss 是否加權合併、權重為何？（未知）
- 推論時是否僅預測「下一拍」或整段 rollout？（未知）

## Relationships

- implements: [[concepts/桌球戰術時序預測]]
- grounded_in: [[sources/2026-ai-cup-桌球戰術-baseline]]
