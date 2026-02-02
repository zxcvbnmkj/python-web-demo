import streamlit as st

with open("streamlit/docs/2026-01.md", "r", encoding="utf-8") as f:
    st.markdown(f.read())