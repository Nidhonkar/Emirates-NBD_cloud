
import streamlit as st
import plotly.express as px
from components.utils import load_csv

st.title("ENBD Digital Transformation Timeline")
df = load_csv("data/enbd_timeline.csv")
fig = px.scatter(df, x="Year", y="Type", color="Type", hover_name="Milestone", size=[10]*len(df))
st.plotly_chart(fig, use_container_width=True)
