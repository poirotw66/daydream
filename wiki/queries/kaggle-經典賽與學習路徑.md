---
type: Query
title: "Kaggle 經典賽與學習路徑？"
description: "ml-intern harness 入門：Getting Started 賽 → 金融銜接；與 autoresearch 分工"
tags: ["query", "kaggle", "ml-intern"]
timestamp: 2026-07-06T10:00:00Z
status: active
source_count: 3
---

# Kaggle 經典賽與學習路徑？

## 問題

[ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md) 應從哪些 Kaggle 競賽起步？與 [autoresearch](https://github.com/karpathy/autoresearch) 如何分工？

## 答案（2026-06-25 survey）

### P0 進度（2026-07-06 更新）

| 項目 | 狀態 |
|------|------|
| [Titanic](https://www.kaggle.com/competitions/titanic) | **✓ 收尾** — Public LB **0.81578** |
| Repo | [github.com/poirotw66/titanic](https://github.com/poirotw66/titanic) |
| 復盤 | [bloss0m blog](https://www.bloss0m.com/blog/37-kaggle-titanic-survival-prediction/) |
| 主提交 | Step 5（815 notebook FE + CatBoost）；不再追 Optuna CV 極致 |
| 下一場 | **P1 House Prices**（回歸） |

教訓（確定）：特徵工程 > 調參；CV 高 ≠ LB 高；Pipeline 防洩漏；嚴格 reproduce。（確定）[2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md)

### 推薦順序（確定為 wiki 建議路徑；賽事狀態以 Kaggle 為準）

| 階段 | 競賽 | 類型 | 為何適合 ml-intern harness |
|------|------|------|---------------------------|
| **P0 起手** | [Titanic](https://www.kaggle.com/competitions/titanic) | 二分類 tabular | **✓ 完成**（LB 0.81578）；練 baseline → 特徵 → 提交 log → Pipeline |
| **P1** | [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | 回歸 tabular | 補齊回歸、缺失值、高維類別特徵、CV |
| **P2** | [Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer) | 影像 / MNIST | 若要走 CNN／深度學習入門（可選） |
| **P2b** | [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic) | 現代 tabular 分類 | Titanic 進階版、pipeline 思維 |
| **P3 金融銜接** | [IEEE-CIS Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection) | 支付詐欺 tabular | 與 [金融業-ai-agent-side-發想](/concepts/金融業-ai-agent-side-發想.md) 呼應；類別不平衡、時間切分、PR-AUC；**競賽可能已結束但資料與 Notebooks 仍可學** |

### 學習重點（對齊 ml-intern，推測）

1. **先可重現，再追分**：固定 `random_seed`、sklearn `Pipeline`、本地 CV 分數 + 每次 submission 變更紀錄。
2. **一次只改一個變因**：對齊 autoresearch「改一項 → 跑固定時長 → 保留／丟棄」心態。
3. **特徵工程 > 複雜模型**（Titanic／House Prices 階段）；金融賽再引入 LightGBM／CatBoost 與 imbalance 指標。

### 與 autoresearch 分工

| | Kaggle 經典賽 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) |
|---|---------------|-------------------------------------------------------------------|
| **目標** | tabular／入門 ML **harness**、金融特徵直覺 | 單 GPU **LLM 訓練**自動研究（agent 改 `train.py`，固定 5min budget，`val_bpb`） |
| **硬體** | CPU 亦可起步 | **官方要求 NVIDIA GPU**（README 標 H100）；Mac 可參考社群 fork |
| **與本路線** | **先做**（1～4 週建立紀律） | **並行或第二階段**（Agent 編排 + 實驗迴圈敘事） |

autoresearch 核心檔：`prepare.py`（固定）、`train.py`（agent 改）、`program.md`（人類寫的 agent 指令，類 lightweight skill）。（確定）[GitHub README](https://github.com/karpathy/autoresearch)

### 與 blog／side 的橋接（推測）

- **Blog（科技前沿）**：可寫 Kaggle 實驗方法、autoresearch 讀後、論文速讀。
- **Side（金融 Agent）**：IEEE-CIS 洞察可轉成「fraud 特徵 → 風控 agent 工具」發想；**不必**把 Kaggle 分數當求職主敘事。

## 不確定

- 擁有者本機 GPU 型號與是否跑 full autoresearch。（未知）
- P1 House Prices 開跑時程。（未知）

## Relationships

- related_to: [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)
- related_to: [kaggle](/entities/kaggle.md)
- related_to: [autoresearch](/entities/autoresearch.md)

# Citations

[1] [2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md) — `raw/sources/2026-06-25-kaggle路徑與輸出分工.md`
[2] [2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog](/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md) — `raw/sources/2026-07-06-kaggle-titanic-survival-prediction-bloss0m-blog.md`
[3] [Kaggle Competitions](https://www.kaggle.com/competitions) — Getting Started 賽事列表（外部）
[4] [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — README（外部）
