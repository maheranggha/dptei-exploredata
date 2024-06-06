from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import pygwalker as pyg

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Data Explorer",
    layout="wide"
)

st.title("Data Visualization Explorer")

# Import dataset
df = pd.read_csv("Cat_Combined_Target.csv")

pyg_app = StreamlitRenderer(df)

pyg_app.explorer()