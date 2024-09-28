import streamlit as st
import requests
import vertexai
from vertexai.generative_models import GenerativeModel
import google.generativeai as genai
import os


gemini_api_key = st.secrets["gemini"]["api_key"]
genai.configure(api_key=gemini_app_key)


# vertexai.init(project="gen-ai-437006", location="us-central1")
# model = GenerativeModel(
#     "gemini-1.5-flash-002",
#     )

model = genai.GenerativeModel("gemini-1.5-flash")


st.title("ConsumeWise")
st.text(
    "This application has been created as part of the Gen AI Exchange Hackathon by Google"
)
ingredients = st.text_input("Ingredients")
if st.button("Submit"):
    if ingredients:
        st.write("Ingredients given :\n",ingredients)
        response = model.generate_content(
            "Analyse if the following ingredients cause any health issue : " + ingredients 
        )
        st.write(response.text)


