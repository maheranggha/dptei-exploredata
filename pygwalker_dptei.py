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

with st.expander("Description:", expanded=True):
    st.markdown("This page is providing you Data Visualization tools of with the DPTEI dataset. Here you can drag and drop some features to build some charts. Please, don't refresh the page before you export the chart! Otherwise you will lose your work.")

# Import dataset
df = pd.read_csv("Cat_Combined_Target.csv")

pyg_app = StreamlitRenderer(df)

pyg_app.explorer()