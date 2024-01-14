
from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## To get response from the model

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
## Initialize the main page of streamlit app

st.set_page_config(page_title="Building a health checker app ")

st.header("Know your health")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Upload image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Calories count")

input_prompt="""
Act as a human body nutrition expert & tell me the calorie count for individual food items given in the image
in the below format:-

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)


