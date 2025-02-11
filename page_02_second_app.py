import streamlit as st
from utils.data_handler import load_data

st.title("2️⃣ Second App")

# Load existing data
data = load_data()
who = data.get("who", "")
why = data.get("why", "")
what = data.get("what", "")

st.json(data)
