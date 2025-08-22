
import streamlit as st

def inject_css():
    st.markdown('''
    <style>
      .block-container { padding-top: 1rem; padding-bottom: 1rem; }
      .source-badge {
        display:inline-block; background:#eef2ff; color:#1e3a8a;
        padding:4px 8px; border-radius:6px; font-size:0.78rem; margin-top:6px;
      }
    </style>
    ''', unsafe_allow_html=True)
