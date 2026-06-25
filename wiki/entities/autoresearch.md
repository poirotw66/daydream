---
type: Entity
title: "Autoresearch"
description: "Karpathy autoresearch：AI agent 在單 GPU 上自動迭代 LLM 訓練實驗（nanochat 簡化版）。"
tags: ["research", "experiment", "automation", "llm"]
timestamp: 2026-06-25T18:00:00Z
status: active
source_count: 2
---
# Autoresearch

## Summary

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**：讓 AI agent 在**單 GPU**、**固定 5 分鐘**訓練預算下，反覆修改 `train.py`、以 **val_bpb** 評估、保留或丟棄實驗 — 模擬「自主 ML 研究」迴圈。（確定）[GitHub README](https://github.com/karpathy/autoresearch)、[2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md)

與 [ml-intern-參賽方法](/entities/ml-intern-參賽方法.md) 並行：Kaggle 練 **tabular harness**；autoresearch 練 **Agent 驅動實驗編排 + LLM 訓練**。（推測）[kaggle-經典賽與學習路徑](/queries/kaggle-經典賽與學習路徑.md)

## Key Points

| 檔案 | 角色 |
|------|------|
| `prepare.py` | 資料與 tokenizer 準備（**不修改**） |
| `train.py` | 模型／訓練迴圈（**agent 修改**） |
| `program.md` | 給 agent 的指令（人類迭代，類 **skill**） |

- 依賴：**NVIDIA GPU**、Python 3.10+、`uv`。（確定）[README](https://github.com/karpathy/autoresearch)
- 小算力可參考 README 的 fork 指引（如 macOS MLX）與縮小 `DEPTH`、`MAX_SEQ_LEN` 等。（確定）
- `program.md` 被作者描述為 lightweight **skill** — 與 [cursor-superpowers](/entities/cursor-superpowers.md) 精神相近。（推測）

## Evidence

- [2026-06-25-學習與-side-主軸調整](/sources/2026-06-25-學習與-side-主軸調整.md)
- [2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md)

## Open Questions

- 本機是否具備 NVIDIA GPU 跑官方設定？（未知）
- 是否 fork 縮小版做「5min budget」實驗日誌公開到 bloss0m？（未知）

## Relationships

- related_to: [ml-intern-autoresearch-路線](/concepts/ml-intern-autoresearch-路線.md)
- related_to: [ml-intern-參賽方法](/entities/ml-intern-參賽方法.md)
- related_to: [kaggle](/entities/kaggle.md)
- related_to: [cursor-superpowers](/entities/cursor-superpowers.md)
- related_to: [每日技術前沿-blog](/concepts/每日技術前沿-blog.md)
- grounded_in: [2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md)

# Citations

[1] [2026-06-25-kaggle路徑與輸出分工](/sources/2026-06-25-kaggle路徑與輸出分工.md) — `raw/sources/2026-06-25-kaggle路徑與輸出分工.md`
[2] [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — README（外部）
