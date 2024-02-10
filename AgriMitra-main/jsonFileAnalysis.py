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

st.set_page_config(page_title="Crop Monitoring App")

st.header("Crop Monitoring APP")
crop_name = st.text_input("Enter Crop Name: ", key="input")
data = st.text_input("Enter Data: ", key="input1")

submit = st.button("Analyse Data")

input_prompt = """
    Act as a Senior Farmer and Enviourmental Scientist. I am Giving you Some data in json file which is enviourment of a crop is given. you just have to Analyze it and tell whether it is suitable or not for a Particular crop. Use Simple Language and Give result in bullet points and tabular form. The crop is

"""
input = input_prompt + crop_name
## If submit button is clicked

if submit:
    response = get_gemini_repsonse(input_prompt, input)
    st.subheader("The Response is")
    st.write(response)

