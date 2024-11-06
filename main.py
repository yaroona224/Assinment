import numpy as np
import pandas as pd
import streamlit as st

st. title("This is Yara" )
st.write("hello everybody")

data=pd. DataFrame ({
    "C1": ['A','B','C','D','E'],
    "C2" : [100,200,300,400,500]
})

st.write("Below are your Marks:")
st. write(data)

chart_data=pd.DataFrame (
    np. random. rand (20,4),
    columns= ['P','l','R','T']
)
st.line_chart(chart_data)