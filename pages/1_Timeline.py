
import streamlit as st, plotly.express as px
from components.utils import load_csv, source_note

st.header("Digital Transformation Timeline — Emirates NBD")
df = load_csv("data/timeline.csv")
fig = px.scatter(df, x="Year", y=[1]*len(df), text="Milestone", size=[12]*len(df))
fig.update_traces(textposition="top center")
fig.update_yaxes(visible=False, showticklabels=False)
fig.update_layout(height=540, xaxis=dict(dtick=1))
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)
source_note("Red Hat (2019); FinTech Futures (2018, 2020); McKinsey (2022); PwC & ENBD (2024)")
