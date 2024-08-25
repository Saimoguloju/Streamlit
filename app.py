import streamlit as st
import time as t

st.image("Image.jpg")
# title -  IT is used to add the title of the app
st.title("Welcome to Moguloju Sai's GitHub")

# Header 
st.header("Data Science")
# Sub header
st.subheader("Machine Learning")
# Information
st.info("User information")
# Warning message
st.warning("warning")
# Error
st.error("error")
# Success
st.success("success")
# Write
st.write("Moguloju Sai")
st.write(range(50))
# Markdone
st.markdown("# Demo")
st.markdown("## Demo")
st.markdown(":moon:")
# text
st.text("demo ohoo")
# TO write the caption
st.caption("caption is here")
# Maths 
st.latex(r''' a+b x^2+c''')
# Widget
# Check box
st.checkbox("Login")
# button
st.button("Click")
# Radio
st.radio("Pick your gender",['Male','Female','other'])
# select box
st.selectbox("pick your course",['ml','pp','ii'])
# multi select
st.multiselect("Chose the dept",['csd','cse','eee'])
# selectslider
st.select_slider("rating",['g','e','b'])
#slider
st.slider("enter utr number",0,50)
# number_input
st.number_input("pick a number",0,100)
# text input
st.text_input("Enter yout email")
# Date
st.date_input("Opening date")
# time input
st.time_input("time")
# text area
st.text_area("welcome to my channel")
# upload
st.file_uploader("upload")
# color
st.color_picker("color")
# 
st.progress(90)
# spinner
with st.spinner("judt wait"):
    t.sleep(1)
    
# balloons
st.balloons()


# siderbar
st.sidebar.title("weloome to my cjkjsfndj")
st.sidebar.text_input("mail")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio('dafegstfgh',['pp','oo'])

# data visual
import pandas as pd
import numpy as np
st.title('Bar Chart')
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)

st.title("Line Chart")
st.line_chart(data)
st.area_chart(data)