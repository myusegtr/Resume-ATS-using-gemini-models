# chat_history

from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# to load model & get responses
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

# initializing the streamlit main page

st.set_page_config(page_title="Chat history demo")

st.header("Building a simple gemini application")

input=st.text_input("Input: ",key="input")


submit=st.button("May i help u with ur question!")

if submit:
    
    response=get_gemini_response(input)
    st.subheader("Here's your response")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)