
import streamlit as st
import plotly.graph_objects as go

st.title("Open Banking Reference Architecture")
labels = ["Customers", "Fintech Apps", "Gov/Reg APIs", "ENBD Channels", "API Gateway (Bawaba)", "Core Banking", "Data & Analytics (Cloud)"]
source = [0,1,2,3,4]
target = [3,4,4,4,5]
value  = [5,5,3,7,10]

fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels, pad=25, thickness=20),
    link=dict(source=source, target=target, value=value)
)])
st.plotly_chart(fig, use_container_width=True)
