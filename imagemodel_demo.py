# Chat with images


from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# to load model & get responses
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

# initializing the streamlit main page

st.set_page_config(page_title="Using Text & images both")

st.header("Building a simple Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("upload an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("explain the uploaded image")

## to procedd if button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("Here's your response")
    st.write(response)