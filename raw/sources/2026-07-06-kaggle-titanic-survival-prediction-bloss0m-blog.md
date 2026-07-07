# 歸檔：Kaggle Titanic 生存預測實作總結（bloss0m blog）

**歸檔日**：2026-07-06  
**來源類型**：擁有者部落格文章（bloss0m.com）  
**URL**：https://www.bloss0m.com/blog/37-kaggle-titanic-survival-prediction/  
**程式碼**：https://github.com/poirotw66/titanic

---

## 原文摘要（擁有者撰寫）

Kaggle [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic) 為經典入門 tabular 二元分類（訓練 891、測試 418；指標 Accuracy）。

### 最終成果

- **Public LB：0.81578**（對外展示以 Step 5 為主）
- 生產提交選 **Step 5**（815 notebook 特徵配方 + CatBoost）；不再追 Optuna CV 極致
- 預設 CLI：`python train.py`（blend）；`--step 5` / `--step 7b` 可重現單模

### 演進表（文章記載）

| Step | 變更 | CV (5-fold) | Public LB | 備註 |
|------|------|-------------|-----------|------|
| 1–2 | 基礎特徵 / OneHot RF | ~0.83 | 0.74–0.75 | 特徵不足 |
| 3–4 | CatBoost / soft voting | ~0.83 | 0.77–0.78 | 換模型 FE 未跟上 |
| **5** | **815 notebook FE + CatBoost** | 0.824 | **0.81578** | 突破 (+3% LB) |
| 6 | Step 5 + Optuna | 0.847 | 0.794 | CV↑ LB↓ |
| 7 | Geeky target encoding（鬆散移植） | 0.763 | 0.734 | 移植不完整 |
| 7b | Geeky 嚴格 ipynb + RF | 0.836 | **0.81578** | scaler/encoder 分開 fit |
| blend | (p₅ + p₇b) / 2 | 0.833 | **0.81578** | public 與單模平手 |

### 五個教訓（文章）

1. 特徵工程 > 調參
2. CV 高 ≠ LB 高（891 vs 418 脫鉤）
3. Pipeline 防洩漏
4. 嚴格 reproduce（Step 7 vs 7b 差 ~7% CV）
5. 知道何時停（0.81578 在合法解法上緣）

### 與個人主線

- 對齊 ml-intern harness：一步一提交、模組化 `features_*.py`、單一 `train.py` 入口
- bloss0m blog 輸出（2026-07-06）
- 下一階段路徑（wiki 脈絡）：P1 House Prices → P3 IEEE-CIS
