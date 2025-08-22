
import streamlit as st
from components.utils import load_csv, kpi_card
import plotly.express as px

st.set_page_config(page_title="ENBD Cloud & Open Banking Strategy", page_icon=":bank:", layout="wide")

st.title("Emirates NBD — Cloud Computing & Open Banking APIs")
st.caption("Interactive dashboard with placeholder data. Replace with sourced values and cite in your report.")

col1, col2, col3, col4 = st.columns(4)
with col1: kpi_card("Goal: IT TCO", "−10%", "2–3y")
with col2: kpi_card("Release Cycle", "≤ 7 days", "from ~30d")
with col3: kpi_card("API Calls / mo", "50k+", "+50k")
with col4: kpi_card("SME Onboarding", "≤ 4 hrs", "from 48h")

st.markdown("---")

st.subheader("Global vs UAE Cloud Adoption (illustrative)")
df = load_csv("data/cloud_adoption.csv")
fig = px.bar(df, x="Region", y="AdoptionRatePct", text="AdoptionRatePct", title="Cloud Adoption in Financial Services")
fig.update_traces(texttemplate="%{text}%", textposition="outside")
fig.update_layout(yaxis_title="Adoption (%)", xaxis_title="Region", height=450)
st.plotly_chart(fig, use_container_width=True)
