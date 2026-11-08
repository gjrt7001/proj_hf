import streamlit as st
import plotly.express as px
import pandas as pd
from proj_hf.get_root import get_root

root = get_root()

def render_popular():
    st.title("🤗 熱門模型與下載/按讚關係研究")
    
    # 使用 💡 提示框呈現核心見解，讓使用者一進來就看到結論
    st.info(
        "💡 **研究核心發現：**\n\n"
        "1. **組織壟斷生態**：在所有模型中，企業組織（Org）占了約 75%，個人製作者（User）僅占 25%。不論是熱門下載還是熱門按讚，主要貢獻者皆為企業組織。\n"
        "2. **下載與喜好脫鉤**：經對比熱門下載與熱門按讚模型，兩者**無明顯正相關**。這代表下載量高的模型（多為基礎工具），並不等同於社群討論度或喜愛度高的熱門模型。"
    )
    
    # 建立數據儀表板的小指標 (Metrics)，增強專業感
    st.subheader("📊 數據焦點快報")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="企業組織模型佔比", value="75.19%")
    with col2:
        st.metric(label="個人製作者佔比", value="24.81%")
    with col3:
        st.metric(label="下載/按讚相關性", value="無正相關", delta="低相關度", delta_color="inverse")

    st.markdown("---")
    
    # 圖表呈現區
    st.subheader("📐 熱門模型與下載/按讚關係圖")
    
    # 使用 columns 讓圖表與詳細故事可以並排或上下對齊
    try:
        # 載入 Power BI 導出的圖表
        st.image(
            f"{root}/static/images/2_1_popular.png", 
            caption="Hugging Face 數據專題 - 熱門模型與下載/按讚關係圖", 
            use_container_width=True
        )
    except Exception:
        st.error("⚠️ 無法載入 2_1_popular 圖片，請確認圖片路徑與副檔名是否正確。")

    # 詳細的故事解說區（使用 Tabs 分頁標籤讓排版更乾淨）
    st.subheader("📑 圖表詳細解說與故事")
    tab1, tab2, tab3 = st.tabs(["1. 創作者生態 (圓餅圖)", "2. 下載 vs 按讚 關係", "3. 前 20 名分布研究"])
    
    with tab1:
        st.markdown("""
        **【創作者結構：企業組織主導市場】**
        * 根據左上角的圓餅圖顯示，Hugging Face 上的模型製作者分布為：
          * **企業組織 (Org)**：高達 **75.19%**
          * **個人製作者 (User)**：僅佔 **24.81%**
        * 這反映出大模型開發需要龐大的算力與資源，因此主要市場份額由大型企業、研究機構或開源組織所壟斷。
        """)
        
    with tab2:
        st.markdown("""
        **【下載量與按讚數的非正相關性】**
        * 觀察右側的「20大 下載量 與 20大 按讚數 模型的相關表」折線/柱狀圖：
          * 兩者的趨勢並沒有同步走向，**下載量極高的模型，其按讚數不一定成正比**。
          * **原因解析**：高下載量的模型通常是企業自動化流程、Pipeline 預設載入的基礎權重（例如基礎的 `sentence-transformers` 或 `bert`），屬於「基礎建設型」；而高讚數的模型通常是近期社群熱烈討論、具備話題性或新技術突破的開源模型（例如新一代的 LLM 或是圖像生成模型）。
        """)
        
    with tab3:
        st.markdown("""
        **【極端分布現象】**
        * **前 20 名極端下載**：第一名模型下載量高達 **16 億次**，但到了第二名就驟降至 **4900 萬次**。這呈現出極端嚴重的「長尾效應」與「贏家全拿」現象。少數幾個明星級別的基礎編碼器/轉換器主宰了全球絕大部分的自動化下載流量。
        * **前 20 名按讚分佈**：相對下載量而言，按讚次數的分佈較為平緩，通常由當前最熱門的開源大語言模型（如 Qwen、Llama 等系列變體）以及影像生成模型（如 Black Forest Labs 的 Flux 系列）瓜分，代表社群技術愛好者的真實關注焦點。
        """)
