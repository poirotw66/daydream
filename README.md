# daydream

個人 **OKF v0.1** 知識庫（第二大腦）— 以 Markdown + 來源歸檔維護，供未來的自己、RAG 與 Agent 使用。

**線上閱讀：** [https://poirotw66.github.io/daydream/](https://poirotw66.github.io/daydream/)

---

## 目前在追什麼（2026-07-06）

| 主軸 | 說明 |
|------|------|
| **年底轉職** | AI agent 開發／應用 → [年底轉職 Agent 準備](wiki/concepts/年底轉職-agent-準備.md) |
| **現職場內案子** | 國泰場景內 Agent 案子 → [現職場內 Agent 案子](wiki/concepts/現職場內-agent-案子.md) |
| **每日輸出** | [每日技術前沿 blog](wiki/concepts/每日技術前沿-blog.md) — **科技前沿**（廣義） |
| **Side 實作** | [金融 Agent 發想](wiki/concepts/金融業-ai-agent-side-發想.md) — [應用探索](wiki/queries/金融業-agent-應用探索.md)、[#002 法規 RAG](wiki/projects/ideas/2026-06-25-002-公開法規-agentic-rag.md)、[#003 詐欺 Copilot](wiki/projects/ideas/2026-06-25-003-詐欺調查-copilot.md) |
| **Kaggle** | [經典賽路徑](wiki/queries/kaggle-經典賽與學習路徑.md) — **Titanic P0 ✓**（[LB 0.816](https://www.bloss0m.com/blog/37-kaggle-titanic-survival-prediction/)）→ House Prices |
| **Autoresearch** | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) |
| **學習** | [李宏毅課程論文深讀](wiki/concepts/李宏毅課程論文深讀.md) |

**已暫停：** [內容農場變現軌](wiki/concepts/內容農場變現軌.md)（recipe.bloss0m）、AI CUP 2026 參賽階段。

---

## 從哪裡讀起

| 入口 | 用途 |
|------|------|
| [wiki/index.md](wiki/index.md) | **點子集散中心**（Side #002／#003、主軸、決策捷徑） |
| [wiki/wiki-guide.md](wiki/wiki-guide.md) | 目錄、Ingest、本機預覽 |
| [wiki/queries/平日時間與三線並行.md](wiki/queries/平日時間與三線並行.md) | 平日時間與主線配置 |
| [AGENTS.md](AGENTS.md) | 維護規約 |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Agent 操作提示 |

---

## 目錄結構

```text
raw/sources/     # 不可變歸檔
wiki/            # OKF Knowledge Bundle（concepts、entities、sources…）
docs/            # 版型、OPERATIONS、mkdocs hooks
mkdocs.yml       # GitHub Pages
```

---

## 本機預覽

```bash
pip install -r requirements-docs.txt
NO_MKDOCS_2_WARNING=1 mkdocs serve
# → http://127.0.0.1:8000/daydream/
```

---

## 給維護者／Agent

Ingest 流程見 [AGENTS.md](AGENTS.md)；主張須有來源，不確定標（確定）／（推測）／（未知）。
