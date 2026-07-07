---
type: Entity
title: "ML-Intern 參賽方法"
description: "可重現 ML 實驗 harness（ml-intern 方法）；每場賽獨立 repo，如 poirotw66/titanic。"
tags: ["方法", "kaggle", "harness", "experiment"]
timestamp: 2026-07-06T10:00:00Z
status: active
source_count: 4
---
# ML-Intern 參賽方法

## Summary

**ML-Intern 方法**原為 AI CUP 2026 參賽取向；自 **2026-06-25** 起納入 [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)，與 [autoresearch](/entities/autoresearch.md) 並行，從 [kaggle](/entities/kaggle.md) **經典競賽**重新啟動。（確定）[2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)

**首個 harness 實作（2026-07-06）**：Kaggle Titanic — Public LB **0.81578**；[github.com/poirotw66/titanic](https://github.com/poirotw66/titanic)；`train.py` + 模組化 `features_*.py`。**這就是 ml-intern**：方法論＋每場賽一個可重現 repo，**不需要**另做 skill 產品層或 subcommand 命名。（確定）擁有者 2026-07；[2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md)

## Key Points

- 核心：baseline、harness、指標記錄、一鍵重跑。（確定）[2026-05-15-ai-cup-參賽筆記](/sources/2026-05-15-ai-cup-參賽筆記.md)
- AI CUP 賽事已結案；Kaggle 取代賽季時間主軸。（確定）[2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)
- Titanic 實證：特徵工程 > 調參；CV 與 LB 可脫鉤。（確定）[2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md)
- eval 思路可與 [#002](/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md) 或 [bloss0m-com](/entities/bloss0m-com.md) 既有實作呼應。（推測）

## Evidence

- [2026-05-15-ai-cup-參賽筆記](/sources/2026-05-15-ai-cup-參賽筆記.md)
- [2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)
- [2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md)

## Open Questions

- 下一場 P1 [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) 何時開跑？（未知）

## Relationships

- related_to: [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)
- related_to: [kaggle](/entities/kaggle.md)
- related_to: [autoresearch](/entities/autoresearch.md)
- related_to: [ai-cup-2026-參賽](/concepts/ai-cup-2026-參賽.md)
- related_to: [年底轉職-agent-準備](/concepts/年底轉職-agent-準備.md)
- grounded_in: [2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)

# Citations

[1] [2026-05-15-ai-cup-參賽筆記](/sources/2026-05-15-ai-cup-參賽筆記.md) — `raw/sources/2026-05-15-ai-cup-參賽筆記.md`
[2] [2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md) — `raw/sources/2026-06-25-學習與-side-主軸調整.md`
[3] [2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md) — `raw/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md`
