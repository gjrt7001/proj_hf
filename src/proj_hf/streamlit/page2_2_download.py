import streamlit as st
import plotly.express as px
import pandas as pd
from proj_hf.get_root import get_root

root = get_root()

def render_download():
    st.title("🤗 下載數據趨勢研究")
    
    # 頂部核心結論提示框
    st.info(
        "💡 **下載趨勢核心洞察：**\n\n"
        "1. **自動化流水線驅動**：高下載量模型主要集中在 `sentence-similarity` 與 `fill-mask` 任務，且模型大小皆**小於 1B**。這證實高下載量並非因為模型具有「話題熱度」，而是企業在每日自動化部署與流水線中重複調用所驅動。\n"
        "2. **關鍵事件衝擊波**：5 月中旬因阿里巴巴發布 **Qwen 2.5/3.5** 系列（此處配合圖表年份修正，如為 3.7 可調整）帶動 `image-text-to-text` 任務暴增；而 6 月中旬因 **Hugging Face 爆發嚴重資安漏洞事件**，導致所有任務下載量出現全線暴跌的斷崖式走勢。"
    )
    
    # 數據快報卡片
    st.subheader("📊 關鍵指標與事件")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="主流模型體積佔比 (<1B)", value="95.0%", delta="絕對主力")
    with col2:
        st.metric(label="5月中旬爆發任務", value="Image-Text-to-Text", delta="Qwen 新模效應")
    with col3:
        st.metric(label="6月中旬異常事件", value="全線暴跌", delta="HF 資安網路漏洞", delta_color="inverse")

    st.markdown("---")
    
    # 圖表呈現區
    st.subheader("✨ 下載數據趨勢圖")
    try:
        # 載入 Power BI 導出的圖表
        st.image(
            f"{root}/static/images/2_2_download.png", 
            caption="Hugging Face 數據專題 - 下載數據趨勢圖", 
            use_container_width=True
        )
    except Exception:
        st.error("⚠️ 無法載入 2_2_download.png 圖片，請確認圖片路徑與副檔名是否正確。")

    # 看圖說故事詳細解說區
    st.subheader("📑 數據分析與時間軸故事")
    tab1, tab2, tab3 = st.tabs(["1. 任務類型與模型體積", "2. 5月中旬：Qwen 熱潮", "3. 6月中旬：資安事件衝擊"])
    
    with tab1:
        st.markdown("""
        **【企業級自動化：小模型主導下載流量】**
        * **任務分佈（左上圓環圖）**：從總下載量（突破 5 十億次）中可以看出，主要流量被 `sentence-similarity`（53.81%）與 `fill-mask`（24.4%）兩大基礎任務瓜分。
        * **模型體積（左下圓餅圖）**：進階對比模型大小後發現，高達 **95% 的下載量皆來自小於 1B 的模型**（1.1B - 4B 僅佔 5%）。
        * **故事結論**：這些由企業研發的地端小模型，之所以能霸榜下載量，是因為它們體積小、延遲低，極度適合企業部署在每日的自動化流水線（CI/CD Pipeline）中高頻率調用，這才是驅動巨額下載量的核心本質，而非社群的炒作熱度。
        """)
        
    with tab2:
        st.markdown("""
        **【技術發布效應：5月中旬的突變】**
        * **趨勢觀察（右上折線圖）**：在 5 月中旬，原本平緩的 `image-text-to-text` 任務下載量突然呈現**爆發性激增**。
        * **背後原因**：經由前 10 名地端模型下載量對比，該時段正逢阿里巴巴（Alibaba）重磅發布新一代 **Qwen** 系列模型。其強大的多模態與視覺文本處理能力（Image-to-Text），瞬間引發全球開發者與企業的測試與導入熱潮，在數據上留下了明顯的技術推進軌跡。
        """)
        
    with tab3:
        st.markdown("""
        **【黑天鵝事件：6月中旬的集體斷崖】**
        * **趨勢觀察（右上與右中折線圖）**：在 6 月中旬，不論是哪一種任務類型，還是前 10 名的明星模型，其下載趨勢線同時出現了**驚人的 V 型暴跌（斷崖式下滑）**。
        * **背後原因**：此數據異常完美吻合了當時 **Hugging Face 官方爆發嚴重網路安全漏洞與入侵事件**。當時官方緊急採取防範措施，許多企業與開發者也基於資安考量暫停了自動化拉取模型的腳本、或是平台部分服務短暫中斷，直接導致了全平台的下載量集體腰斬。這是一個非常典型的「外部事件影響數據走向」的研究案例。
        """)
