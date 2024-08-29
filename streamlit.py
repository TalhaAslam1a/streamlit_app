import streamlit as st

import pandas as pd
df=pd.read_csv("supermarket_sales.csv")
st.dataframe(df,1000,1000)
#st.table(df)
st.title("My first page")
st.write("Welcome to our project")
st.text("Can we chat together")
st.header("Welcome")
st.subheader("Whats new")
st.markdown("This is markdown")
name=st.text_input("Please enter your name")
if st.button("Click me"):
    st.write("Hello {},welcome to streamlit".format(name))
st.success("You have successfully login to your account")
st.warning("You havae entered the wrong passward")
st.error("Filepath not found")