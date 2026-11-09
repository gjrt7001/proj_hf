# 🤗 Hugging Face 數據研究專題

[![Streamlit App](https://streamlit.io)](https://streamlit.app)

本專題透過對 **Hugging Face** 平台上的 AI 模型數據進行深入清洗與分析，探討熱門 AI 模型的發展趨勢、任務分類（Pipeline）與社群指標（下載量、按讚數）之間的關聯性。

## 🌐 專題展示網站
* **線上體驗網址**：[https://streamlit.app](https://streamlit.app)

---

## 🚀 核心功能與頁面規劃

### 🏠 首頁與簡介
* **專題首頁 / 簡介**：探討專題起源、研究動機與核心發現。
* **介紹 Hugging Face 網站**：認識這座當代 AI 模型的開源百寶箱。
* **資料來源與說明**：詳細說明大數據集的來源欄位與系統欄位定義。

### 📈 數據分析專區
* **熱門模型與下載/按讚關係**：透過多維度動態圖表，拆解哪些模型是「叫好又叫座」。
* **AI 模型與任務關係 (下載/按讚)**：分析 NLP、CV、Audio 等不同領域（Pipeline Tag）的熱門分佈趨勢。

---

## 🛠️ 技術棧與工具 (Tech Stack)

* **網頁框架**：`Streamlit` (使用全新 `st.navigation` & `st.Page` 路由架構)
* **資料處理**：`Python`、`Pandas`、`NumPy`
* **資料視覺化**：`Plotly` (動態互動式圖表)
* **環境與套件管理**：`uv` (新型、極速的 Python 包管理器)
* **資料庫管理**：`MariaDB` (資料庫建置與數據維護)

---

## 📂 專案目錄結構

```text
proj_hf/
├─ .streamlit/
│  ├─ config.toml       # ⚙️ 啟用靜態資料夾功能
│  └─ secrets.toml       # 🔏 資料庫敏感資訊加密設定
├─ data/
│  └─ origin_csv/        # 📁 大數據來源 (由於檔案體積過大未上傳)
├─ src/
│  └─ proj_hf/
│     ├─ clear/          # 🛀 資料清洗與前處理程式
│     ├─ connect_db/     # 🔗 資料庫連線模組
│     └─ templates.py    # 🎨 網頁全域公共樣板 (頁首、頁尾)
├─ static/
│  └─ images/           # 🖼️ 網頁靜態圖片資源
├─ app.py               # 🏠 專題網頁主程式入口 (網站大門)
├─ pyproject.toml       # 🔧 uv 專案依賴管理設定檔
└─ uv.lock              # 🔒 套件鎖定檔
```

---

## 💻 本地端快速啟動

如果你想在本地環境執行本專案，請確保已安裝 [uv](https://github.com)，並依序執行以下指令：

1. **複製專案：**
   ```bash
   git clone https://github.com/gjrt7001/proj_hf.git
   cd proj_hf
   ```

2. **還原環境並啟動：**
   ```bash
   uv sync
   uv run streamlit run app.py
   ```
