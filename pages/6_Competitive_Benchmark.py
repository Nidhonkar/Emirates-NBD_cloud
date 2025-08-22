
import streamlit as st
import plotly.express as px
from components.utils import load_csv

st.title("Competitive Benchmarking")
df = load_csv("data/competitive_scores.csv")
melt = df.melt(id_vars=["Bank"], var_name="Metric", value_name="Score")
fig = px.line_polar(melt, r="Score", theta="Metric", color="Bank", line_close=True, range_r=[0,5])
st.plotly_chart(fig, use_container_width=True)
