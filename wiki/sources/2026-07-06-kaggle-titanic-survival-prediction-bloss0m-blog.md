---
type: Source
title: "Kaggle Titanic 實作總結（bloss0m blog）"
description: "P0 Titanic 收尾：Public LB 0.81578；Step 5 特徵工程突破；repo poirotw66/titanic。"
tags: ["kaggle", "titanic", "ml-intern", "bloss0m"]
timestamp: 2026-07-06T10:00:00Z
status: active
source_count: 1
---

# Kaggle Titanic 實作總結（bloss0m blog）

## Summary

- 擁有者完成 Kaggle **P0 [Titanic](https://www.kaggle.com/competitions/titanic)** 一輪完整 ML 循環，**Public LB 0.81578**，對外以 **Step 5**（815 notebook FE + CatBoost）為主提交。（確定）[bloss0m blog](https://www.bloss0m.com/blog/37-kaggle-titanic-survival-prediction/)
- 程式可重現：[github.com/poirotw66/titanic](https://github.com/poirotw66/titanic)；`train.py` 單一入口，`features_kaggle815.py` / `features_geeky837b.py` 模組化。（確定）同上
- 核心教訓：**特徵配方 > 換模型／調參**；Optuna 使 CV 0.847 但 LB 跌至 0.794。（確定）同上
- 對齊 [ml-intern-參賽方法](/entities/ml-intern-參賽方法.md)：一步一提交、Pipeline 防洩漏、submission log 思維。（推測）同上

## Key Concepts

- [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md) — P0 Titanic **已收尾**，下一場 P1 House Prices
- [每日技術前沿-blog](/concepts/每日技術前沿-blog.md) — 2026-07-06 實作復盤文

## Entities

- [kaggle](/entities/kaggle.md) — Titanic 競賽
- [ml-intern-參賽方法](/entities/ml-intern-參賽方法.md) — 首個 harness 實作
- [bloss0m-com](/entities/bloss0m-com.md) — 文章與 Lab 專案頁發佈

## Notable Claims

| 主張 | 標記 |
|------|------|
| 性別 baseline 約 0.765；LB 1.0 多為查表作弊 | （確定）blog |
| Step 5：CV 0.824、LB **0.81578** | （確定）blog |
| Step 6 Optuna：CV 0.847、LB 0.794 | （確定）blog |
| Step 7b 嚴格 reproduce：CV 0.836、LB 0.81578 | （確定）blog |
| blend 兩路 97.6% 硬標籤一致，public LB 仍 0.81578 | （確定）blog |

## Limitations / Gaps

- Private LB 未在文章中公布。（未知）
- P1 House Prices 尚未開始。（確定）wiki 路徑規劃

## Relationships

- related_to: [kaggle-經典賽與學習路徑](/queries/kaggle-經典賽與學習路徑.md)
- related_to: [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)

# Citations

[1] [Kaggle Titanic：從 0.74 到 0.816，特徵工程比調參重要](https://www.bloss0m.com/blog/37-kaggle-titanic-survival-prediction/) — 外部（bloss0m blog）
[2] `raw/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md`（immutable archive）
[3] [github.com/poirotw66/titanic](https://github.com/poirotw66/titanic) — 外部
