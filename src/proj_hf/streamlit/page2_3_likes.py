import streamlit as st
import plotly.express as px
import pandas as pd
from proj_hf.get_root import get_root

root = get_root()

def render_likes():
    st.title("🤗 按讚數據趨勢研究")
    
    # 頂部核心結論提示框
    st.info(
        "💡 **按讚趨勢核心洞察（社群真實風向）：**\n\n"
        "1. **多模態與視覺生成大爆發**：`text-generation`（文本生成，35.49%）雖為基本盤，但 `text-to-image`（26.85%）與 `image-text-to-text`（21.47%）兩大視覺相關任務加總**斬獲近半數（約 48%）的按讚量**。這證實開源社群對視覺生成與多模態技術的開發需求極其強烈。\n"
        "2. **東亞開源雙雄與 Llama 統治力**：熱門按讚榜前段班由 **Qwen（千問）** 與 **DeepSeek** 強勢佔據，印證具備強大雙語與程式碼能力的模型在社群極受歡迎；而 Meta 的 **Llama 3** 系列穩居前列，維持其開源 LLM 統治級基座的地位。"
    )
    
    # 數據快報卡片
    st.subheader("📊 社群真實技術風向標")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="總收獲讚數", value="154.88 千次", delta="社群真實熱度")
    with col2:
        st.metric(label="視覺與多模態讚數佔比", value="48.32%", delta="熱門核心領域")
    with col3:
        st.metric(label="中大型模型按讚主流", value="> 4.1B", delta="分佈較為均勻")

    st.markdown("---")
    
    # 圖表呈現區
    st.subheader("👍 按讚數據趨勢圖")
    try:
        # 載入 Power BI 導出的圖表
        st.image(
            f"{root}/static/images/2_3_likes.png", 
            caption="Hugging Face 數據專題 - 按讚數據趨勢圖", 
            use_container_width=True
        )
    except Exception:
        st.error("⚠️ 無法載入 2_3_likes.png 圖片，請確認圖片路徑與副檔名是否正確。")

    # 看圖說故事詳細解說區
    st.subheader("📑 數據分析與技術風向故事")
    tab1, tab2, tab3 = st.tabs(["1. 任務類型與模型體積", "2. 熱門模型星光榜", "3. 累積按讚時間軸趨勢"])
    
    with tab1:
        st.markdown("""
        **【技術轉移：多模態與視覺生成的黃金交叉】**
        * **任務類型的讚數分佈（左上圓環圖）**：
          * `text-generation` 以 **35.49%** 穩居第一，代表文本大模型仍是剛需。
          * 然而，`text-to-image`（**26.85%**）與 `image-text-to-text`（**21.47%**）緊追其後。這說明社群的興趣正從單純的「聊天機器人」快速轉向「能看圖、能繪圖」的多模態與視覺生成技術。
        * **模型體積（左下圓餅圖）**：
          * 與下載量九成以上集中在 <1B 小模型截然不同，按讚數在各個模型體積（ 1.1B ～ 4B , 4.1B ～ 6B , 35B以上等）的分佈**非常均勻且偏向中大型模型**。
          * **故事結論**：**下載量反映的是企業的流水線日常自動化，而按讚數才真正反映了技術人員對新技術、中大型參數明星模型的狂熱與關注度。**
        """)
        
    with tab2:
        st.markdown("""
        **【群雄割據：誰是開源社群的流量密碼？】**
        * **前 20 名熱門模型（右上長條圖）**：
          * **Qwen 與 DeepSeek 佔領龍頭**：前幾名被 `Qwen/Qwen...` 以及 `deepseek-ai/DeepSeek-R1`（此處可依圖表實際標籤微調）等強勢霸榜。這代表亞洲團隊開發的模型在性能、中英雙語適應性與推理高性價比上，獲得了全球開源社群極高的肯定。
          * **視覺生力軍 FLUX**：Black Forest Labs 的 `black-forest-labs/FLUX.1-dev` 衝上第二名，穩坐 Text-to-Image 領域的新寵兒，印證了社群對高畫質開源圖像生成模型的熱愛。
          * **Meta Llama 基座**：`meta-llama/Llama-3.1-8B-Instruct` 等系列依然名列前茅，展現開源老大哥無可撼動的生態系底氣。
        """)
        
    with tab3:
        st.markdown("""
        **【階梯式暴增：時間軸上的技術突破點】**
        * **任務總按讚數加總趨勢（右下折線圖）**：
          * 觀察歷史走勢，整體讚數並不是平滑上升，而是呈現**非常顯著的「階梯式爆發」**。
          * **技術潮汐線**：
            * **5 月至 6 月**：`text-generation` 有一波明顯的拉升。
            * **8 月至 9 月**：`image-text-to-text`（黃色線）突然從 0 基礎線直接**拔地而起、垂直暴增**！這對應了第三季多模態小模型（如 Qwen2-VL、Llama-3.2-Vision）或是新一代視覺模型的集中發布。
          * **故事結論**：每一次折線圖的陡峭轉折，背後都代表開源界丟出了一顆技術核彈，吸引全球開發者瘋狂湧入點讚。這種數據趨勢成功捕捉到了技術演進的黃金交接棒。
        """)
