import streamlit as st
import pandas as pd
Name = st.text_input("Enter your Name : ")
Class = st.selectbox("Enter your class name : ", (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
Roll_Number = st.selectbox("Enter your Roll Number  : ", (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
adr = st.text_area("Enter you addres : ")
button = st.button("Done")

if button :
    st.markdown(f"""
    Name : {Name}
    Class : {Class}
    Roll Number : {Roll_Number}
    Addrea : {adr}
""")
dataset = pd.read_csv("python1.csv")
st.dataframe(dataset)
st.title("Welcome to my web site")
st.header("Make a web site using python")
st.subheader("Lets Start!")
st.markdown("""A faster way to build and share data apps.
Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our Community Cloud platform to deploy, manage, and share your app.""")
st.subheader("Installation")
st.markdown("Open a terminal and run:")
st.code("$ pip install streamlit")
st.code("$ streamlit hello")
st.markdown("If this opens our sweet Streamlit Hello app in your browser, you're all set! If not, head over to our docs for specific installs.")
st.markdown("The app features a bunch of examples of what you can do with Streamlit. Jump to the quickstart section to understand how that all works.")



