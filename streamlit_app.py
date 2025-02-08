import streamlit as st

# Page config
st.set_page_config(
    page_title="Yumelit",
    page_icon="💡",
    layout="wide"
)

# Multi pages
pages = {
    "Top": [
        st.Page("page_00_top.py", title="Yumelit", icon="💡"),
    ],
    "100 Apps": [
        st.Page("page_01_first_app.py", title="First App", icon="1️⃣"),
    ],
}

pg = st.navigation(pages)
pg.run()
