
import streamlit as st
import plotly.express as px
from components.utils import load_csv, kpi_card, source_note
from components.style import inject_css

st.set_page_config(page_title="Emirates NBD — Digital Transformation", page_icon=":bank:", layout="wide")
inject_css()

col_logo, col_title = st.columns([1,3])
with col_logo:
    st.image("assets/enbd_logo.svg", use_column_width=True)
with col_title:
    st.title("Emirates NBD — Digital Transformation")
    st.subheader("Cloud Computing & Open Banking APIs (UAE Banking Context)")

st.markdown("---")

# KPI cards
c1,c2,c3,c4,c5 = st.columns(5)
with c1: kpi_card("IT TCO (Δ)", "≈ −10%", helptext="PwC (2023)")
with c2: kpi_card("Release Cycle", "≤ 7 days", "from 30d")
with c3: kpi_card("API Volume", "50k+/mo", "+50k")
with c4: kpi_card("SME Onboarding", "≤ 4 hrs", "from 48h")
with c5: kpi_card("NPS (Δ)", "+15 pts", "to ~60")

st.subheader("Cloud Adoption in Financial Services — Global vs Middle East")
df = load_csv("data/cloud_adoption.csv")
fig = px.bar(df, x="Region", y="AdoptionRatePct", text="AdoptionRatePct", color="Region")
fig.update_traces(texttemplate="%{text}%", textposition="outside", showlegend=False)
fig.update_layout(yaxis_title="Adoption (%)", height=420)
st.plotly_chart(fig, use_container_width=True)
source_note("PwC (2023) Global & Middle East FS Cloud Survey")

st.caption("Use sidebar to explore: Timeline, Architecture, KPIs, Competition, Risks")
