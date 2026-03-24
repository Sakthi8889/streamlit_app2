import pandas as pd
import streamlit as st
import numpy as np

st.title("📊 Data Visualization App")

# User input
rows = st.slider("Select number of rows", 5, 100, 20)

data = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=["col1", "col2", "col3"]
)

st.write("### Data Preview")
st.dataframe(data)

st.write("### Charts")
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)