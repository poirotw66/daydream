---
type: Concept
title: "桌球 Baseline LSTM 多任務"
description: "AI CUP 桌球官方 Baseline：LSTM 多頭分類 action、落點與回合勝負，含 padding 與差異化 loss。"
tags: ["baseline", "lstm", "桌球"]
timestamp: 2026-06-25T12:00:00Z
status: active
source_count: 1
---
# 桌球 Baseline LSTM 多任務

## Summary

AI CUP 桌球賽官方 Baseline：以**簡單 LSTM** 對 [桌球戰術時序預測](/concepts/桌球戰術時序預測.md) 的三項目標做多頭分類，並搭配 padding 前處理與差異化 loss。（確定）[2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)

## Key Points

- **前處理**：`train.csv` 選欄；序列長度對齊最長樣本，不足處尾部補 0。（確定）[2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)
- **輸出頭**：Action Logits、Landing Point Logits、Rally winner Logit。（確定）[2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)
- **Loss**：action／落點 → CrossEntropy；回合勝負 → BCEwithLogitsLoss。（確定）[2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)

## Evidence

- [2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)

## Open Questions

- 三 loss 是否加權合併、權重為何？（未知）
- 推論時是否僅預測「下一拍」或整段 rollout？（未知）

## Relationships

- implements: [桌球戰術時序預測](/concepts/桌球戰術時序預測.md)
- grounded_in: [2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md)

# Citations

[1] [2026-ai-cup-桌球戰術-baseline](/sources/2026-ai-cup-桌球戰術-baseline.md) — `raw/sources/2026-ai-cup-桌球戰術-baseline-method.pdf`, `raw/sources/2026-ai-cup-桌球戰術-baseline-文稿.md`
