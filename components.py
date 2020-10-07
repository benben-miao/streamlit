import streamlit as st
import io

slide = st.sidebar.slider("Slide", 0, 20, 10, 1)
checkbox = st.sidebar.checkbox("Checkbox",False)
radio = st.sidebar.radio("Radio",["red","blue","green"],0)
download = st.sidebar.date_input("Date")
number = st.sidebar.number_input("Number",min_value=0,max_value=10,value=3,step=1)
text = st.sidebar.text_input("Text",value="Text")
time = st.sidebar.time_input("Time",value=None)
text_area = st.sidebar.text_area("Text Area",value="Text \n Area")
# table = st.sidebar.table("Table")
select = st.sidebar.selectbox("Select",["Iphone","Huawei","Xiaomi"],index=1)
color = st.sidebar.beta_color_picker("Color",value="#FF0000")
upload = st.sidebar.file_uploader("Uploader")

"Hello World"
