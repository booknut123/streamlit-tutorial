import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Header - Write")

st.write("Hello *World* :sunglasses:")

arr = np.random.rand(200,3)
df = pd.DataFrame(
    arr,
    columns=["a","b","c"]
)
st.write(df)
    
c = alt.Chart(df).mark_circle().encode(
    x="a", y="b", size = "c", color = "c",
).properties(title="Hello")
st.write(c)