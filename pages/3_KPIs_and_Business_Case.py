
import streamlit as st, plotly.express as px
from components.utils import load_csv, source_note

st.header("KPIs & Business Case")
df = load_csv("data/kpis.csv")
st.dataframe(df)
fig = px.treemap(df, path=["Metric"], values="Target", color="Target")
st.plotly_chart(fig, use_container_width=True)
source_note("PwC (2023); Red Hat (2019); Capgemini (2019); FinTech Futures (2020)")
