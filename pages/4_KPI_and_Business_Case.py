
import streamlit as st
import plotly.express as px
from components.utils import load_csv

st.title("KPI Tree & Business Case")
df = load_csv("data/kpi_targets.csv")
st.dataframe(df)
fig = px.treemap(df, path=["Initiative","Metric"], values="Target", title="Targets (Illustrative)")
st.plotly_chart(fig, use_container_width=True)
