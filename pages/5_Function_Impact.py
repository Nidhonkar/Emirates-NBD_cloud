
import streamlit as st
from components.utils import load_csv

st.title("Function-Wise Transformation")
df = load_csv("data/function_before_after.csv")
st.dataframe(df, use_container_width=True)
