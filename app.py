from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

# to load model & get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# initializing the streamlit main page
st.set_page_config(page_title="Chat-Demo")

st.header("Building a simple Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("May I help u with ur question!")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)