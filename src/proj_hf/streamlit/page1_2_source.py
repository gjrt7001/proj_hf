import streamlit as st
from proj_hf.get_root import get_root

root = get_root()

def render_source():
    # ==============================================================================
    # 頂部標題與核心架構說明
    # ==============================================================================
    st.title("📂 資料來源與架構說明")
    st.caption("本專題之原始數據來源、資料庫架構（Medallion Architecture）與開源程式碼說明。")
    st.markdown("---")

    # 使用 Tabs 將「資料來源與架構」和「程式碼開源」分開，畫面更乾淨
    # tab_data, tab_code = st.tabs(["📊 數據來源與架構", "💻 專題開源程式碼"])
    tab_data, tab_code = st.tabs(["📊 數據來源與架構", ""])  # 這邊暫時不做💻 專題開源程式碼

    # ==============================================================================
    # TAB 1: 數據來源與架構
    # ==============================================================================
    with tab_data:
        st.subheader("🌐 原始數據來源")
        
        # 用一個精美的卡片（Container）呈現 Kaggle 來源
        with st.container(border=True):
            col_source_txt, col_source_link = st.columns([3, 1])
            with col_source_txt:
                st.markdown("""
                * **資料集名稱**：Hugging Face Models & Trending Snapshot
                * **時間區間**：`2026-02-24` ~ `2026-09-23`
                * **核心內容**：涵蓋 Hugging Face 上數十萬個 AI 模型的下載量、按讚數、所屬任務（Tasks）及架構元數據。
                """)
            with col_source_link:
                st.write("") # 調整垂直對齊
                st.link_button("🔗 前往 Kaggle 觀看原始資料", "https://www.kaggle.com/datasets/zoupet/hugging-face-models-trending?select=hf_models_snapshot.csv", type="primary")

        st.markdown("---")

        # 介紹獎牌架構（Medallion Architecture），讓專題更有專業感
        st.subheader("🏆 資料倉儲：三層架構（Medallion Architecture）")
        st.markdown("本專題採用標準資料工程的現代化三層架構進行數據處理，確保資料從原始狀態到分析視覺化的準確性：")

        col_bronze, col_silver, col_gold = st.columns(3)
        
        with col_bronze:
            st.markdown("### 🥉 銅牌層 (Bronze)")
            st.info("**原始數據落地**\n\n直接儲存自 Kaggle 下載的原始 `hf_models_snapshot.csv` 檔案，不做任何修改，保留最完整的歷史痕跡。")
            
        with col_silver:
            st.markdown("### 🥈 銀牌層 (Silver)")
            st.success("**清洗與關聯化**\n\n透過網路爬蟲補齊 Hugging Face 官方 API 的模型元數據。進行去重、空值處理、拆分表格並生成**主鍵（PK）**，建置結構化關聯式資料庫。")
            
        with col_gold:
            st.markdown("### 🥇 金牌層 (Gold)")
            st.warning("**計算與預聚合**\n\n針對業務邏輯（如各任務總下載量、按讚趨勢等）進行高性能的**預先聚合與計算**，此層資料可直接供給 Streamlit 儀表板進行秒級渲染。")

        st.markdown("---")

        # 實體關係圖 (ER Model)
        st.subheader("📐 資料庫實體關係圖 (ER Diagram)")
        st.markdown("以下為銀牌層與金牌層整理後的關聯式資料庫架構圖：")
        try:
            st.image(f"{root}/static/images/ERmodel.png", caption="Hugging Face 數據專題 - ER 模型架構圖", use_container_width=True)
        except Exception:
            st.error("⚠️ 無法載入 ERmodel.png，請確認圖片路徑是否正確。")




    # ==============================================================================
    # TAB 2: 專題開源程式碼，這段些不要
    # ==============================================================================

    with tab_code:
        st.subheader("🛠️ 技術棧與專題架構")
        
        # 顯示技術標籤（Badges），增加科技感
        st.markdown("""
        <div style="margin-bottom: 20px;">
            <img src="https://shields.io" />
            <img src="https://shields.io" />
            <img src="https://shields.io" />
            <img src="https://shields.io" />
        </div>
        """, unsafe_allow_html=True)

        st.markdown("本專題的完整程式碼開源於 GitHub，主要由以下三大核心模組構成：")

        # 使用 Expander（可展開區塊）讓使用者點擊查看各模組細節
        with st.expander("🕵️ 1. 資料爬取與清洗模組 (Data Pipeline)", expanded=True):
            st.markdown("""
            * **技術細節**：使用 `requests` 與 `BeautifulSoup` 調用 Hugging Face 官方 API 與網頁解析，補足模型更詳細的元數據。
            * **資料處理**：利用 `Pandas` 處理數十萬筆模型數據的缺失值，並依照資料庫正規化原則進行拆表，產出銀牌層 CSV。
            """)

        with st.expander("📈 2. 數據分析與工程模組 (Data Analysis & Analytics)", expanded=False):
            st.markdown("""
            * **分析特點**：使用 `Pandas` 進行分組聚合（Groupby、Pivot），計算各個 AI 任務（如 NLP、CV、Audio）的下載量與按讚數相關係數。
            * **圖表生成**：藉由 `Matplotlib` 與 `Seaborn` 繪製多維度的熱力圖（Heatmap）與趨勢散點圖，並預聚合成金牌層。
            """)

        with st.expander("🖥️ 3. 互動式網頁儀表板 (Streamlit Dashboard)", expanded=False):
            st.markdown("""
            * **介面設計**：使用現代化的 `st.navigation` 側邊欄分類架構，將多個分析面向整合於單一 Web 應用中。
            * **互動體驗**：提供動態篩選、可視化圖表即時縮放，讓非技術背景的使用者也能秒級洞察 Hugging Face 上的模型生態趨勢。
            """)

        st.markdown("---")
        
        # GitHub 傳送門卡片
        st.subheader("🐙 GitHub 程式碼倉庫")
        with st.container(border=True):
            col_git_logo, col_git_action = st.columns([3, 1])
            with col_git_logo:
                st.markdown("""
                ### **HF-Models-Trend-Analysis**
                歡迎點擊右側按鈕前往 GitHub Repository 查看完整原始碼、專案資料夾結構與部署說明。如果這個專題對你有幫助，歡迎給予 **Star** 鼓勵！
                """)
            with col_git_action:
                st.write("") # 調整垂直對齊
                st.link_button("⭐ 前往 GitHub 倉庫", "https://github.com", type="secondary", icon="🐙")

