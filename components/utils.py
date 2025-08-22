
import pandas as pd
import streamlit as st

@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def kpi_card(label: str, value, delta=None, helptext=None):
    st.metric(label, value, delta=delta, help=helptext)

def source_note(text: str):
    st.markdown(f"<span class='source-badge'>Source: {text}</span>", unsafe_allow_html=True)
