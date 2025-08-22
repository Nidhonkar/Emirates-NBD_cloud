
import streamlit as st
from components.utils import load_csv, source_note

st.header("Risk & Mitigation Matrix")
df = load_csv("data/risks.csv")
st.dataframe(df)
source_note("PwC (2024); PwC (2023); Red Hat (2019); McKinsey (2022); Fintechnews ME (2023)")
