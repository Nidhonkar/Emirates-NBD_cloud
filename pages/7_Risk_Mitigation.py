
import streamlit as st
from components.utils import load_csv

st.title("Risk vs Mitigation Matrix")
df = load_csv("data/risk_mitigation.csv")
st.dataframe(df, use_container_width=True)
