<!-- archived_from: 2026 AI CUP Baseline method基於時序資料之桌球戰術與結果預測競賽.pdf | archived_at: 2026-05-15 -->
<!-- binary copy: raw/sources/2026-ai-cup-桌球戰術-baseline-method.pdf -->

# AI CUP Baseline method（文字摘錄）

## 任務預測說明

1. 下一球（第 n 拍）球種預測 (actionId)：預測對手在下一次回擊時會使用的球種（例如：殺球、切球、挑球等）。
2. 下一球（第 n 拍）落點位置預測 (pointId)：預測下一球會落在球場上的哪個具體位置。
3. 此回合勝負預測：根據此回合（Rally）已進行的擊球序列，預測最終此 Rally 的發球者是否得分。

## 資料集欄位（摘錄）

- rally_uid, match, numberGame, rally_id, strikeNumber, sex
- gamePlayerId, gamePlayerOtherId, scoreSelf, scoreOther
- handId, strengthId, spinId, positionId, strikeId
- actionId（預測目標 1）, pointId（預測目標 2；左右手持拍會影響落點編碼）, serverGetPoint（預測目標 3）

## Baseline 方法

- 前處理：從 train.csv 選特徵；對齊最長序列，尾部以 0 padding。
- 模型：簡單 LSTM，對 action、point_id、回合勝負進行多頭分類。
- Loss：Action / Landing Point → CrossEntropy；Rally Winner → BCEwithLogitsLoss。
- 繳交：在對應 feature 填入預測；以最後一次上傳為最終成績。
