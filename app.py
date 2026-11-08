"""
streamlit run app.py
"""

import streamlit as st

# 核心：從你的 src 資料夾匯入各分頁的渲染函式
from src.proj_hf.streamlit.home import render_home
from proj_hf.streamlit.page1_1_hugging_face import render_hf
from proj_hf.streamlit.page1_2_source import render_source
from proj_hf.streamlit.page2_1_popular import render_popular
from proj_hf.streamlit.page2_2_download import render_download
from proj_hf.streamlit.page2_3_likes import render_likes
from proj_hf.streamlit.page3_1_about import render_about

st.set_page_config(page_title="HF數據研究專題", layout="wide")

# ==============================================================================
# 1. 定義多頁面物件 (將函式包裝成 st.Page)
# ==============================================================================
# 基本頁面
page_home = st.Page(render_home, title="專題首頁 / 簡介", icon="💡", default=True)
page_hf = st.Page(render_hf, title="介紹Hugging Face網站", icon="🤗")
page_source = st.Page(render_source, title="資料來源與說明", icon="📚")

# 數據分析類別底下的子頁面
page_popular = st.Page(render_popular, title="熱門模型與下載/按讚關係", icon="📊")
page_download = st.Page(render_download, title="AI模型與任務關係-下載", icon="🚩")
page_likes = st.Page(render_likes, title="AI模型與任務關係-按讚", icon="👍")

# 其他頁面
page_aboutme = st.Page(render_about, title="關於我", icon="😉")


# ==============================================================================
# 2. 設定有質感的側邊欄分組導覽 (st.navigation)
# ==============================================================================
# 透過字典結構，Key 就是分類名稱，Value 就是該分類底下的頁面清單
pg = st.navigation({
    "🏠 首頁與簡介": [page_home, page_hf, page_source],
    "📈 數據分析專區": [page_popular, page_download, page_likes],
    "📫聯絡資訊": [page_aboutme]
})


# ==============================================================================
# 3. 渲染全域側邊欄元件與執行頁面
# ==============================================================================
# 你依然可以在側邊欄放標題、Logo 或全域篩選器
st.sidebar.title("🤗 Hugging Face數據分析")
st.sidebar.markdown("---")

# 這裡可以放你的全域篩選器（例如：selected_date = st.sidebar.multiselect(...)）

# 啟動導覽路由（會自動執行當前被點選頁面的 render 函式）
pg.run()
