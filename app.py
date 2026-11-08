import streamlit as st

# 核心：從你的 src 資料夾匯入各分頁的渲染函式
from src.proj_hf.streamlit.home import render_home
from src.proj_hf.streamlit.page1_hugging_face import render_hf
from src.proj_hf.streamlit.page2_popular import render_popular
from proj_hf.streamlit.page3_download import render_download
from proj_hf.streamlit.page4_likes import render_likes
from proj_hf.streamlit.page5_aboutme import render_aboutme

st.set_page_config(page_title="HF數據研究專題", layout="wide")

# ==============================================================================
# SIDEBAR (側邊欄控制台) - 留在主程式
# ==============================================================================
st.sidebar.title("🤗 Hugging Face數據分析")

page = st.sidebar.radio(
    "請選擇分析主題：",
    [
        "🏠 專題首頁 / 簡介",
        "🤗 介紹Hugging Face網站",
        "📊 1.熱門模型與下載/按讚關係",
        "🚩 2.AI模型與任務關係-下載",
        "👍 3.AI模型與任務關係-按讚",
        "😉 關於我"
    ]
)

st.sidebar.markdown("---")
# 這裡還可以放全域篩選器（如日期、時間、模型大小滑桿）
# selected_date = st.sidebar.multiselect(...)

# ==============================================================================
# 路由邏輯：根據 Sidebar 的選擇，去執行對應資料夾內的功能
# ==============================================================================
if page == "🏠 專題首頁 / 簡介":
    render_home()

elif page == "🤗 介紹Hugging Face網站":
    render_hf() 

elif page == "📊 1.熱門模型與下載/按讚關係":
    render_popular()
    
elif page == "🚩 2.AI模型與任務關係-下載":
    render_download()

elif page == "👍 3.AI模型與任務關係-按讚":
    render_likes()    

elif page == "😉 關於我":  
    render_aboutme()

else:
    st.error("未知的頁面選擇，請聯絡開發者。")