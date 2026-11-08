import streamlit as st

def render_about():
    st.title("👨‍💻 關於我 & 專題簡介")
    
    # 使用左右分欄：左邊放個人簡介/頭像，右邊放核心技能
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 這裡可以放你的大頭貼或系統預設頭像
        st.image("https://flaticon.com", width=150)
        st.markdown("### **侯柏于**")
        st.caption("🔍 資料分析師 / AI 應用開發者")
        
        # 社交連結按鈕
        st.markdown("[🔗 GitHub 主頁](https://github.com/gjrt7001)")
        # st.markdown("[💼 LinkedIn 檔案](https://linkedin.com)")
        # st.markdown("[📝 個人技術網誌](https://medium.com)")

    with col2:
        st.markdown("### 👤 個人簡介")
        st.write(
            "你好！我是本專題的創作者。我熱衷於從海量數據中挖掘有趣的洞察，"
            "並利用視覺化與網頁技術將複雜的資料轉化為人人都能看懂的故事。"
            "本專題是我針對 🤗 Hugging Face 生態系進行的開源模型數據分析研究。"
        )
        
        # 核心技能標籤
        st.markdown("### 🛠️ 核心技術棧 (Skills)")
        st.markdown(
            "`Python` · `Streamlit` · `Power BI` · `數據分析` · "
            "`SQL`  · `Hugging Face API`"
        )  #`Plotly`

    st.markdown("---")

    # 專題緣起與痛點（告訴別人你為什麼做這個）
    st.subheader("🎯 專題研究緣起")
    st.markdown("""
    * **研究動機**：隨著開源大模型（LLM、多模態）進入爆發期，Hugging Face 已成為全球 AI 開發者的心臟。然而，面對每天成千上萬的新模型，我們該如何評估哪些模型是「真正熱門」，哪些只是「自動化部署的固定流量」？
    * **解決痛點**：本專題透過**下載量**與**按讚數**的雙軌維度分析，成功為企業與開發者揭開了數據背後的「社群真實風向」與「企業流水線操作」，避免盲目跟風。
    """)

    # 專題架構與亮點（展現你的工作流程）
    st.subheader("🚀 專題亮點與工作流")
    
    tab1, tab2 = st.tabs(["📊 資料處理流程", "💡 專題核心發現"])
    
    with tab1:
        st.markdown("""
        1. **資料搜集 (Data Ingestion)**：使用 Python 定時調用 Hugging Face Web API 抓取模型元數據。
        2. **資料清洗 (ETL)**：利用 Pandas 處理缺失值、解析模型體積（Parameters）與任務標籤（Tags）。
        3. **視覺化探索 (BI)**：透過 Power BI 進行多維度交叉建模與動態趨勢分析。
        4. **網頁部署 (Deployment)**：使用 Streamlit 打造沉浸式的故事化數據儀表板。
        """)
        
    with tab2:
        st.markdown("""
        * **熱門模型研究**：發現 75% 的模型生態由企業組織（Org）壟斷，且熱門下載與按讚並無正相關。
        * **下載數據趨勢**：成功捕捉到 5 月份 Qwen 發布潮與 6 月份 Hugging Face 資安黑天鵝事件的數據異動。
        * **按讚數據趨勢**：印證「按讚數」更能代表技術人員的真實技術風向，並發現多模態視覺生成（Image/Video）正迎來爆發式增長。
        """)

    st.markdown("---")
    st.info("📬 **聯絡我**：如果你對本專題的資料集、分析方法或合作感興趣，歡迎透過上方社交連結或 Email (` gjrt7001@gmail.com `) 與我聯絡！")

