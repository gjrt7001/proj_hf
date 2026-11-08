"""

🤗 Hugging Face 開源模型生態與下載數據趨勢研究

專題背景與動機
Hugging Face網站介紹、運作模式、模型生態與下載數據趨勢研究的目的與重要性。

(這裡放你的首頁介紹文字與研究目的)


"""

import streamlit as st

def render_home():
    st.title("🤗 Hugging Face 開源模型生態與下載數據趨勢研究")
    
    # 1. 專題動機
    st.subheader("📌 專題背景與動機")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🌐 全球硬體通膨")
        st.success(
            "生成式 AI 帶動科技巨頭競逐 AI 基礎建設與高階運算晶片，"
            "也可能排擠消費級市場的記憶體與製程產能，推升一般使用者的硬體成本。"
        )
    with col2:
        st.markdown("### 💻 地端開源模型需求")
        st.success(
            "隨著 LLM 與生成式 AI 普及，開源社群提供更多可在本機部署的模型。"
            "使用者也開始重視資訊隱私、場景適應力，以及減少對雲端訂閱的依賴。"
        )
    with col3:
        st.markdown("### 📊 模型評估痛點")
        st.success(
            "Hugging Face 模型數量快速增加，但部分模型可能由自動化流程批次發布，"
            "下載量或流量未必代表真實使用者回饋，造成資訊過載與指標失真。"
        )
    st.warning(
        "**研究目的**：在硬體成本提高與開源模型快速增加的背景下，建立有效的"
        "資料評估方式，辨識真正具社群應用價值的熱門模型，並探討一般使用者"
        "對地端模型的需求與使用行為。"
    )
    
    # 2. 研究核心問題
    st.subheader("🎯 本研究旨在回答以下核心問題：")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📈 趨勢指標")
        st.info("哪些 AI 任務（如 Text-Gen, Text-to-Image）在 2026 年最具備爆發性成長？")
    with col2:
        st.markdown("### 🏢 生態分佈")
        st.info("個人開發者與大型企業組織（如 Google, Meta）在模型釋出上的行為有何不同？")
    with col3:
        st.markdown("### 📊 關聯分析")
        st.info("模型的下載量、按讚數與其參數大小（Model Size）之間是否存在顯著關聯？")

    st.markdown("---")

    # 3. 資料來源與系統架構
    st.subheader("🛠️ 資料來源與研究方法")
    st.markdown("""
    * **數據來源**：透過 Hugging Face 官方 API 觀測與抓取 2026 年 2 月至 9 月之模型動態數據。
    * **數據規模**：包含 2300 個模型取前 20 大熱門模型、數十種 AI 任務分類，累積超過 **21萬筆** 數據。
    * **專題架構**：kaggle抓取  /  Hugging Face API 資料抓取  /  SQL 資料清洗  /  Power BI 趨勢洞察  /  Streamlit 專題介紹。
    """)

    st.markdown("---")

    # 4. 快速導覽（引導評審/使用者去點選 Sidebar）
    st.subheader("🧭 網頁操作導覽")
    st.info("""
    請使用左側的**側邊欄（Sidebar）**切換不同的數據維度：
    1. **熱門模型關係**：觀看個人與組織的佔比，以及 Top 20 模型的下載排行榜。
    2. **任務關係-下載**：從下載量角度看哪種 AI 任務（例如語音、影像、文本）最熱門。
    3. **任務關係-按讚**：從社群口碑（Likes）角度解讀開發者最青睞哪些技術。
    """)