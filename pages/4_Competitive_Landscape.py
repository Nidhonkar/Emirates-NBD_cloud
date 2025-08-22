
import streamlit as st, plotly.express as px
from components.utils import load_csv, source_note

st.header("Competitive Landscape — UAE Banks")
df = load_csv("data/competitive.csv")
melt = df.melt(id_vars=["Bank","Source"], var_name="Metric", value_name="Score")
fig = px.line_polar(melt, r="Score", theta="Metric", color="Bank", line_close=True, range_r=[0,5])
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)
source_note("ENBD press; Red Hat; analyst notes (placeholders for FAB, ADCB, Mashreq)")
