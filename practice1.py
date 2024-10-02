import numpy as np
import pandas as pd
import streamlit as st

st.title("Hi, Mr. Yogesh Murumkar here!!!")
st.write("This is an example!!")

df=pd.DataFrame({
    "Name":["Yogesh","Sachin","A","B","C"],
    "Marks":[75,85,100,88,60]
})

st.write("Below is the dataframe!!")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,5),columns=['P','Q','R','S','T']
)

st.line_chart(chart_data)