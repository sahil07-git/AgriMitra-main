### Disease Detection APP
from dotenv import load_dotenv

load_dotenv()  ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, prompt])
    return response.text


##initialize our streamlit app

st.set_page_config(page_title="Emotion Detection ")

st.header("Emotion Detection Text")
data = st.text_input("Enter Data: ", key="input1")

submit = st.button("Analyse Data")

input_prompt = """
    Act as senior psychologist and analyze following text and tell which emotion is there in this text and also provide why do you think that. The data is 

"""
input = input_prompt 
## If submit button is clicked

if submit:
    response = get_gemini_repsonse(input_prompt, input)
    st.subheader("The Response is")
    st.write(response)

