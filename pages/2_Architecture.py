
import streamlit as st, plotly.graph_objects as go
from components.utils import source_note

st.header("Open Banking Reference Architecture — Conceptual")

labels = ["Customers","Fintech Apps","Gov/Reg APIs","ENBD Channels",
          "API Gateway","Core Banking","Data & Analytics (Cloud)"]
source = [0,1,2,3,4]
target = [3,4,4,4,5]
value  = [5,5,3,7,10]

fig = go.Figure(data=[go.Sankey(node=dict(label=labels, pad=25, thickness=20),
                                link=dict(source=source,target=target,value=value))])
fig.update_layout(title_text="Ecosystem Flow", height=520)
st.plotly_chart(fig, use_container_width=True)

st.markdown("APIs enable consented data sharing and integration with fintechs.")
source_note("McKinsey (2022); PwC & ENBD (2024)")
