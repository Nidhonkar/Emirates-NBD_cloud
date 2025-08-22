
import streamlit as st
import plotly.express as px
from components.utils import load_csv

st.title("Cloud Adoption Overview")
df = load_csv("data/cloud_adoption.csv")
fig = px.bar(df, x="Region", y="AdoptionRatePct", text="AdoptionRatePct", color="Region", title="Cloud Adoption (FS)")
fig.update_traces(texttemplate="%{text}%", textposition="outside", showlegend=False)
st.plotly_chart(fig, use_container_width=True)
