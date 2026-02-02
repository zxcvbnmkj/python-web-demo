import streamlit as st
import random
import pandas as pd

st.title("模仿 jupyter")

with st.echo():
    def greet():
        return "Hello !!"
    greeting = greet()
    st.success(greeting)

st.divider()

with st.echo(code_location="below"):
    data = [random.random() for _ in range(10)]
    df = pd.DataFrame(data, columns=["Value"])
    st.write("设置 code_location='below'，可以让代码显示在结果的下面")
    st.dataframe(df.head(3))

st.divider()

with st.echo():
    st.write("通过组件快速得到 df 对应的折线图")
    st.line_chart(df)
